# Formeln s187 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s187.md](s187.md)). Kein einziger formel- oder coderelevanter Punkt ist bisher
von Werner am Original bestätigt. Diese Extraktion wurde auf ausdrücklichen
Wunsch Werners trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker
übersprungen) und beruht auf [`ocr_s187.md`](ocr_s187.md) sowie den in
[`skizzen_s187.json`](skizzen_s187.json) festgehaltenen Skizzenbeschreibungen.
Sie ersetzt keine spätere Bestätigung der formelrelevanten Stellen am Original
und darf nicht als menschlich verifiziert gelten.

`s187.md` vermerkte bislang: „Der Fließtext enthält auch keine eigenständigen
Formelzeilen mit Rechenzeichen zwischen Ziffern; es gibt daher keine
`formeln_s187.md`." Dieser Befund wird hier revidiert: Fünf zahlenbasierte
Rechenbeziehungen wurden gefunden – drei im OCR-Fließtext, zwei weitere nur in
den Skizzenbeschreibungen aus `skizzen_s187.json` (zeichnungsgebunden, dort als
wörtliches Zitat aus der Bildregion festgehalten, hier nicht eigenständig am
Original nachgeprüft).

## 1. Abnäherspitzen kürzen

Quelle: `ocr_s187.md`, Zeile 21–22 (Fließtext, Bildunterschrift ☐2).

```text
☐2 Brust-, Taillen- und Schulterabnäher um 2 cm an der Spitze kürzen und
separat nähen.
```

Zeichnungsgebundene Bestätigung (nicht eigenständig am Bild nachgeprüft, aus
`skizzen_s187.json`, Skizze 02 und Skizze 03):

```text
2 cm kürzen (zweimal, grün)
```

Hinweis: „Den Brustpunkt zur Kontrolle ggf. mit einem Bohrloch markieren"
(Zeile 22–23, direkt anschließend) ist eine Konstruktionsanweisung ohne eigenen
Zahlenwert, hier nicht als eigene Formel geführt.

## 2. Saumeinschlag-Breite

Quelle: `ocr_s187.md`, Zeile 39–40 (Fließtext).

```text
Saumeinschläge werden zwischen 2 cm und 4 cm Breite angezeichnet.
```

Zeichnungsgebundene Bestätigung (nicht eigenständig am Bild nachgeprüft, aus
`skizzen_s187.json`, Skizzen 02–05, jeweils unten):

```text
2 bis 4 cm
```

## 3. Ausstellen an den Nähten bei langen Oberteil-Grundschnitten

Quelle: `ocr_s187.md`, Zeile 59–60 und Zeile 67–68. Der Satz ist im OCR-Rohtext
durch Bild und Bildunterschrift (☐3, Zeile 62–65) unterbrochen – Leseordnung
folgt dem physischen Seitenlayout, kein Informationsverlust.

```text
Lange Oberteil-Grundschnitte können an allen Nähten (außer an der hM-Naht) bis
zu 1 cm ausgestellt werden. Dadurch wird der Fall etwas besser.
```

## 4. Vorderer Einschlag für die Übertrittseite

Quelle: `ocr_s187.md`, Zeile 29–30 (Fließtext, nennt den Einschlag ohne
Zahlenwert).

```text
Das VT wird bei der Anprobe an der vM zugesteckt und daher mit einem Einschlag
für die Übertrittseite versehen.
```

Zeichnungsgebundener Zahlenwert (nicht eigenständig am Bild nachgeprüft, aus
`skizzen_s187.json`, Skizze 02):

```text
vorderer Einschlag ca. 2 cm bis 4 cm
```

Hinweis: Dies ist eine andere Stelle als der Saumeinschlag in Abschnitt 2,
auch wenn derselbe Zahlenbereich „2 bis 4 cm" verwendet wird – laut
Skizzenbeschreibung liegen beide Angaben getrennt nebeneinander in Skizze 02
(„vorderer Einschlag ca. 2 cm bis 4 cm" und separat „unten 2 bis 4 cm").

## 5. Kontrollmaß Brustbreite

Quelle: nur zeichnungsgebunden, `skizzen_s187.json`, Skizze 04 (nicht im
OCR-Fließtext enthalten, nicht eigenständig am Bild nachgeprüft).

```text
Kontrolle = ½ oBrB
```

Hinweis: Abkürzung „oBrB" auf dieser Seite nicht aufgelöst; keine Vermutung
ergänzt.

## Nicht als Formel erfasst

- „me +" (Skizze 04, laut `skizzen_s187.json`): unklare, möglicherweise
  abgeschnittene Notation ohne erkennbare Rechenbeziehung; hier nicht als
  Formel geführt, aber als offene Stelle vermerkt.
- „1,5 cm" (Skizze 04, laut `skizzen_s187.json`): isolierter Maßwert ohne im
  Beschreibungstext genannte Rechen- oder Auswahlbeziehung.
- Nahtzugaben „2 cm", „1 cm" (Skizzen 02–05, laut `skizzen_s187.json`):
  isolierte Nahtzugabenwerte ohne Rechenbeziehung.
- Seitenverweise „Seite 376 ff" (zweimal, Zeile 47 und 57/72–73) und „Seite
  388 ff" (Zeile 51): reine Querverweise, keine Formeln.
- Labels vM, hM, SN, BrP, vAP, hAP: Punktbezeichnungen ohne eigenen
  Zahlenwert oder Rechenbeziehung.
