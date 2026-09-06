# Fachlich normalisierte Formeln — S. 44

Quelle der Normalisierung: `formeln_s44_glockenrock.md`
Originaltranskript: `s44_glockenrock.md`
Buchseite: Hofenbitzer, Band 1, S. 44

## HOF-B1-S044-F01 — Taillenradius der Vollglocke

- **Fachlicher Zweck:** Inneren Radius des Taillenkreises einer Vollglocke aus der Taillenweite bestimmen.
- **Quelle:** `formeln_s44_glockenrock.md`, Zeilen 13–18; Originaltranskript `s44_glockenrock.md`, Zeilen 33–39; Buchseite 44.
- **Originalbezeichnung:** `rTaW = TaW : (2 × π)`
- **Normalisierte Bezeichnung:** `taillenradius_vollglocke`

### Buchfassung

```text
rTaW = TaW : (2 × π)
     = 72 cm : (2 × 3,14)
     = 11,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenweite` | TaW | 72 | cm |
| `pi_buch` | π | 3,14 | dimensionslos |
| `vollkreisfaktor` | 2 | 2 | dimensionslos |

### Formel und Rechenschritte

```text
taillenradius_vollglocke = taillenweite / (vollkreisfaktor * pi_buch)
                          = 72 cm / (2 * 3,14)
                          = 11,464... cm
Buchwert                 = 11,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenradius_vollglocke` | Innerer Radius des vollständigen Taillenkreises | 11,5 | cm |

- **Abhängigkeiten:** `taillenweite`, `pi_buch` und Vollkreisfaktor `2`.
- **Gültigkeitsbereich:** Vollglocke beziehungsweise Tellerrock als vollständiger Kreisring auf S. 44; laut Quelle auch für eine entsprechend definierte Volant-Ansatzweite verwendbar.
- **Technische Randbedingung:** Der Nenner darf nicht `0` sein. Das Buch rechnet mit `π = 3,14` und gibt den Radius auf eine Dezimalstelle an.
- **Offene Fragen oder Widersprüche:** Keine. Ob die spätere Engine mit `3,14` oder höherer π-Präzision rechnet, ist eine sichtbare technische Entscheidung und keine Buchkorrektur.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Buchwert und intern präziser Rechenwert getrennt nachvollziehbar halten; keine unbemerkte Änderung der Buchrundung.

## HOF-B1-S044-F02 — Saumradius der Vollglocke

- **Fachlicher Zweck:** Äußeren Radius des Saumkreises als Summe aus Taillenradius und Modelllänge bestimmen.
- **Quelle:** `formeln_s44_glockenrock.md`, Zeilen 20–25; Originaltranskript `s44_glockenrock.md`, Zeilen 41–47; Buchseite 44.
- **Originalbezeichnung:** `rSaW = rTaW + MoL`
- **Normalisierte Bezeichnung:** `saumradius_vollglocke`

### Buchfassung

```text
rSaW = rTaW + MoL
     = 11,5 cm + 50 cm
     = 61,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenradius` | rTaW | 11,5 | cm |
| `modelllaenge` | MoL | 50 | cm |

### Formel und Rechenschritte

```text
saumradius_vollglocke = taillenradius + modelllaenge
                       = 11,5 cm + 50 cm
                       = 61,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumradius_vollglocke` | Äußerer Radius bis zur Saumkante | 61,5 | cm |

- **Abhängigkeiten:** `HOF-B1-S044-F01` und gewählte `modelllaenge`.
- **Gültigkeitsbereich:** Vollglocke als Kreisring; bei Volants tritt die Volantlänge an die Stelle der Rock-Modelllänge.
- **Technische Randbedingung:** Beide Eingaben müssen dieselbe Längeneinheit tragen und die Modelllänge darf nicht negativ sein.
- **Offene Fragen oder Widersprüche:** Keine; `11,5 cm + 50 cm = 61,5 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Innen- und Außenradius vom selben Kreismittelpunkt aus konstruieren; die Differenz beider Radien ist die Modelllänge.

## HOF-B1-S044-F03 — Saumweite der Vollglocke

- **Fachlicher Zweck:** Gesamten Umfang des Saumkreises aus dem Saumradius bestimmen.
- **Quelle:** `formeln_s44_glockenrock.md`, Zeilen 27–32; Originaltranskript `s44_glockenrock.md`, Zeilen 49–55; Buchseite 44.
- **Originalbezeichnung:** `SaW = 2 × π × rSaW`
- **Normalisierte Bezeichnung:** `saumweite_vollglocke`

### Buchfassung

```text
SaW = 2 × π × rSaW
    = 2 × 3,14 × 61,5 cm
    = 386,2 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumradius` | rSaW | 61,5 | cm |
| `pi_buch` | π | 3,14 | dimensionslos |
| `vollkreisfaktor` | 2 | 2 | dimensionslos |

### Formel und Rechenschritte

```text
saumweite_vollglocke = vollkreisfaktor * pi_buch * saumradius
                      = 2 * 3,14 * 61,5 cm
                      = 386,22 cm
Buchwert              = 386,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumweite_vollglocke` | Gesamter Umfang des äußeren Saumkreises | 386,2 | cm |

- **Abhängigkeiten:** `HOF-B1-S044-F02`, `pi_buch` und Vollkreisfaktor `2`.
- **Gültigkeitsbereich:** Vollständiger Kreisring der Vollglocke auf S. 44.
- **Technische Randbedingung:** Der Radius darf nicht negativ sein; die Rechnung verwendet den im Buch eingesetzten Wert `π = 3,14`.
- **Offene Fragen oder Widersprüche:** Keine; `386,22 cm` wird im Buch auf `386,2 cm` angegeben, ohne eine allgemeine Rundungsregel zu nennen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Saumweite aus dem ungerundeten Radius berechnen oder die Buchreihenfolge bewusst reproduzieren; beide Wege können leicht unterschiedliche Endwerte liefern und müssen dokumentiert werden.

## HOF-B1-S044-F04 — Taillenradius mit Nahtzugaben

- **Fachlicher Zweck:** Taillenradius für eine Naht- oder Schlitzlösung bestimmen, indem zwei Nahtzugaben zur Taillenweite addiert werden.
- **Quelle:** `formeln_s44_glockenrock.md`, Zeilen 34–37; Originaltranskript `s44_glockenrock.md`, Zeilen 69–82; Buchseite 44.
- **Originalbezeichnung:** `rTaW = (TaW + 2 × NZg) : (2 × π)`
- **Normalisierte Bezeichnung:** `taillenradius_vollglocke_mit_nahtzugaben`

### Buchfassung

```text
rTaW = (TaW + 2 × NZg) : (2 × π)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenweite` | TaW | nicht festgelegt | cm |
| `nahtzugabe` | NZg | frei zu wählen | cm |
| `anzahl_nahtzugaben` | 2 × NZg | 2 | dimensionslos |
| `pi_buch` | π | 3,14 im Seitenbeispiel | dimensionslos |

### Formel und Rechenschritte

```text
taillenradius_vollglocke_mit_nahtzugaben = (taillenweite + (anzahl_nahtzugaben * nahtzugabe))
                                            / (2 * pi_buch)
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `taillenradius_vollglocke_mit_nahtzugaben` | Innerer Radius einschließlich zweier Nahtzugaben in der Ansatzweite | cm |

- **Abhängigkeiten:** `taillenweite`, gewählte `nahtzugabe` und verwendeter π-Wert.
- **Gültigkeitsbereich:** Auf S. 44 beschriebene Naht-/Schlitzlösung des vollständigen Kreisrings.
- **Technische Randbedingung:** Taillenweite und Nahtzugabe müssen dieselbe Einheit tragen; `NZg` bleibt ein Parameter, da die Seite keinen festen Wert vorgibt.
- **Offene Fragen oder Widersprüche:** Keine. Die konkrete Nahtzugabe ist fachlich zu wählen und nicht aus dieser Formel ableitbar.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die zwei Nahtzugaben ausdrücklich als zwei Kanten derselben Naht-/Schlitzlösung modellieren und nicht pauschal auf jede Zuschnittvariante übertragen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s44_glockenrock.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 9–10 | 2 | Gegebene Eingabewerte `TaW = 72 cm` und `MoL = 50 cm`; sie werden in `F01` und `F02` verwendet, sind aber keine eigenständigen Berechnungsformeln |
