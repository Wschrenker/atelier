# Fachlich normalisierte Formeln — S. 45

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/03_modelle_roecke_s40-105/formeln_s45.md`
Originaltranskript: `../hofenbitzer_band_1_digital/03_modelle_roecke_s40-105/s45.md`
Buchseite: Hofenbitzer, Band 1, S. 45

## HOF-B1-S045-F01 — Taillenradius der Halbglocke

- **Fachlicher Zweck:** Inneren Radius des halbkreisförmigen Taillenbogens einer Halbglocke aus der Taillenweite bestimmen.
- **Quelle:** `formeln_s45.md`, Zeilen 7–12; Originaltranskript `s45.md`, Zeilen 32–37; Buchseite 45.
- **Originalbezeichnung:** `rTaW = TaW : π`
- **Normalisierte Bezeichnung:** `taillenradius_halbglocke`

### Buchfassung

```text
rTaW = TaW : π
     = 72 cm : 3,14
     = 22,9 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenweite` | TaW | 72 | cm |
| `pi_buch` | π | 3,14 | dimensionslos |

### Formel und Rechenschritte

```text
taillenradius_halbglocke = taillenweite / pi_buch
                          = 72 cm / 3,14
                          = 22,929... cm
Buchwert                 = 22,9 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenradius_halbglocke` | Innerer Radius des halbkreisförmigen Taillenbogens | 22,9 | cm |

- **Abhängigkeiten:** `taillenweite` und `pi_buch`.
- **Gültigkeitsbereich:** Halbglocke als halber Kreisring auf S. 45.
- **Technische Randbedingung:** `pi_buch` darf nicht `0` sein. Das Buch verwendet `π = 3,14` und gibt den Radius auf eine Dezimalstelle an.
- **Offene Fragen oder Widersprüche:** Keine. Der fehlende Faktor `2` gegenüber der Vollglocke ist fachlich durch den halben Taillenkreis begründet.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Kreisring-Anteil als ausdrückliche Varianteninformation führen; Voll- und Halbglocke dürfen nicht dieselbe Radiusformel verwenden.

## HOF-B1-S045-F02 — Saumradius der Halbglocke

- **Fachlicher Zweck:** Äußeren Radius des Saumbogens als Summe aus Taillenradius und Modelllänge bestimmen.
- **Quelle:** `formeln_s45.md`, Zeilen 14–19; Originaltranskript `s45.md`, Zeilen 39–41; Buchseite 45.
- **Originalbezeichnung:** `rSaW = rTaW + MoL`
- **Normalisierte Bezeichnung:** `saumradius_halbglocke`

### Buchfassung

```text
rSaW = rTaW + MoL
     = 22,9 cm + 50 cm
     = 72,9 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenradius` | rTaW | 22,9 | cm |
| `modelllaenge` | MoL | 50 | cm |

### Formel und Rechenschritte

```text
saumradius_halbglocke = taillenradius + modelllaenge
                       = 22,9 cm + 50 cm
                       = 72,9 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumradius_halbglocke` | Äußerer Radius bis zum Saum des halben Kreisrings | 72,9 | cm |

- **Abhängigkeiten:** `HOF-B1-S045-F01` und gewählte `modelllaenge`.
- **Gültigkeitsbereich:** Halbglocke auf S. 45; die Seite nennt dieselbe Beziehung auch für eine Volantlänge.
- **Technische Randbedingung:** Beide Eingaben müssen dieselbe Längeneinheit tragen und die Modelllänge darf nicht negativ sein.
- **Offene Fragen oder Widersprüche:** Keine; `22,9 cm + 50 cm = 72,9 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Innen- und Außenradius vom selben Kreismittelpunkt aus aufbauen.

## HOF-B1-S045-F03 — Saumweite der Halbglocke

- **Fachlicher Zweck:** Länge des halbkreisförmigen Saumbogens aus dem Saumradius bestimmen.
- **Quelle:** `formeln_s45.md`, Zeilen 21–26; Originaltranskript `s45.md`, Zeilen 43–45; Buchseite 45.
- **Originalbezeichnung:** `SaW = π · rSaW`
- **Normalisierte Bezeichnung:** `saumweite_halbglocke`

### Buchfassung

```text
SaW  = π · rSaW
     = 3,14 · 72,9 cm
     = 229 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumradius` | rSaW | 72,9 | cm |
| `pi_buch` | π | 3,14 | dimensionslos |

### Formel und Rechenschritte

```text
saumweite_halbglocke = pi_buch * saumradius
                      = 3,14 * 72,9 cm
                      = 228,906 cm
Buchwert              = 229 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumweite_halbglocke` | Länge des äußeren Halbkreisbogens | 229 | cm |

- **Abhängigkeiten:** `HOF-B1-S045-F02` und `pi_buch`.
- **Gültigkeitsbereich:** Halber Kreisring der Halbglocke auf S. 45.
- **Technische Randbedingung:** Der Radius darf nicht negativ sein; die Rechnung verwendet den Buchwert `π = 3,14`.
- **Offene Fragen oder Widersprüche:** Keine; `228,906 cm` wird im Buch auf ganze Zentimeter als `229 cm` angegeben, ohne eine allgemeine Rundungsregel zu nennen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Rundung erst nach Berechnung des Bogenmaßes anwenden und Buchrundung von interner Präzision unterscheiden.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s45.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 30 | 1 | Schnittteil-/Zuschnittbeschriftung `Halbglocke 1×`; Stückzahl, keine Berechnung |
| Zeile 35 | 1 | Schnittteil-/Zuschnittbeschriftung `Halbglocke 2×`; Stückzahl, keine Berechnung |
| Zeile 40 | 1 | Fotozuordnung mit sichtbarer Seitenzahl und Dateipfad; administrativer Nachweis, keine Formel |
| **Summe** | **3** | **3 ausgeschlossene Kandidatenzeilen** |
