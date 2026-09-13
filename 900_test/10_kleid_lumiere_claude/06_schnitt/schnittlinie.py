"""Eine gerade Schnittlinie durch ein Schnittteil legen.

Modellentwicklung besteht zu einem grossen Teil daraus, an einer Linie etwas
wegzunehmen: ein Ausschnitt, eine Passe, ein Wickelteil. Diese Datei kann genau
das - mehr nicht.
"""

from __future__ import annotations

from typing import List, Sequence

from geometrie import Punkt


def _seite(a: Punkt, b: Punkt, p: Punkt) -> float:
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def _schnitt(a: Punkt, b: Punkt, p: Punkt, q: Punkt) -> Punkt:
    sp = _seite(a, b, p)
    sq = _seite(a, b, q)
    t = sp / (sp - sq)
    return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))


def schneide_halbebene(kontur: Sequence[Punkt], a: Punkt, b: Punkt,
                       behalte_positiv: bool = True) -> List[Punkt]:
    """Beschneidet eine geschlossene Kontur an der Geraden a-b.

    `behalte_positiv` waehlt die Seite: positiv ist die Seite, auf der das
    Kreuzprodukt (b-a) x (p-a) positiv ist - bei Y nach unten also die Seite
    **rechts** der Laufrichtung a -> b.
    """
    if len(kontur) < 3:
        return list(kontur)
    vorzeichen = 1.0 if behalte_positiv else -1.0
    ergebnis: List[Punkt] = []
    n = len(kontur)
    for i in range(n):
        p = kontur[i]
        q = kontur[(i + 1) % n]
        sp = _seite(a, b, p) * vorzeichen
        sq = _seite(a, b, q) * vorzeichen
        if sp >= 0:
            ergebnis.append(p)
        if (sp > 0 > sq) or (sp < 0 < sq):
            ergebnis.append(_schnitt(a, b, p, q))
    return ergebnis
