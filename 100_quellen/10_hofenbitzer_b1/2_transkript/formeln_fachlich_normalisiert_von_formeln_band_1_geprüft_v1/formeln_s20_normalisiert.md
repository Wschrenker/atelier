# Fachlich normalisierte Formeln — S. 20

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s20.md`
Originaltranskript: `../Band_1_geprüft_v1/s20.md`
Buchseite: Hofenbitzer, Band 1, S. 20

Die extrahierten Kandidaten aus `formeln_s20.md`, Zeilen 9, 19–20, 25, 30 und 35, sind Randregister, Maßbereich-Beschriftungen, Nachweistext, eine Fußnote oder eine unvollständige Bezeichnungsliste. Sie sind keine Rechenformeln und werden nicht normalisiert.

## HOF-B1-S020-F01 — Konfektionsgröße aus Brustumfang

- **Fachlicher Zweck:** Die Bezeichnung der Damen-Konfektionsgröße aus dem Brustumfang bestimmen.
- **Quelle:** `formeln_s20.md`, Zeile 14; Originaltranskript `s20.md`, Zeile 18; Buchseite 20.
- **Originalbezeichnung:** `Konfektionsgröße`
- **Normalisierte Bezeichnung:** `konfektionsgroesse`

### Buchfassung

```text
In der Damen-Oberbekleidung (DOB) werden die Größenbezeichnungen von den Maßen KöH, BrU und HüU abgelei­tet (Konfektionsgröße = BrU : 2 - 6 cm).
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Wert in der Buchfassung | Einheit |
|---|---|---|---:|---|
| `brustumfang` | Brustumfang | `BrU` | variabel | cm |
| `halbierungsfaktor` | Halbierung | — | 2 | dimensionslos |
| `groessenversatz` | fester Versatz | — | 6 | cm |

### Formel und Rechenschritte

```text
konfektionsgroesse = (brustumfang / halbierungsfaktor) - groessenversatz
halbierungsfaktor = 2
groessenversatz = 6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `konfektionsgroesse` | numerische Bezeichnung der Damen-Konfektionsgröße | dimensionslos |

- **Abhängigkeiten:** `brustumfang`, `halbierungsfaktor`, `groessenversatz`.
- **Gültigkeitsbereich:** Die Buchfassung nennt die Regel für Größenbezeichnungen der Damen-Oberbekleidung. Sie belegt nicht, wie `KöH` und `HüU` die Auswahl einer Größenreihe beeinflussen.
- **Technische Randbedingung:** `brustumfang` und `groessenversatz` müssen vor der Subtraktion in derselben Längeneinheit stehen; das Ergebnis wird als dimensionslose Größenbezeichnung verwendet.
- **Offene Fragen oder Widersprüche:** Der Satz nennt `KöH`, `BrU` und `HüU` als Ableitungsgrundlage, die gezeigte Rechnung verwendet jedoch nur `BrU`. Die Rolle von `KöH` und `HüU` ist in dieser Formel nicht bestimmt. Die Tabelle auf derselben Seite enthält nur gerade Größen; eine Rundungs- oder Zuordnungsregel für abweichende Brustumfänge ist nicht angegeben.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Rechenformel kann abgebildet werden, darf aber ohne separate belegte Auswahl- und Rundungsregeln noch keine vollständige Konfektionsgrößen-Zuordnung steuern.
