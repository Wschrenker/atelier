# Fachlich normalisierte Formeln — S. 328

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s328.md`  
Originaltranskript: `s328.md`  
Buchseite: Hofenbitzer, Band 1, S. 328

## HOF-B1-S328-F01 — Drittelteilung der hinteren Halslochlänge

- **Fachlicher Zweck:** Einschnittabstände am zweiteiligen Reverskragen aus einem Drittel der hinteren Halslochlänge ableiten.
- **Quelle:** `formeln_s328.md`, Extraktzeile 19; Originaltranskript `s328.md`, Zeile 37; Buchseite 328.
- **Originalbezeichnung:** `je ca. ⅓ hHlL = 2,9 cm`
- **Normalisierte Bezeichnung:** `einschnittabstand_als_drittel_der_hinteren_halslochlaenge`

### Buchfassung
```text
- je ca. ⅓ hHlL = 2,9 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hintere_halslochlaenge` | hHlL | nicht angegeben | cm |
| `drittel_faktor` | ⅓ | 1/3 | dimensionslos |

### Formel und Rechenschritte
```text
einschnittabstand ≈ hintere_halslochlaenge / 3
```

Der gedruckte Einzelabstand beträgt `2,9 cm`. Ein Ausgangswert für hHlL ist im Extrakt nicht angegeben und wird nicht zurückgerechnet.

### Ausgabe
`einschnittabstand` — je ungefähr ein Drittel der hinteren Halslochlänge, gedruckt `2,9 cm`.

- **Abhängigkeiten:** hHlL.
- **Gültigkeitsbereich:** Einschnittteilung des zweiteiligen Reverskragens, S. 328.
- **Offene Fragen oder Widersprüche:** Der Eingabewert hHlL fehlt; die technische Ausführung bleibt deshalb nicht ausführbar.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Erst implementieren, wenn hHlL aus der Extraktionsschicht als Eingabe belegt ist; den Wert `2,9 cm` nicht zur Rekonstruktion von hHlL verwenden.

## Ausgeschlossene Kandidaten

| Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Maßstabsfaktor ohne fachliche Zielberechnung |
| 14 | 1 | Beschreibung einer Grundform und Maßstabsangabe ohne Rechenbeziehung |
| 24 | 1 | Maßliste und Farb-/Zeichnungszuordnung ohne berechnete Ausgabe |
| 25 | 1 | Unklare bzw. widersprüchliche Beschriftung `X / X = 2,6 cm`; keine sicher bestimmbare Relation |
| **Summe** | **4** | **Maßstabs-, Kontext-, Maßlisten- und unklare Beschriftungen ausgeschlossen** |
