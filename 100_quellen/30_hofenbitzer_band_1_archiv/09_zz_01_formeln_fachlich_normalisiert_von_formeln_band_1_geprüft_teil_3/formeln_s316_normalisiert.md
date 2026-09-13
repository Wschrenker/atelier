# Fachlich normalisierte Formeln — S. 316

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s316.md`  
Originaltranskript: `s316.md`  
Buchseite: Hofenbitzer, Band 1, S. 316

## HOF-B1-S316-F01 — Hintere Kragenbreite aus hinterer Stegbreite

- **Fachlicher Zweck:** Die sichtbare hintere Kragenbreite aus der hinteren Stegbreite und einem Mindestzuschlag bestimmen.
- **Quelle:** `formeln_s316.md`, Zeile 26 (Buchfassung Zeile 41); Originaltranskript `s316.md`, Zeile 41; Buchseite 316.
- **Originalbezeichnung:** `hKrB = mind. hStegB + 1 cm bis max. 7 cm`
- **Normalisierte Bezeichnung:** `hintere_kragenbreite_aus_hinterer_stegbreite`

### Buchfassung

```text
- hKrB = mind. hStegB + 1 cm bis max. 7 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hintere_stegbreite` | hStegB | variabel | cm |
| `hinterer_kragen_zuschlag` | mind. 1 cm | 1 oder größer | cm |

### Formel und Rechenschritte

```text
hintere_kragenbreite_min = hintere_stegbreite + 1 cm
hintere_kragenbreite_max = 7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hintere_kragenbreite` | sichtbare hintere Kragenbreite hKrB | cm |

- **Abhängigkeiten:** Hintere Stegbreite hStegB.
- **Gültigkeitsbereich:** Schalkragen mit separatem Unterkragen auf S. 316; die sichtbare hintere Kragenbreite darf laut Transkript nicht breiter als 7 cm sein.
- **Technische Randbedingung:** Der konkrete Wert muss mindestens `hStegB + 1 cm` betragen und darf `7 cm` nicht überschreiten.
- **Offene Fragen oder Widersprüche:** Die Quelle sagt nicht, wie innerhalb des zulässigen Bereichs ausgewählt wird.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Mindestwert und obere Grenze getrennt prüfen; keine automatische Auswahl im Bereich erfinden.

## HOF-B1-S316-F02 — Hintere Kragenbreite mit X-Anteil

- **Fachlicher Zweck:** Den zusätzlichen zehnten Anteil des Abstands X zur hinteren Kragenbreite addieren.
- **Quelle:** `formeln_s316.md`, Zeile 27 (Buchfassung Zeile 42); Originaltranskript `s316.md`, Zeile 42; Buchseite 316.
- **Originalbezeichnung:** `hKrB + ⅒ X`
- **Normalisierte Bezeichnung:** `hintere_kragenbreite_mit_x_zehntel`

### Buchfassung

```text
- hKrB + ⅒ X = 3,5 cm + 4,8 cm : 10 = 3,5 cm + 0,5 cm = 4,0 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hintere_kragenbreite` | hKrB | 3,5 | cm |
| `abstand_x` | X | 4,8 | cm |
| `x_anteil` | ⅒ | 1/10 | dimensionslos |

### Formel und Rechenschritte

```text
hintere_kragenbreite_mit_x_anteil = hintere_kragenbreite + (abstand_x / 10)
                                   = 3,5 cm + (4,8 cm / 10)
                                   = 3,5 cm + 0,48 cm
                                   = 3,98 cm
```

Der Druck rundet den Zwischenwert `0,48 cm` auf `0,5 cm` und gibt anschließend `4,0 cm` aus. Ohne belegte Rundungsregel bleiben die exakte und die gedruckte Rechenfolge getrennt.

### Ausgabe

| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `hintere_kragenbreite_mit_x_anteil` | Abtraglänge aus hKrB plus einem Zehntel von X | 4,0 gedruckt; 3,98 exakt | cm |

- **Abhängigkeiten:** Hintere Kragenbreite hKrB und Abstand X zwischen Kragenbruch/vM und Brustlinie.
- **Gültigkeitsbereich:** Schalkragen-Konstruktion an das Vorderteil auf S. 316.
- **Technische Randbedingung:** X ist vorzeichenbehaftet; liegt der Schnittpunkt unter der Brustlinie, ist X negativ. Die Quelle nennt keine Rundungsregel.
- **Offene Fragen oder Widersprüche:** Wörtlich ergibt `4,8 / 10 = 0,48 cm` und damit `3,98 cm`, nicht exakt `4,0 cm` ohne Rundung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Mit Dezimal- oder rationaler Rechnung arbeiten und exakten Wert, gedruckten Zwischenwert sowie gedrucktes Ergebnis getrennt speichern.

## Ausgeschlossene Kandidaten

| Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Maßstabsfaktorangabe ohne fachliche Zielberechnung |
| 14 | 1 | Seitliche Stegbreite als Eingabebereich und direkte Abtragsanweisung |
| 19–21 | 3 | Halslochverbreiterung, Stegbreitenbereich und Begriffsdefinition ohne eigenständige Zielberechnung |
| 28 | 1 | X-Messung, Mindestlänge und Brustlinie als Eingabe-/Konstruktionsangaben |
| **Summe** | **6** | **Maßstabs-, Eingabe-, Konstruktions- und Definitionsangaben ausgeschlossen** |

## Extraktionsgrenze

Das Originaltranskript enthält weitere Konstruktionsschritte, die im verbindlichen Extrakt nicht als eigenständige Rechenbeziehungen vorliegen. Sie wurden nicht als zusätzliche Buchfassungen ergänzt.
