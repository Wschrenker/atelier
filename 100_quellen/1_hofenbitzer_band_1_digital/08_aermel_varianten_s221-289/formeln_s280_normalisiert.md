# Fachlich normalisierte Formeln — S. 280

Quelle der Normalisierung: `formeln_s280_digital_geprüft.md`
Originaltranskript: `s280_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 280
Extraktionsstand: v2

## HOF-B1-S280-F01 — Armlochverbreiterung aus der Armlochvertiefung

- **Fachlicher Zweck:** Die Armlochverbreiterung vorne und hinten als ergänzende Anteile der Armlochvertiefung bestimmen.
- **Quelle:** `formeln_s280_digital_geprüft.md`, Zeilen 14 und 24; Originaltranskript `s280_digital_geprüft.md`, Zeilen 32 und 47; Buchseite 280.
- **Originalbezeichnung:** Al-Verbreit., Al-Vert.
- **Normalisierte Bezeichnung:** `armlochverbreiterung_vorne_hinten`

### Buchfassung

Vorderteil:

```text
- Al-Verbreit. = ca. ⅓ Al-Vert.
```

Rückteil:

```text
- Al-Verbreit. = ca. ⅔ Al-Vert.
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `armlochvertiefung` | Al-Vert. | cm |

### Formel und Rechenschritte

```text
armlochverbreiterung_vorne = armlochvertiefung * (1 / 3)
armlochverbreiterung_hinten = armlochvertiefung * (2 / 3)

armlochverbreiterung_vorne + armlochverbreiterung_hinten = armlochvertiefung
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `armlochverbreiterung_vorne` | Armlochverbreiterung am Vorderteil | cm |
| `armlochverbreiterung_hinten` | Armlochverbreiterung am Rückteil | cm |

- **Abhängigkeiten:** Die für die Dolman-Anlage gewählte Armlochvertiefung.
- **Gültigkeitsbereich:** Dolman-Ärmel-Anlage auf S. 280; der vordere Drittelanteil gilt für das Vorderteil, der hintere Zweidrittelanteil für das Rückteil.
- **Technische Randbedingung:** Beide Beziehungen sind mit `ca.` angegeben. Die Armlochvertiefung muss als nichtnegative Länge vorliegen. Die Summe der idealen Bruchteile ist eine technische Kontrollgleichung, keine zusätzliche Buchfassung.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Unstimmigkeit. Die Quelle nennt keine Rundungsregel und keinen festen Wert innerhalb des Bereichs von `2 bis 10 cm`, der nur im Transkript als Zeichnungsangabe erscheint.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Beide Ausgaben gemeinsam aus derselben Armlochvertiefung berechnen, als Näherungswerte kennzeichnen und die Summenkontrolle mit einer Dezimaltoleranz durchführen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s280_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Bildnummern-/Konstruktionsanweisung mit einer Mindestvertiefung von `2 cm`; Eingabegrenze und Methode, keine berechnete Ausgabe |
| Zeile 19 | 1 | Übertragungslabel `wie vorne (2×)`; Wiederholungsnotation ohne eigenständige Rechenbeziehung |
| **Summe** | **2** | **1 Methoden-/Eingabezeile + 1 Wiederholungslabel** |

## Extraktionsgrenze

Das Originaltranskript nennt in Zeile 11 den Anlagepunkt als `⅔ bis zum ganzen Betrag der Armlochvertiefung`, in Zeile 12 eine Schulterüberschneidung von `0 bis 1 cm` und in Zeile 14 einen maximalen Abstand von `3 cm`. Diese Angaben fehlen im verbindlichen Extrakt und wurden nicht als zusätzliche Buchfassungen normalisiert. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
