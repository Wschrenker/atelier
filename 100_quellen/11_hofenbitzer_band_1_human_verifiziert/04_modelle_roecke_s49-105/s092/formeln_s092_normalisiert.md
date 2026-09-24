# Formeln s092 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s092.md`](formeln_s092.md) vermerkt, ist außer dem
Kürzel `NZg` (zweimal bestätigt) keine Stelle dieser Seite von Werner am
Original bestätigt. Alle sechs Formeln stehen deshalb auf `offen`, unabhängig
von der inhaltlichen Klarheit der Buchfassung. Dies ist ein
Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung.

## Formel 1 – Futterlänge, Mindest-Kürzung gegenüber Oberstoff-Rock

- **Quelle:** [`formeln_s092.md`](formeln_s092.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Der Futterrock muss immer mindestens 2 cm kürzer als der Rock aus Oberstoff
  gearbeitet sein, damit das Futter am Saum nicht hervor schaut.
  ```
- **Technische Formel:**
  ```text
  laenge_futterrock ≤ laenge_oberstoffrock - 2 cm
  ```
- **Eingaben und Einheiten:** `laenge_oberstoffrock` (cm), Saumlänge des Rocks
  aus Oberstoff.
- **Ausgabe und Einheit:** `laenge_futterrock` (cm), obere Schranke.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „mindestens 2 cm" ist
  eine Untergrenze für die Differenz, kein fester Betrag – der Futterrock darf
  auch mehr als 2 cm kürzer sein. Kein oberer Grenzwert genannt.
- **Abhängigkeiten:** keine weiteren auf dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 2 – Saumzugabe bei runden Saumkanten

- **Quelle:** [`formeln_s092.md`](formeln_s092.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Am Saum werden bei runden Saumkanten ca. 1,5 bis 2,5 cm Saumenschlag + 1 cm
  Einschlag zum Ansteppen angezeichnet.
  ```
- **Technische Formel:**
  ```text
  saumzugabe = saumenschlag + einschlag_ansteppen
  saumenschlag ∈ [ca. 1,5 cm, ca. 2,5 cm]
  einschlag_ansteppen = 1 cm
  ```
- **Eingaben und Einheiten:** keine Zahleneingabe; `saumenschlag` als
  Bereichswert, `einschlag_ansteppen` als fester Wert, beide in cm.
- **Ausgabe und Einheit:** `saumzugabe` (cm), am Saum anzuzeichnende
  Gesamtzugabe.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** gilt laut Buchwortlaut
  nur „bei runden Saumkanten"; Auswahl des konkreten Werts im Bereich 1,5–2,5 cm
  bleibt offen (fachliche Auswahlentscheidung). Für nicht runde Saumkanten
  liefert die Seite keine Regel.
- **Abhängigkeiten:** keine weiteren auf dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - OCR-Schreibweise „Saumenschlag" nicht am Original geprüft (vermutlich
    „Saumeinschlag").

## Formel 3 – Futteransatznaht-Verschiebung am RV-Schlitz an hM

- **Quelle:** [`formeln_s092.md`](formeln_s092.md), Abschnitt 3
- **Buchfassung:**
  ```text
  An der hM vom Futter verschiebt man die Futteransatznaht am RV-Schlitz um ca.
  0,5 cm nach innen, weil das Futter neben den an der hM befindlichen Zähnchen
  auf das RV-Band genäht wird (siehe Seite 59).
  ```
- **Technische Formel:**
  ```text
  position_naht_neu = position_naht_alt - delta  (Richtung: nach innen)
  delta ≈ 0,5 cm  (ca.)
  ```
- **Eingaben und Einheiten:** `position_naht_alt` (cm) der Futteransatznaht am
  RV-Schlitz, hM.
- **Ausgabe und Einheit:** `position_naht_neu` (cm), verschobene Nahtlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` erhalten;
  Richtung „nach innen" laut Buch, Bezugsachse nicht spezifiziert; Begründung
  (Zähnchen des RV-Bands) im Buch genannt, aber nicht quantifiziert.
- **Abhängigkeiten:** Buch verweist auf Seite 59 ([[Formel 3 – s059]],
  [`../s059/formeln_s059.md`](../s059/formeln_s059.md), Abschnitt 3): dort
  wortgleicher Wert „ca. 0,5 cm nach innen", jedoch an anderer Naht (linke
  Seitennaht statt hM) und ebenfalls Status `offen`. Kein Beweis füreinander,
  nur als Parallelstelle dokumentiert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Bezugsrichtung „nach innen" nicht geometrisch präzisiert (bezogen worauf).

## Formel 4 – Nahtzugabe (NZg) an Futteransatznaht am RV-Schlitz

- **Quelle:** [`formeln_s092.md`](formeln_s092.md), Abschnitt 4
- **Buchfassung:**
  ```text
  An die Futteransatznaht am RV-Schlitz kommt eine NZg von 1 cm.
  ```
- **Technische Formel:**
  ```text
  nzg_futteransatznaht_rv_schlitz = 1 cm
  ```
- **Eingaben und Einheiten:** keine.
- **Ausgabe und Einheit:** `nzg_futteransatznaht_rv_schlitz` (cm), fester Wert.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert „1 cm" ohne
  `ca.` – kein Spielraum laut Buchwortlaut.
- **Abhängigkeiten:** [[Formel 6]] (gleicher Kontext, dieselbe NZg-Linie).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Das Kürzel `NZg` selbst ist von Werner am Original bestätigt (siehe
    [s092.md](s092.md)); der Zahlenwert „1 cm" und der übrige Satz sind es
    nicht.

## Formel 5 – RV-Schlitz-Verlängerung an hM

- **Quelle:** [`formeln_s092.md`](formeln_s092.md), Abschnitt 5
- **Buchfassung:**
  ```text
  Den RV-Schlitz an hM um ca. 2 bis 3 cm verlangern
  ```
- **Technische Formel:**
  ```text
  laenge_rv_schlitz_neu = laenge_rv_schlitz_alt + delta
  delta ∈ [ca. 2 cm, ca. 3 cm]
  ```
- **Eingaben und Einheiten:** `laenge_rv_schlitz_alt` (cm), Länge des
  RV-Schlitzes an hM vor der Verlängerung.
- **Ausgabe und Einheit:** `laenge_rv_schlitz_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „2 bis 3 cm"
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel 6]] (gleicher Satz, RV-Ende als Bezugspunkt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - OCR-Schreibweise „verlangern" laut bekannter OCR-Lücke in
    [s092.md](s092.md) am Original vermutlich „verlängern".

## Formel 6 – NZg-Linie zwischen RV-Ende und Futter-Schlitzende

- **Quelle:** [`formeln_s092.md`](formeln_s092.md), Abschnitt 6
- **Buchfassung:**
  ```text
  die NZg zwischen RV-Ende und Futter-Schlitzende schrag beschreiben
  ```
- **Technische Formel:**
  ```text
  linie_nzg = strecke(punkt_rv_ende, punkt_futter_schlitzende)
  breite(linie_nzg) = nzg_futteransatznaht_rv_schlitz  (= 1 cm, siehe Formel 4)
  ```
- **Eingaben und Einheiten:** `punkt_rv_ende`, `punkt_futter_schlitzende` als
  Bezugspunkte (Koordinaten nicht auf dieser Seite quantifiziert);
  `nzg_futteransatznaht_rv_schlitz` = 1 cm aus Formel 4.
- **Ausgabe und Einheit:** `linie_nzg`, eine schräg verlaufende NZg-Linie
  zwischen den beiden Punkten.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine eigenen
  Zahlenwerte; reine geometrische Linienführung, abhängig vom Ergebnis von
  Formel 5 (neue Länge des RV-Schlitzes bestimmt die Lage von
  `punkt_rv_ende`).
- **Abhängigkeiten:** [[Formel 4]] (Wert der NZg), [[Formel 5]] (Lage von
  RV-Ende nach Verlängerung).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Das Kürzel `NZg` selbst ist von Werner am Original bestätigt (siehe
    [s092.md](s092.md)); die geometrische Linienführung und ihr Bezug zu
    Formel 4/5 sind es nicht.
  - Keine Angabe, ob „schräg" eine feste Richtung/Winkel meint oder nur die
    freihändige Verbindungslinie zwischen den zwei Punkten beschreibt.
