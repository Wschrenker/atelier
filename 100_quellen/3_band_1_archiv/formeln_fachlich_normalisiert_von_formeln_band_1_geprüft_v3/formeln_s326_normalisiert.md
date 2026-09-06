# Fachlich normalisierte Formeln — S. 326

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s326.md`  
Originaltranskript: `s326.md`  
Buchseite: Hofenbitzer, Band 1, S. 326

## HOF-B1-S326-F01 — Hintere Stegbreite beim steigenden Revers

- **Fachlicher Zweck:** Hintere Stegbreite aus der seitlichen Stegbreite bestimmen.
- **Quelle:** `formeln_s326.md`, Extraktzeile 16; Originaltranskript `s326.md`, Zeile 32; Buchseite 326.
- **Originalbezeichnung:** `hStegB = sStegB + 0,5 cm`
- **Normalisierte Bezeichnung:** `hintere_stegbreite_steigendes_revers`

### Buchfassung
```text
- hStegB = sStegB + 0,5 cm
```

### Eingaben
`seitliche_stegbreite` (sStegB), variabel, cm; Zuschlag `0,5 cm`, cm.

### Formel und Rechenschritte
```text
hintere_stegbreite = seitliche_stegbreite + 0,5 cm
```

### Ausgabe
`hintere_stegbreite` — hStegB, cm.

- **Abhängigkeiten:** sStegB.
- **Gültigkeitsbereich:** Steigendes Revers, S. 326.
- **Offene Fragen oder Widersprüche:** Keine für die additive Beziehung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Festen Zuschlag von `0,5 cm` verwenden.

## HOF-B1-S326-F02 — Hintere Kragenbreite beim steigenden Revers

- **Fachlicher Zweck:** Mindest- und Höchstbereich der hinteren Kragenbreite festlegen.
- **Quelle:** `formeln_s326.md`, Extraktzeilen 14–15; Originaltranskript `s326.md`, Zeilen 30–31; Buchseite 326.
- **Originalbezeichnung:** `hKrB = mind. hStegB + 1 cm bis max. 7 cm`
- **Normalisierte Bezeichnung:** `hintere_kragenbreite_steigendes_revers`

### Buchfassung
```text
- hKrB = mind. hStegB + 1 cm bis max. 7 cm
```

```text
- hKrB = hStegB + 1 cm bis max. 7 cm
```

### Eingaben
`hintere_stegbreite` (hStegB), variabel, cm; Mindestzuschlag `1 cm`, cm; Obergrenze `7 cm`, cm.

### Formel und Rechenschritte
```text
hintere_kragenbreite_min = hintere_stegbreite + 1 cm
hintere_kragenbreite_max = 7 cm
```

### Ausgabe
`hintere_kragenbreite` — hKrB, cm.

- **Abhängigkeiten:** hStegB.
- **Gültigkeitsbereich:** Steigendes Revers, S. 326.
- **Offene Fragen oder Widersprüche:** Auswahl innerhalb des Bereichs fehlt; die zwei Buchzeilen sind zwei Nachweise derselben Beziehung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereich prüfen, nicht automatisch wählen.

## Ausgeschlossene Kandidaten

| Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Maßstabsfaktor ohne fachliche Zielberechnung |
| 21 | 1 | X-Messung als Eingabewert |
| 22 | 1 | Fassondefinition ohne Rechenoperation |
| **Summe** | **3** | **Maßstabs-, Eingabe- und Definitionsangaben ausgeschlossen** |
