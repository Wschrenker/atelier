# Formeln s075 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s075.md`](formeln_s075.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle drei Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Grenzwert Abstand Passennaht zu Abnäherspitze

- **Quelle:** [`formeln_s075.md`](formeln_s075.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Gewünschte Abtrennungen gestalten. Hierbei darauf achten, dass die
  Passennähte keinen größeren Abstand als 2 cm zu den Abnäherspitzen haben.
  ```
- **Technische Formel:**
  ```text
  abstand(passennaht, abnaeherspitze) <= 2 cm
  ```
- **Eingaben und Einheiten:** `position_passennaht` (cm), `position_abnaeherspitze`
  (cm) — Lage der jeweiligen Passennaht und der zugehörigen Abnäherspitze.
- **Ausgabe und Einheit:** Bool'sche Auswahlbedingung für die Gestaltung der
  Abtrennungslinien (Passennähte werden nur dort gesetzt, wo die Bedingung
  erfüllt bleibt); keine numerische Ausgabe.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** feste Obergrenze 2 cm
  ohne `ca.` — laut Buchwortlaut ein harter Grenzwert, keine Untergrenze
  angegeben.
- **Abhängigkeiten:** wirkt auf die Passenform, die vor den Formeln 2 und 3
  dieser Seite feststehen muss (Abtrennungen werden zuerst gestaltet, dann
  erst um die Mehrweite geöffnet).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unklar, ob sich „Abnäherspitzen" auf alle Abnäher der Ausgangsteilung
    bezieht oder nur auf die an der jeweiligen Passennaht angrenzenden.

## Formel 2 – Mehrweiten-Verteilung an Teilungsnähten und Seitennähten

- **Quelle:** [`formeln_s075.md`](formeln_s075.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Genauzo wie beim saumerweiterten und Glockenrock aus dem 10-Bahnen-Rock wird
  die Abtrennung sowohl an den Teilungsnahen als auch an der Seitennah um die
  gewünschte Weite geöffnet. An jeder Teilungsnaht um 1/10 und an den
  Seitennahen jeweils um 1/20 der gewünschten Mehrweite.
  ```
- **Technische Formel:**
  ```text
  mehrweite_je_teilungsnaht = mehrweite_gewuenscht * (1/10)
  mehrweite_je_seitennaht   = mehrweite_gewuenscht * (1/20)
  ```
- **Eingaben und Einheiten:** `mehrweite_gewuenscht` (cm) — gewünschte
  Mehrweite laut Buchtext; Anzahl der Teilungsnähte und Seitennähte aus der
  zugrundeliegenden 10-Bahnen-Einteilung.
- **Ausgabe und Einheit:** `mehrweite_je_teilungsnaht` (cm) je Teilungsnaht,
  `mehrweite_je_seitennaht` (cm) je Seitennaht — Öffnungsmaß der Abtrennung an
  der jeweiligen Naht.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** feste Brüche 1/10 und
  1/20 ohne `ca.` — kein Spielraum laut Buchwortlaut. Die Zuordnung folgt dem
  Querverweis „wie beim saumerweiterten und Glockenrock aus dem
  10-Bahnen-Rock" (andere Seite, hier nur verlinkt).
- **Abhängigkeiten:** [[Formel 3]] (vM/hM erhalten keine Mehrweite, also 0
  statt eines Bruchteils); Querverweis auf die Seite mit dem
  saumerweiterten/Glockenrock aus dem 10-Bahnen-Rock (vermutlich s073, nicht
  kopiert).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unklar, ob `mehrweite_gewuenscht` ein einziger Gesamtwert ist, der auf
    alle Teilungsnähte und Seitennähte gleichzeitig mit je 1/10 bzw. 1/20
    angewandt wird, oder ob 1/10 und 1/20 sich auf unterschiedliche
    Bezugsgrößen beziehen.
  - Die genaue Anzahl der Teilungsnähte und Seitennähte auf dieser
    Modellvariante steht nicht im OCR-Text dieser Seite, sondern ergibt sich
    vermutlich aus der Zeichnung ☐2 bzw. der verlinkten 10-Bahnen-Einteilung.
  - Ob sich die Brüche auf dieselbe Mehrweite oder je Nahtart auf eine eigene
    „gewünschte Mehrweite" beziehen, ist aus dem Wortlaut nicht eindeutig.

## Formel 3 – Randbedingung: keine Mehrweite an vM/hM

- **Quelle:** [`formeln_s075.md`](formeln_s075.md), Abschnitt 3
- **Buchfassung:**
  ```text
  An vM und hM wird, da es sich hier um eine Spiegellinie und keine Naht
  handelt, keine Mehrweite angezeichnet.
  ```
- **Technische Formel:**
  ```text
  mehrweite(vM) = 0
  mehrweite(hM) = 0
  ```
- **Eingaben und Einheiten:** keine (Sonderfall ohne Zahlenwert).
- **Ausgabe und Einheit:** `mehrweite` (cm) an vM bzw. hM, fest 0.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bedingung „Spiegellinie,
  keine Naht" als Begründung für den Ausschluss; keine Bereichsangabe nötig,
  da fester Wert 0.
- **Abhängigkeiten:** [[Formel 2]] (Sonderfall/Ausnahme zur allgemeinen
  Mehrweiten-Verteilung an den übrigen Nähten).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
