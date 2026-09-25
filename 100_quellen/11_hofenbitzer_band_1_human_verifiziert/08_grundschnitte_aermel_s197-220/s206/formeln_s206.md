# Formeln s206 – fototreue Extraktion (noch nicht menschlich verifiziert)

**Status: Walking Skeleton – OCR-/Eigenlesung, noch nicht von Werner bestätigt.**

Seite 206 gehört zu `08_grundschnitte_aermel_s197-220/`, einer Kategorie, für
die der Formelextraktions-Prompt laut `AGENT.md` nicht ausdrücklich benannt
ist (dort nur `03_grundschnitte_roecke_s32-48/`, `04_modelle_roecke_s49-105/`,
`07_grundschnitte_oberteile_s171-196/`). Diese Datei entsteht auf Werners
ausdrücklichen Wunsch als Walking Skeleton ("mach es bitte #"), obwohl weder
die Kategorie-Zuordnung noch die einzelnen Stellen bereits am Original
bestätigt sind. Alle Angaben unten sind entsprechend vorläufig.

`s206.md`, Prüfstelle 5, hatte ursprünglich vermerkt, die Seite enthalte keine
eigene Formel. Bei genauerem Abgleich mit der Definition dieses Prompts
(Bereiche, Grenzwerte, Bedingungen, geometrische Beziehungen) enthält der
Fließtext jedoch mehrere quantifizierte Konstruktionsangaben. Diese werden
hier erfasst; rein narrative Konstruktionsschritte ohne Zahlenbezug (z. B.
"von P10 parallel … zeichnen", "Ärmelflächen kopieren und spiegeln") bleiben
außen vor.

## 1. Saum-Konstruktion (Schritt ⑬ laut s206.md, OCR-Ziffer "16", ☐6)

Quelle: [`ocr_s206.md`](ocr_s206.md), Zeile 24.

```text
An der Saumlinie 2 bis 3 cm hochmessen und 1/2 ÄSaW zur Saumlinie abtragen → Saum.
```

Hinweis: Im OCR-Rohtext steht statt „ÄSaW" die Zeichenfolge „A5aW" (Zeile 24
in `ocr_s206.md`, unverändert stehen gelassen). Die Lesung „ÄSaW" folgt der
eigenen, noch nicht von Werner bestätigten Lesung in `s206.md` unter
„Bekannte auffällige Stellen im Rohtext".

Zusätzliches, zeichnungsgebundenes Rechenbeispiel (`geprueft: false` laut
[`skizzen_s206.json`](skizzen_s206.json), skizze_01, Label ☐6):

```text
1/2 ÄsW 13 cm
```

Offen: Ob „ÄSaW" (Fließtext) und „ÄsW" (Skizzenbeschreibung) dieselbe
Abkürzung meinen und wofür sie steht, ist nicht belegt.

Zusätzliche, nicht quantifizierte Auswahlregel im selben Abschnitt (Zeile 36,
Abschnitt „7"):

```text
Die ÄSaW kann/sollte bei unelastischen Materialien hierbei etwas größer ausfallen.
```

(OCR-Rohtext Zeile 36: „Die A5aW kann/sollte bei unelastischen Materialien
hierbei etwas großer ausfallen.")

## 2. Ellenbogen-Einstellung hinten (Schritt ⑭ laut s206.md, ohne Ziffer im Rohtext)

Quelle: [`ocr_s206.md`](ocr_s206.md), Zeile 25.

```text
An der Ellenbogenlinie hinten (rechts) 0,5 bis 1 cm einstellen. Von P8 über die Einstellung weiter zum Saum zeichnen → hinterer Ärmelbruch.
```

Zeichnungsgebundener Beleg (`geprueft: false` laut `skizzen_s206.json`,
skizze_01, Label ☐6): Maßangabe „0,5 bis 1 cm" in der Bildbeschreibung.

## 3. Ärmelnaht-Einstellung ohne Abnäher – Grenzwert (Schritt ⑱ laut s206.md, ohne Ziffer im Rohtext)

Quelle: [`ocr_s206.md`](ocr_s206.md), Zeile 37.

```text
An beiden Ärmelnähten maximal 4 cm einstellen.
```

(OCR-Rohtext Zeile 37: „An beiden Armelnähten maximal 4 cm einstellen.")

Zeichnungsgebundener Beleg (`geprueft: false` laut `skizzen_s206.json`,
skizze_04, Label ☐9): Maßangabe „max. 4 cm beidseitig".

## 4. Nahtlängen-Ausgleich (Schritt ⑳ laut s206.md, ohne Ziffer im Rohtext)

Quelle: [`ocr_s206.md`](ocr_s206.md), Zeile 39.

```text
Die längere (hintere) Ärmelnaht messen und auf die kürzere (vordere) Ärmelnaht übertragen.
```

(OCR-Rohtext Zeile 39: „Die langere (hintere) Ärmelnaht messen und auf die
kürzere (vordere) Ärmelnaht übertragen.")

## Nicht erfasst

- Reine Konstruktionsanweisungen ohne Zahlen- oder Grenzwertbezug (z. B.
  Zeile 26, 32, 38, 40 in `ocr_s206.md`).
- Die Kästchen-, Punkt- und Schrittnummerierungen selbst (☐6–☐9, P8, P10 usw.)
  sind Bezeichner, keine Formeln.

## Offene Prüfung

Keine der obigen Stellen ist am Original bestätigt. Vor jeder Normalisierung
über den Walking-Skeleton-Stand hinaus müssen sie wie in `s206.md`,
Prüfstellen 2–4, von Werner geprüft werden – insbesondere die Lesung „ÄSaW"
gegenüber dem OCR-Rohtext „A5aW" und gegenüber „ÄsW" in der Skizzenbeschreibung.
