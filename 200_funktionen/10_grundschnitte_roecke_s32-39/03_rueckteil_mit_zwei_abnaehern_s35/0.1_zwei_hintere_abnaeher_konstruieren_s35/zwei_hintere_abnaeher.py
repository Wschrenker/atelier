"""Konstruiert zwei hintere Rockabnäher nach Hofenbitzer Band 1, S. 35."""

from __future__ import annotations

import math
from dataclasses import dataclass


CONTRACT_VERSION = "1.0.0"
KONTROLLSUMMEN_ABS_TOL_MM = 1e-9


class WertAusserhalbBereichError(ValueError):
    """Ein Wert verletzt den auf S. 35 belegten Fachbereich."""


class InkonsistenteErhoehungError(ValueError):
    """Eine übergebene Erhöhung passt nicht zur Vorgängerkonstruktion."""


class InkonsistenteVerteilungError(ValueError):
    """Die übergebenen Verteilungsbeträge ergeben nicht den Taillenausfall."""


class GeometrieVertragError(ValueError):
    """Die Grundgeometrie ist nicht endlich, entartet oder rechtwinklig."""


class NichtEndlicherWertError(ValueError):
    """Ein Maß- oder Entscheidungswert ist nicht endlich."""


class PositionAusserhalbRueckteilError(ValueError):
    """Hüftbogen oder Abnäherschenkel liegen nicht innerhalb des Rückteils."""


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


def _pruefe_bereich(wert_name: str, wert: float, minimum: float, maximum: float) -> None:
    if not math.isfinite(wert) or not minimum <= wert <= maximum:
        raise WertAusserhalbBereichError(
            f"{wert_name}={wert!r} mm liegt nicht im Bereich {minimum}-{maximum} mm"
        )


def _pruefe_endlich(wert_name: str, wert: float) -> None:
    if not math.isfinite(wert):
        raise NichtEndlicherWertError(f"{wert_name} muss endlich sein")


def _normierter_vektor(a: Punkt2D, b: Punkt2D) -> tuple[float, float]:
    if any(
        not math.isfinite(wert)
        for wert in (a.x_mm, a.y_mm, b.x_mm, b.y_mm)
    ):
        raise GeometrieVertragError("Punktkoordinaten müssen endlich sein")
    dx = b.x_mm - a.x_mm
    dy = b.y_mm - a.y_mm
    laenge_mm = math.hypot(dx, dy)
    if not math.isfinite(laenge_mm) or laenge_mm <= KONTROLLSUMMEN_ABS_TOL_MM:
        raise GeometrieVertragError("Richtungsvektor ist entartet")
    return dx / laenge_mm, dy / laenge_mm


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

    for wert_name, wert in (
        ("taillenausfall_mm", taillenausfall_mm),
        ("hueftabstich_mm", hueftabstich_mm),
        ("vorderer_abnaeherinhalt_mm", vorderer_abnaeherinhalt_mm),
        ("hinterer_gesamtinhalt_mm", hinterer_gesamtinhalt_mm),
        ("inhaltsdifferenz_mm", inhaltsdifferenz_mm),
        (
            "positionskorrektur_erster_abnaeher_mm",
            positionskorrektur_erster_abnaeher_mm,
        ),
        ("taillenerhoehung_seitenlinie_mm", taillenerhoehung_seitenlinie_mm),
        (
            "taillenerhoehung_vorderer_abnaeher_mm",
            taillenerhoehung_vorderer_abnaeher_mm,
        ),
        (
            "taillenerhoehung_erster_hinterer_abnaeher_mm",
            taillenerhoehung_erster_hinterer_abnaeher_mm,
        ),
        (
            "laenge_erster_hinterer_abnaeher_mm",
            laenge_erster_hinterer_abnaeher_mm,
        ),
        (
            "laenge_zweiter_hinterer_abnaeher_mm",
            laenge_zweiter_hinterer_abnaeher_mm,
        ),
    ):
        _pruefe_endlich(wert_name, wert)

    if taillenausfall_mm <= 0.0:
        raise WertAusserhalbBereichError("Taillenausfall muss größer als 0 mm sein")
    if hueftabstich_mm < 0.0 or vorderer_abnaeherinhalt_mm < 0.0:
        raise WertAusserhalbBereichError(
            "Hüftabstich und vorderer Abnäher dürfen nicht negativ sein"
        )
    if hinterer_gesamtinhalt_mm <= 0.0:
        raise WertAusserhalbBereichError(
            "Hinterer Gesamtinhalt muss größer als 0 mm sein"
        )

    _pruefe_bereich(
        "positionskorrektur_erster_abnaeher_mm",
        positionskorrektur_erster_abnaeher_mm,
        0.0,
        10.0,
    )
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
    _pruefe_bereich(
        "laenge_erster_hinterer_abnaeher_mm",
        laenge_erster_hinterer_abnaeher_mm,
        130.0,
        160.0,
    )
    _pruefe_bereich(
        "laenge_zweiter_hinterer_abnaeher_mm",
        laenge_zweiter_hinterer_abnaeher_mm,
        120.0,
        140.0,
    )
    erwartete_erhoehung_mm = taillenerhoehung_seitenlinie_mm / 3.0
    if not math.isclose(
        taillenerhoehung_erster_hinterer_abnaeher_mm,
        erwartete_erhoehung_mm,
        abs_tol=KONTROLLSUMMEN_ABS_TOL_MM,
        rel_tol=0.0,
    ):
        raise InkonsistenteErhoehungError(
            "Erster hinterer Abnäher muss die Erhöhung aus S. 34 übernehmen"
        )

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
    kontrollsumme_mm = math.fsum(
        (
            hueftabstich_mm,
            vorderer_abnaeherinhalt_mm,
            erster_inhalt_mm,
            zweiter_inhalt_mm,
        )
    )
    if not math.isclose(
        kontrollsumme_mm,
        taillenausfall_mm,
        abs_tol=KONTROLLSUMMEN_ABS_TOL_MM,
        rel_tol=0.0,
    ):
        raise InkonsistenteVerteilungError(
            "Hüftabstich und drei Abnäher ergeben nicht den Taillenausfall"
        )

    taillenrichtung = _normierter_vektor(hintere_mitte, p7)
    seitenrichtung = _normierter_vektor(p7, p8)
    if not math.isclose(
        taillenrichtung[0] * seitenrichtung[0]
        + taillenrichtung[1] * seitenrichtung[1],
        0.0,
        abs_tol=1e-12,
        rel_tol=0.0,
    ):
        raise GeometrieVertragError(
            "Taillen- und Seitenrichtung müssen rechtwinklig sein"
        )
    rueckteilbreite_mm = math.hypot(
        p7.x_mm - hintere_mitte.x_mm,
        p7.y_mm - hintere_mitte.y_mm,
    )
    erhoehungsrichtung = (-seitenrichtung[0], -seitenrichtung[1])

    erste_mitte_position_mm = (
        rueckteilbreite_mm / 3.0 + positionskorrektur_erster_abnaeher_mm
    )
    erster_hm_schenkel_position_mm = erste_mitte_position_mm - erster_inhalt_mm / 2.0
    erster_sn_schenkel_position_mm = erste_mitte_position_mm + erster_inhalt_mm / 2.0
    if not (
        0.0
        < erster_hm_schenkel_position_mm
        < erster_sn_schenkel_position_mm
        < rueckteilbreite_mm
    ):
        raise PositionAusserhalbRueckteilError(
            "Der erste hintere Abnäher passt nicht zwischen hM und Seitenlinie"
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
    if not all(math.isfinite(wert) for wert in hueftbogen_vektor):
        raise GeometrieVertragError("Hinterer Hüftbogenpunkt muss endlich sein")
    hueftbogen_position_mm = (
        hueftbogen_vektor[0] * taillenrichtung[0]
        + hueftbogen_vektor[1] * taillenrichtung[1]
    )
    if not erster_sn_schenkel_position_mm < hueftbogen_position_mm <= rueckteilbreite_mm:
        raise PositionAusserhalbRueckteilError(
            "Der Hüftbogen muss seitennahtwärts hinter dem ersten Abnäher liegen"
        )
    zweite_mitte_position_mm = (
        hueftbogen_position_mm + erster_sn_schenkel_position_mm
    ) / 2.0
    zweiter_hm_schenkel_position_mm = zweite_mitte_position_mm - zweiter_inhalt_mm / 2.0
    zweiter_sn_schenkel_position_mm = zweite_mitte_position_mm + zweiter_inhalt_mm / 2.0
    if not (
        erster_sn_schenkel_position_mm
        < zweiter_hm_schenkel_position_mm
        < zweiter_sn_schenkel_position_mm
        < hueftbogen_position_mm
    ):
        raise PositionAusserhalbRueckteilError(
            "Der zweite Abnäher passt nicht zwischen Hüftbogen und erstem Schenkel"
        )
    zweiter_abnaeher = _baue_abnaeher(
        basis=hintere_mitte,
        taillenrichtung=taillenrichtung,
        erhoehungsrichtung=erhoehungsrichtung,
        mitte_position_mm=zweite_mitte_position_mm,
        erhoehung_mm=taillenerhoehung_vorderer_abnaeher_mm,
        inhalt_mm=zweiter_inhalt_mm,
        laenge_mm=laenge_zweiter_hinterer_abnaeher_mm,
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
