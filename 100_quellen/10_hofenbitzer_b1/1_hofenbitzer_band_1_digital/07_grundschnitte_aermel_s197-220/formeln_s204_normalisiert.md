# Fachlich normalisierte Formeln — S. 204

Quelle der Normalisierung: `formeln_s204_digital_geprüft.md`
Originaltranskript: `s204_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 204
Extraktionsstand: v2

## HOF-B1-S204-F01 — Einhalteweite des schmalen Ärmels

- **Fachlicher Zweck:** Die Einhalteweite der Ärmelkugel aus 8 Prozent des Armlochumfangs bestimmen.
- **Quelle:** `formeln_s204_digital_geprüft.md`, Zeile 9; Originaltranskript `s204_digital_geprüft.md`, Zeile 17; Buchseite 204.
- **Originalbezeichnung:** `AlU`, `Einhalteweite in %`, `EW in cm`
- **Normalisierte Bezeichnung:** `einhalteweite_schmaler_aermel`

### Buchfassung

```text
| EW in % | Einhalteweite in % | 8 % | `AlU · Einhalteweite in %` | 3,3 cm | EW in cm |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochumfang` | AlU | 41,2 | cm |
| `einhalteweite_anteil` | Einhalteweite in % | 8 | % |

### Formel und Rechenschritte

```text
einhalteweite_exakt = 41,2 cm * 0,08 = 3,296 cm
gedruckte_einhalteweite = 3,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `einhalteweite_cm` | EW in cm | 3,3 gedruckt; 3,296 exakt | cm |

- **Abhängigkeiten:** AlU 41,2 cm aus derselben Konstruktionstabelle im Originaltranskript.
- **Gültigkeitsbereich:** Schmaler Ärmel-Grundschnitt mit hoher Ärmelkugel, Größe 38, PK 3, S. 204.
- **Technische Randbedingung:** Exakten und gedruckten Wert getrennt erhalten.
- **Offene Fragen oder Widersprüche:** Die Rundung auf `3,3 cm` ist rechnerisch plausibel; eine allgemeine Rundungsregel nennt die Quelle nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern mit dem exakten Wert rechnen und die Darstellungsrundung separat behandeln.

## HOF-B1-S204-F02 — Diagonale zur Ärmelkugellinie mit 48 Prozent des Ärmelkugelumfangs

- **Fachlicher Zweck:** Die mathematisch exakter bezeichnete Diagonale zur Lage der Ärmelkugellinie aus 48 Prozent des Ärmelkugelumfangs bestimmen.
- **Quelle:** `formeln_s204_digital_geprüft.md`, Zeile 19; Originaltranskript `s204_digital_geprüft.md`, Zeile 43; Buchseite 204.
- **Originalbezeichnung:** `48% ÄkU`
- **Normalisierte Bezeichnung:** `diagonale_aermelkugellinie_48_prozent`

### Buchfassung

```text
- `exakter: 48% ÄkU = 44,5 cm · 0,48 = 21,4 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `aermelkugelumfang` | ÄkU | 44,5 | cm |
| `diagonalanteil` | 48 % | 0,48 | dimensionslos |

### Formel und Rechenschritte

```text
diagonale_exakt = 44,5 cm * 0,48 = 21,36 cm
gedruckte_diagonale = 21,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `diagonale_aermelkugellinie` | Strecke von der Schulterlinie zur vorgesehenen ÄkLi | 21,4 gedruckt; 21,36 exakt | cm |

- **Abhängigkeiten:** ÄkU aus AlU plus Einhalteweite; diese Summenbeziehung steht im Transkript, wurde aber nicht in den verbindlichen Extrakt aufgenommen.
- **Gültigkeitsbereich:** Grundgerüst des schmalen Ärmels auf S. 204.
- **Technische Randbedingung:** Die alternative Buchmethode `½ ÄkU - 1 cm` ist nicht Teil des Extrakts und wird hier nicht normalisiert.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Abweichung außer der nicht allgemein belegten Rundung auf eine Dezimalstelle.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den 48-Prozent-Pfad implementieren; die nicht extrahierte Alternativmethode erst nach Ergänzung der Extraktionsschicht behandeln.

## HOF-B1-S204-F03 — Kontrollbereich der Ärmelkugellinien-Position

- **Fachlicher Zweck:** Die Höhe eines Kontrollschritts für die optimale Lage der Ärmelkugellinie als Zehntel der Armlochhöhe bestimmen.
- **Quelle:** `formeln_s204_digital_geprüft.md`, Zeile 24; Originaltranskript `s204_digital_geprüft.md`, Zeilen 45–46; Buchseite 204.
- **Originalbezeichnung:** `⅒ AlH`, `Kontrollbereich`
- **Normalisierte Bezeichnung:** `kontrollschritt_aermelkugellinien_position`

### Buchfassung

```text
- `⅒ AlH = Kontrollbereich → Bereich der optimalen Ärmelkugellinien-Position`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochhoehe` | AlH | 17,2 | cm |
| `kontrollanteil` | ⅒ | 0,1 | dimensionslos |

### Formel und Rechenschritte

```text
kontrollschritt = armlochhoehe / 10
kontextrechnung = 17,2 cm / 10 = 1,72 cm
gedrucktes_zeichnungslabel_ausserhalb_des_extrakts = 1,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `kontrollschritt` | Ein Zehntel AlH als Schritt des Kontrollbereichs | 1,72 exakt; 1,7 im Transkriptlabel | cm |

- **Abhängigkeiten:** AlH 17,2 cm und das Zeichnungslabel 1,7 cm stammen nur aus dem Originaltranskript; sie dienen als ausdrücklich gekennzeichneter Rechenkontext.
- **Gültigkeitsbereich:** Kontrollbereich zur Lage der ÄkLi im Grundgerüst S. 204.
- **Technische Randbedingung:** Das Transkript beschreibt zwei aufeinanderfolgende Schritte zu je ⅒ AlH; die extrahierte Buchfassung belegt nur die Größe eines Schritts.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine allgemeine Rundungsregel für 1,72 cm auf 1,7 cm.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einen Schritt als `armlochhoehe / 10` berechnen; Anzahl und Richtung der Schritte in der späteren Geometrie getrennt modellieren.

## HOF-B1-S204-F04 — Ellenbogenlinie bei 60 Prozent Ärmellänge

- **Fachlicher Zweck:** Den Abstand der Ellenbogenlinie als 60 Prozent der Ärmellänge bestimmen.
- **Quelle:** `formeln_s204_digital_geprüft.md`, Zeile 29; Originaltranskript `s204_digital_geprüft.md`, Zeile 47; Buchseite 204.
- **Originalbezeichnung:** `60% ÄL`
- **Normalisierte Bezeichnung:** `ellenbogenlinienhoehe_schmaler_aermel`

### Buchfassung

```text
- `60 cm · 0,60 = 36 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `aermellaenge` | ÄL | 60 | cm |
| `ellenbogenanteil` | 60 % | 0,60 | dimensionslos |

### Formel und Rechenschritte

```text
ellenbogenlinienhoehe = 60 cm * 0,60 = 36 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `ellenbogenlinienhoehe` | Abstand zur Ellenbogenlinie | 36 | cm |

- **Abhängigkeiten:** ÄL aus der Konstruktionstabelle.
- **Gültigkeitsbereich:** Grundgerüst des schmalen Ärmels auf S. 204.
- **Technische Randbedingung:** Die Strecke wird entlang der Ärmellängenlinie abgetragen.
- **Offene Fragen oder Widersprüche:** Keine; die Rechnung ist exakt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Dieselbe 60-Prozent-Beziehung wie bei den Ärmelgrundschnitten S. 200 und S. 202 wiederverwenden, aber die Seitenprovenienz erhalten.

## HOF-B1-S204-F05 — Armlochtiefe aus Oberarmumfang

- **Fachlicher Zweck:** Einen Kontrollwert für die Armlochtiefe aus dem Oberarmumfang bestimmen.
- **Quelle:** `formeln_s204_digital_geprüft.md`, Zeile 34; Originaltranskript `s204_digital_geprüft.md`, Zeile 82; Buchseite 204.
- **Originalbezeichnung:** `ArD`, `OaU`
- **Normalisierte Bezeichnung:** `armlochtiefe_kontrollwert_aus_oberarmumfang`

### Buchfassung

```text
3. Armloch kontrollieren: `ArD = OaU : 10 · 6 - 7,5 cm`. Das Armloch am Oberteil-Grundschnitt ggf. verbreitern (ArD nachmessen und berechnen sowie die AlT am Körper nachmessen). Dann den AlU neu messen, den ÄkU neu berechnen und die Diagonale am Ärmel neu abtragen → die ÄkLi wird tiefer.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `oberarmumfang` | OaU | 28 im Seitenkontext | cm |
| `faktor` | 6 | 6 | dimensionslos |
| `abzug` | 7,5 | 7,5 | cm |

### Formel und Rechenschritte

```text
armlochtiefe = (oberarmumfang / 10) * 6 - 7,5 cm
kontextrechnung = (28 cm / 10) * 6 - 7,5 cm = 9,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefe_kontrollwert` | berechnete ArD zur Armlochkontrolle | 9,3 bei OaU 28 | cm |

- **Abhängigkeiten:** OaU muss am Körper gemessen sein; der Wert 28 cm steht in der Konstruktionstabelle des Originaltranskripts, nicht in der extrahierten Buchfassung.
- **Gültigkeitsbereich:** Korrekturreihenfolge bei zu hoher ÄkLi des schmalen Ärmel-Grundschnitts.
- **Technische Randbedingung:** Division und Multiplikation werden links nach rechts als `(OaU / 10) * 6` ausgeführt; anschließend werden 7,5 cm abgezogen.
- **Offene Fragen oder Widersprüche:** Die Formel ist rechnerisch eindeutig. Ob der Kontextwert 28 cm für eine konkrete Korrektur verwendet werden soll, bleibt eine Eingabeentscheidung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Formel als Kontrollwert ausgeben; Änderungen am Oberteil-Armloch und die anschließende Neuberechnung von AlU und ÄkU sind getrennte Konstruktionsschritte.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s204_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Isolierter Messwert `me = 2,7 cm`; Eingabe- beziehungsweise Zeichnungslabel ohne Rechenbeziehung |
| **Summe** | **1** | **1 isolierter Messwert** |

## Extraktionslücken

Im Originaltranskript stehen zusätzlich `ÄkU = AlU + Einhalteweite in cm`, `½ OaW + 0,5 bis 0,7` und `½ ÄkU - 1 cm`. Diese Beziehungen fehlen im verbindlichen Extrakt und wurden deshalb nicht stillschweigend als Buchfassung normalisiert.
