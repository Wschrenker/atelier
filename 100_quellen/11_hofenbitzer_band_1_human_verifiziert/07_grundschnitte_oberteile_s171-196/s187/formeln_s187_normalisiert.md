# Formeln s187 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s187.md`](formeln_s187.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle fünf Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Abnäherspitzen kürzen

- **Quelle:** [`formeln_s187.md`](formeln_s187.md), Abschnitt 1
- **Buchfassung:**
  ```text
  ☐2 Brust-, Taillen- und Schulterabnäher um 2 cm an der Spitze kürzen und
  separat nähen.
  ```
- **Technische Formel:**
  ```text
  laenge_abnaeher_neu = laenge_abnaeher_alt - 2 cm  (an der Spitze)
  ```
- **Eingaben und Einheiten:** `laenge_abnaeher_alt` (cm) je Brust-, Taillen-
  und Schulterabnäher.
- **Ausgabe und Einheit:** `laenge_abnaeher_neu` (cm), separat genähter,
  gekürzter Abnäher.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert „2 cm" ohne
  `ca.` – kein Spielraum laut Buchwortlaut.
- **Abhängigkeiten:** keine weiteren Formeln dieser Seite; Brustpunkt wird laut
  Fließtext ggf. zusätzlich mit Bohrloch markiert (Konstruktionshinweis, keine
  Rechenbeziehung).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob die 2 cm je Abnäher einzeln oder als Gesamtreduzierung über alle drei
    Abnäher gelten, ist aus dem Wortlaut nicht eindeutig.

## Formel 2 – Saumeinschlag-Breite

- **Quelle:** [`formeln_s187.md`](formeln_s187.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Saumeinschläge werden zwischen 2 cm und 4 cm Breite angezeichnet.
  ```
- **Technische Formel:**
  ```text
  saum_einschlag ∈ [2 cm, 4 cm]
  ```
- **Eingaben und Einheiten:** keine externe Eingabe; feste Bereichsangabe.
- **Ausgabe und Einheit:** `saum_einschlag` (cm), Breite des angezeichneten
  Saumeinschlags.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „2 bis 4 cm"
  bleibt Bereich, kein fester Default laut Buch. Auswahl innerhalb des
  Bereichs nicht weiter geregelt.
- **Abhängigkeiten:** keine.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 3 – Ausstellen an den Nähten bei langen Oberteil-Grundschnitten

- **Quelle:** [`formeln_s187.md`](formeln_s187.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Lange Oberteil-Grundschnitte können an allen Nähten (außer an der hM-Naht)
  bis zu 1 cm ausgestellt werden. Dadurch wird der Fall etwas besser.
  ```
- **Technische Formel:**
  ```text
  naht_neu = naht_alt + delta
  delta ∈ [0 cm, 1 cm]  (bis zu)
  ```
- **Eingaben und Einheiten:** `naht_alt` (cm), Nahtposition einer beliebigen
  Naht des Oberteil-Grundschnitts außer der hM-Naht.
- **Ausgabe und Einheit:** `naht_neu` (cm), ausgestellte Nahtposition.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bedingung „lange
  Oberteil-Grundschnitte"; Ausnahme hM-Naht; Bereich „bis zu 1 cm" bleibt
  offen, kein fester Default.
- **Abhängigkeiten:** keine weiteren Formeln dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Was „lange Oberteil-Grundschnitte" von dieser Seite abgrenzt (Kriterium
    für „lang"), ist im Fließtext dieser Seite nicht definiert.

## Formel 4 – Vorderer Einschlag für die Übertrittseite

- **Quelle:** [`formeln_s187.md`](formeln_s187.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Das VT wird bei der Anprobe an der vM zugesteckt und daher mit einem
  Einschlag für die Übertrittseite versehen.

  vorderer Einschlag ca. 2 cm bis 4 cm
  ```
- **Technische Formel:**
  ```text
  einschlag_breite ≈ [2 cm, 4 cm]  (ca.)
  ```
- **Eingaben und Einheiten:** keine externe Eingabe; Bereichsangabe an der vM.
- **Ausgabe und Einheit:** `einschlag_breite` (cm), Zugabe für den
  Übertritt-Einschlag am VT.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` erhalten; Bereich
  bleibt Bereich, keine feste Auswahl. Zweck laut Fließtext: Zustecken an der
  vM bei der Anprobe.
- **Abhängigkeiten:** Zahlenwert stammt nur aus der Skizzenbeschreibung
  (zeichnungsgebunden), nicht aus dem OCR-Fließtext selbst.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Zahlenwert nicht im Fließtext, nur in der Skizzenbeschreibung belegt.
  - Verhältnis zu Formel 2 (identischer Zahlenbereich „2 bis 4 cm" für einen
    anderen Zweck, laut Skizzenbeschreibung an derselben Skizze 02 getrennt
    notiert) am Original zu klären.

## Formel 5 – Kontrollmaß Brustbreite

- **Quelle:** [`formeln_s187.md`](formeln_s187.md), Abschnitt 5
- **Buchfassung:**
  ```text
  Kontrolle = ½ oBrB
  ```
- **Technische Formel:**
  ```text
  kontrolle = oBrB / 2
  ```
- **Eingaben und Einheiten:** `oBrB` (Einheit unklar, vermutlich cm) –
  Abkürzung auf dieser Seite nicht aufgelöst.
- **Ausgabe und Einheit:** `kontrolle` (gleiche Einheit wie `oBrB`).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine, fester
  Faktor ½.
- **Abhängigkeiten:** `oBrB` wird auf dieser Seite nicht definiert; vermutlich
  auf einer anderen Seite bestimmt (nicht ermittelt).
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Formel stammt ausschließlich aus einer Skizzenbeschreibung
    (`skizzen_s187.json`), nicht aus eigener Bildprüfung in dieser Sitzung und
    nicht aus dem OCR-Fließtext – Wortlaut und Zeichensetzung („½" vs. „1/2")
    am Original zu prüfen.
  - Abkürzung „oBrB" nicht aufgelöst; ohne Definition nicht rechenbar.
