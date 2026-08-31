# Fachlich normalisierte Formeln — S. 137

Quelle der Normalisierung: `formeln_s137.md`
Originaltranskript: `s137.md`
Buchseite: Hofenbitzer, Band 1, S. 137

## HOF-B1-S137-F01 — Hosenausschnitt der legeren Hose

- **Fachlicher Zweck:** Den Hosenausschnitt der legeren Hose für eine Normalfigur mittlerer Größe bestimmen.
- **Quelle:** `formeln_s137.md`, Zeilen 9, 14 und 19; Originaltranskript `s137.md`, Zeilen 41–53; Buchseite 137.
- **Originalbezeichnung:** `HüU : 4 - 3 cm (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_legere_hose`

### Buchfassung

```text
HüU : 4 - 3 cm (± 1 cm)
```

```text
97 cm : 4 - 3 cm
```

```text
= 21,3 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `grundabzug` | 3 cm | 3 | cm |
| `toleranz` | ± 1 cm | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_basis_exakt = (hueftumfang / 4) - grundabzug
                             = (97 cm / 4) - 3 cm
                             = 21,25 cm
Buchwert                    = 21,3 cm
hosenausschnitt_untergrenze = Buchwert - toleranz
                             = 20,3 cm
hosenausschnitt_obergrenze  = Buchwert + toleranz
                             = 22,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_basis` | Hosenausschnitt der legeren Hose | 21,3 | cm |
| `hosenausschnitt_untergrenze` | untere Toleranzgrenze | 20,3 | cm |
| `hosenausschnitt_obergrenze` | obere Toleranzgrenze | 22,3 | cm |

- **Abhängigkeiten:** Hüftumfang und Toleranz der Kontrollmessung.
- **Gültigkeitsbereich:** Legere Hose für eine „Normalfigur mittlerer Größe“.
- **Technische Randbedingung:** Das Buch rundet `21,25 cm` auf `21,3 cm`; die Toleranz wird um den gedruckten Basiswert geführt.
- **Offene Fragen oder Widersprüche:** Die Überschrift im Originaltranskript lautet irrtümlich „Hosenausschnitt an der Bundfaltenhose“, während die Seite die legere Hose behandelt. Die Zahlenbeziehung selbst ist eindeutig; die Normalisierung folgt dem Seitenkontext.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Hosentyp als Kontextparameter führen und die fehlerhafte Zwischenüberschrift nicht als Typumschaltung auswerten.

## HOF-B1-S137-F02 — Hosenausschnitt der legeren Hose bei flachem Gesäß

- **Fachlicher Zweck:** Den Hosenausschnitt bei flachem Gesäß aus dem Basiswert vermindern.
- **Quelle:** `formeln_s137.md`, Zeile 24; Originaltranskript `s137.md`, Zeilen 55–57; Buchseite 137.
- **Originalbezeichnung:** `21,3 cm - 1,5 cm = 19,8 cm (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_legere_hose_flaches_gesaess`

### Buchfassung

```text
21,3 cm - 1,5 cm = 19,8 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_basis` | Hosenausschnitt der legeren Hose | 21,3 | cm |
| `korrektur_flaches_gesaess` | ca. 1,5 cm weniger | 1,5 | cm |
| `toleranz` | ± 1 cm | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_flaches_gesaess = hosenausschnitt_basis - korrektur_flaches_gesaess
                                  = 21,3 cm - 1,5 cm
                                  = 19,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_flaches_gesaess` | figurkorrigierter Hosenausschnitt | 19,8 | cm |

- **Abhängigkeiten:** Basiswert aus `HOF-B1-S137-F01`.
- **Gültigkeitsbereich:** Legere Hose bei flachem Gesäß.
- **Technische Randbedingung:** Die Toleranz von ±1 cm bleibt zusätzlich bestehen.
- **Offene Fragen oder Widersprüche:** Keine; `21,3 - 1,5 = 19,8`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Figurklasse und Korrektur getrennt führen.

## HOF-B1-S137-F03 — Hosenausschnitt der legeren Hose bei starkem Gesäß

- **Fachlicher Zweck:** Den Hosenausschnitt bei starkem Gesäß aus dem Basiswert vergrößern.
- **Quelle:** `formeln_s137.md`, Zeile 29; Originaltranskript `s137.md`, Zeilen 59–61; Buchseite 137.
- **Originalbezeichnung:** `21,3 cm + 1,5 cm = 22,8 cm (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_legere_hose_starkes_gesaess`

### Buchfassung

```text
21,3 cm + 1,5 cm = 22,8 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_basis` | Hosenausschnitt der legeren Hose | 21,3 | cm |
| `korrektur_starkes_gesaess` | ca. 1,5 cm mehr | 1,5 | cm |
| `toleranz` | ± 1 cm | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_starkes_gesaess = hosenausschnitt_basis + korrektur_starkes_gesaess
                                  = 21,3 cm + 1,5 cm
                                  = 22,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_starkes_gesaess` | figurkorrigierter Hosenausschnitt | 22,8 | cm |

- **Abhängigkeiten:** Basiswert aus `HOF-B1-S137-F01`.
- **Gültigkeitsbereich:** Legere Hose bei starkem Gesäß.
- **Technische Randbedingung:** Die Toleranz von ±1 cm bleibt zusätzlich bestehen.
- **Offene Fragen oder Widersprüche:** Keine; `21,3 + 1,5 = 22,8`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Dieselbe Basisfunktion wie F02 mit positivem Vorzeichen verwenden.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s137.md` enthält weitere formelartige Beziehungen, die in `formeln_s137.md` fehlen: die Übertragung der halben Vorderhosen-Saumweite plus 2 cm in Zeile 10, die Verdopplung der hinteren Hosenausschnitt-Verbreiterung in Zeile 18, die Übertragung der vorderen Innenbeinnaht minus 0 bis 1,5 cm in Zeile 20 sowie die Halbierung zwischen Seiten- und Innenbeinnaht in Zeile 24. Sie wurden nicht stillschweigend normalisiert. Die widersprüchliche Zwischenüberschrift in Zeile 41 wurde sichtbar als Kontextfehler festgehalten.
