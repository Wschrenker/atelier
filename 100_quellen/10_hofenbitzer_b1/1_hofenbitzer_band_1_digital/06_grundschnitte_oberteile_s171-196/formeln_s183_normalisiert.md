# Fachlich normalisierte Formeln — S. 183

Quelle der Normalisierung: `formeln_s183_digital_geprüft.md`
Originaltranskript: `s183_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 183
Extraktionsstand: v2

## HOF-B1-S183-F01 — Maximalabstand für den Brustabnäher

- **Fachlicher Zweck:** Den maximalen Abstand zur vorderen Armlinie aus einem Zwanzigstel des Brustumfangs bestimmen, bis zu dem der vordere Schulterpunkt für den Brustabnäher gedreht werden darf.
- **Quelle:** `formeln_s183_digital_geprüft.md`, Zeile 9; Originaltranskript `s183_digital_geprüft.md`, Zeilen 25, 50 und 52; Buchseite 183.
- **Originalbezeichnung:** `maximal BrU:20`
- **Normalisierte Bezeichnung:** `maximalabstand_brustabnaeher_zur_armlinie`

### Buchfassung

```text
- maximal BrU:20
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `brustumfang` | BrU | nicht angegeben | cm |
| `teilungsfaktor` | 20 | 20 | dimensionslos |

### Formel und Rechenschritte

```text
maximalabstand_zur_armlinie = brustumfang / 20
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `maximalabstand_zur_armlinie` | maximaler Abstand rechts der vorderen Armlinie bis Li26 | nicht angegeben | cm |

- **Abhängigkeiten:** Brustumfang und geometrische Lage der vorderen Armlinie.
- **Gültigkeitsbereich:** Legerer Oberteil-Grundschnitt mit Brust- und Schulterabnäher auf S. 183; Begrenzung der Drehung von vSuP1 in Richtung Li26.
- **Technische Randbedingung:** Der Brustumfang muss positiv sein. Das Buch erlaubt ausdrücklich eine kleinere Drehung (`hier weniger`); der berechnete Wert ist eine Obergrenze, kein automatisch zu verwendender Zielwert.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine Regel, nach der innerhalb der Obergrenze der tatsächlich verwendete Abstand gewählt wird.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Maximalbedingung modellieren. Den tatsächlichen Drehbetrag als gesonderte, auf `0 <= drehabstand <= brustumfang / 20` begrenzte Eingabe verlangen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s183_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Unvollständiges Zeichnungslabel `+ hHüB messen = HüB`; Wiederholung der auf S. 182 vollständig normalisierten Beziehung `HOF-B1-S182-F01`, die der Text auf S. 183 ausdrücklich von der vorhergehenden Seite übernimmt |
| **Summe** | **1** | **1 unvollständige seitenübergreifende Wiederholung ausgeschlossen** |
