# Formeln s188 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s188.md`](formeln_s188.md) vermerkt, sind nur
drei Stellen dieser Seite von Werner am Original bestätigt (Formeln 10, 17 und
18). Alle übrigen Formeln stehen auf `offen`, unabhängig von der inhaltlichen
Klarheit der Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz
für die Bestätigung der übrigen Stellen.

## Formel 1 – Brustweite aus Brustumfang und Zugabe

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 1
- **Buchfassung:**
  ```text
  BrU | Brustumfang | 88 | + | 2 | = | BrW | 90 | ½ 45
  ```
- **Technische Formel:**
  ```text
  BrW = BrU + zugabe_BrU
  halb_BrW = BrW / 2
  ```
- **Eingaben und Einheiten:** `BrU` = 88 cm; `zugabe_BrU` = 2 cm.
- **Ausgabe und Einheit:** `BrW` = 90 cm; `halb_BrW` = 45 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; fester Beispielwert
  aus der Konstruktionstabelle für Größe 38, PK1.
- **Abhängigkeiten:** [[Formel 8]] (Kontrollrechnung nutzt dieselben Größen).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Zeile ist von Werner
  am Original bestätigt.

## Formel 2 – Taillenweite aus Taillenumfang und Zugabe

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 2
- **Buchfassung:**
  ```text
  TaU | Taillenumfang | 72 | + | --- | = | TaW | 72 | ½ 36
  ```
- **Technische Formel:**
  ```text
  TaW = TaU + zugabe_TaU
  halb_TaW = TaW / 2
  ```
- **Eingaben und Einheiten:** `TaU` = 72 cm; `zugabe_TaU` laut Foto leer
  („---“), hier als 0 cm zu lesen, aber nicht ausdrücklich als „0“ gedruckt.
- **Ausgabe und Einheit:** `TaW` = 72 cm; `halb_TaW` = 36 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Keine feste Zugabe
  gedruckt; nicht als 0 cm interpretieren, ohne dass das am Original bestätigt
  ist.
- **Abhängigkeiten:** [[Formel 15]] (nutzt `halb_TaW` = 36 als Vergleichswert).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Bedeutung der leeren Zugabe-Spalte
  („---“ = 0 oder „nicht zutreffend“?) am Original zu klären.

## Formel 3 – Hüftweite aus Hüftumfang und Zugabe

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 3
- **Buchfassung:**
  ```text
  HUU | Hüftumfang | 97 | + | 0 | = | HUW | 97 | ½ 48,5
  ```
- **Technische Formel:**
  ```text
  HueW = HueU + zugabe_HueU
  halb_HueW = HueW / 2
  ```
- **Eingaben und Einheiten:** `HueU` = 97 cm; `zugabe_HueU` = 0 cm.
- **Ausgabe und Einheit:** `HueW` = 97 cm; `halb_HueW` = 48,5 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[Formel 16]] (nutzt `halb_HueW` = 48,5 als
  Vergleichswert).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kürzel-Schreibweise mit ü (HüU/HüW)
  am Original zu bestätigen.

## Formel 4 – Armlochtiefe mit Zugabe

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 4
- **Buchfassung:**
  ```text
  AIT | Armüchtiefe | 20,1 | + | 0,5 | = | AIT+ | 20,6
  ```
- **Technische Formel:**
  ```text
  AlT_plus = AlT + 0,5
  ```
- **Eingaben und Einheiten:** `AlT` = 20,1 cm.
- **Ausgabe und Einheit:** `AlT_plus` = 20,6 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine, fester Wert.
- **Abhängigkeiten:** [[Formel 18]] (Sollwert-Formel bezieht sich auf „Zugabe
  zur AlT“, evtl. dieselbe Zugabe oder eine eigene).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Ob die „Zugabe zur AlT“ in Formel 18
  dieselbe 0,5-cm-Zugabe ist wie hier, ist am Original zu klären.

## Formel 5 – Rückenbreite mit Zugabe

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 5
- **Buchfassung:**
  ```text
  RUB | Rückenbreite (½) | 16,5 | + | 0,1 | = | RUB+ | 16,6
  ```
- **Technische Formel:**
  ```text
  RueB_plus = RueB + 0,1
  ```
- **Eingaben und Einheiten:** `RueB` = 16,5 cm (halbe Rückenbreite).
- **Ausgabe und Einheit:** `RueB_plus` = 16,6 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** keine erkennbaren auf dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kürzel-Schreibweise mit ü (RüB/RüB+)
  am Original zu bestätigen.

## Formel 6 – Armdurchmesser mit Zugabe und Teilwerten

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 6
- **Buchfassung:**
  ```text
  ArD | Armdurchmesser | 9,3 | + | 0,3 | = | ArD+ | 9,6 | ¼ 2,4 ⅓ 3,2
  ```
- **Technische Formel:**
  ```text
  ArD_plus = ArD + 0,3
  viertel_ArD_plus = ArD_plus / 4
  drittel_ArD_plus = ArD_plus / 3
  ```
- **Eingaben und Einheiten:** `ArD` = 9,3 cm.
- **Ausgabe und Einheit:** `ArD_plus` = 9,6 cm; Teilwerte ¼ = 2,4 cm, ⅓ = 3,2 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** keine erkennbaren auf dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Rechnerisch ergibt 9,6 / 4 = 2,4 (passt)
  und 9,6 / 3 = 3,2 (passt); nur Nachrechnung, kein Ersatz für eine
  Original-Bestätigung.

## Formel 7 – Brustbreite mit Zugabe

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 7
- **Buchfassung:**
  ```text
  BrB | Brustbreite (½) | 18,2 | + | 0,6 | = | BrB+ | 18,8
  ```
- **Technische Formel:**
  ```text
  BrB_plus = BrB + 0,6
  ```
- **Eingaben und Einheiten:** `BrB` = 18,2 cm (halbe Brustbreite).
- **Ausgabe und Einheit:** `BrB_plus` = 18,8 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[Formel 8]] (Kontrollrechnung).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine über die fehlende Bestätigung
  hinaus.

## Formel 8 – Kontrollformel Summe der Halbmaße

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 8
- **Buchfassung:**
  ```text
  Kontrolle: Σ = ½ BrU | 44 | + | 1 | = | ½ BrW | 45
  ```
- **Technische Formel:**
  ```text
  summe_kontrolle = halb_BrU + 1
  ```
- **Eingaben und Einheiten:** `halb_BrU` = 44 cm (= ½ von 88 cm `BrU`, siehe
  [[Formel 1]]); Zuschlag 1 cm.
- **Ausgabe und Einheit:** `summe_kontrolle` = 45 cm, soll `halb_BrW`
  entsprechen (siehe [[Formel 1]]).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Es bleibt offen, ob
  diese Zeile eine reine Rechenkontrolle ist (Summe mehrerer Einzelbreiten
  soll ½ BrW ergeben) oder eine eigenständige Formel; der Buchtext nennt nur
  „Σ“, ohne die Summanden auf dieser Seite auszuweisen.
- **Abhängigkeiten:** [[Formel 1]] (`halb_BrW` = 45 als Sollwert der Kontrolle).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Die Summanden hinter „Σ“ sind auf
  dieser Seite nicht ausgewiesen; ob es sich um RüB+ + ArD-Teilwert + BrB+ o.ä.
  handelt, ist nicht aus dem Buchtext dieser Seite ableitbar.

## Formel 9 – Schulternahtlänge aus Schulterbreite und Zugabe

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 9
- **Buchfassung:**
  ```text
  SuB | Schulterbreite | 12,2 | + | 0 | = | SuNL | 12,2
  ```
- **Technische Formel:**
  ```text
  SuNL = SuB + 0
  ```
- **Eingaben und Einheiten:** `SuB` = 12,2 cm.
- **Ausgabe und Einheit:** `SuNL` = 12,2 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[Formel 10]] (`SuNL` ist Eingabe der hinteren
  Schulternahtlänge).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine über die fehlende Bestätigung
  hinaus.

## Formel 10 – Hintere Schulternahtlänge (bestätigt)

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 10
- **Buchfassung:**
  ```text
  SuNL + Einhalteweite 0,5 cm bis 1 cm
  ```
  Rohbeleg-Zeile (nicht deckungsgleich, siehe unten):
  ```text
  hSuNL | hintere Schulternahtlänge | SuNL = Einmalzweite 0,5 cm bis 1 cm | + | 0,2 | = | hSuNL | 12,4
  ```
- **Technische Formel:**
  ```text
  hSuNL = SuNL + einhalteweite
  einhalteweite ∈ [0,5 cm, 1 cm]
  ```
- **Eingaben und Einheiten:** `SuNL` (cm, siehe [[Formel 9]]); `einhalteweite`
  im Bereich 0,5 cm bis 1 cm.
- **Ausgabe und Einheit:** `hSuNL` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 0,5 cm bis 1 cm
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel 9]] (liefert `SuNL`).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** Die Zahlenzeile der Tabelle zeigt für
  dieses Rechenbeispiel `+0,2` und Ergebnis `12,4` (12,2 + 0,2), was
  außerhalb des von Werner bestätigten Bereichs 0,5–1 cm liegt. Diese
  gedruckte Abweichung wird sichtbar dokumentiert und nicht als Beleg für eine
  andere Formel verwendet; die Regel selbst (`hSuNL = SuNL + Einhalteweite`,
  Bereich 0,5–1 cm) gilt laut Werners Bestätigung.

## Formel 11 – Schulterwinkel-Zeile (unklare Rechenbeziehung)

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 11
- **Buchfassung:**
  ```text
  SuWI | Schulterwinkel (in Grad. °) | 20° | auf Körpfer | — | — | SuWI | 20°
  ```
- **Technische Formel:** nicht ableitbar.
- **Eingaben und Einheiten:** `SuWi` = 20° (Grad).
- **Ausgabe und Einheit:** `SuWi` = 20° (unverändert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** nicht bestimmbar; die
  orange hinterlegte Zelle (vermutet „− Auflockerung“) könnte eine Operation
  andeuten, ohne dass Operand oder Ergebnis der Operation in der Zeile
  erkennbar sind.
- **Abhängigkeiten:** keine erkennbaren.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** Sowohl der Zellinhalt („auf Körpfer“
  vs. vermutet „− Auflockerung“) als auch die Bedeutung der Operatorspalten
  („—“) sind ungeklärt; ohne Original-Bestätigung keine Formel ableitbar.

## Formel 12 – Individuelle Balance aus Vorder- und Rückenlänge

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 12
- **Buchfassung:**
  ```text
  RUL | Rückenlänge (waagerechte Taille) | 41,6
  VL | Vorderlänge (waagerechte Taille) | 45,3
  Differenz VL - RUL = individuelle Balance = 3,7
  ```
- **Technische Formel:**
  ```text
  balance_individuell = VL - RueL
  ```
- **Eingaben und Einheiten:** `VL` = 45,3 cm; `RueL` = 41,6 cm.
- **Ausgabe und Einheit:** `balance_individuell` = 3,7 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[Formel 13]], [[Formel 14]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kürzel „RUL“ statt „RüL“ am Original zu
  bestätigen.

## Formel 13 – Korrigierte Balance (unverändert übernommen)

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 13
- **Buchfassung:**
  ```text
  korrigierte Balance = 3,7
  ```
- **Technische Formel:**
  ```text
  balance_korrigiert = balance_individuell + korrektur
  korrektur = 0  (keine Korrektur eingetragen)
  ```
- **Eingaben und Einheiten:** `balance_individuell` = 3,7 cm (siehe
  [[Formel 12]]).
- **Ausgabe und Einheit:** `balance_korrigiert` = 3,7 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Korrektur-Spalte zeigt
  „±---“; ob das grundsätzlich 0 bedeutet oder „nicht zutreffend“, ist nicht
  eindeutig aus dem Buchtext.
- **Abhängigkeiten:** [[Formel 12]] (liefert `balance_individuell`);
  [[Formel 14]] (Vergleich mit optimaler Balance).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Bedeutung von „±---“ am Original zu
  klären.

## Formel 14 – Balance-Vergleichsregel und Toleranzentscheidung

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 14
- **Buchfassung:**
  ```text
  Bal | optimale Balance (aus Maßstabel) | 3,5 | Optimale und korrigierte Balance müssten (wzrt sehr ähnlich sein, ca 1 cm Toleranz, nur wenn kein Figurproblem zu beobachten ist)
  ```
  ```text
  Die Differenz von 0,2 cm zwischen individueller und optimaler Balance liegt
  innerhalb der Toleranz und wird vernachlässigt. Somit werden die RUL und die
  VL unkorrigiert verwendet.
  ```
- **Technische Formel:**
  ```text
  differenz_balance = |balance_korrigiert - balance_optimal|
  wenn differenz_balance <= toleranz_balance:
      RueL, VL unkorrigiert verwenden
  sonst:
      Korrektur erforderlich (auf dieser Seite nicht spezifiziert)
  toleranz_balance ≈ 1 cm  (ca., nur wenn kein Figurproblem beobachtet wird)
  ```
- **Eingaben und Einheiten:** `balance_korrigiert` = 3,7 cm (siehe
  [[Formel 13]]); `balance_optimal` = 3,5 cm (aus Maßtabelle, hier nicht
  Teil dieser Seite); `toleranz_balance` ≈ 1 cm.
- **Ausgabe und Einheit:** Auswahlentscheidung (unkorrigiert verwenden oder
  nicht), keine numerische Ausgabe.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca. 1 cm` Toleranz
  bleibt Näherung, kein fester Grenzwert; Bedingung „nur wenn kein
  Figurproblem zu beobachten ist“ ist eine fachliche Zusatzbedingung ohne
  quantifizierbares Kriterium auf dieser Seite. Der angewendete Beispielfall
  zeigt eine Differenz von 0,2 cm (3,7 − 3,5), die als „innerhalb der
  Toleranz“ eingestuft wird.
- **Abhängigkeiten:** [[Formel 12]], [[Formel 13]]; `balance_optimal` stammt
  aus einer Maßtabelle außerhalb dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Wortlaut der Zeile „Bal“ ist laut
  [s188.md](s188.md) unsicher (OCR „müssten (wzrt ... ca 1 cm“ vs. vermutet
  „müssen jetzt ... ± 1 cm“); die Herkunft von `balance_optimal` (Maßtabelle)
  liegt außerhalb dieser Seite und ist hier nur referenziert, nicht kopiert.

## Formel 15 – Gemessene Taillenbreite gegen halbe Taillenweite (bestätigt)

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 15
- **Buchfassung:**
  ```text
  gemessene TaB | 44,6 | - ½ TaW | 36 | = | 8,6
  ```
  Rohbeleg-Zeile (OCR, abweichender Zahlenwert):
  ```text
  Minimere + TaB | 44,3 | - ½ TaW | 36 | = | 8,6
  ```
- **Technische Formel:**
  ```text
  differenz_TaB = gemessene_TaB - halb_TaW
  ```
- **Eingaben und Einheiten:** `gemessene_TaB` = 44,6 cm (bestätigt) bzw. 44,3 cm
  (OCR-Rohwert, abweichend); `halb_TaW` = 36 cm (siehe [[Formel 2]]).
- **Ausgabe und Einheit:** `differenz_TaB` = 8,6 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[Formel 2]] (`halb_TaW`).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** OCR-Wert 44,3 vs. bestätigter Wert 44,6
  – beide rechnerisch mit Ergebnis 8,6 nicht exakt deckungsgleich (44,6 − 36 =
  8,6 stimmt; 44,3 − 36 = 8,3, nicht 8,6). Die Abweichung wird dokumentiert,
  nicht aufgelöst; maßgeblich ist Werners Bestätigung `44,6 − 36 = 8,6`.

## Formel 16 – Gemessene Hüftbreite gegen halbe Hüftweite

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 16
- **Buchfassung:**
  ```text
  Minimere - HuB | 43,8 | - ½ HuW | 48,5 | = | -4,7
  ```
- **Technische Formel:**
  ```text
  differenz_HueB = gemessene_HueB - halb_HueW
  ```
- **Eingaben und Einheiten:** `gemessene_HueB` = 43,8 cm; `halb_HueW` = 48,5 cm
  (siehe [[Formel 3]]).
- **Ausgabe und Einheit:** `differenz_HueB` = -4,7 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[Formel 3]] (`halb_HueW`).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Diese Zeile ist laut
  [tabellen_s188.md](tabellen_s188.md) weiterhin unbestätigt; Rechnung
  43,8 − 48,5 = −4,7 stimmt rechnerisch, ersetzt aber keine Original-Prüfung.

## Formel 17 – Mehrweite im Armloch (bestätigt)

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 17
- **Buchfassung:**
  ```text
  vAlU + hAlU − AraU
  ```
- **Technische Formel:**
  ```text
  mehrweite_armloch = vAlU + hAlU - AraU
  ```
- **Eingaben und Einheiten:** `vAlU` (cm, vorderer Armlochumfang), `hAlU` (cm,
  hinterer Armlochumfang), `AraU` (cm, Armumfang) – Herkunft dieser Einzelmaße
  liegt nicht auf dieser Seite.
- **Ausgabe und Einheit:** `mehrweite_armloch` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine auf dieser Seite
  genannt.
- **Abhängigkeiten:** [[Formel 18]] (Sollwert-Vergleich für dieselbe
  Mehrweite); Herkunft von `vAlU`, `hAlU`, `AraU` außerhalb dieser Seite.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** keine über die fehlende Herkunftsangabe
  der Einzelmaße hinaus.

## Formel 18 – Sollwert der Mehrweite im Armloch (bestätigt)

- **Quelle:** [`formeln_s188.md`](formeln_s188.md), Abschnitt 18
- **Buchfassung:**
  ```text
  Sollwert = 2 × Zugabe zur AlT (Toleranz +2 cm bis -1 cm)
  ```
  Rohbeleg-Zeile (OCR, unverändert):
  ```text
  Sollwert der Mehrweite | = 2 - Zugabe zur AIT (Toleranz +2 cm bis -1 cm) = |  |  | | Nur bei Oberteilen mit Brustabnäher!
  ```
- **Technische Formel:**
  ```text
  sollwert_mehrweite = 2 * zugabe_AlT
  toleranz ∈ [-1 cm, +2 cm]
  gilt_nur_wenn: Oberteil mit Brustabnäher
  ```
- **Eingaben und Einheiten:** `zugabe_AlT` (cm) – möglicherweise identisch mit
  der Zugabe 0,5 cm aus [[Formel 4]], nicht auf dieser Seite bestätigt.
- **Ausgabe und Einheit:** `sollwert_mehrweite` (cm), mit Toleranzband -1 cm
  bis +2 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Toleranzband bleibt
  Bereich, kein fester Wert; Bedingung „nur bei Oberteilen mit Brustabnäher“
  wörtlich erhalten.
- **Abhängigkeiten:** [[Formel 17]] (Vergleich mit `mehrweite_armloch`);
  [[Formel 4]] (mögliche gemeinsame `zugabe_AlT`, ungeklärt).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** Ob `zugabe_AlT` hier dieselbe Zugabe
  wie in [[Formel 4]] ist, ist am Original zu klären.
