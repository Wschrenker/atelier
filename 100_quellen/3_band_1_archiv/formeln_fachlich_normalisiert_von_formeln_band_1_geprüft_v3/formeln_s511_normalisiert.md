# Fachlich normalisierte Formeln — S. 511

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s511.md`  
Originaltranskript: `s511.md`  
Buchseite: Hofenbitzer, Band 1, S. 511

## HOF-B1-S511-F01 — Ausschnittumfang

- **Fachlicher Zweck:** Umfang des gesamten runden Ausschnitts aus vorderer und hinterer Ausschnittlänge bestimmen.
- **Quelle:** `formeln_s511.md`, Zeilen 9–10; Originaltranskript `s511.md`, Zeilen 21–22.
- **Originalbezeichnung:** `AusU = 2× (vAusL + hAusL)`; `AusU = 42,4 cm`.
- **Normalisierte Bezeichnung:** `ausschnittumfang`

### Buchfassung
```text
- AusU = 2× (vAusL + hAusL)
- AusU = 42,4 cm
```

### Eingaben
`vordere_ausschnittlaenge` — vAusL, 12,5 cm; `hintere_ausschnittlaenge` — hAusL, 10,2 cm.

### Formel und Rechenschritte
```text
ausschnittumfang = 2 * (vordere_ausschnittlaenge + hintere_ausschnittlaenge)
                  = 2 * (12,5 cm + 10,2 cm)
                  = 45,4 cm
```

### Ausgabe
`ausschnittumfang` — AusU, technisch 45,4 cm; gedruckt 42,4 cm.

- **Abhängigkeiten:** vAusL und hAusL.
- **Gültigkeitsbereich:** Rund ausgeformter T-Shirt-Ausschnitt.
- **Offene Fragen oder Widersprüche:** Die Buchrechnung `2 × (12,5 + 10,2)` ergibt 45,4 cm, nicht den gedruckten Wert 42,4 cm. Die Quelle dokumentiert den Widerspruch ausdrücklich.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis der gedruckte Wert oder die zugrunde liegende Ausschnittlänge geklärt ist.

## HOF-B1-S511-F02 — Bündchenweite aus Ausschnittumfang

- **Fachlicher Zweck:** Bündchenstreifen wegen Materialdehnung um 8 % verkürzen.
- **Quelle:** `formeln_s511.md`, Zeilen 15–17; Originaltranskript `s511.md`, Zeilen 26–28.
- **Originalbezeichnung:** `= AusW · (100 % − 8 %) : 100 %`; `= 45,4 cm · 0,92`; `= 41,8 cm`.
- **Normalisierte Bezeichnung:** `buendchenweite_ausschnitt`

### Buchfassung
```text
- = AusW · (100 % − 8 %) : 100 %
- = 45,4 cm · 0,92
- = 41,8 cm
```

### Eingaben
`ausschnittumfang_fuer_buendchen` — AusW, 45,4 cm; `dehnfaktor` — 0,92, dimensionslos.

### Formel und Rechenschritte
```text
buendchenweite = ausschnittumfang_fuer_buendchen * 0,92
                = 45,4 cm * 0,92
                = 41,768 cm ≈ 41,8 cm
```

### Ausgabe
`buendchenweite` — BüW, 41,8 cm gedruckt.

- **Abhängigkeiten:** Ausschnittumfang und materialabhängiger Dehnfaktor.
- **Gültigkeitsbereich:** Halsbündchen aus dehnbarem Material.
- **Offene Fragen oder Widersprüche:** Die Folgeformel verwendet `AusW` und 45,4 cm, während die vorherige Zeile `AusU = 42,4 cm` nennt. Beide Buchangaben bleiben getrennt erhalten.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den verwendeten Umfang als Eingabe führen; keinen Widerspruch automatisch auflösen.

## Ausgeschlossene Kandidaten

| Extraktbereich | Anzahl | Ausschlussgrund |
|---|---:|---|
| Zeile 22 | 1 | Redaktionelle Widerspruchsnotiz; kein zusätzlicher Formelblock |
| Zeilen 27, 32–33, 38, 43, 48, 53 | 6 | Produktionsschnittteile, direkte Mess-/Eingabewerte und Stückzahlangaben ohne eigene Berechnung |
| **Summe** | **7** | **Prüfnotiz, Produktionsangaben und Eingabewerte ausgeschlossen** |

### Prüfhinweis
Die Abweichung `42,4 cm`/`45,4 cm` ist ein Quellenwiderspruch. Die technische Rechnung und der gedruckte Wert werden nicht vermischt.
