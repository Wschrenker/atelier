# Fachlich normalisierte Formeln — S. 323

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s323.md`  
Originaltranskript: `s323.md`  
Buchseite: Hofenbitzer, Band 1, S. 323

## HOF-B1-S323-F01 — Hintere Stegbreite aus seitlicher Stegbreite

- **Fachlicher Zweck:** Hintere Stegbreite aus der seitlichen Stegbreite und einem Zuschlag bestimmen.
- **Quelle:** `formeln_s323.md`, Extraktzeilen 14 und 20; Originaltranskript `s323.md`, Zeilen 31 und 41; Buchseite 323.
- **Originalbezeichnung:** `hStegB = sStegB + 0,5 cm`
- **Normalisierte Bezeichnung:** `hintere_stegbreite_aus_seitlicher_stegbreite`

### Buchfassung
```text
13. die hStegB = sStegB + 0,5 cm abtragen. Dann den Kragenbruch in den Reb einlaufend formen.
```

```text
- hStegB = sStegB + 0,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `seitliche_stegbreite` | sStegB | variabel | cm |
| `hinterer_steg_zuschlag` | + 0,5 cm | 0,5 | cm |

### Formel und Rechenschritte
```text
hintere_stegbreite = seitliche_stegbreite + 0,5 cm
```

### Ausgabe
`hintere_stegbreite` — hStegB, in cm.

- **Abhängigkeiten:** `seitliche_stegbreite`.
- **Gültigkeitsbereich:** Fallendes Revers, S. 323.
- **Offene Fragen oder Widersprüche:** Keine für die additive Beziehung; die Zeichnungsanwendung bleibt geometrischer Konstruktionsschritt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zuschlag als festen Wert von `0,5 cm` führen.

## HOF-B1-S323-F02 — Hintere Kragenbreite aus hinterer Stegbreite

- **Fachlicher Zweck:** Hintere Kragenbreite mit Mindestzuschlag und Obergrenze angeben.
- **Quelle:** `formeln_s323.md`, Extraktzeilen 15 und 21; Originaltranskript `s323.md`, Zeilen 32 und 42; Buchseite 323.
- **Originalbezeichnung:** `hKrB = mind. hStegB + 1 cm bis max. 7 cm`
- **Normalisierte Bezeichnung:** `hintere_kragenbreite_aus_hinterer_stegbreite_fallendes_revers`

### Buchfassung
```text
14. Die hKrB = mind. hStegB + 1 cm bis max. 7 cm abtragen.
```

```text
- hKrB = hStegB + 1 cm bis max. 7 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hintere_stegbreite` | hStegB | variabel | cm |
| `minimaler_zuschlag` | + 1 cm | 1 | cm |
| `maximale_hintere_kragenbreite` | max. 7 cm | 7 | cm |

### Formel und Rechenschritte
```text
hintere_kragenbreite_min = hintere_stegbreite + 1 cm
hintere_kragenbreite_max = 7 cm
```

### Ausgabe
`hintere_kragenbreite` — hKrB, in cm.

- **Abhängigkeiten:** hStegB.
- **Gültigkeitsbereich:** Fallendes Revers, S. 323.
- **Offene Fragen oder Widersprüche:** Die Auswahl innerhalb des zulässigen Bereichs ist nicht belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereichsprüfung statt automatischer Auswahl implementieren.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Maßstabsfaktor ohne fachliche Zielberechnung |
| **Summe** | **1** | **Maßstabsangabe ausgeschlossen** |
