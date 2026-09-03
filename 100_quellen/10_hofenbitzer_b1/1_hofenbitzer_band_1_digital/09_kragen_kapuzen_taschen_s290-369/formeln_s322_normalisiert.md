# Fachlich normalisierte Formeln — S. 322

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s322.md`  
Originaltranskript: `s322.md`  
Buchseite: Hofenbitzer, Band 1, S. 322

## HOF-B1-S322-F01 — Hintere Kragenbreite beim fallenden Revers

- **Fachlicher Zweck:** Zulässige hintere Kragenbreite aus der hinteren Stegbreite bestimmen.
- **Quelle:** `formeln_s322.md`, Extraktzeile 19; Originaltranskript `s322.md`, Zeile 31; Buchseite 322.
- **Originalbezeichnung:** `hKrB = mind. hStegB + 1 cm bis max. 7 cm`
- **Normalisierte Bezeichnung:** `hintere_kragenbreite_fallendes_revers`

### Buchfassung
```text
- hKrB = mind. hStegB + 1 cm bis max. 7 cm
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
`hintere_kragenbreite` — sichtbare hintere Kragenbreite hKrB, in cm.

- **Abhängigkeiten:** `hintere_stegbreite`.
- **Gültigkeitsbereich:** Reverskragen an fallendem Fasson auf S. 322.
- **Gültigkeitsbedingung:** `hintere_kragenbreite >= hintere_stegbreite + 1 cm` und `<= 7 cm`.
- **Offene Fragen oder Widersprüche:** Auswahlregel innerhalb des Bereichs fehlt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Untere und obere Grenze getrennt prüfen; keinen Wert innerhalb des Bereichs automatisch auswählen.

## HOF-B1-S322-F02 — Hintere Kragenbreite mit X-Zehntel

- **Fachlicher Zweck:** Einen zehnten Anteil des Abstands X zur gewünschten hinteren Kragenbreite addieren.
- **Quelle:** `formeln_s322.md`, Extraktzeilen 24–26; Originaltranskript `s322.md`, Zeilen 42–44; Buchseite 322.
- **Originalbezeichnung:** `gewünschte hKrB + ⅒ X`; die Bezeichnungszeile ist im Extrakt nicht enthalten.
- **Normalisierte Bezeichnung:** `hintere_kragenbreite_mit_x_zehntel`

### Buchfassung
```text
- = 3,5 cm + 4,8 cm : 10
- = 3,5 cm + 0,5 cm
- = 4,0 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hintere_kragenbreite` | hKrB | 3,5 | cm |
| `abstand_x` | X | 4,8 | cm |
| `x_anteil` | ⅒ | 1/10 | dimensionslos |

### Formel und Rechenschritte
```text
hintere_kragenbreite_mit_x_anteil = hintere_kragenbreite + (abstand_x / 10)
                                   = 3,5 cm + (4,8 cm / 10)
                                   = 3,5 cm + 0,48 cm
                                   = 3,98 cm
```

Gedruckt wird der Zwischenwert auf `0,5 cm` und anschließend `4,0 cm`. Die Buchfassung bleibt unverändert; eine Rundungsregel ist nicht belegt.

### Ausgabe
`hintere_kragenbreite_mit_x_anteil` — Abtraglänge, gedruckt `4,0 cm`; ungerundet `3,98 cm`.

- **Abhängigkeiten:** hKrB und X.
- **Gültigkeitsbereich:** Konstruktion am Vorderteil, fallendes Revers, S. 322.
- **Offene Fragen oder Widersprüche:** Exakte Rechnung und gedruckter Rechenweg unterscheiden sich durch die nicht erklärte Rundung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Dezimal- oder rationale Rechnung verwenden und exakten sowie gedruckten Wert getrennt speichern.

## Ausgeschlossene Kandidaten

| Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Maßstabsfaktor ohne fachliche Zielberechnung |
| 14 | 1 | Seitliche Stegbreite als Eingabebereich und direkte Abtragsanweisung |
| 27–28 | 2 | X-Messung und Stegbreitenbereich als Eingaben |
| 33 | 1 | Halslochverbreiterungsbereich als Eingabe |
| 38 | 1 | Begriffsdefinition `Fasson`; keine Rechenoperation |
| **Summe** | **6** | **Eingabe-, Maßstabs- und Definitionsangaben ausgeschlossen** |
