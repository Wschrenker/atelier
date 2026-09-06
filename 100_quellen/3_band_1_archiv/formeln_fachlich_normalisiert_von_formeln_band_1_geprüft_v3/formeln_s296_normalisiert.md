# Fachlich normalisierte Formeln — S. 296

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s296.md`  
Originaltranskript: `s296.md`  
Buchseite: Hofenbitzer, Band 1, S. 296

## HOF-B1-S296-F01 — Vordere Halsloch-Länge mit Abzug

- **Fachlicher Zweck:** Die im Modell verkürzte vordere Halsloch-Länge dokumentieren.
- **Quelle:** `formeln_s296.md`, Zeilen 19 und 24; Originaltranskript `s296.md`, Zeilen 49 und 53; Buchseite 296.
- **Originalbezeichnung:** `vHlL = 12,3 cm − 0,5 cm`
- **Normalisierte Bezeichnung:** `vordere_halslochlaenge_verkuerzt`

### Buchfassung

```text
vHlL = 12,3 cm − 0,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vordere_halslochlaenge_basis` | vHlL | 12,3 | cm |
| `halsloch_abzug` | `0,5 cm` | 0,5 | cm |

### Formel und Rechenschritte

```text
vordere_halslochlaenge_neu = vordere_halslochlaenge_basis - halsloch_abzug
                            = 12,3 cm - 0,5 cm
                            = 11,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vordere_halslochlaenge_neu` | verkürzte vordere Halsloch-Länge | 11,8 | cm |

- **Abhängigkeiten:** Ausgangswert vHlL und Abzug.
- **Gültigkeitsbereich:** S-förmig gerundete einteilige Umlegekragen.
- **Technische Randbedingung:** Der Abzug gilt nur für die beiden ausdrücklich so bezeichneten Varianten.
- **Offene Fragen oder Widersprüche:** Keine arithmetische Unklarheit.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ausgangslänge und Abzug getrennt führen.

## HOF-B1-S296-F02 — Kragenbreite aus Stegbreite mit Variantenbereich

- **Fachlicher Zweck:** Kragenbreite aus Stegbreite und variantenspezifischem Zuschlagsbereich bestimmen.
- **Quelle:** `formeln_s296.md`, Zeilen 14, 19 und 24; Originaltranskript `s296.md`, Zeilen 45, 49 und 53; Buchseite 296.
- **Originalbezeichnung:** `KrB = StegB + 0,7 bis 2 cm`, `... + 0,7 bis 3 cm`, `... + 0,7 bis 4 cm`
- **Normalisierte Bezeichnung:** `kragenbreite_aus_stegbreite_s_form`

### Buchfassung

```text
KrB = StegB + 0,7 bis 2 cm
KrB = StegB + 0,7 bis 3 cm
KrB = StegB + 0,7 bis 4 cm
```

### Eingaben und Rechenschritte

```text
kragenbreite = stegbreite + kragen_zuschlag
```

`kragen_zuschlag` bleibt je Variante einer der drei gedruckten Bereiche.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kragenbreite` | Kragenbreite der gewählten Variante | cm |

- **Abhängigkeiten:** StegB und gewählte Zuschlagsvariante.
- **Gültigkeitsbereich:** Einteilige Umlegekragen mit S-förmiger Kragennaht.
- **Technische Randbedingung:** Keine automatische Bereichsauswahl.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Variante explizit übergeben.

## Ausgeschlossene Kandidaten

| Extraktzeilen | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Direkte Halsloch-Länge ohne eigenständige Rechenbeziehung |
| **Summe** | **1** | **Eingabelabel ausgeschlossen** |
