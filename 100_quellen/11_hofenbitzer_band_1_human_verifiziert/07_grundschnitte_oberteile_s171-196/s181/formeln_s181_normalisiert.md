# Formeln s181 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s181.md`](formeln_s181.md) vermerkt, trägt die
Seite weiterhin den Status `OCR-Rohfassung – noch nicht menschlich
verifiziert`. Nur die Buchfassung von Formel 1 (`HlB + 0,5 cm`, Label `HlP`)
ist von Werner am Original bestätigt; alle übrigen Formeln sind unbestätigt.
Alle 15 Formeln stehen dennoch auf `offen`, da für keine von ihnen die
vollständige Bereitschaftsstufe (alle abhängigen Stellen der Seite bestätigt)
erreicht ist. Dies ist ein Walking-Skeleton-Durchlauf auf ausdrücklichen
Wunsch Werners, kein Ersatz für die Bestätigung.

## Formel 1 – Hinteres Halsloch, horizontal

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 1
- **Buchfassung:**
  ```text
  HlP Von P1 nach links die Halslochbreite (HlB) + 0,5 cm abtragen.
  ```
- **Technische Formel:**
  ```text
  HlP = P1 - (HlB + 0,5 cm)   (entlang der horizontalen Achse, nach links)
  ```
- **Eingaben und Einheiten:** `P1` (Bezugspunkt, Koordinate); `HlB`
  (Halslochbreite, cm, aus Konstruktionstabelle/Maßsatz, nicht auf dieser
  Seite hergeleitet).
- **Ausgabe und Einheit:** `HlP` (Halslochpunkt, Koordinate).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Zuschlag
  „+ 0,5 cm", kein `ca.`, kein Bereich.
- **Abhängigkeiten:** `HlB` stammt aus der Konstruktionstabelle (Quelle
  außerhalb dieser Seite, nicht ermittelt). [[Formel 12]] verwendet dieselbe
  Formel für die vordere, vertikale Halslochstelle.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Buchfassung (Wortlaut) ist am Original bestätigt (siehe `s181.md`). Status
    bleibt dennoch `offen`, da Herkunft und Einheit von `HlB` sowie die
    übrige Seite nicht bestätigt sind.
  - Richtung „nach links" nicht als Vorzeichen/Achse geometrisch präzisiert.

## Formel 2 – Schulterwinkel hinten

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Den Schulterwinkel aus der Konstruktionstabelle und -2° vom hinteren HlP
  nach links unten zeichnen.
  ```
- **Technische Formel:**
  ```text
  winkel_schulter_hinten = schulterwinkel_tabelle - 2°
  ```
- **Eingaben und Einheiten:** `schulterwinkel_tabelle` (Grad, aus
  Konstruktionstabelle, nicht auf dieser Seite).
- **Ausgabe und Einheit:** `winkel_schulter_hinten` (Grad), Richtung der
  hinteren Schulternaht ab `HlP`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Abzug „-2°".
- **Abhängigkeiten:** Basiswert aus Konstruktionstabelle (nicht auf s181);
  [[Formel 13]] (analoge Formel vorne, „+2°").
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Formel ist am Original bestätigt.
  - Konstruktionstabelle selbst nicht Teil dieser Seite/Extraktion.

## Formel 3 – Hintere Schulternahtlänge (hSuNL)

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 3
- **Buchfassung:**
  ```text
  SUP hSuNL in der Konstruktionstabelle ablesen und vom HlP aus abtragen →
  hintere Schulter.
  ```
- **Technische Formel:**
  ```text
  hintere_schulter_endpunkt = HlP + hSuNL   (entlang Schulternaht-Richtung
                                              aus Formel 2)
  ```
- **Eingaben und Einheiten:** `HlP` (Koordinate); `hSuNL` (cm, aus
  Konstruktionstabelle).
- **Ausgabe und Einheit:** Endpunkt der hinteren Schulternaht (Koordinate).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext.
- **Abhängigkeiten:** [[Formel 1]] (`HlP`), [[Formel 2]] (Richtung); `hSuNL`
  aus Konstruktionstabelle.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Ovales Label laut OCR „SUP", vermutlich „hSuP" – Zuordnung h-/v- am
    Original zu bestätigen.
  - Konstruktionstabelle selbst nicht Teil dieser Seite.

## Formel 4 – Streckenhalbierung P10–P16 → P17

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 4
- **Buchfassung:**
  ```text
  NAP Die Strecke von P10 bis P16 halbieren → P17 und die Schulterblattlinie
  nach rechts abwinkeln.
  ```
- **Technische Formel:**
  ```text
  P17 = P10 + 0,5 * (P16 - P10)
  ```
- **Eingaben und Einheiten:** `P10`, `P16` (Koordinaten).
- **Ausgabe und Einheit:** `P17` (Koordinate), Ausgangspunkt der
  Schulterblattlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `P16` selbst ist laut
  `formeln_s181.md` (Nicht als Formel erfasst, Zeile 18) bedingt definiert
  (Ausnahmefall bei großer RüB/schmaler Schulter) – diese Bedingung ist nicht
  Teil dieser Formel, aber Voraussetzung für `P16`.
- **Abhängigkeiten:** `P16` (bedingt definiert, Zeile 18 der OCR, nicht als
  eigene Formel geführt); [[Formel 5]] (nutzt dieselbe Strecke weiter).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Ovales Label laut OCR „NAP", vermutlich „hÄP" – am Original zu
    bestätigen (Widerspruch: Label steht am Absatzanfang, „hÄP" wird aber
    erst zwei Sätze später im Fließtext definiert).
  - Zeichnung zeigt zusätzlich „½" bei P17 (siehe `formeln_s181.md`,
    Abschnitt 4) – bestätigt den Halbierungsfaktor, selbst aber unbestätigt.

## Formel 5 – Streckenhalbierung untere Hälfte → hinterer Ärmelpunkt (hÄP)

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 5
- **Buchfassung:**
  ```text
  Die untere Hälfte der Strecke nochmals halbieren → hinterer Ärmelpunkt
  (hÄP)
  ```
- **Technische Formel:**
  ```text
  hÄP = P17 + 0,5 * (P16 - P17)
      = P10 + 0,75 * (P16 - P10)
  ```
- **Eingaben und Einheiten:** `P17`, `P16` (Koordinaten aus Formel 4).
- **Ausgabe und Einheit:** `hÄP` (Koordinate), hinterer Ärmelpunkt.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext über
  die zweifache Halbierung hinaus.
- **Abhängigkeiten:** [[Formel 4]] (`P17`, `P16`).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Formel ist am Original bestätigt.
  - Zeichnung zeigt zusätzlich „¼" bei hÄP (bezogen auf P10–P16 gesamt) –
    konsistent mit der hergeleiteten 0,75-Faktor-Rechnung ab P10 bzw.
    0,25-Faktor ab P16, aber selbst unbestätigt.

## Formel 6 – Zeichnungsgebundene Zusatzmaße an hÄP/Schulterblattlinie

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 6
- **Buchfassung:**
  ```text
  ca. 1 cm
  ca. 1,5 cm
  ```
- **Technische Formel:**
  ```text
  # Bezugsgrößen unklar – kein Umrechnungsschritt formulierbar
  ```
- **Eingaben und Einheiten:** unklar (vermutlich Abstände nahe P17/hÄP,
  Schulterblattlinie).
- **Ausgabe und Einheit:** unklar.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** beide Werte mit „ca."
  im Original.
- **Abhängigkeiten:** vermutlich zu [[Formel 4]]/[[Formel 5]] gehörig, aber
  nicht im Fließtext dieser Seite verankert.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Kein Textbeleg für diese beiden Maße; ausschließlich in der Zeichnung
    sichtbar. Ohne Bestätigung, welche Strecke genau gemeint ist, ist keine
    technische Formel formulierbar.

## Formel 7 – Kontrollhinweis RüB

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 7
- **Buchfassung:**
  ```text
  Kontrolle: obere gemessene RüB + RüB-Zugabe
  ```
- **Technische Formel:**
  ```text
  kontrollwert = RüB_obere_gemessene + RüB_zugabe
  ```
- **Eingaben und Einheiten:** `RüB_obere_gemessene` (cm, Messwert);
  `RüB_zugabe` (cm, Zugabe – Herkunft/Wert nicht auf dieser Seite).
- **Ausgabe und Einheit:** `kontrollwert` (cm), zur Gegenprüfung der
  Konstruktion an der Schulterblattlinie/hÄP-Region.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext.
- **Abhängigkeiten:** vermutlich Kontrolle für [[Formel 4]]/[[Formel 5]]
  (Position von P17/hÄP), geometrisch aber nicht spezifiziert.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Kein Textbeleg im Fließtext dieser Seite; ausschließlich Zeichnungslabel.
  - `RüB_zugabe` als Größe nicht definiert (Wert/Herkunft unbekannt).

## Formel 8 – Vorderlänge (VL)

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 8
- **Buchfassung:**
  ```text
  Von P19 nach oben die Vorderlänge (VL) - 1 cm abtragen
  ```
- **Technische Formel:**
  ```text
  P20 = P19 + (VL - 1 cm)   (entlang der vertikalen Achse, nach oben)
  ```
- **Eingaben und Einheiten:** `P19` (Koordinate); `VL` (Vorderlänge, cm,
  Körper-/Konstruktionsmaß, nicht auf dieser Seite hergeleitet).
- **Ausgabe und Einheit:** `P20` (Koordinate) – Zielpunkt wird im
  Buchtext nicht benannt, aus dem Folgeabsatz (Zeile 32) erschlossen.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Abzug „-1 cm".
- **Abhängigkeiten:** `VL` extern (Maßsatz); [[Formel 9]] setzt am selben
  Punkt `P20` an.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Zielpunktbezeichnung „P20" ist Rückschluss aus dem Folgesatz, nicht
    explizit in diesem Satz genannt – am Original zu bestätigen.

## Formel 9 – Brusttiefe (BrT)

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 9
- **Buchfassung:**
  ```text
  und von P20 nach unten die Brusttiefe (BrT) - 1 cm abtragen.
  ```
- **Technische Formel:**
  ```text
  P21 = P20 - (BrT - 1 cm)   (entlang der vertikalen Achse, nach unten)
  ```
- **Eingaben und Einheiten:** `P20` (Koordinate, aus Formel 8); `BrT`
  (Brusttiefe, cm, Maßsatz).
- **Ausgabe und Einheit:** `P21` (Koordinate) – Zielpunkt aus dem Folgesatz
  (Zeile 34) erschlossen.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Abzug „-1 cm".
- **Abhängigkeiten:** [[Formel 8]] (`P20`); [[Formel 10]] setzt an `P21` an.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Zielpunktbezeichnung „P21" ist Rückschluss aus dem Folgesatz, nicht
    explizit genannt – am Original zu bestätigen.

## Formel 10 – Brustpunkt (BrP)

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 10
- **Buchfassung:**
  ```text
  BrP Von P21 nach rechts die halbe Brustbreite+ (½ BrB+) - 0,3 cm abtragen →
  Brustpunkt.
  ```
- **Technische Formel:**
  ```text
  BrP = P21 + (0,5 * BrB+ - 0,3 cm)   (entlang der horizontalen Achse, nach
                                        rechts)
  ```
- **Eingaben und Einheiten:** `P21` (Koordinate, aus Formel 9); `BrB+`
  (Brustbreite mit Zuschlag, cm, Maßsatz/Tabelle – das „+" ist Teil der
  Buchbezeichnung, nicht dieser Formel selbst zugeordnet).
- **Ausgabe und Einheit:** `BrP` (Brustpunkt, Koordinate).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Abzug
  „-0,3 cm", kein `ca.`.
- **Abhängigkeiten:** [[Formel 9]] (`P21`); `BrB+` extern (Konstruktions-
  tabelle/Maßsatz, Herkunft des „+" nicht auf dieser Seite geklärt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Bedeutung von „BrB+" (welcher Zuschlag, aus welcher Tabelle) nicht auf
    dieser Seite definiert.

## Formel 11 – Vorderes Halsloch, horizontal

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 11
- **Buchfassung:**
  ```text
  HlP Von P20 nach rechts die HlB abtragen.
  ```
- **Technische Formel:**
  ```text
  HlP_vorne = P20 + HlB   (entlang der horizontalen Achse, nach rechts)
  ```
- **Eingaben und Einheiten:** `P20` (Koordinate, aus Formel 8); `HlB`
  (Halslochbreite, cm – gleiche Größe wie in Formel 1).
- **Ausgabe und Einheit:** `HlP_vorne` (Koordinate).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Zuschlag, anders
  als [[Formel 1]] und [[Formel 12]] (dort „+ 0,5 cm").
- **Abhängigkeiten:** [[Formel 8]] (`P20`); `HlB` wie in [[Formel 1]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Buchtext bestätigt keinen Zuschlag an dieser Stelle – bewusster
    Unterschied zu Formel 1/12 oder OCR-Auslassung? Am Original zu prüfen.

## Formel 12 – Vorderes Halsloch, vertikal

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 12
- **Buchfassung:**
  ```text
  Von P20 nach unten HlB + 0,5 abtragen und zum HlP das vordere Halsloch
  formen.
  ```
- **Technische Formel:**
  ```text
  P_vorne_unten = P20 - (HlB + 0,5 cm)   (entlang der vertikalen Achse, nach
                                           unten)
  ```
- **Eingaben und Einheiten:** `P20` (Koordinate); `HlB` (Halslochbreite, cm);
  Zuschlag „0,5" – Einheit „cm" im Buchtext hier nicht wiederholt (siehe
  [[Formel 1]], dort „+ 0,5 cm" vollständig).
- **Ausgabe und Einheit:** Zielpunkt für das vordere Halsloch (Koordinate,
  zusammen mit `HlP_vorne` aus Formel 11).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Zuschlag,
  gleicher Betrag wie Formel 1.
- **Abhängigkeiten:** [[Formel 1]] (gleiche Formel, hintere Seite);
  [[Formel 11]] (`HlP_vorne`, gemeinsame Halslochformung).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Einheit von „0,5" hier nicht explizit als „cm" wiederholt – Übernahme aus
    Formel 1 plausibel, aber Buchtext-Wortlaut an dieser Stelle selbst nicht
    bestätigt.

## Formel 13 – Schulterwinkel vorne

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 13
- **Buchfassung:**
  ```text
  Aus der Konstruktionstabelle den Schulterwinkel ablesen und + 2° vom HlP
  die vordere Schulternaht nach rechts unten zeichnen.
  ```
- **Technische Formel:**
  ```text
  winkel_schulter_vorne = schulterwinkel_tabelle + 2°
  ```
- **Eingaben und Einheiten:** `schulterwinkel_tabelle` (Grad, wie in
  Formel 2).
- **Ausgabe und Einheit:** `winkel_schulter_vorne` (Grad), Richtung der
  vorderen Schulternaht ab `HlP_vorne`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Zuschlag „+2°".
- **Abhängigkeiten:** [[Formel 2]] (analoge Formel hinten, „-2°"); gleicher
  Tabellenwert `schulterwinkel_tabelle`.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Formel ist am Original bestätigt.

## Formel 14 – Vordere Schulternahtlänge (SuNL)

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 14
- **Buchfassung:**
  ```text
  SUP Die SuNL aus der Konstruktionstabelle ablesen und ab dem Halsloch
  abtragen → vordere Schulter und vSuP.
  ```
- **Technische Formel:**
  ```text
  vSuP = HlP_vorne + SuNL   (entlang Schulternaht-Richtung aus Formel 13)
  ```
- **Eingaben und Einheiten:** `HlP_vorne` (Koordinate, aus Formel 11/12);
  `SuNL` (cm, aus Konstruktionstabelle – Bezeichnung ohne „h"-Vorsilbe, im
  Unterschied zu „hSuNL" in Formel 3).
- **Ausgabe und Einheit:** `vSuP` (vorderer Schulterpunkt, Koordinate).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext.
- **Abhängigkeiten:** [[Formel 11]]/[[Formel 12]] (`HlP_vorne`),
  [[Formel 13]] (Richtung); [[Formel 3]] (analoge hintere Formel, dort
  „hSuNL").
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Ovales Label laut OCR „SUP", vermutlich „vSuP" – am Original zu
    bestätigen.
  - Ob „SuNL" hier ein eigener Tabellenwert ist oder mit „hSuNL" (Formel 3)
    zusammenhängt, ist aus dem Wortlaut nicht eindeutig.

## Formel 15 – Vorderer Ärmelpunkt (vÄP)

- **Quelle:** [`formeln_s181.md`](formeln_s181.md), Abschnitt 15
- **Buchfassung:**
  ```text
  NAP □6 An der vorderen Armlinie ¼ ArD+ von P13 nach oben abtragen →
  vorderer Ärmelpunkt (vÄP).
  ```
- **Technische Formel:**
  ```text
  vÄP = P13 + 0,25 * ArD+   (entlang der vorderen Armlinie, nach oben)
  ```
- **Eingaben und Einheiten:** `P13` (Koordinate); `ArD+` (Armdurchmesser mit
  Zuschlag, cm, Maßsatz/Tabelle – „+" Teil der Buchbezeichnung, wie bei
  `BrB+` in Formel 10).
- **Ausgabe und Einheit:** `vÄP` (vorderer Ärmelpunkt, Koordinate).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Faktor „¼",
  kein `ca.`.
- **Abhängigkeiten:** `ArD+` extern (Konstruktionstabelle/Maßsatz);
  [[Formel 5]] (analoger hinterer Ärmelpunkt `hÄP`, dort andere Herleitung
  über Streckenhalbierung statt `¼ ArD+`).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Ovales Label laut OCR „NAP", vermutlich „vÄP" – am Original zu
    bestätigen.
  - Bedeutung von „ArD+" (welcher Zuschlag, aus welcher Tabelle) nicht auf
    dieser Seite definiert.
  - Unterschiedliche Herleitungsart für hinteren (`hÄP`, Streckenhalbierung)
    und vorderen (`vÄP`, `¼ ArD+`) Ärmelpunkt – im Buch offenbar bewusst
    unterschiedlich, nicht als Widerspruch zu werten, aber als Auffälligkeit
    festgehalten.
