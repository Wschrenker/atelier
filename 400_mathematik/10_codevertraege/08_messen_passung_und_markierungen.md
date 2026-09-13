# Messen, Passung und Markierungen

**Status:** `bereit` für allgemeine Zuordnung; fachliche Mehrweite und Toleranz kommen aus dem Funktionsvertrag.

**Herleitung:** [`12_kurvenlaenge_und_passung.md`](../90_recherche/12_kurvenlaenge_und_passung.md); die Unterscheidung von Nahtlinie, Schnittlinie und genähtem Zustand ist technischer Vertrag.

## Begriffe

- **Nahtlinie:** Strecke, die später zusammengenäht wird.
- **Schnittlinie:** Kontur einschließlich Nahtzugabe.
- **genähter Zustand:** Geometrie nach Schließen von Abnähern/Falten oder anderen formverändernden Nähten.

Nahtpassung wird auf der Nahtlinie im genähten Zustand geprüft, nicht automatisch auf der offenen Papierkante oder Schnittlinie.

## Zielprimitiven

```python
path_length(path, *, tolerance) -> float
point_at_path_length(path, distance_mm, *, tolerance) -> PathPosition
normalized_path_position(path, distance_mm, *, tolerance) -> float
transfer_position(source_path, target_path, source_distance_mm, *, mode, tolerance) -> PathPosition
compare_seam_lengths(a, b, *, required_ease_mm: float | None, allowed_difference_mm, tolerance) -> SeamMatch
```

Ein Pfad kann aus Linien, Kreisbögen und Beziersegmenten bestehen. Seine Länge ist die Summe der Segmentlängen.

## Positionsmodelle

Absolute Position:

```text
s in mm entlang des Pfades
```

Relative Position:

```text
u = s / Gesamtlänge, 0≤u≤1
```

Übertragung erfolgt nur mit benanntem Modus:

- `ABSOLUTE_LENGTH`: derselbe Millimeterabstand vom Startpunkt;
- `RELATIVE_FRACTION`: derselbe relative Anteil;
- `FROM_END`: Abstand vom Pfadende;
- fachlich festgelegte Paarung von Teilstrecken.

Die Mathematik darf keinen Modus erraten.

## Nahtvergleich

```text
difference_mm = length_b - length_a
matches = |difference_mm - required_ease_mm| ≤ allowed_difference_mm
```

`required_ease_mm` und die erlaubte Abweichung sind fachliche Eingaben. `SeamMatch` enthält mindestens `length_a_mm`, `length_b_mm`, `difference_mm`, `required_ease_mm`, `residual_mm` und `matches: bool | None`. Ohne belegte Mehrweite wird `required_ease_mm=None`, die rohe Differenz berichtet und `matches=None` gesetzt; es entsteht kein erfundenes Passungsurteil.

## Markierungen

Knipse und Bohrpunkte speichern mindestens:

- Trägerpfad und Seite;
- Abstand `s` vom festgelegten Pfadstart;
- Art und fachliche Bedeutung;
- Quelle;
- optional Paarungs-ID zur Gegennaht.

Nach einer formtreuen Transformation wird die Markierung mittransformiert. Nach einer Konturänderung muss ihre Pfadposition neu bestimmt oder bewusst für ungültig erklärt werden.

## Sonderfälle

- leerer Pfad → `DegenerateGeometryError`;
- Strecke außerhalb des Pfades → Bereichsfehler, kein stilles Klemmen;
- Nullpfad kann keine relative Position besitzen;
- uneindeutige Pfadrichtung → Vertrag vor Übertragung offen;
- Abnäherkante im offenen statt geschlossenen Zustand → falsche Beweisstufe, Prüfung abbrechen.

## Invarianten

- `point_at_path_length(path,0)` ist der Startpunkt.
- Position bei Gesamtlänge ist der Endpunkt.
- Pfadlänge ist unabhängig von der Darstellungsabtastung innerhalb der Messtoleranz.
- Paarige Knipse erscheinen in derselben fachlich gewählten Reihenfolge.
- Nahtvergleich verändert keine Geometrie.

## Prüffälle

- Pfad aus Linien `30 mm + 40 mm` hat Länge `70 mm`.
- Position `35 mm` liegt `5 mm` im zweiten Segment.
- Relative Hälfte eines `100-mm`-Pfades entspricht `50 mm`.
- Nähte `500.0` und `505.0 mm` ergeben rohe Differenz `+5.0 mm`; Passung bleibt ohne fachliche Mehrweitenregel unbewertet.
