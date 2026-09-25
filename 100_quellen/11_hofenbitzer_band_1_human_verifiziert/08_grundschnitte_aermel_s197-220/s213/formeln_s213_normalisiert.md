# Formeln s213 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s213.md`](formeln_s213.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle sieben Formeln
stehen deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Ärmelkugelhöhe: Vertiefung an beiden Ärmelnähten

- **Quelle:** [`formeln_s213.md`](formeln_s213.md), Abschnitt 1
- **Buchfassung:**
  ```text
  An beiden Ärmelnähten für eine höhere Ärmelkugel ½ Armloch-Vertiefung nach
  unten abtragen, für ei- Vertiefung. Die neue ÄKLI (blau) zeichnen.
  ```
- **Technische Formel:**
  ```text
  naht_punkt_neu = naht_punkt_alt - 0,5 * armloch_vertiefung   (Richtung: nach unten)
  ```
- **Eingaben und Einheiten:** `armloch_vertiefung` (cm), auf einer Vorseite
  ermittelte Armloch-Vertiefung; `naht_punkt_alt` (cm) an beiden Ärmelnähten.
- **Ausgabe und Einheit:** `naht_punkt_neu` (cm), neuer Ärmelkugel-Ansatzpunkt;
  daraus die neue ÄkLi.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Faktor `½` gilt laut
  Buchtext „für eine höhere Ärmelkugel“. Der zweite Halbsatz („für ei-
  Vertiefung“) bricht ab – ob es eine zweite Variante mit anderem Faktor
  (z. B. für eine niedrigere Ärmelkugel) gibt, ist aus dem Wortlaut nicht
  ablesbar.
- **Abhängigkeiten:** `armloch_vertiefung` stammt von einer anderen,
  namentlich nicht genannten Seite (Ergebnis der vorangegangenen
  Armloch-Vertiefung); nur zu verlinken, sobald die Quellseite ermittelt ist.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Satzlücke „für ei- Vertiefung“ – mindestens ein Wort fehlt in der OCR;
    am Original zu klären, ob eine zweite Faktor-Variante gemeint ist.

## Formel 2 – Vordere Ärmelnaht: Verbreiterung auf der Achsellinie

- **Quelle:** [`formeln_s213.md`](formeln_s213.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Auf der neuen Achsellinie an der vorderen Ärmelnaht ½ Armloch-Verbreiterung
  nach außen abtragen.
  ```
- **Technische Formel:**
  ```text
  naht_punkt_neu = naht_punkt_alt + 0,5 * armloch_verbreiterung   (Richtung: nach außen)
  ```
- **Eingaben und Einheiten:** `armloch_verbreiterung` (cm), auf einer Vorseite
  ermittelte Armloch-Verbreiterung; `naht_punkt_alt` (cm) an der vorderen
  Ärmelnaht, auf der neuen Achsellinie.
- **Ausgabe und Einheit:** `naht_punkt_neu` (cm), neuer Punkt auf der
  Achsellinie an der vorderen Ärmelnaht.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Fester Faktor `½`, kein
  `ca.` im Buchtext.
- **Abhängigkeiten:** `armloch_verbreiterung` von einer anderen, namentlich
  nicht genannten Seite; [[Formel 3 – Hintere Ärmelnaht]] verwendet dieselbe
  Größe mit Faktor 1.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 3 – Hintere Ärmelnaht: volle Verbreiterung

- **Quelle:** [`formeln_s213.md`](formeln_s213.md), Abschnitt 3
- **Buchfassung:**
  ```text
  An der hinteren Ärmelnaht die ganze Armloch-Verbreiterung abtragen.
  ```
- **Technische Formel:**
  ```text
  naht_punkt_neu = naht_punkt_alt + 1 * armloch_verbreiterung   (Richtung: nach außen, implizit)
  ```
- **Eingaben und Einheiten:** `armloch_verbreiterung` (cm); `naht_punkt_alt`
  (cm) an der hinteren Ärmelnaht.
- **Ausgabe und Einheit:** `naht_punkt_neu` (cm), neuer Punkt an der hinteren
  Ärmelnaht.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Fester Faktor `1`
  („die ganze“), kein `ca.`. Richtung „nach außen“ nicht explizit im
  Buchsatz genannt, aber aus dem Kontext (Verbreiterung) naheliegend – nicht
  als bestätigt geführt.
- **Abhängigkeiten:** [[Formel 2 – Vordere Ärmelnaht]] (gleiche Ausgangsgröße
  `armloch_verbreiterung`, anderer Faktor).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Richtung „nach außen“ nur erschlossen, nicht wörtlich belegt.

## Formel 4 – Hintere Ärmelkugel: Anteil der Verbreiterung (Widerspruch)

- **Quelle:** [`formeln_s213.md`](formeln_s213.md), Abschnitt 4
- **Buchfassung (Fließtext):**
  ```text
  Am hinteren Ärmel die Kugel verbreitern. Dabei parallel zur Ärmelkurve ¼
  der Armlochverbreiterung nach außen zeichnen.
  ```
- **Buchfassung (Zeichnung, `s213_skizze_01.png`):**
  ```text
  1/6 Armloch-Verbreiterung
  ```
- **Technische Formel:**
  ```text
  # Faktor je nach Quelle unterschiedlich:
  versatz_kurve = 0,25 * armlochverbreiterung   # laut Fließtext (¼)
  versatz_kurve = (1/6) * armlochverbreiterung  # laut Zeichnungslabel (⅙)
  ```
- **Eingaben und Einheiten:** `armlochverbreiterung` (cm); Bezug: Kurve
  parallel zur (neuen) Ärmelkurve am hinteren Ärmel.
- **Ausgabe und Einheit:** `versatz_kurve` (cm), Abstand der neuen parallelen
  Kurve zur ursprünglichen Ärmelkurve.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Kein Bereich, sondern
  ein fester Bruch – aber mit zwei widersprüchlichen Werten aus derselben
  Seite. Keiner der beiden Werte wird hier als richtig ausgewählt.
- **Abhängigkeiten:** dieselbe `armlochverbreiterung` wie in
  [[Formel 2 – Vordere Ärmelnaht]] / [[Formel 3 – Hintere Ärmelnaht]]
  vermutet, aber nicht am Original bestätigt, ob es sich um denselben Wert
  handelt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Fließtext („¼“) und Zeichnungslabel („⅙“) widersprechen sich unmittelbar;
    welcher Wert im Original tatsächlich gedruckt/gezeichnet ist, muss Werner
    klären.

## Formel 5 – Neuer hÄBr: Halbierung der Reststrecke

- **Quelle:** [`formeln_s213.md`](formeln_s213.md), Abschnitt 5
- **Buchfassung:**
  ```text
  Den Abstand zur Ärmelnaht messen und in den Ärmel übertragen (spiegeln).
  Diesen Punkt auf der Achsellinie markieren. Von dort die Hälfte der Strecke
  zur hinteren Ärmelnaht messen, markieren und parallel zum alten hÄBr den
  neuen hÄBr zeichnen.
  ```
- **Buchfassung (Zeichnung, `s213_skizze_03.png`):**
  ```text
  ½ | ½
  ```
- **Technische Formel:**
  ```text
  punkt_gespiegelt = spiegel(abstand_vorderer_äbr, achse)
  punkt_neuer_häbr = punkt_gespiegelt + 0,5 * (punkt_hintere_naht - punkt_gespiegelt)
  ```
- **Eingaben und Einheiten:** `abstand_vorderer_äbr` (cm, aus Punkt 11
  abgeleitet); `punkt_hintere_naht` (Position der hinteren Ärmelnaht auf der
  Achsellinie).
- **Ausgabe und Einheit:** `punkt_neuer_häbr` (cm-Position auf der
  Achsellinie), Ausgangspunkt für den neuen hÄBr (parallel zum alten hÄBr).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Faktor `½` fest, kein
  `ca.`. Zeichnungslabel bestätigt die Halbierung, ohne einen abweichenden
  Wert zu zeigen (kein Widerspruch wie bei Formel 4).
- **Abhängigkeiten:** [[Formel 4 – Hintere Ärmelkugel]] bzw. Punkt 11
  („neuer vÄBr“) liefert `abstand_vorderer_äbr`; nicht auf dieser Seite
  selbst berechnet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 6 – Knipsabstand an der vorderen Ärmelnaht

- **Quelle:** [`formeln_s213.md`](formeln_s213.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Neue Knipse an der vorderen Ärmelnaht markieren. Der Abstand sollte ca. 14
  bis 16 cm sein.
  ```
- **Buchfassung (Zeichnung, `s213_skizze_03.png`):**
  ```text
  Knips-Abstand ca. 14 bis 16 cm
  ```
- **Technische Formel:**
  ```text
  knips_abstand ∈ [ca. 14 cm, ca. 16 cm]
  ```
- **Eingaben und Einheiten:** keine Berechnungseingabe, reiner Bereichswert.
- **Ausgabe und Einheit:** `knips_abstand` (cm), Abstand der Knipse an der
  vorderen Ärmelnaht.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „14 bis 16 cm“
  bleibt Bereich, kein fester Default gewählt; Fließtext und
  Zeichnungslabel stimmen hier überein (kein Widerspruch).
- **Abhängigkeiten:** keine.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 7 – Ärmelsaumweite über den Abnäher (qualitativ, unquantifiziert)

- **Quelle:** [`formeln_s213.md`](formeln_s213.md), Abschnitt 7
- **Buchfassung:**
  ```text
  Die Ärmelsaumweite kann am Abnäher reguliert werden. Soll z. B. die ÄSaW
  größer werden, wird den Abnäher entsprechend kleiner gezeichnet (siehe
  Seite 211).
  ```
- **Technische Formel:**
  ```text
  # keine quantifizierte Formel auf dieser Seite, nur Richtungsbeziehung:
  äsaw ↑  ⇔  abnäher_breite ↓   (genauer Zusammenhang: siehe Seite 211)
  ```
- **Eingaben und Einheiten:** nicht auf dieser Seite quantifiziert.
- **Ausgabe und Einheit:** nicht auf dieser Seite quantifiziert.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** rein qualitative
  Auswahlregel, kein Zahlenwert auf s213 selbst.
- **Abhängigkeiten:** Seitenübergreifende Abhängigkeit zu Seite 211 (dort
  vermutlich die eigentliche Rechenbeziehung); auf dieser Seite nur
  verlinkt, nicht übernommen.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Die eigentliche quantitative Regel liegt außerhalb dieser Seite (Seite
    211) und wurde hier nicht mitkopiert.
