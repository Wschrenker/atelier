# Formeln s052 – Normalisierung

**Vorbehalt:** Seite noch nicht menschlich verifiziert, Extraktion noch nicht
am Original bestätigt (siehe [formeln_s052.md](formeln_s052.md) und
[s052.md](s052.md)). Diese Normalisierung wurde auf Werners ausdrücklichen
Wunsch als Walking Skeleton vor der Bestätigung erstellt. Alle Formeln unten
sind daher zusätzlich zu ihrem fachlichen Status als „technisch vorläufig,
Buchbestätigung aussteht" zu behandeln.

## Formel 1 – Taillenvertiefung vM/hM mit Seitennaht-Zuschlag

- **Quelle:** [formeln_s052.md](formeln_s052.md), Abschnitt 1
- **Buchfassung:**

  ```text
  Da bei einem Rock mit einer kleinen Taillenvertiefung (bis ca. 4 cm) häufig
  der Bund noch waagerecht liegt, kann vorne und hinten jeweils derselbe
  Betrag entfernt werden, an der Seitennaht zusätzlich ca. 10 %.

  Beispiel: Vertiefung an vM und hM je 3 cm, an den SN 3,3 cm.

  seitliche Taillenvertiefung
  bis 4 cm
  + 10 %
  = 4,4 cm
  ```

- **Technische Formel:** `v_SN = v_vM_hM * 1,10` (v_vM_hM ≤ ca. 4 cm)
- **Eingaben und Einheiten:** `v_vM_hM` – Taillenvertiefung an vM/hM, in cm,
  Bereich bis ca. 4 cm.
- **Ausgabe und Einheit:** `v_SN` – Taillenvertiefung an der Seitennaht, in
  cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Nur anwendbar, wenn
  „der Bund noch waagerecht liegt" (fachliche Vorbedingung, nicht weiter
  quantifiziert). Obergrenze für `v_vM_hM` ist „bis ca. 4 cm" – als Bereich
  belassen, kein fester Grenzwert im Buch angegeben.
- **Abhängigkeiten:** Siehe Buchverweis „Seite 38, 50, 51" im Fließtext
  (ocr_s052.md, Zeile 28) – nicht kopiert, nur als Verweis vermerkt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Beide Beispielrechnungen (3 cm → 3,3 cm
  und 4 cm → 4,4 cm) sind mit `* 1,10` konsistent nachrechenbar. Ob „ca. 10 %"
  gerundet oder exakt gemeint ist, sagt das Buch nicht; Rundungsregel offen.

## Formel 2 – Mindestreduzierung der oberen Rockkante (Taillenzugabe)

- **Quelle:** [formeln_s052.md](formeln_s052.md), Abschnitt 2
- **Buchfassung:**

  ```text
  ① Die Weite der oberen Rockkante muss in jedem Fall mindestens um die
  Taillenzugabe des Grundschnitts von 0,5 bis 1 cm am halben Rock (besser
  noch mehr) reduziert werden.
  ```

- **Technische Formel:** `reduzierung_min = Taillenzugabe_GS` (Untergrenze,
  „besser noch mehr" bleibt unquantifiziert)
- **Eingaben und Einheiten:** `Taillenzugabe_GS` – Taillenzugabe des
  Grundschnitts, in cm, Bereich 0,5 bis 1 cm, bezogen auf den halben Rock.
- **Ausgabe und Einheit:** Mindestreduzierung der oberen Rockkantenweite, in
  cm, am halben Rock.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 0,5–1 cm ist
  eine Untergrenze, kein fester Wert; „besser noch mehr" ist eine
  Fachempfehlung ohne Obergrenze – nicht durch einen Default ersetzt.
- **Abhängigkeiten:** Bezieht sich auf den nicht auf dieser Seite
  dokumentierten Grundschnitt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Laut s052.md ist unklar, ob die
  Schrittkennung „①" hier überhaupt eine Schrittnummer oder nur ein
  Warnsymbol im Original ist. Betrifft nur die Kennzeichnung, nicht den
  Formelinhalt.

## Formel 3 – Beispielrechnung ☐4 (kleine Taillenvertiefung, ein Wert)

- **Quelle:** [formeln_s052.md](formeln_s052.md), Abschnitt 3
- **Buchfassung:**

  ```text
  1 ☐4 Die Abtrennung für eine kleine Taillenvertiefung kann an vM und hM
  bis zu 4 cm erfolgen (hier 3 cm). An der Seitennaht + 10% (hier 3,3 cm).
  Die Abtrennlinie optisch parallel zur Taillennaht zeichnen.
  ```

- **Technische Formel:** Spezialfall von Formel 1 mit `v_vM_hM = 3 cm` →
  `v_SN = 3 * 1,10 = 3,3 cm`. Unabhängig nachgerechnet: stimmt.
- **Eingaben und Einheiten:** `v_vM_hM` in cm, Bereich bis 4 cm, hier
  Beispielwert 3 cm.
- **Ausgabe und Einheit:** `v_SN` in cm, hier Beispielwert 3,3 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „Abtrennlinie optisch
  parallel zur Taillennaht zeichnen" ist eine geometrische Zusatzregel ohne
  Zahlenwert – als fachliche Auswahlspielraum-Anweisung erhalten, nicht
  quantifiziert.
- **Abhängigkeiten:** [[Formel 1]] (gleiche Beziehung, gleicher Beleg).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** Keine; Beispiel ist rechnerisch
  konsistent mit Formel 1 und dient nicht als Beweis für eine andere
  Buchformel.

## Formel 4 – Zweiter Abnäher (Inhalt und Länge)

- **Quelle:** [formeln_s052.md](formeln_s052.md), Abschnitt 4
- **Buchfassung:**

  ```text
  2 Die zweiten Abnäher in VT und RT mit 0,5 bis 0,7 cm Inhalt und 7 bis 9 cm
  Länge wie skizziert an der Taille einzeichnen.
  ```

- **Technische Formel:** Keine Rechenformel, sondern zwei unabhängige
  Bemaßungsbereiche für ein geometrisches Element (zweiter Abnäher).
- **Eingaben und Einheiten:** Keine Eingabegröße im Sinne einer Berechnung.
- **Ausgabe und Einheit:** `abnaeher_inhalt` in cm, Bereich 0,5–0,7 cm;
  `abnaeher_laenge` in cm, Bereich 7–9 cm. Beide gelten je für VT und RT.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Beide Bereiche bleiben
  Bereiche, kein Default gewählt. Lage „an der Taille, wie skizziert" ist
  zeichnungsgebunden (skizze_03/skizze_04) und nicht weiter quantifiziert.
- **Abhängigkeiten:** Keine zu anderen Formeln dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Keine Auswahlregel im Buch, wie
  innerhalb der Bereiche zu wählen ist (z. B. nach Rockweite oder
  Kundenmaß).

## Formel 5 – Sonderfall zwei RT-Abnäher (kein dritter Abnäher)

- **Quelle:** [formeln_s052.md](formeln_s052.md), Abschnitt 5
- **Buchfassung:**

  ```text
  3 ☐5 Bei einem Rock-GS mit zwei Abnähern im RT muss kein dritter Abnäher
  gezeichnet werden. Man kann zusätzlich etwas an der Seitennaht reduzieren.
  Optional wäre auch eine Vergrößerung des 2. hinteren Abnähers möglich
  (hier nicht gezeigt).
  ```

- **Technische Formel:** Keine Zahlenformel; eine Auswahlregel mit zwei
  optionalen, unquantifizierten Alternativen (zusätzliche
  Seitennaht-Reduzierung ODER Vergrößerung des 2. hinteren Abnähers).
- **Eingaben und Einheiten:** Keine.
- **Ausgabe und Einheit:** Keine quantifizierte Ausgabe.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bedingung: Rock-GS mit
  bereits zwei RT-Abnähern. Auswahlspielraum zwischen zwei Optionen bleibt
  offen, „etwas" und „Vergrößerung" sind nicht beziffert.
- **Abhängigkeiten:** Betrifft die gleiche Seitennaht-Reduzierung wie
  [[Formel 7]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Keine Zahl angegeben; nicht
  quantifizierbar ohne weitere Buchstelle.

## Formel 6 – Belegbreite

- **Quelle:** [formeln_s052.md](formeln_s052.md), Abschnitt 6
- **Buchfassung:**

  ```text
  4 ☐4-5 Parallel zur Taillenvertiefung bzw. zur neuen oberen Rockkante und
  rechtwinklig zur vM und hM wird die Belegbreite von 4 bis 6 cm
  eingezeichnet.
  ```

- **Technische Formel:** Keine Rechenformel; ein Bemaßungsbereich für ein
  geometrisches Element (Taillenbeleg).
- **Eingaben und Einheiten:** Keine Eingabegröße im Sinne einer Berechnung.
- **Ausgabe und Einheit:** `belegbreite` in cm, Bereich 4–6 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich bleibt
  Bereich. Geometrische Bedingung: parallel zur neuen oberen Rockkante,
  rechtwinklig zu vM/hM.
- **Abhängigkeiten:** Setzt die neue obere Rockkante nach Formel 1/3 voraus.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** OCR-Label „☐4-5" könnte laut s052.md
  im Original „☐4+5" heißen; betrifft nur die Bildreferenz, nicht den
  Zahlenwert.

## Formel 7 – Zusätzliche Weiten-Reduzierung an der Seitennaht

- **Quelle:** [formeln_s052.md](formeln_s052.md), Abschnitt 7
- **Buchfassung (Fließtext):**

  ```text
  Zusätzliche Weiten-Reduzierung an der Seitennaht nach Bedarf vornehmen
  (insgesamt ca. 0 bis 0,5 cm)
  ```

- **Buchfassung (Zeichnung, nur skizze_04):**

  ```text
  Zusätzliche Weiten-Reduzierung an der Seitennaht nach Bedarf vornehmen
  (insgesamt ca. 0 bis 1 cm)
  alternativ auch am 2. hinteren Abnäher
  ```

- **Technische Formel:** Keine Rechenformel; ein Zusatzbetrag „nach Bedarf"
  ohne feste Auswahlregel.
- **Eingaben und Einheiten:** Keine Eingabegröße.
- **Ausgabe und Einheit:** `zusatz_reduzierung_SN` in cm – laut Fließtext
  Bereich ca. 0–0,5 cm, laut Zeichnung (skizze_04) Bereich ca. 0–1 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „nach Bedarf" bleibt
  unquantifiziert. Zeichnung nennt zusätzlich eine Alternative am 2.
  hinteren Abnäher, die im Fließtext an dieser Stelle nicht vorkommt.
- **Abhängigkeiten:** Ergänzt [[Formel 5]] (gleiche Seitennaht-Reduzierung
  im Sonderfall zwei RT-Abnäher).
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** Fließtext und Zeichnung nennen
  unterschiedliche Obergrenzen (0,5 cm vs. 1 cm) für denselben Betrag; dazu
  kommt die in s052.md dokumentierte Schrittkennungs-Unsicherheit (blaue „5"
  im Original vs. „6" in der OCR) an genau dieser Textstelle. Keine der
  beiden Fassungen wurde als Fehler behandelt; Auflösung braucht Werners
  Prüfung am Original.
