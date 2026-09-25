# Formeln normalisiert – s218 (vorläufig, Walking Skeleton)

Technische Fassung zu [formeln_s218.md](formeln_s218.md). Keine der Formeln
F1–F7 ist laut [s218.md](s218.md) am Original bestätigt — die ganze Seite steht
dort noch als `OCR-Rohfassung – noch nicht menschlich verifiziert`. Diese Datei
stammt aus einem Walking-Skeleton-Durchlauf auf ausdrücklichen Wunsch Werners
(Blocker „Kapitel 08 nicht im Formel-Prompt vorgesehen" und Blocker
„Seite nicht menschlich verifiziert" wurden bewusst übersprungen). Sie erzeugt
keine Python-Funktion, keinen Engine-Vertrag und keine neue Fachregel.

## F1 – Neues Armloch (AlU)

- **Quelle:** [formeln_s218.md](formeln_s218.md), Abschnitt 1.
- **Buchfassung:**
  ```text
  AlU = vorderes Armloch + hinteres Armloch
  hier = 24,2 cm + 26 cm = 50,2 cm
  ```
- **Technische Formel:** `AlU = armloch_vorne + armloch_hinten`
- **Eingaben und Einheiten:** `armloch_vorne` (cm, gemessen am neuen/erweiterten
  Armloch), `armloch_hinten` (cm, gemessen).
- **Ausgabe und Einheit:** `AlU` (Armlochumfang neu, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine — feste
  Summenbildung aus zwei Messwerten.
- **Abhängigkeiten:** Eingabe für F3 (neuer Ärmelkugelumfang) und F4
  (Fehlweite).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Rechenbeispiel nachgerechnet: `24,2 + 26 = 50,2` — stimmt mit dem
    gedruckten Ergebnis überein.

## F2 – Ärmelkugelumfang des vorhandenen Ärmels (ÄkU_ALT)

- **Quelle:** [formeln_s218.md](formeln_s218.md), Abschnitt 2.
- **Buchfassung:**
  ```text
  2 Den Ärmelkugelumfang (ÄkUAC) des vorhandenen Ärmels messen und am Ärmel
  notieren:
  hier ÄkUACT = 48,5 cm
  ```
- **Technische Formel:** keine Berechnung — reiner Messwert:
  `ÄkU_ALT = 48,5 cm` (Beispielwert).
- **Eingaben und Einheiten:** direkt am vorhandenen Ärmel gemessen, cm.
- **Ausgabe und Einheit:** `ÄkU_ALT` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** Eingabe für F4 (Fehlweite).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Variablenname im Rohtext uneinheitlich (`ÄkUAC` / `ÄkUACT`); vermutete
    Lesung `ÄkU_ALT` (siehe `s218.md`, Prüfstelle 2, und
    `skizzen_s218.json`/`skizze_02`: „ÄkU_ALT messen = 48,5 cm") ist nicht
    bestätigt.

## F3 – Neuer Ärmelkugel-Umfang (ÄkU_NEU)

- **Quelle:** [formeln_s218.md](formeln_s218.md), Abschnitt 3.
- **Buchfassung:**
  ```text
  ÄkUABC = AlU · (100% + EW in %) : 100%
  hier = 50,2 cm · (100% + 7%) : 100%
  = 50,2 cm · 1,07
  ÄkUABC = 53,7 cm
  ```
- **Technische Formel:** `ÄkU_NEU = AlU * (1 + EW_pct / 100)`
- **Eingaben und Einheiten:** `AlU` (cm, aus F1); `EW_pct` (Einhalteweite in %,
  fachlich nach Stoffqualität bestimmt — Buchbeispiel nennt 7 %; laut Text
  alternativ auch in cm bestimmbar, dann anderer Rechenweg als hier
  normalisiert).
- **Ausgabe und Einheit:** `ÄkU_NEU` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `EW_pct` ist keine feste
  Buchvorgabe, sondern eine fachliche Auswahl je nach Stoffqualität; kein
  Bereich oder Default im Buchtext genannt außer dem Beispielwert 7 %.
- **Abhängigkeiten:** [[F1]] → F3 → [[F4]].
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Rechenbeispiel nachgerechnet: `50,2 · 1,07 = 53,714`, gedruckt gerundet auf
    `53,7 cm` — stimmt überein.
  - Variablenname im Rohtext uneinheitlich (`ÄkUABC` hier, `ÄkUADC` an anderer
    Stelle der Seite); vermutete Lesung `ÄkU_NEU` nicht bestätigt.
  - Der alternative Rechenweg „Einhalteweite auch in cm bestimmbar" ist im
    Buchtext nur erwähnt, aber nicht als eigene Formel ausformuliert — hier
    nicht ergänzt.

## F4 – Fehlweite

- **Quelle:** [formeln_s218.md](formeln_s218.md), Abschnitt 4.
- **Buchfassung:**
  ```text
  Fehlweite = ÄkUACT - ÄkUABC
  hier = 48,5 cm - 53,7 cm
  = -5,2 cm → Fehlweite = 5,2 cm
  ```
- **Technische Formel:** `Fehlweite = abs(ÄkU_ALT - ÄkU_NEU)`
- **Eingaben und Einheiten:** `ÄkU_ALT` (cm, aus F2), `ÄkU_NEU` (cm, aus F3).
- **Ausgabe und Einheit:** `Fehlweite` (cm, als Betrag).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[F2]], [[F3]] → F4.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Rechenbeispiel nachgerechnet: `48,5 - 53,7 = -5,2`, `abs(-5,2) = 5,2` —
    stimmt mit dem gedruckten Vorzeichenwechsel überein.
  - Ob `Fehlweite` in der Engine immer als Betrag (wie hier normalisiert) oder
    vorzeichenbehaftet (Richtung alt→neu) geführt werden soll, ist aus dem
    Buchtext allein nicht eindeutig — die Buchfassung zeigt beide Schreibweisen
    nebeneinander.

## F5 – Schulterpolster-Öffnung vorne (⅓ der Erhöhung)

- **Quelle:** [formeln_s218.md](formeln_s218.md), Abschnitt 5.
- **Buchfassung:**
  ```text
  3 Die Kugel wird waagerecht um ca. ⅓ der Polstererhöhung geöffnet.
  hier Öffnung = 2,5 cm : 3 = 0,8 cm
  ```
- **Technische Formel:** `Oeffnung_vorne = SuPoE / 3`
- **Eingaben und Einheiten:** `SuPoE` (Schulterpolster-Erhöhung, cm;
  Beispielwert 2,5 cm laut `skizzen_s218.json`/`skizze_01`, Beschriftung
  „Schulterpolster-Erhöhung = 2,5 cm").
- **Ausgabe und Einheit:** `Oeffnung_vorne` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Buchwortlaut „ca. ⅓" —
  Näherung, kein exakter Bruch als feste Regel; `ca.` bleibt erhalten.
- **Abhängigkeiten:** Eingabe für F6 (Mehrweite gesamt).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Rechenbeispiel nachgerechnet: `2,5 : 3 = 0,8333…`, gedruckt gerundet auf
    `0,8 cm` — stimmt mit der Zeichnungsbeschriftung „⅓ Schulterpolster-Erhöhung
    vorne hier 0,8 cm" überein.

## F6 – Mehrweite gesamt (⅔ der Erhöhung)

- **Quelle:** [formeln_s218.md](formeln_s218.md), Abschnitt 6.
- **Buchfassung:**
  ```text
  Diese Öffnung erzielt insgesamt ca. die doppelte Mehrweite an der linken und
  an der rechten Ärmelkugel:
  hier
  2 · ⅓ SuPoE = ⅔ SuPoE → ⅔ von 2,5 cm = ca. 1,7 cm
  ```
- **Technische Formel:** `Mehrweite_gesamt = 2 * (SuPoE / 3)` bzw. gleichwertig
  `(2/3) * SuPoE`
- **Eingaben und Einheiten:** `SuPoE` (cm, wie F5).
- **Ausgabe und Einheit:** `Mehrweite_gesamt` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Buchwortlaut „ca." —
  Näherung erhalten.
- **Abhängigkeiten:** [[F5]] (gleicher SuPoE-Eingabewert).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Rechenbeispiel nachgerechnet: `2,5 · 2/3 = 1,6667…`, gedruckt gerundet auf
    `ca. 1,7 cm` — stimmt überein.
  - Widerspruch zwischen Fließtext und Zeichnung: Der Fließtext beschreibt
    `⅔ SuPoE` als „insgesamt … doppelte Mehrweite an der linken und rechten
    Ärmelkugel" (ein Gesamtwert für beide Seiten zusammen), während
    `skizzen_s218.json`/`skizze_01` denselben Wert `1,7 cm` explizit als „⅔
    Schulterpolster-Erhöhung **hinten**" beschriftet (neben `0,8 cm` als „⅓ …
    **vorne**"). Ob `1,7 cm` ein Gesamtwert oder ein lokaler Wert nur für die
    hintere Seite ist, ist am Original zu klären — hier nicht aufgelöst.

## F7 – Kapplänge an der Ärmelkugel (Einschnittlinie)

- **Quelle:** [formeln_s218.md](formeln_s218.md), Abschnitt 7.
- **Buchfassung:**
  ```text
  2 Die Armelkugel bei ca. 5 cm kappen und
  wie dargestellt, bis zum Saum einschneiden.
  ```
- **Technische Formel:** keine Rechenformel — geometrische Konstruktions-
  anweisung: Kapppunkt bei Abstand `kapplaenge ≈ 5 cm` ab einem in der
  Zeichnung markierten Bezugspunkt (Punkt ③ laut `skizzen_s218.json`,
  `skizze_02`); anschließend Einschnitt „wie dargestellt" bis zum Saum, dessen
  genauer Linienverlauf nur aus der Zeichnung selbst hervorgeht.
- **Eingaben und Einheiten:** Bezugspunkt an der Ärmelkugel (aus Zeichnung,
  nicht textlich definiert).
- **Ausgabe und Einheit:** `kapplaenge` (cm, Näherungswert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca. 5 cm` bleibt
  Näherung, kein fester Wert.
- **Abhängigkeiten:** Geometrie aus `skizze_02`; kein textlicher Bezug zu
  F1–F6.
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Der genaue Einschnittverlauf („wie dargestellt … bis zum Saum") ist ohne
    geometrische Vermessung der Zeichnung nicht in eine Formel überführbar;
    Status deshalb `gesperrt` statt nur `offen`, bis eine Zeichnungsauswertung
    vorliegt.
