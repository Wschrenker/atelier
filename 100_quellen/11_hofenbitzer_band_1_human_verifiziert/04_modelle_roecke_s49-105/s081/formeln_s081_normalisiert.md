# Formeln s081 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s081.md`](formeln_s081.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle fünf Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung. Die Seite enthält keine Zahlenwerte für die hier normalisierten
Beziehungen; es handelt sich durchgehend um geometrische
Konstruktionsbeziehungen und Auswahlregeln ohne bezifferte Maße.

## Formel 1 – Ansatzposition der Glocke

- **Quelle:** [`formeln_s081.md`](formeln_s081.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Die Glocken können entsprechend der Formung
  der Tailleinhalt wahlweise direkt aus der Taille fallen (wie
  hier am VT) oder welcher unterhalb der Taille (wie hier am
  RT gezeigt).
  ```
- **Technische Formel:**
  ```text
  ansatzposition_glocke ∈ { Taille, unterhalb_Taille }
  ```
- **Eingaben und Einheiten:** keine bezifferten Eingaben; Auswahl aus zwei
  Varianten.
- **Ausgabe und Einheit:** `ansatzposition_glocke` (kategorial, keine Einheit).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** freie fachliche
  Auswahl laut Buch („wahlweise"); Beispiel VT = Taille, Beispiel RT =
  unterhalb der Taille, ohne dass „unterhalb" quantifiziert wird (kein Betrag,
  kein Bereich in cm genannt).
- **Abhängigkeiten:** keine auf dieser Seite benannt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - OCR-Wort „welcher" laut `s081.md` vermutlich „weicher" – Lesart ändert an
    dieser Formel nichts, da hier ohnehin nur die Positionswahl (Taille vs.
    unterhalb) normalisiert wird.
  - „unterhalb der Taille" bleibt ohne Maß oder Bereich; kein Default wählbar.

## Formel 2 – Verschiebung der Teilungsnaht-Abnäher an den Öffnungspunkt

- **Quelle:** [`formeln_s081.md`](formeln_s081.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die Abnaher der vorderen bzw. hinteren Teilungsnahte werden an die Öffnungsposition verschoben, indem Dort die beiden Schnittteile um die Beträge der Abnaherinhalte überschnitten werden.
  ```
- **Technische Formel:**
  ```text
  ueberschneidung_schnittteile = abnaeherinhalt_teilungsnaht
  ```
- **Eingaben und Einheiten:** `abnaeherinhalt_teilungsnaht` (cm), getrennt für
  vordere bzw. hintere Teilungsnaht; Herkunft/Wert auf dieser Seite nicht
  beziffert.
- **Ausgabe und Einheit:** `ueberschneidung_schnittteile` (cm), Betrag der
  Überschneidung der beiden Schnittteile an der Öffnungsposition.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; die Beziehung
  ist als Gleichsetzung formuliert („um die Beträge der Abnäherinhalte").
- **Abhängigkeiten:** `abnaeherinhalt_teilungsnaht` stammt aus der
  Grundkonstruktion des 10-Bahnenrocks („Modellentwicklung aus dem
  10-Bahnenrock (14)", siehe [s081.md](s081.md)); genaue Quellseite/-formel
  auf s081 nicht benannt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unklar, ob je Teilungsnaht (vorne/hinten) getrennt oder ein
    gemeinsamer Betrag gemeint ist.
  - Ausgangsseite/-formel für `abnaeherinhalt_teilungsnaht` nicht ermittelt.

## Formel 3 – Saumöffnung für die Glocke

- **Quelle:** [`formeln_s081.md`](formeln_s081.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Am Saum wird für die Glocke die gewünschte Weite geöffnet
  ```
- **Technische Formel:**
  ```text
  saum_oeffnung = gewuenschte_weite
  ```
- **Eingaben und Einheiten:** `gewuenschte_weite` (cm), frei gewählt, kein
  Buchwert.
- **Ausgabe und Einheit:** `saum_oeffnung` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** vollständig freie
  fachliche Auswahl laut Buch („gewünschte Weite"); kein Bereich, kein
  Default.
- **Abhängigkeiten:** keine auf dieser Seite benannt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kein Zahlenwert oder Bereich im Buchtext – bleibt Auswahlgröße, kein
    fester Wert wählbar.

## Formel 4 – Ausrundung der Ecke an der Ansatznaht (Auswahlregel)

- **Quelle:** [`formeln_s081.md`](formeln_s081.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Wird die entstandene Ecke an der Ansatznah nicht ausgerundet, fällt die Glocke klar und scharf.
  Bei einem ausgerundeten Verlauf der Ansatznah, fällt die Glocke welcher und breiter.
  ```
- **Technische Formel:**
  ```text
  wenn ecke_ausgerundet == falsch:
      glocke_fall = "klar_scharf"
  wenn ecke_ausgerundet == wahr:
      glocke_fall = "weicher_breiter"
  ```
- **Eingaben und Einheiten:** `ecke_ausgerundet` (boolesche Auswahl, keine
  Einheit).
- **Ausgabe und Einheit:** `glocke_fall` (kategorial, keine Einheit).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** zwei sich
  ausschließende Ausprägungen laut Buch; kein Zwischenzustand oder Gradmaß der
  Ausrundung benannt.
- **Abhängigkeiten:** keine auf dieser Seite benannt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - OCR-Wort „welcher" laut `s081.md` vermutlich „weicher" – hier als
    `weicher_breiter` normalisiert, am Original zu bestätigen.
  - Keine geometrische Größe (Radius, Winkel) für „ausgerundet" benannt.

## Formel 5 – Modell 2: zusätzliches Ausstellen beider Seitennähte

- **Quelle:** [`formeln_s081.md`](formeln_s081.md), Abschnitt 5
- **Buchfassung:**
  ```text
  Bei Modell 2 werden beide Seiten-
  nähte (wie hier am RT gezeigt) für
  mehr Saumweite ausgestellt.
  ```
  Zeichnungsgebunden (`skizzen_kontaktbogen.jpg`): „hier **ohne** zusätzliches
  Ausstellen an SN" (Modell 1) vs. „hier **mit** zusätzlichem Ausstellen an
  SN" (Modell 2).
- **Technische Formel:**
  ```text
  ausstellung_seitennaht(modell_1) = 0
  ausstellung_seitennaht(modell_2) > 0   # Betrag im Buch nicht beziffert
  ```
- **Eingaben und Einheiten:** `modell` ∈ {1, 2}; Ausstellbetrag für Modell 2
  (cm) nicht angegeben.
- **Ausgabe und Einheit:** `ausstellung_seitennaht` (cm), zusätzliche
  Saumweite je Seitennaht.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Modell 1 ohne
  Ausstellen, Modell 2 mit Ausstellen an beiden Seitennähten; konkreter Betrag
  weder im Fließtext noch in der Zeichnung beziffert.
- **Abhängigkeiten:** [[Formel 1]] (beide betreffen die Modellunterscheidung
  VT/Modell 1 vs. RT/Modell 2, jedoch an unterschiedlichen Nähten).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kein Zahlenwert für den Ausstellbetrag bei Modell 2 vorhanden.
