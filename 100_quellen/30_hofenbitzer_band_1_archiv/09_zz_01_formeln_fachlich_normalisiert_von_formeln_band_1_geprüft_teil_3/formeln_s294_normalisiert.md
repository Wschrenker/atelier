# Fachlich normalisierte Formeln — S. 294

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s294.md`  
Originaltranskript: `s294.md`  
Buchseite: Hofenbitzer, Band 1, S. 294

## HOF-B1-S294-F01 — Kragenbreite aus Stegbreite

- **Fachlicher Zweck:** Die Kragenbreite über der Stegbreite bestimmen.
- **Quelle:** `formeln_s294.md`, Zeilen 14, 19 und 24; Originaltranskript `s294.md`, Zeilen 41, 49 und 53; Buchseite 294.
- **Originalbezeichnung:** `KrB = StegB + 0,7 bis 1,5 cm`
- **Normalisierte Bezeichnung:** `kragenbreite_aus_stegbreite`

### Buchfassung

```text
KrB = StegB + 0,7 bis 1,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `stegbreite` | StegB | variabel | cm |
| `kragen_zuschlag` | `0,7 bis 1,5 cm` | Bereich | cm |

### Formel und Rechenschritte

```text
kragenbreite = stegbreite + kragen_zuschlag
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kragenbreite` | Breite des Kragens über der Stegbreite | cm |

- **Abhängigkeiten:** StegB und gewählter Zuschlag.
- **Gültigkeitsbereich:** Anliegende einteilige Umlegekragen auf S. 294.
- **Technische Randbedingung:** Der Zuschlag ist ein Bereich und wird nicht automatisch ausgewählt.
- **Offene Fragen oder Widersprüche:** Keine Auswahlregel innerhalb des Bereichs belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zuschlag als expliziten Parameter führen.

## Ausgeschlossene Kandidaten

| Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9, 37 | 1 | Modellbeschreibung und direkte Halsloch-Längen; keine eigenständige Rechenbeziehung |
| **Summe** | **1** | **Kontext- und Maßlabel ausgeschlossen** |
