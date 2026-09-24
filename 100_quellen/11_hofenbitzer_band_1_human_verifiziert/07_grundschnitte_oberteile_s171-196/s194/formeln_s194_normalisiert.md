# Formeln s194 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s194.md`](formeln_s194.md) vermerkt, ist die
Seite insgesamt nicht menschlich verifiziert. Anders als bei anderen
Walking-Skeleton-Durchläufen sind hier sechs konkrete Zahlenwerte
(Konstruktionstabelle ☐1) von Werner am Original bestätigt; diese erhalten
unten den Status `normalisiert`, soweit die Rechenbeziehung eindeutig ist.
Alle übrigen Formeln – Zugabentabelle ☐2, Zugabe-Boxen, Zeichnungswerte ☐3 und
die Rechenanweisungen im Fließtext – bleiben unbestätigt und stehen auf
`offen`. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die noch
ausstehende Bestätigung.

## Formel 1 – AlT + Zugabe (bestätigt)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 1
- **Buchfassung:**
  ```text
  AlT 20,1 + 1,3 = 21,4
  ```
- **Technische Formel:**
  ```text
  AlT_plus = AlT + zugabe_AlT
  ```
- **Eingaben und Einheiten:** `AlT` = 20,1 cm (Nennmaß, Konstruktionstabelle
  ☐1); `zugabe_AlT` = 1,3 cm.
- **Ausgabe und Einheit:** `AlT_plus` = 21,4 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert laut Buch,
  kein Bereich.
- **Abhängigkeiten:** Teil der Konstruktionstabelle ☐1, Passformklasse PK 3;
  vgl. den (unbestätigten) Zeichnungswert „Zugabe zur AlT" in [[Formel 12]].
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** Bedeutung der Abkürzung „AlT" und ihr
  weiterer Verwendungszusammenhang sind auf dieser Seite nicht spezifiziert;
  nur der Zahlenwert ist bestätigt.

## Formel 2 – BrB + Zugabe (bestätigt)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 1
- **Buchfassung:**
  ```text
  BrB 18,2 + 1,0 = 19,2
  ```
- **Technische Formel:**
  ```text
  BrB_plus = BrB + zugabe_BrB
  ```
- **Eingaben und Einheiten:** `BrB` = 18,2 cm; `zugabe_BrB` = 1,0 cm.
- **Ausgabe und Einheit:** `BrB_plus` = 19,2 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert laut Buch,
  kein Bereich.
- **Abhängigkeiten:** Teil der Konstruktionstabelle ☐1, Passformklasse PK 3;
  vgl. den (unbestätigten) Wert „Zugabe zur BrB" (PK 3 = 1,0 cm) in
  [[Formel 8]] – dort stimmt der PK-3-Wert mit diesem überein.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** keine.

## Formel 3 – SuB + Zugabe = SuNL (bestätigt)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 1
- **Buchfassung:**
  ```text
  SuB 12,2 + 0,3 = SuNL 12,5
  ```
- **Technische Formel:**
  ```text
  SuNL = SuB + zugabe_SuB
  ```
- **Eingaben und Einheiten:** `SuB` = 12,2 cm; `zugabe_SuB` = 0,3 cm.
- **Ausgabe und Einheit:** `SuNL` = 12,5 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert laut Buch,
  kein Bereich.
- **Abhängigkeiten:** Eingangsgröße für [[Formel 5]] (`hSuNL`).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** keine.

## Formel 4 – Kontrollrechnung (bestätigt, Variablenbezug ungeklärt)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Kontrolle: 44 + 3 = 47
  ```
- **Technische Formel:**
  ```text
  wert_plus = wert + zugabe
  44 + 3 = 47
  ```
- **Eingaben und Einheiten:** unbenannter Ausgangswert 44 (cm, vermutlich
  Brustumfang-bezogen, siehe Offene Fragen); Zugabe 3 (cm).
- **Ausgabe und Einheit:** 47 (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert laut Buch,
  kein Bereich.
- **Abhängigkeiten:** keine bekannten.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Werner hat nur die Zahlenwerte
  44/3/47 bestätigt, nicht die zugehörige Zeilenbezeichnung. Die
  OCR-Rohzeile in `tabellen_s194.md` (`tbl-0.md`) liefert dafür nur den
  unlesbaren Zeilenkopf „Bremside 2 � � BrH … � BrW"; welche Maßgröße hier
  konkret berechnet wird, ist ungeklärt.

## Formel 5 – hSuNL = SuNL + Einhalteweite (bestätigt)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 1
- **Buchfassung:**
  ```text
  hSuNL = SuNL + Einhalteweite
  12,5 + 0,7 = 13,2
  ```
- **Technische Formel:**
  ```text
  hSuNL = SuNL + einhalteweite
  ```
- **Eingaben und Einheiten:** `SuNL` = 12,5 cm (aus [[Formel 3]]);
  `einhalteweite` = 0,7 cm.
- **Ausgabe und Einheit:** `hSuNL` = 13,2 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert laut Buch,
  kein Bereich.
- **Abhängigkeiten:** [[Formel 3]] (`SuNL`).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** Die Rohzeile fehlt vollständig im
  OCR-Text (Modell-Halluzination an dieser Stelle, siehe `tabellen_s194.md`);
  die Formelbeziehung stammt ausschließlich aus Werners Bestätigung am
  Original, nicht aus einer geprüften Buchzeile mit Wortlaut.

## Formel 6 – PK 9: SuB-Zugabe (bestätigter Einzelwert)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 1 und Abschnitt 2
- **Buchfassung:**
  ```text
  PK 9: SuB-Zugabe 0,9
  ```
- **Technische Formel:**
  ```text
  zugabe_SuB(PK9) = 0,9 cm
  ```
- **Eingaben und Einheiten:** Passformklasse PK 9.
- **Ausgabe und Einheit:** `zugabe_SuB(PK9)` = 0,9 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert laut Buch,
  kein Bereich.
- **Abhängigkeiten:** letzter Wert derselben Zugabentabellen-Zeile wie
  [[Formel 7]] (Zugabentabelle ☐2); nur dieser eine Wert ist bestätigt, die
  übrigen Werte der Zeile in [[Formel 7]] nicht.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** ersetzt den OCR-Rohwert `0,3` aus
  `tbl-1.md`.

## Formel 7 – Zugabentabelle ☐2, Zeile PK 9 (unbestätigt)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Passformklasse 9: BrU 18, TaU 12 - 20, HüU 10 - 20, AlT 4, RüB 2, ArD 5, BrB 2
  ```
- **Technische Formel:**
  ```text
  zugabe_BrU(PK9)  = 18       cm
  zugabe_TaU(PK9) ∈ [12, 20]  cm
  zugabe_HueU(PK9) ∈ [10, 20] cm
  zugabe_AlT(PK9)  = 4        cm
  zugabe_RueB(PK9) = 2        cm
  zugabe_ArD(PK9)  = 5        cm
  zugabe_BrB(PK9)  = 2        cm
  ```
- **Eingaben und Einheiten:** Passformklasse PK 9.
- **Ausgabe und Einheit:** sieben Zugabewerte/-bereiche (cm), je Maßgröße.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `TaU` und `HüU` sind im
  Buch als Bereich angegeben; als Bereich erhalten, kein Default gewählt. Die
  übrigen fünf Werte stehen als Einzelwerte.
- **Abhängigkeiten:** [[Formel 6]] (letzter, bestätigter Wert derselben
  Tabellenzeile); Spaltenzuordnung übernimmt Prüfstelle 3 aus `s194.md`.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kopfzeilen der Rohtabelle sind
  erkennbar verschoben/verwechselt; die Zuordnung der Werte zu
  BrU/TaU/HüU/AlT/RüB/ArD/BrB ist nicht am Original bestätigt.

## Formel 8 – Zugabe zur BrB (☐3, unbestätigt)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Zugabe zur BrB: PK 3 = 1,0 cm, PK 9 = 2,0 cm, Differenz = 1,0 cm
  ```
- **Technische Formel:**
  ```text
  differenz_BrB = zugabe_BrB(PK9) - zugabe_BrB(PK3)
  2,0 - 1,0 = 1,0
  ```
- **Eingaben und Einheiten:** `zugabe_BrB(PK3)` = 1,0 cm;
  `zugabe_BrB(PK9)` = 2,0 cm.
- **Ausgabe und Einheit:** `differenz_BrB` = 1,0 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** feste Werte laut Buch.
- **Abhängigkeiten:** `zugabe_BrB(PK3)` deckt sich zahlenmäßig mit der
  bestätigten [[Formel 2]] (1,0 cm); dies ist ein Rechen-Cross-Check, kein
  Beleg für diese unbestätigte Box.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** noch nicht am Original bestätigt
  (Prüfstelle 4, `s194.md`).

## Formel 9 – Zugabe zum ArD (☐3, unbestätigt)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Zugabe zum ArD: PK 3 = 1,5 cm, PK 9 = 5,0 cm, Differenz = 3,5 cm
  ```
- **Technische Formel:**
  ```text
  differenz_ArD = zugabe_ArD(PK9) - zugabe_ArD(PK3)
  5,0 - 1,5 = 3,5
  ```
- **Eingaben und Einheiten:** `zugabe_ArD(PK3)` = 1,5 cm;
  `zugabe_ArD(PK9)` = 5,0 cm.
- **Ausgabe und Einheit:** `differenz_ArD` = 3,5 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** feste Werte laut Buch.
- **Abhängigkeiten:** `differenz_ArD` wird laut Fließtext in [[Formel 17]] und
  [[Formel 18]] im Verhältnis ⅓/⅔ auf VT und RT verteilt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** noch nicht am Original bestätigt
  (Prüfstelle 4, `s194.md`).

## Formel 10 – Zugabe zur RüB (☐3, unbestätigt)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Zugabe zur RüB: PK 3 = 0,5 cm, PK 9 = 2,0 cm, Differenz = 1,5 cm
  ```
- **Technische Formel:**
  ```text
  differenz_RueB = zugabe_RueB(PK9) - zugabe_RueB(PK3)
  2,0 - 0,5 = 1,5
  ```
- **Eingaben und Einheiten:** `zugabe_RueB(PK3)` = 0,5 cm;
  `zugabe_RueB(PK9)` = 2,0 cm.
- **Ausgabe und Einheit:** `differenz_RueB` = 1,5 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** feste Werte laut Buch.
- **Abhängigkeiten:** `differenz_RueB` wird laut Fließtext in [[Formel 15]]
  („restlicher Differenzbetrag") verwendet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** noch nicht am Original bestätigt
  (Prüfstelle 4, `s194.md`).

## Formel 11 – Zeichnungswerte ☐3: Einschnitt-Öffnungsweiten (unbestätigt)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 4
- **Buchfassung:**
  ```text
  ① ½ = 0,5 cm
  ② ½ = 0,5 cm
  ⅓ = 1,2 cm
  ③ Rest 1 cm
  ① wie am VT 0,5 cm
  ⅔ = 2,3 cm
  ```
- **Technische Formel:**
  ```text
  oeffnung_1 = 0,5 cm   (½)
  oeffnung_2 = 0,5 cm   (½)
  oeffnung_3 = 1,2 cm   (⅓)
  oeffnung_4 = 1,0 cm   (Rest)
  oeffnung_5 = 0,5 cm   (wie VT)
  oeffnung_6 = 2,3 cm   (⅔)
  ```
- **Eingaben und Einheiten:** aus dem Bildausschnitt gelesene
  Bruchbezeichnungen (½, ⅓, ⅔, „Rest") mit zugehörigen cm-Werten.
- **Ausgabe und Einheit:** sechs Öffnungs-/Ausstellweiten (cm) an den
  markierten Schnitteinschnitten von VT und RT.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Bereiche, feste
  Zeichnungswerte.
- **Abhängigkeiten:** Zuordnung zu den Kreisnummern ①–⑦ der Zeichnung, die
  laut `skizzen_s194.json` den Punktnummern im Fließtext „1 OT-GS erweitern"
  entsprechen sollen (vgl. [[Formel 13]]–[[Formel 18]]); genaue Zuordnung
  Kreis-zu-Punktnummer nicht durch eigene Bildprüfung bestätigt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** vorläufige KI-Ablesung aus dem
  Bildausschnitt (`bestaetigt: false` in `skizzen_s194.json`), noch nicht am
  Original bestätigt (Prüfstelle 5, `s194.md`).

## Formel 12 – Zeichnung ☐3: Zugabe zur AlT (unbestätigt)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Zugabe zur AlT: PK 3 = 1,3 cm, PK 9 = 4,0 cm, Differenz = 2,7 cm
  ```
- **Technische Formel:**
  ```text
  differenz_AlT = zugabe_AlT(PK9) - zugabe_AlT(PK3)
  4,0 - 1,3 = 2,7
  ```
- **Eingaben und Einheiten:** `zugabe_AlT(PK3)` = 1,3 cm;
  `zugabe_AlT(PK9)` = 4,0 cm.
- **Ausgabe und Einheit:** `differenz_AlT` = 2,7 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** feste Werte laut Buch.
- **Abhängigkeiten:** Der PK-3-Wert (1,3 cm) stimmt zahlenmäßig mit
  `zugabe_AlT` aus der bestätigten [[Formel 1]] überein; dies ist ein
  Rechen-Cross-Check, kein Beleg für diese unbestätigte Zeichnungsbox.
  `differenz_AlT` wird laut Fließtext in [[Formel 16]] verwendet
  („Armloch um die AlT-Differenz vertiefen").
- **Status:** offen
- **Offene Fragen oder Widersprüche:** noch nicht am Original bestätigt
  (Prüfstelle 5, `s194.md`).

## Formel 13 – Einschneideabstand und Öffnungsanweisung an vM/hM (Punkt 1)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 5
- **Buchfassung:**
  ```text
  1 An VT und RT ca. 3 cm neben der vM bzw. hM in (oder direkt neben den) den
  Halslöchern zum Saum einschneiden und jeweils die Hälfte der errechneten
  Mehrweiten-Differenz zur BrB exakt waagerecht öffnen.
  ```
- **Technische Formel:**
  ```text
  einschnitt_abstand ≈ 3 cm  (ca., ab vM bzw. hM)
  oeffnung_je_teil = differenz_BrB / 2
  ```
- **Eingaben und Einheiten:** `differenz_BrB` (cm), vgl. [[Formel 8]].
- **Ausgabe und Einheit:** `oeffnung_je_teil` (cm), waagerechte
  Öffnungsweite je VT/RT-Einschnitt.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` vor dem
  Einschneideabstand erhalten; kein fester Wert.
- **Abhängigkeiten:** [[Formel 8]] (`differenz_BrB`).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** noch nicht am Original bestätigt;
  Wortlaut „Seitennahlt" an anderer Stelle der Seite auffällig, hier nicht
  betroffen.

## Formel 14 – Öffnung am seitlichen VT-Einschnitt (Punkt 3)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 5
- **Buchfassung:**
  ```text
  3 Am seitlichen VT-Einschnitt wie am VT-Halsloch öffnen (hier 0,5 cm).
  ```
- **Technische Formel:**
  ```text
  oeffnung_VT_seitlich = oeffnung_je_teil  (hier: 0,5 cm)
  ```
- **Eingaben und Einheiten:** `oeffnung_je_teil` aus [[Formel 13]]; im
  Buchbeispiel 0,5 cm.
- **Ausgabe und Einheit:** `oeffnung_VT_seitlich` = 0,5 cm (Beispielwert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein eigener Bereich;
  Wert folgt aus [[Formel 13]].
- **Abhängigkeiten:** [[Formel 13]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:** noch nicht am Original bestätigt.

## Formel 15 – Öffnung am seitlichen RT-Einschnitt (Punkt 4)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 5
- **Buchfassung:**
  ```text
  4 Am seitlichen RT-Einschnitt den restlichen Differenzbetrag zur
  RüB-Differenz öffnen (hier 1 cm).
  ```
- **Technische Formel:**
  ```text
  oeffnung_RT_seitlich = differenz_RueB - oeffnung_VT_seitlich  (hier: 1 cm)
  ```
- **Eingaben und Einheiten:** `differenz_RueB` (cm), vgl. [[Formel 10]];
  `oeffnung_VT_seitlich` aus [[Formel 14]].
- **Ausgabe und Einheit:** `oeffnung_RT_seitlich` = 1 cm (Beispielwert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein eigener Bereich.
- **Abhängigkeiten:** [[Formel 10]], [[Formel 14]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Rechenprobe mit den Beispielwerten
  (1,5 cm − 0,5 cm = 1,0 cm) passt zu `differenz_RueB` aus [[Formel 10]];
  dies bestätigt aber nur die interne Konsistenz des Buchbeispiels, nicht
  dessen Originaltreue.

## Formel 16 – Armloch-Vertiefung um AlT-Differenz (Punkt 5)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 5
- **Buchfassung:**
  ```text
  5 Das Armloch um die AlT-Differenz vertiefen und die neue Brustlinie
  zeichnen.
  ```
- **Technische Formel:**
  ```text
  armloch_tiefe_neu = armloch_tiefe_alt + differenz_AlT
  ```
- **Eingaben und Einheiten:** `armloch_tiefe_alt` (cm, nicht auf dieser Seite
  beziffert); `differenz_AlT` (cm), vgl. [[Formel 12]].
- **Ausgabe und Einheit:** `armloch_tiefe_neu` (cm); zusätzlich „neue
  Brustlinie" (geometrische Anweisung ohne eigenen Zahlenwert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Bereich.
- **Abhängigkeiten:** [[Formel 12]] (`differenz_AlT`).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** noch nicht am Original bestätigt.

## Formel 17 – Ausstellung Seitennaht VT: ein Drittel der ArD-Differenz (Punkt 6)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 5
- **Buchfassung:**
  ```text
  6 Ein Drittel der ArD-Differenz an der Seitennahlt vom VT ausstellen.
  ```
- **Technische Formel:**
  ```text
  ausstellung_VT_seitennaht = differenz_ArD * 1/3
  ```
- **Eingaben und Einheiten:** `differenz_ArD` (cm), vgl. [[Formel 9]].
- **Ausgabe und Einheit:** `ausstellung_VT_seitennaht` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Bereich, fester
  Bruchteil ⅓.
- **Abhängigkeiten:** [[Formel 9]]; ergänzt durch [[Formel 18]] (⅔ am RT).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** OCR-Schreibweise „Seitennahlt"
  (vermutlich „Seitennaht") unverändert übernommen, siehe Prüfstelle 1 in
  `s194.md`; noch nicht am Original bestätigt.

## Formel 18 – Ausstellung Seitennaht RT: zwei Drittel der ArD-Differenz (Punkt 7)

- **Quelle:** [`formeln_s194.md`](formeln_s194.md), Abschnitt 5
- **Buchfassung:**
  ```text
  7 Zwei Drittel an der Seitennahlt vom RT ausstellen.
  ```
- **Technische Formel:**
  ```text
  ausstellung_RT_seitennaht = differenz_ArD * 2/3
  ```
- **Eingaben und Einheiten:** `differenz_ArD` (cm), vgl. [[Formel 9]]; Bezug
  „Zwei Drittel" nur implizit auf die ArD-Differenz aus Punkt 6 rückbezogen,
  nicht in diesem Satz selbst wiederholt.
- **Ausgabe und Einheit:** `ausstellung_RT_seitennaht` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Bereich, fester
  Bruchteil ⅔; zusammen mit [[Formel 17]] ergibt sich `1/3 + 2/3 = 1` der
  `differenz_ArD`.
- **Abhängigkeiten:** [[Formel 9]], [[Formel 17]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Der Bezug „Zwei Drittel" wovon ist im
  Satz selbst elliptisch (nur aus Punkt 6 erschließbar); noch nicht am
  Original bestätigt.
