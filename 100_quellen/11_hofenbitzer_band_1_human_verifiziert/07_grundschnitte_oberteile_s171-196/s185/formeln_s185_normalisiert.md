# Formeln s185 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s185.md`](formeln_s185.md) vermerkt, ist die
Seite als Ganzes noch nicht menschlich verifiziert. Alle Formeln stehen
deshalb unabhängig vom Bestätigungsgrad einzelner Zahlenwerte auf `offen`.
Vier Rechenergebnisse (Formeln 1, 3, 6, 7) sind bereits von Werner am
Original bestätigt – das ist bei „Offene Fragen oder Widersprüche" jeweils
vermerkt und bleibt ein Fakt, keine offene Frage. Dies ist ein
Walking-Skeleton-Durchlauf, kein Ersatz für die noch fehlende Bestätigung
der übrigen Seite.

## Formel 1 – Aufteilung des Taillenausfalls

- **Quelle:** [`formeln_s185.md`](formeln_s185.md), Abschnitt 1
- **Buchfassung:**
  ```text
  0 bis 2 cm  SN     2 × 1 cm  = 2,0 cm
  1 bis 3 cm  shAbl            = 2,0 cm
  2 bis 4 cm  hAbl             = 2,8 cm
  T = Kontrolle TaAf           = 6,8 cm
  ```
- **Technische Formel:**
  ```text
  sn_anteil    = 2 × 1 cm        = 2,0 cm
  shabl_anteil = ?                = 2,0 cm   (Rechenweg in OCR nicht erfasst)
  habl_anteil  = ?                = 2,8 cm   (Rechenweg in OCR nicht erfasst)
  kontrolle_taaf = sn_anteil + shabl_anteil + habl_anteil = 6,8 cm  (Beobachtung, nicht bestätigt)
  ```
- **Eingaben und Einheiten:** Bereichsangaben „0 bis 2 cm", „1 bis 3 cm",
  „2 bis 4 cm" (cm) je Zeile; Bedeutung dieser Bereiche zur Formel nicht
  geklärt.
- **Ausgabe und Einheit:** `sn_anteil`, `shabl_anteil`, `habl_anteil`,
  `kontrolle_taaf` (alle cm) als Anteile des Taillenausfalls (TaAf).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bedeutung der
  linken Bereichsspalte („0 bis 2 cm" usw.) zur restlichen Zeile ungeklärt.
- **Abhängigkeiten:** Bezug zu [[Formel 3]] (Kontrollwert 6,8 cm taucht dort
  in anderer Tabelle als „TaB − ½ TaW" wieder auf) nicht geklärt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Zeile 1 („2 × 1 cm = 2,0 cm") ist von Werner am Original bestätigt.
  - Zeilen 2–4 sind nicht bestätigt; der Rechenweg der mittleren Spalte
    fehlt in der OCR-Tabelle vollständig.
  - Ob „Kontrolle TaAf = 6,8 cm" tatsächlich die Summe der drei Zeilen
    darüber ist, ist eine unbestätigte Beobachtung.

## Formel 2 – Hüftausfall (HüAf) im Vorderteil

- **Quelle:** [`formeln_s185.md`](formeln_s185.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Hüftausfall (HüAf)
  = vAbl -2cm
  = 3,2cm - 2cm
  = 1,2cm
  ```
- **Technische Formel:**
  ```text
  HüAf = vAbl - 2 cm
  ```
- **Eingaben und Einheiten:** `vAbl` (cm) – vermutlich „vorderer Abnäher"
  oder vergleichbare Vorderteil-Bezugsgröße; Bedeutung nicht abschließend
  geklärt.
- **Ausgabe und Einheit:** `HüAf` (cm), Hüftausfall.
- **Bereiche, Bedingungen und Auswahlentscheidungen:**
  ```text
  HüAf < 0,5 cm  → kein Hüftausfall zeichnen
  0,5 cm ≤ HüAf ≤ 1 cm → ggf. vernachlässigbar (fachliche Auswahl)
  HüAf < 0 (Minusbetrag) → kein Hüftausfall zeichnen
  ```
  Alle drei Fälle führen zum „taillierten Oberteil-Grundschnitt ohne
  Hüftausfall auf Seite 186" (Querverweis).
- **Abhängigkeiten:** Alternativkonstruktion bei HüAf ≈ 0 auf Seite 186
  (nicht kopiert, nur Verweis).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Teil dieser Formel ist von Werner am Original bestätigt (s185.md,
    Prüfstelle 5).
  - Genaue Bedeutung/Herkunft von `vAbl` nicht aus dieser Seite ableitbar.
  - Ob die drei Bereichsregeln exklusiv oder mit Überschneidung gelten
    (z. B. bei genau 0,5 cm oder genau 1 cm), ist im Buchtext nicht
    präzisiert.

## Formel 3 – Hüft-Fehlbetrag (HüFb)

- **Quelle:** [`formeln_s185.md`](formeln_s185.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Hüft-Fehlbetrag (HüFb)
  = HUB - 1/2HüW
  = 44,9cm - 50,5cm
  = -5,6cm → 5,6cm 1/2 = 2,8cm
  ```
- **Technische Formel:**
  ```text
  HüFb = HüB - HüW / 2
  halber_HüFb = |HüFb| / 2
  ```
- **Eingaben und Einheiten:** `HüB` (cm, gemessener Hüftumfang inkl.
  Vorder- und Rückenanteil ohne Hüftausfall), `HüW` (cm, Hüftweite/Maßtabelle).
- **Ausgabe und Einheit:** `HüFb` (cm, kann negativ sein), `halber_HüFb`
  (cm) zum Ausstellen an den Seitenlinien.
- **Bereiche, Bedingungen und Auswahlentscheidungen:**
  ```text
  |HüFb| < 2 cm  → HüU unterproportional
  |HüFb| > 8 cm  → HüU überproportional
  ```
  Beide Fälle als möglicher Hinweis auf ein Figurproblem (Band 2), keine
  automatische Korrekturregel auf dieser Seite.
- **Abhängigkeiten:** Zahlenwerte decken sich mit [[Formel 4]] (Tabelle
  „gemessene HüB 44,9 − ½ HüW 50,5 = −5,6"); ob beide Stellen dieselbe
  Rechnung sind oder unabhängige Belege, ist offen.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Der letzte Rechenschritt „5,6 cm : 2 = 2,8 cm" ist von Werner am
    Original bestätigt.
  - „HüB 44,9 − ½ HüW 50,5 = −5,6" sowie die Bereichsregeln (< 2 cm, > 8 cm)
    sind nicht bestätigt (s185.md, Prüfstelle 5 und 6).
  - Herkunft von `HüB` als Summe „vHüB + hHüB" wird im Fließtext erwähnt
    („HÜB und hHÜB … messen, addieren = HÜB"), aber in der Formel selbst
    nicht ausgeschrieben – möglicherweise fehlt hier ein Additionsschritt.

## Formel 4 – Kontrolltabelle TaB/HüB (gemessen − ½ Weite)

- **Quelle:** [`formeln_s185.md`](formeln_s185.md), Abschnitt 4
- **Buchfassung:**
  ```text
  genossene TaB  42,8  - � TaW  36    - 6,8
  genossene H�B  44,9  - � H�W  50,5  - -5,6
  ```
- **Technische Formel:**
  ```text
  kontrolle_taille = TaB - halbe_TaW
  kontrolle_huefte = HüB - halbe_HüW
  ```
  Die Tabellenwerte „36" und „50,5" stehen bereits für `halbe_TaW` bzw.
  `halbe_HüW` (nicht für TaW/HüW selbst): 42,8 − 36 = 6,8 und
  44,9 − 50,5 = −5,6 stimmen so exakt mit der Buchfassung überein.
- **Eingaben und Einheiten:** `TaB` (cm, gemessene Taillenbreite/-umfang),
  `halbe_TaW` (cm, halbe Taillenweite laut Maßtabelle), `HüB`, `halbe_HüW`
  wie in [[Formel 3]].
- **Ausgabe und Einheit:** Kontrollwerte (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine im OCR-Text
  erkennbar.
- **Abhängigkeiten:** [[Formel 3]] – die `HüB`-Zeile dieser Tabelle ist
  zahlengleich mit dem ersten Rechenschritt der dortigen HüFb-Formel
  (44,9 − 50,5 = −5,6, vor der abschließenden Halbierung auf 2,8).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Unabhängig nachgerechnet: Beide Zeilen stimmen rechnerisch, wenn „36"
    bzw. „50,5" als bereits halbierte Weite gelesen werden – kein
    Widerspruch zur Buchfassung.
  - „�" ersetzt in der Mistral-Antwort „½" bzw. „ü" (siehe
    `tabellen_s185.md`); diese Lesart ist noch nicht am Original bestätigt.
  - Nicht geklärt, ob diese Tabelle eine eigenständige Kontrollrechnung ist
    oder nur den Zwischenschritt der HüFb-Formel aus [[Formel 3]] erneut
    zeigt.

## Formel 5 – Kontrolle der Oberbrustbreite

- **Quelle:** [`formeln_s185.md`](formeln_s185.md), Abschnitt 5
- **Buchfassung:**
  ```text
  4a Die Strecke zwischen vM und Armloch messen und mit der halben
  Oberbrustbreite vergleichen.

  Kontrolle = ½ oBrB + 0 bis 1,5 cm
  ```
- **Technische Formel:**
  ```text
  strecke_vM_armloch  (Messwert)
  kontrollwert = oBrB / 2 + delta
  delta ∈ [0 cm, 1,5 cm]
  ```
- **Eingaben und Einheiten:** `strecke_vM_armloch` (cm, Messwert an der
  Zeichnung), `oBrB` (cm, Oberbrustbreite).
- **Ausgabe und Einheit:** Vergleich `strecke_vM_armloch` gegen
  `kontrollwert` (cm); kein expliziter Rückgabewert, nur Vergleichsregel.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Toleranzbereich
  „0 bis 1,5 cm" bleibt Bereich, kein fester Default.
- **Abhängigkeiten:** Bei „unerwünschter Mehrweite" Verweis auf Englische
  Naht, S. 376 (nicht Teil dieser Formel).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Die Zeichnungsbeschriftung „Kontrolle = ½ oBrB + 0 bis 1,5 cm" ist noch
    nicht am Original bestätigt (s185.md, Prüfstelle 11).
  - Ob „vergleichen" eine Prüfregel (Muss-Bereich) oder nur eine
    Plausibilitätskontrolle ohne Konsequenz ist, ist aus dem Fließtext
    allein nicht eindeutig.

## Formel 6 – Mehrweite im Armloch

- **Quelle:** [`formeln_s185.md`](formeln_s185.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Beide Armlochkurven messen und addieren. Hiervon den am Körper gemessenen
  Armansatzumfang (AraU) absenen. Die Differenz ist die Mehrzeiten im
  Armloch.

  vAlU 22,5 + hAlU 24,8 - AraU 44,5 = 2,8 cm
  ```
- **Technische Formel:**
  ```text
  mehrweite_armloch = vAlU + hAlU - AraU
  ```
- **Eingaben und Einheiten:** `vAlU` (cm, vordere Armlochkurve),
  `hAlU` (cm, hintere Armlochkurve), `AraU` (cm, Armansatzumfang, am Körper
  gemessen).
- **Ausgabe und Einheit:** `mehrweite_armloch` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine eigene
  Bedingung in dieser Formel; Sollwertvergleich siehe [[Formel 7]].
- **Abhängigkeiten:** [[Formel 7]] (Sollwert-Vergleich für dieses
  Ergebnis).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Diese Formel samt Zahlenwerten (22,5 + 24,8 − 44,5 = 2,8) ist von
    Werner am Original bestätigt.
  - Die OCR-Tabelle (`tbl-3.md`) zeigt davon abweichend „haAu 22,5 + haU
    24,5 − hAu 44,5 = 2,8" (andere Kürzel, 24,5 statt 24,8) – durch Werners
    Bestätigung ersetzt, nicht die OCR-Lesung.
  - Status trotz bestätigter Zahlen auf `offen`, da die übrige Seite
    (Herkunft/Definition von `vAlU`, `hAlU`, `AraU` im Volltext) noch nicht
    vollständig verifiziert ist.

## Formel 7 – Sollwert der Mehrweite im Armloch

- **Quelle:** [`formeln_s185.md`](formeln_s185.md), Abschnitt 7
- **Buchfassung:**
  ```text
  Sie sollte min- bis zweifachen der destens dem ein- bis zweifachen der
  Zugabe zur AIT entsprechen (siehe Auszug der Konstruktionstabelle unten).

  Sollwert der Mehrweite = 2 × Zugabe zur AlT (Toleranz +2 cm bis −1 cm)
  = 2 × 1,3 = 2,6 cm
  Nur bei Oberteilen mit Brustabnäher!
  ```
- **Technische Formel:**
  ```text
  sollwert_mehrweite = 2 × zugabe_AlT
  zugabe_AlT = 1,3 cm   (bestätigtes Beispiel)
  bereich_mindest_mehrweite = [1 × zugabe_AlT, 2 × zugabe_AlT]
  toleranz_sollwert = [sollwert_mehrweite - 1 cm, sollwert_mehrweite + 2 cm]
  ```
- **Eingaben und Einheiten:** `zugabe_AlT` (cm, Zugabe zur Armlochtiefe,
  vermutete Bedeutung von „AlT").
- **Ausgabe und Einheit:** `sollwert_mehrweite` (cm), `bereich_mindest_mehrweite`
  (cm-Bereich) zum Vergleich mit [[Formel 6]]s Ergebnis.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „ein- bis
  zweifachen der Zugabe zur AlT" bleibt Bereich; Toleranz „+2 cm bis −1 cm"
  um den Sollwert erhalten. Regel gilt laut Buchfassung nur „bei Oberteilen
  mit Brustabnäher" – Auswahlbedingung, nicht weiter spezifiziert.
- **Abhängigkeiten:** [[Formel 6]] (Vergleichswert `mehrweite_armloch`).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Die Rechnung „2 × 1,3 = 2,6 cm" ist von Werner am Original bestätigt.
  - Die zweite Tabellenzeile fehlt in der OCR-Ausgabe von `tbl-3.md`
    vollständig; Wortlaut „(Toleranz +2 cm bis −1 cm)" und „Nur bei
    Oberteilen mit Brustabnäher!" stammen aus `tabellen_s185.md` und sind
    über die bestätigte Rechnung hinaus noch nicht separat am Original
    geprüft.
  - Die Bereichsregel im Fließtext („mindestens dem ein- bis zweifachen der
    Zugabe zur AlT") enthält laut s185.md eine vermutlich doppelt erfasste
    OCR-Passage; unverändert übernommen, nicht bereinigt.
  - Bedeutung von „AlT" (Armlochtiefe?) nicht auf dieser Seite definiert.
