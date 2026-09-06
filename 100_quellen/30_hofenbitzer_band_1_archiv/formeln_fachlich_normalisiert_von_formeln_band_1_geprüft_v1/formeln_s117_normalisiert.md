# Fachlich normalisierte Formeln — S. 117

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/formeln_s117.md`
Originaltranskript: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/s117.md`
Buchseite: Hofenbitzer, Band 1, S. 117

## HOF-B1-S117-F01 — Hosenausschnitt der Standardhose

- **Fachlicher Zweck:** Den Hosenausschnitt einer Normalfigur mittlerer Größe aus einem Fünftel des Hüftumfangs bestimmen.
- **Quelle:** `formeln_s117.md`, Zeilen 9 und 14; Originaltranskript `s117.md`, Zeilen 17–25; Buchseite 117.
- **Originalbezeichnung:** `HüU : 5 (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_standardhose`

### Buchfassung

```text
HüU : 5 (± 1 cm)
```

```text
= 19,4 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `toleranz_hosenausschnitt` | ± 1 cm | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_basis = hueftumfang / 5
                       = 97 cm / 5
                       = 19,4 cm

hosenausschnitt_untergrenze = hosenausschnitt_basis - toleranz_hosenausschnitt
                             = 18,4 cm
hosenausschnitt_obergrenze = hosenausschnitt_basis + toleranz_hosenausschnitt
                            = 20,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_basis` | Hosenausschnitt der Standardhose | 19,4 | cm |
| `hosenausschnitt_untergrenze` | untere Grenze der angegebenen Toleranz | 18,4 | cm |
| `hosenausschnitt_obergrenze` | obere Grenze der angegebenen Toleranz | 20,4 | cm |

- **Abhängigkeiten:** Hüftumfang und die von der Quelle angegebene Toleranz.
- **Gültigkeitsbereich:** Standardhose für eine „Normalfigur mittlerer Größe“ auf S. 117.
- **Technische Randbedingung:** Die Toleranz ist als zulässiger Bereich um den Basiswert zu führen, nicht als automatisch zu addierender Betrag.
- **Offene Fragen oder Widersprüche:** Keine; `97 cm / 5 = 19,4 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Basiswert und Toleranzintervall getrennt ausgeben; Figurkorrekturen aus F02 und F03 nicht zugleich anwenden.

## HOF-B1-S117-F02 — Hosenausschnitt bei flachem Gesäß

- **Fachlicher Zweck:** Den Hosenausschnitt für eine Figur mit flachem Gesäß aus dem Standardwert reduzieren.
- **Quelle:** `formeln_s117.md`, Zeile 19; Originaltranskript `s117.md`, Zeilen 27–29; Buchseite 117.
- **Originalbezeichnung:** `19,4 cm − 1,5 cm = 17,9 cm (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_flaches_gesaess`

### Buchfassung

```text
19,4 cm − 1,5 cm = 17,9 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_basis` | Hosenausschnitt der Standardhose | 19,4 | cm |
| `korrektur_flaches_gesaess` | ca. 1,5 cm weniger | 1,5 | cm |
| `toleranz_hosenausschnitt` | ± 1 cm | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_flaches_gesaess = hosenausschnitt_basis - korrektur_flaches_gesaess
                                  = 19,4 cm - 1,5 cm
                                  = 17,9 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_flaches_gesaess` | angepasster Hosenausschnitt bei flachem Gesäß | 17,9 | cm |

- **Abhängigkeiten:** Basiswert aus `HOF-B1-S117-F01` und figurabhängiger Korrekturbetrag.
- **Gültigkeitsbereich:** Im Buch beschriebenes Beispiel einer Figur mit flachem Gesäß.
- **Technische Randbedingung:** Der Korrekturbetrag ist mit `ca.` angegeben; das Toleranzintervall von ±1 cm bleibt zusätzlich bestehen.
- **Offene Fragen oder Widersprüche:** Keine; `19,4 cm - 1,5 cm = 17,9 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Figurklasse und Korrekturbetrag explizit als Auswahlparameter führen.

## HOF-B1-S117-F03 — Hosenausschnitt bei starkem Gesäß

- **Fachlicher Zweck:** Den Hosenausschnitt für eine Figur mit starkem Gesäß aus dem Standardwert vergrößern.
- **Quelle:** `formeln_s117.md`, Zeile 24; Originaltranskript `s117.md`, Zeilen 31–33; Buchseite 117.
- **Originalbezeichnung:** `19,4 cm + 1,5 cm = 20,9 cm (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_starkes_gesaess`

### Buchfassung

```text
19,4 cm + 1,5 cm = 20,9 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_basis` | Hosenausschnitt der Standardhose | 19,4 | cm |
| `korrektur_starkes_gesaess` | ca. 1,5 cm mehr | 1,5 | cm |
| `toleranz_hosenausschnitt` | ± 1 cm | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_starkes_gesaess = hosenausschnitt_basis + korrektur_starkes_gesaess
                                  = 19,4 cm + 1,5 cm
                                  = 20,9 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_starkes_gesaess` | angepasster Hosenausschnitt bei starkem Gesäß | 20,9 | cm |

- **Abhängigkeiten:** Basiswert aus `HOF-B1-S117-F01` und figurabhängiger Korrekturbetrag.
- **Gültigkeitsbereich:** Im Buch beschriebenes Beispiel einer Figur mit starkem Gesäß.
- **Technische Randbedingung:** Der Korrekturbetrag ist mit `ca.` angegeben; das Toleranzintervall von ±1 cm bleibt zusätzlich bestehen.
- **Offene Fragen oder Widersprüche:** Keine; `19,4 cm + 1,5 cm = 20,9 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Dieselbe Basisfunktion wie F02 verwenden, aber das Vorzeichen der figurabhängigen Korrektur explizit führen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s117.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 29 | 1 | Zeichnungslabel `Hosenausschnitt = ca. HüU : 5`; inhaltliche Wiederholung von `HOF-B1-S117-F01` |
| **Summe** | **1** | **1 Wiederholung ausgeschlossen** |
