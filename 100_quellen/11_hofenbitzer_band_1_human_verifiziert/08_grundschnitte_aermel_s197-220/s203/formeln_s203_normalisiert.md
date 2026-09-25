# Formeln normalisiert – s203 (vorläufig, Walking Skeleton)

Technische Fassung zu [formeln_s203.md](formeln_s203.md). Kein Abschnitt dort
ist laut [s203.md](s203.md) am Original bestätigt; alle Einträge unten stehen
deshalb auf `offen` oder `gesperrt`, unabhängig von der inhaltlichen Klarheit
der Buchfassung. Seite 203 gehört zu `08_grundschnitte_aermel_s197-220/`, das
vom Formelextraktions-Prompt formal nicht erfasste Kapitel — diese Datei
entstand auf ausdrücklichen Wunsch Werners als Walking-Skeleton-Durchlauf.
Diese Datei erzeugt keine Python-Funktion, keinen Engine-Vertrag und keine
neue Fachregel.

## F1 – Vorderer Ärmelpunkt (vÄP)

- **Quelle:** [formeln_s203.md](formeln_s203.md), Abschnitt 1.
- **Buchfassung:**
  ```text
  6 An der unteren Armelkurve die vAchsel auf die vA übertragen
  → vorderer Armelpunkt = vAP.
  ```
- **Technische Formel:** `vAP = vAchsel` (direkte Übertragung ohne Zuschlag,
  entlang der unteren Ärmelkurve auf die vordere Ärmelkantenlinie vA).
- **Eingaben und Einheiten:** `vAchsel` (cm; laut Zeichnung 4,5 cm, Herkunft
  vermutlich Vorseite dieser Konstruktion, nicht auf s203 definiert).
- **Ausgabe und Einheit:** `vAP` (Position auf vA, cm ab tP).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** `vAchsel` vermutlich aus vorangehender Seite
  (Grundgerüst-Konstruktion, außerhalb s203); Ausgangspunkt für Abschnitt 4
  (Saumhalbierung) und F4 unten.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Herkunft von `vAchsel` (welche Seite/Formel) ist hier nicht dokumentiert.

## F2 – Hinterer Ärmelpunkt (hÄP)

- **Quelle:** [formeln_s203.md](formeln_s203.md), Abschnitt 2.
- **Buchfassung:**
  ```text
  Die hAchsel + 20% der EW (0,3 cm) auf die hA übertragen
  → hinterer Armelpunkt = hAP.
  ```
  Zeichnungsgebundene Rechnung:
  ```text
  8,6 cm + 1,3 cm · 0,20
  8,6 cm + 0,3 cm
  = 8,9 cm
  ```
- **Technische Formel:** `hAP = hAchsel + 0,20 * EW`.
- **Eingaben und Einheiten:** `hAchsel` (cm; laut Zeichnung 8,6 cm); `EW`
  (cm; laut Zeichnung 1,3 cm — auf s203 nicht definiert, vermutlich von einer
  vorherigen Seite übernommen).
- **Ausgabe und Einheit:** `hAP` (Position auf hA, cm ab tP).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine — fester
  Prozentsatz 20 % laut Buchwortlaut.
- **Abhängigkeiten:** `hAchsel`, `EW` vermutlich aus vorangehender Seite;
  Ausgangspunkt für F3 (Knips) und Abschnitt 4 (Saumhalbierung).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Rechenprobe: `1,3 · 0,20 = 0,26`, gedruckt jedoch als `0,3 cm` (auch im
    OCR-Fließtext so wiederholt: „20% der EW (0,3 cm)"). Differenz von
    0,04 cm ist eine gedruckte Rundung, nicht als Fehler still korrigiert.
  - Herkunft von `EW` (welche Seite/Formel, gleiche oder andere Größe wie
    „Einhalteweite" auf s200) ist hier nicht dokumentiert und nicht
    unterstellt.

## F3 – Zweiter Knips (hinterer Ärmelbereich)

- **Quelle:** [formeln_s203.md](formeln_s203.md), Abschnitt 3.
- **Buchfassung:**
  ```text
  Ein zweiter Knips wird 1 cm oberhalb des hAP markiert.
  ```
- **Technische Formel:** `knips_2 = hAP + 1 cm` (Richtung: oberhalb, entlang
  hA).
- **Eingaben und Einheiten:** `hAP` (cm, aus F2).
- **Ausgabe und Einheit:** `knips_2` (Position auf hA, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine — fester Wert
  1 cm.
- **Abhängigkeiten:** F2 → F3.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## F4 – Saumhalbierung und ½ Ärmelsaumweite

- **Quelle:** [formeln_s203.md](formeln_s203.md), Abschnitt 4.
- **Buchfassung:**
  ```text
  7 Die Saumlinie halbieren. Von Dort jeweils die 1/2 Armelsaumweite (ASaW)
  nach links und rechts abtragen.
  ```
- **Technische Formel:**
  ```text
  saumkante_links  = saummitte - 0,5 * AeSaW
  saumkante_rechts = saummitte + 0,5 * AeSaW
  ```
- **Eingaben und Einheiten:** `AeSaW` (Ärmelsaumweite, cm; laut Zeichnung
  22 cm an dieser Stelle der Konstruktion).
- **Ausgabe und Einheit:** `saumkante_links`, `saumkante_rechts` (cm ab
  Saummitte).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine — feste
  Halbierung.
- **Abhängigkeiten:** F1/F2 (Ärmelkugelkonstruktion) liegen geometrisch
  darüber; `AeSaW = 22 cm` steht im Widerspruch zu `AeSaW = OaW = 37 cm` in
  `skizzen/s203_skizze_01.png` — vermutlich zwei verschiedene Konstruktions-
  stufen (Ärmelkugelhöhe vs. reduzierter Saum), auf s203 selbst nicht als
  eigene Rechnung hergeleitet.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Herleitung von `AeSaW = 22 cm` aus `AeSaW = OaW = 37 cm` fehlt auf s203;
    keine Rechenvorschrift für die Reduzierung von 37 cm auf 22 cm
    dokumentiert.

## Nicht separat normalisiert

- [formeln_s203.md](formeln_s203.md), Abschnitt 5 (Fadenlinie zur ÄkLi,
  rechtwinkliges Formen der Ärmelnähte ab Saum): geometrische Anweisung ohne
  eigenen Zahlenwert, deshalb keine eigene technische Formel.

## F5 – Kontrolle der Oberarmweite (OaW)

- **Quelle:** [formeln_s203.md](formeln_s203.md), Abschnitt 6.
- **Buchfassung:**
  ```text
  Die OaW kontrrollieren (hier 2 cm geringer, da zu Beginn der Konstruktion
  kein Ausgleichsbetrag addiert wurde).
  ```
- **Technische Formel:** `OaW_kontrolle_ist = OaW_soll - 2 cm` (in dieser
  Konstruktion; Abweichung laut Buchtext durch fehlenden Ausgleichsbetrag zu
  Konstruktionsbeginn erklärt).
- **Eingaben und Einheiten:** `OaW_soll` (Oberarmweite, cm; laut Zeichnung
  35 cm).
- **Ausgabe und Einheit:** `OaW_kontrolle_ist` (cm) — Kontrollwert, keine
  Konstruktionsgröße.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Abweichung von 2 cm
  ist laut Buchtext erklärt, aber nicht als wählbarer Bereich zu lesen —
  fester, beschriebener Konstruktionseffekt.
- **Abhängigkeiten:** `Ausgleichsbetrag` wird auf einer vorangehenden Seite
  dieser Konstruktion erwähnt (auf s203 nicht selbst hergeleitet).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Welche vorangehende Seite/Formel den „Ausgleichsbetrag" definiert, ist
    hier nicht dokumentiert.

## F6 – Mehrlänge im Bereich der Elle

- **Quelle:** [formeln_s203.md](formeln_s203.md), Abschnitt 7.
- **Buchfassung:**
  ```text
  Dieser weite, am Saum gekrauselte Hemdenärmel erhält, wie alle Ärmel mit
  Bündchen- oder Manschettenabschluss, eine Mehrlänge von 1,5 cm im Bereich
  der Elle.
  ```
- **Technische Formel:** `mehrlaenge_elle = 1,5 cm`, gültig für Ärmel mit
  Bündchen- oder Manschettenabschluss (Auswahlbedingung an Modelltyp).
- **Eingaben und Einheiten:** keine Rechengröße, fester Zuschlag (cm).
- **Ausgabe und Einheit:** `mehrlaenge_elle` (cm), addiert im
  Ellenbogenbereich.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bedingung
  „Bündchen- oder Manschettenabschluss" muss zutreffen; kein Bereich, fester
  Wert.
- **Abhängigkeiten:** Modelltyp-Auswahl (Bündchen/Manschette) außerhalb
  dieser Seite definiert.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob der zeichnungsgebundene Wert „1,5 cm" in `skizzen/s203_skizze_03.png`
    (Abschnitt 9 in [formeln_s203.md](formeln_s203.md)) dieselbe Größe ist,
    ist ungeklärt (siehe F8 unten).

## F7 – Schlitzposition

- **Quelle:** [formeln_s203.md](formeln_s203.md), Abschnitt 8.
- **Buchfassung:**
  ```text
  8 Die Schlitzposition bestimmen und einzeln.
  ```
  Zeichnungsgebundener Wert: „⅓ ÄSaW".
- **Technische Formel:** `schlitzposition = (1/3) * AeSaW`, gemessen von der
  hinteren Ärmelnaht (hÄN) am Saum Richtung Mitte.
- **Eingaben und Einheiten:** `AeSaW` (Ärmelsaumweite, cm; siehe F4).
- **Ausgabe und Einheit:** `schlitzposition` (cm ab hÄN, am Saum).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine — fester
  Bruchteil ⅓.
- **Abhängigkeiten:** F4 (`AeSaW`) → F7.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Buchtext („Die Schlitzposition bestimmen und einzeln.") nennt den Wert
    „⅓ ÄSaW" nicht selbst; er stammt ausschließlich aus der Zeichnung.

## F8 – Weitere Maße am Schlitz (ungeklärt)

- **Quelle:** [formeln_s203.md](formeln_s203.md), Abschnitt 9.
- **Buchfassung:** keine (nur zeichnungsgebunden, `skizzen/s203_skizze_03.png`):
  ```text
  1 cm (an der SuP-Mittellinie)
  1,5 cm (an der Schlitzlinie)
  ```
- **Technische Formel:** nicht ableitbar — Bedeutung und Bezugspunkt beider
  Maße sind aus Bild und Text allein nicht eindeutig.
- **Eingaben und Einheiten:** unklar.
- **Ausgabe und Einheit:** unklar.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** unklar.
- **Abhängigkeiten:** möglicherweise identisch mit F6 (Mehrlänge 1,5 cm),
  nicht bestätigt.
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob „1,5 cm" hier dieselbe Größe wie F6 (Mehrlänge im Bereich der Elle)
    ist oder ein eigenes Schlitzmaß, ist am Original zu klären.
  - Bedeutung von „1 cm" an der SuP-Mittellinie ist nicht dokumentiert und
    wird hier nicht geraten.
