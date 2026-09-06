# Flächen teilen, vereinigen und kopieren

**Status:** `offen` für die konkrete robuste Bibliothek/Topologieimplementierung; Ergebnis- und Provenienzvertrag sind festgelegt.

**Bedarfsbezug:** [`MATHEBEDARF.md`](../../200_funktionen/03_modelle_roecke_s40-105_funktionen/02_taille_bund_passe_und_verschluss_s40-41_s50-63_s74_s78-79_s88-89_s98-103/MATHEBEDARF.md); allgemeine Flächentopologie, keine Hofenbitzer-Fachregel.

## Zielprimitiven

```python
split_polygon(polygon, cutter_path, *, tolerance) -> SplitResult
split_closed_path(path, positions, *, tolerance) -> tuple[Path, ...]
cyclic_reorder_path(path, new_start, *, tolerance) -> Path
partition_path_equal_length(path, count, *, tolerance) -> tuple[PathPosition, ...]
polygon_union(polygons, *, merge_touching: bool, tolerance) -> tuple[Polygon, ...]
polygon_difference(subject, cutters, *, tolerance) -> tuple[Polygon, ...]
copy_region(polygon, boundary_paths, *, tolerance) -> Polygon
```

„Abtrennen“, „anschneiden“, „kopieren“ und „wegschneiden“ sind verschiedene Operationen und dürfen nicht über eine einzige unbenannte Funktion laufen.

## Verträge

### Teilen

`split_polygon` zerschneidet eine Fläche entlang eines offenen oder geschlossenen Trennpfads. Das Ergebnis benennt:

- alle entstandenen Flächen;
- gemeinsame neue Kanten;
- Zuordnung der Originalkanten;
- Orientierung;
- Herkunft des Trennpfads.

Welche Fläche „Bund“, „Passe“, „Beleg“ oder „Rockteil“ heißt, entscheidet der aufrufende Fachschritt.

### Geschlossene Pfade teilen und neu beginnen

`split_closed_path` teilt eine geschlossene Kontur an eindeutig bestimmten Pfadpositionen, ohne ihre Geometrie zu ändern. `cyclic_reorder_path` wählt auf derselben geschlossenen Kontur einen neuen Startpunkt; Orientierung, Segmentrollen und Gesamtlänge bleiben erhalten. Das ist keine Spiegelung und keine Formänderung.

`partition_path_equal_length` liefert `count` gleichmäßig nach Bogenlänge verteilte Positionen. Es verteilt keine Faltenweite und trifft keine fachliche Auswahl darüber, welcher Konturabschnitt geteilt wird.

### Vereinigen/Anschneiden

`polygon_union` vereinigt Flächen mit positiver Überlappungsfläche immer topologisch. Nur kantenberührende Flächen werden ausschließlich bei `merge_touching=True` zu einer Fläche verschmolzen; die entfernte gemeinsame Kante bleibt dann als Provenienz erhalten. Bei `merge_touching=False`, reiner Punktberührung oder getrennten Flächen bleiben mehrere Polygone im Ergebnis. Dadurch wird eine fachliche Naht-/Bruchkante nicht versehentlich gelöscht.

### Differenz/Wegschneiden

`polygon_difference` entfernt die Schneideflächen. Null, eine oder mehrere Restflächen sind mögliche explizite Ergebnisse.

### Kopieren

`copy_region` erzeugt eine unabhängige Geometrie mit Provenienz. Kopieren verändert das Original nicht. Spiegelung, Reduktion und Abnäherschluss erfolgen danach als eigene, protokollierte Operationen.

## Sonderfälle

- Trennpfad schneidet die Fläche nicht oder nur tangential → expliziter `NO_SPLIT`-Zustand.
- Trennpfad läuft teilweise auf einer vorhandenen Kante → `AMBIGUOUS_BOUNDARY`, sofern der Fachschritt keine Regel vorgibt.
- Mehrere Ergebnisflächen → keine automatische Auswahl der größten Fläche.
- Selbstüberschneidender Trennpfad → Validierungsfehler.

## Invarianten

- Bei einer reinen Teilung entspricht die Summe der Ergebnisflächen der Eingangsfläche innerhalb Toleranz.
- Vereinigung und Differenz liefern valide, einfache Polygone.
- Originalgeometrie und Originalmetadaten bleiben unverändert.
- Jede neue Kante kann auf Originalkante oder Trennpfad zurückgeführt werden.
- Eine Bruch-, Naht- oder Schnittkante verliert ihre Rolle nicht still durch eine boolesche Operation.

## Prüffälle

- Rechteck `100×50 mm`, vertikaler Schnitt bei `x=40`: zwei Flächen `40×50` und `60×50 mm`.
- Zwei Rechtecke mit gemeinsamer Überlappung: Vereinigungsfläche entspricht `A+B−Überlappung`.
- Schneidefläche außerhalb des Subjekts: Differenz ergibt geometrisch unverändertes Subjekt.
- Tangentialer Cutter an einer Ecke: `NO_SPLIT`, keine Nullflächen.
