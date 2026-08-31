# Fachlich normalisierte Formeln — S. 175

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s175.md`
Originaltranskript: `../Band_1_geprüft_v1/s175.md`
Buchseite: Hofenbitzer, Band 1, S. 175

## HOF-B1-S175-F01 — Korrektur der Rückenlänge bei rundem Rücken

- **Fachlicher Zweck:** Die zu lange Rückenlänge für das gemeinsame Grundgerüst kürzen.
- **Quelle:** `formeln_s175.md`, Zeile 9; Originaltranskript `s175.md`, Zeile 15; Buchseite 175.
- **Originalbezeichnung:** `□4a Figur mit rundem Rücken`
- **Normalisierte Bezeichnung:** `rueckenlaenge_konstruktion_runder_ruecken`

### Buchfassung

```text
- **□4a** Figur mit rundem Rücken — VL: Maßtabelle `46`, waagerechtes Taillenband `46`, vorderer Korrekturwert `0`, Konstruktion `46`; RüL: Maßtabelle `43,5`, waagerechtes Taillenband `43,5`, hinterer Korrekturwert `−1,5`, Konstruktion `42`. „Balance ist nicht korrekt hier 3 cm" · „Vorderlänge ist ok." · „Rückenlänge ist bei rundem Rücken um 1,5 cm zu lang. Sie wird für die Konstruktion um 1,5 cm gekürzt."
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_gemessen` | VL | 46 | cm |
| `rueckenlaenge_gemessen` | RüL | 43,5 | cm |
| `vorderer_korrekturwert` | vorderer Korrekturwert | 0 | cm |
| `hinterer_korrekturwert` | hinterer Korrekturwert | −1,5 | cm |

### Formel und Rechenschritte

```text
balance_individuell_rechnerisch = 46 cm - 43,5 cm
                                 = 2,5 cm
gedruckte individuelle Balance = 3 cm
rueckenlaenge_konstruktion = 43,5 cm + (−1,5 cm)
                            = 42 cm
vorderlaenge_konstruktion = 46 cm + 0 cm
                           = 46 cm
balance_konstruktion = 46 cm - 42 cm
                      = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `rueckenlaenge_konstruktion` | gekürzte RüL für die Konstruktion | 42 | cm |
| `vorderlaenge_konstruktion` | unveränderte VL für die Konstruktion | 46 | cm |
| `balance_konstruktion` | optimierte Differenz der Konstruktionsmaße | 4 | cm |

- **Abhängigkeiten:** Gemessene VL und RüL; hinterer Korrekturwert `−1,5 cm`.
- **Gültigkeitsbereich:** Figur mit rundem Rücken im Beispiel □4a.
- **Technische Randbedingung:** Der signierte Korrekturwert wird zur gemessenen RüL addiert.
- **Offene Fragen oder Widersprüche:** Die gedruckte Korrektur ist konsistent: `43,5 cm - 1,5 cm = 42 cm`. Die ungerundete Messdifferenz beträgt jedoch 2,5 cm, während die Buchfassung „hier 3 cm" nennt; eine Rundungsregel ist nicht angegeben. Dieser Konflikt ändert die eindeutige Längenkorrektur nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Gemessene, gedruckte und optimierte Balance getrennt protokollieren; nicht stillschweigend auf ganze Zentimeter runden.

## HOF-B1-S175-F02 — Korrektur der Rückenlänge bei geradem Rücken

- **Fachlicher Zweck:** Die zu kurze Rückenlänge für das gemeinsame Grundgerüst verlängern.
- **Quelle:** `formeln_s175.md`, Zeile 10; Originaltranskript `s175.md`, Zeile 16; Buchseite 175.
- **Originalbezeichnung:** `□5a Figur mit geradem Rücken`
- **Normalisierte Bezeichnung:** `rueckenlaenge_konstruktion_gerader_ruecken`

### Buchfassung

```text
- **□5a** Figur mit geradem Rücken — VL: Maßtabelle `46`, waagerechtes Taillenband `46`, vorderer Korrekturwert `0`, Konstruktion `46`; RüL: Maßtabelle `41`, waagerechtes Taillenband `41`, hinterer Korrekturwert `+1`, Konstruktion `42`. „Balance ist nicht korrekt hier 5 cm" · „Vorderlänge ist ok." · „Rückenlänge ist bei geraden, flachen Rücken um 1 cm zu kurz. Sie wird für die Konstruktion um 1 cm vergrößert."
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_gemessen` | VL | 46 | cm |
| `rueckenlaenge_gemessen` | RüL | 41 | cm |
| `vorderer_korrekturwert` | vorderer Korrekturwert | 0 | cm |
| `hinterer_korrekturwert` | hinterer Korrekturwert | +1 | cm |

### Formel und Rechenschritte

```text
balance_individuell = 46 cm - 41 cm
                     = 5 cm
rueckenlaenge_konstruktion = 41 cm + 1 cm
                            = 42 cm
vorderlaenge_konstruktion = 46 cm + 0 cm
                           = 46 cm
balance_konstruktion = 46 cm - 42 cm
                      = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `rueckenlaenge_konstruktion` | verlängerte RüL für die Konstruktion | 42 | cm |
| `vorderlaenge_konstruktion` | unveränderte VL für die Konstruktion | 46 | cm |
| `balance_konstruktion` | optimierte Differenz der Konstruktionsmaße | 4 | cm |

- **Abhängigkeiten:** Gemessene VL und RüL; hinterer Korrekturwert `+1 cm`.
- **Gültigkeitsbereich:** Figur mit geradem, flachem Rücken im Beispiel □5a.
- **Technische Randbedingung:** Der signierte Korrekturwert wird zur gemessenen RüL addiert.
- **Offene Fragen oder Widersprüche:** Die Zahlen dieses Kandidaten sind konsistent. Das Originaltranskript nennt in der späteren Bildunterschrift □5b dennoch „runden Rücken"; diese nicht extrahierte Kontextinkonsistenz ändert die Rechnung nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Figurtyp und numerische Korrektur getrennt führen, damit der Buchfehler in □5b nicht die Rechenrichtung verändert.

## HOF-B1-S175-F03 — Gemeinsame VL- und RüL-Korrektur bei Skoliose

- **Fachlicher Zweck:** Vorder- und Rückenlänge einer Figur mit extrem rundem Rücken und eingefallener Brust auf das gemeinsame Grundgerüst normalisieren.
- **Quelle:** `formeln_s175.md`, Zeile 11; Originaltranskript `s175.md`, Zeile 17; Buchseite 175.
- **Originalbezeichnung:** `□6a Figur mit extrem rundem Rücken und eingefallener Brust (Buckel, Skoliose)`
- **Normalisierte Bezeichnung:** `balancemasse_konstruktion_skoliose`

### Buchfassung

```text
- **□6a** Figur mit extrem rundem Rücken und eingefallener Brust (Buckel, Skoliose) — VL: Maßtabelle `44,5`, waagerechtes Taillenband `44,5`, vorderer Korrekturwert `+1,5`, Konstruktion `46`; RüL: Maßtabelle `44,5`, waagerechtes Taillenband `44,5`, hinterer Korrekturwert `−2,5`, Konstruktion `42`. „Balance ist nicht korrekt hier 0 cm" · „Vorderlänge ist bei eingefallener Brust um 1,5 cm zu kurz. Sie wird für die Konstruktion um 1,5 cm vergrößert." · „Rückenlänge ist bei rundem Rücken um 2,5 cm zu lang. Sie wird für die Konstruktion um 2,5 cm gekürzt."
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_gemessen` | VL | 44,5 | cm |
| `rueckenlaenge_gemessen` | RüL | 44,5 | cm |
| `vorderer_korrekturwert` | vorderer Korrekturwert | +1,5 | cm |
| `hinterer_korrekturwert` | hinterer Korrekturwert | −2,5 | cm |

### Formel und Rechenschritte

```text
balance_individuell = 44,5 cm - 44,5 cm
                     = 0 cm
vorderlaenge_konstruktion = 44,5 cm + 1,5 cm
                           = 46 cm
rueckenlaenge_konstruktion = 44,5 cm + (−2,5 cm)
                            = 42 cm
balance_konstruktion = 46 cm - 42 cm
                      = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_konstruktion` | verlängerte VL für die Konstruktion | 46 | cm |
| `rueckenlaenge_konstruktion` | gekürzte RüL für die Konstruktion | 42 | cm |
| `balance_konstruktion` | optimierte Differenz der Konstruktionsmaße | 4 | cm |

- **Abhängigkeiten:** Beide gemessenen Längen und beide figurabhängigen Korrekturwerte.
- **Gültigkeitsbereich:** Beispiel □6a für extrem runden Rücken mit eingefallener Brust beziehungsweise Skoliose.
- **Technische Randbedingung:** Beide signierten Korrekturwerte werden unabhängig auf ihre jeweilige Länge angewendet.
- **Offene Fragen oder Widersprüche:** Keine in den Zahlen dieses Kandidaten; beide Korrekturpfade führen zu den gemeinsamen Konstruktionsmaßen 46 cm und 42 cm.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** VL- und RüL-Korrektur als getrennte Parameter anwenden und gemeinsam gegen die Zielbalance prüfen.

## HOF-B1-S175-F04 — Rückübertragung der Skoliose-Korrekturen auf den Grundschnitt

- **Fachlicher Zweck:** Die für das gemeinsame Grundgerüst vorgenommenen Längenkorrekturen an der individuellen Schnittform wieder zurücknehmen.
- **Quelle:** `formeln_s175.md`, Zeile 22; Originaltranskript `s175.md`, Zeile 27; Buchseite 175.
- **Originalbezeichnung:** `□6b Optimierung für die Skoliose`
- **Normalisierte Bezeichnung:** `balancemasse_rueckuebertragung_skoliose`

### Buchfassung

```text
- **□6b** Optimierung für die Skoliose: Für die Konstruktion wurde die VL um 1,5 cm verlängert, die RüL um 2,5 cm gekürzt. Diese VL-Verlängerung um 1,5 cm wird nun reduziert und die RüL-Kürzung um 2,5 cm wieder zugelegt. Der Brustabnäher wird kleiner, der Schulterabnäher wird größer.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_konstruktion` | für die Konstruktion verlängerte VL | 46 | cm |
| `rueckenlaenge_konstruktion` | für die Konstruktion gekürzte RüL | 42 | cm |
| `vorderlaengen_verlaengerung` | VL-Verlängerung | 1,5 | cm |
| `rueckenlaengen_kuerzung` | RüL-Kürzung | 2,5 | cm |

### Formel und Rechenschritte

```text
vorderlaenge_individuell = vorderlaenge_konstruktion - vorderlaengen_verlaengerung
                          = 46 cm - 1,5 cm
                          = 44,5 cm
rueckenlaenge_individuell = rueckenlaenge_konstruktion + rueckenlaengen_kuerzung
                           = 42 cm + 2,5 cm
                           = 44,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderlaenge_individuell` | wiederhergestellte individuelle VL | 44,5 | cm |
| `rueckenlaenge_individuell` | wiederhergestellte individuelle RüL | 44,5 | cm |

- **Abhängigkeiten:** Konstruktionsmaße und Korrekturbeträge aus `HOF-B1-S175-F03`.
- **Gültigkeitsbereich:** Grundschnittoptimierung □6b für das dargestellte Skoliose-Beispiel.
- **Technische Randbedingung:** Die Rückübertragung kehrt die Vorzeichen der temporären Konstruktionskorrekturen um. Die Änderungen der Abnähergrößen sind qualitativ genannt, aber nicht numerisch bestimmt.
- **Offene Fragen oder Widersprüche:** Die Längenpfade sind mit □6a konsistent. Für die Verteilung auf Brust- und Schulterabnäher fehlt im extrahierten Bestand eine quantitative Regel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Längenrückübertragung und geometrische Abnäheränderung als zwei getrennte Schritte modellieren; für die Abnäher noch keine Beträge erfinden.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s175.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 16–17 | 2 | wiederholte Messbeschriftungen der RüL und Maßnotizen aus □4a/□5a; reine Eingabe- und Zeichnungslabels ohne eigenständige Rechenbeziehung |
| **Summe** | **2** | **2 wiederholte Mess- und Zeichnungslabels ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s175.md` enthält in den Zeilen 25–26 die Rückübertragungsregeln für □4b und □5b sowie in den Zeilen 35–48 die allgemeine Arbeitsfolge vom Balance-Problem über normalisierte Konstruktionsmaße bis zur Wiederherstellung der individuellen Körpermaße. Diese Beziehungen fehlen im verbindlichen Extrakt und wurden nicht stillschweigend als Buchfassungen normalisiert. Der Buchfehler in Zeile 26 — □5b nennt „runden Rücken", obwohl □5a den geraden Rücken behandelt — bleibt als Kontextwiderspruch sichtbar.
