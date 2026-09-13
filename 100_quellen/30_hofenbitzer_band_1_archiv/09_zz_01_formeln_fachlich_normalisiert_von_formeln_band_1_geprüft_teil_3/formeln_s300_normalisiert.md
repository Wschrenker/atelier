# Fachlich normalisierte Formeln — S. 300

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s300.md`  
Originaltranskript: `s300.md`  
Buchseite: Hofenbitzer, Band 1, S. 300

## HOF-B1-S300-F01 — Vordere Stegbreite aus hinterer Stegbreite

- **Fachlicher Zweck:** Die vordere Stegbreite gegenüber der hinteren Stegbreite reduzieren.
- **Quelle:** `formeln_s300.md`, Zeilen 14 und 47; Originaltranskript `s300.md`, Zeilen 24 und 69; Buchseite 300.
- **Originalbezeichnung:** `vStegB = hStegB − 0 bis − 1,5 cm`
- **Normalisierte Bezeichnung:** `vordere_stegbreite_aus_hinterer_stegbreite`

### Buchfassung

```text
vStegB = hStegB − 0 bis − 1,5 cm
```

### Formel und Rechenschritte

```text
vordere_stegbreite = hintere_stegbreite - stegbreiten_abzug
```

Der Abzug liegt laut Buch zwischen `0` und `1,5 cm`.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `vordere_stegbreite` | vordere Stegbreite | cm |

- **Abhängigkeiten:** Hintere Stegbreite hStegB und gewählter Abzug.
- **Gültigkeitsbereich:** Napoleon- und Trenchcoat-Kragen.
- **Technische Randbedingung:** Die Schreibweise wird als Bereich eines nichtnegativen Abzugs technisch eindeutig dargestellt.
- **Offene Fragen oder Widersprüche:** Keine Rechenwerte für eine konkrete Auswahl.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `stegbreiten_abzug` zwischen 0 und 1,5 cm validieren.

## HOF-B1-S300-F02 — Kragenbreite aus hinterer Stegbreite

- **Fachlicher Zweck:** Die Kragenbreite des Napoleon- beziehungsweise Trenchcoat-Kragens bestimmen.
- **Quelle:** `formeln_s300.md`, Zeilen 19, 27, 35, 40 und 52; Originaltranskript `s300.md`, Zeilen 26, 45, 54, 64 und 71; Buchseite 300.
- **Originalbezeichnung:** `KrB = hStegB + 1 bis 4 cm` mit den Beispielen `+ 1,5 cm` und `+ 3,5 cm`.
- **Normalisierte Bezeichnung:** `kragenbreite_aus_hinterer_stegbreite`

### Buchfassung

```text
KrB = hStegB + 1 bis 4 cm
KrB = hStegB + 1 bis 4 cm (+ 1,5 cm)
KrB = hStegB + 1 bis 4 cm (+ 3,5 cm)
```

### Formel und Rechenschritte

```text
kragenbreite = hintere_stegbreite + kragen_zuschlag
```

`kragen_zuschlag` liegt im allgemeinen Bereich `1 bis 4 cm`; die Beispiele `1,5 cm` und `3,5 cm` bleiben Variantenwerte.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kragenbreite` | Kragenbreite | cm |

- **Abhängigkeiten:** hStegB und gewählter Zuschlag.
- **Gültigkeitsbereich:** Napoleon- und Trenchcoat-Kragen.
- **Technische Randbedingung:** Die Buchvariante muss vor der Berechnung gewählt werden.
- **Offene Fragen oder Widersprüche:** Die Hochstellung des Napoleon-Kragens ist im Transkript uneinheitlich angegeben; dieser Widerspruch betrifft die Konstruktion, nicht die Kragenbreitenformel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** allgemeinen Bereich und Beispielzuschlag getrennt speichern.

## HOF-B1-S300-F03 — Übertragung der gemessenen Stegnaht

- **Fachlicher Zweck:** Die gemessene Stegnaht mit dem zusätzlichen Buchbetrag übertragen.
- **Quelle:** `formeln_s300.md`, Zeilen 24–27 und 32–35; Originaltranskript `s300.md`, Zeilen 42–45 und 51–54; Buchseite 300.
- **Originalbezeichnung:** `übertragen 5,1 cm + 1,5 cm = 6,6 cm` beziehungsweise `4,6 cm + 3,5 cm = 8,1 cm`.
- **Normalisierte Bezeichnung:** `uebertragene_stegnahtlaenge`

### Buchfassung

```text
übertragen 5,1 cm + 1,5 cm = 6,6 cm
übertragen 4,6 cm + 3,5 cm = 8,1 cm
```

### Formel und Rechenschritte

```text
uebertragene_stegnahtlaenge = gemessene_stegnahtlaenge + uebertragungszuschlag

Napoleon: 5,1 cm + 1,5 cm = 6,6 cm
Trenchcoat: 4,6 cm + 3,5 cm = 8,1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `uebertragene_stegnahtlaenge` | auf die Hilfslinie übertragene Länge | 6,6 oder 8,1 | cm |

- **Abhängigkeiten:** Gemessene Stegnahtlänge und variantenspezifischer Zuschlag.
- **Gültigkeitsbereich:** Zwei Konstruktionsvarianten von Napoleon- und Trenchcoat-Kragen.
- **Technische Randbedingung:** Messwert und Zuschlag bleiben getrennte Eingaben.
- **Offene Fragen oder Widersprüche:** Keine arithmetische Unklarheit.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Variante bestimmt den Zuschlag; nicht aus Kragenbreite ableiten.

## Ausgeschlossene Kandidaten

| Extraktzeilen | Anzahl | Ausschlussgrund |
|---|---:|---|
| 22 | 1 | Direkte Halsloch-Längenangabe ohne eigene Zielberechnung |
| **Summe** | **1** | **Eingabelabel ausgeschlossen** |
