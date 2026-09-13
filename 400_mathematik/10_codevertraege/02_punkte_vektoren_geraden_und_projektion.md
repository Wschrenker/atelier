# Punkte, Vektoren, Geraden und Projektion

**Status:** `bereit`

**Herleitung:** [`02_punkte_und_vektoren.md`](../90_recherche/02_punkte_und_vektoren.md), [`07_geraden_und_schnittpunkte.md`](../90_recherche/07_geraden_und_schnittpunkte.md), [`08_normalen_und_rechte_winkel.md`](../90_recherche/08_normalen_und_rechte_winkel.md).

## Datentypen

```python
Point2D(x_mm: float, y_mm: float)
Vector2D(dx_mm: float, dy_mm: float)
```

Punkt ± Vektor ergibt einen Punkt. Punkt − Punkt ergibt einen Vektor. Zwei Punkte dürfen nicht ohne benannte geometrische Bedeutung addiert werden.

## Grundprimitiven

```python
vector(a, b) -> Vector2D
distance(a, b) -> float
midpoint(a, b) -> Point2D
lerp(a, b, t) -> Point2D
point_from_direction(start, direction, length_mm) -> Point2D
project_point_to_line(p, a, b, *, zero_tol_mm) -> Projection
line_intersection(a, b, c, d, *, parallel_tol) -> LineIntersection
segment_intersection(a, b, c, d, *, tolerance) -> SegmentIntersection
trim_or_extend_to_intersection(start, end, target_a, target_b, *, tolerance) -> TrimExtendResult
```

## Formeln

```text
v = B - A
|v| = sqrt(vx² + vy²)
lerp(A,B,t) = A + t(B-A)
point_from_direction(A,d,L) = A + L × d/|d|
```

`point_from_direction` normalisiert einen nichtverschwindenden Richtungsvektor; die geforderte Länge wird dadurch nicht von der ursprünglichen Vektorlänge verfälscht.

Projektion von `P` auf die unendliche Gerade durch `A,B`:

```text
d = B - A
t = dot(P-A, d) / dot(d,d)
H = A + t d
```

`t < 0` liegt vor A, `0 ≤ t ≤ 1` auf dem Segment und `t > 1` hinter B. Die Projektion darf je nach Fachschritt anschließend ausdrücklich auf `[0,1]` begrenzt werden; die Geradenfunktion tut dies nicht still.

Geradenschnitt:

```text
r = B-A
s = D-C
divisor = cross(r,s)
t = cross(C-A,s) / divisor
P = A + t r
```

## Kürzen oder verlängern bis zu einer Linie

`trim_or_extend_to_intersection` schneidet die unendliche Gerade durch `start,end` mit der Zielgeraden. Der Start bleibt fest; der neue Endpunkt ist der eindeutige Schnittpunkt. Das Ergebnis benennt anhand des ursprünglichen Segmentparameters:

```text
0 ≤ t < 1  → TRIMMED
 t ≈ 1     → UNCHANGED
 t > 1     → EXTENDED
 t < 0     → BEHIND_START
```

`PARALLEL`, `COINCIDENT` und `BEHIND_START` werden nicht still in eine scheinbar gültige Kante umgewandelt. Ob Verlängern oder Kürzen fachlich erlaubt ist, entscheidet der aufrufende Schritt.

## Ergebniszustände

- Geraden: `UNIQUE`, `PARALLEL`, `COINCIDENT`.
- Segmente zusätzlich: `NONE`, `TOUCH`, `CROSS`, `OVERLAP`.
- `A≈B` oder `C≈D` → `DegenerateGeometryError`; keine Gerade aus einer Nullkante.

## Invarianten

- `distance(A,B) = distance(B,A) ≥ 0`.
- `lerp(A,B,0)=A`, `lerp(A,B,1)=B`.
- Beim Lot gilt `dot(P-H, B-A)≈0`.
- Ein eindeutiger Geradenschnitt liegt auf beiden unendlichen Geraden.
- Geraden- und Segment-Schnitt werden nicht verwechselt.

## Prüffälle

| Operation | Eingabe | Erwartung |
|---|---|---|
| Abstand | `(0,0)`, `(30,40)` | `50 mm` |
| Mittelpunkt | `(0,0)`, `(10,20)` | `(5,10)` |
| Teilung | `A=(0,0)`, `B=(100,0)`, `t=0.25` | `(25,0)` |
| Projektion | `P=(20,30)`, Linie `(0,0)→(100,0)` | `H=(20,0)`, `t=0.2`, Abstand `30` |
| Geradenschnitt | waagrecht durch `y=10`, senkrecht durch `x=20` | `(20,10)`, `UNIQUE` |
| parallel | `y=0` und `y=10` | `PARALLEL`, kein Ersatzpunkt |
