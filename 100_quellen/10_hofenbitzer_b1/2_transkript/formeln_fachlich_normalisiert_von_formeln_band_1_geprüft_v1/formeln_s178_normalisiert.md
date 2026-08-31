# Fachlich normalisierte Formeln — S. 178

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/06_grundschnitte_oberteile_s171-196/formeln_s178.md`
Originaltranskript: `../Band_1_geprüft_v1/s178.md`
Buchseite: Hofenbitzer, Band 1, S. 178

## HOF-B1-S178-F01 — Brustumfang zum Brustweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Brustumfang und Zugabe addieren und das Modellmaß halbieren.
- **Quelle:** `formeln_s178.md`, Zeile 14; Originaltranskript `s178.md`, Zeile 37; Buchseite 178.
- **Originalbezeichnung:** `BrU + 6 = BrW; ½ BrW`
- **Normalisierte Bezeichnung:** `brustweite_oberteil_pk3`

### Buchfassung

```text
| BrU | Brustumfang | 88 | + 6 | BrW = 94 | ½ = 47 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustumfang` | BrU | 88 | cm |
| `brustumfang_zugabe` | Zugabe | 6 | cm |

### Formel und Rechenschritte

```text
brustweite = brustumfang + brustumfang_zugabe
            = 88 cm + 6 cm
            = 94 cm
halbe_brustweite = brustweite / 2
                  = 94 cm / 2
                  = 47 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `brustweite` | BrW | 94 | cm |
| `halbe_brustweite` | ½ BrW | 47 | cm |

- **Abhängigkeiten:** BrU und PK-3-Zugabensatz aus `HOF-B1-S176-F02`.
- **Gültigkeitsbereich:** Konstruktionstabelle des taillierten Oberteil-Grundschnitts, Größe 38, PK 3.
- **Technische Randbedingung:** Erst die Ganzumfangszugabe addieren, danach halbieren.
- **Offene Fragen oder Widersprüche:** Keine; beide Druckwerte stimmen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ganzes und halbes Modellmaß getrennt speichern.

## HOF-B1-S178-F02 — Taillenumfang zum Taillenweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Taillenumfang und gewählte Zugabe addieren und das Ergebnis halbieren.
- **Quelle:** `formeln_s178.md`, Zeile 15; Originaltranskript `s178.md`, Zeile 38; Buchseite 178.
- **Originalbezeichnung:** `TaU + 4 = TaW; ½ TaW`
- **Normalisierte Bezeichnung:** `taillenweite_oberteil_pk3`

### Buchfassung

```text
| TaU | Taillenumfang | 68 | + 4 | TaW = 72 | ½ = 36 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 68 | cm |
| `taillenumfang_zugabe` | gewählte PK-3-Zugabe | 4 | cm |

### Formel und Rechenschritte

```text
taillenweite = taillenumfang + taillenumfang_zugabe
              = 68 cm + 4 cm
              = 72 cm
halbe_taillenweite = taillenweite / 2
                    = 72 cm / 2
                    = 36 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `taillenweite` | TaW | 72 | cm |
| `halbe_taillenweite` | ½ TaW | 36 | cm |

- **Abhängigkeiten:** TaU und gewählter Wert aus dem PK-3-Bereich `4 bis 6 cm` auf S. 176.
- **Gültigkeitsbereich:** Taillierter Oberteil-Grundschnitt, Größe 38, PK 3.
- **Technische Randbedingung:** Das Buch belegt keine allgemeine Auswahlregel innerhalb des Bereichs.
- **Offene Fragen oder Widersprüche:** Keine in der Rechnung; der Auswahlgrund für 4 cm bleibt offen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zugabebereich und gewählten Wert getrennt führen.

## HOF-B1-S178-F03 — Hüftumfang zum Hüftweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Hüftumfang und gewählte Zugabe addieren und das Ergebnis halbieren.
- **Quelle:** `formeln_s178.md`, Zeile 16; Originaltranskript `s178.md`, Zeile 39; Buchseite 178.
- **Originalbezeichnung:** `HüU + 4 = HüW; ½ HüW`
- **Normalisierte Bezeichnung:** `hueftweite_oberteil_pk3`

### Buchfassung

```text
| HüU | Hüftumfang | 97 | + 4 | HüW = 101 | ½ = 50,5 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `hueftumfang_zugabe` | gewählte PK-3-Zugabe | 4 | cm |

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
| `hueftweite` | HüW | 101 | cm |
| `halbe_hueftweite` | ½ HüW | 50,5 | cm |

- **Abhängigkeiten:** HüU und gewählter Wert aus dem PK-3-Bereich `4 bis 6 cm` auf S. 176.
- **Gültigkeitsbereich:** Taillierter Oberteil-Grundschnitt, Größe 38, PK 3.
- **Technische Randbedingung:** Das Buch belegt keine allgemeine Auswahlregel innerhalb des Bereichs.
- **Offene Fragen oder Widersprüche:** Keine in der Rechnung; der Auswahlgrund für 4 cm bleibt offen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereichsauswahl als explizite Eingabe verlangen.

## HOF-B1-S178-F04 — Armlochtiefe mit widersprüchlichem Druckergebnis

- **Fachlicher Zweck:** Die PK-3-Zugabe zur gemessenen Armlochtiefe addieren.
- **Quelle:** `formeln_s178.md`, Zeile 17; Originaltranskript `s178.md`, Zeile 40; Buchseite 178.
- **Originalbezeichnung:** `AIT + 1,3 = AIT+ = 21,8`
- **Normalisierte Bezeichnung:** `armlochtiefe_mit_zugabe_pk3`

### Buchfassung

```text
| AIT | Armlochtiefe | 20,1 | + 1,3 | AIT+ = 21,8 `[BUCHFEHLER?]` | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefe` | AIT | 20,1 | cm |
| `armlochtiefe_zugabe` | PK-3-Zugabe | 1,3 | cm |

### Formel und Rechenschritte

```text
allgemeine Formel:
armlochtiefe_mit_zugabe = armlochtiefe + armlochtiefe_zugabe

wörtlich eingesetzte Werte:
20,1 cm + 1,3 cm = 21,4 cm

gedrucktes Ergebnis:
AIT+ = 21,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Rechnerischer Wert | Druckwert | Einheit |
|---|---|---:|---:|---|
| `armlochtiefe_mit_zugabe` | AIT+ | 21,4 | 21,8 | cm |

- **Abhängigkeiten:** AIT und AIT-Zugabe der PK 3.
- **Gültigkeitsbereich:** Beispielkonstruktion auf S. 178.
- **Technische Randbedingung:** Formel, eingesetzte Werte und Druckergebnis müssen getrennt erhalten bleiben.
- **Offene Fragen oder Widersprüche:** `20,1 + 1,3 = 21,4`, nicht `21,8`; die Buchfassung widerspricht sich rechnerisch.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis der gültige AIT+-Wert fachlich entschieden ist.

## HOF-B1-S178-F05 — Rückenbreite mit Zugabe

- **Fachlicher Zweck:** Die Zugabe zur halben Rückenbreite addieren.
- **Quelle:** `formeln_s178.md`, Zeile 22; Originaltranskript `s178.md`, Zeile 45; Buchseite 178.
- **Originalbezeichnung:** `RüB + 0,5 = RüB+`
- **Normalisierte Bezeichnung:** `rueckenbreite_mit_zugabe_pk3`

### Buchfassung

```text
| RüB | Rückenbreite (½) | 16,5 | + 0,5 | RüB+ = 17 | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_rueckenbreite` | RüB | 16,5 | cm |
| `rueckenbreite_zugabe` | Zugabe | 0,5 | cm |

### Formel und Rechenschritte

```text
rueckenbreite_mit_zugabe = halbe_rueckenbreite + rueckenbreite_zugabe
                          = 16,5 cm + 0,5 cm
                          = 17 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `rueckenbreite_mit_zugabe` | RüB+ | 17 | cm |

- **Abhängigkeiten:** RüB und PK-3-Zugabe.
- **Gültigkeitsbereich:** Halbe Rückenbreite der Beispielkonstruktion.
- **Technische Randbedingung:** RüB ist bereits ein halbes Breitenmaß.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Halbmaßkennzeichnung erhalten.

## HOF-B1-S178-F06 — Armdurchmesser mit Zugabe und Teilungen

- **Fachlicher Zweck:** Den Armdurchmesser vergrößern und das Modellmaß vierteln beziehungsweise dritteln.
- **Quelle:** `formeln_s178.md`, Zeile 23; Originaltranskript `s178.md`, Zeile 46; Buchseite 178.
- **Originalbezeichnung:** `ArD + 1,5 = ArD+; ¼; ⅓`
- **Normalisierte Bezeichnung:** `armdurchmesser_mit_zugabe_und_teilungen_pk3`

### Buchfassung

```text
| ArD | Armdurchmesser | 9,3 | + 1,5 | ArD+ = 10,8 | ¼ = 2,7 ; ⅓ = 3,6 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser` | ArD | 9,3 | cm |
| `armdurchmesser_zugabe` | Zugabe | 1,5 | cm |

### Formel und Rechenschritte

```text
armdurchmesser_mit_zugabe = 9,3 cm + 1,5 cm = 10,8 cm
viertel_armdurchmesser = 10,8 cm / 4 = 2,7 cm
drittel_armdurchmesser = 10,8 cm / 3 = 3,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser_mit_zugabe` | ArD+ | 10,8 | cm |
| `viertel_armdurchmesser` | ¼ ArD+ | 2,7 | cm |
| `drittel_armdurchmesser` | ⅓ ArD+ | 3,6 | cm |

- **Abhängigkeiten:** ArD und PK-3-Zugabe.
- **Gültigkeitsbereich:** Beispielkonstruktion auf S. 178.
- **Technische Randbedingung:** Die Teilungen beziehen sich auf ArD+.
- **Offene Fragen oder Widersprüche:** Keine; alle Druckwerte stimmen exakt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** ArD+ einmal bilden und beide Teilwerte daraus ableiten.

## HOF-B1-S178-F07 — Brustbreite mit Zugabe

- **Fachlicher Zweck:** Die Zugabe zur halben Brustbreite addieren.
- **Quelle:** `formeln_s178.md`, Zeile 24; Originaltranskript `s178.md`, Zeile 47; Buchseite 178.
- **Originalbezeichnung:** `BrB + 1 = BrB+`
- **Normalisierte Bezeichnung:** `brustbreite_mit_zugabe_pk3`

### Buchfassung

```text
| BrB | Brustbreite (½) | 18,2 | + 1 | BrB+ = 19,2 | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_brustbreite` | BrB | 18,2 | cm |
| `brustbreite_zugabe` | Zugabe | 1 | cm |

### Formel und Rechenschritte

```text
brustbreite_mit_zugabe = halbe_brustbreite + brustbreite_zugabe
                        = 18,2 cm + 1 cm
                        = 19,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `brustbreite_mit_zugabe` | BrB+ | 19,2 | cm |

- **Abhängigkeiten:** BrB und PK-3-Zugabe.
- **Gültigkeitsbereich:** Halbe Brustbreite der Beispielkonstruktion.
- **Technische Randbedingung:** BrB ist bereits ein halbes Breitenmaß.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Halbmaßkennzeichnung erhalten.

## HOF-B1-S178-F08 — Widersprüchliche Kontrolle der halben Brustweite

- **Fachlicher Zweck:** Körperbreiten und Zugaben gegen die halbe Brustweite kontrollieren.
- **Quelle:** `formeln_s178.md`, Zeile 25; Originaltranskript `s178.md`, Zeile 48; Buchseite 178.
- **Originalbezeichnung:** `Kontrolle: Σ = ½ BrU; 44 + 3 = ½ BrW = 48`
- **Normalisierte Bezeichnung:** `kontrolle_halbe_brustweite_pk3`

### Buchfassung

```text
| Kontrolle: Σ = ½ BrU | | 44 | + 3 | ½ BrW = 48 `[BUCHFEHLER?]` | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halber_brustumfang` | ½ BrU / Summe RüB + ArD + BrB | 44 | cm |
| `brustbreiten_zugaben_summe` | Summe der drei Breitenzugaben | 3 | cm |

### Formel und Rechenschritte

```text
halber_brustumfang = 16,5 cm + 9,3 cm + 18,2 cm = 44 cm
brustbreiten_zugaben_summe = 0,5 cm + 1,5 cm + 1 cm = 3 cm
wörtlich eingesetzte Kontrolle = 44 cm + 3 cm = 47 cm
halbe_brustweite aus HOF-B1-S178-F01 = 94 cm / 2 = 47 cm
gedrucktes Kontrollergebnis = 48 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Rechnerischer Wert | Druckwert | Einheit |
|---|---|---:|---:|---|
| `halbe_brustweite_kontrolliert` | ½ BrW | 47 | 48 | cm |

- **Abhängigkeiten:** `HOF-B1-S178-F01`, `F05`, `F06` und `F07`.
- **Gültigkeitsbereich:** Breitenkontrolle der Beispielkonstruktion auf S. 178.
- **Technische Randbedingung:** Beide unabhängigen Rechenwege müssen denselben Wert liefern.
- **Offene Fragen oder Widersprüche:** Die Bestandteile und `94 / 2` ergeben 47 cm; gedruckt sind 48 cm.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Als Invariante prüfen; den Druckwert 48 cm nicht übernehmen.

## HOF-B1-S178-F09 — Schulternahtlänge aus Schulterbreite

- **Fachlicher Zweck:** Die Schulterbreitenzugabe zur Schulterbreite addieren.
- **Quelle:** `formeln_s178.md`, Zeile 26; Originaltranskript `s178.md`, Zeile 49; Buchseite 178.
- **Originalbezeichnung:** `SuB + 0,3 = SuNL`
- **Normalisierte Bezeichnung:** `schulternahtlaenge_pk3`

### Buchfassung

```text
| SuB | Schulterbreite | 12,2 | + 0,3 | SuNL = 12,5 | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `schulterbreite` | SuB | 12,2 | cm |
| `schulterbreite_zugabe` | Zugabe | 0,3 | cm |

### Formel und Rechenschritte

```text
schulternahtlaenge = 12,2 cm + 0,3 cm = 12,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `schulternahtlaenge` | SuNL | 12,5 | cm |

- **Abhängigkeiten:** SuB und PK-3-Zugabe.
- **Gültigkeitsbereich:** Schulter der Beispielkonstruktion.
- **Technische Randbedingung:** Die Ausgabe ist eine Nahtlänge, obwohl die Eingabe als Breite bezeichnet wird.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Original- und Zielbezeichnung getrennt führen.

## HOF-B1-S178-F10 — Hintere Schulternahtlänge mit Einhalteweite

- **Fachlicher Zweck:** Eine gewählte Einhalteweite zur Schulternahtlänge addieren.
- **Quelle:** `formeln_s178.md`, Zeile 27; Originaltranskript `s178.md`, Zeile 50; Buchseite 178.
- **Originalbezeichnung:** `SuNL + Einhalteweite; + 0,7 = hSuNL`
- **Normalisierte Bezeichnung:** `hintere_schulternahtlaenge_pk3`

### Buchfassung

```text
| hSuNL | hintere Schulternahtlänge | „SuNL + Einhalteweite 0,5 cm bis 1 cm" | + 0,7 | hSuNL = 13,2 | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `schulternahtlaenge` | SuNL | 12,5 | cm |
| `einhalteweite_schulter` | gewählte Einhalteweite aus 0,5 bis 1 | 0,7 | cm |

### Formel und Rechenschritte

```text
hintere_schulternahtlaenge = schulternahtlaenge + einhalteweite_schulter
                            = 12,5 cm + 0,7 cm
                            = 13,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hintere_schulternahtlaenge` | hSuNL | 13,2 | cm |

- **Abhängigkeiten:** SuNL aus `HOF-B1-S178-F09` und gewählte Einhalteweite.
- **Gültigkeitsbereich:** Hintere Schulter der Beispielkonstruktion.
- **Technische Randbedingung:** 0,7 cm ist ein gewählter Wert innerhalb des Bereichs 0,5 bis 1 cm.
- **Offene Fragen oder Widersprüche:** Die Auswahlregel für 0,7 cm ist nicht belegt; die Rechnung stimmt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einhalteweite als Parameter mit Bereichsprüfung führen.

## HOF-B1-S178-F11 — Korrekturblock der Balancemaße

- **Fachlicher Zweck:** Korrigierte Vorder- und Rückenlänge sowie ihre Balance erfassen.
- **Quelle:** `formeln_s178.md`, Zeilen 33–35; Originaltranskript `s178.md`, Zeilen 57–59; Buchseite 178.
- **Originalbezeichnung:** `RüL ± ---; VL ± ---; Differenz VL − RüL`
- **Normalisierte Bezeichnung:** `korrigierte_balancemasse_pk3_unbestimmt`

### Buchfassung

```text
| RüL | Rückenlänge (waagerechte Taille) | 41,6 | ± --- | RüL = 41,6 |
| VL | Vorderlänge (waagerechte Taille) | 45,3 | ± --- | VL = 45,3 |
| Differenz VL − RüL = individuelle Balance | | 3,7 | | korrigierte Balance = 3,7 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `rueckenlaenge_gemessen` | RüL | 41,6 | cm |
| `vorderlaenge_gemessen` | VL | 45,3 | cm |
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
| `rueckenlaenge_korrigiert` | RüL | 41,6 | cm |
| `vorderlaenge_korrigiert` | VL | 45,3 | cm |
| `korrigierte_balance` | Differenz VL − RüL | 3,7 | cm |

- **Abhängigkeiten:** Gemessene VL/RüL und zwei figurabhängige Korrekturwerte.
- **Gültigkeitsbereich:** Balanceblock der Beispielkonstruktion auf S. 178.
- **Technische Randbedingung:** Die Platzhalter `± ---` dürfen nicht als belegte Nullwerte interpretiert werden.
- **Offene Fragen oder Widersprüche:** Die Ergebnisfelder sind konsistent, aber die beiden Korrekturwerte fehlen; der vollständige Korrekturweg ist nicht ausführbar.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Gemessene Ausgangsmaße und signierte Korrekturwerte als Pflichtparameter verlangen.

## HOF-B1-S178-F12 — Taillenausfall

- **Fachlicher Zweck:** Den Taillenausfall als Differenz zwischen gemessener Taillenbreite und halber Taillenweite bestimmen.
- **Quelle:** `formeln_s178.md`, Zeile 40; Originaltranskript `s178.md`, Zeile 70; Buchseite 178.
- **Originalbezeichnung:** `gemessene TaB − ½ TaW`
- **Normalisierte Bezeichnung:** `taillenausfall_oberteil_pk3`

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
- **Hinweis für die spätere Python-Umsetzung:** Vorzeichen als fachliche Richtung erhalten.

## HOF-B1-S178-F13 — Hüftfehlbetrag

- **Fachlicher Zweck:** Den Hüftfehlbetrag als Differenz zwischen gemessener Hüftbreite und halber Hüftweite bestimmen.
- **Quelle:** `formeln_s178.md`, Zeile 41; Originaltranskript `s178.md`, Zeile 71; Buchseite 178.
- **Originalbezeichnung:** `gemessene HüB − ½ HüW`
- **Normalisierte Bezeichnung:** `hueftfehlbetrag_oberteil_pk3`

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

## HOF-B1-S178-F14 — Mehrweite im Armloch

- **Fachlicher Zweck:** Die Mehrweite aus vorderem und hinterem Armlochumfang abzüglich Armrundungsumfang bestimmen.
- **Quelle:** `formeln_s178.md`, Zeile 42; Originaltranskript `s178.md`, Zeile 72; Buchseite 178.
- **Originalbezeichnung:** `vAlU + hAlU − AraU`
- **Normalisierte Bezeichnung:** `mehrweite_im_armloch_pk3`

### Buchfassung

```text
| (Mehrweite im Armloch) | | vAlU + hAlU − AraU = [leer] — „Nur bei Oberteilen mit Brustabnäher" |
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
- **Gültigkeitsbereich:** Laut Buch nur Oberteile mit Brustabnäher.
- **Technische Randbedingung:** Alle Umfänge müssen entlang der fachlich vorgesehenen Linien gemessen werden.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel eingetragen; die allgemeine Formel ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Gültigkeitsbedingung und Messpfade validieren.

## HOF-B1-S178-F15 — Sollwert der Armlochmehrweite mit Toleranz

- **Fachlicher Zweck:** Den Sollwert der Armlochmehrweite aus der doppelten AIT-Zugabe bestimmen.
- **Quelle:** `formeln_s178.md`, Zeile 43; Originaltranskript `s178.md`, Zeile 73; Buchseite 178.
- **Originalbezeichnung:** `2 · Zugabe zur AIT; Toleranz +2 cm bis −1 cm`
- **Normalisierte Bezeichnung:** `sollwert_armlochmehrweite_pk3`

### Buchfassung

```text
| Sollwert der Mehrweite | | = 2 · Zugabe zur AIT (Toleranz +2 cm bis −1 cm) = [leer] |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Beispiel | Einheit |
|---|---|---:|---|
| `armlochtiefe_zugabe` | Zugabe zur AIT | 1,3 | cm |
| `toleranz_unterhalb` | `−1 cm` | 1 | cm |
| `toleranz_oberhalb` | `+2 cm` | 2 | cm |

### Formel und Rechenschritte

```text
sollwert_armlochmehrweite = 2 * armlochtiefe_zugabe
                           = 2 * 1,3 cm
                           = 2,6 cm
untere_toleranzgrenze = 2,6 cm - 1 cm = 1,6 cm
obere_toleranzgrenze = 2,6 cm + 2 cm = 4,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Beispiel | Einheit |
|---|---|---:|---|
| `sollwert_armlochmehrweite` | Sollwert | 2,6 | cm |
| `untere_toleranzgrenze` | kleinster Wert nach `−1 cm` | 1,6 | cm |
| `obere_toleranzgrenze` | größter Wert nach `+2 cm` | 4,6 | cm |

- **Abhängigkeiten:** AIT-Zugabe aus `HOF-B1-S178-F04`; Istwert aus `HOF-B1-S178-F14`.
- **Gültigkeitsbereich:** Kontrolle der Armlochmehrweite im unteren Tabellenteil.
- **Technische Randbedingung:** Die gedruckte Reihenfolge `+2 cm bis −1 cm` wird nach resultierendem Wert als obere beziehungsweise untere Grenze benannt.
- **Offene Fragen oder Widersprüche:** Kein Istwert eingetragen; Sollwert und Toleranzrelation sind dennoch eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Sollwert und asymmetrische Toleranzgrenzen getrennt speichern.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s178.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Kopffelder und Tabellenbeschreibung; Kontext, keine Rechenformel |
| Zeile 28 | 1 | Schulterwinkel `20°` wird ohne bezifferte Änderung übernommen; Eingabe-/Ausgabelabel |
| Zeile 48 | 1 | redaktionelle Prüfnotiz zu den bereits in `F04` und `F08` dargestellten Widersprüchen; keine zusätzliche Buchformel |
| **Summe** | **3** | **3 Metadaten-, Eingabe- oder Prüfzeilen ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s178.md` enthält zusätzlich die optimale Balance `3,5 cm`, den Hinweis auf eine Toleranz von ± 1 cm und die begründete Verwendung unkorrigierter VL/RüL. Diese Aussagen fehlen im verbindlichen Extrakt und wurden nicht als zusätzliche Buchfassung ergänzt. Sie lösen insbesondere die im extrahierten Korrekturblock fehlenden signierten Korrekturwerte nicht. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
