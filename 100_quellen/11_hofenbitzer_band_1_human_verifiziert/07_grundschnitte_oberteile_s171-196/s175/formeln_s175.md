# Formeln s175 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s175.md](s175.md)). Kein einziger formel- oder coderelevanter Punkt ist bisher
von Werner am Original bestätigt (siehe dort Prüfstellen 3 und 4). Diese
Extraktion wurde auf ausdrücklichen Wunsch Werners trotzdem als
Walking-Skeleton-Durchlauf erstellt (Blocker übersprungen) und beruht auf
[`ocr_s175.md`](ocr_s175.md) sowie, für die drei Balance-Maßboxen, auf den
vorläufigen KI-Ablesungen in [`skizzen_s175.json`](skizzen_s175.json). Sie
ersetzt keine spätere Bestätigung der formelrelevanten Stellen am Original und
darf nicht als menschlich verifiziert gelten.

Zwei Quellenarten werden unterschieden:

- **Text-Quelle:** Rechenbeziehung steht wörtlich im OCR-Fließtext (`ocr_s175.md`).
- **Zeichnungsgebundene Quelle:** Rechenbeziehung steht nur in einer Maßbox der
  Zeichnung und wurde von der KI aus dem Bildausschnitt abgelesen, nicht von der
  OCR-Engine als Text erkannt (siehe Warnhinweis in `skizzen_s175.json`).

## 1. Balance-Kontrollschema – Figur 1, runder Rücken (☐4a)

Quelle: zeichnungsgebunden, `skizzen_s175.json`, Eintrag `skizzen/s175_skizze_01.png`
(Bildunterschrift laut `ocr_s175.md` Zeile 12: „☐4a Figur mit rundem Rücken").

```text
Balance muss korrekt sein! hier 4 cm
VL für Konstruktion 46
RüL für Konstruktion 42
± vorderer Korrekturwert 0
± hinterer Korrekturwert -1,5
VL bei waagerechtem Taillenband 46
RüL bei waagerechtem Taillenband 43,5
3 Balance korrekt?
VL aus Maßtabelle 46
RüL aus Maßtabelle 43,5
Balance ist nicht korrekt hier 3 cm
Vorderlänge ist ok.
Rückenlänge ist bei rundem Rücken um 1,5 cm zu lang. Sie wird für die
Konstruktion um 1,5 cm gekürzt.
```

Hinweis: „3 Balance korrekt?" ist im abgelesenen Text isoliert; ob die „3" eine
Schrittnummer innerhalb der Maßbox oder Teil eines anderen Labels ist, ist aus
der Ablesung nicht sicher erkennbar.

## 2. Balance-Kontrollschema – Figur 2, gerader Rücken (☐5a)

Quelle: zeichnungsgebunden, `skizzen_s175.json`, Eintrag `skizzen/s175_skizze_02.png`
(Bildunterschrift laut `ocr_s175.md` Zeile 14: „☐5a Figur mit geradem Rücken").

```text
Balance muss korrekt sein! hier 4 cm
VL für Konstruktion 46
RüL für Konstruktion 42
± vorderer Korrekturwert 0
± hinterer Korrekturwert +1
VL bei waagerechtem Taillenband 46
RüL bei waagerechtem Taillenband 41
3 Balance korrekt?
VL aus Maßtabelle 46
RüL aus Maßtabelle 41
Balance ist nicht korrekt hier 5 cm
Vorderlänge ist ok.
Rückenlänge ist bei geraden, flachen Rücken um 1 cm zu kurz. Sie wird für die
Konstruktion um 1 cm vergrößert.
```

## 3. Balance-Kontrollschema – Figur 3, extrem runder Rücken/Skoliose (☐6a)

Quelle: zeichnungsgebunden, `skizzen_s175.json`, Eintrag `skizzen/s175_skizze_03.png`
(Bildunterschrift laut `ocr_s175.md` Zeile 16: „☐6a Figur mit extrem rundem
Rücken und eingefallener Brust (Buckel, Skollose)" – OCR-Schreibweise
„Skollose" unverändert übernommen, siehe [s175.md](s175.md) Prüfstelle 2).

```text
Balance muss korrekt sein! hier 4 cm
VL für Konstruktion 46
RüL für Konstruktion 42
± vorderer Korrekturwert +1,5
± hinterer Korrekturwert -2,5
VL bei waagerechtem Taillenband 44,5
RüL bei waagerechtem Taillenband 44,5
3 Balance korrekt?
VL aus Maßtabelle 44,5
RüL aus Maßtabelle 44,5
Balance ist nicht korrekt hier 0 cm
Vorderlänge ist bei eingefallener Brust um 1,5 cm zu kurz. Sie wird für die
Konstruktion um 1,5 cm vergrößert.
Rückenlänge ist bei rundem Rücken um 2,5 cm zu lang. Sie wird für die
Konstruktion um 2,5 cm gekürzt.
```

## 4. Schnittkorrektur Rückenteil – runder Rücken (☐4b)

Quelle: Text, `ocr_s175.md` Zeile 24–25; ergänzend zeichnungsgebunden,
`skizzen_s175.json`, Eintrag `skizzen/s175_skizze_04.png`.

```text
☐4b Optimierung für runden Rücken:
Für die Konstruktion wurde die RüL um 1,5 cm gekürzt. Diese Kürzung um 1,5 cm
wird nun an der Konstruktion wieder ergänzt. Der Schulterabnäher wird größer.
```

Zeichnungslabels (Skizze 04, unbestätigte KI-Ablesung): „1,5 cm",
„gemessene RüL = 43,5 cm", Teilebezeichnung „RT", Punktbezeichnung „hÄP".

## 5. Schnittkorrektur Rückenteil – gerader Rücken (☐5b)

Quelle: Text, `ocr_s175.md` Zeile 35–36; ergänzend zeichnungsgebunden,
`skizzen_s175.json`, Eintrag `skizzen/s175_skizze_06.png`.

```text
☐5b Optimierung für runden Rücken:
Für die Konstruktion wurde die RüL um 1 cm verlängert. Diese Verlängerung um
1 cm wird nun an der Konstruktion wieder reduziert. Der Schulterabnäher wird
kleiner.
```

Hinweis: Die Bildunterschrift beginnt in der OCR ebenfalls mit „Optimierung für
runden Rücken" (nicht „geraden Rücken"), obwohl sie zur Figur mit geradem
Rücken (☐5a) gehört; unverändert übernommen, nicht still korrigiert.

Zeichnungslabels (Skizze 06, unbestätigte KI-Ablesung): „1 cm",
„gemessene RüL = 41 cm", Teilebezeichnung „RT", Punktbezeichnung "hÄP".

## 6. Schnittkorrektur Vorder- und Rückenteil – Skoliose (☐6b)

Quelle: Text, `ocr_s175.md` Zeile 48–49; ergänzend zeichnungsgebunden,
`skizzen_s175.json`, Eintrag `skizzen/s175_skizze_05.png`.

```text
☐6b Optimierung für die Skollose:
Für die Konstruktion wurde die VL um 1,5 cm verlängert, die RüL um 2,5 cm
gekürzt. Diese VL-Verlängerung um 1,5 cm wird nun an der Konstruktion wieder
reduziert und die RüL-Kürzung um 2,5 cm wieder verlängert. Der Brustabnäher
wird kleiner, der Schulterabnäher wird größer.
```

Zeichnungslabels (Skizze 05, unbestätigte KI-Ablesung): „gemessene VL -1 cm =
44,5 cm", „1,5 cm", Punktbezeichnung „vÄP", Punktbezeichnung „BrP",
Teilebezeichnung „VT", „1 cm", „2 cm", „2,5 cm", Punktbezeichnung „hÄP",
„gemessene RüL = 44,5 cm", Teilebezeichnung „RT". Die doppelten Maßangaben
(1 cm/2 cm sowie 1,5 cm/2,5 cm) sind in der Ablesung nicht eindeutig einer
einzelnen Rechenbeziehung zugeordnet – siehe [s175.md](s175.md) Prüfstelle 4.

## Nicht als Formel erfasst

- Zeile 27 („... muss nach der Ursache geforscht werden. ... Maße ggf. noch
  einmal zum exakt waagerecht liegenden Taillenband nachgewiesen."): keine
  Zahl, keine eigene Rechenbeziehung; betrifft die Prüfmethode, nicht einen
  Rechenwert. OCR-Wort „nachgewiesen" laut [s175.md](s175.md) am Original als
  „nachgemessen" zu prüfen.
- Zeile 31 (☐7, „Das Balance-Problem wird errechnet..."): allgemeine
  Verfahrensbeschreibung ohne Zahl.
- Zeile 33 (☐2a, „... die zu lange VL so weit gekürzt dass die Balance ...
  stimmt."): allgemeines Beispiel ohne Zahlenwert.
- Zeile 40–42 (☐1b, „Mit den normalisierten ... Balancemaßen ... wird nun der
  Grundschnitt konstruiert." sowie der Hinweis auf das gleiche Grundgerüst für
  alle drei Figuren): keine eigene Rechenbeziehung, nur Kontext für die
  Balance-Kontrollschemata oben.
- Zeile 46 (☐5, „Der auf diese Weise konstruierte Grundschnitt ist ... noch
  nicht passend."): allgemeine Überleitung ohne Zahl.
- Zeile 51–53 (Schlussabsatz „Dort, wo zuvor ein Balancemaß gekürzt wurde ...";
  „Nur durch diese Anpassungen ..."): zusammenfassender Text ohne eigenen
  Zahlenwert, beschreibt nur das bereits in Abschnitt 4–6 erfasste Prinzip.
