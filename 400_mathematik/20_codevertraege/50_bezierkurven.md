# Bezierkurven

**Status:** `bereit`

**Herleitung:** [`03_kurven_bezier.md`](../90_recherche/03_kurven_bezier.md), [`11_bezier_kubisch_und_splines.md`](../90_recherche/11_bezier_kubisch_und_splines.md), [`12_kurvenlaenge_und_passung.md`](../90_recherche/12_kurvenlaenge_und_passung.md).

## Datentypen

```python
QuadraticBezier(p0, p1, p2)
CubicBezier(p0, p1, p2, p3)
```

Kontrollpunkte sind Teil der Kurvendefinition. Ihre fachliche Lage darf nicht aus einer gezeichneten Kurve geraten werden, wenn die Quelle dafür keine Regel liefert.

## Zielprimitiven

```python
evaluate(curve, t) -> Point2D
derivative(curve, t) -> Vector2D
split(curve, t) -> tuple[Curve, Curve]
flatten(curve, *, flatness_tol_mm) -> tuple[Point2D, ...]
curve_length(curve, *, length_tol_mm) -> float
point_at_length(curve, distance_mm, *, length_tol_mm) -> PointAtLength
```

## Formeln

Quadratisch:

```text
B(t)=(1-t)²P0 + 2(1-t)tP1 + t²P2
```

Kubisch:

```text
B(t)=(1-t)³P0 + 3(1-t)²tP1 + 3(1-t)t²P2 + t³P3
```

Für beide gilt `0≤t≤1`. `split` verwendet de Casteljau und muss zwei Teilkurven liefern, die zusammen exakt dieselbe mathematische Kurve bilden.

## Tangenten und Anschluss

```text
quadratisch: B'(0)=2(P1-P0), B'(1)=2(P2-P1)
kubisch:     B'(0)=3(P1-P0), B'(1)=3(P3-P2)
```

- gemeinsamer Endpunkt → C0;
- kollineare, gleichgerichtete Endtangenten → G1;
- gleiche Ableitungsvektoren → C1.

Ein optisch weicher Nahtanschluss verlangt mindestens eine belegte G1-Entscheidung; die Mathematik wählt die Kontrollpunkte nicht selbst.

## Abflachung und Länge

`flatten` unterteilt adaptiv, bis die geometrische Abweichung innerhalb `flatness_tol_mm` liegt. Eine feste Zahl von sechs Segmenten ist kein allgemeiner Genauigkeitsvertrag.

`curve_length` misst die Kurve unabhängig von einer Anzeigeabtastung. Zulässig sind adaptive Unterteilung oder numerische Quadratur, sofern der Fehlervertrag eingehalten und getestet wird.

`point_at_length` sucht einen Parameter `t`, dessen Teilbogenlänge der geforderten Strecke entspricht. Werte außerhalb `[0, Gesamtlänge]` erzeugen einen Bereichsfehler, sofern nicht ausdrücklich geklemmt angefordert.

## Sonderfälle

- `t` außerhalb `[0,1]` → `ValueError`.
- alle Kontrollpunkte gleich → gültige Nullkurve für Auswertung, aber nicht als Naht.
- verschwindende Tangente → Anschlussrichtung nicht definiert.
- nichtpositive Toleranz → `ValueError`.

## Invarianten

- `evaluate(curve,0)=P0`, `evaluate(curve,1)=Pend`.
- Split-Ende links = Split-Anfang rechts.
- Split erhält Gesamtform und Gesamtlänge innerhalb Toleranz.
- Kurvenlänge ist mindestens der direkte Endpunktabstand.
- Kleinere Abflachungstoleranz darf die bestätigte Fehlergrenze nicht verschlechtern.

## Prüffälle

- Gerade kubische Kurve mit kollinearen Kontrollpunkten von `(0,0)` bis `(100,0)` hat Länge `100 mm`.
- Quadratische Kurve `(0,0),(50,50),(100,0)` liefert bei `t=0.5` den Punkt `(50,25)`.
- Split derselben Kurve bei `t=0.5` verbindet sich in `(50,25)`.
