# Fachlich normalisierte Formeln — S. 79

Quelle der Normalisierung: `formeln_s79_codex_v2_digital_geprueft.md`
Originaltranskript: `s79_codex_v2_digital_geprueft.md`
Buchseite: Hofenbitzer, Band 1, S. 79

## HOF-B1-S079-F01 — Saumweitenreduzierung des Ballonrocks

- **Fachlicher Zweck:** Den Bereich der gesamten Saumweitenreduzierung aus der Überlappung je Naht und der Anzahl der Nähte bestimmen.
- **Quelle:** `formeln_s79_codex_v2_digital_geprueft.md`, Zeile 9; Originaltranskript `s79_codex_v2_digital_geprueft.md`, Zeile 23; Buchseite 79.
- **Originalbezeichnung:** `10 Nähten = 5 bis 15 cm Saumweitenreduzierung`
- **Normalisierte Bezeichnung:** `saumweitenreduzierung_ballonrock`

### Buchfassung

```text
1. Die Schnittteile am Saum an den Nähten ca. 0,5 bis 1,5 cm übereinander legen (ergibt bei 10 Nähten = 5 bis 15 cm Saumweitenreduzierung)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `anzahl_naehte` | Nähte | 10 | dimensionslos |
| `ueberlappung_je_naht_min` | kleinste Überlappung an jeder Naht | ca. 0,5 | cm |
| `ueberlappung_je_naht_max` | größte Überlappung an jeder Naht | ca. 1,5 | cm |

### Formel und Rechenschritte

```text
saumweitenreduzierung_min = anzahl_naehte * ueberlappung_je_naht_min
                            = 10 * 0,5 cm
                            = 5 cm

saumweitenreduzierung_max = anzahl_naehte * ueberlappung_je_naht_max
                            = 10 * 1,5 cm
                            = 15 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumweitenreduzierung_min` | kleinste gesamte Saumweitenreduzierung | ca. 5 | cm |
| `saumweitenreduzierung_max` | größte gesamte Saumweitenreduzierung | ca. 15 | cm |

- **Abhängigkeiten:** `anzahl_naehte` und gleich gewählte Überlappung an jeder Naht innerhalb des Buchbereichs.
- **Gültigkeitsbereich:** Ballonrock aus dem 10-Bahnenrock auf S. 79 mit zehn Nähten und einer Überlappung von ca. 0,5 bis 1,5 cm je Naht.
- **Technische Randbedingung:** Die Überlappung muss an allen zehn Nähten in derselben Längeneinheit angesetzt werden; die Buchwerte sind Näherungswerte.
- **Offene Fragen oder Widersprüche:** Keine; `10 × 0,5 cm = 5 cm` und `10 × 1,5 cm = 15 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den zulässigen Bereich als zwei Grenzen führen; bei unterschiedlichen Überlappungen je Naht müssen die Einzelbeträge summiert werden.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s79_codex_v2_digital_geprueft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 14–15 | 2 | Schnittteil- und Zuschnittbeschriftungen mit Modellnummern, Stückzahlen, Stofflage und Einlage; Pluszeichen verbinden Modellvarianten beziehungsweise Materialien und sind keine Rechenoperatoren |
| **Summe** | **2** | **2 Fehlklassifikationen ausgeschlossen** |
