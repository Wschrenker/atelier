# Formeln s219 – Normalisierung

Grundlage: [`formeln_s219.md`](formeln_s219.md). Formel 1 und 2 sind am
Original bestätigt (`s219.md`, 2026-09-24). Formel 3 und 4 sind **nicht**
bestätigt (Prüfstelle 4, `s219.md`) und werden als Walking-Skeleton-Durchlauf
mit Status `offen` mitgeführt.

## Formel 1 – Senkrechter Öffnungsbetrag

- **Quelle:** [`formeln_s219.md`](formeln_s219.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Öffnung = Fehlweite − ⅔ SuPoE
  hier = 5,2 cm − 1,7 cm = 4,5 cm
  ```
  Bestätigte Arbeitslesung (Werner, 2026-09-24):
  ```text
  Öffnung = 5,2 cm − 1,7 cm = 3,5 cm
  ```
- **Technische Formel:**
  ```text
  oeffnung_vertikal_cm = fehlweite_cm - zwei_drittel_supoe_cm
  ```
- **Eingaben und Einheiten:** `fehlweite_cm` (hier 5,2 cm);
  `zwei_drittel_supoe_cm` – bereits um den Faktor ⅔ reduzierter
  Schulterpolstererhöhungs-Anteil (hier 1,7 cm). Die vollständige Herleitung
  von `SuPoE` und des Faktors ⅔ liegt nicht auf dieser Seite.
- **Ausgabe und Einheit:** `oeffnung_vertikal_cm` (bestätigt: 3,5 cm für die
  gegebenen Eingaben; Buchfassung druckt abweichend 4,5 cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – Rechenergebnis
  aus festen Eingaben, kein Auswahlspielraum.
- **Abhängigkeiten:** `SuPoE`-Herkunft und ⅔-Faktor auf einer Vorseite dieser
  Ärmelanpassung, nicht auf s219 selbst; nur zu verlinken, sobald bekannt.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Gedruckter Zwischenwert 4,5 cm widerspricht der Rechnung 5,2 − 1,7 = 3,5;
    Buchfassung bleibt als Bildbeleg unverändert stehen.

## Formel 2 – Aufteilung der Öffnung (½ oder ⅓)

- **Quelle:** [`formeln_s219.md`](formeln_s219.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Nach links und nach rechts ca. ⅓ oder ½ der berechneten senkrechten Öffnung öffnen.
  ```
  Bestätigte Werte (Basis 3,5 cm): ½ von 3,5 cm = 1,75 cm ≈ 1,8 cm;
  ⅓ von 3,5 cm = 1,166… cm ≈ 1,2 cm.
- **Technische Formel:**
  ```text
  teil_oeffnung_cm = oeffnung_vertikal_cm * faktor
  faktor ∈ {1/2, 1/3}
  ```
- **Eingaben und Einheiten:** `oeffnung_vertikal_cm` ([[Formel 1]]); `faktor`
  – fachliche Auswahl zwischen ½ und ⅓, keine Automatikentscheidung.
- **Ausgabe und Einheit:** `teil_oeffnung_cm`. Für die bestätigte Basis
  3,5 cm: 1,8 cm (½) bzw. 1,2 cm (⅓), jeweils gerundet.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `faktor` bleibt
  Buchwahl zwischen ½ und ⅓; ½ ergibt mehr Oberarmweite und geringere
  Ärmelkugelhöhe, ⅓ das Gegenteil – laut Buchwortlaut, kein fester Default.
  Rundung laut bestätigten Werten: 1,75 → 1,8; 1,166… → 1,2 (kaufmännisch auf
  eine Dezimalstelle).
- **Abhängigkeiten:** [[Formel 1]] (Basiswert `oeffnung_vertikal_cm`).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Gedruckte Folgewerte 2,25 cm / 1,5 cm (aus dem falschen Zwischenwert
    4,5 cm rechnerisch korrekt geteilt) sind für die bestätigte Arbeitslesung
    nicht zu verwenden; sie belegen nur, dass das Buch selbst konsistent mit
    seinem eigenen (falschen) Zwischenwert weiterrechnet.

## Formel 3 – Fehlbetrag des Ärmelkugel-Umfangs

- **Quelle:** [`formeln_s219.md`](formeln_s219.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Fehlbetrag = ÄkU_min − nachgemessene neue ÄkU
  hier = 53,7 cm − 52,5 cm = 1,2 cm
  ```
- **Technische Formel:**
  ```text
  fehlbetrag_cm = aeku_min_cm - aeku_neu_gemessen_cm
  ```
- **Eingaben und Einheiten:** `aeku_min_cm` (gewünschter/Mindest-Ärmelkugel-
  Umfang, Herkunft nicht auf dieser Seite); `aeku_neu_gemessen_cm`
  (nachgemessener Umfang nach der Öffnung aus Formel 2).
- **Ausgabe und Einheit:** `fehlbetrag_cm`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine erkennbar; reine
  Differenzrechnung laut Buchwortlaut.
- **Abhängigkeiten:** [[Formel 2]] (Ärmelkugelumfang nach Öffnung); Herkunft
  von `ÄkU_min` nicht auf s219, vermutlich Vorseite(n) 207/208 (Randverweise
  in `s219.md`) – nur zu verlinken, sobald bekannt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt
    (Prüfstelle 4, `s219.md`): Zahlenwerte, Kürzel `ÄkU_min` und die
    Zuordnung der Formel zu diesem Abschnitt stehen noch aus.

## Formel 4 – Korrektur der neuen Ärmelkugel-Höhe und Saumkürzung

- **Quelle:** [`formeln_s219.md`](formeln_s219.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Die Ärmelkugel oben um ½ Fehlbetrag erhöhen und die Ärmelkugel wie skizziert formen
  ```
  ```text
  Um ½ des Fehlbetrags sollte der Ärmel am Saum gekürzt und geformt sowie ggf. der Abnäher angehoben werden.
  ```
- **Technische Formel:**
  ```text
  aermelkugel_erhoehung_cm = fehlbetrag_cm / 2
  saum_kuerzung_cm         = fehlbetrag_cm / 2
  ```
- **Eingaben und Einheiten:** `fehlbetrag_cm` ([[Formel 3]]).
- **Ausgabe und Einheit:** `aermelkugel_erhoehung_cm`, `saum_kuerzung_cm`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Saumkürzung „sowie ggf.
  der Abnäher angehoben werden“ – optionale Zusatzmaßnahme, kein fester Wert
  dafür im Buch. Optionale Erweiterung der Saumweite am Abnäher laut Querverweis
  Seite 211, hier nicht mitgeführt (nur zu verlinken).
- **Abhängigkeiten:** [[Formel 3]] (`fehlbetrag_cm`); Querverweise Seite 211
  (Saumweite/Abnäher) und Seite 207 (hinterer Ärmelpunkt/Schulterpunkt) – nicht
  Teil dieser Formel, nur zu verlinken.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Hängt vollständig von `Formel 3` ab, die selbst noch offen ist.
  - OCR-Rohtext hatte zwischen „Fehlbetrags“ und „sollte“ kein Leerzeichen;
    hier zur Lesbarkeit ergänzt, siehe Hinweis in `formeln_s219.md`.
