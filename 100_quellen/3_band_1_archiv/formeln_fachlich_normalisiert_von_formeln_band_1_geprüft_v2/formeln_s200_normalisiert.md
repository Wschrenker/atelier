# Fachlich normalisierte Formeln — S. 200

Quelle der Normalisierung: `formeln_s200_digital_geprüft.md`
Originaltranskript: `s200_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 200
Extraktionsstand: v2

## HOF-B1-S200-F01 — Einhalteweite des engen Ärmels

- **Fachlicher Zweck:** Die Einhalteweite des Beispielärmels aus Armlochumfang und Prozentwert bestimmen.
- **Quelle:** `formeln_s200_digital_geprüft.md`, Zeile 9; Originaltranskript `s200_digital_geprüft.md`, Zeile 29; Buchseite 200.
- **Originalbezeichnung:** `AlU`, `Einhalteweite in %`, `EW in cm`
- **Normalisierte Bezeichnung:** `einhalteweite_enger_aermel_beispiel`

### Buchfassung

```text
| EW in % | Einhalteweite in % | 1 % | `AlU · Einhalteweite in %` | 0,8 cm | EW in cm |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochumfang` | AlU | 41 | cm |
| `einhalteweite_anteil` | Einhalteweite in % | 1 | % |

### Formel und Rechenschritte

```text
einhalteweite_exakt = 41 cm * 0,01 = 0,41 cm
gedruckte_einhalteweite = 0,8 cm
abweichung = 0,8 cm - 0,41 cm = 0,39 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `einhalteweite_exakt` | Ergebnis der gedruckten Operanden | 0,41 | cm |
| `gedruckte_einhalteweite` | Tabellenwert | 0,8 | cm |

- **Abhängigkeiten:** `HOF-B1-S199-F02`; AlU 41 cm aus der Konstruktionstabelle des Originaltranskripts.
- **Gültigkeitsbereich:** Beispiel des engen Ärmels in PK 1 auf S. 200.
- **Technische Randbedingung:** Formelpfad und Tabellenwert bleiben bis zur Quellenklärung getrennt.
- **Offene Fragen oder Widersprüche:** `1 %` von `41 cm` sind `0,41 cm`, nicht `0,8 cm`. Die im Transkript folgende, nicht extrahierte Tabellenzeile mit ÄKU `41,4 cm` passt gerundet zu `0,4 cm`, nicht zu `0,8 cm`.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Den gedruckten Wert nicht automatisieren, bevor Foto- oder Fachprüfung den gültigen Wert bestätigt.

## HOF-B1-S200-F02 — Ellenbogenlinie bei 60 Prozent Ärmellänge

- **Fachlicher Zweck:** Die Höhe der Ellenbogenlinie als 60 Prozent der Ärmellänge bestimmen.
- **Quelle:** `formeln_s200_digital_geprüft.md`, Zeile 14; Originaltranskript `s200_digital_geprüft.md`, Zeile 45; Buchseite 200.
- **Originalbezeichnung:** `60% ÄL`, `Ellenbogenlinie`
- **Normalisierte Bezeichnung:** `ellenbogenlinienhoehe`

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
ellenbogenlinienhoehe = aermellaenge * ellenbogenanteil
                       = 60 cm * 0,60
                       = 36 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `ellenbogenlinienhoehe` | Abstand vom SuP zur Ellenbogenlinie | 36 | cm |

- **Abhängigkeiten:** ÄL aus der Konstruktionstabelle.
- **Gültigkeitsbereich:** Grundgerüst des engen Ärmel-Grundschnitts auf S. 200.
- **Technische Randbedingung:** Der Wert wird entlang der ÄL-Linie vom SuP abgetragen.
- **Offene Fragen oder Widersprüche:** Keine; die Rechnung ist exakt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Anteil als `0.60` speichern und auf die aktuelle Ärmellänge anwenden.

## HOF-B1-S200-F03 — Hilfsteilungen der Ärmelkugellinie

- **Fachlicher Zweck:** Vier Hilfsabstände aus der gemessenen Ärmelkugellinie bestimmen.
- **Quelle:** `formeln_s200_digital_geprüft.md`, Zeilen 19–20, 25 und 30; Originaltranskript `s200_digital_geprüft.md`, Zeilen 54–55, 61 und 63; Buchseite 200.
- **Originalbezeichnung:** `ÄkLi : 8`, `ÄkLi : 5`, `ÄkLi : 12`, `ÄkLi : 9`
- **Normalisierte Bezeichnung:** `hilfsteilungen_aermelkugellinie_enger_aermel`

### Buchfassung

```text
- `30 cm : 8 = 3,8 cm`
- `30 cm : 5 = 6 cm`
```

```text
- `30 cm : 12 = 2,5 cm`
```

```text
- `30 cm : 9 = 3,3 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `aermelkugellinie` | ÄkLi | 30 | cm |
| `teiler_vorne_unten` | 8 | 8 | dimensionslos |
| `teiler_hinten_unten` | 5 | 5 | dimensionslos |
| `teiler_vorne_oben` | 12 | 12 | dimensionslos |
| `teiler_hinten_oben` | 9 | 9 | dimensionslos |

### Formel und Rechenschritte

```text
hilfsabstand_vorne_unten_exakt = 30 cm / 8 = 3,75 cm
hilfsabstand_vorne_unten_gedruckt = 3,8 cm
hilfsabstand_hinten_unten = 30 cm / 5 = 6 cm
hilfsabstand_vorne_oben = 30 cm / 12 = 2,5 cm
hilfsabstand_hinten_oben_exakt = 30 cm / 9 = 3,333... cm
hilfsabstand_hinten_oben_gedruckt = 3,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hilfsabstand_vorne_unten` | ÄkLi : 8 | 3,8 gedruckt; 3,75 exakt | cm |
| `hilfsabstand_hinten_unten` | ÄkLi : 5 | 6 | cm |
| `hilfsabstand_vorne_oben` | ÄkLi : 12 | 2,5 | cm |
| `hilfsabstand_hinten_oben` | ÄkLi : 9 | 3,3 gedruckt; 3,333... exakt | cm |

- **Abhängigkeiten:** Gemessene ÄkLi nach `HOF-B1-S200-F04`.
- **Gültigkeitsbereich:** Hilfslinien der Ärmelkugel des engen Ärmels auf S. 200.
- **Technische Randbedingung:** Exakte und gedruckte gerundete Werte getrennt erhalten.
- **Offene Fragen oder Widersprüche:** Die Druckwerte sind auf eine Dezimalstelle gerundet; eine allgemeine Rundungsregel nennt die Quelle nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern mit ungerundeten Quotienten rechnen; Darstellungsrundung separat konfigurieren.

## HOF-B1-S200-F04 — Länge der Ärmelkugellinie

- **Fachlicher Zweck:** Die Ärmelkugellinie aus Oberarmweite und Ausgleichszugabe bestimmen.
- **Quelle:** `formeln_s200_digital_geprüft.md`, Zeile 35; Originaltranskript `s200_digital_geprüft.md`, Zeile 72; Buchseite 200.
- **Originalbezeichnung:** `OaW`, `ÄkLi`
- **Normalisierte Bezeichnung:** `aermelkugellinie_enger_aermel`

### Buchfassung

```text
3. □3 Die OaW + 1 bis 1,5 cm zeichnen = ÄkLi.
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `oberarmweite` | OaW | cm |
| `ausgleichszugabe` | 1 bis 1,5 cm | cm |

### Formel und Rechenschritte

```text
aermelkugellinie = oberarmweite + ausgleichszugabe
1 cm <= ausgleichszugabe <= 1,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `aermelkugellinie` | ÄkLi | cm |

- **Abhängigkeiten:** OaW aus der Konstruktionstabelle S. 200.
- **Gültigkeitsbereich:** Enger Ärmel-Grundschnitt für enge Modelle aus Maschenware.
- **Technische Randbedingung:** Die Ausgleichszugabe muss explizit innerhalb des gedruckten Bereichs gewählt werden.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine Auswahlregel zwischen 1 und 1,5 cm.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zugabe als Pflichtparameter mit geschlossener Bereichsprüfung führen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s200_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 40 | 1 | Wiederholt `ÄkLi = OaW + Zugabe` aus `HOF-B1-S200-F04`, ohne neuen Operanden oder Auswahlwert |
| **Summe** | **1** | **1 Rechenwiederholung** |
