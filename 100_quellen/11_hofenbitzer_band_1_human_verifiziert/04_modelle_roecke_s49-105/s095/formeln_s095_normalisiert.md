# Formeln s095 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s095.md`](formeln_s095.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle Formeln stehen
deshalb auf `offen` oder `gesperrt`, unabhängig von der inhaltlichen Klarheit
der Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Futteransatznaht-Erhöhung oberhalb eines gefütterten Schlitzes

- **Quelle:** [`formeln_s095.md`](formeln_s095.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Das Futter wird unten am Schlitzeinschlag angenäht. Oberhalb eines
  gefütterten Schlitzes benötigt das Futter Mehrlänge. Die Futteransatznaht
  dort um ca. 0,5 bis 1 cm erhöhen.
  ```
- **Technische Formel:**
  ```text
  futteransatznaht_neu = futteransatznaht_alt + delta
  delta ∈ [ca. 0,5 cm, ca. 1 cm]
  ```
- **Eingaben und Einheiten:** `futteransatznaht_alt` (cm), Position der
  Futteransatznaht oberhalb eines gefütterten Schlitzes.
- **Ausgabe und Einheit:** `futteransatznaht_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „0,5 bis 1 cm"
  bleibt Bereich, kein fester Default gewählt. Gilt nur „oberhalb eines
  gefütterten Schlitzes" – Bedingung erhalten.
- **Abhängigkeiten:** [[Formel 5]] (Zeichnungsfassung derselben Stelle, siehe
  dort abweichender Wortlaut).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Textfassung nennt „ca.", die inhaltlich verwandte Zeichnungsfassung
    (Formel 5) nicht – ungeklärt, ob dies einen fachlichen Unterschied
    markiert oder nur eine Kürzung in der Zeichnungsbeschriftung ist.

## Formel 2 – Futteransatznaht-Verschiebung am RV-Schlitz an hM

- **Quelle:** [`formeln_s095.md`](formeln_s095.md), Abschnitt 2
- **Buchfassung:**
  ```text
  An der hM von Taillenbeleg und Futter verschiebt man die Futteransatznaht am
  RV-Schlitz um ca. 0,5 cm nach innen, weil das Futter neben den an der hM
  befindlichen Zähnchen auf das RV-Band genäht wird (siehe Seite 59).
  ```
- **Technische Formel:**
  ```text
  position_naht_neu = position_naht_alt - ca. 0,5 cm  (Richtung: nach innen)
  ```
- **Eingaben und Einheiten:** `position_naht_alt` (cm), Position der
  Futteransatznaht am RV-Schlitz an hM.
- **Ausgabe und Einheit:** `position_naht_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` erhalten;
  Richtung „nach innen" laut Buch, Bezugsachse nicht spezifiziert. Begründung
  im Buch (Zähnchen an hM, RV-Band) als Kontext, nicht als eigene Formel
  geführt.
- **Abhängigkeiten:** Querverweis „siehe Seite 59" – andere Buchseite, hier
  nur verlinkt, nicht kopiert oder nachgerechnet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Bezugsrichtung „nach innen" nicht geometrisch präzisiert (bezogen worauf).

## Formel 3 – Nahtzugabe an der Futteransatznaht am RV-Schlitz

- **Quelle:** [`formeln_s095.md`](formeln_s095.md), Abschnitt 3
- **Buchfassung:**
  ```text
  An die Futteransatznaht am RV-Schlitz kommt eine NZg von 1 cm.
  ```
- **Technische Formel:**
  ```text
  nzg_futteransatznaht_rv_schlitz = 1 cm
  ```
- **Eingaben und Einheiten:** keine (fester Wert).
- **Ausgabe und Einheit:** `nzg_futteransatznaht_rv_schlitz` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert „1 cm" ohne
  `ca.` – kein Spielraum laut Buchwortlaut.
- **Abhängigkeiten:** gleiche Stelle wie [[Formel 2]] (Futteransatznaht am
  RV-Schlitz), keine direkte Rechenabhängigkeit.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 4 – RV-Schlitz-Verlängerung an hM

- **Quelle:** [`formeln_s095.md`](formeln_s095.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Den RV-Schlitz an hM um ca. 2 bis 3 cm verlängern und die NZg zwischen
  RV-Ende und Futterschlitzende schräg beschneiden.
  ```
- **Technische Formel:**
  ```text
  laenge_rv_schlitz_neu = laenge_rv_schlitz_alt + delta
  delta ∈ [ca. 2 cm, ca. 3 cm]
  ```
- **Eingaben und Einheiten:** `laenge_rv_schlitz_alt` (cm), Länge des
  RV-Schlitzes an hM.
- **Ausgabe und Einheit:** `laenge_rv_schlitz_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „2 bis 3 cm"
  bleibt Bereich, kein fester Default gewählt. Zusatzoperation „NZg …schräg
  beschneiden" ist eine Handlungsanweisung ohne eigenen Zahlenwert, hier nicht
  separat quantifiziert.
- **Abhängigkeiten:** [[Formel 6]] (Zeichnungsfassung, gleicher Wertebereich
  „ca. 2 bis 3 cm", aber andere Naht (SN statt hM) und andere Operation
  (Verschieben statt Verlängern) – nicht gleichgesetzt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 5 – Futternaht-Verlängerung oberhalb eines Schlitzes (Zeichnung)

- **Quelle:** [`formeln_s095.md`](formeln_s095.md), Abschnitt 5,
  zeichnungsgebunden (`skizzen/s095_skizze_01.png`)
- **Buchfassung:**
  ```text
  Die Futternaht oberhalb eines Schlitzes um 0,5 bis 1 cm verlängern
  ```
- **Technische Formel:**
  ```text
  futternaht_neu = futternaht_alt + delta
  delta ∈ [0,5 cm, 1 cm]
  ```
- **Eingaben und Einheiten:** `futternaht_alt` (cm), Position der Futternaht
  oberhalb eines Schlitzes.
- **Ausgabe und Einheit:** `futternaht_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „0,5 bis 1 cm"
  bleibt Bereich; anders als bei [[Formel 1]] steht in der Zeichnung kein
  `ca.` vor dem Bereich – als Abweichung dokumentiert, nicht vereinheitlicht.
- **Abhängigkeiten:** [[Formel 1]] (Textfassung derselben Stelle).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Verhältnis zu Formel 1 (gleiche Stelle, abweichender Wortlaut und Fehlen
    von „ca.") am Original zu klären.

## Formel 6 – Schlitzende für den RV: Verschiebung an der SN (Zeichnung)

- **Quelle:** [`formeln_s095.md`](formeln_s095.md), Abschnitt 6,
  zeichnungsgebunden (`skizzen/s095_skizze_01.png`)
- **Buchfassung:**
  ```text
  Das Schlitzende für den RV an der SN um ca. 2 bis 3 cm nach unten
  verschieben
  ```
- **Technische Formel:**
  ```text
  position_schlitzende_rv_sn_neu = position_schlitzende_rv_sn_alt - delta
  delta ∈ [ca. 2 cm, ca. 3 cm]  (Richtung: nach unten)
  ```
- **Eingaben und Einheiten:** `position_schlitzende_rv_sn_alt` (cm), Position
  des Schlitzendes für den RV an der SN.
- **Ausgabe und Einheit:** `position_schlitzende_rv_sn_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „ca. 2 bis 3
  cm" bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel 4]] (Textfassung, gleicher Wertebereich, andere
  Naht und Operation – nicht gleichgesetzt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Verhältnis zu Formel 4 (gleicher Zahlenbereich, andere Naht/Richtung) am
    Original zu klären – möglicherweise zwei unabhängige Maßnahmen an
    unterschiedlichen Nähten, nicht ermittelt.

## Formel 7 – Saum-/Zugabebereich an VT-Futter und RT-Futter (Zeichnung, unbeschriftet)

- **Quelle:** [`formeln_s095.md`](formeln_s095.md), Abschnitt 7,
  zeichnungsgebunden (`skizzen/s095_skizze_01.png`)
- **Buchfassung:**
  ```text
  2 bis 4 cm
  1 bis 4 cm
  ```
- **Technische Formel:** nicht ableitbar ohne Beschriftung – kein Bezug
  (Saum? Zugabe? welche Kante?) im Ausschnitt erkennbar. Keine Formel erzeugt,
  um keine Fachregel zu erfinden.
- **Eingaben und Einheiten:** unbekannt.
- **Ausgabe und Einheit:** unbekannt.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** zwei Bereiche „2 bis 4
  cm" und „1 bis 4 cm", identisch auf VT-Futter und RT-Futter, ohne erkennbare
  Bedingung.
- **Abhängigkeiten:** keine ermittelt.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Bedeutung der beiden Maßlinien (welche Linie ist Saum, welche Zugabe o. Ä.)
    ist aus dem Bildausschnitt nicht ablesbar; ohne Beschriftung oder
    Werners Auskunft am Original nicht zu klären.
