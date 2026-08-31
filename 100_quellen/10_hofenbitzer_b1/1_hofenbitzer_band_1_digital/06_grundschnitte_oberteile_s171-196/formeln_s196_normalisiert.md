# Fachlich normalisierte Formeln — S. 196

Quelle der Normalisierung: `formeln_s196.md`
Originaltranskript: `s196.md`
Buchseite: Hofenbitzer, Band 1, S. 196

## HOF-B1-S196-F01 — Brustbreiten-Zugabedifferenz von PK 3 zu PK 0

- **Fachlicher Zweck:** Die überschüssige Brustbreiten-Zugabe beim Reduzieren eines PK-3-Grundschnitts auf PK 0 bestimmen.
- **Quelle:** `formeln_s196.md`, Zeilen 27–29; Originaltranskript `s196.md`, Zeilen 69–71; Buchseite 196.
- **Originalbezeichnung:** `PK 3 − PK 0 = Differenz`
- **Normalisierte Bezeichnung:** `brustbreiten_zugabedifferenz_pk3_zu_pk0`

### Buchfassung

```text
- PK 3: 1,0 cm
- PK 0: 0,2 cm
- Differenz = 0,8 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustbreite_zugabe_pk3` | Zugabe zur BrB, PK 3 | 1,0 | cm |
| `brustbreite_zugabe_pk0` | Zugabe zur BrB, PK 0 | 0,2 | cm |

### Formel und Rechenschritte

```text
brustbreiten_zugabedifferenz = brustbreite_zugabe_pk3 - brustbreite_zugabe_pk0
                              = 1,0 cm - 0,2 cm
                              = 0,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `brustbreiten_zugabedifferenz` | an der BrB zu entfernende Zugabe | 0,8 | cm |

- **Abhängigkeiten:** Gewählte BrB-Zugaben der Passformklassen 3 und 0.
- **Gültigkeitsbereich:** Reduzierung eines optimierten, eng anliegenden PK-3-Oberteil-Grundschnitts auf einen PK-0-Korsagen-Grundschnitt.
- **Technische Randbedingung:** BrB und ihre Zugabe beziehen sich laut Seitenkontext auf den halben Schnitt.
- **Offene Fragen oder Widersprüche:** Die Zugabentabelle nennt für PK 0 einen BrB-Bereich von `0–0,4 cm`; das Beispiel wählt `0,2 cm`, ohne die Auswahlregel zu belegen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den gewählten PK-0-Wert als Eingabe führen und nicht aus dem Bereich ableiten.

## HOF-B1-S196-F02 — Armdurchmesser-Zugabedifferenz und hälftige Reduzierung

- **Fachlicher Zweck:** Die überschüssige ArD-Zugabe bestimmen und gleich auf die beiden Seitennähte des halben Schnitts verteilen.
- **Quelle:** `formeln_s196.md`, Zeilen 39–42; Originaltranskript `s196.md`, Zeilen 75–78; Buchseite 196.
- **Originalbezeichnung:** `PK 3 − PK 0 = Differenz; jeweils ½`
- **Normalisierte Bezeichnung:** `armdurchmesser_zugabedifferenz_pk3_zu_pk0`

### Buchfassung

```text
- PK 3: 1,5 cm
- PK 0: 0 cm
- Differenz = 1,5 cm
- jeweils ½ = 0,75 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser_zugabe_pk3` | Zugabe zum ArD, PK 3 | 1,5 | cm |
| `armdurchmesser_zugabe_pk0` | Zugabe zum ArD, PK 0 | 0 | cm |
| `anzahl_seitennaehte_halber_schnitt` | Seitennähte von VT und RT | 2 | dimensionslos |

### Formel und Rechenschritte

```text
armdurchmesser_zugabedifferenz = armdurchmesser_zugabe_pk3 - armdurchmesser_zugabe_pk0
                                = 1,5 cm - 0 cm
                                = 1,5 cm
reduzierung_je_seitennaht = armdurchmesser_zugabedifferenz / 2
                           = 1,5 cm / 2
                           = 0,75 cm
Kontrolle: 0,75 cm + 0,75 cm = 1,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser_zugabedifferenz` | insgesamt am ArD zu entfernende Zugabe | 1,5 | cm |
| `reduzierung_je_seitennaht` | Reduzierung an der Seitennaht von VT beziehungsweise RT | 0,75 | cm |

- **Abhängigkeiten:** ArD-Zugaben der Passformklassen 3 und 0.
- **Gültigkeitsbereich:** Reduzierung eines optimierten, eng anliegenden PK-3-Oberteil-Grundschnitts auf einen PK-0-Korsagen-Grundschnitt.
- **Technische Randbedingung:** Der Seitenkontext verteilt die ArD-Differenz an den Seitennähten jeweils zur Hälfte.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Differenz und hälftigen Nahtbetrag getrennt speichern; ihre Summe als Invariante prüfen.

## HOF-B1-S196-F03 — Rückenbreiten-Zugabedifferenz von PK 3 zu PK 0

- **Fachlicher Zweck:** Die überschüssige Rückenbreiten-Zugabe beim Reduzieren auf PK 0 bestimmen.
- **Quelle:** `formeln_s196.md`, Zeilen 52–54; Originaltranskript `s196.md`, Zeilen 82–84; Buchseite 196.
- **Originalbezeichnung:** `PK 3 − PK 0 = Differenz`
- **Normalisierte Bezeichnung:** `rueckenbreiten_zugabedifferenz_pk3_zu_pk0`

### Buchfassung

```text
- PK 3: 0,5 cm
- PK 0: 0 cm
- Differenz = 0,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `rueckenbreite_zugabe_pk3` | Zugabe zur RüB, PK 3 | 0,5 | cm |
| `rueckenbreite_zugabe_pk0` | Zugabe zur RüB, PK 0 | 0 | cm |

### Formel und Rechenschritte

```text
rueckenbreiten_zugabedifferenz = rueckenbreite_zugabe_pk3 - rueckenbreite_zugabe_pk0
                                = 0,5 cm - 0 cm
                                = 0,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `rueckenbreiten_zugabedifferenz` | an der RüB zu entfernende Zugabe | 0,5 | cm |

- **Abhängigkeiten:** RüB-Zugaben der Passformklassen 3 und 0.
- **Gültigkeitsbereich:** Reduzierung eines optimierten, eng anliegenden PK-3-Oberteil-Grundschnitts auf einen PK-0-Korsagen-Grundschnitt.
- **Technische Randbedingung:** RüB und ihre Zugabe beziehen sich laut Seitenkontext auf den halben Schnitt.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Reduzierung als eigene Breitenänderung führen.

## HOF-B1-S196-F04 — Armlochtiefen-Zugabedifferenz von PK 3 zu PK 0

- **Fachlicher Zweck:** Den Betrag bestimmen, um den die Armlochtiefe beim Reduzieren auf PK 0 angehoben wird.
- **Quelle:** `formeln_s196.md`, Zeilen 59–61; Originaltranskript `s196.md`, Zeilen 88–90; Buchseite 196.
- **Originalbezeichnung:** `PK 3 − PK 0 = Differenz`
- **Normalisierte Bezeichnung:** `armlochtiefen_zugabedifferenz_pk3_zu_pk0`

### Buchfassung

```text
- PK 3: 1,3 cm
- PK 0: 0 cm
- Differenz = 1,3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefe_zugabe_pk3` | Zugabe zur AlT, PK 3 | 1,3 | cm |
| `armlochtiefe_zugabe_pk0` | Zugabe zur AlT, PK 0 | 0 | cm |

### Formel und Rechenschritte

```text
armlochtiefen_zugabedifferenz = armlochtiefe_zugabe_pk3 - armlochtiefe_zugabe_pk0
                               = 1,3 cm - 0 cm
                               = 1,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefen_zugabedifferenz` | Betrag zum Anheben der AlT beziehungsweise Brustlinie | 1,3 | cm |

- **Abhängigkeiten:** AlT-Zugaben der Passformklassen 3 und 0.
- **Gültigkeitsbereich:** Reduzierung eines optimierten, eng anliegenden PK-3-Oberteil-Grundschnitts auf einen PK-0-Korsagen-Grundschnitt.
- **Technische Randbedingung:** Der Differenzbetrag ist eine vertikale Änderung und wird nicht halbiert.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorzeichen und Koordinatenrichtung beim geometrischen Anheben ausdrücklich festlegen.

## HOF-B1-S196-F05 — Taillenweiten-Zugabedifferenz von PK 3 zu PK 0

- **Fachlicher Zweck:** Die überschüssige Zugabe zur ganzen Taillenweite beim Reduzieren auf PK 0 bestimmen.
- **Quelle:** `formeln_s196.md`, Zeilen 71–72; Originaltranskript `s196.md`, Zeilen 94–95; Buchseite 196.
- **Originalbezeichnung:** `PK 3 − PK 0`
- **Normalisierte Bezeichnung:** `taillenweiten_zugabedifferenz_pk3_zu_pk0`

### Buchfassung

```text
- PK 3: 4 cm
- PK 0: 0 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenweiten_zugabe_pk3` | Zugabe zur TaW, PK 3 | 4 | cm |
| `taillenweiten_zugabe_pk0` | Zugabe zur TaW, PK 0 | 0 | cm |

### Formel und Rechenschritte

```text
taillenweiten_zugabedifferenz = taillenweiten_zugabe_pk3 - taillenweiten_zugabe_pk0
                               = 4 cm - 0 cm
                               = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `taillenweiten_zugabedifferenz` | überschüssige Zugabe der ganzen Taillenweite | 4 | cm |

- **Abhängigkeiten:** TaW-Zugaben der Passformklassen 3 und 0 sowie der Abschnittskontext „Differenzen ermitteln“.
- **Gültigkeitsbereich:** Reduzierung eines optimierten, eng anliegenden PK-3-Oberteil-Grundschnitts auf einen PK-0-Korsagen-Grundschnitt.
- **Technische Randbedingung:** Die `4 cm` gelten laut Seitenkontext für den ganzen Schnitt; sie sind nicht unmittelbar der an einer einzelnen Seitennaht zu entfernende Betrag.
- **Offene Fragen oder Widersprüche:** Der Extrakt druckt für TaW keine eigene Differenzzeile und belegt keine Verteilung der `4 cm` auf halben Schnitt und Seitennähte.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Nur die Umfangszugaben-Differenz implementieren; eine geometrische Verteilung erst nach separatem Quellenbeleg ergänzen.

## HOF-B1-S196-F06 — Hüftweiten-Zugabedifferenz von PK 3 zu PK 0

- **Fachlicher Zweck:** Die überschüssige Zugabe zur ganzen Hüftweite beim Reduzieren auf PK 0 bestimmen.
- **Quelle:** `formeln_s196.md`, Zeilen 77–78; Originaltranskript `s196.md`, Zeilen 99–100; Buchseite 196.
- **Originalbezeichnung:** `PK 3 − PK 0`
- **Normalisierte Bezeichnung:** `hueftweiten_zugabedifferenz_pk3_zu_pk0`

### Buchfassung

```text
- PK 3: 4 cm
- PK 0: 0 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftweiten_zugabe_pk3` | Zugabe zur HüW, PK 3 | 4 | cm |
| `hueftweiten_zugabe_pk0` | Zugabe zur HüW, PK 0 | 0 | cm |

### Formel und Rechenschritte

```text
hueftweiten_zugabedifferenz = hueftweiten_zugabe_pk3 - hueftweiten_zugabe_pk0
                             = 4 cm - 0 cm
                             = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hueftweiten_zugabedifferenz` | überschüssige Zugabe der ganzen Hüftweite | 4 | cm |

- **Abhängigkeiten:** HüW-Zugaben der Passformklassen 3 und 0 sowie der Abschnittskontext „Differenzen ermitteln“.
- **Gültigkeitsbereich:** Reduzierung eines optimierten, eng anliegenden PK-3-Oberteil-Grundschnitts auf einen PK-0-Korsagen-Grundschnitt.
- **Technische Randbedingung:** Die `4 cm` gelten laut Seitenkontext für den ganzen Schnitt; Mehrweite darf laut Originaltranskript im Korsagen-Grundschnitt verbleiben oder alternativ entfernt werden.
- **Offene Fragen oder Widersprüche:** Der Extrakt druckt für HüW keine eigene Differenzzeile und belegt weder die Entscheidung zum Entfernen noch die geometrische Verteilung der `4 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zugabendifferenz und optionale geometrische Hüftkorrektur als getrennte Schritte modellieren.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s196.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 9–12 | 4 | PK-3-Konstruktionstabellenzeilen, die dieselben Ausgangsmaße und Ergebnisse wie S. 194 wiederholen; Kontext und Eingaben der Reduzierung, keine neuen Formeln dieser Tranche |
| Zeile 17 | 1 | Geltungsbereich der Zugaben für ganzen beziehungsweise halben Schnitt; fachlicher Kontext, keine eigenständige Rechenformel |
| Zeilen 22, 34, 47 und 66 | 4 | Abschnittsüberschriften für BrB-, ArD-, RüB- und TaW-Zugaben; Bezeichnungen, keine Rechenformeln |
| Zeile 83 | 1 | Zeichnungswiederholung des bereits in `HOF-B1-S196-F02` abgebildeten Halbwerts `0,75 cm` |
| Zeilen 88 und 93 | 2 | gemessene halbe Taillen- und Hüftweiten als Kontrolllabels; ohne extrahierte Zielwert- oder Differenzrechnung keine eigenständigen Formeln |
| **Summe** | **12** | **4 wiederholte Tabellenzeilen, 1 Kontextzeile, 4 Überschriften und 3 wiederholte beziehungsweise isolierte Zeichnungslabels ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Die Seitenüberschriften bezeichnen keinen zweiten, unabhängigen Formelblock: Das Reduzieren der Weite eines erprobten PK-3-Oberteil-Grundschnitts ist auf dieser Seite die dargestellte Methode, um daraus einen PK-0-Korsagen-Grundschnitt zu gewinnen. Die beiden Themen wurden deshalb nicht künstlich getrennt.

Das Originaltranskript `s196.md` enthält außerhalb des verbindlichen Extrakts weitere Konstruktionsregeln: die Differenzbeträge werden durch Zulegen und Wegzeichnen entfernt, die ArD-Differenz wird an den Seitennähten halbiert, die AlT um `1,3 cm` angehoben, der Brustpunkt abhängig von der Brustgröße um `0 bis 3 cm` angehoben und überschüssige Taillen- beziehungsweise optional Hüftweite an den Seitennähten entfernt. Diese Beziehungen wurden nicht als zusätzliche Buchfassungen erzeugt. Die beiden gemessenen Kontrollwerte `½ TaW = 34,7 cm` und `½ HüW = 49,2 cm` bleiben mangels extrahierter Zielwert- oder Differenzrechnung ausgeschlossen. Der Abschluss von `O07` gilt für den vorhandenen extrahierten Kandidatenbestand.
