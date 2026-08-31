"""DOB-Groeszentabelle der Damen-Konfektionsgroeszen.

Quelle: Hofenbitzer, *Grundschnitte und Modellentwicklungen*, Band 1,
3. Auflage 2024, **S. 20** - Tabelle "DOB-Groeszentabelle der Damen-
Konfektionsgroeszen, basierend auf den Reihenmessungen von 1994".

Transkript im Repo:
`100_quellen/10_hofenbitzer_b1/band_1_geprueft_v1/s20.md`

Alle Werte in **Zentimeter**, wie im Buch gedruckt. Die Umrechnung nach
Millimeter geschieht erst in der Konstruktion (`geometrie.cm`).

Buchfehler werden hier **nicht still korrigiert**. Das Transkript vermerkt
zwei auffaellige Stellen, beide auszerhalb der hier benutzten Groeszen:

* `7.HW bis Fuszsohle`, Groesze 58: im Foto "15,5" - vermuteter Buchfehler.
* `ArD`, Groeszen 46/48/50: 12,1 / 12,2 / 14,3 - Sprung, so im Foto lesbar.

Die Zeilen "7.HW bis Kniekehle" und "7.HW bis Fuszsohle" tragen im Buch keine
Abkuerzung und werden hier unter `hw_kniekehle` / `hw_fusssohle` gefuehrt.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

# Spaltenkopf der Buchtabelle
DOB_GROESSEN: List[int] = [32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]

# Zeilen der Buchtabelle, digit-fuer-digit aus dem Transkript S.20.
DOB_TABELLE: Dict[str, List[float]] = {
    "KoeH":  [168, 168, 168, 168, 168, 168, 168, 168, 168, 168, 168, 168, 168, 168, 168],
    "BrU":   [76, 80, 84, 88, 92, 96, 100, 104, 110, 116, 122, 128, 134, 140, 146],
    "uBrU":  [68, 71, 74, 77, 80, 84, 88, 92, 98, 104, 110, 116, 122, 128, 134],
    "TaU":   [62, 65, 68, 72, 76, 80, 84, 88, 94.5, 101, 107.5, 114, 120.5, 127, 133.5],
    "HueU":  [86, 90, 94, 97, 100, 103, 106, 109, 114, 119, 124, 129, 134, 139, 144],
    "HaU":   [34.2, 34.8, 35.4, 36, 36.6, 37.2, 37.8, 38.4, 39.6, 40.8, 42, 43.2, 44.4, 45.6, 46.8],
    "HlB":   [6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7.1, 7.3, 7.5, 7.7, 7.9, 8.1, 8.3],
    "AlT":   [18.9, 19.3, 19.7, 20.1, 20.5, 20.9, 21.3, 21.7, 22.1, 22.5, 22.9, 23.3, 23.7, 24.1, 24.5],
    "RueL":  [41.4, 41.4, 41.4, 41.6, 41.8, 42, 42.2, 42.4, 42.7, 43, 43.3, 43.6, 43.6, 43.6, 43.6],
    "hw_kniekehle": [100.6, 100.9, 101.2, 101.5, 101.8, 102.1, 102.4, 102.7, 103.1, 103.5, 103.9, 104.3, 104.7, 105.1, 105.5],
    # Groesze 58 steht im Buch als 15,5 - vermuteter Buchfehler, siehe Modulkopf.
    "hw_fusssohle": [146, 146.3, 146.6, 146.9, 147.2, 147.5, 147.8, 148.1, 148.5, 148.9, 149.3, 149.7, 150.1, 15.5, 150.9],
    "HueT":  [21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21],
    "BrT":   [25.7, 26.5, 27.3, 28.1, 28.9, 29.7, 30.5, 31.3, 32.5, 33.7, 34.9, 36.1, 37.3, 38.5, 39.7],
    "VL":    [43.9, 44.3, 44.7, 45.3, 45.9, 46.5, 47.1, 47.7, 48.8, 49.9, 51, 52.1, 52.9, 53.7, 54.5],
    "oRueB": [16.2, 16.7, 17.2, 17.7, 18.2, 18.7, 19.2, 19.7, 20.5, 21.2, 22, 22.7, 23.5, 24.2, 25],
    "RueB":  [15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19.2, 19.9, 20.6, 21.3, 22, 22.7, 23.4],
    # Groeszen 46/48/50 im Buch auffaellig, wortwoertlich uebernommen.
    "ArD":   [7.2, 7.9, 8.6, 9.3, 10, 10.7, 11.4, 12.1, 12.2, 14.3, 15.4, 16.5, 17.6, 18.7, 19.8],
    "BrB":   [15.8, 16.6, 17.4, 18.2, 19, 19.8, 20.6, 21.4, 22.6, 23.8, 25, 26.2, 27.4, 28.6, 29.8],
    "BrPA":  [7.6, 8, 8.4, 8.8, 9.2, 9.6, 10, 10.4, 11, 11.6, 12.2, 12.8, 13.4, 14, 14.6],
    "SuB":   [11.9, 12, 12.1, 12.2, 12.4, 12.6, 12.8, 13, 13.2, 13.4, 13.6, 13.8, 14, 14.2, 14.4],
    "SuWi":  [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20],
    "ArL":   [59.4, 59.6, 59.8, 60, 60.2, 60.4, 60.6, 60.8, 61.1, 61.4, 61.7, 62, 62, 62, 62],
    "OaU":   [25.6, 26.2, 26.8, 28, 29.2, 30.4, 31.6, 32.8, 34.6, 36.4, 38.2, 40, 41.8, 43.6, 45.4],
    "HgU":   [14.6, 15, 15.4, 15.8, 16.2, 16.6, 17, 17.4, 18, 18.6, 19.2, 19.8, 20.4, 21, 21.6],
    "sTaH":  [106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106, 106],
    "OsU":   [50.2, 52, 53.8, 55.6, 57.4, 59.2, 61, 62.8, 65, 67.2, 69.4, 71.6, 73.8, 76, 78.2],
    "SiH":   [24.9, 25.3, 25.7, 26.1, 26.5, 26.9, 27.3, 27.7, 28.3, 28.9, 29.5, 30.1, 30.7, 31.3, 31.9],
    "SrH":   [81.1, 80.7, 80.3, 79.9, 79.5, 79.1, 78.7, 78.3, 77.7, 77.1, 76.5, 75.9, 75.3, 74.7, 74.1],
    "FeU":   [23, 23.5, 24, 24.5, 25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 30],
    "KoU":   [55.2, 55.4, 55.6, 55.8, 56, 56.2, 56.4, 56.6, 56.8, 57, 57.2, 57.4, 57.6, 57.8, 58],
}


@dataclass(frozen=True)
class Koerpermasse:
    """Koerpermasze einer Konfektionsgroesze. Alle Werte in Zentimeter."""

    groesse: int
    KoeH: float
    BrU: float
    uBrU: float
    TaU: float
    HueU: float
    HaU: float
    HlB: float
    AlT: float
    RueL: float
    HueT: float
    BrT: float
    VL: float
    oRueB: float
    RueB: float
    ArD: float
    BrB: float
    BrPA: float
    SuB: float
    SuWi: float
    sTaH: float

    def balance(self) -> float:
        """Individuelle Balance = VL - RueL (S.177, Abschnitt Balancemasze)."""
        return round(self.VL - self.RueL, 4)


def koerpermasse(groesse: int) -> Koerpermasse:
    """Koerpermasze einer Konfektionsgroesze aus der Buchtabelle S.20."""
    if groesse not in DOB_GROESSEN:
        raise ValueError(
            f"Groesze {groesse} steht nicht in der DOB-Tabelle S.20. "
            f"Vorhanden: {DOB_GROESSEN}"
        )
    i = DOB_GROESSEN.index(groesse)
    return Koerpermasse(
        groesse=groesse,
        KoeH=DOB_TABELLE["KoeH"][i],
        BrU=DOB_TABELLE["BrU"][i],
        uBrU=DOB_TABELLE["uBrU"][i],
        TaU=DOB_TABELLE["TaU"][i],
        HueU=DOB_TABELLE["HueU"][i],
        HaU=DOB_TABELLE["HaU"][i],
        HlB=DOB_TABELLE["HlB"][i],
        AlT=DOB_TABELLE["AlT"][i],
        RueL=DOB_TABELLE["RueL"][i],
        HueT=DOB_TABELLE["HueT"][i],
        BrT=DOB_TABELLE["BrT"][i],
        VL=DOB_TABELLE["VL"][i],
        oRueB=DOB_TABELLE["oRueB"][i],
        RueB=DOB_TABELLE["RueB"][i],
        ArD=DOB_TABELLE["ArD"][i],
        BrB=DOB_TABELLE["BrB"][i],
        BrPA=DOB_TABELLE["BrPA"][i],
        SuB=DOB_TABELLE["SuB"][i],
        SuWi=DOB_TABELLE["SuWi"][i],
        sTaH=DOB_TABELLE["sTaH"][i],
    )
