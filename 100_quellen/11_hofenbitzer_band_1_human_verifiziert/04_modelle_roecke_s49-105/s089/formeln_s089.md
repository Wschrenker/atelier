# Formeln s089 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s089.md](s089.md)). Kein einziger formel- oder coderelevanter Punkt ist bisher
von Werner am Original bestätigt. Diese Extraktion wurde auf ausdrücklichen
Wunsch Werners trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker
übersprungen) und beruht auf [`ocr_s089.md`](ocr_s089.md) sowie den bereits
angefertigten Skizzenausschnitten [`skizzen/s089_skizze_01.png`](skizzen/s089_skizze_01.png),
[`skizzen/s089_skizze_03.png`](skizzen/s089_skizze_03.png) und
[`skizzen/s089_skizze_04.png`](skizzen/s089_skizze_04.png). Sie ersetzt keine
spätere Bestätigung der formelrelevanten Stellen am Original und darf nicht als
menschlich verifiziert gelten.

Bekannte OCR-Lücken aus [s089.md](s089.md), die diese Extraktion betreffen:

- Die eingekreiste Schrittzahl ⑨ (vor „□4 Am VT und am RT …") gibt die OCR
  fälschlich als Buchstabe „A" aus.
- Im selben Satz steht am Foto vermutlich das Entsprechungszeichen „≙"
  (`Falteninhalt (≙ FaT)`); die OCR gibt dort ein Plusminuszeichen aus
  (`(± FaT)`). Beide Schreibweisen werden unten nebeneinander dokumentiert,
  nicht still vereinheitlicht.
- Die eingekreisten Schrittzahlen ⑩–⑭ fehlen im OCR-Text vollständig; die
  zugehörigen Sätze erscheinen dort als fortlaufender Text ohne
  Schrittkennung. Die Kennziffern ⑩–⑭, die unten zeichnungsgebunden zitiert
  werden, stammen direkt aus den sichtbaren Kreisen auf
  `skizzen/s089_skizze_04.png` (siehe auch `skizzen_s089.json`, „Kennziffern
  10-13"), nicht aus einer eigenen Zuordnung zu einzelnen OCR-Sätzen. Eine
  feste Satz-für-Satz-Zuordnung ist damit nicht hergestellt.

## 1. Halber Falteninhalt an VT und RT (Markierung Falteninnennaht)

Quelle: `ocr_s089.md`, Zeile 20 (Schrittfließtext, laut Lückenhinweis Foto-Schritt
⑨), zusätzlich zeichnungsgebunden bestätigt durch `skizzen/s089_skizze_01.png`
(mVT, Kennziffer 9, Beschriftung „½ FaI" über „FaT") und
`skizzen/s089_skizze_03.png` (mRT, gleiche Beschriftung ohne sichtbare
Kennziffer).

```text
Am VT und am RT jeweils einen halben Falteninhalt (± FaT) in entsprechender
Höhe anzeichnen → Falteninnennaht.
```

Hinweis: OCR-Zeichen „±" unverändert übernommen; am Original vermutlich „≙"
(Entsprechungszeichen), siehe Lückenhinweis oben. In der Zeichnung erscheint
an dieser Stelle kein Zeichen, sondern die gestapelte Beschriftung „½ FaI" /
„FaT".

## 2. Beginn des Faltenteils mit halbem Falteninhalt

Quelle: `ocr_s089.md`, Zeile 22, zusätzlich zeichnungsgebunden
(`skizzen/s089_skizze_04.png`, Segment „1. Faltensegment" mit Kennziffern
⑩ und ⑪, Beschriftung „½ FaI" über „FaT" am linken Rand).

```text
Am Faltenteil mit der anderen Hälfte des Falteninhalts = Faltentiefe (FaT)
beginnen → Falteninnennaht.
Das erste Faltensegment ansetzen.
```

## 3. Ganzer Falteninhalt je Folgesegment

Quelle: `ocr_s089.md`, Zeilen 24 und 26, zusätzlich zeichnungsgebunden
(`skizzen/s089_skizze_04.png`, Kennziffer ⑫, sich wiederholende Beschriftung
„FaI" / „FaA" zwischen erstem und letztem Faltensegment).

```text
Daran einen ganzen Falteninhalt zeichnen.

So fortfahren, bis alle Faltensegmente angesetzt sind.
```

Hinweis: Die Zeichnung zeigt zwischen den Falteninhalt-Segmenten („FaI")
jeweils ein zusätzlich beschriftetes Zwischenstück „FaA". Dieses Kürzel wird
im OCR-Text auf s089 nicht erklärt; keine Bedeutung erfinden.

## 4. Abschluss des Faltenteils mit halbem Falteninhalt

Quelle: `ocr_s089.md`, Zeile 27, zusätzlich zeichnungsgebunden
(`skizzen/s089_skizze_04.png`, Segment „letztes Faltensegment" mit Kennziffer
⑬, Beschriftung „½ FaI" über „FaT" am rechten Rand).

```text
Das Faltenteil nach dem letzten Faltensegment wieder mit einem halben
Falteninhalt = Faltentiefe (FaT) beenden → Falteninnennaht.
```

## 5. Randbedingung: vorhandene Stoffbreite (nur zeichnungsgebunden)

Quelle: ausschließlich `skizzen/s089_skizze_04.png` (Beschriftung unterhalb
der gesamten Faltenteil-Zeichnung); keine Textquelle in `ocr_s089.md`.

```text
Faltenteil 2×-p OSt
vorhandene Stoffbreite 92 cm
```

Hinweis: „92 cm" ist ein Zahlenwert mit erkennbarer Grenzwertfunktion für die
Gesamtbreite des zusammengesetzten Faltenteils (alle Faltensegmente inklusive
beider Halbsegmente). „2×-p OSt" ist eine Produktionskennzeichnung/Stückzahl
und wird hier nicht als Formel geführt (nur als Teil des Bildzitats
mitgeführt).

## Nicht als Formel erfasst

- Zeile 14 („Taschenbeutel an den Eingriff … anschneiden. Der Taschenbeutel
  kann auch separat zugeschnitten werden."): Konstruktionsanweisung ohne Zahl
  oder Rechenbeziehung.
- Zeile 15 („Vordere Teilungsnahthe formen."): keine Zahl.
- Zeile 16 („Abnaher in der Rückteilpasse zulegen … NZg und SaEs anzeichnen
  und markieren (hier nicht gezeigt)."): reine Bezeichner ohne Zahlenwert.
- Zeile 28 („Das Faltenteil mit Rückschnitten und Markierungen versehen."):
  keine Zahl.
- Zeile 30 („NZg, SaEs und Knipse zeichnen."): reine Bezeichner ohne
  Zahlenwert.
- Bildunterschriften „☐5 Produktionsschnitt Faltenteil" (Zeilen 34–36) und
  „Eingestellter Rock mit Faltenteil" (Zeile 38): Teile-/Themenbezeichnungen
  ohne eigenen Zahlenwert.
- Stückzahl-/Produktionskennzeichen „1× OSt" und „2×-p OSt" auf den
  Skizzenausschnitten: ausdrücklich ausgeschlossen laut Extraktionsregeln.
