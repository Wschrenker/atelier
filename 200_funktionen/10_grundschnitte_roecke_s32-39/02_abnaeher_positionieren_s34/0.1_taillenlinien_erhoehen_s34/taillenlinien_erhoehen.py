"""Kleine reine Geometrie fuer die erhoehten Taillenlinien auf S. 34."""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum


CONTRACT_VERSION = "1.0.0"
NULLVEKTOR_ABS_TOL_MM = 1e-9
RECHTWINKEL_ABS_TOL = 1e-12


class Taillenlinienstatus(str, Enum):
    VOLLSTAENDIG = "vollstaendig"


class GeometrieVertragError(ValueError):
    """Die Eingangsgeometrie ist nicht endlich, entartet oder nicht rechtwinklig."""


class WertAusserhalbBereichError(ValueError):
    """Eine Fachentscheidung liegt ausserhalb des auf S. 34 belegten Bereichs."""

    def __init__(
        self, wert_name: str, wert_mm: float, minimum_mm: float, maximum_mm: float
    ) -> None:
        self.wert_name = wert_name
        self.wert_mm = wert_mm
        self.minimum_mm = minimum_mm
        self.maximum_mm = maximum_mm
        super().__init__(
            f"{wert_name}={wert_mm!r} mm liegt nicht im Bereich "
            f"{minimum_mm}-{maximum_mm} mm"
        )


class NichtEndlicherBerechnungswertError(ArithmeticError):
    """Eine abgeleitete Koordinate oder Laenge ist nicht endlich."""


@dataclass(frozen=True)
class Punkt2D:
    x_mm: float
    y_mm: float


@dataclass(frozen=True)
class Provenienz:
    source_page: int
    source_statement: str
    formula_ids: tuple[str, ...]
    math_contracts: tuple[str, ...]
    input_names: tuple[str, ...]
    selected_options: tuple[tuple[str, float], ...]
    contract_version: str


@dataclass(frozen=True)
class ErhoehteTaillenlinien:
    p10: Punkt2D
    erhoehungsrichtung: tuple[float, float]
    taillenrichtung: tuple[float, float]
    taillenerhoehung_seitenlinie_mm: float
    taillenerhoehung_vorderer_abnaeher_mm: float
    taillenerhoehung_hinterer_abnaeher_mm: float
    status: Taillenlinienstatus
    provenienz: Provenienz


def _pruefe_punkte(*punkte: Punkt2D) -> None:
    if any(
        not math.isfinite(punkt.x_mm) or not math.isfinite(punkt.y_mm)
        for punkt in punkte
    ):
        raise GeometrieVertragError("Alle Punktkoordinaten muessen endlich sein")


def _normierter_vektor(a: Punkt2D, b: Punkt2D) -> tuple[float, float]:
    _pruefe_punkte(a, b)
    dx_mm = b.x_mm - a.x_mm
    dy_mm = b.y_mm - a.y_mm
    if not math.isfinite(dx_mm) or not math.isfinite(dy_mm):
        raise GeometrieVertragError("Punktdifferenz ist nicht endlich")
    laenge_mm = math.hypot(dx_mm, dy_mm)
    if not math.isfinite(laenge_mm) or laenge_mm <= NULLVEKTOR_ABS_TOL_MM:
        raise GeometrieVertragError("Richtungsvektor ist entartet")
    return dx_mm / laenge_mm, dy_mm / laenge_mm


def _pruefe_bereich(
    wert_name: str, wert_mm: float, minimum_mm: float, maximum_mm: float
) -> None:
    if not math.isfinite(wert_mm) or not minimum_mm <= wert_mm <= maximum_mm:
        raise WertAusserhalbBereichError(
            wert_name, wert_mm, minimum_mm, maximum_mm
        )


def taillenlinien_erhoehen(
    *,
    p7: Punkt2D,
    p8: Punkt2D,
    taillenlinie_start: Punkt2D,
    taillenlinie_ende: Punkt2D,
    taillenerhoehung_seitenlinie_mm: float,
    taillenerhoehung_vorderer_abnaeher_mm: float,
) -> ErhoehteTaillenlinien:
    """Setzt P10 und die drei belegten Erhoehungen ohne Rundung fest."""

    _pruefe_bereich(
        "taillenerhoehung_seitenlinie_mm",
        taillenerhoehung_seitenlinie_mm,
        10.0,
        15.0,
    )
    _pruefe_bereich(
        "taillenerhoehung_vorderer_abnaeher_mm",
        taillenerhoehung_vorderer_abnaeher_mm,
        5.0,
        7.0,
    )
    seitenrichtung = _normierter_vektor(p7, p8)
    taillenrichtung = _normierter_vektor(taillenlinie_start, taillenlinie_ende)
    skalarprodukt = (
        seitenrichtung[0] * taillenrichtung[0]
        + seitenrichtung[1] * taillenrichtung[1]
    )
    if not math.isclose(
        skalarprodukt, 0.0, abs_tol=RECHTWINKEL_ABS_TOL, rel_tol=0.0
    ):
        raise GeometrieVertragError(
            "Seitenlinie und Taillenlinie muessen rechtwinklig sein"
        )

    erhoehungsrichtung = (-seitenrichtung[0], -seitenrichtung[1])
    p10 = Punkt2D(
        p7.x_mm + erhoehungsrichtung[0] * taillenerhoehung_seitenlinie_mm,
        p7.y_mm + erhoehungsrichtung[1] * taillenerhoehung_seitenlinie_mm,
    )
    _pruefe_punkte(p10)
    taillenerhoehung_hinterer_abnaeher_mm = (
        taillenerhoehung_seitenlinie_mm / 3.0
    )
    if not math.isfinite(taillenerhoehung_hinterer_abnaeher_mm):
        raise NichtEndlicherBerechnungswertError(
            "Hintere Taillenerhoehung ist nicht endlich"
        )

    return ErhoehteTaillenlinien(
        p10=p10,
        erhoehungsrichtung=erhoehungsrichtung,
        taillenrichtung=taillenrichtung,
        taillenerhoehung_seitenlinie_mm=taillenerhoehung_seitenlinie_mm,
        taillenerhoehung_vorderer_abnaeher_mm=(
            taillenerhoehung_vorderer_abnaeher_mm
        ),
        taillenerhoehung_hinterer_abnaeher_mm=(
            taillenerhoehung_hinterer_abnaeher_mm
        ),
        status=Taillenlinienstatus.VOLLSTAENDIG,
        provenienz=Provenienz(
            source_page=34,
            source_statement="Erhoehte Taillenlinien, Schritte 10-12",
            formula_ids=("HOF-B1-S034-F02",),
            math_contracts=(
                "400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md",
                "400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md",
                "400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md",
            ),
            input_names=(
                "p7",
                "p8",
                "taillenlinie_start",
                "taillenlinie_ende",
            ),
            selected_options=(
                (
                    "taillenerhoehung_seitenlinie_mm",
                    taillenerhoehung_seitenlinie_mm,
                ),
                (
                    "taillenerhoehung_vorderer_abnaeher_mm",
                    taillenerhoehung_vorderer_abnaeher_mm,
                ),
            ),
            contract_version=CONTRACT_VERSION,
        ),
    )
