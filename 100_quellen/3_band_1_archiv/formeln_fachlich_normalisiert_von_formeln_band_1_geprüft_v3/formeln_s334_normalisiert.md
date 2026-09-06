# Fachlich normalisierte Formeln — S. 334

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s334.md`  
Originaltranskript: `s334.md`  
Buchseite: Hofenbitzer, Band 1, S. 334

## HOF-B1-S334-F01 — Verstürzweite als halbe Rollweite

- **Fachlicher Zweck:** Eine ungefähre Verstürzweite aus der Rollweite ableiten.
- **Quelle:** `formeln_s334.md`, Extraktzeile 9; Originaltranskript `s334.md`, Zeile 8; Buchseite 334.
- **Originalbezeichnung:** `½ Rollweite = Verstürzweite`
- **Normalisierte Bezeichnung:** `verstuerzweite_als_halbe_rollweite_breiter_schalkragen`

### Buchfassung
```text
23. Unten am Kragenbeginn nur ca. ½ Rollweite = Verstürzweite anzeichnen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `rollweite` | Rollweite | variabel | cm |
| `halbierungsfaktor` | ½ | 1/2 | dimensionslos |

### Formel und Rechenschritte
```text
verstuerzweite ≈ rollweite / 2
```

### Ausgabe
`verstuerzweite` — ungefähre anzuzeichnende Verstürzweite am Kragenbeginn, in cm.

- **Abhängigkeiten:** `rollweite`.
- **Gültigkeitsbereich:** Breiter Schalkragen mit Rückteil-Anlage, S. 334.
- **Offene Fragen oder Widersprüche:** `ca.` kennzeichnet eine Näherung; eine Rundungs- oder Fertigungsregel ist nicht belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Näherungscharakter erhalten und Rundung nicht automatisch festlegen.

## Ausgeschlossene Kandidaten

Keine. Die einzige extrahierte Kandidatenzeile ist in `HOF-B1-S334-F01` abgebildet.
