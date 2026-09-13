# Fachlich normalisierte Formeln — S. 513

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s513.md`  
Originaltranskript: `s513.md`  
Buchseite: Hofenbitzer, Band 1, S. 513

## HOF-B1-S513-F01 — Saumbundweite aus Saumweite

- **Fachlicher Zweck:** Saumumfang aus vier Teilstrecken bilden.
- **Quelle:** `formeln_s513.md`, Zeilen 9–9; `s513.md`, Zeile 17.

### Buchfassung
```text
- SaW = 4× 24 cm = 96 cm
```

### Formel und Rechenschritte
```text
saumweite = 4 * 24 cm = 96 cm
```

- **Ausgabe:** SaW 96 cm.
- **Eingaben:** Teilstrecke 24 cm.
- **Status:** `normalisiert`
- **Hinweis für Python:** Teilungsfaktor als explizite Konstruktionsangabe führen.

## HOF-B1-S513-F02 — Saumbundweite mit Materialdehnung

- **Fachlicher Zweck:** Saumbund wegen Materialdehnung um 8 % verkürzen.
- **Quelle:** `formeln_s513.md`, Zeilen 10–12; `s513.md`, Zeilen 18–20.

### Buchfassung
```text
- BuW = SaW · (100 % − 8 %) : 100 %
- = 96 cm · 0,92
- = 88,3 cm
```

### Formel und Rechenschritte
```text
saumbundweite = saumweite * 0,92
               = 96 cm * 0,92
               = 88,32 cm ≈ 88,3 cm
```

- **Ausgabe:** BuW 88,3 cm gedruckt.
- **Abhängigkeiten:** SaW; materialabhängiger Dehnfaktor 0,92.
- **Status:** `normalisiert`
- **Offene Fragen:** Keine Rundungsregel angegeben.

## HOF-B1-S513-F03 — Ärmelbündchenweite

- **Fachlicher Zweck:** Ärmelbündchen aus Ärmelsaumweite und 8-%-Dehnabzug bestimmen.
- **Quelle:** `formeln_s513.md`, Zeilen 22–25; `s513.md`, Zeilen 50–53.

### Buchfassung
```text
- ÄSaW = 24 cm
- BüW = ÄSaW · (100 % − 8 %) : 100 %
- = 24 cm · 0,92
- = 22,1 cm
```

### Formel und Rechenschritte
```text
aermelbuendchenweite = aermelsaumweite * 0,92
                      = 24 cm * 0,92
                      = 22,08 cm ≈ 22,1 cm
```

- **Ausgabe:** BüW 22,1 cm gedruckt.
- **Status:** `normalisiert`
- **Hinweis für Python:** Materialfaktor nicht global festschreiben.

## HOF-B1-S513-F04 — Halsbündchen-Streifenaufteilung

- **Fachlicher Zweck:** Vorderes und hinteres Halsloch in einem Bündchenstreifen mit 8-%-Abzug anordnen.
- **Quelle:** `formeln_s513.md`, Zeilen 30–31; `s513.md`, Zeilen 66–67.

### Buchfassung
```text
- Streifenaufteilung: SuN | vHlL · 0,92 | vM | vHlL · 0,92 | SuN | hHlL · 0,92 | hM | hHlL · 0,92 | SuN
- Bündchenweite (BüW) = (vHlL + hHlL) · 2 · 0,92
```

### Formel und Rechenschritte
```text
halsbuendchenweite = (vordere_halslochlaenge + hintere_halslochlaenge) * 2 * 0,92
```

- **Ausgabe:** BüW, cm; Teilstrecken vHlL·0,92 und hHlL·0,92.
- **Eingaben:** vHlL und hHlL in cm; 0,92 dimensionslos.
- **Status:** `normalisiert`
- **Hinweis für Python:** Nahtstrecken und Mittellinien als getrennte Streifenabschnitte erhalten.

## Ausgeschlossene Kandidaten

| Extraktbereich | Anzahl | Ausschlussgrund |
|---|---:|---|
| Zeile 17 | 1 | `2 × Bundbreite` ist Konstruktions-/Stückangabe ohne berechnete Ausgabe |
| **Summe** | **1** | **Konstruktionsangabe ausgeschlossen** |
