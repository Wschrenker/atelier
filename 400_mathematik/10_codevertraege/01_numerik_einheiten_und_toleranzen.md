# Numerik, Einheiten und Toleranzen

**Status:** `bereit`

**Herleitung:** [`01_koordinatensystem.md`](../90_recherche/01_koordinatensystem.md), [`06_einheiten_und_masshaltigkeit.md`](../90_recherche/06_einheiten_und_masshaltigkeit.md); allgemeine Zahlen- und Einheitenregeln, keine Hofenbitzer-Fachregel.

## Datengrundlage

```text
LengthMm = float
AngleDeg = float
AngleRad = float
```

Alle Werte müssen endlich sein. Negative Längen sind nur zulässig, wenn der Vertrag ausdrücklich eine gerichtete Verschiebung beschreibt; geometrische Abstände, Radien und Toleranzen sind nichtnegativ.

## Einheiten

```text
mm = cm × 10
cm = mm ÷ 10
rad = deg × π ÷ 180
deg = rad × 180 ÷ π
```

Die Umrechnung erfolgt einmal an der Systemgrenze. Zwischenwerte bleiben ungerundet in Millimetern. Anzeige- und Exportformatierung erhalten Kopien der Werte.

## Koordinaten- und Winkelkonvention

- X zeigt nach rechts, Y nach unten.
- `angle_deg = 0` zeigt nach rechts.
- Positive Engine-Winkel drehen sichtbar im Uhrzeigersinn.
- Für Python-Trigonometrie gilt daher direkt:

```text
dx = length_mm × cos(angle_rad)
dy = length_mm × sin(angle_rad)
```

Ein aus einer mathematischen Y-nach-oben-Quelle übernommener Winkel muss vor Verwendung ausdrücklich umgerechnet werden. Die Quelleinheit gehört in den Parameternamen oder Datentyp.

## Skalare Hilfsoperationen

Zielsignaturen:

```python
clamp(value, lower, upper) -> float
mean(values) -> float
equal_partition(total, count) -> tuple[float, ...]
```

- `clamp` darf nur verwendet werden, wenn der Fachvertrag das Begrenzen ausdrücklich fordert; sonst ist ein Bereichsfehler sichtbar zu melden.
- `lower ≤ upper`, `count > 0` und alle Werte endlich.
- `mean` auf leerer Folge ist unzulässig.
- `equal_partition` liefert `count` gleiche Anteile, deren Summe innerhalb Rechentoleranz wieder `total` ergibt. Eine Buchangabe „ungefähr gleich“ benötigt zusätzlich eine fachliche Abweichungstoleranz.

## Vergleiche

Zielsignatur:

```python
is_close(a: float, b: float, *, abs_tol: float, rel_tol: float = 0.0) -> bool
```

```text
|a - b| ≤ max(abs_tol, rel_tol × max(|a|, |b|))
```

- `abs_tol` muss `≥ 0` und zweckbezogen sein.
- Nahtpassung, Polygonabschluss und Kurvenabflachung verwenden getrennte Toleranzen.
- Exakte Gleichheit ist nur für diskrete Werte wie Stückzahlen oder Zustandsnamen geeignet.

## Fehlerfälle

- NaN oder unendlich → `NonFiniteValueError`.
- Unbekannte Einheit → `UnitError`.
- Negative Toleranz → `ValueError`.
- Fachwert außerhalb seines Quellenbereichs → Fehler des aufrufenden Funktionsvertrags, nicht dieser Mathematikschicht.

## Invarianten

- `cm_to_mm(mm_to_cm(x))` ist innerhalb der angegebenen Vergleichstoleranz wieder `x`.
- Einheiten werden nicht still gemischt.
- Rundung verändert keinen nachfolgenden Konstruktionspunkt.

## Prüffälle

| Eingabe | Erwartung |
|---|---|
| `cm_to_mm(4.4)` | `44.0` |
| `mm_to_cm(58.0)` | `5.8` |
| `deg_to_rad(180)` | `π` |
| `is_close(10.0, 10.0005, abs_tol=0.001)` | `True` |
| `is_close(10.0, 10.002, abs_tol=0.001)` | `False` |
