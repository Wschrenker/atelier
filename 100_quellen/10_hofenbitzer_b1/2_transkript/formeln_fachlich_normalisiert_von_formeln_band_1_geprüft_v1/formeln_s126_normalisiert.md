# Fachlich normalisierte Formeln — S. 126

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/formeln_s126.md`
Originaltranskript: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/s126.md`
Buchseite: Hofenbitzer, Band 1, S. 126

## HOF-B1-S126-F01 — Hinterer Hosenausschnitt der engen Hose

- **Fachlicher Zweck:** Den normalen hinteren Hosenausschnitt der engen Hose aus der Hinterhosenbreite bestimmen.
- **Quelle:** `formeln_s126.md`, Zeile 9; Originaltranskript `s126.md`, Zeile 16; Buchseite 126.
- **Originalbezeichnung:** `hHoB : 4 + 0,5 bis 1 cm`
- **Normalisierte Bezeichnung:** `hinterer_hosenausschnitt_enge_hose`

### Buchfassung

```text
25. Von P24 aus hHoB : 4 + 0,5 bis 1 cm nach rechts abtragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hinterhosenbreite` | hHoB | 25,2 | cm |
| `zuschlag` | 0,5 bis 1 | wählbar | cm |

### Formel und Rechenschritte

```text
hinterer_hosenausschnitt_min = (hinterhosenbreite / 4) + 0,5 cm
                              = (25,2 cm / 4) + 0,5 cm
                              = 6,8 cm
hinterer_hosenausschnitt_max = (hinterhosenbreite / 4) + 1 cm
                              = 7,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hinterer_hosenausschnitt` | Abtrag von P24 nach rechts | 6,8 bis 7,3 | cm |

- **Abhängigkeiten:** Hinterhosenbreite `hHoB` aus `HOF-B1-S120-F05` beziehungsweise der wiederholten Tabelle auf S. 124.
- **Gültigkeitsbereich:** Enge Hose ohne abweichende Gesäßform.
- **Technische Randbedingung:** Zuschlag innerhalb des belegten Bereichs wählen.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Gewählten Zuschlag mit der Figurvariante speichern.

## HOF-B1-S126-F02 — Hinterer Hosenausschnitt bei starkem Gesäß

- **Fachlicher Zweck:** Den größeren hinteren Hosenausschnitt für eine Figur mit starkem Gesäß bestimmen.
- **Quelle:** `formeln_s126.md`, Zeile 14; Originaltranskript `s126.md`, Zeilen 20–22; Buchseite 126.
- **Originalbezeichnung:** `hHoB : 4 − 0,5 bis −1 cm`
- **Normalisierte Bezeichnung:** `hinterer_hosenausschnitt_starkes_gesaess`

### Buchfassung

```text
hHoB : 4 − 0,5 bis −1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hinterhosenbreite` | hHoB | 25,2 | cm |
| `abzug` | 0,5 bis 1 | wählbar | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_max = (hinterhosenbreite / 4) - 0,5 cm
                     = 5,8 cm
hosenausschnitt_min = (hinterhosenbreite / 4) - 1 cm
                     = 5,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hinterer_hosenausschnitt` | figurabhängiger Abtrag | 5,3 bis 5,8 | cm |

- **Abhängigkeiten:** Hinterhosenbreite und Figurklassifikation.
- **Gültigkeitsbereich:** Enge Hose für eine Figur mit starkem Gesäß.
- **Technische Randbedingung:** Die Quelle bezeichnet diese Variante als größeren Hosenausschnitt, obwohl der numerische Abtrag ab P24 kleiner ist; die geometrische Wirkung folgt aus der Konstruktion.
- **Offene Fragen oder Widersprüche:** Kein Rechenwiderspruch; „größer“ bezeichnet den resultierenden Ausschnitt, nicht den abgetragenen Zahlenwert.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Geometrische Wirkung nicht aus der bloßen Größe des Abtrags ableiten.

## HOF-B1-S126-F03 — Hinterer Hosenausschnitt bei flachem Gesäß

- **Fachlicher Zweck:** Den kleineren hinteren Hosenausschnitt für eine Figur mit flachem Gesäß bestimmen.
- **Quelle:** `formeln_s126.md`, Zeile 19; Originaltranskript `s126.md`, Zeilen 24–26; Buchseite 126.
- **Originalbezeichnung:** `hHoB : 4 + 0,5 bis +1 cm`
- **Normalisierte Bezeichnung:** `hinterer_hosenausschnitt_flaches_gesaess`

### Buchfassung

```text
hHoB : 4 + 0,5 bis +1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hinterhosenbreite` | hHoB | 25,2 | cm |
| `zuschlag` | 0,5 bis 1 | wählbar | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_min_abtrag = (hinterhosenbreite / 4) + 0,5 cm
                            = 6,8 cm
hosenausschnitt_max_abtrag = (hinterhosenbreite / 4) + 1 cm
                            = 7,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hinterer_hosenausschnitt_abtrag` | figurabhängiger Abtrag | 6,8 bis 7,3 | cm |

- **Abhängigkeiten:** Hinterhosenbreite und Figurklassifikation.
- **Gültigkeitsbereich:** Enge Hose für eine Figur mit flachem Gesäß.
- **Technische Randbedingung:** Die Quelle bezeichnet den resultierenden Ausschnitt als kleiner; der abgetragene Zahlenwert ist größer.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** F01 und F03 haben denselben Zahlenbereich, aber F03 bindet ihn ausdrücklich an die Figurklasse „flaches Gesäß“.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s126.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 24 | 1 | Zeichnungswiederholung des Bereichs aus `HOF-B1-S126-F01` beziehungsweise F03; der gewählte Wert 0,7 cm ist ein Eingabewert, keine neue Formel |
| Zeile 25 | 1 | Gewählter Gesäßwinkel `α = 76°`; Konstruktionsparameter, keine Berechnung |
| **Summe** | **2** | **1 Wiederholung und 1 Eingabewert ausgeschlossen** |
