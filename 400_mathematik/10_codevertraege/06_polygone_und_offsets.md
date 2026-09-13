# Polygone und Offsets

**Status:** `offen` für die konkrete robuste Bibliothek/Topologieimplementierung; Ein-/Ausgabe- und Fehlervertrag sind festgelegt.

**Herleitung:** [`04_nahtzugabe_offset.md`](../90_recherche/04_nahtzugabe_offset.md), [`05_flaeche_und_orientierung.md`](../90_recherche/05_flaeche_und_orientierung.md), [`08_normalen_und_rechte_winkel.md`](../90_recherche/08_normalen_und_rechte_winkel.md).

## Datentypen

```python
Polyline(points)
Polygon(outer_ring, holes=())
PathSide = LEFT | RIGHT
EdgeAllowance(edge_id: str, distance_mm: float)
AllowanceTransition(vertex_id: str, join_style, miter_limit: float | None)
OffsetOptions(distance_mm, join_style, miter_limit, tolerance)
```

Ein Ring wird intern ohne doppelten Endpunkt oder mit ausdrücklich dokumentierter Abschlusskonvention gespeichert; beide Formen dürfen nicht gemischt werden.

## Zielprimitiven

```python
signed_area(ring) -> float
orientation(ring, *, area_tol) -> Orientation
is_simple(ring, *, tolerance) -> bool
validate_polygon(polygon, *, tolerance) -> ValidationResult
contains_point(polygon, point, *, tolerance) -> Containment
path_offset(path, distance_mm, *, side: PathSide, join_style, cap_style, tolerance) -> tuple[Polyline, ...]
polygon_offset(polygon, options) -> tuple[Polygon, ...]
variable_seam_allowance(seam_ring, edge_allowances: tuple[EdgeAllowance, ...], *, transitions: tuple[AllowanceTransition, ...], tolerance) -> tuple[Polygon, ...]
```

## Fläche und Orientierung

```text
A = 1/2 Σ(x_i y_(i+1) - x_(i+1) y_i)
```

Im festgelegten Y-nach-unten-System bedeutet positives Vorzeichen eine visuell im Uhrzeigersinn laufende äußere Ringfolge. Code soll für „außen“ dennoch nicht nur ein Wort wie `clockwise` verwenden, sondern Ringrolle und Flächenvorzeichen prüfen.

## Validierung vor Offset

Mindestens prüfen:

- alle Punkte endlich;
- mindestens drei unterschiedliche Punkte;
- keine Nullkanten;
- Betrag der Fläche größer als Flächentoleranz;
- keine Selbstüberschneidung;
- Löcher liegen innerhalb des Außenrings und überschneiden ihn nicht.

## Offsetvertrag

Für einen **offenen gerichteten Pfad** ist `distance_mm ≥ 0`; `side=LEFT|RIGHT` bezeichnet die sichtbare Seite relativ zur Laufrichtung im Y-nach-unten-System. Ein negatives Vorzeichen wird hier nicht zusätzlich verwendet.

Für einen **Polygonring** gilt:

- positive Distanz bedeutet für den Außenring **nach außen**;
- negative Distanz bedeutet nach innen;
- `join_style`: `MITER`, `BEVEL` oder `ROUND`;
- `MITER` benötigt ein `miter_limit` gegen extreme Spitzen;
- konkave Ecken und Selbstüberschneidungen werden topologisch bereinigt;
- ein Offset darf null, ein oder mehrere Polygone ergeben;
- verschwundene kleine Konturen sind ein explizites leeres Ergebnis, kein kaputtes Polygon.

Nahtzugaben werden aus dem **geschlossenen Nahtlinienring** erzeugt. `edge_allowances` ordnet jeder stabilen `edge_id` genau eine nichtnegative Zugabe zu. An jedem Übergang zweier verschiedener Zugaben legt `transitions` den Stil fest: `MITER` schneidet die beiden versetzten Kantengeraden innerhalb `miter_limit`, `BEVEL` verbindet ihre Endpunkte geradlinig, `ROUND` mit einem Kreisbogen um den Originalscheitel. Fehlende oder doppelte Kantenzuordnungen und fehlende Übergänge führen zum Stop. Offene Einzelpfade werden ausschließlich mit `path_offset(..., cap_style=...)` behandelt.

## Sonderfälle

- Selbstüberschneidender Eingangsring → Validierungsfehler.
- Nullkante → Validierungsfehler.
- Zu große Innenverschiebung → leeres Ergebnis möglich.
- Mehrere Ergebnisinseln → geordnete Ergebnismenge, nicht still nur die größte Fläche.

## Invarianten

- Ausgabe ist geschlossen, endlich und einfach.
- Eingabe wird nicht mutiert.
- Abstand auf geraden, nicht durch Ecken beeinflussten Abschnitten entspricht der Offsetdistanz innerhalb Toleranz.
- Orientierung und Ringrollen sind nach Ausgabe konsistent.
- `offset(distance=0)` ergibt geometrisch die Eingabe innerhalb Toleranz.

## Prüffälle

- Rechteck `100×50 mm`, Offset `10 mm`: äußere Begrenzung `120×70 mm` bei Miter-Ecken.
- Konkaves L-Polygon: Ergebnis bleibt einfach und enthält keine zurücklaufenden Spitzen.
- Dreieck mit sehr spitzem Winkel und kleinem `miter_limit`: Ecke wird begrenzt statt extrem verlängert.
- Selbstschneidende Schleife: Offset wird vorab abgelehnt.
