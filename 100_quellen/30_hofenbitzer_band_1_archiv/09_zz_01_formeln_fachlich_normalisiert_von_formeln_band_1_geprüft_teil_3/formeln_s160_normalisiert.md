# Fachlich normalisierte Formeln — S. 160

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s160.md`
Originaltranskript: `s160.md`
Buchseite: Hofenbitzer, Band 1, S. 160

## HOF-B1-S160-F01 — Vordere Saumweite als Buchbeispielwert

- **Fachlicher Zweck:** Den im Modell verwendeten vorderen Saumweitenwert dokumentieren.
- **Quelle:** `formeln_s160.md`, Zeile 9; Originaltranskript `s160.md`, Zeile 51; Buchseite 160.
- **Originalbezeichnung:** `vordere Saumweite`
- **Normalisierte Bezeichnung:** `saumweite_vorne`

### Buchfassung

```text
- vordere Saumweite = 29,5 cm
```

### Eingaben

Keine; die Quelle gibt den Wert direkt als Buchbeispiel an.

### Formel und Rechenschritte

```text
saumweite_vorne = 29,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite_vorne` | vordere Saumweite | 29,5 | cm |

- **Abhängigkeiten:** Buchbeispielwert für die nachfolgende gesamte Saumweite.
- **Gültigkeitsbereich:** Marlene-Dietrich-Hose, Größe 38, Modellvorschlag.
- **Technische Randbedingung:** Direkter Mess-/Beispielwert; keine allgemeine Berechnung.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Eingabe- beziehungsweise Beispielwert führen, nicht aus Körpermaßen ableiten.

## HOF-B1-S160-F02 — Saumweitendifferenz als Fehlbetrag

- **Fachlicher Zweck:** Die Differenz zwischen gemessener und gewünschter Saumweite bestimmen.
- **Quelle:** `formeln_s160.md`, Zeile 14; Originaltranskript `s160.md`, Zeile 65; Buchseite 160.
- **Originalbezeichnung:** `SaW-Differenz: gemessene SaW − gewünschte SaW`
- **Normalisierte Bezeichnung:** `saumweite_differenz`

### Buchfassung

```text
- `SaW-Differenz: gemessene SaW − gewünschte SaW = 63 cm − 79 cm = −16 cm (= Fehlbetrag)`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite_gemessen` | gemessene SaW | 63 | cm |
| `saumweite_gewuenscht` | gewünschte SaW | 79 | cm |

### Formel und Rechenschritte

```text
saumweite_differenz = saumweite_gemessen - saumweite_gewuenscht
                    = 63 cm - 79 cm
                    = -16 cm
fehlbetrag = 16 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite_differenz` | signierte Differenz | −16 | cm |
| `fehlbetrag` | positive Größe des Fehlbetrags | 16 | cm |

- **Abhängigkeiten:** Gemessene und gewünschte Saumweite.
- **Gültigkeitsbereich:** Zusätzliche Saumweitenvergrößerung der Marlene-Dietrich-Hose.
- **Technische Randbedingung:** Die Quelle verwendet zuerst die signierte Differenz und benennt anschließend deren positive Fehlbetragsgröße.
- **Offene Fragen oder Widersprüche:** Im Originaltranskript ist in der Fertigmaßtabelle `SaW2 = 81 cm` angegeben, während die extrahierte Rechenzeile mit `79 cm` rechnet. Die Buchfassung bleibt unverändert; die explizite Rechnung mit 79 cm ist arithmetisch konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Signierte Differenz und positiver Fehlbetrag getrennt führen.

## HOF-B1-S160-F03 — Gesamte Saumweite aus vorderem und hinterem Anteil

- **Fachlicher Zweck:** Die gesamte Saumweite aus den beiden Saumweitenanteilen bestimmen.
- **Quelle:** `formeln_s160.md`, Zeile 15; Originaltranskript `s160.md`, Zeile 66; Buchseite 160.
- **Originalbezeichnung:** `gesamte Saumweite`
- **Normalisierte Bezeichnung:** `saumweite_gesamt`

### Buchfassung

```text
- `gesamte Saumweite = 29,5 cm + 33,5 cm = 63 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite_vorne` | vordere Saumweite | 29,5 | cm |
| `saumweite_hinten` | hintere Saumweite | 33,5 | cm |

### Formel und Rechenschritte

```text
saumweite_gesamt = saumweite_vorne + saumweite_hinten
                 = 29,5 cm + 33,5 cm
                 = 63 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite_gesamt` | gesamte Saumweite | 63 | cm |

- **Abhängigkeiten:** `HOF-B1-S160-F01` und hinterer Saumweitenanteil.
- **Gültigkeitsbereich:** Gerade beziehungsweise ausgestellte Hinterhose der Marlene-Dietrich-Hose.
- **Technische Randbedingung:** Die beiden Teilwerte werden addiert.
- **Offene Fragen oder Widersprüche:** Keine; die Addition ist rechnerisch konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorderen und hinteren Anteil als getrennte Eingaben modellieren.

## HOF-B1-S160-F04 — Untertrittbreite aus Knopflochlänge und Zuschlag

- **Fachlicher Zweck:** Die Breite des Untertritts am Bund aus Knopflochlänge und Zuschlag bestimmen.
- **Quelle:** `formeln_s160.md`, Zeile 20; Originaltranskript `s160.md`, Zeile 73; Buchseite 160.
- **Originalbezeichnung:** `Untertritt-Breite = Länge des Knopflochs + ca. 1 cm (2,5)`
- **Normalisierte Bezeichnung:** `untertritt_breite`

### Buchfassung

```text
- Untertritt-Breite = Länge des Knopflochs + ca. 1 cm (2,5)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `knopflochlaenge` | Länge des Knopflochs | nicht angegeben | cm |
| `untertritt_zuschlag` | Zuschlag | ca. 1 | cm |

### Formel und Rechenschritte

```text
untertritt_breite = knopflochlaenge + untertritt_zuschlag
                   ≈ knopflochlaenge + 1 cm
```

Der Klammerwert `2,5` wird als gedruckter Beispielwert erhalten. Die Quelle weist im Extrakt die zugehörige Knopflochlänge nicht separat aus.

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `untertritt_breite` | Breite des Untertritts | 2,5 | cm |

- **Abhängigkeiten:** Länge des Knopflochs und ungefähr 1 cm Zuschlag.
- **Gültigkeitsbereich:** Gerader Marlene-Bund mit Verschluss an der linken Seitennaht.
- **Technische Randbedingung:** `ca. 1 cm` ist ein ungefährer Zuschlag; die Quelle nennt keine Auswahl- oder Rundungsregel.
- **Offene Fragen oder Widersprüche:** Die Knopflochlänge, aus der sich der Klammerwert `2,5` ergeben soll, ist im Extrakt nicht separat angegeben. Der Wert bleibt daher ein Buchbeispiel und wird nicht zurückgerechnet.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Knopflochlänge und Zuschlag explizit übergeben; den Beispielwert nicht als allgemeine Regel verwenden.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---:|---:|---|
| 21 | 1 | Produktionsangabe `Marlene Bund, 1× OSt + EI`; keine Rechenoperation |
| **Summe** | **1** | **Produktionsangabe ausgeschlossen** |
