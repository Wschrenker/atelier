# Fachlich normalisierte Formeln — S. 43

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/03_modelle_roecke_s40-105/formeln_s43.md`
Originaltranskript: `../Band_1_geprüft_v1/s43.md`
Buchseite: Hofenbitzer, Band 1, S. 43

## HOF-B1-S043-F01 — Erweiterungskeile am halben Rock

- **Fachlicher Zweck:** Anzahl der vollständigen Keil-Äquivalente am halben Rock aus den Erweiterungsstellen in Vorderteil, Rückteil und Seitennähten bestimmen.
- **Quelle:** `formeln_s43.md`, Zeilen 7–10; Originaltranskript `s43.md`, Zeilen 7–10; Buchseite 43.
- **Originalbezeichnung:** `3 Keile am halben Rock`
- **Normalisierte Bezeichnung:** `keilaequivalente_halber_rock`

### Buchfassung

```text
- Die weißen Keile am Saum stellen die Saumerweiterung dar: **je ein Keil im VT und im RT** plus **je ein halber Keil an den beiden Seitennähten** = **3 Keile am halben Rock**.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `keile_vorderteil` | ein Keil im VT | 1 | Keil |
| `keile_rueckteil` | ein Keil im RT | 1 | Keil |
| `halbe_keile_seitennaht` | je ein halber Keil an beiden Seitennähten | 2 × 0,5 | Keil |

### Formel und Rechenschritte

```text
keilaequivalente_halber_rock = keile_vorderteil
                               + keile_rueckteil
                               + halbe_keile_seitennaht
                             = 1 + 1 + (2 * 0,5)
                             = 3 Keile
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `keilaequivalente_halber_rock` | Summe der vollständigen Keil-Äquivalente am halben Rock | 3 | Keile |

- **Abhängigkeiten:** Verteilung der Öffnungen auf VT, RT und beide Seitennähte.
- **Gültigkeitsbereich:** Saumerweiterter Rock-Grundschnitt auf S. 43; gezählt wird die im Buch dargestellte Hälfte des Rocks.
- **Technische Randbedingung:** Zwei halbe Seitennahtkeile werden rechnerisch zu einem vollständigen Keil-Äquivalent zusammengefasst.
- **Offene Fragen oder Widersprüche:** Keine. Der Originaltranskripttext nennt zusätzlich sechs Keile am gesamten Rock; diese allgemeine Verdopplungsbeziehung fehlt als eigener Block in der extrahierten Formeldatei und wird hier nicht als zusätzliche Buchfassung erzeugt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zwischen geometrischen Erweiterungsstellen und vollständigen Keil-Äquivalenten unterscheiden; die beiden halben Seitennahtkeile bleiben räumlich getrennte Stellen.

## HOF-B1-S043-F02 — Saumerweiterung aus Keilanzahl und Öffnungsbetrag

- **Fachlicher Zweck:** Gesamte Saumerweiterung aus der Anzahl gleich großer Keile und dem Öffnungsbetrag je Keil bestimmen.
- **Quelle:** `formeln_s43.md`, Zeilen 12–15; Originaltranskript `s43.md`, Zeilen 7–10; Buchseite 43.
- **Originalbezeichnung:** `6 Keile · 6 cm Öffnung = 36 cm Saumerweiterung`
- **Normalisierte Bezeichnung:** `saumerweiterung_aus_keilen`

### Buchfassung

```text
- Beispiel im Buch: **6 Keile · 6 cm Öffnung = 36 cm Saumerweiterung**.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `erweiterungsstellen` | Keile | 6 | dimensionslos |
| `oeffnungsbetrag` | Öffnung je Keil | 6 | cm |

### Formel und Rechenschritte

```text
saumerweiterung = erweiterungsstellen * oeffnungsbetrag
                 = 6 * 6 cm
                 = 36 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `saumerweiterung` | Zusätzliche gesamte Saumweite | 36 | cm |

- **Abhängigkeiten:** Anzahl der gleichmäßig verteilten `erweiterungsstellen` und einheitlicher `oeffnungsbetrag`.
- **Gültigkeitsbereich:** Beispiel des gesamten saumerweiterten Rocks auf S. 43 mit sechs gleich großen Öffnungen.
- **Technische Randbedingung:** Alle Erweiterungsstellen müssen für diese Multiplikation denselben Öffnungsbetrag erhalten.
- **Offene Fragen oder Widersprüche:** Keine; `6 × 6 cm = 36 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bei ungleichen Öffnungsbeträgen statt der Multiplikation eine Summe der einzelnen Beträge verwenden; diese Variante ist eine technische Verallgemeinerung und keine Aussage dieser Buchformel.

## HOF-B1-S043-F03 — Öffnungsbetrag je Erweiterungsstelle

- **Fachlicher Zweck:** Gleichmäßigen Öffnungsbetrag je Erweiterungsstelle aus gewünschter gesamter Saumerweiterung und Anzahl der Erweiterungsstellen bestimmen.
- **Quelle:** `formeln_s43.md`, Zeilen 17–21; Originaltranskript `s43.md`, Zeilen 12–16; Buchseite 43.
- **Originalbezeichnung:** `Öffnungsbetrag = gewünschte Saumerweiterung : Erweiterungsstellen`
- **Normalisierte Bezeichnung:** `oeffnungsbetrag_je_erweiterungsstelle`

### Buchfassung

```text
Öffnungsbetrag = gewünschte Saumerweiterung : Erweiterungsstellen
Beispiel:       = 48 cm : 6 = 8 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `gewuenschte_saumerweiterung` | gewünschte Saumerweiterung | 48 | cm |
| `erweiterungsstellen` | Erweiterungsstellen | 6 | dimensionslos |

### Formel und Rechenschritte

```text
oeffnungsbetrag_je_erweiterungsstelle = gewuenschte_saumerweiterung / erweiterungsstellen
                                        = 48 cm / 6
                                        = 8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `oeffnungsbetrag_je_erweiterungsstelle` | Gleichmäßiger Öffnungsbetrag an jeder Erweiterungsstelle | 8 | cm |

- **Abhängigkeiten:** `gewuenschte_saumerweiterung` und Anzahl der `erweiterungsstellen`.
- **Gültigkeitsbereich:** Gleichmäßige Verteilung der Saumerweiterung auf die sechs Stellen des gesamten Rocks.
- **Technische Randbedingung:** `erweiterungsstellen` muss größer als `0` und als Anzahl ganzzahlig sein.
- **Offene Fragen oder Widersprüche:** Keine; `48 cm / 6 = 8 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Anzahl der Erweiterungsstellen validieren und die Einheit der Saumerweiterung im Ergebnis erhalten.

## HOF-B1-S043-F04 — Ausstellbetrag an der Seitennaht

- **Fachlicher Zweck:** Ausstellbetrag an jeder Seitennaht als Hälfte des Öffnungsbetrags einer vollständigen Erweiterungsstelle bestimmen.
- **Quelle:** `formeln_s43.md`, Zeilen 23–27; Originaltranskript `s43.md`, Zeilen 18–21; Buchseite 43.
- **Originalbezeichnung:** `ausstellen hier 3 cm = halber Öffnungsbetrag`
- **Normalisierte Bezeichnung:** `ausstellbetrag_seitennaht`

### Buchfassung

```text
- Punkt 9: **„ausstellen hier 3 cm"** = **halber Öffnungsbetrag** an der Seitennaht (½ von 6 cm); rechts **„ausstellen wie vorne"**.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `oeffnungsbetrag` | Öffnungsbetrag | 6 | cm |
| `seitennaht_anteil` | ½ | 0,5 | dimensionslos |

### Formel und Rechenschritte

```text
ausstellbetrag_seitennaht = oeffnungsbetrag * seitennaht_anteil
                            = 6 cm * 0,5
                            = 3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `ausstellbetrag_seitennaht` | Ausstellbetrag an einer Seitennaht | 3 | cm |

- **Abhängigkeiten:** Gewählter `oeffnungsbetrag` der vollständigen Erweiterungsstellen.
- **Gültigkeitsbereich:** Beide Seitennähte des saumerweiterten Rock-Grundschnitts auf S. 43.
- **Technische Randbedingung:** Der Seitennahtbetrag ist je Seite die Hälfte des Öffnungsbetrags; beide Seiten werden getrennt ausgestellt.
- **Offene Fragen oder Widersprüche:** Keine; die Quelle setzt `3 cm` ausdrücklich mit der Hälfte von `6 cm` gleich.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den halben Betrag an jeder Seitennaht platzieren; nicht beide Seitennahtbeträge zu einer einzigen geometrischen Öffnung zusammenziehen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s43.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 25 | 1 | Zeichnungsbeschriftung `öffnen hier 6 cm` und Wiederholung desselben Werts auf der Gegenseite; keine zusätzliche Formel neben `HOF-B1-S043-F02` und `F04` |
| Zeile 31 | 1 | Bei der Extraktion abgeschnittener Satz zum Maß `12 bis 15 cm`; isolierter Wertebereich ohne vollständige Rechenbeziehung |
| Zeile 36 | 1 | Bei der Extraktion abgeschnittener Erklärungssatz mit Punktverweis `Punkt 7 = vM`; keine Rechenformel |
| **Summe** | **3** | **3 ausgeschlossene Kandidatenzeilen** |
