# Formeln s180 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s180.md](s180.md)). Kein einziger formel- oder coderelevanter Punkt ist bisher
von Werner am Original bestätigt. Diese Extraktion wurde auf ausdrücklichen
Wunsch Werners trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker
übersprungen) und beruht auf [`ocr_s180.md`](ocr_s180.md) sowie – für die
zeichnungsgebundene Formel unten – der Bildregion
[`skizzen/s180_skizze_01.png`](skizzen/s180_skizze_01.png) laut Beschreibung in
[`skizzen_s180.json`](skizzen_s180.json). Sie ersetzt keine spätere Bestätigung
der formelrelevanten Stellen am Original und darf nicht als menschlich
verifiziert gelten.

Diese Fassung ersetzt die frühere rein mechanische Regex-Ziehung (die nur die
Zeile mit „½ BrW" fand); sie ergänzt die dabei nicht erfassten Bruch- und
Bereichsangaben aus dem Schrittfließtext sowie die zeichnungsgebundene Formel
im Kontrollkasten.

Zusätzlich gilt die bekannte OCR-Lücke aus [s180.md](s180.md): Die fünf im Foto
eingekreisten Ziffern ⑩–⑭ wurden von der OCR als einzelne lateinische
Buchstaben „H", „H", „V", „B", „W" wiedergegeben. Die unten angegebene
Foto-Schrittzahl ist eine unbestätigte Zuordnung nach Reihenfolge (⑩=1. „H",
⑪=2. „H", ⑫=„V", ⑬=„B", ⑭=„W"), nicht aus eigener Bildprüfung.

## 1. Hintere Armlinie – Anteil ⅔ ArD+ ab P10

Quelle: `ocr_s180.md`, Zeile 17 (Schrittabsatz, Fotomarkierung „H", vermutlich
Foto-Schritt ⑪).

```text
Von P10 nach links ⅔ Armdurchmesser+ (ArD+) aus der Konstruktionstabelle ablesen und abtragen.
```

## 2. Vordere Armlinie – Anteil ⅓ ArD+ (Rest) ab P12

Quelle: `ocr_s180.md`, Zeile 25 (Schrittabsatz, Fotomarkierung „B", vermutlich
Foto-Schritt ⑬).

```text
Von P12 nach links ⅓ ArD+ (den restlichen ArD+) aus der Konstruktionstabelle abtragen.
```

Hinweis: Der Wortlaut „den restlichen ArD+" verknüpft diese Stelle mit
Abschnitt 1 (⅔ + ⅓ = ganzer ArD+); beide Abschnitte zusammen sind eine
Aufteilung derselben Größe ArD+ auf zwei Punkte (P10 und P12).

## 3. Zwischenraum RT/VT ab P11

Quelle: `ocr_s180.md`, Zeile 21 (Schrittabsatz, Fotomarkierung „V", vermutlich
Foto-Schritt ⑫).

```text
Von P11 nach links einen Zwischenraum zwischen RT und VT von ca. 7 bis 10 cm abtragen
```

## 4. Kontrolle der BrW

Quelle: `ocr_s180.md`, Zeile 35 (Fließtext unter der Überschrift „Kontrolle der
BrW:").

```text
Von P14 bis P12 die vBrW messen und von P11 bis P9 die hBrW messen. Die Summe der Messungen muss ½ BrW ergeben.
```

Zusätzlich, zeichnungsgebunden (nicht als eigener OCR-Textblock erkannt,
sondern nur über die Bildregion `img-0.jpeg` / `s180_skizze_01.png` belegt,
siehe [s180.md](s180.md), Abschnitt „Offene Punkte", und
[`skizzen_s180.json`](skizzen_s180.json)):

```text
vBrW + hBrW = ½ BrW
```

## Nicht als Formel erfasst

- Zeile 13 („... die Rückenbreite+ (RüB+) aus demr Konstruktionstabelle ablesen
  und abtragen."): reiner Tabellenwert ohne Bruch- oder Rechenbeziehung auf
  dieser Seite.
- Zeile 29 („... die Brustbreite+ (BrB+) aus der Konstruktionstabelle ablesen
  und abtragen."): reiner Tabellenwert ohne Bruch- oder Rechenbeziehung auf
  dieser Seite.
- Zeilen 15, 19, 23, 27, 31 (Pfeil-Anweisungen zu Linien zeichnen): geometrische
  Anweisungen ohne Zahl oder Rechenbeziehung.
- Bildunterschrift „☐4 Brustweite abtragen, Hilfslinien und vM zeichnen"
  (Zeile 39): reine Teile-/Zuordnungsbeschreibung ohne Zahlenwert.
