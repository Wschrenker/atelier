# Fachlich normalisierte Formeln — S. 174

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s174.md`
Originaltranskript: `../Band_1_geprüft_v1/s174.md`
Buchseite: Hofenbitzer, Band 1, S. 174

## HOF-B1-S174-F01 — Unveränderte Balancemaße der Normalfigur

- **Fachlicher Zweck:** Vorder- und Rückenlänge der Figur ohne Wuchs- oder Haltungsabweichung unverändert als Konstruktionsmaße übernehmen.
- **Quelle:** `formeln_s174.md`, Zeile 9; Originaltranskript `s174.md`, Zeile 15; Buchseite 174.
- **Originalbezeichnung:** `□1a Figur ohne Wuchs- oder Haltungsabweichung`
- **Normalisierte Bezeichnung:** `balancemasse_normalfigur`

### Buchfassung

```text
- **□1a** Figur ohne Wuchs- oder Haltungsabweichung — VL: Maßtabelle `46`, waagerechtes Taillenband `46`, vorderer Korrekturwert `0`, Konstruktion `46`; RüL jeweils `42`, hinterer Korrekturwert `0`. „Balance ist korrekt hier 4 cm".
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_gemessen` | VL am waagerechten Taillenband | 46 | cm |
| `rueckenlaenge_gemessen` | RüL | 42 | cm |
| `vorderer_korrekturwert` | vorderer Korrekturwert | 0 | cm |
| `hinterer_korrekturwert` | hinterer Korrekturwert | 0 | cm |

### Formel und Rechenschritte

```text
vorderlaenge_konstruktion = vorderlaenge_gemessen + vorderer_korrekturwert
                           = 46 cm + 0 cm
                           = 46 cm
rueckenlaenge_konstruktion = rueckenlaenge_gemessen + hinterer_korrekturwert
                            = 42 cm + 0 cm
                            = 42 cm
balance_gemessen = vorderlaenge_gemessen - rueckenlaenge_gemessen
                  = 46 cm - 42 cm
                  = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_konstruktion` | VL für die Konstruktion | 46 | cm |
| `rueckenlaenge_konstruktion` | RüL für die Konstruktion | 42 | cm |
| `balance_gemessen` | Differenz zwischen VL und RüL | 4 | cm |

- **Abhängigkeiten:** Gemessene VL und RüL sowie beide Korrekturwerte.
- **Gültigkeitsbereich:** Figur ohne Wuchs- oder Haltungsabweichung im Beispiel □1a.
- **Technische Randbedingung:** Die Korrekturwerte werden mit ihrem gedruckten Vorzeichen addiert.
- **Offene Fragen oder Widersprüche:** Keine; beide Konstruktionsmaße bleiben unverändert und `46 cm - 42 cm = 4 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Messwert, Korrekturwert und Konstruktionswert getrennt speichern.

## HOF-B1-S174-F02 — Korrektur der Vorderlänge bei starker Brust

- **Fachlicher Zweck:** Die zu lange Vorderlänge für ein gemeinsames Grundgerüst kürzen.
- **Quelle:** `formeln_s174.md`, Zeile 10; Originaltranskript `s174.md`, Zeile 16; Buchseite 174.
- **Originalbezeichnung:** `□2a Figur mit starker Brust`
- **Normalisierte Bezeichnung:** `vorderlaenge_konstruktion_starke_brust`

### Buchfassung

```text
- **□2a** Figur mit starker Brust — VL: Maßtabelle `48`, waagerechtes Taillenband `48`, vorderer Korrekturwert `−2`, Konstruktion `46`; RüL jeweils `42`, hinterer Korrekturwert `0`. „Balance ist nicht korrekt hier 6 cm" · „Vorderlänge ist bei starker Brust um 2 cm zu lang. Die VL wird für die Konstruktion um 2 cm gekürzt." · „Rückenlänge ist ok."
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_gemessen` | VL am waagerechten Taillenband | 48 | cm |
| `rueckenlaenge_gemessen` | RüL | 42 | cm |
| `vorderer_korrekturwert` | vorderer Korrekturwert | −2 | cm |
| `hinterer_korrekturwert` | hinterer Korrekturwert | 0 | cm |

### Formel und Rechenschritte

```text
balance_individuell = vorderlaenge_gemessen - rueckenlaenge_gemessen
                     = 48 cm - 42 cm
                     = 6 cm
vorderlaenge_konstruktion = vorderlaenge_gemessen + vorderer_korrekturwert
                           = 48 cm + (−2 cm)
                           = 46 cm
rueckenlaenge_konstruktion = 42 cm + 0 cm
                            = 42 cm
balance_konstruktion = 46 cm - 42 cm
                      = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_konstruktion` | gekürzte VL für die Konstruktion | 46 | cm |
| `rueckenlaenge_konstruktion` | unveränderte RüL für die Konstruktion | 42 | cm |
| `balance_konstruktion` | optimierte Differenz der Konstruktionsmaße | 4 | cm |

- **Abhängigkeiten:** Gemessene VL und RüL; vorderer Korrekturwert `−2 cm`.
- **Gültigkeitsbereich:** Figur mit starker Brust im Beispiel □2a.
- **Technische Randbedingung:** Der signierte Korrekturwert wird zur gemessenen VL addiert.
- **Offene Fragen oder Widersprüche:** Keine in diesem Kandidaten; `48 cm - 2 cm = 46 cm` und die korrigierte Balance beträgt 4 cm.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Figurbeobachtung wählt den Korrekturwert; der Zahlenwert darf nicht allein aus der Balanceabweichung erraten werden.

## HOF-B1-S174-F03 — Korrektur der Vorderlänge bei flacher Brust

- **Fachlicher Zweck:** Die zu kurze Vorderlänge für ein gemeinsames Grundgerüst verlängern.
- **Quelle:** `formeln_s174.md`, Zeile 11; Originaltranskript `s174.md`, Zeile 17; Buchseite 174.
- **Originalbezeichnung:** `□3a Figur mit flacher Brust`
- **Normalisierte Bezeichnung:** `vorderlaenge_konstruktion_flache_brust`

### Buchfassung

```text
- **□3a** Figur mit flacher Brust — VL: Maßtabelle `45`, waagerechtes Taillenband `45`, vorderer Korrekturwert `+1`, Konstruktion `46`; RüL jeweils `42`, hinterer Korrekturwert `0`. „Balance ist nicht korrekt hier 3 cm" · „Vorderlänge ist bei eingefallener, kleiner oder flacher Brust um 1 cm zu kurz. Sie wird für die Konstruktion um 1 cm vergrößert." · „Rückenlänge ist ok."
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_gemessen` | VL am waagerechten Taillenband | 45 | cm |
| `rueckenlaenge_gemessen` | RüL | 42 | cm |
| `vorderer_korrekturwert` | vorderer Korrekturwert | +1 | cm |
| `hinterer_korrekturwert` | hinterer Korrekturwert | 0 | cm |

### Formel und Rechenschritte

```text
balance_individuell = 45 cm - 42 cm
                     = 3 cm
vorderlaenge_konstruktion = 45 cm + 1 cm
                           = 46 cm
rueckenlaenge_konstruktion = 42 cm + 0 cm
                            = 42 cm
balance_konstruktion = 46 cm - 42 cm
                      = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_konstruktion` | verlängerte VL für die Konstruktion | 46 | cm |
| `rueckenlaenge_konstruktion` | unveränderte RüL für die Konstruktion | 42 | cm |
| `balance_konstruktion` | optimierte Differenz der Konstruktionsmaße | 4 | cm |

- **Abhängigkeiten:** Gemessene VL und RüL; vorderer Korrekturwert `+1 cm`.
- **Gültigkeitsbereich:** Figur mit flacher Brust im Beispiel □3a.
- **Technische Randbedingung:** Der signierte Korrekturwert wird zur gemessenen VL addiert.
- **Offene Fragen oder Widersprüche:** Keine in diesem Kandidaten; `45 cm + 1 cm = 46 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Korrekturrichtung über das Vorzeichen abbilden, nicht über getrennte Kürzungs- und Verlängerungsfunktionen.

## HOF-B1-S174-F04 — Unvollständige VL-Rechnung der Skizze □2b

- **Fachlicher Zweck:** Die in Skizze □2b gedruckte Subtraktion an der gemessenen Vorderlänge technisch erfassen.
- **Quelle:** `formeln_s174.md`, Zeile 16; Originaltranskript `s174.md`, Zeile 21; Buchseite 174.
- **Originalbezeichnung:** `gemessene VL − 1 cm = 48 cm − 1 cm`
- **Normalisierte Bezeichnung:** `vorderlaenge_skizze_2b_ungeklaert`

### Buchfassung

```text
- □2b-Skizze: „gemessene VL − 1 cm = 48 cm − 1 cm"; Maßnotizen „0,5 bis 1 cm", „2 cm".
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_gemessen` | gemessene VL | 48 | cm |
| `abzug_skizze` | `1 cm` in der Skizzenformel | 1 | cm |

### Formel und Rechenschritte

```text
vorderlaenge_skizze = vorderlaenge_gemessen - abzug_skizze
                     = 48 cm - 1 cm
                     = 47 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert rechnerisch | Einheit |
|---|---|---:|---|
| `vorderlaenge_skizze` | rechnerisches Ergebnis der gedruckten Skizzenformel | 47 | cm |

- **Abhängigkeiten:** Gemessene VL und der in der Skizze gedruckte Abzug.
- **Gültigkeitsbereich:** Skizze □2b zur Figur mit starker Brust.
- **Technische Randbedingung:** Die Maßnotizen `0,5 bis 1 cm` und `2 cm` sind ohne eindeutige Zuordnung keine zusätzlichen Operanden dieser Formel.
- **Offene Fragen oder Widersprüche:** Das Ergebnis ist im Extrakt nicht gedruckt. Zudem widerspricht der Abzug `1 cm` dem Korrekturwert `−2 cm` und dem Konstruktionswert `46 cm` in □2a. Die beabsichtigte Größe ist nicht sicher bestimmbar.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis Skizzenmaß und Bezug des Abzugs am Buchbild fachlich geklärt sind.

## HOF-B1-S174-F05 — Unvollständige VL-Rechnung der Skizze □3b

- **Fachlicher Zweck:** Die in Skizze □3b gedruckte Subtraktion an der gemessenen Vorderlänge technisch erfassen.
- **Quelle:** `formeln_s174.md`, Zeile 17; Originaltranskript `s174.md`, Zeile 22; Buchseite 174.
- **Originalbezeichnung:** `gemessene VL − 1 cm = 45 cm − 1 cm`
- **Normalisierte Bezeichnung:** `vorderlaenge_skizze_3b_ungeklaert`

### Buchfassung

```text
- □3b-Skizze: „gemessene VL − 1 cm = 45 cm − 1 cm"; Maßnotiz „1 cm"; Beschriftung „VT".
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_gemessen` | gemessene VL | 45 | cm |
| `abzug_skizze` | `1 cm` in der Skizzenformel | 1 | cm |

### Formel und Rechenschritte

```text
vorderlaenge_skizze = vorderlaenge_gemessen - abzug_skizze
                     = 45 cm - 1 cm
                     = 44 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert rechnerisch | Einheit |
|---|---|---:|---|
| `vorderlaenge_skizze` | rechnerisches Ergebnis der gedruckten Skizzenformel | 44 | cm |

- **Abhängigkeiten:** Gemessene VL und der in der Skizze gedruckte Abzug.
- **Gültigkeitsbereich:** Skizze □3b zur Figur mit flacher Brust.
- **Technische Randbedingung:** Die Beschriftung `VT` benennt einen Punkt und ist kein Operand.
- **Offene Fragen oder Widersprüche:** Das Ergebnis ist im Extrakt nicht gedruckt. Die Subtraktion ergibt 44 cm, während □3a die gemessene VL um 1 cm auf den Konstruktionswert 46 cm vergrößert. Die beabsichtigte Größe ist nicht sicher bestimmbar.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis Bedeutung und Richtung der Skizzenrechnung geklärt sind.

## HOF-B1-S174-F06 — Optimale Balance aus dem Brustumfang ab 100 cm

- **Fachlicher Zweck:** Die optimale Balance `Bal` für vier Brustumfangsbereiche nach der gedruckten Konstruktionstabelle berechnen.
- **Quelle:** `formeln_s174.md`, Zeilen 22–25; Originaltranskript `s174.md`, Zeilen 43–46; Buchseite 174.
- **Originalbezeichnung:** `optimale Balance Bal`
- **Normalisierte Bezeichnung:** `optimale_balance_nach_brustumfang`

### Buchfassung

```text
| 100 bis 109 | (BrU − 100) : 10 + 4,5 |
| 110 bis 119 | (BrU − 100) : 10 + 5,0 |
| 120 bis 129 | (BrU − 100) : 10 + 5,5 |
| 130 bis 150 | (BrU − 100) : 10 + 6,0 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustumfang` | BrU | variabel, 100 bis 150 | cm |
| `bereichs_zuschlag` | gedruckter Summand je Zeile | 4,5 / 5,0 / 5,5 / 6,0 | cm |

### Formel und Rechenschritte

```text
wenn 100 <= brustumfang <= 109:
    optimale_balance = ((brustumfang - 100 cm) / 10) + 4,5 cm
wenn 110 <= brustumfang <= 119:
    optimale_balance = ((brustumfang - 100 cm) / 10) + 5,0 cm
wenn 120 <= brustumfang <= 129:
    optimale_balance = ((brustumfang - 100 cm) / 10) + 5,5 cm
wenn 130 <= brustumfang <= 150:
    optimale_balance = ((brustumfang - 100 cm) / 10) + 6,0 cm

wörtliche Endpunktkontrolle:
100 bis 109 -> 4,5 cm bis 5,4 cm
110 bis 119 -> 6,0 cm bis 6,9 cm
120 bis 129 -> 7,5 cm bis 8,4 cm
130 bis 150 -> 9,0 cm bis 11,0 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `optimale_balance` | optimale Differenz zwischen VL und RüL | cm |

- **Abhängigkeiten:** Brustumfang und Auswahl genau einer Tabellenzeile.
- **Gültigkeitsbereich:** Gedruckte Bereiche `100 bis 150` der Tabelle □7.
- **Technische Randbedingung:** Die Bereichsgrenzen sind einschließlich interpretiert; alle vier Zeilen verwenden wörtlich den Subtrahenden `100`.
- **Offene Fragen oder Widersprüche:** Die Formeln sind rechnerisch eindeutig, erzeugen aber zwischen den Bereichen Sprünge von 5,4 auf 6,0 cm, von 6,9 auf 7,5 cm und von 8,4 auf 9,0 cm. Eine abweichende Bereichs- oder Rundungsregel ist nicht belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als explizite bereichsabhängige Funktion umsetzen und keine Glättung oder andere Subtrahenden ergänzen.

## HOF-B1-S174-F07 — Balance-Problem der Figur mit starker Brust

- **Fachlicher Zweck:** Die Abweichung zwischen optimaler und individueller Balance bestimmen.
- **Quelle:** `formeln_s174.md`, Zeile 30; Originaltranskript `s174.md`, Zeile 57; Buchseite 174.
- **Originalbezeichnung:** `Bal − individuelle Balance = Balance-Problem`
- **Normalisierte Bezeichnung:** `balance_problem_vorzeichen_ungeklaert`

### Buchfassung

```text
> Bal − individuelle Balance = Balance-Problem = **2**
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `optimale_balance` | Bal | 4,0 | cm |
| `individuelle_balance` | individuelle Balance | 6,0 | cm |

### Formel und Rechenschritte

```text
balance_problem_woertlich = optimale_balance - individuelle_balance
                           = 4,0 cm - 6,0 cm
                           = −2,0 cm

gedrucktes Ergebnis = 2 cm
mögliche, nicht belegte Betragslesart = abs(4,0 cm - 6,0 cm) = 2,0 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `balance_problem_woertlich` | Ergebnis der gedruckten Operandenreihenfolge | −2,0 | cm |
| `balance_problem_gedruckt` | gedrucktes Ergebnisfeld | 2 | cm |

- **Abhängigkeiten:** Optimale Balance aus Tabelle □7 und individuelle Balance aus VL minus RüL.
- **Gültigkeitsbereich:** Rechenbeispiel zur Figur mit starker Brust in □2a.
- **Technische Randbedingung:** Allgemeine Formel, Einsetzwerte und Druckergebnis werden getrennt ausgewertet.
- **Offene Fragen oder Widersprüche:** `4,0 cm - 6,0 cm = −2,0 cm`, nicht `2 cm`. Betrag oder umgekehrte Subtraktion wären rechnerisch passend, sind im Extrakt aber nicht belegt.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Keine Vorzeichenkorrektur oder Betragsbildung implementieren, bevor die fachliche Bedeutung des Vorzeichens geklärt ist.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s174.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 35 | 1 | redaktionelle Notiz zur bereits in `HOF-B1-S174-F07` dokumentierten Inkonsistenz; keine zusätzliche Buchformel |
| **Summe** | **1** | **1 redaktionelle Prüfnotiz ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s174.md` enthält zusätzliche formelartige Stellen, die im verbindlichen Extrakt fehlen: Zeile 20 nennt für □1b `optimierte VL − 1 cm = 46 cm − 1 cm` und `optimierte RüL = 42 cm`; Zeile 25 bezeichnet die optimale Balance als Differenz von VL und RüL; die Zeilen 26–27 beschreiben die Rückübertragung der zuvor vorgenommenen Vorderlängen-Korrekturen. Diese Beziehungen wurden nicht stillschweigend als Buchfassungen normalisiert. Die konstanten Tabellenzeilen für BrU 80–99 aus dem Originaltranskript sind ebenfalls nicht Bestandteil des extrahierten Kandidatenblocks.
