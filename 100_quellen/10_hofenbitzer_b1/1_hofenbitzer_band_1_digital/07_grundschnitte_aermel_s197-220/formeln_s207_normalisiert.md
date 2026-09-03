# Fachlich normalisierte Formeln — S. 207 mit Wiederholungsnachweis S. 208

Primärquelle der Normalisierung: `formeln_s207_digital_geprüft.md`
Zusätzlicher Anwendungsnachweis: `formeln_s208_digital_geprüft.md`
Originaltranskripte: `s207_digital_geprüft.md`, `s208_digital_geprüft.md`
Buchseiten: Hofenbitzer, Band 1, S. 207–208
Extraktionsstand: v2

Die identischen Rechnungen erscheinen in zwei verschiedenen Ärmelvarianten. Sie bleiben je Vorkommen wortgetreu erhalten, erhalten aber nur je eine Formel-ID, damit keine doppelte technische Regel entsteht.

## HOF-B1-S207-F01 — Einhalteweite mit mittlerem hinterem Anteil

- **Fachlicher Zweck:** Die gesamte Einhalteweite aus vorderem Anteil und gewähltem hinterem Anteil bestimmen.
- **Quelle:** `formeln_s207_digital_geprüft.md`, Zeilen 20–21, Originaltranskript `s207_digital_geprüft.md`, Zeilen 57–58; zusätzlich `formeln_s208_digital_geprüft.md`, Zeilen 20–21, Originaltranskript `s208_digital_geprüft.md`, Zeilen 63–64; Buchseiten 207–208.
- **Originalbezeichnung:** `EW`, `me`
- **Normalisierte Bezeichnung:** `einhalteweite_aus_vorderem_und_hinterem_anteil`

### Buchfassung

Vorkommen S. 207:

```text
- `EW = 2,6 cm + 0,7 cm = 3,3 cm`
- me = 2,6 cm
```

Vorkommen S. 208:

```text
- `EW = 2,6 cm + 0,7 cm = 3,3 cm`
- me = 2,6 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderer_einhalteweitenanteil` | im Zeichnungslabel `me` | 2,6 | cm |
| `hinterer_einhalteweitenanteil` | mittlere EW-Zugabe | 0,7 | cm |

### Formel und Rechenschritte

```text
einhalteweite = 2,6 cm + 0,7 cm = 3,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `einhalteweite` | gesamte EW | 3,3 | cm |

- **Abhängigkeiten:** Der Transkripttext bestimmt 0,5 cm bei kleiner, 1 cm bei großer und 0,7 cm bei mittlerer EW; das Zeichnungslabel liefert 2,6 cm als ersten Summanden.
- **Gültigkeitsbereich:** Einnaht-Ärmel für natürliche Armform S. 207 und Blazerärmel für schlecht dehnbare Stoffe S. 208.
- **Technische Randbedingung:** Die Auswahl klein/mittel/groß muss ausdrücklich vorgegeben werden; aus der Quelle wird keine automatische Schwelle abgeleitet.
- **Offene Fragen oder Widersprüche:** Das Kürzel `me` ist im Extrakt nicht erklärt. Die Zahlenrechnung selbst ist eindeutig und wird durch beide Varianten belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Eine gemeinsame Regel verwenden und die Variantenseiten als zwei Provenienznachweise erhalten.

## HOF-B1-S207-F02 — Hintere Ärmelpunktstrecke mit mittlerem Einhalteweitenanteil

- **Fachlicher Zweck:** Die hintere Ärmelpunktstrecke aus hinterer Achselstrecke und mittlerem Einhalteweitenanteil bestimmen.
- **Quelle:** `formeln_s207_digital_geprüft.md`, Zeile 26, Originaltranskript `s207_digital_geprüft.md`, Zeile 64; zusätzlich `formeln_s208_digital_geprüft.md`, Zeile 26, Originaltranskript `s208_digital_geprüft.md`, Zeile 70; Buchseiten 207–208.
- **Originalbezeichnung:** `hAchsel`, `EW 0,7 cm`, `hÄP`
- **Normalisierte Bezeichnung:** `hintere_aermelpunktstrecke_mittlere_einhalteweite`

### Buchfassung

Vorkommen S. 207:

```text
- `8,5 cm + 0,7 cm = 9,5 cm`
```

Vorkommen S. 208:

```text
- `8,5 cm + 0,7 cm = 9,5 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hintere_achselstrecke` | hAchsel | 8,5 | cm |
| `einhalteweitenanteil_hinten` | mittlere EW-Zugabe | 0,7 | cm |

### Formel und Rechenschritte

```text
rechnerisches_ergebnis = 8,5 cm + 0,7 cm = 9,2 cm
gedrucktes_ergebnis = 9,5 cm
abweichung = 9,5 cm - 9,2 cm = 0,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hintere_aermelpunktstrecke_rechnerisch` | Summe der gedruckten Operanden | 9,2 | cm |
| `hintere_aermelpunktstrecke_gedruckt` | gedrucktes Ergebnis | 9,5 | cm |

- **Abhängigkeiten:** hAchsel 8,5 cm und der für mittlere EW gewählte Anteil 0,7 cm.
- **Gültigkeitsbereich:** Hinterer Ärmelpunkt der Varianten auf S. 207 und S. 208.
- **Technische Randbedingung:** Operandenpfad und Druckergebnis bis zur Quellenklärung getrennt erhalten.
- **Offene Fragen oder Widersprüche:** `8,5 + 0,7` ergibt `9,2`, nicht `9,5`. Derselbe Widerspruch ist auf beiden Seiten gedruckt; Summand oder Ergebnis muss am Buch fachlich geprüft werden.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht als freigegebene Regel implementieren, bevor der Widerspruch geklärt ist.

## Ausgeschlossene Kandidaten

### S. 207

| Quelle in `formeln_s207_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 9–10 | 2 | Definition der Ärmelnaht als Parallele und Bezeichnung des Abnäherschenkels; geometrische Labels ohne Berechnung |
| Zeile 15 | 1 | Isolierter Messwert `me = 13,8 cm`; kein berechneter Output |
| Zeile 31 | 1 | Bildnummernverweis `□7+8` und Spiegelanweisung; Pluszeichen ist kein Rechenoperator |
| **Summe S. 207** | **4** | **2 geometrische Definitionen + 1 isolierter Messwert + 1 Bildverweis/Spiegelanweisung** |

### S. 208

| Quelle in `formeln_s208_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Bezeichnung des Abnäherschenkels; geometrisches Label ohne Berechnung |
| Zeilen 14–15 | 2 | Isolierte Messwerte `me = 14,4 cm` und `me = 13,8 cm`; keine berechneten Outputs |
| Zeile 31 | 1 | Bildnummernverweis `□7+8` und Spiegelanweisung; Pluszeichen ist kein Rechenoperator |
| **Summe S. 208** | **4** | **1 geometrische Definition + 2 isolierte Messwerte + 1 Bildverweis/Spiegelanweisung** |

## Extraktionsgrenze

Die Auswahlregel für 0,5 cm, 0,7 cm oder 1 cm steht nur in den Originaltranskripten. Sie dient als fachlicher Kontext, ist aber keine zusätzliche Buchfassung. Weitere Konstruktionsbeziehungen der beiden Seiten wurden nicht stillschweigend aus den Transkripten in die Normalisierung übernommen.
