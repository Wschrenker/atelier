# Fachlich normalisierte Formeln — S. 130

Quelle der Normalisierung: `formeln_s130.md`
Originaltranskript: `s130.md`
Buchseite: Hofenbitzer, Band 1, S. 130

## HOF-B1-S130-F01 — Vorderer Hosenausschnitt bei breiten Hüften und flachem Gesäß

- **Fachlicher Zweck:** Den kleineren vorderen Hosenausschnitt der Bundfaltenhose aus der verbreiterten Vorderhosenbreite bestimmen.
- **Quelle:** `formeln_s130.md`, Zeile 14; Originaltranskript `s130.md`, Zeilen 26–28; Buchseite 130.
- **Originalbezeichnung:** `vHoB1 : 4 -0,5 bis -1 cm`
- **Normalisierte Bezeichnung:** `vorderer_hosenausschnitt_bundfaltenhose_flaches_gesaess`

### Buchfassung

```text
vHoB1 : 4 -0,5 bis -1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderhosenbreite_bundfalte` | vHoB1 | 26,2 | cm |
| `abzug` | 0,5 bis 1 | wählbar | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_max = (vorderhosenbreite_bundfalte / 4) - 0,5 cm
                     = (26,2 cm / 4) - 0,5 cm
                     = 6,05 cm
hosenausschnitt_min = (vorderhosenbreite_bundfalte / 4) - 1 cm
                     = 5,55 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderer_hosenausschnitt` | kleinerer Abtrag für diese Figurform | 5,55 bis 6,05 | cm |

- **Abhängigkeiten:** `vHoB1` aus `HOF-B1-S131-F01`; Figurklassifikation.
- **Gültigkeitsbereich:** Bundfaltenhose für breite Hüften und flaches Gesäß.
- **Technische Randbedingung:** Die Ergebnisgrenzen sind nach ihrem Wert, nicht nach der Druckreihenfolge benannt.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Figurvariante und Abzug explizit auswählen.

## HOF-B1-S130-F02 — Vorderer Hosenausschnitt bei schmalen Hüften und starkem Gesäß

- **Fachlicher Zweck:** Den größeren vorderen Hosenausschnitt der Bundfaltenhose bestimmen.
- **Quelle:** `formeln_s130.md`, Zeile 19; Originaltranskript `s130.md`, Zeilen 30–32; Buchseite 130.
- **Originalbezeichnung:** `vHoB1 : 4 +0,5 bis +1 cm`
- **Normalisierte Bezeichnung:** `vorderer_hosenausschnitt_bundfaltenhose_starkes_gesaess`

### Buchfassung

```text
vHoB1 : 4 +0,5 bis +1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderhosenbreite_bundfalte` | vHoB1 | 26,2 | cm |
| `zuschlag` | 0,5 bis 1 | wählbar | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_min = (vorderhosenbreite_bundfalte / 4) + 0,5 cm
                     = (26,2 cm / 4) + 0,5 cm
                     = 7,05 cm
hosenausschnitt_max = (vorderhosenbreite_bundfalte / 4) + 1 cm
                     = 7,55 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderer_hosenausschnitt` | größerer Abtrag für diese Figurform | 7,05 bis 7,55 | cm |

- **Abhängigkeiten:** `vHoB1` aus `HOF-B1-S131-F01`; Figurklassifikation.
- **Gültigkeitsbereich:** Bundfaltenhose für schmale Hüften und starkes Gesäß.
- **Technische Randbedingung:** Zuschlag innerhalb des belegten Bereichs wählen.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Getrennte Variante zu F01 führen.

## HOF-B1-S130-F03 — Saumbetrag der Vorderhose

- **Fachlicher Zweck:** Den beidseitig von P12 abzutragenden Saumbetrag bestimmen.
- **Quelle:** `formeln_s130.md`, Zeile 24; Originaltranskript `s130.md`, Zeile 36; Buchseite 130.
- **Originalbezeichnung:** `SaW : 4 -1 cm`
- **Normalisierte Bezeichnung:** `saumbetrag_vorderhose_bundfaltenhose`

### Buchfassung

```text
15./16. Von P12 aus SaW : 4 -1 cm nach rechts und nach links abtragen → P15 und P16.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite` | SaW | 42 | cm |
| `saumabzug` | 1 cm | 1 | cm |

### Formel und Rechenschritte

```text
saumbetrag_vorderhose = (saumweite / 4) - saumabzug
                       = (42 cm / 4) - 1 cm
                       = 9,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumbetrag_vorderhose` | Betrag rechts und links von P12 | 9,5 | cm |

- **Abhängigkeiten:** Gewählte Saumweite der Bundfaltenhose.
- **Gültigkeitsbereich:** Vorderhose der Bundfaltenhose auf S. 130.
- **Technische Randbedingung:** Derselbe Betrag wird beidseitig abgetragen.
- **Offene Fragen oder Widersprüche:** Keine; `42 / 4 - 1 = 9,5`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einen Betrag berechnen und symmetrisch anwenden.

## HOF-B1-S130-F04 — Länge der erhöhten vorderen Taillenlinie

- **Fachlicher Zweck:** Den auf der erhöhten Taillenlinie abzutragenden Betrag einschließlich Bundfalteninhalt und Einhalteweite bestimmen.
- **Quelle:** `formeln_s130.md`, Zeile 29; Originaltranskript `s130.md`, Zeile 40; Buchseite 130.
- **Originalbezeichnung:** `TaU : 4 + gewünschten Bundfalteninhalt + gewünschte Einhalteweite`
- **Normalisierte Bezeichnung:** `vordere_taillenlinienlaenge_bundfaltenhose`

### Buchfassung

```text
21. Von P20 wird TaU : 4 + gewünschten Bundfalteninhalt + gewünschte Einhalteweite auf die erhöhte Taillenlinie abgetragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |
| `bundfalteninhalt` | gewünschter Bundfalteninhalt | 6 | cm |
| `einhalteweite` | gewünschte Einhalteweite | 0 bis 0,5 | cm |

### Formel und Rechenschritte

```text
taillenlinienlaenge_min = (taillenumfang / 4) + bundfalteninhalt + 0 cm
                         = (72 cm / 4) + 6 cm
                         = 24 cm
taillenlinienlaenge_max = (taillenumfang / 4) + bundfalteninhalt + 0,5 cm
                         = 24,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vordere_taillenlinienlaenge` | Betrag auf der erhöhten Taillenlinie | 24 bis 24,5 | cm |

- **Abhängigkeiten:** Taillenumfang, festgelegter Bundfalteninhalt und gewählte Einhalteweite.
- **Gültigkeitsbereich:** Vorderhose der Bundfaltenhose.
- **Technische Randbedingung:** Bundfalteninhalt und Einhalteweite bleiben getrennte Operanden.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Wertebereiche der Einhalteweite validieren.

## HOF-B1-S130-F05 — Verbreiterte Vorderhosenbreite

- **Fachlicher Zweck:** Die Vorderhosenbreite aus dem Hüftumfang bestimmen und für die Bundfaltenhose verbreitern.
- **Quelle:** `formeln_s130.md`, Zeile 34; Originaltranskript `s130.md`, Zeile 92; Buchseite 130.
- **Originalbezeichnung:** `¼ HüU -1 cm ± +3`
- **Normalisierte Bezeichnung:** `vorderhosenbreite_bundfaltenhose`

### Buchfassung

```text
| vHoB | Vorderhosenbreite | ¼ HüU -1 cm ± +3 | 23,2 | 26,2 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `grundabzug_vorne` | −1 cm | 1 | cm |
| `verbreiterung_vorne` | +3 cm | 3 | cm |

### Formel und Rechenschritte

```text
vorderhosenbreite_basis_exakt = (hueftumfang / 4) - grundabzug_vorne
                               = (97 cm / 4) - 1 cm
                               = 23,25 cm
Buchtabellenwert_basis        = 23,2 cm
vorderhosenbreite_bundfalte   = Buchtabellenwert_basis + verbreiterung_vorne
                               = 23,2 cm + 3 cm
                               = 26,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderhosenbreite_bundfalte` | geänderte Vorderhosenbreite | 26,2 | cm |

- **Abhängigkeiten:** Hüftumfang und festgelegte Verbreiterung für den Bundfalteninhalt.
- **Gültigkeitsbereich:** Konstruktionstabelle der Bundfaltenhose auf S. 130.
- **Technische Randbedingung:** Die Tabelle rechnet mit ihrem auf eine Dezimalstelle angegebenen Ausgangswert weiter.
- **Offene Fragen oder Widersprüche:** Der exakte Grundwert ist `23,25 cm`, die Tabelle druckt `23,2 cm`; die Weiterrechnung `23,2 + 3 = 26,2` ist konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Exakten Rechenwert und gedruckten Tabellenwert getrennt protokollieren; Rundungsregel nicht erfinden.

## HOF-B1-S130-F06 — Verbreiterte Hinterhosenbreite

- **Fachlicher Zweck:** Die Hinterhosenbreite aus dem Hüftumfang bestimmen und optional verbreitern.
- **Quelle:** `formeln_s130.md`, Zeile 35; Originaltranskript `s130.md`, Zeile 93; Buchseite 130.
- **Originalbezeichnung:** `¼ HüU +1 cm ± 0 bis +1`
- **Normalisierte Bezeichnung:** `hinterhosenbreite_bundfaltenhose`

### Buchfassung

```text
| hHoB | Hinterhosenbreite | ¼ HüU +1 cm ± 0 bis +1 | 25,2 | 26 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `grundzuschlag_hinten` | +1 cm | 1 | cm |
| `verbreiterung_hinten` | 0 bis +1 cm | wählbar | cm |

### Formel und Rechenschritte

```text
hinterhosenbreite_basis_exakt = (hueftumfang / 4) + grundzuschlag_hinten
                               = (97 cm / 4) + 1 cm
                               = 25,25 cm
Buchtabellenwert_basis        = 25,2 cm
hinterhosenbreite_min         = Buchtabellenwert_basis + 0 cm
                               = 25,2 cm
hinterhosenbreite_max         = Buchtabellenwert_basis + 1 cm
                               = 26,2 cm
Buchtabellenwert_geaendert    = 26 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich und Buchwahl | Einheit |
|---|---|---:|---|
| `hinterhosenbreite_bundfalte` | geänderte Hinterhosenbreite | 25,2 bis 26,2; eingetragen 26 | cm |

- **Abhängigkeiten:** Hüftumfang und gewählte Verbreiterung der Hinterhose.
- **Gültigkeitsbereich:** Konstruktionstabelle der Bundfaltenhose auf S. 130.
- **Technische Randbedingung:** Der eingetragene Wert `26 cm` liegt im belegten Bereich; der genaue Zuschlag wird nicht ausdrücklich genannt.
- **Offene Fragen oder Widersprüche:** Der exakte Grundwert ist `25,25 cm`, die Tabelle druckt `25,2 cm`; keine Rundungsregel ist belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereich und gewählten Tabellenwert getrennt speichern; keinen Zuschlag von `0,8 cm` als Buchregel festschreiben.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s130.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Festgelegter Eingabewert `Bundfalteninhalt = 6 cm`; keine berechnete Ausgabe |
| Zeile 40 | 1 | Kniehöhe; Wiederholung von `HOF-B1-S120-F06` |
| **Summe** | **2** | **1 Eingabewert und 1 Wiederholung ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s130.md` enthält in Zeile 20 die Beziehung `vHoB1 = vHoB + ½ gewünschter Bundfalteninhalt`; sie fehlt in `formeln_s130.md`, ist aber als Zeichnungsbeschriftung in `formeln_s131.md` extrahiert und wird dort normalisiert. Die Aufteilung des gesamten Bundfalteninhalts auf 4 cm und 2 cm in den Zeilen 48–54 fehlt im Extrakt und wurde hier nicht als zusätzliche Buchfassung erzeugt.
