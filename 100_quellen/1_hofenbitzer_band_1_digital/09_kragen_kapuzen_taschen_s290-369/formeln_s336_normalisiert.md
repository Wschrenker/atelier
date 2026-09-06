# Fachlich normalisierte Formeln — S. 336

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s336.md`  
Zusätzlicher Buchnachweis: `formeln_s340.md`  
Buchseite: Hofenbitzer, Band 1, S. 336

## HOF-B1-S336-F01 — Einschnittabstand als Drittel der hinteren Halslochlänge

- **Fachlicher Zweck:** Einschnittabstände für die Abtrennung eines separaten Kragenstegs aus der hinteren Halslochlänge ableiten.
- **Quelle:** `formeln_s336.md`, Extraktzeile 13; zusätzlicher Anwendungsnachweis `formeln_s340.md`, Extraktzeile 14; Buchseiten 336 und 340.
- **Originalbezeichnung:** `je ca. ⅓ hHlL = 3 cm`
- **Normalisierte Bezeichnung:** `einschnittabstand_als_drittel_der_hinteren_halslochlaenge_breiter_kragen`

### Buchfassung
```text
- 0,7 cm / je ca. ⅓ hHlL = 3 cm
```

```text
- `je ca. ⅓ hHlL = 3 cm`
```

Die erste Buchfassung ist eine gemischte Kandidatenzeile: `0,7 cm` bezeichnet die Stegabtrennung, die anschließende Beziehung den Abstand der weiteren Einschnitte. Beide Teile bleiben unverändert erhalten.

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hintere_halslochlaenge` | hHlL | nicht angegeben | cm |
| `drittel_faktor` | ⅓ | 1/3 | dimensionslos |
| `stegabtrennung` | parallel unterhalb des Kragenbruchs | 0,7 | cm |

### Formel und Rechenschritte
```text
einschnittabstand ≈ hintere_halslochlaenge / 3
```

Der gedruckte Beispielwert beträgt `3 cm`; ein konkreter hHlL-Ausgangswert ist im Extrakt nicht angegeben. Die `0,7 cm` sind eine separate direkte Abtrennung und kein Teil der Drittelrechnung.

### Ausgabe
`einschnittabstand` — je ungefähr ein Drittel der hinteren Halslochlänge, im Buchbeispiel `3 cm`.

- **Abhängigkeiten:** `hintere_halslochlaenge` (hHlL).
- **Gültigkeitsbereich:** Einschnittteilung des zweiteiligen breiten Schalkragens mit Kragensteg, S. 336 und der entsprechende Reverskragen auf S. 340.
- **Offene Fragen oder Widersprüche:** Der hHlL-Eingabewert fehlt; der Beispielwert `3 cm` wird nicht zur Rückrechnung verwendet. Die Genauigkeit von `ca.` ist nicht festgelegt.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Erst ausführbar machen, wenn hHlL als Eingabe belegt ist; `3 cm` nicht als allgemeine Konstante verwenden.

## Ausgeschlossene Kandidaten

| Buchseite / Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| S. 336, 9–12 | 4 | Bild-/Entwicklungs- und Maßstabsangaben ohne eigenständige Rechenbeziehung |
| **Summe S. 336** | **4** | **Maßstabs- und Entwicklungsangaben ausgeschlossen** |

Die Kandidatenzeile S. 340/14 ist oben als zusätzlicher Buchnachweis vertreten.
