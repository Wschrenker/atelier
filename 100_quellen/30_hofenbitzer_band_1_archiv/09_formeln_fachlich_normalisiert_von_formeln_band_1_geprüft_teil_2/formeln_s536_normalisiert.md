# Fachlich normalisierte Formeln — S. 536

Quelle der Normalisierung: `formeln_s536_digital_geprüft.md`
Originaltranskript: `s536_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 536

## HOF-B1-S536-F01 — Taillenausfall des Rockgrundschnitts

- **Fachlicher Zweck:** Den gesamten Taillenausfall aus halber Hüft- und Taillenweite bestimmen und anschließend halbieren.
- **Quelle:** `formeln_s536_digital_geprüft.md`, Zeile 9; Originaltranskript `s536_digital_geprüft.md`, Zeile 15; Buchseite 536.
- **Originalbezeichnung:** `½ HüW − ½ TaW =; ½`.
- **Normalisierte Bezeichnung:** `taillenausfall_rock_und_halbwert`

### Buchfassung

```text
| TaAf | Taillenausfall | ½ HüW − ½ TaW =; ½ |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_hueftweite` | ½ HüW | variabel | cm |
| `halbe_taillenweite` | ½ TaW | variabel | cm |

### Formel und Rechenschritte

```text
taillenausfall = halbe_hueftweite - halbe_taillenweite
halber_taillenausfall = taillenausfall / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `taillenausfall` | TaAf | cm |
| `halber_taillenausfall` | ½ TaAf | cm |

- **Abhängigkeiten:** HüW und TaW des Rockgrundschnitts.
- **Gültigkeitsbereich:** Leere Konstruktionstabelle für einen Rock auf S. 536.
- **Technische Randbedingung:** Beide Eingaben sind Halbweiten; erst ihre Differenz wird nochmals halbiert.
- **Offene Fragen oder Widersprüche:** Keine; konkrete Zugaben und Maße sind im Formular nicht eingetragen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** TaAf und ½ TaAf getrennt ausgeben.

## HOF-B1-S536-F02 — Kontrolle der Taillenausfallverteilung

- **Fachlicher Zweck:** Prüfen, ob die Summe der verteilten Taillenausfallanteile dem berechneten Taillenausfall entspricht.
- **Quelle:** `formeln_s536_digital_geprüft.md`, Zeile 14; Originaltranskript `s536_digital_geprüft.md`, Zeile 29; Buchseite 536.
- **Originalbezeichnung:** `Σ = TaAf`.
- **Normalisierte Bezeichnung:** `kontrolle_taillenausfallverteilung`

### Buchfassung

```text
| Kontrolle | Σ = TaAf |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenausfall_anteile` | Hüftabstich und Abnäherinhalte | variable Liste | cm |
| `taillenausfall` | TaAf | variabel | cm |

### Formel und Rechenschritte

```text
verteilte_summe = sum(taillenausfall_anteile)
kontrolle_erfuellt = verteilte_summe == taillenausfall
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `verteilte_summe` | Σ der verteilten Taillenausfallanteile | cm |
| `kontrolle_erfuellt` | Gleichheit mit TaAf | boolesch |

- **Abhängigkeiten:** TaAf aus `HOF-B1-S536-F01` sowie die fachlich gewählten Hüftabstich- und Abnäheranteile.
- **Gültigkeitsbereich:** Kontrollfeld der Rock-Konstruktionstabelle auf S. 536.
- **Technische Randbedingung:** Nur tatsächlich verwendete Verteilungsanteile summieren; das optionale Feld des zweiten hinteren Abnähers darf nicht als unbekannter Zahlenwert eingehen.
- **Offene Fragen oder Widersprüche:** Die Quelle enthält keine ausgefüllten Anteile und keine Toleranzregel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Kontrolle mit einer fachlich festgelegten numerischen Toleranz ausführen.

## HOF-B1-S536-F03 — Vorder- und Hinterhosenbreite

- **Fachlicher Zweck:** Vorder- und Hinterhosenbreite als komplementäre Viertel des Hüftumfangs mit Grundverschiebung und optionaler signierter Anpassung bestimmen.
- **Quelle:** `formeln_s536_digital_geprüft.md`, Zeilen 19–20; Originaltranskript `s536_digital_geprüft.md`, Zeilen 51–52; Buchseite 536.
- **Originalbezeichnung:** `¼ HüU − 1 cm ±` und `¼ HüU + 1 cm ±`.
- **Normalisierte Bezeichnung:** `vorder_und_hinterhosenbreite`

### Buchfassung

```text
| vHoB | Vorderhosenbreite: ¼ HüU − 1 cm ± |
| hHoB | Hinterhosenbreite: ¼ HüU + 1 cm ± |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | variabel | cm |
| `vorderhosenbreite_anpassung` | `±` bei vHoB | variabel, signiert | cm |
| `hinterhosenbreite_anpassung` | `±` bei hHoB | variabel, signiert | cm |
| `grundverschiebung` | `1 cm` | 1 | cm |

### Formel und Rechenschritte

```text
vorderhosenbreite = (hueftumfang / 4) - 1 cm + vorderhosenbreite_anpassung
hinterhosenbreite = (hueftumfang / 4) + 1 cm + hinterhosenbreite_anpassung
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `vorderhosenbreite` | vHoB | cm |
| `hinterhosenbreite` | hHoB | cm |

- **Abhängigkeiten:** HüU und gegebenenfalls fachlich bestimmte signierte Anpassungen.
- **Gültigkeitsbereich:** Leere Konstruktionstabelle für eine Hose auf S. 536.
- **Technische Randbedingung:** Das gedruckte `±` wird je Breite als eigener vorzeichenbehafteter Parameter erhalten.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt weder Anlass noch Berechnung der optionalen Anpassungen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Beide Anpassungen explizit verlangen und nicht automatisch koppeln; ohne Anpassung muss fachlich ausdrücklich null gewählt werden.

## HOF-B1-S536-F04 — Kniehöhe aus der Schritthöhe

- **Fachlicher Zweck:** Die Kniehöhe als vier Zehntel der Schritthöhe berechnen.
- **Quelle:** `formeln_s536_digital_geprüft.md`, Zeile 25; Originaltranskript `s536_digital_geprüft.md`, Zeile 54; Buchseite 536.
- **Originalbezeichnung:** `SrH : 10 · 4`.
- **Normalisierte Bezeichnung:** `kniehoehe_aus_schritthoehe`

### Buchfassung

```text
| KnH | Kniehöhe: SrH : 10 · 4 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `schritthoehe` | SrH | variabel | cm |

### Formel und Rechenschritte

```text
kniehoehe = (schritthoehe / 10) * 4
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kniehoehe` | KnH | cm |

- **Abhängigkeiten:** SrH.
- **Gültigkeitsbereich:** Leere Konstruktionstabelle für eine Hose auf S. 536.
- **Technische Randbedingung:** Division und Multiplikation werden in der gedruckten Reihenfolge ausgeführt; algebraisch entspricht dies `0,4 * SrH`.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den belegten Bruch `4/10` exakt erhalten und erst bei der Ausgabe runden.

## HOF-B1-S536-F05 — Einhalteweite und Ärmelkugelumfang

- **Fachlicher Zweck:** Die Einhalteweite aus Armlochumfang und Prozentsatz sowie daraus den Ärmelkugelumfang bestimmen.
- **Quelle:** `formeln_s536_digital_geprüft.md`, Zeilen 30–31; Originaltranskript `s536_digital_geprüft.md`, Zeilen 89–90; Buchseite 536.
- **Originalbezeichnung:** `EW in cm = AlU · Einhalteweite in %` und `ÄKU = AlU + Einhalteweite in cm`.
- **Normalisierte Bezeichnung:** `einhalteweite_und_aermelkugelumfang`

### Buchfassung

```text
| EW in % | Einhalteweite in % | Einhalteweite in cm = AlU · Einhalteweite in % = EW in cm |
|  | Ärmelkugelumfang = AlU + Einhalteweite in cm | ÄKU |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochumfang` | AlU | variabel | cm |
| `einhalteweite_prozent` | EW in % | variabel | % |

### Formel und Rechenschritte

```text
einhalteweite_faktor = einhalteweite_prozent / 100
einhalteweite_cm = armlochumfang * einhalteweite_faktor
aermelkugelumfang = armlochumfang + einhalteweite_cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `einhalteweite_cm` | EW in cm | cm |
| `aermelkugelumfang` | ÄKU | cm |

- **Abhängigkeiten:** AlU und ein zur Ärmelform gewählter Prozentsatz, beispielsweise aus `HOF-B1-S536-F06`.
- **Gültigkeitsbereich:** Leere Ärmel-Konstruktionstabelle auf S. 536.
- **Technische Randbedingung:** Prozentangaben vor der Multiplikation durch 100 teilen; negative Werte verkleinern den Ärmelkugelumfang.
- **Offene Fragen oder Widersprüche:** Keine Zahlenwerte sind eingetragen; die Rechenfolge ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Prozentwert, Faktor und Zentimeterbetrag getrennt führen.

## HOF-B1-S536-F06 — Zugabenbereiche nach Ärmelform

- **Fachlicher Zweck:** Oberarmweite, Ärmelsaumweite und Einhalteweite aus Körpermaßen, Passformklasse und gewählter Ärmelform bestimmen.
- **Quelle:** `formeln_s536_digital_geprüft.md`, Zeilen 36–38; Originaltranskript `s536_digital_geprüft.md`, Zeilen 96–98; Buchseite 536.
- **Originalbezeichnung:** Berechnungstabelle für schmalen, engen und weiten Ärmel.
- **Normalisierte Bezeichnung:** `aermelmasse_nach_aermelform`

### Buchfassung

```text
| Schmaler Ärmel | OaU + 0,7 bis 1 · PK* des Oberteils | HgU + 1 bis 2 · PK* des Oberteils | +3 % bis +10 % des AlU |
| Enger Ärmel | OaU + 0,5 bis 1 · PK* des Oberteils | HgU + 0 bis 1,5 · PK* des Oberteils | 0 % bis +3 % des AlU |
| Weiter Ärmel | OaU + 1 bis 2,5 · PK* des Oberteils | entsteht automatisch | −1 % bis +3 % des AlU |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `aermelform` | schmal, eng oder weit | explizite Auswahl | dimensionslos |
| `oberarmumfang` | OaU | variabel | cm |
| `handgelenkumfang` | HgU | variabel | cm |
| `armlochumfang` | AlU | variabel | cm |
| `passformklasse_oberteil` | PK des Oberteils | variabel | cm |
| `oberarm_faktor` | Faktor aus Tabellenbereich | explizite Auswahl | dimensionslos |
| `saum_faktor` | Faktor aus Tabellenbereich | explizite Auswahl | dimensionslos |
| `einhalteweite_prozent` | Prozentwert aus Tabellenbereich | explizite Auswahl | % |

### Formel und Rechenschritte

```text
oberarmweite = oberarmumfang + (oberarm_faktor * passformklasse_oberteil)

Für schmalen Ärmel: 0,7 <= oberarm_faktor <= 1
Für engen Ärmel: 0,5 <= oberarm_faktor <= 1
Für weiten Ärmel: 1 <= oberarm_faktor <= 2,5

Für schmalen Ärmel:
aermelsaumweite = handgelenkumfang + (saum_faktor * passformklasse_oberteil)
1 <= saum_faktor <= 2

Für engen Ärmel:
aermelsaumweite = handgelenkumfang + (saum_faktor * passformklasse_oberteil)
0 <= saum_faktor <= 1,5

Für weiten Ärmel:
aermelsaumweite = automatisch aus der Konstruktion

Für schmalen Ärmel: 3 <= einhalteweite_prozent <= 10
Für engen Ärmel: 0 <= einhalteweite_prozent <= 3
Für weiten Ärmel: -1 <= einhalteweite_prozent <= 3
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `oberarmweite` | OaW | cm |
| `aermelsaumweite` | ÄSaW; beim weiten Ärmel geometrisch entstehend | cm |
| `einhalteweite_prozent` | EW in % | % |

- **Abhängigkeiten:** PK nach `HOF-B1-S536-F07`; Einhalteweite in cm und ÄKU können danach mit `HOF-B1-S536-F05` berechnet werden.
- **Gültigkeitsbereich:** Berechnungstabelle für schmale, enge und weite Ärmel auf S. 536.
- **Technische Randbedingung:** Ärmelform und konkrete Werte innerhalb aller zugehörigen Bereiche müssen fachlich explizit gewählt werden; beim weiten Ärmel liefert die Tabelle keine skalare Formel für ÄSaW.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine Auswahlregel innerhalb der Bereiche und keine Formel für die automatisch entstehende ÄSaW des weiten Ärmels.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Varianten als getrennte Zweige modellieren, Bereichsgrenzen validieren und beim weiten Ärmel ÄSaW nicht aus HgU und PK erfinden.

## HOF-B1-S536-F07 — Passformklasse des Oberteils

- **Fachlicher Zweck:** Die Passformklasse entweder aus einer vorgegebenen Brustweitenzugabe zum halben Grundschnitt oder aus gemessener halber Brustweite minus halbem Brustumfang bestimmen.
- **Quelle:** `formeln_s536_digital_geprüft.md`, Zeile 43; Originaltranskript `s536_digital_geprüft.md`, Zeile 100; Buchseite 536.
- **Originalbezeichnung:** `PK = BrW-Zugabe zum ½ Grundschnitt oder ½ BrW − ½ BrU`.
- **Normalisierte Bezeichnung:** `passformklasse_oberteil`

### Buchfassung

```text
`* PK = BrW-Zugabe zum ½ Grundschnitt oder ½ BrW (½ gemessene BrW am Schnitt) − ½ BrU (½ gemesser BrU am Körper)`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `bestimmungsweg` | Zugabe oder Messdifferenz | explizite Auswahl | dimensionslos |
| `brustweite_zugabe_halber_grundschnitt` | BrW-Zugabe zum ½ Grundschnitt | variabel | cm |
| `halbe_brustweite_gemessen` | ½ gemessene BrW am Schnitt | variabel | cm |
| `halber_brustumfang` | ½ gemessener BrU am Körper | variabel | cm |

### Formel und Rechenschritte

```text
Weg Zugabe:
passformklasse_oberteil = brustweite_zugabe_halber_grundschnitt

Weg Messdifferenz:
passformklasse_oberteil = halbe_brustweite_gemessen - halber_brustumfang
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `passformklasse_oberteil` | PK des Oberteils | cm |

- **Abhängigkeiten:** Explizit gewählter Bestimmungsweg und dessen Eingaben.
- **Gültigkeitsbereich:** Fußnote der Ärmel-Berechnungstabelle auf S. 536.
- **Technische Randbedingung:** Die beiden Wege sind Alternativen und dürfen nicht addiert oder gemischt werden.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine Regel zur Wahl des Bestimmungswegs. `gemesser` ist im Transkript als gedruckter Buchfehler markiert, verändert aber die Formel nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Bestimmungsweg als Pflichtparameter führen und die jeweils unbenutzten Eingaben nicht auswerten.
