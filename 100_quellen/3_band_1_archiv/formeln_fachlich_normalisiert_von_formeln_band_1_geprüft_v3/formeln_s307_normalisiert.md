# Fachlich normalisierte Formeln — S. 307

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s307.md`  
Originaltranskript: `s307.md`  
Buchseite: Hofenbitzer, Band 1, S. 307

## HOF-B1-S307-F01 — Teilungsabstände am Volantkragen

- **Fachlicher Zweck:** Den hinteren Grundabstand und die übrigen, doppelt so großen Einschnittabstände am Volantkragen bestimmen.
- **Quelle:** `formeln_s307.md`, Zeilen 7–10, 12–15 und 17–20 (Buchfassung Zeilen 48, 50 und 54); Originaltranskript `s307.md`, Zeilen 48, 50 und 54; Buchseite 307.
- **Originalbezeichnung:** `1 : (geplante Einschnitte · 2 + 1)`; Beispiel `1 : (7 Einschnitte · 2 + 1) = 1/15`; übrige Abstände `2/15`.
- **Normalisierte Bezeichnung:** `volantkragen_einschnittabstaende_aus_anzahl_der_einschnitte`

### Buchfassung

```text
> 1 : (geplante Einschnitte · 2 + 1)
```

```text
> hier: 1 : (7 Einschnitte · 2 + 1) = 1/15
```

```text
Zeichnungsangaben: 1/15 (an der hM); 2/15 (siebenmal); KrB an der hM = ca. 0 bis 1 cm; KrB an der vM = ca. 1 bis 3 cm; KrB (dreimal); ca. ½ SuB; KrKa; SuP; SuN; hM; vM; RT-Grundschnitt; VT-Grundschnitt.
```

### Formel und Rechenschritte

```text
hinterer_einschnittabstand = 1 / (geplante_einschnitte * 2 + 1)
uebriger_einschnittabstand = 2 * hinterer_einschnittabstand
```

Buchbeispiel:

```text
hinterer_einschnittabstand = 1 / (7 * 2 + 1) = 1/15
uebriger_einschnittabstand = 2 * 1/15 = 2/15
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hinterer_einschnittabstand` | hinterer Abstand als Anteil der Bezugslänge | 1/15 | dimensionslos |
| `uebriger_einschnittabstand` | übriger Abstand als Anteil der Bezugslänge | 2/15 | dimensionslos |

- **Abhängigkeiten:** Anzahl der geplanten Einschnitte; Bezugslänge der Kragenkante.
- **Gültigkeitsbereich:** Volantkragen am breiten Ausschnitt; die Buchseite nennt sieben geplante Einschnitte und sieben übrige Abstände.
- **Technische Randbedingung:** Die Bruchteile sind Anteile einer noch zu bestimmenden Bezugslänge, nicht bereits Zentimeterwerte.
- **Offene Fragen oder Widersprüche:** Keine arithmetische Unklarheit. Die konkrete Bezugslänge und die Auswahl der Kragenbreiten werden nicht durch diese Teilungsformel bestimmt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Anzahl der Einschnitte als positive ganze Zahl validieren; Bezugslänge separat übergeben.
