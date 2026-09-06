# Fachlich normalisierte Formeln — S. 154

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s154.md`
Originaltranskript: `s154.md`
Buchseite: Hofenbitzer, Band 1, S. 154

## HOF-B1-S154-F01 — Kniebundumfang aus Unterknieumfang und Mehrweite

- **Fachlicher Zweck:** Den Kniebundumfang der schmalen Kniebundhose bestimmen.
- **Quelle:** `formeln_s154.md`, Zeilen 14–15; Originaltranskript `s154.md`, Zeilen 34–37; Buchseite 154.
- **Originalbezeichnung:** `Unterknieumfang uKnU + Mehrweite`
- **Normalisierte Bezeichnung:** `kniebundumfang_schmale_kniebundhose`

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

- **Abhängigkeiten:** Unterknieumfang und Mehrweite.
- **Gültigkeitsbereich:** Schmale Kniebundhose/Pagenhose.
- **Technische Randbedingung:** Der Druckwert `33 cm` verwendet offenbar `1 cm` aus dem angegebenen Bereich; eine Auswahlregel ist nicht genannt.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Gewählte Mehrweite getrennt speichern.

## HOF-B1-S154-F02 — Saumweite aus Kniebundumfang und Abnäherinhalt

- **Fachlicher Zweck:** Die Saumweite aus Kniebundumfang und gesamtem Abnäherinhalt bestimmen.
- **Quelle:** `formeln_s154.md`, Zeilen 20–21; Originaltranskript `s154.md`, Zeilen 39–44; Buchseite 154.
- **Originalbezeichnung:** `Kniebundumfang + Abnäher`
- **Normalisierte Bezeichnung:** `saumweite_schmale_kniebundhose`

### Buchfassung

```text
= 33 cm + 4 bis 6 cm  
hier = 38 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `kniebundumfang` | Kniebundumfang | 33 | cm |
| `abnaeherinhalt_gesamt` | Abnäher | 4 bis 6 | cm |

### Formel und Rechenschritte

```text
saumweite = kniebundumfang + abnaeherinhalt_gesamt
            = 33 cm + 5 cm
            = 38 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite` | fertige Saumweite | 38 | cm |

- **Abhängigkeiten:** `HOF-B1-S154-F01` und gesamter Abnäherinhalt.
- **Gültigkeitsbereich:** Schmale Kniebundhose/Pagenhose.
- **Technische Randbedingung:** Der gedruckte Wert `38 cm` entspricht einem ausgewählten Abnäherinhalt von `5 cm`.
- **Offene Fragen oder Widersprüche:** Die Auswahl innerhalb des Bereichs ist nicht erklärt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereich und ausgewählten Wert getrennt führen.

## HOF-B1-S154-F03 — Gesamter Abnäherinhalt

- **Fachlicher Zweck:** Den insgesamt verfügbaren Abnäherinhalt dokumentieren.
- **Quelle:** `formeln_s154.md`, Zeile 26; Originaltranskript `s154.md`, Zeile 44; Buchseite 154.
- **Originalbezeichnung:** `gesamter Abnäherinhalt = 5 cm`
- **Normalisierte Bezeichnung:** `abnaeherinhalt_gesamt_schmale_kniebundhose`

### Buchfassung

```text
gesamter Abnäherinhalt = 5 cm
```

### Eingaben

Keine; die Quelle gibt den Gesamtwert direkt an.

### Formel und Rechenschritte

```text
abnaeherinhalt_gesamt = 5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `abnaeherinhalt_gesamt` | gesamter Abnäherinhalt | 5 | cm |

- **Abhängigkeiten:** Eingabewert für die Saumweitenrechnung.
- **Gültigkeitsbereich:** Schmale Kniebundhose/Pagenhose, Beispiel Größe 38.
- **Technische Randbedingung:** Direkt gesetzter Buchwert, keine allgemeine Berechnung.
- **Offene Fragen oder Widersprüche:** Die Quelle erklärt im Extrakt nicht die Herleitung des Gesamtwerts.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Buchbeispielwert beziehungsweise fachliche Eingabe behandeln.

## HOF-B1-S154-F04 — Verteilung des Abnäherinhalts

- **Fachlicher Zweck:** Den Abnäherinhalt auf Vorder- und Rückteil sowie die einzelnen Abnäher verteilen.
- **Quelle:** `formeln_s154.md`, Zeilen 31–33; Originaltranskript `s154.md`, Zeilen 50–58; Buchseite 154.
- **Originalbezeichnung:** `VT: beidseitig ¼ SaW − 1 cm; RT: beidseitig ¼ SaW + 1 cm; ¼ Abnäherinhalt = 1,2 cm`
- **Normalisierte Bezeichnung:** `abnaeherverteilung_schmale_kniebundhose`

### Buchfassung

```text
- VT: beidseitig `¼ SaW − 1 cm`
- RT: beidseitig `¼ SaW + 1 cm`
- je Hosenteil zwei Abnäher, beschriftet mit `¼ Abnäherinhalt = 1,2 cm` (Beschriftung je einmal an VT und RT)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite` | SaW | 38 | cm |
| `abnaeherinhalt_gesamt` | Abnäherinhalt | 5 | cm |
| `abnaeherinhalt_je_viertel` | ¼ Abnäherinhalt | 1,2 | cm |

### Formel und Rechenschritte

```text
vt_seitenanteil = saumweite / 4 - 1 cm
rt_seitenanteil = saumweite / 4 + 1 cm
abnaeherinhalt_je_viertel = 1,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `vt_seitenanteil` | beidseitiger VT-Anteil | cm |
| `rt_seitenanteil` | beidseitiger RT-Anteil | cm |
| `abnaeherinhalt_je_viertel` | beschrifteter Einzelanteil | cm |

- **Abhängigkeiten:** Saumweite und gesamter Abnäherinhalt.
- **Gültigkeitsbereich:** Abnäherverteilung der schmalen Kniebundhose.
- **Technische Randbedingung:** Die beidseitigen VT-/RT-Anteile und die Einzelabnäher bleiben als getrennte Beziehungen erhalten.
- **Offene Fragen oder Widersprüche:** Bei vier beschrifteten Viertelanteilen ergäben `4 × 1,2 cm = 4,8 cm`, nicht der separat gedruckte Gesamtwert `5 cm`. Die Buchangaben werden nicht korrigiert; die Verteilung bleibt bis zur Fachentscheidung gesperrt.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht ausführen, bevor die Abweichung zwischen Gesamtwert und Einzelbeschriftung geklärt ist.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---:|---:|---|
| 9 | 1 | Bild-/Konstruktionsverweis `□2 + 4`; keine Rechenoperation |
| **Summe** | **1** | **Konstruktionsverweis ausgeschlossen** |
