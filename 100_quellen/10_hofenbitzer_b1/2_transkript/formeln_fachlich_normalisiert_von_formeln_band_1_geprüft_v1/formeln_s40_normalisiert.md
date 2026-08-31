# Fachlich normalisierte Formeln — S. 40

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/03_modelle_roecke_s40-105/formeln_s40.md`
Originaltranskript: `../Band_1_geprüft_v1/s40.md`
Buchseite: Hofenbitzer, Band 1, S. 40

## HOF-B1-S040-F01 — Knopflochlänge am geraden Bund

- **Fachlicher Zweck:** Länge des Knopflochs aus dem Knopfdurchmesser und einem Zuschlag bestimmen.
- **Quelle:** `formeln_s40.md`, Zeilen 7–10; Originaltranskript `s40.md`, Zeilen 18–21; Buchseite 40.
- **Originalbezeichnung:** `Knopflochlänge = Knopfdurchmesser + ca. 2 mm`
- **Normalisierte Bezeichnung:** `knopflochlaenge`

### Buchfassung

```text
- 2: Knopfloch am Übertritt passend zum **Knopfdurchmesser** markieren; das **Auge** (Knopflochbeginn) liegt an der markierten Knopfmitte. **Knopflochlänge = Knopfdurchmesser + ca. 2 mm.**
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `knopfdurchmesser` | Knopfdurchmesser | nicht festgelegt | mm |
| `knopfloch_zuschlag` | ca. 2 mm | ungefähr 2 | mm |

### Formel und Rechenschritte

```text
knopflochlaenge = knopfdurchmesser + knopfloch_zuschlag
knopfloch_zuschlag ≈ 2 mm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `knopflochlaenge` | Gesamtlänge des Knopflochs | mm |

- **Abhängigkeiten:** Tatsächlicher `knopfdurchmesser` und der ungefähre `knopfloch_zuschlag`.
- **Gültigkeitsbereich:** Knopfloch am Übertritt des auf S. 40 beschriebenen geraden Bundes.
- **Technische Randbedingung:** Knopfdurchmesser und Zuschlag müssen in derselben Einheit verrechnet werden. Das Wort `ca.` erlaubt keine unbelegt erfundene exakte Toleranz.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keinen zulässigen Bereich um die ungefähren `2 mm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern eine einheitliche Längeneinheit verwenden; den Zuschlag als sichtbaren Parameter mit belegtem Richtwert `2 mm` führen.

## Ausgeschlossener Kandidat

| Quelle in `formeln_s40.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Schnittteil-Beschriftung `1× Ost + El` und Kundinnen-/Datumsplatzhalter; Zuschnitt- und Produktionsangabe, keine Berechnung |
