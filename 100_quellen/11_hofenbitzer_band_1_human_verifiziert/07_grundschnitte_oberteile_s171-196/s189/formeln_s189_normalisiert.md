# Formeln s189 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s189.md`](formeln_s189.md) vermerkt, ist die
Seite als Ganzes nicht menschlich verifiziert. Nur die arithmetische Lesart
„43,8 − 36 = 7,8 cm" (Formel 1) ist von Werner bestätigt, und diese
Bestätigung deckt ausdrücklich nur diese eine Rechenstelle ab — nicht die
Variablennamen, die allgemeine Formel oder ihre Anwendung. Beide Formeln
stehen deshalb auf `offen`. Dies ist ein Walking-Skeleton-Durchlauf, kein
Ersatz für die Bestätigung.

## Formel 1 – Taillenausfall (TaAf)

- **Quelle:** [`formeln_s189.md`](formeln_s189.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Taillenausfall (TaAf)
  vTaB + hTaB - 1/2 TaW
  44,6cm -36cm
  = 7,8cm
  ```
  Von Werner bestätigte Rechenstelle (nicht Buchwortlaut, sondern Klärung des
  OCR-Werts): `43,8 − 36 = 7,8 cm`; Hälfte `3,9 cm` je Seite.
- **Technische Formel:**
  ```text
  TaAf = vTaB + hTaB - 1/2 * TaW
  halber_ausfallbetrag = TaAf / 2
  ```
- **Eingaben und Einheiten:** `vTaB` (cm, vordere Taillenbreite), `hTaB` (cm,
  hintere Taillenbreite), `TaW` (cm, Taillenweite laut Konstruktionstabelle).
  Bestätigter Zahlenbeispiel-Eingang: `vTaB + hTaB = 43,8 cm`, `1/2 TaW = 36
  cm` (also `TaW = 72 cm`).
- **Ausgabe und Einheit:** `TaAf` (cm, Taillenausfall); `halber_ausfallbetrag`
  (cm) je Seite, im Beispiel `3,9 cm` (bestätigt).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Keine Bereichs- oder
  Auswahlangabe im Buchtext; reine Rechenformel. Der halbe Ausfallbetrag wird
  laut Fließtext „an der erhöhten Taillenlinie jeweils nach innen" abgetragen
  – Richtungs-/Bezugsangabe, kein eigener Zahlenwert.
- **Abhängigkeiten:** `vTaB`, `hTaB`, `TaW` stammen aus der
  Konstruktionstabelle des Grundgerüsts ab Seite 179 (auf s189 nicht
  wiederholt, nur verlinkt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Die Seite als Ganzes ist nicht menschlich verifiziert; nur die Rechenstelle
    „43,8 − 36 = 7,8" ist bestätigt, nicht die Variablennamen `vTaB`/`hTaB`/
    `TaW` oder die allgemeine Formel.
  - OCR zeigt „44,6cm" statt des rechnerisch passenden „43,8cm" – gedruckter
    Wert nicht still korrigiert, siehe Hinweis in `formeln_s189.md`.
  - Das Label „jeweils 1/2 Ausfallbetrag (hier 3,9 cm)" aus der Zeichnung ist
    als eigenständige Beschriftung noch nicht von Werner bestätigt, auch wenn
    es rechnerisch zur bestätigten Textstelle passt.

## Formel 2 – Hüft-Fehlbetrag (HüFb)

- **Quelle:** [`formeln_s189.md`](formeln_s189.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Hüft-Fehlbetrag (HüFb)
  vHüB + hHüB - 1/2 HüW
  43,8cm -48,5cm
  -4,7cm → 4,7cm 1/2 = 2,4cm
  ```
- **Technische Formel:**
  ```text
  HüFb = vHüB + hHüB - 1/2 * HüW
  halber_fehlbetrag = |HüFb| / 2
  ```
- **Eingaben und Einheiten:** `vHüB` (cm, vordere Hüftbreite), `hHüB` (cm,
  hintere Hüftbreite), `HüW` (cm, Hüftweite laut Konstruktionstabelle).
  Zahlenbeispiel: `vHüB + hHüB = 43,8 cm`, `1/2 HüW = 48,5 cm` (also `HüW =
  97 cm`), `HüFb = -4,7 cm`.
- **Ausgabe und Einheit:** `HüFb` (cm, Hüft-Fehlbetrag, im Beispiel negativ);
  `halber_fehlbetrag` (cm) je Seite, im Beispiel `2,4 cm`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Buchbeispiel bildet den
  Betrag `|HüFb|` vor der Halbierung (`-4,7cm → 4,7cm`, dann `1/2 = 2,4cm`);
  keine allgemeine Bereichs- oder Vorzeichenregel im Text formuliert, nur das
  Zahlenbeispiel. Der halbe Fehlbetrag wird laut Fließtext „in Hüfthöhe
  jeweils an den Seitenlinien hinzu" gegeben.
- **Abhängigkeiten:** [[Formel 1]] (gleiche Konstruktionstabelle,
  gleichartiger Rechenaufbau); `vHüB`, `hHüB`, `HüW` stammen aus der
  Konstruktionstabelle des Grundgerüsts ab Seite 179.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Rechenstelle ist von Werner am Original bestätigt (siehe
    Prüfstelle 5 in `s189.md`).
  - Ob die Betragsbildung vor der Halbierung eine allgemeine Buchregel oder
    nur eine Beispielrechnung für den negativen Fall ist, ist aus dem
    Wortlaut nicht eindeutig.
  - Das Label „jeweils 1/2 Hüft-Fehlbetrag (hier 2,4 cm)" aus der Zeichnung ist
    noch nicht von Werner bestätigt.
