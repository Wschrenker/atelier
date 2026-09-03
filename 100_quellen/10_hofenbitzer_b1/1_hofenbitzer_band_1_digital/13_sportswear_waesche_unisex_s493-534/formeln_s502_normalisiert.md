# Fachlich normalisierte Formeln — S. 502

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s502.md`
Originaltranskript: `s502.md`
Buchseite: Hofenbitzer, Band 1, S. 502

Die Seite eröffnet im Block „Sport · Wäsche · Unisex" die Modellentwicklungen aus der Leggings und zeigt die Unisex-Varianten Shortpants und Bikerpants. Sie führt keinen eigenen Grundschnitt, sondern wandelt den Leggings-Grundschnitt der S. 500–501 ab; alle Modelle sind laut Buch „nur mit sehr elastischen Materialien" zu fertigen. Die vier extrahierten Kandidatenblöcke stammen aus dem Abschnitt „Mögliche Reduzierung der TaW", aus den Beschriftungen der Grundschnitt-Abwandlung `□1` und aus den Beschriftungen des Bundes für Gummitunnel `□2`. Der Maßsatz stammt aus der Konstruktionstabelle auf S. 500 (DOB-Größe 38, TaU 72 cm).

## HOF-B1-S502-F01 — Mögliche Reduzierung der Taillenweite

- **Fachlicher Zweck:** Die Taillenweite der Modellabwandlung aus dem gemessenen Taillenumfang durch eine prozentuale Reduzierung bestimmen; die Weite gilt für die Hose und für den Bund.
- **Quelle:** `formeln_s502.md`, Zeilen 9–11; Originaltranskript `s502.md`, Zeilen 19–21; Buchseite 502. Zeichnungsbeleg: `formeln_s502.md`, Zeile 28 (`s502.md`, Zeile 51, Bund `□2`).
- **Originalbezeichnung:** `TaW = TaU − 0 bis −5 %`
- **Normalisierte Bezeichnung:** `taillenweite_reduziert_modellabwandlung`

### Buchfassung

```text
- TaW = TaU − 0 bis −5 %
- = 72 cm · 0,95
- = 68,4 cm
```

```text
- TaU − 0 bis −5 %
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenumfang_gemessen` | TaU | 72 (Konstruktionstabelle S. 500) | cm |
| `taillenreduzierung_prozent` | `0 bis 5 %` | 0 bis 5 | Prozent |

### Formel und Rechenschritte

```text
taillenweite = taillenumfang_gemessen * (1 - taillenreduzierung_prozent / 100)
mit taillenreduzierung_prozent aus dem Bereich 0 % bis 5 %

Buchwerte (TaU = 72 cm), gedruckter Rechenweg mit 5 %:
taillenweite = 72 cm * 0,95 = 68,4 cm

Die untere Bereichsgrenze ergaebe:
taillenweite = 72 cm * (1 - 0/100) = 72 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `taillenweite` | reduzierte Taillenweite von Hose und Bund | 68,4 (bei 5 %) | cm |

- **Abhängigkeiten:** Gemessener `TaU` aus der Konstruktionstabelle auf S. 500.
- **Gültigkeitsbereich:** Modellabwandlungen der Leggings (Shortpants, Bikerpants), Grundschnitt-Abwandlung `□1` und Bund für Gummitunnel `□2`. S. 503, Schritt 5 sagt ausdrücklich, dass die Taillenweitenberechnung „für die Hose und den Bund" durchzuführen ist, und verweist dafür auf diese Seite.
- **Technische Randbedingung:** Der Faktor `0,95` ist die gedruckte Umrechnung des Prozentsatzes 5 %; er ist nicht als zusätzliche Buchgröße zu führen. Eine Auswahlregel innerhalb von `0 bis 5 %` nennt die Quelle nicht.
- **Offene Fragen oder Widersprüche:** Keine innerhalb der Zeile. Der Rechenweg ist konsistent: `72 · 0,95 = 68,4`.
- **Abgrenzung:** Die Beziehung ist wortgleich mit `HOF-B1-S501-F01` (Leggings-Grundschnitt, Bund für Gummitunnel). Dort ist das gedruckte Ergebnis `72 cm`, also der Prozentsatz 0 %; hier ist der Rechenweg mit 5 % ausgeschrieben und ergibt 68,4 cm. Beide Seiten drucken ein eigenes Ergebnis und erklären keine Identität; S. 502 ist zudem eine Modellabwandlungsseite. Die Zeile erhält deshalb eine eigene ID. Die Wiederholung `TaU − 0 bis −5 %` an der Bundzeichnung `□2` derselben Seite ist ein Beleg zu dieser Formel und erhält nach der Regel aus `V3-J05` keine zweite ID.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Prozentsatz als Parameter mit dem Bereich `0 bis 5 %` führen, getrennt vom Umfangs- (`−15 %`) und vom Längenprozentsatz (`−5 %`) der Leggings. Das Ergebnis ist die Eingabe der Ausfallberechnung `HOF-B1-S502-F02`.

## HOF-B1-S502-F02 — Taillenausfall aus der Weitendifferenz

- **Fachlicher Zweck:** Die an der Taille zu entfernende Mehrweite („Ausfall") als Differenz zweier halber Taillenweiten bestimmen.
- **Quelle:** `formeln_s502.md`, Zeilen 16–17; Originaltranskript `s502.md`, Zeilen 38–39; Buchseite 502. Zugehöriger Schritttext auf S. 503, Schritt 4 (`s503.md`, Zeile 15), selbst nicht extrahiert.
- **Originalbezeichnung:** `½ TaW − ½ TaU = Ausfall` mit `36,5 cm − 34,2 cm = 2,3 cm`
- **Normalisierte Bezeichnung:** `taillenausfall_modellabwandlung`

### Buchfassung

```text
- ½ TaW − ½ TaU = Ausfall
- 36,5 cm − 34,2 cm = 2,3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `halbe_weite_minuend` | `½ TaW` laut Wortformel | 36,5 | cm |
| `halbe_weite_subtrahend` | `½ TaU` laut Wortformel | 34,2 | cm |

### Formel und Rechenschritte

```text
taillenausfall = halbe_weite_minuend - halbe_weite_subtrahend

Gedruckte Rechnung:
taillenausfall = 36,5 cm - 34,2 cm = 2,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `taillenausfall` | an der Taille zu entfernende Mehrweite der Schnitthälfte | 2,3 | cm |

- **Abhängigkeiten:** `HOF-B1-S502-F01` liefert `TaW = 68,4 cm`, also `½ TaW = 34,2 cm`; der Maßsatz auf S. 500 liefert `TaU = 72 cm`, also `½ TaU = 36 cm`.
- **Gültigkeitsbereich:** Grundschnitt-Abwandlung `□1`, Damenmodelle. S. 503, Schritt 4 ordnet den Ausfall ausdrücklich den Damen zu: „Gleichzeitig kann bei Damen die Mehrweite an der Taille nach der Reduzierung um 0 bis 5 % dort als Taillenausfall entfernt werden."
- **Technische Randbedingung:** Die Rechnung arbeitet mit halben Weiten, also mit der Schnitthälfte, nicht mit dem Umfang. Die Verteilung des Ausfalls auf Seitennaht und Abnäher ist nicht extrahiert.
- **Offene Fragen oder Widersprüche:** **Zwei gedruckte Defekte in derselben Zeile.**
  1. **Reihenfolge der Benennungen:** Die Wortformel nennt `½ TaW` als Minuend und `½ TaU` als Subtrahend. Nach der Definition derselben Seite ist `TaW` jedoch die **reduzierte** Weite (68,4 cm, also `½ TaW = 34,2 cm`) und `TaU` das gemessene Körpermaß (72 cm, also `½ TaU = 36 cm`). Die Wortformel ergäbe damit `34,2 − 36 = −1,8 cm`; die gedruckte Zahlenzeile rechnet in umgekehrter Richtung. Der Subtrahend 34,2 cm ist eindeutig `½ TaW`, steht in der Zahlenzeile aber an der Stelle von `½ TaU`.
  2. **Unbelegter Minuend:** Der Wert `36,5 cm` ist weder `½ · 72 cm = 36 cm` noch `½ · 68,4 cm = 34,2 cm`. Der Leggings-Grundschnitt arbeitet nach `HOF-B1-S501-F01` mit dem ungekürzten `TaU = 72 cm`, also mit einer halben Taillenweite von 36 cm. Woher die zusätzlichen `0,5 cm` stammen, sagt die Seite nicht; die Zeichnungsbeschriftung `0,5 bis 1 cm` (`s502.md`, Zeile 35) steht an anderer Stelle und wurde nicht als Erklärung übernommen. Die gedruckte Differenz selbst ist arithmetisch richtig: `36,5 − 34,2 = 2,3`.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, solange Benennungsrichtung und Herkunft des Minuenden nicht am Buch geklärt sind. Ein korrigierter Wert wurde nicht erfunden. Die rechnerisch naheliegende Form `taillenausfall = halber_taillenumfang - halbe_taillenweite = 36 cm - 34,2 cm = 1,8 cm` ist hier nur als geprüfte, **nicht belegte** Lesart festgehalten und ausdrücklich nicht die Buchfassung.

## HOF-B1-S502-F03 — Ansatzlänge des Bundes für den Gummitunnel

- **Fachlicher Zweck:** Die Länge des Bundstreifens für den Gummitunnel aus den am Schnitt gemessenen Taillennähten von Rück- und Vorderteil bestimmen.
- **Quelle:** `formeln_s502.md`, Zeilen 22–23; Originaltranskript `s502.md`, Zeilen 48–49; Buchseite 502, Zeichnung `□2`.
- **Originalbezeichnung:** `2 × h.TaN messen` und `2 × v.TaN messen`
- **Normalisierte Bezeichnung:** `bundlaenge_gummitunnel`

### Buchfassung

```text
- 2 × h.TaN messen
- 2 × v.TaN messen
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hintere_taillennaht` | h.TaN — hintere Taillennaht der Schnitthälfte | am Schnitt gemessen | cm |
| `vordere_taillennaht` | v.TaN — vordere Taillennaht der Schnitthälfte | am Schnitt gemessen | cm |
| `spiegelungsfaktor` | `2 ×` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
bundabschnitt_hinten = 2 * hintere_taillennaht
bundabschnitt_vorne  = 2 * vordere_taillennaht
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `bundabschnitt_hinten` | hinterer Abschnitt des Bundstreifens zwischen den Seitennähten | cm |
| `bundabschnitt_vorne` | vorderer Abschnitt des Bundstreifens zwischen den Seitennähten | cm |

- **Abhängigkeiten:** Die beiden Taillennahtlängen werden am abgewandelten Schnitt `□1` abgegriffen; sie sind keine Körpermaße und im Buch nicht beziffert.
- **Gültigkeitsbereich:** Bund mit Tunnel zum Einziehen eines Gummibands, Zeichnung `□2`. Die Zeichnung trägt zusätzlich die Bezeichnungen `rSN` und `lSN` für die beiden Seitennähte, die den Bund in den hinteren und den vorderen Abschnitt teilen.
- **Technische Randbedingung:** Der Faktor `2` spiegelt die Schnitthälfte auf die volle Weite. Die **Summe** beider Abschnitte zur gesamten Bundlänge ist im Buch nicht gedruckt und wird hier nicht als Buchfassung geführt; sie ergäbe sich technisch als `2 * hintere_taillennaht + 2 * vordere_taillennaht`.
- **Offene Fragen oder Widersprüche:** Das Buch beziffert weder `h.TaN` noch `v.TaN` und nennt keine Zugabe für Tunnel oder Verarbeitung. Die Beziehung zur reduzierten Taillenweite `TaU − 0 bis −5 %`, die auf derselben Zeichnung steht, ist nicht ausgeschrieben: Ob die gemessenen Nahtlängen die reduzierte Weite bereits enthalten, sagt die Seite nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Beide Nahtlängen als gemessene Schnittgrößen führen, nicht als Körpermaße. Den Faktor `2` als reine Spiegelung ohne Einheit implementieren. Eine Gesamtlänge erst nach Klärung der Verarbeitungszugabe zusammensetzen.

## Ausgeschlossene Kandidaten

Keine. Alle vier extrahierten Kandidatenblöcke mit insgesamt acht Zeilen sind in den Formelblöcken abgebildet: Zeilen 9–11 in `HOF-B1-S502-F01`, Zeilen 16–17 in `HOF-B1-S502-F02`, Zeilen 22–23 in `HOF-B1-S502-F03` und Zeile 28 als Zeichnungsbeleg zu `HOF-B1-S502-F01`.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s502.md` enthält weitere bemaßte Angaben, die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen und deshalb nicht als Buchfassungen ergänzt wurden:

- die Modelllängen `z. B. 30 bis 38 cm` (Shortpants) und `z. B. 43 bis 50 cm` (Bikerpants) sowie die Beschriftung `neue Modell-Länge` (Zeilen 32–34);
- die Saumerweiterung `0,5 bis 1 cm` mit dem Zusatz `maximal` (Zeilen 35 und 37);
- die Beschriftungen `h.TaN messen` und `v.TaN messen` an der Grundschnitt-Abwandlung `□1` (Zeile 36), also die Messanweisung ohne den Faktor `2 ×`;
- die Reduktionspfeile `−15 %` und `−5 %` (Zeile 41), die auf die Umfangs- und Längenreduzierung der Leggings verweisen (`HOF-B1-S501-F02` und `HOF-B1-S501-F03`);
- die Linienbezeichnungen HüLi, SrLi, KnLi, WaLi, hM und vM sowie die Symbole ♀ und ♂ am vorderen Hosenausschnitt (Zeilen 30, 31 und 40).

Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
