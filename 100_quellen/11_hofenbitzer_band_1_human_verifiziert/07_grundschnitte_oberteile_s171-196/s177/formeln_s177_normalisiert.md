# Formeln s177 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Die Seite trägt weiterhin den Status
`OCR-Rohfassung – noch nicht menschlich verifiziert` ([s177.md](s177.md)).
Formeln 1–8 stützen sich auf konkret bestätigte Stellen aus dem Abschnitt
„Vorab geklärte formel- und coderelevante Stellen" in `s177.md` und erhalten
deshalb den Status `normalisiert`. Formeln 9–15 sind **nicht** bestätigt; sie
wurden auf ausdrücklichen Wunsch Werners trotzdem als Walking-Skeleton-Durchlauf
normalisiert (Blocker übersprungen) und stehen alle auf `offen`, unabhängig
von der inhaltlichen Klarheit der Buchfassung.

## Formel 1 – Kennmaß-Erweiterung BrU → BrW, TaU → TaW, HüU → HüW

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 1
- **Buchfassung:**
  ```text
  BrU 88 + 8 = BrW 96; ½ = 48
  TaU 72 + 6 = TaW 78; ½ = 39
  HüU 97 + 4 = HüW 101; ½ = 50,5
  ```
- **Technische Formel:**
  ```text
  BrW = BrU + zugabe_BrU     (zugabe_BrU = 8)
  TaW = TaU + zugabe_TaU     (zugabe_TaU = 6)
  HüW = HüU + zugabe_HüU     (zugabe_HüU = 4)
  BrW_halb = BrW / 2
  TaW_halb = TaW / 2
  HüW_halb = HüW / 2
  ```
- **Eingaben und Einheiten:** `BrU`, `TaU`, `HüU` (cm) – Körpermaße Brust-,
  Taillen-, Hüftumfang.
- **Ausgabe und Einheit:** `BrW`, `TaW`, `HüW` (cm) sowie deren Hälften (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Zugabewerte (8/6/4 cm)
  stehen hier als feste Zahlen für Größe 38, PK 4, laut Kopfzeile der Tabelle
  (`tabellen_s177.md`, Tabelle 1); kein Bereich oder `ca.` im Buchtext dieser
  Zeilen.
- **Abhängigkeiten:** Zugabewerte hängen laut Tabellenkopf von Modell und
  Größe/Passgrad ab (vgl. [[Formel 15]], Zugabentabelle Tabelle 7); genauer
  Zusammenhang zwischen beiden Tabellen auf dieser Seite nicht ausgeschrieben.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Ob die Zugabewerte 8/6/4 aus der Zugabentabelle (Tabelle 7) für einen
    bestimmten Passgrad abgeleitet sind oder unabhängig davon fest für
    Größe 38 gelten, ist auf dieser Seite nicht spezifiziert.

## Formel 2 – Armlochtiefe-Zugabe AlT → AlT+

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 2
- **Buchfassung:**
  ```text
  AlT 20,1 + 1,7 = AlT+ 21,8
  ```
- **Technische Formel:**
  ```text
  AlT_plus = AlT + 1,7
  ```
- **Eingaben und Einheiten:** `AlT` (cm) – Armlochtiefe (Körpermaß).
- **Ausgabe und Einheit:** `AlT_plus` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 1,7 cm ohne
  `ca.`.
- **Abhängigkeiten:** keine auf dieser Seite.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** keine.

## Formel 3 – Rückenbreite-Zugabe RüB → RüB+

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 3
- **Buchfassung:**
  ```text
  RüB 16,5 + 0,8 = RüB+ 17,3
  ```
- **Technische Formel:**
  ```text
  RueB_plus = RueB + 0,8
  ```
- **Eingaben und Einheiten:** `RueB` (cm) – Rückenbreite (½, Körpermaß).
- **Ausgabe und Einheit:** `RueB_plus` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 0,8 cm ohne
  `ca.`.
- **Abhängigkeiten:** keine auf dieser Seite.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** keine.

## Formel 4 – Armdurchmesser-Zugabe ArD → ArD+ mit Teilwerten ¼ und ⅓

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 4
- **Buchfassung:**
  ```text
  ArD 9,3 + 2 = ArD+ 11,3; ¼ = 2,8; ⅓ = 3,8
  ```
- **Technische Formel:**
  ```text
  ArD_plus = ArD + 2
  ArD_viertel = ArD_plus / 4
  ArD_drittel = ArD_plus / 3
  ```
- **Eingaben und Einheiten:** `ArD` (cm) – Armdurchmesser (Körpermaß).
- **Ausgabe und Einheit:** `ArD_plus`, `ArD_viertel`, `ArD_drittel` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 2 cm ohne
  `ca.`.
- **Abhängigkeiten:** keine auf dieser Seite.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Nachrechnen: 11,3 / 4 = 2,825 (Buch rundet auf 2,8); 11,3 / 3 = 3,7667…
    (Buch rundet auf 3,8, aufgerundet statt abgerundet) – Buchwert unverändert
    übernommen, keine stille Korrektur.

## Formel 5 – Brustbreite-Zugabe BrB → BrB+

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 5
- **Buchfassung:**
  ```text
  BrB 18,2 + 1,2 = BrB+ 19,4
  ```
- **Technische Formel:**
  ```text
  BrB_plus = BrB + 1,2
  ```
- **Eingaben und Einheiten:** `BrB` (cm) – Brustbreite (½, Körpermaß).
- **Ausgabe und Einheit:** `BrB_plus` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 1,2 cm ohne
  `ca.`.
- **Abhängigkeiten:** keine auf dieser Seite.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** keine.

## Formel 6 – Kontrolle ½ BrU

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Kontrolle: Σ = ½ BrU | 44 + 4 = ½ BrW 48
  ```
- **Technische Formel:**
  ```text
  BrU_halb = BrU / 2                     (= 44)
  kontrolle = BrU_halb + zugabe_BrU/2    (= 44 + 4 = 48)
  pruefung: kontrolle == BrW_halb        (vgl. Formel 1)
  ```
- **Eingaben und Einheiten:** `BrU` (cm), `zugabe_BrU` = 8 cm (aus Formel 1).
- **Ausgabe und Einheit:** `kontrolle` (cm) – Prüfwert gegen `BrW_halb`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine, reine
  Konsistenzprüfung zwischen zwei Rechenwegen (erst halbieren + halbe Zugabe
  vs. erst addieren + halbieren).
- **Abhängigkeiten:** [[Formel 1]] (BrW, BrW_halb).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Ob „Σ" in der Buchfassung nur die Spaltenüberschrift für ½ BrU ist oder
    fachlich eine eigenständige Summe mehrerer Teilbreiten meint, bleibt aus
    dem Wortlaut dieser Seite nicht abschließend eindeutig; die Rechnung
    selbst (44 + 4 = 48) ist unabhängig davon nachvollzogen.

## Formel 7 – Schulterbreite → SuNL

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 7
- **Buchfassung:**
  ```text
  SuB 12,2 + 0,4 = SuNL 12,6
  ```
- **Technische Formel:**
  ```text
  SuNL = SuB + 0,4
  ```
- **Eingaben und Einheiten:** `SuB` (cm) – Schulterbreite (Körpermaß).
- **Ausgabe und Einheit:** `SuNL` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 0,4 cm ohne
  `ca.`.
- **Abhängigkeiten:** [[Formel 8]] (SuNL als Eingabe für hSuNL).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** keine.

## Formel 8 – Hintere Schulternahtlänge hSuNL

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 8
- **Buchfassung:**
  ```text
  hSuNL: 12,6 + 0,7 = 13,3; Einhalteweite 0,5 bis 1 cm
  ```
- **Technische Formel:**
  ```text
  hSuNL = SuNL + 0,7
  einhalteweite ∈ [0,5 cm, 1 cm]
  ```
- **Eingaben und Einheiten:** `SuNL` (cm, aus Formel 7).
- **Ausgabe und Einheit:** `hSuNL` (cm); `einhalteweite` (cm, Bereich).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „0,5 bis 1 cm"
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel 7]] (SuNL).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Die mechanisch aus der OCR gezogene Rohtabelle (`tabellen_s177.md`, Tabelle
    2) liest die Einhalteweite als „0,5 cm bis 5cm"; Werners Bestätigung in
    `s177.md` lautet „0,5 bis 1 cm". Für diese Normalisierung gilt Werners
    bestätigte Fassung. Die abweichende Rohlesart bleibt in `formeln_s177.md`
    dokumentiert.

## Formel 9 – Schulterwinkel SuWi

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 9
- **Buchfassung:**
  ```text
  SuWi | Schulterwinkel (in Grad °) | 20° auf lockerung | --- = | SuWi | 20°
  ```
- **Technische Formel:**
  ```text
  SuWi = 20°
  ```
- **Eingaben und Einheiten:** keine Eingabe erkennbar; `SuWi` scheint fester
  Ausgangswert.
- **Ausgabe und Einheit:** `SuWi` (Grad °).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Zusatz „auf lockerung"
  (vermutlich „auf Lockerung", OCR-Tippfehler unverändert übernommen) nicht
  näher erläutert; „--- =" könnte „keine Korrektur/Zuschlag" bedeuten, ist auf
  dieser Seite nicht ausgeschrieben.
- **Abhängigkeiten:** keine auf dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht am Original bestätigt (Walking Skeleton, Blocker übersprungen).
  - Bedeutung von „--- =" und „auf lockerung" ungeklärt.

## Formel 10 – Balancemaße RÜL, VL, Differenz, korrigierte Balance

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 10
- **Buchfassung:**
  ```text
  RÜL | Rückenlänge (waagerechte Taille) | 41,6 | ± --- = | RÜL | 41,6
  VL | Vorderlänge (waagerechte Taille) | 45,3 | ± --- = | VL | 45,3
  Differenz VL - RÜL = | individuelle Balance = | 3,7 | korrigierte Balance = | 3,7
  BaI | optimale Balance aus Maßtabelle | 3,5
  ```
- **Technische Formel:**
  ```text
  individuelle_balance = VL - RUEL          (= 45,3 - 41,6 = 3,7)
  korrigierte_balance = individuelle_balance + korrektur   (korrektur hier: 0)
  vergleich: korrigierte_balance vs. BaI    (3,7 vs. 3,5 aus Maßtabelle)
  ```
- **Eingaben und Einheiten:** `RÜL`, `VL` (cm) – Rücken-/Vorderlänge
  (waagerechte Taille); `BaI` (cm) – optimale Balance aus Maßtabelle
  (Referenzwert, Herkunft nicht auf dieser Seite).
- **Ausgabe und Einheit:** `individuelle_balance`, `korrigierte_balance` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „± ---" bei RÜL und VL
  deutet auf „keine Korrektur" hin, ist aber nicht ausdrücklich im Buchtext
  dieser Seite erklärt. Nachrechnen: 45,3 − 41,6 = 3,7 ✓ (stimmt mit Buchwert
  überein).
- **Abhängigkeiten:** `BaI` stammt vermutlich aus einer Maßtabelle außerhalb
  dieser Seite; Quelle nicht ermittelt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht am Original bestätigt (Walking Skeleton, Blocker übersprungen).
  - Bedeutung von „± ---" ungeklärt.
  - Wie „korrigierte Balance" von „individuelle Balance" abweichen könnte
    (Korrekturregel) ist auf dieser Seite nicht ausgeschrieben; im
    vorliegenden Beispiel sind beide Werte identisch (3,7).
  - Verhältnis zwischen `korrigierte_balance` (3,7) und `BaI` (3,5) – ob und
    wie ein Vergleich/eine weitere Korrektur daraus folgt, ist offen.

## Formel 11 – Taillenausfall TaAf

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 11
- **Buchfassung:**
  ```text
  TaAf | Taillenausfall | gemessene TaB | - ½ TaW =
  ```
- **Technische Formel:**
  ```text
  TaAf = gemessene_TaB - TaW_halb
  ```
- **Eingaben und Einheiten:** `gemessene_TaB` (cm) – am Körper/Modell
  gemessene Taillenbreite; `TaW_halb` (cm, aus Formel 1).
- **Ausgabe und Einheit:** `TaAf` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Zahlenwerte auf
  dieser Seite eingetragen – reine Formelzeile ohne Rechenbeispiel.
- **Abhängigkeiten:** [[Formel 1]] (TaW_halb).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht am Original bestätigt (Walking Skeleton, Blocker übersprungen).
  - Kein Rechenbeispiel auf dieser Seite zur Gegenprobe vorhanden.

## Formel 12 – Hüftfehlbetrag HüFb

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 12
- **Buchfassung:**
  ```text
  HüFb | Hüftfehlbetrag | gemessene HüB | - ½ HüW =
  ```
- **Technische Formel:**
  ```text
  HueFb = gemessene_HueB - HueW_halb
  ```
- **Eingaben und Einheiten:** `gemessene_HueB` (cm); `HueW_halb` (cm, aus
  Formel 1).
- **Ausgabe und Einheit:** `HueFb` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Zahlenwerte auf
  dieser Seite eingetragen.
- **Abhängigkeiten:** [[Formel 1]] (HueW_halb).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht am Original bestätigt (Walking Skeleton, Blocker übersprungen).
  - Kein Rechenbeispiel auf dieser Seite zur Gegenprobe vorhanden.

## Formel 13 – Mehrweite im Armloch

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 13
- **Buchfassung:**
  ```text
  Mehrweite im Armloch | vAlU | + hAlU | - AlaU =
  ```
- **Technische Formel:**
  ```text
  mehrweite_armloch = vAlU + hAlU - AlaU
  ```
- **Eingaben und Einheiten:** `vAlU`, `hAlU`, `AlaU` (cm) – vordere/hintere
  Armlochweite und Ärmel-Armlochweite (Abkürzungen aus dem Buchtext dieser
  Seite nicht weiter erläutert).
- **Ausgabe und Einheit:** `mehrweite_armloch` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Zahlenwerte auf
  dieser Seite eingetragen.
- **Abhängigkeiten:** [[Formel 14]] (Sollwert der Mehrweite als Vergleichsgröße).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht am Original bestätigt (Walking Skeleton, Blocker übersprungen).
  - Bedeutung von `vAlU`, `hAlU`, `AlaU` nur aus Kürzel erschlossen, nicht im
    Buchtext dieser Seite ausgeschrieben.

## Formel 14 – Sollwert der Mehrweite

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 14
- **Buchfassung:**
  ```text
  Sollwert der Mehrweite | = 2 · Zugabe zur AlT | (Toletanz +2 cm bis -1 cm) =
  ```
- **Technische Formel:**
  ```text
  sollwert_mehrweite = 2 * zugabe_AlT
  toleranz ∈ [-1 cm, +2 cm]
  ```
- **Eingaben und Einheiten:** `zugabe_AlT` (cm) – vermutlich die Zugabe zur
  Armlochtiefe (vgl. Formel 2, `AlT_plus − AlT` = 1,7 cm), auf dieser Seite
  aber nicht ausdrücklich verknüpft.
- **Ausgabe und Einheit:** `sollwert_mehrweite` (cm); `toleranz` (cm, Bereich).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Toleranzbereich „+2 cm
  bis -1 cm" bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel 13]] (Vergleich mit `mehrweite_armloch`);
  möglich [[Formel 2]] (`zugabe_AlT`), nicht auf dieser Seite bestätigt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht am Original bestätigt (Walking Skeleton, Blocker übersprungen).
  - Ob `zugabe_AlT` hier dieselbe Zugabe wie in Formel 2 (1,7 cm) meint, ist
    auf dieser Seite nicht ausdrücklich gesagt.
  - OCR-Schreibweise „Toletanz" (statt „Toleranz") unverändert übernommen.

## Formel 15 – Zugabentabelle für Oberteil-Konstruktionen (Passgrad → Zugaben)

- **Quelle:** [`formeln_s177.md`](formeln_s177.md), Abschnitt 15
- **Buchfassung:**
  ```text
  Pass Arm-Muise | Zugaben (für den ganzen Schnitt): HU, TaU, HüU, AlT | BrW-Zugaben (für ½ Schnitt): HüB, ArD, BrA | SuB
  0 | 0 | 0 | 0 | 0 - 0,5 | 0 | 0 | 0 - 0,4 | 0
  1 | 2 | 0 - 2 | 0 - 2 | 0,2 - 0,7 | 0,1 | 0,3 | 0,6 | 0,1
  2 | 4 | 2 - 4 | 2 - 4 | 0,5 - 1 | 0,3 | 0,9 | 0,8 | 0,2
  3 | 6 | 4 - 6 | 4 - 6 | 1,3 | 0,5 | 1,5 | 1 | 0,3
  4 | 8 | 4 - 8 | 4 - 8 | 1,7 | 0,8 | 2 | 1,2 | 0,4
  5 | 10 | 8 - 12 | 6 - 8 | 2,1 | 1,1 | 2,5 | 1,4 | 0,5
  6 | 12 | 8 - 16 | 6 - 10 | 2,5 | 1,4 | 3 | 1,6 | 0,6
  7 | 14 | 12 - 16 | 8 - 12 | 3 | 1,6 | 3,6 | 1,8 | 0,7
  8 | 16 | 12 - 20 | 8 - 16 | 3,5 | 1,8 | 4,2 | 2 | 0,8
  9 | 18 | 12 - 20 | 10 - 20 | 4 | 2 | 5 | 2 | 0,9
  10 | 20 | 16 - 24 | 10 - 24 | 4,5 | 2,2 | 5,8 | 2 | 1
  ```
- **Technische Formel:**
  ```text
  zugaben(passgrad) = tabellenzeile[passgrad]   (passgrad ∈ {0..10})
  ```
  Nachschlagetabelle, keine geschlossene Formel; pro `passgrad` (Spalte
  „Pass Arm-Muise") liefert die Zeile die Zugaben für `HU`, `TaU` (Bereich ab
  Grad 1), `HüU` (Bereich ab Grad 1), `AlT` (Bereich durchgehend), `HüB`,
  `ArD`, `BrA`, `SuB`.
- **Eingaben und Einheiten:** `passgrad` (ganzzahlig 0–10, dimensionslose
  Passstufe „Pass Arm-Muise").
- **Ausgabe und Einheit:** Zugabewerte je Spalte (cm), teils fest, teils als
  Bereich.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Mehrere Spalten
  (`TaU`, `HüU` ab Grad 1, `AlT` durchgehend) geben Bereiche statt fester Werte
  an; kein Default innerhalb eines Bereichs ausgewählt.
- **Abhängigkeiten:** möglich [[Formel 1]] (Zugaben zu BrU/TaU/HüU für
  Größe 38, PK 4 könnten einem bestimmten Passgrad dieser Tabelle entsprechen);
  auf dieser Seite nicht ausdrücklich verknüpft.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht am Original bestätigt (Walking Skeleton, Blocker übersprungen).
  - Spaltenköpfe der Rohtabelle sind über zwei Zeilen verteilt und teils
    doppeldeutig (`HU` vs. `HüU`, `HüB` vs. `HüU`); Zuordnung hier nach
    bestem Verständnis zusammengeführt, nicht am Original geprüft.
  - Zusammenhang zu den festen Zugaben aus Formel 1 (8/6/4 cm) ungeklärt.
