# Fachlich normalisierte Formeln — S. 122

Quelle der Normalisierung: `formeln_s122.md`
Originaltranskript: `s122.md`
Buchseite: Hofenbitzer, Band 1, S. 122

## HOF-B1-S122-F01 — Hintere Taillenvertiefung im Beispiel

- **Fachlicher Zweck:** Die hintere Taillenvertiefung als ungefähr zwei Drittel der vorderen Taillenvertiefung bestimmen.
- **Quelle:** `formeln_s122.md`, Zeile 11; Originaltranskript `s122.md`, Zeile 62; Buchseite 122.
- **Originalbezeichnung:** `hintere Taillenvertiefung ⅔ von vTaV (8 cm) = ca. 5 cm`
- **Normalisierte Bezeichnung:** `hintere_taillenvertiefung_zwei_drittel`

### Buchfassung

```text
- hintere Taillenvertiefung ⅔ von vTaV (8 cm) = ca. 5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vordere_taillenvertiefung` | vTaV | 8 | cm |
| `anteil_hintere_vertiefung` | ⅔ | 2/3 | dimensionslos |

### Formel und Rechenschritte

```text
hintere_taillenvertiefung_exakt = vordere_taillenvertiefung * anteil_hintere_vertiefung
                                  = 8 cm * (2 / 3)
                                  = 5,333... cm
Buchwert                         = ca. 5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hintere_taillenvertiefung` | hTaV im gezeigten Beispiel | ca. 5 | cm |

- **Abhängigkeiten:** Vordere Taillenvertiefung und der für ihren Bereich geltende Anteil.
- **Gültigkeitsbereich:** Beispiel auf S. 122 mit `vTaV = 8 cm`; laut Originaltranskript liegt dies im Bereich 7 bis 9 cm.
- **Technische Randbedingung:** `ca. 5 cm` ist der Buchwert; die technische Rechnung ergibt exakt `5,333... cm`. Eine allgemeine Rundungsregel ist nicht belegt.
- **Offene Fragen oder Widersprüche:** Keine; die Abweichung ist durch die ungefähre Angabe sichtbar.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Exakten Wert und gewählten Konstruktionswert getrennt halten; die bereichsabhängigen Anteile fehlen teilweise in der Extraktionsschicht.

## HOF-B1-S122-F02 — Seitliche Taillenvertiefung als Mittelwert

- **Fachlicher Zweck:** Die seitliche Taillenvertiefung als arithmetische Mitte aus vorderer und hinterer Taillenvertiefung bestimmen.
- **Quelle:** `formeln_s122.md`, Zeilen 9–10; Originaltranskript `s122.md`, Zeilen 59–61; Buchseite 122.
- **Originalbezeichnung:** `8 cm + 5 cm = 13 cm; 13 cm : 2 = 6,5 cm`
- **Normalisierte Bezeichnung:** `seitliche_taillenvertiefung_mittelwert`

### Buchfassung

```text
- 8 cm + 5 cm = 13 cm
- 13 cm : 2 = 6,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vordere_taillenvertiefung` | vTaV | 8 | cm |
| `hintere_taillenvertiefung_buchwert` | hTaV | ca. 5 | cm |

### Formel und Rechenschritte

```text
summe_vertiefungen = vordere_taillenvertiefung + hintere_taillenvertiefung_buchwert
                     = 8 cm + 5 cm
                     = 13 cm

seitliche_taillenvertiefung = summe_vertiefungen / 2
                             = 13 cm / 2
                             = 6,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `seitliche_taillenvertiefung` | seitliche Taillenvertiefung zwischen vTaV und hTaV | 6,5 | cm |

- **Abhängigkeiten:** Vordere Taillenvertiefung und der gerundete Buchwert der hinteren Taillenvertiefung aus `HOF-B1-S122-F01`.
- **Gültigkeitsbereich:** Gezeigtes Beispiel der vereinfachten Taillenvertiefung auf S. 122.
- **Technische Randbedingung:** Die Buchrechnung verwendet `5 cm`, nicht den exakten Zweidrittelwert `5,333... cm`; beide Eingaben müssen dieselbe Einheit tragen.
- **Offene Fragen oder Widersprüche:** Würde der exakte Zweidrittelwert verwendet, ergäbe sich `6,666... cm` statt `6,5 cm`. Die Buchrechnung ist mit ihrem gerundeten Eingabewert rechnerisch korrekt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Festlegen, ob der seitliche Wert aus dem exakten oder aus einem fachlich gerundeten hinteren Wert gebildet wird; die Buchreproduktion verwendet 5 cm.
