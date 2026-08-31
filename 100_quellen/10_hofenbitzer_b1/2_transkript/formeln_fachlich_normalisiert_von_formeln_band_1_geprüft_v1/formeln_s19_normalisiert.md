# Fachlich normalisierte Formeln — S. 19

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/01_grundlagen_s8-31/formeln_s19.md`
Originaltranskript: `../Band_1_geprüft_v1/s19.md`
Buchseite: Hofenbitzer, Band 1, S. 19

## HOF-B1-S019-F01 — Halslochbreite aus Halsansatzumfang

- **Fachlicher Zweck:** Die Halslochbreite aus dem Halsansatzumfang bestimmen.
- **Quelle:** `formeln_s19.md`, Zeile 9; Originaltranskript `s19.md`, Zeile 29; Buchseite 19.
- **Originalbezeichnung:** `Halslochbreite HlB`
- **Normalisierte Bezeichnung:** `halslochbreite`

### Buchfassung

```text
| HaU | Halsansatzumfang | `HaU : 6 + 0,5 cm = Halslochbreite HlB` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Wert | Einheit |
|---|---|---|---:|---|
| `halsansatzumfang` | Halsansatzumfang | `HaU` | variabel | cm |
| `halsloch_divisor` | Teilungsfaktor | — | 6 | dimensionslos |
| `halsloch_zugabe` | feste Zugabe | — | 0,5 | cm |

### Formel und Rechenschritte

```text
halslochbreite = (halsansatzumfang / halsloch_divisor) + halsloch_zugabe
halsloch_divisor = 6
halsloch_zugabe = 0,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `halslochbreite` | Halslochbreite | `HlB` | cm |

- **Abhängigkeiten:** `halsansatzumfang`, `halsloch_divisor`, `halsloch_zugabe`.
- **Gültigkeitsbereich:** Rechenfeld der Maßtabelle auf S. 19.
- **Technische Randbedingung:** Der feste Divisor `6` ist ungleich `0`; Längenwerte müssen in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Das Kürzel `HaU` wird auf derselben Seite zusätzlich für „Handumfang“ verwendet. In dieser Formel ist durch die Tabellenzeile eindeutig der Halsansatzumfang gemeint.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Wegen der Kürzelkollision nicht allein `HaU` als technischen Variablennamen verwenden.

## HOF-B1-S019-F02 — Rückenlänge mit hinterer Taillenschräglage

- **Fachlicher Zweck:** Die gemessene Rückenlänge um die hintere Taillenschräglage zur Konstruktions-Rückenlänge anpassen.
- **Quelle:** `formeln_s19.md`, Zeile 10; Originaltranskript `s19.md`, Zeile 30; Buchseite 19.
- **Originalbezeichnung:** `Rückenlänge RüL`
- **Normalisierte Bezeichnung:** `rueckenlaenge`

### Buchfassung

```text
| gRüL | gemessene Rückenlänge | `± Taillenschräglage hinten = Rückenlänge RüL` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Einheit |
|---|---|---|---|
| `gemessene_rueckenlaenge` | gemessene Rückenlänge | `gRüL` | cm |
| `taillenschraeglage_hinten` | Taillenschräglage hinten | — | cm |

### Formel und Rechenschritte

```text
rueckenlaenge = gemessene_rueckenlaenge ± taillenschraeglage_hinten
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `rueckenlaenge` | angepasste Rückenlänge | `RüL` | cm |

- **Abhängigkeiten:** `gemessene_rueckenlaenge`, `taillenschraeglage_hinten`.
- **Gültigkeitsbereich:** Rechenfeld der Maßtabelle; die endgültigen Konstruktionswerte sollen laut S. 19 durch Figurbeobachtung ermittelt werden.
- **Technische Randbedingung:** Beide Längen müssen in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Die Buchfassung nennt nur `±`, aber keine belegte Entscheidungsregel für Addition oder Subtraktion.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bevor Vorzeichen und Herkunft der Taillenschräglage fachlich belegt sind.

## HOF-B1-S019-F03 — Brusttiefe aus gemessener Brusttiefe

- **Fachlicher Zweck:** Die Brusttiefe durch Abzug der Halslochbreite von der gemessenen Brusttiefe bestimmen.
- **Quelle:** `formeln_s19.md`, Zeile 11; Originaltranskript `s19.md`, Zeile 31; Buchseite 19.
- **Originalbezeichnung:** `Brusttiefe BrT`
- **Normalisierte Bezeichnung:** `brusttiefe`

### Buchfassung

```text
| gBrT | gemessene Brusttiefe | `r`, `l`, `Ø`; `gBrT - HlB = Brusttiefe BrT` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Einheit |
|---|---|---|---|
| `gemessene_brusttiefe` | gemessene Brusttiefe | `gBrT` | cm |
| `halslochbreite` | Halslochbreite | `HlB` | cm |

### Formel und Rechenschritte

```text
brusttiefe = gemessene_brusttiefe - halslochbreite
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `brusttiefe` | Brusttiefe | `BrT` | cm |

- **Abhängigkeiten:** `gemessene_brusttiefe`, `halslochbreite`; `halslochbreite` kann nach `HOF-B1-S019-F01` bestimmt werden.
- **Gültigkeitsbereich:** Rechenfeld der Maßtabelle auf S. 19; dort sind rechte, linke und durchschnittliche Messwerte vorgesehen.
- **Technische Randbedingung:** Beide Eingaben müssen in derselben Längeneinheit vorliegen.
- **Offene Fragen oder Widersprüche:** Die Formel legt nicht fest, ob `gBrT` der rechte, linke oder durchschnittliche Wert sein soll.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Messseite beziehungsweise Durchschnitt als eigenen, noch zu belegenden Auswahlparameter führen.

## HOF-B1-S019-F04 — Vorderlänge mit vorderer Taillenschräglage

- **Fachlicher Zweck:** Aus gemessener Vorderlänge und Halslochbreite eine Grundgröße bilden und diese um die vordere Taillenschräglage anpassen.
- **Quelle:** `formeln_s19.md`, Zeile 12; Originaltranskript `s19.md`, Zeile 32; Buchseite 19.
- **Originalbezeichnung:** `Vorderlänge VL`
- **Normalisierte Bezeichnung:** `vorderlaenge`

### Buchfassung

```text
| gVL | gemessene Vorderlänge | `r`, `l`, `Ø`; `gVL - HlB`; `± Taillenschräglage vorne = Vorderlänge VL` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Einheit |
|---|---|---|---|
| `gemessene_vorderlaenge` | gemessene Vorderlänge | `gVL` | cm |
| `halslochbreite` | Halslochbreite | `HlB` | cm |
| `taillenschraeglage_vorne` | Taillenschräglage vorne | — | cm |

### Formel und Rechenschritte

```text
vorderlaenge_grundwert = gemessene_vorderlaenge - halslochbreite
vorderlaenge = vorderlaenge_grundwert ± taillenschraeglage_vorne
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `vorderlaenge` | angepasste Vorderlänge | `VL` | cm |

- **Abhängigkeiten:** `gemessene_vorderlaenge`, `halslochbreite`, `taillenschraeglage_vorne`; `halslochbreite` kann nach `HOF-B1-S019-F01` bestimmt werden.
- **Gültigkeitsbereich:** Rechenfeld der Maßtabelle; die endgültigen Konstruktionswerte sollen laut S. 19 durch Figurbeobachtung ermittelt werden.
- **Technische Randbedingung:** Alle Längen müssen in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Die Verknüpfung der beiden notierten Rechenschritte ist als Abfolge lesbar, aber nicht mit einer vollständigen Buchgleichung ausgeschrieben. Außerdem fehlen die Auswahlregel für `r`, `l` oder `Ø` und die Vorzeichenregel für `±`.
- **Status:** `hypothetisch`
- **Hinweis für die spätere Python-Umsetzung:** Die dokumentierte Abfolge nicht als freigegebene Regel implementieren, bevor Auswahl und Vorzeichen geklärt sind.

## HOF-B1-S019-F05 — Kontrollwert der Armlochtiefe

- **Fachlicher Zweck:** Einen Kontrollwert für die Armlochtiefe aus Körperhöhe und Brustumfang berechnen.
- **Quelle:** `formeln_s19.md`, Zeile 13; Originaltranskript `s19.md`, Zeile 33; Buchseite 19.
- **Originalbezeichnung:** `Armlochtiefe AlT`
- **Normalisierte Bezeichnung:** `armlochtiefe_kontrollwert`

### Buchfassung

```text
| gAlT | gemessene Armlochtiefe | Kontrolle: `(KöH + BrU) : 10 - 6 cm = Armlochtiefe AlT` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Wert | Einheit |
|---|---|---|---:|---|
| `koerperhoehe` | Körperhöhe | `KöH` | variabel | cm |
| `brustumfang` | Brustumfang | `BrU` | variabel | cm |
| `armlochtiefe_divisor` | Teilungsfaktor | — | 10 | dimensionslos |
| `armlochtiefe_abzug` | fester Abzug | — | 6 | cm |

### Formel und Rechenschritte

```text
armlochtiefe_kontrollwert = ((koerperhoehe + brustumfang) / armlochtiefe_divisor) - armlochtiefe_abzug
armlochtiefe_divisor = 10
armlochtiefe_abzug = 6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `armlochtiefe_kontrollwert` | berechneter Kontrollwert der Armlochtiefe | `AlT` | cm |

- **Abhängigkeiten:** `koerperhoehe`, `brustumfang`, `armlochtiefe_divisor`, `armlochtiefe_abzug`.
- **Gültigkeitsbereich:** Die Tabellenzeile bezeichnet das Ergebnis ausdrücklich als Kontrolle der gemessenen Armlochtiefe.
- **Technische Randbedingung:** Körperhöhe, Brustumfang und Abzug müssen in kompatiblen Längeneinheiten vorliegen; der feste Divisor `10` ist ungleich `0`.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Mehrdeutigkeit; eine Regel zur Übernahme oder Korrektur des gemessenen Wertes steht nicht in dieser Formel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Kontrollwert und gemessenen Wert getrennt speichern; keine automatische Ersetzung ableiten.

## HOF-B1-S019-F06 — Rückenbreite aus gemessener Rückenbreite

- **Fachlicher Zweck:** Die Rückenbreite durch Halbierung der gemessenen Rückenbreite bestimmen.
- **Quelle:** `formeln_s19.md`, Zeile 14; Originaltranskript `s19.md`, Zeile 34; Buchseite 19.
- **Originalbezeichnung:** `RüB`
- **Normalisierte Bezeichnung:** `rueckenbreite`

### Buchfassung

```text
| gRüB | gemessene Rückenbreite | `gRüB : 2 = RüB` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Einheit |
|---|---|---|---|
| `gemessene_rueckenbreite` | gemessene Rückenbreite | `gRüB` | cm |
| `halbierungsfaktor` | Halbierung | — | dimensionslos |

### Formel und Rechenschritte

```text
rueckenbreite = gemessene_rueckenbreite / halbierungsfaktor
halbierungsfaktor = 2
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `rueckenbreite` | Rückenbreite | `RüB` | cm |

- **Abhängigkeiten:** `gemessene_rueckenbreite`, `halbierungsfaktor`.
- **Gültigkeitsbereich:** Rechenfeld der Maßtabelle auf S. 19.
- **Technische Randbedingung:** Der feste Divisor `2` ist ungleich `0`.
- **Offene Fragen oder Widersprüche:** Keine innerhalb der extrahierten Formel; sie stimmt mit `HOF-B1-S014-F01` überein.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Später eine gemeinsame, seitenbelegte Formeldefinition statt doppelter Implementierung verwenden.

## HOF-B1-S019-F07 — Brustbreite aus gemessener Brustbreite

- **Fachlicher Zweck:** Die Brustbreite durch Halbierung der gemessenen Brustbreite bestimmen.
- **Quelle:** `formeln_s19.md`, Zeile 19; Originaltranskript `s19.md`, Zeile 36; Buchseite 19.
- **Originalbezeichnung:** `BrB`
- **Normalisierte Bezeichnung:** `brustbreite_aus_messung`

### Buchfassung

```text
| gBrB | gemessene Brustbreite | `gBrB : 2 = BrB` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Einheit |
|---|---|---|---|
| `gemessene_brustbreite` | gemessene Brustbreite | `gBrB` | cm |
| `halbierungsfaktor` | Halbierung | — | dimensionslos |

### Formel und Rechenschritte

```text
brustbreite_aus_messung = gemessene_brustbreite / halbierungsfaktor
halbierungsfaktor = 2
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `brustbreite_aus_messung` | Brustbreite aus direkter Messung | `BrB` | cm |

- **Abhängigkeiten:** `gemessene_brustbreite`, `halbierungsfaktor`.
- **Gültigkeitsbereich:** Rechenfeld der Maßtabelle auf S. 19.
- **Technische Randbedingung:** Der feste Divisor `2` ist ungleich `0`.
- **Offene Fragen oder Widersprüche:** S. 14 enthält zusätzlich eine alternative Berechnung der Brustbreite aus `BrU`, `RüB` und `ArD`; die Methoden werden nicht gleichgesetzt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Messmethode und alternative Berechnung als getrennte Eingangswege führen.

## HOF-B1-S019-F08 — Brustumfang aus Teilstrecken

- **Fachlicher Zweck:** Den halben Brustumfang aus Rückenbreite, Armdurchmesser und Brustbreite kontrollieren und daraus den ganzen Brustumfang bilden.
- **Quelle:** `formeln_s19.md`, Zeile 20; Originaltranskript `s19.md`, Zeile 37; Buchseite 19.
- **Originalbezeichnung:** `BrU`
- **Normalisierte Bezeichnung:** `brustumfang_aus_teilstrecken`

### Buchfassung

```text
| BrU | Brustumfang waagerecht | `RüB + ArD + BrB = 1/2 BrU`; `Σ =`; `· 2 = BrU` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Einheit |
|---|---|---|---|
| `rueckenbreite` | Rückenbreite | `RüB` | cm |
| `armdurchmesser` | Armdurchmesser | `ArD` | cm |
| `brustbreite` | Brustbreite | `BrB` | cm |
| `verdoppelungsfaktor` | Verdopplung | — | dimensionslos |

### Formel und Rechenschritte

```text
halber_brustumfang_aus_teilstrecken = rueckenbreite + armdurchmesser + brustbreite
brustumfang_aus_teilstrecken = halber_brustumfang_aus_teilstrecken * verdoppelungsfaktor
verdoppelungsfaktor = 2
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `brustumfang_aus_teilstrecken` | aus den Teilstrecken rekonstruierter Brustumfang | `BrU` | cm |

- **Abhängigkeiten:** `rueckenbreite`, `armdurchmesser`, `brustbreite`, `verdoppelungsfaktor`.
- **Gültigkeitsbereich:** Rechen- und Kontrollfelder der Maßtabelle auf S. 19.
- **Technische Randbedingung:** Alle Teilstrecken müssen in derselben Längeneinheit vorliegen.
- **Offene Fragen oder Widersprüche:** Die Felder `Σ =` und `· 2 = BrU` enthalten keine Zahlenwerte; die zweistufige Rechenfolge ist jedoch ausdrücklich notiert.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den rekonstruierten Brustumfang nicht ohne Toleranzregel mit einem gemessenen Brustumfang gleichsetzen.

## HOF-B1-S019-F09 — Optimale Balance bei BrU 100 bis 109 cm

- **Fachlicher Zweck:** Die optimale Balance für einen Brustumfang von 100 bis 109 cm bestimmen.
- **Quelle:** `formeln_s19.md`, Zeile 25; Originaltranskript `s19.md`, Zeile 71; Buchseite 19.
- **Originalbezeichnung:** `optimale Balance Bal`
- **Normalisierte Bezeichnung:** `optimale_balance_100_bis_109`

### Buchfassung

```text
| 100 bis 109 | `(BrU - 100) : 10 + 4,5` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Wert | Einheit |
|---|---|---|---:|---|
| `brustumfang` | Brustumfang | `BrU` | 100 bis 109 | cm |
| `bereichsbasis` | Untergrenze der Rechenstaffel | — | 100 | cm |
| `staffel_divisor` | Divisor der Staffel | — | 10 | dimensionslos |
| `balance_basiswert` | Basiswert der Balance | — | 4,5 | cm |

### Formel und Rechenschritte

```text
optimale_balance_100_bis_109 = ((brustumfang - bereichsbasis) / staffel_divisor) + balance_basiswert
bereichsbasis = 100 cm
staffel_divisor = 10
balance_basiswert = 4,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `optimale_balance_100_bis_109` | optimale Balance im angegebenen BrU-Bereich | `Bal` | cm |

- **Abhängigkeiten:** `brustumfang`, `bereichsbasis`, `staffel_divisor`, `balance_basiswert`.
- **Gültigkeitsbereich:** `100 cm <= brustumfang <= 109 cm` gemäß Tabellenzeile.
- **Technische Randbedingung:** Brustumfang, Bereichsbasis und Basiswert müssen in Zentimetern eingesetzt werden.
- **Offene Fragen oder Widersprüche:** Die Buchfassung nennt keine Rundungsregel für Zwischenwerte.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereichsgrenzen einschließlich behandeln; keine Interpolation außerhalb des Bereichs zulassen.

## HOF-B1-S019-F10 — Optimale Balance bei BrU 110 bis 119 cm

- **Fachlicher Zweck:** Die optimale Balance für einen Brustumfang von 110 bis 119 cm bestimmen.
- **Quelle:** `formeln_s19.md`, Zeile 26; Originaltranskript `s19.md`, Zeile 72; Buchseite 19.
- **Originalbezeichnung:** `optimale Balance Bal`
- **Normalisierte Bezeichnung:** `optimale_balance_110_bis_119`

### Buchfassung

```text
| 110 bis 119 | `(BrU - 100) : 10 + 5,0` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Wert | Einheit |
|---|---|---|---:|---|
| `brustumfang` | Brustumfang | `BrU` | 110 bis 119 | cm |
| `bereichsbasis` | Rechenbasis | — | 100 | cm |
| `staffel_divisor` | Divisor der Staffel | — | 10 | dimensionslos |
| `balance_basiswert` | Basiswert der Balance | — | 5,0 | cm |

### Formel und Rechenschritte

```text
optimale_balance_110_bis_119 = ((brustumfang - bereichsbasis) / staffel_divisor) + balance_basiswert
bereichsbasis = 100 cm
staffel_divisor = 10
balance_basiswert = 5,0 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `optimale_balance_110_bis_119` | optimale Balance im angegebenen BrU-Bereich | `Bal` | cm |

- **Abhängigkeiten:** `brustumfang`, `bereichsbasis`, `staffel_divisor`, `balance_basiswert`.
- **Gültigkeitsbereich:** `110 cm <= brustumfang <= 119 cm` gemäß Tabellenzeile.
- **Technische Randbedingung:** Brustumfang, Rechenbasis und Basiswert müssen in Zentimetern eingesetzt werden.
- **Offene Fragen oder Widersprüche:** Keine Rundungsregel ist angegeben; am Übergang der Tabellenbereiche entstehen unterschiedliche Basiswerte.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Tabellenbereiche als ausdrücklich getrennte Zweige abbilden, nicht zu einer einzigen linearen Formel zusammenziehen.

## HOF-B1-S019-F11 — Optimale Balance bei BrU 120 bis 129 cm

- **Fachlicher Zweck:** Die optimale Balance für einen Brustumfang von 120 bis 129 cm bestimmen.
- **Quelle:** `formeln_s19.md`, Zeile 27; Originaltranskript `s19.md`, Zeile 73; Buchseite 19.
- **Originalbezeichnung:** `optimale Balance Bal`
- **Normalisierte Bezeichnung:** `optimale_balance_120_bis_129`

### Buchfassung

```text
| 120 bis 129 | `(BrU - 100) : 10 + 5,5` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Wert | Einheit |
|---|---|---|---:|---|
| `brustumfang` | Brustumfang | `BrU` | 120 bis 129 | cm |
| `bereichsbasis` | Rechenbasis | — | 100 | cm |
| `staffel_divisor` | Divisor der Staffel | — | 10 | dimensionslos |
| `balance_basiswert` | Basiswert der Balance | — | 5,5 | cm |

### Formel und Rechenschritte

```text
optimale_balance_120_bis_129 = ((brustumfang - bereichsbasis) / staffel_divisor) + balance_basiswert
bereichsbasis = 100 cm
staffel_divisor = 10
balance_basiswert = 5,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `optimale_balance_120_bis_129` | optimale Balance im angegebenen BrU-Bereich | `Bal` | cm |

- **Abhängigkeiten:** `brustumfang`, `bereichsbasis`, `staffel_divisor`, `balance_basiswert`.
- **Gültigkeitsbereich:** `120 cm <= brustumfang <= 129 cm` gemäß Tabellenzeile.
- **Technische Randbedingung:** Brustumfang, Rechenbasis und Basiswert müssen in Zentimetern eingesetzt werden.
- **Offene Fragen oder Widersprüche:** Keine Rundungsregel ist angegeben; am Übergang der Tabellenbereiche entstehen unterschiedliche Basiswerte.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Tabellenbereiche als ausdrücklich getrennte Zweige abbilden.

## HOF-B1-S019-F12 — Optimale Balance bei BrU 130 bis 150 cm

- **Fachlicher Zweck:** Die optimale Balance für einen Brustumfang von 130 bis 150 cm bestimmen.
- **Quelle:** `formeln_s19.md`, Zeile 28; Originaltranskript `s19.md`, Zeile 74; Buchseite 19.
- **Originalbezeichnung:** `optimale Balance Bal`
- **Normalisierte Bezeichnung:** `optimale_balance_130_bis_150`

### Buchfassung

```text
| 130 bis 150 | `(BrU - 100) : 10 + 6,0` |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Wert | Einheit |
|---|---|---|---:|---|
| `brustumfang` | Brustumfang | `BrU` | 130 bis 150 | cm |
| `bereichsbasis` | Rechenbasis | — | 100 | cm |
| `staffel_divisor` | Divisor der Staffel | — | 10 | dimensionslos |
| `balance_basiswert` | Basiswert der Balance | — | 6,0 | cm |

### Formel und Rechenschritte

```text
optimale_balance_130_bis_150 = ((brustumfang - bereichsbasis) / staffel_divisor) + balance_basiswert
bereichsbasis = 100 cm
staffel_divisor = 10
balance_basiswert = 6,0 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `optimale_balance_130_bis_150` | optimale Balance im angegebenen BrU-Bereich | `Bal` | cm |

- **Abhängigkeiten:** `brustumfang`, `bereichsbasis`, `staffel_divisor`, `balance_basiswert`.
- **Gültigkeitsbereich:** `130 cm <= brustumfang <= 150 cm` gemäß Tabellenzeile.
- **Technische Randbedingung:** Brustumfang, Rechenbasis und Basiswert müssen in Zentimetern eingesetzt werden.
- **Offene Fragen oder Widersprüche:** Keine Rundungsregel ist angegeben; der letzte Bereich umfasst 21 ganzzahlige Zentimeterwerte und ist breiter als die vorigen Bereiche.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Obere Grenze `150 cm` einschließlich behandeln und keine Extrapolation über diesen Bereich ergänzen.

## HOF-B1-S019-F13 — Individuelle Balance

- **Fachlicher Zweck:** Die individuelle Balance als Differenz von Vorderlänge und Rückenlänge bestimmen.
- **Quelle:** `formeln_s19.md`, Zeile 33; Originaltranskript `s19.md`, Zeile 78; Buchseite 19.
- **Originalbezeichnung:** `individuelle Balance`
- **Normalisierte Bezeichnung:** `individuelle_balance`

### Buchfassung

```text
- `VL minus RüL = individuelle Balance`.
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Einheit |
|---|---|---|---|
| `vorderlaenge` | Vorderlänge | `VL` | cm |
| `rueckenlaenge` | Rückenlänge | `RüL` | cm |

### Formel und Rechenschritte

```text
individuelle_balance = vorderlaenge - rueckenlaenge
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `individuelle_balance` | individuelle Balance | cm |

- **Abhängigkeiten:** `vorderlaenge`, `rueckenlaenge`.
- **Gültigkeitsbereich:** Rechenfeld „Balance“ der Maßtabelle auf S. 19.
- **Technische Randbedingung:** Vorder- und Rückenlänge müssen in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Die Eingangsgrößen hängen von den noch offenen Vorzeichen- und Auswahlregeln in `HOF-B1-S019-F02` und `HOF-B1-S019-F04` ab.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Differenz selbst ist eindeutig; vorgelagerte offene Formeln müssen separat gesperrt bleiben.

## HOF-B1-S019-F14 — Balance-Problem

- **Fachlicher Zweck:** Die Abweichung der individuellen Balance von der optimalen Balance bestimmen.
- **Quelle:** `formeln_s19.md`, Zeile 34; Originaltranskript `s19.md`, Zeile 79; Buchseite 19.
- **Originalbezeichnung:** `Balance-Problem`
- **Normalisierte Bezeichnung:** `balance_problem`

### Buchfassung

```text
- `Bal - individuelle Balance = Balance-Problem`.
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Einheit |
|---|---|---|---|
| `optimale_balance` | optimale Balance | `Bal` | cm |
| `individuelle_balance` | individuelle Balance | — | cm |

### Formel und Rechenschritte

```text
balance_problem = optimale_balance - individuelle_balance
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `balance_problem` | Differenz zwischen optimaler und individueller Balance | cm |

- **Abhängigkeiten:** `optimale_balance`, `individuelle_balance`; die individuelle Balance wird in `HOF-B1-S019-F13` berechnet, die optimale Balance für die extrahierten Bereiche in `HOF-B1-S019-F09` bis `HOF-B1-S019-F12`.
- **Gültigkeitsbereich:** Rechenfeld „Balance“ der Maßtabelle. Für `BrU` 80 bis 99 cm nennt das Originaltranskript feste Werte, die nicht Bestandteil der extrahierten Formeldatei sind.
- **Technische Randbedingung:** Beide Eingaben müssen in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Die Quelle bezeichnet das Ergebnis als „Balance-Problem“, gibt in der Formel selbst aber keine Bewertung des Vorzeichens vor. Der Hinweistext erlaubt Abweichungen bis 1 cm unter einer zusätzlichen Beobachtungsbedingung; daraus wird hier keine automatische Entscheidung abgeleitet.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Differenzwert und fachliche Bewertung trennen; Toleranz und Figurbeobachtung nicht ohne eigene belegte Regel automatisieren.
