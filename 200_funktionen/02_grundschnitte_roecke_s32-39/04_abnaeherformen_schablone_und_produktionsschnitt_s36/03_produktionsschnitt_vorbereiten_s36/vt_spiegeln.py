"""Spiegelt ausdrücklich gewählte VT-Punkte an der vM nach S. 36, Bild 2.

Reine Punktgeometrie in mm, X nach rechts, Y nach unten.
Kein Konturzusammenbau, keine Nahtzugaben und keine Markierungsautomatik.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


CONTRACT_VERSION = "1.0.0"


class GeometrieVertragError(ValueError):
    """Geometrie oder Toleranz ist leer, entartet oder nicht endlich."""


@dataclass(frozen=True)
class Punkt2D:
    x_mm: float
    y_mm: float


@dataclass(frozen=True)
class VtSpiegelung:
    original: tuple[Punkt2D, ...]
    gespiegelt: tuple[Punkt2D, ...]
    vm_oben: Punkt2D
    vm_unten: Punkt2D
    achsen_nulltoleranz_mm: float
    quellseite: int = 36
    bildnummer: int = 2


def vt_punkte_spiegeln(
    *,
    punkte: tuple[Punkt2D, ...],
    vm_oben: Punkt2D,
    vm_unten: Punkt2D,
    achsen_nulltoleranz_mm: float,
) -> VtSpiegelung:
    """Original und Spiegelpunkte in gleicher Reihenfolge zurückgeben.

    Die vM wird als unendliche Gerade durch zwei explizite Punkte übergeben.
    Der Aufrufer wählt die zu spiegelnde Geometrie; RV-Markierungen oder
    andere asymmetrische Produktionsangaben gehören nicht automatisch dazu.
    """
    if not math.isfinite(achsen_nulltoleranz_mm) or achsen_nulltoleranz_mm < 0:
        raise GeometrieVertragError("Achsen-Nulltoleranz muss endlich und >= 0 mm sein")
    original = tuple(Punkt2D(p.x_mm, p.y_mm) for p in punkte)
    if not original:
        raise GeometrieVertragError("Mindestens ein ausdrücklich gewählter Punkt nötig")
    for p in (*original, vm_oben, vm_unten):
        if not math.isfinite(p.x_mm) or not math.isfinite(p.y_mm):
            raise GeometrieVertragError("Punktkoordinaten müssen endlich sein")
    dx = vm_unten.x_mm - vm_oben.x_mm
    dy = vm_unten.y_mm - vm_oben.y_mm
    laenge = math.hypot(dx, dy)
    if not math.isfinite(laenge) or laenge <= achsen_nulltoleranz_mm:
        raise GeometrieVertragError("vM-Achse ist entartet oder numerisch nicht darstellbar")
    ux, uy = dx / laenge, dy / laenge
    gespiegelt = []
    for p in original:
        px, py = p.x_mm - vm_oben.x_mm, p.y_mm - vm_oben.y_mm
        # P' = P - 2 * dot(P-A, n) * n, mit Einheitsnormaler n=(-uy, ux).
        # Algebraisch identisch zu P'=2H-P aus dem Transformationsvertrag.
        lotabstand = px * (-uy) + py * ux
        spiegelpunkt = Punkt2D(
            p.x_mm + 2.0 * lotabstand * uy,
            p.y_mm - 2.0 * lotabstand * ux,
        )
        if not all(math.isfinite(wert) for wert in (
            px, py, lotabstand, spiegelpunkt.x_mm, spiegelpunkt.y_mm,
        )):
            raise GeometrieVertragError("Spiegelung ist numerisch nicht darstellbar")
        gespiegelt.append(spiegelpunkt)
    return VtSpiegelung(
        original, tuple(gespiegelt), vm_oben, vm_unten,
        achsen_nulltoleranz_mm,
    )
