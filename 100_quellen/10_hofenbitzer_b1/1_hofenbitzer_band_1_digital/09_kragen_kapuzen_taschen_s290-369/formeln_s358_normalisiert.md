# Fachlich normalisierte Formeln — S. 358 und S. 360

Quelle der Normalisierung: `formeln_s358_digital_geprüft.md`, zusätzlicher Anwendungsnachweis in `formeln_s360_digital_geprüft.md`
Originaltranskripte: `s358_digital_geprüft.md`, `s360_digital_geprüft.md`
Buchseiten: Hofenbitzer, Band 1, S. 358 und S. 360
Extraktionsstand: v2

## HOF-B1-S358-F01 — Gesamter Falteninhalt einer Kellerfalte

- **Fachlicher Zweck:** Den gesamten Öffnungsbetrag einer Kellerfalte als vierfache Faltentiefe bestimmen.
- **Quelle:** `formeln_s358_digital_geprüft.md`, Zeile 9; Originaltranskript `s358_digital_geprüft.md`, Zeile 38; zusätzlicher Anwendungsnachweis in `formeln_s360_digital_geprüft.md`, Zeile 9, und `s360_digital_geprüft.md`, Zeile 12; Buchseiten 358 und 360.
- **Originalbezeichnung:** gesamter Falteninhalt, `4× FaT`
- **Normalisierte Bezeichnung:** `gesamter_falteninhalt_kellerfalte`

### Buchfassung

```text
1. Die Taschenform nach Wunsch gestalten und das halbierte Vorderblatt waagerecht um den gesamten Falteninhalt (4× FaT) öffnen.
```

Zusätzlicher Anwendungsnachweis auf S. 360 mit Buchwert:

```text
2. Die Tasche in der Mitte für die Kellerfalte teilen und entsprechend den gesamten Falteninhalt öffnen (4× FaT, hier 4 mal 1,5 cm).
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert auf S. 360 | Einheit |
|---|---|---:|---|
| `faltentiefe` | FaT, Faltentiefe | 1,5 | cm |
| `anzahl_faltentiefen` | `4×` | 4 | dimensionslos |

### Formel und Rechenschritte

```text
gesamter_falteninhalt_kellerfalte = anzahl_faltentiefen * faltentiefe
                                      = 4 * faltentiefe
Buchwert S. 360:                     = 4 * 1,5 cm
Technisch berechnet:                 = 6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Technisch berechneter Wert auf S. 360 | Einheit |
|---|---|---:|---|
| `gesamter_falteninhalt_kellerfalte` | gesamter Öffnungsbetrag der Kellerfalte | 6 | cm |

- **Abhängigkeiten:** Eine für die jeweilige Tasche festgelegte `faltentiefe`; keine seitenübergreifende Zahlenabhängigkeit. Die Bezeichnung FaT ist mit der auf S. 89 belegten Faltentiefe vereinbar, der konkrete Taschenwert wird hier jedoch eigenständig gewählt.
- **Gültigkeitsbereich:** Uniformtasche mit Kellerfalte auf S. 358 und Cargotasche mit angeschnittenem Rahmen und Kellerfalte auf S. 360.
- **Technische Randbedingung:** Die Faltentiefe muss als nichtnegative Länge vorliegen. Der Faktor `4` gehört zur beidseitig gelegten Kellerfalte und darf nicht ungeprüft auf andere Faltenarten übertragen werden.
- **Offene Fragen oder Widersprüche:** Kein rechnerischer Widerspruch. S. 360 druckt die Multiplikation `4 mal 1,5 cm`, aber kein Ergebnis; `6 cm` ist deshalb als technische Berechnung und nicht als Buchergebnis ausgewiesen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Eine Kellerfaltenfunktion mit expliziter `faltentiefe` verwenden und den Gesamtöffnungsbetrag mit dem festen, auf diesen beiden Konstruktionen belegten Faktor `4` berechnen.

## Ausgeschlossene Kandidaten

| Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s358_digital_geprüft.md`, Zeile 14 | 1 | Produktionsbeschriftung `Patte 2× OSt (+El)`; Stückzahl und Material, keine berechnete Ausgabe |
| `formeln_s360_digital_geprüft.md`, Zeile 14 | 1 | Produktionsbeschriftung `Patte 2× OSt (+El)`; Stückzahl und Material, keine berechnete Ausgabe |
| **Summe** | **2** | **2 Produktionsbeschriftungen** |

## Extraktionsgrenze

Die Originaltranskripte enthalten weitere Gestaltungsbereiche, Nahtzugaben, einzelne Zeichnungsmaße und Produktionsbeschriftungen. Sie bilden im verbindlichen Extrakt keine zusätzlichen vollständigen Rechenbeziehungen und wurden nicht als Buchfassungen ergänzt. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
