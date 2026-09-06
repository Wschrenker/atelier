# Fachlich normalisierte Formeln — S. 90

Quelle der Normalisierung: `formeln_s90_digital_geprüft.md`
Originaltranskript: `s90_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 90
Extraktionsstand: v2

## HOF-B1-S090-F01 — Ansatzradius eines Vollkreis-Volants

- **Fachlicher Zweck:** Den inneren Radius eines Vollkreis-Volants aus seiner Ansatzweite bestimmen.
- **Quelle:** `formeln_s90_digital_geprüft.md`, Zeilen 9, 14 und 19; Originaltranskript `s90_digital_geprüft.md`, Zeilen 39, 41 und 43; Buchseite 90.
- **Originalbezeichnung:** `r_AnW = AnW : (2 · π)`
- **Normalisierte Bezeichnung:** `ansatzradius_vollkreis_volant`

### Buchfassung

```text
r_AnW = AnW : (2 · π)
```

```text
= 118 cm : (2 · 3,14)
```

```text
= 18,8 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `ansatzweite` | Ansatzweite AnW | 118 | cm |
| `pi_buch` | π, im Beispiel als 3,14 | 3,14 | dimensionslos |

### Formel und Rechenschritte

```text
ansatzradius = ansatzweite / (2 * pi_buch)
              = 118 cm / (2 * 3,14)
              = 18,7898... cm
Buchwert     = 18,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `ansatzradius` | Radius r_AnW des inneren Kreises | 18,8 | cm |

- **Abhängigkeiten:** Gemessene `ansatzweite` und der im Buchbeispiel verwendete Näherungswert 3,14 für π.
- **Gültigkeitsbereich:** Ein Volant aus einem Vollkreis auf S. 90.
- **Technische Randbedingung:** `ansatzweite` muss positiv sein; alle Längen müssen dieselbe Einheit verwenden.
- **Offene Fragen oder Widersprüche:** Der Buchwert ist auf eine Dezimalstelle gerundet; eine allgemeine Rundungsregel nennt die Quelle nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern mit einer präzisen π-Konstante rechnen; Buchreproduktion mit `3.14` und gesonderter Ausgaberundung anbieten.

## HOF-B1-S090-F02 — Saumradius eines Vollkreis-Volants

- **Fachlicher Zweck:** Den äußeren Radius aus Ansatzradius und Volantbreite bestimmen.
- **Quelle:** `formeln_s90_digital_geprüft.md`, Zeilen 24, 29 und 34; Originaltranskript `s90_digital_geprüft.md`, Zeilen 45, 47 und 49; Buchseite 90.
- **Originalbezeichnung:** `r_SaW = r_AnW + VoB`
- **Normalisierte Bezeichnung:** `saumradius_vollkreis_volant`

### Buchfassung

```text
r_SaW = r_AnW + VoB
```

```text
= 18,8 cm + 20 cm
```

```text
= 38,8 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `ansatzradius` | r_AnW | 18,8 | cm |
| `volantbreite` | VoB | 20 | cm |

### Formel und Rechenschritte

```text
saumradius = ansatzradius + volantbreite
            = 18,8 cm + 20 cm
            = 38,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumradius` | Radius r_SaW des äußeren Kreises | 38,8 | cm |

- **Abhängigkeiten:** `ansatzradius` aus `HOF-B1-S090-F01` und gewählte `volantbreite`.
- **Gültigkeitsbereich:** Vollkreis-Volant auf S. 90.
- **Technische Randbedingung:** Beide Eingaben müssen nichtnegative Längen in derselben Einheit sein.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den äußeren Radius als Summe der zwei Längen bilden; die Volantbreite nicht mit einer Umfangsweite verwechseln.

## HOF-B1-S090-F03 — Saumweite eines Vollkreis-Volants

- **Fachlicher Zweck:** Die äußere Saumweite des Vollkreis-Volants aus dem Saumradius bestimmen.
- **Quelle:** `formeln_s90_digital_geprüft.md`, Zeilen 39, 44 und 49; Originaltranskript `s90_digital_geprüft.md`, Zeilen 51, 53 und 55; Buchseite 90.
- **Originalbezeichnung:** `SaW = 2 · π · r_SaW`
- **Normalisierte Bezeichnung:** `saumweite_vollkreis_volant`

### Buchfassung

```text
SaW = 2 · π · r_SaW
```

```text
= 2 · 3,14 · 38,8 cm
```

```text
= 244 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumradius` | r_SaW | 38,8 | cm |
| `pi_buch` | π, im Beispiel als 3,14 | 3,14 | dimensionslos |

### Formel und Rechenschritte

```text
saumweite = 2 * pi_buch * saumradius
           = 2 * 3,14 * 38,8 cm
           = 243,664 cm
Buchwert  = 244 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumweite` | äußerer Umfang SaW | 244 | cm |

- **Abhängigkeiten:** `saumradius` aus `HOF-B1-S090-F02` und der verwendete π-Wert.
- **Gültigkeitsbereich:** Vollkreis-Volant auf S. 90.
- **Technische Randbedingung:** `saumradius` muss nichtnegativ sein.
- **Offene Fragen oder Widersprüche:** Der exakte Buchweg mit π = 3,14 ergibt 243,664 cm; 244 cm ist dazu gerundet. Eine allgemeine Rundungsregel nennt die Quelle nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Rechenwert und gerundeten Buchausgabewert getrennt halten.

## HOF-B1-S090-F04 — Gesamte Nahtzugabe je eingeschnittenem Kreisring

- **Fachlicher Zweck:** Die für zwei Schnittkanten benötigte gesamte Nahtzugabe bestimmen.
- **Quelle:** `formeln_s90_digital_geprüft.md`, Zeile 60; Originaltranskript `s90_digital_geprüft.md`, Zeile 67; Buchseite 90.
- **Originalbezeichnung:** `2 x 1 cm = 2 cm`
- **Normalisierte Bezeichnung:** `nahtzugabe_kreisring_gesamt`

### Buchfassung

```text
Werden mehrere Kreisringe benötigt, müssen sie in geradem Fadenlauf eingeschnitten und zusammengenäht werden. Hierfür muss zur Anssatzweite 2 mal die benötigte Nahtzugabe addiert werden, hier z.B.: 2 x 1 cm = 2 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `anzahl_schnittkanten` | 2 mal | 2 | dimensionslos |
| `nahtzugabe_je_schnittkante` | benötigte Nahtzugabe | 1 | cm |

### Formel und Rechenschritte

```text
gesamte_nahtzugabe = anzahl_schnittkanten * nahtzugabe_je_schnittkante
                     = 2 * 1 cm
                     = 2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `gesamte_nahtzugabe` | addierter Nahtzugabenbetrag für die zwei Schnittkanten | 2 | cm |

- **Abhängigkeiten:** Zwei Schnittkanten und die gewählte Nahtzugabe je Kante.
- **Gültigkeitsbereich:** Eingeschnittene und zusammengenähte Kreisringe auf S. 90; 1 cm je Kante ist der Buchbeispielwert.
- **Technische Randbedingung:** Anzahl und Einzelzugabe müssen nichtnegativ sein.
- **Offene Fragen oder Widersprüche:** Im Buchwort `Anssatzweite` steht ein zusätzliches `s`; die Buchfassung bleibt unverändert.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die gesamte Nahtzugabe aus Anzahl der Schnittkanten und Einzelzugabe berechnen, nicht als festes Maß 2 cm hinterlegen.

## HOF-B1-S090-F05 — Ansatzradius bei zwei Kreisringen

- **Fachlicher Zweck:** Den Ansatzradius jedes der zwei Kreisringe aus Ansatzweite und Nahtzugabe bestimmen.
- **Quelle:** `formeln_s90_digital_geprüft.md`, Zeilen 65, 70, 75 und 110; Originaltranskript `s90_digital_geprüft.md`, Zeilen 71, 73, 75 und 93; Buchseite 90.
- **Originalbezeichnung:** `r_AnW = (AnW + NZg) : (2 · π) : 2`
- **Normalisierte Bezeichnung:** `ansatzradius_zwei_kreisringe`

### Buchfassung

```text
r_AnW = (AnW + NZg) : (2 · π) : 2
```

```text
= (118 cm + 2 cm) : (2 · 3,14) : 2
```

```text
= 9,6 cm
```

```text
- innerer Umfang = 1/2 Ansatzweite (AnW) + 2x NZg
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `ansatzweite` | AnW | 118 | cm |
| `nahtzugabe_buch` | NZg | 2 | cm |
| `anzahl_kreisringe` | `: 2` | 2 | dimensionslos |
| `pi_buch` | π, im Beispiel als 3,14 | 3,14 | dimensionslos |

### Formel und Rechenschritte

Wörtlicher Weg der gedruckten Formel:

```text
ansatzradius = ((ansatzweite + nahtzugabe_buch) / (2 * pi_buch))
                / anzahl_kreisringe
              = ((118 cm + 2 cm) / (2 * 3,14)) / 2
              = 9,5541... cm
Buchwert     = 9,6 cm
```

Wörtlicher Weg der Zeichnungsbeschriftung für einen inneren Umfang:

```text
innerer_umfang_je_ring = (ansatzweite / 2) + nahtzugabe_buch
                         = 59 cm + 2 cm
                         = 61 cm
ansatzradius_aus_label = innerer_umfang_je_ring / (2 * pi_buch)
                        = 61 cm / (2 * 3,14)
                        = 9,7133... cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `ansatzradius` | Radius r_AnW jedes Kreisrings | 9,6 | cm |

- **Abhängigkeiten:** `ansatzweite`, Nahtzugabe, zwei Kreisringe und π.
- **Gültigkeitsbereich:** Volant aus zwei Vollkreisen auf S. 90.
- **Technische Randbedingung:** Alle Längen müssen dieselbe Einheit verwenden; die Anzahl der Kreisringe muss größer als 0 sein.
- **Offene Fragen oder Widersprüche:** Formel und Zeichnungsbeschriftung verteilen die Nahtzugabe verschieden. Die Formel teilt `(118 cm + 2 cm)` nachträglich durch 2 und verwendet damit rechnerisch 60 cm Umfang je Ring. Die Beschriftung verlangt dagegen `½ Ansatzweite + 2x NZg`, im Buchkontext 59 cm + 2 cm = 61 cm. Beide Wege liefern nicht denselben Radius; die beabsichtigte Nahtzugabenverteilung ist ungeklärt.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis geklärt ist, ob die gesamte Nahtzugabe vor oder nach der Teilung der Ansatzweite je Kreisring addiert wird.

## HOF-B1-S090-F06 — Saumradius bei zwei Kreisringen

- **Fachlicher Zweck:** Den äußeren Radius jedes Kreisrings aus Ansatzradius und Volantbreite bestimmen.
- **Quelle:** `formeln_s90_digital_geprüft.md`, Zeilen 80, 85 und 90; Originaltranskript `s90_digital_geprüft.md`, Zeilen 77, 79 und 81; Buchseite 90.
- **Originalbezeichnung:** `r_SaW = r_AnW + VoB`
- **Normalisierte Bezeichnung:** `saumradius_zwei_kreisringe`

### Buchfassung

```text
r_SaW = r_AnW + VoB
```

```text
= 9,6 cm + 20 cm
```

```text
= 29,6 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `ansatzradius` | r_AnW | 9,6 | cm |
| `volantbreite` | VoB | 20 | cm |

### Formel und Rechenschritte

```text
saumradius = ansatzradius + volantbreite
            = 9,6 cm + 20 cm
            = 29,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumradius` | Radius r_SaW jedes Kreisrings | 29,6 | cm |

- **Abhängigkeiten:** Gedruckter `ansatzradius` aus `HOF-B1-S090-F05` und `volantbreite`.
- **Gültigkeitsbereich:** Volant aus zwei Vollkreisen auf S. 90.
- **Technische Randbedingung:** Beide Eingaben müssen nichtnegative Längen in derselben Einheit sein.
- **Offene Fragen oder Widersprüche:** Die Addition ist eindeutig und rechnerisch richtig; der zugrunde liegende Ansatzradius bleibt jedoch wegen `HOF-B1-S090-F05` fachlich gesperrt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Additionsregel kann separat implementiert werden, darf aber erst nach Freigabe eines gültigen Ansatzradius ausgeführt werden.

## HOF-B1-S090-F07 — Gesamte Saumweite bei zwei Kreisringen

- **Fachlicher Zweck:** Die gesamte äußere Saumweite des Volants aus zwei Kreisringen bestimmen.
- **Quelle:** `formeln_s90_digital_geprüft.md`, Zeilen 95, 100, 105 und 111; Originaltranskript `s90_digital_geprüft.md`, Zeilen 83, 85, 87 und 94; Buchseite 90.
- **Originalbezeichnung:** `SaW = (2 · π · r_SaW) - NZg · 2`
- **Normalisierte Bezeichnung:** `saumweite_zwei_kreisringe`

### Buchfassung

```text
SaW = (2 · π · r_SaW) - NZg · 2
```

```text
= (2 · 3,14 · 29,6 cm) - 2 cm · 2
```

```text
= 368 cm
```

```text
- äußerer Umfang = 1/2 Saumweite (SaW) + 2x NZg
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumradius` | r_SaW | 29,6 | cm |
| `nahtzugabe_buch` | NZg | 2 | cm |
| `anzahl_kreisringe` | zwei Vollkreise | 2 | dimensionslos |
| `pi_buch` | π, im Beispiel als 3,14 | 3,14 | dimensionslos |

### Formel und Rechenschritte

Wörtlicher Weg der gedruckten Formel und Einsetzzeile:

```text
saumweite_formel = (2 * pi_buch * saumradius)
                    - (nahtzugabe_buch * anzahl_kreisringe)
                  = (2 * 3,14 * 29,6 cm) - (2 cm * 2)
                  = 181,888 cm
Gedrucktes Ergebnis = 368 cm
```

Rechenweg, der den gedruckten Ergebniswert durch Einbezug beider Kreisringe näherungsweise erklärt:

```text
saumweite_hypothese = anzahl_kreisringe * (2 * pi_buch * saumradius)
                       - (nahtzugabe_buch * anzahl_kreisringe)
                     = 2 * (2 * 3,14 * 29,6 cm) - (2 cm * 2)
                     = 367,776 cm
Gerundet            = 368 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumweite` | gesamte Saumweite SaW der zwei Kreisringe | 368 | cm |

- **Abhängigkeiten:** `saumradius` aus `HOF-B1-S090-F06`, Anzahl der Kreisringe, Nahtzugabe und π.
- **Gültigkeitsbereich:** Volant aus zwei Vollkreisen auf S. 90.
- **Technische Randbedingung:** Alle Längen müssen dieselbe Einheit verwenden; die Anzahl der Kreisringe muss positiv sein.
- **Offene Fragen oder Widersprüche:** Die gedruckte Formel und Einsetzzeile enthalten keinen Faktor für zwei Kreisringe und ergeben wörtlich 181,888 cm statt 368 cm. Das Druckergebnis ist nur mit einem zusätzlichen Faktor 2 vor dem Kreisumfang näherungsweise erreichbar. Die Zeichnungsbeschriftung belegt zwei äußere Halbanteile, löst aber die genaue Nahtzugabenbehandlung nicht eindeutig.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis der fehlende Ringfaktor und die Abzugsregel für Nahtzugaben fachlich bestätigt sind.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s90_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 54–55 | 2 | Direkte Umfangs-/Begriffslabels des Vollkreises; die zugehörigen Rechenbeziehungen sind bereits in `HOF-B1-S090-F01` und `HOF-B1-S090-F03` vollständig belegt |
| Zeile 116 | 1 | Wiederholte isolierte Nahtzugaben-Zuweisung `NZg = 2 x 1 cm = 2 cm`; bereits vollständig in `HOF-B1-S090-F04` abgebildet |
| **Summe** | **3** | **2 wiederholte Labels und 1 wiederholte Eingabe ausgeschlossen** |
