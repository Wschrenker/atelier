# Formeln s202 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s202.md`](formeln_s202.md) vermerkt, ist nur
eine einzige Rechenstelle dieser Seite von Werner am Original bestätigt
(Formel 8, ÄkLi : 14). Alle übrigen Formeln stehen deshalb auf `offen`,
unabhängig von der inhaltlichen Klarheit der Buchfassung. Dies ist ein
Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung der übrigen
Stellen.

## Formel 1 – Oberarmweite aus Oberarmumfang

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 1
- **Buchfassung:**
  ```text
  OaU | Oberarmumfang | 28 + 9 = Oberarmweite OaW | 37
  ```
- **Technische Formel:**
  ```text
  OaW = OaU + Zugabe
  Beispiel: OaW = 28 + 9 = 37
  ```
- **Eingaben und Einheiten:** `OaU` (Oberarmumfang, cm), `Zugabe` (cm, aus der
  Berechnungstabelle Seite 199, hier nicht kopiert).
- **Ausgabe und Einheit:** `OaW` (Oberarmweite, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Zugabe stammt aus der
  auf Seite 199 verlinkten Berechnungstabelle; auf s202 nur als angewandtes
  Zahlenbeispiel (9 cm) sichtbar, keine allgemeine Regel dafür auf dieser
  Seite.
- **Abhängigkeiten:** Berechnungstabelle Seite 199 (verlinkt, nicht kopiert);
  [[Formel 4]] (OaW als Eingabe des Grundgerüsts), [[Formel 7]] (ÄkLi = OaW +
  Zugabe).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt.

## Formel 2 – Einhalteweite in cm aus Armlochumfang

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 1
- **Buchfassung:**
  ```text
  AbH | Ärmlochhöhe | --- ... Ärmlochumfang | ÄlU | 43,5
  EW in % | Einhalteweite in % | 3 % | Einhalteweite in cm = ÄlU · Einhalteweite in % | EW in cm | 1,3 cm
  ```
- **Technische Formel:**
  ```text
  EW_cm = ÄlU · EW_prozent
  Beispiel: EW_cm = 43,5 · 0,03 = 1,305 ≈ 1,3 cm
  ```
- **Eingaben und Einheiten:** `ÄlU` (Armlochumfang, cm) = 43,5 cm;
  `EW_prozent` (Einhalteweite in %) = 3 %.
- **Ausgabe und Einheit:** `EW_cm` (Einhalteweite in cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `EW_prozent` ist laut
  Schritt 2 (`formeln_s202.md`, „Nicht als Formel erfasst") vom Anwender
  gewählt („gewünschte Einhalteweite (EW) in %"), kein fester Buchwert –
  3 % ist hier nur das gedruckte Beispiel.
- **Abhängigkeiten:** [[Formel 3]] (Ärmelkugelumfang nutzt EW_cm als Eingabe).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Der gedruckte Rundungsschritt (1,305 → 1,3) ist nicht als eigene Regel
    ausgeschrieben, nur am Ergebnis erkennbar.

## Formel 3 – Ärmelkugelumfang

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Ärmelkugelumfang = ÄlU + Einhalteweite in cm | ÄKLI | 44,6
  ```
- **Technische Formel:**
  ```text
  ÄKU = ÄlU + EW_cm
  Beispiel A (gedruckter Tabellenwert, Rohtext): ÄKU = 44,6
  Beispiel B (nachgerechnet): 43,5 + 1,3 = 44,8
  ```
- **Eingaben und Einheiten:** `ÄlU` = 43,5 cm, `EW_cm` = 1,3 cm (aus
  Formel 2).
- **Ausgabe und Einheit:** `ÄKU` (Ärmelkugelumfang, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[Formel 2]] (EW_cm als Eingabe); Verhältnis zu
  „ÄkLi" (Formel 7/8) ungeklärt, siehe unten.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Das eigene Nachrechnen (43,5 + 1,3 = 44,8) ergibt einen anderen Wert als
    der gedruckte Rohtext „44,6"; `s202.md` vermutet als Sichtlesung „ÄKU
    44,8" statt „ÄKLI 44,6". Beide Fassungen bleiben nebeneinander stehen,
    keine wird hier als Buchformel-Beweis verwendet (Regel 4 des Prompts).
    Zusätzlich ist unklar, ob „ÄKLI/ÄKU" (Tabelle) und „ÄkLi"
    (Fließtext/Skizzen, Schritt 9) dieselbe Größe oder zwei verschiedene
    Größen bezeichnen – siehe Offene Frage bei Formel 7.

## Formel 4 – Grundgerüst-Basislinie (waagerecht)

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 2
- **Buchfassung:**
  ```text
  3 Die OaW + 0 bis 2 cm waagerecht abtragen.
  ```
- **Technische Formel:**
  ```text
  basislinie = OaW + zugabe
  zugabe ∈ [0 cm, 2 cm]
  ```
- **Eingaben und Einheiten:** `OaW` (cm, aus Formel 1).
- **Ausgabe und Einheit:** `basislinie` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „0 bis 2 cm"
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel 1]] (OaW als Eingabe).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt. Auswahlkriterium für den konkreten Wert innerhalb
  0–2 cm nicht auf dieser Seite angegeben.

## Formel 5 – Bogenradius vorne (vAlU)

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 2
- **Buchfassung:**
  ```text
  4 Vorne den vAIU - 0 cm bis - 1 cm als Kreisbogen zeichnen.
  ```
- **Technische Formel:**
  ```text
  radius_vorne = vAlU - zugabe
  zugabe ∈ [0 cm, 1 cm]
  ```
- **Eingaben und Einheiten:** `vAlU` (cm, laut Skizze 1 im Beispiel 19,6 cm,
  nicht auf dieser Seite bestätigt).
- **Ausgabe und Einheit:** `radius_vorne` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „0 bis 1 cm"
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** `vAlU` stammt aus Skizze 1 (□1 Ärmloch), auf s202 selbst
  gemessen (Schritt 1), nicht aus der Tabelle.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt.

## Formel 6 – Bogenradius hinten (hAlU)

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 2
- **Buchfassung:**
  ```text
  5 Die hintere Linie mit hAIU - 0 bis - 1 cm auf den Bogen abtragen und zeichnen.
  ```
- **Technische Formel:**
  ```text
  radius_hinten = hAlU - zugabe
  zugabe ∈ [0 cm, 1 cm]
  ```
- **Eingaben und Einheiten:** `hAlU` (cm, laut Skizze 1 im Beispiel 23,9 cm,
  nicht auf dieser Seite bestätigt).
- **Ausgabe und Einheit:** `radius_hinten` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „0 bis 1 cm"
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel 5]] (gleicher Konstruktionsschritt, gleiches
  Grundgerüst); `hAlU` aus Skizze 1.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt.

## Formel 7 – 60-%-Linie der Ärmellänge

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 2
- **Buchfassung:**
  ```text
  6 Vom Schnittpunkt (SuP) die ÄL
  7 und 60% der ÄL abtragen.
  ```
  ```text
  60 % ÄL = 60 cm · 0,60 = 36 cm
  ```
- **Technische Formel:**
  ```text
  strecke_60 = ÄL · 0,60
  Beispiel: 60 · 0,60 = 36
  ```
- **Eingaben und Einheiten:** `ÄL` (Ärmellänge, cm) = 60 cm (aus
  Konstruktionstabelle, Abschnitt 1).
- **Ausgabe und Einheit:** `strecke_60` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine, fester
  Prozentsatz laut Buchtext.
- **Abhängigkeiten:** `ÄL` aus Konstruktionstabelle (Abschnitt 1, `formeln_s202.md`).
- **Status:** normalisiert (Rechenbeispiel selbst stimmig nachgerechnet:
  60 · 0,60 = 36), **aber** die zugrundeliegende Seitenverifikation ist
  offen – siehe Offene Fragen.
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt; „normalisiert" bezieht sich hier ausschließlich auf
  die interne rechnerische Stimmigkeit des Beispiels, nicht auf eine
  Bestätigung am Original.

## Formel 8 – Ärmelkugellinie (ÄkLi) aus Oberarmweite

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 3
- **Buchfassung:**
  ```text
  9 ☐4 Die ÄkLi messen → = OaW + Zugabe
  ```
- **Technische Formel:**
  ```text
  ÄkLi = OaW + zugabe
  ```
- **Eingaben und Einheiten:** `OaW` (cm, aus Formel 1), `zugabe` (cm, Quelle
  auf s202 nicht benannt).
- **Ausgabe und Einheit:** `ÄkLi` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Bereichsangabe
  auf dieser Seite; „Zugabe" ohne Zahlenwert oder Quellenverweis.
- **Abhängigkeiten:** [[Formel 1]] (OaW als Eingabe); [[Formel 9]],
  [[Formel 10]], [[Formel 11]] und [[Formel 12]] (ÄkLi als Eingabe der
  Teilungen).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unklar, ob „ÄkLi" (diese Formel) und „ÄKLI"/„ÄKU"
    (Ärmelkugelumfang, Formel 3) dieselbe Größe sind. Die Divisionsergebnisse
    in Formel 9–12 passen rechnerisch zu ÄkLi = 37 cm (= OaW, Zugabe hier 0),
    nicht zu ÄKLI/ÄKU = 44,6/44,8 cm. Diese Beobachtung stützt eine
    Unterscheidung der beiden Größen, ist aber keine Bestätigung.

## Formel 9 – ÄkLi-Teilung : 8 (vordere Hilfslinie)

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 3
- **Buchfassung:**
  ```text
  10 und ÄkLi : 8 vom SuP nach vorne (links) abtragen.
  ```
  ```text
  ÄkLi : 8 = 4,6 cm
  ```
- **Technische Formel:**
  ```text
  strecke_vorne_8 = ÄkLi / 8
  Beispiel (Bildbeleg, nicht bestätigt): 37 / 8 = 4,625 ≈ 4,6
  ```
- **Eingaben und Einheiten:** `ÄkLi` (cm, aus Formel 8).
- **Ausgabe und Einheit:** `strecke_vorne_8` (cm), vom SuP nach vorne.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[Formel 8]] (ÄkLi als Eingabe).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt; der Wert 4,6 cm ist nicht einzeln geprüft (nur
  rechnerisch mit ÄkLi = 37 cm konsistent, siehe Formel 8).

## Formel 10 – ÄkLi-Teilung : 5 (hintere Hilfslinie)

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 3
- **Buchfassung:**
  ```text
  11 ÄkLi : 5 nach hinten (rechts) abtragen.
  ```
  ```text
  ÄkLi : 5 = 7,4 cm
  ```
- **Technische Formel:**
  ```text
  strecke_hinten_5 = ÄkLi / 5
  Beispiel (Bildbeleg, nicht bestätigt): 37 / 5 = 7,4
  ```
- **Eingaben und Einheiten:** `ÄkLi` (cm, aus Formel 8).
- **Ausgabe und Einheit:** `strecke_hinten_5` (cm), nach hinten.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[Formel 8]] (ÄkLi als Eingabe).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kein Punkt dieser Seite ist von Werner
  am Original bestätigt.

## Formel 11 – ÄkLi-Teilung : 12 (vordere Markierung P10)

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 3
- **Buchfassung:**
  ```text
  12 Vorne auf der ÄkLi die ÄkLi : 12 markieren und zu P10
  ```
  ```text
  ÄkLi : 12 = 3,1 cm
  ```
- **Technische Formel:**
  ```text
  strecke_vorne_12 = ÄkLi / 12
  Beispiel (Bildbeleg, nicht bestätigt): 37 / 12 = 3,083… ≈ 3,1
  ```
- **Eingaben und Einheiten:** `ÄkLi` (cm, aus Formel 8).
- **Ausgabe und Einheit:** `strecke_vorne_12` (cm), Markierung zu Punkt 10.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[Formel 8]] (ÄkLi als Eingabe); [[Formel 9]] (P10 laut
  Schritt 10 bereits über die :8-Teilung gesetzt – Verhältnis der beiden
  Punkte auf dieser Seite nicht eindeutig geklärt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Schritt 10 und Schritt 12 beziehen sich beide auf „P10"; ob es sich um
    denselben Punkt oder zwei verschiedene Bezugspunkte handelt, ist aus dem
    Wortlaut nicht eindeutig.

## Formel 12 – ÄkLi-Teilung : 14 (hintere Markierung, bereits bestätigt)

- **Quelle:** [`formeln_s202.md`](formeln_s202.md), Abschnitt 3
- **Buchfassung:**
  ```text
  13 hinten ÄkLi : 14 abtragen und Hilfslinien zu P11 zeichnen.
  ```
  ```text
  ÄkLi : 14 = 2,4 cm
  ```
- **Technische Formel:**
  ```text
  strecke_hinten_14 = ÄkLi / 14
  Buchfassung (Bildbeleg): 37 / 14 = 2,4 (gedruckt)
  Bestätigte Arbeitslesung: 37 / 14 = 2,642857… ≈ 2,6
  ```
- **Eingaben und Einheiten:** `ÄkLi` = 37 cm (aus Formel 8, hier als
  Bildbeleg der bestätigten Stelle verwendet).
- **Ausgabe und Einheit:** `strecke_hinten_14` (cm), Markierung zu Punkt 11.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** [[Formel 8]] (ÄkLi als Eingabe).
- **Status:** normalisiert – **nur für die Division selbst**, bestätigt am
  2026-09-24 laut `s202.md`.
- **Offene Fragen oder Widersprüche:**
  - Der gedruckte Buchwert `2,4 cm` ist als Rechenfehler erkannt; die
    bestätigte Arbeitslesung ist `≈ 2,6 cm`. Die gedruckte Fassung bleibt
    unverändert als Bildbeleg stehen (Regel 4 des Prompts – kein stilles
    Berichtigen).
  - Diese Bestätigung deckt ausschließlich die Division `37 : 14`. Der
    Eingabewert `ÄkLi = 37` selbst (Formel 8) ist auf dieser Seite nicht
    eigenständig bestätigt.

## Nicht normalisiert (siehe `formeln_s202.md`, „Nicht als Formel erfasst")

- Schritt 1 (Messanweisungen vAlU/hAlU/vAchsel/hAchsel): keine
  Rechenbeziehung.
- Skizze 1 (□1 Ärmloch) Einzelmaße: isolierte Messwerte ohne Rechenbeziehung
  auf dieser Seite.
- Schritt 15 (Ärmelkugel formen): freihändige Kurvenführung ohne Formel.
- Saumweite-Zeile der Tabelle (ÄSaW): Wortlaut selbst unklar/lückenhaft,
  siehe Hinweis in `formeln_s202.md`, Abschnitt 1; hier nicht als eigene
  Formel geführt, bis der Wortlaut bestätigt ist.
