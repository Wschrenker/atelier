"""Konstruiert zwei hintere Rockabnäher nach Hofenbitzer Band 1, S. 35."""

from __future__ import annotations

import math
from dataclasses import dataclass


CONTRACT_VERSION = "1.0.0"
KONTROLLSUMMEN_ABS_TOL_MM = 1e-9


class WertAusserhalbBereichError(ValueError):
    """Ein Wert verletzt den auf S. 35 belegten Fachbereich."""


@dataclass(frozen=True)
class Punkt2D:
    x_mm: float
    y_mm: float


@dataclass(frozen=True)
class Abnaeher:
    mitte: Punkt2D
    schenkel_zur_hinteren_mitte: Punkt2D
    schenkel_zur_seitennaht: Punkt2D
    spitze: Punkt2D
    inhalt_mm: float
    laenge_mm: float


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
class ZweiHintereAbnaeher:
    erster_abnaeher: Abnaeher
    zweiter_abnaeher: Abnaeher
    kontrollsumme_mm: float
    verteilung_ist_vollstaendig: bool
    provenienz: Provenienz


def _punkt(
    basis: Punkt2D,
    taillenrichtung: tuple[float, float],
    erhoehungsrichtung: tuple[float, float],
    position_mm: float,
    erhoehung_mm: float,
) -> Punkt2D:
    return Punkt2D(
        basis.x_mm
        + taillenrichtung[0] * position_mm
        + erhoehungsrichtung[0] * erhoehung_mm,
        basis.y_mm
        + taillenrichtung[1] * position_mm
        + erhoehungsrichtung[1] * erhoehung_mm,
    )


def _baue_abnaeher(
    *,
    basis: Punkt2D,
    taillenrichtung: tuple[float, float],
    erhoehungsrichtung: tuple[float, float],
    mitte_position_mm: float,
    erhoehung_mm: float,
    inhalt_mm: float,
    laenge_mm: float,
) -> Abnaeher:
    halber_inhalt_mm = inhalt_mm / 2.0
    mitte = _punkt(
        basis,
        taillenrichtung,
        erhoehungsrichtung,
        mitte_position_mm,
        erhoehung_mm,
    )
    return Abnaeher(
        mitte=mitte,
        schenkel_zur_hinteren_mitte=_punkt(
            basis,
            taillenrichtung,
            erhoehungsrichtung,
            mitte_position_mm - halber_inhalt_mm,
            erhoehung_mm,
        ),
        schenkel_zur_seitennaht=_punkt(
            basis,
            taillenrichtung,
            erhoehungsrichtung,
            mitte_position_mm + halber_inhalt_mm,
            erhoehung_mm,
        ),
        spitze=Punkt2D(
            mitte.x_mm - erhoehungsrichtung[0] * laenge_mm,
            mitte.y_mm - erhoehungsrichtung[1] * laenge_mm,
        ),
        inhalt_mm=inhalt_mm,
        laenge_mm=laenge_mm,
    )


def zwei_hintere_abnaeher_konstruieren(
    *,
    p7: Punkt2D,
    p8: Punkt2D,
    hintere_mitte: Punkt2D,
    hinterer_hueftbogenpunkt: Punkt2D,
    taillenausfall_mm: float,
    hueftabstich_mm: float,
    vorderer_abnaeherinhalt_mm: float,
    hinterer_gesamtinhalt_mm: float,
    inhaltsdifferenz_mm: float,
    positionskorrektur_erster_abnaeher_mm: float,
    taillenerhoehung_seitenlinie_mm: float,
    taillenerhoehung_vorderer_abnaeher_mm: float,
    taillenerhoehung_erster_hinterer_abnaeher_mm: float,
    laenge_erster_hinterer_abnaeher_mm: float,
    laenge_zweiter_hinterer_abnaeher_mm: float,
) -> ZweiHintereAbnaeher:
    """Teilt den hinteren Gesamtinhalt und positioniert beide RT-Abnäher."""

    if not 5.0 <= inhaltsdifferenz_mm <= 10.0:
        raise WertAusserhalbBereichError(
            "Der zweite hintere Abnäher muss 5-10 mm weniger Inhalt haben"
        )
    erster_inhalt_mm = (hinterer_gesamtinhalt_mm + inhaltsdifferenz_mm) / 2.0
    zweiter_inhalt_mm = hinterer_gesamtinhalt_mm - erster_inhalt_mm
    if erster_inhalt_mm > 45.0:
        raise WertAusserhalbBereichError(
            "Der erste hintere Abnäher darf höchstens 45 mm Inhalt haben"
        )
    if zweiter_inhalt_mm <= 0.0:
        raise WertAusserhalbBereichError(
            "Eine Zwei-Abnäher-Konstruktion benötigt zwei positive Inhalte"
        )

    dx = p7.x_mm - hintere_mitte.x_mm
    dy = p7.y_mm - hintere_mitte.y_mm
    rueckteilbreite_mm = math.hypot(dx, dy)
    taillenrichtung = (dx / rueckteilbreite_mm, dy / rueckteilbreite_mm)

    sdx = p8.x_mm - p7.x_mm
    sdy = p8.y_mm - p7.y_mm
    seitenlaenge_mm = math.hypot(sdx, sdy)
    erhoehungsrichtung = (-sdx / seitenlaenge_mm, -sdy / seitenlaenge_mm)

    erste_mitte_position_mm = (
        rueckteilbreite_mm / 3.0 + positionskorrektur_erster_abnaeher_mm
    )
    erster_abnaeher = _baue_abnaeher(
        basis=hintere_mitte,
        taillenrichtung=taillenrichtung,
        erhoehungsrichtung=erhoehungsrichtung,
        mitte_position_mm=erste_mitte_position_mm,
        erhoehung_mm=taillenerhoehung_erster_hinterer_abnaeher_mm,
        inhalt_mm=erster_inhalt_mm,
        laenge_mm=laenge_erster_hinterer_abnaeher_mm,
    )

    hueftbogen_vektor = (
        hinterer_hueftbogenpunkt.x_mm - hintere_mitte.x_mm,
        hinterer_hueftbogenpunkt.y_mm - hintere_mitte.y_mm,
    )
    hueftbogen_position_mm = (
        hueftbogen_vektor[0] * taillenrichtung[0]
        + hueftbogen_vektor[1] * taillenrichtung[1]
    )
    erster_schenkel_position_mm = erste_mitte_position_mm + erster_inhalt_mm / 2.0
    zweite_mitte_position_mm = (
        hueftbogen_position_mm + erster_schenkel_position_mm
    ) / 2.0
    zweiter_abnaeher = _baue_abnaeher(
        basis=hintere_mitte,
        taillenrichtung=taillenrichtung,
        erhoehungsrichtung=erhoehungsrichtung,
        mitte_position_mm=zweite_mitte_position_mm,
        erhoehung_mm=taillenerhoehung_vorderer_abnaeher_mm,
        inhalt_mm=zweiter_inhalt_mm,
        laenge_mm=laenge_zweiter_hinterer_abnaeher_mm,
    )

    kontrollsumme_mm = (
        hueftabstich_mm
        + vorderer_abnaeherinhalt_mm
        + erster_inhalt_mm
        + zweiter_inhalt_mm
    )
    return ZweiHintereAbnaeher(
        erster_abnaeher=erster_abnaeher,
        zweiter_abnaeher=zweiter_abnaeher,
        kontrollsumme_mm=kontrollsumme_mm,
        verteilung_ist_vollstaendig=math.isclose(
            kontrollsumme_mm,
            taillenausfall_mm,
            abs_tol=KONTROLLSUMMEN_ABS_TOL_MM,
            rel_tol=0.0,
        ),
        provenienz=Provenienz(
            source_page=35,
            source_statement="Rückteil mit zwei RT-Abnähern, Schritte 19-21",
            formula_ids=("HOF-B1-S035-F01",),
            math_contracts=(
                "400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md",
                "400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md",
                "400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md",
            ),
            input_names=(
                "p7",
                "p8",
                "hintere_mitte",
                "hinterer_hueftbogenpunkt",
                "taillenausfall_mm",
                "hueftabstich_mm",
                "vorderer_abnaeherinhalt_mm",
                "hinterer_gesamtinhalt_mm",
            ),
            selected_options=(
                ("inhaltsdifferenz_mm", inhaltsdifferenz_mm),
                (
                    "positionskorrektur_erster_abnaeher_mm",
                    positionskorrektur_erster_abnaeher_mm,
                ),
                (
                    "laenge_erster_hinterer_abnaeher_mm",
                    laenge_erster_hinterer_abnaeher_mm,
                ),
                (
                    "laenge_zweiter_hinterer_abnaeher_mm",
                    laenge_zweiter_hinterer_abnaeher_mm,
                ),
            ),
            contract_version=CONTRACT_VERSION,
        ),
    )
