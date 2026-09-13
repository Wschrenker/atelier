"""Kleine, reine Referenzgeometrie fuer den geraden Rock auf S. 33."""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum


RICHTUNGS_KREUZPRODUKT_ABS_TOL = 1e-12
RICHTUNGS_SKALARPRODUKT_ABS_TOL = 1e-12
GERADENSCHNITT_PARALLEL_ABS_TOL = 1e-12
RICHTUNGSVEKTOR_NULL_ABS_TOL_MM = 1e-9
CONTRACT_VERSION = "1.0.0"


class Geometriestatus(str, Enum):
    VOLLSTAENDIG = "vollstaendig"


class KeinEindeutigerGeradenschnittError(ValueError):
    """Die beiden Geraden besitzen keinen eindeutig berechenbaren Schnitt."""


class EntarteteGeradeError(ValueError):
    """Mindestens eine Gerade besitzt keinen Richtungsvektor."""


class NichtEndlicherPunktError(ValueError):
    """Mindestens eine Punktkoordinate ist nicht endlich."""


class NichtEndlicherGeometrieZwischenwertError(ArithmeticError):
    """Eine Geometrieoperation erzeugte einen nicht endlichen Zwischenwert."""


class UngueltigerGeometriewertError(ValueError):
    """Ein Grundgeruestmass ist nicht endlich oder nicht positiv."""

    def __init__(self, wert_name: str, wert_mm: float) -> None:
        self.wert_name = wert_name
        self.wert_mm = wert_mm
        super().__init__(f"{wert_name}={wert_mm!r} mm ist kein gueltiges Grundgeruestmass")


class UngueltigeGrundgeruestProportionError(ValueError):
    """Die Hüftlinie läge unterhalb des Saums."""


@dataclass(frozen=True)
class Punkt2D:
    x_mm: float
    y_mm: float


def _pruefe_punkte(*punkte: Punkt2D) -> None:
    for punkt in punkte:
        if not math.isfinite(punkt.x_mm) or not math.isfinite(punkt.y_mm):
            raise NichtEndlicherPunktError(f"Nicht endlicher Punkt: {punkt!r}")


def _differenzvektor(a: Punkt2D, b: Punkt2D) -> tuple[float, float]:
    _pruefe_punkte(a, b)
    x_mm = b.x_mm - a.x_mm
    y_mm = b.y_mm - a.y_mm
    if not math.isfinite(x_mm) or not math.isfinite(y_mm):
        raise NichtEndlicherGeometrieZwischenwertError(
            "Punktdifferenz ist nicht endlich"
        )
    return x_mm, y_mm


def _richtungsvektor(a: Punkt2D, b: Punkt2D) -> tuple[float, float]:
    x_mm, y_mm = _differenzvektor(a, b)
    if math.hypot(x_mm, y_mm) <= RICHTUNGSVEKTOR_NULL_ABS_TOL_MM:
        raise EntarteteGeradeError("Geradenpunkte sind identisch")
    return x_mm, y_mm


def _normierter_richtungsvektor(a: Punkt2D, b: Punkt2D) -> tuple[float, float]:
    x_mm, y_mm = _richtungsvektor(a, b)
    skala_mm = max(abs(x_mm), abs(y_mm))
    return x_mm / skala_mm, y_mm / skala_mm


def mittelpunkt(a: Punkt2D, b: Punkt2D) -> Punkt2D:
    """Liefert den echten Mittelpunkt der Strecke a-b."""

    _pruefe_punkte(a, b)
    return Punkt2D(
        x_mm=a.x_mm / 2.0 + b.x_mm / 2.0,
        y_mm=a.y_mm / 2.0 + b.y_mm / 2.0,
    )


def geradenschnitt(a: Punkt2D, b: Punkt2D, c: Punkt2D, d: Punkt2D) -> Punkt2D:
    """Liefert den eindeutigen Schnitt der unendlichen Geraden a-b und c-d."""

    r_x, r_y = _normierter_richtungsvektor(a, b)
    s_x, s_y = _normierter_richtungsvektor(c, d)
    divisor = r_x * s_y - r_y * s_x
    if math.isclose(
        divisor,
        0.0,
        abs_tol=GERADENSCHNITT_PARALLEL_ABS_TOL,
        rel_tol=0.0,
    ):
        raise KeinEindeutigerGeradenschnittError(
            "Geraden sind parallel oder identisch"
        )
    ac_x, ac_y = _differenzvektor(a, c)
    zaehler = ac_x * s_y - ac_y * s_x
    if not math.isfinite(zaehler):
        raise NichtEndlicherGeometrieZwischenwertError(
            "Geradenschnittzaehler ist nicht endlich"
        )
    t_mm = zaehler / divisor
    if not math.isfinite(t_mm):
        raise NichtEndlicherGeometrieZwischenwertError(
            "Geradenschnittparameter ist nicht endlich"
        )
    schnittpunkt = Punkt2D(a.x_mm + t_mm * r_x, a.y_mm + t_mm * r_y)
    _pruefe_punkte(schnittpunkt)
    return schnittpunkt


def sind_parallel(a: Punkt2D, b: Punkt2D, c: Punkt2D, d: Punkt2D) -> bool:
    """Prueft zwei Geraden ueber das Kreuzprodukt ihrer Richtungen."""

    ab_x, ab_y = _normierter_richtungsvektor(a, b)
    cd_x, cd_y = _normierter_richtungsvektor(c, d)
    return math.isclose(
        ab_x * cd_y - ab_y * cd_x,
        0.0,
        abs_tol=RICHTUNGS_KREUZPRODUKT_ABS_TOL,
        rel_tol=0.0,
    )


def stehen_rechtwinklig(a: Punkt2D, b: Punkt2D, c: Punkt2D, d: Punkt2D) -> bool:
    """Prueft zwei Geraden ueber das Skalarprodukt ihrer Richtungen."""

    ab_x, ab_y = _normierter_richtungsvektor(a, b)
    cd_x, cd_y = _normierter_richtungsvektor(c, d)
    return math.isclose(
        ab_x * cd_x + ab_y * cd_y,
        0.0,
        abs_tol=RICHTUNGS_SKALARPRODUKT_ABS_TOL,
        rel_tol=0.0,
    )


def punkt_liegt_auf_gerade(p: Punkt2D, a: Punkt2D, b: Punkt2D) -> bool:
    """Prueft ueber das Kreuzprodukt, ob p auf der Geraden a-b liegt."""

    _pruefe_punkte(p)
    ab_x, ab_y = _normierter_richtungsvektor(a, b)
    ap_x, ap_y = _differenzvektor(a, p)
    return math.isclose(
        ab_x * ap_y - ab_y * ap_x,
        0.0,
        abs_tol=RICHTUNGSVEKTOR_NULL_ABS_TOL_MM,
        rel_tol=0.0,
    )


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
class Grundgeruest:
    p1: Punkt2D
    p2: Punkt2D
    p3: Punkt2D
    p4: Punkt2D
    p5: Punkt2D
    p6: Punkt2D
    p7: Punkt2D
    p8: Punkt2D
    p9: Punkt2D
    geometriestatus: Geometriestatus
    provenienz: Provenienz

    def punkt(self, name: str) -> Punkt2D:
        """Gibt einen Buchpunkt ueber seine Beschriftung zurueck."""

        return {
            "P1": self.p1,
            "P2": self.p2,
            "P3": self.p3,
            "P4": self.p4,
            "P5": self.p5,
            "P6": self.p6,
            "P7": self.p7,
            "P8": self.p8,
            "P9": self.p9,
        }[name]


def grundgeruest_zeichnen(
    *,
    modelllaenge_mm: float,
    huefttiefe_mm: float,
    halbe_hueftweite_mm: float,
) -> Grundgeruest:
    """Setzt P1-P6 in Engine-Koordinaten, X rechts und Y unten."""

    for wert_name, wert_mm, minimum_exklusiv_mm in (
        (
            "modelllaenge_mm",
            modelllaenge_mm,
            RICHTUNGSVEKTOR_NULL_ABS_TOL_MM,
        ),
        ("huefttiefe_mm", huefttiefe_mm, 0.0),
        (
            "halbe_hueftweite_mm",
            halbe_hueftweite_mm,
            RICHTUNGSVEKTOR_NULL_ABS_TOL_MM,
        ),
    ):
        if not math.isfinite(wert_mm) or wert_mm <= minimum_exklusiv_mm:
            raise UngueltigerGeometriewertError(wert_name, wert_mm)
    if huefttiefe_mm > modelllaenge_mm:
        raise UngueltigeGrundgeruestProportionError(
            "huefttiefe_mm darf modelllaenge_mm nicht überschreiten"
        )

    p1 = Punkt2D(0.0, 0.0)
    p2 = Punkt2D(0.0, modelllaenge_mm)
    p3 = Punkt2D(0.0, huefttiefe_mm)
    p4 = Punkt2D(halbe_hueftweite_mm, 0.0)
    p5 = Punkt2D(halbe_hueftweite_mm, modelllaenge_mm)
    p6 = Punkt2D(halbe_hueftweite_mm, huefttiefe_mm)
    p7 = mittelpunkt(p1, p4)
    p8 = mittelpunkt(p2, p5)
    p9 = geradenschnitt(p7, p8, p3, p6)
    provenienz = Provenienz(
        source_page=33,
        source_statement="Grundgeruest P1-P9, Schritte 1-9",
        formula_ids=("HOF-B1-S033-F03",),
        math_contracts=(
            "400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md",
            "400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md",
            "400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md",
        ),
        input_names=("modelllaenge_mm", "huefttiefe_mm", "halbe_hueftweite_mm"),
        selected_options=(),
        contract_version=CONTRACT_VERSION,
    )
    return Grundgeruest(
        p1=p1,
        p2=p2,
        p3=p3,
        p4=p4,
        p5=p5,
        p6=p6,
        p7=p7,
        p8=p8,
        p9=p9,
        geometriestatus=Geometriestatus.VOLLSTAENDIG,
        provenienz=provenienz,
    )
