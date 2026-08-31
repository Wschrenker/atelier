# Fachlich normalisierte Formeln — S. 116

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/formeln_s116.md`
Originaltranskript: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/s116.md`
Buchseite: Hofenbitzer, Band 1, S. 116

## HOF-B1-S116-F01 — Hintere Taillenlinienlänge mit Abnäherinhalt

- **Fachlicher Zweck:** Den auf der hinteren Taillenlinie abzutragenden Betrag aus einem Viertel des Taillenumfangs, dem Abnäherinhalt und gegebenenfalls Einhalteweite bestimmen.
- **Quelle:** `formeln_s116.md`, Zeile 9; Originaltranskript `s116.md`, Zeile 15; Buchseite 116.
- **Originalbezeichnung:** `TaU : 4 + Abnäherinhalt + ggf. Einhalteweite`
- **Normalisierte Bezeichnung:** `hintere_taillenlinienlaenge`

### Buchfassung

```text
Von P34 aus TaU : 4 + Abnäherinhalt + ggf. Einhalteweite auf der hinteren Taillenlinie abtragen. Auf der Hälfte zwischen P27 und P28 die Abnähermitte zur Taille abwinkeln und von oben 13 bis 15 cm lang die Abnäherlänge nach unten abtragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | nicht angegeben | cm |
| `abnaeherinhalt_hinten` | Abnäherinhalt | nicht angegeben | cm |
| `einhalteweite_hinten` | ggf. Einhalteweite | optional, nicht angegeben | cm |

### Formel und Rechenschritte

```text
hintere_taillenlinienlaenge = (taillenumfang / 4)
                               + abnaeherinhalt_hinten
                               + einhalteweite_hinten
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hintere_taillenlinienlaenge` | Von P34 auf der hinteren Taillenlinie abzutragender Betrag | nicht angegeben | cm |

- **Abhängigkeiten:** Taillenumfang, zuvor bestimmter hinterer Abnäherinhalt und gegebenenfalls gewählte Einhalteweite.
- **Gültigkeitsbereich:** Standardhose, Variante 1 zur Bestimmung des hinteren Abnähers und Hüftbogens auf S. 116.
- **Technische Randbedingung:** Ohne Einhalteweite ist technisch `einhalteweite_hinten = 0 cm` anzusetzen; alle Längen müssen dieselbe Einheit tragen.
- **Offene Fragen oder Widersprüche:** Keine in der Rechenbeziehung. Der Zahlenbereich für den Abnäherinhalt steht nur im wiederholenden Zeichnungslabel und ist kein allgemeiner Festwert dieser Formel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den optionalen Summanden explizit mit dem Standardwert `0 cm` führen; die Abnäherlänge von 13 bis 15 cm ist eine getrennte Konstruktionsvorgabe.

## HOF-B1-S116-F02 — Hinterer Abnäherinhalt aus Bundnahtmessungen

- **Fachlicher Zweck:** Den hinteren Abnäherinhalt aus der gemessenen hinteren Strecke, der gemessenen vorderen Bundnaht und dem halben Taillenumfang bestimmen.
- **Quelle:** `formeln_s116.md`, Zeile 14; Originaltranskript `s116.md`, Zeile 25; Buchseite 116.
- **Originalbezeichnung:** `Abstand zwischen P34 und P35 + vordere Bundnaht − ½ TaU = Abnäherinhalt`
- **Normalisierte Bezeichnung:** `hinterer_abnaeherinhalt_variante_2`

### Buchfassung

```text
Abstand zwischen P34 und P35 messen, die gemessene vordere Bundnaht (siehe Seite 113, □4) addieren, minus ½ TaU = Abnäherinhalt
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `abstand_p34_p35` | Abstand zwischen P34 und P35 | nicht angegeben | cm |
| `vordere_bundnahtlaenge` | gemessene vordere Bundnaht | nicht angegeben | cm |
| `taillenumfang` | TaU | nicht angegeben | cm |

### Formel und Rechenschritte

```text
hinterer_abnaeherinhalt = abstand_p34_p35
                           + vordere_bundnahtlaenge
                           - (taillenumfang / 2)
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hinterer_abnaeherinhalt` | Abnäherinhalt der Hinterhose | nicht angegeben | cm |

- **Abhängigkeiten:** Gemessene Strecke P34–P35, gemessene vordere Bundnaht nach S. 113 und Taillenumfang.
- **Gültigkeitsbereich:** Standardhose, Variante 2 mit übertragenen Vorderhosenmessungen auf S. 116.
- **Technische Randbedingung:** Beide Nahtmessungen müssen entlang der bezeichneten Nahtverläufe und in derselben Einheit wie der Taillenumfang vorliegen.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Messwerte samt Messpfad speichern; die Formel erst nach dem Formen beziehungsweise Festlegen der betreffenden Bundnahtabschnitte ausführen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s116.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 19 | 1 | Zeichnungslabel mit Wiederholung von `TaU : 4 + Abnäherinhalt` und einem beispielhaften Abnäherbereich; keine zusätzliche Formel neben `HOF-B1-S116-F01` |
| **Summe** | **1** | **1 Wiederholung ausgeschlossen** |
