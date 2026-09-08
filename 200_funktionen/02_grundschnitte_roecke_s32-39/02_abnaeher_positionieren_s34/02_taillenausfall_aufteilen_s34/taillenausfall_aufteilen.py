"""Reine Aufteilung des Taillenausfalls nach S. 34."""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum


CONTRACT_VERSION = "1.0.0"
KONTROLLSUMMEN_ABS_TOL_MM = 1e-9


class Hueftform(str, Enum):
    FLACH = "flach"
    DURCHSCHNITTLICH = "durchschnittlich"
    STARK = "stark"


class Verteilungsstatus(str, Enum):
    VOLLSTAENDIG_EIN_HINTERER_ABNAEHER = (
        "vollstaendig_ein_hinterer_abnaeher"
    )
    ZWEI_HINTERE_ABNAEHER_ERFORDERLICH = (
        "zwei_hintere_abnaeher_erforderlich"
    )


class EntscheidungFehltError(ValueError):
    """Eine fuer die gewaehlte Variante erforderliche Entscheidung fehlt."""


class UnpassendeEntscheidungError(ValueError):
    """Eine Entscheidung wurde fuer eine Variante geliefert, die sie nicht nutzt."""


class WertAusserhalbBereichError(ValueError):
    """Ein Wert verletzt den belegten Fachbereich."""

    def __init__(self, wert_name: str, wert_mm: float, regel: str) -> None:
        self.wert_name = wert_name
        self.wert_mm = wert_mm
        self.regel = regel
        super().__init__(f"{wert_name}={wert_mm!r} mm verletzt {regel}")


class NegativerRestbetragError(ValueError):
    """Die gewaehlten Betraege uebersteigen den Taillenausfall."""


class NichtEndlicherBerechnungswertError(ArithmeticError):
    """Ein abgeleiteter Wert ist nicht endlich."""


@dataclass(frozen=True)
class Provenienz:
    source_page: int
    source_statement: str
    formula_ids: tuple[str, ...]
    math_contracts: tuple[str, ...]
    input_names: tuple[str, ...]
    selected_options: tuple[tuple[str, str | float], ...]
    contract_version: str


@dataclass(frozen=True)
class Taillenausfallverteilung:
    taillenausfall_mm: float
    hueftform: Hueftform
    hueftform_korrektur_mm: float | None
    hueftabstich_mm: float
    vorderer_abnaeherinhalt_mm: float
    hinterer_abnaeherinhalt_mm: float
    kontrollsumme_mm: float
    verteilung_ist_vollstaendig: bool
    status: Verteilungsstatus
    provenienz: Provenienz


def _pruefe_endlich(wert_name: str, wert: float) -> None:
    if not math.isfinite(wert):
        raise WertAusserhalbBereichError(wert_name, wert, "endlicher Wert")


def _pruefe_vorderen_abnaeher(wert_mm: float) -> None:
    _pruefe_endlich("vorderer_abnaeherinhalt_mm", wert_mm)
    if wert_mm != 0.0 and not 10.0 <= wert_mm <= 25.0:
        raise WertAusserhalbBereichError(
            "vorderer_abnaeherinhalt_mm",
            wert_mm,
            "0 mm oder 10-25 mm aus Text und Tabelle auf S. 34",
        )


def taillenausfall_aufteilen(
    *,
    taillenausfall_mm: float,
    hueftform: Hueftform,
    hueftform_korrektur_mm: float | None,
    vorderer_abnaeherinhalt_mm: float,
) -> Taillenausfallverteilung:
    """Teilt TaAf in Hueftabstich, vorderen und hinteren Restbetrag."""

    _pruefe_endlich("taillenausfall_mm", taillenausfall_mm)
    if taillenausfall_mm <= 0.0:
        raise WertAusserhalbBereichError(
            "taillenausfall_mm", taillenausfall_mm, "groesser als 0 mm"
        )
    if not isinstance(hueftform, Hueftform):
        raise WertAusserhalbBereichError(
            "hueftform", math.nan, "eine explizite Hueftform"
        )
    _pruefe_vorderen_abnaeher(vorderer_abnaeherinhalt_mm)

    halber_taillenausfall_mm = taillenausfall_mm / 2.0
    if not math.isfinite(halber_taillenausfall_mm):
        raise NichtEndlicherBerechnungswertError(
            "Halber Taillenausfall ist nicht endlich"
        )

    formula_ids: tuple[str, ...]
    if hueftform is Hueftform.DURCHSCHNITTLICH:
        if hueftform_korrektur_mm is not None:
            raise UnpassendeEntscheidungError(
                "Die durchschnittliche Hueftform verwendet keine Korrektur"
            )
        hueftabstich_mm = halber_taillenausfall_mm
        formula_ids = ("HOF-B1-S034-F01",)
    else:
        if hueftform_korrektur_mm is None:
            raise EntscheidungFehltError(
                "Fuer flache oder starke Hueftform fehlt hueftform_korrektur_mm"
            )
        _pruefe_endlich("hueftform_korrektur_mm", hueftform_korrektur_mm)
        if not 10.0 <= hueftform_korrektur_mm <= 15.0:
            raise WertAusserhalbBereichError(
                "hueftform_korrektur_mm",
                hueftform_korrektur_mm,
                "10-15 mm",
            )
        if hueftform is Hueftform.FLACH:
            hueftabstich_mm = halber_taillenausfall_mm - hueftform_korrektur_mm
            formula_ids = ("HOF-B1-S034-F01", "HOF-B1-S034-F03")
        else:
            hueftabstich_mm = halber_taillenausfall_mm + hueftform_korrektur_mm
            formula_ids = ("HOF-B1-S034-F01", "HOF-B1-S034-F04")

    if not math.isfinite(hueftabstich_mm):
        raise NichtEndlicherBerechnungswertError("Hueftabstich ist nicht endlich")
    if hueftabstich_mm < 0.0:
        raise WertAusserhalbBereichError(
            "hueftabstich_mm", hueftabstich_mm, "nichtnegativer Rest"
        )

    hinterer_abnaeherinhalt_mm = (
        taillenausfall_mm - hueftabstich_mm - vorderer_abnaeherinhalt_mm
    )
    if not math.isfinite(hinterer_abnaeherinhalt_mm):
        raise NichtEndlicherBerechnungswertError(
            "Hinterer Abnaeherinhalt ist nicht endlich"
        )
    if hinterer_abnaeherinhalt_mm < 0.0:
        raise NegativerRestbetragError(
            "Hueftabstich und vorderer Abnaeher uebersteigen TaAf"
        )

    kontrollsumme_mm = (
        hueftabstich_mm
        + vorderer_abnaeherinhalt_mm
        + hinterer_abnaeherinhalt_mm
    )
    if not math.isfinite(kontrollsumme_mm):
        raise NichtEndlicherBerechnungswertError(
            "Kontrollsumme ist nicht endlich"
        )
    verteilung_ist_vollstaendig = math.isclose(
        kontrollsumme_mm,
        taillenausfall_mm,
        abs_tol=KONTROLLSUMMEN_ABS_TOL_MM,
        rel_tol=0.0,
    )
    status = (
        Verteilungsstatus.VOLLSTAENDIG_EIN_HINTERER_ABNAEHER
        if hinterer_abnaeherinhalt_mm <= 45.0
        else Verteilungsstatus.ZWEI_HINTERE_ABNAEHER_ERFORDERLICH
    )

    selected_options: list[tuple[str, str | float]] = [
        ("hueftform", hueftform.value),
        ("vorderer_abnaeherinhalt_mm", vorderer_abnaeherinhalt_mm),
    ]
    if hueftform_korrektur_mm is not None:
        selected_options.append(
            ("hueftform_korrektur_mm", hueftform_korrektur_mm)
        )

    return Taillenausfallverteilung(
        taillenausfall_mm=taillenausfall_mm,
        hueftform=hueftform,
        hueftform_korrektur_mm=hueftform_korrektur_mm,
        hueftabstich_mm=hueftabstich_mm,
        vorderer_abnaeherinhalt_mm=vorderer_abnaeherinhalt_mm,
        hinterer_abnaeherinhalt_mm=hinterer_abnaeherinhalt_mm,
        kontrollsumme_mm=kontrollsumme_mm,
        verteilung_ist_vollstaendig=verteilung_ist_vollstaendig,
        status=status,
        provenienz=Provenienz(
            source_page=34,
            source_statement="Taillenausfall aufteilen, Schritte 13-15",
            formula_ids=formula_ids,
            math_contracts=(
                "400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md",
                "400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md",
            ),
            input_names=("taillenausfall_mm",),
            selected_options=tuple(selected_options),
            contract_version=CONTRACT_VERSION,
        ),
    )
