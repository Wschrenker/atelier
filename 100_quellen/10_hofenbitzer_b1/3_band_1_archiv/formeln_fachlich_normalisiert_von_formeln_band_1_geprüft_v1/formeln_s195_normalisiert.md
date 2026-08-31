# Fachlich normalisierte Formeln — S. 195

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/06_grundschnitte_oberteile_s171-196/formeln_s195.md`
Originaltranskript: `../hofenbitzer_band_1_digital/06_grundschnitte_oberteile_s171-196/s195.md`
Buchseite: Hofenbitzer, Band 1, S. 195

## HOF-B1-S195-F01 — Schulterbreiten-Zugabedifferenz von PK 3 zu PK 9

- **Fachlicher Zweck:** Die zusätzliche Schulterbreiten-Zugabe beim Wechsel von PK 3 zu PK 9 bestimmen.
- **Quelle:** `formeln_s195.md`, Zeilen 9–11; Originaltranskript `s195.md`, Zeilen 23–25; Buchseite 195.
- **Originalbezeichnung:** `PK 9 − PK 3 = Differenz`
- **Normalisierte Bezeichnung:** `schulterbreiten_zugabedifferenz_pk3_zu_pk9`

### Buchfassung

```text
- PK 3: 0,3 cm
- PK 9: 0,9 cm
- Differenz = 0,6 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `schulterbreite_zugabe_pk3` | Zugabe zur SuB, PK 3 | 0,3 | cm |
| `schulterbreite_zugabe_pk9` | Zugabe zur SuB, PK 9 | 0,9 | cm |

### Formel und Rechenschritte

```text
schulterbreiten_zugabedifferenz = schulterbreite_zugabe_pk9 - schulterbreite_zugabe_pk3
                                 = 0,9 cm - 0,3 cm
                                 = 0,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `schulterbreiten_zugabedifferenz` | fehlende SuB-Zugabe von PK 3 zu PK 9 | 0,6 | cm |

- **Abhängigkeiten:** SuB-Zugaben der Passformklassen 3 und 9.
- **Gültigkeitsbereich:** Erweiterung eines erprobten PK-3-Oberteil-Grundschnitts auf PK 9.
- **Technische Randbedingung:** Zielzugabe minus Ausgangszugabe rechnen.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ausgangs- und Ziel-Passformklasse als getrennte Eingaben führen.

## HOF-B1-S195-F02 — Neue vordere Schulternahtlänge

- **Fachlicher Zweck:** Die neue vordere Schulternahtlänge aus alter Länge und SuB-Zugabedifferenz bilden.
- **Quelle:** `formeln_s195.md`, Zeilen 16–18; Originaltranskript `s195.md`, Zeilen 30–32; Buchseite 195.
- **Originalbezeichnung:** `neue vSuN = alte vSuN + Diff`
- **Normalisierte Bezeichnung:** `neue_vordere_schulternahtlaenge_pk9`

### Buchfassung

```text
neue vSuN = alte vSuN + Diff
           = 12,5 + 0,6 cm
           = 13,1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `alte_vordere_schulternahtlaenge` | alte vSuN | 12,5 | cm |
| `schulterbreiten_zugabedifferenz` | Diff | 0,6 | cm |

### Formel und Rechenschritte

```text
neue_vordere_schulternahtlaenge = alte_vordere_schulternahtlaenge + schulterbreiten_zugabedifferenz
                                 = 12,5 cm + 0,6 cm
                                 = 13,1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `neue_vordere_schulternahtlaenge` | neue vSuN | 13,1 | cm |

- **Abhängigkeiten:** Alte vSuN und `HOF-B1-S195-F01`.
- **Gültigkeitsbereich:** Schulternahtkorrektur beim Öffnen des PK-3-Grundschnitts auf PK 9.
- **Technische Randbedingung:** Die Differenz wird einmal zur alten vSuN addiert.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Alte und neue Schulternahtlänge getrennt speichern.

## HOF-B1-S195-F03 — Neue hintere Schulternahtlänge mit Einhalteweite

- **Fachlicher Zweck:** Die neue hintere Schulternahtlänge aus neuer vSuN und Einhalteweite bilden.
- **Quelle:** `formeln_s195.md`, Zeilen 23–25; Originaltranskript `s195.md`, Zeilen 34–36; Buchseite 195.
- **Originalbezeichnung:** `neue hSuN = neue vSuN + EW`
- **Normalisierte Bezeichnung:** `neue_hintere_schulternahtlaenge_pk9`

### Buchfassung

```text
neue hSuN = neue vSuN + EW
           = 13,1 cm + 0,7 cm
           = 13,8 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `neue_vordere_schulternahtlaenge` | neue vSuN | 13,1 | cm |
| `einhalteweite_schulter` | EW | 0,7 | cm |

### Formel und Rechenschritte

```text
neue_hintere_schulternahtlaenge = neue_vordere_schulternahtlaenge + einhalteweite_schulter
                                 = 13,1 cm + 0,7 cm
                                 = 13,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `neue_hintere_schulternahtlaenge` | neue hSuN | 13,8 | cm |

- **Abhängigkeiten:** `HOF-B1-S195-F02` und gewählte Einhalteweite.
- **Gültigkeitsbereich:** Schulternahtkorrektur beim Öffnen des PK-3-Grundschnitts auf PK 9.
- **Technische Randbedingung:** Die Quelle nennt im Original eine Einhalteweite zwischen 0,5 und 1 cm; im Beispiel werden 0,7 cm verwendet.
- **Offene Fragen oder Widersprüche:** Die Auswahlregel innerhalb des Einhalteweitenbereichs ist nicht belegt; die Beispielrechnung ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einhalteweite als explizite Eingabe mit Bereichsprüfung führen.

## HOF-B1-S195-F04 — Vertiefung der Ärmelpunkte aus der AlT-Differenz

- **Fachlicher Zweck:** Die Ärmelpunkte um drei Viertel der Armlochvertiefung nach unten verschieben.
- **Quelle:** `formeln_s195.md`, Zeilen 30 und 74; Originaltranskript `s195.md`, Zeilen 47 und 103; Buchseite 195.
- **Originalbezeichnung:** `¾ der Vertiefung des Armlochs; ¾ von 2,7 cm = 2,0 cm`
- **Normalisierte Bezeichnung:** `aermelpunkt_vertiefung_aus_alt_differenz`

### Buchfassung

```text
11. Die Ärmelpunkte an beiden Armlöchern um ¾ der Vertiefung des Armlochs (= ¾ Vergrößerung der AlT) nach unten verschieben.
```

```text
- ¾ von 2,7 cm = 2,0 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefen_zugabedifferenz` | Vergrößerung der AlT | 2,7 | cm |
| `aermelpunkt_anteil` | ¾ | 3/4 | dimensionslos |

### Formel und Rechenschritte

```text
aermelpunkt_vertiefung_exakt = armlochtiefen_zugabedifferenz * 3 / 4
                              = 2,7 cm * 3 / 4
                              = 2,025 cm
gedruckte_aermelpunkt_vertiefung = 2,0 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Exakter Wert | Druckwert | Einheit |
|---|---|---:|---:|---|
| `aermelpunkt_vertiefung` | Verschiebung von vÄP und hÄP nach unten | 2,025 | 2,0 | cm |

- **Abhängigkeiten:** AlT-Differenz `2,7 cm` aus `HOF-B1-S194-F08`.
- **Gültigkeitsbereich:** Eingesetzter Ärmel am auf PK 9 vergrößerten Armloch.
- **Technische Randbedingung:** Beide Ärmelpunkte werden um denselben Betrag nach unten verschoben; exakten und gedruckten Wert getrennt erhalten.
- **Offene Fragen oder Widersprüche:** Für `2,025 cm → 2,0 cm` ist keine Rundungsregel belegt; der Druckwert ist mit dem Bruch näherungsweise vereinbar.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Exakten Wert berechnen und eine spätere fachliche Rundungsregel nicht vorwegnehmen.

## HOF-B1-S195-F05 — Taillenweiten-Mehrbetrag mit widersprüchlicher Folgekorrektur

- **Fachlicher Zweck:** Den Mehrbetrag der gemessenen halben Taillenweite gegenüber der Ziel-Taillenweite bestimmen.
- **Quelle:** `formeln_s195.md`, Zeilen 40–41 und 46–49; Originaltranskript `s195.md`, Zeilen 53–60; Buchseite 195.
- **Originalbezeichnung:** `½ TaW − (TaU + Zugabe) : 2 = 0,6 cm Mehrbetrag`
- **Normalisierte Bezeichnung:** `taillenweiten_mehrbetrag_pk9_s195`

### Buchfassung

```text
- PK 3: 4 cm
- PK 9: 16 cm
```

```text
½ TaW − (TaU + Zugabe) : 2
= 44,6 cm − (72 cm + 16 cm) : 2
= 44,6 cm − 44 cm
= 0,6 cm Mehrbetrag
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |
| `taillenweiten_zugabe_pk3` | Zugabe zur TaW, PK 3 | 4 | cm |
| `taillenweiten_zugabe_pk9` | Zugabe zur TaW, PK 9 | 16 | cm |
| `gemessene_halbe_taillenweite` | ½ TaW am geöffneten Schnitt | 44,6 | cm |

### Formel und Rechenschritte

```text
ziel_halbe_taillenweite = (taillenumfang + taillenweiten_zugabe_pk9) / 2
                         = (72 cm + 16 cm) / 2
                         = 44 cm
taillenweiten_mehrbetrag = gemessene_halbe_taillenweite - ziel_halbe_taillenweite
                          = 44,6 cm - 44 cm
                          = 0,6 cm
Folgesatz im Originaltranskript: 0,4 cm sollen am halben Schnitt entfernt werden.
Differenz zwischen Rechenergebnis und Folgesatz: 0,6 cm - 0,4 cm = 0,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Rechenwert | Folgesatz | Einheit |
|---|---|---:|---:|---|
| `taillenweiten_mehrbetrag` | Überschuss der gemessenen halben Taillenweite | 0,6 | 0,4 zu entfernen | cm |

- **Abhängigkeiten:** TaU, PK-9-Zugabe und gemessene ½ TaW.
- **Gültigkeitsbereich:** Taillenweitenkontrolle des von PK 3 auf PK 9 geöffneten Oberteil-Grundschnitts.
- **Technische Randbedingung:** Rechenweg und nachfolgende Korrekturanweisung müssen getrennt erhalten bleiben.
- **Offene Fragen oder Widersprüche:** Die extrahierte Rechnung ergibt eindeutig `0,6 cm Mehrbetrag`; Originaltranskript Zeile 63 und die Zeichnung nennen insgesamt `0,4 cm` Entfernung. Der gültige Korrekturbetrag ist nicht entscheidbar.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht als Korrekturoperation implementieren, bis `0,6 cm` gegenüber `0,4 cm` fachlich geklärt ist.

## HOF-B1-S195-F06 — Hüftweiten-Mehrbetrag mit widersprüchlicher Folgekorrektur

- **Fachlicher Zweck:** Den Mehrbetrag der gemessenen halben Hüftweite gegenüber der Ziel-Hüftweite bestimmen.
- **Quelle:** `formeln_s195.md`, Zeilen 54–55 und 60–63; Originaltranskript `s195.md`, Zeilen 71–78; Buchseite 195.
- **Originalbezeichnung:** `½ HüW − (HüU + Zugabe) : 2 = 1,6 cm Mehrbetrag`
- **Normalisierte Bezeichnung:** `hueftweiten_mehrbetrag_pk9_s195`

### Buchfassung

```text
- PK 3: 4 cm
- PK 9: 12 cm
```

```text
½ HüW − (HüU + Zugabe) : 2
= 56,1 cm − (97 cm + 12 cm) : 2
= 56,1 cm − 54,5 cm
= 1,6 cm Mehrbetrag
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `hueftweiten_zugabe_pk3` | Zugabe zur HüW, PK 3 | 4 | cm |
| `hueftweiten_zugabe_pk9` | Zugabe zur HüW, PK 9 | 12 | cm |
| `gemessene_halbe_hueftweite` | ½ HüW am geöffneten Schnitt | 56,1 | cm |

### Formel und Rechenschritte

```text
ziel_halbe_hueftweite = (hueftumfang + hueftweiten_zugabe_pk9) / 2
                       = (97 cm + 12 cm) / 2
                       = 54,5 cm
hueftweiten_mehrbetrag = gemessene_halbe_hueftweite - ziel_halbe_hueftweite
                        = 56,1 cm - 54,5 cm
                        = 1,6 cm
Folgesatz im Originaltranskript: 0,8 cm sollen am halben Schnitt entfernt werden.
Verhältnis: 1,6 cm / 2 = 0,8 cm; eine Halbierungsbegründung steht nicht im Extrakt.
```

### Ausgabe

| Technische Variable | Bedeutung | Rechenwert | Folgesatz | Einheit |
|---|---|---:|---:|---|
| `hueftweiten_mehrbetrag` | Überschuss der gemessenen halben Hüftweite | 1,6 | 0,8 zu entfernen | cm |

- **Abhängigkeiten:** HüU, PK-9-Zugabe und gemessene ½ HüW.
- **Gültigkeitsbereich:** Hüftweitenkontrolle des von PK 3 auf PK 9 geöffneten Oberteil-Grundschnitts.
- **Technische Randbedingung:** Rechenweg und nachfolgende Korrekturanweisung müssen getrennt erhalten bleiben.
- **Offene Fragen oder Widersprüche:** Die extrahierte Rechnung ergibt `1,6 cm Mehrbetrag`, während Originaltranskript Zeile 81 und die Zeichnung insgesamt `0,8 cm` Entfernung nennen. Die Zahl `0,8 cm` ist die Hälfte des Mehrbetrags, aber die Quelle belegt nicht, warum der bereits am halben Schnitt berechnete Betrag nochmals halbiert wird.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht als Korrekturoperation implementieren, bis Bedeutung und Verteilung von `1,6 cm` gegenüber `0,8 cm` geklärt sind.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s195.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 35 | 1 | Abschnittsüberschrift zur TaW-Zugabe; Bezeichnung, keine Rechenformel |
| Zeilen 68–69 | 2 | Zeichnungsbeschriftungen, welche die in `HOF-B1-S195-F02` und `F03` bereits dargestellten Schulternahtrechnungen wiederholen |
| Zeilen 79 und 84 | 2 | Zeichnungslabels der bereits als Eingaben in `HOF-B1-S195-F05` und `F06` abgebildeten gemessenen Halbweiten |
| **Summe** | **5** | **1 Überschrift und 4 wiederholte Zeichnungs- oder Eingabelabels ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s195.md` enthält außerhalb des verbindlichen Extrakts weitere Konstruktionsangaben: den Einhalteweitenbereich `0,5 bis 1 cm`, die Anweisung zur Armlochneuzeichnung, die Folgesätze zu den Taillen- und Hüftkorrekturen sowie die zeichnerischen Verteilungen `−0,2 cm / −0,2 cm` und `−0,4 cm / −0,4 cm`. Sie wurden nicht als zusätzliche Buchfassungen erzeugt. Die Folgesätze wurden nur zur Widerspruchsprüfung herangezogen: `0,6 cm` Rechenergebnis steht `0,4 cm` Entfernung gegenüber; `1,6 cm` Rechenergebnis steht `0,8 cm` Entfernung gegenüber. Beide Korrekturoperationen bleiben deshalb gesperrt. Der Abschluss von `O06` gilt für den vorhandenen extrahierten Kandidatenbestand.
