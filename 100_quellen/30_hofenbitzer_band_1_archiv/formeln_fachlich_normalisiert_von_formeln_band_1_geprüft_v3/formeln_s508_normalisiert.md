# Fachlich normalisierte Formeln — S. 508

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s508.md`
Originaltranskript: `s508.md`
Buchseite: Hofenbitzer, Band 1, S. 508

Die Seite eröffnet das Kapitel **Shirts**. Sie enthält den Einführungstext, die vollständige Konstruktionstabelle `□2 Konstruktionstabelle für Shirts` und die Erläuterung des Brustabnäher-Ausgleichs. Der Grundschnitt gilt ausdrücklich für T-Shirt und Sweatshirt gemeinsam und ist ein Unisex-Schnitt; VT und RT werden deckungsgleich konstruiert (S. 509, Schrittteil 1).

Vier Kandidatenzeilen sind extrahiert: drei Tabellenzeilen der Konstruktionstabelle und die redaktionelle Anmerkung des Transkripts zur Zeile `HgU`. Die drei Tabellenzeilen tragen zusammen sechs Rechenbeziehungen und erhalten sechs Formel-IDs; die Anmerkung ist ausgeschlossen und unter den Prüfhinweisen als `⚠️` geführt.

Bezugsgrößen der Seite aus der Konstruktionstabelle (nicht extrahiert, hier nur als Eingabewerte zitiert): `KöH = 168 cm`, `BrU = 88 cm` mit `+ 8 cm` Zugabe → `BrW = 96 cm` (`½ = 48`, `¼ = 24`), `RüL = 41,6 cm`, `VL = 45,3 cm`, Größe 38.

## HOF-B1-S508-F01 — Armdurchmesser mit Zugabe

- **Fachlicher Zweck:** Aus dem gemessenen Armdurchmesser das Konstruktionsmaß `ArD+` bilden, das die Breite des angeschnittenen Ärmelansatzes bestimmt.
- **Quelle:** `formeln_s508.md`, Zeile 9; Originaltranskript `s508.md`, Zeile 43; Buchseite 508.
- **Originalbezeichnung:** `ArD + 1 bis 2 → ArD+`
- **Normalisierte Bezeichnung:** `armdurchmesser_mit_zugabe`

### Buchfassung

```text
| ArD | Armdurchmesser | 9,3 | + 1 bis 2 | ArD+ | 10,8 | ½ = 5,4 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser` | ArD | 9,3 | cm |
| `armdurchmesser_zugabe` | `+ 1 bis 2` | 1 bis 2 (im Beispiel 1,5) | cm |

### Formel und Rechenschritte

```text
armdurchmesser_plus = armdurchmesser + armdurchmesser_zugabe

Bereichsgrenzen mit dem Buchwert ArD = 9,3 cm:
armdurchmesser_plus = 9,3 cm + 1 cm = 10,3 cm   (untere Grenze)
armdurchmesser_plus = 9,3 cm + 2 cm = 11,3 cm   (obere Grenze)

Gedruckter Buchwert:
armdurchmesser_plus = 10,8 cm   -> entspricht der Zugabe 1,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `armdurchmesser_plus` | Armdurchmesser mit Weitenzugabe, Konstruktionsmaß `ArD+` | cm |

- **Abhängigkeiten:** `ArD` als gemessenes Körpermaß der Konstruktionstabelle. Weiterverwendet in `HOF-B1-S508-F02`, `HOF-B1-S509-F01` und `HOF-B1-S509-F03`.
- **Gültigkeitsbereich und Randbedingungen:** Konstruktionstabelle `□2` für Shirts, Größe 38. Der Zugabebereich `1 bis 2 cm` steht in der Tabelle ohne Modellbindung; die Zugabe ist eine Weitenzugabe, keine Dehnungsreduzierung.
- **Offene Fragen oder Widersprüche:** Die im Beispiel verwendete Zugabe von `1,5 cm` ist nicht als Zahl gedruckt, sondern nur aus `9,3 + x = 10,8` erschließbar. Sie liegt in der Mitte des gedruckten Bereichs. Die Quelle nennt keine Auswahlregel innerhalb des Bereichs `1 bis 2 cm`; eine solche wurde nicht ergänzt. Bereich und gewählter Beispielwert bleiben getrennt geführt.
- **Abgrenzung:** S. 508 nennt zwei Weitenklassen für die Brustweitenzugabe (T-Shirt `ca. 6 bis 12 cm`, Sweatshirt `ca. 10 bis 16 cm`). Für die Armdurchmesserzugabe unterscheidet die Quelle **nicht** nach Modell. Eine Kopplung an die Brustweitenzugabe wurde nicht erfunden.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `armdurchmesser_zugabe` als Parameter mit dem Bereich `[1, 2]` und dem Vorgabewert `1,5` führen, den Beispielwert also als Vorgabe und nicht als Konstante. Die Zugabe verändert über `HOF-B1-S509-F01` unmittelbar die Ärmelweite; S. 508 hält dazu fest: „Mit der Größe des Armlochs verändert sich auch die Ärmelweite am Oberarm."

## HOF-B1-S508-F02 — Halber Armdurchmesser mit Zugabe

- **Fachlicher Zweck:** Das in der Konstruktion tatsächlich abgetragene Teilmaß `½ ArD+` bereitstellen.
- **Quelle:** `formeln_s508.md`, Zeile 9; Originaltranskript `s508.md`, Zeile 43; Buchseite 508.
- **Originalbezeichnung:** `½ = 5,4`
- **Normalisierte Bezeichnung:** `halber_armdurchmesser_mit_zugabe`

### Buchfassung

```text
| ArD | Armdurchmesser | 9,3 | + 1 bis 2 | ArD+ | 10,8 | ½ = 5,4 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser_plus` | ArD+ | 10,8 | cm |
| `halbierungsfaktor` | `½` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
halber_armdurchmesser_plus = armdurchmesser_plus / 2

Gedruckter Buchwert (ArD+ = 10,8 cm):
halber_armdurchmesser_plus = 10,8 cm / 2 = 5,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `halber_armdurchmesser_plus` | Teilmaß `½ ArD+`, Abtragungsmaß der Rumpf- und Ärmelkonstruktion | cm |

- **Abhängigkeiten:** `HOF-B1-S508-F01`.
- **Gültigkeitsbereich und Randbedingungen:** Teilmaßspalte der Konstruktionstabelle `□2`. Die Tabelle rechnet das Teilmaß vor, weil die Konstruktion auf S. 509 ausschließlich mit dem halben Wert arbeitet.
- **Offene Fragen oder Widersprüche:** Keine. `10,8 : 2 = 5,4` geht exakt auf.
- **Verwendung:** `HOF-B1-S509-F01` (Schritt 7, Abtragung von P6) und — vermindert um 1 cm — `HOF-B1-S509-F03` (Schritt 16, Ärmelkugel).
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Nicht als eigenes Eingabemaß führen, sondern immer aus `armdurchmesser_plus` ableiten, damit eine geänderte Zugabe in Rumpf- und Ärmelkonstruktion gleichzeitig wirkt.

## HOF-B1-S508-F03 — Brustpunktabstand als Proportionsmaß

- **Fachlicher Zweck:** Den waagerechten Abstand des Brustpunkts von der vorderen Mitte proportional aus dem Brustumfang bestimmen.
- **Quelle:** `formeln_s508.md`, Zeile 10; Originaltranskript `s508.md`, Zeile 44; Buchseite 508.
- **Originalbezeichnung:** `Brustpunktabstand = BrU/10`
- **Normalisierte Bezeichnung:** `brustpunktabstand`

### Buchfassung

```text
| BrPA | Brustpunktabstand = BrU/10 | 8,8 | + 0,6 | BrPA+ | 9,4 |  |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustumfang` | BrU | 88 | cm |
| `teiler` | `/10` | 10 | dimensionslos |

### Formel und Rechenschritte

```text
brustpunktabstand = brustumfang / 10

Buchwert der Konstruktionstabelle (BrU = 88 cm):
brustpunktabstand = 88 cm / 10 = 8,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `brustpunktabstand` | Waagerechter Abstand des Brustpunkts von der vorderen Mitte, `BrPA` | cm |

- **Abhängigkeiten:** `BrU` aus den Hauptmaßen der Konstruktionstabelle. Der **gemessene** Brustumfang wird verwendet, nicht die Brustweite `BrW = 96 cm`; die Zeile rechnet ausdrücklich mit `BrU/10`, und der gedruckte Wert `8,8` bestätigt das (`96 : 10` wäre `9,6`).
- **Gültigkeitsbereich und Randbedingungen:** Konstruktionstabelle `□2`. Das Maß wird im Grundschnitt selbst nicht gebraucht: Es geht erst in die Vorderteil-Optimierung mit Brustabnäher auf S. 510 ein (dort Schritt 2, „Brustpunktabstand+ (BrPA+) von der vM ins VT abtragen → BrP").
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit. Die Spaltenzuordnung ist untypisch: Der berechnete Proportionswert `8,8` steht in der Spalte **Körpermaß**, obwohl er kein gemessenes Maß ist; die Berechnungsvorschrift steht stattdessen in der Namensspalte. Das ist so gedruckt und wurde nicht umsortiert.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `BrPA` als abgeleitete Größe aus `BrU` führen und nicht als messbares Körpermaß anlegen, obwohl die Tabellenspalte das nahelegt. Ein gemessener Brustpunktabstand könnte später als Alternativeingabe daneben stehen; die Quelle sieht das an dieser Stelle nicht vor.

## HOF-B1-S508-F04 — Brustpunktabstand mit Zugabe

- **Fachlicher Zweck:** Den Brustpunktabstand um die Zugabe erweitern, mit der auf S. 510 der Brustpunkt angetragen wird.
- **Quelle:** `formeln_s508.md`, Zeile 10; Originaltranskript `s508.md`, Zeile 44; Buchseite 508.
- **Originalbezeichnung:** `BrPA + 0,6 → BrPA+`
- **Normalisierte Bezeichnung:** `brustpunktabstand_mit_zugabe`

### Buchfassung

```text
| BrPA | Brustpunktabstand = BrU/10 | 8,8 | + 0,6 | BrPA+ | 9,4 |  |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustpunktabstand` | BrPA | 8,8 | cm |
| `brustpunktabstand_zugabe` | `+ 0,6` | 0,6 | cm |

### Formel und Rechenschritte

```text
brustpunktabstand_plus = brustpunktabstand + brustpunktabstand_zugabe

Buchwerte:
brustpunktabstand_plus = 8,8 cm + 0,6 cm = 9,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `brustpunktabstand_plus` | Brustpunktabstand mit Zugabe, Konstruktionsmaß `BrPA+` | cm |

- **Abhängigkeiten:** `HOF-B1-S508-F03`.
- **Gültigkeitsbereich und Randbedingungen:** Konstruktionstabelle `□2`; verwendet in Schritt 2 der Vorderteil-Optimierung auf S. 510.
- **Offene Fragen oder Widersprüche:** Die Zugabe `0,6 cm` steht als **fester Einzelwert ohne Bereich** — anders als alle übrigen Zugaben derselben Tabelle (`+ 0 bis 1`, `+ 1 bis 2`, `− 0 bis 2°`). Die Quelle begründet den Wert nicht und nennt keine Abhängigkeit von Größe oder Weitenklasse. Er ist unverändert als Konstante übernommen; eine Herleitung wurde nicht erfunden.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `0,6 cm` als benannte, änderbare Konstante führen und die fehlende Begründung im Modell vermerken. Solange nur eine Größe belegt ist, lässt sich nicht entscheiden, ob der Wert größenkonstant oder größenabhängig gemeint ist.

## HOF-B1-S508-F05 — Differenz aus Vorderlänge und Rückenlänge

- **Fachlicher Zweck:** Die Mehrlänge des Vorderteils gegenüber dem Rückenteil bestimmen, aus der sich der Bedarf an Brustabnäherinhalt ableitet.
- **Quelle:** `formeln_s508.md`, Zeile 15; Originaltranskript `s508.md`, Zeile 49; Buchseite 508.
- **Originalbezeichnung:** `Differenz VL − RüL`
- **Normalisierte Bezeichnung:** `laengendifferenz_vt_rt`

### Buchfassung

```text
|  | Differenz VL − RüL | 3,7 | − 3 bis 4 | Abnäherinhalt | [leer] |  |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderlaenge` | VL (waagerechte Taille) | 45,3 | cm |
| `rueckenlaenge` | RüL (waagerechte Taille) | 41,6 | cm |

### Formel und Rechenschritte

```text
laengendifferenz = vorderlaenge - rueckenlaenge

Buchwerte der Konstruktionstabelle (VL = 45,3 cm, RüL = 41,6 cm):
laengendifferenz = 45,3 cm - 41,6 cm = 3,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `laengendifferenz` | Mehrlänge der Vorderlänge gegenüber der Rückenlänge | cm |

- **Abhängigkeiten:** `VL` und `RüL` aus der Konstruktionstabelle, beide an der **waagerechten** Taille gemessen. Beide Zeilen stehen selbst nicht im Extrakt und sind hier nur als Eingabewerte zitiert.
- **Gültigkeitsbereich und Randbedingungen:** Konstruktionstabelle `□2`. Die Differenz ist keine Abtragung, sondern eine Kontrollgröße: Sie entscheidet, ob der Grundschnitt unverändert verwendet werden kann.
- **Offene Fragen oder Widersprüche:** Keine. `45,3 − 41,6 = 3,7` geht exakt auf.
- **Abgrenzung:** Dieselbe Beziehung steht auf S. 510 mit einem zweiten Zahlenbeispiel (`VL = 46,8 cm`) und ist dort als `HOF-B1-S510-F01` eigenständig geführt. Die Begründung steht in den Prüfhinweisen von `formeln_s510_normalisiert.md`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Vorderlänge geht in den Rumpf-Grundschnitt auf S. 509 **nicht** ein — S. 510 hält ausdrücklich fest, die Optimierung gelte „für alle Konstruktionen dieser Art von Shirt-Grundschnitten, bei denen die Vorderlänge (VL) nicht in der Konstruktion verwendet wird". `VL` ist damit ausschließlich Eingabe dieser Kontrollrechnung.

## HOF-B1-S508-F06 — Abnäherinhalt aus der Längendifferenz

- **Fachlicher Zweck:** Aus der Längendifferenz den Inhalt des Brustabnähers in der Seitennaht bestimmen; der Wertebereich stellt die im Vorderteil fehlende Mehrlänge dar.
- **Quelle:** `formeln_s508.md`, Zeile 15; Originaltranskript `s508.md`, Zeile 49; Buchseite 508.
- **Originalbezeichnung:** `− 3 bis 4 → Abnäherinhalt`
- **Normalisierte Bezeichnung:** `abnaeherinhalt_brustabnaeher`

### Buchfassung

```text
|  | Differenz VL − RüL | 3,7 | − 3 bis 4 | Abnäherinhalt | [leer] |  |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `laengendifferenz` | Differenz VL − RüL | 3,7 | cm |
| `laengenausgleich` | `− 3 bis 4` | 3 bis 4 | cm |

### Formel und Rechenschritte

```text
abnaeherinhalt = laengendifferenz - laengenausgleich

Bereichsgrenzen mit dem Buchwert der Differenz (3,7 cm):
abnaeherinhalt = 3,7 cm - 3 cm = 0,7 cm    (Abzug 3 cm)
abnaeherinhalt = 3,7 cm - 4 cm = -0,3 cm   (Abzug 4 cm)

Gedrucktes Ergebnis: [leer]
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abnaeherinhalt` | Inhalt des Brustabnähers in der Seitennaht, als Öffnungsmaß des Vorderteils | cm |

- **Abhängigkeiten:** `HOF-B1-S508-F05`.
- **Gültigkeitsbereich und Randbedingungen:** Gilt laut S. 510 für alle Shirt-Grundschnitte dieser Art. Der Abzug `3 bis 4 cm` ist der Anteil der Längendifferenz, den der Grundschnitt ohne Abnäher bereits aufnimmt; nur der Überschuss wird als Abnäher abgeführt. Die Quelle nennt keine Auswahlregel innerhalb des Bereichs `3 bis 4 cm`.
- **Offene Fragen oder Widersprüche:** Die Ergebnisspalte ist im Buch **leer**. Der Fließtext derselben Seite erklärt das: „Beträgt die fehlende Mehrlänge wie in unserem Beispiel um die 0 cm, kann der Grundschnitt ohne weitere Optimierung verwendet werden." Der rechnerische Bereich `−0,3 bis 0,7 cm` deckt sich damit. Das Buch druckt weder diesen Bereich noch eine Schwelle, ab der die Optimierung nötig wird; eine Schwelle wurde nicht erfunden. Ebenso wenig sagt die Quelle, wie ein **negativer** Wert zu behandeln ist — fachlich naheliegend ist „kein Abnäher", belegt ist das nicht.
- **Abgrenzung:** Dieselbe Beziehung steht auf S. 510 mit einem zweiten Zahlenbeispiel und dort erstmals mit gedrucktem Ergebnis (`1,2 bis 2,2 cm`); sie ist als `HOF-B1-S510-F02` eigenständig geführt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Intervall rechnen und das Ergebnis nicht bei 0 abschneiden, sondern das Vorzeichen erhalten — es ist das Unterscheidungsmerkmal zwischen „Grundschnitt genügt" und „Optimierung nach S. 510 nötig". Die Entscheidungsschwelle als offenen Parameter führen, nicht als festen Vergleich gegen 0.

## Ausgeschlossene Kandidaten

| Extraktzeile | Seite / Transkriptzeile | Anzahl | Ausschlussgrund |
|---|---|---:|---|
| Zeile 20 | S. 508, Zeile 54 | 1 | Redaktionelle Anmerkung des Transkripts zum Widerspruch in der Zeile `HgU`. Die Zeile ist keine Buchzeile, sondern eine Feststellung der Transkription; die zugehörige Tabellenzeile `HgU` selbst liegt nicht im Extrakt. Der Widerspruch ist unter Prüfhinweis 1 vollständig festgehalten. |

Dieselbe Behandlung hatten bereits die redaktionellen Anmerkungen zum Satzfehler auf S. 497 in `V3-S02`.

## Prüfhinweise

1. **`⚠️` — Rechenwiderspruch in der Zeile `HgU` (Ärmelsaumweite):** Die Tabellenzeile lautet gedruckt `| HgU | Handgelenkumfang | 16 | − 6 [Zugabe handschriftlich] | Ärmelsaumweite ÄSaW | 22 |`. Das Rechenzeichen ist nach der geprüften Transkription eindeutig ein Minus derselben Type wie in der Zeile `ArL`, der handschriftliche Wert eindeutig `6`, das Ergebnis eindeutig `22`. `16 − 6 = 22` geht nicht auf; rechnerisch stimmig wäre `16 + 6 = 22`. Der Widerspruch wurde **nicht** aufgelöst und die Zeile **nicht** normalisiert: Sie liegt nicht als Kandidatenzeile im Extrakt vor, sondern nur als redaktionelle Anmerkung. Folgenlos ist sie nicht — Schritt 15 auf S. 509 trägt „½ Ärmelsaumweite" ab, also `22 : 2 = 11 cm`. Das gedruckte **Ergebnis** `22` ist eindeutig und für die Konstruktion ausreichend; allein der Weg dorthin ist widersprüchlich. Für eine spätere Nachextraktion ist die Zeile als `gesperrt`-Kandidat vorgemerkt.
2. **Zwei Weitenklassen ohne eigene Tabellenzeile:** Der Fließtext nennt Brustweitenzugaben von `ca. 6 bis 12 cm` (T-Shirt) und `ca. 10 bis 16 cm` (Sweatshirt). Die Tabelle trägt dagegen den Einzelwert `+ 8` ein, der in beiden Bereichen liegt und die Modellfrage damit nicht entscheidet. Beide Angaben liegen außerhalb des Extrakts; sie sind hier nur als Bezugsgrößen zitiert und nicht als Formel geführt.
3. **Unisex-Schnitt ohne Geschlechtsunterscheidung:** S. 508 hält ausdrücklich fest, dass beide Grundschnitte „für Herren und Damen identisch" sind. Anders als bei den Hosen-Grundschnitten (`Für Herren + ca. 0,7 cm`, S. 499 und S. 501) gibt es hier keinen geschlechtsabhängigen Korrekturwert. Die einzige figurabhängige Anpassung ist die Vorderteil-Optimierung auf S. 510, und diese ist über die Längendifferenz gesteuert, nicht über das Geschlecht.
4. **Leere und unausgefüllte Tabellenzeilen:** `TaU` und `HüU` tragen `+ ---` und ein leeres Ergebnis, `OaU` trägt `+ ---` und `---`, `ArL` trägt `− ---`. Taillen- und Hüftweite werden in dieser Konstruktion nicht gebraucht — S. 508 nennt die Schnitte „eher weit und kaum tailliert" und weist die Verlängerung zum Kleid als unüblich aus, weil dann die Hüftweite zu berücksichtigen wäre. Die Zeilen sind bewusst leer und keine Fehlstellen; sie liegen nicht im Extrakt und wurden nicht als Formeln ergänzt. Dieselbe Zurückhaltung wie bei den unausgefüllten `vHoB`- und `hHoB`-Zeilen in `V3-S03`.
5. **Ärmellänge mit zwei Werten:** Die Zeile `ArL` trägt als Ergebnis `60 / 22 [handschriftlich]` — Armlänge und gekürzte Ärmellänge des kurzen Ärmels nebeneinander. Schritt 20 auf S. 509 deckt das ab („Nach Wunsch die Ärmellänge kürzen"), nennt aber keine Rechenbeziehung. Die Zeile liegt nicht im Extrakt; `22 cm` ist ein gewählter Modellwert, keine abgeleitete Größe.
6. **Extraktionsgrenze:** Das Originaltranskript `s508.md` enthält weitere rechenfähige Beziehungen, die im verbindlichen Extrakt fehlen und deshalb nicht als Buchfassungen ergänzt wurden:
   - Zeile 32: `BrU 88 + 8 → BrW 96` mit den Teilmaßen `½ = 48` und `¼ = 24` (letzteres ist die Eingabe von `HOF-B1-S509-F02`);
   - Zeile 40: `AlT 20,1 + 0 bis 1 → AlT+ 20,6`;
   - Zeile 45: `SuB 12,2 + 1 bis 2 → SuNL 13,6`;
   - Zeile 46: `SuWi 20° − 0 bis 2° → SuWi− 18°`;
   - Zeile 52: `HgU 16 − 6 → ÄSaW 22` (siehe Prüfhinweis 1);
   - Zeile 11: die beiden Brustweitenzugabe-Bereiche;
   - Zeile 68: `Einhalteweite (EW) in der Ärmelkugel (ÄK) = 0 cm` — eine belegte Festlegung, die die Länge der Ärmelkugel unmittelbar an die Armlochlänge bindet (S. 509, Schritt 17).

   Besonders `AlT+`, `SuNL`, `SuWi−` und `EW = 0 cm` sind vollständige Rechenbeziehungen mit benannter Eingabe und Ausgabe und tragen den Rumpf-Grundschnitt auf S. 509. Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
