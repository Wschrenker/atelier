# Fachlich normalisierte Formeln — S. 212 mit Wiederholungsnachweis S. 214

Primärquelle der Normalisierung: `formeln_s212_digital_geprüft.md`
Zusätzlicher Anwendungsnachweis: `formeln_s214_digital_geprüft.md`
Originaltranskripte: `s212_digital_geprüft.md`, `s214_digital_geprüft.md`
Buchseiten: Hofenbitzer, Band 1, S. 212 und 214
Extraktionsstand: v2

Die beiden Beziehungen erscheinen für den einfachen schmalen Ärmel und für den Blazerärmel mit vorverlegter Ärmelnaht. Jedes Vorkommen bleibt wortgetreu erhalten; technisch entsteht je Beziehung nur eine Formel-ID.

## HOF-B1-S212-F01 — Gesamte Armlochverbreiterung

- **Fachlicher Zweck:** Die gesamte Armlochverbreiterung aus vorderem und hinterem Anteil bestimmen.
- **Quelle:** `formeln_s212_digital_geprüft.md`, Zeile 9, Originaltranskript `s212_digital_geprüft.md`, Zeile 23; zusätzlich `formeln_s214_digital_geprüft.md`, Zeile 14, Originaltranskript `s214_digital_geprüft.md`, Zeile 24; Buchseiten 212 und 214.
- **Originalbezeichnung:** Armloch-Verbreiterung, vordere Verbreiterung, hintere Verbreiterung
- **Normalisierte Bezeichnung:** `gesamte_armlochverbreiterung`

### Buchfassung

Vorkommen S. 212:

```text
- Armloch-Verbreiterung = vordere + hintere Verbreiterung
```

Vorkommen S. 214:

```text
- Armloch-Verbreiterung = vordere + hintere Verbreiterung
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `armlochverbreiterung_vorne` | vordere Verbreiterung | cm |
| `armlochverbreiterung_hinten` | hintere Verbreiterung | cm |

### Formel und Rechenschritte

```text
armlochverbreiterung_gesamt = armlochverbreiterung_vorne + armlochverbreiterung_hinten
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `armlochverbreiterung_gesamt` | gesamte Armlochverbreiterung | cm |

- **Abhängigkeiten:** Vorderer und hinterer Verbreiterungsbetrag müssen aus der Änderung des Oberteil-Armlochs vorliegen.
- **Gültigkeitsbereich:** Ärmelanpassung nach Armlochvertiefung und -verbreiterung; belegt für den einfachen schmalen Ärmel auf S. 212 und den Blazerärmel auf S. 214.
- **Technische Randbedingung:** Beide Anteile müssen sich auf dasselbe geänderte Armloch beziehen.
- **Offene Fragen oder Widersprüche:** Keine in der extrahierten Summenbeziehung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorderen und hinteren Anteil getrennt speichern; die Summe als Kontroll- und Konstruktionswert ausgeben.

## HOF-B1-S212-F02 — Vertiefungsanteil der neuen Ärmelkugellinie

- **Fachlicher Zweck:** Den Anteil der Armlochvertiefung bestimmen, um den die neue Ärmelkugellinie vertieft wird.
- **Quelle:** `formeln_s212_digital_geprüft.md`, Zeile 20, Originaltranskript `s212_digital_geprüft.md`, Zeilen 40–46 und 51; zusätzlich `formeln_s214_digital_geprüft.md`, Zeile 19, Originaltranskript `s214_digital_geprüft.md`, Zeilen 48–54; Buchseiten 212 und 214.
- **Originalbezeichnung:** ½ bis ganze Armlochvertiefung, Normwert ¾
- **Normalisierte Bezeichnung:** `vertiefung_neue_aermelkugellinie`

### Buchfassung

Vorkommen S. 212:

```text
½ bis ganze Armlochvertiefung (Normwert = ¾)
```

Vorkommen S. 214:

```text
- ½ bis ganze Armlochvertiefung (Normwert = ¾)
```

### Eingaben

| Technische Variable | Buchbegriff | Bereich / Normwert | Einheit |
|---|---|---:|---|
| `armlochvertiefung` | Armlochvertiefung | Eingabemaß | cm |
| `vertiefungsfaktor` | ½ bis ganze; Normwert ¾ | 0,5 bis 1; Normwert 0,75 | dimensionslos |

### Formel und Rechenschritte

```text
vertiefung_neue_aermelkugellinie = armlochvertiefung * vertiefungsfaktor
0,5 <= vertiefungsfaktor <= 1
normwert_vertiefungsfaktor = 0,75
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `vertiefung_neue_aermelkugellinie` | Vertiefungsbetrag der neuen Ärmelkugellinie | cm |

- **Abhängigkeiten:** Armlochvertiefung des geänderten Oberteil-Grundschnitts und ausdrücklich gewählter Vertiefungsfaktor.
- **Gültigkeitsbereich:** Ärmelanpassung an ein vertieftes und verbreitertes Armloch; belegt für beide Ärmelvarianten auf S. 212 und 214.
- **Technische Randbedingung:** Der Faktor muss zwischen ½ und 1 liegen. ¾ ist der gedruckte Normwert, keine zwingende Auswahl für jeden Fall.
- **Offene Fragen oder Widersprüche:** Die Quelle beschreibt qualitativ, dass ein kleiner Wert eine flachere Kugel mit kleinerer Einhalteweite und ein großer Wert eine höhere Kugel mit größerer Einhalteweite ergibt; eine automatische Auswahlregel nennt sie nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Faktor als begrenzte Eingabe mit 0,75 als vorgeschlagenem Standardwert führen; keine automatische Wahl aus der Einhalteweite erfinden.

## Ausgeschlossene Kandidaten

### S. 212

| Quelle in `formeln_s212_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 14–15 | 2 | Gemessene halbe Taillen- und Hüftweite des Oberteil-Grundschnitts; direkte Eingabewerte ohne Berechnung für die Ärmelanpassung |
| **Summe S. 212** | **2** | **2 gemessene Eingabewerte** |

### S. 214

| Quelle in `formeln_s214_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Bildnummernverweis `□2+3` und methodische Umstellungsanweisung; Pluszeichen ist kein Rechenoperator |
| **Summe S. 214** | **1** | **1 Bildverweis/Methodenanweisung** |

## Extraktionsgrenze

Die konkreten Abtragungen von ½ beziehungsweise der ganzen Armlochverbreiterung und weitere geometrische Arbeitsschritte stehen nur in den Originaltranskripten. Sie wurden nicht als zusätzliche Buchfassungen aus dem Transkript erfunden.
