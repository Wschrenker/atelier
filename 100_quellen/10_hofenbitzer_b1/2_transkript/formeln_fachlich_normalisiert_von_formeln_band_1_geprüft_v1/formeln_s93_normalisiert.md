# Fachlich normalisierte Formeln — S. 93

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/03_modelle_roecke_s40-105/formeln_s93.md`
Originaltranskript: `../Band_1_geprüft_v1/s93.md`
Buchseite: Hofenbitzer, Band 1, S. 93

## HOF-B1-S093-F01 — Doppelter Schlitzeinschlag

- **Fachlicher Zweck:** Die gesamte Breite des doppelten Schlitzeinschlags aus zwei gleich breiten Einschlägen bestimmen.
- **Quelle:** `formeln_s93.md`, Zeile 9; Originaltranskript `s93.md`, Zeile 13; Buchseite 93.
- **Originalbezeichnung:** `doppelter Schlitz-Einschlag z.B. mit 2 × 2 cm`
- **Normalisierte Bezeichnung:** `doppelter_schlitzeinschlag`

### Buchfassung

```text
6. Wird das Rockfutter bzw. ein Futterrock aus einer geraden oder ausgestellten Rockform (siehe Seite 32, 46) gearbeitet, sollte für mehr Schrittweite zusätzlich ein offener Schlitz in die Seitennähte gearbeitet werden. Der doppelte Schlitz-Einschlag wird z.B. mit 2 × 2 cm angezeichnet.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `anzahl_einschlaege` | doppelter Schlitz-Einschlag | 2 | dimensionslos |
| `breite_je_einschlag` | Breite eines Einschlags | 2 | cm |

### Formel und Rechenschritte

```text
gesamtbreite_schlitzeinschlag = anzahl_einschlaege * breite_je_einschlag
                               = 2 * 2 cm
                               = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert aus der Buchfassung | Einheit |
|---|---|---:|---|
| `gesamtbreite_schlitzeinschlag` | gesamte Breite beider Einschläge am offenen Seitenschlitz | 4 | cm |

- **Abhängigkeiten:** Anzahl und Breite der beiden gleich angesetzten Schlitzeinschläge.
- **Gültigkeitsbereich:** Gerades oder ausgestelltes Rockfutter beziehungsweise Futterrock mit offenem Schlitz in der Seitennaht auf S. 93; der Wert von 2 cm je Einschlag ist ausdrücklich ein Beispiel.
- **Technische Randbedingung:** Beide Einschläge müssen in derselben Längeneinheit geführt werden. Für abweichende Einzelbreiten sind die beiden Beträge zu summieren.
- **Offene Fragen oder Widersprüche:** Keine; aus `2 × 2 cm` ergeben sich rechnerisch 4 cm Gesamtbreite. Das Buch druckt den Ergebniswert nicht gesondert aus.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Einzelbreite als wählbaren Produktionsparameter führen; 2 cm ist nur der belegte Beispielwert.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s93.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Quellenfoto-Zuordnung; keine Rechenformel |
| **Summe** | **1** | **1 Fehlklassifikation ausgeschlossen** |
