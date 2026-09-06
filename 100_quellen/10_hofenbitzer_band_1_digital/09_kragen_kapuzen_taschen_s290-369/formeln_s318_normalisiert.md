# Fachlich normalisierte Formeln — S. 318

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s318.md`  
Originaltranskript: `s318.md`  
Buchseite: Hofenbitzer, Band 1, S. 318

## HOF-B1-S318-F01 — Verstürzweite aus halber Rollweite

- **Fachlicher Zweck:** Die am unteren Kragenbeginn anzutragende Verstürzweite aus ungefähr der halben Rollweite bestimmen.
- **Quelle:** `formeln_s318.md`, Zeile 14 (Buchfassung Zeile 14); Originaltranskript `s318.md`, Zeile 14; Buchseite 318.
- **Originalbezeichnung:** `ca. ½ Rollweite = Verstürzweite`
- **Normalisierte Bezeichnung:** `verstuerzweite_aus_halber_rollweite`

### Buchfassung

```text
20. Unten am Kragenbeginn nur ca. ½ Rollweite = Verstürzweite anzeichnen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `rollweite` | Rollweite | variabel | cm |
| `rollweiten_anteil` | ca. ½ | ungefähr 1/2 | dimensionslos |

### Formel und Rechenschritte

```text
verstaerzweite = rollweite / 2
```

Die Kennzeichnung `ca.` bleibt erhalten: Der Buchtext beschreibt eine ungefähre Konstruktionsgröße, keine mathematisch exakte Rundungsregel.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `verstaerzweite` | Verstürzweite am unteren Kragenbeginn | cm |

- **Abhängigkeiten:** Rollweite des Kragens.
- **Gültigkeitsbereich:** Schalkragen-Produktionsschnitt am unteren Kragenbeginn auf S. 318.
- **Technische Randbedingung:** Die Größe ist als ungefähr halbe Rollweite anzutragen; die konkrete Fertigungs- und Rundungsentscheidung bleibt modellabhängig.
- **Offene Fragen oder Widersprüche:** Keine Rechenabweichung; die Quelle legt keine Genauigkeit oder Rundungsregel für `ca.` fest.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Näherungskennzeichnung und eine explizite Toleranz beziehungsweise Fertigungsentscheidung außerhalb dieser Buchformel führen.

## Ausgeschlossene Kandidaten

| Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Maßstabsfaktorangabe ohne fachliche Zielberechnung |
| 19 | 1 | Abbildungsverweis und Zuschnittanweisung ohne Rechenoperation |
| 24 | 1 | Produktionsschnitt-Maßstabsfaktor und Schnittteilauflistung; keine berechnete Ausgabe |
| **Summe** | **3** | **Maßstabs-, Verweis- und Produktionsangaben ausgeschlossen** |
