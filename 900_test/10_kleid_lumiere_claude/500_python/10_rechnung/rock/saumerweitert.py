"""Saumerweiterter Rock-Grundschnitt.

Quelle: Hofenbitzer Band 1, 3. Auflage 2024

* **S. 42** - Einschnittlinien, Abnaeher verschieben, Saum oeffnen (Schritte 1-10)
* **S. 43** - Oeffnungsbetrag, RT-Abnaeher verschieben, Taillennaht und Saum
  ausformen (Schritte 11-13)

Transkripte: `100_quellen/.../band_1_geprueft_v1/s42.md`, `s43.md`

Buchformel S.43:

    Oeffnungsbetrag = gewuenschte Saumerweiterung : Erweiterungsstellen
    Beispiel        = 48 cm : 6 = 8 cm

Es gibt **sechs Erweiterungsstellen** am ganzen Rock: je ein Keil im VT und im
RT, je ein halber Keil an den beiden Seitennaehten - am halben Rock also drei
Keile.

Konstruktionsweg, wie ihn das Buch beschreibt
---------------------------------------------
1. Einschnittlinien: im VT bei 1/3 der halben VT-Breite von der vM, im RT bei
   2/3 der halben RT-Breite von der SN (S.42, Abschnitt 1).
2. Die Abnaeherinhalte werden auf die Einschnittlinie verschoben; die neue
   Abnaeherspitze liegt mindestens 3 cm oberhalb der Hueftlinie.
3. VT: der vordere Abnaeher wird zugelegt, fuer mehr Saumweite wird an der
   Spitze zusaetzlich geoeffnet - der Drehpunkt liegt dann an der Taille.
4. RT: um denselben Betrag am Saum oeffnen, Drehpunkt ist die neue
   Abnaeherspitze. Der verbleibende Abnaeher ist immer noch grosz genug.
5. An den Seitennaehten jeweils den halben Oeffnungsbetrag ausstellen und die
   neue Seitennaht gerade als Tangente auf den Hueftbogen zeichnen.
6. Taillennaht ausformen, Saum rund formen.

Bewusste Vereinfachung, hier festgehalten
-----------------------------------------
Der Saum wird als **eine glatte Kurve** durch vier Punkte neu geformt: den
Saumpunkt an der vM beziehungsweise hM, die beiden Kanten des geoeffneten Keils
und den neuen Saumpunkt an der Seitennaht. Das Buch sagt nur "Saum rund formen"
(S.43 Schritt 13) und nennt dafuer keine Konstruktion. Die Kurve ist damit eine
Interpretation, kein Buchwert - deshalb steht sie hier und nicht in einer
Formeldatei.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Sequence

from geometrie import (
    Punkt,
    abstand,
    cm,
    drehe,
    einheit,
    glatte_kurve,
    mm_zu_cm,
    normale,
    polylinie_laenge,
    punkt_in_richtung,
    sub,
)
from schnitt import Abnaeher, auf_linie, erhoehte_naht, mit_abnaehern

from .gerader_rock import GeraderRock


def _normiere(winkel: float) -> float:
    while winkel > math.pi:
        winkel -= 2.0 * math.pi
    while winkel < -math.pi:
        winkel += 2.0 * math.pi
    return winkel


@dataclass
class SaumerweiterterRock:
    """Ergebnis von S.42 und S.43. Punkte in Millimeter."""

    grund: GeraderRock
    saumerweiterung_cm: float
    oeffnungsbetrag_cm: float

    vt_kontur: List[Punkt] = field(default_factory=list)
    rt_kontur: List[Punkt] = field(default_factory=list)
    vt_teil: Dict[str, List[Punkt]] = field(default_factory=dict)
    rt_teil: Dict[str, List[Punkt]] = field(default_factory=dict)
    rt_abnaeher: Abnaeher | None = None
    rest_abnaeher_cm: float = 0.0

    saumweite_cm: float = 0.0
    taillenweite_cm: float = 0.0
    hinweise: List[str] = field(default_factory=list)


def saumerweitert(
    r: GeraderRock,
    *,
    saumerweiterung_cm: float,
    abnaeherspitze_ueber_huefte_cm: float = 3.0,
    rt_abnaeher_laenge_cm: float = 13.5,
    taillenerhoehung_sn_cm: float = 1.0,
) -> SaumerweiterterRock:
    """Entwickelt den geraden Rock-GS zum saumerweiterten Rock-GS.

    `saumerweiterung_cm` ist die gewuenschte Erweiterung der **gesamten**
    Saumweite. Der Oeffnungsbetrag je Erweiterungsstelle ergibt sich daraus
    nach S.43 als Saumerweiterung : 6.

    `rt_abnaeher_laenge_cm` ist S.43 Schritt 11 beziehungsweise die Maszangabe
    "12 bis 15 cm" der Abbildung 3.
    """
    t = r.tabelle
    P = r.punkt
    O = cm(saumerweiterung_cm / 6.0)

    e = SaumerweiterterRock(
        grund=r,
        saumerweiterung_cm=saumerweiterung_cm,
        oeffnungsbetrag_cm=saumerweiterung_cm / 6.0,
    )

    erh_sn = cm(taillenerhoehung_sn_cm)
    erh_v = erh_sn / 2.0
    erh_h = erh_sn / 3.0
    y_saum = r.y_saumlinie
    y_spitze = r.y_hueftlinie - cm(abnaeherspitze_ueber_huefte_cm)

    x_v_seite = P["Taille_v_seite"][0]
    x_h_seite = P["Taille_h_seite"][0]

    # ------------------------------------------------- S.42 Abschnitt 1: Einschnitte
    x_ev = r.x_seitenlinie / 3.0                                    # VT: 1/3 von der vM
    x_eh = r.x_seitenlinie + (r.x_hm - r.x_seitenlinie) * 2.0 / 3.0  # RT: 2/3 von der SN

    # =========================================================== Vorderteil
    vt_linie = erhoehte_naht(0.0, x_v_seite, 0.0,
                             [(0.0, 0.0), (x_ev, erh_v), (x_v_seite, erh_sn)])
    i_v = cm(t.v_abnaeher)
    A_v = auf_linie(vt_linie, x_ev - i_v / 2.0)
    B_v = auf_linie(vt_linie, x_ev + i_v / 2.0)
    spitze_v = (x_ev, y_spitze)

    # Schritt 7: den vorderen Abnaeher zulegen (Drehung um die Spitze)
    theta_zulegen = _normiere(
        math.atan2(A_v[1] - spitze_v[1], A_v[0] - spitze_v[0])
        - math.atan2(B_v[1] - spitze_v[1], B_v[0] - spitze_v[0])
    )
    saum_schnitt = (x_ev, y_saum)
    nach_zulegen = drehe(saum_schnitt, spitze_v, theta_zulegen)
    geoeffnet = abstand(nach_zulegen, saum_schnitt)

    # Schritt 7 Fortsetzung: fuer mehr Saumweite an der Spitze zusaetzlich
    # oeffnen - der Drehpunkt ZP liegt dann an der Taille.
    rest = O - geoeffnet
    if rest > 0:
        radius = abstand(A_v, nach_zulegen)
        theta_extra = math.copysign(2.0 * math.asin(min(1.0, rest / (2.0 * radius))),
                                    theta_zulegen)
    else:
        theta_extra = 0.0
        e.hinweise.append(
            f"Das Zulegen des vorderen Abnaehers oeffnet den Saum bereits um "
            f"{mm_zu_cm(geoeffnet):.1f} cm - mehr als der Oeffnungsbetrag "
            f"{e.oeffnungsbetrag_cm:.1f} cm. Der Rock wird weiter als gewuenscht."
        )

    def T_v(p: Punkt) -> Punkt:
        return drehe(drehe(p, spitze_v, theta_zulegen), A_v, theta_extra)

    vt_taille_fest = [p for p in vt_linie if p[0] < A_v[0]] + [A_v]
    vt_taille_aussen = [T_v(p) for p in ([B_v] + [p for p in vt_linie if p[0] > B_v[0]])]
    vt_hueft = [T_v(p) for p in r.vt_hueftbogen]
    p9_v = T_v(P["P9"])
    p8_v = T_v(P["P8"])
    saum_v_rot = T_v(saum_schnitt)

    # Schritt 9: an der Seitennaht den halben Oeffnungsbetrag ausstellen
    richtung = einheit(sub(p8_v, p9_v))
    aus = normale(richtung)
    if aus[0] < 0:
        aus = (-aus[0], -aus[1])
    s_v = punkt_in_richtung(p8_v, aus, O / 2.0)

    # Schritt 13: Saum rund formen
    saum_v = glatte_kurve([(0.0, y_saum), saum_schnitt, saum_v_rot, s_v],
                          teile_je_abschnitt=14)

    e.vt_teil = {
        "taille": vt_taille_fest + vt_taille_aussen,
        "hueftbogen": vt_hueft,
        "seitennaht": [p9_v, s_v],
        "saum": saum_v,
        "vm": [(0.0, y_saum), (0.0, 0.0)],
        "einschnittlinie": [(x_ev, A_v[1]), spitze_v],
    }
    e.vt_kontur = (
        vt_taille_fest + vt_taille_aussen
        + vt_hueft[1:]
        + [s_v]
        + list(reversed(saum_v))[1:]
    )

    # ============================================================ Rueckteil
    rt_linie = erhoehte_naht(x_h_seite, r.x_hm, 0.0,
                             [(x_h_seite, erh_sn), (x_eh, erh_h), (r.x_hm, 0.0)])
    i_h = cm(t.h_abnaeher_1 + t.h_abnaeher_2)
    A_h = auf_linie(rt_linie, x_eh - i_h / 2.0)
    B_h = auf_linie(rt_linie, x_eh + i_h / 2.0)
    spitze_h = (x_eh, y_spitze)

    # Schritt 8: um denselben Betrag oeffnen, Drehpunkt ist die Abnaeherspitze
    radius_h = abstand(spitze_h, (x_eh, y_saum))
    theta_h = 2.0 * math.asin(min(1.0, O / (2.0 * radius_h)))

    def T_h(p: Punkt) -> Punkt:
        return drehe(p, spitze_h, theta_h)

    A_h_neu = T_h(A_h)
    e.rest_abnaeher_cm = round(mm_zu_cm(abstand(A_h_neu, B_h)), 4)
    if e.rest_abnaeher_cm < 1.0:
        e.hinweise.append(
            f"Der verbleibende RT-Abnaeher betraegt nur noch "
            f"{e.rest_abnaeher_cm:.1f} cm. S.42 Schritt 10 setzt voraus, dass er "
            "grosz genug zum Naehen bleibt."
        )

    rt_taille_fest = [B_h] + [p for p in rt_linie if p[0] > B_h[0]]
    rt_taille_aussen = [T_h(p) for p in
                        ([p for p in rt_linie if p[0] < A_h[0]] + [A_h])]
    rt_hueft = [T_h(p) for p in r.rt_hueftbogen]
    p9_h = T_h(P["P9"])
    p8_h = T_h(P["P8"])
    saum_h_rot = T_h((x_eh, y_saum))

    richtung = einheit(sub(p8_h, p9_h))
    aus = normale(richtung)
    if aus[0] > 0:
        aus = (-aus[0], -aus[1])
    s_h = punkt_in_richtung(p8_h, aus, O / 2.0)

    saum_h = glatte_kurve([s_h, saum_h_rot, (x_eh, y_saum), (r.x_hm, y_saum)],
                          teile_je_abschnitt=14)

    # S.43 Schritt 11: RT-Abnaeher in die Mitte des Rueckteils zurueckverschieben
    rt_taille_ohne = rt_taille_aussen + rt_taille_fest[1:]
    rt_taille_ohne = sorted(rt_taille_ohne, key=lambda p: p[0])
    x_mitte = (rt_taille_ohne[0][0] + r.x_hm) / 2.0
    halb = cm(e.rest_abnaeher_cm / 2.0)
    abn = Abnaeher(
        "h. Abnaeher",
        auf_linie(rt_taille_ohne, x_mitte - halb),
        (x_mitte, cm(rt_abnaeher_laenge_cm)),
        auf_linie(rt_taille_ohne, x_mitte + halb),
        e.rest_abnaeher_cm,
    )
    e.rt_abnaeher = abn
    rt_taille = mit_abnaehern(rt_taille_ohne, [abn])

    e.rt_teil = {
        "taille": rt_taille,
        "hueftbogen": rt_hueft,
        "seitennaht": [p9_h, s_h],
        "saum": saum_h,
        "hm": [(r.x_hm, 0.0), (r.x_hm, y_saum)],
        "einschnittlinie": [(x_eh, B_h[1]), spitze_h],
    }
    # Umlauf: Seitennaht -> Hueftbogen -> Taille -> hM -> Saum -> zurueck
    e.rt_kontur = (
        [s_h]
        + list(reversed(rt_hueft))
        + rt_taille[1:]
        + [(r.x_hm, y_saum)]
        + list(reversed(saum_h))[1:-1]
    )

    # ------------------------------------------------------------- Kontrollen
    e.saumweite_cm = round(2.0 * mm_zu_cm(
        polylinie_laenge(saum_v) + polylinie_laenge(saum_h)), 1)
    e.taillenweite_cm = round(2.0 * mm_zu_cm(
        polylinie_laenge(e.vt_teil["taille"]) + polylinie_laenge(rt_taille_ohne)
        - cm(e.rest_abnaeher_cm)), 1)

    l_v = abstand(p9_v, s_v)
    l_h = abstand(p9_h, s_h)
    if abs(l_v - l_h) > cm(0.3):
        e.hinweise.append(
            f"S.43 Schritt 13: die Seitennaehte sind unterschiedlich lang "
            f"(VT {mm_zu_cm(l_v):.1f} cm, RT {mm_zu_cm(l_h):.1f} cm)."
        )
    return e
