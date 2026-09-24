# Formeln s184 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s184.md`](formeln_s184.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle neun Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Maximale Drehung des Brustabnäher-Dreiecks (Li26)

- **Quelle:** [`formeln_s184.md`](formeln_s184.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Rechts der vorderen Armlinie den maximalen Abstand zur Armlinie anzeichnen → Li26.

  maximal
  BrU:20
  +1 cm
  ```
- **Technische Formel:**
  ```text
  abstand_li26_max = BrU / 20 + 1 cm
  ```
- **Eingaben und Einheiten:** `BrU` (Brustumfang, cm).
- **Ausgabe und Einheit:** `abstand_li26_max` (cm), Obergrenze für den Abstand
  von Li26 zur vorderen Armlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** ausdrücklich ein
  Maximalwert – das Dreieck kann laut Fließtext (Zeilen 33–51 in
  `ocr_s184.md`) frei bis zu diesem Maximum gedreht werden; kein fester
  Startwert vorgeschrieben. Je weiter gedreht, desto größer Brustabnäher und
  desto kleiner das Armloch.
- **Abhängigkeiten:** wirkt mit der allgemeinen Dreieck-Drehung aus „7
  Brustabnäher konstruieren" zusammen; Querverweis im Buch auf „Seiten 192 und
  217" für die Rückdrehung zur Armlochauflockerung (nicht Teil dieser Seite).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob „BrU:20" tatsächlich `BrU / 20` bedeutet oder eine andere Lesart (z. B.
    Bezug auf eine Konstruktionstabellen-Spalte „BrU 20") vorliegt, ist am
    Original zu klären.

## Formel 2 – Schulterabnäher-Inhalt

- **Quelle:** [`formeln_s184.md`](formeln_s184.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Den Schulterabnäher mit 1,5 cm Inhalt ins Armloch zeichnen.
  ```
- **Technische Formel:**
  ```text
  schulterabnaeher_inhalt = 1,5 cm
  ```
- **Eingaben und Einheiten:** keine (Festwert).
- **Ausgabe und Einheit:** `schulterabnaeher_inhalt` (cm), am hSuP ins Armloch
  gezeichnet.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert ohne `ca.`
  oder Bereich laut Buchwortlaut.
- **Abhängigkeiten:** wirkt mit [[Formel 3]] zusammen (Formung des hinteren
  Armlochs im selben Konstruktionsschritt „8 Armlöcher und
  Schulterabnäher").
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 3 – Hinteres Armloch, Abstand zu hAP

- **Quelle:** [`formeln_s184.md`](formeln_s184.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Hinteres Armloch von der Seite, ca. 1,5 cm am hAP vorbei, senkrecht an P17 zum hSuP formen.
  ```
- **Technische Formel:**
  ```text
  position_armlochkurve(hAP) = hAP_position ± ca. 1,5 cm  (Richtung: "vorbei", nicht weiter spezifiziert)
  ```
- **Eingaben und Einheiten:** Position von `hAP` (Landmarke).
- **Ausgabe und Einheit:** Verlauf der hinteren Armlochkurve (cm-Offset an
  `hAP`), zusätzlich Bedingung „senkrecht an P17".
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` erhalten;
  Richtung des Vorbeilaufens („vorbei am hAP") geometrisch nicht exakt
  spezifiziert.
- **Abhängigkeiten:** [[Formel 2]] (gleicher Konstruktionsschritt); Landmarke
  `hAP` selbst nicht auf dieser Seite hergeleitet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Schreibweise „hAP" im Fließtext vs. Zeichnungslabel „hÄP" (siehe
    Prüfstelle 5 in `s184.md`) – vermutlich OCR-Fehler, nicht bestätigt.

## Formel 4 – Taillenlinie-Erhöhung an Seitenlinien und hinterer Armlinie

- **Quelle:** [`formeln_s184.md`](formeln_s184.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Die Taillenlinie an den Seitenlinien um 1 cm und an der hinteren Armlinie um 0,5 cm erhöhen.
  ```
- **Technische Formel:**
  ```text
  taillenlinie_seitenlinie_neu      = taillenlinie_alt + 1 cm
  taillenlinie_hintere_armlinie_neu = taillenlinie_alt + 0,5 cm
  ```
- **Eingaben und Einheiten:** `taillenlinie_alt` (cm) an den jeweiligen
  Bezugslinien (beide Seitenlinien; hintere Armlinie).
- **Ausgabe und Einheit:** `taillenlinie_seitenlinie_neu`,
  `taillenlinie_hintere_armlinie_neu` (cm) – Punkte der „erhöhten
  Taillenlinie".
- **Bereiche, Bedingungen und Auswahlentscheidungen:** beide Werte fest, ohne
  `ca.` oder Bereich laut Buchwortlaut.
- **Abhängigkeiten:** die erhöhte Taillenlinie ist vermutlich Bezugslinie für
  die spätere Messung von `vTaB`/`hTaB` in [[Formel 7]]; auf dieser Seite
  nicht ausdrücklich verknüpft.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob die beiden Erhöhungswerte (1 cm bzw. 0,5 cm) linear zwischen
    Seitenlinie und hinterer Armlinie interpoliert werden oder als getrennte
    Punkte mit gerader Verbindung stehen bleiben, ist am Original zu klären.

## Formel 5 – Vorderer Taillenabnäher, Abtrag ¼ TaU

- **Quelle:** [`formeln_s184.md`](formeln_s184.md), Abschnitt 5
- **Buchfassung:**
  ```text
  Von der vorderen Armlinie zur vM (1/4) TaU abtragen (nicht (1/4) TaW!)

  Reicht dieser Abtrag von (1/4) TaU über die vM hinaus, deutet dies auf eine "Starke Figur" hin. Nähere Informationen über die Konstruktion für eine Starke Figur findet man in Band 2.
  ```
- **Technische Formel:**
  ```text
  abtrag_vAM_bis_vM = TaU / 4
  ```
- **Eingaben und Einheiten:** `TaU` (Taillenumfang, cm) – ausdrücklich nicht
  `TaW`.
- **Ausgabe und Einheit:** `abtrag_vAM_bis_vM` (cm), Punkt auf der vorderen
  Armlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Auswahlregel: reicht der
  Abtrag über die vM hinaus → Verweis „Starke Figur" auf Band 2 (kein
  eigener Algorithmus auf dieser Seite, nur Verweis).
- **Abhängigkeiten:** Ausgangspunkt für die Messung von `me` in [[Formel 6]]
  (vermutlich dieselbe Strecke, siehe dortige offene Frage); Verweis auf Band 2
  für „Starke Figur" (außerhalb dieses Buchbands).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Der Absatz steht im Rohtext zweimal; am Original zu prüfen, ob er im Buch
    tatsächlich einmal oder zweimal gedruckt ist (siehe Prüfstelle 8 in
    `s184.md`).

## Formel 6 – Vorderer Taillenabnäher-Inhalt (vAbl) mit Passformklassen-Zuschlag

- **Quelle:** [`formeln_s184.md`](formeln_s184.md), Abschnitt 6
- **Buchfassung:**
  ```text
  10 Strecke zur vM messen und + 0 bis 1
  cm als Abnäherinhalt übertragen.
  vAbl = me + 0 bis 1 cm = 3,2 cm

  bis Passformklasse 4 + 1,0 cm
  Passformklasse 5 bis 7 + 0,5 cm
  ab Passformklasse 8 + 0 cm
  ```
- **Technische Formel:**
  ```text
  vAbl = me + zuschlag(passformklasse)

  zuschlag(PK) = 1,0 cm   wenn PK ≤ 4
  zuschlag(PK) = 0,5 cm   wenn 5 ≤ PK ≤ 7
  zuschlag(PK) = 0 cm     wenn PK ≥ 8
  ```
- **Eingaben und Einheiten:** `me` (gemessene Reststrecke zur vM, cm),
  `passformklasse` (PK, Ordinalzahl 1–8+).
- **Ausgabe und Einheit:** `vAbl` (cm), Inhalt des vorderen Taillenabnähers.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** allgemeine Bereichsangabe
  „+ 0 bis 1 cm" wird durch die Passformklassen-Tabelle in drei feste
  Zuschlagsstufen aufgelöst; kein weiterer Spielraum innerhalb einer Stufe laut
  Buchwortlaut.
- **Abhängigkeiten:** [[Formel 5]] (Strecke `me` vermutlich Rest nach dem
  ¼-TaU-Abtrag – am Original zu klären, ob „Strecke zur vM messen" dieselbe
  Teilstrecke meint); Nachrechenbeispiel `me = 2,2 cm` + Zuschlag `1,0 cm` (PK
  ≤ 4) `= 3,2 cm` stimmt arithmetisch mit der gedruckten Beispielrechnung
  überein.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nicht ausdrücklich belegt, dass das Rechenbeispiel `3,2 cm` die
    Passformklasse ≤ 4 verwendet – aus der Arithmetik (`2,2 + 1,0 = 3,2`)
    plausibel abgeleitet, aber nicht Buchtext-identisch benannt.
  - Zusammenhang zwischen `me` und dem Abtrag aus Formel 5 am Original zu
    prüfen.

## Formel 7 – Taillenausfall (TaAf), Textfassung

- **Quelle:** [`formeln_s184.md`](formeln_s184.md), Abschnitt 7
- **Buchfassung:**
  ```text
  11 vTaB (ohne Abnäherinhalt) und
  hTaB messen, addieren = TaB. Die
  ½ TaW aus der Konstruktions-
  tabelle entnehmen und dort den
  TaAf berechnen:

  Taillenausfall (TaAf)

  = TaB - ½ TaW
  = 42,8 cm - 36 cm = 6,8 cm
  ```
- **Technische Formel:**
  ```text
  TaB  = vTaB + hTaB
  TaAf = TaB - halbe_TaW
  ```
- **Eingaben und Einheiten:** `vTaB` (cm, ohne Abnäherinhalt gemessen),
  `hTaB` (cm), `halbe_TaW` (cm, aus Konstruktionstabelle entnommen, nicht auf
  dieser Seite hergeleitet).
- **Ausgabe und Einheit:** `TaAf` (cm), Taillenausfall.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** feste Rechenvorschrift
  ohne `ca.`; `halbe_TaW` selbst kommt aus einer externen Tabelle (Bezug außerhalb
  dieser Seite).
- **Abhängigkeiten:** [[Formel 8]] (identische Teilformel `TaB = vTaB + hTaB`,
  zeichnungsgebunden bestätigt); `halbe_TaW` aus der Konstruktionstabelle
  (Quelle nicht auf s184).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nachgerechnet: `42,8 cm - 36 cm = 6,8 cm` stimmt arithmetisch; dies
    bestätigt nur die Rechnung selbst, nicht die Herkunft der Werte `42,8 cm`
    und `36 cm` (aus `vTaB+hTaB` bzw. Konstruktionstabelle, hier nicht
    nachvollziehbar).
  - Bezeichnung „TaW" hier vs. „½ TaW" – ob dies dieselbe Größe wie in Formel 5
    ausgeschlossenes „TaW" ist, am Original zu klären.

## Formel 8 – Taillenausfall, Zeichnungsformel vTaB + hTaB = TaB

- **Quelle:** [`formeln_s184.md`](formeln_s184.md), Abschnitt 8
- **Buchfassung:**
  ```text
  vTaB + hTaB = TaB
  ```
- **Technische Formel:**
  ```text
  TaB = vTaB + hTaB
  ```
- **Eingaben und Einheiten:** `vTaB`, `hTaB` (cm).
- **Ausgabe und Einheit:** `TaB` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; einfache Summe.
- **Abhängigkeiten:** identisch mit dem Teilschritt in [[Formel 7]];
  zeichnungsgebundener Doppelbeleg derselben Beziehung, nicht als Nachweis für
  eine andere Formel verwendet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 9 – Hintere Taillenlinie, „½ / ½"-Aufteilung

- **Quelle:** [`formeln_s184.md`](formeln_s184.md), Abschnitt 9
- **Buchfassung:**
  ```text
  ½ / ½
  ```
- **Technische Formel:** nicht ableitbar – die geteilte Größe ist im Fließtext
  nicht benannt.
- **Eingaben und Einheiten:** unbekannt.
- **Ausgabe und Einheit:** unbekannt.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Angabe im
  Fließtext; nur als Zeichnungslabel bei Punkt 30 (hintere Taillenlinie /
  hintere Abnähermitte) belegt.
- **Abhängigkeiten:** möglicher Bezug zu [[Formel 4]] (erhöhte Taillenlinie)
  oder zur hinteren Abnähermitte-Konstruktion; nicht auf dieser Seite geklärt.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ohne Klärung am Original keine technische Formel ableitbar – absichtlich
    nicht spekulativ ergänzt (siehe Prüfstelle 9 in `s184.md`).
