# Formeln s204 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s204.md`](formeln_s204.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt, und die Buchkategorie
`08_grundschnitte_aermel_s197-220` gehört nicht zu den drei Kategorien, für die
`AGENT.md` eine gesonderte Formelextraktion vorschreibt. Alle Formeln stehen
deshalb auf `offen` oder `gesperrt`, unabhängig davon, wie klar die
Buchfassung wirkt oder wie gut ein Rechenbeispiel aufgeht. Dies ist ein
Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung.

## Formel 1 – Oberarmweite aus Oberarmumfang

- **Quelle:** [`formeln_s204.md`](formeln_s204.md), Abschnitt 1
- **Buchfassung:**
  ```text
  OaU | Oberarmumfang | 28 | ± 2,5 | Oberarmweite | OaW | 30,5
  ```
- **Technische Formel:**
  ```text
  OaW = OaU + zugabe_oaw
  zugabe_oaw = 2,5 cm  (Buchsymbol „±", Nachrechnung stützt „+")
  ```
- **Eingaben und Einheiten:** `OaU` (Oberarmumfang, cm).
- **Ausgabe und Einheit:** `OaW` (Oberarmweite, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Buchsymbol „±" nicht
  eindeutig; Nachrechnung 28 + 2,5 = 30,5 passt exakt zu „+", eine Subtraktion
  (28 − 2,5 = 25,5) passt nicht zum Tabellenwert.
- **Abhängigkeiten:** [[Formel 3]] (OaW wird in Abschnitt 3 der Zeichnung
  weiterverwendet, „½ OaW + 0,5 bis 0,7").
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Keine Stelle von Werner am Original bestätigt.
  - Bedeutung des Symbols „±" in dieser Tabellenspalte nicht geklärt (feste
    Zugabe vs. Toleranzbereich).

## Formel 2 – Saumweite aus Handgelenkumfang

- **Quelle:** [`formeln_s204.md`](formeln_s204.md), Abschnitt 1
- **Buchfassung:**
  ```text
  HgU | Handgelenkumfang | 16 | ± 5 | Saumweite | SaW | 21
  ```
- **Technische Formel:**
  ```text
  SaW = HgU + zugabe_saw
  zugabe_saw = 5 cm  (Buchsymbol „±", Nachrechnung stützt „+")
  ```
- **Eingaben und Einheiten:** `HgU` (Handgelenkumfang, cm).
- **Ausgabe und Einheit:** `SaW` (Saumweite, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** wie Formel 1 – Symbol
  „±" nicht eindeutig, Nachrechnung 16 + 5 = 21 stützt „+".
- **Abhängigkeiten:** keine weitere Verwendung auf dieser Seite erkennbar.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Keine Stelle von Werner am Original bestätigt.
  - Gleiche Symbol-Unklarheit wie Formel 1.

## Formel 3 – Ärmellänge (Fixwert mit unklarer Toleranz)

- **Quelle:** [`formeln_s204.md`](formeln_s204.md), Abschnitt 1
- **Buchfassung:**
  ```text
  ÄL | Ärmellänge | 60 | ± 10 | Ärmellänge | ÄL | 60
  ```
  (Foto laut s204.md-Prüfstelle 1 möglicherweise „± 0" statt „± 10".)
- **Technische Formel:**
  ```text
  ÄL = 60 cm  (Ein-/Ausgabewert identisch; Rolle von „± 10" bzw. „± 0" unklar)
  ```
- **Eingaben und Einheiten:** –
- **Ausgabe und Einheit:** `ÄL` (Ärmellänge, cm), Beispielwert 60.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Kein fester Wert
  ausgewählt. Zwei gedruckte Lesarten stehen nebeneinander: „± 10" (OCR) und
  „± 0" (Foto, unbestätigt). Anders als bei OaU/HgU ist der Ein- und
  Ausgabewert hier identisch (60 = 60), sodass unklar bleibt, ob „±" hier eine
  Maßtoleranz, eine wählbare Korrektur oder einen Übertragungsfehler bezeichnet.
- **Abhängigkeiten:** [[Formel 4]] (60 % ÄL für die Ellenbogenlinie verwendet
  ÄL = 60 als Rechenbeispiel).
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Keine Stelle von Werner am Original bestätigt.
  - Widerspruch „± 10" (OCR) vs. „± 0" (Foto laut s204.md) ungeklärt.
  - Tabellenstruktur (identischer Ein-/Ausgabewert) unterscheidet sich von den
    übrigen Zeilen der Tabelle; Bedeutung von „±" hier eigenständig zu klären.

## Formel 4 – Ellenbogenlinie (60 % der Ärmellänge)

- **Quelle:** [`formeln_s204.md`](formeln_s204.md), Abschnitt 2
- **Buchfassung:**
  ```text
  60% der AL abtragen, Dort abwinkeln → Ellenbogenlinie.

  60% ÄL
  60 cm · 0,60 = 36 cm
  ```
- **Technische Formel:**
  ```text
  abstand_ellenbogenlinie = ÄL * 0,60
  ```
- **Eingaben und Einheiten:** `ÄL` (Ärmellänge, cm; siehe [[Formel 3]]).
- **Ausgabe und Einheit:** `abstand_ellenbogenlinie` (cm), gemessen ab dem
  oberen Ende der vorderen Linie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Bereich, fester
  Faktor 0,60 laut Buch- und Zeichnungsfassung.
- **Abhängigkeiten:** [[Formel 3]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Keine Stelle von Werner am Original bestätigt (Zeichnungswerte stimmen
    intern konsistent, das ersetzt keine Bestätigung).

## Formel 5 – Hintere Linie (½ Oberarmweite + Korrekturbetrag)

- **Quelle:** [`formeln_s204.md`](formeln_s204.md), Abschnitt 3
- **Buchfassung (Fließtext, OCR):**
  ```text
  Auf der Schulterlinie 1/2 OaW × 0,5 bis 0,7 abtragen (× 0,5 bis 0,7 cm ist
  ein Korrekturbetrag) → hintere Linie.
  ```
- **Buchfassung (Zeichnung):**
  ```text
  ½ OaW + 0,5 bis 0,7
  (hier 15,9)
  ```
- **Technische Formel:**
  ```text
  abstand_hintere_linie = 0,5 * OaW + korrekturbetrag
  korrekturbetrag ∈ [0,5 cm, 0,7 cm]
  ```
  (Operator laut Zeichnung „+"; Fließtext-OCR zeigt „×" – siehe Widerspruch
  unten. Die technische Formel folgt hier der Zeichnung, weil die
  Nachrechnung nur mit „+" zum Beispielwert passt; das ist keine
  Werner-Bestätigung.)
- **Eingaben und Einheiten:** `OaW` (Oberarmweite, cm; siehe [[Formel 1]]).
- **Ausgabe und Einheit:** `abstand_hintere_linie` (cm), ab der vorderen Linie
  auf der Schulterlinie gemessen.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „0,5 bis 0,7 cm"
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel 1]].
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Keine Stelle von Werner am Original bestätigt.
  - Operator-Widerspruch OCR „×" vs. Zeichnung „+"; Nachrechnung (½ · 30,5 +
    0,5 = 15,75 bzw. + 0,7 = 15,95) stützt „+" gegen den Beispielwert „hier
    15,9", eine Multiplikation ergäbe 7,6–10,7 und passt nicht.

## Formel 6 – Kontrollbereich für die Ärmelkugellinie (Anteil der AlH)

- **Quelle:** [`formeln_s204.md`](formeln_s204.md), Abschnitt 4
- **Buchfassung (Fließtext, OCR):**
  ```text
  Auf der vorderen Linie die AlH abtragen. Von Dort 1/2 AlH nach oben messen
  und ein weiteres Mal 1/2 AlH nach oben abtragen. Dies ist der Bereich der
  optimalen Armelkugellinie.
  ```
- **Buchfassung (Zeichnung):**
  ```text
  AlH (hier 17,2 cm)
  1/10 AlH (hier 1,7)
  1/10 AlH = Kontrollbereich → Bereich der optimalen Ärmelkugellinien-Position
  ```
- **Technische Formel:**
  ```text
  kontrollbereich_breite = AlH * 0,10
  kontrollbereich = [AlH - kontrollbereich_breite, AlH + kontrollbereich_breite]
  ```
  (Faktor laut Zeichnung 1/10; Fließtext-OCR zeigt „1/2" – siehe Widerspruch
  unten. Die technische Formel folgt hier der Zeichnung, weil nur 1/10 zum
  Beispielwert 1,7 passt; das ist keine Werner-Bestätigung.)
- **Eingaben und Einheiten:** `AlH` (Tabellenwert, cm; siehe
  [`formeln_s204.md`](formeln_s204.md), Abschnitt 1 – Bezeichnung selbst noch
  ungeklärt, „AlH" laut Zeichnung vs. „AhH"/„Armlochhöhe" laut s204.md-Prüfstelle
  1 auf dem Foto).
- **Ausgabe und Einheit:** `kontrollbereich` (cm), symmetrischer Bereich um
  den AlH-Abtrag auf der vorderen Linie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich bleibt Bereich
  (kein einzelner Zielpunkt); Buch nennt ihn ausdrücklich „Kontrollbereich",
  nicht Vorschrift für einen festen Punkt.
- **Abhängigkeiten:** [[Formel 1 – Abschnitt „AlH"]] (Tabellenwert AlH), keine
  eigene Formelnummer, da die Herkunft von AlH selbst offen ist.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Keine Stelle von Werner am Original bestätigt.
  - Operator-/Faktor-Widerspruch OCR „1/2 AlH" (zweimal) vs. Zeichnung „1/10
    AlH"; Nachrechnung 17,2 : 10 = 1,72 ≈ 1,7 passt zur Zeichnung, 17,2 : 2 =
    8,6 passt nicht zum Beispielwert.
  - Herkunft und exakte Bedeutung von „AlH" auf dieser Seite selbst
    widersprüchlich (Tabelle vs. Zeichnung vs. Foto laut s204.md).

## Formel 7 – Ärmelkugellinie auf der vorderen Linie

- **Quelle:** [`formeln_s204.md`](formeln_s204.md), Abschnitt 5
- **Buchfassung (Fließtext, OCR):**
  ```text
  Rechts an der Schulterlinie auf die vordere Linie 1/2 AkU − 1 cm abtragen.
  Dort sollte die Armelkugellinie (AkLi) liegen. Mathematisch exakter ware es,
  48% AkU abzutragen.
  ```
- **Buchfassung (Zeichnung):**
  ```text
  ½ ÄkU – 1 cm
  exakter: 48% ÄkU = 44,5 cm · 0,48 = 21,4 cm
  ```
- **Technische Formel:**
  ```text
  # Buchvariante A (Diagonale, einfache Regel):
  position_aeklinie_a = 0,5 * ÄkU - 1 cm

  # Buchvariante B (vom Buch selbst als "exakter" bezeichnet):
  position_aeklinie_b = ÄkU * 0,48
  ```
- **Eingaben und Einheiten:** `ÄkU` (Ärmelkugelumfang, cm; siehe
  [`formeln_s204.md`](formeln_s204.md), Abschnitt 1 – Formel `ÄkU = AlU + EW
  in cm`, dort ebenfalls `offen`).
- **Ausgabe und Einheit:** `position_aeklinie_a` bzw. `position_aeklinie_b`
  (cm), Abstand auf der vorderen Linie ab der Schulterlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Zwei Buchvarianten
  stehen ausdrücklich nebeneinander (die einfache Diagonale und die vom Buch
  selbst „exakter" genannte Prozentregel); keine der beiden wird hier als
  Default gewählt.
- **Abhängigkeiten:** [[Ärmelkugelumfang-Formel]] (`formeln_s204.md`,
  Abschnitt 1).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Keine Stelle von Werner am Original bestätigt.
  - Nachrechnung Variante B: 44,5 · 0,48 = 21,36 ≈ 21,4 (passt zum
    Zeichnungswert). Variante A: 0,5 · 44,5 − 1 = 21,25 (nahe, aber nicht
    identisch mit 21,4 – laut Buch zwei unterschiedlich genaue Methoden, kein
    Fehler).

## Formel 8 – Einhalteweite in cm

- **Quelle:** [`formeln_s204.md`](formeln_s204.md), Abschnitt 1
- **Buchfassung:**
  ```text
  EW in % | Einhalteweite in % | 8 % | Einhalteweite in cm ≙ AlU ≙
  Einhalteweite in % | EW in cm | 3,3 cm
  ```
- **Technische Formel:**
  ```text
  EW_cm = AlU * EW_prozent
  ```
  (Verknüpfungszeichen „≙" im OCR nicht eindeutig; Nachrechnung stützt
  Multiplikation.)
- **Eingaben und Einheiten:** `AlU` (Armlochumfang, cm – Wert und Herkunft
  selbst laut s204.md-Prüfstelle 1 ungeklärt), `EW_prozent` (Einhalteweite in
  %, hier 8 %).
- **Ausgabe und Einheit:** `EW_cm` (Einhalteweite, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `EW_prozent` laut Buch
  frei wählbar („gewünschte Einhalteweite … bestimmen", `ocr_s204.md` Zeile
  18); kein fester Wert vorgeschrieben, 8 % nur Beispiel dieser Seite.
- **Abhängigkeiten:** [[Formel 9]] (ÄkU verwendet EW_cm weiter).
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Keine Stelle von Werner am Original bestätigt.
  - Wert und exakte Definition von `AlU` auf dieser Seite selbst
    widersprüchlich (s. Formel 6, gleiche Ungeklärtheit).
  - Nachrechnung 41,2 · 0,08 = 3,296 ≈ 3,3 stützt Multiplikation, ist aber
    keine Bestätigung des Buchsymbols „≙".

## Formel 9 – Ärmelkugelumfang

- **Quelle:** [`formeln_s204.md`](formeln_s204.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Ärmelkugelumfang ≙ AlU ≙ Einhalteweite in cm | ÄkU | 44,5
  ```
- **Technische Formel:**
  ```text
  ÄkU = AlU + EW_cm
  ```
- **Eingaben und Einheiten:** `AlU` (cm, siehe Formel 8), `EW_cm` (cm, siehe
  [[Formel 8]]).
- **Ausgabe und Einheit:** `ÄkU` (Ärmelkugelumfang, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – fester
  Rechenschritt laut Tabelle.
- **Abhängigkeiten:** [[Formel 8]], wird weiterverwendet in [[Formel 7]].
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Keine Stelle von Werner am Original bestätigt.
  - Gleiche `AlU`-Unklarheit wie Formel 8.
  - Nachrechnung 41,2 + 3,3 = 44,5 stützt Addition.

## Formel 10 – Armlochkontrolle (ArD)

- **Quelle:** [`formeln_s204.md`](formeln_s204.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Armloch kontrollieren: ArD = OaU: 10 · 6 - 7,5 cm
  ```
- **Technische Formel:** nicht gebildet – Buchfassung nicht eindeutig
  auflösbar (Reihenfolge Doppelpunkt/Punkt/Minus unklar, keine Klammerung
  erkennbar, keine Bildsichtung möglich).
- **Eingaben und Einheiten:** vermutlich `OaU` (Oberarmumfang, cm), unklar.
- **Ausgabe und Einheit:** vermutlich `ArD` (cm), auf dieser Seite nicht
  definiert.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** nicht ermittelbar.
- **Abhängigkeiten:** vermutlich Querverweis auf eine Formel des
  Oberteil-Grundschnitts (Text: „Das Armloch am Oberteil-Grundschnitt ggf.
  verbreitern"); Zielseite nicht ermittelt, nicht kopiert.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Keine Stelle von Werner am Original bestätigt.
  - OCR-Fassung der Formel selbst nicht eindeutig lesbar; keine Bildsichtung
    möglich, da diese Zeile außerhalb der erfassten Skizzenausschnitte liegt.
  - Bedeutung von „ArD" und „AlT" auf dieser Seite nicht definiert.
