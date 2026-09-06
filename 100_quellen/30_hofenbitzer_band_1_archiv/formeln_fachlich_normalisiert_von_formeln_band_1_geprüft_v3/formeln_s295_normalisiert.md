# Fachlich normalisierte Formeln — S. 295

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s295.md`  
Originaltranskript: `s295.md`  
Buchseite: Hofenbitzer, Band 1, S. 295

## HOF-B1-S295-F01 — Kragenbreite aus Stegbreite bei halsfernen Kragen

- **Fachlicher Zweck:** Die Kragenbreite aus Stegbreite und modellabhängigem Zuschlag bestimmen.
- **Quelle:** `formeln_s295.md`, Zeilen 14, 19, 24 und 29; Originaltranskript `s295.md`, Zeilen 32, 38, 42 und 46; Buchseite 295.
- **Originalbezeichnung:** `KrB = StegB + 1 bis 2 cm`, `KrB = StegB + 1,5 bis 2,5 cm`, `KrB = StegB + 2 bis 3 cm`
- **Normalisierte Bezeichnung:** `kragenbreite_aus_stegbreite_halsfern`

### Buchfassung

```text
KrB = StegB + 1 bis 2 cm
KrB = StegB + 1,5 bis 2,5 cm
KrB = StegB + 2 bis 3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `stegbreite` | StegB | variabel | cm |
| `kragen_zuschlag` | `1 bis 2 cm`, `1,5 bis 2,5 cm` oder `2 bis 3 cm` | Bereich | cm |

### Formel und Rechenschritte

```text
kragenbreite = stegbreite + kragen_zuschlag
```

Die drei Zuschlagsbereiche bleiben als getrennte Buchvarianten erhalten.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kragenbreite` | Kragenbreite der jeweiligen Variante | cm |

- **Abhängigkeiten:** StegB und gewählte Kragenvariante.
- **Gültigkeitsbereich:** Halsferne einteilige Umlegekragen.
- **Technische Randbedingung:** Nur einen der drei Bereiche je Modellvariante verwenden.
- **Offene Fragen oder Widersprüche:** Die Quelle legt keine automatische Zuordnung von Stegbreite und Zuschlagsbereich fest.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Variante und Zuschlagsbereich getrennt speichern.

## Ausgeschlossene Kandidaten

| Extraktzeilen | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9, 29, 38, 42, 46 | 4 | Direkte Halsloch-Längen, Tiefstellungen und sonstige Zeichnungsangaben ohne eigenständige Zielberechnung |
| **Summe** | **4** | **Eingabe- und Konstruktionsangaben ausgeschlossen** |
