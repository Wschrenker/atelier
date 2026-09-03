# Fachlich normalisierte Formeln — S. 163

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s163.md`
Originaltranskript: `s163.md`
Buchseite: Hofenbitzer, Band 1, S. 163

## HOF-B1-S163-F01 — Öffnung aus den Seitennähtenverbreiterungen

- **Fachlicher Zweck:** Die Öffnung am Bund aus den Verbreiterungen von Vorder- und Rückteil bestimmen.
- **Quelle:** `formeln_s163.md`, Zeile 31; Originaltranskript `s163.md`, Zeile 60; Buchseite 163.
- **Originalbezeichnung:** `Öffnung wie die Verbreiterung an den Seitennähten von VT + RT`
- **Normalisierte Bezeichnung:** `bundoeffnung_aus_seitennahtverbreiterung`

### Buchfassung

```text
- Öffnung wie die Verbreiterung an den Seitennähten von VT + RT (2 × 1 cm) = 2 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `seitennahtverbreiterung_vt` | Verbreiterung VT | 1 | cm |
| `seitennahtverbreiterung_rt` | Verbreiterung RT | 1 | cm |

### Formel und Rechenschritte

```text
bundoeffnung = seitennahtverbreiterung_vt + seitennahtverbreiterung_rt
              = 1 cm + 1 cm
              = 2 cm
```

Äquivalent zur gedruckten Kurzform:

```text
bundoeffnung = 2 * 1 cm = 2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `bundoeffnung` | Öffnung am Bund | 2 | cm |

- **Abhängigkeiten:** Verbreiterung an den Seitennähten von VT und RT.
- **Gültigkeitsbereich:** Bund der Funktionshose, Ausführung mit Gummiband.
- **Technische Randbedingung:** Die Quelle setzt zwei gleiche Verbreiterungen von jeweils 1 cm voraus.
- **Offene Fragen oder Widersprüche:** Keine; `2 × 1 cm = 2 cm` ist rechnerisch konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Beide Seitennähte getrennt modellieren, damit ungleiche Verbreiterungen möglich bleiben.

## Ausgeschlossene Kandidaten

| Extraktzeilen | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9–12, 17, 22–26 | 10 | Produktionsschnittteile, Material-/Stückzahlangaben und Beschriftungen ohne Rechenoperation |
| **Summe** | **10** | **Produktions- und Beschriftungsangaben ausgeschlossen** |
