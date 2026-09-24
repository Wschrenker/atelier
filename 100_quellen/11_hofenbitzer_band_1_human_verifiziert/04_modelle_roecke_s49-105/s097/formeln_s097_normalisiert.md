# Formeln s097 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s097.md`](formeln_s097.md) vermerkt, ist nur
Formel 4 (mittleres Futterteil) von Werner am Original bestätigt; die übrigen
drei Formeln stammen unbestätigt aus OCR bzw. dokumentierten Zeichnungslabels.
Alle vier Formeln stehen deshalb auf `offen` – Formel 4, weil ihre fachliche
Zuordnung trotz bestätigter Zahlenfolge unklar ist, die übrigen, weil keine
formelrelevante Stelle am Original bestätigt ist. Dies ist ein
Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung.

## Formel 1 – Nahtzugabe an der Futteransatznaht am RV-Schlitz

- **Quelle:** [`formeln_s097.md`](formeln_s097.md), Abschnitt 1
- **Buchfassung:**
  ```text
  An die Futteransatznaht am RV-Schlitz kommt eine NZg von 1 cm.
  ```
- **Technische Formel:**
  ```text
  nzg_futteransatznaht_rv_schlitz = 1 cm
  ```
- **Eingaben und Einheiten:** keine (fester Wert).
- **Ausgabe und Einheit:** `nzg_futteransatznaht_rv_schlitz` (cm), Nahtzugabe
  an der Futteransatznaht am RV-Schlitz.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert „1 cm" ohne
  `ca.` – kein Spielraum laut Buchwortlaut.
- **Abhängigkeiten:** [[Formel 2]] (gleicher Satzblock: NZg wird zwischen
  RV-Ende und Futter-Schlitzende schräg beschnitten, siehe Querverweis in
  `formeln_s097.md`, Abschnitt 2).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 2 – Futter-Schlitz-Verlängerung an der Seitennaht

- **Quelle:** [`formeln_s097.md`](formeln_s097.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Futter-Schlitz an SN um ca. 2 bis 3 cm verlangern
  ```
  Zeichnungsgebundene Parallelstelle (noch nicht am Original bestätigt):
  ```text
  Schlitzende für das Futter an der SN ca. 2 bis 3 cm nach unten verschieben
  ```
- **Technische Formel:**
  ```text
  laenge_futter_schlitz_neu = laenge_futter_schlitz_alt + delta
  delta ∈ [ca. 2 cm, ca. 3 cm]
  ```
- **Eingaben und Einheiten:** `laenge_futter_schlitz_alt` (cm), Länge des
  Futter-Schlitzes an der Seitennaht (SN) vor der Verlängerung.
- **Ausgabe und Einheit:** `laenge_futter_schlitz_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „2 bis 3 cm"
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel 1]] (gleicher Satzblock, NZg-Beschneidung
  zwischen RV-Ende und Futter-Schlitzende).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Fließtext („verlangern") und Zeichnungslabel („nach unten verschieben")
    sind unterschiedlich formuliert; ob beide dieselbe Maßnahme oder zwei
    verschiedene Operationen beschreiben, ist am Original zu klären.
  - OCR-Schreibweise „verlangern" (statt „verlängern") unverändert übernommen,
    nicht still korrigiert.

## Formel 3 – Futteransatznaht-Erhöhung oberhalb eines gefütterten Schlitzes

- **Quelle:** [`formeln_s097.md`](formeln_s097.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Oberhalb eines gefütterten Schlitzes benötigt das Futter Mehrlänge. Die
  Futteransatznaht dort um ca. 0,5 bis 1 cm erhöhen.
  ```
  Zeichnungsgebundene Parallelstelle (noch nicht am Original bestätigt):
  ```text
  Futternaht oberhalb eines Schlitzes um 0,5 bis 1 cm verlängern
  ```
- **Technische Formel:**
  ```text
  position_futteransatznaht_neu = position_futteransatznaht_alt + delta
  delta ∈ [ca. 0,5 cm, ca. 1 cm]
  ```
- **Eingaben und Einheiten:** `position_futteransatznaht_alt` (cm), Lage der
  Futteransatznaht oberhalb eines gefütterten Schlitzes vor der Erhöhung.
- **Ausgabe und Einheit:** `position_futteransatznaht_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „0,5 bis 1 cm"
  bleibt Bereich, kein fester Default gewählt. Bedingung: gilt nur „oberhalb
  eines gefütterten Schlitzes".
- **Abhängigkeiten:** keine weiteren auf dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Fließtext und Zeichnungslabel stimmen inhaltlich weitgehend überein; als
    zwei Belege derselben Regel dokumentiert, nicht stillschweigend
    zusammengeführt.

## Formel 4 – Mittleres Futterteil, Maßfolge

- **Quelle:** [`formeln_s097.md`](formeln_s097.md), Abschnitt 4
- **Buchfassung:**
  ```text
  2 bis 4 cm / 1 bis 4 cm
  ```
- **Technische Formel:**
  ```text
  wert_1 ∈ [2 cm, 4 cm]
  wert_2 ∈ [1 cm, 4 cm]
  ```
- **Eingaben und Einheiten:** unbekannt – Bezugsgröße am mittleren Futterteil
  nicht spezifiziert.
- **Ausgabe und Einheit:** unbekannt – zwei Bereiche in cm, ihre Bedeutung
  (z. B. zwei Kanten, zwei Rechenschritte) ist nicht dokumentiert.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** beide Bereiche bleiben
  Bereiche, kein fester Wert gewählt.
- **Abhängigkeiten:** keine auf dieser Seite ermittelt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Die Zahlenfolge selbst ist von Werner am Original bestätigt, ihre
    fachliche Zuordnung (welche Strecke(n) am mittleren Futterteil sie
    bezeichnet) ist in `s097.md` nicht weiter ausgeführt und daher hier nicht
    ergänzt.
