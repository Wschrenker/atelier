# Fachlich normalisierte Formeln — S. 519

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s519.md`  
Originaltranskript: `s519.md`  
Buchseite: Hofenbitzer, Band 1, S. 519

Die Seite zeigt den weitenreduzierten engen Oberteil-Grundschnitt für Herren. Die Tabelle verwendet denselben Reduktionsfaktor wie S. 518, führt aber einen eigenen Maßsatz.

## HOF-B1-S519-F01 — Reduzierte halbe Rückenbreite

- **Fachlicher Zweck:** Die halbe Rückenbreite um 7 % reduzieren.
- **Quelle:** `formeln_s519.md`, Zeile 17; Originaltranskript `s519.md`, Zeile 57; Buchseite 519.
- **Originalbezeichnung:** `RüB + −7 % = RüB+ 18,6`.
- **Normalisierte Bezeichnung:** `reduzierte_rueckenbreite_halb_herren`

### Buchfassung
```text
RüB | Rückenbreite (½) | 20 | + −7 % | RüB+ 18,6
```

### Formel und Rechenschritte
```text
reduzierte_rueckenbreite_halb = 20 cm * 0,93 = 18,6 cm
```

### Ausgabe
`reduzierte_rueckenbreite_halb` — RüB+, 18,6 cm.

- **Abhängigkeiten:** RüB und Weitenreduzierung 7 %.
- **Gültigkeitsbereich:** Herren, Größe 50, enger Oberteil-Grundschnitt.
- **Offene Fragen oder Widersprüche:** Keine rechnerische; Rundungsregel fehlt allgemein.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Faktor als Parameter der Materialdehnung führen.

## HOF-B1-S519-F02 — Reduzierter Armdurchmesser und Viertelwert

- **Fachlicher Zweck:** Armdurchmesser reduzieren und den Viertelwert bestimmen.
- **Quelle:** `formeln_s519.md`, Zeile 18; Originaltranskript `s519.md`, Zeile 58; Buchseite 519.
- **Originalbezeichnung:** `ArD + −7 % = ArD+ 10,7; ¼ 2,7; 3,6`.
- **Normalisierte Bezeichnung:** `reduzierter_armdurchmesser_herren`

### Buchfassung
```text
ArD | Armdurchmesser | 11,5 | + −7 % | ArD+ 10,7; ¼ 2,7; 3,6
```

### Formel und Rechenschritte
```text
armdurchmesser_reduziert = 11,5 cm * 0,93 = 10,695 cm ≈ 10,7 cm
viertel_armdurchmesser = 10,695 cm / 4 = 2,67375 cm ≈ 2,7 cm
```

### Ausgabe
`armdurchmesser_reduziert` — ArD+, 10,7 cm; `viertel_armdurchmesser` — 2,7 cm.

- **Abhängigkeiten:** ArD.
- **Gültigkeitsbereich:** Herren-Grundschnitt ohne Brustabnäher.
- **Offene Fragen oder Widersprüche:** Der zusätzliche Druckwert `3,6` ist keiner benannten Teilung eindeutig zugeordnet.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nur den eindeutig benannten Viertelwert implementieren; die Teilungsposition des Werts 3,6 nicht erraten.

## HOF-B1-S519-F03 — Reduzierte halbe Brustbreite

- **Fachlicher Zweck:** Die halbe Brustbreite um 7 % reduzieren.
- **Quelle:** `formeln_s519.md`, Zeile 19; Originaltranskript `s519.md`, Zeile 59; Buchseite 519.
- **Originalbezeichnung:** `BrB + −7 % = BrB+ 17,2`.
- **Normalisierte Bezeichnung:** `reduzierte_brustbreite_halb_herren`

### Buchfassung
```text
BrB | Brustbreite (½) | 18,5 | + −7 % | BrB+ 17,2
```

### Formel und Rechenschritte
```text
reduzierte_brustbreite_halb = 18,5 cm * 0,93
                             = 17,205 cm ≈ 17,2 cm
```

### Ausgabe
`reduzierte_brustbreite_halb` — BrB+, 17,2 cm.

- **Abhängigkeiten:** BrB.
- **Gültigkeitsbereich:** Herren, Größe 50.
- **Offene Fragen oder Widersprüche:** Keine rechnerische; Rundungsregel fehlt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Gedruckten Wert nur als Darstellung führen.

## HOF-B1-S519-F04 — Kontrollwert der reduzierten halben Brustweite

- **Fachlicher Zweck:** Die halbe Brustumfangskontrolle um 7 % reduzieren.
- **Quelle:** `formeln_s519.md`, Zeile 20; Originaltranskript `s519.md`, Zeile 60; Buchseite 519.
- **Originalbezeichnung:** `Σ = ½ BrU`; `½ BrW 46,5`.
- **Normalisierte Bezeichnung:** `reduzierte_halbe_brustweite_kontrolle_herren`

### Buchfassung
```text
Kontrolle | Σ = ½ BrU | 50 | + −7 % | ½ BrW 46,5
```

### Formel und Rechenschritte
```text
reduzierte_halbe_brustweite = 50 cm * 0,93 = 46,5 cm
```

### Ausgabe
`reduzierte_halbe_brustweite` — ½ BrW, 46,5 cm.

- **Abhängigkeiten:** ½ BrU.
- **Gültigkeitsbereich:** Kontrollzeile der Herrenkonstruktion.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Summenkontrolle über die reduzierten Breiten verwenden.

## HOF-B1-S519-F05 — Unvollständige Balance-Differenz

- **Fachlicher Zweck:** Die auf der Seite vorgesehene Balance-Differenz dokumentieren.
- **Quelle:** `formeln_s519.md`, Zeile 25; Originaltranskript `s519.md`, Zeile 71; Buchseite 519.
- **Originalbezeichnung:** `VL − RüL`.
- **Normalisierte Bezeichnung:** `individuelle_balance_herren`

### Buchfassung
```text
Differenz VL − RüL | individuelle Balance | --- | korrigierte Balance | ---
```

### Ausgabe
Keine, da beide Eingabewerte und das Ergebnis fehlen.

- **Abhängigkeiten:** VL und RüL.
- **Gültigkeitsbereich:** Herren, Größe 50.
- **Offene Fragen oder Widersprüche:** Die Buchfassung enthält nur Leerstriche. Eine Berechnung oder ein Beispielwert darf nicht ergänzt werden.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Erst nach Vorliegen der Werte berechnen; keine Defaultwerte verwenden.

## Ausgeschlossene Kandidaten

| Extraktbereich | Anzahl | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Halsloch-, Schulterwinkel- und Schulternahtangaben ohne vollständige Rechenzeile; die im Block enthaltene hSuNL-Beziehung ist nicht mit einem eingesetzten Wert belegt. |
| Zeile 10 | 1 | Armlochpositionen und Teilungsbereiche; der Druckwert `3,6` bleibt mangels eindeutiger Zuordnung in F02 offen. |
| Zeile 11 | 1 | Taillenweiten-/Ausfallbeschriftungen ohne vollständige Eingabe-Ausgabe-Beziehung. |
| Zeile 12 | 1 | Hüftbreiten-, Fehlbetrags- und Reduktionsbeschriftungen ohne vollständige Rechenzeile im Extrakt. |
| **Summe** | **4** | **Bereiche, Konstruktionslabels und unvollständige Beziehungen ausgeschlossen** |

### Prüfhinweise

1. `20 · 0,93 = 18,6`, `11,5 · 0,93 = 10,695 ≈ 10,7`, `18,5 · 0,93 = 17,205 ≈ 17,2` und `50 · 0,93 = 46,5 cm` sind rechnerisch konsistent.
2. Die Herrentabelle enthält bei `AlT 23,4 + −3 % = AlT+ 22,6` den passenden Kontext zum Buchwiderspruch auf S. 518: `23,4 · 0,97 = 22,698 ≈ 22,6`. Das bestätigt nicht die fehlerhafte Damenzeile auf S. 518, sondern bleibt ein separater Tabellenbeleg.
3. Eine Längenreduzierung von `0 bis ca. 5 %` ist allgemeiner Seitenkontext und im Extrakt keine eigenständige Rechenzeile.
