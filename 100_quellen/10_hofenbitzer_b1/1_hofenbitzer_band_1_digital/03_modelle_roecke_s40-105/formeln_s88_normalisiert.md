# Fachlich normalisierte Formeln — S. 88

Quelle der Normalisierung: `formeln_s88_digital_geprüft.md`
Originaltranskript: `s88_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 88
Extraktionsstand: v2

## HOF-B1-S088-F01 — Verbleibender Stoff für Falteninhalte

- **Fachlicher Zweck:** Den aus der vorhandenen Stoffbreite verbleibenden Gesamtbetrag für alle Falteninhalte bestimmen.
- **Quelle:** `formeln_s88_digital_geprüft.md`, Zeilen 9, 14 und 19; Originaltranskript `s88_digital_geprüft.md`, Zeilen 65, 67 und 69; Buchseite 88.
- **Originalbezeichnung:** `Σ FaI = StB - 2 · 1 cm NZg - geW`
- **Normalisierte Bezeichnung:** `summe_falteninhalte`

### Buchfassung

```text
Σ FaI = StB - 2 · 1 cm NZg - geW
```

```text
= 92 cm - 2 cm - 32 cm
```

```text
= 58 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `stoffbreite` | vorhandene Stoffbreite StB | 92 | cm |
| `anzahl_nahtzugaben` | `2` | 2 | dimensionslos |
| `nahtzugabe_je_kante` | NZg | 1 | cm |
| `geschlossene_weite` | geschlossene Weite geW | 32 | cm |

### Formel und Rechenschritte

```text
summe_falteninhalte = stoffbreite
                       - (anzahl_nahtzugaben * nahtzugabe_je_kante)
                       - geschlossene_weite
                     = 92 cm - (2 * 1 cm) - 32 cm
                     = 58 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `summe_falteninhalte` | verbleibender Stoff für alle Falteninhalte Σ FaI | 58 | cm |

- **Abhängigkeiten:** Vorhandene `stoffbreite`, beidseitige Nahtzugaben und `geschlossene_weite` des Faltenteils.
- **Gültigkeitsbereich:** Passenrock mit Seitentaschen und Faltenteil auf S. 88; Buchbeispiel mit 92 cm Stoffbreite und 32 cm geschlossener Weite.
- **Technische Randbedingung:** Alle Längen müssen in derselben Einheit vorliegen; der verbleibende Betrag darf für eine ausführbare Konstruktion nicht negativ sein.
- **Offene Fragen oder Widersprüche:** Keine; `92 cm - 2 cm - 32 cm = 58 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Anzahl und Einzelbreite der Nahtzugaben getrennt führen und vor der Subtraktion zum gesamten Nahtzugabenbetrag multiplizieren.

## HOF-B1-S088-F02 — Falteninhalt je geplanter Einheit

- **Fachlicher Zweck:** Den gleichmäßigen Falteninhalt aus dem verfügbaren Gesamtbetrag und der Zahl der Falteninhalte bestimmen.
- **Quelle:** `formeln_s88_digital_geprüft.md`, Zeilen 24, 29 und 34; Originaltranskript `s88_digital_geprüft.md`, Zeilen 73, 75 und 77; Buchseite 88.
- **Originalbezeichnung:** `FaI = Σ FaI : Zahl der Falteninhalte`
- **Normalisierte Bezeichnung:** `falteninhalt_je_einheit`

### Buchfassung

```text
FaI = Σ FaI : Zahl der Falteninhalte
```

```text
= 58 cm : 10
```

```text
= 5,8 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `summe_falteninhalte` | Σ FaI | 58 | cm |
| `anzahl_falteninhalte` | Zahl der Falteninhalte | 10 | dimensionslos |

### Formel und Rechenschritte

```text
falteninhalt = summe_falteninhalte / anzahl_falteninhalte
              = 58 cm / 10
              = 5,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `falteninhalt` | Falteninhalt FaI je geplanter Einheit | 5,8 | cm |

- **Abhängigkeiten:** `summe_falteninhalte` aus `HOF-B1-S088-F01` und die auf der Seite festgelegte `anzahl_falteninhalte`.
- **Gültigkeitsbereich:** Faltenteil des Passenrocks auf S. 88 mit zehn Falteninhalten.
- **Technische Randbedingung:** `anzahl_falteninhalte` muss größer als 0 sein.
- **Offene Fragen oder Widersprüche:** Keine; `58 cm / 10 = 5,8 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Anzahl als positive dimensionslose Eingabe validieren; nicht mit der auf der Seite genannten Anzahl von elf sichtbaren Falten verwechseln.

## Ausgeschlossene Kandidaten

Keine. Alle 6 extrahierten Kandidatenzeilen sind in Formelblöcken abgebildet.
