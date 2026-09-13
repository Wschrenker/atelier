"""Reiner Hüftabstich nach ausdrücklich gewählter Figurform, S. 37."""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum


CONTRACT_VERSION = "1.0.0"


class Figurform(str, Enum):
    BREITE_HUEFTE_FLACHES_GESAESS = "breite_huefte_flaches_gesaess"
    SCHMALE_HUEFTE_STARKES_GESAESS = "schmale_huefte_starkes_gesaess"


class EntscheidungFehltError(ValueError):
    """Eine ausdrückliche Fachentscheidung fehlt."""


class UngueltigeFigurformError(ValueError):
    """Keine der beiden auf S. 37 geregelten Figurformen."""


class UngueltigerZahlentypError(TypeError):
    """Nur int/float, keine bool-Werte oder stillen Textumwandlungen."""


class NichtEndlicherWertError(ValueError):
    """Ein Maß ist nicht als endlicher float darstellbar."""


class WertAusserhalbBereichError(ValueError):
    """Ein Maß verletzt seinen fachlichen oder technischen Bereich."""


@dataclass(frozen=True)
class Provenienz:
    source_page: int
    formula_ids: tuple[str, ...]
    math_contracts: tuple[str, ...]
    input_names: tuple[str, ...]
    selected_options: tuple[tuple[str, str | float], ...]
    contract_version: str


@dataclass(frozen=True)
class Hueftabstich:
    taillenausfall_mm: float
    figurform: Figurform
    hueftform_korrektur_mm: float
    hueftabstich_mm: float
    provenienz: Provenienz


def hueftabstich_berechnen(
    *,
    taillenausfall_mm: float,
    figurform: Figurform,
    hueftform_korrektur_mm: float,
) -> Hueftabstich:
    """Berechnet nur den Abstich; keine Abnäherverteilung oder Hüftkurve."""
    if figurform is None or hueftform_korrektur_mm is None:
        raise EntscheidungFehltError("Figurform und Korrekturbetrag ausdrücklich wählen")
    if not isinstance(figurform, Figurform):
        raise UngueltigeFigurformError("Eine Figurform aus S. 37 ist erforderlich")
    for name, wert in (
        ("taillenausfall_mm", taillenausfall_mm),
        ("hueftform_korrektur_mm", hueftform_korrektur_mm),
    ):
        if isinstance(wert, bool) or not isinstance(wert, (int, float)):
            raise UngueltigerZahlentypError(f"{name}: int oder float erforderlich")
        try:
            endlich = math.isfinite(wert)
        except OverflowError as exc:
            raise NichtEndlicherWertError(f"{name}: außerhalb des float-Bereichs") from exc
        if not endlich:
            raise NichtEndlicherWertError(f"{name}: endlicher Wert erforderlich")
    if taillenausfall_mm <= 0.0:
        raise WertAusserhalbBereichError("Taillenausfall muss größer als 0 mm sein")
    if not 5.0 <= hueftform_korrektur_mm <= 15.0:
        raise WertAusserhalbBereichError("S. 37: Korrekturbetrag von 5 bis 15 mm")

    if figurform is Figurform.BREITE_HUEFTE_FLACHES_GESAESS:
        abstich = taillenausfall_mm / 2.0 + hueftform_korrektur_mm
        formula_id = "HOF-B1-S037-F01"
    else:
        abstich = taillenausfall_mm / 2.0 - hueftform_korrektur_mm
        formula_id = "HOF-B1-S037-F02"

    # Technische Mengenbilanz, keine zusätzliche gedruckte S.37-Fachregel.
    if not 0.0 <= abstich <= taillenausfall_mm:
        raise WertAusserhalbBereichError("Hüftabstich muss zwischen 0 mm und TaAf liegen")

    return Hueftabstich(
        taillenausfall_mm=taillenausfall_mm,
        figurform=figurform,
        hueftform_korrektur_mm=hueftform_korrektur_mm,
        hueftabstich_mm=abstich,
        provenienz=Provenienz(
            source_page=37,
            formula_ids=(formula_id,),
            math_contracts=(
                "400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md",
                "400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md",
            ),
            input_names=("taillenausfall_mm",),
            selected_options=(
                ("figurform", figurform.value),
                ("hueftform_korrektur_mm", hueftform_korrektur_mm),
            ),
            contract_version=CONTRACT_VERSION,
        ),
    )
