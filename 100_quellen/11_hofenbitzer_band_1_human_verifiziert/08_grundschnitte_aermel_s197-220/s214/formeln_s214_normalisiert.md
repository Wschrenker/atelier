# Formeln Seite 214 (normalisiert) – Ärmelanpassung nach Armloch-Vertiefung und -Verbreiterung (3)

**Status der Seite: Walking-Skeleton-Entwurf, nicht menschlich verifiziert.**
Alle Einträge sind gesperrt/offen, solange Prüfstelle 6 (und 4) in
[`s214.md`](s214.md) nicht bestätigt sind. Diese Datei erzeugt keinen
Engine-Vertrag.

## Formel 1 – Armloch-Vertiefung (Bereich mit Normwert)

- **Quelle:** [`formeln_s214.md`, Abschnitt 1](formeln_s214.md#1-armloch-vertiefung--bereich-und-normwert)
- **Buchfassung:**
  ```text
  ½ bis ganze Armlochvertiefung (Normwert = ¾)
  an beiden Seiten denselben Wert vertiefen
  ```
- **Technische Formel:**
  ```text
  vertiefung_vaP = vertiefung_haP = f * armlochvertiefung_basis
  mit f ∈ [0,5 ; 1,0], Normwert f = 0,75
  ```
- **Eingaben und Einheiten:** `armlochvertiefung_basis` (Bezugsgröße,
  Einheit cm, Herkunft auf dieser Seite nicht angegeben — vermutlich Wert aus
  der Grundschnittkonstruktion „ab Seite 191“); Faktor `f` dimensionslos.
- **Ausgabe und Einheit:** `vertiefung_vaP`, `vertiefung_haP` (cm), auf
  beiden Seiten identisch.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `f` frei wählbar im
  Bereich ½ bis 1 (ganz); Normwert/Empfehlung `f = ¾`, keine Buchregel für
  eine feste Auswahl innerhalb des Bereichs.
- **Abhängigkeiten:** `armlochvertiefung_basis` stammt vermutlich von einer
  vorhergehenden Seite (Referenzkachel „208“ auf `skizze_04`, Bildunterschrift
  „ab Seite 191“); auf dieser Seite nicht selbst hergeleitet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Bezugsgröße `armlochvertiefung_basis`
  nicht auf s214 definiert und noch nicht verlinkt; Prüfstelle 6 in
  `s214.md` unbestätigt.

## Formel 2 – Armloch-Verbreiterung (feste Zuordnung vorn/hinten)

- **Quelle:** [`formeln_s214.md`, Abschnitt 2](formeln_s214.md#2-armloch-verbreiterung--vordere-und-hintere-seite)
- **Buchfassung:**
  ```text
  ½ der Armloch-Verbreiterung (vorn)
  ganze Armloch-Verbreiterung (hinten)
  ```
- **Technische Formel:**
  ```text
  verbreiterung_vaP = 0,5 * armlochverbreiterung_basis
  verbreiterung_haP = 1,0 * armlochverbreiterung_basis
  ```
- **Eingaben und Einheiten:** `armlochverbreiterung_basis` (Bezugsgröße,
  Einheit cm, Herkunft auf dieser Seite nicht angegeben, analog zu Formel 1
  vermutlich aus der Grundschnittkonstruktion).
- **Ausgabe und Einheit:** `verbreiterung_vaP` (vorn), `verbreiterung_haP`
  (hinten), beide in cm; hinten doppelt so groß wie vorn.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Auswahl — feste
  Aufteilung ½ vorn / ganz hinten, anders als bei der Vertiefung (Formel 1)
  ohne Bereichsspielraum.
- **Abhängigkeiten:** dieselbe unklare Bezugsgröße wie Formel 1;
  wahrscheinlich `armlochverbreiterung_basis` ≠ `armlochvertiefung_basis`
  (getrennte Größen für Vertiefung und Verbreiterung), aber auf dieser Seite
  nicht belegt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Bezugsgröße nicht definiert; ungeklärt,
  ob `armlochverbreiterung_basis` mit einer bereits an anderer Stelle
  normalisierten Größe übereinstimmt.

## Eintrag 3 – Konstruktionsschritte „Ärmelnaht an den tP verlegen“ (keine Zahlenformel)

- **Quelle:** [`formeln_s214.md`, Abschnitt 3](formeln_s214.md#3-konstruktionsschritte-ärmelnaht-an-den-tp-verlegen)
- **Buchfassung:**
  ```text
  1 ☐2 Den schmalen Ärmel mit vorverlegter Ärmelnaht am tP paral-tel zur
  hinteren Ärmelnaht durchtrennen.
  2 ☐3 Die Abtrennung am Ellenbogen durchtrennen und an die vÄN verschieben.
  Dort wieder anfügen.
  3 Hierbei entsteht nun ein größerer Überschneidungsbetrag an der
  Ellenbogenlinie.
  ```
- **Technische Formel:** keine — reine Schnitt-/Verschiebeoperation
  (Durchtrennen entlang einer Linie parallel zu einer Bezugslinie,
  Verschieben des abgetrennten Teils an eine andere Bezugslinie, erneutes
  Verbinden). Kein Zahlenwert im Buchtext.
- **Eingaben und Einheiten:** keine bezifferten Eingaben; Bezugslinien
  „hintere Ärmelnaht“ (hÄN), „vordere Ärmelnaht“ (vÄN), Schnittpunkt „tP“,
  Ellenbogenlinie.
- **Ausgabe und Einheit:** „Überschneidungsbetrag an der Ellenbogenlinie“ —
  im Buchtext benannt, aber nicht beziffert; keine Einheit angegeben.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** setzt den in Abschnitt „Passformklassen-Anpassung“
  beschriebenen Blazerärmel-Ausgangsschnitt voraus (☐2+3, vorverlegte
  Ärmelnaht).
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** „paral-tel“ vermutlich Lesefehler für
  „parallel“ (Prüfstelle 4, unbestätigt); ohne bezifferten
  Überschneidungsbetrag ist kein Codevertrag möglich, unabhängig von der
  Verifizierung.
