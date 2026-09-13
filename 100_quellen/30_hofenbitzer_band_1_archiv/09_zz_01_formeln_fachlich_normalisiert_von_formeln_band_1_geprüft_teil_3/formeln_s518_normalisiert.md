# Fachlich normalisierte Formeln — S. 518

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s518.md`  
Originaltranskript: `s518.md`  
Buchseite: Hofenbitzer, Band 1, S. 518

Die Seite zeigt den weitenreduzierten engen Oberteil-Grundschnitt für Damen. Die Konstruktionsbeziehungen betreffen Halsloch, Schulter, Brust-/Rückenbreite, Armloch sowie die Kontrolle von Taillen- und Hüftweite. Die Herrentabelle auf S. 519 ist eine eigene Buchfassung und wird dort separat normalisiert.

## HOF-B1-S518-F01 — Hintere Schulternahtlänge mit Einhalteweite

- **Fachlicher Zweck:** Die hintere Schulternaht aus der Schulternahtlänge und einer kleinen Einhalteweite bestimmen.
- **Quelle:** `formeln_s518.md`, Zeile 14; Originaltranskript `s518.md`, Zeile 32; Buchseite 518.
- **Originalbezeichnung:** `hSuNL = SuNL + 0 bis 0,5 cm`.
- **Normalisierte Bezeichnung:** `hintere_schulternahtlaenge`

### Buchfassung
```text
hSuNL = SuNL + 0 bis 0,5 cm
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `schulternahtlaenge` | SuNL | 11,3 | cm |
| `schulternaht_einhalteweite` | 0 bis 0,5 cm | 0 bis 0,5 | cm |

### Formel und Rechenschritte
```text
hintere_schulternahtlaenge = schulternahtlaenge + schulternaht_einhalteweite
```

### Ausgabe
`hintere_schulternahtlaenge` — hSuNL, cm.

- **Abhängigkeiten:** SuNL aus der Tabelle.
- **Gültigkeitsbereich:** Damen, Größe 38, enger Oberteil-Grundschnitt.
- **Offene Fragen oder Widersprüche:** Die Tabelle nennt hSuNL mit 11,3 cm trotz einer möglichen Einhalteweite; die konkrete Auswahl ist nicht belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Einhalteweite als Bereichsparameter führen; nicht automatisch einen Wert auswählen.

## HOF-B1-S518-F02 — Reduzierte hintere Rückenbreite

- **Fachlicher Zweck:** Die halbe Rückenbreite um 7 % reduzieren.
- **Quelle:** `formeln_s518.md`, Zeile 23; Originaltranskript `s518.md`, Zeile 57; Buchseite 518.
- **Originalbezeichnung:** `RüB + −7 % = RüB+ 15,3`.
- **Normalisierte Bezeichnung:** `reduzierte_rueckenbreite_halb`

### Buchfassung
```text
RüB | Rückenbreite (½) | 16,5 | + −7 % | RüB+ 15,3
```

### Formel und Rechenschritte
```text
reduzierte_rueckenbreite_halb = rueckenbreite_halb * (1 - 0,07)
                               = 16,5 cm * 0,93
                               = 15,345 cm
```

### Ausgabe
`reduzierte_rueckenbreite_halb` — RüB+, gedruckt 15,3 cm.

- **Abhängigkeiten:** RüB.
- **Gültigkeitsbereich:** Damen, Größe 38, weitenreduzierter Grundschnitt.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine Rundungsregel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern mit 15,345 cm weiterrechnen und die Druckdarstellung getrennt halten.

## HOF-B1-S518-F03 — Reduzierter Armdurchmesser und Teilungen

- **Fachlicher Zweck:** Den Armdurchmesser reduzieren und daraus Teilstrecken am hinteren Armloch ableiten.
- **Quelle:** `formeln_s518.md`, Zeile 24; Originaltranskript `s518.md`, Zeile 58; Buchseite 518.
- **Originalbezeichnung:** `ArD + −7 %`; `¼ ArD+`, `⅓ ArD+`, `⅔ ArD+`.
- **Normalisierte Bezeichnung:** `reduzierter_armdurchmesser_und_armlochteilungen`

### Buchfassung
```text
ArD | Armdurchmesser | 9,3 | + −7 % | ArD+ 8,7; ¼ 2,2; 3,9
```

### Formel und Rechenschritte
```text
armdurchmesser_reduziert = armdurchmesser * 0,93
                          = 9,3 cm * 0,93
                          = 8,649 cm ≈ 8,7 cm

viertel_armdurchmesser = armdurchmesser_reduziert / 4
                        ≈ 2,2 cm

drittel_armloch = armdurchmesser_reduziert / 3
                 = 2,883 cm
zweidrittel_armloch = armdurchmesser_reduziert * 2 / 3
                    = 5,766 cm
```

### Ausgabe
`armdurchmesser_reduziert` — ArD+, gedruckt 8,7 cm; Teilungswerte in cm.

- **Abhängigkeiten:** ArD und die gewählte Position der Seitennaht.
- **Gültigkeitsbereich:** Damen-Grundschnitt mit oder ohne Brustabnäher.
- **Offene Fragen oder Widersprüche:** Der Druckwert `3,9` ist keiner der angegebenen Teilungen eindeutig zugeordnet; die Buchfassung enthält keine vollständige Zuordnung. Die technischen Teilungen sind deshalb nicht als Buchwert ausgegeben.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Reduktion und Teilungsgeometrie getrennt führen; die Position `½`, `⅓` oder `⅔` als Modellentscheidung behandeln.

## HOF-B1-S518-F04 — Reduzierte halbe Brustbreite

- **Fachlicher Zweck:** Die halbe Brustbreite um 7 % reduzieren.
- **Quelle:** `formeln_s518.md`, Zeile 25; Originaltranskript `s518.md`, Zeile 59; Buchseite 518.
- **Originalbezeichnung:** `BrB + −7 % = BrB+ 16,9`.
- **Normalisierte Bezeichnung:** `reduzierte_brustbreite_halb`

### Buchfassung
```text
BrB | Brustbreite (½) | 18,2 | + −7 % | BrB+ 16,9
```

### Formel und Rechenschritte
```text
reduzierte_brustbreite_halb = brustbreite_halb * 0,93
                             = 18,2 cm * 0,93
                             = 16,926 cm ≈ 16,9 cm
```

### Ausgabe
`reduzierte_brustbreite_halb` — BrB+, 16,9 cm gedruckt.

- **Abhängigkeiten:** BrB.
- **Gültigkeitsbereich:** Damen-Grundschnitt, Größe 38.
- **Offene Fragen oder Widersprüche:** Keine rechnerische; Rundungsregel fehlt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Prozentsatz als Reduktionsparameter führen.

## HOF-B1-S518-F05 — Kontrollwert der reduzierten halben Brustweite

- **Fachlicher Zweck:** Die halbe Brustumfangskontrolle um 7 % reduzieren.
- **Quelle:** `formeln_s518.md`, Zeile 26; Originaltranskript `s518.md`, Zeile 60; Buchseite 518.
- **Originalbezeichnung:** `Σ = ½ BrU`; `½ BrW 40,9`.
- **Normalisierte Bezeichnung:** `reduzierte_halbe_brustweite_kontrolle`

### Buchfassung
```text
Kontrolle | Σ = ½ BrU | 44 | + −7 % | ½ BrW 40,9
```

### Formel und Rechenschritte
```text
reduzierte_halbe_brustweite = halber_brustumfang * 0,93
                             = 44 cm * 0,93
                             = 40,92 cm ≈ 40,9 cm
```

### Ausgabe
`reduzierte_halbe_brustweite` — ½ BrW, gedruckt 40,9 cm.

- **Abhängigkeiten:** BrU beziehungsweise ½ BrU.
- **Gültigkeitsbereich:** Kontrollzeile der Damenkonstruktion.
- **Offene Fragen oder Widersprüche:** Keine rechnerische; Rundungsregel fehlt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Kontrolle gegen die Summe der reduzierten Breiten auswerten.

## HOF-B1-S518-F06 — Individuelle Balance

- **Fachlicher Zweck:** Die Differenz zwischen Vorder- und Rückenlänge als individuelle Balance bestimmen.
- **Quelle:** `formeln_s518.md`, Zeile 31; Originaltranskript `s518.md`, Zeile 71; Buchseite 518.
- **Originalbezeichnung:** `VL − RüL`.
- **Normalisierte Bezeichnung:** `individuelle_balance`

### Buchfassung
```text
Differenz VL − RüL | individuelle Balance | 3,7 | korrigierte Balance | 3,7
```

### Formel und Rechenschritte
```text
individuelle_balance = vorderlaenge - rueckenlaenge
                     = 45,3 cm - 41,6 cm
                     = 3,7 cm
```

### Ausgabe
`individuelle_balance` — 3,7 cm.

- **Abhängigkeiten:** VL und RüL.
- **Gültigkeitsbereich:** Damen, Größe 38.
- **Offene Fragen oder Widersprüche:** Keine; die nach der Reduktion gedruckten Längenergebnisse werden nicht in dieser Kandidatenzeile berechnet.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Balance als signierte Längendifferenz speichern.

## HOF-B1-S518-F07 — Unvollständige Brustumfangs-Teilung

- **Fachlicher Zweck:** Die abgebildete Teilungsbeziehung des Brustumfangs dokumentieren.
- **Quelle:** `formeln_s518.md`, Zeile 16; Originaltranskript `s518.md`, Zeile 36; Buchseite 518.
- **Originalbezeichnung:** `BrU : 20 ± 1 bis`.
- **Normalisierte Bezeichnung:** `brustumfang_teilung_unvollstaendig`

### Buchfassung
```text
BrU : 20 ± 1 bis
```

### Formel und Rechenschritte
```text
unvollstaendige_beziehung = brustumfang / 20 ± nicht_bekannter_folgewert
```

### Ausgabe
Keine eindeutige Ausgabe.

- **Abhängigkeiten:** BrU.
- **Gültigkeitsbereich:** Beschriftung der Damenkonstruktion.
- **Offene Fragen oder Widersprüche:** Der Folgewert fehlt. Die Quelle markiert dies als Satzfehler im Buch; es darf kein Wert ergänzt werden.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis der fehlende Buchwert geklärt ist.

## Ausgeschlossene Kandidaten

| Extraktbereich | Anzahl | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Direkte Eingaben und Bereiche (`HlB`, `SuWi`, `SuNL`) ohne vollständige Zielausgabe; die eigenständige hSuNL-Beziehung ist in F01 geführt. |
| Zeile 15 | 1 | Konstruktions- und Teilungsbeschriftungen ohne eindeutig benannte Ausgabe; F03 führt nur die belegbare ArD-Reduktion und markiert die Teilungszuordnung offen. |
| Zeile 17 | 1 | Taillenabnäher- und Ausfallbeschriftungen ohne eingesetzte Buchwerte beziehungsweise vollständige Zielzuordnung. |
| Zeile 18 | 1 | Hüftbreiten-, Fehlbetrags- und Reduktionsbeschriftungen ohne vollständige Rechenzeile im Extrakt. |
| Zeile 36 | 1 | Unvollständige Beziehung; als F07 gesperrt dokumentiert, nicht als ausführbare Formel. |
| **Summe** | **5** | **Bereiche, Konstruktionslabels und unvollständige Buchfassung ausgeschlossen** |

### Prüfhinweise

1. Die vier Tabellenrechnungen mit `−7 %` sind rechnerisch konsistent: `16,5 · 0,93 = 15,345`, `9,3 · 0,93 = 8,649`, `18,2 · 0,93 = 16,926` und `44 · 0,93 = 40,92 cm`; die Druckwerte sind auf eine Nachkommastelle verkürzt oder gerundet.
2. Die Tabellenzeile `AlT 20,1 + −3 % = AlT+ 22,6` bleibt als geprüfter Buchwiderspruch außerhalb des normalisierten Formelbestands: `20,1 · 0,97 = 19,5 cm`, nicht `22,6 cm`. Die Buchquelle nennt ausdrücklich den Widerspruch zu S. 519.
3. Die Konstruktionsangaben `HlB`, `SuWi`, Taillen-/Hüftausfall und die Armlochpositionen bleiben im Transkript belegt, wurden aber nicht zu zusätzlichen Buchformeln erweitert, wenn der Extrakt keine vollständige Eingabe-Ausgabe-Beziehung liefert.
