# Formeln s090 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s090.md`](formeln_s090.md) vermerkt, trägt die
Seite weiterhin den Status `OCR-Rohfassung – noch nicht menschlich
verifiziert`. Nur die Radiusvariablen `r_AnW`/`r_SaW` und die Gruppierung der
SaW-Formel für □2 sind laut [s090.md](s090.md) bereits am Original bestätigt;
das betrifft ausschließlich diese Teilstellen. Alle drei Formeln stehen
deshalb weiterhin auf `offen`. Dies ist ein Walking-Skeleton-Durchlauf, kein
Ersatz für die vollständige Bestätigung.

## Formel 1 – Volant aus einem Vollkreis (□1)

- **Quelle:** [`formeln_s090.md`](formeln_s090.md), Abschnitt 1
- **Buchfassung:**
  ```text
  r_AnW = AnW : (2 · π)
        = 118 cm : (2 · 3,14)
        = 18,8 cm

  r_SaW = r_AnW + VoB
        = 18,8 cm + 20 cm
        = 38,8 cm

  SaW = 2 · π · r_SaW
      = 2 · 3,14 · 38,8 cm
      = 244 cm
  ```
- **Technische Formel:**
  ```text
  r_AnW = AnW / (2 · π)
  r_SaW = r_AnW + VoB
  SaW   = 2 · π · r_SaW
  ```
- **Eingaben und Einheiten:** `AnW` (Ansatzweite, cm) – Beispielwert 118 cm;
  `VoB` (Volantbreite, cm) – Beispielwert 20 cm.
- **Ausgabe und Einheit:** `SaW` (Saumweite des Volant-Außenrands, cm);
  Zwischenergebnisse `r_AnW`, `r_SaW` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Bereichsangabe im
  Buch; `π` wird durchgehend als 3,14 gerechnet (Rundung, kein exakter Wert).
  Gilt laut Bildunterschrift für den Zuschnitt „1× zuschneiden" (ein
  durchgehender Vollkreisring).
- **Abhängigkeiten:** [[Formel 3]] nicht erforderlich (nur ein Kreisring, daher
  keine zusätzliche Nahtzugabe `NZg` zum Zusammennähen); vergleichbar mit
  [[Formel 2]] (Volant aus zwei Vollkreisen, gleiche Seite), dort mit
  zusätzlichem `NZg`-Term.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Die konkrete Rechenkette dieser Box ist von Werner noch nicht am Original
    bestätigt; nur die Variablennamen `r_AnW`/`r_SaW` sind laut
    [s090.md](s090.md) allgemein bestätigt.
  - Rundung: `2 · 3,14 · 38,8 cm = 243,66 cm`, im Buch auf `244 cm` gerundet
    angegeben – Rundungsregel nicht spezifiziert.
  - Diese Berechnungsbox steckt als Bildinhalt in `s090_skizze_02.png` und ist
    nicht durch OCR-Text belegt.

## Formel 2 – Volant aus zwei Vollkreisen (□2)

- **Quelle:** [`formeln_s090.md`](formeln_s090.md), Abschnitt 2
- **Buchfassung:**
  ```text
  r_awW = (AnW + NZg) : (2 · π) : 2
        = (118 cm + 2 cm) : (2 · 3,14) : 2
        = 9,6 cm

  r_SaW = r_awW + VoB
        = 9,6 cm + 20 cm
        = 29,6 cm

  SaW = (2 · π · r_SaW) − NZg · 2
      = (2 · 3,14 · 29,6 cm) − 2 cm · 2
      = 368 cm
  ```
- **Technische Formel:**
  ```text
  r_AnW = (AnW + NZg) / (2 · π) / 2
  r_SaW = r_AnW + VoB
  SaW   = ((2 · π · r_SaW) − NZg) · 2
  ```
- **Eingaben und Einheiten:** `AnW` (Ansatzweite, cm) – Beispielwert 118 cm;
  `NZg` (Nahtzugabe, cm) – Beispielwert 2 cm, siehe [[Formel 3]]; `VoB`
  (Volantbreite, cm) – Beispielwert 20 cm.
- **Ausgabe und Einheit:** `SaW` (Saumweite, cm); Zwischenergebnisse `r_AnW`,
  `r_SaW` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Bereichsangabe im
  Buch; `π` als 3,14 gerechnet. Gilt laut Bildunterschrift für den Zuschnitt
  „2× zuschneiden" (zwei Halbkreisringe, die zu einem Vollkreisring
  zusammengenäht werden – daher `NZg` einmal in `r_AnW` und einmal in der
  SaW-Formel).
- **Abhängigkeiten:** [[Formel 3]] (`NZg = 2 × 1 cm = 2 cm`, gleiche Seite);
  vergleichbar mit [[Formel 1]] (Ein-Kreis-Variante derselben
  Volant-Berechnung).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Werner hat laut [s090.md](s090.md) bereits bestätigt: die
    Variablennamen `r_AnW`/`r_SaW` sowie die Gruppierung
    `SaW = ((2 × π × r_SaW) − NZg) × 2 = 368 cm`. Die vorgelagerten Schritte
    `r_AnW = (AnW + NZg) : (2 · π) : 2` und `r_SaW = r_AnW + VoB` sind davon
    nicht ausdrücklich erfasst und bleiben ungeprüft.
  - Die gedruckte Zeile `SaW = (2 · π · r_SaW) − NZg · 2` ist ohne die von
    Werner bestätigte äußere Klammerung mehrdeutig: naiv von links nach rechts
    gelesen ergäbe sich `(2 · 3,14 · 29,6 cm) − (2 cm · 2) ≈ 181,9 cm`, nicht
    `368 cm`. Nur mit der Gruppierung `((2 · π · r_SaW) − NZg) · 2` stimmt das
    gedruckte Ergebnis. Dieser Widerspruch der gedruckten Klammerung wird hier
    sichtbar dokumentiert, nicht still aufgelöst.
  - OCR-Schreibweise `r_awW` (`ocr_s090.md`) vs. Bildbeleg `r_AnW`
    (`s090_skizze_03.png`) – siehe Hinweis in
    [`formeln_s090.md`](formeln_s090.md), Abschnitt 2.
  - Rundung: `120 cm : 6,28 : 2 = 9,554 cm`, im Buch als `9,6 cm` angegeben;
    `2 · 3,14 · 29,6 cm = 185,888 cm`, damit `(185,888 − 2) · 2 = 367,776 cm`,
    im Buch als `368 cm` angegeben – Rundungsregel nicht spezifiziert.

## Formel 3 – Nahtzugabe bei mehreren Kreisringen

- **Quelle:** [`formeln_s090.md`](formeln_s090.md), Abschnitt 3
- **Buchfassung:**
  ```text
  2 × 1 cm = 2 cm
  ```
- **Technische Formel:**
  ```text
  NZg = anzahl_naehte × naht_breite
  ```
- **Eingaben und Einheiten:** `anzahl_naehte` (Anzahl, hier 2 – Anzahl der
  Kreisringe/Nähte); `naht_breite` (cm, hier 1 cm).
- **Ausgabe und Einheit:** `NZg` (Nahtzugabe, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** gilt laut Fließtext nur,
  „werden mehrere Kreisringe benötigt"; keine Bereichsangabe, Beispielwert im
  Buch als „z.B." gekennzeichnet.
- **Abhängigkeiten:** liefert den `NZg`-Wert für [[Formel 2]] (Volant aus zwei
  Vollkreisen).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist bislang von Werner am Original bestätigt,
    soweit nicht ausdrücklich in [s090.md](s090.md) vermerkt (dort nicht
    erwähnt).
  - Ob `anzahl_naehte` allgemein der Anzahl benötigter Kreisringe entspricht
    oder ausschließlich für den Zwei-Kreis-Fall aus Formel 2 gilt, ist aus dem
    Fließtext nicht abschließend geklärt.
