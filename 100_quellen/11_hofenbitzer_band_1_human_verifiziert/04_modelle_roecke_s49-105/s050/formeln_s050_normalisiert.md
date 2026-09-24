# Formeln – s050 (normalisiert)

Technische Fassung zu [formeln_s050.md](formeln_s050.md). Jede Formel verweist
auf ihren Abschnitt dort. Buchfassung und technische Fassung bleiben getrennt.

Walking Skeleton: Auf Werners ausdrücklichen Wunsch entstand diese Fassung ohne
vollständige Vorab-Bestätigung. Nur die Kürzel `TaA`/`BuA` sind bestätigt; alle
Formeln unten führen daher überwiegend den Status `offen`, keinen `normalisiert`.

## F1 – Direkte Übertragung des Taillenabstands (TaA)

- **Quelle:** [formeln_s050.md](formeln_s050.md), Abschnitt 1.
- **Buchfassung:**

```text
Alle Vertiefungen sind entsprechend der gemessenen Taillenabstände (Tak) vorzunehmen
```

- **Technische Formel:** `Vertiefung(Punkt) = TaA(Punkt)` — der an einem Punkt
  gemessene Taillenabstand wird unverändert als Vertiefungsbetrag an genau
  diesem Punkt übernommen.
- **Eingaben und Einheiten:** `TaA(Punkt)` in cm, gemessen laut Verweis auf
  Seite 13 (nicht kopiert).
- **Ausgabe und Einheit:** `Vertiefung(Punkt)` in cm, zahlengleich mit
  `TaA(Punkt)`.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine; feste
  Eins-zu-eins-Übertragung laut Buchtext.
- **Abhängigkeiten:** Messvorschrift auf Seite 13 (Verweis, nicht kopiert).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Die OCR-Schreibweise `Tak` weicht vom
  bestätigten Kürzel `TaA` ab (vermutliche OCR-Verlesung). Der Satz selbst
  sowie sein genauer Anwendungsbereich (an welchen Punkten? wie viele
  Messpunkte?) sind nicht bestätigt.

## F2 – Direkte Übertragung des Bundabstands (BuA)

- **Quelle:** [formeln_s050.md](formeln_s050.md), Abschnitt 2.
- **Buchfassung:**

```text
Für die Abtrennung sind die gemessenen Bundabstände (Bull) abzutragen und die obere Rockkante leicht geschwungen zu zeichnen.
```

- **Technische Formel:** `Bundlinie(Punkt) = Grundschnittlinie(Punkt) - BuA(Punkt)`,
  anschließend Bundlinie leicht geschwungen (nicht als Geradenzug) zeichnen.
- **Eingaben und Einheiten:** `BuA(Punkt)` in cm.
- **Ausgabe und Einheit:** Position der oberen Rockkante (Bundlinie) je Punkt,
  in cm-Versatz zur Grundschnittlinie.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** „leicht geschwungen" ist
  eine qualitative Zeichenanweisung ohne Zahlenwert.
- **Abhängigkeiten:** parallele Struktur zu F1 (TaA), hier für BuA.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Die OCR-Schreibweise `Bull` weicht vom
  bestätigten Kürzel `BuA` ab (vermutliche OCR-Verlesung). Nicht bestätigt,
  ob F1 und F2 zwei benannte Varianten derselben Methode sind oder fachlich
  unterschiedliche Vertiefungsarten (Taillenabstand vs. Bundabstand).

## F3 – Taillenmehrweite-Reduktion

- **Quelle:** [formeln_s050.md](formeln_s050.md), Abschnitt 3.
- **Buchfassung:**

```text
Taillenmehrweite (am halben Rock) = ca. 1 bis 1,5 cm
```

- **Technische Formel:** `Reduktion_obere_Rockkante = Taillenmehrweite_Grundschnitt`,
  `Taillenmehrweite_Grundschnitt ∈ [1 cm, 1,5 cm]` (ca., am halben Rock).
- **Eingaben und Einheiten:** Wert bereits im Grundschnitt enthalten, keine
  externe Messgröße auf dieser Seite.
- **Ausgabe und Einheit:** Reduktionsbetrag an der oberen Rockkante, cm.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** `ca. 1–1,5 cm`, kein
  Default gewählt; Ausdruck „ca." bleibt erhalten.
- **Abhängigkeiten:** wird gemäß F4 auf Seitennähte und hintere Abnäher verteilt.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** keine Rechnung zu prüfen, reine
  Bereichsangabe.

## F4 – Verteilung der Weitenreduzierung

- **Quelle:** [formeln_s050.md](formeln_s050.md), Abschnitt 4.
- **Buchfassung:**

```text
Weitenreduzierung an: Seitennähten UND (ein hinterer Abnäher ODER beide hinteren Abnäher)
```

- **Technische Formel:** nicht ableitbar als Zahlenformel; Auswahlregel
  zwischen zwei hinteren Verteilungsvarianten, kombiniert mit fester
  Beteiligung der Seitennähte.
- **Eingaben und Einheiten:** `Taillenmehrweite_Grundschnitt` aus F3.
- **Ausgabe und Einheit:** keine quantifizierte Ausgabe im Buchtext (keine
  Aufteilungsanteile genannt).
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Auswahl „ein oder beide
  hintere Abnäher"; zusätzliche Abnäher bei geringer Taillenvertiefung laut
  Verweis auf Folgeseite (nicht kopiert).
- **Abhängigkeiten:** F3.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Keine Aufteilungsanteile zwischen
  Seitennähten und Abnähern im Buchtext genannt; ohne weitere Buchregel keine
  Standardaufteilung ergänzt.

## F5 – Schwellenwert für sichelförmigen Abnäher

- **Quelle:** [formeln_s050.md](formeln_s050.md), Abschnitt 5.
- **Buchfassung:**

```text
Wenn Taillenvertiefung_hinten >= ca. 4 cm: Abnäher dort sichelförmig nähen (siehe Seite 38)
```

- **Technische Formel:** `if Taillenvertiefung_hinten >= 4 cm (ca.): Abnäherform = "sichelförmig"`.
- **Eingaben und Einheiten:** `Taillenvertiefung_hinten` in cm.
- **Ausgabe und Einheit:** kategoriale Auswahl der Abnäherform, keine
  Zahlenausgabe.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Schwellenwert „ca. 4 cm",
  keine feste Grenze; „ca." bleibt erhalten.
- **Abhängigkeiten:** Seite 38 (Verweis auf dortige Konstruktion des
  sichelförmigen Abnähers, nicht kopiert).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** keine Rechnung zu prüfen.

## F6 – Bedingung: große Taillenvertiefung ohne vordere Abnäher

- **Quelle:** [formeln_s050.md](formeln_s050.md), Abschnitt 6.
- **Buchfassung:**

```text
Wenn Taillenvertiefung = groß: vordere Abnäher entfallen vollständig
```

- **Technische Formel:** `if Taillenvertiefung == "groß": vordere_Abnäher = 0` —
  nicht quantitativ ableitbar, da „groß" im Buch nicht definiert ist.
- **Eingaben und Einheiten:** nicht ableitbar (kein Zahlenwert für „groß").
- **Ausgabe und Einheit:** nicht ableitbar.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** qualitative Bedingung ohne
  Zahlengrenze; kein Default ergänzt.
- **Abhängigkeiten:** möglicherweise zu F5, aber im Buch nicht explizit
  verknüpft.
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** Ohne Zahlenwert für „groß" ist diese
  Regel für einen späteren Codevertrag nicht direkt nutzbar; hier bewusst
  nicht mit dem Schwellenwert aus F5 gleichgesetzt, da das Buch das nicht
  ausdrücklich sagt.

## F7 – Positionsbezogene Bundabstände vBuA/sBuA/hBuA (zeichnungsgebunden)

- **Quelle:** [formeln_s050.md](formeln_s050.md), Abschnitt 7.
- **Buchfassung:**

```text
vBuA (vorne)
sBuA (seitlich)
hBuA (hinten)
```

- **Technische Formel:** drei getrennte Positionswerte, keine Berechnung auf
  dieser Seite; analog zu `BuA v/s/h` in F8 aus s038.
- **Eingaben und Einheiten:** keine Zahlenwerte auf s050 erfasst (siehe offene
  Frage).
- **Ausgabe und Einheit:** nicht ableitbar ohne Zahlenwerte.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** zeichnungsgebunden, siehe
  [skizzen_s050.json](skizzen_s050.json) und
  [skizzen/s050_skizze_02.png](skizzen/s050_skizze_02.png); strukturell
  vergleichbar mit `BuA v/s/h` auf s038 (dort mit Zahlenwerten belegt).
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** Auf s050 sind für `vBuA`/`sBuA`/`hBuA`
  keine Zahlenwerte erfasst; laut s050.md sind Beschriftungen und Werte am
  Original noch zu bestätigen.

## F8 – Beispielwerte schlanke Figur (zeichnungsgebunden)

- **Quelle:** [formeln_s050.md](formeln_s050.md), Abschnitt 8.
- **Buchfassung:**

```text
hier 5,5 cm
hier 4 cm
hier 3 cm
```

- **Technische Formel:** nicht ableitbar; drei isolierte Beispielwerte ohne
  bestätigte Punktzuordnung.
- **Eingaben und Einheiten:** `5,5 cm`, `4 cm`, `3 cm`.
- **Ausgabe und Einheit:** nicht ableitbar ohne Punktzuordnung.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine erkennbar ohne
  Zuordnung.
- **Abhängigkeiten:** zeichnungsgebunden, siehe
  [skizzen/s050_skizze_03.png](skizzen/s050_skizze_03.png); möglicher Bezug zu
  F7 (`vBuA`/`sBuA`/`hBuA`), im Buch aber nicht explizit verknüpft.
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** Welcher Wert zu welchem Punkt
  (vorne/seitlich/hinten) gehört, ist laut s050.md noch am Original zu
  prüfen. Keine Zuordnung geraten.
