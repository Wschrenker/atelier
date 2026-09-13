"""Einstellbare Arbeitskurven. Eigene Modellentscheidung, keine Hofenbitzer-Formel.

Millimeter, X rechts, Y unten. Taillenabschnitte laufen von links nach rechts.
Die Kurven verändern ihre Anker nicht; Nahtpassung/Abnäherausgleich bleibt separat.
"""
from dataclasses import dataclass
import math


class KurvenVertragError(ValueError):
    """Ungültige oder numerisch nicht berechenbare Arbeitskurve."""


def _endlich(*werte):
    if not all(math.isfinite(w) for w in werte):
        raise KurvenVertragError("Werte und Zwischenwerte müssen endlich sein")


def _punkte(*punkte):
    for p in punkte:
        _endlich(p.x_mm, p.y_mm)


@dataclass(frozen=True)
class Punkt:
    x_mm: float
    y_mm: float


@dataclass(frozen=True)
class Kubisch:
    p0: Punkt
    p1: Punkt
    p2: Punkt
    p3: Punkt


@dataclass(frozen=True)
class Messung:
    punkte: tuple[Punkt, ...]
    untergrenze_mm: float
    obergrenze_mm: float


def messen(k: Kubisch, *, fehler_mm: float) -> Messung:
    """Adaptive Teilung: Sehnensumme <= Länge <= Kontrollpolygonsumme.

    Intervallbreite und Kontrollpunktabstand zur Teilsehne <= fehler_mm.
    Technische Genauigkeit, keine fachliche Nahttoleranz; IEEE-Rundung bleibt.
    """
    _endlich(fehler_mm)
    _punkte(k.p0,k.p1,k.p2,k.p3)
    if fehler_mm <= 0:
        raise KurvenVertragError("Messfehler muss positiv sein")

    def dist(a,b):
        d = math.hypot(b.x_mm-a.x_mm,b.y_mm-a.y_mm)
        _endlich(d)
        return d

    def mid(a,b):
        return Punkt(a.x_mm/2+b.x_mm/2,a.y_mm/2+b.y_mm/2)

    def teil(c,budget,tiefe):
        a,b,d,e = c.p0,c.p1,c.p2,c.p3
        unten = dist(a,e)
        oben = dist(a,b)+dist(b,d)+dist(d,e)
        _endlich(oben)
        def abstand(p):
            if unten == 0:
                return dist(a,p)
            ux,uy = (e.x_mm-a.x_mm)/unten,(e.y_mm-a.y_mm)/unten
            s = (p.x_mm-a.x_mm)*ux+(p.y_mm-a.y_mm)*uy
            _endlich(s)
            s = min(unten,max(0,s))
            return dist(p,Punkt(a.x_mm+s*ux,a.y_mm+s*uy))
        if oben-unten <= budget and max(abstand(b),abstand(d)) <= fehler_mm:
            return Messung((a,e),unten,max(unten,oben))
        if tiefe >= 24:
            raise KurvenVertragError("Messgenauigkeit nicht innerhalb Teilungsgrenze erreicht")
        ab,bd,de = mid(a,b),mid(b,d),mid(d,e)
        l,r = mid(ab,bd),mid(bd,de)
        m = mid(l,r)
        links = teil(Kubisch(a,ab,l,m),budget/2,tiefe+1)
        rechts = teil(Kubisch(m,r,de,e),budget/2,tiefe+1)
        return Messung(links.punkte+rechts.punkte[1:],
                       links.untergrenze_mm+rechts.untergrenze_mm,
                       links.obergrenze_mm+rechts.obergrenze_mm)
    return teil(k,fehler_mm,0)


def auswerten(k: Kubisch, t: float) -> Punkt:
    """Kubische Bézierkurve mit de Casteljau auswerten."""
    _endlich(t)
    _punkte(k.p0, k.p1, k.p2, k.p3)
    if not 0 <= t <= 1:
        raise KurvenVertragError("t muss in [0,1] liegen")
    punkte = [k.p0, k.p1, k.p2, k.p3]
    while len(punkte) > 1:
        punkte = [Punkt((1-t)*a.x_mm+t*b.x_mm, (1-t)*a.y_mm+t*b.y_mm)
                  for a, b in zip(punkte, punkte[1:])]
    _punkte(punkte[0])
    return punkte[0]


def hueftbogen(a: Punkt, b: Punkt, *, form: float) -> Kubisch:
    """Monotone Kubik mit senkrechter Endtangente an der Hüftlinie."""
    _punkte(a, b)
    dy, dx = b.y_mm-a.y_mm, b.x_mm-a.x_mm
    _endlich(dy, dx, form)
    if dy <= 1e-9 or dx < 0 or not 0 < form <= 0.5:
        raise KurvenVertragError("Hüftbogen verlangt Y-Zuwachs, X>=Start, 0<form<=0.5")
    k = Kubisch(a, Punkt(b.x_mm, a.y_mm+dy*form),
                Punkt(b.x_mm, b.y_mm-dy*form), b)
    _punkte(k.p1, k.p2)
    return k


def taillenbogen(a: Punkt, b: Punkt, *, durchhang_mm: float) -> tuple[Kubisch, Kubisch]:
    """Zwei C1-verbundene Kubiken; Durchhang am X-Mittelpunkt gegen die Sehne.

    Waagrechte Endtangenten sind unsere digitale Wahl, kein Buchgebot.
    """
    _punkte(a, b)
    dx, dy = b.x_mm-a.x_mm, b.y_mm-a.y_mm
    _endlich(dx, dy, durchhang_mm)
    if dx <= 1e-9 or durchhang_mm < 0:
        raise KurvenVertragError("Taillenbogen verlangt X-Zuwachs und Durchhang>=0")
    m = Punkt(a.x_mm/2+b.x_mm/2, a.y_mm/2+b.y_mm/2+durchhang_mm)
    ergebnis = (
        Kubisch(a, Punkt(a.x_mm+dx/6, a.y_mm),
                Punkt(m.x_mm-dx/6, m.y_mm-dy/6), m),
        Kubisch(m, Punkt(m.x_mm+dx/6, m.y_mm+dy/6),
                Punkt(b.x_mm-dx/6, b.y_mm), b),
    )
    for k in ergebnis:
        _punkte(k.p0, k.p1, k.p2, k.p3)
    return ergebnis
