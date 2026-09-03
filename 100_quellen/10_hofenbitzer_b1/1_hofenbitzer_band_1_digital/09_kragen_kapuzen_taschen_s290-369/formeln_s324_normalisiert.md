# Fachlich normalisierte Formeln — S. 324

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s324.md`  
Originaltranskript: `s324.md`  
Buchseite: Hofenbitzer, Band 1, S. 324

## HOF-B1-S324-F01 — Verstürzweite als Drittel der Rollweite

- **Fachlicher Zweck:** Eine ungefähre Verstürzweite aus der Rollweite ableiten.
- **Quelle:** `formeln_s324.md`, Extraktzeile 14; Originaltranskript `s324.md`, Zeile 55; Buchseite 324.
- **Originalbezeichnung:** `Verstürzweite = ca. ⅓ Rollweite anzeichnen`
- **Normalisierte Bezeichnung:** `verstuerzweite_als_drittel_der_rollweite`

### Buchfassung
```text
- Verstürzweite = ca. ⅓ Rollweite anzeichnen
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `rollweite` | Rollweite | variabel | cm |
| `drittel_faktor` | ⅓ | 1/3 | dimensionslos |

### Formel und Rechenschritte
```text
verstuerzweite ≈ rollweite / 3
```

### Ausgabe
`verstuerzweite` — anzuzeichnende Verstürzweite, in cm.

- **Abhängigkeiten:** Rollweite.
- **Gültigkeitsbereich:** Revers- und Oberkragenvarianten auf S. 324.
- **Randbedingung:** `ca.` kennzeichnet eine ungefähre Konstruktionsregel, keine exakte Fertigungs- oder Rundungsvorschrift.
- **Offene Fragen oder Widersprüche:** Genauigkeit und Rundung sind nicht festgelegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Näherungswert ausgeben und die fachliche Auswahl beziehungsweise Rundung außerhalb dieser Formel entscheiden.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Maßstabsfaktor ohne fachliche Zielberechnung |
| **Summe** | **1** | **Maßstabsangabe ausgeschlossen** |
