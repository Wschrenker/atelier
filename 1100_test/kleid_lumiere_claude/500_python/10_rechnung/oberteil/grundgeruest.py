"""Grundgeruest fuer saemtliche Oberteil-Grundschnitte.

Quelle: Hofenbitzer Band 1, 3. Auflage 2024

* **S. 177** - Konstruktionstabelle, taillierter Oberteil-GS, Groesze 38, PK 4
* **S. 178** - Konstruktionstabelle PK 3 (enthaelt zwei markierte Buchfehler)
* **S. 179** - Schritte 1 bis 9: erste Linien, hintere Mitte
* **S. 180** - Schritte 10 bis 14: Brustweite abtragen, Hilfslinien, vM
* **S. 181** - Schritte 15 bis 24: Halsloecher und Schultern

Transkripte:
`100_quellen/10_hofenbitzer_b1/2_transkript/band_1_geprueft_v1/s177..s181.md`

Rechnung in **Millimeter**, Y nach unten. Die hM liegt rechts bei x = 0, die
vM links bei negativem x - so wie das Buch zeichnet ("Senkrechte Grundlinie
rechts am Blattrand").

Offene Buchstelle, bewusst nicht still entschieden
--------------------------------------------------
S.181 nennt Punkt P4 nicht ausdruecklich. Die Nummerierung P1-P6 folgt hier
den Schritten 1 bis 6 von S.179 in der Reihenfolge, in der das Buch sie
abtraegt: P3 = Saumlinie, P4 = Brustlinie, P5 = Taillenlinie, P6 = Hueftlinie.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List

from geometrie import (
    Punkt,
    abstand,
    cm,
    einheit,
    kurve_durch,
    normale,
    punkt_in_richtung,
    richtung_grad,
    schnitt_mit_waagerechter,
    sub,
)
from masse import Koerpermasse


# --------------------------------------------------------- Konstruktionstabelle

@dataclass(frozen=True)
class TabelleOberteil:
    """Ausgefuellte Konstruktionstabelle nach S.177. Alle Werte in **cm**."""

    groesse: int
    passformklasse: int

    BrU: float
    TaU: float
    HueU: float
    BrW: float
    TaW: float
    HueW: float

    AlT_plus: float
    HueT: float
    BrT: float
    MoL: float
    HlB: float
    RueB_plus: float
    ArD_plus: float
    BrB_plus: float

    SuNL: float
    hSuNL: float
    SuWi: float

    RueL: float
    VL: float

    @property
    def halb_BrW(self) -> float:
        return self.BrW / 2.0

    @property
    def halb_TaW(self) -> float:
        return self.TaW / 2.0

    @property
    def halb_HueW(self) -> float:
        return self.HueW / 2.0

    @property
    def individuelle_balance(self) -> float:
        """VL - RueL (S.177, Abschnitt Balancemasze)."""
        return round(self.VL - self.RueL, 4)

    def kontrolle_brustweite(self) -> float:
        """Kontrolle S.177 / S.180: RueB+ + ArD+ + BrB+ muss 1/2 BrW ergeben.

        Rueckgabe ist die Abweichung in cm. 0 heiszt: Kontrolle bestanden.
        """
        summe = self.RueB_plus + self.ArD_plus + self.BrB_plus
        return round(summe - self.halb_BrW, 6)


def konstruktionstabelle(
    masse: Koerpermasse,
    *,
    passformklasse: int = 4,
    zg_BrU: float = 8.0,
    zg_TaU: float = 6.0,
    zg_HueU: float = 4.0,
    zg_AlT: float = 1.7,
    zg_RueB: float = 0.8,
    zg_ArD: float = 2.0,
    zg_BrB: float = 1.2,
    zg_SuB: float = 0.4,
    einhalteweite: float = 0.7,
    MoL: float = 95.0,
) -> TabelleOberteil:
    """Fuellt die Konstruktionstabelle S.177 aus.

    Die Vorgabewerte sind exakt die des Buchbeispiels S.177
    (taillierter Oberteil-GS, Groesze 38, PK 4). Die Zugaben stammen aus der
    Zugabentabelle S.176 und sind bewusst Parameter: sie entscheiden ueber die
    Passformklasse und damit ueber die Verwendung des Grundschnitts.

    `einhalteweite` ist die Einhalteweite der hinteren Schulternaht,
    S.177: "SuNL + Einhalteweite 0,5 cm bis 1 cm".
    """
    SuNL = masse.SuB + zg_SuB
    return TabelleOberteil(
        groesse=masse.groesse,
        passformklasse=passformklasse,
        BrU=masse.BrU,
        TaU=masse.TaU,
        HueU=masse.HueU,
        BrW=masse.BrU + zg_BrU,
        TaW=masse.TaU + zg_TaU,
        HueW=masse.HueU + zg_HueU,
        AlT_plus=round(masse.AlT + zg_AlT, 6),
        HueT=masse.HueT,
        BrT=masse.BrT,
        MoL=MoL,
        HlB=masse.HlB,
        RueB_plus=round(masse.RueB + zg_RueB, 6),
        ArD_plus=round(masse.ArD + zg_ArD, 6),
        BrB_plus=round(masse.BrB + zg_BrB, 6),
        SuNL=round(SuNL, 6),
        hSuNL=round(SuNL + einhalteweite, 6),
        SuWi=masse.SuWi,
        RueL=masse.RueL,
        VL=masse.VL,
    )


# ------------------------------------------------------------- Grundgeruest

@dataclass
class Grundgeruest:
    """Ergebnis von S.179 bis S.181. Alle Punkte in **Millimeter**."""

    tabelle: TabelleOberteil
    punkt: Dict[str, Punkt] = field(default_factory=dict)

    # waagerechte Linien (y-Werte)
    y_brustlinie: float = 0.0
    y_taillenlinie: float = 0.0
    y_hueftlinie: float = 0.0
    y_saumlinie: float = 0.0

    # senkrechte Hilfslinien (x-Werte)
    x_hintere_armlinie: float = 0.0
    x_hintere_seitenlinie: float = 0.0
    x_vordere_seitenlinie: float = 0.0
    x_vordere_armlinie: float = 0.0
    x_vm: float = 0.0
    x_brustabnaeher_linie: float = 0.0

    hinteres_halsloch: List[Punkt] = field(default_factory=list)
    vorderes_halsloch: List[Punkt] = field(default_factory=list)
    hintere_mitte: List[Punkt] = field(default_factory=list)

    def __getitem__(self, name: str) -> Punkt:
        return self.punkt[name]


def grundgeruest(t: TabelleOberteil, *, zwischenraum: float = 8.5) -> Grundgeruest:
    """Konstruiert das Grundgeruest nach S.179 bis S.181.

    `zwischenraum` ist der Abstand zwischen RT und VT auf der Brustlinie,
    S.180 Schritt 12: "einen Zwischenraum zwischen RT und VT von ca. 7 bis
    10 cm abtragen". Vorgabe 8,5 cm = Mitte der Buchspanne.

    Es wird ausschlieszlich die **taillierte hintere Mitte mit Naht**
    konstruiert (S.179 Schritte 7 und 8, Variante Kasten 1c) - das ist die
    Variante, die ein Kleid mit Rueckenverschluss braucht.
    """
    if not (7.0 <= zwischenraum <= 10.0):
        raise ValueError(
            "Zwischenraum RT/VT liegt laut S.180 Schritt 12 zwischen 7 und 10 cm, "
            f"hier: {zwischenraum} cm"
        )

    g = Grundgeruest(tabelle=t)
    P = g.punkt

    # --- S.179 Schritt 1: Grundlinie rechts, P1 oben -----------------------
    P["P1"] = (0.0, 0.0)

    # Schritt 2: von P1 HlB : 3 + 1 cm nach unten
    P["P2"] = (0.0, cm(t.HlB / 3.0 + 1.0))

    # Schritt 3: von P2 die Modelllaenge nach unten -> Saumlinie
    P["P3"] = (0.0, P["P2"][1] + cm(t.MoL))
    g.y_saumlinie = P["P3"][1]

    # Schritt 4: von P2 die Armlochtiefe mit Zugabe nach unten -> Brustlinie
    P["P4"] = (0.0, P["P2"][1] + cm(t.AlT_plus))
    g.y_brustlinie = P["P4"][1]

    # Schritt 5: von P2 die Rueckenlaenge nach unten -> Taillenlinie
    P["P5"] = (0.0, P["P2"][1] + cm(t.RueL))
    g.y_taillenlinie = P["P5"][1]

    # Schritt 6: von P5 die Huefttiefe nach unten -> Hueftlinie
    P["P6"] = (0.0, P["P5"][1] + cm(t.HueT))
    g.y_hueftlinie = P["P6"][1]

    # Schritt 7: von P5 und P3 jeweils 2 cm nach links (taillierte hM)
    P["P7"] = (-cm(2.0), g.y_taillenlinie)
    P["P8"] = (-cm(2.0), g.y_saumlinie)

    # Schritt 8: taillierte hM von P2 ueber P7 nach P8
    g.hintere_mitte = [P["P2"], P["P7"], P["P8"]]

    # Schritt 9: Schnittpunkt der hM mit der Brustlinie
    P["P9"] = schnitt_mit_waagerechter(P["P2"], P["P7"], g.y_brustlinie)

    # --- S.180: Brustweite abtragen ---------------------------------------
    x9 = P["P9"][0]
    g.x_hintere_armlinie = x9 - cm(t.RueB_plus)                       # Schritt 10
    g.x_hintere_seitenlinie = g.x_hintere_armlinie - cm(t.ArD_plus * 2.0 / 3.0)  # 11
    g.x_vordere_seitenlinie = g.x_hintere_seitenlinie - cm(zwischenraum)         # 12
    g.x_vordere_armlinie = g.x_vordere_seitenlinie - cm(t.ArD_plus / 3.0)        # 13
    g.x_vm = g.x_vordere_armlinie - cm(t.BrB_plus)                               # 14

    P["P10"] = (g.x_hintere_armlinie, g.y_brustlinie)
    P["P11"] = (g.x_hintere_seitenlinie, g.y_brustlinie)
    P["P12"] = (g.x_vordere_seitenlinie, g.y_brustlinie)
    P["P13"] = (g.x_vordere_armlinie, g.y_brustlinie)
    P["P14"] = (g.x_vm, g.y_brustlinie)

    # --- S.181 Abschnitt 4: hinteres Halsloch und Schulter -----------------
    P["HlP_h"] = (-cm(t.HlB + 0.5), 0.0)

    # Schritt 15: hinteres Halsloch rechtwinklig aus der hM formen.
    hm_richtung = einheit(sub(P["P7"], P["P2"]))
    raus_aus_hm = normale(hm_richtung)                # zeigt aus der hM nach links
    if raus_aus_hm[0] > 0:
        raus_aus_hm = (-raus_aus_hm[0], -raus_aus_hm[1])
    hals_h = abstand(P["P2"], P["HlP_h"])
    g.hinteres_halsloch = kurve_durch(
        P["P2"], raus_aus_hm, hals_h * 0.62,
        P["HlP_h"], (0.0, 1.0), hals_h * 0.32,
    )

    # Schulterwinkel - 2 Grad vom hinteren HlP nach links unten
    hi_su_richtung = (-math.cos(math.radians(t.SuWi - 2.0)),
                      math.sin(math.radians(t.SuWi - 2.0)))
    P["hSuP"] = punkt_in_richtung(P["HlP_h"], hi_su_richtung, cm(t.hSuNL))

    # Schritt 16: Schnittpunkt hintere Armlinie / Schulternaht
    strecke_bis_armlinie = (P["HlP_h"][0] - g.x_hintere_armlinie) / abs(hi_su_richtung[0])
    if strecke_bis_armlinie <= cm(t.hSuNL):
        P["P16"] = punkt_in_richtung(P["HlP_h"], hi_su_richtung, strecke_bis_armlinie)
    else:
        # "Bei groszer RueB und schmaler Schulter ergibt sich ggf. kein
        #  Schnittpunkt. Dann endet die hintere Armlinie auf Hoehe des hSuP."
        P["P16"] = (g.x_hintere_armlinie, P["hSuP"][1])

    # Schritt 17: Strecke P10 bis P16 halbieren -> P17, Schulterblattlinie
    P["P17"] = (g.x_hintere_armlinie, (P["P10"][1] + P["P16"][1]) / 2.0)
    # untere Haelfte nochmals halbieren -> hinterer Aermelpunkt
    P["hAP"] = (g.x_hintere_armlinie, (P["P17"][1] + P["P10"][1]) / 2.0)
    # Schritt 18: Hilfslinie nach links -> Schnittpunkt mit vorderer Armlinie
    P["P18"] = (g.x_vordere_armlinie, P["hAP"][1])

    # --- S.181 Abschnitt 5: vorderes Halsloch ------------------------------
    P["P19"] = (g.x_vm, g.y_taillenlinie)                       # Schritt 19
    P["P20"] = (g.x_vm, g.y_taillenlinie - cm(t.VL - 1.0))      # Schritt 20
    P["P21"] = (g.x_vm, P["P20"][1] + cm(t.BrT - 1.0))          # Schritt 21
    P["BrP"] = (g.x_vm + cm(t.BrB_plus / 2.0 - 0.3), P["P21"][1])
    g.x_brustabnaeher_linie = P["BrP"][0]                       # Schritt 22

    P["HlP_v"] = (g.x_vm + cm(t.HlB), P["P20"][1])
    P["vHalsloch_vm"] = (g.x_vm, P["P20"][1] + cm(t.HlB + 0.5))  # Schritt 23

    hals_v = abstand(P["vHalsloch_vm"], P["HlP_v"])
    g.vorderes_halsloch = kurve_durch(
        P["vHalsloch_vm"], (1.0, 0.0), hals_v * 0.58,
        P["HlP_v"], (0.0, 1.0), hals_v * 0.55,
    )

    # --- S.181 Abschnitt 6: vordere Schulter -------------------------------
    vo_su_richtung = richtung_grad(t.SuWi + 2.0)   # nach rechts unten
    P["vSuP"] = punkt_in_richtung(P["HlP_v"], vo_su_richtung, cm(t.SuNL))
    # vorderer Aermelpunkt: 1/4 ArD+ von P13 nach oben
    P["vAP"] = (g.x_vordere_armlinie, g.y_brustlinie - cm(t.ArD_plus / 4.0))

    return g
