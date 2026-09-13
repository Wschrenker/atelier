# Fachlich normalisierte Formeln — S. 317

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s317.md`  
Originaltranskript: `s317.md`  
Buchseite: Hofenbitzer, Band 1, S. 317

## HOF-B1-S317-F01 — Hintere Stegbreite aus seitlicher Stegbreite

- **Fachlicher Zweck:** Die hintere Stegbreite aus der seitlichen Stegbreite mit einem Zuschlag von `0,5 cm` bestimmen.
- **Quelle:** `formeln_s317.md`, Zeile 14 (Buchfassung Zeile 15); Originaltranskript `s317.md`, Zeile 15; Buchseite 317.
- **Originalbezeichnung:** `hStegB = sStegB + 0,5 cm`
- **Normalisierte Bezeichnung:** `hintere_stegbreite_aus_seitlicher_stegbreite`

### Buchfassung

```text
13. die hStegB = sStegB + 0,5 cm abtragen sowie den Kragenbruch in den KrB einlaufend formen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `seitliche_stegbreite` | sStegB | variabel | cm |
| `hintere_steg_zuschlag` | `0,5 cm` | 0,5 | cm |

### Formel und Rechenschritte

```text
hintere_stegbreite = seitliche_stegbreite + 0,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hintere_stegbreite` | hStegB, hintere Stegbreite | cm |

- **Abhängigkeiten:** Seitliche Stegbreite sStegB.
- **Gültigkeitsbereich:** Schalkragen-Konstruktion mit hinterem Kragensteg auf S. 317.
- **Technische Randbedingung:** Der Zuschlag ist im Buch fest mit `0,5 cm` angegeben.
- **Offene Fragen oder Widersprüche:** Keine arithmetische Unklarheit.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `0,5 cm` als feste Buchkonstante führen; die anschließende Formgebung des Kragenbruchs ist keine Rechenregel.

## Ausgeschlossene Kandidaten

| Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Maßstabsfaktorangabe ohne fachliche Zielberechnung |
| 15 | 1 | Wiederholte hKrB-Bereichsangabe; bereits als `HOF-B1-S316-F01` belegt |
| 20 | 1 | Abbildungsverweis auf die Fertigstellung; keine Rechenoperation |
| 25 | 1 | Wiederholte hKrB-Bereichsangabe ohne neue Beziehung |
| **Summe** | **4** | **Maßstabs-, Wiederholungs- und Verweisangaben ausgeschlossen** |

## Extraktionsgrenze

Die Variantenkonstruktion, Belegbreiten und direkten Maßbereiche sind im Transkript belegt, liegen im verbindlichen Extrakt aber nicht als zusätzliche vollständige Rechenbeziehungen vor.
