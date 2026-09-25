# Formeln s209 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s209.md`](formeln_s209.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung am Original.

## Formel 1 – Abstand der neuen Ärmelnaht vom vÄBr

- **Quelle:** [`formeln_s209.md`](formeln_s209.md), Abschnitt 1
- **Buchfassung:**
  ```text
  1 Hierzu eine neue Ärmelnaht im Abstand von 1,5 bis 2,5 cm vom vÄBr entfernt als Abtrennlinie einzeichnen.
  ```
- **Technische Formel:**
  ```text
  abstand_neue_naht ∈ [1,5 cm, 2,5 cm], gemessen vom vÄBr (vordere Ärmelbruchlinie)
  ```
- **Eingaben und Einheiten:** `vÄBr` (Bezugslinie, keine eigene Länge; Punkt
  auf dieser Linie als Nullpunkt der Messung).
- **Ausgabe und Einheit:** `abstand_neue_naht` (cm), Lage der neuen
  Abtrennlinie/Ärmelnaht relativ zu `vÄBr`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „1,5 bis
  2,5 cm" bleibt Bereich; kein fester Default oder Auswahlkriterium auf
  dieser Seite angegeben.
- **Abhängigkeiten:** Ausgangskonstruktion „einfache Variante des schmalen
  Ärmel-Grundschnitts" von Seite 207 (verlinkt, nicht kopiert); [[Formel 3]]
  (Lücke an hinterer Ärmelnaht hängt vom hier gewählten Wert ab).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt. Kein Auswahlkriterium für den konkreten Wert
  innerhalb 1,5–2,5 cm auf dieser Seite angegeben (z. B. abhängig von
  Stoffdehnbarkeit, Größe o. ä.).

## Formel 2 – Knipsabstand von der Ellenbogenlinie

- **Quelle:** [`formeln_s209.md`](formeln_s209.md), Abschnitt 2
- **Buchfassung:**
  ```text
  2 An die neue Ärmelnaht Knipse im Anstand von 6 bis 8 cm oberhalb und unterhalb der Ellenbogenlinie anbringen.
  ```
- **Technische Formel:**
  ```text
  knipsabstand ∈ [6 cm, 8 cm], je einmal oberhalb und einmal unterhalb der Ellenbogenlinie
  ```
- **Eingaben und Einheiten:** Ellenbogenlinie (Bezugslinie aus dem
  Grundgerüst, auf dieser Seite nicht neu hergeleitet).
- **Ausgabe und Einheit:** `knipsabstand` (cm), zwei Knipse auf der neuen
  Ärmelnaht (Formel 1).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „6 bis 8 cm"
  bleibt Bereich; kein fester Default oder Auswahlkriterium auf dieser Seite
  angegeben.
- **Abhängigkeiten:** [[Formel 1]] (Knipse liegen auf der dort festgelegten
  neuen Ärmelnaht); Ellenbogenlinie aus dem Grundgerüst der Ausgangsseite 207
  (verlinkt, nicht kopiert).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt. Kein Auswahlkriterium für den konkreten Wert
  innerhalb 6–8 cm auf dieser Seite angegeben.

## Formel 3 – Lücke an der hinteren Ärmelnaht = Dehnbetrag vorne

- **Quelle:** [`formeln_s209.md`](formeln_s209.md), Abschnitt 3
- **Buchfassung:**
  ```text
  6 Die Lücke an der hinteren Ärmelnaht entspricht dem Dehnbetrag an der vorderen Ärmelnaht. Die neue hintere Ärmelnaht neu zeichnen.
  ```
- **Technische Formel:**
  ```text
  lücke_hintere_naht = dehnbetrag_vordere_naht
  ```
- **Eingaben und Einheiten:** `dehnbetrag_vordere_naht` (cm) – auf dieser
  Seite nicht als eigener Rechenausdruck hergeleitet; laut Fließtext das
  Ergebnis des Verschiebens der vorderen Ärmelnaht um den in Formel 1
  gewählten Wert.
- **Ausgabe und Einheit:** `lücke_hintere_naht` (cm), Öffnung, die beim
  Zusammenlegen der beiden verschobenen Schnittflächen an der hinteren
  Ärmelnaht entsteht (Schritt 4–5) und über die die neue hintere Ärmelnaht
  gezeichnet wird.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine eigene Angabe;
  reine Gleichheitsbeziehung.
- **Abhängigkeiten:** [[Formel 1]] (Abstand der neuen vorderen Ärmelnaht
  bestimmt vermutlich den Dehnbetrag, auf dieser Seite nicht explizit
  hergeleitet).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt. Der Buchtext definiert „Dehnbetrag an der vorderen
  Ärmelnaht" nicht als eigenen Rechenausdruck; ob er identisch mit dem in
  Formel 1 gewählten Abstandswert ist oder zusätzlich von anderen Größen
  abhängt (z. B. Stoffdehnung), ist auf dieser Seite offen.

## Nicht normalisiert (siehe `formeln_s209.md`, „Nicht als Formel erfasst")

- Schritt 3–5 (Schnittfläche abschneiden/durchtrennen, verschieben, an hAN
  sowie tP und Saum passend anlegen): reine Handlungsanweisungen ohne eigene
  Zahl oder Rechenbeziehung auf dieser Seite.
- „verschieben / nicht spiegeln!" und „schmaler Ärmel G 38 PK 3"
  (Skizzenbeschriftungen): Handlungsanweisung bzw. Größen-/Modellkennung,
  keine Formel.
- Seitenverweise „207" und „214" sowie die vermutliche OCR-Fehllesung „210":
  keine Formel.
