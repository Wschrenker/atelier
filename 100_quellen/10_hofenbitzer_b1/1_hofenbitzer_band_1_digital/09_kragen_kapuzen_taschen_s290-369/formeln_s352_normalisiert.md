# Fachlich normalisierte Formeln — S. 352 und S. 353

Quelle der Normalisierung: `formeln_s352_digital_geprüft.md`, zusätzlicher Anwendungsnachweis in `formeln_s353_digital_geprüft.md`
Originaltranskripte: `s352_digital_geprüft.md`, `s353_digital_geprüft.md`
Buchseiten: Hofenbitzer, Band 1, S. 352 und S. 353
Extraktionsstand: v2

## HOF-B1-S352-F01 — Kapuzenhöhe aus dem Überkopfumfang

- **Fachlicher Zweck:** Die Kapuzenhöhe als Hälfte des Überkopfumfangs bestimmen.
- **Quelle:** `formeln_s352_digital_geprüft.md`, Zeilen 9 und 14; Originaltranskript `s352_digital_geprüft.md`, Zeilen 11 und 27; zusätzlicher Anwendungsnachweis in `formeln_s353_digital_geprüft.md`, Zeile 10, und `s353_digital_geprüft.md`, Zeile 12; Buchseiten 352 und 353.
- **Originalbezeichnung:** Kapuzenhöhe (KapH), üKoU
- **Normalisierte Bezeichnung:** `kapuzenhoehe`

### Buchfassung

```text
- Kapuzenhöhe (KapH) = ½ üKoU
```

Zweiter Nachweis auf S. 352 für eine weitere Kapuzenvariante:

```text
- Kapuzenhöhe (KapH) = ½ üKoU
```

Zusätzlicher Anwendungsnachweis auf S. 353:

```text
- Kapuzenhöhe (KapH) = ½ üKoU
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `ueberkopfumfang` | üKoU, Überkopfumfang | cm |

### Formel und Rechenschritte

```text
kapuzenhoehe = ueberkopfumfang / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kapuzenhoehe` | KapH, Kapuzenhöhe | cm |

- **Abhängigkeiten:** Gemessener Überkopfumfang `üKoU`.
- **Gültigkeitsbereich:** Die auf S. 352 dargestellten sportlichen Kapuzenvarianten mit Diagonalnaht sowie die elegante Kapuze auf S. 353; jeweils für alle Materialien laut Seitenüberschrift.
- **Technische Randbedingung:** Der Überkopfumfang muss als nichtnegative Länge vorliegen. Die Formel bestimmt nur die Höhe; Form, Weite und Teilungsnähte werden dadurch nicht festgelegt.
- **Offene Fragen oder Widersprüche:** Keine. Die dreifache wortgleiche Angabe belegt dieselbe Beziehung für drei Kapuzenvarianten und erzeugt keine drei technischen Regeln.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Eine gemeinsame Funktion verwenden, die `ueberkopfumfang / 2` berechnet; die drei Buchvorkommen bleiben Anwendungsnachweise derselben Regel.

## Ausgeschlossene Kandidaten

Keine. Beide extrahierten Kandidatenzeilen von S. 352 sind als Buchfassungsnachweise abgebildet.

## Extraktionsgrenze

Das Originaltranskript nennt auf S. 352 zusätzlich die Teilungsverhältnisse `ca. ⅖ bis ⅗ der vHlL` und `⅓`, auf S. 353 die Bereiche `ca. ⅖ bis ⅘ der vHlL`, `⅓` sowie weitere unbezeichnete Zeichnungsmaße. Diese Angaben fehlen im verbindlichen Extrakt oder besitzen dort keine vollständige Rechenbeziehung und wurden nicht als zusätzliche Buchfassungen erfunden. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
