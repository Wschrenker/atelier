# Formeln s100 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s100.md`](formeln_s100.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Beide Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Mindestabstand der Wickelkanten-Linie zum Abnäher

- **Quelle:** [`formeln_s100.md`](formeln_s100.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Um den Abnaher zu verdecken, wird hier die Linie mindestens 1 cm über den Abnaher gezeichnet.
  ```
- **Technische Formel:**
  ```text
  abstand_linie_abnaeher >= 1 cm
  ```
- **Eingaben und Einheiten:** `abstand_linie_abnaeher` (cm) – Abstand zwischen
  der neu gezeichneten Wickelkanten-Linie und dem Abnäher.
- **Ausgabe und Einheit:** Lageregel für die Wickelkanten-Linie relativ zum
  Abnäher (keine berechnete Zahl, sondern eine Mindestabstandsbedingung).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Nur ein Mindestwert
  „mindestens 1 cm" angegeben; kein Höchstwert im Buchtext. `mindestens`
  erhalten, kein fester Betrag gewählt.
- **Abhängigkeiten:** Setzt die Lage des Abnähers am kopierten/gespiegelten VT
  voraus (Abnäher-Position selbst nicht auf s100 definiert, stammt aus dem
  zugrunde liegenden Rockschnitt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Bezugsrichtung „über den Abnaher" nicht geometrisch präzisiert (Richtung
    Saum oder Richtung Taille).
  - Die genaue Punktnummer im roten Kasten vor dem ersten Absatz der Seite ist
    laut `s100.md` noch offen (`48`? unscharf) und wirkt sich möglicherweise
    auf die Schrittzuordnung dieser Formel aus.

## Formel 2 – Abstand Wickelkante–Markierung entspricht dem Abnäherinhalt

- **Quelle:** [`formeln_s100.md`](formeln_s100.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die spätere Lage der Wickelkante an der Taille markieren: Der Abstand der Wickelkante zur Markierung entspricht dem Abnaherinhalt.
  ```
- **Technische Formel:**
  ```text
  abstand_wickelkante_markierung = abnaeherinhalt
  ```
- **Eingaben und Einheiten:** `abnaeherinhalt` (cm) – Inhalt/Breite des
  betroffenen Abnähers.
- **Ausgabe und Einheit:** `abstand_wickelkante_markierung` (cm) – Abstand
  zwischen der Wickelkante und der Markierung an der Taille.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Keine Bereichsangabe;
  Buchtext setzt eine direkte Gleichheit, kein `ca.` oder Spielraum.
- **Abhängigkeiten:** [[Formel 1]] (gleicher Abschnitt „Wickeltell
  gestalten"); `abnaeherinhalt` selbst wird auf s100 nicht berechnet, sondern
  aus dem zugrunde liegenden, hier gespiegelten Rockschnitt übernommen
  (Herkunftsseite nicht ermittelt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unklar, ob „Abnaherinhalt" hier den vollen Inhalt eines einzelnen Abnähers
    oder die Summe mehrerer Abnäher meint, falls das VT mehr als einen Abnäher
    hat.
  - OCR-Schreibweise „Abnaherinhalt" (fehlender Umlaut) nicht am Original
    geprüft.
