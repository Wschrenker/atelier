# Formeln – s174 (normalisiert)

Technische Fassung zu [formeln_s174.md](formeln_s174.md). Jede Formel
verweist auf ihren Abschnitt dort. Buchfassung und technische Fassung bleiben
getrennt. Walking-Skeleton-Durchlauf auf ausdrücklichen Wunsch Werners; die
Seite trägt weiterhin insgesamt den Status
`OCR-Rohfassung – noch nicht menschlich verifiziert` (s174.md).

## F1 – Optimale Balance Bal nach Brustumfang BrU

- **Quelle:** [formeln_s174.md](formeln_s174.md), Abschnitt 1.
- **Buchfassung:**

```text
Brustumfang BrU | optimale Balance Bal
80 bis 89        | + 3,5
90 bis 99        | + 4,0
100 bis 109      | (BrU - 100) : 10 + 4,5
110 bis 119      | (BrU - 110) : 10 + 5,0
120 bis 129      | (BrU - 120) : 10 + 5,5
130 bis 150      | (BrU - 130) : 10 + 6,0
```

- **Technische Formel:**
  ```text
  Bal(BrU) =
      + 3,5                     für 80  ≤ BrU ≤ 89
      + 4,0                     für 90  ≤ BrU ≤ 99
      (BrU - 100) / 10 + 4,5    für 100 ≤ BrU ≤ 109
      (BrU - 110) / 10 + 5,0    für 110 ≤ BrU ≤ 119
      (BrU - 120) / 10 + 5,5    für 120 ≤ BrU ≤ 129
      (BrU - 130) / 10 + 6,0    für 130 ≤ BrU ≤ 150
  ```
- **Eingaben und Einheiten:** `BrU` (cm), Brustumfang, laut Tabelle im Bereich
  80–150 cm definiert.
- **Ausgabe und Einheit:** `Bal` (cm), optimale Balance.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** sechs sich nicht
  überschneidende `BrU`-Bereiche, je eine eigene Teilformel; die Buchtabelle
  gibt die Grenzen als „bis"-Bereiche an, eine Regel für Werte exakt auf
  einer Bereichsgrenze wird nicht separat genannt (die „bis"-Formulierung legt
  Einschluss der oberen Grenze nahe, hier nicht weiter angenommen).
- **Abhängigkeiten:** Eingabe für F5 (Balance-Problem); F2 ist ein aus dieser
  Tabelle abgelesenes Beispiel.
- **Status:** teilweise normalisiert.
  - `80 bis 89 → + 3,5`: offen (nicht bestätigt).
  - `90 bis 99 → + 4,0`: offen (nicht bestätigt).
  - `100 bis 109 → (BrU - 100) : 10 + 4,5`: offen (nicht bestätigt).
  - `110 bis 119 → (BrU - 110) : 10 + 5,0`: normalisiert (bestätigt).
  - `120 bis 129 → (BrU - 120) : 10 + 5,5`: normalisiert (bestätigt).
  - `130 bis 150 → (BrU - 130) : 10 + 6,0`: normalisiert (bestätigt).
- **Offene Fragen oder Widersprüche:** Die Zeile „100 bis 109" folgt im
  Zahlenmuster der Basis „Bereichsuntergrenze" wie die drei bestätigten
  Zeilen (`(BrU - 100)` passt zur Untergrenze 100), das ist aber eine
  Beobachtung, keine Bestätigung, und wird nicht als Wert übernommen. Die
  beiden obersten Zeilen (`+ 3,5`, `+ 4,0`) sind Festwerte ohne erkennbare
  Rechenvorschrift und ebenfalls unbestätigt.

## F2 – Bal-Beispielwert für Figur ☐2a

- **Quelle:** [formeln_s174.md](formeln_s174.md), Abschnitt 2.
- **Buchfassung:**

```text
optimale Balance Bal = 4,0
```

- **Technische Formel:** `Bal_Beispiel = Bal(BrU_☐2a)`, abgelesen aus F1.
- **Eingaben und Einheiten:** `BrU` der Figur ☐2a; auf dieser Seite nicht
  beziffert.
- **Ausgabe und Einheit:** `Bal_Beispiel = 4,0 cm`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine eigene, folgt
  aus F1.
- **Abhängigkeiten:** F1 (Herkunftstabelle); Eingabe für F5.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Der `BrU`-Wert der Figur ☐2a wird auf
  dieser Seite nicht genannt. Der Wert `4,0` stimmt zahlenmäßig mit der Zeile
  „90 bis 99 → + 4,0" aus F1 überein; das ist hier nur als Beobachtung
  vermerkt, nicht als Beleg für die Herkunft der Zeile verwendet.

## F3 – Toleranzregel für die Balance-Abweichung

- **Quelle:** [formeln_s174.md](formeln_s174.md), Abschnitt 3.
- **Buchfassung:**

```text
Abweichungen von der optimalen Balance bis zu 1 cm können vernachlässigt
werden, wenn kein Figurproblem beobachtet werden kann.
```

- **Technische Formel:**
  ```text
  wenn |Balance_Problem| ≤ 1 cm UND kein_Figurproblem_beobachtet:
      Korrektur_nötig = falsch
  ```
- **Eingaben und Einheiten:** `Balance_Problem` (cm, aus F5);
  `kein_Figurproblem_beobachtet` (boolesch, fachliche Beobachtung, nicht
  quantifiziert).
- **Ausgabe und Einheit:** boolesche Entscheidung, ob eine Korrektur nötig
  ist.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Schwelle „bis zu 1 cm"
  als Obergrenze; UND-Verknüpfung mit einer nicht numerisch gefassten
  Fachbeobachtung.
- **Abhängigkeiten:** F5 (Balance-Problem).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** „kein Figurproblem beobachtet werden
  kann" ist keine numerische Bedingung und hier nicht weiter spezifizierbar.

## F4 – Individuelle Balance aus VL und RüL (Beispiel ☐2a)

- **Quelle:** [formeln_s174.md](formeln_s174.md), Abschnitt 4.
- **Buchfassung:**

```text
VL                    = 48
minus RüL             = - 42
individuelle Balance  = 6,0
```

- **Technische Formel:** `individuelle_Balance = VL - RüL`.
- **Eingaben und Einheiten:** `VL = 48 cm`, `RüL = 42 cm` (Beispielwerte).
- **Ausgabe und Einheit:** `individuelle_Balance = 6,0 cm`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine, Einzelrechnung
  für dieses Beispiel.
- **Abhängigkeiten:** Eingabe für F5.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Unabhängig nachgerechnet:
  `48 - 42 = 6,0`, stimmt mit der Buchfassung überein.

## F5 – Balance-Problem

- **Quelle:** [formeln_s174.md](formeln_s174.md), Abschnitt 5.
- **Buchfassung:**

```text
Bal - Individuelle Balance = Balance-Problem =
```

- **Technische Formel:** `Balance_Problem = Bal - individuelle_Balance`.
- **Eingaben und Einheiten:** `Bal` (cm, aus F1/F2), `individuelle_Balance`
  (cm, aus F4).
- **Ausgabe und Einheit:** `Balance_Problem` (cm); im Buch kein Zahlenwert
  ausgefüllt bzw. per OCR erfasst.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine explizite Regel
  auf dieser Seite; das Vorzeichen scheint für die Korrekturrichtung in F6/F7
  bedeutsam.
- **Abhängigkeiten:** F1/F2 (`Bal`), F4 (`individuelle_Balance`).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Der Ergebniswert fehlt in der
  Buchfassung. Setzt man die Beispielwerte aus F2 (`Bal = 4,0`) und F4
  (`individuelle_Balance = 6,0`) probeweise ein, ergibt sich rechnerisch
  `4,0 - 6,0 = -2,0 cm`. Das passt der Größenordnung nach zu der in F6
  beschriebenen Korrektur „VL um 2 cm gekürzt"; dies wird hier nur als
  Beobachtung vermerkt, nicht als Beleg für F1, F2 oder F6 verwendet.

## F6 – VL-Korrektur bei starker Brust (☐2b)

- **Quelle:** [formeln_s174.md](formeln_s174.md), Abschnitt 6.
- **Buchfassung:**

```text
Für die Konstruktion wurde die VL um 2 cm gekürzt. Diese Kürzung um 2 cm wird
nun an der Konstruktion wieder ergänzt. Der Brustabnäher wird größer.
```

- **Technische Formel:**
  ```text
  VL_Konstruktion = VL_Ausgang - 2 cm
  VL_final         = VL_Konstruktion + 2 cm  (= VL_Ausgang)
  ```
- **Eingaben und Einheiten:** `VL_Ausgang` (cm, auf dieser Seite nicht
  beziffert); fester Wert `2 cm`.
- **Ausgabe und Einheit:** `VL_final = VL_Ausgang` (cm); zusätzlich ein
  vergrößerter Brustabnäher, im Buch nicht quantifiziert.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert `2 cm`,
  kein Bereich.
- **Abhängigkeiten:** vermutlicher fachlicher Zusammenhang mit dem
  Balance-Problem der Figur ☐2a (F5); zeichnungsgebunden auf ☐2a/☐2b.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Die Reihenfolge „erst kürzen, dann
  wieder ergänzen" ist aus dem Buchtext nicht abschließend erklärt (vermutlich
  Konstruktionsschritt-Reihenfolge: Grundgerüst zunächst mit einheitlicher
  Balance konstruieren, danach für starke Brust wieder ausgleichen); die
  Größe des vergrößerten Brustabnähers ist nicht beziffert.

## F7 – VL-Korrektur bei flacher Brust (☐3b)

- **Quelle:** [formeln_s174.md](formeln_s174.md), Abschnitt 7.
- **Buchfassung:**

```text
Für die Konstruktion wurde die VL um 1 cm verlängert. Diese Verlängerung um
1 cm wird nun an der Konstruktion wieder reduziert. Der Brustabnäher wird
kleiner.
```

- **Technische Formel:**
  ```text
  VL_Konstruktion = VL_Ausgang + 1 cm
  VL_final         = VL_Konstruktion - 1 cm  (= VL_Ausgang)
  ```
- **Eingaben und Einheiten:** `VL_Ausgang` (cm, auf dieser Seite nicht
  beziffert); fester Wert `1 cm`.
- **Ausgabe und Einheit:** `VL_final = VL_Ausgang` (cm); zusätzlich ein
  verkleinerter Brustabnäher, im Buch nicht quantifiziert.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert `1 cm`,
  kein Bereich.
- **Abhängigkeiten:** [[F6]] (spiegelbildlicher Fall, andere Figur ☐3a/☐3b).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Analog zu F6 ist die Reihenfolge
  „erst verlängern, dann wieder reduzieren" nicht abschließend erklärt; die
  Größe des verkleinerten Brustabnähers ist nicht beziffert.
