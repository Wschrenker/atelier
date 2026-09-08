"""Kleine, reine Konstruktionstabelle fuer den geraden Rock auf S. 32-33."""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from typing import Mapping


ENTSCHEIDUNGSNAMEN = (
    "hueftzugabe",
    "taillenzugabe",
    "hueftabstich",
    "vorderer_abnaeherinhalt",
    "erster_hinterer_abnaeherinhalt",
    "zweiter_hinterer_abnaeherinhalt",
)
KONTROLLSUMMEN_ABS_TOL_MM = 1e-9
CONTRACT_VERSION = "1.0.0"


class Berechnungsstatus(str, Enum):
    VOLLSTAENDIG = "vollstaendig"
    UNVOLLSTAENDIG = "unvollstaendig"


class EntscheidungFehltError(ValueError):
    """Mindestens eine fachlich erforderliche Entscheidung wurde ausgelassen."""

    def __init__(self, fehlende_entscheidungen: tuple[str, ...]) -> None:
        self.fehlende_entscheidungen = fehlende_entscheidungen
        super().__init__(
            "Fehlende Entscheidungen: " + ", ".join(fehlende_entscheidungen)
        )


class ZugabeAusserhalbBereichError(ValueError):
    """Eine explizite Zugabe liegt ausserhalb des auf S. 33 belegten Bereichs."""

    def __init__(
        self,
        entscheidung_name: str,
        wert_mm: float,
        minimum_mm: float,
        maximum_mm: float,
    ) -> None:
        self.entscheidung_name = entscheidung_name
        self.wert_mm = wert_mm
        self.minimum_mm = minimum_mm
        self.maximum_mm = maximum_mm
        super().__init__(
            f"{entscheidung_name}={wert_mm} mm liegt nicht im Bereich "
            f"{minimum_mm}-{maximum_mm} mm"
        )


class EntscheidungAusserhalbBereichError(ValueError):
    """Eine Fachentscheidung verletzt die auf S. 33 belegte Regel."""

    def __init__(self, entscheidung_name: str, wert_mm: float, regel: str) -> None:
        self.entscheidung_name = entscheidung_name
        self.wert_mm = wert_mm
        self.regel = regel
        super().__init__(f"{entscheidung_name}={wert_mm} mm verletzt {regel}")


class UngueltigerLaengenwertError(ValueError):
    """Ein Laengenwert verletzt seine Endlichkeits- oder Vorzeichengrenze."""

    def __init__(self, wert_name: str, wert_cm: float) -> None:
        self.wert_name = wert_name
        self.wert_cm = wert_cm
        super().__init__(f"{wert_name}={wert_cm!r} cm ist keine gueltige Laenge")


class NichtEndlicherBerechnungswertError(ArithmeticError):
    """Eine Umrechnung oder abgeleitete Rechnung ist nicht endlich."""

    def __init__(self, wert_name: str, wert: float) -> None:
        self.wert_name = wert_name
        self.wert = wert
        super().__init__(f"{wert_name}={wert!r} ist kein endlicher Berechnungswert")


def _endlicher_berechnungswert(wert_name: str, wert: float) -> float:
    if not math.isfinite(wert):
        raise NichtEndlicherBerechnungswertError(wert_name, wert)
    return wert


def cm_zu_mm(wert_cm: float) -> float:
    """Rechnet einen Eingabewert einmalig an der Systemgrenze in mm um."""

    return _endlicher_berechnungswert("cm_zu_mm", float(wert_cm) * 10.0)


def taillenausfall_aus_halben_weiten(
    halbe_hueftweite_mm: float,
    halbe_taillenweite_mm: float,
) -> float:
    """HOF-B1-S033-F01: Differenz der zugabenhaltigen Halbweiten."""

    return _endlicher_berechnungswert(
        "taillenausfall_mm",
        halbe_hueftweite_mm - halbe_taillenweite_mm,
    )


@dataclass(frozen=True)
class Provenienz:
    source_page: int
    formula_ids: tuple[str, ...]
    math_contracts: tuple[str, ...]
    input_names: tuple[str, ...]
    selected_options: tuple[tuple[str, float], ...]
    contract_version: str


@dataclass(frozen=True)
class Konstruktionstabelle:
    hueftumfang_mm: float
    taillenumfang_mm: float
    huefttiefe_mm: float
    modelllaenge_mm: float
    hueftzugabe_mm: float
    taillenzugabe_mm: float
    hueftweite_mm: float
    halbe_hueftweite_mm: float
    viertel_hueftweite_mm: float
    taillenweite_mm: float
    halbe_taillenweite_mm: float
    viertel_taillenweite_mm: float
    taillenausfall_mm: float
    halber_taillenausfall_mm: float
    hueftabstich_mm: float
    vorderer_abnaeherinhalt_mm: float
    erster_hinterer_abnaeherinhalt_mm: float
    zweiter_hinterer_abnaeherinhalt_mm: float
    kontrollsumme_taillenausfall_mm: float
    verteilung_ist_vollstaendig: bool
    berechnungsstatus: Berechnungsstatus
    provenienz: Provenienz


def konstruktionstabelle_erstellen(
    *,
    hueftumfang_cm: float,
    taillenumfang_cm: float,
    huefttiefe_cm: float,
    modelllaenge_cm: float,
    entscheidungen_cm: Mapping[str, float | None],
) -> Konstruktionstabelle:
    """Berechnet die belegten Tabellenwerte; Eingaben liegen nur hier in cm vor."""

    fehlende_entscheidungen = tuple(
        name
        for name in ENTSCHEIDUNGSNAMEN
        if name not in entscheidungen_cm or entscheidungen_cm[name] is None
    )
    if fehlende_entscheidungen:
        raise EntscheidungFehltError(fehlende_entscheidungen)

    for wert_name, wert_cm in (
        ("hueftumfang_cm", hueftumfang_cm),
        ("taillenumfang_cm", taillenumfang_cm),
        ("huefttiefe_cm", huefttiefe_cm),
        ("modelllaenge_cm", modelllaenge_cm),
    ):
        if not math.isfinite(wert_cm) or wert_cm <= 0.0:
            raise UngueltigerLaengenwertError(wert_name, wert_cm)

    for wert_name in ENTSCHEIDUNGSNAMEN:
        wert_cm = entscheidungen_cm[wert_name]
        if not math.isfinite(wert_cm) or wert_cm < 0.0:
            raise UngueltigerLaengenwertError(wert_name, wert_cm)

    hueftumfang_mm = cm_zu_mm(hueftumfang_cm)
    taillenumfang_mm = cm_zu_mm(taillenumfang_cm)
    huefttiefe_mm = cm_zu_mm(huefttiefe_cm)
    modelllaenge_mm = cm_zu_mm(modelllaenge_cm)

    hueftzugabe_mm = cm_zu_mm(entscheidungen_cm["hueftzugabe"])
    taillenzugabe_mm = cm_zu_mm(entscheidungen_cm["taillenzugabe"])
    for name, wert_mm, minimum_mm, maximum_mm in (
        ("hueftzugabe", hueftzugabe_mm, 20.0, 30.0),
        ("taillenzugabe", taillenzugabe_mm, 10.0, 20.0),
    ):
        if not minimum_mm <= wert_mm <= maximum_mm:
            raise ZugabeAusserhalbBereichError(
                name, wert_mm, minimum_mm, maximum_mm
            )

    hueftweite_mm = _endlicher_berechnungswert(
        "hueftweite_mm",
        hueftumfang_mm + hueftzugabe_mm,
    )
    taillenweite_mm = _endlicher_berechnungswert(
        "taillenweite_mm",
        taillenumfang_mm + taillenzugabe_mm,
    )
    halbe_hueftweite_mm = _endlicher_berechnungswert(
        "halbe_hueftweite_mm",
        hueftweite_mm / 2.0,
    )
    halbe_taillenweite_mm = _endlicher_berechnungswert(
        "halbe_taillenweite_mm",
        taillenweite_mm / 2.0,
    )
    taillenausfall_mm = _endlicher_berechnungswert(
        "taillenausfall_mm",
        taillenausfall_aus_halben_weiten(
            halbe_hueftweite_mm,
            halbe_taillenweite_mm,
        ),
    )

    hueftabstich_mm = cm_zu_mm(entscheidungen_cm["hueftabstich"])
    vorderer_abnaeherinhalt_mm = cm_zu_mm(
        entscheidungen_cm["vorderer_abnaeherinhalt"]
    )
    erster_hinterer_abnaeherinhalt_mm = cm_zu_mm(
        entscheidungen_cm["erster_hinterer_abnaeherinhalt"]
    )
    zweiter_hinterer_abnaeherinhalt_mm = cm_zu_mm(
        entscheidungen_cm["zweiter_hinterer_abnaeherinhalt"]
    )

    halber_taillenausfall_mm = _endlicher_berechnungswert(
        "halber_taillenausfall_mm",
        taillenausfall_mm / 2.0,
    )
    hueftabstich_min_mm = _endlicher_berechnungswert(
        "hueftabstich_min_mm",
        halber_taillenausfall_mm - 10.0,
    )
    hueftabstich_max_mm = _endlicher_berechnungswert(
        "hueftabstich_max_mm",
        halber_taillenausfall_mm + 10.0,
    )
    if not hueftabstich_min_mm <= hueftabstich_mm <= hueftabstich_max_mm:
        raise EntscheidungAusserhalbBereichError(
            "hueftabstich",
            hueftabstich_mm,
            "½ TaAf ± 10 mm",
        )
    if not (
        math.isclose(vorderer_abnaeherinhalt_mm, 0.0, abs_tol=KONTROLLSUMMEN_ABS_TOL_MM)
        or 15.0 <= vorderer_abnaeherinhalt_mm <= 25.0
    ):
        raise EntscheidungAusserhalbBereichError(
            "vorderer_abnaeherinhalt",
            vorderer_abnaeherinhalt_mm,
            "0 mm oder 15-25 mm",
        )
    if erster_hinterer_abnaeherinhalt_mm > 45.0:
        raise EntscheidungAusserhalbBereichError(
            "erster_hinterer_abnaeherinhalt",
            erster_hinterer_abnaeherinhalt_mm,
            "höchstens 45 mm",
        )
    if zweiter_hinterer_abnaeherinhalt_mm != 0.0:
        raise EntscheidungAusserhalbBereichError(
            "zweiter_hinterer_abnaeherinhalt",
            zweiter_hinterer_abnaeherinhalt_mm,
            "auf S. 33 genau 0 mm",
        )

    kontrollsumme_taillenausfall_mm = _endlicher_berechnungswert(
        "kontrollsumme_taillenausfall_mm",
        hueftabstich_mm
        + vorderer_abnaeherinhalt_mm
        + erster_hinterer_abnaeherinhalt_mm
        + zweiter_hinterer_abnaeherinhalt_mm,
    )
    verteilung_ist_vollstaendig = math.isclose(
        kontrollsumme_taillenausfall_mm,
        taillenausfall_mm,
        abs_tol=KONTROLLSUMMEN_ABS_TOL_MM,
        rel_tol=0.0,
    )
    berechnungsstatus = (
        Berechnungsstatus.VOLLSTAENDIG
        if verteilung_ist_vollstaendig
        else Berechnungsstatus.UNVOLLSTAENDIG
    )
    selected_options = (
        ("hueftzugabe_mm", hueftzugabe_mm),
        ("taillenzugabe_mm", taillenzugabe_mm),
        ("hueftabstich_mm", hueftabstich_mm),
        ("vorderer_abnaeherinhalt_mm", vorderer_abnaeherinhalt_mm),
        ("erster_hinterer_abnaeherinhalt_mm", erster_hinterer_abnaeherinhalt_mm),
        ("zweiter_hinterer_abnaeherinhalt_mm", zweiter_hinterer_abnaeherinhalt_mm),
    )
    provenienz = Provenienz(
        source_page=33,
        formula_ids=(
            "HOF-B1-S033-F01",
            "HOF-B1-S033-F02",
            "HOF-B1-S033-F03",
        ),
        math_contracts=(
            "400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md",
            "400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md",
        ),
        input_names=(
            "hueftumfang_cm",
            "taillenumfang_cm",
            "huefttiefe_cm",
            "modelllaenge_cm",
        ),
        selected_options=selected_options,
        contract_version=CONTRACT_VERSION,
    )

    return Konstruktionstabelle(
        hueftumfang_mm=hueftumfang_mm,
        taillenumfang_mm=taillenumfang_mm,
        huefttiefe_mm=huefttiefe_mm,
        modelllaenge_mm=modelllaenge_mm,
        hueftzugabe_mm=hueftzugabe_mm,
        taillenzugabe_mm=taillenzugabe_mm,
        hueftweite_mm=hueftweite_mm,
        halbe_hueftweite_mm=halbe_hueftweite_mm,
        viertel_hueftweite_mm=hueftweite_mm / 4.0,
        taillenweite_mm=taillenweite_mm,
        halbe_taillenweite_mm=halbe_taillenweite_mm,
        viertel_taillenweite_mm=taillenweite_mm / 4.0,
        taillenausfall_mm=taillenausfall_mm,
        halber_taillenausfall_mm=halber_taillenausfall_mm,
        hueftabstich_mm=hueftabstich_mm,
        vorderer_abnaeherinhalt_mm=vorderer_abnaeherinhalt_mm,
        erster_hinterer_abnaeherinhalt_mm=erster_hinterer_abnaeherinhalt_mm,
        zweiter_hinterer_abnaeherinhalt_mm=zweiter_hinterer_abnaeherinhalt_mm,
        kontrollsumme_taillenausfall_mm=kontrollsumme_taillenausfall_mm,
        verteilung_ist_vollstaendig=verteilung_ist_vollstaendig,
        berechnungsstatus=berechnungsstatus,
        provenienz=provenienz,
    )
