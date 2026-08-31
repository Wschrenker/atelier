"""DXF-Export (AutoCAD R12, ASCII).

Bewusst ohne Fremdpaket: R12 ist das breiteste gemeinsame Format und wird von
CLO 3D, Optitex, Gerber, AutoCAD, LibreCAD und Inkscape gelesen. Damit muss
fuer den ersten Exportfall keine Abhaengigkeit festgelegt werden
(siehe `500_python/AGENT.md`, Abschnitt "Offene Stellen").

**Einheit:** Millimeter. `$INSUNITS = 4` sagt das der Gegenstelle.

**Y-Achse:** Die Konstruktion rechnet mit Y nach unten, DXF zeichnet mit Y
nach oben. Der Export spiegelt deshalb einmalig `y -> -y`. Das ist die einzige
Stelle, an der das passiert.

**Layer:** Die Namen sind hier frei gewaehlt. Die verbindliche Zuordnung zu den
Schnittzeichen des Buchs (S. 21-31) ist noch nicht verifiziert - siehe
Roadmap-Punkt A2. Solange gilt: aussagekraeftige Namen, keine Norm-Behauptung.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, Sequence

from geometrie import Punkt

from .schnittteil import Beschriftung, Linie, Schnittteil

# Layername -> AutoCAD-Farbnummer
LAYER = {
    "SCHNITTKANTE": 7,   # weisz/schwarz - fertige Schnittkante
    "STOFFBRUCH": 6,     # magenta - Kante liegt im Bruch
    "ABNAEHER": 1,       # rot
    "HILFSLINIE": 8,     # grau - Konstruktions- und Grundgeruestlinien
    "FADENLAUF": 3,      # gruen
    "KNIPS": 5,          # blau
    "SCHLITZ": 4,        # cyan
    "TEXT": 2,           # gelb
}


def _paar(code: int, wert) -> str:
    return f"{code}\n{wert}\n"


def _y(wert: float) -> float:
    """Konstruktion rechnet Y nach unten, DXF zeichnet Y nach oben."""
    return -wert


def _polylinie(punkte: Sequence[Punkt], layer: str, geschlossen: bool) -> str:
    if len(punkte) < 2:
        return ""
    teile = [
        _paar(0, "POLYLINE"),
        _paar(8, layer),
        _paar(66, 1),
        _paar(10, 0.0), _paar(20, 0.0), _paar(30, 0.0),
        _paar(70, 1 if geschlossen else 0),
    ]
    for p in punkte:
        teile.append(_paar(0, "VERTEX"))
        teile.append(_paar(8, layer))
        teile.append(_paar(10, f"{p[0]:.4f}"))
        teile.append(_paar(20, f"{_y(p[1]):.4f}"))
        teile.append(_paar(30, "0.0"))
    teile.append(_paar(0, "SEQEND"))
    teile.append(_paar(8, layer))
    return "".join(teile)


def _text(b: Beschriftung) -> str:
    return "".join([
        _paar(0, "TEXT"),
        _paar(8, b.layer),
        _paar(10, f"{b.punkt[0]:.4f}"),
        _paar(20, f"{_y(b.punkt[1]):.4f}"),
        _paar(30, "0.0"),
        _paar(40, f"{b.hoehe:.4f}"),
        _paar(1, b.text),
    ])


def _kopf(minx: float, miny: float, maxx: float, maxy: float) -> str:
    return "".join([
        _paar(0, "SECTION"), _paar(2, "HEADER"),
        _paar(9, "$ACADVER"), _paar(1, "AC1009"),
        _paar(9, "$INSUNITS"), _paar(70, 4),          # 4 = Millimeter
        _paar(9, "$MEASUREMENT"), _paar(70, 1),       # 1 = metrisch
        _paar(9, "$EXTMIN"), _paar(10, f"{minx:.4f}"),
        _paar(20, f"{miny:.4f}"), _paar(30, "0.0"),
        _paar(9, "$EXTMAX"), _paar(10, f"{maxx:.4f}"),
        _paar(20, f"{maxy:.4f}"), _paar(30, "0.0"),
        _paar(0, "ENDSEC"),
    ])


def _tabellen() -> str:
    teile = [
        _paar(0, "SECTION"), _paar(2, "TABLES"),
        _paar(0, "TABLE"), _paar(2, "LAYER"), _paar(70, len(LAYER)),
    ]
    for name, farbe in LAYER.items():
        teile += [
            _paar(0, "LAYER"),
            _paar(2, name),
            _paar(70, 0),
            _paar(62, farbe),
            _paar(6, "CONTINUOUS"),
        ]
    teile += [_paar(0, "ENDTAB"), _paar(0, "ENDSEC")]
    return "".join(teile)


def schreibe_dxf(teile: Iterable[Schnittteil], pfad: Path | str,
                 abstand_mm: float = 60.0) -> Path:
    """Schreibt Schnittteile nebeneinander in eine DXF-Datei.

    Die Teile werden anhand ihrer Huellrechtecke nebeneinander gelegt, mit
    `abstand_mm` Luft dazwischen. Die Konstruktion selbst wird dabei nicht
    veraendert - nur verschoben.
    """
    teile = list(teile)
    gelegt: List[Schnittteil] = []
    x_cursor = 0.0
    for t in teile:
        minx, miny, maxx, maxy = t.bbox()
        gelegt.append(t.verschoben(x_cursor - minx, -miny))
        x_cursor += (maxx - minx) + abstand_mm

    alle_punkte: List[Punkt] = []
    for t in gelegt:
        alle_punkte.extend(t.kontur)
        for l in t.linien:
            alle_punkte.extend(l.punkte)
    if not alle_punkte:
        raise ValueError("Keine Geometrie zum Schreiben")

    xs = [p[0] for p in alle_punkte]
    ys = [_y(p[1]) for p in alle_punkte]

    inhalt = [_kopf(min(xs), min(ys), max(xs), max(ys)), _tabellen()]
    inhalt.append(_paar(0, "SECTION"))
    inhalt.append(_paar(2, "ENTITIES"))
    for t in gelegt:
        inhalt.append(_polylinie(t.kontur, "SCHNITTKANTE", geschlossen=True))
        for l in t.linien:
            inhalt.append(_polylinie(l.punkte, l.layer, l.geschlossen))
        for b in t.beschriftungen:
            inhalt.append(_text(b))
    inhalt.append(_paar(0, "ENDSEC"))
    inhalt.append(_paar(0, "EOF"))

    ziel = Path(pfad)
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text("".join(inhalt), encoding="ascii", errors="replace")
    return ziel
