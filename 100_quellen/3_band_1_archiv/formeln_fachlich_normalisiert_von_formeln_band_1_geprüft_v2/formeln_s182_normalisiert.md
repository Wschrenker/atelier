# Fachlich normalisierte Formeln — S. 182

Quelle der Normalisierung: `formeln_s182_digital_geprüft.md`
Originaltranskript: `s182_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 182
Extraktionsstand: v2

## HOF-B1-S182-F01 — Gesamte gemessene Hüftbreite

- **Fachlicher Zweck:** Die am Vorder- und Rückteil gemessenen Hüftbreiten zur gesamten gemessenen Hüftbreite addieren.
- **Quelle:** `formeln_s182_digital_geprüft.md`, Zeile 14; Originaltranskript `s182_digital_geprüft.md`, Zeile 53; Buchseite 182.
- **Originalbezeichnung:** `vHüB und hHüB messen und addieren = HüB`
- **Normalisierte Bezeichnung:** `gemessene_hueftbreite_gesamt`

### Buchfassung

```text
28. vHüB und hHüB messen und addieren = HüB. Die ½ HüW aus der Konstruktionstabelle entnehmen und dort den Hüft-Fehlbetrag berechnen (siehe Tabelle rechts):
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `vordere_hueftbreite` | vHüB | nicht angegeben | cm |
| `hintere_hueftbreite` | hHüB | nicht angegeben | cm |

### Formel und Rechenschritte

```text
gemessene_hueftbreite = vordere_hueftbreite + hintere_hueftbreite
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `gemessene_hueftbreite` | Summe der am Vorder- und Rückteil gemessenen Hüftbreiten | nicht angegeben | cm |

- **Abhängigkeiten:** Messung von vHüB und hHüB am konstruierten Vorder- und Rückteil.
- **Gültigkeitsbereich:** Legerer Oberteil-Grundschnitt ohne Taillierung und ohne Brust- oder Schulterabnäher auf S. 182.
- **Technische Randbedingung:** Beide Teilbreiten müssen in derselben Einheit und auf derselben Konstruktionsebene gemessen werden.
- **Offene Fragen oder Widersprüche:** Keine für die Additionsbeziehung. Die Quelle nennt keine einzelnen Messwerte für vHüB und hHüB.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die zwei gemessenen Teilbreiten addieren; die nachfolgende Sollwertkontrolle getrennt in `HOF-B1-S182-F02` ausführen.

## HOF-B1-S182-F02 — Hüftfehlbetrag und hälftige Anstellung

- **Fachlicher Zweck:** Den Hüftfehlbetrag aus gemessener Hüftbreite und halber Soll-Hüftweite bestimmen und seinen positiven hälftigen Betrag für beide Seitenlinien berechnen.
- **Quelle:** `formeln_s182_digital_geprüft.md`, Zeile 24; Originaltranskript `s182_digital_geprüft.md`, Zeilen 60 und 62; Buchseite 182.
- **Originalbezeichnung:** `Hüft-Fehlbetrag (HüFb) = HüB − ½ HüW`
- **Normalisierte Bezeichnung:** `hueftfehlbetrag_und_haelftige_anstellung`

### Buchfassung

```text
`Hüft-Fehlbetrag (HüFb) = HüB − ½ HüW = 47,3 cm − 50,5 cm = −3,2 cm → 3,2 cm ½ = 1,6 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `gemessene_hueftbreite` | HüB | 47,3 | cm |
| `halbe_soll_hueftweite` | ½ HüW | 50,5 | cm |
| `teilungsfaktor_seiten` | ½ | 1/2 | dimensionslos |

### Formel und Rechenschritte

```text
hueftfehlbetrag = gemessene_hueftbreite - halbe_soll_hueftweite
                 = 47,3 cm - 50,5 cm
                 = -3,2 cm

positiver_hueftfehlbetrag = abs(hueftfehlbetrag)
                           = 3,2 cm

anstellung_je_seite = positiver_hueftfehlbetrag / 2
                    = 3,2 cm / 2
                    = 1,6 cm
```

Die technische Betragsbildung bildet den gedruckten Übergang von `−3,2 cm` zu `3,2 cm` ab. Die folgende Konstruktionsanweisung im Transkript verteilt den halben Hüftfehlbetrag auf die Seitenlinien.

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftfehlbetrag` | Differenz aus gemessener Hüftbreite und halber Soll-Hüftweite | −3,2 | cm |
| `anstellung_je_seite` | positiver halber Hüftfehlbetrag für eine Seitenlinie | 1,6 | cm |

- **Abhängigkeiten:** `HOF-B1-S182-F01` für HüB sowie die halbe Hüftweite aus der Konstruktionstabelle.
- **Gültigkeitsbereich:** Hüftweitenkontrolle des legeren Oberteil-Grundschnitts auf S. 182.
- **Technische Randbedingung:** HüB und ½ HüW müssen in derselben Einheit vorliegen. Die Betragsbildung gilt für das gedruckte Beispiel mit negativem HüFb; ein positiver Überschuss ist nicht als Anstellung belegt.
- **Offene Fragen oder Widersprüche:** Das Buch schreibt `3,2 cm ½ = 1,6 cm` ohne sichtbaren Multiplikations- oder Divisionsoperator. Ergebnis und Folgetext belegen die Halbierung. Eine allgemeine Regel für einen positiven oder null großen Hüftfehlbetrag nennt die Quelle nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** HüFb vorzeichenbehaftet erhalten. Die hälftige Anstellung nur im belegten Fehlbetragsfall `hueftfehlbetrag < 0` aus `abs(hueftfehlbetrag) / 2` berechnen; andere Vorzeichen ausdrücklich behandeln statt automatisch zu spiegeln.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s182_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Unvollständiges Zeichnungslabel `+ hHüB messen = HüB`; die vollständige Additionsbeziehung ist in `HOF-B1-S182-F01` abgebildet |
| Zeile 19 | 1 | Tabellarische Wiederholung der in `HOF-B1-S182-F02` vollständig erhaltenen Einsetzrechnung; keine zusätzliche Beziehung |
| **Summe** | **2** | **1 unvollständiges Zeichnungslabel + 1 Wiederholung ausgeschlossen** |
