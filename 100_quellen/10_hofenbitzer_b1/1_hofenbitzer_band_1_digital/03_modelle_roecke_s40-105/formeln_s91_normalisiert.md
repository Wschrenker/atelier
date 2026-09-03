# Fachlich normalisierte Formeln — S. 91

Quelle der Normalisierung: `formeln_s91_digital_geprüft.md`
Originaltranskript: `s91_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 91
Extraktionsstand: v2

## HOF-B1-S091-F01 — Ansatzradius bei vier Kreisringen

- **Fachlicher Zweck:** Den Ansatzradius jedes der vier Kreisringe aus Ansatzweite und Nahtzugabe bestimmen.
- **Quelle:** `formeln_s91_digital_geprüft.md`, Zeilen 9, 14, 19 und 54; Originaltranskript `s91_digital_geprüft.md`, Zeilen 11, 13, 15 und 33; Buchseite 91.
- **Originalbezeichnung:** `r_AnW = (AnW + NZg) : (2 · π) : 4`
- **Normalisierte Bezeichnung:** `ansatzradius_vier_kreisringe`

### Buchfassung

```text
r_AnW = (AnW + NZg) : (2 · π) : 4
```

```text
= (118 cm + 2 cm) : (2 · 3,14) : 4
```

```text
= 4,8 cm
```

```text
- innerer Umfang = 1/4 Ansatzweite (AnW) + 2x NZg
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `ansatzweite` | AnW | 118 | cm |
| `nahtzugabe_buch` | NZg | 2 | cm |
| `anzahl_kreisringe` | `: 4` | 4 | dimensionslos |
| `pi_buch` | π, im Beispiel als 3,14 | 3,14 | dimensionslos |

### Formel und Rechenschritte

Wörtlicher Weg der gedruckten Formel:

```text
ansatzradius = ((ansatzweite + nahtzugabe_buch) / (2 * pi_buch))
                / anzahl_kreisringe
              = ((118 cm + 2 cm) / (2 * 3,14)) / 4
              = 4,7770... cm
Buchwert     = 4,8 cm
```

Wörtlicher Weg der Zeichnungsbeschriftung für einen inneren Umfang:

```text
innerer_umfang_je_ring = (ansatzweite / 4) + nahtzugabe_buch
                         = 29,5 cm + 2 cm
                         = 31,5 cm
ansatzradius_aus_label = innerer_umfang_je_ring / (2 * pi_buch)
                        = 31,5 cm / (2 * 3,14)
                        = 5,0159... cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `ansatzradius` | Radius r_AnW jedes Kreisrings | 4,8 | cm |

- **Abhängigkeiten:** `ansatzweite`, Nahtzugabe, vier Kreisringe und π.
- **Gültigkeitsbereich:** Volant aus vier Vollkreisen auf S. 91.
- **Technische Randbedingung:** Alle Längen müssen dieselbe Einheit verwenden; die Anzahl der Kreisringe muss größer als 0 sein.
- **Offene Fragen oder Widersprüche:** Die Formel teilt den einmal addierten Nahtzugabenbetrag nachträglich durch vier und verwendet rechnerisch 30 cm inneren Umfang je Ring. Die Zeichnungsbeschriftung verlangt dagegen `¼ Ansatzweite + 2x NZg`, im Buchkontext 29,5 cm + 2 cm = 31,5 cm. Beide Wege liefern nicht denselben Radius; die beabsichtigte Nahtzugabenverteilung ist ungeklärt.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis die Position der Nahtzugabenaddition relativ zur Viertelung fachlich geklärt ist.

## HOF-B1-S091-F02 — Saumradius bei vier Kreisringen

- **Fachlicher Zweck:** Den äußeren Radius jedes Kreisrings aus Ansatzradius und Volantbreite bestimmen.
- **Quelle:** `formeln_s91_digital_geprüft.md`, Zeilen 24, 29 und 34; Originaltranskript `s91_digital_geprüft.md`, Zeilen 17, 19 und 21; Buchseite 91.
- **Originalbezeichnung:** `r_SaW = r_AnW + VoB`
- **Normalisierte Bezeichnung:** `saumradius_vier_kreisringe`

### Buchfassung

```text
r_SaW = r_AnW + VoB
```

```text
= 4,8 cm + 20 cm
```

```text
= 24,8 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `ansatzradius` | r_AnW | 4,8 | cm |
| `volantbreite` | VoB | 20 | cm |

### Formel und Rechenschritte

```text
saumradius = ansatzradius + volantbreite
            = 4,8 cm + 20 cm
            = 24,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumradius` | Radius r_SaW jedes Kreisrings | 24,8 | cm |

- **Abhängigkeiten:** Gedruckter `ansatzradius` aus `HOF-B1-S091-F01` und `volantbreite`.
- **Gültigkeitsbereich:** Volant aus vier Vollkreisen auf S. 91.
- **Technische Randbedingung:** Beide Eingaben müssen nichtnegative Längen in derselben Einheit sein.
- **Offene Fragen oder Widersprüche:** Die Addition ist eindeutig und rechnerisch richtig; der zugrunde liegende Ansatzradius bleibt jedoch wegen `HOF-B1-S091-F01` fachlich gesperrt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Additionsregel separat halten, aber erst mit einem freigegebenen Ansatzradius anwenden.

## HOF-B1-S091-F03 — Gesamte Saumweite bei vier Kreisringen

- **Fachlicher Zweck:** Die gesamte äußere Saumweite des Volants aus vier Kreisringen bestimmen.
- **Quelle:** `formeln_s91_digital_geprüft.md`, Zeilen 39, 44, 49 und 55; Originaltranskript `s91_digital_geprüft.md`, Zeilen 23, 25, 27 und 34; Buchseite 91.
- **Originalbezeichnung:** `SaW = (2 · π · r_SaW) - NZg · 4`
- **Normalisierte Bezeichnung:** `saumweite_vier_kreisringe`

### Buchfassung

```text
SaW = (2 · π · r_SaW) - NZg · 4
```

```text
= (2 · 3,14 · 24,8 cm) - 2 cm · 4
```

```text
= 615 cm
```

```text
- äußerer Umfang = 1/4 Saumweite (SaW) + 2x NZg
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumradius` | r_SaW | 24,8 | cm |
| `nahtzugabe_buch` | NZg | 2 | cm |
| `anzahl_kreisringe` | vier Vollkreise | 4 | dimensionslos |
| `pi_buch` | π, im Beispiel als 3,14 | 3,14 | dimensionslos |

### Formel und Rechenschritte

Wörtlicher Weg der gedruckten Formel und Einsetzzeile:

```text
saumweite_formel = (2 * pi_buch * saumradius)
                    - (nahtzugabe_buch * anzahl_kreisringe)
                  = (2 * 3,14 * 24,8 cm) - (2 cm * 4)
                  = 147,744 cm
Gedrucktes Ergebnis = 615 cm
```

Rechenweg, der den gedruckten Ergebniswert durch Einbezug aller vier Kreisringe erklärt:

```text
saumweite_hypothese = anzahl_kreisringe * (2 * pi_buch * saumradius)
                       - (nahtzugabe_buch * anzahl_kreisringe)
                     = 4 * (2 * 3,14 * 24,8 cm) - (2 cm * 4)
                     = 614,976 cm
Gerundet            = 615 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumweite` | gesamte Saumweite SaW der vier Kreisringe | 615 | cm |

- **Abhängigkeiten:** `saumradius` aus `HOF-B1-S091-F02`, Anzahl der Kreisringe, Nahtzugabe und π.
- **Gültigkeitsbereich:** Volant aus vier Vollkreisen auf S. 91.
- **Technische Randbedingung:** Alle Längen müssen dieselbe Einheit verwenden; die Anzahl der Kreisringe muss positiv sein.
- **Offene Fragen oder Widersprüche:** Die gedruckte Formel und Einsetzzeile enthalten keinen Faktor für vier Kreisringe und ergeben wörtlich 147,744 cm statt 615 cm. Das Druckergebnis ist nur mit einem zusätzlichen Faktor 4 vor dem Kreisumfang näherungsweise erreichbar. Die genaue Nahtzugabenbehandlung bleibt dabei ungeklärt.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis der fehlende Ringfaktor und die Abzugsregel für Nahtzugaben fachlich bestätigt sind.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s91_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 60 | 1 | Isolierte Wiederholung `NZg = 2 x 1 cm = 2 cm`; bereits durch `HOF-B1-S090-F04` als Eingabeberechnung belegt |
| **Summe** | **1** | **1 wiederholte Eingabe ausgeschlossen** |
