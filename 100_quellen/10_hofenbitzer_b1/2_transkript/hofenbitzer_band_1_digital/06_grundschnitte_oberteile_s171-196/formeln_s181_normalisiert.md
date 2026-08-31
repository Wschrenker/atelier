# Fachlich normalisierte Formeln — S. 181

Quelle der Normalisierung: `formeln_s181.md`
Originaltranskript: `s181.md`
Buchseite: Hofenbitzer, Band 1, S. 181

## HOF-B1-S181-F01 — Horizontale Lage des Brustpunkts

- **Fachlicher Zweck:** Den Abstand von P21 zum Brustpunkt aus der halben BrB+ abzüglich 0,3 cm bestimmen.
- **Quelle:** `formeln_s181.md`, Zeile 14; Originaltranskript `s181.md`, Zeile 29; Buchseite 181.
- **Originalbezeichnung:** `½ BrB+ − 0,3 cm`
- **Normalisierte Bezeichnung:** `abstand_p21_brustpunkt`

### Buchfassung

```text
> (BrP) Von P21 nach rechts die halbe Brustbreite+ (½ BrB+) − 0,3 cm abtragen → Brustpunkt.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert auf S. 178 | Einheit |
|---|---|---:|---|
| `brustbreite_mit_zugabe` | BrB+ | 19,2 | cm |
| `brustpunkt_korrektur` | `0,3 cm` | 0,3 | cm |

### Formel und Rechenschritte

```text
halbe_brustbreite_mit_zugabe = brustbreite_mit_zugabe / 2
                              = 19,2 cm / 2
                              = 9,6 cm
abstand_p21_brustpunkt = halbe_brustbreite_mit_zugabe - brustpunkt_korrektur
                       = 9,6 cm - 0,3 cm
                       = 9,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Beispiel | Einheit |
|---|---|---:|---|
| `abstand_p21_brustpunkt` | von P21 nach rechts abzutragende Strecke | 9,3 | cm |

- **Abhängigkeiten:** BrB+ aus `HOF-B1-S178-F07`.
- **Gültigkeitsbereich:** Vorderes Halsloch und Brustpunkt des Oberteil-Grundgerüsts.
- **Technische Randbedingung:** Erst BrB+ halbieren, danach 0,3 cm abziehen; Richtung ist von P21 nach rechts.
- **Offene Fragen oder Widersprüche:** Keine; der Kontextwert ist eindeutig berechenbar.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die geometrische Richtung getrennt vom positiven Streckenbetrag speichern.

## HOF-B1-S181-F02 — Lage des vorderen Ärmelpunkts

- **Fachlicher Zweck:** Den vorderen Ärmelpunkt um ein Viertel von ArD+ oberhalb P13 festlegen.
- **Quelle:** `formeln_s181.md`, Zeile 19; Originaltranskript `s181.md`, Zeile 38; Buchseite 181.
- **Originalbezeichnung:** `¼ ArD+`
- **Normalisierte Bezeichnung:** `abstand_p13_vorderer_aermelpunkt`

### Buchfassung

```text
> (vAP) □6 An der vorderen Armlinie ¼ ArD+ von P13 nach oben abtragen → vorderer Ärmelpunkt (vAP).
```

### Eingaben

| Technische Variable | Buchbegriff | Wert auf S. 178 | Einheit |
|---|---|---:|---|
| `armdurchmesser_mit_zugabe` | ArD+ | 10,8 | cm |

### Formel und Rechenschritte

```text
abstand_p13_vorderer_aermelpunkt = armdurchmesser_mit_zugabe / 4
                                 = 10,8 cm / 4
                                 = 2,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Beispiel | Einheit |
|---|---|---:|---|
| `abstand_p13_vorderer_aermelpunkt` | Strecke von P13 nach oben zu vAP | 2,7 | cm |

- **Abhängigkeiten:** ArD+ aus `HOF-B1-S178-F06`.
- **Gültigkeitsbereich:** Vordere Schulter des Oberteil-Grundgerüsts.
- **Technische Randbedingung:** Die Strecke liegt auf der vorderen Armlinie und verläuft von P13 nach oben.
- **Offene Fragen oder Widersprüche:** Keine; der Wert stimmt mit dem Viertelwert auf S. 178 überein.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Streckenbetrag aus ArD+ ableiten und die Linienbindung geometrisch validieren.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s181.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | `P18 = Schnittpunkt` definiert einen geometrischen Punkt ohne Rechenbeziehung; Konstruktionslabel, keine Formel |
| **Summe** | **1** | **1 geometrische Punktdefinition ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s181.md` enthält weitere formelartige Beziehungen zu Halslochbreite, Schulterwinkeln, Streckenhalbierungen, VL und BrT. Sie fehlen im verbindlichen Extrakt und wurden nicht stillschweigend normalisiert. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
