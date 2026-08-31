# Fachlich normalisierte Formeln — S. 124

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/formeln_s124.md`
Originaltranskript: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/s124.md`
Buchseite: Hofenbitzer, Band 1, S. 124

## HOF-B1-S124-F01 — Vorderer Hosenausschnitt der engen Hose

- **Fachlicher Zweck:** Den normalen vorderen Hosenausschnitt der engen Hose aus der Vorderhosenbreite bestimmen.
- **Quelle:** `formeln_s124.md`, Zeile 9; Originaltranskript `s124.md`, Zeile 21; Buchseite 124.
- **Originalbezeichnung:** `vHoB : 4 − 0,5 bis −1 cm`
- **Normalisierte Bezeichnung:** `vorderer_hosenausschnitt_enge_hose`

### Buchfassung

```text
10. Von P8 aus um vHoB : 4 − 0,5 bis −1 cm die Hüftlinie nach rechts verlängern.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderhosenbreite` | vHoB | 23,2 | cm |
| `abzug_vorderer_hosenausschnitt` | 0,5 bis 1 | wählbar | cm |

### Formel und Rechenschritte

```text
vorderer_hosenausschnitt_max = (vorderhosenbreite / 4) - 0,5 cm
                              = (23,2 cm / 4) - 0,5 cm
                              = 5,3 cm
vorderer_hosenausschnitt_min = (vorderhosenbreite / 4) - 1 cm
                              = 4,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderer_hosenausschnitt` | Verlängerungsbetrag ab P8 | 4,8 bis 5,3 | cm |

- **Abhängigkeiten:** Vorderhosenbreite `vHoB` aus `HOF-B1-S120-F04` beziehungsweise der wiederholten Tabelle auf S. 124.
- **Gültigkeitsbereich:** Enge Hose für eine normal proportionierte Figur auf S. 124.
- **Technische Randbedingung:** Die gedruckte Reihenfolge führt vom größeren Ergebnis bei `−0,5 cm` zum kleineren bei `−1 cm`; die Grenzen sind nach dem Ergebnis benannt.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Abzug als wählbaren Bereich führen und Ergebnisgrenzen numerisch sortieren.

## HOF-B1-S124-F02 — Vorderer Hosenausschnitt bei breiten Hüften und flachem Gesäß

- **Fachlicher Zweck:** Den kleineren vorderen Hosenausschnitt für breite Hüften und flaches Gesäß bestimmen.
- **Quelle:** `formeln_s124.md`, Zeile 14; Originaltranskript `s124.md`, Zeilen 25–27; Buchseite 124.
- **Originalbezeichnung:** `vHoB : 4 − 1 bis −1,5 cm`
- **Normalisierte Bezeichnung:** `vorderer_hosenausschnitt_breite_hueften_flaches_gesaess`

### Buchfassung

```text
vHoB : 4 − 1 bis −1,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderhosenbreite` | vHoB | 23,2 | cm |
| `abzug` | 1 bis 1,5 | wählbar | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_max = (vorderhosenbreite / 4) - 1 cm
                     = 4,8 cm
hosenausschnitt_min = (vorderhosenbreite / 4) - 1,5 cm
                     = 4,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderer_hosenausschnitt` | kleinerer Abtrag für diese Figurform | 4,3 bis 4,8 | cm |

- **Abhängigkeiten:** Vorderhosenbreite und Figurklassifikation.
- **Gültigkeitsbereich:** Enge Hose für breite Hüften und flaches Gesäß.
- **Technische Randbedingung:** Ergebnisgrenzen nach ihrem Wert, nicht nach der Druckreihenfolge benennen.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Figurklasse als explizite Auswahl behandeln.

## HOF-B1-S124-F03 — Vorderer Hosenausschnitt bei schmalen Hüften und starkem Gesäß

- **Fachlicher Zweck:** Den größeren vorderen Hosenausschnitt für schmale Hüften und starkes Gesäß bestimmen.
- **Quelle:** `formeln_s124.md`, Zeile 19; Originaltranskript `s124.md`, Zeilen 29–31; Buchseite 124.
- **Originalbezeichnung:** `vHoB : 4 + 0 bis +0,5 cm`
- **Normalisierte Bezeichnung:** `vorderer_hosenausschnitt_schmale_hueften_starkes_gesaess`

### Buchfassung

```text
vHoB : 4 + 0 bis +0,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderhosenbreite` | vHoB | 23,2 | cm |
| `zuschlag` | 0 bis 0,5 | wählbar | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_min = (vorderhosenbreite / 4) + 0 cm
                     = 5,8 cm
hosenausschnitt_max = (vorderhosenbreite / 4) + 0,5 cm
                     = 6,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderer_hosenausschnitt` | größerer Abtrag für diese Figurform | 5,8 bis 6,3 | cm |

- **Abhängigkeiten:** Vorderhosenbreite und Figurklassifikation.
- **Gültigkeitsbereich:** Enge Hose für schmale Hüften und starkes Gesäß.
- **Technische Randbedingung:** Zuschlag muss innerhalb des belegten Bereichs gewählt werden.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Figurabhängige Variante getrennt von F01 und F02 wählen.

## HOF-B1-S124-F04 — Viertel-Saumweite der Vorderhose

- **Fachlicher Zweck:** Den seitlich von P12 abzutragenden Saumbetrag bestimmen.
- **Quelle:** `formeln_s124.md`, Zeile 24; Originaltranskript `s124.md`, Zeilen 35–37; Buchseite 124.
- **Originalbezeichnung:** `SaW : 4 − 0,5 cm`
- **Normalisierte Bezeichnung:** `saumbetrag_vorderhose_enge_hose`

### Buchfassung

```text
15. Von P12 aus SaW : 4 − 0,5 cm nach rechts
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite` | SaW | 32 | cm |
| `saumabzug` | 0,5 cm | 0,5 | cm |

### Formel und Rechenschritte

```text
saumbetrag_vorderhose = (saumweite / 4) - saumabzug
                       = (32 cm / 4) - 0,5 cm
                       = 7,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumbetrag_vorderhose` | Betrag rechts und links von P12 | 7,5 | cm |

- **Abhängigkeiten:** Gewählte Saumweite der engen Hose.
- **Gültigkeitsbereich:** Vorderhose der engen Hose auf S. 124.
- **Technische Randbedingung:** Derselbe Betrag wird laut Folgeschritt nach rechts und links abgetragen.
- **Offene Fragen oder Widersprüche:** Keine; `32 / 4 - 0,5 = 7,5`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einen Betrag berechnen und symmetrisch um P12 anwenden.

## HOF-B1-S124-F05 — Erhöhte vordere Taillenlinie

- **Fachlicher Zweck:** Den auf der erhöhten vorderen Taillenlinie abzutragenden Betrag bestimmen.
- **Quelle:** `formeln_s124.md`, Zeile 29; Originaltranskript `s124.md`, Zeilen 43–49; Buchseite 124.
- **Originalbezeichnung:** `TaU : 4 + 1 cm + gewünschte Einhalteweite`
- **Normalisierte Bezeichnung:** `vordere_taillenlinienlaenge_enge_hose`

### Buchfassung

```text
Von P20 wird TaU : 4 + 1 cm + gewünschte Einhalteweite auf die erhöhte Taillenlinie abgetragen → P21.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |
| `hueftbogen_zugabe_vorne` | 1 cm | 1 | cm |
| `einhalteweite_vorne` | gewünschte Einhalteweite | nicht angegeben | cm |

### Formel und Rechenschritte

```text
vordere_taillenlinienlaenge = (taillenumfang / 4)
                              + hueftbogen_zugabe_vorne
                              + einhalteweite_vorne
Buchbasis_ohne_Einhalteweite = (72 cm / 4) + 1 cm
                              = 19 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert ohne Einhalteweite | Einheit |
|---|---|---:|---|
| `vordere_taillenlinienlaenge` | Betrag von P20 bis P21 | 19 + Einhalteweite | cm |

- **Abhängigkeiten:** Taillenumfang und gewählte Einhalteweite.
- **Gültigkeitsbereich:** Vorderteil-Grundschnitt der engen Hose ohne Vorderabnäher.
- **Technische Randbedingung:** Die feste Zugabe von 1 cm verhindert laut Originaltranskript einen zu runden Hüftbogen und wird an der Hinterhose wieder abgezogen.
- **Offene Fragen oder Widersprüche:** Die Einhalteweite ist nicht numerisch festgelegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Feste 1-cm-Zugabe und variable Einhalteweite als getrennte Operanden führen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s124.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 34–35 | 2 | Teilwerte von TaU und HüU; identische Wiederholungen von `HOF-B1-S120-F01` und `HOF-B1-S120-F02` |
| Zeile 36 | 1 | Leere BuU-Tabellenzeile ohne Werte |
| Zeilen 41–42 | 2 | Vorder- und Hinterhosenbreite; identische Wiederholungen von `HOF-B1-S120-F04` und `HOF-B1-S120-F05` |
| Zeile 47 | 1 | Kniehöhe; identische Wiederholung von `HOF-B1-S120-F06` |
| **Summe** | **6** | **6 Wiederholungen oder leere Tabellenzeilen ausgeschlossen** |
