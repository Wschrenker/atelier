# Fachlich normalisierte Formeln — S. 537

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/14_anhang_sachwortverzeichnis_s535-544/formeln_s537.md`
Originaltranskript: `../hofenbitzer_band_1_digital/14_anhang_sachwortverzeichnis_s535-544/s537.md`
Buchseite: Hofenbitzer, Band 1, S. 537

## HOF-B1-S537-F01 — Brustumfang zum Brustweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Brustumfang und Zugabe zur Brustweite addieren und anschließend halbieren.
- **Quelle:** `formeln_s537.md`, Zeile 9; Originaltranskript `s537.md`, Zeile 18; Buchseite 537.
- **Originalbezeichnung:** `Körpermaße + Zugaben = BrW; anschließend ½`.
- **Normalisierte Bezeichnung:** `brustweite_oberteil_allgemein`

### Buchfassung

```text
| BrU | Brustumfang | Körpermaße + Zugaben = BrW; anschließend ½ |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustumfang` | BrU, Körpermaß | variabel | cm |
| `brustumfang_zugabe` | Zugabe zum Brustumfang | variabel | cm |

### Formel und Rechenschritte

```text
brustweite = brustumfang + brustumfang_zugabe
halbe_brustweite = brustweite / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `brustweite` | BrW des ganzen Schnitts | cm |
| `halbe_brustweite` | ½ BrW | cm |

- **Abhängigkeiten:** BrU und eine für den vorgesehenen Oberteil gewählte BrU-Zugabe.
- **Gültigkeitsbereich:** Allgemeines Konstruktionsformular für Oberteile auf S. 537.
- **Technische Randbedingung:** Die Zugabe wird zum ganzen Umfang addiert; erst das Ergebnis wird halbiert.
- **Offene Fragen oder Widersprüche:** Keine; die allgemeine Beziehung ist eindeutig. Die Auswahl der Zugabe ist nicht Teil dieser Formel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ganze und halbe Brustweite getrennt speichern; die Zugabe als explizite Eingabe verlangen.

## HOF-B1-S537-F02 — Taillenumfang zum Taillenweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Taillenumfang und Zugabe zur Taillenweite addieren und anschließend halbieren.
- **Quelle:** `formeln_s537.md`, Zeile 10; Originaltranskript `s537.md`, Zeile 19; Buchseite 537.
- **Originalbezeichnung:** `Körpermaße + Zugaben = TaW; anschließend ½`.
- **Normalisierte Bezeichnung:** `taillenweite_oberteil_allgemein`

### Buchfassung

```text
| TaU | Taillenumfang | Körpermaße + Zugaben = TaW; anschließend ½ |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU, Körpermaß | variabel | cm |
| `taillenumfang_zugabe` | Zugabe zum Taillenumfang | variabel | cm |

### Formel und Rechenschritte

```text
taillenweite = taillenumfang + taillenumfang_zugabe
halbe_taillenweite = taillenweite / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `taillenweite` | TaW des ganzen Schnitts | cm |
| `halbe_taillenweite` | ½ TaW | cm |

- **Abhängigkeiten:** TaU und eine für den vorgesehenen Oberteil gewählte TaU-Zugabe.
- **Gültigkeitsbereich:** Allgemeines Konstruktionsformular für Oberteile auf S. 537.
- **Technische Randbedingung:** Die Zugabe wird zum ganzen Umfang addiert; erst das Ergebnis wird halbiert.
- **Offene Fragen oder Widersprüche:** Keine; die Auswahl innerhalb eines Zugabenbereichs muss außerhalb dieser Formel erfolgen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zugabenbereich und gewählten Wert getrennt führen.

## HOF-B1-S537-F03 — Hüftumfang zum Hüftweiten-Konstruktionsmaß

- **Fachlicher Zweck:** Hüftumfang und Zugabe zur Hüftweite addieren und anschließend halbieren.
- **Quelle:** `formeln_s537.md`, Zeile 11; Originaltranskript `s537.md`, Zeile 20; Buchseite 537.
- **Originalbezeichnung:** `Körpermaße + Zugaben = HüW; anschließend ½`.
- **Normalisierte Bezeichnung:** `hueftweite_oberteil_allgemein`

### Buchfassung

```text
| HüU | Hüftumfang | Körpermaße + Zugaben = HüW; anschließend ½ |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU, Körpermaß | variabel | cm |
| `hueftumfang_zugabe` | Zugabe zum Hüftumfang | variabel | cm |

### Formel und Rechenschritte

```text
hueftweite = hueftumfang + hueftumfang_zugabe
halbe_hueftweite = hueftweite / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftweite` | HüW des ganzen Schnitts | cm |
| `halbe_hueftweite` | ½ HüW | cm |

- **Abhängigkeiten:** HüU und eine für den vorgesehenen Oberteil gewählte HüU-Zugabe.
- **Gültigkeitsbereich:** Allgemeines Konstruktionsformular für Oberteile auf S. 537.
- **Technische Randbedingung:** Die Zugabe wird zum ganzen Umfang addiert; erst das Ergebnis wird halbiert.
- **Offene Fragen oder Widersprüche:** Keine; die Auswahl der Zugabe ist eine vorgelagerte Entscheidung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereichsentscheidungen nicht aus einem einzelnen Tabellenwert ableiten.

## HOF-B1-S537-F04 — Armlochtiefe mit Zugabe

- **Fachlicher Zweck:** Die Armlochtiefenzugabe zum gemessenen Körpermaß addieren.
- **Quelle:** `formeln_s537.md`, Zeile 12; Originaltranskript `s537.md`, Zeile 21; Buchseite 537.
- **Originalbezeichnung:** `Körpermaße + Zugaben = AlT+`.
- **Normalisierte Bezeichnung:** `armlochtiefe_mit_zugabe_allgemein`

### Buchfassung

```text
| AlT | Armlochtiefe | Körpermaße + Zugaben = AlT+ |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefe` | AlT, Körpermaß | variabel | cm |
| `armlochtiefe_zugabe` | Zugabe zur AlT | variabel | cm |

### Formel und Rechenschritte

```text
armlochtiefe_mit_zugabe = armlochtiefe + armlochtiefe_zugabe
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `armlochtiefe_mit_zugabe` | AlT+ | cm |

- **Abhängigkeiten:** AlT und die gewählte Zugabe zur AlT.
- **Gültigkeitsbereich:** Allgemeines Konstruktionsformular für Oberteile auf S. 537.
- **Technische Randbedingung:** Körpermaß und Zugabe müssen als Längen in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Keine; die Auswahl der Zugabe ist nicht Teil der Additionsformel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Körpermaß und Zugabe als getrennte Felder erhalten.

## HOF-B1-S537-F05 — Kontrolle der halben Körperbreite

- **Fachlicher Zweck:** Die Summe aus Rückenbreite, Armdurchmesser und Brustbreite gegen den halben Brustumfang kontrollieren.
- **Quelle:** `formeln_s537.md`, Zeile 17; Originaltranskript `s537.md`, Zeile 34; Buchseite 537.
- **Originalbezeichnung:** `Kontrolle: Σ = ½ BrU`.
- **Normalisierte Bezeichnung:** `kontrolle_halber_brustumfang`

### Buchfassung

```text
| Kontrolle | `Σ = ½ BrU` |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `rueckenbreite_halb` | RüB | variabel | cm |
| `armdurchmesser` | ArD | variabel | cm |
| `brustbreite_halb` | BrB | variabel | cm |
| `brustumfang` | BrU | variabel | cm |

### Formel und Rechenschritte

```text
breitensumme = rueckenbreite_halb + armdurchmesser + brustbreite_halb
halber_brustumfang = brustumfang / 2
kontrolle_erfuellt = breitensumme == halber_brustumfang
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `breitensumme` | Σ der drei Proportionsmaße | cm |
| `halber_brustumfang` | ½ BrU | cm |
| `kontrolle_erfuellt` | Gleichheit der beiden Werte | boolesch |

- **Abhängigkeiten:** Die unmittelbar vor dem Kontrollfeld aufgeführten Proportionsmaße RüB, ArD und BrB sowie BrU.
- **Gültigkeitsbereich:** Proportionsmaß-Kontrolle des Oberteil-Konstruktionsformulars auf S. 537.
- **Technische Randbedingung:** RüB und BrB sind bereits Halbmaße; ArD wird einmal addiert.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel ist eingetragen; die symbolische Kontrolle ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Gleichheit als prüfbare Invariante ausführen und eine fachlich festgelegte numerische Toleranz separat definieren.

## HOF-B1-S537-F06 — Korrigierte Rücken- und Vorderlänge

- **Fachlicher Zweck:** Gemessene Rücken- und Vorderlänge mit ihren signierten Korrekturen in Konstruktionsmaße überführen.
- **Quelle:** `formeln_s537.md`, Zeilen 23–24; Originaltranskript `s537.md`, Zeilen 44–45; Buchseite 537.
- **Originalbezeichnung:** `Korrekturen ±; Konstruktionsmaß = RüL / VL`.
- **Normalisierte Bezeichnung:** `korrigierte_balance_laengen`

### Buchfassung

```text
| RüL | Rückenlänge (waagerechte Taille); Korrekturen `±`; Konstruktionsmaß `= RüL` |
| VL | Vorderlänge (waagerechte Taille); Korrekturen `±`; Konstruktionsmaß `= VL` |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `rueckenlaenge_gemessen` | gemessene RüL | variabel | cm |
| `rueckenlaenge_korrektur` | Korrektur `±` | variabel, signiert | cm |
| `vorderlaenge_gemessen` | gemessene VL | variabel | cm |
| `vorderlaenge_korrektur` | Korrektur `±` | variabel, signiert | cm |

### Formel und Rechenschritte

```text
rueckenlaenge_korrigiert = rueckenlaenge_gemessen + rueckenlaenge_korrektur
vorderlaenge_korrigiert = vorderlaenge_gemessen + vorderlaenge_korrektur
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `rueckenlaenge_korrigiert` | RüL als Konstruktionsmaß | cm |
| `vorderlaenge_korrigiert` | VL als Konstruktionsmaß | cm |

- **Abhängigkeiten:** Gemessene RüL/VL und die jeweils fachlich ermittelten signierten Korrekturen.
- **Gültigkeitsbereich:** Balancemaße des Oberteil-Konstruktionsformulars auf S. 537.
- **Technische Randbedingung:** `±` wird technisch als vorzeichenbehaftete Eingabe geführt; ein positiver Wert verlängert, ein negativer verkürzt.
- **Offene Fragen oder Widersprüche:** Das Formular enthält keine Werte und keine Regel zur Ermittlung der Korrekturen; die Additionsstruktur ist dennoch eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Korrekturwerte als Pflichtparameter führen und niemals leere Felder als null interpretieren.

## HOF-B1-S537-F07 — Individuelle Balance

- **Fachlicher Zweck:** Die individuelle Balance als Differenz von Vorder- und Rückenlänge bestimmen.
- **Quelle:** `formeln_s537.md`, Zeile 25; Originaltranskript `s537.md`, Zeile 46; Buchseite 537.
- **Originalbezeichnung:** `VL - RüL = individuelle Balance`.
- **Normalisierte Bezeichnung:** `individuelle_balance_allgemein`

### Buchfassung

```text
| Differenz `VL - RüL =` | individuelle Balance `=` |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderlaenge` | VL | variabel | cm |
| `rueckenlaenge` | RüL | variabel | cm |

### Formel und Rechenschritte

```text
individuelle_balance = vorderlaenge - rueckenlaenge
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `individuelle_balance` | Differenz VL − RüL | cm |

- **Abhängigkeiten:** VL und RüL; nach einer Korrektur sind die Ausgaben von `HOF-B1-S537-F06` einzusetzen.
- **Gültigkeitsbereich:** Balancemaße des Oberteil-Konstruktionsformulars auf S. 537.
- **Technische Randbedingung:** Die Operandenreihenfolge ist ausdrücklich VL minus RüL.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel ist eingetragen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Gemessene und korrigierte Balance getrennt benennen, obwohl beide dieselbe Differenzformel verwenden.

## HOF-B1-S537-F08 — Taillenausfall

- **Fachlicher Zweck:** Den Taillenausfall aus gemessener Taillenbreite und halber Taillenweite bestimmen.
- **Quelle:** `formeln_s537.md`, Zeile 35; Originaltranskript `s537.md`, Zeile 58; Buchseite 537.
- **Originalbezeichnung:** `gemessene TaB - ½ TaW`.
- **Normalisierte Bezeichnung:** `taillenausfall_oberteil_allgemein`

### Buchfassung

```text
- `TaAf` – Taillenausfall; `gemessene TaB - ½ TaW =`
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

- **Abhängigkeiten:** Gemessene TaB und ½ TaW, beispielsweise aus `HOF-B1-S537-F02`.
- **Gültigkeitsbereich:** Oberteil-Konstruktionsformular auf S. 537; Berechnung im Laufe der Konstruktion.
- **Technische Randbedingung:** Beide Breiten müssen dieselbe halbe Schnittseite betreffen.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel ist eingetragen; die Formel ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Das Vorzeichen erhalten und fachlich getrennt validieren.

## HOF-B1-S537-F09 — Hüftfehlbetrag

- **Fachlicher Zweck:** Den Hüftfehlbetrag aus gemessener Hüftbreite und halber Hüftweite bestimmen.
- **Quelle:** `formeln_s537.md`, Zeile 36; Originaltranskript `s537.md`, Zeile 59; Buchseite 537.
- **Originalbezeichnung:** `gemessene HüB - ½ HüW`.
- **Normalisierte Bezeichnung:** `hueftfehlbetrag_oberteil_allgemein`

### Buchfassung

```text
- `HüFb` – Hüftfehlbetrag; `gemessene HüB - ½ HüW =`
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

- **Abhängigkeiten:** Gemessene HüB und ½ HüW, beispielsweise aus `HOF-B1-S537-F03`.
- **Gültigkeitsbereich:** Oberteil-Konstruktionsformular auf S. 537; Berechnung im Laufe der Konstruktion.
- **Technische Randbedingung:** Beide Breiten müssen dieselbe halbe Schnittseite betreffen.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel ist eingetragen; die Formel ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Das Vorzeichen als fachlich bedeutsame Richtung erhalten.

## HOF-B1-S537-F10 — Armlochmehrweite und Sollwert

- **Fachlicher Zweck:** Die vorhandene Armlochmehrweite berechnen und gegen den aus der Armlochtiefenzugabe abgeleiteten Sollwert prüfen.
- **Quelle:** `formeln_s537.md`, Zeilen 41–42; Originaltranskript `s537.md`, Zeilen 61–62; Buchseite 537.
- **Originalbezeichnung:** `vAlU + hAlU - AraU =` und `2 · Zugabe zur AlT (Toleranz +2 cm bis -1 cm)`.
- **Normalisierte Bezeichnung:** `armlochmehrweite_mit_sollwert`

### Buchfassung

```text
- **Mehrweite im Armloch:** `vAlU + hAlU - AraU =`
- **Sollwert der Mehrweite:** `= 2 · Zugabe zur AlT (Toleranz +2 cm bis -1 cm) =`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderer_armlochumfang` | vAlU | variabel | cm |
| `hinterer_armlochumfang` | hAlU | variabel | cm |
| `armrundungsumfang` | AraU | variabel | cm |
| `armlochtiefe_zugabe` | Zugabe zur AlT | variabel | cm |
| `toleranz_unten` | Toleranz `-1 cm` | −1 | cm |
| `toleranz_oben` | Toleranz `+2 cm` | +2 | cm |

### Formel und Rechenschritte

```text
armlochmehrweite = vorderer_armlochumfang + hinterer_armlochumfang - armrundungsumfang
armlochmehrweite_soll = 2 * armlochtiefe_zugabe
armlochmehrweite_min = armlochmehrweite_soll - 1 cm
armlochmehrweite_max = armlochmehrweite_soll + 2 cm
kontrolle_erfuellt = armlochmehrweite_min <= armlochmehrweite <= armlochmehrweite_max
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `armlochmehrweite` | vorhandene Mehrweite im Armloch | cm |
| `armlochmehrweite_soll` | Sollwert als doppelte AlT-Zugabe | cm |
| `armlochmehrweite_min` | untere Toleranzgrenze | cm |
| `armlochmehrweite_max` | obere Toleranzgrenze | cm |
| `kontrolle_erfuellt` | Lage der vorhandenen Mehrweite im Toleranzbereich | boolesch |

- **Abhängigkeiten:** vAlU, hAlU, AraU sowie die Zugabe zur AlT; die Beziehung gilt laut Originaltranskript nur bei Oberteilen mit Brustabnähern.
- **Gültigkeitsbereich:** Armlochkontrolle im Oberteil-Konstruktionsformular auf S. 537, nur bei Oberteilen mit Brustabnähern.
- **Technische Randbedingung:** Die im Buch als `+2 cm bis -1 cm` gedruckten Toleranzwerte werden nach resultierender Größe als Untergrenze `Sollwert − 1 cm` und Obergrenze `Sollwert + 2 cm` benannt.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel ist eingetragen. Das Buch nennt keine weitere Regel innerhalb des Toleranzbereichs.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Istwert, Sollwert und beide asymmetrischen Toleranzgrenzen getrennt ausgeben; keine symmetrische Toleranz daraus machen.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s537.md`, Zeile 18 | 1 | Liste von Rechenfeld-Bezeichnungen und Teilungszeichen ohne vollständige Beziehung; keine zusätzliche Formel |
| `formeln_s537.md`, Zeile 30 | 1 | leeres Ausgabefeld `korrigierte Balance =` ohne Operanden oder eigene Beziehung |
| `formeln_s537.md`, Zeile 47 | 1 | Fotozuordnungs- und Provenienzzeile; keine Rechenformel |
| **Summe** | **3** | **1 unvollständiges Feldlabel, 1 leeres Ausgabefeld und 1 Provenienzzeile ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze und zu Wiederholungen

Die zehn Formeln auf S. 537 wiederholen Beziehungen, die auf S. 177 bereits an einer ausgefüllten PK-4-Konstruktion beziehungsweise im dortigen unteren Tabellenblock belegt sind. S. 537 erweitert ihre Anwendbarkeit jedoch materiell: Das leere Konstruktionsformular stellt sie als allgemeine Beziehungen für Oberteil-Konstruktionen dar. Deshalb erhalten sie seitenlokale Formel-IDs; die konkrete PK-4-Rechnung von S. 177 wird nicht dupliziert.

Das Originaltranskript enthält außerhalb des verbindlichen Extrakts die Zugabentabelle für Passformklassen 0 bis 10, die Schulterbeziehungen, die Aussage zur Ähnlichkeit von optimaler und korrigierter Balance sowie den Gültigkeitshinweis „nur bei Oberteilen mit Brustabnähern“. Diese Stellen wurden nicht als zusätzliche Buchfassungen erzeugt. Der Gültigkeitshinweis begrenzt lediglich die vollständig extrahierte Armlochkontrolle. Der Abschluss von `Z01` gilt für den vorhandenen extrahierten Kandidatenbestand.
