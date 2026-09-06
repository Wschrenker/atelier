# Fachlich normalisierte Formeln — S. 286

Quelle der Normalisierung: `formeln_s286_digital_geprüft.md`
Originaltranskript: `s286_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 286
Extraktionsstand: v2

## HOF-B1-S286-F01 — Schulteröffnung für ein Schulterpolster

- **Fachlicher Zweck:** Die günstige Schulteröffnung bei einem Fledermausärmel näherungsweise aus der Schulterpolsterdicke bestimmen.
- **Quelle:** `formeln_s286_digital_geprüft.md`, Zeile 9; Originaltranskript `s286_digital_geprüft.md`, Zeile 13; Buchseite 286.
- **Originalbezeichnung:** Öffnung an der Schulter, Schulterpolsterdicke
- **Normalisierte Bezeichnung:** `schulteroeffnung_fledermausaermel`

### Buchfassung

```text
□1+2 Vom Knips am Schulterpunkt wird an VT und RT an dieselbe Stelle zur Unterarmnaht eingeschnitten. Die Öffnung an der Schulter ist abhängig von der Dicke des Schulterpolsters. Günstig wäre, ca. die doppelte Schulterpolsterdicke zu öffnen.
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `schulterpolsterdicke` | Dicke des Schulterpolsters | cm |

### Formel und Rechenschritte

```text
schulteroeffnung = 2 * schulterpolsterdicke
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `schulteroeffnung` | günstiger näherungsweiser Öffnungsbetrag an der Schulter von VT und RT | cm |

- **Abhängigkeiten:** Die Dicke des vorgesehenen Schulterpolsters.
- **Gültigkeitsbereich:** Fledermausärmel-Anlage mit Schulterpolster auf S. 286; die Öffnung erfolgt an Vorder- und Rückteil vom Schulterpunkt zur Unterarmnaht.
- **Technische Randbedingung:** Der Faktor `2` ist dimensionslos. Wegen `ca.` und `Günstig wäre` ist das Ergebnis ein Richtwert, keine exakte Vorgabe.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Unstimmigkeit. Die Quelle nennt keine Toleranz für die näherungsweise Verdopplung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Wert als empfohlenen Näherungswert ausgeben, `schulterpolsterdicke >= 0` prüfen und die geometrische Lage der Einschnitte separat behandeln.

## Ausgeschlossene Kandidaten

Keine. Die eine extrahierte Kandidatenzeile ist vollständig abgebildet.

## Extraktionsgrenze

Das Originaltranskript nennt in Zeile 15 als optimale Aufteilung der Schulterpolster-Erhöhung vorne `⅓` und hinten `⅔`. Diese zusätzliche Beziehung fehlt im verbindlichen Extrakt und wurde nicht als Buchfassung normalisiert. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
