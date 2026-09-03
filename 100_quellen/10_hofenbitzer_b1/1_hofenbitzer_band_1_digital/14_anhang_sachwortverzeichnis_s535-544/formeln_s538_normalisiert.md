# Fachlich normalisierte Formeln — S. 538

Quelle der Normalisierung: `formeln_s538_digital_geprüft.md`
Originaltranskript: `s538_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 538

## HOF-B1-S538-F01 — Brustbreite der DOB-Größentabelle für starke Figuren

- **Fachlicher Zweck:** Die Brustbreite aus dem halben Brustumfang nach Abzug von Rückenbreite und Armdurchmesser bestimmen und die Tabellenwerte kontrollieren.
- **Quelle:** `formeln_s538_digital_geprüft.md`, Zeile 9; Originaltranskript `s538_digital_geprüft.md`, Zeile 34; Buchseite 538.
- **Originalbezeichnung:** `BrB Brustbreite ½BrU − RüB − ArD`.
- **Normalisierte Bezeichnung:** `brustbreite_starke_figuren`

### Buchfassung

```text
| BrB Brustbreite ½BrU − RüB − ArD | 21,7 | 23,2 | 24,8 | 26,3 | 27,9 | 29,4 | 31 | 32,5 | 34,1 |
```

### Eingaben

| Technische Variable | Buchbegriff | Größen 48–64 | Einheit |
|---|---|---|---|
| `brustumfang` | BrU | 110; 116; 122; 128; 134; 140; 146; 152; 158 | cm |
| `rueckenbreite` | RüB | 20,1; 20,8; 21,4; 22,1; 22,7; 23,4; 24,0; 24,7; 25,3 | cm |
| `armdurchmesser` | ArD | 13,2; 14,0; 14,8; 15,6; 16,4; 17,2; 18,0; 18,8; 19,6 | cm |

### Formel und Rechenschritte

```text
brustbreite = (brustumfang / 2) - rueckenbreite - armdurchmesser

Größe 48: (110 cm / 2) - 20,1 cm - 13,2 cm = 21,7 cm
Größe 50: (116 cm / 2) - 20,8 cm - 14,0 cm = 23,2 cm
Größe 52: (122 cm / 2) - 21,4 cm - 14,8 cm = 24,8 cm
Größe 54: (128 cm / 2) - 22,1 cm - 15,6 cm = 26,3 cm
Größe 56: (134 cm / 2) - 22,7 cm - 16,4 cm = 27,9 cm
Größe 58: (140 cm / 2) - 23,4 cm - 17,2 cm = 29,4 cm
Größe 60: (146 cm / 2) - 24,0 cm - 18,0 cm = 31,0 cm
Größe 62: (152 cm / 2) - 24,7 cm - 18,8 cm = 32,5 cm
Größe 64: (158 cm / 2) - 25,3 cm - 19,6 cm = 34,1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Größen 48–64 | Einheit |
|---|---|---|---|
| `brustbreite` | BrB | 21,7; 23,2; 24,8; 26,3; 27,9; 29,4; 31,0; 32,5; 34,1 | cm |

- **Abhängigkeiten:** BrU, RüB und ArD derselben Konfektionsgröße aus der DOB-Größentabelle der starken Figuren.
- **Gültigkeitsbereich:** Tabellenwerte für die Größen 48 bis 64 auf S. 538; keine individuelle Maßableitung außerhalb dieses Maßsatzes.
- **Technische Randbedingung:** Für jede Größe müssen alle drei Eingaben aus derselben Tabellenspalte stammen.
- **Offene Fragen oder Widersprüche:** Keine; alle neun gedruckten BrB-Werte stimmen mit der Formel überein.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Formel von den tabellierten Eingabedaten trennen und spaltenweise Konsistenz prüfen.
