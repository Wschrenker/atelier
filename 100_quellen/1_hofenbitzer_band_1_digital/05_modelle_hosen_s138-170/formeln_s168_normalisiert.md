# Fachlich normalisierte Formeln — S. 168

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s168.md`  
Originaltranskript: `s168.md`  
Buchseite: Hofenbitzer, Band 1, S. 168

## HOF-B1-S168-F01 — Wadenhöhe aus Kniehöhe

- **Fachlicher Zweck:** Die Wadenhöhe als halbe Kniehöhe bestimmen.
- **Quelle:** `formeln_s168.md`, Zeile 14; Originaltranskript `s168.md`, Zeile 82; Buchseite 168.
- **Originalbezeichnung:** `WaH = KnH : 2`
- **Normalisierte Bezeichnung:** `wadenhoehe_aus_kniehoehe`

### Buchfassung

```text
WaH = KnH : 2
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `kniehoehe` | KnH | variabel | cm |

### Formel und Rechenschritte

```text
wadenhoehe = kniehoehe / 2
```

Der Divisor `2` ist dimensionslos.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `wadenhoehe` | Abstand beziehungsweise Höhe der Wadenlinie nach Buchbezeichnung WaH | cm |

- **Abhängigkeiten:** Kniehöhe KnH.
- **Gültigkeitsbereich:** Konstruktion der Breeches/Reithose auf S. 168.
- **Technische Randbedingung:** Die Buchnotation `:` wird als Division dargestellt.
- **Offene Fragen oder Widersprüche:** Die Quelle erläutert im Formelblock nicht, von welchem Bezugspunkt KnH gemessen wird. Die Buchbezeichnung wird deshalb unverändert erhalten.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `kniehoehe` als Längenwert validieren; `wadenhoehe = kniehoehe / 2` berechnen.

## HOF-B1-S168-F02 — Weiten an VT und RT aus Kniebund-, Waden- und Fußumfang

- **Fachlicher Zweck:** Die vorgegebenen Weiten an Kniekehle, Wadenhöhe und Saum für Vorderteil und Rückteil der Breeches bestimmen.
- **Quelle:** `formeln_s168.md`, Zeilen 18–23; Originaltranskript `s168.md`, Zeilen 92–97; Buchseite 168.
- **Originalbezeichnung:** Vorderteil jeweils `... : 4 − 1 cm`; Rückteil jeweils `... : 4 + 1 cm`.
- **Normalisierte Bezeichnung:** `breeches_weiten_vt_rt`

### Buchfassung

```text
VT: `(uKnU + 2 cm) : 4 − 1 cm`
VT: `WaU : 4 − 1 cm`
VT: `(FeU + 1 cm) : 4 − 1 cm`
RT: `(uKnU + 2 cm) : 4 + 1 cm`
RT: `WaU : 4 + 1 cm`
RT: `(FeU + 1 cm) : 4 + 1 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `unterknieumfang` | uKnU | variabel | cm |
| `wadenumfang` | WaU | variabel | cm |
| `fussumfang` | FeU | variabel | cm |
| `knie_zuschlag` | `2 cm` innerhalb der uKnU-Beziehung | 2 | cm |
| `fuss_zuschlag` | `1 cm` innerhalb der FeU-Beziehung | 1 | cm |
| `viertelung` | `4` | 4 | dimensionslos |
| `vt_anpassung` | `− 1 cm` | −1 | cm |
| `rt_anpassung` | `+ 1 cm` | +1 | cm |

### Formel und Rechenschritte

```text
vt_knieweite = (unterknieumfang + 2 cm) / 4 - 1 cm
vt_wadenweite = wadenumfang / 4 - 1 cm
vt_fussweite = (fussumfang + 1 cm) / 4 - 1 cm

rt_knieweite = (unterknieumfang + 2 cm) / 4 + 1 cm
rt_wadenweite = wadenumfang / 4 + 1 cm
rt_fussweite = (fussumfang + 1 cm) / 4 + 1 cm
```

Die drei Bezugsumfänge werden jeweils separat verarbeitet. Die Bezeichnungen `VT` und `RT` bleiben als Vorderteil beziehungsweise Rückteil erhalten.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `vt_knieweite` | Weitenanteil des Vorderteils an der Knie-/Kniekehlenlinie | cm |
| `vt_wadenweite` | Weitenanteil des Vorderteils an der Wadenhöhe | cm |
| `vt_fussweite` | Weitenanteil des Vorderteils am Saum/Fußumfang | cm |
| `rt_knieweite` | Weitenanteil des Rückteils an der Knie-/Kniekehlenlinie | cm |
| `rt_wadenweite` | Weitenanteil des Rückteils an der Wadenhöhe | cm |
| `rt_fussweite` | Weitenanteil des Rückteils am Saum/Fußumfang | cm |

- **Abhängigkeiten:** Unterknieumfang uKnU, Wadenumfang WaU und Fußumfang FeU; die sechs Beziehungen gehören zur Schnittentwicklung der Breeches.
- **Gültigkeitsbereich:** Vorgegebene Weiten an Kniekehle, Wadenhöhe und Saum der Breeches/Reithose.
- **Technische Randbedingung:** Die Plus- und Minuswerte von `1 cm` werden als signierte Anpassungen modelliert. Die Quelle erklärt nicht, ob die Weiten anschließend beidseitig oder je Schnittteilkante abgetragen werden; die Ausgaben sind daher nur die ausgewiesenen Buchwerte.
- **Offene Fragen oder Widersprüche:** Die Transkription nennt keine Buchbeispiele mit eingesetzten Umfangswerten. Eine zusätzliche Interpretation der geometrischen Abtragung wird nicht ergänzt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die sechs Ausgaben getrennt führen; keine automatische Umrechnung in Gesamtumfänge oder Kantenabstände vornehmen.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---:|---:|---|
| 13 | 1 | Beschreibender Modell- und Verarbeitungsabschnitt ohne Rechenoperation |
| **Summe** | **1** | **Kontextzeile ausgeschlossen** |
