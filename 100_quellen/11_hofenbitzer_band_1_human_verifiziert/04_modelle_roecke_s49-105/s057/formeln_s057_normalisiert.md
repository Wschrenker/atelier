# Formeln s057 (normalisiert)

Walking-Skeleton-Durchlauf auf Werners ausdrücklichen Wunsch: Alle Einträge
stehen auf `offen` oder `gesperrt`, weil s057 noch nicht menschlich
verifiziert ist und keine formel- oder coderelevante Stelle dieser Seite
bisher am Original bestätigt wurde (siehe [`formeln_s057.md`](formeln_s057.md)).
Kein Eintrag ist bereit für einen Codevertrag.

## 1. Reduzierung der Innenbund-Teile (Weite und Breite)

- **Quelle:** [formeln_s057.md, Abschnitt 1](formeln_s057.md#1-reduzierung-der-innenbund-teile-weite-und-breite)
- **Buchfassung:**
  ```text
  Innenbund-Teile mit Weiten- und Breiten-Reduzierung um ca. 0,2 cm
  ```
- **Technische Formel:** `weite_innenbund = weite_aussenbund - reduktion` und
  `breite_innenbund = breite_aussenbund - reduktion`, mit `reduktion ≈ 0,2 cm`
  (nicht im Buchtext als Formel geschrieben, sondern aus Bildunterschrift und
  Zeichnung erschlossen)
- **Eingaben und Einheiten:** `weite_aussenbund`, `breite_aussenbund` [cm];
  `reduktion` ≈ 0,2 cm, als „ca."-Angabe
- **Ausgabe und Einheit:** `weite_innenbund`, `breite_innenbund` [cm]
- **Bereiche, Bedingungen, Auswahlentscheidungen:** „ca." — kein exakter
  Wert; keine Buchregel für eine feste Auswahl innerhalb der Toleranz.
- **Abhängigkeiten:** Bezug zu den Außenbund-/Formbundteilen derselben Seite
  (Zeichnungen skizze_09–11).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Ob sich die Reduzierung auf Weite und
  Breite gemeinsam oder unabhängig bezieht, ist aus dem Wortlaut nicht
  eindeutig. Die Zeichnung zeigt die reduzierte Kontur nur gestrichelt, ohne
  eigene aufgedruckte Maßzahl.

## 2. Kürzung der Rockteile für das Futter

- **Quelle:** [formeln_s057.md, Abschnitt 2](formeln_s057.md#2-kürzung-der-rockteile-für-das-futter)
- **Buchfassung:**
  ```text
  Hier z. B. können für das Futter die Rockteile um 2 cm gekürzt verwendet
  werden.
  ```
- **Technische Formel:** `laenge_futter_rockteil = laenge_rockteil - 2 cm`
- **Eingaben und Einheiten:** `laenge_rockteil` [cm]
- **Ausgabe und Einheit:** `laenge_futter_rockteil` [cm]
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Buchtext markiert dies
  ausdrücklich als Beispiel („z. B."), nicht als verbindliche Regel.
- **Abhängigkeiten:** Rockfutter-Konstruktion für Rock mit Innenbund/
  Taillenbeleg ab Seite 59 — nur verlinken, sobald dort bestätigt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Ist `2 cm` eine allgemeine Faustregel
  oder nur ein Beispielwert für dieses konkrete Modell?

## 3. Saumeinschlag des Futters

- **Quelle:** [formeln_s057.md, Abschnitt 3](formeln_s057.md#3-saumeinschlag-des-futters)
- **Buchfassung:**
  ```text
  Der Saum ist mit 2× 2 cm breitem Einschlag zu versehen.
  ```
- **Technische Formel:** nicht eindeutig festlegbar, siehe offene Frage;
  mögliche Lesart `saumzugabe_futter = 2 * 2 cm` (zweilagiger Einschlag)
- **Eingaben und Einheiten:** Einschlagbreite = 2 cm, Faktor 2×
- **Ausgabe und Einheit:** `saumzugabe_futter` [cm]
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine angegeben.
- **Abhängigkeiten:** keine weitere auf dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Bedeutet „2× 2 cm", dass der
  Einschlag doppelt gelegt wird (Gesamtzugabe 4 cm), oder sind zwei
  getrennte Kanten mit je 2 cm gemeint? Am Original zu klären.

## 4. Rückschnitt des Futters am Reißverschluss-Schlitz

- **Quelle:** [formeln_s057.md, Abschnitt 4](formeln_s057.md#4-rückschnitt-des-futters-am-reißverschluss-schlitz)
- **Buchfassung:**
  ```text
  Am Reißverschluss-Schlitz wird das Futter an der hM-Naht um 1,5 bis 2 cm
  zurückgeschnitten, um es an das RV-Band zu nähen.
  ```
- **Technische Formel:** `rueckschnitt_futter_rv ∈ [1,5 cm; 2 cm]`
- **Eingaben und Einheiten:** hM-Naht-Position als Bezug
- **Ausgabe und Einheit:** `rueckschnitt_futter_rv` [cm], Bereich 1,5–2 cm
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Bereich bleibt Bereich;
  keine Buchregel für eine feste Auswahl innerhalb `1,5 bis 2 cm`.
- **Abhängigkeiten:** RV an der hM, siehe Seite 63 — nur verlinken, sobald
  dort bestätigt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine Auswahlregel für den exakten
  Wert innerhalb des Bereichs angegeben.

## 5. Weite der inneren Formbundteile (Verweis auf Taillenbeleg)

- **Quelle:** [formeln_s057.md, Abschnitt 5](formeln_s057.md#5-weite-der-inneren-formbundteile-verweis-auf-taillenbeleg)
- **Buchfassung:**
  ```text
  Die Weite der inneren Formbundteile wird wie beim Taillenbeleg reduziert.
  ```
- **Technische Formel:** keine eigene Formel auf dieser Seite; Verweis auf
  eine Reduzierungsregel des Taillenbelegs (andere, hier nicht identifizierte
  Seite).
- **Eingaben und Einheiten:** –
- **Ausgabe und Einheit:** –
- **Bereiche, Bedingungen, Auswahlentscheidungen:** –
- **Abhängigkeiten:** Reduzierungsregel „Taillenbeleg" auf anderer Seite —
  Zielseite noch nicht ermittelt; nur verlinken, sobald bekannt und
  bestätigt.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** Die Quelle dieser Zeile ist laut
  `s057.md` eine ungeprüfte manuelle Abschrift vom Foto, keine OCR-Ausgabe.
  Welche Seite/Formel die Taillenbeleg-Reduzierung definiert, ist noch nicht
  ermittelt.

## Nicht erfasst

- Bildunterschriften ☐5–☐7 und ☐9 sowie Materiallabels in den Zeichnungen
  (`1× OSt + El`, Bauteilnamen, Konstruktionslinien-Kürzel) sind Stückzahlen
  und Bezeichnungen ohne eigene Rechen- oder Auswahlbeziehung.
- Die manuell abgeschriebene Passage zu Punkt 6 sowie der Warnhinweis zur
  Spiegelung sind Handlungsanweisungen ohne Zahlen- oder Rechenbeziehung.
- Der Hinweis zur provisorischen Anprobe (Zeile 93) ist eine
  Vorgehensempfehlung ohne Formel.
