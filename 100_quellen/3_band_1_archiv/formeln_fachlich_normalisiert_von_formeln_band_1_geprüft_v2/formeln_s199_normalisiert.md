# Fachlich normalisierte Formeln — S. 199

Quelle der Normalisierung: `formeln_s199_digital_geprüft.md`
Originaltranskript: `s199_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 199
Extraktionsstand: v2

## HOF-B1-S199-F01 — Armdurchmesser aus Oberarmumfang

- **Fachlicher Zweck:** Den Armdurchmesser ohne Zugabe aus dem gemessenen Oberarmumfang bestimmen.
- **Quelle:** `formeln_s199_digital_geprüft.md`, Zeile 19; Originaltranskript `s199_digital_geprüft.md`, Zeile 67; Buchseite 199.
- **Originalbezeichnung:** `ArD`, `OaU`
- **Normalisierte Bezeichnung:** `armdurchmesser_aus_oberarmumfang`

### Buchfassung

```text
- Der Armdurchmesser (ohne Zugabe) muss zum gemessenen Oberarmumfang (OaU) passen. Sicherheitshalber den ArD aus dem OaU berechnen (siehe Seite 14): `OaU : 10 · 6 − 7,5 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `oberarmumfang` | OaU | cm |
| `proportionsfaktor` | `: 10 · 6` | dimensionslos |
| `korrekturbetrag` | `7,5 cm` | cm |

### Formel und Rechenschritte

```text
armdurchmesser = (oberarmumfang / 10) * 6 - 7,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `armdurchmesser` | ArD ohne Zugabe | cm |

- **Abhängigkeiten:** Gemessener OaU; Verhältnisformel von S. 14.
- **Gültigkeitsbereich:** Sicherheitskontrolle für Ärmelkonstruktionen auf S. 199.
- **Technische Randbedingung:** Division und Multiplikation werden von links nach rechts vor der Subtraktion ausgeführt.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel im Extrakt; die symbolische Rechenfolge ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Korrekturbetrag erst nach der proportionalen Umrechnung abziehen.

## HOF-B1-S199-F02 — Einhalteweite in Zentimetern

- **Fachlicher Zweck:** Die prozentuale Einhalteweite in ein Längenmaß umrechnen.
- **Quelle:** `formeln_s199_digital_geprüft.md`, Zeile 24; Originaltranskript `s199_digital_geprüft.md`, Zeile 91; Buchseite 199.
- **Originalbezeichnung:** `AlU`, `Einhalteweite in %`, `EW in cm`
- **Normalisierte Bezeichnung:** `einhalteweite_cm`

### Buchfassung

```text
| EW in % | Einhalteweite in % |  | Einhalteweite in cm = AlU · Einhalteweite in % | EW in cm |
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `armlochumfang` | AlU | cm |
| `einhalteweite_anteil` | Einhalteweite in % | dimensionslos |

### Formel und Rechenschritte

```text
einhalteweite_cm = armlochumfang * einhalteweite_anteil
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `einhalteweite_cm` | EW in cm | cm |

- **Abhängigkeiten:** Gemessener AlU und fachlich gewählter Prozentwert.
- **Gültigkeitsbereich:** Konstruktionstabelle für Ärmel auf S. 199.
- **Technische Randbedingung:** Prozentangaben werden technisch als Anteil gespeichert, zum Beispiel `3 % = 0,03`.
- **Offene Fragen oder Widersprüche:** Die Auswahl des Prozentwerts hängt vom Material und Ärmeltyp ab und ist außerhalb dieser Formel zu treffen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Prozentwert vor der Multiplikation durch 100 teilen.

## HOF-B1-S199-F03 — Ärmelkugelumfang

- **Fachlicher Zweck:** Den Ärmelkugelumfang aus Armlochumfang und Einhalteweite bestimmen.
- **Quelle:** `formeln_s199_digital_geprüft.md`, Zeile 25; Originaltranskript `s199_digital_geprüft.md`, Zeile 92; Buchseite 199.
- **Originalbezeichnung:** `AlU`, `Einhalteweite in cm`, `ÄKU`
- **Normalisierte Bezeichnung:** `aermelkugelumfang`

### Buchfassung

```text
|  |  |  | Ärmelkugelumfang = AlU + Einhalteweite in cm | ÄKU |
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `armlochumfang` | AlU | cm |
| `einhalteweite_cm` | Einhalteweite in cm | cm |

### Formel und Rechenschritte

```text
aermelkugelumfang = armlochumfang + einhalteweite_cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `aermelkugelumfang` | ÄKU | cm |

- **Abhängigkeiten:** `HOF-B1-S199-F02`.
- **Gültigkeitsbereich:** Konstruktionstabelle für Ärmel auf S. 199.
- **Technische Randbedingung:** Beide Längen müssen in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Einhalteweite als Längenwert addieren, nicht nochmals als Prozentwert.

## HOF-B1-S199-F04 — Zugaben für den schmalen Ärmel

- **Fachlicher Zweck:** Die Wertebereiche für Oberarmweite, Ärmelsaumweite und Einhalteweite des schmalen Ärmels bestimmen.
- **Quelle:** `formeln_s199_digital_geprüft.md`, Zeile 30; Originaltranskript `s199_digital_geprüft.md`, Zeile 100; Buchseite 199.
- **Originalbezeichnung:** `OaU`, `HgU`, `PK`, `AlU`
- **Normalisierte Bezeichnung:** `schmaler_aermel_zugabebereiche`

### Buchfassung

```text
| Schmaler Ärmel | `OaU + 0,7 bis 1 · PK* des Oberteils` | `HgU + 1 bis 2 · PK* des Oberteils` | `+3 % bis +10 % des AlU` |
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `oberarmumfang` | OaU | cm |
| `handgelenkumfang` | HgU | cm |
| `passformklasse` | PK des Oberteils | cm |
| `armlochumfang` | AlU | cm |
| `oa_faktor` | 0,7 bis 1 | dimensionslos |
| `saum_faktor` | 1 bis 2 | dimensionslos |
| `einhalteweite_anteil` | +3 % bis +10 % | dimensionslos |

### Formel und Rechenschritte

```text
oberarmweite = oberarmumfang + oa_faktor * passformklasse
aermelsaumweite = handgelenkumfang + saum_faktor * passformklasse
einhalteweite_cm = armlochumfang * einhalteweite_anteil
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `oberarmweite` | OaW | cm |
| `aermelsaumweite` | ÄSaW | cm |
| `einhalteweite_cm` | EW in cm | cm |

- **Abhängigkeiten:** PK nach `HOF-B1-S199-F07`; Einhalteweitenrechnung nach `HOF-B1-S199-F02`.
- **Gültigkeitsbereich:** Schmaler Ärmel laut Berechnungstabelle S. 199.
- **Technische Randbedingung:** Alle drei Werte innerhalb ihrer gedruckten Bereiche müssen ausdrücklich gewählt werden.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine automatische Auswahlregel innerhalb der Bereiche.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die drei Faktoren als validierte Eingaben führen; keine Mittelwerte annehmen.

## HOF-B1-S199-F05 — Zugaben für den engen Ärmel

- **Fachlicher Zweck:** Die Wertebereiche für Oberarmweite, Ärmelsaumweite und Einhalteweite des engen Ärmels bestimmen.
- **Quelle:** `formeln_s199_digital_geprüft.md`, Zeile 31; Originaltranskript `s199_digital_geprüft.md`, Zeile 101; Buchseite 199.
- **Originalbezeichnung:** `OaU`, `HgU`, `PK`, `AlU`
- **Normalisierte Bezeichnung:** `enger_aermel_zugabebereiche`

### Buchfassung

```text
| Enger Ärmel | `OaU + 0,5 bis 1 · PK* des Oberteils` | `HgU + 0 bis 1,5 · PK* des Oberteils` | `0 % bis +3 % des AlU` |
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `oberarmumfang` | OaU | cm |
| `handgelenkumfang` | HgU | cm |
| `passformklasse` | PK des Oberteils | cm |
| `armlochumfang` | AlU | cm |
| `oa_faktor` | 0,5 bis 1 | dimensionslos |
| `saum_faktor` | 0 bis 1,5 | dimensionslos |
| `einhalteweite_anteil` | 0 % bis +3 % | dimensionslos |

### Formel und Rechenschritte

```text
oberarmweite = oberarmumfang + oa_faktor * passformklasse
aermelsaumweite = handgelenkumfang + saum_faktor * passformklasse
einhalteweite_cm = armlochumfang * einhalteweite_anteil
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `oberarmweite` | OaW | cm |
| `aermelsaumweite` | ÄSaW | cm |
| `einhalteweite_cm` | EW in cm | cm |

- **Abhängigkeiten:** PK nach `HOF-B1-S199-F07`; Einhalteweitenrechnung nach `HOF-B1-S199-F02`.
- **Gültigkeitsbereich:** Enger Ärmel laut Berechnungstabelle S. 199.
- **Technische Randbedingung:** Die Auswahlwerte müssen innerhalb der drei gedruckten Bereiche liegen.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine automatische Auswahlregel innerhalb der Bereiche.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereichsprüfung getrennt für Oberarm, Saum und Einhalteweite ausführen.

## HOF-B1-S199-F06 — Zugaben für den weiten Ärmel

- **Fachlicher Zweck:** Den Oberarmweiten- und Einhalteweitenbereich des weiten Ärmels bestimmen.
- **Quelle:** `formeln_s199_digital_geprüft.md`, Zeile 32; Originaltranskript `s199_digital_geprüft.md`, Zeile 102; Buchseite 199.
- **Originalbezeichnung:** `OaU`, `PK`, `AlU`; ÄSaW „entsteht automatisch“
- **Normalisierte Bezeichnung:** `weiter_aermel_zugabebereiche`

### Buchfassung

```text
| Weiter Ärmel | `OaU + 1 bis 2,5 · PK* des Oberteils` | entsteht automatisch | `−1 % bis +3 % des AlU` |
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `oberarmumfang` | OaU | cm |
| `passformklasse` | PK des Oberteils | cm |
| `armlochumfang` | AlU | cm |
| `oa_faktor` | 1 bis 2,5 | dimensionslos |
| `einhalteweite_anteil` | −1 % bis +3 % | dimensionslos |

### Formel und Rechenschritte

```text
oberarmweite = oberarmumfang + oa_faktor * passformklasse
einhalteweite_cm = armlochumfang * einhalteweite_anteil
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `oberarmweite` | OaW | cm |
| `einhalteweite_cm` | EW in cm; darf negativ sein | cm |
| `aermelsaumweite` | entsteht in der Konstruktion | cm |

- **Abhängigkeiten:** PK nach `HOF-B1-S199-F07`; Einhalteweitenrechnung nach `HOF-B1-S199-F02`.
- **Gültigkeitsbereich:** Weiter Ärmel laut Berechnungstabelle S. 199.
- **Technische Randbedingung:** Negative Einhalteweite bleibt als zulässiger Wert erhalten; für ÄSaW ist hier keine eigenständige Formel belegt.
- **Offene Fragen oder Widersprüche:** Die konstruktive Entstehung der ÄSaW wird in dieser Tabellenzeile nicht berechnet.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** ÄSaW nicht aus einer erfundenen Zugabeformel berechnen; aus der späteren Geometrie übernehmen.

## HOF-B1-S199-F07 — Passformklasse des Oberteils

- **Fachlicher Zweck:** Die Passformklasse als Brustweitenzugabe beziehungsweise als Differenz zweier halber Brustmaße bestimmen.
- **Quelle:** `formeln_s199_digital_geprüft.md`, Zeile 37; Originaltranskript `s199_digital_geprüft.md`, Zeile 104; Buchseite 199.
- **Originalbezeichnung:** `PK`, `BrW-Zugabe`, `½ BrW`, `½ BrU`
- **Normalisierte Bezeichnung:** `passformklasse_oberteil`

### Buchfassung

```text
`* PK = BrW-Zugabe zum ½ Grundschnitt oder ½ BrW (½ gemessene BrW am Schnitt) − ½ BrU (½ gemesser BrU am Körper)`
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `brustweitenzugabe_halber_grundschnitt` | BrW-Zugabe zum ½ Grundschnitt | cm |
| `halbe_brustweite_schnitt` | ½ gemessene BrW am Schnitt | cm |
| `halber_brustumfang_koerper` | ½ gemesser BrU am Körper | cm |

### Formel und Rechenschritte

```text
passformklasse = brustweitenzugabe_halber_grundschnitt
oder
passformklasse = halbe_brustweite_schnitt - halber_brustumfang_koerper
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `passformklasse` | PK beziehungsweise Zugabe zur halben Brustweite | cm |

- **Abhängigkeiten:** Vorhandener Oberteil-Grundschnitt und seine gemessene halbe Brustweite.
- **Gültigkeitsbereich:** Auswahl der Ärmelzugaben auf S. 199.
- **Technische Randbedingung:** Die zwei Buchwege sind Alternativen und dürfen nicht addiert werden.
- **Offene Fragen oder Widersprüche:** Die Buchfassung enthält `gemesser`; dies wird originalgetreu erhalten. Rechnerisch sind beide Wege eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Genau einen Berechnungsweg verlangen und bei vorhandenen Werten optional ihre Übereinstimmung kontrollieren.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s199_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Isoliertes Zeichnungslabel `¼ ArD+`; direkter Teilwert ohne vollständige Berechnungsbeziehung auf dieser Seite |
| Zeile 14 | 1 | Bezeichnungsdefinition `ArD+ = ArD+Zugabe`; erklärt das Kürzel, berechnet aber keinen Wert |
| **Summe** | **2** | **1 unvollständiges Zeichnungslabel + 1 Bezeichnungsdefinition** |
