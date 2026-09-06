# Fachlich normalisierte Formeln — S. 528

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s528.md`  
Originaltranskript: `s528.md`  
Buchseite: Hofenbitzer, Band 1, S. 528

Die Seite ergänzt den engen Oberteil-Grundschnitt zum unisex Bodysuit. Die Formelblöcke bestimmen Hüftlinien und kontrollieren Taillen- und Hüftweite.

## HOF-B1-S528-F01 — Neue Hüftlinie

- **Fachlicher Zweck:** Die neue Hüftlinie aus der Sitzhöhe und dem Hüftumfang bestimmen.
- **Quelle:** `formeln_s528.md`, Zeile 14; Originaltranskript `s528.md`, Zeile 46; Buchseite 528.
- **Originalbezeichnung:** `HüU : 20 + 3 cm`.
- **Normalisierte Bezeichnung:** `bodysuit_neue_hueftlinie_abstand`

### Buchfassung
```text
2. Von dort die neue Hüftlinie mit HüU : 20 + 3 cm bestimmen.
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 102 | cm |
| `hueftlinien_zugabe` | `3 cm` | 3 | cm |

### Formel und Rechenschritte
```text
neue_hueftlinienhoehe = (hueftumfang / 20) + 3 cm
                       = (102 cm / 20) + 3 cm
                       = 5,1 cm + 3 cm
                       = 8,1 cm
```

### Ausgabe
| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `neue_hueftlinienhoehe` | Abstand zur neuen Hüftlinie | 8,1 | cm |

- **Abhängigkeiten:** HüU aus der Maßtabelle auf S. 528.
- **Gültigkeitsbereich:** Bodysuit-Grundschnitt, Schritt 2.
- **Offene Fragen oder Widersprüche:** Der Ausgangspunkt „von dort“ ist die zuvor abgetragene SiH; der Extrakt benennt ihn nicht als eigene Variable.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Abstand relativ zum vorherigen Konstruktionspunkt speichern, nicht als absolute Körperhöhe.

## HOF-B1-S528-F02 — Vorderer Abstand an der Schritthöhe

- **Fachlicher Zweck:** An der Schritthöhe den vorderen Abstand von der vM bestimmen.
- **Quelle:** `formeln_s528.md`, Zeilen 19–20; Originaltranskript `s528.md`, Zeile 48; Buchseite 528.
- **Originalbezeichnung:** `HüU : 20 + 1,5 cm`.
- **Normalisierte Bezeichnung:** `bodysuit_vorderer_schrittabstand`

### Buchfassung
```text
4. An der Schritthöhe ab der vM HüU : 20 + 1,5 cm und ab der Grundlinie HüU : 10 abtragen.
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 102 | cm |
| `vorderer_schritt_zuschlag` | `1,5 cm` | 1,5 | cm |

### Formel und Rechenschritte
```text
vorderer_schrittabstand = (hueftumfang / 20) + 1,5 cm
                         = 5,1 cm + 1,5 cm
                         = 6,6 cm
```

### Ausgabe
| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `vorderer_schrittabstand` | Abtragung ab der vM an der Schritthöhe | 6,6 | cm |

- **Abhängigkeiten:** HüU.
- **Gültigkeitsbereich:** Bodysuit-Grundschnitt, Schritt 4.
- **Offene Fragen oder Widersprüche:** Die Einheit `cm` ist durch den Zahlenkontext und die parallele Formel belegt; der Extrakt schreibt sie nicht nach jedem Summanden aus.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als seitlichen Abstand an der Schritthöhe modellieren.

## HOF-B1-S528-F03 — Abstand von der Grundlinie

- **Fachlicher Zweck:** Den zweiten Schrittabstand von der Grundlinie aus dem Hüftumfang bestimmen.
- **Quelle:** `formeln_s528.md`, Zeilen 19–20; Originaltranskript `s528.md`, Zeile 48; Buchseite 528.
- **Originalbezeichnung:** `HüU : 10`.
- **Normalisierte Bezeichnung:** `bodysuit_grundlinien_schrittabstand`

### Buchfassung
```text
4. An der Schritthöhe ab der vM HüU : 20 + 1,5 cm und ab der Grundlinie HüU : 10 abtragen.
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 102 | cm |
| `zehntel_faktor` | `10` | 10 | dimensionslos |

### Formel und Rechenschritte
```text
grundlinien_schrittabstand = hueftumfang / 10
                             = 102 cm / 10
                             = 10,2 cm
```

### Ausgabe
| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `grundlinien_schrittabstand` | Abtragung von der Grundlinie | 10,2 | cm |

- **Abhängigkeiten:** HüU.
- **Gültigkeitsbereich:** Bodysuit-Grundschnitt, Schritt 4.
- **Offene Fragen oder Widersprüche:** Die räumliche Richtung der Abtragung ist durch den Buchsatz gegeben, eine Punktbezeichnung fehlt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Längenwert getrennt von der späteren Punkt-/Liniengeometrie führen.

## HOF-B1-S528-F04 — Kontrolle der Taillenweite

- **Fachlicher Zweck:** Prüfen, ob die gemessene Taillenweite mindestens innerhalb des angegebenen Bereichs liegt.
- **Quelle:** `formeln_s528.md`, Zeile 24; Originaltranskript `s528.md`, Zeile 64; Buchseite 528.
- **Originalbezeichnung:** `messen + messen = ½ TaU + 0 bis 2 cm`.
- **Normalisierte Bezeichnung:** `bodysuit_taillenweiten_kontrolle`

### Buchfassung
```text
- Kontrolle der TaW → messen + messen = ½ TaU + 0 bis 2 cm
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `gemessene_taillenweite` | messen + messen | variabel | cm |
| `halber_taillenumfang` | ½ TaU | 44 | cm |
| `taillen_zugabe` | `0 bis 2 cm` | 0 bis 2 | cm |

### Formel und Rechenschritte
```text
erwartete_taillenweite_bereich = halber_taillenumfang + (0 bis 2 cm)
                                 = 44 cm bis 46 cm
pruefung: gemessene_taillenweite liegt im angegebenen Bereich
```

### Ausgabe
| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `taillenweiten_kontrolle` | Bereichsprüfung der gemessenen TaW | cm |

- **Abhängigkeiten:** TaU und die zwei gemessenen Taillenstrecken.
- **Gültigkeitsbereich:** Bodysuit-Grundschnitt, Kontrolle der TaW.
- **Offene Fragen oder Widersprüche:** Das Buch nennt keine Toleranz außerhalb des Bereichs und keine Korrekturregel bei Abweichung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Bereichskontrolle implementieren, nicht als automatische Taillenweiten-Zuweisung.

## HOF-B1-S528-F05 — Kontrolle der Hüftweite

- **Fachlicher Zweck:** Prüfen, ob die gemessene Hüftweite innerhalb des angegebenen Zuschlagsbereichs liegt.
- **Quelle:** `formeln_s528.md`, Zeile 25; Originaltranskript `s528.md`, Zeile 65; Buchseite 528.
- **Originalbezeichnung:** `messen + messen = ½ HüU + 0 bis 0,5 cm`.
- **Normalisierte Bezeichnung:** `bodysuit_hueftweiten_kontrolle`

### Buchfassung
```text
- Kontrolle der HüW → messen + messen = ½ HüU + 0 bis 0,5 cm
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `gemessene_hueftweite` | messen + messen | variabel | cm |
| `halber_hueftumfang` | ½ HüU | 51 | cm |
| `hueft_zugabe` | `0 bis 0,5 cm` | 0 bis 0,5 | cm |

### Formel und Rechenschritte
```text
erwartete_hueftweite_bereich = halber_hueftumfang + (0 bis 0,5 cm)
                               = 51 cm bis 51,5 cm
pruefung: gemessene_hueftweite liegt im angegebenen Bereich
```

### Ausgabe
| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftweiten_kontrolle` | Bereichsprüfung der gemessenen HüW | cm |

- **Abhängigkeiten:** HüU und die zwei gemessenen Hüftstrecken.
- **Gültigkeitsbereich:** Bodysuit-Grundschnitt, Kontrolle der HüW.
- **Offene Fragen oder Widersprüche:** Eine Korrekturregel für einen Fehlbetrag ist nur qualitativ als seitliches Anzeichnen und Formen beschrieben.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Bereich als Prüfgrenze führen; die Korrekturgeometrie nicht aus der Kontrollformel ableiten.

## Ausgeschlossene Kandidaten

Keine. Die Wiederholung der drei Beziehungen in der Beschriftung `HüU : 20 + 1,5 cm / HüU : 20 + 3 cm / HüU : 10` ist als Buchnachweis zu F01–F03 geführt und erzeugt keine zweiten Formel-IDs.
