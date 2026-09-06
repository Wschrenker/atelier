# Fachlich normalisierte Formeln — S. 299

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s299.md`  
Originaltranskript: `s299.md`  
Buchseite: Hofenbitzer, Band 1, S. 299

## HOF-B1-S299-F01 — Kragenbreite aus Stegbreite

- **Fachlicher Zweck:** Die Kragenbreite des zweiteiligen Kragens aus der Stegbreite bestimmen.
- **Quelle:** `formeln_s299.md`, Zeilen 14, 29 und 44; Originaltranskript `s299.md`, Zeilen 36, 53 und 69; Buchseite 299.
- **Originalbezeichnung:** `KrB = StegB + 0,7 bis 1,5 cm`
- **Normalisierte Bezeichnung:** `kragenbreite_aus_stegbreite_herrenstil`

### Buchfassung

```text
KrB = StegB + 0,7 bis 1,5 cm
```

### Formel und Rechenschritte

```text
kragenbreite = stegbreite + kragen_zuschlag
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kragenbreite` | Kragenbreite | cm |

- **Abhängigkeiten:** StegB und Zuschlag.
- **Gültigkeitsbereich:** Zweiteilige Umlegekragen im Herrenstil und breite Varianten.
- **Technische Randbedingung:** Zuschlagsbereich nicht automatisch auswählen.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zuschlag als Modellparameter führen.

## HOF-B1-S299-F02 — Übertritt aus Kragen- und Stegbreite

- **Fachlicher Zweck:** Den ausgewiesenen Übertritt aus Mehrweite, Kragenbreite und Stegbreite nachvollziehen.
- **Quelle:** `formeln_s299.md`, Zeile 39; Originaltranskript `s299.md`, Zeile 67; Buchseite 299.
- **Originalbezeichnung:** `üb + KrB − StegB = 0,4 cm + 8,3 cm − 7 cm`
- **Normalisierte Bezeichnung:** `uebertritt_aus_kragen_und_stegbreite`

### Buchfassung

```text
üb + KrB − StegB = 0,4 cm + 8,3 cm − 7 cm
```

### Formel und Rechenschritte

```text
uebertritt = mehrweite + kragenbreite - stegbreite
           = 0,4 cm + 8,3 cm - 7 cm
           = 1,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `uebertritt` | Übertritt beziehungsweise Differenzbetrag | 1,7 | cm |

- **Abhängigkeiten:** Mehrweite, KrB und StegB.
- **Gültigkeitsbereich:** Breite zweiteilige Steh-Umlegekragen, Variante 9.
- **Technische Randbedingung:** `üb` wird technisch als Übertritt gelesen; diese Benennung folgt dem Buchkontext.
- **Offene Fragen oder Widersprüche:** Keine arithmetische Unklarheit.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Mehrweite, Kragenbreite und Stegbreite getrennt führen.

## Ausgeschlossene Kandidaten

| Extraktzeilen | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9, 36, 48 | 3 | Modellbeschreibung, direkte Maße und Konstruktionsangaben ohne eigene Rechenbeziehung |
| **Summe** | **3** | **Kontext-, Eingabe- und Konstruktionsangaben ausgeschlossen** |
