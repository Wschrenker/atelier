# Formeln s084 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s084.md`](formeln_s084.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Die Formel steht deshalb
auf `offen`, unabhängig von der inhaltlichen Klarheit der Buchfassung. Dies
ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung.

## Formel 1 – Einschlagsbreite am Falteneinschlag

- **Quelle:** [`formeln_s084.md`](formeln_s084.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Die Schlitzhöhe und die Einschlagsbreite 2 bis 5 cm bestimmen.

  Längere Schlitze sollenn einen breiteren Einschlag erhalten, damit beim
  Umschlagen der Schlitzkante das Futter oder das Ende des Einschlags weniger
  schnell sightbar ist.
  ```
- **Technische Formel:**
  ```text
  einschlagsbreite ∈ [2 cm, 5 cm]
  einschlagsbreite steigt qualitativ mit schlitzhoehe (Auswahlregel, kein
  numerischer Zusammenhang im Buchtext)
  ```
- **Eingaben und Einheiten:** `schlitzhoehe` (cm) – bestimmender Faktor laut
  Buchtext; auf dieser Seite kein eigener Zahlenwert genannt.
- **Ausgabe und Einheit:** `einschlagsbreite` (cm), Breite des Falteneinschlags
  an den Teilungsnähten in VT und/oder RT.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 2–5 cm bleibt
  Bereich, kein fester Default gewählt. Auswahlregel „Längere Schlitze sollten
  einen breiteren Einschlag erhalten“ ist eine qualitative Monotonie-Regel
  (länger → breiter innerhalb des Bereichs), kein quantifizierter
  Zusammenhang.
- **Abhängigkeiten:** keine weiteren Formeln auf dieser Seite. Bezug zur
  „Schlitzhöhe“, die an anderer Buchstelle bzw. auf der Zeichnung definiert
  sein dürfte, auf s084 aber nicht beziffert wird.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Der Satz „Die Schlitzhöhe und die Einschlagsbreite 2 bis 5 cm bestimmen.“
    ist syntaktisch unklar (möglicher OCR-Wortstellungsfehler); hier naheliegend
    als „Schlitzhöhe bestimmt Einschlagsbreite“ gelesen, aber nicht
    stillschweigend umformuliert – siehe Buchfassung oben.
  - Kein Zahlenwert für „Schlitzhöhe“ auf dieser Seite; die Auswahlregel bleibt
    daher rein qualitativ (länger → breiter), nicht quantifizierbar ohne
    weitere Buchstelle.
