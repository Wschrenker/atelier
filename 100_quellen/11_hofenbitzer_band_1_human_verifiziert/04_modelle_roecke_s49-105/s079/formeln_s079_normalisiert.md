# Formeln s079 – Normalisierung (vorläufig, Walking Skeleton — Formel 1 bestätigt)

**Achtung:** Wie in [`formeln_s079.md`](formeln_s079.md) vermerkt, ist bisher
nur Formel 1 dieser Seite von Werner am Original bestätigt; ob weitere Stellen
der Seite formelrelevant sind, ist nicht abschließend geprüft. Formel 1 selbst
ist rechnerisch eindeutig und wird deshalb als `normalisiert` geführt.

## Formel 1 – Saumweitenreduzierung durch Nahtüberlappung

- **Quelle:** [`formeln_s079.md`](formeln_s079.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Die Schnittteile am Saum an den Nähten ca. 0,5 bis 1,5 cm übereinander legen (ergibt bei 10 Nähten = 5 bis 15 cm Saumweitenreduzierung)
  ```
- **Technische Formel:**
  ```text
  ueberlappung_pro_naht ∈ [ca. 0,5 cm, ca. 1,5 cm]
  anzahl_naehte = 10
  saumweitenreduzierung = anzahl_naehte × ueberlappung_pro_naht
  saumweitenreduzierung ∈ [5 cm, 15 cm]  (ca.)
  ```
- **Eingaben und Einheiten:** `ueberlappung_pro_naht` (cm, Bereich ca. 0,5 bis
  1,5 cm je Naht); `anzahl_naehte` = 10 (fest, für diesen 10-Bahnenrock).
- **Ausgabe und Einheit:** `saumweitenreduzierung` (cm), Bereich 5 bis 15 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` vor dem
  Wertebereich erhalten – kein fester Betrag laut Buch. `anzahl_naehte` = 10
  gilt nur für den in diesem Modell verwendeten 10-Bahnenrock; bei anderer
  Bahnenzahl ändert sich das Ergebnis (auf dieser Seite nicht geregelt).
  Rechnerisch stimmig: 10 × 0,5 cm = 5 cm, 10 × 1,5 cm = 15 cm.
- **Abhängigkeiten:** Bezug auf die „Zehn-Bahnenrock-Einteilung" aus ☐1
  (Schnittentwicklung); Grundlage ist der 10-Bahnenrock, dessen eigene
  Konstruktion nicht auf dieser Seite liegt (Quellseite nicht ermittelt/nicht
  verlinkt).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Die übrige Seite (Punkte 2–6, Bildunterschriften) ist formeltechnisch nicht
    abschließend geprüft; laut `s079.md` betrifft die Bestätigung „nur diese
    Rechenstelle".
  - Ob `ueberlappung_pro_naht` bei allen 10 Nähten gleich groß gewählt wird
    oder je Naht individuell variieren darf, ist aus dem Buchwortlaut nicht
    spezifiziert; die Endpunkte des Ergebnisbereichs sind bei gleichmäßiger
    Wahl rechnerisch konsistent (10 × 0,5 = 5, 10 × 1,5 = 15).
