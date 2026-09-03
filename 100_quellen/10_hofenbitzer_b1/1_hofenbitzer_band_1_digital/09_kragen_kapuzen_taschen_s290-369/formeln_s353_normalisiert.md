# Fachlich normalisierte Formeln — S. 353

Quelle der Normalisierung: `formeln_s353_digital_geprüft.md`
Originaltranskript: `s353_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 353
Extraktionsstand: v2

Hinweis: Die auf dieser Seite ebenfalls extrahierte Kapuzenhöhenformel ist als zusätzlicher Anwendungsnachweis unter `HOF-B1-S352-F01` in `formeln_s352_normalisiert.md` erhalten.

## HOF-B1-S353-F01 — Kapuzentiefe aus Kapuzenhöhe

- **Fachlicher Zweck:** Die Kapuzentiefe durch Abzug eines ungefähren Bereichs von der Kapuzenhöhe bestimmen.
- **Quelle:** `formeln_s353_digital_geprüft.md`, Zeile 9; Originaltranskript `s353_digital_geprüft.md`, Zeile 11; Buchseite 353.
- **Originalbezeichnung:** Kapuzentiefe (KapT), Kapuzenhöhe (KapH)
- **Normalisierte Bezeichnung:** `kapuzentiefe`

### Buchfassung

```text
- Kapuzentiefe (KapT) = KapH – ca. 4 bis 6 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `kapuzenhoehe` | KapH, Kapuzenhöhe | nach `HOF-B1-S352-F01` | cm |
| `tiefenabzug` | ca. 4 bis 6 cm | 4 bis 6 | cm |

### Formel und Rechenschritte

```text
kapuzentiefe = kapuzenhoehe - tiefenabzug
kapuzentiefe_min = kapuzenhoehe - 6 cm
kapuzentiefe_max = kapuzenhoehe - 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchergebnis | Einheit |
|---|---|---:|---|
| `kapuzentiefe` | KapT, Kapuzentiefe | KapH minus ca. 4 bis 6 | cm |

- **Abhängigkeiten:** Kapuzenhöhe `KapH`, technisch aus `HOF-B1-S352-F01`, sowie ein fachlich gewählter Abzug im ungefähren Bereich von `4 bis 6 cm`.
- **Gültigkeitsbereich:** Elegante Kapuze mit tiefer Diagonalnaht und zusätzlicher Weite auf S. 353; laut Seitenüberschrift für alle Materialien.
- **Technische Randbedingung:** Wegen der Subtraktion erzeugt der größere Abzug die kleinere Kapuzentiefe. Die Ausgabegrenzen werden nach ihrer Größe und nicht nach der gedruckten Reihenfolge der Abzüge benannt. Der gewählte Abzug darf die Kapuzenhöhe nicht überschreiten.
- **Offene Fragen oder Widersprüche:** Kein rechnerischer Widerspruch. Die Quelle kennzeichnet den Abzug mit `ca.` und nennt keine Auswahlregel für einen konkreten Wert zwischen `4` und `6 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Abzug als explizite Eingabe im Bereich `4 bis 6 cm` verlangen, die Näherungskennzeichnung erhalten und keine automatische Auswahlregel erfinden.

## Ausgeschlossene Kandidaten

Keine. Die zweite extrahierte Kandidatenzeile dieser Seite ist als Anwendungsnachweis der Kapuzenhöhenformel in `formeln_s352_normalisiert.md` abgebildet.

## Extraktionsgrenze

Das Originaltranskript enthält auf S. 353 weitere Verhältnis- und Maßangaben wie `ca. ⅖ bis ⅘ der vHlL`, `⅓`, `2 bis 4 cm` und die vier unbezeichneten Bereiche für die Kapuze mit Mittelstreifen. Diese Angaben fehlen im verbindlichen Extrakt und wurden nicht als zusätzliche Buchfassungen erfunden. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
