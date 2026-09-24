# Formeln – s047 (normalisiert, technische Fassung)

Diese Fassung trennt die Buchformeln von `formeln_s047.md` (fototreu) von
einer technischen Lesart. **Von den sieben erfassten Stellen ist bisher nur
ein Zahlenausdruck** – `HüU : 8 − 1,5 bis −2 cm` an der vM (siehe `s047.md`,
Abschnitt „Vorab geklärte formel- und coderelevante Stellen") – **am Original
bestätigt.** Alle übrigen Stellen stehen auf `offen`, bis Werner sie am
Original geprüft hat.

## Formel 1 – Sitzhöhe an vM und hM (Textschritt)

**Quelle:** [formeln_s047.md](formeln_s047.md), Abschnitt 1
(→ [ocr_s047.md](ocr_s047.md), Zeile 11).

**Buchfassung:**

```text
☐4 + 5 Sitzhöhe 0 bis +2 cm an vM und hM nach unten abtragen und nach außen abwinkeln.
```

**Technische Formel:**

```text
sitzhoehe_versatz(vM, hM) = 0 bis +2 cm   (nach unten abtragen, dann nach außen abwinkeln)
```

**Eingaben und Einheiten:** keine Eingabegröße; `0 bis +2 cm` ist der
gedruckte Bereich selbst.

**Ausgabe und Einheit:** `sitzhoehe_versatz` – Streckenmaß an vM und hM, cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich `0` bis `+2 cm`,
keine Buchregel im Textschritt selbst zur Auswahl eines konkreten Werts.
Siehe aber Formel 6 und 7: dort sind für die beiden Hosenrock-Varianten je
eigene, engere Bereiche (`+0 bis 1 cm` bzw. `+1 bis 2 cm`) beschriftet.

**Abhängigkeiten:** Gleiche Konstruktionsstelle wie Formel 6 und 7
(Sitzhöhe je Variante); siehe „Beobachtete Übereinstimmung" in
`formeln_s047.md`.

**Status:** offen

**Offene Fragen:** Ob der Textbereich `0 bis +2 cm` die beiden
Variantenbereiche aus Formel 6/7 bewusst zusammenfasst oder eine eigene,
unabhängige Buchregel ist, hat Werner am Original zu klären.

## Formel 2 – HüU-Formel an der vM (Textschritt)

**Quelle:** [formeln_s047.md](formeln_s047.md), Abschnitt 2
(→ [ocr_s047.md](ocr_s047.md), Zeile 12).

**Buchfassung:**

```text
An der vM wird HüU : 8 − 1,5 bis −2 cm nach außen und nach oben abgetragen.
```

**Technische Formel:**

```text
versatz_vM = HueU / 8 − (1,5 bis 2) cm   (nach außen und nach oben abgetragen)
```

**Eingaben und Einheiten:** `HueU` – Hüftumfang, cm.

**Ausgabe und Einheit:** `versatz_vM` – Streckenmaß an der vM, cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich `1,5` bis `2 cm`
Abzug von `HueU / 8`, keine Buchregel im Textschritt zur Auswahl eines
konkreten Werts innerhalb des Bereichs. Siehe Formel 6/7 für die je
Variante festen Einzelwerte (`−2 cm` bzw. `−1,5 cm`).

**Abhängigkeiten:** Gleiche Konstruktionsstelle wie Formel 6 (vM, ☐4) und
Formel 7 (vM, ☐5).

**Status je Teil:**

- Zahlenausdruck `HüU : 8 − 1,5 bis −2 cm` — bestätigt (s047.md).
- Satzrahmen „nach außen und nach oben abgetragen" — nicht gesondert
  bestätigt.

**Status (gesamt):** offen

**Offene Fragen:** Ob `1,5 bis 2 cm` als freier fachlicher Auswahlbereich
gilt oder ausschließlich über die Hosenrock-Variante (☐4/☐5) bestimmt wird,
ist ungeklärt.

## Formel 3 – HüU-Formel an der hM (Textschritt)

**Quelle:** [formeln_s047.md](formeln_s047.md), Abschnitt 3
(→ [ocr_s047.md](ocr_s047.md), Zeile 14).

**Buchfassung:**

```text
An der hM wird HüU : 8 + 2 bis + 3 cm nach außen und nach oben abgetragen.
```

**Technische Formel:**

```text
versatz_hM = HueU / 8 + (2 bis 3) cm   (nach außen und nach oben abgetragen)
```

**Eingaben und Einheiten:** `HueU` – Hüftumfang, cm.

**Ausgabe und Einheit:** `versatz_hM` – Streckenmaß an der hM, cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich `2` bis `3 cm`
Zuschlag auf `HueU / 8`, keine Buchregel im Textschritt zur Auswahl eines
konkreten Werts. Siehe Formel 6/7 für die je Variante festen Einzelwerte
(`+2 cm` bzw. `+3 cm`).

**Abhängigkeiten:** Gleiche Konstruktionsstelle wie Formel 6 (hM, ☐4) und
Formel 7 (hM, ☐5).

**Status:** offen

**Offene Fragen:** Wie Formel 2 – Verhältnis von Textbereich zu den festen
Variantenwerten ungeklärt; kein Teil dieser Formel ist bestätigt.

## Formel 4 – Gesäßnaht-Hilfslinien (geometrisch)

**Quelle:** [formeln_s047.md](formeln_s047.md), Abschnitt 4
(→ [ocr_s047.md](ocr_s047.md), Zeile 16;
`skizzen/s047_skizze_01.png`–`s047_skizze_04.png`).

**Buchfassung:**

```text
Für die Gesäßnaht jeweils die zwei Hilfslinien entsprechend der Skizze zeichnen und die Gesäßnaht formen.

VT (Punkt 2 → Punkt 4), beide Varianten: Teilung in drei gleiche Abschnitte 1/2, 1/2, 1/2
RT (Punkt 3 → Punkt 4), beide Varianten: Teilung in zwei ungleiche Abschnitte 1/2, 1/2 + 0,5
```

**Technische Formel:** Keine Rechenbeziehung mit Zahlwert, sondern eine
Konstruktionsvorschrift über Hilfslinien und eine daraus geformte Kurve:

```text
gesaessnaht_kurve = kurve_durch(hilfslinien(punkt_2_oder_3, punkt_4, teilverhaeltnis))
```

**Eingaben und Einheiten:** Teilverhältnis-Bezeichnungen `1/2` (VT, dreimal)
bzw. `1/2` und `1/2 + 0,5` (RT), ohne erkennbare Bezugsgröße im Buchtext.

**Ausgabe und Einheit:** Kurvenverlauf der Gesäßnaht, keine Zahlengröße.

**Bereiche, Bedingungen und Auswahlentscheidungen:** VT und RT unterscheiden
sich in Anzahl und Größe der Teilabschnitte; keine Buchregel, wovon dieser
Unterschied fachlich abhängt.

**Abhängigkeiten:** Baut auf Punkt 2/3 (Formel 2/3 bzw. 6/7) und Punkt 4 auf.

**Status:** offen

**Offene Fragen:** Bezugsgröße von „1/2" ungeklärt (Hälfte wovon); Grund für
die unterschiedliche Teilung an VT und RT nicht im Buchtext erkennbar.

## Formel 5 – Saum und Innenbeinnaht gewinkelt

**Quelle:** [formeln_s047.md](formeln_s047.md), Abschnitt 5
(→ [ocr_s047.md](ocr_s047.md), Zeile 17).

**Buchfassung:**

```text
Saum und Innenbeinnaht jeweils gewinkelt zeichnen.
```

**Technische Formel:** Keine Rechenbeziehung, reine Richtungsanweisung ohne
Winkel- oder Zahlenwert:

```text
saum_innenbeinnaht = gewinkelt_an(punkt_5)
```

**Eingaben und Einheiten:** keine.

**Ausgabe und Einheit:** keine Zahlengröße; Kurven-/Linienform am Punkt 5.

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext.

**Abhängigkeiten:** Endpunkt der in Formel 1/6/7 bestimmten Streckenführung.

**Status:** offen

**Offene Fragen:** Kein Winkelwert im Buchtext; „gewinkelt" bleibt
qualitativ.

## Formel 6 – Zeichnungswerte Gerader Hosenrock (☐4)

**Quelle:** [formeln_s047.md](formeln_s047.md), Abschnitt 6
(→ [skizzen_s047.json](skizzen_s047.json), Skizze 01/02).

**Buchfassung:**

```text
Gerader Hosenrock:
vM (Punkt 2): HüU : 8 − 2 cm
hM (Punkt 3): HüU : 8 + 2 cm
Sitzhöhe an vM und hM: + 0 bis 1 cm
```

**Technische Formel:**

```text
versatz_vM(gerade) = HueU / 8 − 2 cm
versatz_hM(gerade) = HueU / 8 + 2 cm
sitzhoehe_versatz(gerade) = 0 bis 1 cm
```

**Eingaben und Einheiten:** `HueU` – Hüftumfang, cm.

**Ausgabe und Einheit:** `versatz_vM`, `versatz_hM`, `sitzhoehe_versatz` –
Streckenmaße, cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** `versatz_vM` und
`versatz_hM` sind feste Werte (kein Bereich); `sitzhoehe_versatz` bleibt ein
Bereich `0` bis `1 cm` ohne Auswahlregel.

**Abhängigkeiten:** Eine der beiden Hosenrock-Varianten der Seite; betrifft
dieselbe Konstruktionsstelle wie Formel 1/2/3 (Textbereiche) und Formel 7
(andere Variante).

**Status:** offen

**Offene Fragen:** Werte stammen aus der Skizzenbeschreibung, nicht aus dem
OCR-Text, und sind am Original noch nicht bestätigt.

## Formel 7 – Zeichnungswerte Saumerweiterter Hosenrock (☐5)

**Quelle:** [formeln_s047.md](formeln_s047.md), Abschnitt 7
(→ [skizzen_s047.json](skizzen_s047.json), Skizze 03/04).

**Buchfassung:**

```text
Saumerweiterter Hosenrock:
vM (Punkt 2): HüU : 8 − 1,5 cm
hM (Punkt 3): HüU : 8 + 3 cm
Sitzhöhe an vM und hM: + 1 bis 2 cm
```

**Technische Formel:**

```text
versatz_vM(saumerweitert) = HueU / 8 − 1,5 cm
versatz_hM(saumerweitert) = HueU / 8 + 3 cm
sitzhoehe_versatz(saumerweitert) = 1 bis 2 cm
```

**Eingaben und Einheiten:** `HueU` – Hüftumfang, cm.

**Ausgabe und Einheit:** `versatz_vM`, `versatz_hM`, `sitzhoehe_versatz` –
Streckenmaße, cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** `versatz_vM` und
`versatz_hM` sind feste Werte (kein Bereich); `sitzhoehe_versatz` bleibt ein
Bereich `1` bis `2 cm` ohne Auswahlregel.

**Abhängigkeiten:** Andere der beiden Hosenrock-Varianten der Seite; betrifft
dieselbe Konstruktionsstelle wie Formel 1/2/3 (Textbereiche) und Formel 6
(andere Variante). Der saumerweiterte Rock-Grundschnitt selbst ist laut
Seitentext ein größeres Innenbeinteil „hier kürzer als in ☐2" – Bezug auf
eine Vorseite dieses Kapitels, hier nicht kopiert.

**Status:** offen

**Offene Fragen:** Werte stammen aus der Skizzenbeschreibung, nicht aus dem
OCR-Text, und sind am Original noch nicht bestätigt. Verweis „kürzer als in
☐2" auf Vorseite noch nicht verlinkt.

## Zusammenfassung

Sieben Stellen erfasst, keine davon vollständig fachlich bestätigt – nur der
Zahlenausdruck `HüU : 8 − 1,5 bis −2 cm` (Formel 2, Teil) ist am Original
bestätigt. Die drei Textschritte (Formel 1–3) geben Bereiche an, die sich
zahlenmäßig genau aus den festen Einzelwerten der beiden gezeichneten
Hosenrock-Varianten (Formel 6, 7) zusammensetzen – ob das eine bewusste
Buchregel oder Zufall ist, bleibt offen. Formel 4 und 5 sind reine
geometrische Konstruktionsanweisungen ohne Zahlenwert. Für einen späteren
Codevertrag muss Werner mindestens klären, ob die Auswahl zwischen den
Hosenrock-Varianten (☐4/☐5) die Textbereiche vollständig erklärt, und die
übrigen in „Offene Fragen" genannten Punkte am Original prüfen.
