# Fachlich normalisierte Formeln — S. 177

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s177.md`
Originaltranskript: `../Band_1_geprüft_v1/s177.md`
Buchseite: Hofenbitzer, Band 1, S. 177

## HOF-B1-S177-F01 — Brustumfang zum Brustweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Brustumfang und Zugabe zum Brustweiten-Konstruktionsmaß addieren und halbieren.
- **Quelle:** `formeln_s177.md`, Zeile 24; Originaltranskript `s177.md`, Zeile 22; Buchseite 177.
- **Originalbezeichnung:** `BrU + 8 = BrW; ½ BrW`
- **Normalisierte Bezeichnung:** `brustweite_oberteil`

### Buchfassung

```text
| BrU | Brustumfang | 88 | + 8 | BrW = 96 | ½ = 48 | Kontrolle |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustumfang` | BrU | 88 | cm |
| `brustumfang_zugabe` | Zugabe | 8 | cm |

### Formel und Rechenschritte

```text
brustweite = brustumfang + brustumfang_zugabe
            = 88 cm + 8 cm
            = 96 cm
halbe_brustweite = brustweite / 2
                  = 96 cm / 2
                  = 48 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `brustweite` | BrW des ganzen Schnitts | 96 | cm |
| `halbe_brustweite` | ½ BrW | 48 | cm |

- **Abhängigkeiten:** BrU und für PK 4 gewählte BrU-Zugabe aus S. 176.
- **Gültigkeitsbereich:** Konstruktionstabelle des taillierten Oberteil-Grundschnitts, Größe 38, PK 4.
- **Technische Randbedingung:** Erst die Ganzumfangszugabe addieren, danach halbieren.
- **Offene Fragen oder Widersprüche:** Keine; beide Druckergebnisse stimmen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ganzes und halbes Modellmaß getrennt speichern.

## HOF-B1-S177-F02 — Taillenumfang zum Taillenweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Taillenumfang und gewählte Zugabe addieren und das Ergebnis halbieren.
- **Quelle:** `formeln_s177.md`, Zeile 25; Originaltranskript `s177.md`, Zeile 23; Buchseite 177.
- **Originalbezeichnung:** `TaU + 6 = TaW; ½ TaW`
- **Normalisierte Bezeichnung:** `taillenweite_oberteil`

### Buchfassung

```text
| TaU | Taillenumfang | 72 | + 6 | TaW = 78 | ½ = 39 | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |
| `taillenumfang_zugabe` | gewählte Zugabe innerhalb PK-4-Bereich 4–8 | 6 | cm |

### Formel und Rechenschritte

```text
taillenweite = taillenumfang + taillenumfang_zugabe
              = 72 cm + 6 cm
              = 78 cm
halbe_taillenweite = taillenweite / 2
                    = 78 cm / 2
                    = 39 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `taillenweite` | TaW des ganzen Schnitts | 78 | cm |
| `halbe_taillenweite` | ½ TaW | 39 | cm |

- **Abhängigkeiten:** TaU und gewählte TaU-Zugabe aus dem PK-4-Bereich auf S. 176.
- **Gültigkeitsbereich:** Taillierter Oberteil-Grundschnitt, Größe 38, PK 4.
- **Technische Randbedingung:** Der Wert 6 cm ist eine Auswahl innerhalb `4 bis 8 cm`; das Buch belegt keine allgemeine Auswahlregel.
- **Offene Fragen oder Widersprüche:** Keine in der Rechnung; Auswahlgrund für 6 cm bleibt offen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereich und gewählten Wert getrennt protokollieren.

## HOF-B1-S177-F03 — Hüftumfang zum Hüftweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Hüftumfang und gewählte Zugabe addieren und das Ergebnis halbieren.
- **Quelle:** `formeln_s177.md`, Zeile 26; Originaltranskript `s177.md`, Zeile 24; Buchseite 177.
- **Originalbezeichnung:** `HüU + 4 = HüW; ½ HüW`
- **Normalisierte Bezeichnung:** `hueftweite_oberteil`

### Buchfassung

```text
| HüU | Hüftumfang | 97 | + 4 | HüW = 101 | ½ = 50,5 | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `hueftumfang_zugabe` | gewählte Zugabe innerhalb PK-4-Bereich 4–8 | 4 | cm |

### Formel und Rechenschritte

```text
hueftweite = hueftumfang + hueftumfang_zugabe
            = 97 cm + 4 cm
            = 101 cm
halbe_hueftweite = hueftweite / 2
                  = 101 cm / 2
                  = 50,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hueftweite` | HüW des ganzen Schnitts | 101 | cm |
| `halbe_hueftweite` | ½ HüW | 50,5 | cm |

- **Abhängigkeiten:** HüU und gewählte HüU-Zugabe aus dem PK-4-Bereich auf S. 176.
- **Gültigkeitsbereich:** Taillierter Oberteil-Grundschnitt, Größe 38, PK 4.
- **Technische Randbedingung:** Der Wert 4 cm ist eine Auswahl innerhalb `4 bis 8 cm`; keine allgemeine Auswahlregel ergänzen.
- **Offene Fragen oder Widersprüche:** Keine in der Rechnung; Auswahlgrund für den unteren Bereichswert bleibt offen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereichsentscheidung als explizite Eingabe verlangen.

## HOF-B1-S177-F04 — Armlochtiefe mit Zugabe

- **Fachlicher Zweck:** Die Längenzugabe zur gemessenen Armlochtiefe addieren.
- **Quelle:** `formeln_s177.md`, Zeile 31; Originaltranskript `s177.md`, Zeile 30; Buchseite 177.
- **Originalbezeichnung:** `AIT + 1,7 = AIT+`
- **Normalisierte Bezeichnung:** `armlochtiefe_mit_zugabe`

### Buchfassung

```text
| AIT | Armlochtiefe | 20,1 | + 1,7 | AIT+ = 21,8 | | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefe` | AIT | 20,1 | cm |
| `armlochtiefe_zugabe` | PK-4-Zugabe | 1,7 | cm |

### Formel und Rechenschritte

```text
armlochtiefe_mit_zugabe = armlochtiefe + armlochtiefe_zugabe
                         = 20,1 cm + 1,7 cm
                         = 21,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefe_mit_zugabe` | AIT+ | 21,8 | cm |

- **Abhängigkeiten:** AIT und AIT-Zugabe der PK 4.
- **Gültigkeitsbereich:** Beispielkonstruktion auf S. 177.
- **Technische Randbedingung:** Die Längenzugabe wird einmal addiert.
- **Offene Fragen oder Widersprüche:** Keine; `20,1 + 1,7 = 21,8`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Körpermaß und Zugabe getrennt führen.

## HOF-B1-S177-F05 — Rückenbreite mit Zugabe

- **Fachlicher Zweck:** Die Zugabe zur halben Rückenbreite addieren.
- **Quelle:** `formeln_s177.md`, Zeile 36; Originaltranskript `s177.md`, Zeile 35; Buchseite 177.
- **Originalbezeichnung:** `RüB + 0,8 = RüB+`
- **Normalisierte Bezeichnung:** `rueckenbreite_mit_zugabe`

### Buchfassung

```text
| RüB | Rückenbreite (½) | 16,5 | + 0,8 | RüB+ = 17,3 | | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_rueckenbreite` | RüB | 16,5 | cm |
| `rueckenbreite_zugabe` | Zugabe | 0,8 | cm |

### Formel und Rechenschritte

```text
rueckenbreite_mit_zugabe = halbe_rueckenbreite + rueckenbreite_zugabe
                          = 16,5 cm + 0,8 cm
                          = 17,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `rueckenbreite_mit_zugabe` | RüB+ | 17,3 | cm |

- **Abhängigkeiten:** RüB und PK-4-Zugabe.
- **Gültigkeitsbereich:** Halbe Rückenbreite der Beispielkonstruktion.
- **Technische Randbedingung:** RüB ist bereits ein halbes Breitenmaß.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Halbmaßkennzeichnung im Datentyp erhalten.

## HOF-B1-S177-F06 — Armdurchmesser mit Zugabe und Teilungen

- **Fachlicher Zweck:** Den Armdurchmesser vergrößern und das Modellmaß vierteln beziehungsweise dritteln.
- **Quelle:** `formeln_s177.md`, Zeile 37; Originaltranskript `s177.md`, Zeile 36; Buchseite 177.
- **Originalbezeichnung:** `ArD + 2 = ArD+; ¼; ⅓`
- **Normalisierte Bezeichnung:** `armdurchmesser_mit_zugabe_und_teilungen`

### Buchfassung

```text
| ArD | Armdurchmesser | 9,3 | + 2 | ArD+ = 11,3 | ¼ = 2,8 ; ⅓ = 3,8 | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser` | ArD | 9,3 | cm |
| `armdurchmesser_zugabe` | Zugabe | 2 | cm |

### Formel und Rechenschritte

```text
armdurchmesser_mit_zugabe = 9,3 cm + 2 cm
                           = 11,3 cm
exakt: 11,3 cm / 4 = 2,825 cm
Buchwert: ¼ = 2,8 cm
exakt: 11,3 cm / 3 = 3,766666... cm
Buchwert: ⅓ = 3,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Exakter Wert | Buchwert | Einheit |
|---|---|---:|---:|---|
| `armdurchmesser_mit_zugabe` | ArD+ | 11,3 | 11,3 | cm |
| `viertel_armdurchmesser` | ¼ ArD+ | 2,825 | 2,8 | cm |
| `drittel_armdurchmesser` | ⅓ ArD+ | 3,766666… | 3,8 | cm |

- **Abhängigkeiten:** ArD, Zugabe und Teilungsfaktor.
- **Gültigkeitsbereich:** Beispielkonstruktion auf S. 177.
- **Technische Randbedingung:** Exakte Teilung und gedruckter Wert werden getrennt erhalten.
- **Offene Fragen oder Widersprüche:** Die Druckwerte entsprechen einer Rundung auf eine Dezimalstelle; eine allgemeine Rundungsregel ist im Kandidaten nicht genannt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern exakt rechnen und die Darstellungsrundung konfigurierbar halten.

## HOF-B1-S177-F07 — Brustbreite mit Zugabe

- **Fachlicher Zweck:** Die Zugabe zur halben Brustbreite addieren.
- **Quelle:** `formeln_s177.md`, Zeile 38; Originaltranskript `s177.md`, Zeile 37; Buchseite 177.
- **Originalbezeichnung:** `BrB + 1,2 = BrB+`
- **Normalisierte Bezeichnung:** `brustbreite_mit_zugabe`

### Buchfassung

```text
| BrB | Brustbreite (½) | 18,2 | + 1,2 | BrB+ = 19,4 | | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_brustbreite` | BrB | 18,2 | cm |
| `brustbreite_zugabe` | Zugabe | 1,2 | cm |

### Formel und Rechenschritte

```text
brustbreite_mit_zugabe = halbe_brustbreite + brustbreite_zugabe
                        = 18,2 cm + 1,2 cm
                        = 19,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `brustbreite_mit_zugabe` | BrB+ | 19,4 | cm |

- **Abhängigkeiten:** BrB und PK-4-Zugabe.
- **Gültigkeitsbereich:** Halbe Brustbreite der Beispielkonstruktion.
- **Technische Randbedingung:** BrB ist bereits ein halbes Breitenmaß.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Halbmaßkennzeichnung erhalten.

## HOF-B1-S177-F08 — Kontrolle der halben Brustweite

- **Fachlicher Zweck:** Körperbreiten und ihre Zugaben gegen die halbe Brustweite kontrollieren.
- **Quelle:** `formeln_s177.md`, Zeile 39; Originaltranskript `s177.md`, Zeile 38; Buchseite 177.
- **Originalbezeichnung:** `Kontrolle: Σ = ½ BrU; 44 + 4 = ½ BrW = 48`
- **Normalisierte Bezeichnung:** `kontrolle_halbe_brustweite`

### Buchfassung

```text
| Kontrolle: Σ = ½ BrU | | 44 | + 4 | ½ BrW = 48 | | Kontrolle |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halber_brustumfang` | ½ BrU / Summe RüB + ArD + BrB | 44 | cm |
| `brustbreiten_zugaben_summe` | Summe RüB-, ArD- und BrB-Zugabe | 4 | cm |

### Formel und Rechenschritte

```text
halber_brustumfang = 16,5 cm + 9,3 cm + 18,2 cm = 44 cm
brustbreiten_zugaben_summe = 0,8 cm + 2 cm + 1,2 cm = 4 cm
halbe_brustweite = halber_brustumfang + brustbreiten_zugaben_summe
                  = 44 cm + 4 cm
                  = 48 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `halbe_brustweite` | kontrollierte ½ BrW | 48 | cm |

- **Abhängigkeiten:** `HOF-B1-S177-F05` bis `F07` und halbe BrW aus `F01`.
- **Gültigkeitsbereich:** Breitenkontrolle der Beispielkonstruktion.
- **Technische Randbedingung:** Alle drei Körperbreiten und Zugaben müssen dieselbe halbe Schnittseite betreffen.
- **Offene Fragen oder Widersprüche:** Keine; beide Summen und die Kontrolle stimmen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Invariante prüfen und bei Abweichung einen Validierungsfehler ausgeben.

## HOF-B1-S177-F09 — Schulternahtlänge aus Schulterbreite

- **Fachlicher Zweck:** Die Schulterbreitenzugabe zur Schulterbreite addieren.
- **Quelle:** `formeln_s177.md`, Zeile 44; Originaltranskript `s177.md`, Zeile 46; Buchseite 177.
- **Originalbezeichnung:** `SuB + 0,4 = SuNL`
- **Normalisierte Bezeichnung:** `schulternahtlaenge`

### Buchfassung

```text
| SuB | Schulterbreite | 12,2 | + 0,4 | SuNL = 12,6 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `schulterbreite` | SuB | 12,2 | cm |
| `schulterbreite_zugabe` | Zugabe | 0,4 | cm |

### Formel und Rechenschritte

```text
schulternahtlaenge = schulterbreite + schulterbreite_zugabe
                    = 12,2 cm + 0,4 cm
                    = 12,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `schulternahtlaenge` | SuNL | 12,6 | cm |

- **Abhängigkeiten:** SuB und PK-4-SuB-Zugabe.
- **Gültigkeitsbereich:** Schulter der Beispielkonstruktion.
- **Technische Randbedingung:** Die Ausgabe ist eine Nahtlänge, obwohl die Eingabe als Breite bezeichnet wird.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Inkonsistenz.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Original- und Zielbezeichnung getrennt führen.

## HOF-B1-S177-F10 — Hintere Schulternahtlänge mit Einhalteweite

- **Fachlicher Zweck:** Eine gewählte Einhalteweite zur Schulternahtlänge addieren.
- **Quelle:** `formeln_s177.md`, Zeile 45; Originaltranskript `s177.md`, Zeile 47; Buchseite 177.
- **Originalbezeichnung:** `SuNL + Einhalteweite 0,5 cm bis 1 cm; + 0,7 = hSuNL`
- **Normalisierte Bezeichnung:** `hintere_schulternahtlaenge`

### Buchfassung

```text
| hSuNL | hintere Schulternahtlänge | „SuNL + Einhalteweite 0,5 cm bis 1 cm" | + 0,7 | hSuNL = 13,3 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `schulternahtlaenge` | SuNL | 12,6 | cm |
| `einhalteweite_schulter` | gewählte Einhalteweite aus 0,5 bis 1 | 0,7 | cm |

### Formel und Rechenschritte

```text
hintere_schulternahtlaenge = schulternahtlaenge + einhalteweite_schulter
                            = 12,6 cm + 0,7 cm
                            = 13,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hintere_schulternahtlaenge` | hSuNL | 13,3 | cm |

- **Abhängigkeiten:** SuNL aus `HOF-B1-S177-F09` und gewählte Einhalteweite.
- **Gültigkeitsbereich:** Hintere Schulter der Beispielkonstruktion.
- **Technische Randbedingung:** 0,7 cm ist ein gewählter Wert innerhalb des gedruckten Bereichs 0,5 bis 1 cm.
- **Offene Fragen oder Widersprüche:** Auswahlregel für 0,7 cm ist nicht belegt; die Rechnung stimmt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einhalteweite als expliziten Parameter mit Bereichsprüfung führen.

## HOF-B1-S177-F11 — Individuelle Balance

- **Fachlicher Zweck:** Die individuelle Balance als Differenz zwischen Vorder- und Rückenlänge bestimmen.
- **Quelle:** `formeln_s177.md`, Zeile 51; Originaltranskript `s177.md`, Zeile 56; Buchseite 177.
- **Originalbezeichnung:** `Differenz VL − RüL = individuelle Balance`
- **Normalisierte Bezeichnung:** `individuelle_balance`

### Buchfassung

```text
| Differenz VL − RüL = individuelle Balance = | | 3,7 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im extrahierten Kandidaten | Einheit |
|---|---|---:|---|
| `vorderlaenge` | VL | nicht enthalten | cm |
| `rueckenlaenge` | RüL | nicht enthalten | cm |

### Formel und Rechenschritte

```text
individuelle_balance = vorderlaenge - rueckenlaenge
Buchergebnis = 3,7 cm

Kontextkontrolle im Originaltranskript, nicht Teil der Buchfassung:
45,3 cm - 41,6 cm = 3,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `individuelle_balance` | Differenz VL − RüL | 3,7 | cm |

- **Abhängigkeiten:** VL und RüL.
- **Gültigkeitsbereich:** Balancemaße der Beispielkonstruktion.
- **Technische Randbedingung:** Die Operandenreihenfolge ist ausdrücklich VL minus RüL.
- **Offene Fragen oder Widersprüche:** Die Zahlenoperanden fehlen im extrahierten Kandidaten, sind aber im Originaltranskript unmittelbar davor als 45,3 cm und 41,6 cm belegt; die Differenz stimmt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** VL und RüL als Pflichtparameter verlangen; den Ergebniswert nicht als Konstante übernehmen.

## HOF-B1-S177-F12 — Unbestimmte Korrektur der Balancemaße

- **Fachlicher Zweck:** Korrigierte Vorder- und Rückenlänge sowie ihre Balance erfassen, obwohl die Korrekturwerte nicht eingetragen sind.
- **Quelle:** `formeln_s177.md`, Zeilen 56–58; Originaltranskript `s177.md`, Zeilen 63–65; Buchseite 177.
- **Originalbezeichnung:** `± --- = RüL / VL; korrigierte Balance`
- **Normalisierte Bezeichnung:** `korrigierte_balancemasse_unbestimmt`

### Buchfassung

```text
| ± --- | = | RüL | 41,6 |
| ± --- | = | VL | 45,3 |
| | | korrigierte Balance = | 3,7 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `rueckenlaenge_gemessen` | gemessene RüL | im Kandidaten nicht enthalten | cm |
| `vorderlaenge_gemessen` | gemessene VL | im Kandidaten nicht enthalten | cm |
| `rueckenlaenge_korrektur` | `± ---` | unbekannt | cm |
| `vorderlaenge_korrektur` | `± ---` | unbekannt | cm |

### Formel und Rechenschritte

```text
rueckenlaenge_korrigiert = rueckenlaenge_gemessen + rueckenlaenge_korrektur
                          = 41,6 cm laut Ausgabefeld
vorderlaenge_korrigiert = vorderlaenge_gemessen + vorderlaenge_korrektur
                         = 45,3 cm laut Ausgabefeld
korrigierte_balance = vorderlaenge_korrigiert - rueckenlaenge_korrigiert
                     = 45,3 cm - 41,6 cm
                     = 3,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `rueckenlaenge_korrigiert` | RüL für die Konstruktion | 41,6 | cm |
| `vorderlaenge_korrigiert` | VL für die Konstruktion | 45,3 | cm |
| `korrigierte_balance` | Differenz der korrigierten Maße | 3,7 | cm |

- **Abhängigkeiten:** Gemessene VL/RüL und zwei figurabhängige Korrekturwerte.
- **Gültigkeitsbereich:** Korrekturblock der Beispielkonstruktion.
- **Technische Randbedingung:** Die Platzhalter `± ---` dürfen nicht als belegte Nullwerte interpretiert werden.
- **Offene Fragen oder Widersprüche:** Die Ausgaben und ihre Differenz sind vorhanden, aber beide Korrekturwerte und die zugehörigen Eingabewerte fehlen im extrahierten Kandidaten. Der Rechenweg zu den Ausgaben ist daher nicht ausführbar.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Blockieren, bis gemessene Ausgangsmaße und signierte Korrekturwerte als Eingaben vorliegen.

## HOF-B1-S177-F13 — Taillenausfall

- **Fachlicher Zweck:** Den Taillenausfall als Differenz zwischen gemessener Taillenbreite und halber Taillenweite bestimmen.
- **Quelle:** `formeln_s177.md`, Zeile 63; Originaltranskript `s177.md`, Zeile 77; Buchseite 177.
- **Originalbezeichnung:** `gemessene TaB − ½ TaW`
- **Normalisierte Bezeichnung:** `taillenausfall_oberteil`

### Buchfassung

```text
| TaAf | Taillenausfall | gemessene TaB − ½ TaW = [leer] |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenbreite_gemessen` | gemessene TaB | variabel | cm |
| `halbe_taillenweite` | ½ TaW | variabel | cm |

### Formel und Rechenschritte

```text
taillenausfall = taillenbreite_gemessen - halbe_taillenweite
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `taillenausfall` | TaAf | cm |

- **Abhängigkeiten:** Gemessene TaB und ½ TaW.
- **Gültigkeitsbereich:** Unterer Teil der Oberteil-Konstruktionstabelle.
- **Technische Randbedingung:** Beide Breiten müssen dieselbe halbe Schnittseite betreffen.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel eingetragen; die allgemeine Formel ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Positives und negatives Ergebnis fachlich getrennt validieren.

## HOF-B1-S177-F14 — Hüftfehlbetrag

- **Fachlicher Zweck:** Den Hüftfehlbetrag als Differenz zwischen gemessener Hüftbreite und halber Hüftweite bestimmen.
- **Quelle:** `formeln_s177.md`, Zeile 64; Originaltranskript `s177.md`, Zeile 78; Buchseite 177.
- **Originalbezeichnung:** `gemessene HüB − ½ HüW`
- **Normalisierte Bezeichnung:** `hueftfehlbetrag_oberteil`

### Buchfassung

```text
| HüFb | Hüftfehlbetrag | gemessene HüB − ½ HüW = [leer] |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftbreite_gemessen` | gemessene HüB | variabel | cm |
| `halbe_hueftweite` | ½ HüW | variabel | cm |

### Formel und Rechenschritte

```text
hueftfehlbetrag = hueftbreite_gemessen - halbe_hueftweite
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftfehlbetrag` | HüFb | cm |

- **Abhängigkeiten:** Gemessene HüB und ½ HüW.
- **Gültigkeitsbereich:** Unterer Teil der Oberteil-Konstruktionstabelle.
- **Technische Randbedingung:** Beide Breiten müssen dieselbe halbe Schnittseite betreffen.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel eingetragen; die allgemeine Formel ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorzeichen als fachliche Richtung erhalten.

## HOF-B1-S177-F15 — Mehrweite im Armloch

- **Fachlicher Zweck:** Die Mehrweite im Armloch aus vorderem und hinterem Armlochumfang abzüglich Armrundungsumfang bestimmen.
- **Quelle:** `formeln_s177.md`, Zeile 65; Originaltranskript `s177.md`, Zeile 79; Buchseite 177.
- **Originalbezeichnung:** `vAlU + hAlU − AraU`
- **Normalisierte Bezeichnung:** `mehrweite_im_armloch`

### Buchfassung

```text
| (Mehrweite im Armloch) | | vAlU + hAlU − AraU = [leer] |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderer_armlochumfang` | vAlU | variabel | cm |
| `hinterer_armlochumfang` | hAlU | variabel | cm |
| `armrundungsumfang` | AraU | variabel | cm |

### Formel und Rechenschritte

```text
mehrweite_im_armloch = vorderer_armlochumfang + hinterer_armlochumfang - armrundungsumfang
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `mehrweite_im_armloch` | Differenz zwischen gesamtem Armloch- und Armrundungsumfang | cm |

- **Abhängigkeiten:** vAlU, hAlU und AraU.
- **Gültigkeitsbereich:** Kontrollmaß im unteren Teil der Oberteil-Konstruktionstabelle.
- **Technische Randbedingung:** Alle Umfänge müssen entlang der fachlich vorgesehenen Linien gemessen werden.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel eingetragen; die allgemeine Formel ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Messpfade und Einheiten vor der Subtraktion validieren.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s177.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Kopffelder mit Modell, Größe und PK; Kontextwerte, keine Rechenformel |
| Zeile 14 | 1 | Spaltengruppen der Konstruktionstabelle; Tabellenstruktur, keine Rechenformel |
| Zeile 19 | 1 | redaktionelle Beschreibung der Spaltenlogik; keine Buchrechnung |
| Zeile 46 | 1 | Schulterwinkel `20°` wird ohne numerische Änderung übernommen; die Auflockerung ist nicht beziffert, daher nur Eingabe-/Ausgabelabel |
| **Summe** | **4** | **3 Tabellen-/Metadatenzeilen und 1 unverändertes Winkelmaß ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s177.md` enthält weitere Körper- und Modellmaße, die nicht in den verbindlichen Formelbestand extrahiert wurden. Besonders die Zahlenoperanden VL `45,3 cm` und RüL `41,6 cm` stehen nur im Originalkontext vor der extrahierten Balanceformel. Sie wurden zur getrennt gekennzeichneten Kontextkontrolle verwendet, aber nicht als zusätzliche Buchfassung erfunden. Die Toleranzaussage in Zeile 67 und die leeren Maßfelder des unteren Tabellenteils wurden ebenfalls nicht über den Extrakt hinaus ergänzt.
