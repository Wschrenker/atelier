"""Gerader Rock-Grundschnitt.

Quelle: Hofenbitzer Band 1, 3. Auflage 2024

* **S. 33** - Konstruktionstabelle Rock, Grundgeruest (Schritte 1 bis 9)
* **S. 34** - erhoehte Taillenlinien, Taillenausfall aufteilen, Hueftbogen und
  Abnaeher (Schritte 10 bis 18)
* **S. 35** - Rueckteil mit zwei Abnaehern, Taillennaht (Schritte 19 bis 26)

Transkripte: `100_quellen/.../band_1_geprueft_v1/s33.md`, `s34.md`, `s35.md`

Rechnung in **Millimeter**, Y nach unten. Die vM liegt links bei x = 0, die hM
rechts bei x = 1/2 HueW - so wie das Buch zeichnet ("P1 ist links oben am
Blattrand").
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Tuple

from geometrie import Punkt, cm, glatte_kurve, mm_zu_cm
from schnitt import Abnaeher, auf_linie, erhoehte_naht, mit_abnaehern


@dataclass(frozen=True)
class TabelleRock:
    """Ausgefuellte Konstruktionstabelle nach S.33. Werte in **cm**."""

    groesse: int
    HueU: float
    TaU: float
    HueW: float
    TaW: float
    HueT: float
    MoL: float

    hueftabstich: float
    v_abnaeher: float
    h_abnaeher_1: float
    h_abnaeher_2: float

    @property
    def halb_HueW(self) -> float:
        return self.HueW / 2.0

    @property
    def halb_TaW(self) -> float:
        return self.TaW / 2.0

    @property
    def TaAf(self) -> float:
        """Taillenausfall = 1/2 HueW - 1/2 TaW (S.33)."""
        return round(self.halb_HueW - self.halb_TaW, 6)

    def kontrolle_taillenausfall(self) -> float:
        """Kontrolle S.33: Summe der Aufteilung muss den TaAf ergeben.

        Rueckgabe ist die Abweichung in cm. 0 heiszt: Kontrolle bestanden.
        """
        summe = (self.hueftabstich + self.v_abnaeher
                 + self.h_abnaeher_1 + self.h_abnaeher_2)
        return round(summe - self.TaAf, 6)


def konstruktionstabelle_rock(
    masse,
    *,
    zg_HueU: float = 3.0,
    zg_TaU: float = 2.0,
    MoL: float = 50.0,
    hueftabstich: float | None = None,
    v_abnaeher: float = 2.5,
    h_abnaeher_2: float = 0.0,
) -> TabelleRock:
    """Fuellt die Konstruktionstabelle S.33 aus.

    Vorgabewerte sind die des Buchbeispiels S.33 (Groesze 38, HueU 97 + 3,
    TaU 72 + 2, MoL 50, Hueftabstich 6,5, v. Abnaeher 2,5, ein RT-Abnaeher 4,0).

    `hueftabstich` ohne Angabe: 1/2 TaAf (S.34 Schritt 13, Normalfall).
    Flache Hueftrundung: 1/2 TaAf - 1 bis 1,5 · starke Hueftrundung:
    1/2 TaAf + 1 bis 1,5.

    Der erste hintere Abnaeher ergibt sich als Rest. Uebersteigt er 4,5 cm,
    empfiehlt S.34 zwei Abnaeher im Rueckteil (S.35).
    """
    HueW = masse.HueU + zg_HueU
    TaW = masse.TaU + zg_TaU
    TaAf = HueW / 2.0 - TaW / 2.0
    if hueftabstich is None:
        hueftabstich = TaAf / 2.0
    h1 = TaAf - hueftabstich - v_abnaeher - h_abnaeher_2
    return TabelleRock(
        groesse=masse.groesse,
        HueU=masse.HueU,
        TaU=masse.TaU,
        HueW=HueW,
        TaW=TaW,
        HueT=masse.HueT,
        MoL=MoL,
        hueftabstich=round(hueftabstich, 6),
        v_abnaeher=round(v_abnaeher, 6),
        h_abnaeher_1=round(h1, 6),
        h_abnaeher_2=round(h_abnaeher_2, 6),
    )


@dataclass
class GeraderRock:
    """Ergebnis von S.33 bis S.35. Alle Punkte in **Millimeter**."""

    tabelle: TabelleRock
    punkt: Dict[str, Punkt] = field(default_factory=dict)

    y_hueftlinie: float = 0.0
    y_saumlinie: float = 0.0
    x_seitenlinie: float = 0.0
    x_hm: float = 0.0

    vt_taille: List[Punkt] = field(default_factory=list)
    rt_taille: List[Punkt] = field(default_factory=list)
    vt_hueftbogen: List[Punkt] = field(default_factory=list)
    rt_hueftbogen: List[Punkt] = field(default_factory=list)
    abnaeher: List[Abnaeher] = field(default_factory=list)
    hinweise: List[str] = field(default_factory=list)


def gerader_rock(
    t: TabelleRock,
    *,
    taillenerhoehung_sn_cm: float = 1.0,
    v_abnaeher_laenge_cm: float = 9.0,
    h_abnaeher_laenge_cm: float = 14.0,
) -> GeraderRock:
    """Konstruiert den geraden Rock-Grundschnitt bis zur Taillennaht.

    `taillenerhoehung_sn_cm` ist Schritt 10, S.34: "von P7 die Seitenlinie um
    1 bis 1,5 cm nach oben verlaengern". Die Erhoehung am vorderen Abnaeher
    betraegt die Haelfte davon (Schritt 11), am hinteren ein Drittel
    (Schritt 12).

    Abnaeherlaengen aus S.34: vorne 8 bis 10 cm, hinten 13 bis 16 cm.
    """
    r = GeraderRock(tabelle=t)
    P = r.punkt

    halb_hue = cm(t.halb_HueW)
    r.x_hm = halb_hue
    r.y_saumlinie = cm(t.MoL)
    r.y_hueftlinie = cm(t.HueT)

    # --- S.33 Schritte 1 bis 9 --------------------------------------------
    P["P1"] = (0.0, 0.0)
    P["P2"] = (0.0, r.y_saumlinie)
    P["P3"] = (0.0, r.y_hueftlinie)
    P["P4"] = (halb_hue, 0.0)
    P["P5"] = (halb_hue, r.y_saumlinie)
    P["P6"] = (halb_hue, r.y_hueftlinie)
    P["P7"] = (halb_hue / 2.0, 0.0)
    P["P8"] = (halb_hue / 2.0, r.y_saumlinie)
    P["P9"] = (halb_hue / 2.0, r.y_hueftlinie)
    r.x_seitenlinie = P["P7"][0]

    # --- S.34 Schritt 10 bis 12: erhoehte Taillenlinien --------------------
    erh_sn = cm(taillenerhoehung_sn_cm)
    erh_v = erh_sn / 2.0
    erh_h = erh_sn / 3.0
    P["P10"] = (r.x_seitenlinie, -erh_sn)

    # --- S.34 Schritt 16: Hueftbogen --------------------------------------
    halb_abstich = cm(t.hueftabstich / 2.0)
    P["Taille_v_seite"] = (r.x_seitenlinie - halb_abstich, -erh_sn)
    P["Taille_h_seite"] = (r.x_seitenlinie + halb_abstich, -erh_sn)

    r.vt_hueftbogen = glatte_kurve([
        P["Taille_v_seite"],
        (r.x_seitenlinie - halb_abstich * 0.30, r.y_hueftlinie * 0.52),
        P["P9"],
    ])
    r.rt_hueftbogen = glatte_kurve([
        P["Taille_h_seite"],
        (r.x_seitenlinie + halb_abstich * 0.30, r.y_hueftlinie * 0.52),
        P["P9"],
    ])

    # --- S.34 Schritt 17: vorderer Abnaeher --------------------------------
    x_va = P["Taille_v_seite"][0] - cm(t.TaU / 10.0)
    vt_linie = erhoehte_naht(0.0, P["Taille_v_seite"][0], 0.0,
                             [(0.0, 0.0), (x_va, erh_v),
                              (P["Taille_v_seite"][0], erh_sn)])
    if t.v_abnaeher > 0:
        halb = cm(t.v_abnaeher / 2.0)
        va = Abnaeher(
            "v. Abnaeher",
            auf_linie(vt_linie, x_va - halb),
            (x_va, cm(v_abnaeher_laenge_cm)),
            auf_linie(vt_linie, x_va + halb),
            t.v_abnaeher,
        )
        r.abnaeher.append(va)
        r.vt_taille = mit_abnaehern(vt_linie, [va])
    else:
        r.vt_taille = vt_linie

    # --- S.34 Schritt 18 / S.35 Schritt 20: hintere Abnaeher ---------------
    # Abnaehermitte in der Mitte zwischen hinterem Hueftbogen und hM
    x_ha1 = (P["Taille_h_seite"][0] + halb_hue) / 2.0
    stuetzen = [(P["Taille_h_seite"][0], erh_sn), (x_ha1, erh_h), (halb_hue, 0.0)]
    rt_linie = erhoehte_naht(P["Taille_h_seite"][0], halb_hue, 0.0, stuetzen)

    hintere: List[Abnaeher] = []
    if t.h_abnaeher_1 > 0:
        halb = cm(t.h_abnaeher_1 / 2.0)
        hintere.append(Abnaeher(
            "1. h. Abnaeher",
            auf_linie(rt_linie, x_ha1 - halb),
            (x_ha1, cm(h_abnaeher_laenge_cm)),
            auf_linie(rt_linie, x_ha1 + halb),
            t.h_abnaeher_1,
        ))
    if t.h_abnaeher_2 > 0:
        # S.35 Schritt 21: Mitte zwischen Hueftbogen und Schenkel des 1. Abnaehers
        x_ha2 = (P["Taille_h_seite"][0] + (x_ha1 - cm(t.h_abnaeher_1 / 2.0))) / 2.0
        halb = cm(t.h_abnaeher_2 / 2.0)
        hintere.append(Abnaeher(
            "2. h. Abnaeher",
            auf_linie(rt_linie, x_ha2 - halb),
            (x_ha2, cm(h_abnaeher_laenge_cm - 2.0)),
            auf_linie(rt_linie, x_ha2 + halb),
            t.h_abnaeher_2,
        ))
    r.abnaeher.extend(hintere)
    r.rt_taille = mit_abnaehern(rt_linie, hintere) if hintere else rt_linie

    if t.h_abnaeher_1 > 4.5 and t.h_abnaeher_2 == 0:
        r.hinweise.append(
            f"1. h. Abnaeher = {t.h_abnaeher_1} cm ueberschreitet 4,5 cm. "
            "S.34 empfiehlt dann zwei Abnaeher im Rueckteil (S.35)."
        )
    fehler = t.kontrolle_taillenausfall()
    if abs(fehler) > 1e-6:
        r.hinweise.append(
            f"Kontrolle S.33 nicht erfuellt: Summe der Aufteilung weicht um "
            f"{fehler} cm vom Taillenausfall ab."
        )
    return r
