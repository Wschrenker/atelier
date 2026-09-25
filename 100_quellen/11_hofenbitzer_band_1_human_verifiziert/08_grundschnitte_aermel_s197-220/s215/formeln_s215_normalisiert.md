# Formeln s215 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s215.md`](formeln_s215.md) vermerkt, ist keine
Rechenstelle dieser Seite von Werner am Original bestätigt. Alle Formeln
stehen deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung der Stellen am Original.

## Formel 1 – Abstand der neuen Ärmelnaht vom vÄBr

- **Quelle:** [`formeln_s215.md`](formeln_s215.md), Abschnitt 1
- **Buchfassung:**
  ```text
  1 ☐5 Eine neue Ärmelnaht im Abstand von 1,5 bis 2,5 cm vom vÄBr entfernt einzeichnen.
  ```
- **Technische Formel:**
  ```text
  abstand_neue_naht = vÄBr + zugabe
  zugabe ∈ [1,5 cm, 2,5 cm]
  ```
- **Eingaben und Einheiten:** `vÄBr` (vordere Ärmelbreite, cm, aus
  vorangehender Konstruktion, auf s215 nicht neu bestimmt).
- **Ausgabe und Einheit:** `abstand_neue_naht` (cm), Lage der neuen Ärmelnaht
  relativ zu vÄBr.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „1,5 bis
  2,5 cm“ bleibt Bereich; kein Auswahlkriterium für den konkreten Wert auf
  dieser Seite angegeben.
- **Abhängigkeiten:** `vÄBr` aus vorangehender Ärmelkonstruktion (verlinkt,
  nicht kopiert); [[Formel 4]] (dieselbe neue Ärmelnaht wird dort verschoben
  und geschlossen).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt.

## Formel 2 – Knipse-Abstand von der Ellenbogenlinie

- **Quelle:** [`formeln_s215.md`](formeln_s215.md), Abschnitt 2
- **Buchfassung:**
  ```text
  4 An die neue Ärmelnaht Knipse im Anstand von 6 bis 8 cm oberhalb und unterhalb der Ellenbogenlinie anbringen.
  ```
- **Technische Formel:**
  ```text
  knipse_position = ellenbogenlinie ± abstand
  abstand ∈ [6 cm, 8 cm]
  ```
- **Eingaben und Einheiten:** `ellenbogenlinie` (Bezugslinie aus
  Grundkonstruktion, auf s215 nicht neu bestimmt).
- **Ausgabe und Einheit:** `knipse_position` (cm, zwei Punkte: oberhalb und
  unterhalb der Ellenbogenlinie).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „6 bis 8 cm“
  bleibt Bereich; kein Auswahlkriterium für den konkreten Wert auf dieser
  Seite angegeben. Gilt beidseitig (oberhalb und unterhalb) laut Zeichnung.
- **Abhängigkeiten:** [[Formel 1]] (Knipse liegen an der in Formel 1
  bestimmten neuen Ärmelnaht).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt.

## Formel 3 – Lücke an der hinteren Ärmelnaht entspricht Dehnbetrag vorne

- **Quelle:** [`formeln_s215.md`](formeln_s215.md), Abschnitt 4
- **Buchfassung:**
  ```text
  8 Die Lücke an der hinteren Ärmelnaht entspricht dem Dehnbetrag an der vorderen Ärmelnaht. Die neue hintere Ärmelnaht schließen.
  ```
- **Technische Formel:**
  ```text
  luecke_hinten = dehnbetrag_vorne
  ```
- **Eingaben und Einheiten:** `dehnbetrag_vorne` (cm) – der Betrag, um den
  sich die vordere Ärmelnaht beim Abtrennen und Verschieben der Schnittfläche
  gedehnt hat. Auf s215 nicht als eigener Zahlenwert oder Formel angegeben,
  sondern als Ergebnis der vorangehenden Konstruktionsschritte (Formel 1/2
  sowie das Verschieben selbst).
- **Ausgabe und Einheit:** `luecke_hinten` (cm), zu schließende Lücke an der
  neuen hinteren Ärmelnaht.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; feste
  Gleichheitsbeziehung laut Buchtext.
- **Abhängigkeiten:** [[Formel 1]], [[Formel 2]] (bestimmen indirekt den
  Dehnbetrag vorne); Neubestimmung von hÄP/SuP (Seite 208, verlinkt, nicht
  kopiert) als Folgeschritt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt. Wie `dehnbetrag_vorne` konkret aus den
  vorangehenden Schritten berechnet wird (z. B. als Differenz zweier
  Bogenlängen), ist auf s215 nicht explizit angegeben.

## Formel 4 – ⅛ Armloch-Verbreiterung (nur Zeichnung)

- **Quelle:** [`formeln_s215.md`](formeln_s215.md), Abschnitt 6
- **Buchfassung:**
  ```text
  ⅛ Armloch-Verbreiterung (Beschriftung in skizzen/s215_skizze_01.png, Punkt 5, kein Fließtext auf dieser Seite)
  ```
- **Technische Formel:**
  ```text
  verschiebung_punkt5 = armloch_verbreiterung / 8
  ```
- **Eingaben und Einheiten:** `armloch_verbreiterung` (cm) – vermutlich der
  auf einer früheren Seite festgelegte Gesamtbetrag der Armloch-Verbreiterung;
  auf s215 selbst nicht benannt oder verlinkt.
- **Ausgabe und Einheit:** `verschiebung_punkt5` (cm), Verschiebung an Punkt 5
  der oberen Zeichnung.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine auf dieser
  Seite.
- **Abhängigkeiten:** `armloch_verbreiterung` vermutlich aus vorangehender
  Seite (Ärmelanpassung nach Armloch-Vertiefung/-Verbreiterung, Seiten
  212/213 laut Seitentitel), auf s215 nicht verlinkt oder beziffert.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kein begleitender Fließtext auf s215 vorhanden; Quelle und Zahlenwert von
    `armloch_verbreiterung` sind auf dieser Seite nicht angegeben. Ohne
    Klärung der Ursprungsseite bleibt diese Formel gesperrt.

## Nicht normalisiert (siehe `formeln_s215.md`, „Nicht als Formel erfasst“)

- Abschnitt „2 Ärmelanpassung durchführen“: reiner Verweis auf die Verfahren
  der Seiten 212, 213 und 209, keine eigene Rechenbeziehung auf dieser Seite.
- Schritt „Schnittfläche abtrennen“ (formeln_s215.md, Abschnitt 3): reine
  Arbeitsanweisung ohne Zahlenwert.
- Neubestimmung von hÄP/SuP (formeln_s215.md, Abschnitt 5): Verweis auf
  Seite 208, keine eigene Formel auf dieser Seite.
- Randmarkierungen, Reiterzeichenfolgen und Bildunterschriften: keine
  Formeln.
