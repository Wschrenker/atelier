# Transformationen

**Status:** `bereit`

**Herleitung:** [`09_trigonometrie_und_polarkoordinaten.md`](../90_recherche/09_trigonometrie_und_polarkoordinaten.md), [`10_rotation_und_abnaeher_verlegung.md`](../90_recherche/10_rotation_und_abnaeher_verlegung.md).

## Zielprimitiven

```python
translate_point(p, v) -> Point2D
rotate_point(p, pivot, angle_deg) -> Point2D
mirror_point_across_line(p, a, b, *, zero_tol_mm) -> Point2D
scale_point(p, pivot, factor_x, factor_y=None) -> Point2D
transform_points(points, transform) -> tuple[Point2D, ...]
```

Fachliche Operationen wie „Abnäher schließen“ bestimmen zuerst, **welche** Punkte transformiert werden. Dieser Vertrag beschreibt nur die Transformation.

## Verschiebung

```text
P' = P + v
```

## Rotation im Y-nach-unten-System

```text
x0 = x - px
y0 = y - py
x' = px + x0 cos(θ) - y0 sin(θ)
y' = py + x0 sin(θ) + y0 cos(θ)
```

Positive Engine-Winkel drehen sichtbar im Uhrzeigersinn.

## Spiegelung an einer Geraden

Zuerst Lotfuß `H` aus dem Projektionsvertrag bestimmen:

```text
H = projection(P, line(A,B))
P' = 2H - P
```

Die Spiegelachse ist eine unendliche Gerade. Soll nur an einer vorhandenen Kante gespiegelt werden, ist dies fachlich trotzdem dieselbe Gerade; Segmentbegrenzung wäre ein anderer Vertrag.

## Skalierung um einen festen Punkt

```text
x' = px + factor_x × (x-px)
y' = py + factor_y × (y-py)
```

Bei einheitlicher Skalierung gilt `factor_y=factor_x`. Negative Faktoren spiegeln zusätzlich und müssen ausdrücklich angefordert werden.

## Sonderfälle

- Spiegelachse `A≈B` → `DegenerateGeometryError`.
- Faktor `0` kollabiert Geometrie und ist standardmäßig unzulässig.
- Ein Abnäher darf nicht allein durch Auswahl „irgendwelcher Punkte“ geschlossen werden; Drehpunkt, bewegte Konturseite und Zielkante müssen der Fachfunktion gehören.

## Invarianten

- Translation, Rotation und Spiegelung erhalten paarweise Abstände.
- Rotation erhält den Abstand jedes Punktes zum Drehpunkt.
- Zweimalige Spiegelung an derselben Achse ergibt die Ausgangslage.
- Spiegelpunkte auf der Achse bleiben unverändert.
- Transformationen verändern keine Fachmetadaten ohne ausdrückliches Mapping.

## Prüffälle

| Operation | Eingabe | Erwartung |
|---|---|---|
| Rotation | `(10,0)` um `(0,0)`, `90°` | `(0,10)` |
| Spiegelung | `(20,30)` an `x=0` | `(-20,30)` |
| Spiegelung | `(20,30)` an `y=10` | `(20,-10)` |
| Translation | `(5,7)` um `(10,-2)` | `(15,5)` |
| Skalierung | `(10,20)` um `(0,0)` mit `2` | `(20,40)` |
