# Fachlich normalisierte Formeln — S. 327

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s327.md`  
Originaltranskript: `s327.md`  
Buchseite: Hofenbitzer, Band 1, S. 327

## HOF-B1-S327-F01 — Verstürzweite als halbe Rollweite

- **Fachlicher Zweck:** Eine ungefähre Verstürzweite aus der Rollweite ableiten.
- **Quelle:** `formeln_s327.md`, Extraktzeile 14; Originaltranskript `s327.md`, Zeile 25; Buchseite 327.
- **Originalbezeichnung:** `Verstürzweite = ca. ½ Rollweite anzeichnen`
- **Normalisierte Bezeichnung:** `verstuerzweite_als_halbe_rollweite`

### Buchfassung
```text
- Verstürzweite = ca. ½ Rollweite anzeichnen
```

### Eingaben
`rollweite`, variabel, cm; Faktor `½`, dimensionslos.

### Formel und Rechenschritte
```text
verstuerzweite ≈ rollweite / 2
```

### Ausgabe
`verstuerzweite` — anzuzeichnende Verstürzweite, cm.

- **Abhängigkeiten:** Rollweite.
- **Gültigkeitsbereich:** Steigendes Revers, S. 327.
- **Randbedingung:** `ca.` bezeichnet einen Näherungswert; eine exakte Rundungs- oder Fertigungsregel fehlt.
- **Offene Fragen oder Widersprüche:** Keine eindeutige Auswahl der Näherung belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Näherungscharakter und fachliche Rundung getrennt behandeln.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Maßstabsfaktor ohne fachliche Zielberechnung |
| **Summe** | **1** | **Maßstabsangabe ausgeschlossen** |
