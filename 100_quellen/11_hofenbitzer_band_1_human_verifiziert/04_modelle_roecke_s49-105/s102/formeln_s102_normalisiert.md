# Formeln s102 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s102.md`](formeln_s102.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle drei Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Saumkürzung Untertritt-Kante

- **Quelle:** [`formeln_s102.md`](formeln_s102.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Den Saum an der Untertritt-Kante um ca. 0,5 cm kürzen und das Schnittteil
  kopieren (□5).
  ```
- **Technische Formel:**
  ```text
  saum_untertritt_neu = saum_untertritt_alt - delta
  delta ≈ 0,5 cm  (ca.)
  ```
- **Eingaben und Einheiten:** `saum_untertritt_alt` (cm), Saum der zuvor
  eingezeichneten Untertritt-Kante.
- **Ausgabe und Einheit:** `saum_untertritt_neu` (cm), gekürzter Saum;
  anschließend Kopie des Schnittteils (□5).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` vor dem Wert
  erhalten – kein fester Betrag laut Buchwortlaut.
- **Abhängigkeiten:** setzt die zuvor bestimmte Untertritt-Kante voraus
  (`ocr_s102.md` Zeile 36, nicht als eigene Formel geführt); Ergebnis wird als
  Schnittteil □5 kopiert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Foto-Schrittkennung laut [s102.md](s102.md) unsicher (vermutlich ⑦, in der
    OCR fehlend).

## Formel 2 – Einschlag-Kante Untertritt = vM

- **Quelle:** [`formeln_s102.md`](formeln_s102.md), Abschnitt 2
  (zeichnungsgebunden, `skizzen/s102_skizze_02.png`)
- **Buchfassung:**
  ```text
  Einschlag-Kante Untertritt = vM
  ```
- **Technische Formel:**
  ```text
  einschlag_kante_untertritt = vM
  ```
- **Eingaben und Einheiten:** `vM` (vordere Mitte), Referenzlinie des
  VT-Schnittteils.
- **Ausgabe und Einheit:** `einschlag_kante_untertritt`, Konstruktionslinie
  (Lagegleichheit, keine Längen- oder Winkelmaßangabe).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; feste geometrische
  Gleichsetzung laut Zeichnung.
- **Abhängigkeiten:** [[Formel 3]] (gleiches VT-Teil, gleiche
  Bund-Konstruktion); Bezug zur Untertritt-Kante aus Formel 1 nicht
  eindeutig – ob „Einschlag-Kante" und „Untertritt-Kante" dieselbe Linie
  meinen, ist auf dieser Seite nicht geklärt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Verhältnis von „Einschlag-Kante Untertritt" zu „Untertritt-Kante" (Formel 1)
    nicht geklärt – möglicherweise zwei verschiedene Linien am selben Teil.

## Formel 3 – Bundlänge = gemessene Taillen-Strecke

- **Quelle:** [`formeln_s102.md`](formeln_s102.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Die Taillen-Strecken am Rock messen und auf den passenden Bund-GS für den
  Übertritt-Bund und den Untertritt-Bund übertragen.
  ```
- **Technische Formel:**
  ```text
  bund_länge_übertritt   = taillen_strecke_übertritt_VT
  bund_länge_untertritt  = taillen_strecke_untertritt_VT
  ```
- **Eingaben und Einheiten:** `taillen_strecke_übertritt_VT` (cm),
  `taillen_strecke_untertritt_VT` (cm) – an den jeweiligen VT-Teilen entlang
  der Taille gemessen.
- **Ausgabe und Einheit:** `bund_länge_übertritt` (cm), `bund_länge_untertritt`
  (cm), übertragen auf den jeweiligen Bund-Grundschnitt (Bund-GS).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** reine Kopierbeziehung
  (Messen und Übertragen), kein Rechenoperator und kein Zahlenwert im
  Buchwortlaut.
- **Abhängigkeiten:** [[Formel 2]] (Einschlag-Kante Untertritt = vM, gleiches
  VT-Teil); Folgeschritt „Bundteile an der hM anschneiden" (`ocr_s102.md`
  Zeile 42) nicht als eigene Formel geführt, da ohne Zahlenwert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob „Taillen-Strecke" die volle Taillenweite oder nur einen Teilabschnitt
    (z. B. zwischen zwei Bezugslinien) meint, ist aus Text und Zeichnung nicht
    eindeutig herleitbar.
  - Bedeutung der Beschriftungen „me" und „üb" in der Zeichnung ungeklärt,
    daher nicht in die Formel aufgenommen (siehe „Nicht als Formel erfasst" in
    [`formeln_s102.md`](formeln_s102.md)).
