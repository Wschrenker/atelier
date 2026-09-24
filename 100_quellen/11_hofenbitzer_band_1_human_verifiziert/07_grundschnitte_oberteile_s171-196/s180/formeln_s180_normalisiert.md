# Formeln s180 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s180.md`](formeln_s180.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle vier Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der Buchfassung.
Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung.

## Formel 1 – Hintere Armlinie, Anteil ⅔ ArD+ ab P10

- **Quelle:** [`formeln_s180.md`](formeln_s180.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Von P10 nach links ⅔ Armdurchmesser+ (ArD+) aus der Konstruktionstabelle ablesen und abtragen.
  ```
- **Technische Formel:**
  ```text
  abstand_P10 = (2/3) * ArD_plus
  ```
- **Eingaben und Einheiten:** `ArD_plus` (cm), Wert aus der
  Konstruktionstabelle (nicht auf dieser Seite definiert, nur referenziert).
- **Ausgabe und Einheit:** `abstand_P10` (cm) – Abtrag nach links von P10 zur
  hinteren Armlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Bruch ⅔, kein
  Spielraum laut Buchwortlaut.
- **Abhängigkeiten:** [[Formel 2]] (gemeinsame Aufteilung von `ArD_plus` auf
  P10 und P12); `ArD_plus` selbst stammt aus der Konstruktionstabelle
  (eigene Seite, hier nur zu verlinken, nicht zu kopieren).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Herkunft und Definition von `ArD_plus` liegen außerhalb dieser Seite.

## Formel 2 – Vordere Armlinie, Anteil ⅓ ArD+ (Rest) ab P12

- **Quelle:** [`formeln_s180.md`](formeln_s180.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Von P12 nach links ⅓ ArD+ (den restlichen ArD+) aus der Konstruktionstabelle abtragen.
  ```
- **Technische Formel:**
  ```text
  abstand_P12 = (1/3) * ArD_plus = ArD_plus - abstand_P10
  ```
- **Eingaben und Einheiten:** `ArD_plus` (cm); alternativ `abstand_P10` (cm).
- **Ausgabe und Einheit:** `abstand_P12` (cm) – Abtrag nach links von P12 zur
  vorderen Armlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Bruch ⅓ (laut
  Buchwortlaut „der restliche ArD+" zu ⅔ aus Formel 1), kein Spielraum.
- **Abhängigkeiten:** [[Formel 1]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Rechnerisch ergänzen sich ⅔ (Formel 1) und ⅓ (hier) exakt zu `ArD_plus`;
    dies beruht auf dem Buchwortlaut „restlicher ArD+", ist aber am Original
    noch zu bestätigen.

## Formel 3 – Zwischenraum RT/VT ab P11

- **Quelle:** [`formeln_s180.md`](formeln_s180.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Von P11 nach links einen Zwischenraum zwischen RT und VT von ca. 7 bis 10 cm abtragen
  ```
- **Technische Formel:**
  ```text
  zwischenraum_P11 ∈ [ca. 7 cm, ca. 10 cm]
  ```
- **Eingaben und Einheiten:** keine; freie Wahl innerhalb des Bereichs.
- **Ausgabe und Einheit:** `zwischenraum_P11` (cm) – Abtrag nach links von P11.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „7 bis 10 cm"
  bleibt Bereich; `ca.` erhalten; kein fester Default und keine im Buchtext
  dieser Seite genannte Auswahlregel innerhalb des Bereichs.
- **Abhängigkeiten:** keine auf dieser Seite erkennbaren.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kriterium für die konkrete Wahl innerhalb 7–10 cm (z. B. nach Modell,
    Stoff oder Körpermaß) ist auf dieser Seite nicht angegeben.

## Formel 4 – Kontrolle der BrW

- **Quelle:** [`formeln_s180.md`](formeln_s180.md), Abschnitt 4 (Fließtext und
  zeichnungsgebundener Kontrollkasten)
- **Buchfassung:**
  ```text
  Von P14 bis P12 die vBrW messen und von P11 bis P9 die hBrW messen. Die Summe der Messungen muss ½ BrW ergeben.
  ```
  ```text
  vBrW + hBrW = ½ BrW
  ```
- **Technische Formel:**
  ```text
  vBrW + hBrW = BrW / 2
  ```
- **Eingaben und Einheiten:** `vBrW` (cm, gemessen P14–P12), `hBrW` (cm,
  gemessen P11–P9), `BrW` (cm, Brustweite – Herkunft nicht auf dieser Seite
  ausgewiesen).
- **Ausgabe und Einheit:** kein neuer Konstruktionswert, sondern eine
  Prüfbedingung (Gleichheit muss nach den vorangehenden Abtrag-Schritten
  erfüllt sein).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; exakte
  Kontrollgleichung ohne `ca.` oder Bereich.
- **Abhängigkeiten:** `BrW` stammt vermutlich aus der Konstruktionstabelle
  (nicht auf dieser Seite ausgewiesen); [[Formel 1]] und [[Formel 2]] tragen zu
  den Punktabständen bei, die vBrW/hBrW mitbestimmen; P9 und P14 werden auf
  dieser Seite selbst nicht konstruiert, nur referenziert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Zwei Quellen derselben Formel (Fließtext und Zeichnungskasten) sind
    inhaltlich identisch, aber beide unbestätigt.
  - Herkunft von P9 und P14 liegt außerhalb dieser Seite und ist noch zu
    klären bzw. zu verlinken.
