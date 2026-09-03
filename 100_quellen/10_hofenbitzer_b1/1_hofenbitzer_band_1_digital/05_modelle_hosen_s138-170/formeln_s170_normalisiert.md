# Fachlich normalisierte Formeln — S. 170

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s170.md`  
Originaltranskript: `s170.md`  
Buchseite: Hofenbitzer, Band 1, S. 170

## HOF-B1-S170-F01 — Mindest-Taillenweite der historischen Sarouelhose

- **Fachlicher Zweck:** Die minimale Taillenweite der historischen Sarouelhose aus einem Viertel des Hüftumfangs bestimmen.
- **Quelle:** `formeln_s170.md`, Zeile 14; Originaltranskript `s170.md`, Zeile 35; Buchseite 170.
- **Originalbezeichnung:** `mind. ¼ HüU + 1 cm`
- **Normalisierte Bezeichnung:** `mindest_taillenweite_historische_sarouelhose`

### Buchfassung

```text
mind. ¼ HüU + 1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | variabel | cm |
| `bund_zuschlag` | `+ 1 cm` | 1 | cm |
| `viertelung` | `¼` | 1/4 | dimensionslos |

### Formel und Rechenschritte

```text
mindest_taillenweite = hueftumfang / 4 + 1 cm
```

`mind.` bleibt als Mindestbedingung erhalten: Die tatsächliche Taillenweite darf größer sein, ist nach dieser Buchzeile aber nicht kleiner als der berechnete Wert.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `mindest_taillenweite` | mindestens erforderliche Taillenweite zum Hineingelangen in die Hose | cm |

- **Abhängigkeiten:** Hüftumfang HüU.
- **Gültigkeitsbereich:** Historische Sarouel-/Harem-/Pluderhose mit Tunnelbund auf S. 170.
- **Technische Randbedingung:** Die Quelle begründet im Seitenkontext, dass der Hüftumfang für den Taillenabschluss maßgebend ist. Eine konkrete Bundkonstruktion oder Rundungsregel ist nicht angegeben.
- **Offene Fragen oder Widersprüche:** Die Quelle sagt nicht, ob `HüU` als voller Taillenabschlussumfang oder als Konstruktionsmaß eines einzelnen Schnittteils verwendet wird. Die Normalisierung übernimmt daher nur die ausgewiesene Beziehung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ergebnis als Mindestwert markieren und nicht automatisch auf einen exakten Taillenumfang festlegen.

## HOF-B1-S170-F02 — Reduzierte halbe Taillenweite für Maschenware

- **Fachlicher Zweck:** Die für Maschenware reduzierte halbe Taillenweite aus dem Mindestviertel des Hüftumfangs und einem materialabhängigen Dehnbetrag darstellen.
- **Quelle:** `formeln_s170.md`, Zeile 30; Originaltranskript `s170.md`, Zeile 67; Buchseite 170.
- **Originalbezeichnung:** `reduzierte ½ TaW = mind. ¼ HüU − prozentualer materialabhängiger Dehnbetrag`
- **Normalisierte Bezeichnung:** `reduzierte_halbe_taillenweite_maschenware`

### Buchfassung

```text
reduzierte ½ TaW = mind. ¼ HüU − prozentualer materialabhängiger Dehnbetrag
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | variabel | cm |
| `dehnbetrag` | prozentualer materialabhängiger Dehnbetrag | variabel | cm |
| `viertelung` | `¼` | 1/4 | dimensionslos |

### Formel und Rechenschritte

```text
reduzierte_halbe_taillenweite = hueftumfang / 4 - dehnbetrag
```

Die Quelle schreibt im zweiten Formelblock nur `mind. ¼ HüU`, ohne den zuvor genannten `+ 1 cm` erneut zu wiederholen. Der Zuschlag aus F01 wird deshalb nicht automatisch in diese Rechnung eingesetzt.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `reduzierte_halbe_taillenweite` | reduzierte halbe Taillenweite für elastisches Material | cm |

- **Abhängigkeiten:** Hüftumfang HüU und materialabhängiger Dehnbetrag; Kontextbezug zu `HOF-B1-S170-F01`.
- **Gültigkeitsbereich:** Modernisierte Sarouelhose aus Maschenware.
- **Technische Randbedingung:** Der Dehnbetrag muss vor der Berechnung als Längenwert aus einer fachlich festgelegten Prozentangabe bestimmt werden. Die Quelle gibt keine Prozentzahl, Materialklasse oder Messmethode an.
- **Offene Fragen oder Widersprüche:** Offen bleibt, ob der `+ 1 cm`-Zuschlag aus F01 Bestandteil der zweiten Beziehung ist oder ob `mind. ¼ HüU` dort bewusst ohne ihn verwendet wird. Ebenso fehlt die Regel zur Umrechnung des Prozentwerts in `cm`.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Erst nach fachlicher Entscheidung implementieren; `dehnbetrag` und die Einbeziehung des `+ 1 cm`-Zuschlags als getrennte Parameter führen.

## Ausgeschlossene Kandidaten

| Extraktzeilen | Anzahl | Ausschlussgrund |
|---|---:|---|
| 25 | 1 | Historischer Material- und Schnittkontext ohne Rechenoperation |
| 48 | 1 | Maßstabsangabe `1:10`; kein Konstruktionswert |
| 53 | 1 | Beschreibender Übergang zur modernen Modellform ohne Rechenoperation |
| 66 | 1 | Maßstabsangabe `1:10`; kein Konstruktionswert |
| **Summe** | **4** | **2 Kontext-/Beschreibungszeilen + 2 Maßstabsangaben ausgeschlossen** |
