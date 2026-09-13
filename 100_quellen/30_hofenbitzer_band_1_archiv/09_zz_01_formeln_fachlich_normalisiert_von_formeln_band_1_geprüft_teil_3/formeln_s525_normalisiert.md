# Fachlich normalisierte Formeln — S. 525

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s525.md`  
Originaltranskript: `s525.md`  
Buchseite: Hofenbitzer, Band 1, S. 525

Die Seite ergänzt den Body-Grundschnitt Variante 2 ohne hM-Naht. Die Formelblöcke betreffen die hM-Verlängerung, den Hüft-Fehlbetrag und den Taillenausfall.

## HOF-B1-S525-F01 — Verlängerung der hinteren Mitte

- **Fachlicher Zweck:** Die hM gegenüber der vM beziehungsweise Grundlinie um einen Hüftweitenanteil verlängern.
- **Quelle:** `formeln_s525.md`, Zeile 9; Originaltranskript `s525.md`, Zeile 56; Buchseite 525.
- **Originalbezeichnung:** `HüW : 10 + 1 bis 1,5 cm`.
- **Normalisierte Bezeichnung:** `body_hintere_mitte_verlaengerung`

### Buchfassung
```text
- HüW : 10 / HüW : 10 + 1 bis 1,5 cm
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftweite` | HüW | variabel | cm |
| `hintere_mitte_zugabe` | `1 bis 1,5 cm` | 1 bis 1,5 | cm |

### Formel und Rechenschritte
```text
vordere_mitte_verlaengerung = hueftweite / 10
hintere_mitte_verlaengerung = (hueftweite / 10) + hintere_mitte_zugabe
```

### Ausgabe
| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `vordere_mitte_verlaengerung` | Verlängerung der vM | cm |
| `hintere_mitte_verlaengerung` | Verlängerung der hM | cm |

- **Abhängigkeiten:** HüW; Schritt 9 und 10 der Body-Variante 2.
- **Gültigkeitsbereich:** Body-Grundschnitt Variante 2, Maschenware.
- **Offene Fragen oder Widersprüche:** Die Extraktzeile stellt zwei Varianten nebeneinander; die Zuordnung zu vM und hM ergibt sich erst aus den Schritten des Originaltranskripts.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** vM und hM als getrennte Ausgaben führen; die hM-Zugabe als Bereichsparameter offen wählbar lassen.

## HOF-B1-S525-F02 — Hüft-Fehlbetrag

- **Fachlicher Zweck:** Den Fehlbetrag zwischen gemessener halber Hüftweite und der Soll-Hüftweite bestimmen.
- **Quelle:** `formeln_s525.md`, Zeilen 19–21; Originaltranskript `s525.md`, Zeilen 47–49; Buchseite 525.
- **Originalbezeichnung:** `vHüB + hHüB − ½ HüW`.
- **Normalisierte Bezeichnung:** `body_hueftfehlbetrag`

### Buchfassung
```text
= vHüB + hHüB − ½ HüW (S.518)
= 44,5 cm       − 45,1 cm
= −0,6 cm       → 0,6 cm
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `gemessene_halbe_hueftweite` | vHüB + hHüB | 44,5 | cm |
| `soll_halbe_hueftweite` | ½ HüW | 45,1 | cm |

### Formel und Rechenschritte
```text
hueftfehlbetrag_signiert = gemessene_halbe_hueftweite - soll_halbe_hueftweite
                         = 44,5 cm - 45,1 cm
                         = -0,6 cm
hueftfehlbetrag_betrag = abs(hueftfehlbetrag_signiert) = 0,6 cm
```

### Ausgabe
| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `hueftfehlbetrag_signiert` | gerichtete Abweichung der Messung | −0,6 | cm |
| `hueftfehlbetrag_betrag` | auszustellender Betrag laut Zeichnung | 0,6 | cm |

- **Abhängigkeiten:** vHüB, hHüB und ½ HüW aus dem engen Oberteilgrundschnitt, S. 518.
- **Gültigkeitsbereich:** Body-Grundschnitt Variante 2, Schritt 5–6.
- **Offene Fragen oder Widersprüche:** Das Buch wechselt vom negativen Differenzwert zum positiven Betrag. Die Richtung der geometrischen Ausstellung ist nicht durch ein Vorzeichen codiert.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Signierten Fehler und Betrag getrennt speichern; die Richtung als eigene geometrische Entscheidung behandeln.

## HOF-B1-S525-F03 — Taillenausfall

- **Fachlicher Zweck:** Den Taillenausfall aus gemessener Taillenbreite und halber Soll-Taillenweite bestimmen.
- **Quelle:** `formeln_s525.md`, Zeilen 31–33; Originaltranskript `s525.md`, Zeilen 65–67; Buchseite 525.
- **Originalbezeichnung:** `vTaB + hTaB − ½ TaW`.
- **Normalisierte Bezeichnung:** `body_taillenausfall`

### Buchfassung
```text
= vTaB + hTaB − ½ TaW
= 45,8 cm      − 36 cm
= 9,8 cm
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `gemessene_halbe_taillenweite` | vTaB + hTaB | 45,8 | cm |
| `soll_halbe_taillenweite` | ½ TaW | 36 | cm |

### Formel und Rechenschritte
```text
taillenausfall = gemessene_halbe_taillenweite - soll_halbe_taillenweite
                = 45,8 cm - 36 cm
                = 9,8 cm
```

### Ausgabe
| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `taillenausfall` | auf Seite und Abnäher zu verteilender Ausfall | 9,8 | cm |

- **Abhängigkeiten:** vTaB, hTaB und ½ TaW.
- **Gültigkeitsbereich:** Body-Grundschnitt Variante 2, Schritt 14–16.
- **Offene Fragen oder Widersprüche:** Die Aufteilung auf Seiten und rückwärtigen Abnäher wird qualitativ beschrieben; eine exakte Verteilungsformel ist nicht extrahiert.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Gesamtbetrag berechnen und die Verteilung als separates, fachlich zu bestimmendes Konstruktionsparameter behandeln.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 14 | 1 | `3. Die RüB-Linie verschieben und das Armloch neu formen.` — Konstruktionsanweisung ohne Rechenoperation |
| **Summe** | **1** | **Konstruktionsanweisung ausgeschlossen** |

## Prüfhinweis

Die Berechnungen `44,5 − 45,1 = −0,6` und `45,8 − 36 = 9,8` sind rechnerisch konsistent. Die auf S. 518 verwiesene Grundschnittkonstruktion liefert die Maßgrundlage, wird hier aber nicht erneut normalisiert.
