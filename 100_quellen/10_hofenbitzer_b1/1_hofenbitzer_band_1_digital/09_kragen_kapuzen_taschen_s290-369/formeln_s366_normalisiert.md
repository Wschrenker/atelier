# Fachlich normalisierte Formeln — S. 366 und S. 367

Quelle der Normalisierung: `formeln_s366_digital_geprüft.md`, zusätzliche Anwendungsnachweise in `formeln_s367_digital_geprüft.md`
Originaltranskripte: `s366_digital_geprüft.md`, `s367_digital_geprüft.md`
Buchseiten: Hofenbitzer, Band 1, S. 366 und S. 367
Extraktionsstand: v2

## HOF-B1-S366-F01 — Gesamtbreite der beiden Paspeln

- **Fachlicher Zweck:** Die Gesamtbreite zweier gleich breiter Paspeln aus der einzelnen Paspelbreite bestimmen.
- **Quelle:** `formeln_s366_digital_geprüft.md`, Zeile 9; Originaltranskript `s366_digital_geprüft.md`, Zeile 30; zusätzlicher Anwendungsnachweis in `formeln_s367_digital_geprüft.md`, Zeile 37, und `s367_digital_geprüft.md`, Zeile 80; Buchseiten 366 und 367.
- **Originalbezeichnung:** `2 x Paspelbreite`, `2 × Paspel-Breite`
- **Normalisierte Bezeichnung:** `gesamtbreite_zweier_paspeln`

### Buchfassung

```text
- `2 x Paspelbreite je 0,5 cm = 1 cm`
```

Zusätzlicher Anwendungsnachweis auf S. 367:

```text
- `2 × Paspel-Breite`
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert auf S. 366 | Einheit |
|---|---|---:|---|
| `paspelbreite` | Paspelbreite | 0,5 | cm |
| `anzahl_paspeln` | `2 x`, `2 ×` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
gesamtbreite_zweier_paspeln = anzahl_paspeln * paspelbreite
                              = 2 * paspelbreite
Buchwert S. 366:             = 2 * 0,5 cm
                              = 1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchwert auf S. 366 | Einheit |
|---|---|---:|---|
| `gesamtbreite_zweier_paspeln` | Gesamtbreite der zwei Paspeln | 1 | cm |

- **Abhängigkeiten:** Eine für die Tasche festgelegte `paspelbreite`.
- **Gültigkeitsbereich:** Gerade Paspeltasche auf S. 366 und paspelierte Pattentasche auf S. 367 mit zwei gleich breiten Paspeln.
- **Technische Randbedingung:** Die Paspelbreite muss als nichtnegative Länge vorliegen. Der Faktor `2` gilt für die zwei hier dargestellten Paspeln.
- **Offene Fragen oder Widersprüche:** Kein Widerspruch; `2 * 0,5 cm = 1 cm` ist rechnerisch richtig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die einzelne Paspelbreite als Eingabe führen und die Gesamtbreite mit dem festen, für diese Konstruktionen belegten Faktor `2` berechnen.

## HOF-B1-S366-F02 — Zuschnittbreite eines einzelnen Paspelstreifens

- **Fachlicher Zweck:** Die Zuschnittbreite eines Paspelstreifens aus dreifacher Paspelbreite und einer zusätzlichen Breite bestimmen.
- **Quelle:** `formeln_s366_digital_geprüft.md`, Zeilen 21 und 39; Originaltranskript `s366_digital_geprüft.md`, Zeilen 37 und 81; zusätzliche Anwendungsnachweise in `formeln_s367_digital_geprüft.md`, Zeilen 20 und 38, und `s367_digital_geprüft.md`, Zeilen 44 und 81; Buchseiten 366 und 367.
- **Originalbezeichnung:** `3 x Paspelbreite + 1 bis 1,5 cm`, `3 × Paspelbreite + 1 cm`
- **Normalisierte Bezeichnung:** `zuschnittbreite_einzelner_paspelstreifen`

### Buchfassung

Gerade Paspeltasche auf S. 366:

```text
- oberer Paspelstreifen `1× OSt`: `(3 x Paspelbreite + 1 bis 1,5 cm)`
```

Schräge Paspeltasche auf S. 366:

```text
- Paspelstreifen `2× OSt`: `(3 x Paspelbreite + 1 bis 1,5 cm)`
```

Geschweifte Paspeltasche auf S. 367:

```text
- Paspelstreifen `2× OSt`: `3 × Paspelbreite + 1 cm`
```

Paspelierte Pattentasche auf S. 367:

```text
- Paspelstreifen `2× OSt`: `3 × Paspelbreite + 1 bis 1,5 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `paspelbreite` | Paspelbreite | variabel | cm |
| `zusatzbreite_einzelstreifen` | zusätzliche Breite | 1 bis 1,5; bei der geschweiften Paspeltasche 1 | cm |
| `paspelbreiten_faktor` | `3 x`, `3 ×` | 3 | dimensionslos |

### Formel und Rechenschritte

```text
zuschnittbreite_einzelner_paspelstreifen = 3 * paspelbreite + zusatzbreite_einzelstreifen

Allgemeiner Bereich S. 366–367:
zuschnittbreite_min = 3 * paspelbreite + 1 cm
zuschnittbreite_max = 3 * paspelbreite + 1,5 cm

Geschweifte Paspeltasche S. 367:
zuschnittbreite_einzelner_paspelstreifen = 3 * paspelbreite + 1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `zuschnittbreite_einzelner_paspelstreifen` | Zuschnittbreite eines oberen, schrägen oder paarweise zugeschnittenen Paspelstreifens | cm |

- **Abhängigkeiten:** Eine festgelegte `paspelbreite` und die für die Variante gewählte `zusatzbreite_einzelstreifen`.
- **Gültigkeitsbereich:** Gerade und schräge Paspeltasche auf S. 366 sowie geschweifte Paspeltasche und paspelierte Pattentasche auf S. 367.
- **Technische Randbedingung:** Paspelbreite und Zusatzbreite müssen in derselben Längeneinheit vorliegen. Für die Bereichsangabe muss die Zusatzbreite ausdrücklich zwischen `1 cm` und `1,5 cm` gewählt werden.
- **Offene Fragen oder Widersprüche:** Kein rechnerischer Widerspruch. Die Quelle nennt keine Auswahlregel innerhalb des Bereichs `1 bis 1,5 cm`; bei der geschweiften Paspeltasche ist ausdrücklich `1 cm` gedruckt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Zusatzbreite als explizite Eingabe führen und auf den für die jeweilige Taschenvariante belegten Wert oder Bereich begrenzen; keine automatische Auswahlregel erfinden.

## HOF-B1-S366-F03 — Zuschnittbreite des unteren Paspelstreifens

- **Fachlicher Zweck:** Den unteren Paspelstreifen um die Kürzung des vorderen Taschenbeutels verlängern.
- **Quelle:** `formeln_s366_digital_geprüft.md`, Zeile 22; Originaltranskript `s366_digital_geprüft.md`, Zeile 38; Buchseite 366.
- **Originalbezeichnung:** `3 x Paspelbreite + 1 bis 1,5 cm + Kürzung des vorderen Tb`
- **Normalisierte Bezeichnung:** `zuschnittbreite_unterer_paspelstreifen`

### Buchfassung

```text
- unterer Paspelstreifen `1× OSt`: `(3 x Paspelbreite + 1 bis 1,5 cm + Kürzung des vorderen Tb)`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `paspelbreite` | Paspelbreite | variabel | cm |
| `zusatzbreite_einzelstreifen` | zusätzliche Breite | 1 bis 1,5 | cm |
| `kuerzung_vorderer_taschenbeutel` | Kürzung des vorderen Tb | 0 bis 2 laut Originaltranskript | cm |
| `paspelbreiten_faktor` | `3 x` | 3 | dimensionslos |

### Formel und Rechenschritte

```text
zuschnittbreite_unterer_paspelstreifen = 3 * paspelbreite
                                         + zusatzbreite_einzelstreifen
                                         + kuerzung_vorderer_taschenbeutel
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `zuschnittbreite_unterer_paspelstreifen` | um die Taschenbeutelkürzung verlängerte Zuschnittbreite des unteren Paspelstreifens | cm |

- **Abhängigkeiten:** `paspelbreite`, gewählte Zusatzbreite und tatsächliche Kürzung des vorderen Taschenbeutels. Die Kürzung `0 bis 2 cm` steht im Originaltranskript, ist im extrahierten Formelblock aber nur als benannter Summand enthalten.
- **Gültigkeitsbereich:** Gerade Paspeltasche auf S. 366, wenn der vordere Taschenbeutel gekürzt wird und oberer und unterer Paspelstreifen getrennt zugeschnitten werden.
- **Technische Randbedingung:** Alle Längen müssen in derselben Einheit vorliegen. Die Kürzung darf technisch erst nach einer fachlichen Wahl innerhalb des im Transkript genannten Bereichs eingesetzt werden.
- **Offene Fragen oder Widersprüche:** Kein Widerspruch. Die Quelle nennt keine Auswahlregel für die Zusatzbreite von `1 bis 1,5 cm` oder die Kürzung von `0 bis 2 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zusatzbreite und Taschenbeutelkürzung als getrennte Eingaben führen. Die Kürzung nicht in die Grundbreite des oberen Paspelstreifens einrechnen.

## HOF-B1-S366-F04 — Zuschnittbreite eines gemeinsamen Paspelstreifens

- **Fachlicher Zweck:** Die Zuschnittbreite eines gemeinsamen Streifens für obere und untere Paspel bestimmen und dabei eine Kürzung des vorderen Taschenbeutels ausgleichen.
- **Quelle:** `formeln_s366_digital_geprüft.md`, Zeilen 27 und 40; Originaltranskript `s366_digital_geprüft.md`, Zeilen 40 und 82; zusätzlicher Anwendungsnachweis in `formeln_s367_digital_geprüft.md`, Zeile 39, und `s367_digital_geprüft.md`, Zeile 82; Buchseiten 366 und 367.
- **Originalbezeichnung:** `6 x Paspelbreite + 2 bis 3 cm + Kürzung des vorderen Tb`
- **Normalisierte Bezeichnung:** `zuschnittbreite_gemeinsamer_paspelstreifen`

### Buchfassung

Gerade Paspeltasche auf S. 366:

```text
- Paspelstreifen `1× Ost`: `(6 x Paspelbreite + 2 bis 3 cm + Kürzung des vorderen Tb)`, für obere und untere Paspel
```

Schräge Paspeltasche auf S. 366:

```text
- Paspelstreifen `1× Ost`: `(6 x Paspelbreite + 2 bis 3 cm + Kürzung des vorderen Tb)`, für obere und untere Paspel
```

Paspelierte Pattentasche auf S. 367:

```text
- alternativ Paspelstreifen `1× OSt`: `6 × Paspelbreite + 2 bis 3 cm + Kürzung des vorderen Tb`, für obere und untere Paspel
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `paspelbreite` | Paspelbreite | variabel | cm |
| `zusatzbreite_gemeinsamer_streifen` | zusätzliche Breite | 2 bis 3 | cm |
| `kuerzung_vorderer_taschenbeutel` | Kürzung des vorderen Tb | 0 bis 2 laut Transkript S. 366 | cm |
| `paspelbreiten_faktor` | `6 x`, `6 ×` | 6 | dimensionslos |

### Formel und Rechenschritte

```text
zuschnittbreite_gemeinsamer_paspelstreifen = 6 * paspelbreite
                                             + zusatzbreite_gemeinsamer_streifen
                                             + kuerzung_vorderer_taschenbeutel
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `zuschnittbreite_gemeinsamer_paspelstreifen` | Zuschnittbreite des gemeinsamen Streifens für obere und untere Paspel | cm |

- **Abhängigkeiten:** `paspelbreite`, gewählte Zusatzbreite und tatsächliche Kürzung des vorderen Taschenbeutels.
- **Gültigkeitsbereich:** Alternative handwerkliche Fertigungsvariante mit einem gemeinsamen Paspelstreifen für gerade und schräge Paspeltaschen auf S. 366 sowie für die paspelierte Pattentasche auf S. 367.
- **Technische Randbedingung:** Alle Längen müssen in derselben Einheit vorliegen. Die Zusatzbreite muss ausdrücklich zwischen `2 cm` und `3 cm` gewählt werden; eine mögliche Taschenbeutelkürzung ist separat einzusetzen.
- **Offene Fragen oder Widersprüche:** Kein rechnerischer Widerspruch. Die Quelle nennt keine Auswahlregel innerhalb der Bereiche. Bei der schrägen Paspeltasche wurde der vordere Taschenbeutel laut Transkript nicht gekürzt; dort ist für die konkrete Anwendung daher `kuerzung_vorderer_taschenbeutel = 0 cm` anzusetzen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Diese Alternative getrennt von zwei einzelnen Paspelstreifen modellieren. Zusatzbreite und Kürzung als explizite Eingaben führen und keine automatische Variantenwahl vornehmen.

## Ausgeschlossene Kandidaten

| Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s366_digital_geprüft.md`, Zeilen 14–16 | 3 | Taschenspiegel- und Taschenbeutel-Zuschnittbeschriftungen mit Stückzahl, Material und Kopieranweisung; keine berechnete Ausgabe |
| `formeln_s366_digital_geprüft.md`, Zeilen 32–34 | 3 | Wiederholte Taschenspiegel- und Taschenbeutel-Zuschnittbeschriftungen; keine Rechenformeln |
| `formeln_s367_digital_geprüft.md`, Zeile 9 | 1 | Produktionsbeschriftung `Oberstoff (2×)`; Stückzahl statt Multiplikationsausgabe |
| `formeln_s367_digital_geprüft.md`, Zeile 14 | 1 | Taschenbeutel-Zuschnittbeschriftung mit Stückzahl und Material |
| `formeln_s367_digital_geprüft.md`, Zeile 19 | 1 | Taschenspiegel-Zuschnittbeschriftung mit Stückzahl und Material |
| `formeln_s367_digital_geprüft.md`, Zeile 25 | 1 | Wiederholte Produktionsbeschriftung `Oberstoff (2×)` |
| `formeln_s367_digital_geprüft.md`, Zeilen 30–32 | 3 | Patten- und Taschenbeutel-Zuschnittbeschriftungen mit Stückzahl, Material und Einlage |
| **Summe** | **13** | **13 Produktions-, Zuschnitt- oder Kopierbeschriftungen** |

## Extraktionsgrenze

Die Originaltranskripte enthalten weitere formelartige Beziehungen, die im verbindlichen Extrakt fehlen: Auf S. 366 entsprechen die Taschenbeuteltiefen ungefähr der Eingrifflänge (Zeilen 11, 32, 52 und 76), der untere Paspelstreifen wird um die tatsächliche Kürzung des vorderen Taschenbeutels verlängert (Zeilen 17–20), und der hintere Taschenbeutel wird für die Biese um die doppelte Biesentiefe geöffnet (Zeilen 66–68 und 80). Auf S. 367 wird der Taschenbeutel beidseitig um `0,3 cm` verbreitert (Zeilen 50–52 und 72). Diese Stellen wurden nicht als Buchfassungen erfunden. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
