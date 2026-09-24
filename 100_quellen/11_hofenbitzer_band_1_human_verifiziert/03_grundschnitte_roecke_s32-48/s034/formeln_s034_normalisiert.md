# Formeln – s034 (normalisiert)

Technische Fassung zu [formeln_s034.md](formeln_s034.md). Walking-Skeleton-Durchgang:
alle Formeln der Seite sind erfasst, aber nur die in [s034.md](s034.md) genannten
Stellen sind am Original bestätigt (`Status: normalisiert`). Alle anderen
Formeln stehen auf `Status: offen`, bis Werner sie am Buch bestätigt.

## F0 – Taillenausfall als Ausgangsgröße

- **Quelle:** [formeln_s034.md](formeln_s034.md#f0--taillenausfall-als-ausgangsgröße)
- **Buchfassung:**
  ```text
  Aus der Differenz zwischen Hüft- und Taillenweite ergibt sich der
  Taillenausfall, der zur Formung der Figur aufgeteilt und abgenäht wird.
  ```
- **Technische Formel:** `TaAf = Hueftweite - Taillenweite`
- **Eingaben und Einheiten:** `Hueftweite` (cm), `Taillenweite` (cm)
- **Ausgabe und Einheit:** `TaAf` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine auf dieser Seite genannt
- **Abhängigkeiten:** Grundgröße für F5, F6, F7, F9; Variablennamen
  `Hueftweite`/`Taillenweite` vermutlich auf einer Vorseite definiert (nicht
  Teil dieser Seite, nur verlinken)
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Auf dieser Seite steht nur Prosatext,
  keine explizite Gleichung; Herkunft von `Hueftweite`/`Taillenweite` (Maß
  oder abgeleitete Größe) ist hier nicht belegt.

## F1 – Taillenerhöhung an der Seitenlinie (P7 → P10)

- **Quelle:** [formeln_s034.md](formeln_s034.md#f1--taillenerhöhung-an-der-seitenlinie-p7--p10)
- **Buchfassung:**
  ```text
  Von P7 aus die Seitenlinie um 1 bis 1,5 cm nach oben verlängern → P10.
  Normal ausgeprägte Hüftrundung: 1 cm Taillenerhöhung an der Seitenlinie.
  Stärkere Hüftrundung: Taillenerhöhung von bis zu 1,5 cm.
  ```
- **Technische Formel:** `TaillenerhoehungSeitenlinie = 1 cm` (normale
  Hüftrundung) `oder bis 1,5 cm` (stärkere Hüftrundung)
- **Eingaben und Einheiten:** Hüftrundungsgrad (kategorial: normal / stärker
  ausgeprägt)
- **Ausgabe und Einheit:** `TaillenerhoehungSeitenlinie` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Buch nennt für „normal"
  einen festen Wert (1 cm), für „stärker" nur eine Obergrenze („bis zu
  1,5 cm") ohne Untergrenze; ob dazwischen ein Bereich oder zwei diskrete
  Fälle gemeint sind, bleibt offen.
- **Abhängigkeiten:** Eingangsgröße für F3, F4 (Anteile der Erhöhung)
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Kategorisierung der Hüftrundung
  („normal" vs. „stärker") ist nicht weiter definiert; keine Untergrenze für
  den stärkeren Fall.

## F2 – Erhöhte Taillenlinie ab P10 auswinkeln

- **Quelle:** [formeln_s034.md](formeln_s034.md#f2--erhöhte-taillenlinie-ab-p10-auswinkeln)
- **Buchfassung:**
  ```text
  Von P10 aus eine erhöhte Taillenlinie ca. 6 cm nach links und nach rechts auswinkeln.
  ```
- **Technische Formel:** `ErhoehteTaillenlinieLaenge = ca. 6 cm` je Seite
- **Eingaben und Einheiten:** keine
- **Ausgabe und Einheit:** `ErhoehteTaillenlinieLaenge` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** `ca.` erhalten, kein
  fester Wert
- **Abhängigkeiten:** geometrische Hilfslinie für F3/F4/F9
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine

## F3 – Erhöhung für den vorderen Abnäher

- **Quelle:** [formeln_s034.md](formeln_s034.md#f3--erhöhung-für-den-vorderen-abnäher)
- **Buchfassung:**
  ```text
  0,5 bis 0,7 cm ca. 1/2 Erhöhung an der Seitenlinie
  ```
- **Technische Formel:** `vErhoehung = 0,5 bis 0,7 cm ≈ 1/2 * TaillenerhoehungSeitenlinie`
- **Eingaben und Einheiten:** `TaillenerhoehungSeitenlinie` (cm, aus F1)
- **Ausgabe und Einheit:** `vErhoehung` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Bereich `0,5 bis 0,7 cm`
  wörtlich erhalten
- **Abhängigkeiten:** F1
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Das Zeichnungslabel `½ wie bei P10`
  ist bestätigt, der Zahlenbereich `0,5 bis 0,7 cm` selbst noch nicht. Die
  rechnerische Hälfte von F1 (1 bis 1,5 cm) wäre 0,5 bis 0,75 cm, das Buch
  nennt aber 0,5 bis 0,7 cm – Abweichung dokumentiert, nicht geglättet.

## F4 – Erhöhung für den hinteren Abnäher (bestätigt)

- **Quelle:** [formeln_s034.md](formeln_s034.md#f4--erhöhung-für-den-hinteren-abnäher-bestätigt)
- **Buchfassung:**
  ```text
  0,3 bis 0,5 cm ≈ ⅓ der Erhöhung an der Seitenlinie
  ```
- **Technische Formel:** `hErhoehung = 0,3 bis 0,5 cm ≈ 1/3 * TaillenerhoehungSeitenlinie`
- **Eingaben und Einheiten:** `TaillenerhoehungSeitenlinie` (cm, aus F1)
- **Ausgabe und Einheit:** `hErhoehung` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Bereich `0,3 bis 0,5 cm`
  wörtlich erhalten
- **Abhängigkeiten:** F1
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** keine

## F5 – Tabelle Hüftabstich und Abnäherinhalte

- **Quelle:** [formeln_s034.md](formeln_s034.md#f5--tabelle-hüftabstich-und-abnäherinhalte)
- **Buchfassung:**
  ```text
  Hüftabstich:      ½ TaAf ± 1        Beispiel: 6,5
  v. Abnäher:        0 oder 1,5 bis 2,5   Beispiel: 2,5
  1.h. Abnäher:      bis 4,5          Beispiel: 4
  2.h. Abnäher:      optional         Beispiel: ---
  Kontrolle:         Σ = TaAf         Beispiel: 13
  ```
- **Technische Formel:**
  ```text
  Hueftabstich = TaAf/2 ± 1
  vAbnInhalt   = 0 oder [1,5 .. 2,5]
  hAbn1Inhalt  = [0 .. 4,5]
  hAbn2Inhalt  = optional
  Kontrolle: Hueftabstich + vAbnInhalt + hAbn1Inhalt + hAbn2Inhalt = TaAf
  ```
- **Eingaben und Einheiten:** `TaAf` (cm, aus F0)
- **Ausgabe und Einheit:** `Hueftabstich`, `vAbnInhalt`, `hAbn1Inhalt`,
  `hAbn2Inhalt` (je cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Bereiche wörtlich
  erhalten; `2.h. Abnäher` ausdrücklich optional
- **Abhängigkeiten:** F0, F7 (Hüftabstich-Formel im Fließtext), F6
  (Bedingung für zweiten hinteren Abnäher), F8 (vorderer Abnäherinhalt im
  Fließtext)
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Die Tabelle nennt für den Hüftabstich `½ TaAf ± 1` (symmetrisch), der
    Fließtext (F7) nennt für flache Hüftrundung `−1 bis −1,5 cm` und für
    starke `+1 bis +1,5 cm` (asymmetrisch, mit größerer Obergrenze). Beide
    Fassungen nebeneinander dokumentiert, nicht zusammengeführt.
  - Die Tabelle nennt für den vorderen Abnäher `0 oder 1,5 bis 2,5`, der
    Fließtext (F8) unterscheidet drei Fälle: normal `ca. 2`, schwach `0 oder
    1 bis 1,5`, stark `bis 2,5`. Die Bereiche decken sich nicht deckungsgleich
    (Tabelle kennt z. B. keinen separaten `1 bis 1,5`-Fall). Nicht glätten,
    beide Fassungen stehen lassen.
  - Beispielwerte (6,5 / 2,5 / 4 / 13) sind durch die Zeichnung
    (skizzen/s034_skizze_01.png, Pfeile `6,5 cm`/`2,5 cm`/`4,0 cm`) gestützt,
    aber nicht einzeln von Werner bestätigt.

## F6 – Regel zweiter hinterer Abnäher

- **Quelle:** [formeln_s034.md](formeln_s034.md#f6--regel-zweiter-hinterer-abnäher)
- **Buchfassung:**
  ```text
  Beträgt der Inhalt für den hinteren Abnäher mehr als 4,5 cm, sollten zwei
  Abnäher im Rückteil gezeichnet werden (siehe folgende Seite).
  ```
- **Technische Formel:** `wenn hAbn1Inhalt > 4,5 cm: zwei Abnäher im Rückteil, sonst: ein Abnäher`
- **Eingaben und Einheiten:** `hAbn1Inhalt` (cm, aus F5)
- **Ausgabe und Einheit:** Auswahlentscheidung (ein/zwei Abnäher)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Schwellenwert `4,5 cm`
  wörtlich erhalten
- **Abhängigkeiten:** F5; die konkrete Aufteilung auf zwei Abnäher ist auf
  einer Folgeseite beschrieben (siehe Buchhinweis „siehe folgende Seite") –
  nicht Teil dieser Seite, nur verlinken
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine

## F7a – Hüftabstich bei durchschnittlicher Hüftrundung

- **Quelle:** [formeln_s034.md](formeln_s034.md#f7--hüftabstich-grundregel-und-sonderfälle-teilweise-bestätigt)
- **Buchfassung:**
  ```text
  Bei einer durchschnittlich geformten Hüftrundung trägt man den halben
  Taillenausfall ab (beachte Seite 37).
  ```
- **Technische Formel:** `Hueftabstich = TaAf / 2`
- **Eingaben und Einheiten:** `TaAf` (cm, aus F0)
- **Ausgabe und Einheit:** `Hueftabstich` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** gilt bei „durchschnittlich
  geformter Hüftrundung"
- **Abhängigkeiten:** F0; Buch verweist zusätzlich auf Seite 37 – nur
  verlinken, nicht kopieren
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine

## F7b – Hüftabstich bei flacher Hüftrundung (bestätigt)

- **Quelle:** [formeln_s034.md](formeln_s034.md#f7--hüftabstich-grundregel-und-sonderfälle-teilweise-bestätigt)
- **Buchfassung:**
  ```text
  TaAf : 2 − 1 bis −1,5 cm
  ```
- **Technische Formel:** `Hueftabstich = TaAf/2 - [1 .. 1,5]`
- **Eingaben und Einheiten:** `TaAf` (cm, aus F0)
- **Ausgabe und Einheit:** `Hueftabstich` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** gilt bei „flacher
  Hüftrundung"; Bereich `1 bis 1,5 cm` wörtlich erhalten
- **Abhängigkeiten:** F0
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** siehe Widerspruch zu F5 (Tabelle
  nennt `± 1` statt `−1 bis −1,5`)

## F7c – Hüftabstich bei starker Hüftrundung (bestätigt)

- **Quelle:** [formeln_s034.md](formeln_s034.md#f7--hüftabstich-grundregel-und-sonderfälle-teilweise-bestätigt)
- **Buchfassung:**
  ```text
  TaAf : 2 + 1 bis +1,5 cm
  ```
- **Technische Formel:** `Hueftabstich = TaAf/2 + [1 .. 1,5]`
- **Eingaben und Einheiten:** `TaAf` (cm, aus F0)
- **Ausgabe und Einheit:** `Hueftabstich` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** gilt bei „starker
  Hüftrundung"; Bereich `1 bis 1,5 cm` wörtlich erhalten
- **Abhängigkeiten:** F0
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** siehe Widerspruch zu F5 (Tabelle
  nennt `± 1` statt `+1 bis +1,5`)

## F8 – Vorderer Abnäherinhalt (Beckenknochen-Formung)

- **Quelle:** [formeln_s034.md](formeln_s034.md#f8--vorderer-abnäherinhalt-beckenknochen-formung)
- **Buchfassung:**
  ```text
  Hüftknochen normal ausgeprägt:  ca. 2 cm Inhalt
  Hüftknochen schwach ausgeprägt: kein Abnäher oder 1 bis 1,5 cm Inhalt
  Hüftknochen stark ausgeprägt:   bis zu 2,5 cm Inhalt
  ```
- **Technische Formel:**
  ```text
  wenn Hueftknochen = normal:  vAbnInhalt = ca. 2 cm
  wenn Hueftknochen = schwach: vAbnInhalt = 0 oder [1 .. 1,5]
  wenn Hueftknochen = stark:   vAbnInhalt = bis 2,5
  ```
- **Eingaben und Einheiten:** Ausprägung des Hüftknochens (kategorial:
  schwach / normal / stark)
- **Ausgabe und Einheit:** `vAbnInhalt` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** drei Fälle wörtlich
  erhalten; für „stark" keine Untergrenze genannt
- **Abhängigkeiten:** siehe Widerspruch zu F5 (Tabellenwerte)
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Verhältnis zu den Tabellenwerten aus
  F5 ungeklärt (siehe dort); keine Untergrenze für „stark ausgeprägt".

## F9 – Hüftbogen von P10 aus abtragen

- **Quelle:** [formeln_s034.md](formeln_s034.md#f9--hüftbogen-von-p10-aus-abtragen)
- **Buchfassung:**
  ```text
  Von P10 aus den halben Hüftabstich-Betrag jeweils nach rechts und nach links abtragen.
  ```
- **Technische Formel:** `HueftbogenBetrag = Hueftabstich / 2` (je Seite, ab P10)
- **Eingaben und Einheiten:** `Hueftabstich` (cm, aus F5/F7)
- **Ausgabe und Einheit:** `HueftbogenBetrag` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine
- **Abhängigkeiten:** F5, F7a/F7b/F7c
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine

## F10a – Vorderer Abnäher: Länge (bestätigt)

- **Quelle:** [formeln_s034.md](formeln_s034.md#f10--vorderer-abnäher-position-und-länge-länge-bestätigt)
- **Buchfassung:**
  ```text
  senkrecht nach unten die Abnäherlänge 8 bis 10 cm lang auswinkeln → Abnäherspitze
  ```
- **Technische Formel:** `vAbnLaenge = [8 .. 10]` cm
- **Eingaben und Einheiten:** keine
- **Ausgabe und Einheit:** `vAbnLaenge` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Bereich wörtlich erhalten
- **Abhängigkeiten:** keine
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** keine

## F10b – Vorderer Abnäher: Position (Abnähermitte TaU:10)

- **Quelle:** [formeln_s034.md](formeln_s034.md#f10--vorderer-abnäher-position-und-länge-länge-bestätigt)
- **Buchfassung:**
  ```text
  Die Abnähermitte TaU:10 vom vorderen Hüftbogen auf die erhöhte
  Abnäherlinie abtragen
  ```
- **Technische Formel:** `vAbnMitte = TaU:10` (ungeklärt, siehe unten)
- **Eingaben und Einheiten:** ungeklärt
- **Ausgabe und Einheit:** `vAbnMitte` (cm, vermutlich)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine
- **Abhängigkeiten:** möglicherweise Taillenumfang (nicht auf dieser Seite
  definiert)
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** Unklar, ob `TaU:10` eine Formel
  (z. B. Taillenumfang geteilt durch 10) oder ein reines Zeichnungspunkt-Label
  ist. Ohne Werners Bestätigung am Original nicht auflösbar.

## F11 – Vorderer Abnäherinhalt: Aufteilung

- **Quelle:** [formeln_s034.md](formeln_s034.md#f11--vorderer-abnäherinhalt-aufteilung)
- **Buchfassung:**
  ```text
  Den vorderen Abnäherinhalt jeweils zur Hälfte nach rechts und links
  abtragen und die Abnäherschenkel zur Abnäherspitze gerade einzeichnen.
  ```
- **Technische Formel:** `vAbnSchenkelLinks = vAbnSchenkelRechts = vAbnInhalt / 2`
- **Eingaben und Einheiten:** `vAbnInhalt` (cm, aus F5/F8)
- **Ausgabe und Einheit:** `vAbnSchenkelLinks`, `vAbnSchenkelRechts` (je cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine
- **Abhängigkeiten:** F5, F8
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine

## F12a – Hinterer Abnäher: Länge (bestätigt)

- **Quelle:** [formeln_s034.md](formeln_s034.md#f12--hinterer-abnäher-position-länge-und-aufteilung-länge-bestätigt)
- **Buchfassung:**
  ```text
  13 bis 16 cm lang nach unten abwinkeln
  ```
- **Technische Formel:** `hAbnLaenge = [13 .. 16]` cm
- **Eingaben und Einheiten:** keine
- **Ausgabe und Einheit:** `hAbnLaenge` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Bereich wörtlich erhalten
- **Abhängigkeiten:** keine
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** keine

## F12b – Hinterer Abnäher: Position und Aufteilung

- **Quelle:** [formeln_s034.md](formeln_s034.md#f12--hinterer-abnäher-position-länge-und-aufteilung-länge-bestätigt)
- **Buchfassung:**
  ```text
  In der Abnähermitte zwischen hinterem Hüftbogen und der hinteren Mitte
  Abnähermitte markieren. Den Abnäherinhalt jeweils zur Hälfte nach rechts
  und links abtragen und die Abnäherschenkel gerade einzeichnen.
  ```
- **Technische Formel:**
  ```text
  hAbnMitte = Mitte(hintererHueftbogen, hintereMitte)
  hAbnSchenkelLinks = hAbnSchenkelRechts = hAbn1Inhalt / 2
  ```
- **Eingaben und Einheiten:** Positionen `hintererHueftbogen`,
  `hintereMitte` (nicht auf dieser Seite definiert); `hAbn1Inhalt` (cm, aus F5)
- **Ausgabe und Einheit:** `hAbnMitte` (Position), `hAbnSchenkelLinks`,
  `hAbnSchenkelRechts` (je cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine
- **Abhängigkeiten:** F5; Bezugspunkte `hintererHueftbogen`/`hintereMitte`
  vermutlich aus einer Vorseite – nur verlinken
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine
