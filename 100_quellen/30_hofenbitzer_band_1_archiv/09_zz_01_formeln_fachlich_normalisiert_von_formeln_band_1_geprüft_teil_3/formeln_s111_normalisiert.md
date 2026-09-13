# Fachlich normalisierte Formeln — S. 111

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s111.md`
Originaltranskript: `s111.md`
Buchseite: Hofenbitzer, Band 1, S. 111

## HOF-B1-S111-F01 — Vorderer Hosenausschnitt nach Figurform

- **Fachlicher Zweck:** Den Abtrag für den vorderen Hosenausschnitt aus der Vorderhosenbreite und der gewählten Figurvariante bestimmen.
- **Quelle:** `formeln_s111.md`, Zeilen 9, 14 und 19; Originaltranskript `s111.md`, Zeilen 9, 17 und 21; Buchseite 111.
- **Originalbezeichnung:** `vHoB : 4` mit figurabhängigen Abzügen oder Zuschlägen.
- **Normalisierte Bezeichnung:** `vorderer_hosenausschnitt_nach_figurform`

### Buchfassung

```text
10. □2 Von P8 aus die Hüftlinie nach rechts verlängern und vHoB : 4 − 0 bis −0,5 cm abtragen.
```

```text
vHoB : 4 − 0,5 bis −1 cm
```

```text
vHoB : 4 + 0 bis +0,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderhosenbreite` | vHoB | variabel | cm |
| `figurvariante` | normal; breite Hüften/flaches Gesäß; schmale Hüften/starkes Gesäß | explizite Auswahl | dimensionslos |
| `ausschnitt_anpassung` | figurabhängiger Bereich | explizite Auswahl | cm |

### Formel und Rechenschritte

```text
basisabtrag = vorderhosenbreite / 4
abtrag_vorderer_hosenausschnitt = basisabtrag + ausschnitt_anpassung

Normal proportioniert: -0,5 cm <= ausschnitt_anpassung <= 0 cm
Breite Hüften, flaches Gesäß: -1 cm <= ausschnitt_anpassung <= -0,5 cm
Schmale Hüften, starkes Gesäß: 0 cm <= ausschnitt_anpassung <= 0,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abtrag_vorderer_hosenausschnitt` | von P8 auf der verlängerten Hüftlinie abzutragender Wert | cm |

- **Abhängigkeiten:** vHoB und ausdrücklich gewählte Figurvariante samt Wert innerhalb ihres Bereichs.
- **Gültigkeitsbereich:** Vorderhose des Standardhosen-Grundschnitts auf S. 111.
- **Technische Randbedingung:** Die gedruckten Schreibungen `− 0 bis −0,5` und `− 0,5 bis −1` werden als signierte Anpassungsbereiche modelliert; die Auswahl wird nicht automatisiert.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine Schwellenwerte für die Figurklassifikation und keine Auswahlregel innerhalb der Bereiche.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Figurvariante und signierten Anpassungswert getrennt validieren; keine anthropometrische Klassifikation erfinden.

## HOF-B1-S111-F02 — Halbe Hosenbeinweite an der Saumlinie

- **Fachlicher Zweck:** Den beidseitig vom Vorderhosenbruch abzutragenden Saumabstand aus der gesamten Saumweite bestimmen.
- **Quelle:** `formeln_s111.md`, Zeile 29; Originaltranskript `s111.md`, Zeile 29; Buchseite 111.
- **Originalbezeichnung:** `SaW : 4 − 1 cm`.
- **Normalisierte Bezeichnung:** `saumabstand_vorderhose`

### Buchfassung

```text
15./16. Von P12 aus SaW : 4 − 1 cm nach rechts und nach links abtragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `saumweite` | SaW | variabel | cm |
| `saum_abzug` | `1 cm` | 1 | cm |

### Formel und Rechenschritte

```text
saumabstand_je_seite = (saumweite / 4) - 1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `saumabstand_je_seite` | Abstand von P12 nach rechts und nach links | cm |

- **Abhängigkeiten:** Gewählte SaW und Punkt P12 auf dem Vorderhosenbruch.
- **Gültigkeitsbereich:** Vorderhose des Standardhosen-Grundschnitts auf S. 111.
- **Technische Randbedingung:** Derselbe berechnete Betrag wird symmetrisch in beide Richtungen abgetragen.
- **Offene Fragen oder Widersprüche:** Keine; die Seite enthält kein ausgefülltes Ergebnis.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einen Betrag berechnen und geometrisch mit entgegengesetzten Richtungsvektoren anwenden.

## Ausgeschlossene Kandidaten

| Extraktzeilen | Anzahl | Ausschlussgrund |
|---|---:|---|
| 24 und 39 | 2 | Gleichsetzung von Vorderhosenbruch, Bügelkante und Fadenlauf; geometrische Begriffsdefinition ohne skalare Berechnung |
| 34 | 1 | Wiederholtes Zeichnungslabel der in Zeile 9 vollständig erhaltenen Beziehung |
| 44 | 1 | Wiederholtes Zeichnungslabel der in Zeile 29 vollständig erhaltenen Beziehung |
| **Summe** | **4** | **2 Definitionen + 2 Wiederholungen** |
