"""Geometrie-Primitive - modeblind.

Konventionen (aus `500_python/AGENT.md`):

* Einheit intern **Millimeter**. `cm()` rechnet am Eintritt um.
* Die **Y-Achse zeigt nach unten**. Ein positiver Drehwinkel dreht deshalb
  auf dem Bildschirm im Uhrzeigersinn.
* Reine Funktionen: keine Datei, kein Zufall, kein globaler Zustand.

Diese Datei kennt keine Buchseite und keinen Fachbegriff. Sie setzt die
Primitive B1 bis B9 der Roadmap um:

| Primitive | Funktion hier |
|---|---|
| B1 Kreis um Mittelpunkt mit Radius | `kreisbogen` |
| B2 Lot / rechter Winkel durch Punkt | `normale` |
| B3 Kreisbogen-Segment | `kreisbogen` |
| B4 Drehen um Punkt | `drehe`, `drehe_alle` |
| B5 Spiegeln an Achse | `spiegle_senkrecht`, `spiegle_alle` |
| B6 Kurve durch gegebene Punkte | `bezier3` |
| B7 Parallelversatz | bewusst noch nicht enthalten (erst mit Nahtzugaben) |
| B8 Schnittpunkt Linie/Linie | `schnitt_gerade_gerade` und die beiden Achsenfaelle |
| B9 Laenge entlang Kurve | `polylinie_laenge` |
"""

from __future__ import annotations

import math
from typing import Iterable, List, Sequence, Tuple

Punkt = Tuple[float, float]


# ---------------------------------------------------------------- Einheiten

def cm(wert: float) -> float:
    """Zentimeter aus dem Buch in Millimeter der Rechnung."""
    return wert * 10.0


def mm_zu_cm(wert: float) -> float:
    """Millimeter der Rechnung zurueck in Zentimeter fuer die Anzeige."""
    return wert / 10.0


# ------------------------------------------------------------------ Vektor

def add(a: Punkt, b: Punkt) -> Punkt:
    return (a[0] + b[0], a[1] + b[1])


def sub(a: Punkt, b: Punkt) -> Punkt:
    return (a[0] - b[0], a[1] - b[1])


def skal(a: Punkt, faktor: float) -> Punkt:
    return (a[0] * faktor, a[1] * faktor)


def laenge(a: Punkt) -> float:
    return math.hypot(a[0], a[1])


def abstand(a: Punkt, b: Punkt) -> float:
    return math.hypot(b[0] - a[0], b[1] - a[1])


def einheit(a: Punkt) -> Punkt:
    betrag = laenge(a)
    if betrag == 0.0:
        raise ValueError("Nullvektor hat keine Richtung")
    return (a[0] / betrag, a[1] / betrag)


def normale(richtung: Punkt) -> Punkt:
    """B2 - Lot. Um 90 Grad gedrehter Einheitsvektor."""
    e = einheit(richtung)
    return (-e[1], e[0])


# ------------------------------------------------------------- Bewegungen

def drehe(punkt: Punkt, zentrum: Punkt, winkel_rad: float) -> Punkt:
    """B4 - Drehen um einen Punkt."""
    dx = punkt[0] - zentrum[0]
    dy = punkt[1] - zentrum[1]
    c = math.cos(winkel_rad)
    s = math.sin(winkel_rad)
    return (zentrum[0] + dx * c - dy * s, zentrum[1] + dx * s + dy * c)


def spiegle_senkrecht(punkt: Punkt, x_achse: float) -> Punkt:
    """B5 - Spiegeln an einer senkrechten Achse (z.B. an der vM)."""
    return (2.0 * x_achse - punkt[0], punkt[1])


def winkel_grad(grad: float) -> float:
    return math.radians(grad)


def richtung_grad(grad: float) -> Punkt:
    """Einheitsvektor. 0 Grad = nach rechts, positive Grad = nach unten."""
    r = math.radians(grad)
    return (math.cos(r), math.sin(r))


def punkt_in_richtung(start: Punkt, richtung: Punkt, strecke: float) -> Punkt:
    e = einheit(richtung)
    return (start[0] + e[0] * strecke, start[1] + e[1] * strecke)


# ---------------------------------------------------------------- Kurven

def bezier3(p0: Punkt, p1: Punkt, p2: Punkt, p3: Punkt, teile: int = 24) -> List[Punkt]:
    """B6 - kubische Bezierkurve, als Polylinie ausgegeben."""
    punkte: List[Punkt] = []
    for i in range(teile + 1):
        t = i / teile
        u = 1.0 - t
        x = (u * u * u * p0[0] + 3 * u * u * t * p1[0]
             + 3 * u * t * t * p2[0] + t * t * t * p3[0])
        y = (u * u * u * p0[1] + 3 * u * u * t * p1[1]
             + 3 * u * t * t * p2[1] + t * t * t * p3[1])
        punkte.append((x, y))
    return punkte


def kurve_durch(start: Punkt, start_richtung: Punkt, start_griff: float,
                ende: Punkt, ende_richtung: Punkt, ende_griff: float,
                teile: int = 24) -> List[Punkt]:
    """Kurve, die `start` und `ende` mit vorgegebenen Tangenten verbindet.

    `start_richtung` zeigt aus dem Startpunkt in die Kurve hinein,
    `ende_richtung` aus dem Endpunkt in die Kurve hinein.
    """
    p1 = punkt_in_richtung(start, start_richtung, start_griff)
    p2 = punkt_in_richtung(ende, ende_richtung, ende_griff)
    return bezier3(start, p1, p2, ende, teile)


def glatte_kurve(stuetzpunkte: Sequence[Punkt], teile_je_abschnitt: int = 12,
                 spannung: float = 0.5) -> List[Punkt]:
    """B6 - eine glatte Kurve **durch** gegebene Stuetzpunkte (Catmull-Rom).

    Anders als `bezier3` liegen die uebergebenen Punkte alle auf der Kurve.
    Genau das braucht eine Armloch- oder Taillenkurve, die durch benannte
    Konstruktionspunkte laufen muss.
    """
    p = list(stuetzpunkte)
    if len(p) < 2:
        return list(p)
    if len(p) == 2:
        return [p[0], p[1]]
    erweitert = [add(p[0], sub(p[0], p[1]))] + p + [add(p[-1], sub(p[-1], p[-2]))]
    ergebnis: List[Punkt] = []
    for i in range(len(p) - 1):
        p0, p1, p2, p3 = erweitert[i], erweitert[i + 1], erweitert[i + 2], erweitert[i + 3]
        c1 = add(p1, skal(sub(p2, p0), spannung / 3.0))
        c2 = sub(p2, skal(sub(p3, p1), spannung / 3.0))
        stueck = bezier3(p1, c1, c2, p2, teile_je_abschnitt)
        ergebnis.extend(stueck if i == 0 else stueck[1:])
    return ergebnis


def kreisbogen(mittelpunkt: Punkt, radius: float,
               von_grad: float, bis_grad: float, teile: int = 64) -> List[Punkt]:
    """B1 + B3 - Kreis beziehungsweise Kreisbogen-Segment."""
    punkte: List[Punkt] = []
    for i in range(teile + 1):
        g = von_grad + (bis_grad - von_grad) * i / teile
        r = math.radians(g)
        punkte.append((mittelpunkt[0] + radius * math.cos(r),
                       mittelpunkt[1] + radius * math.sin(r)))
    return punkte


# ----------------------------------------------------------- Schnittpunkte

def schnitt_gerade_gerade(a1: Punkt, a2: Punkt, b1: Punkt, b2: Punkt) -> Punkt:
    """B8 - Schnittpunkt zweier Geraden (nicht Strecken)."""
    x1, y1 = a1
    x2, y2 = a2
    x3, y3 = b1
    x4, y4 = b2
    nenner = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(nenner) < 1e-12:
        raise ValueError("Geraden sind parallel")
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / nenner
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))


def schnitt_mit_senkrechter(a: Punkt, b: Punkt, x: float) -> Punkt:
    """Schnittpunkt der Geraden a-b mit der Senkrechten bei `x`."""
    if abs(b[0] - a[0]) < 1e-12:
        raise ValueError("Gerade ist selbst senkrecht")
    t = (x - a[0]) / (b[0] - a[0])
    return (x, a[1] + t * (b[1] - a[1]))


def schnitt_mit_waagerechter(a: Punkt, b: Punkt, y: float) -> Punkt:
    """Schnittpunkt der Geraden a-b mit der Waagerechten bei `y`."""
    if abs(b[1] - a[1]) < 1e-12:
        raise ValueError("Gerade ist selbst waagerecht")
    t = (y - a[1]) / (b[1] - a[1])
    return (a[0] + t * (b[0] - a[0]), y)


# -------------------------------------------------------------- Messungen

def polylinie_laenge(punkte: Sequence[Punkt]) -> float:
    """B9 - Laenge entlang einer Kurve."""
    summe = 0.0
    for i in range(len(punkte) - 1):
        summe += abstand(punkte[i], punkte[i + 1])
    return summe


def strecke_teilen(a: Punkt, b: Punkt, anteil: float) -> Punkt:
    return (a[0] + (b[0] - a[0]) * anteil, a[1] + (b[1] - a[1]) * anteil)


def bbox(punkte: Iterable[Punkt]) -> Tuple[float, float, float, float]:
    liste = list(punkte)
    xs = [p[0] for p in liste]
    ys = [p[1] for p in liste]
    return (min(xs), min(ys), max(xs), max(ys))


# ------------------------------------------------------- Sammel-Operationen

def verschiebe_alle(punkte: Sequence[Punkt], dx: float, dy: float) -> List[Punkt]:
    return [(p[0] + dx, p[1] + dy) for p in punkte]


def drehe_alle(punkte: Sequence[Punkt], zentrum: Punkt, winkel_rad: float) -> List[Punkt]:
    return [drehe(p, zentrum, winkel_rad) for p in punkte]


def spiegle_alle(punkte: Sequence[Punkt], x_achse: float) -> List[Punkt]:
    return [spiegle_senkrecht(p, x_achse) for p in punkte]
