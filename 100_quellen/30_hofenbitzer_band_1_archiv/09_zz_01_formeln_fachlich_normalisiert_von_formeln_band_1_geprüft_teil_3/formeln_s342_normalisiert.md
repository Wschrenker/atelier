# Fachlich normalisierte Formeln — S. 342

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s342.md`  
Originaltranskript: `s342.md`  
Buchseite: Hofenbitzer, Band 1, S. 342

## HOF-B1-S342-F01 — Abstand zur Schulterlinie

- **Fachlicher Zweck:** Abstand der Schulterlinie aus der vorderen Halslochlänge bestimmen.
- **Quelle:** `formeln_s342.md`, Extraktzeile 25; Originaltranskript `s342.md`, Zeile 50.

### Buchfassung
```text
- `14,4 cm · 3 : 5 = 8,6 cm`
```

### Eingaben
`vordere_halsloechlänge` = 14,4 cm; gewählter Anteil = 3/5.

### Formel und Rechenschritte
```text
abstand_zur_schulterlinie = vordere_halsloechlänge · 3 / 5
```

### Ausgabe
Abstand zur SuLi, in cm.

- **Offene Fragen oder Widersprüche:** Die Quelle zeigt den gewählten Bereich ⅖ bis ⅘, berechnet hier aber den Zwischenwert ⅗.
- **Status:** `normalisiert`

## HOF-B1-S342-F02 — Abstand zur oberen Linie

- **Quelle:** `formeln_s342.md`, Extraktzeile 30; Originaltranskript `s342.md`, Zeile 52.

### Buchfassung
```text
- `8,6 cm : 3 = 3,8 cm`
```

### Formel und Rechenschritte
```text
abstand_zur_oberen_linie = abstand_zur_schulterlinie / 3
```

### Ausgabe
Abstand zur oLi, in cm.

- **Status:** `normalisiert`

## HOF-B1-S342-F03 — Kapuzenhöhe

### Buchfassung
```text
9. □6 Darauf die Kapuzenhöhe (KapH) = ½ üKoU + 2 bis 5 cm von der SuLi nach oben abtragen.
```

```text
- Kapuzenhöhe (KapH) = ½ üKoU + 2 bis 5 cm
```

### Formel und Rechenschritte
```text
kapuzenhöhe_min = überkopfumfang / 2 + 2 cm
kapuzenhöhe_max = überkopfumfang / 2 + 5 cm
```

- **Status:** `normalisiert`

## HOF-B1-S342-F04 — Kapuzentiefe

### Buchfassung
```text
10. Die Kapuzentiefe (= KapH – 2 bis 6 cm) nach links abwinkeln.
```

```text
- Kapuzentiefe (KapT) = KapH – ca. 2 bis 6 cm
```

### Formel und Rechenschritte
```text
kapuzentiefe_max = kapuzenhöhe - 2 cm
kapuzentiefe_min = kapuzenhöhe - 6 cm
```

- **Offene Fragen:** Die Auswahl innerhalb des Bereichs ist nicht belegt.
- **Status:** `normalisiert`

```text
- Kapuzenhöhe (KapH) = ½ üKoU + 2 bis 5 cm
```

```text
- Kapuzentiefe (KapT) = KapH – ca. 2 bis 6 cm
```

Die beiden Blöcke sind zusätzliche exakte Buchnachweise derselben Beziehungen.

## Ausgeschlossene Kandidaten

| Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9, 14–15 | 3 | direkte Maß-/Eingabewerte ohne Rechenoperation |
| 20 | 1 | erläuternder Konstruktionskontext ohne Rechenoperation |
| **Summe** | **4** | **Maß- und Kontextangaben ausgeschlossen** |

Die Buchfassung der wiederholten Zusammenfassung auf Extraktzeilen 41–42 ist in F03/F04 als zusätzlicher exakter Nachweis vertreten.
