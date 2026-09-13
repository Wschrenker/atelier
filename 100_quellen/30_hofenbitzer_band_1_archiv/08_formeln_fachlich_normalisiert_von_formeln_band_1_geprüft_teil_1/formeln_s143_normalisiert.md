# Fachlich normalisierte Formeln — S. 143

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/05_modelle_hosen_s138-170/formeln_s143.md`
Originaltranskript: `../hofenbitzer_band_1_digital/05_modelle_hosen_s138-170/s143.md`
Buchseite: Hofenbitzer, Band 1, S. 143

## HOF-B1-S143-F01 — Gemessene gesamte Knieweite der Chinos

- **Fachlicher Zweck:** Die gemessene gesamte Knieweite aus Vorder- und Hinterhosenanteil bestimmen.
- **Quelle:** `formeln_s143.md`, Zeile 14; Originaltranskript `s143.md`, Zeile 38; Buchseite 143.
- **Originalbezeichnung:** `Knieweite = 23 cm + 27 cm = 50 cm`
- **Normalisierte Bezeichnung:** `knieweite_chinos_gemessen`

### Buchfassung

```text
- Knieweite = 23 cm + 27 cm = 50 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `knieweite_vorderhose` | vordere Knieweite | 23 | cm |
| `knieweite_hinterhose` | hintere Knieweite | 27 | cm |

### Formel und Rechenschritte

```text
knieweite_gemessen = knieweite_vorderhose + knieweite_hinterhose
                    = 23 cm + 27 cm
                    = 50 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `knieweite_gemessen` | gesamte gemessene Knieweite | 50 | cm |

- **Abhängigkeiten:** Gemessene Kniebreiten der Vorder- und Hinterhose.
- **Gültigkeitsbereich:** Chinos-Modellentwicklung auf S. 142–143.
- **Technische Randbedingung:** Beide Teilweiten müssen am selben Grundschnitt und auf derselben Knielinie gemessen werden.
- **Offene Fragen oder Widersprüche:** Keine; `23 cm + 27 cm = 50 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorder- und Hinterhosenanteil getrennt protokollieren und erst danach summieren.

## HOF-B1-S143-F02 — Knieweiten-Differenz zur gewünschten Chinosweite

- **Fachlicher Zweck:** Die zu reduzierende Knieweite aus gemessener und gewünschter Gesamtweite bestimmen.
- **Quelle:** `formeln_s143.md`, Zeile 15; Originaltranskript `s143.md`, Zeile 39; Buchseite 143.
- **Originalbezeichnung:** `gemessene KnW - gewünschte KnW`
- **Normalisierte Bezeichnung:** `knieweiten_differenz_chinos`

### Buchfassung

```text
- KnW-Differenz: gemessene KnW - gewünschte KnW = 50 cm - 48 cm = 2 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `knieweite_gemessen` | gemessene KnW | 50 | cm |
| `knieweite_gewuenscht` | gewünschte KnW | 48 | cm |

### Formel und Rechenschritte

```text
knieweiten_differenz = knieweite_gemessen - knieweite_gewuenscht
                      = 50 cm - 48 cm
                      = 2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `knieweiten_differenz` | insgesamt abzutragende Mehrweite am Knie | 2 | cm |

- **Abhängigkeiten:** Gemessene Knieweite aus `HOF-B1-S143-F01` und gewünschte Knieweite von 48 cm.
- **Gültigkeitsbereich:** Chinos-Modellentwicklung für die vorgeschlagenen Fertigmaße der Größe 38.
- **Technische Randbedingung:** Ein positives Ergebnis bezeichnet hier eine Reduzierung; die Verteilung auf vier Nahtseiten ist nicht Bestandteil der extrahierten Buchfassung.
- **Offene Fragen oder Widersprüche:** Keine; `50 cm - 48 cm = 2 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorzeichen semantisch als Reduktions- oder Erweiterungsfall kennzeichnen; Verteilungsregel separat halten.

## HOF-B1-S143-F03 — Gemessene gesamte Saumweite der Chinos

- **Fachlicher Zweck:** Die gemessene gesamte Saumweite aus Vorder- und Hinterhosenanteil bestimmen.
- **Quelle:** `formeln_s143.md`, Zeile 20; Originaltranskript `s143.md`, Zeile 41; Buchseite 143.
- **Originalbezeichnung:** `Saumweite = 21 cm + 25 cm = 46 cm`
- **Normalisierte Bezeichnung:** `saumweite_chinos_gemessen`

### Buchfassung

```text
- Saumweite = 21 cm + 25 cm = 46 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite_vorderhose` | vordere Saumweite | 21 | cm |
| `saumweite_hinterhose` | hintere Saumweite | 25 | cm |

### Formel und Rechenschritte

```text
saumweite_gemessen = saumweite_vorderhose + saumweite_hinterhose
                    = 21 cm + 25 cm
                    = 46 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite_gemessen` | gesamte gemessene Saumweite | 46 | cm |

- **Abhängigkeiten:** Gemessene Saumbreiten der Vorder- und Hinterhose.
- **Gültigkeitsbereich:** Chinos-Modellentwicklung auf S. 142–143.
- **Technische Randbedingung:** Beide Teilweiten müssen am selben Grundschnitt und auf derselben Saumlinie gemessen werden.
- **Offene Fragen oder Widersprüche:** Keine; `21 cm + 25 cm = 46 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorder- und Hinterhosenanteil getrennt protokollieren und erst danach summieren.

## HOF-B1-S143-F04 — Saumweiten-Differenz zur gewünschten Chinosweite

- **Fachlicher Zweck:** Die zu reduzierende Saumweite aus gemessener und gewünschter Gesamtweite bestimmen.
- **Quelle:** `formeln_s143.md`, Zeile 21; Originaltranskript `s143.md`, Zeile 42; Buchseite 143.
- **Originalbezeichnung:** `gemessene SaW - gewünschte SaW`
- **Normalisierte Bezeichnung:** `saumweiten_differenz_chinos`

### Buchfassung

```text
- SaW-Differenz: gemessene SaW - gewünschte SaW = 46 cm - 42 cm = 4 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite_gemessen` | gemessene SaW | 46 | cm |
| `saumweite_gewuenscht` | gewünschte SaW | 42 | cm |

### Formel und Rechenschritte

```text
saumweiten_differenz = saumweite_gemessen - saumweite_gewuenscht
                      = 46 cm - 42 cm
                      = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweiten_differenz` | insgesamt abzutragende Mehrweite am Saum | 4 | cm |

- **Abhängigkeiten:** Gemessene Saumweite aus `HOF-B1-S143-F03` und gewünschte Saumweite von 42 cm.
- **Gültigkeitsbereich:** Chinos-Modellentwicklung für die vorgeschlagenen Fertigmaße der Größe 38.
- **Technische Randbedingung:** Ein positives Ergebnis bezeichnet hier eine Reduzierung; die Verteilung auf vier Nahtseiten ist nicht Bestandteil der extrahierten Buchfassung.
- **Offene Fragen oder Widersprüche:** Keine; `46 cm - 42 cm = 4 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorzeichen semantisch kennzeichnen und Verteilung geometrisch getrennt ausführen.

## HOF-B1-S143-F05 — Öffnungsbetrag für die Biese

- **Fachlicher Zweck:** Den gesamten Öffnungsbetrag aus zweimal der Biesenbreite bestimmen.
- **Quelle:** `formeln_s143.md`, Zeile 36; Originaltranskript `s143.md`, Zeile 61; Buchseite 143.
- **Originalbezeichnung:** `Biesenbreite öffnen 2 × 0,5 cm = 1 cm`
- **Normalisierte Bezeichnung:** `biesen_oeffnungsbetrag_chinos`

### Buchfassung

```text
- Biesenbreite öffnen 2 × 0,5 cm = 1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `biesenbreite` | Biesenbreite | 0,5 | cm |
| `anzahl_biesenbreiten` | 2 × | 2 | dimensionslos |

### Formel und Rechenschritte

```text
biesen_oeffnungsbetrag = anzahl_biesenbreiten * biesenbreite
                        = 2 * 0,5 cm
                        = 1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `biesen_oeffnungsbetrag` | am unteren Taschenspiegel zu öffnender Gesamtbetrag | 1 | cm |

- **Abhängigkeiten:** Gewählte Biesenbreite.
- **Gültigkeitsbereich:** Optionale Biese im hinteren Taschenbeutel der Chinos.
- **Technische Randbedingung:** Der Gesamtbetrag entspricht zwei Biesenbreiten.
- **Offene Fragen oder Widersprüche:** Keine; `2 × 0,5 cm = 1 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Biesenbreite als Parameter führen und den Öffnungsbetrag daraus berechnen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s143.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Bildverweis `□8+9`; das Pluszeichen verbindet Bildnummern und ist kein Rechenoperator |
| Zeile 26 | 1 | Geometrische Kopier- und Zusammenstellungsanweisung für eine Taschenbeutelfläche; keine numerische Maßbeziehung |
| Zeile 31 | 1 | Gleichsetzung von Eingriff und oberer Ansatznaht; Begriffs- beziehungsweise Linienlabel, keine Rechenformel |
| **Summe** | **3** | **1 Bildverweis und 2 Konstruktionslabels ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s143.md` enthält in den Zeilen 40 und 43 die Verteilung der Knie- beziehungsweise Saumweiten-Differenz auf vier Nahtseiten: `¼ von 2 cm, hier 0,5 cm, beidseitig` und `¼ von 4 cm, hier 1 cm, beidseitig`. Diese Beziehungen fehlen in `formeln_s143.md` und wurden deshalb nicht als Buchfassungen normalisiert.
