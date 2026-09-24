# Formeln s191 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s191.md`](formeln_s191.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Armloch-Verbreiterung → Brustweite und Passformklasse (Beispiel)

- **Quelle:** [`formeln_s191.md`](formeln_s191.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Durch die Armloch-Verbreiterung, hier um 2 cm, vergrößert
  sich die Brustweite um 4 cm. So
  wird aus dem Grundschnitt mit PK
  3 ein Grundschnitt mit PK 5.
  ```
- **Technische Formel:**
  ```text
  brustweite_ganz_delta = 2 * armloch_verbreiterung_delta
  PK_neu = PK_alt + armloch_verbreiterung_delta   (1 Punkt pro 1 cm)
  ```
- **Eingaben und Einheiten:** `armloch_verbreiterung_delta` = 2 cm (Beispiel),
  `PK_alt` = 3 (Passformklasse, dimensionslos).
- **Ausgabe und Einheit:** `brustweite_ganz_delta` = 4 cm; `PK_neu` = 5.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** konkretes Rechenbeispiel,
  kein Bereich an dieser Stelle; der zulässige Bereich der
  Armloch-Verbreiterung steht in [[Formel 3]].
- **Abhängigkeiten:** [[Formel 3]] (Bereich/Aufteilung der
  Armloch-Verbreiterung), [[Formel 4]] (allgemeine Regel, aus der dieses
  Beispiel als Spezialfall folgt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unabhängig nachgerechnet: 2 cm × 2 (ganzer Schnitt) = 4 cm Brustweite und
    2 cm × 1 Punkt/cm = 2 PK-Punkte (3 → 5) stimmen intern mit der
    allgemeinen Regel aus Formel 4 überein.
  - Ob „die Brustweite" hier die ganze oder die halbe Brustweite meint, ist
    nur über den Vergleich mit Formel 4 erschlossen, nicht im Beispielsatz
    selbst benannt.

## Formel 2 – Armloch-Vertiefung → Armlochtiefe (AIT, Beispiel)

- **Quelle:** [`formeln_s191.md`](formeln_s191.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Durch die Armloch-Vertiefung,
  hier um 1,5 cm vergrößert sich die
  Armlochtiefe (AIT) um 1,5 cm.
  ```
- **Technische Formel:**
  ```text
  armlochtiefe_delta = armloch_vertiefung_delta
  ```
- **Eingaben und Einheiten:** `armloch_vertiefung_delta` = 1,5 cm (Beispiel).
- **Ausgabe und Einheit:** `armlochtiefe_delta` (AIT/AlT) = 1,5 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; 1:1-Beziehung im
  Beispiel.
- **Abhängigkeiten:** verwandt mit [[Formel 5]] (Armloch-Vertiefung als Anteil
  der Armloch-Verbreiterung), die denselben `armloch_vertiefung_delta`-Wert
  liefert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unklar, ob dies eine unabhängig geprüfte Rechenregel oder eine reine
    Definition ist (Armlochtiefen-Zunahme = Betrag der Armloch-Vertiefung).
  - OCR-Schreibweise „AIT" vs. vermutete Buchabkürzung „AlT" nicht am
    Original geklärt.

## Formel 3 – Armloch-Verbreiterung: Gesamtbereich und Aufteilung VT/RT

- **Quelle:** [`formeln_s191.md`](formeln_s191.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Das Armloch kann je nach ge-
  wünschter Passformklasse an
  der Seitennaht um insge-
  samt 1 bis 6 cm verbreitert
  werden: ⅓ am VT und ⅔ am
  RT.
  ```
- **Technische Formel:**
  ```text
  armloch_verbreiterung_gesamt ∈ [1 cm, 6 cm]
  armloch_verbreiterung_VT = (1/3) * armloch_verbreiterung_gesamt
  armloch_verbreiterung_RT = (2/3) * armloch_verbreiterung_gesamt
  ```
- **Eingaben und Einheiten:** `armloch_verbreiterung_gesamt` (cm), gewählt nach
  gewünschter Passformklasse.
- **Ausgabe und Einheit:** `armloch_verbreiterung_VT` (cm),
  `armloch_verbreiterung_RT` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 1 bis 6 cm
  bleibt Bereich, kein fester Default gewählt. Aufteilung ⅓/⅔ ist im
  Buchtext fest, nicht als „ca." markiert.
- **Abhängigkeiten:** liefert die Eingangsgröße für [[Formel 4]], [[Formel 5]],
  [[Formel 6]], [[Formel 7]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - „An der Seitennaht" bezogen auf den halben oder ganzen Grundschnitt nicht
    eindeutig; siehe dieselbe Unklarheit bei Formel 1/4.

## Formel 4 – Passformklasse und Brustweite je cm Armloch-Verbreiterung

- **Quelle:** [`formeln_s191.md`](formeln_s191.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Die Passformklasse (PK) vergrö-
  ßert sich um einen Punkt pro 1
  cm der Armloch-Verbreiterung.
  Am halben Grundschnitt vergrö-
  ßert sich die halbe Brustweite
  dabei ebenfalls um 1 cm. Am gan-
  zen Schnitt also um den doppel-
  ten Betrag.
  ```
- **Technische Formel:**
  ```text
  PK_delta            = armloch_verbreiterung_delta            (1 Punkt / cm)
  brustweite_halb_delta = armloch_verbreiterung_delta           (1 cm / cm)
  brustweite_ganz_delta = 2 * brustweite_halb_delta
  ```
- **Eingaben und Einheiten:** `armloch_verbreiterung_delta` (cm).
- **Ausgabe und Einheit:** `PK_delta` (Punkte), `brustweite_halb_delta` (cm),
  `brustweite_ganz_delta` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** vermutlich gültig im
  Rahmen des Bereichs aus [[Formel 3]] (1–6 cm), hier nicht erneut
  eingeschränkt.
- **Abhängigkeiten:** [[Formel 3]] liefert die Eingangsgröße; erzeugt das
  Beispiel in [[Formel 1]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 5 – Armloch-Vertiefung als Anteil der Armloch-Verbreiterung

- **Quelle:** [`formeln_s191.md`](formeln_s191.md), Abschnitt 5
- **Buchfassung:**
  ```text
  Das Armloch um ca. \(1 / 2\) bis \(3 / 4\) der Armloch-Verbreiterung vertiefen; die AIT wird groBer.
  ```
- **Technische Formel:**
  ```text
  armloch_vertiefung_delta = anteil * armloch_verbreiterung_gesamt
  anteil ∈ [ca. 1/2, ca. 3/4]
  ```
- **Eingaben und Einheiten:** `armloch_verbreiterung_gesamt` (cm, aus
  [[Formel 3]]).
- **Ausgabe und Einheit:** `armloch_vertiefung_delta` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich ½ bis ¾ bleibt
  Bereich, `ca.` erhalten, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel 3]] (Eingangsgröße); Ergebnis wird in
  [[Formel 2]] (Beispiel) und [[Formel 8]] (Ärmelpunkte-Verschiebung)
  weiterverwendet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob sich „der Armloch-Verbreiterung" auf den Gesamtwert oder auf den
    VT-/RT-Anteil aus Formel 3 bezieht, ist nicht eindeutig.

## Formel 6 – Schulter-Verbreiterung als Anteil der Armloch-Verbreiterung

- **Quelle:** [`formeln_s191.md`](formeln_s191.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Schulter-Verbreiterung um \(1 / 10\) der Armloch-Verbreiterung.
  ```
- **Technische Formel:**
  ```text
  schulter_verbreiterung = (1/10) * armloch_verbreiterung_gesamt
  ```
- **Eingaben und Einheiten:** `armloch_verbreiterung_gesamt` (cm, aus
  [[Formel 3]]).
- **Ausgabe und Einheit:** `schulter_verbreiterung` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Faktor 1/10,
  kein `ca.` im Buchtext.
- **Abhängigkeiten:** [[Formel 3]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 7 – BrB- und RüB-Vergrößerung beim Formen der neuen Armlöcher

- **Quelle:** [`formeln_s191.md`](formeln_s191.md), Abschnitt 7
- **Buchfassung:**
  ```text
  Beim Formen der neuen Armlocher die BrB um ca. \(1 / 8\) der Armloch-Verbreiterung
  und die RuB um ca. \(1 / 4\) der Armlochverbreiterung vergro-bern. Dabei konnen auch die Armlinien verschoben werden.
  ```
- **Technische Formel:**
  ```text
  BrB_delta  = anteil_BrB  * armloch_verbreiterung_gesamt,  anteil_BrB  ≈ 1/8
  RueB_delta = anteil_RueB * armloch_verbreiterung_gesamt,  anteil_RueB ≈ 1/4
  ```
- **Eingaben und Einheiten:** `armloch_verbreiterung_gesamt` (cm, aus
  [[Formel 3]]).
- **Ausgabe und Einheit:** `BrB_delta` (cm), `RueB_delta` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** beide Faktoren mit
  `ca.` markiert, kein fester Wert.
- **Abhängigkeiten:** [[Formel 3]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ausschreibung von „BrB" und „RüB"/„RuB" nicht gesichert (vermutlich
    Brustbreite/Rückenbreite), siehe Prüfstelle 7 in `s191.md`.
  - Bezugsgröße (Gesamt-Verbreiterung oder VT-/RT-Anteil aus Formel 3) nicht
    eindeutig.
  - Zusatzhinweis „Dabei können auch die Armlinien verschoben werden" ist eine
    Auswahlmöglichkeit ohne Zahlenwert, hier nicht als eigene Formel geführt.

## Formel 8 – Ärmelpunkte-Verschiebung nach unten

- **Quelle:** [`formeln_s191.md`](formeln_s191.md), Abschnitt 8
- **Buchfassung:**
  ```text
  Beide Armelpunkte um \(3 / 4\) der Armloch-Vertiefung nach unten verschiben.
  ```
- **Technische Formel:**
  ```text
  aermelpunkt_verschiebung = (3/4) * armloch_vertiefung_delta   (Richtung: nach unten)
  ```
- **Eingaben und Einheiten:** `armloch_vertiefung_delta` (cm, aus
  [[Formel 5]]).
- **Ausgabe und Einheit:** `aermelpunkt_verschiebung` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Faktor 3/4, kein
  `ca.` im Buchtext.
- **Abhängigkeiten:** [[Formel 5]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 9 – Neue Seitennähte parallel zu den alten (geometrische Beziehung)

- **Quelle:** [`formeln_s191.md`](formeln_s191.md), Abschnitt 9
- **Buchfassung:**
  ```text
  Die neuen Seitennahte parallel zu den alten Seitennahten zeichnen (gepunktete Linie), Nahtlingen kontrollieren.
  ```
- **Technische Formel:**
  ```text
  seitennaht_neu = parallel_offset(seitennaht_alt, betrag = ?)
  ```
- **Eingaben und Einheiten:** `seitennaht_alt` (Kurve/Linie).
- **Ausgabe und Einheit:** `seitennaht_neu` (parallel verschobene Linie).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Zahlenwert an
  dieser Stelle im Buchtext genannt.
- **Abhängigkeiten:** möglicherweise [[Formel 10]] (Betrag der Verschiebung
  könnte aus der Hüftweiten-Reduzierung folgen), nicht bestätigt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Der Verschiebungsbetrag ist an dieser Stelle nicht angegeben; ob er sich
    aus der neuen Armlochkontur ergibt oder eigenständig gewählt wird, ist
    unklar.

## Formel 10 – Hüftweite-Reduzierung an der Seitennaht (Beispiel)

- **Quelle:** [`formeln_s191.md`](formeln_s191.md), Abschnitt 10
- **Buchfassung:**
  ```text
  Die Hüftweite kann nach der Verbreiterung wieder reduziert werden (hier an der Seitennaht um 0,5 cm, das sind insgesamt 2 cm Reduzierung).
  ```
- **Technische Formel:**
  ```text
  hueftweite_reduktion_je_seitennaht = 0,5 cm   (Beispiel)
  hueftweite_reduktion_gesamt        = 2 cm     (Beispiel, "insgesamt")
  ```
- **Eingaben und Einheiten:** `hueftweite_reduktion_je_seitennaht` (cm).
- **Ausgabe und Einheit:** `hueftweite_reduktion_gesamt` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „kann... reduziert
  werden" – optionale Maßnahme, kein Zwang; 0,5 cm ist ein Beispielwert
  („hier"), kein Buchdefault.
- **Abhängigkeiten:** möglicherweise [[Formel 9]] (Parallelverschiebung der
  Seitennaht).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unabhängig nachgerechnet: 2 cm ÷ 0,5 cm = 4 – der Buchtext erklärt nicht,
    welche vier Nahtkanten oder Bezugspunkte hier gemeint sind (vermutlich je
    zwei Seitennähte an VT und RT, aber nicht belegt).
