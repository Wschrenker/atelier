# Formeln s055 – Normalisierung (Walking Skeleton)

Diese Fassung trennt die fototreue Buchfassung (siehe
[formeln_s055.md](formeln_s055.md)) von der technischen Lesart. Kein Eintrag
hier ist bereits als Engine-Vertrag verwendbar: Bis auf die Bruchangabe in
Formel 2 ist keine Stelle dieser Seite am Original bestätigt; Werner hat
ausdrücklich angewiesen, für diesen Walking Skeleton trotzdem zu
normalisieren, ohne die fehlende Bestätigung zu verschweigen.

## Formel 1 – Vordere Taillenvertiefung (Basiswert)

- **Quelle:** [formeln_s055.md](formeln_s055.md#1-vordere-taillenvertiefung-basiswert)
- **Buchfassung:**
  ```text
  1 ☐4 Taillenvertiefung vorne ab ca. 5 cm,
  ```
- **Technische Formel:** `vTV = ca. 5 cm` (Mindest-/Richtwert, kein fester Wert)
- **Eingaben und Einheiten:** keine Eingabegröße; Zahlenangabe direkt im Buch, Einheit cm.
- **Ausgabe und Einheit:** `vTV` – vordere Taillenvertiefung, cm.
- **Bereiche, Bedingungen, Auswahl:** „ab ca. 5 cm" – Näherungswert, nach Buchtext offenbar ein Startwert ohne genannte Obergrenze; keine feste Zahl wählbar.
- **Abhängigkeiten:** Eingangsgröße für Formel 2 und Formel 3 dieser Seite.
- **Status:** offen
- **Offene Fragen:** Nicht am Original bestätigt. Unklar, ob „ab ca. 5 cm" ein Mindestwert oder ein typischer Ausgangswert ist.

## Formel 2 – Hintere Taillenvertiefung im Verhältnis zur vorderen

- **Quelle:** [formeln_s055.md](formeln_s055.md#2-hintere-taillenvertiefung-im-verhältnis-zur-vorderen-bestätigt)
- **Buchfassung:**
  ```text
  2 hintere Vertiefung ⅔, ungefähr ¾ der vorderen Vertiefung,
  ```
- **Technische Formel:** unklar zwischen zwei möglichen Lesarten:
  - `hTV = 2/3 * vTV`, mit „ungefähr ¾" als zusätzliche Näherungsangabe, oder
  - `hTV ≈ Bereich [2/3 * vTV, 3/4 * vTV]`.
  Keine der beiden Lesarten wird hier ausgewählt.
- **Eingaben und Einheiten:** `vTV` (Formel 1), cm.
- **Ausgabe und Einheit:** `hTV` – hintere Taillenvertiefung, cm.
- **Bereiche, Bedingungen, Auswahl:** Buchtext nennt zwei Bruchwerte (⅔ und ¾) nebeneinander; ohne weitere Buchregel keine Auswahl zwischen fixem Verhältnis und Bereich.
- **Abhängigkeiten:** benötigt `vTV` aus Formel 1; Eingangsgröße für Formel 3.
- **Status:** offen
- **Offene Fragen:** Nur der Wortlaut dieser Zeile ist von Werner am Original bestätigt (`s055.md`), nicht ihre fachliche Auflösung. Klären, ob ⅔ und ¾ zwei getrennte Fälle, ein Bereich oder eine Präzisierung sind.

## Formel 3 – Seitliche Taillenvertiefung als Durchschnitt

- **Quelle:** [formeln_s055.md](formeln_s055.md#3-seitliche-taillenvertiefung-als-durchschnitt)
- **Buchfassung:**
  ```text
  3 seitlich ca. der Durchschnitt von vorderer und hinterer Vertiefung.
  ```
- **Technische Formel:** `sTV = ca. (vTV + hTV) / 2`
- **Eingaben und Einheiten:** `vTV` (Formel 1), `hTV` (Formel 2), cm.
- **Ausgabe und Einheit:** `sTV` – seitliche Taillenvertiefung, cm.
- **Bereiche, Bedingungen, Auswahl:** „ca." – Näherungsangabe, kein exakter Mittelwert vorgeschrieben.
- **Abhängigkeiten:** benötigt `hTV` aus Formel 2, damit indirekt auch `vTV` aus Formel 1. Schritt 6 der Seite (siehe `formeln_s055.md`, Abschnitt 3, Hinweis) verweist qualitativ auf Formel 2 und diese Formel, ohne eigene Werte.
- **Status:** offen
- **Offene Fragen:** Nicht am Original bestätigt. Hängt zusätzlich von der ungeklärten Auflösung aus Formel 2 ab.

## Formel 4 – Reißverschluss-Reduzierung an der Seitennaht

- **Quelle:** [formeln_s055.md](formeln_s055.md#4-reißverschluss-reduzierung-an-der-seitennaht)
- **Buchfassung:**
  ```text
  ☐8 Reduzierung um 0,5 bis 0,7 cm für den Reißverschluss nur an der
  Reißverschlussielfe, hier an der linken Seitannaht. Die rechte Seite
  bleibt unberührt!
  ```
- **Technische Formel:** `reduzierung_RV ∈ [0,5 cm, 0,7 cm]`, angewendet ausschließlich an der linken Seitennaht.
- **Eingaben und Einheiten:** keine weitere Eingabegröße; Bereich direkt im Buch, Einheit cm.
- **Ausgabe und Einheit:** `reduzierung_RV` – Reduzierung an der linken Seitennaht, cm.
- **Bereiche, Bedingungen, Auswahl:** Bereich 0,5–0,7 cm bleibt Bereich, kein Default. Bedingung: nur linke Seite (Reißverschlussseite); rechte Seite unverändert.
- **Abhängigkeiten:** keine zu anderen Formeln dieser Seite; betrifft dieselbe Seitennaht wie Formel 5.
- **Status:** offen
- **Offene Fragen:** Nicht am Original bestätigt. OCR-Verlesungen „Reißverschlussielfe"/„Seitannaht" ungeklärt (vgl. `s055.md`).

## Formel 5 – Restlicher Abnäherinhalt an der Seitennaht

- **Quelle:** [formeln_s055.md](formeln_s055.md#5-restlicher-abnäherinhalt-an-der-seitennaht)
- **Buchfassung:**
  ```text
  5 Der restliche Abnaherinhalt von nicht mehr als 0,7 cm kann an der
  Seitennaht entfernt werden werden, da er zum Nahen und zum Zulegen zu
  kurz ist. Der Abnaherinhalt wird gemessen und an der vorderen
  Seitennaht entfernt.
  ```
- **Technische Formel:** Bedingung `restlicher_Abnaeherinhalt ≤ 0,7 cm` → Entfernung an der vorderen Seitennaht; kein numerischer Ausgabewert außer der gemessenen Restgröße selbst.
- **Eingaben und Einheiten:** `restlicher_Abnaeherinhalt` – gemessener Wert, cm.
- **Ausgabe und Einheit:** Entscheidung „entfernen an vorderer Seitennaht" (ja/nein), keine cm-Ausgabe.
- **Bereiche, Bedingungen, Auswahl:** Obergrenze 0,7 cm für die Anwendung dieser Regel; kein Buchtext für den Fall, dass der Rest größer als 0,7 cm ist.
- **Abhängigkeiten:** keine zu anderen Formeln dieser Seite bekannt.
- **Status:** offen
- **Offene Fragen:** Nicht am Original bestätigt. Verhalten bei Restinhalt über 0,7 cm nicht im Buchtext dieser Seite geregelt.

## Formel 6 – Kürzung an den Taillenbelegen und Nahtzugabe

- **Quelle:** [formeln_s055.md](formeln_s055.md#6-kürzung-an-den-taillenbelegen-und-nahtzugabe)
- **Buchfassung:**
  ```text
  8 Bei den Taillenbelegen wird jetzt nur an den linken Seitennähen ca.
  0,5 bis 1 cm gekürzt. Sie werden Dort mit 1 cm NZg auf das
  Reißverschlussband genäht.
  ```
- **Technische Formel:** `kuerzung_Taillenbeleg ∈ [0,5 cm, 1 cm]` an den linken Seitennähen; zusätzlich `NZg_Reissverschlussband = 1 cm`.
- **Eingaben und Einheiten:** keine weitere Eingabegröße; Werte direkt im Buch, Einheit cm.
- **Ausgabe und Einheit:** `kuerzung_Taillenbeleg` (cm) und `NZg_Reissverschlussband` (cm), jeweils nur an den linken Belegteilen.
- **Bereiche, Bedingungen, Auswahl:** „ca. 0,5 bis 1 cm" bleibt Bereich, kein Default. `NZg_Reissverschlussband` ist mit 1 cm fest angegeben.
- **Abhängigkeiten:** betrifft dieselben linken Belegteile wie Formel 4 (asymmetrische Reduzierung wegen Reißverschluss).
- **Status:** offen
- **Offene Fragen:** Nicht am Original bestätigt.

## Formel 7 – Beleg-Breite und -Weite Reduzierung (Skizzenbeschriftung ☐7)

- **Quelle:** [formeln_s055.md](formeln_s055.md#7-beleg-breite-und--weite-reduzierung-skizzenbeschriftung-☐7)
- **Buchfassung:**
  ```text
  ☐7 Beleg-Breite und -Weite um ca. 0,2 cm Weite reduzieren
  ```
- **Technische Formel:** `reduzierung_Belegweite = ca. 0,2 cm`
- **Eingaben und Einheiten:** keine weitere Eingabegröße; Wert direkt in der Skizzenbeschriftung, Einheit cm.
- **Ausgabe und Einheit:** `reduzierung_Belegweite` – Weite-Reduzierung an Beleg-Breite/-Weite, cm.
- **Bereiche, Bedingungen, Auswahl:** „ca." – Näherungswert, kein fester Wert.
- **Abhängigkeiten:** zeichnungsgebunden, betrifft dieselben Belegteile wie Formel 6.
- **Status:** offen
- **Offene Fragen:** Nicht am Original bestätigt; nur als Bildinhalt in der Skizze vorhanden, nicht im OCR-Fließtext.

## Formel 8 – Abnähertiefe am hinteren Rockteil (Skizzenmaß)

- **Quelle:** [formeln_s055.md](formeln_s055.md#8-abnähertiefe-am-hinteren-rockteil-skizzenmaß)
- **Buchfassung:**
  ```text
  Abnäher 1 (hinteres Rockteil): 2 cm
  Abnäher 2 (hinteres Rockteil): 2 cm
  ```
- **Technische Formel:** `abnaehertiefe_hinten_1 = 2 cm`, `abnaehertiefe_hinten_2 = 2 cm`
- **Eingaben und Einheiten:** keine weitere Eingabegröße; Werte direkt in der Skizze bemaßt, Einheit cm.
- **Ausgabe und Einheit:** zwei Abnähertiefen am Schnittteil „Hüftrock RT 2×-p OSt", jeweils cm.
- **Bereiche, Bedingungen, Auswahl:** feste Skizzenmaße, kein Bereich angegeben.
- **Abhängigkeiten:** keine zu anderen Formeln dieser Seite bekannt.
- **Status:** offen
- **Offene Fragen:** Nicht am Original bestätigt; zeichnungsgebundenes Maß, keine Textbestätigung vorhanden.
