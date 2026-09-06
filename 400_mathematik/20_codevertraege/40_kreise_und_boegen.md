# Kreise und Bögen

**Status:** `bereit` für allgemeine Geometrie; fachliche Auswahl von Radius, Mittelpunkt und Bogen bleibt im Funktionsschritt.

**Herleitung:** allgemeine analytische Geometrie; derzeit keine Hofenbitzer-Fachregel und keine eigene Kreisnotiz in `90_recherche`.

## Datentypen

```python
Circle(center: Point2D, radius_mm: float)
Arc(center: Point2D, radius_mm: float, start_angle_deg: float, sweep_angle_deg: float)
```

`radius_mm > 0`. Ein Vollkreis und ein Bogen werden nicht durch zufällig gleiche Start-/Endpunkte unterschieden, sondern durch den ausdrücklich gespeicherten Öffnungswinkel.

## Zielprimitiven

```python
point_on_circle(circle, angle_deg) -> Point2D
arc_length(arc) -> float
line_circle_intersections(a, b, circle, *, tolerance) -> IntersectionResult
circle_circle_intersections(c1, c2, *, tolerance) -> IntersectionResult
sample_arc(arc, *, max_sagitta_mm) -> tuple[Point2D, ...]
```

## Formeln

Im Y-nach-unten-System:

```text
x = cx + r cos(θ)
y = cy + r sin(θ)
Bogenlänge = r × |sweep_rad|
Kreisumfang = 2πr
```

## Schnittalgorithmen

Gerade durch `A` und `B` mit `D=B-A`, `F=A-C` für Kreismittelpunkt `C`:

```text
P(t) = A + tD
a = dot(D,D)
b = 2 dot(F,D)
c = dot(F,F) - r²
diskriminante = b² - 4ac
t = (-b ± sqrt(diskriminante)) / (2a)
```

Negative Diskriminante → `NONE`, innerhalb Toleranz null → `TANGENT`, positiv → `TWO_POINTS`. `A≈B` ist keine Gerade.

Für zwei Kreise mit Mittelpunkten `C1,C2`, Abstand `d` und Radien `r1,r2`:

```text
a = (r1² - r2² + d²) / (2d)
h² = r1² - a²
M = C1 + a × (C2-C1)/d
S1,2 = M ± sqrt(h²) × perpendicular(C2-C1)/d
```

`d>r1+r2` oder `d<|r1-r2|` → `NONE`; `h²≈0` → `TANGENT`; `d≈0` bei gleichen Radien → `COINCIDENT`. Ein kleines negatives `h²` innerhalb numerischer Toleranz darf für den Tangentialfall auf null gesetzt werden; eine echte negative Größe nicht.

Gerade–Kreis und Kreis–Kreis können `NONE`, `TANGENT`, `TWO_POINTS` oder bei identischen Kreisen `COINCIDENT` liefern. Die Reihenfolge zweier Punkte muss durch die aufrufende Konstruktion festgelegt werden, zum Beispiel entlang der Geraden oder nach Winkel.

## Bogenabtastung

Für Radius `r`, Sweep `α_rad` und gewünschte maximale Pfeilhöhe `s=max_sagitta_mm` gilt bei `r>0` und `s>0`:

```text
δ_max = min(π, 2 arccos(max(-1, 1 - s/r)))
N = max(1, ceil(|α_rad| / δ_max))
δ = α_rad / N
```

Die Ausgabe enthält Start und Ende sowie die `N-1` Zwischenpunkte in Sweep-Richtung. Sweep `0` liefert genau den Startpunkt. Für `s≥r` greift die Kappung auf höchstens Halbkreissegmente. Damit ist die Abweichung jeder Polygonsehne vom echten Bogen höchstens `max_sagitta_mm`; eine feste Segmentzahl für alle Radien ist unzulässig.

## Sonderfälle

- Radius `≤ 0` → `DegenerateGeometryError`.
- identische Kreise → unendlich viele Schnittpunkte, `COINCIDENT`.
- Tangentialität liefert genau einen Punkt.
- Auswahl „oberer“, „linker“ oder „fachlich passender“ Schnittpunkt gehört als explizite Auswahlregel in `200_funktionen`.

## Invarianten

- Jeder berechnete Kreispunkt hat Abstand `r` zum Mittelpunkt.
- `arc_length` ist nichtnegativ.
- `360°` ergibt `2πr`.
- Schnittpunkte erfüllen beide beteiligten Gleichungen innerhalb der Toleranz.

## Prüffälle

| Operation | Eingabe | Erwartung |
|---|---|---|
| Kreispunkt | Mittelpunkt `(0,0)`, `r=100`, `90°` | `(0,100)` |
| Halbkreis | `r=50`, Sweep `180°` | `50π mm` |
| Gerade–Kreis | `y=0`, Mittelpunkt `(0,0)`, `r=10` | `(-10,0)` und `(10,0)` |
| Tangente | `y=10`, Mittelpunkt `(0,0)`, `r=10` | `(0,10)`, `TANGENT` |
| getrennte Kreise | Mittelpunktsabstand `30`, Radien `10` und `10` | `NONE` |
