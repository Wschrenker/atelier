# Fachlich normalisierte Formeln — S. 309

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s309.md`  
Originaltranskript: `s309.md`  
Buchseite: Hofenbitzer, Band 1, S. 309

## HOF-B1-S309-F01 — Hintere Kragenbreite aus Schulterbreite

- **Fachlicher Zweck:** Die hintere Kragenbreite des Matrosenkragens aus der Kragenbreite an der Schulter mit einem variablen Zuschlag bestimmen.
- **Quelle:** `formeln_s309.md`, Zeilen 7–10 (Buchfassung Zeile 34); Originaltranskript `s309.md`, Zeile 34; Buchseite 309.
- **Originalbezeichnung:** `hKrB = KrB an der Schulter + 0 bis 2 cm`.
- **Normalisierte Bezeichnung:** `hintere_kragenbreite_aus_schulterkragenbreite`

### Buchfassung

```text
Zeichnungsangaben: hKrB = KrB an der Schulter + 0 bis 2 cm; ca. 0,3 bis 0,8 cm; KrB an der Schulter ca. 8 bis 12 cm; nicht überschneiden; ca. 3 bis 4 cm (Ansatzpunkt); ca. 40 bis 80 cm (Bindeband); Bemaßung der Bandspitze mit dem Kürzel „üb“; SuP; SuN; hM; RT-Grundschnitt; VT-Grundschnitt.
```

### Formel und Rechenschritte

```text
hintere_kragenbreite = kragenbreite_schulter + kragenbreiten_zuschlag
```

Der Zuschlag liegt laut Buch zwischen `0` und `2 cm`.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hintere_kragenbreite` | Kragenbreite an der hinteren Mitte | cm |

- **Abhängigkeiten:** Kragenbreite an der Schulter und gewählter Kragenbreitenzuschlag.
- **Gültigkeitsbereich:** Matrosenkragen mit Bindeband.
- **Technische Randbedingung:** Der Zuschlag ist ein Bereich und muss als Modellparameter gewählt werden.
- **Offene Fragen oder Widersprüche:** Keine arithmetische Unklarheit; die Quelle legt keine Auswahlregel innerhalb des Bereichs fest.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `kragenbreiten_zuschlag` auf `0 bis 2 cm` begrenzen; nicht automatisch aus Bindebandlänge oder Ausschnitttiefe ableiten.
