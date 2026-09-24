# Formeln s056 – Normalisierung (Formbund (1): Rock ohne Taillenvertiefung)

Alle Einträge basieren auf [formeln_s056.md](formeln_s056.md), einer noch nicht
menschlich verifizierten Extraktion (Werners ausdrückliche Freigabe für diesen Walking
Skeleton, Blocker übersprungen). Kein Eintrag hier darf vor Werners Bestätigung am
Original als Fachwahrheit in einen Codevertrag übernommen werden.

## Formel 1 – Taillenweite-Reduzierung an der oberen Formbundkante

- **Quelle:** [formeln_s056.md](formeln_s056.md) Abschnitt 1
- **Buchfassung:**
  ```text
  muss die Weite (1 bis 1,5 cm) jetzt an der oberen Kante des Formbundes reduziert werden
  ```
- **Technische Formel:** `reduzierung_formbund_oben` ∈ `[1,0 cm; 1,5 cm]`
- **Eingaben und Einheiten:** keine Eingabegröße genannt; Wert ist ein fixer
  Erfahrungsbereich in cm, unabhängig von Körpermaßen.
- **Ausgabe und Einheit:** Reduzierbetrag an der oberen Formbundkante, in cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 1,0–1,5 cm; keine Regel
  im Buch, wie innerhalb des Bereichs gewählt wird (fachlicher Auswahlspielraum bleibt
  offen).
- **Abhängigkeiten:** Ersetzt bei diesem Modell die sonst am geraden Bund
  zusammengefasste Taillenmehrweite; siehe auch Formel 4 (Zulegen der Taillenabnäher
  plus Weiten-Reduzierungen).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Auswahlkriterium für einen konkreten Wert
  im Bereich dokumentiert. Nicht am Original bestätigt.

## Formel 2 – Zusätzliche Weiten-Reduzierung an der Seitennaht, Variante ☐2 (ein RT-Abnäher)

- **Quelle:** [formeln_s056.md](formeln_s056.md) Abschnitt 2
- **Buchfassung:**
  ```text
  Zusätzliche Weiten-Reduzierung an der Seitennaht nach Bedarf vornehmen (insgesamt ca. 0 bis 0,5 cm)
  ```
  ```text
  0,5 bis 0,7 cm
  ```
- **Technische Formel:** zwei widersprüchliche Buchwerte für dieselbe Stelle:
  `reduzierung_seitennaht_1abnaeher_fliesstext` ∈ `[0 cm; 0,5 cm] (ca.)` versus
  `reduzierung_seitennaht_1abnaeher_skizze` ∈ `[0,5 cm; 0,7 cm]`.
- **Eingaben und Einheiten:** keine Eingabegröße genannt; Bedarfsgröße „nach Bedarf“.
- **Ausgabe und Einheit:** zusätzlicher Reduzierbetrag an der Seitennaht, in cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „nach Bedarf“ – ausdrücklicher
  fachlicher Auswahlspielraum, kein fester Wert oder Default zulässig. „ca.“ nur beim
  Fließtext-Wert vermerkt, nicht beim Skizzenwert.
- **Abhängigkeiten:** Gilt nur für die Variante mit einem hinteren (RT-)Abnäher
  (Formel 4, Skizze ☐2); ergänzt Formel 1.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** Fließtext nennt „insgesamt ca. 0 bis 0,5 cm“,
  die Skizze am selben Modell „0,5 bis 0,7 cm“ – unterschiedliche Bereiche für
  scheinbar dieselbe Stelle. Nicht eigenständig auflösbar ohne Werners Prüfung am
  Original, welcher Wert zur Seitennaht-Reduzierung und welcher zu einer anderen
  Maßlinie gehört.

## Formel 3 – Zusätzliche Weiten-Reduzierung an der Seitennaht, Variante ☐3 (zwei RT-Abnäher)

- **Quelle:** [formeln_s056.md](formeln_s056.md) Abschnitt 3
- **Buchfassung:**
  ```text
  Zusätzliche Weiten-Reduzierung an der Seitennaht nach Bedarf vornehmen (insgesamt ca. 0 bis 0,7 cm)
  ```
  ```text
  alternativ auch am 2. hinteren Abnäher
  ```
- **Technische Formel:** `reduzierung_seitennaht_2abnaeher_fliesstext` ∈
  `[0 cm; 0,7 cm] (ca.)`; auf der zugehörigen Skizze steht wie bei Formel 2 zusätzlich
  `0,5 bis 0,7 cm` an derselben Eckposition.
- **Eingaben und Einheiten:** keine Eingabegröße genannt; Bedarfsgröße „nach Bedarf“.
- **Ausgabe und Einheit:** zusätzlicher Reduzierbetrag an der Seitennaht, in cm; sowie
  eine Auswahlregel, an welchem Abnäher die Reduzierung stattfindet.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „nach Bedarf“, Bereich bis
  ca. 0,7 cm. Zusätzliche Auswahlregel: die Reduzierung kann alternativ am zweiten
  hinteren Abnäher vorgenommen werden statt an der Seitennaht – Buch nennt keine
  Bedingung, wann welche Variante zu wählen ist.
- **Abhängigkeiten:** Gilt nur für die Variante mit zwei hinteren (RT-)Abnähern
  (Formel 4, Skizze ☐3); ergänzt Formel 1.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** Gleicher Fließtext/Skizze-Widerspruch wie bei
  Formel 2 (0,7 cm im Fließtext, 0,5–0,7 cm auf der Skizze). Kein Auswahlkriterium für
  „Seitennaht“ vs. „2. hinterer Abnäher“ genannt.

## Formel 4 – Bundbreite (zeichnungsgebunden, ☐2 und ☐3)

- **Quelle:** [formeln_s056.md](formeln_s056.md) Abschnitt 4
- **Buchfassung:**
  ```text
  Bundbreite 3 bis 10 cm
  ```
- **Technische Formel:** `bundbreite` ∈ `[3 cm; 10 cm]`
- **Eingaben und Einheiten:** keine Eingabegröße genannt; modellabhängige Wahlgröße.
- **Ausgabe und Einheit:** Breite des Formbund-Schnittteils an VT und RT, in cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 3–10 cm, identisch auf
  beiden Skizzen (☐2 und ☐3) und jeweils an VT und RT. Kein Auswahlkriterium im Buch.
- **Abhängigkeiten:** unabhängig von Formel 1–3; wirkt als eigene Modellgröße für den
  Formbund.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine, außer dem allgemeinen fachlichen
  Auswahlspielraum innerhalb des Bereichs.

## Formel 5 – Maßangabe „7 bis 9 cm“ (zeichnungsgebunden, ☐2 und ☐3)

- **Quelle:** [formeln_s056.md](formeln_s056.md) Abschnitt 4
- **Buchfassung:**
  ```text
  7 bis 9 cm
  ```
- **Technische Formel:** `mass_unbekannt_7bis9cm` ∈ `[7 cm; 9 cm]`
- **Eingaben und Einheiten:** unklar (kein Label-Kästchen, keine Textzuordnung).
- **Ausgabe und Einheit:** vermutlich eine vertikale Längenangabe nahe dem äußersten
  Abnäher, in cm; Bedeutung nicht gesichert.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 7–9 cm, identisch auf
  beiden Skizzen und jeweils an VT und RT.
- **Abhängigkeiten:** unklar, ob zu Formel 1–4 in Beziehung stehend.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** Bedeutung dieser Maßangabe ist aus Text und
  Skizze allein nicht sicher bestimmbar (z. B. Abnähertiefe oder Abstand zu einer
  Referenzlinie sind nur Vermutungen). Keine Fachregel ohne Werners Bestätigung am
  Original ableitbar – ausdrücklich nicht geraten.

## Nicht normalisiert

- „am Bund parallel reduzieren“ (Abschnitt 4 der Extraktion): enthält keinen Zahlenwert,
  nur eine Richtungsangabe; keine eigenständige Formel.
- Seitenverweis „ab Seite 50“ (Abschnitt „Nicht erfasst“ der Extraktion): reine
  Abhängigkeit auf eine andere Seite, keine Formel dieser Seite.
