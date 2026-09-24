# Formeln s191 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s191.md](s191.md)). Kein einziger formel- oder coderelevanter Punkt ist bisher
von Werner am Original bestätigt (siehe die neun offenen Prüfstellen dort).
Diese Extraktion wurde auf ausdrücklichen Wunsch Werners trotzdem als
Walking-Skeleton-Durchlauf erstellt (Blocker übersprungen) und beruht
ausschließlich auf [`ocr_s191.md`](ocr_s191.md) sowie der Zeichnungsbeschreibung
in [`skizzen_s191.json`](skizzen_s191.json). Sie ersetzt keine spätere
Bestätigung der formelrelevanten Stellen am Original und darf nicht als
menschlich verifiziert gelten.

`s191.md` vermerkte, dass die Layout-Antwort keinen eigenständigen
Formeltext-Block meldet und deshalb keine `formeln_s191.md` angelegt würde.
Dieser Befund wird hier revidiert: Der Fließtext und die Zeichnung enthalten
mehrere zahlenbasierte Rechenbeziehungen zur Armloch-Vertiefung und
-Verbreiterung.

Zusätzlich gilt die bekannte OCR-Lücke aus [s191.md](s191.md): Die acht blauen
Kreiszahlen ①–⑧ im Buch fehlen im OCR-Fließtext vollständig; die Zuordnung
Kreiszahl↔Satz unten stammt aus der Zeichnungsbeschreibung in
`skizzen_s191.json` (ebenfalls unbestätigt), nicht aus einer eigenen
Bildprüfung durch diese Extraktion.

## 1. Armloch-Verbreiterung → Brustweite und Passformklasse (Rechenbeispiel)

Quelle: `ocr_s191.md`, Zeile 40–44.

```text
Durch die Armloch-Verbreiterung, hier um 2 cm, vergrößert
sich die Brustweite um 4 cm. So
wird aus dem Grundschnitt mit PK
3 ein Grundschnitt mit PK 5.
```

Hinweis: konkretes Zahlenbeispiel im linken/mittleren Einleitungstext, kein
Kreiszahl-Schritt.

## 2. Armloch-Vertiefung → Armlochtiefe/AIT (Rechenbeispiel)

Quelle: `ocr_s191.md`, Zeile 46–48.

```text
Durch die Armloch-Vertiefung,
hier um 1,5 cm vergrößert sich die
Armlochtiefe (AIT) um 1,5 cm.
```

Hinweis: OCR-Schreibweise „AIT" unverändert übernommen; `s191.md` vermutet
„AlT" (Armlochtiefe) als eigentliche Buchabkürzung, am Original zu bestätigen.

## 3. Armloch-Verbreiterung – Gesamtbereich und Aufteilung VT/RT

Quelle: `ocr_s191.md`, Zeile 63–68 (Schrittfließtext, laut Zeichnungsbeschreibung
Kreiszahl ①, doppelt: ⅓-Wert am VT, ⅔-Wert am RT).

```text
Das Armloch kann je nach ge-
wünschter Passformklasse an
der Seitennaht um insge-
samt 1 bis 6 cm verbreitert
werden: ⅓ am VT und ⅔ am
RT.
```

Zeichnungsbeleg (`skizzen_s191.json`, Region `img-0.jpeg`): „Links Kreiszahl
'1' bei '⅓ Armloch-Verbreiterung', rechts Kreiszahl '1' bei '⅔
Armloch-Verbreiterung'".

## 4. Passformklasse und Brustweite je cm Armloch-Verbreiterung (allgemeine Regel)

Quelle: `ocr_s191.md`, Zeile 70–77.

```text
Die Passformklasse (PK) vergrö-
ßert sich um einen Punkt pro 1
cm der Armloch-Verbreiterung.
Am halben Grundschnitt vergrö-
ßert sich die halbe Brustweite
dabei ebenfalls um 1 cm. Am gan-
zen Schnitt also um den doppel-
ten Betrag.
```

Hinweis: allgemeine Regel, aus der sich Abschnitt 1 (2 cm → 4 cm, PK 3 → PK 5)
als Spezialfall ergibt.

## 5. Armloch-Vertiefung als Anteil der Armloch-Verbreiterung

Quelle: `ocr_s191.md`, Zeile 79 (laut Zeichnungsbeschreibung Kreiszahl ②,
doppelt links/rechts).

```text
Das Armloch um ca. \(1 / 2\) bis \(3 / 4\) der Armloch-Verbreiterung vertiefen; die AIT wird groBer.
```

Hinweis: OCR-Schreibweise „groBer" (vermutlich „größer") unverändert
übernommen; LaTeX-Bruchschreibweise `\(1 / 2\)` / `\(3 / 4\)` stammt direkt aus
der OCR-Ausgabe.

## 6. Schulter-Verbreiterung als Anteil der Armloch-Verbreiterung

Quelle: `ocr_s191.md`, Zeile 80 (laut Zeichnungsbeschreibung Kreiszahl ③).

```text
Schulter-Verbreiterung um \(1 / 10\) der Armloch-Verbreiterung.
```

Zeichnungsbeleg: blauer Doppelpfeil zwischen den beiden mittleren
Schulter-/Ärmelspitzen mit Kreiszahl „3".

## 7. BrB- und RüB-Vergrößerung beim Formen der neuen Armlöcher

Quelle: `ocr_s191.md`, Zeile 81–82 (laut Zeichnungsbeschreibung Kreiszahl ④ für
BrB, Kreiszahl ⑤ für RüB).

```text
Beim Formen der neuen Armlocher die BrB um ca. \(1 / 8\) der Armloch-Verbreiterung
und die RuB um ca. \(1 / 4\) der Armlochverbreiterung vergro-bern. Dabei konnen auch die Armlinien verschoben werden.
```

Hinweis: OCR-Schreibweisen „Armlocher" (Armlöcher), „RuB" (vermutlich „RüB"),
„vergro-bern" (vermutlich „vergrößern", zusätzlich falsch getrennt) und
„konnen" (können) unverändert übernommen. Ausschreibung von „BrB"/„RüB"
ungeklärt (vermutlich Brustbreite/Rückenbreite), siehe Prüfstelle 7 in
`s191.md`.

## 8. Ärmelpunkte-Verschiebung nach unten

Quelle: `ocr_s191.md`, Zeile 83 (laut Zeichnungsbeschreibung Kreiszahl ⑥,
doppelt links/rechts, mit grünem Abwärtspfeil).

```text
Beide Armelpunkte um \(3 / 4\) der Armloch-Vertiefung nach unten verschiben.
```

Zeichnungsbeleg: graue Textbox „Ärmelpunkt um ¾ Armloch-Vertiefung nach unten
verschieben" beidseits, mit Kreiszahl „6". OCR-Schreibweise „Armelpunkte"
(Ärmelpunkte) und „verschiben" (verschieben) unverändert übernommen.

## 9. Neue Seitennähte parallel zu den alten (geometrische Beziehung)

Quelle: `ocr_s191.md`, Zeile 87, erster Teilsatz.

```text
Die neuen Seitennahte parallel zu den alten Seitennahten zeichnen (gepunktete Linie), Nahtlingen kontrollieren.
```

Hinweis: keine Zahlenangabe, aber eine geometrische Konstruktionsregel
(Parallelverschiebung); OCR-Schreibweisen „Seitennahte" (Seitennähte) und
„Nahtlingen" (laut `s191.md` am Original als „Nahtlängen" bestätigt sichtbar)
unverändert übernommen.

## 10. Hüftweite-Reduzierung an der Seitennaht (Rechenbeispiel)

Quelle: `ocr_s191.md`, Zeile 88, erster Satz.

```text
Die Hüftweite kann nach der Verbreiterung wieder reduziert werden (hier an der Seitennaht um 0,5 cm, das sind insgesamt 2 cm Reduzierung).
```

Hinweis: konkretes Zahlenbeispiel, keine Kreiszahl im Fließtext erkennbar.

## Nicht als Formel erfasst

- Zeile 50–58 („Die gewünschte neue Passformklasse kann in der Tabelle der
  Passformklassen auf Seite 176 bestimmt und die neuen Zugaben in der
  Zugabentabelle ausgewählt werden. Die Änderungswerte ergeben sich aus den
  Differenzen der jeweiligen Zugaben (siehe auch Seite 194)."): Verweis auf
  Tabellen und Rechenmethode auf anderen Seiten, hier nur zu verlinken, nicht
  zu kopieren.
- Zeile 88, zweiter Satz („Die Taillenweite sollte - wenn notwendig - nur an
  den Abnähern reduziert oder erweitert werden."): Auswahlregel ohne
  Zahlenwert, hier nicht als eigene Formel geführt.
- Zeile 37–38 und 6–14: keine Zahl, keine Rechenbeziehung (Verweise, Zweck der
  Vergrößerung).
- Maßfigur unten links in der Zeichnung („88/72/97" → „10/8/9", „168" laut
  `skizzen_s191.json`): erkennbare Pfeil-Zuordnung, aber Bedeutung und
  Rechenregel aus dem OCR-Text nicht ersichtlich; nicht als Formel erfasst,
  um keine Fachregel zu erfinden (siehe Prüfstelle 6 in `s191.md`).
- Kreiszahlen ⑦ und ⑧ (laut `skizzen_s191.json` entlang der Seitennaht-Linien,
  „dreifach"/„zweifach" mit blauen Pfeilen): im OCR-Fließtext kein zugehöriger
  Zahlenwert gefunden; vermutlich zu Abschnitt „2 Seitennähte und Hüftweite"
  gehörig, aber Zuordnung zu Formel 9/10 nicht bestätigt und daher nicht
  spekulativ ergänzt.
