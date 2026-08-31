# Fachlich normalisierte Formeln — S. 134

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s134.md`
Originaltranskript: `../Band_1_geprüft_v1/s134.md`
Buchseite: Hofenbitzer, Band 1, S. 134

## HOF-B1-S134-F01 — Öffnungsbetrag der Bundfalte mit fehlendem Minuenden

- **Fachlicher Zweck:** Den im Extrakt unvollständig überlieferten Abzug des vorhandenen Abnäherinhalts erfassen.
- **Quelle:** `formeln_s134.md`, Zeile 9; Originaltranskript `s134.md`, Zeilen 20–24 und 43–44; Buchseite 134.
- **Originalbezeichnung:** Im extrahierten Bestand fehlt der Minuend vor `- Abnäherinhalt`.
- **Normalisierte Bezeichnung:** `oeffnungsbetrag_bundfalte_operand_offen`

### Buchfassung

```text
- - Abnäherinhalt (hier 2 cm) = Öffnungsbetrag (hier 3 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `minuend_offen` | im Extrakt nicht enthalten | unbekannt | cm |
| `abnaeherinhalt` | Abnäherinhalt | 2 | cm |

### Formel und Rechenschritte

```text
oeffnungsbetrag = minuend_offen - abnaeherinhalt
Buchfragment    = unbekannt - 2 cm = 3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `oeffnungsbetrag` | symmetrisch zu öffnender Gesamtbetrag | 3 | cm |

- **Abhängigkeiten:** Fehlender Minuend und vorhandener Abnäherinhalt.
- **Gültigkeitsbereich:** Zahlenfragment zur Abwandlung einer Standardhose in eine Bundfaltenhose auf S. 134.
- **Technische Randbedingung:** Aus dem Fragment folgt rechnerisch ein Minuend von 5 cm; diese Rückrechnung ersetzt jedoch nicht die fehlende Buchfassung.
- **Offene Fragen oder Widersprüche:** Das Originaltranskript nennt als Minuenden den gewünschten Bundfalteninhalt von 5 cm. Diese Bezeichnungszeile fehlt im verbindlichen Extrakt und darf deshalb hier nicht fest an die Formel gebunden werden.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis die vollständige Beziehung in der Extraktionsschicht ergänzt und geprüft ist.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s134.md` enthält in Zeile 22 die vollständige Beziehung, dass der vorhandene Abnäherinhalt vom gewünschten Bundfalteninhalt abgezogen wird. `formeln_s134.md` enthält nur das unvollständige Zeichnungsfragment aus Zeile 44. Auch die Halbierung des Öffnungsbetrags aus Zeile 24 sowie die Viertel-Knie- und Saumweiten aus den Zeilen 52–53 fehlen im Extrakt. Diese Stellen wurden nicht als zusätzliche Buchfassungen erzeugt.
