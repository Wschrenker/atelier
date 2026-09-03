# Fachlich normalisierte Formeln — S. 332

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s332.md`  
Zusätzliche Buchnachweise: `formeln_s333.md`, `formeln_s338.md`, `formeln_s339.md`  
Buchseite: Hofenbitzer, Band 1, S. 332

## HOF-B1-S332-F01 — Hintere Stegbreite aus seitlicher Stegbreite

- **Fachlicher Zweck:** Die hintere Stegbreite aus der seitlichen Stegbreite und einem festen Zuschlag bestimmen.
- **Quelle:** `formeln_s332.md`, Extraktzeile 26; zusätzliche Anwendungsnachweise `formeln_s333.md`, Extraktzeile 14, `formeln_s338.md`, Extraktzeile 24, und `formeln_s339.md`, Extraktzeile 14; Buchseiten 332, 333, 338 und 339.
- **Originalbezeichnung:** `hStegB = sStegB + 0,5`
- **Normalisierte Bezeichnung:** `hintere_stegbreite_aus_seitlicher_stegbreite_breiter_kragen`

### Buchfassung
```text
- hStegB = sStegB + 0,5
```

```text
7. Am seitlichen Halsloch 2× die sStegB nach oben abtragen, an der hM 2× die hStegB (= sStegB + 0,5 cm).
```

```text
- `sStegB wie vorne` / `hStegB = sStegB + 0,5`
```

```text
7. Am seitlichen Halsloch 2× die sStegB nach oben abtragen, an der hM 2× die hStegB (= sStegB + 0,5 cm).
```

Die vier Blöcke sind vier eigenständige, exakt erhaltene Buchnachweise derselben additiven Beziehung; sie erzeugen keine doppelten Formel-IDs.

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `seitliche_stegbreite` | sStegB | 1,5 bis 3 | cm |
| `hinterer_steg_zuschlag` | + 0,5 cm | 0,5 | cm |

### Formel und Rechenschritte
```text
hintere_stegbreite = seitliche_stegbreite + 0,5 cm
```

### Ausgabe
`hintere_stegbreite` — hStegB, in cm.

- **Abhängigkeiten:** `seitliche_stegbreite`.
- **Gültigkeitsbereich:** Breite Schal- und Reverskragen mit Rückteil-Anlage, S. 332–339.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt einen Bereich für sStegB, aber keine Auswahlregel. Die `2×`-Angaben sind Abtrag-/Zeichnungsangaben, kein Rechenfaktor.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zuschlag fest mit `0,5 cm` führen; die Bereichsauswahl außerhalb dieser Formel treffen.

## Ausgeschlossene Kandidaten

| Buchseite / Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| S. 332, 9 | 1 | Maßstabsfaktor ohne fachliche Zielberechnung |
| S. 332, 14 und 19–21 | 4 | Direkte Halslochverbreiterung, Stegbreitenbereich, Abtrag- und Zeichnungsangaben ohne eigenständige Zielberechnung |
| S. 332, 31 | 1 | Fassondefinition ohne Rechenoperation |
| **Summe S. 332** | **6** | **Maßstabs-, Eingabe-, Abtrags- und Definitionsangaben ausgeschlossen** |

Die Kandidatenzeilen S. 333/14, S. 338/24 und S. 339/14 sind oben als zusätzliche Buchnachweise vertreten, nicht ausgeschlossen.
