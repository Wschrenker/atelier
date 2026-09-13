# Fachlich normalisierte Formeln — S. 190

Quelle der Normalisierung: `formeln_s190_digital_geprüft.md`
Originaltranskript: `s190_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 190
Extraktionsstand: v2

## HOF-B1-S190-F01 — Unbezeichneter Brustumfangsbereich

- **Fachlicher Zweck:** Den gedruckten Bereich von einem Zwanzigstel des Brustumfangs minus 1 cm bis plus 1 cm technisch darstellen, ohne einen nicht belegten geometrischen Zielreferenten zu erfinden.
- **Quelle:** `formeln_s190_digital_geprüft.md`, Zeile 9; Originaltranskript `s190_digital_geprüft.md`, Zeile 25; Buchseite 190.
- **Originalbezeichnung:** `BrU : 20 − 1 bis + 1 cm`
- **Normalisierte Bezeichnung:** `unbezeichneter_brumfangsbereich`

### Buchfassung

```text
- BrU : 20 − 1 bis + 1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustumfang` | BrU | nicht angegeben | cm |
| `untere_korrektur` | −1 cm | −1 | cm |
| `obere_korrektur` | +1 cm | 1 | cm |

### Formel und Rechenschritte

```text
grundwert = brustumfang / 20
untere_grenze = grundwert - 1 cm
obere_grenze = grundwert + 1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `untere_grenze` | kleinerer Wert des gedruckten Bereichs | nicht angegeben | cm |
| `obere_grenze` | größerer Wert des gedruckten Bereichs | nicht angegeben | cm |

- **Abhängigkeiten:** BrU; der geometrische Anwendungspunkt ist im Extrakt nicht benannt.
- **Gültigkeitsbereich:** Zeichnungsbeschriftung der zwei Vorderteilvarianten des engen Oberteil-Grundschnitts auf S. 190.
- **Technische Randbedingung:** Die Grenzen sind nach resultierender Größe benannt. Eine spätere Anwendung muss den fehlenden geometrischen Referenten ausdrücklich liefern.
- **Offene Fragen oder Widersprüche:** Aus Transkript und Extrakt ist nicht eindeutig ersichtlich, welche Strecke oder Position mit diesem Bereich bestimmt wird. Die Formel ist deshalb nicht ausführbar zugeordnet.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nur die symbolische Bereichsbildung vormerken; bis zur geometrischen Quellenprüfung keine Schnittstrecke damit verändern.

## Ausgeschlossene Kandidaten

Keine. Die einzige extrahierte Kandidatenzeile ist als offene Formel abgebildet.
