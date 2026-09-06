# Fachlich normalisierte Formeln — S. 155

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s155.md`
Originaltranskript: `s155.md`
Buchseite: Hofenbitzer, Band 1, S. 155

## HOF-B1-S155-F01 — Kniebundumfang aus Unterknieumfang und Mehrweite

- **Fachlicher Zweck:** Den Kniebundumfang der weiten Kniebundhose bestimmen.
- **Quelle:** `formeln_s155.md`, Zeilen 9–10; Originaltranskript `s155.md`, Zeilen 14–17; Buchseite 155.
- **Originalbezeichnung:** `Unterknieumfang uKnU + Mehrweite`
- **Normalisierte Bezeichnung:** `kniebundumfang_weite_kniebundhose`

### Buchfassung

```text
= 32 cm + 1 bis 2 cm  
hier = 33 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `unterknieumfang` | uKnU | 32 | cm |
| `kniebund_mehrweite` | Mehrweite | 1 bis 2 | cm |

### Formel und Rechenschritte

```text
kniebundumfang = unterknieumfang + kniebund_mehrweite
                 = 32 cm + 1 cm
                 = 33 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `kniebundumfang` | Umfang des Kniebunds | 33 | cm |

- **Abhängigkeiten:** Unterknieumfang und gewählte Mehrweite.
- **Gültigkeitsbereich:** Weite Kniebundhose.
- **Technische Randbedingung:** Der Beispielwert verwendet `1 cm` aus dem angegebenen Bereich.
- **Offene Fragen oder Widersprüche:** Die Auswahlregel innerhalb des Bereichs ist nicht genannt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Mehrweite als explizite Eingabe führen.

## HOF-B1-S155-F02 — Saumweite aus Kniebundumfang und Falteninhalt

- **Fachlicher Zweck:** Die Saumweite aus Kniebundumfang und Gesamtfalteninhalt bestimmen.
- **Quelle:** `formeln_s155.md`, Zeilen 15–16; Originaltranskript `s155.md`, Zeilen 19–24; Buchseite 155.
- **Originalbezeichnung:** `Kniebundumfang + Falteninhalt`
- **Normalisierte Bezeichnung:** `saumweite_weite_kniebundhose`

### Buchfassung

```text
= 33 cm + 10 bis 16 cm  
hier = 48 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `kniebundumfang` | Kniebundumfang | 33 | cm |
| `falteninhalt_gesamt` | Falteninhalt | 10 bis 16 | cm |

### Formel und Rechenschritte

```text
saumweite = kniebundumfang + falteninhalt_gesamt
            = 33 cm + 15 cm
            = 48 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite` | fertige Saumweite | 48 | cm |

- **Abhängigkeiten:** `HOF-B1-S155-F01` und Gesamtfalteninhalt.
- **Gültigkeitsbereich:** Weite Kniebundhose.
- **Technische Randbedingung:** Der Beispielwert verwendet `15 cm` aus dem Bereich; die Quelle nennt dies im Transkriptkontext als Gesamtinhalt für fünf Falten.
- **Offene Fragen oder Widersprüche:** Die Auswahl innerhalb des Bereichs ist nicht geregelt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Gesamtfalteninhalt und Faltenanzahl getrennt führen.

## HOF-B1-S155-F03 — Verteilung des Falteninhalts

- **Fachlicher Zweck:** Den Falteninhalt auf fünf beziehungsweise zehn gleich große Anteile verteilen.
- **Quelle:** `formeln_s155.md`, Zeilen 21–24; Originaltranskript `s155.md`, Zeilen 46–53; Buchseite 155.
- **Originalbezeichnung:** `je ⅕ Falteninhalt = 3 cm; ¹⁄₁₀ Falteninhalt = 1,5 cm`
- **Normalisierte Bezeichnung:** `falteninhalt_verteilung_weite_kniebundhose`

### Buchfassung

```text
- VT: beidseitig `¼ SaW − 1 cm`
- RT: beidseitig `¼ SaW + 1 cm`
- je `⅕ Falteninhalt = 3 cm`
- `¹⁄₁₀ Falteninhalt = 1,5 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `falteninhalt_gesamt` | Falteninhalt | 15 | cm |
| `faltenanzahl` | Falten | 5 beziehungsweise 10 Teilungsanteile | dimensionslos |

### Formel und Rechenschritte

```text
falteninhalt_je_fuenftel = falteninhalt_gesamt / 5
                          = 15 cm / 5
                          = 3 cm
falteninhalt_je_zehntel = falteninhalt_gesamt / 10
                         = 15 cm / 10
                         = 1,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `falteninhalt_je_fuenftel` | ein Fünftel des Falteninhalts | 3 | cm |
| `falteninhalt_je_zehntel` | ein Zehntel des Falteninhalts | 1,5 | cm |

- **Abhängigkeiten:** Gesamtfalteninhalt aus `HOF-B1-S155-F02` beziehungsweise dem dort genannten Buchkontext.
- **Gültigkeitsbereich:** Faltenaufteilung der weiten Kniebundhose.
- **Technische Randbedingung:** Die gleichmäßige Teilung ist für die gedruckten Anteile dokumentiert; weitere Modellierungsregeln sind nicht belegt.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Abweichung: `5 × 3 cm = 15 cm` und `10 × 1,5 cm = 15 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Zahl der Teilungsanteile ausdrücklich als Parameter führen.

## Ausgeschlossene Kandidaten

Keine. Alle acht extrahierten Kandidatenzeilen sind in den drei Formelblöcken abgebildet.
