# Fachlich normalisierte Formeln — S. 176

Quelle der Normalisierung: `formeln_s176.md`
Originaltranskript: `s176.md`
Buchseite: Hofenbitzer, Band 1, S. 176

## HOF-B1-S176-F01 — Brustumfangszugabe aus der Passformklasse

- **Fachlicher Zweck:** Die Zugabe für den ganzen Brustumfang aus der auf den halben Brustumfang bezogenen Passformklasse bestimmen.
- **Quelle:** `formeln_s176.md`, Zeile 9; Originaltranskript `s176.md`, Zeile 23; Buchseite 176.
- **Originalbezeichnung:** `PK5  2 × 5 cm = 10 cm BrW-Zugabe`
- **Normalisierte Bezeichnung:** `brustumfang_zugabe_aus_passformklasse`

### Buchfassung

```text
> **PK5  2 × 5 cm = 10 cm BrW-Zugabe**  (Marker ⑥)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `passformklasse` | PK | 5 | cm am halben Brustumfang |
| `anzahl_halbe_umfaenge` | `2 ×` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
brustumfang_zugabe = anzahl_halbe_umfaenge * passformklasse
                    = 2 * 5 cm
                    = 10 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `brustumfang_zugabe` | Zugabe für den ganzen Brustumfang | 10 | cm |

- **Abhängigkeiten:** Gewählte Passformklasse.
- **Gültigkeitsbereich:** Hofenbitzer-Passformklassen für Oberteil-Grundschnitte.
- **Technische Randbedingung:** Die PK-Ziffer bezeichnet laut Buch die Zugabe für den halben Brustumfang; für den ganzen Umfang wird sie verdoppelt.
- **Offene Fragen oder Widersprüche:** Keine; `2 × 5 cm = 10 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** PK als halbumfangsbezogenen Wert speichern und die Ganzumfangszugabe ausdrücklich daraus berechnen.

## HOF-B1-S176-F02 — Zugabensatz nach Passformklasse

- **Fachlicher Zweck:** Die zum gewählten Oberteil-Grundschnitt gehörenden Umfangs-, Tiefen- und Brustweitenzugaben als zusammengehörigen Tabellensatz auswählen.
- **Quelle:** `formeln_s176.md`, Zeilen 19–29; Originaltranskript `s176.md`, Zeilen 67–77; Buchseite 176.
- **Originalbezeichnung:** `Zugabentabelle für Oberteil-Konstruktionen`
- **Normalisierte Bezeichnung:** `oberteil_zugabensatz_nach_passformklasse`

### Buchfassung

```text
| 0 | 0 | 0 | 0 | 0 - 0,5 | 0 | 0 | 0 - 0,4 | 0 |
| 1 | 2 | 0 - 2 | 0 - 2 | 0,2 - 0,7 | 0,1 | 0,3 | 0,6 | 0,1 |
| 2 | 4 | 2 - 4 | 2 - 4 | 0,5 - 1 | 0,3 | 0,9 | 0,8 | 0,2 |
| 3 | 6 | 4 - 6 | 4 - 6 | 1,3 | 0,5 | 1,5 | 1 | 0,3 |
| 4 | 8 | 4 - 8 | 4 - 8 | 1,7 | 0,8 | 2 | 1,2 | 0,4 |
| 5 | 10 | 8 - 12 | 6 - 8 | 2,1 | 1,1 | 2,5 | 1,4 | 0,5 |
| 6 | 12 | 8 - 16 | 6 - 10 | 2,5 | 1,4 | 3 | 1,6 | 0,6 |
| 7 | 14 | 12 - 16 | 8 - 12 | 3 | 1,6 | 3,6 | 1,8 | 0,7 |
| 8 | 16 | 12 - 20 | 8 - 16 | 3,5 | 1,8 | 4,2 | 2 | 0,8 |
| 9 | 18 | 12 - 20 | 10 - 20 | 4 | 2 | 5 | 2 | 0,9 |
| 10 | 20 | 16 - 24 | 10 - 24 | 4,5 | 2,2 | 5,8 | 2 | 1 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wertebereich | Einheit |
|---|---|---:|---|
| `passformklasse` | Passform-Klasse | 0 bis 10 | dimensionsloser Klassenindex |

Spaltenfolge des Rückgabesatzes: `BrU`, `TaU`, `HüU`, `AIT`, `RüB`, `ArD`, `BrB`, `SuB`; alle Werte in Zentimetern. Bereichsangaben bleiben Bereiche.

### Formel und Rechenschritte

```text
zugabensatz = tabellenzeile(passformklasse)

Beispiel PK 4:
BrU = 8 cm
TaU = 4 cm bis 8 cm
HüU = 4 cm bis 8 cm
AIT = 1,7 cm
RüB = 0,8 cm
ArD = 2 cm
BrB = 1,2 cm
SuB = 0,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `brustumfang_zugabe` | Zugabe für den ganzen Brustumfang | cm |
| `taillenumfang_zugabe` | Zugabe beziehungsweise Zugabebereich für den ganzen Taillenumfang | cm |
| `hueftumfang_zugabe` | Zugabe beziehungsweise Zugabebereich für den ganzen Hüftumfang | cm |
| `armlochtiefe_zugabe` | Längenzugabe zur Armlochtiefe | cm |
| `rueckenbreite_zugabe` | Zugabe zur halben Rückenbreite | cm |
| `armdurchmesser_zugabe` | Zugabe zum Armdurchmesser | cm |
| `brustbreite_zugabe` | Zugabe zur halben Brustbreite | cm |
| `schulterbreite_zugabe` | Zugabe zur Schulterbreite | cm |

- **Abhängigkeiten:** Passformklasse und fachliche Auswahl innerhalb gedruckter Wertebereiche.
- **Gültigkeitsbereich:** Oberteil-Konstruktionen der Passformklassen 0 bis 10.
- **Technische Randbedingung:** Die Tabelle ist eine verbindliche Zuordnung, keine interpolierbare Zahlenfolge. `BrU`, `TaU`, `HüU` und `AIT` gelten laut Tabellenkopf für den ganzen Schnitt; `RüB`, `ArD`, `BrB` und `SuB` gehören zur Gruppe „BrW-Zugaben (für ½ Schnitt)".
- **Offene Fragen oder Widersprüche:** Das Buch nennt keine Auswahlregel innerhalb der gedruckten Bereiche. Für PK 8 bezeichnet die Anwendungstabelle die Jacke trotz der umgebenden Reihenfolge als „halbweit"; dieser Kontextfehler verändert die Zahlenzeile der Zugabentabelle nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als unveränderte Lookup-Tabelle mit Bereichswerten modellieren; keine Mittelwerte, Interpolation oder automatische Bereichsauswahl erfinden.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s176.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Tabellenkopf mit Spaltengruppen und Kürzeln; notwendiger Lesekontext, aber keine eigene Rechenformel |
| Zeile 34 | 1 | redaktionelle Notiz zu Kreismarkern der PK5-Zeile; keine zusätzliche Buchformel |
| **Summe** | **2** | **1 Tabellenkopf und 1 redaktionelle Prüfnotiz ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s176.md` beschreibt in den Zeilen 15, 19, 21 und 89–94 weitere allgemeine Beziehungen zwischen Körpermaßen, Zugaben und Konstruktionsmaßen sowie die Verwendung korrigierter Balancemaße. Diese Beziehungen fehlen als Buchfassungen im verbindlichen Extrakt und wurden nicht stillschweigend normalisiert. Die Anwendungstabelle der Passformklassen ist ebenfalls nicht Teil des extrahierten Formelblocks; ihre mögliche PK8-Inkonsistenz bleibt deshalb Kontext, nicht Bestandteil einer erfundenen Formel.
