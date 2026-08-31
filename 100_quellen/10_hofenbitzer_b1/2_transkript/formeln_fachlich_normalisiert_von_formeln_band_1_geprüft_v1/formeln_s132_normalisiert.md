# Fachlich normalisierte Formeln — S. 132

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/formeln_s132.md`
Originaltranskript: `../Band_1_geprüft_v1/s132.md`
Buchseite: Hofenbitzer, Band 1, S. 132

## HOF-B1-S132-F01 — Hosenausschnitt der Bundfaltenhose

- **Fachlicher Zweck:** Den Hosenausschnitt der Bundfaltenhose für eine Normalfigur mittlerer Größe bestimmen.
- **Quelle:** `formeln_s132.md`, Zeilen 14, 19 und 24; Originaltranskript `s132.md`, Zeilen 35–45; Buchseite 132.
- **Originalbezeichnung:** `HüU : 4 - 4 cm (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_bundfaltenhose`

### Buchfassung

```text
HüU : 4 - 4 cm (± 1 cm)
```

```text
97 cm : 4 - 4 cm
```

```text
= 20,3 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `grundabzug` | 4 cm | 4 | cm |
| `toleranz` | ± 1 cm | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_basis_exakt = (hueftumfang / 4) - grundabzug
                             = (97 cm / 4) - 4 cm
                             = 20,25 cm
Buchwert                    = 20,3 cm
hosenausschnitt_untergrenze = Buchwert - toleranz
                             = 19,3 cm
hosenausschnitt_obergrenze  = Buchwert + toleranz
                             = 21,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_basis` | Hosenausschnitt der Bundfaltenhose | 20,3 | cm |
| `hosenausschnitt_untergrenze` | untere Toleranzgrenze | 19,3 | cm |
| `hosenausschnitt_obergrenze` | obere Toleranzgrenze | 21,3 | cm |

- **Abhängigkeiten:** Hüftumfang und Toleranz der Kontrollmessung.
- **Gültigkeitsbereich:** Bundfaltenhose für eine „Normalfigur mittlerer Größe“.
- **Technische Randbedingung:** Das Buch rundet den exakten Basiswert `20,25 cm` auf `20,3 cm`; die Toleranz wird um den gedruckten Basiswert geführt.
- **Offene Fragen oder Widersprüche:** Keine; Rechenweg und gedrucktes Ergebnis stimmen bei Rundung auf eine Dezimalstelle überein.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Basiswert, Rundung und Toleranzintervall getrennt ausgeben.

## HOF-B1-S132-F02 — Hosenausschnitt der Bundfaltenhose bei flachem Gesäß

- **Fachlicher Zweck:** Den Hosenausschnitt bei flachem Gesäß aus dem Basiswert vermindern.
- **Quelle:** `formeln_s132.md`, Zeile 29; Originaltranskript `s132.md`, Zeilen 47–49; Buchseite 132.
- **Originalbezeichnung:** `20,3 cm - 1,5 cm = 18,8 cm (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_bundfaltenhose_flaches_gesaess`

### Buchfassung

```text
20,3 cm - 1,5 cm = 18,8 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_basis` | Hosenausschnitt der Bundfaltenhose | 20,3 | cm |
| `korrektur_flaches_gesaess` | ca. 1,5 cm weniger | 1,5 | cm |
| `toleranz` | ± 1 cm | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_flaches_gesaess = hosenausschnitt_basis - korrektur_flaches_gesaess
                                  = 20,3 cm - 1,5 cm
                                  = 18,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_flaches_gesaess` | figurkorrigierter Hosenausschnitt | 18,8 | cm |

- **Abhängigkeiten:** Basiswert aus `HOF-B1-S132-F01`.
- **Gültigkeitsbereich:** Bundfaltenhose bei flachem Gesäß.
- **Technische Randbedingung:** Die Toleranz von ±1 cm bleibt zusätzlich bestehen.
- **Offene Fragen oder Widersprüche:** Keine; `20,3 - 1,5 = 18,8`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Figurklasse und Korrektur getrennt führen.

## HOF-B1-S132-F03 — Hosenausschnitt der Bundfaltenhose bei starkem Gesäß

- **Fachlicher Zweck:** Den Hosenausschnitt bei starkem Gesäß aus dem Basiswert vergrößern.
- **Quelle:** `formeln_s132.md`, Zeile 34; Originaltranskript `s132.md`, Zeilen 51–53; Buchseite 132.
- **Originalbezeichnung:** `20,3 cm + 1,5 cm = 21,8 cm (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_bundfaltenhose_starkes_gesaess`

### Buchfassung

```text
20,3 cm + 1,5 cm = 21,8 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_basis` | Hosenausschnitt der Bundfaltenhose | 20,3 | cm |
| `korrektur_starkes_gesaess` | ca. 1,5 cm mehr | 1,5 | cm |
| `toleranz` | ± 1 cm | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_starkes_gesaess = hosenausschnitt_basis + korrektur_starkes_gesaess
                                  = 20,3 cm + 1,5 cm
                                  = 21,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_starkes_gesaess` | figurkorrigierter Hosenausschnitt | 21,8 | cm |

- **Abhängigkeiten:** Basiswert aus `HOF-B1-S132-F01`.
- **Gültigkeitsbereich:** Bundfaltenhose bei starkem Gesäß.
- **Technische Randbedingung:** Die Toleranz von ±1 cm bleibt zusätzlich bestehen.
- **Offene Fragen oder Widersprüche:** Keine; `20,3 + 1,5 = 21,8`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Dieselbe Basisfunktion wie F02 mit positivem Vorzeichen verwenden.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s132.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Gewählter Gesäßwinkel `α = 85°`; Eingabewert, keine berechnete Formel |
| **Summe** | **1** | **1 Eingabewert ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s132.md` beschreibt in den Zeilen 57 und 61 die Verlängerung um die doppelte Aufschlagbreite beziehungsweise zwei parallele Aufschlagbreiten. Diese formelartige Beziehung fehlt in `formeln_s132.md` und wurde nicht stillschweigend normalisiert.
