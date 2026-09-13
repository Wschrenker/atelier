# Fachlich normalisierte Formeln — S. 264, 266 und 268

Quelle der Normalisierung: `formeln_s264_digital_geprüft.md`, zusätzliche Anwendungsnachweise in `formeln_s266_digital_geprüft.md` und `formeln_s268_digital_geprüft.md`
Originaltranskripte: `s264_digital_geprüft.md`, `s266_digital_geprüft.md`, `s268_digital_geprüft.md`
Buchseiten: Hofenbitzer, Band 1, S. 264, 266 und 268
Extraktionsstand: v2

## HOF-B1-S264-F01 — Mindestabstand zwischen Ärmel- und Rumpffläche

- **Fachlicher Zweck:** Den Mindestabstand zwischen Ärmel- und Rumpffläche so bestimmen, dass die Nahtzugaben der getrennten Schnittteile Platz haben.
- **Quelle:** `formeln_s264_digital_geprüft.md`, Zeilen 14 und 19; Originaltranskript `s264_digital_geprüft.md`, Zeilen 13 und 19; zusätzliche Anwendungsnachweise in `formeln_s266_digital_geprüft.md`, Zeilen 9 und 14, mit Originaltranskript `s266_digital_geprüft.md`, Zeilen 15 und 19, sowie in `formeln_s268_digital_geprüft.md`, Zeile 24, mit Originaltranskript `s268_digital_geprüft.md`, Zeile 37; Buchseiten 264, 266 und 268.
- **Originalbezeichnung:** Mindest-Abstand, Mindestabstand, Nahtzugabe, NZg
- **Normalisierte Bezeichnung:** `mindestabstand_aermel_rumpf`

### Buchfassung

```text
Diagrammhinweis: Mindest-Abstand von 2× Nahtzugabe zwischen Ärmel und Oberteil bei den großen Schnittteilen
```

Zweiter Nachweis auf S. 264:

```text
Die Teilungsnähte haben den Zweck, die Überschneidungsflächen unter dem Arm mit separaten Schnittteilen zu isolieren, so dass diese Flächen wieder doppelt vorliegen. Hierzu ist wichtig, dass ein Mindestabstand zwischen Ärmel- und Rumpf beim großen Schnittteil 2× Nahtzugabe beträgt!
```

Zusätzlicher Diagrammnachweis auf S. 266:

```text
Diagrammhinweis: Mindest-Abstand von 2× Nahtzugabe zwischen Ärmel und Oberteil bei den großen Schnittteilen
```

Zusätzlicher Textnachweis auf S. 266:

```text
□1 Auch hier haben die Teilungsnähte den Zweck, die Überschneidungsflächen unter dem Arm mit separaten Schnittteilen zu isolieren, so dass diese Flächen wieder doppelt vorliegen. Der Mindestabstand zwischen Ärmel- und Rumpf von 2× Nahtzugabe muss eingehalten werden.
```

Anwendungsnachweis am Drachenkeil auf S. 268:

```text
3. □3 Von P1 eine Keilnaht (orange) an die Seitennaht (SN) und von P1 eine weitere Keilnaht (blau) an die Ärmelnaht (ÄN) zeichnen. Dabei muss der untere Abstand mind. 2× NZg betragen. Die Naht an der Seitennaht sollte so kurz als möglich sein.
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `nahtzugabe` | Nahtzugabe / NZg | cm |

### Formel und Rechenschritte

```text
mindestabstand_aermel_rumpf = 2 * nahtzugabe
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `mindestabstand_aermel_rumpf` | kleinster Abstand zwischen Ärmel- und Rumpffläche beziehungsweise zwischen den unteren Keilnähten | cm |

- **Abhängigkeiten:** Die für die betreffenden Schnittteile gewählte Nahtzugabe.
- **Gültigkeitsbereich:** Kimono-Abtrennungen mit separaten Überschneidungsflächen auf S. 264 und 266 sowie die unteren Keilnähte des Drachenkeil-Kimonos auf S. 268.
- **Technische Randbedingung:** Der Faktor `2` ist dimensionslos. Die Abstandsrichtung und die jeweils betroffenen Kanten bleiben geometrische Angaben und dürfen nicht in den skalaren Wert eingemischt werden.
- **Offene Fragen oder Widersprüche:** Keine. Die Quelle nennt keinen festen Zahlenwert für die Nahtzugabe; sie muss als explizite Längeneingabe vorliegen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Eine gemeinsame Regel für alle drei belegten Anwendungen verwenden, `nahtzugabe >= 0` prüfen und den berechneten Mindestabstand getrennt von der geometrischen Kollisionsprüfung führen.

## Ausgeschlossene Kandidaten der Formelquellen

| Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s264_digital_geprüft.md`, Zeile 9 | 1 | Beschreibender Seitenverweis `253 + 255`; Pluszeichen verbindet Buchseiten und ist kein Rechenoperator |
| `formeln_s264_digital_geprüft.md`, Zeile 24 | 1 | Bildnummern- und Methodenverweis zur Nahtführung; keine skalare Rechenausgabe |
| `formeln_s266_digital_geprüft.md`, Zeile 19 | 1 | Bildnummern- und Konstruktionshinweis mit direkter Gleichheitsbedingung für zwei geometrische Abstände; keine skalare Berechnung |
| `formeln_s268_digital_geprüft.md`, Zeile 9 | 1 | Beschreibender Seitenverweis `253 + 255`; Pluszeichen verbindet Buchseiten und ist kein Rechenoperator |
| `formeln_s268_digital_geprüft.md`, Zeilen 14 und 19 | 2 | Unvollständige Zeichnungslabels mit Wiederholungsangabe `(2×)`; Bezugsgröße beziehungsweise Ausgabe fehlt |
| `formeln_s268_digital_geprüft.md`, Zeilen 29 und 34 | 2 | Arbeitspunkt-Beschriftungen mit Wiederholungsangabe `(2×)`; keine Rechenbeziehung |
| **Summe** | **8** | **2 Seitenverweise + 2 Bild-/Methodenangaben + 2 unvollständige Labels + 2 Wiederholungsbeschriftungen** |

## Extraktionsgrenze

Die Transkripte enthalten weitere zahlen- oder gleichheitsartige Konstruktionsangaben, darunter identische Nahtlängen zwischen Knipsen auf S. 262, identische Abstände zwischen SuP und Naht auf S. 266 sowie die Anwendungsgrenze von bis zu `3 cm` Armlochvertiefung und den Abstand von ca. `1 cm` am Ärmelpunkt auf S. 268 und 270. Diese Stellen fehlen entweder im verbindlichen Extrakt oder beschreiben direkte geometrische Bedingungen ohne skalare Rechenausgabe. Sie wurden nicht als zusätzliche Buchformeln erfunden. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
