"""Abnaeher und erhoehte Naehte - Bausteine, die Rock und Oberteil teilen.

Diese Datei kennt keinen Kleidnamen und keine Buchseite. Sie beschreibt nur,
was ein **Abnaeher** geometrisch ist und wie eine **erhoehte Taillenlinie**
zwischen ihren Stuetzwerten verlaeuft.

Warum hier und nicht in `geometrie/`: ein Abnaeher ist bereits Fachwissen. Er
gehoert nicht in die modeblinde Ebene. Warum nicht im Oberteil oder im Rock:
beide brauchen ihn, also besitzt ihn keiner von beiden.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Sequence, Tuple

from geometrie import Punkt, schnitt_mit_senkrechter


def weich(t: float) -> float:
    """Smoothstep - weicher Uebergang zwischen 0 und 1."""
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)


def erhoehung(x: float, stuetzen: Sequence[Tuple[float, float]]) -> float:
    """Erhoehungsbetrag an der Stelle x, weich zwischen den Stuetzwerten."""
    st = sorted(stuetzen)
    if x <= st[0][0]:
        return st[0][1]
    if x >= st[-1][0]:
        return st[-1][1]
    for (x0, h0), (x1, h1) in zip(st, st[1:]):
        if x0 <= x <= x1:
            return h0 + (h1 - h0) * weich((x - x0) / (x1 - x0))
    return st[-1][1]


def erhoehte_naht(x_von: float, x_bis: float, y_basis: float,
                  stuetzen: Sequence[Tuple[float, float]],
                  schritte: int = 48) -> List[Punkt]:
    """Erhoehte Taillenlinie als Polylinie, in x aufsteigend oder absteigend."""
    punkte: List[Punkt] = []
    for i in range(schritte + 1):
        x = x_von + (x_bis - x_von) * i / schritte
        punkte.append((x, y_basis - erhoehung(x, stuetzen)))
    return punkte


def auf_linie(linie: Sequence[Punkt], x: float) -> Punkt:
    """Punkt einer in x monotonen Polylinie bei gegebenem x."""
    for a, b in zip(linie, linie[1:]):
        if (a[0] - x) * (b[0] - x) <= 0 and abs(b[0] - a[0]) > 1e-12:
            return schnitt_mit_senkrechter(a, b, x)
    return min(linie, key=lambda p: abs(p[0] - x))


@dataclass
class Abnaeher:
    """Ein Abnaeher: zwei Schenkel und eine Spitze.

    `schenkel_a` liegt immer beim kleineren x. `inhalt_cm` ist der
    Abnaeherinhalt, wie ihn die Konstruktionstabelle nennt.
    """

    name: str
    schenkel_a: Punkt
    spitze: Punkt
    schenkel_b: Punkt
    inhalt_cm: float

    def linien(self) -> List[List[Punkt]]:
        return [[self.schenkel_a, self.spitze], [self.spitze, self.schenkel_b]]


def mit_abnaehern(linie: Sequence[Punkt], abnaeher: Sequence[Abnaeher]) -> List[Punkt]:
    """Setzt Abnaeher in eine in x aufsteigende Naht ein.

    Der Bereich zwischen den Schenkeln wird durch Schenkel - Spitze - Schenkel
    ersetzt. Das Ergebnis ist die Naht, wie sie spaeter genaeht wird.
    """
    sortiert = sorted(abnaeher, key=lambda a: a.schenkel_a[0])
    ergebnis: List[Punkt] = []
    grenze = -1e18
    for a in sortiert:
        ergebnis += [p for p in linie if grenze < p[0] < a.schenkel_a[0]]
        ergebnis += [a.schenkel_a, a.spitze, a.schenkel_b]
        grenze = a.schenkel_b[0]
    ergebnis += [p for p in linie if p[0] > grenze]
    return ergebnis
