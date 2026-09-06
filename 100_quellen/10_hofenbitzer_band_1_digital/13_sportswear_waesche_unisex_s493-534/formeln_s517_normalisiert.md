# Fachlich normalisierte Formeln — S. 517

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s517.md`
Originaltranskript: `s517.md`
Buchseite: Hofenbitzer, Band 1, S. 517

Die Seite setzt die Modellentwicklung der **Sportjacke mit Raglanärmel und Kragen** von S. 516 fort. Der extrahierte Formelbestand betrifft den Saumbund, das Ärmelbündchen und die Dehnung von Vorder-/Rückenteil-Halsloch sowie Kragenansatz. Die Produktionsschnitt-Beschriftungen und die Konstruktionsangabe zur Streifennaht sind keine eigenständigen Rechenformeln und werden unten ausgeschlossen.

## HOF-B1-S517-F01 — Saumweite aus vier Ansatznahtlängen

- **Fachlicher Zweck:** Die gesamte Ansatznahtlänge für den Saumbund aus vier gleich großen Teilstrecken bestimmen.
- **Quelle:** `formeln_s517.md`, Zeile 9; Originaltranskript `s517.md`, Zeile 38; Buchseite 517.
- **Originalbezeichnung:** `SaW = 4 · 24 cm = 96 cm`
- **Normalisierte Bezeichnung:** `saumweite_sportjacke`

### Buchfassung

```text
SaW = 4 · 24 cm = 96 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `teilnahtlaenge` | `24 cm` | 24 | cm |
| `anzahl_teilnaehte` | `4` | 4 | dimensionslos |

### Formel und Rechenschritte

```text
saumweite = anzahl_teilnaehte * teilnahtlaenge
           = 4 * 24 cm
           = 96 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `saumweite` | gesamte Ansatznahtlänge am Saum für den Saumbund | 96 | cm |

- **Abhängigkeiten:** Vier gleich angesetzte Teilstrecken von jeweils `24 cm`.
- **Gültigkeitsbereich:** Saumbund der Sportjacke, Größe 38, Zeichnung/Konstruktion auf S. 517.
- **Technische Randbedingung:** Die Zahl `4` ist hier ein Rechenfaktor, nicht die Stückzahl eines Produktionsschnittteils.
- **Offene Fragen oder Widersprüche:** Keine; die Rechnung ist eindeutig und ergibt den gedruckten Wert.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Ansatznahtlängen als Liste oder Summe modellieren; `4 * 24 cm` ist nur dann zulässig, wenn alle vier Teilstrecken gleich lang sind.

## HOF-B1-S517-F02 — Saumbundweite aus der Saumweite

- **Fachlicher Zweck:** Die Saumweite um den materialabhängigen Dehnungsbetrag von 3 % reduzieren und daraus die Saumbundweite bestimmen.
- **Quelle:** `formeln_s517.md`, Zeilen 11–13; Originaltranskript `s517.md`, Zeilen 40–42; Buchseite 517.
- **Originalbezeichnung:** `BuW = SaW · (100 % − 3 %) : 100 % = 96 cm · 0,97 = 93,1 cm`
- **Normalisierte Bezeichnung:** `saumbundweite_sportjacke`

### Buchfassung

```text
BuW = SaW · (100 % − 3 %) : 100 %
     = 96 cm · 0,97
     = 93,1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `saumweite` | SaW | 96 | cm |
| `dehnungsanteil` | `3 %` | 3 | Prozent |
| `dehnungsfaktor` | `0,97` | 0,97 | dimensionslos |

### Formel und Rechenschritte

```text
saumbundweite = saumweite * (1 - dehnungsanteil / 100)
              = 96 cm * (1 - 3 / 100)
              = 96 cm * 0,97
              = 93,12 cm

gedruckter Buchwert: 93,1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Exakt / gedruckt | Einheit |
|---|---|---:|---|
| `saumbundweite` | Länge des Saumbundstreifens nach materialbedingter Reduktion | 93,12 / 93,1 | cm |

- **Abhängigkeiten:** `HOF-B1-S517-F01` liefert `SaW = 96 cm`.
- **Gültigkeitsbereich:** Saumbund der Sportjacke; der Dehnungsbetrag ist materialbedingt zu wählen.
- **Technische Randbedingung:** Das Buch nennt allgemein `−0 % bis −5 %` und verwendet im Beispiel `−3 %`. Der konkrete Wert `3 %` ist daher eine Buchbeispiel-Eingabe, keine allgemeine feste Regel.
- **Offene Fragen oder Widersprüche:** `96 · 0,97 = 93,12 cm`, gedruckt ist `93,1 cm`. Eine Rundungsregel ist nicht angegeben; exakter und gedruckter Wert bleiben getrennt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Dehnungsanteil als Materialparameter führen und erst bei der Ausgabe nach einer ausdrücklich festgelegten Rundungsregel runden.

## HOF-B1-S517-F03 — Ärmelbündchenweite aus der Ansatznaht

- **Fachlicher Zweck:** Die Länge des Ärmelbündchens aus der gemessenen Ärmel-Ansatznaht durch 3 % Materialreduktion bestimmen.
- **Quelle:** `formeln_s517.md`, Zeilen 15–17; Originaltranskript `s517.md`, Zeilen 48 und 50–52; Buchseite 517.
- **Originalbezeichnung:** `BuW = ÄSaW · (100 % − 3 %) : 100 % = 24 cm · 0,97 = 23,3 cm`
- **Normalisierte Bezeichnung:** `aermelbuendchenweite_sportjacke`

### Buchfassung

```text
ÄSaW = 24 cm

BuW = ÄSaW · (100 % − 3 %) : 100 %
     = 24 cm · 0,97
     = 23,3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `aermelsaumweite` | ÄSaW | 24 | cm |
| `dehnungsanteil` | `3 %` | 3 | Prozent |
| `dehnungsfaktor` | `0,97` | 0,97 | dimensionslos |

### Formel und Rechenschritte

```text
aermelbuendchenweite = aermelsaumweite * (1 - dehnungsanteil / 100)
                     = 24 cm * 0,97
                     = 23,28 cm

gedruckter Buchwert: 23,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Exakt / gedruckt | Einheit |
|---|---|---:|---|
| `aermelbuendchenweite` | Länge des Ärmelbündchenstreifens nach Materialreduktion | 23,28 / 23,3 | cm |

- **Abhängigkeiten:** `ÄSaW = 24 cm` ist die Ansatznahtlänge des Ärmels; der Wert steht als direkte Eingabe vor der Formel.
- **Gültigkeitsbereich:** Ärmelbündchen der Sportjacke, Größe 38.
- **Technische Randbedingung:** Im Fließtext heißt die Ausgabe `BuW`; die Zeichnung □7 bezeichnet die entsprechende Größe als `BüW` („Bündchenweite“). Beide Schreibungen stehen laut geprüftem Transkript im Buch. Technisch wird die Ausgabe hier wegen der Funktion eindeutig als `aermelbuendchenweite` bezeichnet.
- **Offene Fragen oder Widersprüche:** `24 · 0,97 = 23,28 cm`, gedruckt ist `23,3 cm`. Eine Rundungsregel ist nicht angegeben. Die Quelle legt außerdem nicht fest, ob der Dehnungsbetrag für jedes Material aus einer separaten Probe zu bestimmen ist; sie nennt nur die materialbedingte Auswahl.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Ausgabe nicht mit der Saumbundweite gleichsetzen; dieselbe Reduktionslogik wirkt auf eine andere Ansatznahtlänge.

## HOF-B1-S517-F04 — Vorderes Halsloch unter Materialreduktion

- **Fachlicher Zweck:** Die vordere Halsloch-Länge für den Strick-Stehkragen um 3 % reduzieren.
- **Quelle:** `formeln_s517.md`, Zeilen 19–22; Originaltranskript `s517.md`, Zeilen 58–59; Buchseite 517.
- **Originalbezeichnung:** `vHlL = 9,4 cm · 0,97 = 9,1 cm`
- **Normalisierte Bezeichnung:** `reduzierte_vordere_halslochlaenge_sportjacke`

### Buchfassung

```text
vHlL = 9,4 cm · 0,97 = 9,1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `vordere_halslochlaenge` | vHlL | 9,4 | cm |
| `dehnungsfaktor` | `0,97` | 0,97 | dimensionslos |

### Formel und Rechenschritte

```text
reduzierte_vordere_halslochlaenge = vordere_halslochlaenge * 0,97
                                   = 9,4 cm * 0,97
                                   = 9,118 cm

gedruckter Buchwert: 9,1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Exakt / gedruckt | Einheit |
|---|---|---:|---|
| `reduzierte_vordere_halslochlaenge` | für den Kragenansatz reduzierte vordere Halsloch-Länge | 9,118 / 9,1 | cm |

- **Abhängigkeiten:** vordere Halsloch-Länge `vHlL = 9,4 cm` aus der Halsloch-/Kragendarstellung der Sportjacke.
- **Gültigkeitsbereich:** Vorderer Ansatz des Strick-Stehkragens Nr. 5.
- **Technische Randbedingung:** Der Dehnungsfaktor `0,97` entspricht dem im Beispiel für Saum- und Ärmelbündchen verwendeten `−3 %`.
- **Offene Fragen oder Widersprüche:** Die exakte Rechnung ergibt `9,118 cm`, gedruckt ist `9,1 cm`; eine Rundungsregel fehlt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Reduktion auf der vorderen und hinteren Halslochseite getrennt berechnen; erst danach den Kragenweg konstruieren.

## HOF-B1-S517-F05 — Hinteres Halsloch unter Materialreduktion

- **Fachlicher Zweck:** Die hintere Halsloch-Länge für den Strick-Stehkragen um 3 % reduzieren.
- **Quelle:** `formeln_s517.md`, Zeilen 19–22; Originaltranskript `s517.md`, Zeilen 58–59; Buchseite 517.
- **Originalbezeichnung:** `hHlL = 9,8 cm · 0,97 = 9,5 cm`
- **Normalisierte Bezeichnung:** `reduzierte_hintere_halslochlaenge_sportjacke`

### Buchfassung

```text
hHlL = 9,8 cm · 0,97 = 9,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hintere_halslochlaenge` | hHlL | 9,8 | cm |
| `dehnungsfaktor` | `0,97` | 0,97 | dimensionslos |

### Formel und Rechenschritte

```text
reduzierte_hintere_halslochlaenge = hintere_halslochlaenge * 0,97
                                  = 9,8 cm * 0,97
                                  = 9,506 cm

gedruckter Buchwert: 9,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Exakt / gedruckt | Einheit |
|---|---|---:|---|
| `reduzierte_hintere_halslochlaenge` | für den Kragenansatz reduzierte hintere Halsloch-Länge | 9,506 / 9,5 | cm |

- **Abhängigkeiten:** hintere Halsloch-Länge `hHlL = 9,8 cm` aus der Halsloch-/Kragendarstellung der Sportjacke.
- **Gültigkeitsbereich:** Hinterer Ansatz des Strick-Stehkragens Nr. 5.
- **Technische Randbedingung:** Der Buchwert ist ein Beispiel für denselben materialbedingten Dehnungsfaktor wie bei Saumbund und Ärmelbündchen.
- **Offene Fragen oder Widersprüche:** Die exakte Rechnung ergibt `9,506 cm`, gedruckt ist `9,5 cm`; eine Rundungsregel fehlt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zusammen mit `HOF-B1-S517-F04` als zwei getrennte Kragenansatzlängen führen; die vordere und hintere Halslochseite sind nicht zu mitteln.

## Ausgeschlossene Kandidaten

| Seite / Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| S. 516, Zeilen 3, 29 und 31 | 3 | Kapitelrubrik, direkte Halsloch-/Positionsangaben sowie Produktionsschnittteile; keine Rechenoperation |
| S. 517, Zeilen 7–8 | 2 | Produktionsschnittteile `Sportjacke VT 2×-p G 38` und `Sportjacke RT 1× G 38`; `2×-p` beziehungsweise `1×` sind Zuschnittangaben, keine Rechenfaktoren |
| S. 517, Zeile 15 | 1 | Direkte Eingabe `ÄSaW = 24 cm`; die Größe wird als Operand der Formel verwendet, berechnet aber selbst keine Ausgabe |
| S. 517, Zeilen 25–27 | 3 | Konstruktions-/Produktionsbeschriftungen für Saumbund, Ärmelbündchen und Kragen; keine eigenständige Rechenoperation |
| **Summe** | **9** | **3 S.-516-Kontext-/Labelzeilen + 2 Produktionsschnittteile + 1 direkte Eingabe + 3 Konstruktions-/Produktionsbeschriftungen** |

## Prüfhinweise

1. Die vier Formeln verwenden denselben Buchweg zur Materialreduktion: `Ausgangslänge · (100 % − 3 %) : 100 %`, technisch `Ausgangslänge · 0,97`. Der Wert `3 %` ist im Buch ein Beispiel innerhalb des Bereichs `0 % bis 5 %`.
2. Die exakten Ergebnisse und die gedruckten Werte weichen bei den drei reduzierten Längen durch Rundung beziehungsweise Abschneiden ab: `93,12 → 93,1 cm`, `23,28 → 23,3 cm`, `9,118 → 9,1 cm` und `9,506 → 9,5 cm`. Da keine Rundungsregel gedruckt ist, werden beide Werte getrennt erhalten.
3. `BuW` bezeichnet im Fließtext die Bundweite des Saumbunds; in □7 steht für das Ärmelbündchen `BüW` (Bündchenweite). Die Schreibungsabweichung wird nicht als fachlicher Widerspruch behandelt, weil die Funktionen durch den jeweiligen Abschnitt eindeutig sind.
4. Der Kragenverweis ist im Buch uneinheitlich: Im Fließtext steht „Kragen Nr. 5 auf Seite 297“, in der Bildunterschrift □5 „Vergleiche Seite 293“. Beide gedruckten Angaben bleiben im Transkript erhalten; die fünf normalisierten Formeln hängen nur von den auf S. 517 gedruckten Halslochwerten und dem Dehnungsfaktor ab.
5. Die Extraktionsgrenze bleibt bestehen: Die ursprünglichen Konstruktionsschritte zu Raglanärmel, Streifenführung, Abnäherentfernung und Kragenform werden nicht als zusätzliche Buchformeln ergänzt, wenn sie im verbindlichen Extrakt keine Rechenzeile mit benannter Eingabe und Ausgabe bilden.
