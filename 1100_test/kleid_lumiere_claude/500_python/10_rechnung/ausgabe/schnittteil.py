"""Neutrales Geometriemodell eines Schnittteils.

Bewusst duenn: ein Schnittteil ist eine geschlossene Kontur plus beschriftete
Linien. Es kennt weder Buchseite noch Kleid noch Ausgabeformat.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Sequence, Tuple

from geometrie import Punkt, bbox, verschiebe_alle


@dataclass
class Linie:
    """Eine Polylinie auf einer benannten Ebene."""

    punkte: List[Punkt]
    layer: str
    geschlossen: bool = False


@dataclass
class Beschriftung:
    """Text an einem Punkt. `hoehe` in Millimeter."""

    text: str
    punkt: Punkt
    hoehe: float = 8.0
    layer: str = "TEXT"


@dataclass
class Schnittteil:
    """Ein Schnittteil: geschlossene Schnittkante, Hilfslinien, Beschriftung."""

    name: str
    kontur: List[Punkt]
    linien: List[Linie] = field(default_factory=list)
    beschriftungen: List[Beschriftung] = field(default_factory=list)

    def bbox(self) -> Tuple[float, float, float, float]:
        alle: List[Punkt] = list(self.kontur)
        for linie in self.linien:
            alle.extend(linie.punkte)
        return bbox(alle)

    def verschoben(self, dx: float, dy: float) -> "Schnittteil":
        return Schnittteil(
            name=self.name,
            kontur=verschiebe_alle(self.kontur, dx, dy),
            linien=[Linie(verschiebe_alle(l.punkte, dx, dy), l.layer, l.geschlossen)
                    for l in self.linien],
            beschriftungen=[Beschriftung(b.text, (b.punkt[0] + dx, b.punkt[1] + dy),
                                         b.hoehe, b.layer)
                            for b in self.beschriftungen],
        )

    def hilfslinie(self, punkte: Sequence[Punkt], layer: str = "HILFSLINIE") -> None:
        self.linien.append(Linie(list(punkte), layer))

    def beschrifte(self, text: str, punkt: Punkt, hoehe: float = 8.0,
                   layer: str = "TEXT") -> None:
        self.beschriftungen.append(Beschriftung(text, punkt, hoehe, layer))
