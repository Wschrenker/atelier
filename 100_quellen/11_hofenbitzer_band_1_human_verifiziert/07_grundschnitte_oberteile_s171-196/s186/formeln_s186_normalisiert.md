# Formeln s186 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s186.md`](formeln_s186.md) vermerkt, ist nur ein
kleiner Teil dieser Seite von Werner am Original bestätigt (siehe dort und
`s186.md`, Abschnitt „Vorab geklärte formel- und coderelevante Stellen"). Alle
Formeln stehen deshalb auf `offen`, auch wenn einzelne Teilaussagen bereits
bestätigt sind. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
vollständige Bestätigung.

## Formel 1 – Konstruktionstabelle: Grundmaß + Zugabe = Konstruktionsmaß

- **Quelle:** [`formeln_s186.md`](formeln_s186.md), Abschnitt 1
- **Buchfassung:**
  ```text
  BHJ  Brustumfang     88  6 → BrW   94   ½ 47
  TAU  Taillenumfang   72  4 → TaW   76   ½ 38
  HGU  Haftumfang      97  4 → HüW  101   ½ 50,5
  ALT  Armüschnärh    201  1,3 → ALT+ 21,4
  RUB  Rückenbreite(½)16,5 0,5 → RUB+  17
  ArD  Armdurchmesser  9,3 1,5 → ArD+  10,8  ¼ 2,7  ⅓ 3,6
  BrB  Brustbreite(½) 18,2 1   → BrB+  19,2
  —    Kontrolle Σ=½BrU 44 3   → ½BrW  47
  ```
- **Technische Formel:**
  ```text
  Maß+ = Maß + Zugabe
  Bruchteil_n = Faktor_n * Maß+      (Faktor_n ∈ {½, ¼, ⅓}, je nach Zeile)
  ```
- **Eingaben und Einheiten:** `Maß` (cm, gemessenes Körpermaß je Zeile: BrU,
  TaU, HüU, AlT, RüB, ArD, BrB); `Zugabe` (cm, je Zeile fest vorgegeben).
- **Ausgabe und Einheit:** `Maß+` (cm, Konstruktionsmaß je Zeile: BrW, TaW,
  HüW, AlT+, RüB+, ArD+, BrB+); `Bruchteil_n` (cm) für die Zeilen mit
  Bruchspalte.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Feste Werte je Zeile,
  keine `ca.`-Angaben. Für `ArD+` sind laut Vorab-geklärt-Abschnitt zwei
  Bruchteile gleichzeitig angegeben (¼ und ⅓); für die übrigen Zeilen mit
  Bruchspalte nur ½. Welche Zeile welchen Bruchteil führt, ist noch nicht für
  jede Zeile einzeln am Original bestätigt.
- **Abhängigkeiten:** `TaW` und `HüW` sind Eingaben für [[Formel 3]]
  (Taillenausfall) und [[Formel 6]] (Hüft-Fehlbetrag). Zeile „ALT 201 1,3 →
  ALT+ 21,4" wirkt zahlenmäßig unplausibel (Grundwert 201 im Vergleich zu den
  übrigen Zeilen); nicht korrigiert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Alle Kürzel/Bezeichnungen außer `ArD+` sind laut `s186.md` Prüfstelle 2
    noch nicht am Original bestätigt.
  - Die OCR-Rohwerte der ArD-Bruchspalte („¼ 4,7", „1½ 3,6") weichen von den
    bestätigten Werten (¼ = 2,7 cm, ⅓ = 3,6 cm) ab; nicht aufgeklärt, ob dies
    ein OCR-Lesefehler ist.
  - Zeile „ALT 201 1,3 → ALT+ 21,4": Plausibilität des Grundwerts 201 offen.
  - Bedeutung der Zugabenspalte (additiv vs. andere Operation) nur über das
    generische Muster „Grundmaß + Zugabe = Konstruktionsmaß" angenommen, für
    diese Seite nicht einzeln bestätigt.

## Formel 2 – Taillenbreite (TaB)

- **Quelle:** [`formeln_s186.md`](formeln_s186.md), Abschnitt 2
- **Buchfassung:**
  ```text
  vTaB und hTaB messen, beide addieren = Taillenbreite (TaB)
  vTaB + hTaB = TaB
  ```
- **Technische Formel:**
  ```text
  TaB = vTaB + hTaB
  ```
- **Eingaben und Einheiten:** `vTaB` (cm), `hTaB` (cm) – Teilabstände an der
  Taillenlinie.
- **Ausgabe und Einheit:** `TaB` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; einfache Summe.
- **Abhängigkeiten:** `TaB` ist Eingabe für [[Formel 3]] (Taillenausfall).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Bezugspunkte „vlk" und „hA" im Fließtext vermutlich „vM"/„hM" (laut
    `s186.md` Prüfstelle 3), nicht am Original bestätigt.

## Formel 3 – Taillenausfall (TaAf)

- **Quelle:** [`formeln_s186.md`](formeln_s186.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Taillenausfall (TaAf)
  = TaB − ½ TaW
  = 46,2 cm − 38,5 cm
  = 7,7 cm
  ```
- **Technische Formel:**
  ```text
  TaAf = TaB - 0.5 * TaW
  ```
- **Eingaben und Einheiten:** `TaB` (cm, aus [[Formel 2]]), `TaW` (cm, aus
  [[Formel 1]], Zeile TAU).
- **Ausgabe und Einheit:** `TaAf` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; fester
  Rechenweg laut Buchtext.
- **Abhängigkeiten:** [[Formel 1]] (liefert `TaW = 76 cm`, also `½ TaW =
  38 cm`), [[Formel 2]] (liefert `TaB`). Nachrechnung: Das gedruckte Beispiel
  nennt `TaB = 46,2 cm`; mit `½ TaW = 38,5 cm` (also `TaW = 77 cm`, nicht
  `76 cm` aus Tabelle 1) ergibt sich `46,2 − 38,5 = 7,7 cm`, was zum
  gedruckten Ergebnis passt. Der TaW-Wert im Beispiel (77 cm → 38,5 cm) weicht
  damit von `TaW = 76 cm` (½ = 38 cm) in Tabelle 1 ab; beide Werte stehen so
  gedruckt nebeneinander, nicht aufgelöst.
  `TaAf` (7,7 cm) stimmt mit der Summe der Verteilung in [[Formel 4]]
  überein (2 + 2 + 0 + 3,7 = 7,7 cm).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Symbol „½" in der OCR nur als „1%" erkannt; die Lesung „½" ist laut
    `s186.md` (Vorab geklärte Stellen) bestätigt.
  - Abweichung zwischen `TaW = 76 cm` (Tabelle 1) und dem im TaAf-Beispiel
    implizierten `TaW = 77 cm` nicht aufgelöst, siehe oben.
  - Kürzel-Identität von `TaB`/`TaW` in der großen Konstruktionstabelle laut
    `s186.md` Prüfstelle 2 nicht einzeln bestätigt.

## Formel 4 – Verteilung des Taillenausfalls (Beispielrechnung)

- **Quelle:** [`formeln_s186.md`](formeln_s186.md), Abschnitt 4
- **Buchfassung:**
  ```text
  1 SN 2×1cm = 2cm
  2 vAbI = 2 cm
  3 optional shAbI hier = 0 cm
  4 hAbI = 3,7 cm
  Summe des Ausfalls = 7,7 cm

  vAbI:  0 bis maximal 2,5 cm
  an SN: ca. 0 bis 2 cm
  shAbI: ca. 0 bis 3 cm
  hAbI:  ca. 2 bis 4,5 cm
  ```
- **Technische Formel:**
  ```text
  summe_ausfall = sn_anteil + vAbI + shAbI + hAbI
  sn_anteil = 2 * sn_je_seite               (Beispiel: 2 * 1 cm = 2 cm)

  Bereiche:
  vAbI  ∈ [0 cm, 2,5 cm]
  sn_je_seite ∈ [ca. 0 cm, ca. 2 cm]
  shAbI ∈ [ca. 0 cm, ca. 3 cm]              (optional, kann 0 sein)
  hAbI  ∈ [ca. 2 cm, ca. 4,5 cm]
  ```
- **Eingaben und Einheiten:** `sn_je_seite`, `vAbI`, `shAbI`, `hAbI` (jeweils
  cm), Anteile des Taillenausfalls an den vier Abnäher-/Nahtpositionen.
- **Ausgabe und Einheit:** `summe_ausfall` (cm), muss gleich [[Formel 3]]
  (`TaAf`) sein.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `vAbI` hat eine feste
  Obergrenze ohne „ca." (0 bis maximal 2,5 cm); `an SN`, `shAbI`, `hAbI` sind
  `ca.`-Bereiche. `shAbI` ist ausdrücklich als „optional" bezeichnet und kann
  0 sein. Kein Default/keine feste Aufteilungsregel im Buchtext – die
  Verteilung auf die vier Positionen bleibt eine fachliche Auswahl innerhalb
  der Bereiche, solange die Summe `TaAf` ergibt.
- **Abhängigkeiten:** Summe muss [[Formel 3]] (`TaAf`) entsprechen; im
  gedruckten Beispiel bestätigt sich das: `2 + 2 + 0 + 3,7 = 7,7 cm`.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Die Bereichsangaben stammen aus der Zeichnung, nicht aus dem Fließtext;
    laut `s186.md` Prüfstelle 6 nicht am Original bestätigt.
  - Ob vor jeder Aufzählungszeile im Original ein Kreissymbol (①–④) steht,
    ist laut `s186.md` Prüfstelle 4 offen.
  - Keine Buchregel für die Aufteilungsreihenfolge/-priorität zwischen den
    vier Positionen bei abweichenden `TaAf`-Werten erkennbar; hier keine
    eigene Regel ergänzt.

## Formel 5 – Hüftbreite (HüB)

- **Quelle:** [`formeln_s186.md`](formeln_s186.md), Abschnitt 5
- **Buchfassung:**
  ```text
  V HUB und hHUB messen und addieren = Hufbreite (HUB).
  vHüB + hHüB = HüB
  ```
- **Technische Formel:**
  ```text
  HuB = vHueB + hHueB
  ```
- **Eingaben und Einheiten:** `vHüB` (cm), `hHüB` (cm).
- **Ausgabe und Einheit:** `HüB` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; einfache Summe.
- **Abhängigkeiten:** `HüB` ist Eingabe für [[Formel 6]] (Hüft-Fehlbetrag).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - OCR-Schreibweisen „V HUB", „hHUB", „Hufbreite (HUB)" unverändert
    übernommen; Lesbarkeit am Original noch zu bestätigen.

## Formel 6 – Hüft-Fehlbetrag (HüFb)

- **Quelle:** [`formeln_s186.md`](formeln_s186.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Hüft-Fehlbetrag (HüFb)
  = HüB − ½ HüW
  = 46,5 cm − 51 cm
  = −4,5 cm → 4,5 cm   ν₂ = 2,2 cm

  Jeweils den halben HüFb (hier 2,2 cm) an den Seitenlinien ausstellen.
  ```
- **Technische Formel:**
  ```text
  HueFb_signed = HuB - 0.5 * HueW
  HueFb = abs(HueFb_signed)
  ausstellung_je_seite = HueFb / 2
  ```
- **Eingaben und Einheiten:** `HüB` (cm, aus [[Formel 5]]), `HüW` (cm, aus
  [[Formel 1]], Zeile HGU).
- **Ausgabe und Einheit:** `HüFb` (cm, Betrag), `ausstellung_je_seite` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Vorzeichenwechsel
  „−4,5 cm → 4,5 cm" laut Buchtext ausdrücklich als Betragsbildung
  dargestellt (Defizit wird als positiver Ausstellbetrag verwendet).
- **Abhängigkeiten:** [[Formel 1]] (liefert `HüW = 101 cm`, also
  `½ HüW = 50,5 cm`), [[Formel 5]] (liefert `HüB`). Nachrechnung: Gedrucktes
  Beispiel nennt `HüB = 46,5 cm`, `½ HüW = 51 cm` (also `HüW = 102 cm`, nicht
  `101 cm` aus Tabelle 1) → `46,5 − 51 = −4,5 cm`, passt zum gedruckten
  Zwischenergebnis. Halbierung: `4,5 : 2 = 2,25 cm`, gerundet `≈ 2,3 cm` –
  der gedruckte Wert lautet jedoch `ν₂ = 2,2 cm`. Diese Abweichung ist laut
  `s186.md` (Vorab geklärte Stellen) von Werner unabhängig nachgerechnet und
  ausdrücklich als offene Diskrepanz vermerkt, nicht aufgelöst:
  ```text
  gedruckt:      ν₂ = 2,2 cm
  nachgerechnet: 4,5 cm : 2 = 2,25 cm ≈ 2,3 cm
  ```
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Zahlenwiderspruch `HüW = 101 cm` (Tabelle 1) vs. implizit `HüW = 102 cm`
    (HüFb-Beispiel) nicht aufgelöst.
  - Zahlenwiderspruch zwischen gedrucktem `ν₂ = 2,2 cm` und nachgerechnetem
    `2,25 cm ≈ 2,3 cm` bleibt offen; keiner der beiden Werte wurde als
    Default gewählt.
  - Kürzel-Identität von `HüB`/`HüW` in der großen Konstruktionstabelle laut
    `s186.md` Prüfstelle 2 nicht einzeln bestätigt.

## Formel 7 – Kleine Kontrolltabelle (TaAf/HüFb)

- **Quelle:** [`formeln_s186.md`](formeln_s186.md), Abschnitt 7
- **Buchfassung:**
  ```text
  Brustmenge (A)     46    → ½ TaW  38    → 8
  Armückmenge (AB)   46,5  → ½ HüW  50,5  → 4
  ```
- **Technische Formel:**
  ```text
  zeile_1_ergebnis = 46   - 38    = 8    (Vorzeichen laut Buchdruck: 8, ungeprüft)
  zeile_2_ergebnis = 46,5 - 50,5  = -4   (Vorzeichen bestätigt: -4)
  ```
- **Eingaben und Einheiten:** Zeile 1: `46` (cm, „Brustmenge (A)"), `38`
  (cm, „½ TaW"); Zeile 2: `46,5` (cm, „Armückmenge (AB)"), `50,5`
  (cm, „½ HüW").
- **Ausgabe und Einheit:** `zeile_1_ergebnis`, `zeile_2_ergebnis` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** Zeile 2 entspricht rechnerisch näherungsweise
  [[Formel 6]] (`46,5 − 50,5 = −4` vs. `HüB − ½HüW` mit anderen
  Detailwerten `46,5 − 51 = −4,5`); nicht als Beleg für Formel 6 verwendet,
  nur nebeneinandergestellt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Für Zeile 2 ist das Vorzeichen `−4` laut `s186.md` (Vorab geklärte
    Stellen) am Original bestätigt (OCR zeigte „4" ohne Vorzeichen).
  - Für Zeile 1 ist kein Vorzeichen bestätigt; der gedruckte Wert „8" wird
    unverändert übernommen.
  - Bezeichnungen „Brustmenge (A)"/„Armückmenge (AB)" wirken laut `s186.md`
    verlesen (vermutlich „gemessene TaB"/„gemessene HüB"); nicht korrigiert.
  - Verhältnis dieser Tabelle zu [[Formel 3]] und [[Formel 6]] (gleiche
    Rechenart, leicht andere Werte) nicht fachlich geklärt.
