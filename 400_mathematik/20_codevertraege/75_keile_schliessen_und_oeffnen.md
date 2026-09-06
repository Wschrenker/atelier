# Keile und Schnittbereiche schließen oder öffnen

**Status:** `bereit` für die allgemeine starre Geometrie; die Fachfunktion bestimmt Drehpunkt, bewegte Seite, Ziel und Öffnungsmaß.

**Herleitung:** [`09_trigonometrie_und_polarkoordinaten.md`](../90_recherche/09_trigonometrie_und_polarkoordinaten.md), [`10_rotation_und_abnaeher_verlegung.md`](../90_recherche/10_rotation_und_abnaeher_verlegung.md).

## Zweck

Abnäher schließen, Falten-/Drapierschnitte öffnen und Schnittbereiche um einen gemeinsamen Drehpunkt spreizen beruhen auf derselben Mathematik: Ein ausgewählter Geometriebereich wird starr um einen Drehpunkt rotiert. Dieser Vertrag entscheidet nicht, welcher Bereich bewegt werden darf.

## Zielprimitiven

```python
signed_angle_deg(from_vector, to_vector, *, zero_tol_mm) -> AngleDeg
rotate_region_to_align_ray(points, pivot, moving_ray_point, target_ray_point, *, tolerance) -> RotationResult
open_region_by_angle(points, pivot, angle_deg) -> RotationResult
opening_angle_deg_from_chord(radius_mm, chord_mm) -> AngleDeg
spread_regions(regions, pivots, opening_angles_deg, *, tolerance) -> tuple[RotationResult, ...]
```

## Gerichteter Winkel im Y-nach-unten-System

```text
θ_rad = atan2(cross(von, nach), dot(von, nach))
θ_deg = θ_rad × 180/π
```

Mit X nach rechts und Y nach unten ist ein positiver Gradwinkel sichtbar im Uhrzeigersinn. Nullvektoren besitzen keine Richtung.

## Keil schließen

```text
moving = moving_ray_point - pivot
target = target_ray_point - pivot
θ_deg = signed_angle_deg(moving, target)
bewegter_Bereich' = rotate(bewegter_Bereich, pivot, θ_deg)
```

Die bewegte Keilkante muss danach innerhalb Toleranz auf dem Zielstrahl liegen. Der feste Bereich wird nicht verändert. Die spätere Nahtkontur kann nach dem Schließen eine neue Ausformung benötigen; diese Kurvenregel gehört nicht zur Rotation.

## Keil öffnen

Bei bekanntem Winkel wird der ausgewählte Bereich direkt um `angle_deg` gedreht. Wird stattdessen eine geradlinige Öffnungsweite `g` zwischen zwei Punkten im gleichen Abstand `r` vom Drehpunkt als **Sehnenlänge** gefordert:

```text
g = 2r sin(|θ_rad|/2)
|θ_rad| = 2 asin(g/(2r))
|θ_deg| = |θ_rad| × 180/π
```

Das ist nur gültig für `0 ≤ g ≤ 2r`. Bogenlänge, senkrechter Abstand und Abstand an einer bestimmten Kante sind andere Messarten und dürfen nicht mit der Sehnenlänge gleichgesetzt werden.

## Mehrere Öffnungen

`spread_regions` erhält für jeden Schnitt ein ausdrückliches Öffnungsmaß oder einen Winkel. „Gleichmäßig öffnen“ kann erst nach Festlegung von Gesamtweite, Zahl der Öffnungen und zulässiger Abweichung in gleiche Anteile zerlegt werden. Vollständiger Abnäherschluss und gewünschte Öffnungsweite können konkurrieren; dann stoppt die Fachfunktion statt eine Priorität zu erfinden.

## Sonderfälle

- Drehpunkt und Strahlpunkt fallen zusammen → `DegenerateGeometryError`.
- bewegte Punktmenge enthält Punkte beider fachlicher Seiten ohne Zuordnung → Eingabefehler.
- geforderte Sehne größer als Durchmesser → `UnsatisfiableGeometryError`.
- nach Rotation entstehende Selbstüberschneidung → Geometrieprüfung schlägt fehl.
- bereits ausgerichtete Strahlen → Winkel `0`, Ergebnis `UNCHANGED`.

## Invarianten

- Alle Abstände innerhalb des bewegten Bereichs bleiben erhalten.
- Jeder bewegte Punkt behält seinen Abstand zum Drehpunkt.
- Schließen und anschließendes Öffnen mit entgegengesetztem Winkel ergibt die Ausgangsgeometrie innerhalb Toleranz.
- Nicht ausgewählte Geometrie und Metadaten bleiben unverändert.
- Provenienz benennt Drehpunkt, bewegte Seite, Winkel/Öffnungsmaß und Quelle der Auswahl.

## Prüffälle

- Strahl nach rechts wird auf Strahl nach unten ausgerichtet → `+90°`.
- Punkt `(100,0)` wird um Ursprung `+90°` geöffnet → `(0,100)`.
- Radius `100 mm`, Sehnenöffnung `100 mm` → Öffnungswinkel `60°`.
- Zwei Öffnungen mit Gesamtwinkel `20°` und ausdrücklich gleicher Verteilung → je `10°`.
- Sehnenöffnung `250 mm` bei Radius `100 mm` → `UnsatisfiableGeometryError`.
