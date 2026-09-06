# Fachlich normalisierte Formeln — S. 248 und S. 250

Quelle der Normalisierung: `formeln_s248_digital_geprüft.md`, zusätzlicher Anwendungsnachweis in `formeln_s250_digital_geprüft.md`
Originaltranskripte: `s248_digital_geprüft.md`, `s250_digital_geprüft.md`
Buchseiten: Hofenbitzer, Band 1, S. 248 und S. 250
Extraktionsstand: v2

## HOF-B1-S248-F01 — Ärmelkugel-Teilstrecken mit Einhalteweite

- **Fachlicher Zweck:** Drei am Armloch gemessene Teilstrecken um die jeweils gewählte Einhalteweite vergrößern und als Teilstrecken auf die Ärmelkugel übertragen.
- **Quelle:** `formeln_s248_digital_geprüft.md`, Zeilen 9–14; Originaltranskript `s248_digital_geprüft.md`, Zeilen 45–50; zusätzlicher Anwendungsnachweis in `formeln_s250_digital_geprüft.md`, Zeilen 9–10, und `s250_digital_geprüft.md`, Zeilen 49–50; Buchseiten 248 und 250.
- **Originalbezeichnung:** EW; Teilstrecken am Armloch und an der Ärmelkugel
- **Normalisierte Bezeichnung:** `aermelkugel_teilstrecken_mit_einhalteweite`

### Buchfassung

```text
- EW = 0,5 bis 1 cm
- EW = 0,5 bis 1,5 cm
- 14,6 cm + 0,5 = 15,1 cm
- 14,3 cm + 0,7 = 15 cm
- EW = 0,5 bis 1 cm
- 8,9 cm + 0,5 = 9,4 cm
```

Zusätzlicher Anwendungsnachweis auf S. 250 für dieselbe dritte Teilstrecke mit einer anderen zulässigen Einhalteweite:

```text
- EW = 0,5 bis 1 cm
- 8,9 cm + 0,7 = 9,6 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `armloch_teilstrecke_1` | erste Teilstrecke am Armloch | 14,6 | cm |
| `armloch_teilstrecke_2` | zweite Teilstrecke am Armloch | 14,3 | cm |
| `armloch_teilstrecke_3` | dritte Teilstrecke am Armloch | 8,9 | cm |
| `einhalteweite_1` | EW, Bereich 1 | 0,5 bis 1; gewählt 0,5 | cm |
| `einhalteweite_2` | EW, Bereich 2 | 0,5 bis 1,5; gewählt 0,7 | cm |
| `einhalteweite_3` | EW, Bereich 3 | 0,5 bis 1; auf S. 248 gewählt 0,5, auf S. 250 gewählt 0,7 | cm |

### Formel und Rechenschritte

```text
aermelkugel_teilstrecke_1 = armloch_teilstrecke_1 + einhalteweite_1
aermelkugel_teilstrecke_1 = 14,6 cm + 0,5 cm = 15,1 cm

aermelkugel_teilstrecke_2 = armloch_teilstrecke_2 + einhalteweite_2
aermelkugel_teilstrecke_2 = 14,3 cm + 0,7 cm = 15,0 cm

aermelkugel_teilstrecke_3 = armloch_teilstrecke_3 + einhalteweite_3
aermelkugel_teilstrecke_3 = 8,9 cm + 0,5 cm = 9,4 cm
aermelkugel_teilstrecke_3 = 8,9 cm + 0,7 cm = 9,6 cm
```

Die zulässigen Ausgabebereiche aus den gedruckten EW-Bereichen sind:

```text
aermelkugel_teilstrecke_1 = 15,1 bis 15,6 cm
aermelkugel_teilstrecke_2 = 14,8 bis 15,8 cm
aermelkugel_teilstrecke_3 = 9,4 bis 9,9 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchergebnis | Einheit |
|---|---|---:|---|
| `aermelkugel_teilstrecke_1` | erste abzutragende Teilstrecke an der Ärmelkugel | 15,1 | cm |
| `aermelkugel_teilstrecke_2` | zweite abzutragende Teilstrecke an der Ärmelkugel | 15 | cm |
| `aermelkugel_teilstrecke_3` | dritte abzutragende Teilstrecke an der Ärmelkugel | 9,4 auf S. 248; 9,6 auf S. 250 | cm |

- **Abhängigkeiten:** Gemessene Armloch-Teilstrecken des verwendeten Oberteils und je Teilstrecke fachlich gewählte Einhalteweite innerhalb des gedruckten Bereichs.
- **Gültigkeitsbereich:** Ärmel mit Oberarmnaht auf S. 248 und die Teilung des Einnahtärmels zur Vorbereitung einer Ärmelanlage auf S. 250; das Oberteil und ein gegebenenfalls vergrößertes Armloch müssen vor der Übertragung feststehen.
- **Technische Randbedingung:** Die drei Teilstrecken bleiben getrennt. Die Quelle legt keine Regel fest, nach der innerhalb der drei EW-Bereiche `0,5`, `0,7` beziehungsweise `0,5 cm` gewählt werden.
- **Offene Fragen oder Widersprüche:** Keine Rechenwidersprüche. Alle vier gedruckten Additionen stimmen; `14,3 + 0,7` ergibt technisch `15,0 cm`, im Buch steht `15 cm`. Die Auswahl der konkreten Einhalteweiten bleibt fachlich offen, ohne die Additionsbeziehung zu blockieren. S. 248 und S. 250 wählen für dieselbe Ausgangsstrecke von `8,9 cm` unterschiedliche, jeweils innerhalb des gedruckten Bereichs liegende Werte.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Für jede Teilstrecke eine explizit gewählte Einhalteweite verlangen, gegen den jeweiligen Bereich prüfen und keine automatische Auswahlregel erfinden.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s248_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 19–20 | 2 | Produktions- und Zuschnittbeschriftungen für Vorder- und Hinterärmel |
| **Summe** | **2** | **2 Produktions-/Zuschnittzeilen** |

## Extraktionsgrenze

Das Originaltranskript von S. 248 bezeichnet in Zeile 21 die allgemeine Übertragung der Armloch-Teilstrecken auf die Ärmelkugel zuzüglich der entsprechenden Einhalteweiten. Diese Kontextzeile fehlt im verbindlichen Extrakt; sie dient hier nur zur Einordnung der drei vollständig extrahierten Additionen und wurde nicht als zusätzliche Buchfassung gezählt. Das Transkript von S. 250 enthält weitere gemessene Teilstrecken und geometrische Angaben, die nicht als vollständige Rechenbeziehungen extrahiert wurden. Sie wurden nicht stillschweigend normalisiert. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
