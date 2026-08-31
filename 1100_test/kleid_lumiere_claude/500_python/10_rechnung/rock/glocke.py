"""Echter Glockenrock - Vollglocke / Tellerrock.

Quelle: Hofenbitzer Band 1, 3. Auflage 2024, **S. 44**.
Transkript: `100_quellen/.../band_1_geprueft_v1/s44_glockenrock.md`
**Status der Quelle: fachlich freigegeben durch Werner/Munkhuu am 2026-06-21.**

Buchformeln, woertlich:

    rTaW = TaW : (2 x pi)
    rSaW = rTaW + MoL
    SaW  = 2 x pi x rSaW

und bei Naht- beziehungsweise Schlitzloesung an der Taille:

    rTaW = (TaW + 2 x NZg) : (2 x pi)

Das Buchbeispiel rechnet mit **pi = 3,14**. Ob die Engine 3,14 oder die volle
Genauigkeit benutzt, ist laut Transkript eine dokumentierte
Implementierungsentscheidung, keine offene Lesestelle. Vorgabe hier: `math.pi`.
Fuer die Nachrechnung des Buchbeispiels wird `pi=3.14` uebergeben.

Dieses Modul gehoert nicht zum Kleid "Lumiere" - der fliegt eine A-Linie, keinen
Vollkreis. Es liegt hier, weil S.44 die einzige bereits **fachlich freigegebene**
Rockseite ist und als Pruefwert dient.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List

from geometrie import Punkt, cm, kreisbogen, mm_zu_cm


@dataclass
class Glockenrock:
    """Ergebnis von S.44. Radien in Millimeter, Kontrollmasze in Zentimeter."""

    rTaW_cm: float
    rSaW_cm: float
    SaW_cm: float
    taillenkreis: List[Punkt]
    saumkreis: List[Punkt]


def vollglocke(TaW_cm: float, MoL_cm: float, *, NZg_cm: float = 0.0,
               pi: float = math.pi, anteil: float = 1.0) -> Glockenrock:
    """Echter Glockenrock nach S.44.

    `NZg_cm` ist die Nahtzugabe der Schlitz-/Nahtloesung an der Taille. S.44
    schreibt dafuer keinen festen Zahlenwert vor - sie bleibt Parameter.

    `anteil` ist der gezeichnete Teil des Kreisrings: 1,0 = Vollkreis,
    0,5 = Halbschablone, 0,25 = Viertelschablone. Das Buch weist ausdruecklich
    darauf hin, dass Halb- und Viertelkreis nur die **Schablonenaufteilung**
    beim Zuschnitt bezeichnen; das fertige Kleidungsstueck muss immer einen
    vollstaendigen Kreisring bilden.
    """
    rTaW = (TaW_cm + 2.0 * NZg_cm) / (2.0 * pi)
    rSaW = rTaW + MoL_cm
    SaW = 2.0 * pi * rSaW
    bis = 360.0 * anteil
    return Glockenrock(
        rTaW_cm=rTaW,
        rSaW_cm=rSaW,
        SaW_cm=SaW,
        taillenkreis=kreisbogen((0.0, 0.0), cm(rTaW), 0.0, bis),
        saumkreis=kreisbogen((0.0, 0.0), cm(rSaW), 0.0, bis),
    )
