# Formeln s175 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s175.md`](formeln_s175.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Die drei
Balance-Kontrollschemata (Formeln 1–3) stammen zusätzlich aus einer
zeichnungsgebundenen KI-Ablesung, nicht aus OCR-Text. Alle sechs Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der Buchfassung.
Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung.

## Formel 1 – Balance-Kontrollschema Figur 1 (runder Rücken, ☐4a)

- **Quelle:** [`formeln_s175.md`](formeln_s175.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Balance muss korrekt sein! hier 4 cm
  VL für Konstruktion 46
  RüL für Konstruktion 42
  ± vorderer Korrekturwert 0
  ± hinterer Korrekturwert -1,5
  VL bei waagerechtem Taillenband 46
  RüL bei waagerechtem Taillenband 43,5
  VL aus Maßtabelle 46
  RüL aus Maßtabelle 43,5
  Balance ist nicht korrekt hier 3 cm
  ```
- **Technische Formel:**
  ```text
  balance_soll = VL_konstruktion - RüL_konstruktion
  balance_ist  = VL_tabelle - RüL_tabelle
  korr_vorne   = VL_konstruktion - VL_tabelle
  korr_hinten  = RüL_konstruktion - RüL_tabelle
  ```
- **Eingaben und Einheiten:** `VL_konstruktion` = 46 cm, `RüL_konstruktion` =
  42 cm, `VL_tabelle` = 46 cm, `RüL_tabelle` = 43,5 cm.
- **Ausgabe und Einheit:** `balance_soll` = 4 cm, `balance_ist` (nachgerechnet)
  = 2,5 cm, `korr_vorne` = 0 cm, `korr_hinten` = -1,5 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Bereiche; alle
  Werte laut Buchfassung fest. `VL bei waagerechtem Taillenband` und
  `VL aus Maßtabelle` sind identisch angegeben (ebenso für RüL) – vermutlich
  zwei Kontrollwege zum selben Wert, hier nicht als getrennte Formel geführt.
- **Abhängigkeiten:** gleiches Schema wie [[Formel 2]] und [[Formel 3]]
  (Figuren 2 und 3 derselben Seite); Eingangswerte für [[Formel 4]]
  (Rückkorrektur am Schnittteil ☐4b).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt; die Werte
    selbst sind eine unbestätigte KI-Ablesung aus der Maßbox der Zeichnung,
    nicht von der OCR-Engine als Text erkannt.
  - Nachgerechnet ergibt `balance_ist = VL_tabelle - RüL_tabelle = 46 - 43,5 =
    2,5 cm`. Die Buchfassung nennt „Balance ist nicht korrekt hier 3 cm". Diese
    Abweichung (2,5 statt 3) wird hier sichtbar dokumentiert und nicht
    stillschweigend an den nachgerechneten Wert angeglichen – möglicherweise
    Ablesefehler der KI, möglicherweise abweichende Buchrechnung.
  - Das isolierte Label „3 Balance korrekt?" (Schrittnummer oder eigenständiges
    Label) ist nicht sicher einzuordnen.

## Formel 2 – Balance-Kontrollschema Figur 2 (gerader Rücken, ☐5a)

- **Quelle:** [`formeln_s175.md`](formeln_s175.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Balance muss korrekt sein! hier 4 cm
  VL für Konstruktion 46
  RüL für Konstruktion 42
  ± vorderer Korrekturwert 0
  ± hinterer Korrekturwert +1
  VL bei waagerechtem Taillenband 46
  RüL bei waagerechtem Taillenband 41
  VL aus Maßtabelle 46
  RüL aus Maßtabelle 41
  Balance ist nicht korrekt hier 5 cm
  ```
- **Technische Formel:** wie [[Formel 1]]:
  ```text
  balance_soll = VL_konstruktion - RüL_konstruktion
  balance_ist  = VL_tabelle - RüL_tabelle
  korr_vorne   = VL_konstruktion - VL_tabelle
  korr_hinten  = RüL_konstruktion - RüL_tabelle
  ```
- **Eingaben und Einheiten:** `VL_konstruktion` = 46 cm, `RüL_konstruktion` =
  42 cm, `VL_tabelle` = 46 cm, `RüL_tabelle` = 41 cm.
- **Ausgabe und Einheit:** `balance_soll` = 4 cm, `balance_ist` (nachgerechnet)
  = 5 cm, `korr_vorne` = 0 cm, `korr_hinten` = +1 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Bereiche; alle
  Werte fest.
- **Abhängigkeiten:** gleiches Schema wie [[Formel 1]] und [[Formel 3]];
  Eingangswerte für [[Formel 5]] (Rückkorrektur am Schnittteil ☐5b).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nachgerechnet stimmt `balance_ist = 46 - 41 = 5 cm` mit der Buchfassung
    überein – anders als bei [[Formel 1]].

## Formel 3 – Balance-Kontrollschema Figur 3 (extrem runder Rücken/Skoliose, ☐6a)

- **Quelle:** [`formeln_s175.md`](formeln_s175.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Balance muss korrekt sein! hier 4 cm
  VL für Konstruktion 46
  RüL für Konstruktion 42
  ± vorderer Korrekturwert +1,5
  ± hinterer Korrekturwert -2,5
  VL bei waagerechtem Taillenband 44,5
  RüL bei waagerechtem Taillenband 44,5
  VL aus Maßtabelle 44,5
  RüL aus Maßtabelle 44,5
  Balance ist nicht korrekt hier 0 cm
  ```
- **Technische Formel:** wie [[Formel 1]]:
  ```text
  balance_soll = VL_konstruktion - RüL_konstruktion
  balance_ist  = VL_tabelle - RüL_tabelle
  korr_vorne   = VL_konstruktion - VL_tabelle
  korr_hinten  = RüL_konstruktion - RüL_tabelle
  ```
- **Eingaben und Einheiten:** `VL_konstruktion` = 46 cm, `RüL_konstruktion` =
  42 cm, `VL_tabelle` = 44,5 cm, `RüL_tabelle` = 44,5 cm.
- **Ausgabe und Einheit:** `balance_soll` = 4 cm, `balance_ist` (nachgerechnet)
  = 0 cm, `korr_vorne` = +1,5 cm, `korr_hinten` = -2,5 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Bereiche; alle
  Werte fest.
- **Abhängigkeiten:** gleiches Schema wie [[Formel 1]] und [[Formel 2]];
  Eingangswerte für [[Formel 6]] (Rückkorrektur am Schnittteil ☐6b).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nachgerechnet stimmt `balance_ist = 44,5 - 44,5 = 0 cm` mit der Buchfassung
    überein – wie bei [[Formel 2]], anders als bei [[Formel 1]].

## Formel 4 – Rückkorrektur Rückenteil, runder Rücken (☐4b)

- **Quelle:** [`formeln_s175.md`](formeln_s175.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Für die Konstruktion wurde die RüL um 1,5 cm gekürzt. Diese Kürzung um 1,5 cm
  wird nun an der Konstruktion wieder ergänzt. Der Schulterabnäher wird größer.
  ```
- **Technische Formel:**
  ```text
  rueL_schnittteil_final = RüL_konstruktion + 1,5 cm
  (entspricht rueL_schnittteil_final = RüL_tabelle, siehe Formel 1)
  schulterabnaeher: wird größer (nicht quantifiziert)
  ```
- **Eingaben und Einheiten:** `RüL_konstruktion` = 42 cm (aus [[Formel 1]]);
  Korrekturbetrag 1,5 cm.
- **Ausgabe und Einheit:** `rueL_schnittteil_final` = 43,5 cm; Schulterabnäher
  vergrößert um unbestimmten Betrag.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 1,5 cm, kein
  `ca.`. Größenänderung des Schulterabnähers laut Buch nur qualitativ
  („größer"), kein Zahlenwert angegeben.
- **Abhängigkeiten:** [[Formel 1]] (liefert `RüL_konstruktion` und
  `korr_hinten` = -1,5 cm, betragsgleich mit dieser Korrektur).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Die zeichnungsgebundenen Zusatzlabels „1,5 cm" und „gemessene RüL = 43,5 cm"
    (Skizze 04) stützen diese Rechnung, sind aber selbst unbestätigte
    KI-Ablesungen.
  - Kein Zahlenwert für die Vergrößerung des Schulterabnähers im Buchtext.

## Formel 5 – Rückkorrektur Rückenteil, gerader Rücken (☐5b)

- **Quelle:** [`formeln_s175.md`](formeln_s175.md), Abschnitt 5
- **Buchfassung:**
  ```text
  Für die Konstruktion wurde die RüL um 1 cm verlängert. Diese Verlängerung um
  1 cm wird nun an der Konstruktion wieder reduziert. Der Schulterabnäher wird
  kleiner.
  ```
- **Technische Formel:**
  ```text
  rueL_schnittteil_final = RüL_konstruktion - 1 cm
  (entspricht rueL_schnittteil_final = RüL_tabelle, siehe Formel 2)
  schulterabnaeher: wird kleiner (nicht quantifiziert)
  ```
- **Eingaben und Einheiten:** `RüL_konstruktion` = 42 cm (aus [[Formel 2]]);
  Korrekturbetrag 1 cm.
- **Ausgabe und Einheit:** `rueL_schnittteil_final` = 41 cm; Schulterabnäher
  verkleinert um unbestimmten Betrag.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 1 cm, kein
  `ca.`. Größenänderung des Schulterabnähers nur qualitativ angegeben.
- **Abhängigkeiten:** [[Formel 2]] (liefert `RüL_konstruktion` und
  `korr_hinten` = +1 cm, betragsgleich mit dieser Korrektur).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Die Bildunterschrift in `ocr_s175.md` (Zeile 35) beginnt mit „Optimierung
    für runden Rücken", obwohl sie zur Figur mit geradem Rücken (☐5a) gehört –
    unverändert als Buchfassung übernommen, nicht still korrigiert.
  - Kein Zahlenwert für die Verkleinerung des Schulterabnähers im Buchtext.

## Formel 6 – Rückkorrektur Vorder- und Rückenteil, Skoliose (☐6b)

- **Quelle:** [`formeln_s175.md`](formeln_s175.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Für die Konstruktion wurde die VL um 1,5 cm verlängert, die RüL um 2,5 cm
  gekürzt. Diese VL-Verlängerung um 1,5 cm wird nun an der Konstruktion wieder
  reduziert und die RüL-Kürzung um 2,5 cm wieder verlängert. Der Brustabnäher
  wird kleiner, der Schulterabnäher wird größer.
  ```
- **Technische Formel:**
  ```text
  vl_schnittteil_final  = VL_konstruktion - 1,5 cm
  rueL_schnittteil_final = RüL_konstruktion + 2,5 cm
  (entspricht vl_schnittteil_final = VL_tabelle und
   rueL_schnittteil_final = RüL_tabelle, siehe Formel 3)
  brustabnaeher: wird kleiner (nicht quantifiziert)
  schulterabnaeher: wird größer (nicht quantifiziert)
  ```
- **Eingaben und Einheiten:** `VL_konstruktion` = 46 cm, `RüL_konstruktion` =
  42 cm (beide aus [[Formel 3]]); Korrekturbeträge 1,5 cm und 2,5 cm.
- **Ausgabe und Einheit:** `vl_schnittteil_final` = 44,5 cm,
  `rueL_schnittteil_final` = 44,5 cm; Brustabnäher verkleinert, Schulterabnäher
  vergrößert, beide unbestimmter Betrag.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** feste Werte 1,5 cm und
  2,5 cm, kein `ca.`. Abnäheränderungen nur qualitativ angegeben.
- **Abhängigkeiten:** [[Formel 3]] (liefert `VL_konstruktion`,
  `RüL_konstruktion`, `korr_vorne` = +1,5 cm und `korr_hinten` = -2,5 cm,
  betragsgleich mit diesen Korrekturen).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Die zeichnungsgebundenen Zusatzlabels (Skizze 05) nennen zusätzlich
    doppelte Maße „1 cm"/„2 cm" und „gemessene VL -1 cm = 44,5 cm" neben
    „gemessene RüL = 44,5 cm"; diese lassen sich aus der Ablesung nicht
    eindeutig einer der beiden Korrekturen zuordnen und werden hier nicht in
    die technische Formel übernommen (siehe [s175.md](s175.md) Prüfstelle 4).
  - Keine Zahlenwerte für die Abnäheränderungen im Buchtext.
