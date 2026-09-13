"""Positioniert Hueftbogen-Endpunkte und Abnaeher nach S. 34."""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum


CONTRACT_VERSION = "1.0.0"
NULLVEKTOR_ABS_TOL_MM = 1e-9
GEOMETRIE_ABS_TOL_MM = 1e-9
RECHTWINKEL_ABS_TOL = 1e-12


class Formstatus(str, Enum):
    OFFEN_BIS_S35 = "offen_bis_s35"
    OFFEN_BIS_S36 = "offen_bis_s36"


class GeometrieVertragError(ValueError):
    """Die Grundgeometrie ist nicht endlich, entartet oder falsch angeordnet."""


class WertAusserhalbBereichError(ValueError):
    """Ein Fachwert verletzt den belegten Bereich."""


class InkonsistenteErhoehungError(ValueError):
    """Die hintere Erhoehung entspricht nicht exakt einem Drittel der Seite."""


class ZweiHintereAbnaeherErforderlichError(ValueError):
    """Mehr als 45 mm Restbetrag muessen auf S. 35 weiterbearbeitet werden."""


class PositionAusserhalbSchnittError(ValueError):
    """Ein Abnaeher oder Hueftbogenpunkt laege ausserhalb des Grundschnitts."""


class NichtEndlicherBerechnungswertError(ArithmeticError):
    """Eine abgeleitete Koordinate ist nicht endlich."""


@dataclass(frozen=True)
class Punkt2D:
    x_mm: float
    y_mm: float


@dataclass(frozen=True)
class Abnaeher:
    mitte: Punkt2D
    schenkel_vorne: Punkt2D
    schenkel_hinten: Punkt2D
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
class HueftbogenUndAbnaeher:
    p10: Punkt2D
    vorderer_hueftbogenpunkt: Punkt2D
    hinterer_hueftbogenpunkt: Punkt2D
    vorderer_abnaeher: Abnaeher | None
    hinterer_abnaeher: Abnaeher | None
    hueftbogenstatus: Formstatus
    taillennahtstatus: Formstatus
    provenienz: Provenienz


def _pruefe_endlich(wert_name: str, wert: float) -> None:
    if not math.isfinite(wert):
        raise WertAusserhalbBereichError(f"{wert_name} muss endlich sein")


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


def _punkt_aus_basis(
    basis: Punkt2D,
    taillenrichtung: tuple[float, float],
    erhoehungsrichtung: tuple[float, float],
    position_mm: float,
    erhoehung_mm: float,
) -> Punkt2D:
    punkt = Punkt2D(
        basis.x_mm
        + taillenrichtung[0] * position_mm
        + erhoehungsrichtung[0] * erhoehung_mm,
        basis.y_mm
        + taillenrichtung[1] * position_mm
        + erhoehungsrichtung[1] * erhoehung_mm,
    )
    if not math.isfinite(punkt.x_mm) or not math.isfinite(punkt.y_mm):
        raise NichtEndlicherBerechnungswertError(
            "Abgeleiteter Konstruktionspunkt ist nicht endlich"
        )
    return punkt


def _pruefe_bereich(wert_name: str, wert: float, minimum: float, maximum: float) -> None:
    _pruefe_endlich(wert_name, wert)
    if not minimum <= wert <= maximum:
        raise WertAusserhalbBereichError(
            f"{wert_name}={wert!r} mm liegt nicht im Bereich {minimum}-{maximum} mm"
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
    mitte = _punkt_aus_basis(
        basis,
        taillenrichtung,
        erhoehungsrichtung,
        mitte_position_mm,
        erhoehung_mm,
    )
    schenkel_vorne = _punkt_aus_basis(
        basis,
        taillenrichtung,
        erhoehungsrichtung,
        mitte_position_mm - halber_inhalt_mm,
        erhoehung_mm,
    )
    schenkel_hinten = _punkt_aus_basis(
        basis,
        taillenrichtung,
        erhoehungsrichtung,
        mitte_position_mm + halber_inhalt_mm,
        erhoehung_mm,
    )
    spitze = _punkt_aus_basis(
        basis,
        taillenrichtung,
        erhoehungsrichtung,
        mitte_position_mm,
        erhoehung_mm - laenge_mm,
    )
    return Abnaeher(
        mitte=mitte,
        schenkel_vorne=schenkel_vorne,
        schenkel_hinten=schenkel_hinten,
        spitze=spitze,
        inhalt_mm=inhalt_mm,
        laenge_mm=laenge_mm,
    )


def hueftbogen_und_abnaeher_konstruieren(
    *,
    vordere_mitte: Punkt2D,
    p7: Punkt2D,
    p8: Punkt2D,
    hintere_mitte: Punkt2D,
    taillenerhoehung_seitenlinie_mm: float,
    taillenerhoehung_vorderer_abnaeher_mm: float,
    taillenerhoehung_hinterer_abnaeher_mm: float,
    hueftabstich_mm: float,
    taillenumfang_mm: float,
    vorderer_abnaeherinhalt_mm: float,
    hinterer_abnaeherinhalt_mm: float,
    vordere_abnaeherlaenge_mm: float | None,
    hintere_abnaeherlaenge_mm: float | None,
) -> HueftbogenUndAbnaeher:
    """Konstruiert nur die auf S. 34 numerisch bestimmten Punkte und Geraden."""

    _pruefe_punkte(vordere_mitte, p7, p8, hintere_mitte)
    for name, wert in (
        ("hueftabstich_mm", hueftabstich_mm),
        ("taillenumfang_mm", taillenumfang_mm),
        ("vorderer_abnaeherinhalt_mm", vorderer_abnaeherinhalt_mm),
        ("hinterer_abnaeherinhalt_mm", hinterer_abnaeherinhalt_mm),
    ):
        _pruefe_endlich(name, wert)
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
    erwartete_hintere_erhoehung_mm = taillenerhoehung_seitenlinie_mm / 3.0
    if not math.isclose(
        taillenerhoehung_hinterer_abnaeher_mm,
        erwartete_hintere_erhoehung_mm,
        abs_tol=GEOMETRIE_ABS_TOL_MM,
        rel_tol=0.0,
    ):
        raise InkonsistenteErhoehungError(
            "Hintere Erhoehung muss dem exakten Drittelwert entsprechen"
        )
    if hueftabstich_mm < 0.0 or taillenumfang_mm <= 0.0:
        raise WertAusserhalbBereichError(
            "Hueftabstich muss nichtnegativ und Taillenumfang positiv sein"
        )
    if vorderer_abnaeherinhalt_mm != 0.0 and not (
        10.0 <= vorderer_abnaeherinhalt_mm <= 25.0
    ):
        raise WertAusserhalbBereichError(
            "Vorderer Abnaeher muss 0 mm oder 10-25 mm Inhalt haben"
        )
    if hinterer_abnaeherinhalt_mm < 0.0:
        raise WertAusserhalbBereichError(
            "Hinterer Abnaeherinhalt darf nicht negativ sein"
        )
    if hinterer_abnaeherinhalt_mm > 45.0:
        raise ZweiHintereAbnaeherErforderlichError(
            "Restbetrag ueber 45 mm gehoert in die Zwei-Abnaeher-Konstruktion S. 35"
        )

    taillenrichtung = _normierter_vektor(vordere_mitte, hintere_mitte)
    seitenrichtung = _normierter_vektor(p7, p8)
    skalarprodukt = (
        taillenrichtung[0] * seitenrichtung[0]
        + taillenrichtung[1] * seitenrichtung[1]
    )
    if not math.isclose(
        skalarprodukt, 0.0, abs_tol=RECHTWINKEL_ABS_TOL, rel_tol=0.0
    ):
        raise GeometrieVertragError(
            "Taillen- und Seitenrichtung muessen rechtwinklig sein"
        )
    erhoehungsrichtung = (-seitenrichtung[0], -seitenrichtung[1])
    gesamtbreite_mm = math.hypot(
        hintere_mitte.x_mm - vordere_mitte.x_mm,
        hintere_mitte.y_mm - vordere_mitte.y_mm,
    )
    p7_dx = p7.x_mm - vordere_mitte.x_mm
    p7_dy = p7.y_mm - vordere_mitte.y_mm
    p7_abstand_von_gerade_mm = abs(
        taillenrichtung[0] * p7_dy - taillenrichtung[1] * p7_dx
    )
    if p7_abstand_von_gerade_mm > GEOMETRIE_ABS_TOL_MM:
        raise GeometrieVertragError("P7 muss auf der urspruenglichen Taillenlinie liegen")
    p7_position_mm = p7_dx * taillenrichtung[0] + p7_dy * taillenrichtung[1]
    if not 0.0 <= p7_position_mm <= gesamtbreite_mm:
        raise GeometrieVertragError("P7 muss zwischen vM und hM liegen")

    halber_hueftabstich_mm = hueftabstich_mm / 2.0
    vorderer_hueftbogen_position_mm = p7_position_mm - halber_hueftabstich_mm
    hinterer_hueftbogen_position_mm = p7_position_mm + halber_hueftabstich_mm
    if not (
        0.0
        <= vorderer_hueftbogen_position_mm
        <= p7_position_mm
        <= hinterer_hueftbogen_position_mm
        <= gesamtbreite_mm
    ):
        raise PositionAusserhalbSchnittError(
            "Hueftabstich reicht ueber vM oder hM hinaus"
        )

    p10 = _punkt_aus_basis(
        vordere_mitte,
        taillenrichtung,
        erhoehungsrichtung,
        p7_position_mm,
        taillenerhoehung_seitenlinie_mm,
    )
    vorderer_hueftbogenpunkt = _punkt_aus_basis(
        vordere_mitte,
        taillenrichtung,
        erhoehungsrichtung,
        vorderer_hueftbogen_position_mm,
        taillenerhoehung_seitenlinie_mm,
    )
    hinterer_hueftbogenpunkt = _punkt_aus_basis(
        vordere_mitte,
        taillenrichtung,
        erhoehungsrichtung,
        hinterer_hueftbogen_position_mm,
        taillenerhoehung_seitenlinie_mm,
    )

    vorderer_abnaeher: Abnaeher | None
    if vorderer_abnaeherinhalt_mm == 0.0:
        if vordere_abnaeherlaenge_mm is not None:
            raise WertAusserhalbBereichError(
                "Ohne vorderen Inhalt darf keine Scheinlaenge gesetzt werden"
            )
        vorderer_abnaeher = None
    else:
        if vordere_abnaeherlaenge_mm is None:
            raise WertAusserhalbBereichError("Vordere Abnaeherlaenge fehlt")
        _pruefe_bereich(
            "vordere_abnaeherlaenge_mm",
            vordere_abnaeherlaenge_mm,
            80.0,
            100.0,
        )
        vordere_mitte_position_mm = (
            vorderer_hueftbogen_position_mm - taillenumfang_mm / 10.0
        )
        if (
            vordere_mitte_position_mm - vorderer_abnaeherinhalt_mm / 2.0 < 0.0
            or vordere_mitte_position_mm
            + vorderer_abnaeherinhalt_mm / 2.0
            > vorderer_hueftbogen_position_mm
        ):
            raise PositionAusserhalbSchnittError(
                "Vorderer Abnaeher liegt nicht zwischen vM und vorderem Hueftbogen"
            )
        vorderer_abnaeher = _baue_abnaeher(
            basis=vordere_mitte,
            taillenrichtung=taillenrichtung,
            erhoehungsrichtung=erhoehungsrichtung,
            mitte_position_mm=vordere_mitte_position_mm,
            erhoehung_mm=taillenerhoehung_vorderer_abnaeher_mm,
            inhalt_mm=vorderer_abnaeherinhalt_mm,
            laenge_mm=vordere_abnaeherlaenge_mm,
        )

    hinterer_abnaeher: Abnaeher | None
    if hinterer_abnaeherinhalt_mm == 0.0:
        if hintere_abnaeherlaenge_mm is not None:
            raise WertAusserhalbBereichError(
                "Ohne hinteren Inhalt darf keine Scheinlaenge gesetzt werden"
            )
        hinterer_abnaeher = None
    else:
        if hintere_abnaeherlaenge_mm is None:
            raise WertAusserhalbBereichError("Hintere Abnaeherlaenge fehlt")
        _pruefe_bereich(
            "hintere_abnaeherlaenge_mm",
            hintere_abnaeherlaenge_mm,
            130.0,
            160.0,
        )
        hintere_mitte_position_mm = (
            hinterer_hueftbogen_position_mm + gesamtbreite_mm
        ) / 2.0
        if (
            hintere_mitte_position_mm - hinterer_abnaeherinhalt_mm / 2.0
            < hinterer_hueftbogen_position_mm
            or hintere_mitte_position_mm
            + hinterer_abnaeherinhalt_mm / 2.0
            > gesamtbreite_mm
        ):
            raise PositionAusserhalbSchnittError(
                "Hinterer Abnaeher liegt nicht zwischen Hueftbogen und hM"
            )
        hinterer_abnaeher = _baue_abnaeher(
            basis=vordere_mitte,
            taillenrichtung=taillenrichtung,
            erhoehungsrichtung=erhoehungsrichtung,
            mitte_position_mm=hintere_mitte_position_mm,
            erhoehung_mm=taillenerhoehung_hinterer_abnaeher_mm,
            inhalt_mm=hinterer_abnaeherinhalt_mm,
            laenge_mm=hintere_abnaeherlaenge_mm,
        )

    selected_options = [
        ("taillenerhoehung_seitenlinie_mm", taillenerhoehung_seitenlinie_mm),
        (
            "taillenerhoehung_vorderer_abnaeher_mm",
            taillenerhoehung_vorderer_abnaeher_mm,
        ),
        (
            "taillenerhoehung_hinterer_abnaeher_mm",
            taillenerhoehung_hinterer_abnaeher_mm,
        ),
        ("hueftabstich_mm", hueftabstich_mm),
        ("vorderer_abnaeherinhalt_mm", vorderer_abnaeherinhalt_mm),
        ("hinterer_abnaeherinhalt_mm", hinterer_abnaeherinhalt_mm),
    ]
    if vordere_abnaeherlaenge_mm is not None:
        selected_options.append(
            ("vordere_abnaeherlaenge_mm", vordere_abnaeherlaenge_mm)
        )
    if hintere_abnaeherlaenge_mm is not None:
        selected_options.append(
            ("hintere_abnaeherlaenge_mm", hintere_abnaeherlaenge_mm)
        )

    return HueftbogenUndAbnaeher(
        p10=p10,
        vorderer_hueftbogenpunkt=vorderer_hueftbogenpunkt,
        hinterer_hueftbogenpunkt=hinterer_hueftbogenpunkt,
        vorderer_abnaeher=vorderer_abnaeher,
        hinterer_abnaeher=hinterer_abnaeher,
        hueftbogenstatus=Formstatus.OFFEN_BIS_S36,
        taillennahtstatus=Formstatus.OFFEN_BIS_S35,
        provenienz=Provenienz(
            source_page=34,
            source_statement="Hueftbogen und Abnaeher, Schritte 16-18",
            formula_ids=("HOF-B1-S034-F05",),
            math_contracts=(
                "400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md",
                "400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md",
                "400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md",
            ),
            input_names=(
                "vordere_mitte",
                "p7",
                "p8",
                "hintere_mitte",
                "taillenumfang_mm",
            ),
            selected_options=tuple(selected_options),
            contract_version=CONTRACT_VERSION,
        ),
    )
