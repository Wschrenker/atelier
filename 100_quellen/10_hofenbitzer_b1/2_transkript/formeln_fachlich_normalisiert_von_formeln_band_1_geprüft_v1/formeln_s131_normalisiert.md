# Fachlich normalisierte Formeln — S. 131

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/formeln_s131.md`
Originaltranskript: `../Band_1_geprüft_v1/s131.md`
Buchseite: Hofenbitzer, Band 1, S. 131

## HOF-B1-S131-F01 — Vorderhosenbreite mit halbem Bundfalteninhalt

- **Fachlicher Zweck:** Die für den vorderen Hosenausschnitt verbreiterte Vorderhosenbreite bestimmen.
- **Quelle:** `formeln_s131.md`, Zeile 9; Originaltranskript `s131.md`, Zeile 19; Buchseite 131.
- **Originalbezeichnung:** `vHoB1 = vHoB + ½ gewünschter Bundfalteninhalt`
- **Normalisierte Bezeichnung:** `vorderhosenbreite_mit_halbem_bundfalteninhalt`

### Buchfassung

```text
- vHoB1 = vHoB + ½ gewünschter Bundfalteninhalt
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderhosenbreite` | vHoB | 23,2 | cm |
| `bundfalteninhalt_gesamt` | gewünschter Bundfalteninhalt | 6 | cm |
| `anteil_vorderhosenbreite` | ½ | 0,5 | dimensionslos |

### Formel und Rechenschritte

```text
vorderhosenbreite_bundfalte = vorderhosenbreite
                              + (bundfalteninhalt_gesamt * anteil_vorderhosenbreite)
                            = 23,2 cm + (6 cm * 0,5)
                            = 26,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderhosenbreite_bundfalte` | vHoB1 | 26,2 | cm |

- **Abhängigkeiten:** Vorderhosenbreite und festgelegter gesamter Bundfalteninhalt.
- **Gültigkeitsbereich:** Grundgerüst der Bundfaltenhose auf S. 130–131.
- **Technische Randbedingung:** Nur die Hälfte des gesamten Bundfalteninhalts verbreitert die gemessene Vorderhosenbreite bis `vHoB1`.
- **Offene Fragen oder Widersprüche:** Keine; `23,2 + 6 / 2 = 26,2`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Halbierungsfaktor ausdrücklich führen und nicht mit der späteren Verteilung auf einzelne Falten verwechseln.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s131.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Ausdruck `HüU : 20 +3 cm`; Wiederholung von `HOF-B1-S125-F01`, weiterhin ohne geometrischen Referenten |
| Zeilen 19 und 29 | 2 | Sprachliche Gleichsetzung von Vorderhosen-Bruch, FL und Bügelkante; keine Rechenformel |
| Zeile 24 | 1 | Zeichnungswiederholung von `HOF-B1-S130-F04` mit Wertebereichen |
| Zeile 34 | 1 | Zeichnungswiederholung von `HOF-B1-S130-F03` |
| **Summe** | **5** | **3 Wiederholungen und 2 Begriffslabels ausgeschlossen** |
