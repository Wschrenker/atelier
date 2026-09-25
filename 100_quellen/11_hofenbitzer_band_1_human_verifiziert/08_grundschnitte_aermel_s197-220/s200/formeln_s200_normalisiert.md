# Formeln normalisiert – s200 (teilweise vorläufig, Walking Skeleton)

Technische Fassung zu [formeln_s200.md](formeln_s200.md). Nur F1 ist laut
[s200.md](s200.md) am Original bestätigt; F2–F10 stammen aus einem
Walking-Skeleton-Durchlauf auf Basis der OCR-Rohfassung und stehen deshalb auf
`offen`, unabhängig von der inhaltlichen Klarheit der Buchfassung. Diese Datei
erzeugt keine Python-Funktion, keinen Engine-Vertrag und keine neue
Fachregel.

## F1 – Einhalteweite (EW) und Ärmelkugelumfang (ÄKU)

- **Quelle:** [formeln_s200.md](formeln_s200.md), Abschnitt 1.
- **Buchfassung:**
  ```text
  Einhalteweite in cm = ÄLU : Einhalteweite in %
  Ärmelkugelumfang = ÄLU + Einhalteweite in cm
  ```
- **Technische Formel:**
  ```text
  EW_cm = AlU * (EW_pct / 100)
  AeKU  = AlU + EW_cm
  ```
- **Eingaben und Einheiten:** `AlU` (Ärmlochumfang, cm); `EW_pct`
  (Einhalteweite, %).
- **Ausgabe und Einheit:** `EW_cm` (cm), `AeKU` (Ärmelkugelumfang, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine — feste
  Rechenvorschrift laut bestätigter Arbeitslesung.
- **Abhängigkeiten:** `AlU` und `EW_pct` kommen aus der Konstruktionstabelle
  ([tabellen_s200.md](tabellen_s200.md)); `AeKU` wird für die
  Grundgerüst-Konstruktion (F2 ff.) nicht direkt weiterverwendet, da dort mit
  `ÄkLI` (Oberarmweite-basiert) gearbeitet wird.
- **Status:** normalisiert. Rechenbeispiel geprüft:
  `41 · 1 % = 0,41 ≈ 0,4`; `41 + 0,4 = 41,4` — stimmt mit der bestätigten
  Arbeitslesung überein.
- **Offene Fragen oder Widersprüche:**
  - Gedruckter Tabellenwert `EW in cm = 0,8 cm` ist laut Bestätigung ein
    Rechenfehler und bleibt nur als Bildbeleg stehen, siehe
    [formeln_s200.md](formeln_s200.md).
  - Gedrucktes Rechenzeichen in der Buchfassung ist ein Doppelpunkt; die
    bestätigte Lesung verwendet Multiplikation.

## F2 – Ärmelkopflinie (ÄkLI), Grundgerüst

- **Quelle:** [formeln_s200.md](formeln_s200.md), Abschnitt 2.
- **Buchfassung:**
  ```text
  Die OaW + 1 bis 1,5 cm zeichnen = ÄkLI.
  ```
- **Technische Formel:** `AekLI = OaW + delta`, `delta ∈ [1; 1,5] cm`.
- **Eingaben und Einheiten:** `OaW` (Oberarmweite, cm, aus Konstruktionstabelle).
- **Ausgabe und Einheit:** `AekLI` (Ärmelkopflinie, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich `[1; 1,5] cm`
  bleibt Bereich; keine Buchregel für die Auswahl innerhalb des Bereichs.
- **Abhängigkeiten:** `OaW` aus Konstruktionstabelle. Eingabe für F7–F10
  (Hilfslinien B–E). Siehe auch F6 (widersprüchliche zweite Definition von
  `ÄkLI`).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Widerspruch zu F6: dort wird `ÄkLI = OaW + Zugabe` ohne Zahlenbereich
    angegeben.

## F3 – Vorderer Bogen (vÄLU-Reduzierung)

- **Quelle:** [formeln_s200.md](formeln_s200.md), Abschnitt 3.
- **Buchfassung:**
  ```text
  Vorne (links) vÄLU - 0,5 bis - 1 cm als Kreisbogen zeichnen.
  ```
- **Technische Formel:** `bogen_vorne = vAlU - delta`, `delta ∈ [0,5; 1] cm`.
- **Eingaben und Einheiten:** `vAlU` (vordere Teilstrecke Ärmlochumfang, cm,
  laut Schritt 1 der Seite gemessen).
- **Ausgabe und Einheit:** `bogen_vorne` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich `[0,5; 1] cm`
  bleibt Bereich; keine Buchregel für die Auswahl.
- **Abhängigkeiten:** `vAlU` aus Messschritt 1 der Seite (siehe
  [formeln_s200.md](formeln_s200.md), „Nicht als Formel erfasst").
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Ob `vAlU`/`hAlU` (Labels ohne Umlaut) oder `vÄLU`/`hÄLU` (Fließtext mit
    Umlaut) die korrekte Schreibweise sind, ist laut `s200.md` noch offen
    (Prüfstelle 1).

## F4 – Hintere Linie (hÄLU-Reduzierung)

- **Quelle:** [formeln_s200.md](formeln_s200.md), Abschnitt 4.
- **Buchfassung:**
  ```text
  Die hintere Linie mit hÄLU - 0 bis - 1 cm auf den Bogen abtragen und
  zeichnen.
  ```
- **Technische Formel:** `linie_hinten = hAlU - delta`, `delta ∈ [0; 1] cm`.
- **Eingaben und Einheiten:** `hAlU` (hintere Teilstrecke Ärmlochumfang, cm).
- **Ausgabe und Einheit:** `linie_hinten` (cm), abgetragen auf den Bogen aus
  F3.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich `[0; 1] cm`
  (Reduzierung optional bis 1 cm) bleibt Bereich.
- **Abhängigkeiten:** F3 (Bogen) → F4; `hAlU` aus Messschritt 1 der Seite.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Gleiche Umlaut-Unsicherheit wie F3 (Prüfstelle 1 in `s200.md`).

## F5 – Ärmellänge und Ellenbogenlinie ab Schnittpunkt (SuP)

- **Quelle:** [formeln_s200.md](formeln_s200.md), Abschnitt 5.
- **Buchfassung:**
  ```text
  Vom Schnittpunkt (SuP) die ÄL und vom SuP 60% der ÄL abtragen.
  ```
- **Technische Formel:**
  ```text
  saumlinie_ab_SuP     = AL           (volle Ärmellänge)
  ellenbogenlinie_ab_SuP = 0,6 * AL
  ```
- **Eingaben und Einheiten:** `AL` (Ärmellänge, cm, aus Konstruktionstabelle).
- **Ausgabe und Einheit:** `saumlinie_ab_SuP`, `ellenbogenlinie_ab_SuP` (cm),
  jeweils ab Schnittpunkt SuP.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine — fester
  Prozentsatz `60%` laut Buchwortlaut.
- **Abhängigkeiten:** `AL` aus Konstruktionstabelle; Ergebnis ist Eingabe für
  Schritt 8 (rechtwinkliges Abwinkeln der Saum-, Ellenbogen- und Seitenlinien,
  nicht als eigene Formel erfasst).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Ob „die ÄL" in Schritt 6 die Saumlinie meint (Annahme oben) oder eine
    andere Linie, ist aus dem Wortlaut nicht zweifelsfrei; die Deutung stammt
    aus dem Kontext (Schritt 8 nennt „Saum-, Ellenbogen- und Seitenlinien" als
    Ziel des Abwinkelns).

## F6 – Ärmelkopflinie (ÄkLI), Hilfslinien-Variante (Punkt A)

- **Quelle:** [formeln_s200.md](formeln_s200.md), Abschnitt 6.
- **Buchfassung:**
  ```text
  Die ÄkLI messen → = OaW + Zugabe
  ```
- **Technische Formel:** `AekLI = OaW + Zugabe` (Zugabe nicht beziffert).
- **Eingaben und Einheiten:** `OaW` (Oberarmweite, cm); `Zugabe` (cm, Wert
  hier nicht angegeben).
- **Ausgabe und Einheit:** `AekLI` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Zahlenwert für
  `Zugabe` in dieser Buchstelle; siehe F2 für die andernorts bezifferte
  Fassung (`1 bis 1,5 cm`).
- **Abhängigkeiten:** vermutlich dieselbe Größe wie F2, aber als eigene
  gedruckte Stelle unabhängig dokumentiert (Regel 5: Abweichungen
  nebeneinander stehen lassen).
- **Status:** offen (Widerspruch zu F2).
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Widerspruch/Ergänzung zu F2: `+ Zugabe` (unbeziffert) hier vs.
    `+ 1 bis 1,5 cm` dort — ob beide dieselbe Größe meinen, ist am Original zu
    klären.

## F7 – Hilfslinie B (ÄkLI : 8, vorne)

- **Quelle:** [formeln_s200.md](formeln_s200.md), Abschnitt 7.
- **Buchfassung:**
  ```text
  ÄkLI : 8 vom SuP nach vorne (links) abtragen.
  ```
- **Technische Formel:** `strecke_B = AekLI / 8`, ab `SuP` nach vorne.
- **Eingaben und Einheiten:** `AekLI` (cm, aus F2/F6).
- **Ausgabe und Einheit:** `strecke_B` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine, feste Division.
- **Abhängigkeiten:** F2/F6 → F7.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Welcher Punkt (kein Label im Rohtext genannt) durch `strecke_B` markiert
    wird, ist unklar — anders als bei D (P10) und E (P11) fehlt hier eine
    Punktbezeichnung.

## F8 – Hilfslinie C (ÄkLI : 5, hinten)

- **Quelle:** [formeln_s200.md](formeln_s200.md), Abschnitt 8.
- **Buchfassung:**
  ```text
  ÄkLI : 5 nach hinten (rechts) abtragen
  ```
- **Technische Formel:** `strecke_C = AekLI / 5`, nach hinten.
- **Eingaben und Einheiten:** `AekLI` (cm, aus F2/F6).
- **Ausgabe und Einheit:** `strecke_C` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine, feste Division.
- **Abhängigkeiten:** F2/F6 → F8.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Bezugspunkt für „nach hinten abtragen" (SuP wie bei B, oder ein anderer
    Punkt) im Wortlaut nicht wiederholt — aus dem Satzzusammenhang von B
    übernommen, nicht Buchtext-identisch belegt.
  - Kein Punktlabel genannt (wie bei F7).

## F9 – Hilfslinie D (ÄkLI : 12, vorne → P10)

- **Quelle:** [formeln_s200.md](formeln_s200.md), Abschnitt 9.
- **Buchfassung:**
  ```text
  Vorne auf der ÄkLI die ÄkLI : 12 markieren und zu P10 und
  ```
- **Technische Formel:** `strecke_D = AekLI / 12`, markiert vorne auf ÄkLI,
  Ergebnis-Punkt `P10`.
- **Eingaben und Einheiten:** `AekLI` (cm, aus F2/F6).
- **Ausgabe und Einheit:** `strecke_D` (cm); Punkt `P10`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine, feste Division.
- **Abhängigkeiten:** F2/F6 → F9. Satz geht weiter in F10 (Punkt E).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.

## F10 – Hilfslinie E (ÄkLI : 9, hinten → P11)

- **Quelle:** [formeln_s200.md](formeln_s200.md), Abschnitt 10.
- **Buchfassung:**
  ```text
  hinten ÄkLI : 9 abtragen und Hilfslinien zu P11 zeichnen.
  ```
- **Technische Formel:** `strecke_E = AekLI / 9`, abgetragen hinten, Ergebnis-
  Punkt `P11`.
- **Eingaben und Einheiten:** `AekLI` (cm, aus F2/F6).
- **Ausgabe und Einheit:** `strecke_E` (cm); Punkt `P11`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine, feste Division.
- **Abhängigkeiten:** F2/F6 → F10; [[F9]] (gleicher Satzblock, D und E
  gehören zusammen).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Folgeschritt F („Von P1 und P11 auf die unteren Linien abwinkeln.")
    nennt „P1" statt „P10" — möglicher OCR-Fehler, nicht Teil dieser Formel,
    siehe [formeln_s200.md](formeln_s200.md), „Nicht als Formel erfasst".
