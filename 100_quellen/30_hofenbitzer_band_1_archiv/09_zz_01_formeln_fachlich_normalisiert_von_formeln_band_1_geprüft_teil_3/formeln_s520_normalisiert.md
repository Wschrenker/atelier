# Fachlich normalisierte Formeln — S. 520

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s520.md`  
Originaltranskript: `s520.md`  
Buchseite: Hofenbitzer, Band 1, S. 520

Die Seite zeigt den engen Ärmel für den weitenreduzierten Oberteil-Grundschnitt. Der Ärmel wird weiten-, aber nicht längenreduziert; die Einhalteweite ist null.

## HOF-B1-S520-F01 — Oberarmweite mit Weitenreduzierung

- **Fachlicher Zweck:** Die Oberarmweite aus dem Oberarmumfang und der angegebenen Reduktion bestimmen.
- **Quelle:** `formeln_s520.md`, Zeile 20; Originaltranskript `s520.md`, Zeile 62; Buchseite 520.
- **Originalbezeichnung:** `OaU 25 + −3 % = OaW 27,2`.
- **Normalisierte Bezeichnung:** `reduzierte_oberarmweite`

### Buchfassung
```text
OaU 25 + −3 % = OaW 27,2
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `oberarmumfang` | OaU | 25 | cm |
| `weitenreduzierung` | −3 % | −3 | Prozent |

### Formel und Rechenschritte
```text
oberarmweite = oberarmumfang * (1 - 0,03)
              = 25 cm * 0,97
              = 24,25 cm
```

### Ausgabe
`oberarmweite` — OaW, gedruckt 27,2 cm.

- **Abhängigkeiten:** OaU und Reduktionsfaktor.
- **Gültigkeitsbereich:** Damenärmel, Größe 38, enger Ärmel.
- **Offene Fragen oder Widersprüche:** **Widerspruch.** Die technische Rechnung ergibt 24,25 cm, der Buchwert 27,2 cm. Die Quelle bestätigt, dass die Zeile so im Druck steht; ein korrigierter Wert wird nicht erfunden.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Den gedruckten Wert nicht als erwartetes Rechenergebnis implementieren. Vor einer Umsetzung Quellen- oder Fachentscheidung einholen.

## HOF-B1-S520-F02 — Ärmelsaumweite aus Handgelenkumfang

- **Fachlicher Zweck:** Die Ärmelsaumweite aus dem Handgelenkumfang ohne zusätzliche Zugabe bestimmen.
- **Quelle:** `formeln_s520.md`, Zeile 14; Originaltranskript `s520.md`, Zeile 38; Buchseite 520.
- **Originalbezeichnung:** `HgU 16 + 0 = ÄSaW 16`.
- **Normalisierte Bezeichnung:** `aermelsaumweite_aus_handgelenkumfang`

### Buchfassung
```text
HgU | Handgelenkumfang | 16 + 0 | Saumweite ÄSaW 16
```

### Formel und Rechenschritte
```text
aermelsaumweite = handgelenkumfang + saumeinhalteweite
                 = 16 cm + 0 cm
                 = 16 cm
```

### Ausgabe
`aermelsaumweite` — ÄSaW, 16 cm.

- **Abhängigkeiten:** HgU.
- **Gültigkeitsbereich:** Enger Ärmel-Grundschnitt.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Saumeinhalteweite als optionalen Parameter mit Default 0 führen, nicht als globale Regel.

## HOF-B1-S520-F03 — Einhalteweite und Ärmelkugellinie

- **Fachlicher Zweck:** Bei nullprozentiger Einhalteweite die Einhalteweite in cm und den Ärmelkugelumfang bestimmen.
- **Quelle:** `formeln_s520.md`, Zeile 15; Originaltranskript `s520.md`, Zeile 39; Buchseite 520.
- **Originalbezeichnung:** `Einhalteweite in cm = AlU · Einhalteweite in % = EW in cm 0 cm`; `ÄKU = AlU + Einhalteweite in cm`.
- **Normalisierte Bezeichnung:** `aermelkugelumfang_ohne_einhalteweite`

### Buchfassung
```text
EW in % | Einhalteweite in % | 0 % | Einhalteweite in cm = AlU · Einhalteweite in % = EW in cm 0 cm
Ärmelkugelumfang | AlU + Einhalteweite in cm | ÄKU 39,1
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `armlochumfang` | AlU | 39,1 | cm |
| `einhalteweite_prozent` | EW in % | 0 | Prozent |

### Formel und Rechenschritte
```text
einhalteweite = armlochumfang * einhalteweite_prozent
               = 39,1 cm * 0,00
               = 0 cm

aermelkugelumfang = armlochumfang + einhalteweite
                   = 39,1 cm + 0 cm
                   = 39,1 cm
```

### Ausgabe
`einhalteweite` — 0 cm; `aermelkugelumfang` — ÄKU, 39,1 cm.

- **Abhängigkeiten:** AlU und EW in %.
- **Gültigkeitsbereich:** Enger weitenreduzierter Ärmel ohne Einhalteweite.
- **Offene Fragen oder Widersprüche:** Die Schreibweise der Buchzeile ist redaktionell verdichtet; die anschließende ÄKU-Zeile bestätigt die additive Beziehung. Eine andere Prozentwahl ist allgemeiner Seitenkontext, nicht Teil dieses eingesetzten Beispiels.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Prozentwerte vor der Multiplikation in Dezimalfaktoren umwandeln; ÄKU aus dem tatsächlich berechneten Wert bilden.

## Ausgeschlossene Kandidaten

| Extraktbereich | Anzahl | Ausschlussgrund |
|---|---:|---|
| Zeile 20, Anmerkung | 1 | Die Buchanmerkung bestätigt einen rechnerischen Widerspruch der OaU/OaW-Zeile; sie ist kein zusätzlicher Formelblock. Der Widerspruch ist in F01 dokumentiert. |
| **Summe** | **1** | **Redaktionelle Prüfnotiz ausgeschlossen** |

### Prüfhinweise

1. Die beiden unstrittigen Rechnungen sind `16 + 0 = 16 cm` und bei `0 %` Einhalteweite `39,1 · 0 = 0 cm`, anschließend `39,1 + 0 = 39,1 cm`.
2. Die Seite sagt ausdrücklich, dass der enge Ärmel weiten-, aber nicht längenreduziert wird und keine Einhalteweite besitzt. Diese qualitative Bedingung stützt F03, ersetzt aber keine zusätzliche Formel.
