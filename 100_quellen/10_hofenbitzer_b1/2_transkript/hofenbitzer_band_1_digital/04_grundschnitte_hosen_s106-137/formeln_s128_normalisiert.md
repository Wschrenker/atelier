# Fachlich normalisierte Formeln — S. 128

Quelle der Normalisierung: `formeln_s128.md`
Originaltranskript: `s128.md`
Buchseite: Hofenbitzer, Band 1, S. 128

## HOF-B1-S128-F01 — Dehnung der Materialprobe in Zentimetern

- **Fachlicher Zweck:** Die absolute Dehnung einer Materialprobe aus gedehnter und ungedehnter Breite bestimmen.
- **Quelle:** `formeln_s128.md`, Zeilen 19, 24, 29 und 34; Originaltranskript `s128.md`, Zeilen 38–44; Buchseite 128.
- **Originalbezeichnung:** `Dehnung = Dehnungsbreite − Ausgangsbreite`
- **Normalisierte Bezeichnung:** `materialdehnung_cm`

### Buchfassung

```text
Dehnungsbreite = 24 cm
```

```text
− Ausgangsbreite = 20 cm ≙ 100 %
```

```text
Dehnung = 24 cm − 20 cm
```

```text
= 4 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `dehnungsbreite` | Dehnungsbreite | 24 | cm |
| `ausgangsbreite` | Ausgangsbreite | 20 | cm |

### Formel und Rechenschritte

```text
materialdehnung_cm = dehnungsbreite - ausgangsbreite
                    = 24 cm - 20 cm
                    = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `materialdehnung_cm` | absolute Breitenzunahme der Materialprobe | 4 | cm |

- **Abhängigkeiten:** Zwei Messungen derselben Materialprobe in Schussrichtung.
- **Gültigkeitsbereich:** Bestimmung der Materialdehnung vor der Konstruktion der weitenreduzierten engen Hose.
- **Technische Randbedingung:** Beide Breiten müssen mit derselben auf die gewünschte Kompression abgestimmten Dehnkraft und in derselben Einheit gemessen werden.
- **Offene Fragen oder Widersprüche:** Keine; `24 cm − 20 cm = 4 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Negative oder null Ausgangsbreiten sperren; eine negative Dehnung als Mess- oder Eingabefehler behandeln.

## HOF-B1-S128-F02 — Prozentuale Dehnung der Materialprobe

- **Fachlicher Zweck:** Die absolute Dehnung auf die Ausgangsbreite beziehen und als Prozentwert bestimmen.
- **Quelle:** `formeln_s128.md`, Zeilen 9, 14, 39, 44 und 49; Originaltranskript `s128.md`, Zeilen 30–34 und 46–50; Buchseite 128.
- **Originalbezeichnung:** `Dehnung in % = (100 % · Dehnung) / Ausgangsbreite`
- **Normalisierte Bezeichnung:** `materialdehnung_prozent`

### Buchfassung

```text
− Ausgangsbreite in cm ≙ 100 %
```

```text
Dehnung in cm ≙ x %
```

```text
Dehnung in % = (100 % · Dehnung) / Ausgangsbreite
```

```text
= (100 % · 4 cm) / 20 cm
```

```text
= 20 %
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `materialdehnung_cm` | Dehnung | 4 | cm |
| `ausgangsbreite` | Ausgangsbreite | 20 | cm |
| `prozentbasis` | 100 % | 100 | % |

### Formel und Rechenschritte

```text
materialdehnung_prozent = (100 % * materialdehnung_cm) / ausgangsbreite
                         = (100 % * 4 cm) / 20 cm
                         = 20 %
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `materialdehnung_prozent` | Dehnung bezogen auf die Ausgangsbreite | 20 | % |

- **Abhängigkeiten:** `materialdehnung_cm` aus `HOF-B1-S128-F01` und gemessene Ausgangsbreite.
- **Gültigkeitsbereich:** Materialprobe und Messrichtung der Dehnungsbestimmung auf S. 128.
- **Technische Randbedingung:** Die Ausgangsbreite muss größer als null sein.
- **Offene Fragen oder Widersprüche:** Keine; `(100 % · 4 cm) / 20 cm = 20 %`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern als dimensionslosen Quotienten `materialdehnung_cm / ausgangsbreite` speichern und für die Anzeige mit 100 multiplizieren.

## HOF-B1-S128-F03 — Viertel-Knieweite mit Abzug

- **Fachlicher Zweck:** Den beidseitig von P13 abzutragenden Betrag der reduzierten Knieweite bestimmen.
- **Quelle:** `formeln_s128.md`, Zeile 54; Originaltranskript `s128.md`, Zeile 64; Buchseite 128.
- **Originalbezeichnung:** `KnU : 4 − 0,5 cm`
- **Normalisierte Bezeichnung:** `knieweitenbetrag_vorderhose_reduziert`

### Buchfassung

```text
22./23. Die Knieweite KnU : 4 − 0,5 cm von P13 aus nach links und rechts abtragen → P22 und P23.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `knieumfang_reduziert` | KnU | 30,6 | cm |
| `knieweiten_abzug` | 0,5 cm | 0,5 | cm |

### Formel und Rechenschritte

```text
knieweitenbetrag = (knieumfang_reduziert / 4) - knieweiten_abzug
                  = (30,6 cm / 4) - 0,5 cm
                  = 7,15 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `knieweitenbetrag` | Betrag links und rechts von P13 | 7,15 | cm |

- **Abhängigkeiten:** Reduzierter Knieumfang aus `HOF-B1-S128-F08`.
- **Gültigkeitsbereich:** Vorderhose der weitenreduzierten engen Hose auf S. 128.
- **Technische Randbedingung:** Derselbe Betrag wird beidseitig von P13 abgetragen.
- **Offene Fragen oder Widersprüche:** Keine; `30,6 / 4 − 0,5 = 7,15`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Reduzierten Umfang vor der Viertelung eindeutig auswählen und den Betrag symmetrisch anwenden.

## HOF-B1-S128-F04 — Viertel-Wadenweite mit Abzug

- **Fachlicher Zweck:** Den beidseitig von P13a abzutragenden Betrag der reduzierten Wadenweite bestimmen.
- **Quelle:** `formeln_s128.md`, Zeile 59; Originaltranskript `s128.md`, Zeile 66; Buchseite 128.
- **Originalbezeichnung:** `WaU : 4 − 0,5 cm`
- **Normalisierte Bezeichnung:** `wadenweitenbetrag_vorderhose_reduziert`

### Buchfassung

```text
22a./23a. Die Wadenweite WaU : 4 − 0,5 cm von P13a aus nach links und rechts abtragen → P22a und P23a.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `wadenumfang_reduziert` | WaU | 31,5 | cm |
| `wadenweiten_abzug` | 0,5 cm | 0,5 | cm |

### Formel und Rechenschritte

```text
wadenweitenbetrag = (wadenumfang_reduziert / 4) - wadenweiten_abzug
                   = (31,5 cm / 4) - 0,5 cm
                   = 7,375 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `wadenweitenbetrag` | Betrag links und rechts von P13a | 7,375 | cm |

- **Abhängigkeiten:** Reduzierter Wadenumfang aus `HOF-B1-S128-F09`.
- **Gültigkeitsbereich:** Vorderhose der weitenreduzierten engen Hose auf S. 128.
- **Technische Randbedingung:** Derselbe Betrag wird beidseitig von P13a abgetragen.
- **Offene Fragen oder Widersprüche:** Keine; `31,5 / 4 − 0,5 = 7,375`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Rundung erst bei der Ausgabe oder nach einer später festzulegenden Konstruktionsregel anwenden.

## HOF-B1-S128-F05 — Reduzierter Taillenumfang

- **Fachlicher Zweck:** Den Taillenumfang für die weitenreduzierte enge Hose um 5 Prozent vermindern.
- **Quelle:** `formeln_s128.md`, Zeilen 80 und 85; Originaltranskript `s128.md`, Zeilen 148–150; Buchseite 128.
- **Originalbezeichnung:** `TaU − 5 %`
- **Normalisierte Bezeichnung:** `taillenumfang_reduziert`

### Buchfassung

```text
TaU − 5 %
```

```text
= 72 cm · 0,95 = 68,4 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |
| `reduktionssatz` | 5 % | 5 | % |

### Formel und Rechenschritte

```text
taillenumfang_reduziert = taillenumfang * (1 - reduktionssatz / 100)
                         = 72 cm * 0,95
                         = 68,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `taillenumfang_reduziert` | reduzierter Taillenumfang | 68,4 | cm |

- **Abhängigkeiten:** Gemessener Taillenumfang und gewählter Reduktionssatz.
- **Gültigkeitsbereich:** Buchbeispiel der weitenreduzierten engen Hose; die allgemeine Materialreduktion liegt laut Originaltranskript meist zwischen 5 und 20 Prozent.
- **Technische Randbedingung:** Auf S. 128 wird TaU abweichend von den weiteren gezeigten Umfängen nur um 5 Prozent reduziert.
- **Offene Fragen oder Widersprüche:** Die Überschrift des Abschnitts nennt eine Reduzierung um 10 Prozent, die gedruckte TaU-Formel verwendet jedoch 5 Prozent. Beide Angaben bleiben getrennt; die konkrete Rechnung ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Reduktionssatz je Umfangsmaß speichern und nicht pauschal aus der Abschnittsüberschrift übernehmen.

## HOF-B1-S128-F06 — Reduzierter Hüftumfang

- **Fachlicher Zweck:** Den Hüftumfang für die weitenreduzierte enge Hose um 10 Prozent vermindern.
- **Quelle:** `formeln_s128.md`, Zeilen 90 und 95; Originaltranskript `s128.md`, Zeilen 152–154; Buchseite 128.
- **Originalbezeichnung:** `HüU − 10 %`
- **Normalisierte Bezeichnung:** `hueftumfang_reduziert`

### Buchfassung

```text
HüU − 10 %
```

```text
= 97 cm · 0,9 = 87,3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `reduktionssatz` | 10 % | 10 | % |

### Formel und Rechenschritte

```text
hueftumfang_reduziert = hueftumfang * (1 - reduktionssatz / 100)
                       = 97 cm * 0,9
                       = 87,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hueftumfang_reduziert` | reduzierter Hüftumfang | 87,3 | cm |

- **Abhängigkeiten:** Gemessener Hüftumfang und gewählter Reduktionssatz.
- **Gültigkeitsbereich:** Buchbeispiel der weitenreduzierten engen Hose auf S. 128.
- **Technische Randbedingung:** Der Reduktionssatz muss als Prozentwert in einen Faktor umgerechnet werden.
- **Offene Fragen oder Widersprüche:** Keine; `97 cm · 0,9 = 87,3 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ausgangsmaß, Reduktionssatz und reduziertes Maß getrennt protokollieren.

## HOF-B1-S128-F07 — Unbezeichnete Reduktionsrechnung mit 55,5 cm

- **Fachlicher Zweck:** Die im extrahierten Bestand unbezeichnete Reduktionsrechnung mit dem Ausgangswert 55,5 cm erfassen.
- **Quelle:** `formeln_s128.md`, Zeile 100; Originaltranskript `s128.md`, Zeilen 156–158; Buchseite 128.
- **Originalbezeichnung:** Im extrahierten Bestand fehlt die zugehörige Zeile `OsU − 10 %`; vorhanden ist nur die Einsetzrechnung.
- **Normalisierte Bezeichnung:** `reduziertes_umfangsmass_55_5_offen`

### Buchfassung

```text
= 55,5 cm · 0,9 = 50,0 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `umfangsmass_ausgang_offen` | nicht bezeichnet | 55,5 | cm |
| `reduktionsfaktor` | nicht bezeichnet | 0,9 | dimensionslos |

### Formel und Rechenschritte

```text
umfangsmass_reduziert_offen = umfangsmass_ausgang_offen * reduktionsfaktor
                             = 55,5 cm * 0,9
                             = 49,95 cm
Buchwert                    = 50,0 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `umfangsmass_reduziert_offen` | reduzierter, im Extrakt unbezeichneter Umfang | 50,0 | cm |

- **Abhängigkeiten:** Ausgangswert und Faktor aus der Buchfassung.
- **Gültigkeitsbereich:** Zahlenrechnung auf S. 128; der fachliche Operand ist im verbindlichen Extrakt nicht benannt.
- **Technische Randbedingung:** `49,95 cm` wird im Buch auf eine Dezimalstelle zu `50,0 cm` gerundet.
- **Offene Fragen oder Widersprüche:** Das Originaltranskript bezeichnet die Rechnung als `OsU − 10 %`, doch diese Bezeichnungszeile fehlt in der extrahierten Formeldatei. Die Zuordnung zum Oberschenkelumfang darf erst nach Ergänzung der Extraktionsschicht verbindlich werden.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht als Oberschenkelumfang implementieren, solange der fehlende Quellenblock nicht extrahiert und geprüft ist.

## HOF-B1-S128-F08 — Unbezeichnete Reduktionsrechnung mit 34 cm

- **Fachlicher Zweck:** Die im extrahierten Bestand unbezeichnete Reduktionsrechnung mit dem Ausgangswert 34 cm erfassen.
- **Quelle:** `formeln_s128.md`, Zeile 105; Originaltranskript `s128.md`, Zeilen 160–162; Buchseite 128.
- **Originalbezeichnung:** Im extrahierten Bestand fehlt die zugehörige Zeile `KnU − 10 %`; vorhanden ist nur die Einsetzrechnung.
- **Normalisierte Bezeichnung:** `reduziertes_umfangsmass_34_offen`

### Buchfassung

```text
= 34 cm · 0,9 = 30,6 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `umfangsmass_ausgang_offen` | nicht bezeichnet | 34 | cm |
| `reduktionsfaktor` | nicht bezeichnet | 0,9 | dimensionslos |

### Formel und Rechenschritte

```text
umfangsmass_reduziert_offen = umfangsmass_ausgang_offen * reduktionsfaktor
                             = 34 cm * 0,9
                             = 30,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `umfangsmass_reduziert_offen` | reduzierter, im Extrakt unbezeichneter Umfang | 30,6 | cm |

- **Abhängigkeiten:** Ausgangswert und Faktor aus der Buchfassung.
- **Gültigkeitsbereich:** Zahlenrechnung auf S. 128; der fachliche Operand ist im verbindlichen Extrakt nicht benannt.
- **Technische Randbedingung:** Die Rechnung ist arithmetisch exakt.
- **Offene Fragen oder Widersprüche:** Das Originaltranskript bezeichnet die Rechnung als `KnU − 10 %`, doch diese Bezeichnungszeile fehlt in der extrahierten Formeldatei. Die Zuordnung zum Knieumfang bleibt bis zur Ergänzung der Extraktionsschicht offen.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht als Knieumfang implementieren, solange der fehlende Quellenblock nicht extrahiert und geprüft ist.

## HOF-B1-S128-F09 — Unbezeichnete Reduktionsrechnung mit 35 cm

- **Fachlicher Zweck:** Die im extrahierten Bestand unbezeichnete Reduktionsrechnung mit dem Ausgangswert 35 cm erfassen.
- **Quelle:** `formeln_s128.md`, Zeile 110; Originaltranskript `s128.md`, Zeilen 164–166; Buchseite 128.
- **Originalbezeichnung:** Im extrahierten Bestand fehlt die zugehörige Zeile `WaU − 10 %`; vorhanden ist nur die Einsetzrechnung.
- **Normalisierte Bezeichnung:** `reduziertes_umfangsmass_35_offen`

### Buchfassung

```text
= 35 cm · 0,9 = 31,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `umfangsmass_ausgang_offen` | nicht bezeichnet | 35 | cm |
| `reduktionsfaktor` | nicht bezeichnet | 0,9 | dimensionslos |

### Formel und Rechenschritte

```text
umfangsmass_reduziert_offen = umfangsmass_ausgang_offen * reduktionsfaktor
                             = 35 cm * 0,9
                             = 31,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `umfangsmass_reduziert_offen` | reduzierter, im Extrakt unbezeichneter Umfang | 31,5 | cm |

- **Abhängigkeiten:** Ausgangswert und Faktor aus der Buchfassung.
- **Gültigkeitsbereich:** Zahlenrechnung auf S. 128; der fachliche Operand ist im verbindlichen Extrakt nicht benannt.
- **Technische Randbedingung:** Die Rechnung ist arithmetisch exakt.
- **Offene Fragen oder Widersprüche:** Das Originaltranskript bezeichnet die Rechnung als `WaU − 10 %`, doch diese Bezeichnungszeile fehlt in der extrahierten Formeldatei. Die Zuordnung zum Wadenumfang bleibt bis zur Ergänzung der Extraktionsschicht offen.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht als Wadenumfang implementieren, solange der fehlende Quellenblock nicht extrahiert und geprüft ist.

## HOF-B1-S128-F10 — Unbezeichnete Reduktionsrechnung mit 32 cm

- **Fachlicher Zweck:** Die im extrahierten Bestand unbezeichnete Reduktionsrechnung mit dem Ausgangswert 32 cm erfassen.
- **Quelle:** `formeln_s128.md`, Zeile 115; Originaltranskript `s128.md`, Zeilen 168–170; Buchseite 128.
- **Originalbezeichnung:** Im extrahierten Bestand fehlt die zugehörige Zeile `RiU − 10 %`; vorhanden ist nur die Einsetzrechnung.
- **Normalisierte Bezeichnung:** `reduziertes_umfangsmass_32_offen`

### Buchfassung

```text
= 32 cm · 0,9 = 28,8 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `umfangsmass_ausgang_offen` | nicht bezeichnet | 32 | cm |
| `reduktionsfaktor` | nicht bezeichnet | 0,9 | dimensionslos |

### Formel und Rechenschritte

```text
umfangsmass_reduziert_offen = umfangsmass_ausgang_offen * reduktionsfaktor
                             = 32 cm * 0,9
                             = 28,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `umfangsmass_reduziert_offen` | reduzierter, im Extrakt unbezeichneter Umfang | 28,8 | cm |

- **Abhängigkeiten:** Ausgangswert und Faktor aus der Buchfassung.
- **Gültigkeitsbereich:** Zahlenrechnung auf S. 128; der fachliche Operand ist im verbindlichen Extrakt nicht benannt.
- **Technische Randbedingung:** Die Rechnung ist arithmetisch exakt.
- **Offene Fragen oder Widersprüche:** Das Originaltranskript bezeichnet die Rechnung als `RiU − 10 %`, doch diese Bezeichnungszeile fehlt in der extrahierten Formeldatei. Die Zuordnung zum Ristumfang bleibt bis zur Ergänzung der Extraktionsschicht offen.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht als Ristumfang implementieren, solange der fehlende Quellenblock nicht extrahiert und geprüft ist.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s128.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 64 | 1 | Leere BuU-Tabellenzeile ohne Werte |
| Zeilen 69–70 | 2 | Vorder- und Hinterhosenbreite; Wiederholungen von `HOF-B1-S120-F04` und `HOF-B1-S120-F05`, hier mit reduziertem Hüftumfang |
| Zeile 75 | 1 | Kniehöhe; Wiederholung von `HOF-B1-S120-F06` |
| **Summe** | **4** | **4 Wiederholungen oder leere Tabellenzeilen ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s128.md` enthält in den Zeilen 156, 160, 164 und 168 die Bezeichnungszeilen `OsU − 10 %`, `KnU − 10 %`, `WaU − 10 %` und `RiU − 10 %`. Diese vier Zeilen fehlen in `formeln_s128.md`; dort stehen nur die jeweiligen Einsetzrechnungen. `HOF-B1-S128-F07` bis `F10` erfassen deshalb ausschließlich die vorhandenen Rechnungen und bleiben hinsichtlich ihres fachlichen Operanden `offen`. Die Zuordnungen dürfen erst nach Ergänzung der Extraktionsschicht verbindlich normalisiert werden.
