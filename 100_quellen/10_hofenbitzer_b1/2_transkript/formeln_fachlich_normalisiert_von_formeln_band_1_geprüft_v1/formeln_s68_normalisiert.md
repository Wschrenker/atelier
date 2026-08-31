# Fachlich normalisierte Formeln — S. 68

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/03_modelle_roecke_s40-105/formeln_s68.md`
Originaltranskript: `../Band_1_geprüft_v1/s68.md`
Buchseite: Hofenbitzer, Band 1, S. 68

## HOF-B1-S068-F01 — Rocksaumweite mit eingesetzten Godets

- **Fachlicher Zweck:** Die gesamte Saumweite eines Rocks mit eingesetzten Godets aus der Saumweite des Rock-Grundschnitts und den Saumweiten aller Godets bestimmen.
- **Quelle:** `formeln_s68.md`, Zeile 9; Originaltranskript `s68.md`, Zeile 21; Buchseite 68.
- **Originalbezeichnung:** `SaW_Rock = SaW_Godet × Anzahl_Godets + SaW_Rock-GS`
- **Normalisierte Bezeichnung:** `rocksaumweite_mit_godets`

### Buchfassung

```text
SaW_Rock = SaW_Godet × Anzahl_Godets + SaW_Rock-GS
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---|---|
| `saumweite_godet` | `SaW_Godet` | nicht angegeben | cm |
| `anzahl_godets` | `Anzahl_Godets` | nicht angegeben | dimensionslos |
| `saumweite_rock_grundschnitt` | `SaW_Rock-GS` | nicht angegeben | cm |

### Formel und Rechenschritte

```text
rocksaumweite_mit_godets = saumweite_godet * anzahl_godets
                            + saumweite_rock_grundschnitt
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---|---|
| `rocksaumweite_mit_godets` | gesamte Saumweite des Rocks einschließlich der eingesetzten Godets | nicht angegeben | cm |

- **Abhängigkeiten:** Einheitliche `saumweite_godet`, Anzahl der eingesetzten Godets und `saumweite_rock_grundschnitt` vor dem Einsetzen der Godets.
- **Gültigkeitsbereich:** Bahnenrock mit eingesetzten Godets auf S. 68; die Buchfassung verwendet für alle Godets dieselbe Saumweite.
- **Technische Randbedingung:** Alle Längen müssen in derselben Einheit vorliegen; `anzahl_godets` muss als nichtnegative ganze Anzahl geführt werden.
- **Offene Fragen oder Widersprüche:** Keine. Die Buchfassung enthält kein Zahlenbeispiel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bei unterschiedlich breiten Godets die einzelnen Godetsaumweiten summieren; diese Verallgemeinerung ist keine Aussage der vorliegenden Buchformel.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s68.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 14–15 | 2 | Produktionsschnitt- und Zuschnittbeschriftungen mit Halbierungs-, Stückzahl- und Stofflagenkürzeln; keine Berechnung der Rock- oder Godetmaße |
| Zeile 20 | 1 | Quellenfoto-Zuordnung; keine Rechenformel |
| **Summe** | **3** | **3 Fehlklassifikationen ausgeschlossen** |
