# Formeln s213 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert` ([s213.md](s213.md)).
Kein einziger formel- oder coderelevanter Punkt ist bisher von Werner am
Original bestätigt. Diese Extraktion wurde auf ausdrücklichen Wunsch Werners
trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker aus der vorherigen
Prüfung übersprungen) und beruht auf [`ocr_s213.md`](ocr_s213.md) sowie den drei
Skizzenausschnitten unter [`skizzen/`](skizzen/). Sie ersetzt keine spätere
Bestätigung der formelrelevanten Stellen am Original und darf nicht als
menschlich verifiziert gelten.

`s213.md` vermerkte bislang „Diese Seite enthält keine Tabelle … und keine
Formel“. Dieser Befund wird hier revidiert: Die Seite enthält mehrere
zahlenbasierte geometrische Beziehungen (Anteile der Armloch-Vertiefung/
-Verbreiterung, ein Bruch-Widerspruch zwischen Fließtext und Zeichnung, eine
Streckenhalbierung und eine Bereichsangabe für den Knipsabstand).

Bekannte OCR-Lücke aus `s213.md`: Die Abschnittsnummern und die durchlaufende
Kreisnummerierung sind laut Werners eigener Bildlesung fehlerhaft (siehe
Prüfstellen 2–3 in `s213.md`). Die unten zitierten arabischen Schrittzahlen
(„1“, „2“, „3“ …) sind die Rohwerte aus `ocr_s213.md`, nicht bestätigt.

## 1. Ärmelkugelhöhe – Vertiefung an beiden Ärmelnähten

Quelle: `ocr_s213.md`, Zeilen 16–18 (Schrittfließtext, Schritt „1“ laut OCR).

```text
An beiden Ärmelnähten für eine höhere Ärmelkugel ½ Armloch-Vertiefung nach
unten abtragen, für ei- Vertiefung. Die neue ÄKLI (blau) zeichnen.
```

Hinweis: Der Satz bricht nach „für ei-“ ab und setzt mit „Vertiefung.“ fort –
zwischen beiden Fragmenten fehlt sichtbar mindestens ein Wort (vermutlich ein
Gegenstück zu „höhere“, z. B. eine andere Ärmelkugel-Variante mit einem
anderen Anteil). Fototreu als Lücke übernommen, nicht ergänzt.

## 2. Vordere Ärmelnaht – Verbreiterung auf der Achsellinie

Quelle: `ocr_s213.md`, Zeilen 19–20 (Schrittfließtext, Schritt „2“ laut OCR).

```text
Auf der neuen Achsellinie an der vorderen Ärmelnaht ½ Armloch-Verbreiterung
nach außen abtragen.
```

## 3. Hintere Ärmelnaht – volle Verbreiterung

Quelle: `ocr_s213.md`, Zeilen 21–22 (Schrittfließtext, Schritt „3“ laut OCR).

```text
An der hinteren Ärmelnaht die ganze Armloch-Verbreiterung abtragen.
```

## 4. Hintere Ärmelkugel – Anteil der Verbreiterung (Widerspruch Text/Zeichnung)

Quelle: `ocr_s213.md`, Zeilen 28–32 (Schrittfließtext, Schritt „5“ laut OCR);
zusätzlich zeichnungsgebunden durch [`skizzen/s213_skizze_01.png`](skizzen/s213_skizze_01.png)
(Bildunterschrift laut `skizzen_s213.json`: „☐3 Neue Ärmelkugel formen“).

```text
Am hinteren Ärmel die Kugel verbreitern. Dabei parallel zur Ärmelkurve ¼ der
Armlochverbreiterung nach außen zeichnen. Ärmelkugelnaht neu zeichnen und
dabei die ursprüngliche Form der Ärmelkugel übernehmen.
```

Zeichnungsgebundenes Label in `s213_skizze_01.png` (an derselben Stelle der
Kurve, neben Punktmarkierung „5“):

```text
1/6 Armloch-Verbreiterung
```

Hinweis: Fließtext („¼“) und Bildbeschriftung („⅙“) widersprechen sich an
genau dieser Stelle. Beide Lesarten fototreu nebeneinander erfasst, keine
still berichtigt.

## 5. Neuer hÄBr – Halbierung der Reststrecke zur hinteren Ärmelnaht

Quelle: `ocr_s213.md`, Zeilen 52–57 (Schrittfließtext, Schritte „12“–„14“ laut
OCR); zusätzlich zeichnungsgebunden durch
[`skizzen/s213_skizze_03.png`](skizzen/s213_skizze_03.png) (Bildunterschrift
laut `skizzen_s213.json`: „☐5 Neue Ärmelnähte, Ärmelmitte, Abnäher, Knipse“).

```text
12 Den Abstand zur Ärmelnaht messen und in den Ärmel übertragen (spiegeln).
Diesen Punkt auf der Achsellinie markieren.
13 Von dort die Hälfte der Strecke zur hinteren Ärmelnaht messen, markieren
und
14 parallel zum alten hÄBr den neuen hÄBr zeichnen.
```

Zeichnungsgebundenes Label in `s213_skizze_03.png` (auf der Achsellinie ÄkLi,
beidseitig des Punkts „12“, entlang der Linie „neuer hÄBr“):

```text
½ | ½
```

## 6. Knipsabstand an der vorderen Ärmelnaht

Quelle: `ocr_s213.md`, Zeile 63 (Schrittfließtext, Schritt „17“ laut OCR);
zusätzlich zeichnungsgebunden durch
[`skizzen/s213_skizze_03.png`](skizzen/s213_skizze_03.png) (dieselbe
Bildunterschrift wie Abschnitt 5).

```text
Neue Knipse an der vorderen Ärmelnaht markieren. Der Abstand sollte ca. 14
bis 16 cm sein.
```

Zeichnungsgebundenes Label in `s213_skizze_03.png`:

```text
Knips-Abstand ca. 14 bis 16 cm
```

## 7. Ärmelsaumweite – Auswahlregel über den Abnäher (qualitativ)

Quelle: `ocr_s213.md`, Zeile 67 (Fließtext nach Schritt „19“).

```text
Die Ärmelsaumweite kann am Abnäher reguliert werden. Soll z. B. die ÄSaW
größer werden, wird den Abnäher entsprechend kleiner gezeichnet (siehe Seite
211).
```

Hinweis: Keine Zahlenwerte auf dieser Seite; beschreibt nur eine gegenläufige
Auswahlbeziehung zwischen ÄSaW und Abnähergröße, mit Verweis auf Seite 211.

## Nicht als Formel erfasst

- Zeilen 36–39 („Am vorderen Armloch (VT) die Kurve von der oberen
  Seitennahzt zum vAP messen und vorne auf die neue vordere Ärmelkurve
  übertragen“): Maß wird 1:1 übertragen, keine Rechenbeziehung.
- Zeilen 46–51 (Ärmelnähte parallel zeichnen, neuer vÄBr parallel zur
  vorderen Ärmelnaht): reine Richtungsangaben ohne Zahlenwert.
- Zeilen 58–62 (Abnäher-Verschiebung, Saumverlauf): reine
  Konstruktionsanweisungen ohne Zahlenwert.
- Zeilen 64–66 (Abstände zu den Knipsen messen und auf die hintere Ärmelnaht
  übertragen): Maß wird 1:1 gespiegelt, keine eigene Rechenbeziehung.
- Zeile 68 (Verweis auf hÄP/SuP-Neubestimmung „siehe Seite 207“):
  Seitenverweis, keine eigene Formel dieser Seite.
