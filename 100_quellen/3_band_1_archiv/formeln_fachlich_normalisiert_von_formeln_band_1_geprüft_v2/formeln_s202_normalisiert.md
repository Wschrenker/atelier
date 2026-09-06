# Fachlich normalisierte Formeln — S. 202

Quelle der Normalisierung: `formeln_s202_digital_geprüft.md`
Originaltranskript: `s202_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 202
Extraktionsstand: v2

## HOF-B1-S202-F01 — Ärmelsaumweite des weiten Ärmels

- **Fachlicher Zweck:** Die anfängliche Ärmelsaumweite der Oberarmweite gleichsetzen.
- **Quelle:** `formeln_s202_digital_geprüft.md`, Zeile 9; Originaltranskript `s202_digital_geprüft.md`, Zeile 28; Buchseite 202.
- **Originalbezeichnung:** `HgU`, `OaW`, `ÄSaW`
- **Normalisierte Bezeichnung:** `aermelsaumweite_gleich_oberarmweite`

### Buchfassung

```text
| HgU | Handgelenkumfang | 16 | + --- | = OaW | ÄSaW |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `oberarmweite` | OaW | 37 | cm |
| `handgelenkumfang` | HgU | 16 | cm |

### Formel und Rechenschritte

```text
aermelsaumweite = oberarmweite = 37 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `aermelsaumweite` | ÄSaW vor späterer Reduzierung | 37 | cm |

- **Abhängigkeiten:** OaW aus der Konstruktionstabelle; die Zeile verwendet HgU nicht als Rechenoperand.
- **Gültigkeitsbereich:** Weiter Ärmel-Grundschnitt S. 202 vor der möglichen Saumreduzierung auf S. 203.
- **Technische Randbedingung:** `---` ist keine numerische Zugabe; die Ausgabe wird unmittelbar OaW gleichgesetzt.
- **Offene Fragen oder Widersprüche:** Keine; der Handgelenkumfang ist in dieser Tabellenzeile nur Ausgangskontext.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** ÄSaW aus OaW übernehmen und nicht als `HgU + 0` berechnen.

## HOF-B1-S202-F02 — Einhalteweite des weiten Ärmels

- **Fachlicher Zweck:** Die Einhalteweite des Beispielärmels aus 3 Prozent des Armlochumfangs bestimmen.
- **Quelle:** `formeln_s202_digital_geprüft.md`, Zeile 10; Originaltranskript `s202_digital_geprüft.md`, Zeile 29; Buchseite 202.
- **Originalbezeichnung:** `AlU`, `Einhalteweite in %`, `EW in cm`
- **Normalisierte Bezeichnung:** `einhalteweite_weiter_aermel_beispiel`

### Buchfassung

```text
| EW in % | Einhalteweite in % | 3 % | `AlU · Einhalteweite in %` | 1,3 cm | EW in cm |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochumfang` | AlU | 43,5 | cm |
| `einhalteweite_anteil` | Einhalteweite in % | 3 | % |

### Formel und Rechenschritte

```text
einhalteweite_exakt = 43,5 cm * 0,03 = 1,305 cm
gedruckte_einhalteweite = 1,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `einhalteweite_cm` | EW in cm | 1,3 gedruckt; 1,305 exakt | cm |

- **Abhängigkeiten:** `HOF-B1-S199-F02`; AlU 43,5 cm aus der Konstruktionstabelle.
- **Gültigkeitsbereich:** Weiter Ärmel-Grundschnitt in PK 5 auf S. 202.
- **Technische Randbedingung:** Exakten und gedruckten Wert getrennt erhalten.
- **Offene Fragen oder Widersprüche:** Die Rundung auf `1,3 cm` ist plausibel, aber eine allgemeine Rundungsregel ist nicht belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern `1,305 cm` erhalten und Darstellungsrundung separat behandeln.

## HOF-B1-S202-F03 — Ellenbogenlinie bei 60 Prozent Ärmellänge

- **Fachlicher Zweck:** Die Höhe der Ellenbogenlinie als 60 Prozent der Ärmellänge bestimmen.
- **Quelle:** `formeln_s202_digital_geprüft.md`, Zeile 15; Originaltranskript `s202_digital_geprüft.md`, Zeile 45; Buchseite 202.
- **Originalbezeichnung:** `60% ÄL`, `Ellenbogenlinie`
- **Normalisierte Bezeichnung:** `ellenbogenlinienhoehe_weiter_aermel`

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
| `ellenbogenlinienhoehe` | Abstand vom SuP zur Ellenbogenlinie | 36 | cm |

- **Abhängigkeiten:** ÄL aus der Konstruktionstabelle.
- **Gültigkeitsbereich:** Grundgerüst des weiten Ärmels auf S. 202.
- **Technische Randbedingung:** Der Wert wird entlang der ÄL-Linie vom SuP abgetragen.
- **Offene Fragen oder Widersprüche:** Keine; die Rechnung ist exakt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Dieselbe 60-Prozent-Beziehung wie beim engen Ärmel wiederverwenden, aber die Seitenprovenienz erhalten.

## HOF-B1-S202-F04 — Vordere untere Hilfsteilung der Ärmelkugellinie

- **Fachlicher Zweck:** Den vorderen unteren Hilfsabstand als Achtel der Ärmelkugellinie bestimmen.
- **Quelle:** `formeln_s202_digital_geprüft.md`, Zeile 20; Originaltranskript `s202_digital_geprüft.md`, Zeile 54; Buchseite 202.
- **Originalbezeichnung:** `ÄkLi : 8`
- **Normalisierte Bezeichnung:** `aermelkugellinie_achtel`

### Buchfassung

```text
- `37 cm : 8 = 4,6 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `aermelkugellinie` | ÄkLi | 37 | cm |
| `teiler` | 8 | 8 | dimensionslos |

### Formel und Rechenschritte

```text
hilfsabstand_exakt = 37 cm / 8 = 4,625 cm
gedruckter_hilfsabstand = 4,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hilfsabstand_vorne_unten` | ÄkLi : 8 | 4,6 gedruckt; 4,625 exakt | cm |

- **Abhängigkeiten:** Gemessene ÄkLi.
- **Gültigkeitsbereich:** Hilfslinien der Ärmelkugel S. 202.
- **Technische Randbedingung:** Exakten und gedruckten Wert getrennt erhalten.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine allgemeine Rundungsregel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern mit `4,625 cm` weiterrechnen.

## HOF-B1-S202-F05 — Hintere untere Hilfsteilung der Ärmelkugellinie

- **Fachlicher Zweck:** Den hinteren unteren Hilfsabstand als Fünftel der Ärmelkugellinie bestimmen.
- **Quelle:** `formeln_s202_digital_geprüft.md`, Zeile 21; Originaltranskript `s202_digital_geprüft.md`, Zeile 55; Buchseite 202.
- **Originalbezeichnung:** `ÄkLi : 5`
- **Normalisierte Bezeichnung:** `aermelkugellinie_fuenftel`

### Buchfassung

```text
- `37 cm : 5 = 7,4 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `aermelkugellinie` | ÄkLi | 37 | cm |
| `teiler` | 5 | 5 | dimensionslos |

### Formel und Rechenschritte

```text
hilfsabstand_hinten_unten = 37 cm / 5 = 7,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hilfsabstand_hinten_unten` | ÄkLi : 5 | 7,4 | cm |

- **Abhängigkeiten:** Gemessene ÄkLi.
- **Gültigkeitsbereich:** Hilfslinien der Ärmelkugel S. 202.
- **Technische Randbedingung:** Länge und Ausgabe verwenden dieselbe Einheit.
- **Offene Fragen oder Widersprüche:** Keine; die Rechnung ist exakt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Direkte Division durch 5.

## HOF-B1-S202-F06 — Vordere obere Hilfsteilung der Ärmelkugellinie

- **Fachlicher Zweck:** Den vorderen oberen Hilfsabstand als Zwölftel der Ärmelkugellinie bestimmen.
- **Quelle:** `formeln_s202_digital_geprüft.md`, Zeile 26; Originaltranskript `s202_digital_geprüft.md`, Zeile 61; Buchseite 202.
- **Originalbezeichnung:** `ÄkLi : 12`
- **Normalisierte Bezeichnung:** `aermelkugellinie_zwoelftel`

### Buchfassung

```text
- `37 cm : 12 = 3,1 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `aermelkugellinie` | ÄkLi | 37 | cm |
| `teiler` | 12 | 12 | dimensionslos |

### Formel und Rechenschritte

```text
hilfsabstand_exakt = 37 cm / 12 = 3,083333... cm
gedruckter_hilfsabstand = 3,1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hilfsabstand_vorne_oben` | ÄkLi : 12 | 3,1 gedruckt; 3,083333... exakt | cm |

- **Abhängigkeiten:** Gemessene ÄkLi.
- **Gültigkeitsbereich:** Hilfslinien der Ärmelkugel S. 202.
- **Technische Randbedingung:** Exakten und gedruckten Wert getrennt erhalten.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine allgemeine Rundungsregel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern mit dem exakten Quotienten weiterrechnen.

## HOF-B1-S202-F07 — Hintere obere Hilfsteilung der Ärmelkugellinie

- **Fachlicher Zweck:** Den hinteren oberen Hilfsabstand als Vierzehntel der Ärmelkugellinie bestimmen.
- **Quelle:** `formeln_s202_digital_geprüft.md`, Zeile 31; Originaltranskript `s202_digital_geprüft.md`, Zeile 63; Buchseite 202.
- **Originalbezeichnung:** `ÄkLi : 14`
- **Normalisierte Bezeichnung:** `aermelkugellinie_vierzehntel`

### Buchfassung

```text
- `37 cm : 14 = 2,4 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `aermelkugellinie` | ÄkLi | 37 | cm |
| `teiler` | 14 | 14 | dimensionslos |

### Formel und Rechenschritte

```text
hilfsabstand_laut_formel = 37 cm / 14 = 2,642857... cm
gedruckter_hilfsabstand = 2,4 cm
abweichung = 2,642857... cm - 2,4 cm = 0,242857... cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hilfsabstand_laut_formel` | Ergebnis von ÄkLi : 14 | 2,642857... | cm |
| `gedruckter_hilfsabstand` | Druckergebnis | 2,4 | cm |

- **Abhängigkeiten:** Gemessene ÄkLi.
- **Gültigkeitsbereich:** Hintere obere Hilfslinie der Ärmelkugel S. 202.
- **Technische Randbedingung:** Formelpfad und Druckergebnis bis zur Quellenklärung getrennt erhalten.
- **Offene Fragen oder Widersprüche:** `37 : 14` ergibt rund `2,6`, nicht `2,4`. Weder normale Rundung noch die anderen Teilungen erklären das Druckergebnis.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bevor Teiler, Ausgangswert oder Druckergebnis geprüft sind.

## HOF-B1-S202-F08 — Länge der Ärmelkugellinie

- **Fachlicher Zweck:** Die gemessene Ärmelkugellinie als Summe aus Oberarmweite und gewählter Zugabe kontrollieren.
- **Quelle:** `formeln_s202_digital_geprüft.md`, Zeile 36; Originaltranskript `s202_digital_geprüft.md`, Zeile 91; Buchseite 202.
- **Originalbezeichnung:** `ÄkLi`, `OaW`, `Zugabe`
- **Normalisierte Bezeichnung:** `aermelkugellinie_weiter_aermel`

### Buchfassung

```text
9. □4 Die ÄkLi messen → = OaW + Zugabe
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `oberarmweite` | OaW | cm |
| `ausgleichszugabe` | Zugabe | cm |

### Formel und Rechenschritte

```text
aermelkugellinie = oberarmweite + ausgleichszugabe
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `aermelkugellinie` | ÄkLi | cm |

- **Abhängigkeiten:** OaW aus der Konstruktionstabelle; die gedruckte Bereichsangabe der Zugabe steht außerhalb des Extrakts.
- **Gültigkeitsbereich:** Weiter Ärmel-Grundschnitt S. 202.
- **Technische Randbedingung:** Die Zugabe muss als gesonderter Wert vorliegen; aus diesem Extrakt wird kein Bereich erfunden.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel im Extrakt; die symbolische Beziehung ist vollständig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Zugabe nicht aus der Differenz rückwärts erraten, sondern explizit übergeben.

## Ausgeschlossene Kandidaten

Keine; alle 8 extrahierten Kandidatenzeilen sind in Formelblöcken abgebildet.
