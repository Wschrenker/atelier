# Fachlich normalisierte Formeln — S. 194

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s194.md`
Originaltranskript: `../Band_1_geprüft_v1/s194.md`
Buchseite: Hofenbitzer, Band 1, S. 194

## HOF-B1-S194-F01 — Rückenbreite mit Zugabe im vorhandenen PK-3-Grundschnitt

- **Fachlicher Zweck:** Die Zugabe zur halben Rückenbreite addieren.
- **Quelle:** `formeln_s194.md`, Zeile 9; Originaltranskript `s194.md`, Zeile 37; Buchseite 194.
- **Originalbezeichnung:** `RüB + 0,5 = RüB+`
- **Normalisierte Bezeichnung:** `rueckenbreite_mit_zugabe_pk3_s194`

### Buchfassung

```text
| RüB | Rückenbreite (½) | 16,5 | 0,5 | RüB+ 17 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_rueckenbreite` | RüB | 16,5 | cm |
| `rueckenbreite_zugabe_pk3` | Zugabe zur RüB, PK 3 | 0,5 | cm |

### Formel und Rechenschritte

```text
rueckenbreite_mit_zugabe = halbe_rueckenbreite + rueckenbreite_zugabe_pk3
                          = 16,5 cm + 0,5 cm
                          = 17 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `rueckenbreite_mit_zugabe` | RüB+ | 17 | cm |

- **Abhängigkeiten:** RüB und PK-3-Zugabe des vorhandenen Grundschnitts.
- **Gültigkeitsbereich:** Vorhandener optimierter Oberteil-Grundschnitt, Größe 38, PK 3.
- **Technische Randbedingung:** RüB ist bereits ein Halbmaß.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Körpermaß, Zugabe und Konstruktionsmaß getrennt speichern.

## HOF-B1-S194-F02 — Armdurchmesser mit Zugabe und Teilwerten im PK-3-Grundschnitt

- **Fachlicher Zweck:** Den Armdurchmesser vergrößern und das Konstruktionsmaß vierteln beziehungsweise dritteln.
- **Quelle:** `formeln_s194.md`, Zeile 10; Originaltranskript `s194.md`, Zeile 38; Buchseite 194.
- **Originalbezeichnung:** `ArD + 1,5 = ArD+; ¼; ⅓`
- **Normalisierte Bezeichnung:** `armdurchmesser_mit_zugabe_und_teilungen_pk3_s194`

### Buchfassung

```text
| ArD | Armdurchmesser | 9,3 | 1,5 | ArD+ 10,8; ¼ 2,7; ⅓ 3,6 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser` | ArD | 9,3 | cm |
| `armdurchmesser_zugabe_pk3` | Zugabe zum ArD, PK 3 | 1,5 | cm |

### Formel und Rechenschritte

```text
armdurchmesser_mit_zugabe = armdurchmesser + armdurchmesser_zugabe_pk3
                           = 9,3 cm + 1,5 cm
                           = 10,8 cm
viertel_armdurchmesser = 10,8 cm / 4 = 2,7 cm
drittel_armdurchmesser = 10,8 cm / 3 = 3,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser_mit_zugabe` | ArD+ | 10,8 | cm |
| `viertel_armdurchmesser` | ¼ ArD+ | 2,7 | cm |
| `drittel_armdurchmesser` | ⅓ ArD+ | 3,6 | cm |

- **Abhängigkeiten:** ArD und PK-3-Zugabe des vorhandenen Grundschnitts.
- **Gültigkeitsbereich:** Vorhandener optimierter Oberteil-Grundschnitt, Größe 38, PK 3.
- **Technische Randbedingung:** Beide Teilwerte aus ArD+ bilden.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** ArD+ einmal berechnen und daraus die Teilwerte ableiten.

## HOF-B1-S194-F03 — Brustbreite mit Zugabe im vorhandenen PK-3-Grundschnitt

- **Fachlicher Zweck:** Die Zugabe zur halben Brustbreite addieren.
- **Quelle:** `formeln_s194.md`, Zeile 11; Originaltranskript `s194.md`, Zeile 39; Buchseite 194.
- **Originalbezeichnung:** `BrB + 1 = BrB+`
- **Normalisierte Bezeichnung:** `brustbreite_mit_zugabe_pk3_s194`

### Buchfassung

```text
| BrB | Brustbreite (½) | 18,2 | 1 | BrB+ 19,2 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_brustbreite` | BrB | 18,2 | cm |
| `brustbreite_zugabe_pk3` | Zugabe zur BrB, PK 3 | 1 | cm |

### Formel und Rechenschritte

```text
brustbreite_mit_zugabe = halbe_brustbreite + brustbreite_zugabe_pk3
                        = 18,2 cm + 1 cm
                        = 19,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `brustbreite_mit_zugabe` | BrB+ | 19,2 | cm |

- **Abhängigkeiten:** BrB und PK-3-Zugabe des vorhandenen Grundschnitts.
- **Gültigkeitsbereich:** Vorhandener optimierter Oberteil-Grundschnitt, Größe 38, PK 3.
- **Technische Randbedingung:** BrB ist bereits ein Halbmaß.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Halbmaßkennzeichnung erhalten.

## HOF-B1-S194-F04 — Kontrolle der halben Brustweite im PK-3-Grundschnitt

- **Fachlicher Zweck:** Die drei Körperbreiten und ihre Zugaben gegen die halbe Brustweite kontrollieren.
- **Quelle:** `formeln_s194.md`, Zeile 12; Originaltranskript `s194.md`, Zeile 40; Buchseite 194.
- **Originalbezeichnung:** `Σ = ½ BrU; 44 + 3 = ½ BrW 47`
- **Normalisierte Bezeichnung:** `kontrolle_halbe_brustweite_pk3_s194`

### Buchfassung

```text
| Kontrolle | Σ = ½ BrU | 44 | 3 | ½ BrW 47 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_rueckenbreite` | RüB | 16,5 | cm |
| `armdurchmesser` | ArD | 9,3 | cm |
| `halbe_brustbreite` | BrB | 18,2 | cm |
| `rueckenbreite_zugabe_pk3` | RüB-Zugabe | 0,5 | cm |
| `armdurchmesser_zugabe_pk3` | ArD-Zugabe | 1,5 | cm |
| `brustbreite_zugabe_pk3` | BrB-Zugabe | 1 | cm |

### Formel und Rechenschritte

```text
halber_brustumfang = 16,5 cm + 9,3 cm + 18,2 cm = 44 cm
breitenzugaben_summe = 0,5 cm + 1,5 cm + 1 cm = 3 cm
halbe_brustweite = 44 cm + 3 cm = 47 cm
Kontrolle: 17 cm + 10,8 cm + 19,2 cm = 47 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `halbe_brustweite_kontrolliert` | ½ BrW | 47 | cm |

- **Abhängigkeiten:** `HOF-B1-S194-F01` bis `HOF-B1-S194-F03`.
- **Gültigkeitsbereich:** Breitenkontrolle des vorhandenen Grundschnitts, Größe 38, PK 3.
- **Technische Randbedingung:** Körperbreiten und Breitenzugaben müssen jeweils vollständig summiert werden.
- **Offene Fragen oder Widersprüche:** Keine; beide Rechenwege stimmen mit dem Druckwert überein.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Gleichheit beider Rechenwege als Invariante prüfen.

## HOF-B1-S194-F05 — Brustbreiten-Zugabedifferenz und hälftige Verteilung

- **Fachlicher Zweck:** Die zusätzliche BrB-Zugabe von PK 3 zu PK 9 bestimmen und gleich auf zwei Öffnungen verteilen.
- **Quelle:** `formeln_s194.md`, Zeilen 27–31; Originaltranskript `s194.md`, Zeilen 67–71; Buchseite 194.
- **Originalbezeichnung:** `PK 9 − PK 3 = Differenz; ½ + ½`
- **Normalisierte Bezeichnung:** `brustbreiten_zugabedifferenz_pk3_zu_pk9`

### Buchfassung

```text
- PK 3: 1,0 cm
- PK 9: 2,0 cm
- Differenz = 1,0 cm
- ½ = 0,5 cm
- ½ = 0,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustbreite_zugabe_pk3` | Zugabe zur BrB, PK 3 | 1,0 | cm |
| `brustbreite_zugabe_pk9` | Zugabe zur BrB, PK 9 | 2,0 | cm |
| `anzahl_oeffnungen_brustbreite` | zwei gleich große Öffnungen | 2 | dimensionslos |

### Formel und Rechenschritte

```text
brustbreiten_zugabedifferenz = brustbreite_zugabe_pk9 - brustbreite_zugabe_pk3
                              = 2,0 cm - 1,0 cm
                              = 1,0 cm
oeffnung_brustbreite_je_stelle = brustbreiten_zugabedifferenz / 2
                                = 1,0 cm / 2
                                = 0,5 cm
Kontrolle: 0,5 cm + 0,5 cm = 1,0 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `brustbreiten_zugabedifferenz` | fehlende BrB-Zugabe von PK 3 zu PK 9 | 1,0 | cm |
| `oeffnung_brustbreite_je_stelle` | Hälfte je Öffnung | 0,5 | cm |

- **Abhängigkeiten:** BrB-Zugaben der Passformklassen 3 und 9.
- **Gültigkeitsbereich:** Erweiterung eines erprobten PK-3-Oberteil-Grundschnitts auf PK 9.
- **Technische Randbedingung:** Die Differenz wird in zwei gleiche Beträge geteilt.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ziel- minus Ausgangszugabe rechnen und die Verteilungssumme kontrollieren.

## HOF-B1-S194-F06 — Armdurchmesser-Zugabedifferenz und Verteilung auf Vorder- und Rückteil

- **Fachlicher Zweck:** Die zusätzliche ArD-Zugabe von PK 3 zu PK 9 bestimmen und im Verhältnis ⅓ zu ⅔ auf VT und RT verteilen.
- **Quelle:** `formeln_s194.md`, Zeilen 41–45 und 74; Originaltranskript `s194.md`, Zeilen 75–79 und 105; Buchseite 194.
- **Originalbezeichnung:** `PK 9 − PK 3 = Differenz; ⅓ am VT; ⅔ am RT`
- **Normalisierte Bezeichnung:** `armdurchmesser_zugabedifferenz_pk3_zu_pk9`

### Buchfassung

```text
- PK 3: 1,5 cm
- PK 9: 5,0 cm
- Differenz = 3,5 cm
- ⅓ = 1,2 cm
- ⅔ = 2,3 cm
```

```text
6. Ein Drittel der ArD-Differenz an der Seitennaht vom VT ausstellen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser_zugabe_pk3` | Zugabe zum ArD, PK 3 | 1,5 | cm |
| `armdurchmesser_zugabe_pk9` | Zugabe zum ArD, PK 9 | 5,0 | cm |
| `anteil_vorderteil` | ⅓ | 1/3 | dimensionslos |
| `anteil_rueckteil` | ⅔ | 2/3 | dimensionslos |

### Formel und Rechenschritte

```text
armdurchmesser_zugabedifferenz = armdurchmesser_zugabe_pk9 - armdurchmesser_zugabe_pk3
                                = 5,0 cm - 1,5 cm
                                = 3,5 cm
exakter_vt_anteil = 3,5 cm / 3 = 1,166666... cm
gedruckter_vt_anteil = 1,2 cm
exakter_rt_anteil = 3,5 cm * 2 / 3 = 2,333333... cm
gedruckter_rt_anteil = 2,3 cm
Kontrolle der Druckwerte: 1,2 cm + 2,3 cm = 3,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Exakter Wert | Druckwert | Einheit |
|---|---|---:|---:|---|
| `armdurchmesser_zugabedifferenz` | fehlende ArD-Zugabe | 3,5 | 3,5 | cm |
| `ausstellung_vorderteil` | ⅓ der Differenz am VT | 1,166666... | 1,2 | cm |
| `ausstellung_rueckteil` | ⅔ der Differenz am RT | 2,333333... | 2,3 | cm |

- **Abhängigkeiten:** ArD-Zugaben der Passformklassen 3 und 9.
- **Gültigkeitsbereich:** Erweiterung eines erprobten PK-3-Oberteil-Grundschnitts auf PK 9.
- **Technische Randbedingung:** Exakte Bruchteile und gedruckte Teilwerte getrennt erhalten; die gedruckten Teilwerte ergeben zusammen die Differenz.
- **Offene Fragen oder Widersprüche:** Die Druckwerte sind gemeinsam konsistent; eine Rundungs- oder Ausgleichsregel für `1,166666... → 1,2` und `2,333333... → 2,3` ist nicht belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Exakte Bruchteile berechnen; die Übernahme der Druckwerte als gesonderte fachliche Rundungsentscheidung behandeln.

## HOF-B1-S194-F07 — Rückenbreiten-Zugabedifferenz und Restöffnung am Rückteil

- **Fachlicher Zweck:** Die zusätzliche RüB-Zugabe von PK 3 zu PK 9 bestimmen und nach der gemeinsamen 0,5-cm-Öffnung den Rest am RT öffnen.
- **Quelle:** `formeln_s194.md`, Zeilen 55–57 und 69; Originaltranskript `s194.md`, Zeilen 83–85 und 103; Buchseite 194.
- **Originalbezeichnung:** `PK 9 − PK 3 = RüB-Differenz; Rest 1 cm am RT`
- **Normalisierte Bezeichnung:** `rueckenbreiten_zugabedifferenz_pk3_zu_pk9`

### Buchfassung

```text
- PK 3: 0,5 cm
- PK 9: 2,0 cm
- Differenz = 1,5 cm
```

```text
4. Am seitlichen RT-Einschnitt den restlichen Differenzbetrag zur RüB-Differenz öffnen (hier 1 cm).
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `rueckenbreite_zugabe_pk3` | Zugabe zur RüB, PK 3 | 0,5 | cm |
| `rueckenbreite_zugabe_pk9` | Zugabe zur RüB, PK 9 | 2,0 | cm |
| `gemeinsame_oeffnung_vt_rt` | Öffnung wie am VT-Halsloch | 0,5 | cm |

### Formel und Rechenschritte

```text
rueckenbreiten_zugabedifferenz = rueckenbreite_zugabe_pk9 - rueckenbreite_zugabe_pk3
                                = 2,0 cm - 0,5 cm
                                = 1,5 cm
restoeffnung_rueckteil = rueckenbreiten_zugabedifferenz - gemeinsame_oeffnung_vt_rt
                        = 1,5 cm - 0,5 cm
                        = 1,0 cm
Kontrolle: 0,5 cm + 1,0 cm = 1,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `rueckenbreiten_zugabedifferenz` | fehlende RüB-Zugabe | 1,5 | cm |
| `restoeffnung_rueckteil` | restlicher Betrag am seitlichen RT-Einschnitt | 1,0 | cm |

- **Abhängigkeiten:** RüB-Zugaben der PK 3 und PK 9 sowie die 0,5-cm-Öffnung aus `HOF-B1-S194-F05`.
- **Gültigkeitsbereich:** Erweiterung eines erprobten PK-3-Oberteil-Grundschnitts auf PK 9.
- **Technische Randbedingung:** Die erste 0,5-cm-Öffnung und der Restbetrag dürfen zusammen die RüB-Differenz nicht überschreiten.
- **Offene Fragen oder Widersprüche:** Keine; der gedruckte Restbetrag stimmt mit der Differenzrechnung überein.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Restbetrag aus Gesamtdifferenz minus bereits geöffneter Weite berechnen.

## HOF-B1-S194-F08 — Armlochtiefen-Zugabedifferenz

- **Fachlicher Zweck:** Die zusätzliche AlT-Zugabe von PK 3 zu PK 9 bestimmen.
- **Quelle:** `formeln_s194.md`, Zeilen 62–64; Originaltranskript `s194.md`, Zeilen 91–93; Buchseite 194.
- **Originalbezeichnung:** `PK 9 − PK 3 = AlT-Differenz`
- **Normalisierte Bezeichnung:** `armlochtiefen_zugabedifferenz_pk3_zu_pk9`

### Buchfassung

```text
- PK 3: 1,3 cm
- PK 9: 4,0 cm
- Differenz = 2,7 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefe_zugabe_pk3` | Zugabe zur AlT, PK 3 | 1,3 | cm |
| `armlochtiefe_zugabe_pk9` | Zugabe zur AlT, PK 9 | 4,0 | cm |

### Formel und Rechenschritte

```text
armlochtiefen_zugabedifferenz = armlochtiefe_zugabe_pk9 - armlochtiefe_zugabe_pk3
                               = 4,0 cm - 1,3 cm
                               = 2,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefen_zugabedifferenz` | Betrag zur Vertiefung des Armlochs | 2,7 | cm |

- **Abhängigkeiten:** AlT-Zugaben der Passformklassen 3 und 9.
- **Gültigkeitsbereich:** Erweiterung eines erprobten PK-3-Oberteil-Grundschnitts auf PK 9.
- **Technische Randbedingung:** Zielzugabe minus Ausgangszugabe rechnen.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Differenz als vertikalen Änderungsbetrag speichern.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s194.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 17 | 1 | Geltungsbereich der Zugabentabelle für ganze beziehungsweise halbe Schnitte; fachlicher Kontext, keine eigenständige Rechenformel |
| Zeilen 22, 36 und 50 | 3 | Abschnittsüberschriften für BrB-, ArD- und RüB-Zugaben; Bezeichnungen, keine Rechenformeln |
| Zeilen 79–80 | 2 | Zeichnungsbeschriftungen, die die in `HOF-B1-S194-F06` bereits dargestellten Druckwerte `⅓ = 1,2 cm` und `⅔ = 2,3 cm` wiederholen |
| **Summe** | **6** | **1 Kontextzeile, 3 Überschriften und 2 wiederholte Zeichnungslabels ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s194.md` enthält außerhalb des verbindlichen Extrakts weitere für die Konstruktion relevante Angaben: die PK-9-Zugabenzeile der Tabelle, die Restaufteilung der RüB-Differenz in den Zeilen 86–87, die zweite ArD-Anweisung mit `⅔` am RT in Zeile 106 sowie die Armlochvertiefung und parallelen Seitennähte. Sie wurden nicht als zusätzliche Buchfassungen erzeugt. Die in `HOF-B1-S194-F06` gemeinsam dargestellten Bruchteile und Druckwerte stammen vollständig aus dem Extrakt; die Anweisung für das Drittel am VT bleibt als eigener exakter Buchfassungsblock erhalten. Der Abschluss von `O05` gilt für den vorhandenen extrahierten Kandidatenbestand.
