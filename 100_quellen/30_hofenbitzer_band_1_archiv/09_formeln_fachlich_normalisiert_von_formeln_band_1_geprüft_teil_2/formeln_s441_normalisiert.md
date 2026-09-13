# Fachlich normalisierte Formeln — S. 441

Quelle der Normalisierung: `formeln_s441_digital_geprüft.md`
Originaltranskript: `s441_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 441

## HOF-B1-S441-F01 — Gesamter Saumeinschlag

- **Fachlicher Zweck:** Den gesamten Saumeinschlag aus zwei Einschlägen zu je `0,5 cm` bestimmen.
- **Quelle:** `formeln_s441_digital_geprüft.md`, Zeile 9; Originaltranskript `s441_digital_geprüft.md`, Zeile 28; Buchseite 441.
- **Originalbezeichnung:** Einschlag je nach Verarbeitung `2× 0,5 cm`
- **Normalisierte Bezeichnung:** `saumeinschlag_gesamt`

### Buchfassung

```text
23. Säume wie vorgeschlagen vorne und hinten verlängern, seitlich kürzen und wie gewünscht formen. Einschlag je nach Verarbeitung 2× 0,5 cm.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `einschlag_einfach` | einzelner Einschlag | 0,5 | cm |
| `einschlag_anzahl` | `2×` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
saumeinschlag_gesamt = einschlag_anzahl * einschlag_einfach
saumeinschlag_gesamt = 2 * 0,5 cm
saumeinschlag_gesamt = 1,0 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `saumeinschlag_gesamt` | gesamte für beide Einschläge benötigte Breite | 1,0 | cm |

- **Abhängigkeiten:** Gewählte Verarbeitung mit zwei Einschlägen zu je `0,5 cm`.
- **Gültigkeitsbereich:** Saum der Bluse mit Schulterpasse und Kräuselweite auf S. 441.
- **Technische Randbedingung:** Die Quelle schränkt die Angabe mit „je nach Verarbeitung“ ein; andere Verarbeitungen benötigen eine eigene belegte Vorgabe.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Abweichung; `2 × 0,5 cm = 1,0 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zwei Einschläge als Stückzahl und Einzelbreite getrennt führen; diese Buchvariante ergibt insgesamt `1,0 cm`.
