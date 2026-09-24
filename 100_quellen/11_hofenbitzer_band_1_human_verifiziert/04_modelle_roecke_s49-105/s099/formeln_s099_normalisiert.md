# Formeln s099 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s099.md`](formeln_s099.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Beide Formeln stehen
deshalb auf `offen`. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für
die Bestätigung.

## Formel 1 – Einschlagbreite gegenüber Knopflochbreite

- **Quelle:** [`formeln_s099.md`](formeln_s099.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Die Einschlagbreite mussinnen breiter als das Knopfloch sein.
  ```
- **Technische Formel:**
  ```text
  einschlagbreite > knopflochbreite
  ```
- **Eingaben und Einheiten:** `einschlagbreite` (cm) der Knopfleiste;
  `knopflochbreite` (cm) des Knopflochs.
- **Ausgabe und Einheit:** keine numerische Ausgabe – Prüfbedingung
  (bestanden/nicht bestanden).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** reine
  Größer-als-Bedingung ohne Zahlenwert oder Mindestdifferenz laut Buchtext.
- **Abhängigkeiten:** bezieht sich auf dieselbe Knopfleiste, deren
  Einschlagbreite bereits in Abschnitt 3 dieser Seite angezeichnet wird
  (`ocr_s099.md`, Zeile 9: „Schlitzlänge und Einschlagbreite anzeichnen.“);
  `knopflochbreite` selbst wird auf dieser Seite nicht quantifiziert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - OCR-Schreibweise „mussinnen“ ungeklärt (Fehllesung wahrscheinlich, aber
    nicht am Original geprüft).
  - Kein fester Mindestüberstand angegeben – reine qualitative Bedingung.

## Formel 2 – Münzen-Tasche-Einschlag

- **Quelle:** [`formeln_s099.md`](formeln_s099.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die Münzen-Tasche mit einem Einschlag versehen (1 bis 2 cm).
  ```
- **Technische Formel:**
  ```text
  einschlag_muenzentasche ∈ [1 cm, 2 cm]
  ```
- **Eingaben und Einheiten:** keine Eingabegröße – fester Buchbereich in cm.
- **Ausgabe und Einheit:** `einschlag_muenzentasche` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „1 bis 2 cm“
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** gehört zur Münzen-Tasche/Taschenspiegel-Konstruktion
  desselben Abschnitts 6 (`ocr_s099.md`, Zeilen 46–49); die separate
  Auswahl „mit oder ohne NZg“ an der unteren Taschenkante (Zeile 50, zweiter
  Teilsatz) ist keine eigene Formel und hier nicht mit erfasst.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unklar, ob sich der Einschlag auf die Münzen-Tasche allein oder auf ihr
    Verhältnis zum Taschenspiegel bezieht.
