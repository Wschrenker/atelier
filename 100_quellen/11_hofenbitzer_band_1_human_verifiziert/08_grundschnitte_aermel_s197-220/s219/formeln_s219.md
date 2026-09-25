# Formeln s219 – fototreue Extraktion

Diese Fassung ersetzt die frühere rein mechanische OCR-Formelstellenliste. Sie
folgt dem
[Prompt für Formelextraktion und Normalisierung](../../../910_repertoire/prompt/hofenbitzer_formelextraktion_normalisierung.md)
und stützt sich auf [`ocr_s219.md`](ocr_s219.md) sowie die in
[`s219.md`](s219.md) dokumentierten Bestätigungen und OCR-Anmerkungen.

**Bereitschaftslage:** Von den vier Abschnitten der Seite ist bislang nur der
Abschnitt „Senkrechten Öffnungsbetrag berechnen“ einschließlich seiner
Folgeaufteilung (½ bzw. ⅓) am Original bestätigt (`s219.md`, 2026-09-24). Die
Abschnitte „Kontrolle des neuen Ärmelkugel-Umfangs“ und „Korrektur der neuen
Ärmelkugel-Höhe“ sind **nicht** bestätigt (siehe Prüfstelle 4 in `s219.md`).
Sie werden hier auf ausdrücklichen Wunsch Werners trotzdem als
Walking-Skeleton-Durchlauf mit erfasst (Blocker übersprungen), bleiben aber als
offen gekennzeichnet und ersetzen keine spätere Bestätigung am Original.

## 1. Senkrechten Öffnungsbetrag berechnen (bestätigt)

Quelle: `ocr_s219.md`, Zeilen 19–25 (Abschnitt „1 Senkrechten Öffnungsbetrag
berechnen“); Bestätigung laut `s219.md`, Abschnitt „Vorab geklärte formel- und
coderelevante Stellen“.

Buchfassung (gedruckt, unverändert):

```text
Öffnung = Fehlweite − ⅔ SuPoE
hier = 5,2 cm − 1,7 cm = 4,5 cm
```

Bestätigte Arbeitslesung (Werner, 2026-09-24):

```text
Öffnung = 5,2 cm − 1,7 cm = 3,5 cm
```

Hinweis: Der gedruckte Zwischenwert 4,5 cm ist rechnerisch falsch
(5,2 − 1,7 = 3,5); die Buchfassung bleibt trotzdem unverändert als Bildbeleg
stehen (kein stilles Berichtigen gedruckter Rechenfehler).

## 2. Aufteilung der Öffnung beim Ärmel anpassen (bestätigt, abgeleitet)

Quelle: `ocr_s219.md`, Zeilen 27–35 (Abschnitt „2 Ärmel anpassen“, Schritt
„A □3“); Zahlenwerte laut `s219.md`, Abschnitt „Vorab geklärte …“.

Buchfassung (Fließtext, gedruckt):

```text
Nach links und nach rechts ca. ⅓ oder ½ der berechneten senkrechten Öffnung öffnen.
Bei ½ Öffnung - also mehr Öffnung - entsteht mehr Oberarmweite und eine geringere Ärmelkugelhöhe.
Bei ⅓ Öffnung - also weniger Öffnung - entsteht weniger Oberarmweite und eine höhere Ärmelkugelhöhe.
```

Bestätigte Werte, aus der Arbeitslesung 3,5 cm abgeleitet (`s219.md`):

```text
½ von 3,5 cm = 1,75 cm ≈ 1,8 cm
⅓ von 3,5 cm = 1,166… cm ≈ 1,2 cm
```

Gedruckte Folgewerte – zeichnungsgebunden (Bildlesung, Skizze `skizze_01`,
laut `s219.md` aus dem falschen Zwischenwert 4,5 cm rechnerisch korrekt
geteilt, für die bestätigte Arbeitslesung aber **nicht** zu verwenden):

```text
½ von 4,5 cm = 2,25 cm
⅓ von 4,5 cm = 1,5 cm
```

## 3. Kontrolle des neuen Ärmelkugel-Umfangs (nicht bestätigt – Prüfstelle 4)

Quelle: `ocr_s219.md`, Zeilen 39–43 (Abschnitt „1 Kontrolle des neuen
Ärmelkugel-Umfangs“). Laut `s219.md`, Abschnitt „Bekannte auffällige Stellen“,
hängt die OCR die Formel im Rohtext direkt an Abschnitt 1 an, obwohl sie am
Original zu diesem Abschnitt gehört.

Buchfassung (gedruckt):

```text
Fehlbetrag = ÄkU_min − nachgemessene neue ÄkU
hier = 53,7 cm − 52,5 cm = 1,2 cm
```

Hinweis: Zahlenwerte, Kürzel und Abschnittszuordnung sind noch nicht am
Original bestätigt (Prüfstelle 4, `s219.md`). Status bleibt offen.

## 4. Korrektur der neuen Ärmelkugel-Höhe (nicht bestätigt, abhängig von Abschnitt 3)

Quelle: `ocr_s219.md`, Zeilen 45–51 (Abschnitt „1 Korrektur der neuen
Ärmelkugel-Höhe“, Schritt „A □4“).

Buchfassung (gedruckt):

```text
Die Ärmelkugel oben um ½ Fehlbetrag erhöhen und die Ärmelkugel wie skizziert formen
```

```text
Um ½ des Fehlbetrags sollte der Ärmel am Saum gekürzt und geformt sowie ggf. der Abnäher angehoben werden.
```

Hinweis: Im Rohtext fehlt zwischen „Fehlbetrags“ und „sollte“ ein Leerzeichen
(bereits in `s219.md` vermerkt); hier zur Lesbarkeit mit Leerzeichen
wiedergegeben, ohne den OCR-Befund zu verändern. Beide Teilformeln hängen vom
noch unbestätigten `Fehlbetrag` aus Abschnitt 3 ab und bleiben deshalb
ebenfalls offen.

## Nicht als Formel erfasst

- Marginalie „Optional kann die Saumweite am Abnäher noch vergrößert werden
  (siehe auch Seite 211)“ und „hintere Ärmelpunkt und Schulterpunkt …
  (siehe Seite 207)“: reine Querverweise ohne eigene Rechenbeziehung auf dieser
  Seite, nur zu verlinken.
- Bildunterschriften „Ärmelanpassung für Armlochauflockerung und
  Schulterpolstererhöhung“ und „Neue Ärmelkugel“: Zuordnungsbeschreibungen ohne
  Zahlenwert.
- Am linken Rand mitfotografierter Text der Vorseite (218): gehört nicht zu
  Seite 219, siehe `s219.md`.
- Seitenverweise „207“/„208“ und vertikale Reiterbeschriftung: keine
  Rechenbeziehung.
