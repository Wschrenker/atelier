# Format und Status mathematischer Codeverträge

## Ziel

Ein Vertrag muss so genau sein, dass ein Coding-Agent daraus eine kleine reine Python-Funktion und deren Tests erstellen kann, ohne fachliche Werte zu erfinden.

## Pflichtfelder je Primitive

Mehrere eng verwandte Primitive dürfen gemeinsame Pflichtfelder auf Ebene ihrer Vertragsfamilie verwenden. Abweichende Eingaben, Zustände oder Fehler müssen unmittelbar beim jeweiligen Primitiv stehen.

1. **Zweck** — eine klar begrenzte mathematische Aufgabe.
2. **Eingaben** — Typ, Einheit und Bedeutung.
3. **Ausgabe** — Typ, Einheit und Ergebniszustände.
4. **Formel/Algorithmus** — nachvollziehbar und sprachunabhängig.
5. **Vorbedingungen** — was vor dem Aufruf gelten muss.
6. **Sonderfälle** — Null-Länge, Parallelität, Tangentialität, Mehrdeutigkeit usw.
7. **Invarianten** — Eigenschaften, die jedes Ergebnis erfüllen muss.
8. **Prüffälle** — konkrete Zahlen sowie erwartete Ergebnisse.
9. **Quellenbezug** — mathematische Referenz oder vorhandene Recherche.
10. **Status** — `bereit`, `offen` oder `gesperrt`.

## Status

- `bereit`: vollständig genug für RED–GREEN–REFACTOR im konkreten Python-Modul.
- `offen`: allgemeine Methode bekannt, aber eine technische oder fachliche Auswahl fehlt.
- `gesperrt`: widersprüchliche Anforderungen oder Quelle; nicht implementieren.

`bereit` bedeutet nur **implementierbar**, nicht bereits programmiert, fachlich freigegeben oder physisch geprüft.

## Gemeinsame Ergebnisdatentypen

Die konkreten Python-Namen dürfen beim ersten Modulbau angepasst werden; die Felder und Zustände bleiben verbindlich:

```python
Projection(point, line_parameter, distance_mm)
IntersectionResult(kind, points, parameters_a, parameters_b)
PathPosition(point, segment_index, local_parameter, distance_mm, fraction)
ValidationIssue(code, message, geometry_ref)
ValidationResult(valid, issues)
RotationResult(points, angle_deg, state, provenance)
SplitResult(polygons, shared_edges, edge_provenance, state)
```

- `kind` und `state` verwenden die im Einzelvertrag genannten Enum-Werte.
- Nicht vorhandene Parameter werden als `None` bzw. leere unveränderliche Tupel ausgegeben, nicht durch Ersatzwerte.
- Jede Längenangabe trägt `_mm`, jeder Winkel `_deg` oder `_rad`.
- Spezifische Verträge dürfen Felder ergänzen, aber diese Bedeutung nicht still ändern.

## Ergebnis statt stiller Ersatzwerte

Mehrdeutige Geometrie verwendet explizite Zustände, beispielsweise:

```text
UNIQUE | NONE | PARALLEL | COINCIDENT | TANGENT | TWO_POINTS
```

Ein paralleler Geradenschnitt darf nicht einfach einen vorhandenen Endpunkt zurückgeben. Eine Nullkante darf nicht normalisiert oder versetzt werden.

## Toleranzen

Es gibt keinen fachübergreifenden Zauberwert. Ein Aufruf benennt den Zweck:

```text
comparison_abs_tol_mm
flatness_tol_mm
closure_tol_mm
length_match_tol_mm
```

Fachliche Akzeptanztoleranzen kommen aus dem jeweiligen Funktionsvertrag. Numerische Toleranzen verhindern nur Fehlentscheidungen durch Gleitkomma-Arithmetik.

## Python-Zielbild

- unveränderliche Datenträger (`@dataclass(frozen=True)`);
- reine Funktionen ohne versteckte globale Zustände;
- endliche `float`-Werte intern in Millimetern;
- strukturierte Ergebnisse oder eigene Exceptions;
- keine Rundung innerhalb der Geometriekette;
- Tests gegen Zahlenbeispiele **und** Invarianten.
