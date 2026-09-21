# Formeln s059 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s059.md`](formeln_s059.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle vier Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Innenbund-Reduzierung

- **Quelle:** [`formeln_s059.md`](formeln_s059.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Die beiden Formbundteile werden gespiegelt kopiert und die Weite reduziert

  Innenbund-Teile mit Weiten- und Breiten-Reduziierung um ca. 0,2 cm
  ```
- **Technische Formel:**
  ```text
  weite_neu  = weite_alt  - delta
  breite_neu = breite_alt - delta
  delta ≈ 0,2 cm  (ca.)
  ```
- **Eingaben und Einheiten:** `weite_alt` (cm), `breite_alt` (cm) der kopierten
  Formbundteile; `delta` ≈ 0,2 cm.
- **Ausgabe und Einheit:** `weite_neu`, `breite_neu` (cm), Innenbund-Teile.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` vor dem Wert
  erhalten – kein fester Betrag laut Buch. Unklar, ob `delta` einmal insgesamt
  oder je Formbundteil/-seite abgezogen wird (Teile werden „gespiegelt
  kopiert").
- **Abhängigkeiten:** Ausgangsteile sind Kopien der Formbundteile aus ☐5 (laut
  Bildunterschrift auf s059 selbst); genaue Vorlage nicht auf dieser Seite
  benannt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob `delta` auf Weite und Breite je einzeln oder gemeinsam wirkt, ist aus dem
    Wortlaut nicht eindeutig.
  - Zahlenwert 0,2 cm steht nur in der Bildunterschrift ☐6, nicht im
    Schrittfließtext – Zusammenhang plausibel, aber nicht Buchtext-identisch
    belegt.

## Formel 2 – Saumkürzung Futter-Rockteile

- **Quelle:** [`formeln_s059.md`](formeln_s059.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die beiden Rockteile ohne Formbund (aber mit der Passenfläche) werden aus ☐2
  kopiert und am Saum um 2 cm gekürzt sowie an vM, bzw. hM gespiegelt (hier für
  günstigen Zuschnitt mit hM-Naht).
  ```
- **Technische Formel:**
  ```text
  saum_neu = saum_alt - 2 cm
  ```
- **Eingaben und Einheiten:** `saum_alt` (cm), Saumlänge/-position der aus ☐2
  kopierten Rockteile ohne Formbund.
- **Ausgabe und Einheit:** `saum_neu` (cm), Saum der Futter-Rockteile.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert „2 cm" ohne
  `ca.` – kein Spielraum laut Buchwortlaut. Zusätzlich Spiegelung an vM bzw. hM
  (Auswahl abhängig von Zuschnittvariante), hier nicht weiter quantifiziert.
- **Abhängigkeiten:** Ausgangsteile stammen aus ☐2 – dieser Verweis liegt nicht
  auf s059; Herkunftsseite/-abbildung nicht ermittelt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Herkunft von ☐2 (vermutlich Vorseite) ungeklärt; nicht kopiert, nur zu
    verlinken, sobald bekannt.

## Formel 3 – RV-Schlitz-Verschiebung an der linken Seitennaht

- **Quelle:** [`formeln_s059.md`](formeln_s059.md), Abschnitt 3
- **Buchfassung:**
  ```text
  An der linken Seitennaht wird am RV-Schlitz die Naht um ca. 0,5 cm nach innen
  verschoben
  ```
- **Technische Formel:**
  ```text
  position_naht_neu = position_naht_alt - ca. 0,5 cm  (Richtung: nach innen)
  ```
- **Eingaben und Einheiten:** `position_naht_alt` (cm) der linken Seitennaht am
  RV-Schlitz.
- **Ausgabe und Einheit:** `position_naht_neu` (cm), verschobene Nahtlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` erhalten; Richtung
  „nach innen" laut Buch, Bezugsachse (Rockmitte vs. Schlitzachse) nicht
  spezifiziert.
- **Abhängigkeiten:** Querverweis im selben Satzblock: „Für einen RV an der hM,
  siehe Seiten 63+92" – alternative Konstruktion, nicht Teil dieser Formel.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Bezugsrichtung „nach innen" nicht geometrisch präzisiert (bezogen worauf).

## Formel 4 – Schlitzende-Verlängerung an der linken Seitennaht

- **Quelle:** [`formeln_s059.md`](formeln_s059.md), Abschnitt 4
- **Buchfassung:**
  ```text
  das Schiltzende um ca. 2 bis 3 cm verlängert
  ```
- **Technische Formel:**
  ```text
  laenge_schlitzende_neu = laenge_schlitzende_alt + delta
  delta ∈ [ca. 2 cm, ca. 3 cm]
  ```
- **Eingaben und Einheiten:** `laenge_schlitzende_alt` (cm).
- **Ausgabe und Einheit:** `laenge_schlitzende_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „2 bis 3 cm"
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel 3]] (gleicher Satzblock, gleiche Seitennaht);
  Querverweis „siehe Seiten 63+92" für RV-an-hM-Variante.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - OCR-Schreibweise „Schiltzende" (Tippfehler oder Buchfehler?) nicht am
    Original geprüft.
