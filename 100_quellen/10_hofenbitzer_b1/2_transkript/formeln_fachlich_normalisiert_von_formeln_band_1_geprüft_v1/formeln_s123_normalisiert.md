# Fachlich normalisierte Formeln — S. 123

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s123.md`
Originaltranskript: `../Band_1_geprüft_v1/s123.md`
Buchseite: Hofenbitzer, Band 1, S. 123

## HOF-B1-S123-F01 — Wadenhöhe aus Kniehöhe

- **Fachlicher Zweck:** Die Wadenhöhe als Hälfte der Kniehöhe bestimmen.
- **Quelle:** `formeln_s123.md`, Zeile 9; Originaltranskript `s123.md`, Zeile 42; Buchseite 123.
- **Originalbezeichnung:** `WaH = KnH : 2`
- **Normalisierte Bezeichnung:** `wadenhoehe_aus_kniehoehe`

### Buchfassung

```text
- WaH = KnH : 2
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `kniehoehe` | KnH | nicht angegeben | cm |

### Formel und Rechenschritte

```text
wadenhoehe = kniehoehe / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `wadenhoehe` | WaH | nicht angegeben | cm |

- **Abhängigkeiten:** Kniehöhe der verwendeten Hosenkonstruktion.
- **Gültigkeitsbereich:** Weitenreduzierung der Standardhose beziehungsweise Hose aus elastischem Material auf S. 123.
- **Technische Randbedingung:** Die Kniehöhe muss als nichtnegative Länge vorliegen.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Wadenhöhe einmal berechnen und für Vorder- und Hinterhose gemeinsam verwenden.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s123.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Identische Wiederholung von `WaH = KnH : 2` in der Beschriftung der Hinterhose |
| **Summe** | **1** | **1 Wiederholung ausgeschlossen** |
