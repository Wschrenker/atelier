# Formeln s196 – Normalisierung (vorläufig, Walking Skeleton)

Technische Fassung zu [formeln_s196.md](formeln_s196.md). Jede Formel verweist
auf ihren Abschnitt dort. Buchfassung und technische Fassung bleiben getrennt.
Wie dort vermerkt, ist nur Abschnitt 1 von Werner am Original bestätigt; alle
übrigen Formeln stehen auf `offen` oder `gesperrt`, unabhängig von der
inhaltlichen Klarheit der Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf,
kein Ersatz für die Bestätigung.

## F1 – Hauptmaß- und Zugabetabelle

- **Quelle:** [formeln_s196.md](formeln_s196.md), Abschnitt 1.
- **Buchfassung:**

```text
BrU 88 + 6 = BrW 94; ½ = 47
TaU 72 + 4 = TaW 76; ½ = 38
HüU 97 + 4 = HüW 101; ½ = 50,5
AlT 20,1 + 1,3 = AlT+ 21,4
RüB 16,5 + 0,5 = RüB+ 17
ArD 9,3 + 1,5 = ArD+ 10,8; ¼ = 2,7; ⅓ = 3,6
BrB 18,2 + 1 = BrB+ 19,2
Kontrolle: 44 + 3 = 47
SuB 12,2 + 0,3 = SuNL 12,5
hSuNL: 12,5 + 0,7 = 13,2; Einhalteweite 0,5 bis 1 cm
```

- **Technische Formel:**
  ```text
  BrW   = BrU + 6            ; halbe_BrW  = BrW / 2
  TaW   = TaU + 4            ; halbe_TaW  = TaW / 2
  HueW  = HueU + 4           ; halbe_HueW = HueW / 2
  AlT_plus = AlT + 1,3
  RueB_plus = RueB + 0,5
  ArD_plus  = ArD + 1,5      ; ArD_plus/4 ; ArD_plus/3
  BrB_plus  = BrB + 1
  Kontrolle: halbe_BrU * 3 == halbe_BrW   (44 * ... = 47, Bezug unklar, siehe unten)
  SuNL  = SuB + 0,3
  hSuNL = SuNL + 0,7         ; Einhalteweite ∈ [0,5 cm, 1 cm]
  ```
- **Eingaben und Einheiten:** `BrU = 88 cm`, `TaU = 72 cm`, `HueU = 97 cm`,
  `AlT = 20,1 cm`, `RueB = 16,5 cm`, `ArD = 9,3 cm`, `BrB = 18,2 cm`,
  `SuB = 12,2 cm` (alle Körpermaße in cm).
- **Ausgabe und Einheit:** `BrW = 94 cm`, `TaW = 76 cm`, `HueW = 101 cm`,
  `AlT_plus = 21,4 cm`, `RueB_plus = 17 cm`, `ArD_plus = 10,8 cm`,
  `BrB_plus = 19,2 cm`, `SuNL = 12,5 cm`, `hSuNL = 13,2 cm`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** feste Zugaben je Zeile,
  keine Auswahlspielräume außer der Einhalteweite `0,5 bis 1 cm` am Schluss,
  die als Bereich erhalten bleibt.
- **Abhängigkeiten:** `ArD_plus` wird in F2 als Ausgangswert für die
  Differenztabelle (F7) gebraucht; `AlT_plus`-Zugabe `1,3 cm` erscheint erneut
  in F3.
- **Status:** normalisiert.
- **Offene Fragen oder Widersprüche:** Die Kontrollzeile `44 + 3 = 47` ist
  bestätigt, ihr genauer rechnerischer Bezug (`Σ = ½ BrU`, laut
  `tabellen_s196.md`) ist aus der OCR-Kopfzeile nicht sicher rekonstruierbar
  und wird hier nicht weiter aufgelöst. Die Umbenennung „SuML"/„hSuML" (OCR) zu
  „SuNL"/„hSuNL" (Werners Bestätigung) ist als Abweichung dokumentiert, nicht
  vereinheitlicht.

## F2 – ArD-Verschmälerung bei der BrW-Reduzierung

- **Quelle:** [formeln_s196.md](formeln_s196.md), Abschnitt 2.
- **Buchfassung:**

```text
3 Der ArD wird an den SN jeweils um ½ Differenzbetrags verschmälert.
```

- **Technische Formel:**
  ```text
  ArD_neu = ArD_alt - 0,5 * Differenzbetrag_ArD
  ```
- **Eingaben und Einheiten:** `ArD_alt` (cm, PK-3-Ausgangswert);
  `Differenzbetrag_ArD` vermutlich aus F7 (`1,5 cm`, dort unbestätigt).
- **Ausgabe und Einheit:** `ArD_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „jeweils" legt nahe,
  dass die Halbierung an jeder Seitennaht (SN) einzeln angewendet wird; nicht
  eindeutig, ob insgesamt oder je Seite `0,5 * Differenzbetrag` abgezogen wird.
- **Abhängigkeiten:** F7 (`Differenzbetrag_ArD`).
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** Der Bezug zwischen „Differenzbetrag" im
  Fließtext und der Differenztabelle in F7 ist auf dieser Seite nicht
  ausdrücklich hergestellt; ohne diese Verknüpfung ist kein Zahlenwert
  einsetzbar.

## F3 – AIT-Anhebung um den Differenzbetrag

- **Quelle:** [formeln_s196.md](formeln_s196.md), Abschnitt 3.
- **Buchfassung:**

```text
4 Die AIT um den Differenzbetrag (1,3 cm) (die Brustlinie) anheben.
```

- **Technische Formel:**
  ```text
  AIT_neu = AIT_alt + 1,3 cm
  ```
- **Eingaben und Einheiten:** `AIT_alt = 20,1 cm` (aus F1, bestätigt).
- **Ausgabe und Einheit:** `AIT_neu = 21,4 cm` (zahlengleich mit `AlT_plus`
  aus F1).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert `1,3 cm`,
  keine Auswahl.
- **Abhängigkeiten:** F1 (`AlT`, `AlT_plus`).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Der Zahlenwert `1,3 cm` ist über F1
  bestätigt; die Anweisung selbst („die Brustlinie anheben") sowie die
  Gleichsetzung mit `AlT_plus` sind auf dieser Seite nicht gesondert bestätigt.

## F4 – „Puschen": Brustpunkt anheben

- **Quelle:** [formeln_s196.md](formeln_s196.md), Abschnitt 4.
- **Buchfassung:**

```text
5 Den Brustpunkt anheben: Für kleinere Brüste ca. 0 bis 1 cm, bei großen
Brüsten bis ca. 3 cm. Brust- und Taillenabnäher neu zeichnen.
```

- **Technische Formel:**
  ```text
  anhebung ∈ [ca. 0 cm, ca. 1 cm]   falls Brustgröße "klein"
  anhebung ∈ [ca. 0 cm, ca. 3 cm]   falls Brustgröße "groß"   (nur Obergrenze genannt)
  ```
- **Eingaben und Einheiten:** qualitative Einordnung „kleinere"/„große" Brust
  (keine Schwellenwerte im Buch genannt).
- **Ausgabe und Einheit:** `anhebung` (cm), Position des Brustpunkts; führt zu
  Neuzeichnung von Brust- und Taillenabnäher.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** zwei Bereiche je nach
  Brustgröße, beide mit `ca.`; für „große Brüste" ist nur eine Obergrenze
  („bis ca. 3 cm") angegeben, keine Untergrenze.
- **Abhängigkeiten:** keine auf dieser Seite.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Keine Zahlengrenze für „kleinere"
  gegenüber „große" Brüste definiert; Auswahl bleibt fachlicher Ermessensraum.

## F5 – TaW/HüW anpassen: überschüssige Weite entfernen

- **Quelle:** [formeln_s196.md](formeln_s196.md), Abschnitt 5.
- **Buchfassung:**

```text
6 Die neue ½ TaW messen und ggf. überschüssige Weite jeweils zur Hälfte an den
Seitennähten entfernen.
7 Mehrweite an der Hüfte kann im Korsagen-GS verbleiben. Alternativ kann wie an
der Taille überschüssige Weite an der Seitennaht entfernt werden.
```

- **Technische Formel:**
  ```text
  ueberschuss_taille = halbe_TaW_gemessen - halbe_TaW_ziel     (falls > 0)
  abzug_je_seitennaht_taille = ueberschuss_taille / 2

  # Hüfte: Auswahl zwischen zwei Alternativen, keine Rechenpflicht
  hueft_mehrweite verbleibt im Korsagen-GS
  # oder, analog zur Taille:
  abzug_je_seitennaht_huefte = ueberschuss_huefte / 2
  ```
- **Eingaben und Einheiten:** `halbe_TaW_gemessen` (cm, neu am Modell/Schnitt
  gemessen); `halbe_TaW_ziel` vermutlich `halbe_TaW` aus F1 (`38 cm`, nicht auf
  dieser Seite ausdrücklich verknüpft); `ueberschuss_huefte` analog für die
  Hüfte.
- **Ausgabe und Einheit:** `abzug_je_seitennaht_taille` bzw.
  `abzug_je_seitennaht_huefte` (cm); an Hüfte alternativ keine Änderung.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „ggf." macht den
  Taillen-Abzug bedingt (nur falls Überschuss vorhanden); an der Hüfte
  ausdrückliche Wahlmöglichkeit zwischen Verbleib und Entfernen.
- **Abhängigkeiten:** vermutlich F1 (`halbe_TaW`), auf dieser Seite nicht
  ausdrücklich verknüpft.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Kein expliziter Bezug zwischen der
  „neuen ½ TaW" (Punkt 6) und dem `halbe_TaW`-Wert aus F1; auf dieser Seite
  bleibt offen, ob beide dieselbe Größe meinen.

## F6 – Zugabentabelle für Oberteil-Konstruktionen, PK 0

- **Quelle:** [formeln_s196.md](formeln_s196.md), Abschnitt 6.
- **Buchfassung:**

```text
PK 0: AIT 0 - 0,5 | RüB 0 | ArD 0 | BrB 0 - 0,4 | SuB 0
```

- **Technische Formel:** Nachschlagetabelle, keine Berechnung:
  ```text
  zugabe(PK=0, Merkmal) = { AIT: [0, 0,5], RueB: 0, ArD: 0, BrB: [0, 0,4], SuB: 0 }
  ```
- **Eingaben und Einheiten:** Passformklasse `PK = 0`.
- **Ausgabe und Einheit:** Zugabewerte bzw. -bereiche in cm je Merkmal.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `AIT` und `BrB` als
  Bereich, übrige Merkmale als fester Wert `0`.
- **Abhängigkeiten:** liefert die PK-0-Spalte für F7 (`BrB`, `ArD`, `RüB`
  liegen jeweils innerhalb bzw. an der Grenze dieser Bereiche).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** keine, aber unbestätigt.

## F7 – Differenzbeträge PK 3 zu PK 0

- **Quelle:** [formeln_s196.md](formeln_s196.md), Abschnitt 7.
- **Buchfassung:**

```text
Zugabe zur BrB: PK 3 = 1,0 cm; PK 0 = 0,2 cm; Differenz = 0,8 cm
Zugabe zum ArD: PK 3 = 1,5 cm; PK 0 = 0 cm; Differenz = 1,5 cm
Zugabe zur RüB: PK 3 = 0,5 cm; PK 0 = 0 cm; Differenz = 0,5 cm
```

- **Technische Formel:**
  ```text
  Differenz_BrB = Zugabe_BrB_PK3 - Zugabe_BrB_PK0   = 1,0 - 0,2 = 0,8
  Differenz_ArD = Zugabe_ArD_PK3 - Zugabe_ArD_PK0   = 1,5 - 0   = 1,5
  Differenz_RueB = Zugabe_RueB_PK3 - Zugabe_RueB_PK0 = 0,5 - 0   = 0,5
  ```
- **Eingaben und Einheiten:** alle Werte in cm, siehe Buchfassung.
- **Ausgabe und Einheit:** `Differenz_BrB = 0,8 cm`, `Differenz_ArD = 1,5 cm`,
  `Differenz_RueB = 0,5 cm`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; feste
  Einzelwerte je Merkmal.
- **Abhängigkeiten:** `Differenz_ArD` wird in F2 vermutlich als
  `Differenzbetrag_ArD` gebraucht; `Zugabe_*_PK3`-Werte sind zahlengleich mit
  den in F1 bestätigten Zugaben BrB (+1), ArD (+1,5), RüB (+0,5);
  `Zugabe_*_PK0`-Werte liegen innerhalb der Bereiche aus F6.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Die Übereinstimmung der PK-3-Werte mit
  den bestätigten F1-Zugaben ist eine Beobachtung, kein Beleg für die
  Differenztabellen selbst; `Zugabe_BrB_PK3 = 1,0` steht der in F1 bestätigten
  Zugabe `+1` (nicht `+1,0` mit Nachkommastelle) gegenüber – zahlengleich,
  Schreibweise nicht vereinheitlicht.

## F8 – Isoliertes Rechenergebnis am Zeichnungsende

- **Quelle:** [formeln_s196.md](formeln_s196.md), Abschnitt 8.
- **Buchfassung:**

```text
= 49,2 cm
```

- **Technische Formel:** nicht ableitbar.
- **Eingaben und Einheiten:** nicht ableitbar.
- **Ausgabe und Einheit:** `49,2 cm`, Bezugsgröße unbekannt.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** nicht ableitbar.
- **Abhängigkeiten:** unklar; möglicherweise zeichnungsgebunden (Zeichnung
  `img-0.jpeg`, nicht ausgewertet).
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** Ohne erkennbaren Rechenausdruck oder
  Bezugsgröße in der OCR-Fassung ist dieser Wert nicht auswertbar; erst eine
  Prüfung am Original bzw. an der Zeichnung könnte den Zusammenhang klären.
