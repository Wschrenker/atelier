"""Alternative Seitennaht- und Abnäherlagen nach S. 35, Schritte 24-26."""

from __future__ import annotations

import math
from dataclasses import dataclass


CONTRACT_VERSION = "1.0.0"
NULLVEKTOR_ABS_TOL_MM = 1e-9


class GeometrieVertragError(ValueError):
    """Punkte oder Richtungen bilden keine ausführbare Geometrie."""


class WertAusserhalbBereichError(ValueError):
    """Ein Maß verletzt den Vertrag der gewählten Variante."""


@dataclass(frozen=True)
class Punkt2D:
    x_mm: float
    y_mm: float


@dataclass(frozen=True)
class Provenienz:
    source_page: int
    source_statement: str
    math_contracts: tuple[str, ...]
    input_names: tuple[str, ...]
    selected_options: tuple[tuple[str, float], ...]
    contract_version: str


@dataclass(frozen=True)
class Punktverschiebung:
    alter_punkt: Punkt2D
    neuer_punkt: Punkt2D
    verschiebung_mm: float
    provenienz: Provenienz


@dataclass(frozen=True)
class AbnaeherAnpassung:
    alte_spitze: Punkt2D
    neue_spitze: Punkt2D
    schenkel_a: Punkt2D
    schenkel_b: Punkt2D
    verlaengerter_schenkel: str | None
    gemeinsame_schenkellaenge_mm: float
    provenienz: Provenienz


def _normierter_vektor(a: Punkt2D, b: Punkt2D) -> tuple[float, float]:
    if any(
        not math.isfinite(wert)
        for wert in (a.x_mm, a.y_mm, b.x_mm, b.y_mm)
    ):
        raise GeometrieVertragError("Punktkoordinaten müssen endlich sein")
    dx = b.x_mm - a.x_mm
    dy = b.y_mm - a.y_mm
    laenge_mm = math.hypot(dx, dy)
    if not math.isfinite(laenge_mm) or laenge_mm <= NULLVEKTOR_ABS_TOL_MM:
        raise GeometrieVertragError("Verschiebungsrichtung ist entartet")
    return dx / laenge_mm, dy / laenge_mm


def _verschiebe_zum_ziel(
    punkt: Punkt2D,
    ziel: Punkt2D,
    verschiebung_mm: float,
) -> Punkt2D:
    if not math.isfinite(verschiebung_mm) or verschiebung_mm <= 0.0:
        raise WertAusserhalbBereichError(
            "Verschiebung muss als positiver endlicher Betrag gewählt werden"
        )
    richtung = _normierter_vektor(punkt, ziel)
    neuer_punkt = Punkt2D(
        punkt.x_mm + richtung[0] * verschiebung_mm,
        punkt.y_mm + richtung[1] * verschiebung_mm,
    )
    if not math.isfinite(neuer_punkt.x_mm) or not math.isfinite(neuer_punkt.y_mm):
        raise GeometrieVertragError("Verschobener Punkt ist nicht endlich")
    return neuer_punkt


def seitennaht_oben_nach_vorn_verschieben(
    *,
    seitennaht_oben: Punkt2D,
    richtungspunkt_vorne: Punkt2D,
    verschiebung_mm: float,
) -> Punktverschiebung:
    """Verschiebt die obere Seitennaht um den gewählten Betrag nach vorn."""

    neuer_punkt = _verschiebe_zum_ziel(
        seitennaht_oben,
        richtungspunkt_vorne,
        verschiebung_mm,
    )
    return Punktverschiebung(
        alter_punkt=seitennaht_oben,
        neuer_punkt=neuer_punkt,
        verschiebung_mm=verschiebung_mm,
        provenienz=Provenienz(
            source_page=35,
            source_statement="Schritt 24",
            math_contracts=(
                "400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md",
                "400_mathematik/20_codevertraege/30_transformationen.md",
                "400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md",
            ),
            input_names=("seitennaht_oben", "richtungspunkt_vorne"),
            selected_options=(("verschiebung_mm", verschiebung_mm),),
            contract_version=CONTRACT_VERSION,
        ),
    )


def _punkt_auf_strahl(
    start: Punkt2D,
    richtungspunkt: Punkt2D,
    laenge_mm: float,
) -> Punkt2D:
    richtung = _normierter_vektor(start, richtungspunkt)
    punkt = Punkt2D(
        start.x_mm + richtung[0] * laenge_mm,
        start.y_mm + richtung[1] * laenge_mm,
    )
    if not math.isfinite(punkt.x_mm) or not math.isfinite(punkt.y_mm):
        raise GeometrieVertragError("Verlängerter Schenkelpunkt ist nicht endlich")
    return punkt


def abnaeher_spitze_zur_seitennaht_verschieben(
    *,
    schenkel_a: Punkt2D,
    schenkel_b: Punkt2D,
    spitze: Punkt2D,
    richtungspunkt_seitennaht: Punkt2D,
    verschiebung_mm: float,
) -> AbnaeherAnpassung:
    """Verschiebt die Spitze und verlängert danach den kürzeren Schenkel."""

    neue_spitze = _verschiebe_zum_ziel(
        spitze,
        richtungspunkt_seitennaht,
        verschiebung_mm,
    )
    laenge_a_mm = math.hypot(
        schenkel_a.x_mm - neue_spitze.x_mm,
        schenkel_a.y_mm - neue_spitze.y_mm,
    )
    laenge_b_mm = math.hypot(
        schenkel_b.x_mm - neue_spitze.x_mm,
        schenkel_b.y_mm - neue_spitze.y_mm,
    )
    if (
        not math.isfinite(laenge_a_mm)
        or not math.isfinite(laenge_b_mm)
        or laenge_a_mm <= NULLVEKTOR_ABS_TOL_MM
        or laenge_b_mm <= NULLVEKTOR_ABS_TOL_MM
    ):
        raise GeometrieVertragError("Abnäherschenkel ist entartet")

    gemeinsame_laenge_mm = max(laenge_a_mm, laenge_b_mm)
    if math.isclose(laenge_a_mm, laenge_b_mm, abs_tol=1e-9, rel_tol=0.0):
        neuer_schenkel_a = schenkel_a
        neuer_schenkel_b = schenkel_b
        verlaengerter_schenkel = None
    elif laenge_a_mm < laenge_b_mm:
        neuer_schenkel_a = _punkt_auf_strahl(
            neue_spitze,
            schenkel_a,
            gemeinsame_laenge_mm,
        )
        neuer_schenkel_b = schenkel_b
        verlaengerter_schenkel = "a"
    else:
        neuer_schenkel_a = schenkel_a
        neuer_schenkel_b = _punkt_auf_strahl(
            neue_spitze,
            schenkel_b,
            gemeinsame_laenge_mm,
        )
        verlaengerter_schenkel = "b"

    return AbnaeherAnpassung(
        alte_spitze=spitze,
        neue_spitze=neue_spitze,
        schenkel_a=neuer_schenkel_a,
        schenkel_b=neuer_schenkel_b,
        verlaengerter_schenkel=verlaengerter_schenkel,
        gemeinsame_schenkellaenge_mm=gemeinsame_laenge_mm,
        provenienz=Provenienz(
            source_page=35,
            source_statement="Schritte 25-26",
            math_contracts=(
                "400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md",
                "400_mathematik/20_codevertraege/30_transformationen.md",
                "400_mathematik/20_codevertraege/70_messen_passung_und_markierungen.md",
                "400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md",
            ),
            input_names=(
                "schenkel_a",
                "schenkel_b",
                "spitze",
                "richtungspunkt_seitennaht",
            ),
            selected_options=(("verschiebung_mm", verschiebung_mm),),
            contract_version=CONTRACT_VERSION,
        ),
    )
