"""Taillierter Oberteil-Grundschnitt.

Quelle: Hofenbitzer Band 1, 3. Auflage 2024

* **S. 184** - Abschnitte 7 bis 11: Brustabnaeher, Armloecher, Schulterabnaeher,
  vorderer Taillenabnaeher, Taillenausfall
* **S. 185** - Abschnitte 12 bis 15: Aufteilung des Taillenausfalls, hintere
  Taillenabnaeher, Hueftausfall, Hueft-Fehlbetrag

Transkripte:
`100_quellen/10_hofenbitzer_b1/2_transkript/band_1_geprueft_v1/s184.md`, `s185.md`

Rechnung in **Millimeter**, Y nach unten.

Was dieses Modul bewusst **nicht** tut
--------------------------------------
* **Kein Hueftausfall, kein Hueftbogen (S.185 Abschnitte 14 und 15).** Dieses
  Modul liefert ein Oberteil, das an der **erhoehten Taillenlinie endet** - fuer
  Kleider mit Taillennaht. Hueftausfall und Hueft-Fehlbetrag betreffen nur
  Schnitte, die ueber die Huefte hinaus reichen.
* **Der Schulterabnaeher bleibt stehen.** S.184 Schritt 33 legt ihn ins Armloch
  zu; die Abbildung 8c auf S.185 zeigt ihn jedoch weiterhin als genaehten
  Abnaeher ("zum Naehen wird er auf ca. 10 cm gekuerzt"). Bis Werner die Stelle
  am Buch klaert, bleibt der Abnaeher stehen - das ist die Variante, die 8c
  zeigt.

Offene Buchstellen, hier markiert statt still entschieden
--------------------------------------------------------
1. **Li26 (S.184 Schritt 26).** Das Buch bestimmt den Brustabnaeher grafisch:
   "Rechts der vorderen Armlinie den maximalen Abstand zur Armlinie anzeichnen
   -> Li26", dann wird vSuP1 "maximal bis zur Li26" gedreht. Welche Linie das
   genau ist, geht aus dem Transkript nicht hervor. Hier wird die **vordere
   Seitenlinie** angenommen - sie ist die aeuszerste Senkrechte rechts der
   vorderen Armlinie, die das Grundgeruest kennt. Ergebnis fuer Groesze 38/PK4:
   rund 13,5 Grad Drehung um den BrP. Der Winkel ist als Parameter
   ueberschreibbar. **Werner muss Abb. 8b pruefen.**
2. **Lage des Brustabnaehers im Grundschnitt.** Aus dem Transkript geht nicht
   eindeutig hervor, ob der geoeffnete Abnaeher in der Schulter oder am Armloch
   liegt. Fuer dieses Modul ist das folgenlos: es liefert den Abnaeher als
   **Drehwinkel um den BrP**, und das Kleid legt ihn dorthin, wo das Modell ihn
   braucht (Abnaeherverlegung, S.423). Die Frage bleibt trotzdem offen.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

from geometrie import (
    Punkt,
    abstand,
    cm,
    drehe,
    einheit,
    glatte_kurve,
    mm_zu_cm,
    normale,
    punkt_in_richtung,
    schnitt_mit_senkrechter,
    strecke_teilen,
    sub,
)

from schnitt import Abnaeher, auf_linie, erhoehte_naht, mit_abnaehern

from .grundgeruest import Grundgeruest


# ------------------------------------------------------------------ Ergebnis

@dataclass
class TaillierterGrundschnitt:
    """Taillierter Oberteil-GS bis zur erhoehten Taillenlinie."""

    grundgeruest: Grundgeruest

    # S.184 Abschnitt 7
    brustabnaeher_rad: float = 0.0

    # S.184 Abschnitt 9 bis 11 und S.185 Abschnitt 12, Werte in cm
    me_cm: float = 0.0
    vAbl_cm: float = 0.0
    vTaB_cm: float = 0.0
    hTaB_cm: float = 0.0
    TaAf_cm: float = 0.0
    sn_cm: float = 0.0
    shAbl_cm: float = 0.0
    hAbl_cm: float = 0.0
    starke_figur: bool = False
    hinweise: List[str] = field(default_factory=list)

    # Konturen und Teilstuecke, alle in Millimeter
    vt_kontur: List[Punkt] = field(default_factory=list)
    rt_kontur: List[Punkt] = field(default_factory=list)
    vt_teil: Dict[str, List[Punkt]] = field(default_factory=dict)
    rt_teil: Dict[str, List[Punkt]] = field(default_factory=dict)
    abnaeher: List[Abnaeher] = field(default_factory=list)

    @property
    def brustabnaeher_grad(self) -> float:
        return math.degrees(self.brustabnaeher_rad)


# --------------------------------------------------------------- Konstruktion

def tailliert(
    g: Grundgeruest,
    *,
    li26_x: float | None = None,
    brustabnaeher_grad: float | None = None,
    schulterabnaeher_cm: float = 1.5,
    sn_taillierung_cm: float = 2.0,
    shAbl_anteil: float = 0.42,
    vabl_zugabe_cm: float | None = None,
    vabl_spitze_abstand_cm: float = 0.0,
    shAbl_laenge_cm: float = 13.0,
    hAbl_laenge_cm: float | None = None,
) -> TaillierterGrundschnitt:
    """Entwickelt das Grundgeruest zum taillierten Oberteil-GS.

    `vabl_zugabe_cm` ist der Zuschlag aus S.184 Schritt 36
    ("+ 0 bis 1 cm"): bis PK 4 -> 1,0 · PK 5 bis 7 -> 0,5 · ab PK 8 -> 0.
    Ohne Angabe wird er aus der Passformklasse der Konstruktionstabelle
    abgeleitet.

    `sn_taillierung_cm` ist der **gesamte** Betrag an der Seitennaht
    (S.185: "SN (2 x 1 cm) = 2,0 cm", Vorgabespanne 0 bis 2 cm).

    `hAbl_laenge_cm` ohne Angabe: der hintere Abnaeher laeuft nach S.184
    Schritt 41 bis zur Brustlinie. Die Abbildung 8c auf S.185 vermerkt, dass er
    zum Naehen auf ca. 10 cm gekuerzt wird - dafuer ist der Parameter da.

    `shAbl_anteil` teilt den Rest des Taillenausfalls auf den seitlichen
    hinteren Abnaeher auf. Vorgabe 0,42 entspricht dem Buchbeispiel S.185
    (2,0 von 4,8 cm).
    """
    t = g.tabelle
    P = g.punkt
    e = TaillierterGrundschnitt(grundgeruest=g)

    y_t = g.y_taillenlinie

    # ---------------------------------------------- S.184 Abschnitt 7: Brustabnaeher
    if brustabnaeher_grad is not None:
        e.brustabnaeher_rad = math.radians(brustabnaeher_grad)
    else:
        ziel_x = g.x_vordere_seitenlinie if li26_x is None else li26_x
        v = sub(P["vSuP"], P["BrP"])
        r = math.hypot(*v)
        dx = ziel_x - P["BrP"][0]
        if abs(dx) >= r:
            raise ValueError("Li26 liegt auszerhalb der Drehweite um den BrP")
        winkel_jetzt = math.atan2(v[1], v[0])
        # gedrehter Punkt liegt oberhalb der Brustlinie -> negatives dy
        winkel_ziel = math.atan2(-math.sqrt(r * r - dx * dx), dx)
        e.brustabnaeher_rad = winkel_ziel - winkel_jetzt
    P["vSuP2"] = drehe(P["vSuP"], P["BrP"], e.brustabnaeher_rad)

    # ------------------------------------- S.184 Abschnitt 9: erhoehte Taillenlinie
    # Schritt 34: an den Seitenlinien 1 cm, an der hinteren Armlinie 0,5 cm.
    x_vt_seite = g.x_vordere_seitenlinie - cm(sn_taillierung_cm / 2.0)
    x_rt_seite = g.x_hintere_seitenlinie + cm(sn_taillierung_cm / 2.0)

    vt_stuetzen = [(g.x_vm, 0.0), (x_vt_seite, cm(1.0))]
    rt_stuetzen = [(x_rt_seite, cm(1.0)),
                   (g.x_hintere_armlinie, cm(0.5)),
                   (P["P7"][0], 0.0)]

    vt_taille_voll = erhoehte_naht(g.x_vm, x_vt_seite, y_t, vt_stuetzen)
    rt_taille_voll = erhoehte_naht(x_rt_seite, P["P7"][0], y_t, rt_stuetzen)

    # ------------------------- S.184 Abschnitt 10: vorderer Taillenabnaeher (vAbl)
    # Schritt 35: von der vorderen Armlinie 1/4 TaU abtragen (nicht 1/4 TaW!)
    x_mess = g.x_vordere_armlinie - cm(t.TaU / 4.0)
    e.starke_figur = x_mess < g.x_vm
    if e.starke_figur:
        e.hinweise.append(
            "S.184 Schritt 35: 1/4 TaU reicht ueber die vM hinaus - Hinweis auf "
            "eine 'Starke Figur'. Konstruktion dafuer steht in Band 2."
        )
    e.me_cm = round(mm_zu_cm(abs(x_mess - g.x_vm)), 4)

    if vabl_zugabe_cm is None:
        pk = t.passformklasse
        vabl_zugabe_cm = 1.0 if pk <= 4 else (0.5 if pk <= 7 else 0.0)
    e.vAbl_cm = round(e.me_cm + vabl_zugabe_cm, 4)

    # ------------------------------- S.184 Abschnitt 11: Taillenausfall (TaAf)
    # Schritt 38: "vTaB (ohne Abnaeherinhalt) und hTaB messen, addieren -> TaB"
    # vTaB ist die vordere Taillenbreite von der vM bis zur vorderen Seitenlinie,
    # vermindert um den bereits gezeichneten vorderen Abnaeherinhalt.
    # Nachgerechnet am Buchbeispiel S.184/185 (PK 3, TaU 68):
    #   vTaB = 19,2 + 3,6 - 3,2 = 19,6 · hTaB = 23,2 · TaB = 42,8 · TaAf = 6,8
    e.vTaB_cm = round(
        mm_zu_cm(g.x_vordere_seitenlinie - g.x_vm) - e.vAbl_cm, 4)
    e.hTaB_cm = round(mm_zu_cm(P["P7"][0] - g.x_hintere_seitenlinie), 4)
    e.TaAf_cm = round(e.vTaB_cm + e.hTaB_cm - t.halb_TaW, 4)

    # ------------------------- S.185 Abschnitt 12: Aufteilung des Taillenausfalls
    e.sn_cm = sn_taillierung_cm
    rest = e.TaAf_cm - e.sn_cm
    if rest < 0:
        e.hinweise.append(
            f"Taillenausfall {e.TaAf_cm} cm ist kleiner als die gewaehlte "
            f"Seitennaht-Taillierung {e.sn_cm} cm."
        )
        rest = 0.0
    e.shAbl_cm = round(rest * shAbl_anteil, 4)
    e.hAbl_cm = round(rest - e.shAbl_cm, 4)
    if not (1.0 <= e.shAbl_cm <= 3.0):
        e.hinweise.append(
            f"shAbl = {e.shAbl_cm} cm liegt auszerhalb der Buchspanne 1 bis 3 cm (S.185)."
        )
    if not (2.0 <= e.hAbl_cm <= 4.5):
        e.hinweise.append(
            f"hAbl = {e.hAbl_cm} cm liegt auszerhalb der Buchspanne 2 bis 4 cm (S.185). "
            "Ab 4,5 cm empfiehlt das Buch zwei Abnaeher im Rueckteil (vgl. S.35)."
        )

    # --------------------------------------------------------- Vorderteil bauen
    p_vt_seite = vt_taille_voll[-1]

    x_dart = g.x_brustabnaeher_linie
    halb = cm(e.vAbl_cm / 2.0)
    vabl_a = auf_linie(vt_taille_voll, x_dart - halb)
    vabl_b = auf_linie(vt_taille_voll, x_dart + halb)
    vabl_spitze = (x_dart, P["BrP"][1] + cm(vabl_spitze_abstand_cm))
    vabl = Abnaeher("vAbl", vabl_a, vabl_spitze, vabl_b, e.vAbl_cm)
    e.abnaeher.append(vabl)

    # vM -> Seitennaht, mit eingesetztem vorderem Taillenabnaeher
    vt_taille = mit_abnaehern(vt_taille_voll, [vabl])

    vt_armloch = glatte_kurve([
        P["vSuP"],
        (g.x_vordere_armlinie, P["P18"][1]),
        (g.x_vordere_armlinie + cm(0.4), P["vAP"][1]),
        P["P12"],
    ])
    vt_seitennaht = [P["P12"], p_vt_seite]
    vt_vm = [(g.x_vm, y_t), P["vHalsloch_vm"]]

    e.vt_teil = {
        "vm": vt_vm,
        "halsloch": list(g.vorderes_halsloch),
        "schulter": [P["HlP_v"], P["vSuP"]],
        "armloch": vt_armloch,
        "seitennaht": vt_seitennaht,
        "taille": vt_taille,
        "taille_basis": vt_taille_voll,
    }
    e.vt_kontur = (
        vt_vm
        + list(g.vorderes_halsloch)[1:]
        + [P["vSuP"]]
        + vt_armloch[1:]
        + [p_vt_seite]
        + list(reversed(vt_taille))[1:-1]
    )

    # ---------------------------------------------------------- Rueckteil bauen
    p_rt_seite = rt_taille_voll[0]

    # Schritt 30: hintere Abnaehermitte = Haelfte zwischen hM und hinterer Armlinie
    x_abn_mitte = (P["P7"][0] + g.x_hintere_armlinie) / 2.0
    # seitlicher hinterer Abnaeher zwischen hinterer Armlinie und Seitennaht
    x_shabl_mitte = (g.x_hintere_armlinie + x_rt_seite) / 2.0

    halb_h = cm(e.hAbl_cm / 2.0)
    habl_a = auf_linie(rt_taille_voll, x_abn_mitte - halb_h)
    habl_b = auf_linie(rt_taille_voll, x_abn_mitte + halb_h)
    y_habl_spitze = (g.y_brustlinie if hAbl_laenge_cm is None
                     else y_t - cm(hAbl_laenge_cm))
    habl = Abnaeher("hAbl", habl_a, (x_abn_mitte, y_habl_spitze), habl_b, e.hAbl_cm)
    e.abnaeher.append(habl)

    halb_s = cm(e.shAbl_cm / 2.0)
    shabl_a = auf_linie(rt_taille_voll, x_shabl_mitte - halb_s)
    shabl_b = auf_linie(rt_taille_voll, x_shabl_mitte + halb_s)
    shabl_spitze = (x_shabl_mitte, y_t - cm(shAbl_laenge_cm))
    shabl = Abnaeher("shAbl", shabl_a, shabl_spitze, shabl_b, e.shAbl_cm)
    e.abnaeher.append(shabl)

    # Seitennaht -> hM, mit beiden hinteren Taillenabnaehern
    rt_taille = mit_abnaehern(rt_taille_voll, [shabl, habl])

    # Schulterabnaeher (Schritte 31 und 32)
    schulter_richtung = einheit(sub(P["hSuP"], P["HlP_h"]))
    strecke_bis_mitte = (x_abn_mitte - P["HlP_h"][0]) / schulter_richtung[0]
    su_mitte = punkt_in_richtung(P["HlP_h"], schulter_richtung, strecke_bis_mitte)
    su_a = punkt_in_richtung(su_mitte, schulter_richtung, -cm(schulterabnaeher_cm / 2.0))
    su_b = punkt_in_richtung(su_mitte, schulter_richtung, cm(schulterabnaeher_cm / 2.0))
    su_lot = normale(schulter_richtung)
    if su_lot[1] < 0:
        su_lot = (-su_lot[0], -su_lot[1])
    su_spitze = punkt_in_richtung(su_mitte, su_lot,
                                  (P["P17"][1] - su_mitte[1]) / su_lot[1])
    if schulterabnaeher_cm > 0:
        e.abnaeher.append(
            Abnaeher("Schulterabnaeher", su_a, su_spitze, su_b, schulterabnaeher_cm))
        rt_schulter = [P["HlP_h"], su_a, su_spitze, su_b, P["hSuP"]]
    else:
        # Ohne Schulterabnaeher bleibt die hintere Schulternaht gerade. Die
        # Einhalteweite aus der Konstruktionstabelle bleibt davon unberuehrt.
        rt_schulter = [P["HlP_h"], P["hSuP"]]

    rt_armloch = glatte_kurve([
        P["hSuP"],
        (g.x_hintere_armlinie, P["P17"][1]),
        (g.x_hintere_armlinie - cm(1.5), P["hAP"][1]),
        P["P11"],
    ])
    rt_hm = [P["P2"], P["P7"]]

    e.rt_teil = {
        "hm": rt_hm,
        "halsloch": list(g.hinteres_halsloch),
        "schulter": rt_schulter,
        "armloch": rt_armloch,
        "seitennaht": [P["P11"], p_rt_seite],
        "taille": rt_taille,
        "taille_basis": rt_taille_voll,
    }
    # Umlauf: P2 -> Halsloch -> Schulter -> Armloch -> Seitennaht -> Taille -> P7
    e.rt_kontur = (
        list(g.hinteres_halsloch)
        + rt_schulter[1:]
        + rt_armloch[1:]
        + rt_taille
        + [P["P7"]]
    )

    return e
