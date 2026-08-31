# Fachlich normalisierte Formeln — S. 186

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s186.md`
Originaltranskript: `../Band_1_geprüft_v1/s186.md`
Buchseite: Hofenbitzer, Band 1, S. 186

## HOF-B1-S186-F01 — Brustumfang zum Brustweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Brustumfang und Zugabe addieren und das Ergebnis halbieren.
- **Quelle:** `formeln_s186.md`, Zeile 14; Originaltranskript `s186.md`, Zeile 18; Buchseite 186.
- **Originalbezeichnung:** `BrU + 6 = BrW; ½ BrW`
- **Normalisierte Bezeichnung:** `brustweite_oberteil_pk3_s186`

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
brustweite = 88 cm + 6 cm = 94 cm
halbe_brustweite = 94 cm / 2 = 47 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `brustweite` | BrW | 94 | cm |
| `halbe_brustweite` | ½ BrW | 47 | cm |

- **Abhängigkeiten:** BrU und PK-3-Zugabe.
- **Gültigkeitsbereich:** Konstruktionstabelle S. 186, Größe 38, PK 3.
- **Technische Randbedingung:** Erst addieren, dann halbieren.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ganz- und Halbmaß getrennt speichern.

## HOF-B1-S186-F02 — Taillenumfang zum Taillenweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Taillenumfang und Zugabe addieren und das Ergebnis halbieren.
- **Quelle:** `formeln_s186.md`, Zeile 15; Originaltranskript `s186.md`, Zeile 19; Buchseite 186.
- **Originalbezeichnung:** `TaU + 4 = TaW; ½ TaW`
- **Normalisierte Bezeichnung:** `taillenweite_oberteil_s186`

### Buchfassung

```text
| TaU | Taillenumfang | 72 | + 4 | TaW = 76 | ½ = 38 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |
| `taillenumfang_zugabe` | Zugabe | 4 | cm |

### Formel und Rechenschritte

```text
taillenweite = 72 cm + 4 cm = 76 cm
halbe_taillenweite = 76 cm / 2 = 38 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `taillenweite` | TaW | 76 | cm |
| `halbe_taillenweite` | ½ TaW | 38 | cm |

- **Abhängigkeiten:** TaU und PK-3-Zugabe.
- **Gültigkeitsbereich:** Grundschnitt ohne Hüftausfall, Größe 38.
- **Technische Randbedingung:** Dieser TaU unterscheidet sich vom individuellen TaU auf S. 178.
- **Offene Fragen oder Widersprüche:** Keine in dieser Tabellenzeile.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Eingabedatensatz der Seite eindeutig mitführen.

## HOF-B1-S186-F03 — Hüftumfang zum Hüftweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Hüftumfang und Zugabe addieren und das Ergebnis halbieren.
- **Quelle:** `formeln_s186.md`, Zeile 16; Originaltranskript `s186.md`, Zeile 20; Buchseite 186.
- **Originalbezeichnung:** `HüU + 4 = HüW; ½ HüW`
- **Normalisierte Bezeichnung:** `hueftweite_oberteil_s186`

### Buchfassung

```text
| HüU | Hüftumfang | 97 | + 4 | HüW = 101 | ½ = 50,5 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `hueftumfang_zugabe` | Zugabe | 4 | cm |

### Formel und Rechenschritte

```text
hueftweite = 97 cm + 4 cm = 101 cm
halbe_hueftweite = 101 cm / 2 = 50,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hueftweite` | HüW | 101 | cm |
| `halbe_hueftweite` | ½ HüW | 50,5 | cm |

- **Abhängigkeiten:** HüU und PK-3-Zugabe.
- **Gültigkeitsbereich:** Konstruktionstabelle S. 186.
- **Technische Randbedingung:** Ganzumfang vor Halbierung bilden.
- **Offene Fragen oder Widersprüche:** Keine in dieser Tabellenzeile.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Halbmaß aus dem Modellmaß ableiten.

## HOF-B1-S186-F04 — Armlochtiefe mit Zugabe

- **Fachlicher Zweck:** Die AIT-Zugabe zur Armlochtiefe addieren.
- **Quelle:** `formeln_s186.md`, Zeile 17; Originaltranskript `s186.md`, Zeile 21; Buchseite 186.
- **Originalbezeichnung:** `AIT + 1,3 = AIT+`
- **Normalisierte Bezeichnung:** `armlochtiefe_mit_zugabe_s186`

### Buchfassung

```text
| AIT | Armlochtiefe | 20,1 | + 1,3 | AIT+ = 21,4 | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefe` | AIT | 20,1 | cm |
| `armlochtiefe_zugabe` | Zugabe | 1,3 | cm |

### Formel und Rechenschritte

```text
armlochtiefe_mit_zugabe = 20,1 cm + 1,3 cm = 21,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefe_mit_zugabe` | AIT+ | 21,4 | cm |

- **Abhängigkeiten:** AIT und PK-3-Zugabe.
- **Gültigkeitsbereich:** Konstruktionstabelle S. 186.
- **Technische Randbedingung:** Die Zugabe wird einmal addiert.
- **Offene Fragen oder Widersprüche:** Keine; diese Zeile druckt den rechnerisch richtigen Wert, anders als S. 178.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Seitenabhängige Druckwerte nicht vermischen.

## HOF-B1-S186-F05 — Rückenbreite mit Zugabe

- **Fachlicher Zweck:** Die Zugabe zur halben Rückenbreite addieren.
- **Quelle:** `formeln_s186.md`, Zeile 22; Originaltranskript `s186.md`, Zeile 26; Buchseite 186.
- **Originalbezeichnung:** `RüB + 0,5 = RüB+`
- **Normalisierte Bezeichnung:** `rueckenbreite_mit_zugabe_s186`

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
rueckenbreite_mit_zugabe = 16,5 cm + 0,5 cm = 17 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `rueckenbreite_mit_zugabe` | RüB+ | 17 | cm |

- **Abhängigkeiten:** RüB und Zugabe.
- **Gültigkeitsbereich:** Halbe Rückenbreite S. 186.
- **Technische Randbedingung:** RüB ist bereits ein Halbmaß.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Halbmaßkennzeichnung erhalten.

## HOF-B1-S186-F06 — Armdurchmesser mit Zugabe und Teilungen

- **Fachlicher Zweck:** ArD vergrößern und ArD+ vierteln beziehungsweise dritteln.
- **Quelle:** `formeln_s186.md`, Zeile 23; Originaltranskript `s186.md`, Zeile 27; Buchseite 186.
- **Originalbezeichnung:** `ArD + 1,5 = ArD+; ¼; ⅓`
- **Normalisierte Bezeichnung:** `armdurchmesser_mit_zugabe_und_teilungen_s186`

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

- **Abhängigkeiten:** ArD und Zugabe.
- **Gültigkeitsbereich:** Konstruktionstabelle S. 186.
- **Technische Randbedingung:** Beide Teilwerte aus ArD+ bilden.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** ArD+ nur einmal berechnen.

## HOF-B1-S186-F07 — Brustbreite mit Zugabe

- **Fachlicher Zweck:** Die Zugabe zur halben Brustbreite addieren.
- **Quelle:** `formeln_s186.md`, Zeile 24; Originaltranskript `s186.md`, Zeile 28; Buchseite 186.
- **Originalbezeichnung:** `BrB + 1 = BrB+`
- **Normalisierte Bezeichnung:** `brustbreite_mit_zugabe_s186`

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
brustbreite_mit_zugabe = 18,2 cm + 1 cm = 19,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `brustbreite_mit_zugabe` | BrB+ | 19,2 | cm |

- **Abhängigkeiten:** BrB und Zugabe.
- **Gültigkeitsbereich:** Halbe Brustbreite S. 186.
- **Technische Randbedingung:** BrB ist bereits ein Halbmaß.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Halbmaßkennzeichnung erhalten.

## HOF-B1-S186-F08 — Kontrolle der halben Brustweite

- **Fachlicher Zweck:** Körperbreiten und Zugaben gegen ½ BrW kontrollieren.
- **Quelle:** `formeln_s186.md`, Zeile 25; Originaltranskript `s186.md`, Zeile 29; Buchseite 186.
- **Originalbezeichnung:** `44 + 3 = ½ BrW = 47`
- **Normalisierte Bezeichnung:** `kontrolle_halbe_brustweite_s186`

### Buchfassung

```text
| Kontrolle: Σ = ½ BrU | | 44 | + 3 | ½ BrW = 47 | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halber_brustumfang` | ½ BrU | 44 | cm |
| `breitenzugaben_summe` | RüB-, ArD- und BrB-Zugaben | 3 | cm |

### Formel und Rechenschritte

```text
halber_brustumfang = 16,5 cm + 9,3 cm + 18,2 cm = 44 cm
breitenzugaben_summe = 0,5 cm + 1,5 cm + 1 cm = 3 cm
halbe_brustweite = 44 cm + 3 cm = 47 cm
Kontrolle: 94 cm / 2 = 47 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `halbe_brustweite_kontrolliert` | ½ BrW | 47 | cm |

- **Abhängigkeiten:** `HOF-B1-S186-F01`, `F05`, `F06` und `F07`.
- **Gültigkeitsbereich:** Breitenkontrolle S. 186.
- **Technische Randbedingung:** Beide unabhängigen Wege müssen übereinstimmen.
- **Offene Fragen oder Widersprüche:** Keine; im Gegensatz zu S. 178 stimmen die Werte.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Invariante prüfen.

## HOF-B1-S186-F09 — Inline-Taillenausfall mit widersprüchlicher Zahlenbasis

- **Fachlicher Zweck:** Den TaAf aus gemessener TaB und halber TaW bestimmen.
- **Quelle:** `formeln_s186.md`, Zeile 35; Originaltranskript `s186.md`, Zeilen 43–46 und 71; Buchseite 186.
- **Originalbezeichnung:** `TaAf = 46,2 − 38,5 = 7,7`
- **Normalisierte Bezeichnung:** `taillenausfall_s186_inline`

### Buchfassung

```text
> **Taillenausfall (TaAf) = TaB − ½ TaW = 46,2 cm − 38,5 cm = 7,7 cm**
```

### Eingaben

| Technische Variable | Buchbegriff | Inline-Wert | Einheit |
|---|---|---:|---|
| `taillenbreite_gemessen` | TaB | 46,2 | cm |
| `halbe_taillenweite` | ½ TaW | 38,5 | cm |

### Formel und Rechenschritte

```text
taillenausfall_inline = 46,2 cm - 38,5 cm = 7,7 cm
Konstruktionstabelle: 76 cm / 2 = 38 cm
untere Berechnungstabelle: 46 cm - 38 cm = 8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Inline-Wert | Tabellenwert | Einheit |
|---|---|---:|---:|---|
| `taillenausfall` | TaAf | 7,7 | 8 | cm |

- **Abhängigkeiten:** Gemessene TaB und ½ TaW.
- **Gültigkeitsbereich:** Einfache Taillierung auf S. 186.
- **Technische Randbedingung:** Inline- und Tabellenpfad getrennt erhalten.
- **Offene Fragen oder Widersprüche:** Die Inline-Rechnung stimmt für ihre Werte, widerspricht aber Konstruktionstabelle und unterer Berechnungstabelle.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis die gültige Zahlenbasis geklärt ist.

## HOF-B1-S186-F10 — Verteilung des gedruckten Taillenausfalls

- **Fachlicher Zweck:** Den gedruckten Ausfallbetrag 7,7 cm auf Seitennähte und Abnäher verteilen.
- **Quelle:** `formeln_s186.md`, Zeilen 40–44; Originaltranskript `s186.md`, Zeilen 51–55; Buchseite 186.
- **Originalbezeichnung:** `2 + 2 + 0 + 3,7 = 7,7 cm`
- **Normalisierte Bezeichnung:** `verteilung_taillenausfall_s186`

### Buchfassung

```text
> • SN  2 × 1 cm = 2 cm
> • vAbl = 2 cm
> • optional shAbl  hier = 0 cm
> • hAbl = 3,7 cm
> • Summe des Ausfalls = 7,7 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `ausfall_seitennaehte` | SN | 2 | cm |
| `vorderer_abnaeherinhalt` | vAbl | 2 | cm |
| `seitlicher_hinterer_abnaeherinhalt` | shAbl | 0 | cm |
| `hinterer_abnaeherinhalt` | hAbl | 3,7 | cm |

### Formel und Rechenschritte

```text
summe_ausfall = 2 cm + 2 cm + 0 cm + 3,7 cm = 7,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `summe_ausfall` | verteilte Gesamtsumme | 7,7 | cm |

- **Abhängigkeiten:** Vier gedruckte Verteilungsanteile; Zielwert aus `HOF-B1-S186-F09`.
- **Gültigkeitsbereich:** Gedrucktes Verteilungsbeispiel S. 186.
- **Technische Randbedingung:** Jeder Anteil wird einmal summiert.
- **Offene Fragen oder Widersprüche:** Die Verteilung ist intern korrekt, hängt aber vom gesperrten Inline-TaAf 7,7 cm ab.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Verteilung erst nach Wahl eines gültigen TaAf-Datensatzes verwenden.

## HOF-B1-S186-F11 — Gemeinsame Hüftbreite

- **Fachlicher Zweck:** vHüB und hHüB zur HüB addieren.
- **Quelle:** `formeln_s186.md`, Zeile 49; Originaltranskript `s186.md`, Zeile 59; Buchseite 186.
- **Originalbezeichnung:** `vHüB + hHüB = HüB`
- **Normalisierte Bezeichnung:** `gemeinsame_hueftbreite_s186`

### Buchfassung

```text
> ㊵ vHüB und hHüB messen und addieren = Hüftbreite (HüB).
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vordere_hueftbreite` | vHüB | variabel | cm |
| `hintere_hueftbreite` | hHüB | variabel | cm |

### Formel und Rechenschritte

```text
gemeinsame_hueftbreite = vordere_hueftbreite + hintere_hueftbreite
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `gemeinsame_hueftbreite` | HüB | cm |

- **Abhängigkeiten:** Gemessene vHüB und hHüB.
- **Gültigkeitsbereich:** Hüftkontrolle S. 186.
- **Technische Randbedingung:** Beide Teilbreiten auf derselben Hüftlinie messen.
- **Offene Fragen oder Widersprüche:** Keine in der allgemeinen Beziehung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Messpfade dokumentieren.

## HOF-B1-S186-F12 — Inline-Hüftfehlbetrag mit widersprüchlicher Zahlenbasis

- **Fachlicher Zweck:** Hüftdifferenz, positiven Fehlbetrag und halbe Ausstellung bestimmen.
- **Quelle:** `formeln_s186.md`, Zeile 54; Originaltranskript `s186.md`, Zeilen 62–64 und 72; Buchseite 186.
- **Originalbezeichnung:** `46,5 − 51 = −4,5 → 4,5; ½ = 2,2`
- **Normalisierte Bezeichnung:** `hueftfehlbetrag_s186_inline`

### Buchfassung

```text
> **Hüft-Fehlbetrag (HüFb) = HüB − ½ HüW = 46,5 cm − 51 cm = −4,5 cm → 4,5 cm ; ½ = 2,2 cm**
```

### Eingaben

| Technische Variable | Buchbegriff | Inline-Wert | Einheit |
|---|---|---:|---|
| `gemeinsame_hueftbreite` | HüB | 46,5 | cm |
| `halbe_hueftweite` | ½ HüW | 51 | cm |

### Formel und Rechenschritte

```text
signierte_hueftdifferenz_inline = 46,5 cm - 51 cm = -4,5 cm
hueftfehlbetrag_inline = 4,5 cm
exakter_halbwert = 4,5 cm / 2 = 2,25 cm
gedruckter_halbwert = 2,2 cm
Konstruktionstabelle: 101 cm / 2 = 50,5 cm
untere Berechnungstabelle: 46,5 cm - 50,5 cm = -4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Inline-Wert | Tabellenwert | Einheit |
|---|---|---:|---:|---|
| `signierte_hueftdifferenz` | HüB − ½ HüW | −4,5 | −4 | cm |
| `hueftfehlbetrag` | positiver Betrag | 4,5 | 4 | cm |
| `ausstellung_je_seitenlinie` | halber Betrag | 2,2 gedruckt | 2 | cm |

- **Abhängigkeiten:** HüB und ½ HüW.
- **Gültigkeitsbereich:** Hüftausstellung S. 186.
- **Technische Randbedingung:** Exakten Halbwert und gedruckten Wert getrennt erhalten.
- **Offene Fragen oder Widersprüche:** Inline- und Tabellenwerte widersprechen sich; für `2,25 → 2,2` ist keine Rundungsregel belegt.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis Zahlenbasis und Rundung geklärt sind.

## HOF-B1-S186-F13 — Taillenausfall der unteren Berechnungstabelle

- **Fachlicher Zweck:** Den TaAf mit den Werten der unteren Tabelle berechnen.
- **Quelle:** `formeln_s186.md`, Zeile 64; Originaltranskript `s186.md`, Zeile 71; Buchseite 186.
- **Originalbezeichnung:** `TaB 46 − ½ TaW 38 = 8`
- **Normalisierte Bezeichnung:** `taillenausfall_s186_berechnungstabelle`

### Buchfassung

```text
| TaAf | Taillenausfall | TaB 46 | − ½ TaW | 38 | = | 8 |
```

### Eingaben

| Technische Variable | Buchbegriff | Tabellenwert | Einheit |
|---|---|---:|---|
| `taillenbreite_gemessen` | TaB | 46 | cm |
| `halbe_taillenweite` | ½ TaW | 38 | cm |

### Formel und Rechenschritte

```text
taillenausfall_tabelle = 46 cm - 38 cm = 8 cm
Inline-Pfad: 46,2 cm - 38,5 cm = 7,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Tabellenwert | Inline-Wert | Einheit |
|---|---|---:|---:|---|
| `taillenausfall` | TaAf | 8 | 7,7 | cm |

- **Abhängigkeiten:** Tabellenwerte TaB und ½ TaW.
- **Gültigkeitsbereich:** Untere Berechnungstabelle S. 186.
- **Technische Randbedingung:** Tabellen- und Inline-Datensatz nicht mischen.
- **Offene Fragen oder Widersprüche:** Rechnung intern korrekt, aber im Widerspruch zu `HOF-B1-S186-F09` und zur gedruckten Verteilung 7,7 cm.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Gültigen Datensatz fachlich auswählen lassen.

## HOF-B1-S186-F14 — Hüftfehlbetrag der unteren Berechnungstabelle

- **Fachlicher Zweck:** Die signierte Hüftdifferenz mit den Werten der unteren Tabelle berechnen.
- **Quelle:** `formeln_s186.md`, Zeile 65; Originaltranskript `s186.md`, Zeile 72; Buchseite 186.
- **Originalbezeichnung:** `HüB 46,5 − ½ HüW 50,5 = −4`
- **Normalisierte Bezeichnung:** `hueftfehlbetrag_s186_berechnungstabelle`

### Buchfassung

```text
| HüFb | Hüftfehlbetrag | HüB 46,5 | − ½ HüW | 50,5 | = | −4 |
```

### Eingaben

| Technische Variable | Buchbegriff | Tabellenwert | Einheit |
|---|---|---:|---|
| `gemeinsame_hueftbreite` | HüB | 46,5 | cm |
| `halbe_hueftweite` | ½ HüW | 50,5 | cm |

### Formel und Rechenschritte

```text
signierte_hueftdifferenz_tabelle = 46,5 cm - 50,5 cm = -4 cm
hueftfehlbetrag_tabelle = abs(-4 cm) = 4 cm
halbwert_tabelle = 4 cm / 2 = 2 cm
Inline-Pfad: 46,5 cm - 51 cm = -4,5 cm; gedruckter Halbwert 2,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Tabellenwert | Inline-Wert | Einheit |
|---|---|---:|---:|---|
| `signierte_hueftdifferenz` | HüB − ½ HüW | −4 | −4,5 | cm |
| `hueftfehlbetrag` | positiver Betrag | 4 | 4,5 | cm |
| `ausstellung_je_seitenlinie` | halber Betrag | 2 | 2,2 gedruckt | cm |

- **Abhängigkeiten:** Tabellenwerte HüB und ½ HüW.
- **Gültigkeitsbereich:** Untere Berechnungstabelle S. 186.
- **Technische Randbedingung:** Tabellen- und Inline-Datensatz nicht mischen.
- **Offene Fragen oder Widersprüche:** Rechnung intern korrekt, widerspricht aber Inline-Formel und gedruckter Ausstellung 2,2 cm.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Gültigen Hüftdatensatz vor jeder Konstruktion auswählen lassen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s186.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Modell-, Größen- und PK-Metadaten; keine Rechenformel |
| Zeile 30 | 1 | redaktioneller Seitenvergleich; keine zusätzliche Buchformel |
| Zeile 59 | 1 | Tabellenkopf; Lesekontext, keine Rechenformel |
| Zeile 70 | 1 | redaktionelle Prüfnotiz zu den in `F09`, `F12`, `F13` und `F14` dargestellten Widersprüchen |
| **Summe** | **4** | **2 Metadaten-/Kopfzeilen und 2 redaktionelle Prüfzeilen ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s186.md` enthält weitere Verteilungsbereiche und geometrische Konstruktionsanweisungen, die nicht im verbindlichen Extrakt stehen. Sie wurden nicht als Buchfassungen ergänzt. Die Inline-Rechnungen, die Konstruktionstabelle und die untere Berechnungstabelle bleiben als getrennte, widersprüchliche Pfade sichtbar; keine Zahlenreihe wurde stillschweigend zur gültigen erklärt.
