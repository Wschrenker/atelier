# Fachlich normalisierte Formeln — S. 153

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s153.md`
Originaltranskript: `s153.md`
Buchseite: Hofenbitzer, Band 1, S. 153

## HOF-B1-S153-F01 — Kniebundumfang aus Unterknieumfang und Mehrweite

- **Fachlicher Zweck:** Den Kniebundumfang für Knickerbocker oder Golfhose bestimmen.
- **Quelle:** `formeln_s153.md`, Zeilen 9–10; Originaltranskript `s153.md`, Zeilen 17–20; Buchseite 153.
- **Originalbezeichnung:** `Unterknieumfang uKnU + Mehrweite`
- **Normalisierte Bezeichnung:** `kniebundumfang`

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
                 = 32 cm + (1 bis 2 cm)
                 = 33 bis 34 cm
```

Der gedruckte Beispielwert `33 cm` entspricht der Auswahl von `1 cm` Mehrweite.

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `kniebundumfang` | Umfang des Kniebunds | 33 | cm |

- **Abhängigkeiten:** Unterknieumfang und gewählte Mehrweite.
- **Gültigkeitsbereich:** Kniebund von Knickerbocker oder Golfhose.
- **Technische Randbedingung:** Die konkrete Auswahl innerhalb des Bereichs ist nicht näher geregelt.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Mehrweite als expliziten Parameter führen.

## HOF-B1-S153-F02 — Saumweite aus Kniebundumfang, Raffung und Falteninhalt

- **Fachlicher Zweck:** Die Saumweite aus Kniebundumfang, Gummiraffung und Falteninhalt bestimmen.
- **Quelle:** `formeln_s153.md`, Zeilen 15–16; Originaltranskript `s153.md`, Zeilen 22–28; Buchseite 153.
- **Originalbezeichnung:** `Kniebundumfang + Raffung (Gummi) + Falteninhalte`
- **Normalisierte Bezeichnung:** `saumweite_knickerbocker_golfhose`

### Buchfassung

```text
= 33 cm + 3 cm + 12 cm  
hier = 48 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `kniebundumfang` | Kniebundumfang | 33 | cm |
| `raffungszugabe` | Raffung (Gummi) | 3 | cm |
| `falteninhalt_gesamt` | Falteninhalte | 12 | cm |

### Formel und Rechenschritte

```text
saumweite = kniebundumfang + raffungszugabe + falteninhalt_gesamt
            = 33 cm + 3 cm + 12 cm
            = 48 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite` | fertige Saumweite | 48 | cm |

- **Abhängigkeiten:** `HOF-B1-S153-F01`, Raffung und gesamter Falteninhalt.
- **Gültigkeitsbereich:** Knickerbocker beziehungsweise Golfhose.
- **Technische Randbedingung:** Die Quelle nennt für vier Falten beispielhaft 12 cm Gesamtinhalt, aber keine allgemeine Verteilungsregel.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Falteninhalt als Gesamtwert und Faltenanzahl getrennt führen.

## HOF-B1-S153-F03 — Aufteilung von Saumweite und Falteninhalt

- **Fachlicher Zweck:** Die Saumweite auf Vorder- und Rückteil sowie den einzelnen Falteninhalt verteilen.
- **Quelle:** `formeln_s153.md`, Zeilen 20–22; Originaltranskript `s153.md`, Zeilen 34–43; Buchseite 153.
- **Originalbezeichnung:** `VT: beidseitig ¼ SaW − 1 cm; RT: beidseitig ¼ SaW + 1 cm; je ¼ Falteninhalt = 3 cm`
- **Normalisierte Bezeichnung:** `saumweiten_und_faltenverteilung_knickerbocker`

### Buchfassung

```text
- VT: beidseitig `¼ SaW − 1 cm`
- RT: beidseitig `¼ SaW + 1 cm`
- je `¼ Falteninhalt = 3 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `saumweite` | SaW | Ergebnis aus F01/F02 | cm |
| `falteninhalt_gesamt` | Falteninhalt | variabel | cm |

### Formel und Rechenschritte

```text
vt_seitenanteil = saumweite / 4 - 1 cm
rt_seitenanteil = saumweite / 4 + 1 cm
falteninhalt_je_viertel = falteninhalt_gesamt / 4
```

Das Buchbeispiel weist je Viertel `3 cm` aus; das entspricht bei vier Vierteln einem Gesamtwert von `12 cm`.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `vt_seitenanteil` | beidseitiger VT-Anteil | cm |
| `rt_seitenanteil` | beidseitiger RT-Anteil | cm |
| `falteninhalt_je_viertel` | Anteil je Falte/Viertel | cm |

- **Abhängigkeiten:** Saumweite und Gesamtfalteninhalt.
- **Gültigkeitsbereich:** Schnittaufteilung der Knickerbocker/Golfhose.
- **Technische Randbedingung:** Die Bezeichnungen `VT` und `RT` sowie die beidseitige Anwendung bleiben erhalten.
- **Offene Fragen oder Widersprüche:** Die Quelle legt keine weitere Auswahl- oder Rundungsregel fest.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorzeichen von VT/RT und symmetrische Anwendung getrennt modellieren.

## HOF-B1-S153-F04 — Angeschnittener Gummibund

- **Fachlicher Zweck:** Die Höhe des angeschnittenen Gummibunds aus Bandbreite und Zuschlag bestimmen.
- **Quelle:** `formeln_s153.md`, Zeilen 26–28; Originaltranskript `s153.md`, Zeilen 49–55; Buchseite 153.
- **Originalbezeichnung:** `4 cm breites Gummiband + 0,5 cm (= 4,5 cm)`
- **Normalisierte Bezeichnung:** `angeschnittener_gummibund`

### Buchfassung

```text
4. Den angeschnittenen Gummibund für ein 4 cm breites Gummiband + 0,5 cm (= 4,5 cm) anzeichnen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `gummibandbreite` | Gummiband | 4 | cm |
| `bund_zuschlag` | Zuschlag | 0,5 | cm |

### Formel und Rechenschritte

```text
bundhoehe = gummibandbreite + bund_zuschlag
           = 4 cm + 0,5 cm
           = 4,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `bundhoehe` | Höhe des angeschnittenen Gummibunds | 4,5 | cm |

- **Abhängigkeiten:** Breite des verwendeten Gummibands.
- **Gültigkeitsbereich:** Angeschnittener Gummibund der Knickerbocker/Golfhose.
- **Technische Randbedingung:** Der Zuschlag ist im Buchbeispiel mit `0,5 cm` festgelegt.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zuschlag als eigener Parameter sichtbar halten.
