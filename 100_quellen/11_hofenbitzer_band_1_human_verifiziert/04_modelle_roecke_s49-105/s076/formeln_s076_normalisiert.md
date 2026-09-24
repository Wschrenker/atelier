# Formeln s076 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s076.md`](formeln_s076.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Beide Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Grenzwert Abstand Passennaht–Abnäherspitze

- **Quelle:** [`formeln_s076.md`](formeln_s076.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Gewünschte Abtrennungen gestalten. Hierbei darauf achten, dass die
  Passennähte keinen größeren Abstand als 2 cm zu den Abnäherspitzen haben.
  ```
- **Technische Formel:**
  ```text
  abstand(passennaht, abnaeherspitze) <= 2 cm
  ```
- **Eingaben und Einheiten:** `abstand(passennaht, abnaeherspitze)` (cm) –
  Abstand zwischen der frei gestalteten Passennaht und der jeweils
  zugehörigen Abnäherspitze.
- **Ausgabe und Einheit:** Prüfergebnis (erfüllt/nicht erfüllt) für die
  gewählte Passennaht-Führung; kein Rechenergebnis im engeren Sinn.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Fester Grenzwert 2 cm,
  ohne „ca.“ – strikte Obergrenze laut Buchwortlaut („keinen größeren
  Abstand als“). Die Passennaht-Führung selbst („Gewünschte Abtrennungen
  gestalten“) bleibt ein freier Gestaltungsspielraum, der nur durch diesen
  Grenzwert eingeschränkt wird.
- **Abhängigkeiten:** Lage der Abnäherspitzen stammt aus der
  Grundkonstruktion (vermutlich 10-Bahnenrock, siehe rote Randbox „65“ in
  [s076.md](s076.md)); genaue Quellseite auf s076 selbst nicht benannt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unklar, ob „Abnäherspitzen“ hier die Taillenabnäher des Rockgrundschnitts
    oder bereits auf die Passe übertragene Abnäherspitzen meint.
  - Herkunft und genaue Bedeutung der roten Randbox „65“ nicht ermittelt.

## Formel 2 – Parallele Öffnung der Saumabtrennung um die gewünschte Weite

- **Quelle:** [`formeln_s076.md`](formeln_s076.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die Saumabtrennung an den Teilungsnähten und der Seitennaht um die
  gewünschte Weite parallel öffnen.

  An vM und hM wird, da es sich hier um eine Spiegellinie und keine Naht
  handelt, keine Mehrweite angezeichnet.
  ```
- **Technische Formel:**
  ```text
  an Teilungsnähten und Seitennaht: mehrweite(trennstelle) = w   (parallel geöffnet)
  an vM, hM:                        mehrweite(vM) = mehrweite(hM) = 0
  w = gewünschte Weite  (frei wählbar, kein Buchwert)
  ```
- **Eingaben und Einheiten:** `w` (cm) – frei gewählte Öffnungsweite je
  Saumabtrennung; Menge und Lage der Teilungsnähte ergibt sich aus der
  „Gewünschten Abtrennungen“-Gestaltung in Formel 1.
- **Ausgabe und Einheit:** Erweiterte Saumlinie an jeder Trennstelle
  (Teilungsnähte, Seitennaht) um `w` (cm); an vM und hM unveränderte
  Saumlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `w` ist ein freier
  Wert ohne Buchvorgabe, kein fester Betrag oder Bereich. Ausnahme
  ausdrücklich auf Spiegellinien (vM, hM) begrenzt; an echten Nähten
  (Teilungsnähte, Seitennaht) gilt die Öffnung uneingeschränkt.
- **Abhängigkeiten:** [[Formel 1]] (Anzahl und Lage der Trennstellen aus der
  dort beschriebenen Passennaht-Gestaltung).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unklar, ob `w` für alle Trennstellen gleich groß gewählt wird oder je
    Trennstelle einzeln.
  - Punkt ⑤ (nicht als eigene Formel erfasst, siehe
    [`formeln_s076.md`](formeln_s076.md)) besagt, dass die hinzugegebene
    Weite an vorderem und hinterem Kräuselteil identisch ist – dies bezieht
    sich auf die Rüsche selbst, nicht auf `w` an den einzelnen Trennstellen,
    und wird hier nicht vermischt.
