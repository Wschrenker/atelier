# Fachlich normalisierte Formeln — S. 120

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s120.md`
Originaltranskript: `../Band_1_geprüft_v1/s120.md`
Buchseite: Hofenbitzer, Band 1, S. 120

## HOF-B1-S120-F01 — Teilwerte des Taillenumfangs

- **Fachlicher Zweck:** Den halben und viertel Taillenumfang aus dem Taillenumfang bestimmen.
- **Quelle:** `formeln_s120.md`, Zeile 9; Originaltranskript `s120.md`, Zeile 36; Buchseite 120.
- **Originalbezeichnung:** `TaU Taillenumfang; ½; ¼`
- **Normalisierte Bezeichnung:** `taillenumfang_teilwerte`

### Buchfassung

```text
| TaU | Taillenumfang | 72 | ½ = 36; ¼ = 18 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |

### Formel und Rechenschritte

```text
halber_taillenumfang = taillenumfang / 2
                      = 72 cm / 2
                      = 36 cm
viertel_taillenumfang = taillenumfang / 4
                       = 72 cm / 4
                       = 18 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `halber_taillenumfang` | ½ TaU | 36 | cm |
| `viertel_taillenumfang` | ¼ TaU | 18 | cm |

- **Abhängigkeiten:** Taillenumfang.
- **Gültigkeitsbereich:** Konstruktionstabelle der Standardhose mit vertieftem Bund, Größe 38, auf S. 120.
- **Technische Randbedingung:** Der Taillenumfang muss als nichtnegative Länge vorliegen.
- **Offene Fragen oder Widersprüche:** Keine; `72 / 2 = 36` und `72 / 4 = 18`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Teilwerte stets aus dem vollständigen Umfang ableiten.

## HOF-B1-S120-F02 — Teilwerte des Hüftumfangs

- **Fachlicher Zweck:** Den halben und viertel Hüftumfang aus dem Hüftumfang bestimmen.
- **Quelle:** `formeln_s120.md`, Zeile 10; Originaltranskript `s120.md`, Zeile 37; Buchseite 120.
- **Originalbezeichnung:** `HüU Hüftumfang; ½; ¼`
- **Normalisierte Bezeichnung:** `hueftumfang_teilwerte`

### Buchfassung

```text
| HüU | Hüftumfang | 97 | ½ = 48,5; ¼ = 24,25 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |

### Formel und Rechenschritte

```text
halber_hueftumfang = hueftumfang / 2
                    = 97 cm / 2
                    = 48,5 cm
viertel_hueftumfang = hueftumfang / 4
                     = 97 cm / 4
                     = 24,25 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `halber_hueftumfang` | ½ HüU | 48,5 | cm |
| `viertel_hueftumfang` | ¼ HüU | 24,25 | cm |

- **Abhängigkeiten:** Hüftumfang.
- **Gültigkeitsbereich:** Konstruktionstabelle der Standardhose mit vertieftem Bund, Größe 38, auf S. 120.
- **Technische Randbedingung:** Der Hüftumfang muss als nichtnegative Länge vorliegen.
- **Offene Fragen oder Widersprüche:** Keine; `97 / 2 = 48,5` und `97 / 4 = 24,25`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Viertelwert mit voller Dezimalgenauigkeit erhalten.

## HOF-B1-S120-F03 — Teilwerte des Bundumfangs

- **Fachlicher Zweck:** Den halben und viertel Bundumfang aus dem Bundumfang bestimmen.
- **Quelle:** `formeln_s120.md`, Zeile 11; Originaltranskript `s120.md`, Zeile 38; Buchseite 120.
- **Originalbezeichnung:** `BuU Bundumfang; ½; ¼`
- **Normalisierte Bezeichnung:** `bundumfang_teilwerte`

### Buchfassung

```text
| BuU | Bundumfang | 80 | ½ = 40; ¼ = 20 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `bundumfang` | BuU | 80 | cm |

### Formel und Rechenschritte

```text
halber_bundumfang = bundumfang / 2
                   = 80 cm / 2
                   = 40 cm
viertel_bundumfang = bundumfang / 4
                    = 80 cm / 4
                    = 20 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `halber_bundumfang` | ½ BuU | 40 | cm |
| `viertel_bundumfang` | ¼ BuU | 20 | cm |

- **Abhängigkeiten:** Bundumfang.
- **Gültigkeitsbereich:** Konstruktionstabelle der Standardhose mit vertieftem Bund, Größe 38, auf S. 120.
- **Technische Randbedingung:** Der Bundumfang muss als nichtnegative Länge vorliegen.
- **Offene Fragen oder Widersprüche:** Keine; `80 / 2 = 40` und `80 / 4 = 20`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `BuU` als Bundmaß getrennt von `TaU` führen.

## HOF-B1-S120-F04 — Vorderhosenbreite

- **Fachlicher Zweck:** Die Vorderhosenbreite aus einem Viertel des Hüftumfangs minus 1 cm bestimmen.
- **Quelle:** `formeln_s120.md`, Zeile 16; Originaltranskript `s120.md`, Zeile 53; Buchseite 120.
- **Originalbezeichnung:** `vHoB = ¼ HüU − 1 cm`
- **Normalisierte Bezeichnung:** `vorderhosenbreite_standardhose`

### Buchfassung

```text
| vHoB | Vorderhosenbreite | ¼ HüU − 1 cm | — | 23,2 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `vorderhosen_abzug` | fester Abzug | 1 | cm |

### Formel und Rechenschritte

```text
vorderhosenbreite_exakt = (hueftumfang / 4) - vorderhosen_abzug
                         = 24,25 cm - 1 cm
                         = 23,25 cm
Buchwert                = 23,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `vorderhosenbreite` | vHoB | 23,2 | cm |

- **Abhängigkeiten:** Hüftumfang aus `HOF-B1-S120-F02`.
- **Gültigkeitsbereich:** Standardhose der Konstruktionstabelle auf S. 120.
- **Technische Randbedingung:** Der Buchwert ist gegenüber `23,25 cm` auf eine Dezimalstelle verkürzt; eine allgemeine Rundungsregel ist nicht belegt.
- **Offene Fragen oder Widersprüche:** Unklar ist, ob `23,2 cm` abgeschnitten oder nach einer nicht dokumentierten Regel gerundet wurde.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern `23,25 cm` erhalten; Rundung beziehungsweise Abschneiden erst als gesonderte Ausgabeentscheidung anwenden.

## HOF-B1-S120-F05 — Hinterhosenbreite

- **Fachlicher Zweck:** Die Hinterhosenbreite aus einem Viertel des Hüftumfangs plus 1 cm bestimmen.
- **Quelle:** `formeln_s120.md`, Zeile 17; Originaltranskript `s120.md`, Zeile 54; Buchseite 120.
- **Originalbezeichnung:** `hHoB = ¼ HüU + 1 cm`
- **Normalisierte Bezeichnung:** `hinterhosenbreite_standardhose`

### Buchfassung

```text
| hHoB | Hinterhosenbreite | ¼ HüU + 1 cm | — | 25,2 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `hinterhosen_zuschlag` | fester Zuschlag | 1 | cm |

### Formel und Rechenschritte

```text
hinterhosenbreite_exakt = (hueftumfang / 4) + hinterhosen_zuschlag
                         = 24,25 cm + 1 cm
                         = 25,25 cm
Buchwert                = 25,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hinterhosenbreite` | hHoB | 25,2 | cm |

- **Abhängigkeiten:** Hüftumfang aus `HOF-B1-S120-F02`.
- **Gültigkeitsbereich:** Standardhose der Konstruktionstabelle auf S. 120.
- **Technische Randbedingung:** Der Buchwert ist gegenüber `25,25 cm` auf eine Dezimalstelle verkürzt; eine allgemeine Rundungsregel ist nicht belegt.
- **Offene Fragen oder Widersprüche:** Unklar ist, ob `25,2 cm` abgeschnitten oder nach einer nicht dokumentierten Regel gerundet wurde.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Dieselbe explizite Rundungspolitik wie für die Vorderhosenbreite verwenden.

## HOF-B1-S120-F06 — Kniehöhe aus Schritthöhe

- **Fachlicher Zweck:** Die Kniehöhe als vier Zehntel der Schritthöhe bestimmen.
- **Quelle:** `formeln_s120.md`, Zeile 22; Originaltranskript `s120.md`, Zeile 73; Buchseite 120.
- **Originalbezeichnung:** `KnH = SrH : 10 · 4`
- **Normalisierte Bezeichnung:** `kniehoehe_standardhose`

### Buchfassung

```text
| KnH | Kniehöhe | SrH : 10 · 4 | 32 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `schritthoehe` | SrH | 80 | cm |

### Formel und Rechenschritte

```text
kniehoehe = (schritthoehe / 10) * 4
           = (80 cm / 10) * 4
           = 32 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `kniehoehe` | KnH | 32 | cm |

- **Abhängigkeiten:** Schritthöhe `SrH`; ihre Berechnung aus `sTaH − SiH` steht im Originaltranskript, fehlt aber im extrahierten Formelbestand.
- **Gültigkeitsbereich:** Konstruktionstabelle der Standardhose auf S. 120.
- **Technische Randbedingung:** Die Operationsreihenfolge wird als `(SrH / 10) * 4` festgehalten.
- **Offene Fragen oder Widersprüche:** Keine; `(80 / 10) * 4 = 32`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `SrH` bis zur Ergänzung der Extraktionslücke als Eingabe übernehmen.

## HOF-B1-S120-F07 — Taillenausfall an der figurbedingten Bundposition

- **Fachlicher Zweck:** Den zu verteilenden Taillenausfall aus gemessener Taillenabtrennung und halbem Bundumfang bestimmen.
- **Quelle:** `formeln_s120.md`, Zeilen 27, 32 und 37; Originaltranskript `s120.md`, Zeilen 102–108; Buchseite 120.
- **Originalbezeichnung:** `TaAf = Taillenabtrennung − ½ BuU`
- **Normalisierte Bezeichnung:** `taillenausfall_figurbedingte_bundposition`

### Buchfassung

```text
TaAf = Taillenabtrennung − ½ BuU
```

```text
= 44,3 cm − 40 cm (hier − 0 cm)
```

```text
= 4,3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `taillenabtrennung` | gesamte vordere + hintere Taillenabtrennung | 44,3 | cm |
| `halber_bundumfang` | ½ BuU | 40 | cm |
| `einhalteweiten_abzug` | hier − 0 cm; optional laut Originaltranskript | 0 | cm |

### Formel und Rechenschritte

```text
taillenausfall = taillenabtrennung - halber_bundumfang - einhalteweiten_abzug
                = 44,3 cm - 40 cm - 0 cm
                = 4,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenausfall` | TaAf an der figurbedingten Bundposition | 4,3 | cm |

- **Abhängigkeiten:** Gemessene Taillenabtrennung und halber Bundumfang aus `HOF-B1-S120-F03`.
- **Gültigkeitsbereich:** Individuelle Taillenvertiefung der Standardhose auf S. 120.
- **Technische Randbedingung:** Der optionale Abzug beträgt im Buchbeispiel `0 cm`; das Originaltranskript nennt außerhalb der extrahierten Blöcke gegebenenfalls `0,5 cm EW`.
- **Offene Fragen oder Widersprüche:** Keine im Beispiel; `44,3 - 40 - 0 = 4,3`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einhalteweite als optionalen, standardmäßig null gesetzten Abzug führen und nicht still in die gemessene Taillenabtrennung einrechnen.

## Prüfhinweis zur Extraktionsgrenze

Im Originaltranskript `s120.md` fehlen im extrahierten Formelbestand mehrere formelartige Beziehungen: Zeile 21 nennt die Mittelung linker und rechter Bundabstände, Zeile 72 `SrH = sTaH − SiH`, Zeile 104 den optionalen Abzug `0,5 cm EW` und die Zeilen 112–116 die Verteilung des Taillenausfalls auf Vorder- und Rückteilabnäher. Sie wurden nicht als eigene Buchfassungen ergänzt. Der Abschluss von `H01` gilt für den vorhandenen extrahierten Kandidatenbestand.