# Fachlich normalisierte Formeln — S. 235

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s235_codex_v2_digital_geprueft.md`
Originaltranskript: `../Band_1_geprüft_v1/s235_codex_v2_digital_geprueft.md`
Buchseite: Hofenbitzer, Band 1, S. 235

## HOF-B1-S235-F01 — Erhöhung der Futter-Ärmelkugelnaht unter der Achsel

- **Fachlicher Zweck:** Die Futter-Ärmelkugelnaht unter der Achsel aus zwei Armloch-Nahtzugaben und einem zusätzlichen Betrag erhöhen.
- **Quelle:** `formeln_s235_codex_v2_digital_geprueft.md`, Zeile 9 sowie Zeilen 29–30; Originaltranskript `s235_codex_v2_digital_geprueft.md`, Zeile 19 sowie Zeilen 48–49; Buchseite 235.
- **Originalbezeichnung:** `2× NZg (der Armlochnaht) + 0,5 cm`
- **Normalisierte Bezeichnung:** `erhoehung_futter_aermelkugelnaht_unter_achsel`

### Buchfassung

```text
12. □4 Die Ärmelkugelnaht (unter der Achsel) wird an den Ärmelnähten um 2× NZg (der Armlochnaht) + 0,5 cm erhöht. Das Ärmelfutter wird an dieser Stelle um die Nahtzugabe unter dem Arm herübergeführt, siehe □6.
```

```text
- jeweils 2× NZg des Armlochs + 0,5 cm
- (2 × 1 cm + 0,5 cm = 2,5 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armloch_nahtzugabe` | NZg der Armlochnaht | 1 | cm |
| `anzahl_nahtzugaben` | 2× NZg | 2 | dimensionslos |
| `zusaetzliche_erhoehung` | zusätzlicher Betrag | 0,5 | cm |

### Formel und Rechenschritte

```text
erhoehung_futter_aermelkugelnaht = anzahl_nahtzugaben * armloch_nahtzugabe + zusaetzliche_erhoehung
                                  = 2 * 1 cm + 0,5 cm
                                  = 2,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `erhoehung_futter_aermelkugelnaht` | Erhöhung unter der Achsel an den Ärmelnähten | 2,5 | cm |

- **Abhängigkeiten:** Nahtzugabenbreite der Armlochnaht.
- **Gültigkeitsbereich:** Entwicklung des Futters für den Einnaht-Ärmel der Jacken- und Mantelverarbeitung auf S. 235.
- **Technische Randbedingung:** Die Nahtzugabe wird zweimal angesetzt; der zusätzliche Betrag von `0,5 cm` wird anschließend einmal addiert.
- **Offene Fragen oder Widersprüche:** Keine; die Einsetzrechnung stimmt mit dem Druckergebnis überein.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Nahtzugabenbreite parametrieren und die Anzahl als dimensionslosen Faktor führen.

## HOF-B1-S235-F02 — Kürzung des Futterärmels mit Futtermehrlänge

- **Fachlicher Zweck:** Die tatsächliche Kürzung des Futterärmels aus Saumeinschlag und notwendiger Futtermehrlänge bestimmen.
- **Quelle:** `formeln_s235_codex_v2_digital_geprueft.md`, Zeilen 14, 19, 24 und 35; Originaltranskript `s235_codex_v2_digital_geprueft.md`, Zeilen 27, 29, 31 und 54; Buchseite 235.
- **Originalbezeichnung:** `Kürzung = SaEs - Futtermehrlänge`
- **Normalisierte Bezeichnung:** `kuerzung_futteraermel_mit_mehrlaenge`

### Buchfassung

```text
Kürzung = SaEs - Futtermehrlänge
```

```text
= 3 cm - 1 bis 2 cm
```

```text
= 1,5 cm
```

```text
- Kürzung = 3 cm - 1,5 cm = 1,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `saumeinschlag` | SaEs | 3 | cm |
| `futtermehrlaenge_min` | untere Grenze Futtermehrlänge | 1 | cm |
| `futtermehrlaenge_max` | obere Grenze Futtermehrlänge | 2 | cm |
| `futtermehrlaenge_beispiel` | im Zeichnungsbeispiel verwendete Futtermehrlänge | 1,5 | cm |

### Formel und Rechenschritte

```text
kuerzung_futteraermel = saumeinschlag - futtermehrlaenge

Bei Futtermehrlänge 1 cm:
kuerzung_max = 3 cm - 1 cm = 2 cm

Bei Futtermehrlänge 2 cm:
kuerzung_min = 3 cm - 2 cm = 1 cm

Gedrucktes Beispiel:
kuerzung_beispiel = 3 cm - 1,5 cm = 1,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `kuerzung_futteraermel_min` | kleinste Kürzung bei größter Futtermehrlänge | 1 | cm |
| `kuerzung_futteraermel_max` | größte Kürzung bei kleinster Futtermehrlänge | 2 | cm |
| `kuerzung_futteraermel_beispiel` | Kürzung im Zeichnungsbeispiel | 1,5 | cm |

- **Abhängigkeiten:** Saumeinschlag des Oberstoffärmels und gewählte Futtermehrlänge.
- **Gültigkeitsbereich:** Entwicklung des Futters für den Einnaht-Ärmel ohne Befestigung an einem Schlitzeinschlag.
- **Technische Randbedingung:** Größere Futtermehrlänge ergibt bei gleichem Saumeinschlag eine kleinere Kürzung; die Grenzen der Kürzung laufen deshalb entgegengesetzt zur Reihenfolge der gedruckten Futtermehrlänge.
- **Offene Fragen oder Widersprüche:** Das Beispiel verwendet `1,5 cm` innerhalb des Bereichs `1 bis 2 cm`; eine Auswahlregel für diesen Wert ist nicht belegt. Rechnung und Druckergebnis sind konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Futtermehrlänge als Bereich beziehungsweise expliziten gewählten Wert führen und prüfen, dass sie den Saumeinschlag nicht überschreitet.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s231_codex_v2_digital_geprueft.md`, Zeile 9 | 1 | Schnittteil- und Zuschnittbeschriftung des festlichen Ärmels 3; `2×-p` bezeichnet Stückzahl und paarigen Zuschnitt, keine Berechnung |
| `formeln_s232_codex_v2_digital_geprueft.md`, Zeilen 9 und 14–15 | 3 | Schnittteil- und Zuschnittbeschriftungen der festlichen Ärmel 4 und 6; keine Rechenformeln |
| `formeln_s233_codex_v2_digital_geprueft.md`, Zeilen 9–10 und 15 | 3 | Schnittteil- und Zuschnittbeschriftungen des festlichen Ärmels 7; keine Rechenformeln |
| `formeln_s234_codex_v2_digital_geprueft.md`, Zeile 9 | 1 | Schnittteil- und Zuschnittbeschriftung; keine Rechenformel |
| `formeln_s234_codex_v2_digital_geprueft.md`, Zeile 14 | 1 | festgelegter Saumeinschlag `SaEs = 3 cm`; Eingabewert für `HOF-B1-S235-F02`, keine eigenständige Berechnung |
| `formeln_s235_codex_v2_digital_geprueft.md`, Zeile 40 | 1 | Schnittteil- und Zuschnittbeschriftung des Futterärmels; keine Rechenformel |
| `formeln_s235_codex_v2_digital_geprueft.md`, Zeile 45 | 1 | unvollständiges Nahtdiagramm-Label `2× 1 cm`; bereits im vollständigen Block von `HOF-B1-S235-F01` abgebildet |
| `formeln_s236_codex_v2_digital_geprueft.md`, Zeilen 9–10 | 2 | Schnittteil- und Zuschnittbeschriftungen von Ober- und Unterärmel; keine Rechenformeln |
| **Summe** | **13** | **11 Produktions-/Zuschnittbeschriftungen, 1 Eingabelabel und 1 unvollständige Wiederholung ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Die Seiten 231–233 beschreiben Modellvarianten der festlich-eleganten Ärmel; ihre extrahierten Kandidaten sind ausschließlich Schnittteil- und Zuschnittstempel. Formelartige Konstruktionsangaben zu Öffnungsweiten, Abständen, Faltenlängen und Umfangszugaben stehen nur in den Originaltranskripten und wurden nicht als Buchfassungen ergänzt.

Auf S. 234 und S. 236 fehlen im verbindlichen Extrakt unter anderem die Nahtlängendifferenz von `0,5 bis 0,8 cm`, die Lagen- und Abstandsangaben für Einlagen beziehungsweise Teilungsnähte sowie die Anweisung zum Angleichen der Unterärmel- an die Oberärmel-Nahtlänge. Auf S. 235 enthält das Originaltranskript weitere qualitative und geometrische Regeln zur Futterärmelentwicklung, die keine vollständigen extrahierten Formeln bilden. Diese Beziehungen wurden nicht stillschweigend normalisiert. Der Abschluss von `A01` gilt für den vorhandenen extrahierten Kandidatenbestand.
