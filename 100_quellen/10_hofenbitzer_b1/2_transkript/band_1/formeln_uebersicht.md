# Formeln — Hofenbitzer Band 1, S.181–539

Automatisch extrahierte Konstruktionsformeln aus den Transkriptionen in diesem
Ordner (`Neuer Ordner (2)`), mit Seitenverweis zu jeder Formel.

Stand: 2026-08-22

## Hinweise zur Extraktion

- **416 Formeln** über **158 Seiten mit Formeln** (von insgesamt 189 geprüften
  Einzelseiten: S.181–352, S.382–387, S.407, S.454–461, S.537, S.539).
- Bearbeitet in drei Abschnitten: S.181–262 (187 Formeln), S.263–352
  (182 Formeln), S.382–539 (47 Formeln).
- **Wörtliche Übernahme** aus den Quelltexten — keine Nachrechnung, keine
  Rundung, keine stille Korrektur. Rechenoperatoren, Sonderzeichen (½ ¼ ⅓ ·
  − °) und Zahlen stehen wie im Transkript.
- **Korrekturen:** Nur wo eine Sammel-/Entwurfs-Datei ausdrücklich eine
  Korrektur zur Rohtranskription dokumentiert, wurde die korrigierte Fassung
  übernommen und vermerkt (betrifft S.184, Li26-Formel).
- **Bekannte Unstimmigkeiten** aus den Quellen wurden wörtlich mitübernommen,
  nicht „repariert": S.186 (zwei widersprüchliche TaAf/HüFb-Wertepaare, im
  Quelltext als möglicher Buchfehler markiert) und S.219 (eine als rechnerisch
  widersprüchlich markierte Formel).
- **Abgrenzung:** Die auf fast jeder Konstruktionstabellen-Seite wiederkehrenden
  Körpermaß→Zugabe→Modellmaß-Zeilen (reine Zugabetabellen) wurden nicht einzeln
  aufgenommen, um die Liste nicht mit Boilerplate aufzublähen — nur benannte
  Berechnungs- und Kontrollformeln.
- Seiten ohne eigenständige Formel (reine Beschreibung, reine Bildlegenden)
  fehlen bewusst in dieser Liste.

## Verhältnis zu `300_formeln/`

Diese Datei ist eine **Arbeitsgrundlage**, kein fertiger Eintrag für den
Formel-Bereich des Atelier-Repos. Der dortige Prozess (`300_formeln/AGENT.md`)
verlangt für jede Formel zusätzlich eine `F-<Seite>-<lfd>`-Kennung, einen
nachgerechneten Prüfwert (oder ausdrücklich „keine im Buch"), die benötigten
mathematischen Primitive und eine fachliche Freigabe. Nichts hier ist bereits
freigegeben.

---

## S.181 — Grundgerüst für sämtliche Oberteil-Grundschnitte — Halslöcher und Schultern

*Quelle: `s181_oberteil-grundschnitt_rohtranskription.md`*

- **hinteres Halsloch (HLP):** `HlB + 0,5 cm` — von P1 nach links abgetragen zur Bestimmung des hinteren Halslochpunkts.
- **vorderes Halsloch:** `HlB + 0,5` — von P20 nach unten abgetragen zum vorderen Halsloch.
- **VL:** `VL − 1 cm` — Vorderlänge minus 1 cm, von P19 nach oben abgetragen.
- **BrT:** `BrT − 1 cm` — Brusttiefe minus 1 cm, von P20 nach unten abgetragen.
- **BrP:** `½ BrB+ − 0,3 cm` — halbe Brustbreite+ minus 0,3 cm von P21 nach rechts zum Brustpunkt.
- **Schulterwinkel hinten:** `SuWi − 2°` — für die hintere Schulternaht.
- **Schulterwinkel vorne:** `SuWi + 2°` — für die vordere Schulternaht.
- **vAP:** `¼ ArD+` — von P13 nach oben abgetragen zum vorderen Ärmelpunkt.

### S.182 — Legerer Oberteil-Grundschnitt (1), ohne Brust- und Schulterabnäher

*Quelle: `s182_codex_v2_mit_pruefstellen.md`*

- **Hüft-Fehlbetrag (HüFb):** `HüFb = HüB − ½ HüW = 47,3 cm − 50,5 cm = −3,2 cm → 3,2 cm ½ = 1,6 cm` — Hüftweiten-Differenz, die halbiert an den Seitenlinien angestellt wird.

### S.183 — Legerer Oberteil-Grundschnitt (2), mit Brust- und Schulterabnäher

*Quelle: `s183_codex_v2_mit_pruefstellen.md`*

- **Li26 (Grenzlinie Brustabnäher):** `maximal BrU : 20` — maximaler Abstand der Grenzlinie rechts der vorderen Armlinie für die Drehung des Brustabnäher-Dreiecks.

### S.184 — Taillierter Oberteil-Grundschnitt mit Hüftausfall (1)

*Quelle: `s184_oberteil-grundschnitt_rohtranskription.md`; Korrektur aus `s184-186_oberteil-abnaeher_ENTWURF.md`*

- **Li26:** `Li26 = BrU : 20 + 1 cm` (korrigiert laut s184-186_oberteil-abnaeher_ENTWURF.md; Rohtranskription hatte „BrU : 20 ≈ 1 cm") — Grenzlinie für die maximale Drehung des Brustabnäher-Dreiecks um den BrP.
- **Taillenabtrag:** `¼ TaU` (nicht ¼ TaW) — von der vorderen Armlinie auf der erhöhten Taillenlinie abgetragen, Ausgangspunkt für den vorderen Taillenabnäher.
- **vorderer Taillenabnäher (vAbl):** `vAbl = me + 0 bis 1 cm = 3,2 cm` — Reststrecke me zur vM plus PK-abhängiger Zuschlag ergibt den Abnäherinhalt.
- **Taillenausfall (TaAf):** `TaAf = TaB − ½ TaW = 42,8 cm − 36 cm = 6,8 cm` — Differenz zwischen gemessener Taillenbreite und halber Taillenweite.

### S.185 — Taillierter Oberteil-Grundschnitt mit Hüftausfall (2)

*Quelle: `s185_oberteil-grundschnitt_rohtranskription.md`*

- **Hüftausfall (HüAf):** `HüAf = vAbl − 2 cm = 3,2 cm − 2 cm = 1,2 cm` — besonderer Abnäherinhalt, der bis zum Saum gezeichnet wird.
- **Hüft-Fehlbetrag (HüFb):** `HüFb = HüB − ½ HüW = 44,9 cm − 50,5 cm = −5,6 cm → 5,6 cm ; ½ = 2,8 cm` — je zur Hälfte an den Seitenlinien in Hüfthöhe ausgestellt.
- **TaAf (Berechnungstabelle):** `TaAf = gemeinsame TaB 42,8 − ½ TaW 36 = 6,8` — Kontrollrechnung in der Berechnungstabelle.
- **Mehrweite im Armloch:** `vAlU 22,5 + hAlU 24,8 − AraU 44,5 = 2,8` — Differenz zwischen den gemessenen Armlochkurven und dem Armansatzumfang.
- **Sollwert der Mehrweite:** `= 2 · Zugabe zur AIT (Toleranz +2 cm bis −1 cm) = 2,6` — Vergleichswert zur Kontrolle der Armloch-Mehrweite.

### S.186 — Taillierter Oberteil-Grundschnitt ohne Hüftausfall

*Quelle: `s186_oberteil-grundschnitt_rohtranskription.md`*

- **Taillenausfall (TaAf):** `TaAf = TaB − ½ TaW = 46,2 cm − 38,5 cm = 7,7 cm` — im Fließtext genannte Berechnung (Verteilung SN 2×1cm, vAbl 2cm, shAbl 0cm, hAbl 3,7cm = Σ 7,7cm).
- **Hüft-Fehlbetrag (HüFb):** `HüFb = HüB − ½ HüW = 46,5 cm − 51 cm = −4,5 cm → 4,5 cm ; ½ = 2,2 cm` — im Fließtext genannte Berechnung.
- **TaAf (untere Berechnungstabelle, abweichende Werte):** `TaAf = TaB 46 − ½ TaW 38 = 8` — als im Quelltext ausdrücklich vermerkter Widerspruch zur obigen Fließtext-Formel (Buchfehler, zwei nicht übereinstimmende Wertepaare).
- **HüFb (untere Berechnungstabelle, abweichende Werte):** `HüFb = HüB 46,5 − ½ HüW 50,5 = −4` — ebenfalls Teil des vermerkten Widerspruchs.

### S.188 — Enger Oberteil-Grundschnitt für elastische Materialien (1)

*Quelle: `s188_codex_v2_mit_pruefstellen.md`*

- **Kontrolle BrW:** `Σ = ½ BrU → 44 + 1 = ½ BrW 45` — Kontrollrechnung der halben Brustweite in der Konstruktionstabelle.
- **Balance:** `Differenz VL − RüL = 45,3 − 41,6 = 3,7` — individuelle Balance zur Kontrolle gegen die optimale Balance (3,5) aus der Maßtabelle.
- **Taillenausfall (TaAf):** `gemessene TaB 44,3 − ½ TaW 36 = 8,6` — Berechnungsfeld (laut Prüfstelle rechnerisch auffällig).
- **Hüftfehlbetrag (HüFb):** `gemessene HüB 43,8 − ½ HüW 48,5 = −4,7` — Berechnungsfeld.
- **Mehrweite im Armloch:** `vAlU + hAlU − AraU = [leer]` — Formel ohne eingetragene Werte.
- **Sollwert der Mehrweite:** `2 · Zugabe zur AlT (Toleranz +2 cm bis −1 cm) = [leer]` — Formel ohne eingetragene Werte.

### S.189 — Enger Oberteil-Grundschnitt für elastische Materialien (2)

*Quelle: `s189_codex_v2_mit_pruefstellen.md`*

- **Taillenausfall (TaAf):** `= vTaB + hTaB − ½ TaW = 44,6 cm − 36 cm = 7,8 cm`
- **Hüft-Fehlbetrag (HüFb):** `= vHüB + hHüB − ½ HüW = 43,8 cm − 48,5 cm = −4,7 cm → 4,7 cm ½ = 2,4 cm`
- **Halsloch:** `HlB : 3 + 1 cm` — Beschriftung der Konstruktionszeichnung □3.
- **Halsloch (weitere Werte):** `HlB − 0,5` sowie `HlB + 0 bis 0,5 cm` — Beschriftungen □3.
- **Schulterwinkel:** `SuWi + 2°` und `SuWi − 2°`
- **hSuNL:** `SuNL + EW (0 bis 0,5 cm)`
- **Kontrolle BrW:** `vBrW + hBrW = ½ BrW`
- **BrP:** `½ BrB+ − 0,3 cm`
- **Ärmelpunkte an Schulterblattlinie:** `¼ ArD+`, `⅓ ArD+`, `⅔ ArD+`
- **BrT/VL:** `BrT − 1 cm`, `VL − 1 cm`

### S.190 — Enger Oberteil-Grundschnitt für elastische Materialien (3)

*Quelle: `s190_codex_v2_mit_pruefstellen.md`*

- **Beschriftung:** `BrU : 20 − 1 bis +1 cm` — Konstruktionsbeschriftung im Vergleich der beiden Vorderteilvarianten.

### S.191 — Grundschnitt-Vergrößerungen (1): Armloch-Vertiefung und -Verbreiterung

*Quelle: `s191_grundschnitt-weite-und-korsage_rohtranskription.md`*

- **Verteilung Armloch-Verbreiterung:** `⅓ am VT und ⅔ am RT` — Aufteilung der insgesamt 1–6 cm Verbreiterung an der Seitennaht.
- **Armloch-Vertiefung:** `ca. ½ bis ¾ der Armloch-Verbreiterung` — Vertiefungsmaß relativ zur Verbreiterung.
- **Schulter-Verbreiterung:** `¹⁄₁₀ der Armloch-Verbreiterung`
- **BrB-Vergrößerung:** `ca. ⅛ der Armloch-Verbreiterung`
- **RüB-Vergrößerung:** `ca. ¼ der Armlochverbreiterung`
- **Ärmelpunkte:** `¾ der Armloch-Vertiefung` — Verschiebung beider Ärmelpunkte nach unten.

### S.192 — Grundschnitt-Vergrößerungen (2): gerade hM und Seitennaht

*Quelle: `s192_grundschnitt-weite-und-korsage_rohtranskription.md`*

- **Hüftausfall-Entfernung VT:** `½ Hüftausfall` — maximal die Hälfte des Hüftausfalls wird an der Seitennaht entfernt.

### S.193 — Grundschnitt-Vergrößerungen (3): alle Vergrößerungen auf einen Blick

*Quelle: `s193_grundschnitt-weite-und-korsage_rohtranskription.md`*

- **Schulterverbreiterung:** `¹⁄₁₀ Armloch-Verbreiterung`
- **hSuNL:** entspricht `vordere SuNL + Einhalteweite (0,5 bis 1 cm)`
- **BrB-Ausstellung:** `mind. ⅛ Armloch-Verbreiterung`
- **RüB-Vergrößerung:** `bis zu ¼ der Armlochverbreiterung`
- **Ärmelpunkte:** `¾ der Armlochvertiefung` nach unten verschoben
- **Hüft-Ausstellung RT:** `derselbe Betrag wie am hinteren Armloch + 1 cm`

### S.194 — Weite an erprobtem Oberteil-Grundschnitt hinzugeben (1)

*Quelle: `s194_grundschnitt-weite-und-korsage_rohtranskription.md`*

- **Kontrolle BrW:** `Σ = ½ BrU → 44 + 3 = ½ BrW 47`
- **hSuNL:** `SuNL + Einhalteweite 0,5 cm bis 1 cm` → mit Zugabe 0,7 = `hSuNL 13,2`
- **Zugabe zur BrB (Differenz PK3→PK9):** `Differenz = 1,0 cm`, davon `½ = 0,5 cm`
- **Zugabe zum ArD (Differenz PK3→PK9):** `Differenz = 3,5 cm`, davon `⅓ = 1,2 cm` und `⅔ = 2,3 cm`
- **Zugabe zur RüB (Differenz PK3→PK9):** `Differenz = 1,5 cm`
- **Zugabe zur AlT (Differenz PK3→PK9):** `Differenz = 2,7 cm`

### S.195 — Weite an erprobtem Oberteil-Grundschnitt hinzugeben (2)

*Quelle: `s195_grundschnitt-weite-und-korsage_rohtranskription.md`*

- **neue vSuN:** `neue vSuN = alte vSuN + Diff = 12,5 + 0,6 cm = 13,1 cm`
- **neue hSuN:** `neue hSuN = neue vSuN + EW = 13,1 cm + 0,7 cm = 13,8 cm`
- **Ärmelpunkte:** `¾ der Vertiefung des Armlochs (= ¾ Vergrößerung der AlT)`, Beispiel `¾ von 2,7 cm = 2,0 cm`
- **Taillenweiten-Korrektur:** `½ TaW − (TaU + Zugabe) : 2 = 44,6 cm − (72 cm + 16 cm) : 2 = 44,6 cm − 44 cm = 0,6 cm Mehrbetrag`
- **Hüftweiten-Korrektur:** `½ HüW − (HüU + Zugabe) : 2 = 56,1 cm − (97 cm + 12 cm) : 2 = 56,1 cm − 54,5 cm = 1,6 cm Mehrbetrag`

### S.196 — Weite an erprobtem Oberteil-Grundschnitt reduzieren (Korsagen-Grundschnitt)

*Quelle: `s196_grundschnitt-weite-und-korsage_rohtranskription.md`*

- **Zugabe zur BrB (Differenz PK3→PK0):** `Differenz = 0,8 cm`
- **Zugabe zum ArD (Differenz PK3→PK0):** `Differenz = 1,5 cm`, davon `jeweils ½ = 0,75 cm`
- **Zugabe zur RüB (Differenz PK3→PK0):** `Differenz = 0,5 cm`
- **Zugabe zur AlT (Differenz PK3→PK0):** `Differenz = 1,3 cm` — wird als Anhebung der Brustlinie verwendet.

### S.199 — Ärmelmaße; Konstruktionstabelle und Berechnungstabelle

*Quelle: `s199_codex_v2_mit_pruefstellen.md`*

- **ArD-Kontrolle aus OaU:** `OaU : 10 · 6 - 7,5 cm` — Sicherheits-Berechnung des Armdurchmessers aus dem Oberarmumfang.
- **Passformklasse (PK):** `½ Brustweite (Fertigmaß am Oberteil) minus ½ Brustumfang (Körpermaß)`
- **Einhalteweite in cm:** `EW in cm = AlU · Einhalteweite in %`
- **Ärmelkugelumfang:** `ÄKU = AlU + Einhalteweite in cm`
- **Schmaler Ärmel — OaW:** `OaU + 0,7 bis 1 · PK* des Oberteils`
- **Schmaler Ärmel — ÄSaW:** `HgU + 1 bis 2 · PK* des Oberteils`
- **Schmaler Ärmel — EW:** `+3 % bis +10 % des AlU`
- **Enger Ärmel — OaW:** `OaU + 0,5 bis 1 · PK* des Oberteils`
- **Enger Ärmel — ÄSaW:** `HgU + 0 bis 1,5 · PK* des Oberteils`
- **Enger Ärmel — EW:** `0 % bis +3 % des AlU`
- **Weiter Ärmel — OaW:** `OaU + 1 bis 2,5 · PK* des Oberteils`
- **Weiter Ärmel — EW:** `-1 % bis +3 % des AlU`
- **PK\* (Fußnote):** `PK = ½ BrW (½ gemessene BrW am Schnitt) − ½ BrU (½ BrU am Körper)`

### S.200 — Enger Ärmel-Grundschnitt (1)

*Quelle: `s200_codex_v2_mit_pruefstellen.md`*

- **Einhalteweite:** `AlU · Einhalteweite in % = 0,4 cm` (Beispiel PK1, EW 1 %)
- **Ärmelkugelumfang:** `AlU + Einhalteweite in cm = 41,4 (ÄKU)`
- **ÄKLi:** `OaW + 1 bis 1,5 cm = ÄKLi`
- **vordere Armlochkurve:** `vAlU - 0,5 bis - 1 cm`
- **hintere Armlochkurve:** `hAlU - 0 bis - 1 cm`
- **60 % ÄL:** `60 cm · 0,60 = 36 cm`
- **ÄKLi : 8:** `30 cm : 8 = 3,8 cm`
- **ÄKLi : 5:** `30 cm : 5 = 6 cm`
- **ÄKLi : 12:** `30 cm : 12 = 2,5 cm`
- **ÄKLi : 9:** `30 cm : 9 = 3,3 cm`

### S.201 — Enger Ärmel-Grundschnitte (2)

*Quelle: `s201_codex_v2_mit_pruefstellen.md`*

- **Ärmelsaumweite:** `½ Ärmelsaumweite (ÄSaW)` — von der halbierten Saumlinie nach links und rechts abgetragen.

### S.202 — Weiter Ärmel-Grundschnitt (1)

*Quelle: `s202_codex_v2_mit_pruefstellen.md`*

- **Einhalteweite:** `AlU · Einhalteweite in % = 1,3 cm` (Beispiel PK5, EW 3 %)
- **Ärmelkugelumfang:** `AlU + Einhalteweite in cm = 44,8 (ÄKU)`
- **ÄSaW (weiter Ärmel):** `HgU + --- = OaW → ÄSaW = OaW` — Saumweite entsteht automatisch gleich der Oberarmweite.
- **ÄKLi:** `OaW + 0 bis 2 cm`
- **vordere Armlochkurve:** `vAlU - 0 bis - 1 cm`
- **hintere Armlochkurve:** `hAlU - 0 bis - 1 cm`
- **60 % ÄL:** `60 cm · 0,60 = 36 cm`
- **ÄKLi : 8:** `37 cm : 8 = 4,6 cm`
- **ÄKLi : 5:** `37 cm : 5 = 7,4 cm`
- **ÄKLi : 12:** `37 cm : 12 = 3,1 cm`
- **ÄKLi : 14:** `37 cm : 14 = 2,4 cm`

### S.203 — Weiter Ärmel-Grundschnitt (2)

*Quelle: `s203_codex_v2_mit_pruefstellen.md`*

- **hÄP:** `8,6 cm + 1,3 cm · 0,20 = 8,6 cm + 0,3 cm = 8,9 cm` — hAchsel plus 20 % der Einhalteweite ergibt die Übertragungsstrecke zum hinteren Ärmelpunkt.
- **ÄSaW (weiter Ärmel):** `ÄSaW = OaW = 37 cm` — Ärmelsaumweite entspricht der Oberarmweite.

### S.204 — Schmaler Ärmel-Grundschnitt mit hoher Ärmelkugel (1), Grundgerüst

*Quelle: `s204_codex_v2_mit_pruefstellen.md`*

- **Einhalteweite:** `AlU · Einhalteweite in % = 3,3 cm` (Beispiel PK3, EW 8 %)
- **Ärmelkugelumfang:** `ÄKU = AlU + Einhalteweite in cm = 44,5`
- **hintere Linie:** `½ OaW + 0,5 bis 0,7 cm` (hier 15,9 cm)
- **Ärmelkugellinien-Position:** `½ ÄKU - 1 cm`
- **mathematisch exaktere Alternative:** `48 % ÄKU = 44,5 cm · 0,48 = 21,4 cm`
- **Kontrollbereich ÄKLi:** `⅒ AlH` (hier 1,7 cm)
- **60 % ÄL:** `60 cm · 0,60 = 36 cm`
- **ArD-Kontrolle (Korrekturkasten):** `ArD = OaU : 10 · 6 - 7,5 cm`

### S.205 — Schmaler Ärmel-Grundschnitt mit hoher Ärmelkugel (2)

*Quelle: `s205_codex_v2_mit_pruefstellen.md`*

- **Hilfslinie vÄP:** `Abstand (= ¼ ArD+)` — vom vÄP zur Brustlinie gemessener Abstand, an der Ärmelkugellinie nach oben abgetragen.
- **hintere Mitte:** `üb + 0,5 cm = 2,7 cm + 0,5 cm = 3,2 cm`

### S.206 — Schmaler Ärmel-Grundschnitt mit hoher Ärmelkugel (3)

*Quelle: `s206_codex_v2_mit_pruefstellen.md`*

- **Saum:** `½ ÄSaW = 13 cm` (Beispielwert) — von der Saumlinie abgetragen.

### S.207 — Schmaler Ärmel-Grundschnitt mit hoher Ärmelkugel (4)

*Quelle: `s207_codex_v2_mit_pruefstellen.md`*

- **Einhalteweite:** `EW = 2,6 cm + 0,7 cm = 3,3 cm` — me plus mittlerer Zuschlag.
- **hÄP:** `hAchsel üb + EW 0,5 bis 1 cm` → `8,5 cm + 0,7 cm = 9,5 cm` — Übertragung der hAchsel plus EW-Zuschlag.
- **SuP-Aufteilung:** `SuP bei ⅓ im vorderen Bereich, ⅔ hinten` — Verteilung der Einhalteweite.

### S.208 — Schmaler Ärmel-Grundschnitt mit hoher Ärmelkugel (5), Blazerärmel

*Quelle: `s208_codex_v2_mit_pruefstellen.md`*

- **Einhalteweite:** `EW = 2,6 cm + 0,7 cm = 3,3 cm`
- **hÄP:** `hAchsel üb + EW 0,5 bis 1 cm` → `8,5 cm + 0,7 cm = 9,5 cm`
- **SuP-Aufteilung:** `SuP bei ⅓ im vorderen Bereich, ⅔ hinten`

### S.210 — Oberarmweite vergrößern / Weiter Ärmel aus schmalem Ärmel

*Quelle: `s210_codex_v2_mit_pruefstellen.md`*

- **Öffnung/Mehrweite:** `2 × 1 cm = 2 cm` — Öffnung jeweils um ½ Oberarmvergrößerung ergibt die Mehrweite am Oberarm.
- **Hochstellung Ärmelnaht:** `½ Oberarmvergrößerung` (hier 1 cm)

### S.211 — Ärmelsaumweite verändern / Einhalteweite anpassen

*Quelle: `s211_codex_v2_mit_pruefstellen.md`*

- **Öffnung EW vergrößern:** `ca. ½ der fehlenden EW` (hier 0,7 cm), beidseitig
- **Kugelerhöhung:** `ca. ¼ der fehlenden EW` (hier 0,4 cm)
- **Zulegen EW verkleinern:** `ca. ½ der überschüssigen EW` (hier 0,5 cm), beidseitig
- **Kugelverkürzung:** `ca. ¼ der überschüssigen EW` (hier 0,25 cm)

### S.212 — Ärmelanpassung nach Armloch-Vertiefung und -Verbreiterung (1)

*Quelle: `s212_codex_v2_mit_pruefstellen.md`*

- **Ärmelpunkte:** `¾ der Armlochvertiefung` — Verschiebung der Punkte nach unten.
- **Ärmelkugellinien-Vertiefung:** `½ bis ganze Armlochvertiefung (Normwert = ¾)`
- **Armloch-Verbreiterung:** `Armloch-Verbreiterung = vordere + hintere Verbreiterung`

### S.213 — Ärmelanpassung nach Armloch-Vertiefung und -Verbreiterung (2)

*Quelle: `s213_codex_v2_mit_pruefstellen.md`*

- **neue ÄKLi:** `½ Armloch-Vertiefung` (für höhere Kugel), bis zu ganzer Armloch-Vertiefung
- **vordere Ärmelnaht:** `½ Armloch-Verbreiterung` nach außen
- **hintere Ärmelnaht:** `ganze Armloch-Verbreiterung`
- **Kugelverbreiterung hinten:** `⅙ der Armlochverbreiterung`

### S.214 — Ärmelanpassung nach Armloch-Vertiefung und -Verbreiterung (3), Blazerärmel

*Quelle: `s214_codex_v2_mit_pruefstellen.md`*

- **Ärmelpunkte:** `¾ der Armlochvertiefung`
- **Armloch-Verbreiterung:** `Armloch-Verbreiterung = vordere + hintere Verbreiterung`
- **Ärmelkugellinien-Vertiefung:** `½ bis ganze Armlochvertiefung (Normwert = ¾)`
- **vordere/hintere Verbreiterung:** `½ der Armloch-Verbreiterung` bzw. `ganze Armloch-Verbreiterung`

### S.215 — Ärmelanpassung nach Armloch-Vertiefung und -Verbreiterung (4)

*Quelle: `s215_codex_v2_mit_pruefstellen.md`*

- **vordere Ärmelnaht:** `½ Armloch-Verbreiterung`

### S.216 — Ärmelanpassung nach Schulterpolster-Erhöhung

*Quelle: `s216_codex_v2_mit_pruefstellen.md`*

- **Schulter-Erhöhung Verteilung:** `⅓ Schulter-Erhöhung vorne, ⅔ Schulter-Erhöhung hinten`
- **waagerechte Ärmelöffnung:** `ca. ⅓ Schulterpolster-Erhöhung = ungefähre Polsterdicke`
- **senkrechte Öffnung:** `öffnen um ca. ⅙ Schulterpolster-Erhöhung (= ½ Polsterdicke)`

### S.217 — Ärmelanpassung nach Armlochauflockerung

*Quelle: `s217_codex_v2_mit_pruefstellen.md`*

- **Ärmelöffnung vorne/hinten:** `⅙ bis ⅓ der gesamten Armlochauflockerung`
- **Kugelerhöhung:** `¼ bis ½ der gesamten Armlochauflockerung`

### S.218 — Ärmelanpassung mit gleichzeitiger Einstellung der Einhalteweite (1)

*Quelle: `s218_codex_v2_mit_pruefstellen.md`*

- **AlU:** `AlU = vorderes Armloch + hinteres Armloch = 24,2 cm + 26 cm = 50,2 cm`
- **ÄKU_NEU:** `ÄKU_NEU = AlU · (100 % + EW in %) : 100 % = 50,2 cm · (100 % + 7 %) : 100 % = 50,2 cm · 1,07 = 53,7 cm`
- **Fehlweite:** `Fehlweite = ÄKU_ALT − ÄKU_NEU = 48,5 cm − 53,7 cm = −5,2 cm → 5,2 cm`
- **waagerechte Öffnung:** `Öffnung = 2,5 cm : 3 = 0,8 cm` (ca. ⅓ der Polstererhöhung)
- **Mehrweite gesamt:** `2 · ⅓ SuPoE = ⅔ SuPoE → ⅔ von 2,5 cm = ca. 1,7 cm`

### S.219 — Ärmelanpassung mit gleichzeitiger Einstellung der Einhalteweite (2)

*Quelle: `s219_codex_v2_mit_pruefstellen.md`*

- **senkrechter Öffnungsbetrag:** `Öffnung = Fehlweite − ⅔ SuPoE = 5,2 cm − 1,7 cm = 4,5 cm` (laut Prüfstelle rechnerisch widersprüchlich, aber wörtlich übernommen)
- **Fehlbetrag:** `Fehlbetrag = ÄKU_NEU − nachgemessene neue ÄKU = 53,7 cm − 52,5 cm = 1,2 cm`
- **Kugelkorrektur:** `½ Fehlbetrag` (hier 0,6 cm)
- **Öffnungsaufteilung:** `½ von 4,5 cm = 2,25 cm`; `⅓ von 4,5 cm = 1,5 cm`

### S.221 — Kurze Blusen- und Kleiderärmel

*Quelle: `s221_codex_v2_mit_pruefstellen.md`*

- **Saum-Einschlag:** `Saum-Einschlag (SaEs) = Aufschlagbreite - ca. 1 cm`

### S.222 — Weiter Bündchenärmel

*Quelle: `s222_codex_v2_mit_pruefstellen.md`*

- **Schlitzweite:** `⅓ ÄSaW`

### S.223 — Hemden-, Blusen-Ärmel mit Falten, Schlitz und Manschette

*Quelle: `s223_codex_v2_mit_pruefstellen.md`*

- **Ärmelsaum-Weite:** `Manschettenweite + (Faltenzahl × Falteninhalt) = 20 cm + (2 × 4 cm) = 28 cm`
- **halbe Ärmelsaum-Weite:** `½ Ärmelsaum-Weite` (hier 14 cm)
- **Faltenmindestmaß:** `mind. ½ Fal`

### S.225 — Kurze Ärmel mit Erweiterungen (2)

*Quelle: `s225_codex_v2_mit_pruefstellen.md`*

- **Bündchen-Weite:** `Bündchen-Weite = ca. Oberarmumfang (OaU)`

### S.226 — Weite Ärmel und Form-Manschetten (1)

*Quelle: `s226_codex_v2_mit_pruefstellen.md`*

- **Reißverschluss-Zugabe (verdeckt):** `halbe Breite des Reißverschluss-Bandes anzeichnen`
- **Reißverschluss-Zugabe (sichtbar):** `halbe Breite der Reißverschluss-Zähnchen entfernen`

### S.227 — Weite Ärmel und Form-Manschetten (2)

*Quelle: `s227_codex_v2_mit_pruefstellen.md`*

- **Manschette am Saum:** `½ Manschetten-Weite am Saum`

### S.229 — Schmaler Ärmel in ⅞-Länge mit offenem Schlitz / Trompetenärmel

*Quelle: `s229_codex_v2_mit_pruefstellen.md`*

- **⅞-Ärmel Kürzung:** `ca. ⅛ Ärmellänge (ÄL)`
- **Trompetenärmel Ausstellung:** `an der vorderen Ärmelnaht ca. ¼ mehr ausstellen als an der hinteren`

### S.233 — Festlich-elegante Ärmel 7+8 – Kurze lampionförmige Ärmel

*Quelle: `s233_codex_v2_mit_pruefstellen.md`*

- **Bündchenweite:** `OaU + 0 bis 2 cm`

### S.235 — Einnaht-Ärmel, Futter (2)

*Quelle: `s235_codex_v2_mit_pruefstellen.md`*

- **Ärmelkugelnaht-Erhöhung:** `2× NZg (der Armlochnaht) + 0,5 cm` → Beispiel `(2 × 1 cm + 0,5 cm = 2,5 cm)`
- **Kürzung Futtersaum:** `Kürzung = SaEs - Futtermehrlänge = 3 cm - 1 bis 2 cm = 1,5 cm`

### S.237 — Blazer-Ärmel mit geknöpftem Schlitz sowie „imitierter Ärmel-Schlitz"

*Quelle: `s237_codex_v2_mit_pruefstellen.md`*

- **Knopfabstand vom Saum:** `Abstand vom Saum mind. 2 × Knopfdurchmesser`

### S.238 — Futterschnitte für Zweinaht-Ärmel (1)

*Quelle: `s238_codex_v2_mit_pruefstellen.md`*

- **Ärmelkugelnaht-Erhöhung:** `2× NZg des Armlochs + 0,5 cm` → Beispiel `(2 × 1 cm + 0,5 cm = 2,5 cm)`
- **Kürzung Saumkante:** `Kürzung von Saumkante = 3 cm - 1,5 cm = 1,5 cm`

### S.239 — Futterschnitte für Zweinaht-Ärmel (2)

*Quelle: `s239_codex_v2_mit_pruefstellen.md`*

- **Ärmelkugelnaht-Erhöhung:** `jeweils 2× NZg des Armlochs + 0,5 cm` → Beispiel `(2 × 1 cm + 0,5 cm = 2,5 cm)`

### S.240 — Zweinaht-Ärmel mit offenem Schlitz, Briefecken und Futterschnitt

*Quelle: `s240_codex_v2_mit_pruefstellen.md`*

- **Ärmelkugelnaht-Erhöhung:** `jeweils 2× NZg des Armlochs + 0,5 cm` → Beispiel `(2 × 1 cm + 0,5 cm = 2,5 cm)`

### S.246 — Zweinaht-Ärmel mit Saumaufschlag

*Quelle: `s246_codex_v2_mit_pruefstellen.md`*

- **Saumeinschlag:** `üblicher Saumeinschlag 3 cm + Rollweite 0,5 cm = 3,5 cm`

### S.247 — Zweinaht-Ärmel mit besonderen Saumaufschlägen

*Quelle: `s247_codex_v2_mit_pruefstellen.md`*

- **Saumeinschlag:** `üblicher Saumeinschlag 3 cm + Rollweite 0,5 cm = 3,5 cm`

### S.248 — Ärmel mit Oberarmnaht

*Quelle: `s248_codex_v2_mit_pruefstellen.md`*

- **Ärmelkugel-Übertragung vorne:** `14,6 cm + 0,5 = 15,1 cm`
- **Ärmelkugel-Übertragung vorne (2. Wert):** `14,3 cm + 0,7 = 15 cm`
- **Ärmelkugel-Übertragung hinten:** `8,9 cm + 0,5 = 9,4 cm`

### S.250 — Vorbereitungen für eine Ärmelanlage

*Quelle: `s250_codex_v2_mit_pruefstellen.md`*

- **Ärmelkugel-Übertragung:** `8,9 cm + 0,7 = 9,6 cm`

### S.254 — Aufgelockerte Ärmelanlage mit korrektem Ärmelfall (3)

*Quelle: `s254_codex_v2_mit_pruefstellen.md`*

- **Armlochverbreiterung:** `½ bis die ganze Armlochvertiefung` (hier insgesamt 3 cm); Verteilung `vorne ⅓, hinten ⅔`
- **Ärmelkugel-Übertragung:** `üb = 12,6 cm + 0,7 = 13,3 cm`
- **Ärmelteile anpassen:** `½ bis ¾ Armlochvertiefung`

### S.255 — Aufgelockerte Ärmelanlage mit korrektem Ärmelfall (4)

*Quelle: `s255_codex_v2_mit_pruefstellen.md`*

- **Schulterlücke:** `½ Schulterpolstererhöhung (SuPoErh) + 0,5 bis 1 cm`
- **Verteilung SuPoErh:** `vorne und hinten jeweils die halbe SuPoErh, alternativ vorne ⅓ und hinten ⅔ der SuPoErh`

### S.256 — Legere Ärmelanlage mit großer Hebelänge (1)

*Quelle: `s256_codex_v2_mit_pruefstellen.md`*

- **Armlochverbreiterung:** `½ bis die ganze Armlochvertiefung` (hier insgesamt 3 cm); Verteilung `vorne ⅓, hinten ⅔`

### S.257 — Legere Ärmelanlage mit großer Hebelänge (2)

*Quelle: `s257_codex_v2_mit_pruefstellen.md`*

- **Ärmelkurve hinten:** `üb + anteilige EW`

### S.258 — Legere Ärmelanlage mit großer Hebelänge (3)

*Quelle: `s258_codex_v2_mit_pruefstellen.md`*

- **untere Ärmelkurve hinten:** `üb + 1 cm` (Einhalteweite)

### S.280 — Dolman-Ärmel-Anlage (1) Konstruktion

*Quelle: `s280_codex_v2_mit_pruefstellen.md`*

- **Al-Verbreit.:** `Al-Verbreit. ca. ⅓ Al-Vert.` — Armlochverbreiterung wird mit ca. einem Drittel der Armlochvertiefung bemessen (Dolman-Ärmelanlage).
- **AP (Anlagepunkt):** `An der Ärmelnaht ⅔ bis zum ganzen Betrag der Armlochvertiefung abtragen` — Bestimmung des Anlagepunkts (AP) an der Ärmelnaht des Dolman-Ärmels.
- **Schulterüberschneidung:** `An der Schulter 0 bis 1 cm überschneiden` — Maß der Überschneidung des Ärmels an der Schulter bei der Dolman-Anlage.
- **Nahtführungsabstand:** `Der Abstand zum unteren Armloch darf maximal 3 cm sein` — Grenzwert für den Abstand der Nahtführung zum unteren Armloch.

### S.281 — Dolman-Ärmel-Anlage (2) Fertigstellung

*Quelle: `s281_codex_v2_mit_pruefstellen.md`*

- **Öffnungsbetrag Unterarm:** `denselben Betrag unter dem Arm um ⅔ bis zum ganzen Betrag der Armlochvertiefung öffnen` — Öffnungsmaß am Ärmel unter dem Arm für die Hebelänge.
- **AP-Lage (Variante):** `Bestimmt man den Anlegepunkt (AP) bei ¾ Armlochvertiefung, wird der Ärmel mit größerem Winkel ... abstehen` — alternative Bemessung des Anlagepunkts bei ¾ der Armlochvertiefung.

### S.282 — Fledermaus-Ärmel (1) Grundprinzip der Anlage

*Quelle: `s282_codex_v2_mit_pruefstellen.md`*

- **Ärmelkugel-Überschneidung VT:** `die Ärmelkugel 0 bis 2 cm ins VT überschneidet` — Überschneidungsmaß der Ärmelkugel am Vorderteil.
- **Abstand SN–Ärmelnaht:** `Der Abstand zwischen Seitennaht und Ärmelnaht unter dem Arm sollte 3 bis 5 cm betragen` — Bemessung des Abstands unter dem Arm bei der Fledermaus-Ärmelanlage.
- **Armlochauflockerung VT:** `mindestens 1,5 cm Armlochaufockerung` — Mindestmaß der Armlochauflockerung am Vorderteil.
- **Armlochauflockerung RT:** `mindestens 1 cm Armlochaufockerung` — Mindestmaß der Armlochauflockerung am Rückteil.
- **Überschneidung RT:** `wie am VT – 0 bis 1 cm überschneiden` — Überschneidungsmaß am Rückteil analog zum Vorderteil.

### S.283 — Fledermaus-Ärmel (2) Fertigstellung der Schnittteile

*Quelle: `s283_codex_v2_mit_pruefstellen.md`*

- **Unterarmnaht-Abstand:** `Am VT die Unterarmnaht mit einem Mindestabstand von ca. 6 cm zum unteren Armloch formen` — Mindestabstand der Unterarmnaht zum Armloch.

### S.286 — Fledermaus-Ärmel (5) Mit Schulterpolster und nachträglicher Vergrößerung der Hebelänge

*Quelle: `s286_codex_v2_mit_pruefstellen.md`*

- **Schulterpolster-Öffnung:** `Günstig wäre, ca. die doppelte Schulterpolsterdicke zu öffnen` — Öffnungsmaß am Schulterknips in Abhängigkeit von der Schulterpolsterdicke.
- **Schulterpolster-Aufteilung:** `Aufteilung vorne ⅓ und hinten ⅔ der Schulterpolster-Erhöhung` — Verteilung der Schulterpolster-Erhöhung auf Vorder- und Rückteil.

### S.288 — Fledermaus-Ärmel (7) Aus dem Unisex-Oberteil mit Anpassung für Damen-Oberteil

*Quelle: `s288_codex_v2_mit_pruefstellen.md`*

- **Ärmelsaumwinkel:** `½ Ärmelsaumweite abwinkeln` — Abwinkeln der halben Ärmelsaumweite bei der Armgrundlinien-Konstruktion.
- **Differenz VL–RÜL:** `Differenz VL – RÜL = 5,2` — Berechnung der Längendifferenz zwischen Vorderlänge und Rückenlänge.
- **Abnäherinhalt:** `5,2 - 3 bis 4 = Abnäherinhalt 1,2 bis 2,2` — Rechnung zur Ermittlung des Abnäherinhalts aus der Differenz von VL und RüL.

### S.289 — Fledermaus-Ärmel (8) Kurze Formen

*Quelle: `s289_codex_v2_mit_pruefstellen.md`*

- **SN-Verbreiterung:** `Verbreiterung an der Seitennaht ca. ¼ bis ½ der Armlochvertiefung (vorne und hinten identisch)` — Bemessung der Seitennaht-Verbreiterung anhand der Armlochvertiefung.

### S.291 — Kragen- und Kapuzenformen: Halslochvorbereitung

*Quelle: `s291_codex_v2_mit_pruefstellen.md`*

- **hinteres Halsloch:** `das hintere Halsloch um maximal den halben Verbreiterungsbetrag ... vertieft` — Vertiefung des hinteren Halslochs bei Halslochverbreiterung.
- **vorderes Halsloch:** `das vordere Halsloch um maximal den doppelten Verbreiterungsbetrag vertieft` — Vertiefung des vorderen Halslochs bei Halslochverbreiterung.

### S.292 — Stehkragen (1) Winkelkonstruktionen

*Quelle: `s292_codex_v2_mit_pruefstellen.md`*

- **Hochstellungs-Versatz:** `ca. ¼ Hochstellung nach rechts abtragen` — horizontaler Versatz beim anliegenden Stehkragen, bemessen als Viertel der Hochstellung.
- **Hilfslinie:** `Hilfslinie nach ⅓ vHlL zeichnen` — Hilfslinie am Drittel der vorderen Halslochlänge.
- **vHlL-Reduktion:** `vHlL = 12,3 cm – 0 bis 1 cm` — reduzierte vordere Halslochlänge beim anliegenden Stehkragen.

### S.293 — Stehkragen (2) Winkelkonstruktionen

*Quelle: `s293_codex_v2_mit_pruefstellen.md`*

- **Hochstellungs-Versatz (sehr anliegend):** `ca. ¼ Hochstellung; 1,7 cm nach rechts` — horizontaler Versatz beim sehr anliegenden Stehkragen.
- **Zusatzversatz:** `ca. 1/10 Hochstellung` — weiterer Versatzbetrag beim sehr anliegenden Stehkragen.
- **oLi-Hochstellung:** `Die obere Linie über die uLi 0,7 bis 1,5 cm hochstellen` — Position der oberen Linie relativ zur unteren Linie beim S-förmig gerundeten Stehkragen.
- **Hilfslinie:** `Vorne hochstellen und Hilfslinie zu ⅓ vHLL zeichnen` — Hilfslinie am Drittel der vHLL beim S-förmigen Stehkragen.
- **Tiefstellung:** `Vorne 2 bis ⅔ vHLL nach unten und ¼ der Tiefstellung nach rechts abtragen` — Formel für den abstehenden (trichterförmigen) Stehkragen.

### S.294 — Einteilige Umlegekragen (1)

*Quelle: `s294_codex_v2_mit_pruefstellen.md`*

- **KrB (Kragenbreite):** `KrB = StegB + 0,7 bis 1,5 cm` — Kragenbreite berechnet aus der Stegbreite zuzüglich Zuschlag.
- **Vorderer Kragenbruch:** `Vorne 0 bis 3 cm hochstellen, ggf. ¼ Hochstellung nach rechts` — Hochstellung und deren Versatz beim einteiligen Umlegekragen.
- **Hilfslinie:** `Vom SuP ⅓ vHLL abtragen und mit einer Hilfslinie verbinden` — Hilfslinie am Drittel der vHLL.
- **⅓ vHLL Beispielwert:** `⅓ vHLL = 4,1 cm` — konkreter Rechenwert für den mäßig anliegenden Poloshirt-Kragen.

### S.295 — Einteilige Umlegekragen (2) Halsferne Umlegekragen in Winkelkonstruktion

*Quelle: `s295_codex_v2_mit_pruefstellen.md`*

- **Tiefstellung:** `Vom SuP vHLL abtragen und von dort 1 bis 8 cm nach unten abwinkeln. Nach rechts ¼ Tiefstellung abtragen` — Bestimmung der vorderen Kragenpunkt-Tiefstellung.
- **Hilfslinie:** `Vom SuP ⅓ vHLL abtragen und mit einer Hilfslinie zur vM verbinden` — Hilfslinie am Drittel der vHLL.
- **KrB je Variante:** `KrB = StegB + 1 bis 2 cm` (Grundform / Var. 6) — `KrB = StegB + 1,5 bis 2,5 cm` (Var. 7) — `KrB = StegB + 2 bis 3 cm` (Var. 8) — Kragenbreite in Abhängigkeit von der Stegbreite bei den halsfernen Umlegekragen-Varianten.

### S.296 — Einteilige Umlegekragen (3) Winkelkonstruktion mit S-förmiger Kragennaht

*Quelle: `s296_codex_v2_mit_pruefstellen.md`*

- **Hochstellung vM:** `vHLL abtragen → vM. Dort nach oben 0,2 bis 1 cm abwinkeln` — Hochstellung des vorderen Kragenpunkts.
- **KrB je Variante:** `KrB = StegB + 0,7 bis 2 cm` (Var. 2) — `KrB = StegB + 0,7 bis 3 cm` (Var. 3) — `KrB = StegB + 0,7 bis 4 cm` (Var. 4) — Kragenbreite in Abhängigkeit von der Stegbreite.
- **vHLL-Reduktion:** `vHLL = 12,3 cm − 0,5 cm` (Var. 3 und 4) — reduzierte vordere Halslochlänge bei flacheren Kragenvarianten.

### S.297 — Einteilige Umlegekragen (4) Einteiliger Steh-Umlegekragen mit geradem vorderen Kragenbruch

*Quelle: `s297_codex_v2_mit_pruefstellen.md`*

- **Hochstellung vM:** `vHLL abtragen → vM. Dort nach oben 0,5 bis 1 cm abwinkeln` — Hochstellung des vorderen Kragenpunkts.
- **vordere Stegbreite:** `vordere Stegbreite = StegB − ca. 0,5 cm` — vordere Stegbreite berechnet aus der hinteren Stegbreite.
- **KrB:** `KrB = StegB + 0,7 bis 1,5 cm` — Kragenbreite aus Stegbreite (Grundform und Varianten 6, 7).

### S.298 — Zweiteiliger Steh-Umlegekragen mit angesetztem Steg (1)

*Quelle: `s298_codex_v2_mit_pruefstellen.md`*

- **untere Stegnaht:** `Die untere Stegnaht von der hM abwinkeln und in StegB (2,5 bis 7 cm, je nach Stegrundung) parallel zur vM formen` — Stegbreiten-Bemessung.
- **obere Stegnaht:** `Den Abstand zur StegN messen und darüber + 1 cm übertragen` — Formel für Lage der oberen Stegnaht.
- **KrB:** `An der hM die Kragenbreite (KrB) = StegB + 0,7 bis 1,5 cm abtragen` — Kragenbreite aus Stegbreite.
- **KrKa-Zuschlag:** `KrB + 0 bis 0,4 cm` — Zuschlag zur Kragenkante.
- **⅓ vHLL Beispielwert:** `⅓ vHLL = 4,1 cm` — konkreter Rechenwert.
- **Hochstellungsversatz Varianten:** `¼ Hochstellung = 0,7 cm` (Var. 3) — `¼ Hochstellung 1,7 cm` (Var. 4) — horizontaler Versatz bei stärker anliegenden Varianten.

### S.299 — Zweiteiliger Steh-Umlegekragen mit angesetztem Steg (2)

*Quelle: `s299_codex_v2_mit_pruefstellen.md`*

- **KrB:** `KrB = StegB + 0,7 bis 1,5 cm` — Kragenbreite aus Stegbreite (Varianten 7, 8, 9).
- **KrKa/KrBr-Zuschlag:** `+ 0 bis 0,5 cm` — Zuschlag an Kragenkante/Kragenbruch (Var. 7).

### S.300 — Konstruktions-Varianten von besonderen Steh-Umlegekragen (Napoleon-/Trenchcoat-Kragen)

*Quelle: `s300_codex_v2_mit_pruefstellen.md`*

- **vStegB:** `vStegB = hStegB − 0 bis 1,5 cm` — vordere Stegbreite berechnet aus der hinteren Stegbreite.
- **KrB:** `KrB = hStegB + 1 bis 4 cm` — Kragenbreite aus hinterer Stegbreite.
- **Hochstellung:** `Hochstellung ca. ½ bis ¾ der vHLL` — Bemessung der Hochstellung relativ zur vHLL.
- **Kragenkanten-Viertelteilung:** `je ca. ⅓ hHLL = 3,0 cm` — Konstruktionsmaß für die Viertelteilung der Kragenkante.
- **Napoleon-Stegnaht:** `messen = 5,1 cm; übertragen 5,1 cm + 1,5 cm = 6,6 cm` — Berechnung der übertragenen Stegnaht-Länge beim Napoleon-Kragen.
- **Trenchcoat-Stegnaht:** `messen = 4,6 cm; übertragen 4,6 cm + 3,5 cm = 8,1 cm` — Berechnung der übertragenen Stegnaht-Länge beim Trenchcoat-Kragen.

### S.302 — Anliegender Umlegekragen mit innenliegendem Kragensteg

*Quelle: `s302_codex_v2_mit_pruefstellen.md`*

- **Hochstellung:** `Eine Hochstellung von ca. ¼ bis ½ vHLL abtragen und ca. ¼ der Hochstellung nach rechts abtragen` — Bemessung der Hochstellung und ihres Versatzes.
- **Hilfslinie:** `Hilfslinie von dort zu ⅓ vHLL` — Hilfslinie am Drittel der vHLL.
- **mittlerer Einschnitt:** `Der mittlere Einschnitt erhält ca. ⅓ KrB` — Öffnungsmaß des mittleren Einschnitts an der Kragenbreite.
- **seitliche Einschnitte:** `Die Öffnung der beiden seitlichen Einschnitte ist ca. ½ der Differenz zwischen Kragenbreite (KrB) und Steghöhe (StegH), hier 4,5 cm − 3 cm = 1,5 cm → ½ = 0,7 cm` — vollständige Formel mit Rechenbeispiel für die Öffnung der seitlichen Einschnitte.
- **⅓ hHLL Beispielwert:** `ca. ⅓ hHLL = 3,0 cm` — Einschnittabstand an der Schulter.
- **Nahtzugabe Stegnaht:** `Die Stegnaht erhält bei 0,7 Abstand eine Nahtzugabe (NZg) von 0,5 cm und bei 1 cm Abstand eine NZg von 0,7 cm` — Nahtzugabe in Abhängigkeit vom gewählten Abstand.

### S.303 — Anliegende Umlege- und Flachkragen mit innenliegendem Kragensteg (Winkelkonstruktionen)

*Quelle: `s303_codex_v2_mit_pruefstellen.md`*

- **⅓ hHLL Beispielwert:** `ca. ⅓ hHLL = 3,0 cm` — Einschnittabstand an der Schulter (alle drei Varianten).
- **Öffnungsbeträge Var. 32 (KrB 8 cm, StegH 4 cm):** `öffnen ca. ½ = 2 cm` / `öffnen ⅓ = 2,7 cm` — Öffnungsmaße der Einschnitte, hergeleitet aus KrB und Steghöhe.
- **Öffnungsbeträge Var. 33 (KrB 8 cm, StegH 2,5 cm):** `öffnen ca. ½ = 2,7 cm` / `öffnen ⅓ = 2,7 cm` — Öffnungsmaße der Einschnitte.
- **Öffnungsbeträge Var. 34 (KrB 12 cm, StegH 2,5 cm):** `öffnen ca. ½ = 4,7 cm` / `öffnen ⅓ = 4 cm` — Öffnungsmaße der Einschnitte.

### S.304 — Einfache Flachkragen: Anlagekonstruktionen mit verschiedenen Steghöhen

*Quelle: `s304_codex_v2_mit_pruefstellen.md`*

- **Kragennaht hM:** `Die Kragennaht an der hM ca. 0,3 bis 0,8 cm ins Halsloch zeichnen` — Vertiefung der Kragennaht an der hinteren Mitte.
- **Kragennaht vM:** `An der vM die Kragennaht um ca. 1 cm vertiefen` — Vertiefung der Kragennaht an der vorderen Mitte.
- **Grundform Schulterbreite:** `ca. ⅔ KrB an der Schulter` / `ca. ½ KrB an der Schulter` — Kragenbreiten-Anteil an der Schulter bei der Grundform.
- **Steghöhen-Varianten (Zulage an der Schulter):** `An der Schulter bis ca. ¼ KrB zulegen` (Var. 4, Steghöhe ca. 0,5 cm) — `bis ca. ½ KrB zulegen` (Var. 5, Steghöhe ca. 0,5 bis 1 cm) — `bis ca. ¾ KrB zulegen` (Var. 6, Steghöhe ca. 0,7 bis 1,5 cm) — Zulagebetrag an der Schulter in Abhängigkeit von der gewünschten Steghöhe, jeweils als Bruchteil der Kragenbreite (KrB).
- **Varianten 36–38 Zulage:** `jeweils 1/12 KrB an der Schulter zulegen` (Var. 36) — `jeweils 1/6 KrB an der Schulter zulegen` (Var. 37) — `jeweils ¼ KrB an der Schulter zulegen` (Var. 38) — abgestufte Zulagebeträge als Bruchteil der Kragenbreite.

### S.305 — Rüschenkragen: Anlagekonstruktionen

*Quelle: `s305_codex_v2_mit_pruefstellen.md`*

- **Tiefstellung:** `Tiefstellung 0 bis 1/3 vHLL` — Bemessung der Tiefstellung beim stehenden Rüschenkragen als Bruchteil der vHLL.
- **Tiefstellungs-Versatz:** `ca. 1/4 Tiefstellung, 1,7 cm nach rechts` — horizontaler Versatz als Viertel der Tiefstellung.

### S.306 — Volantkragen an rundem und V-Ausschnitt

*Quelle: `s306_codex_v2_mit_pruefstellen.md`*

- **Einschnittabstand (runder Volantkragen):** `hinterer Abstand des Einschnitts an der Kragenkante = 1 : (geplante Einschnitte * 2 + 1); hier 1 : (6 Einschnitte * 2 + 1) = 1/13. Alle anderen Abstände sind doppelt so weit entfernt = 2/13` — Divisionsformel zur Verteilung der Einschnitte am Volantkragen.
- **Einschnittabstand (Volantkragen am V-Ausschnitt):** `hinterer Abstand des Einschnitts an der Kragenkante = 1 : (geplante Einschnitte * 2 + 1); hier 1 : (8 Einschnitte * 2 + 1) = 1/17. Alle anderen Abstände sind doppelt so weit entfernt = 2/17` — dieselbe Divisionsformel für 8 Einschnitte.

### S.307 — Volantkragen an breitem Ausschnitt und Goller mit Stehkragen

*Quelle: `s307_codex_v2_mit_pruefstellen.md`*

- **Einschnittabstand (breiter Ausschnitt):** `Kragenkante mit Abständen 1/15 und 2/15; Formel 1 : (7 Einschnitte * 2 + 1) = 1/15; alle anderen Abstände 2/15` — Divisionsformel zur Verteilung der Einschnitte.

### S.308 — Matrosenkragen: Anlagekonstruktion

*Quelle: `s308_codex_v2_mit_pruefstellen.md`*

- **hintere Kragenbreite:** `die hintere Kragenbreite ca. 0 bis 2 cm breiter als an der Schulter vom Halsloch aus abtragen` — hKrB berechnet als KrB an der Schulter zuzüglich Zuschlag.
- **Kragennaht hM:** `Die Kragennaht an der hM ca. 0,3 bis 0,8 cm ins Halsloch zeichnen` — Vertiefung der Kragennaht an der hinteren Mitte.

### S.309 — Matrosenkragen mit Bindeband: Anlagekonstruktion

*Quelle: `s309_codex_v2_mit_pruefstellen.md`*

- **Kragennaht hM:** `Die Kragennaht an der hM ca. 0,3 bis 0,8 cm ins Halsloch zeichnen und wie skizziert zur Ausschnitt-Tiefe formen` — Vertiefung der Kragennaht an der hinteren Mitte.

### S.315 — Ans Vorderteil angeschnittener Stehkragen

*Quelle: `s315_codex_v2_mit_pruefstellen.md`*

- **hHL-Vertiefung:** `hHL messen; ca. 1/2 wie an der Schulter` — Vertiefung des hinteren Halslochs als halber Betrag der Schulter-Halslochverbreiterung.
- **Weite Beleg:** `Weite wie am Vorderteil (-0,2 cm) öffnen und dann ausgleichen` — Öffnungsweite des Belegs relativ zum Vorderteil, reduziert um 0,2 cm.

### S.316 — Schalkragen (1): Konstruktion an das Vorderteil

*Quelle: `s316_codex_v2_mit_pruefstellen.md`*

- **Kragenbruch-Beginn:** `Den Beginn des Kragenbruchs (KrB) 0 bis 1 cm oberhalb des obersten Knopfes bestimmen (hier 0 cm)` — Lage des Kragenbruchbeginns relativ zum obersten Knopf.
- **hKrB:** `hKrB = mindestens hStegB + 1 cm bis max. 7 cm` — hintere Kragenbreite berechnet aus der hinteren Stegbreite.
- **hKrB-Rechenbeispiel:** `hKrB + 1/10 X = 3,5 cm + 4,8 cm : 10 = 3,5 cm + 0,5 cm = 4,0 cm` — vollständiges Rechenbeispiel für die hintere Kragenbreite unter Einbeziehung des Werts X (Abstand vom KrB/vM-Schnittpunkt zur Brustlinie).
- **sStegB-Zuschlag:** `sStegB + 0 bis 1 cm` — Zuschlag zur seitlichen Stegbreite.

### S.317 — Schalkragen (2): Konstruktion an das Vorderteil und Produktionsschnitte

*Quelle: `s317_codex_v2_mit_pruefstellen.md`*

- **hStegB:** `hStegB = sStegB + 0,5 cm` — hintere Stegbreite berechnet aus der seitlichen Stegbreite.
- **hKrB:** `hKrB = mind. hStegB + 1 cm bis max. 7 cm` — hintere Kragenbreite aus der hinteren Stegbreite.
- **hKrB mit X-Anteil:** `die gewünschte hintere Kragenbreite (hKrB) + ⅒ X abtragen` — Zuschlag zur hKrB abhängig vom Wert X (Abstand Kragenbruch/vM-Schnittpunkt zur Brustlinie).
- **sKrB:** `Sie entspricht in etwa der hKrB + 0 bis + 1 cm` — seitliche Kragenbreite berechnet aus der hinteren Kragenbreite.

### S.318 — Schalkragen (3): Produktionsschnitte

*Quelle: `s318_codex_v2_mit_pruefstellen.md`*

- **Verstürz-/Rollweite Kragenkante:** `Am Beleg wird an der Kragenkante ... Verstürzweite plus Rollweite angezeichnet` — addierte Zugabe aus Verstürz- und Rollweite an der Kragenkante.
- **Kragenbeginn:** `Unten am Kragenbeginn nur ca. ½ Rollweite = Verstürzweite anzeichnen` — Formel: die Verstürzweite entspricht am Kragenbeginn der halben Rollweite.

### S.320 — Schalkragen komplett am Oberteil angeschnitten (1)

*Quelle: `s320_codex_v2_mit_pruefstellen.md`*

- **hKrB:** `hKrB = mind. hStegB + 1 cm bis max. 4 cm` — hintere Kragenbreite aus der hinteren Stegbreite (Grenzwert hier 4 statt 7 cm).
- **hKrB-Rechenbeispiel:** `hKrB + ⅒ X = 4 cm − 6,1 cm : 10 = 4 cm − 0,6 cm = 3,4 cm` — vollständiges Rechenbeispiel mit negativem X-Wert (X messen = −6,1 cm).

### S.322 — Reverskragen an fallendem Fasson (1): Konstruktion an das Vorderteil

*Quelle: `s322_codex_v2_mit_pruefstellen.md`*

- **Reversbruch-Beginn:** `Den Beginn des Reversbruchs (Reb) 0 bis 1 cm oberhalb des obersten Knopfes bestimmen (hier 0 cm)` — Lage des Reversbruchbeginns relativ zum obersten Knopf.
- **hKrB:** `hKrB = mind. hStegB + 1 cm bis max. 7 cm` — hintere Kragenbreite aus der hinteren Stegbreite.
- **hKrB-Rechenbeispiel:** `gewünschte hKrB + ⅒ X = 3,5 cm + 4,8 cm : 10 = 3,5 cm + 0,5 cm = 4,0 cm` — vollständiges Rechenbeispiel für die hintere Kragenbreite.
- **sStegB-Zuschlag:** `sStegB + 0 bis 1 cm` — Zuschlag zur seitlichen Stegbreite.

### S.323 — Reverskragen an fallendem Fasson (2)

*Quelle: `s323_codex_v2_mit_pruefstellen.md`*

- **hStegB:** `hStegB = sStegB + 0,5 cm` — hintere Stegbreite aus der seitlichen Stegbreite.
- **hKrB:** `hKrB = mind. hStegB + 1 cm bis max. 7 cm` — hintere Kragenbreite aus der hinteren Stegbreite.
- **hKrB mit X-Anteil:** `die gewünschte hintere Kragenbreite (hKrB) + ⅒ X abtragen` — X ist hier der Abstand vom Schnittpunkt des Reversbruchs mit der vM zur Brustlinie.
- **sKrB:** `Sie entspricht in etwa der hKrB + 0 bis + 1 cm` — seitliche Kragenbreite aus der hinteren Kragenbreite.

### S.324 — Reverskragen (3): Roll- und Verstürzweite sowie Produktionsschnitte

*Quelle: `s324_codex_v2_mit_pruefstellen.md`*

- **Kragenbeginn-Öffnung:** `unten am Kragenbeginn nur ca. die Hälfte der Rollweite geöffnet` — Öffnungsmaß am Kragenbeginn als halbe Rollweite.
- **Reverskante-Zugabe:** `An der Reverskante die Roll- plus die Verstürzweite anzeichnen` — addierte Zugabe aus Roll- und Verstürzweite.
- **Verstürzweite (Var. Öffnen):** `Verstürzweite = ca. ⅓ Rollweite anzeichnen` — Verstürzweite als Drittel der Rollweite.
- **Verstürzweite (Var. Anzeichnen):** `Verstürzweite = ca. ½ Rollweite anzeichnen` — Verstürzweite als Hälfte der Rollweite.

### S.326 — Reverskragen an steigendem Fasson (1)

*Quelle: `s326_codex_v2_mit_pruefstellen.md`*

- **hKrB:** `hKrB = mind. hStegB + 1 cm bis max. 7 cm` — hintere Kragenbreite aus der hinteren Stegbreite.
- **Kragenkante-Zugabe:** `Verstürzweite plus Rollweite anzeichnen` — addierte Zugabe aus Verstürz- und Rollweite an der Kragenkante.

### S.327 — Reverskragen an steigendem Fasson (2)

*Quelle: `s327_codex_v2_mit_pruefstellen.md`*

- **Reversbeginn-Öffnung:** `unten am Reversbeginn für ca. die Hälfte der Rollweite geöffnet` — Öffnungsmaß am Reversbeginn als halbe Rollweite.
- **Verstürzweite:** `Verstürzweite = ca. ½ Rollweite anzeichnen` — Verstürzweite als Hälfte der Rollweite.

### S.328 — Zweiteiliger Reverskragen (1): Entwicklung aus der Kragen-Grundform

*Quelle: `s328_codex_v2_mit_pruefstellen.md`*

- **Kragensteg-Abtrennung:** `Den Kragensteg 0,7 bis 1 cm parallel unterhalb des Kragenbruchs abtrennen` — Lage der Stegabtrennung relativ zum Kragenbruch.
- **Einschnittabstand:** `Drei weitere Einschnitte wie skizziert, im Abstand von ca. ⅓ hintere HL einzeichnen` — Einschnittabstand als Drittel der hinteren Halslochlänge.
- **⅓ hHlL Beispielwert:** `je ca. ⅓ hHlL = 2,9 cm` — konkreter Rechenwert.
- **Zulage Umlegekragenteil:** `ca. ½ zulegen wie an Stegnaht` / `an der Kragenkante den jeweils halben Betrag zulegen` — hälftige Zulage am Umlegekragenteil bzw. an der Kragenkante.

### S.329 — Zweiteiliger Reverskragen (2)

*Quelle: `s329_codex_v2_mit_pruefstellen.md`*

- **Kragenkante-Zugabe:** `Verstürzweite plus Rollweite anzeichnen` — addierte Zugabe aus Verstürz- und Rollweite an Kragenkante und Kragenabstich.

### S.330 — Reverskragen an einem Vorderteil mit angeschnittenem Beleg (1)

*Quelle: `s330_codex_v2_mit_pruefstellen.md`*

- **hKrB-Rechenbeispiel:** `hKrB (3 bis 5 cm) + ⅒ X = 3 cm + 4,8 cm : 10 = 3 cm + 0,5 cm = 3,5 cm` — vollständiges Rechenbeispiel für die hintere Kragenbreite.
- **hStegB:** `hStegB = sStegB + 0,5 cm` — hintere Stegbreite aus der seitlichen Stegbreite.
- **sKrB:** `sKrB = hKrB + 0 bis 0,5 cm` — seitliche Kragenbreite aus der hinteren Kragenbreite.

### S.331 — Reverskragen an einem Vorderteil mit angeschnittenem Beleg (2)

*Quelle: `s331_codex_v2_mit_pruefstellen.md`*

- **Kragensteg-Zulage:** `am Kragensteg ca. ½ Rollweite zulegen` — Zulagebetrag als halbe Rollweite.
- **Umlegekragenteil-Öffnung:** `am Umlegekragenteil ca. ½ Rollweite öffnen` — Öffnungsbetrag als halbe Rollweite.
- **Verstürzweite:** `Verstürzweite ca. ½ Rollweite` — Verstürzweite als Hälfte der Rollweite.

### S.332 — Breiter Schalkragen mit Rückteil-Anlage (1)

*Quelle: `s332_codex_v2_mit_pruefstellen.md`*

- **Kragenbruch-Beginn:** `Den Beginn des Kragenbruchs (KrB) 0 bis 1 cm oberhalb des obersten Knopfes bestimmen (hier 0 cm)` — Lage des Kragenbruchbeginns relativ zum obersten Knopf.
- **hStegB:** `hStegB = sStegB + 0,5` — hintere Stegbreite aus der seitlichen Stegbreite.
- **Schwellenwert Kragenbreite:** `breiter als ½ Schulter` — Bedingung für die Notwendigkeit einer Rückteil-Anlage: Kragenbreite an der Schulter größer als die halbe Schulterbreite.

### S.333 — Breiter Schalkragen mit Rückteil-Anlage (2)

*Quelle: `s333_codex_v2_mit_pruefstellen.md`*

- **Stegbreiten-Verdopplung:** `Am seitlichen Halsloch 2× die sStegB nach oben abtragen, an der hM 2× die hStegB (= sStegB + 0,5 cm)` — doppelte Steg- bzw. hintere Stegbreite für die Rückteil-Anlage.
- **Anlege-Linie:** `Die natürliche Schulterbreite halbieren und von dort 1 cm nach unten abtragen` — Bestimmung des Anlegepunkts über die halbe Schulterbreite abzüglich 1 cm.

### S.334 — Breiter Schalkragen mit Rückteil-Anlage (3): Produktionsschnitte

*Quelle: `s334_codex_v2_mit_pruefstellen.md`*

- **Belegkante-Zugabe:** `Verstürzweite plus Rollweite an die Belegkante anzeichnen` — addierte Zugabe aus Verstürz- und Rollweite.
- **Kragenbeginn:** `Unten am Kragenbeginn nur ca. ½ Rollweite = Verstürzweite anzeichnen` — Verstürzweite als halbe Rollweite am Kragenbeginn.

### S.336 — Halsnaher breiter Schalkragen mit Kragensteg (1): Zweiteiliger breiter Schalkragen

*Quelle: `s336_codex_v2_mit_pruefstellen.md`*

- **Stegabtrennung:** `Die Stegabtrennung ist die spätere Stegnaht und befindet sich 0,7 cm parallel unterhalb des Kragenbruchs` — Lage der Stegabtrennung relativ zum Kragenbruch.
- **Einschnittabstand:** `Drei weitere Einschnitte wie skizziert, im Abstand von ca. ⅓ hintere HL einzeichnen` — Einschnittabstand als Drittel der hinteren Halslochlänge.
- **⅓ hHlL Beispielwert:** `je ca. ⅓ hHlL = 3 cm` — konkreter Rechenwert.
- **Zulage Umlegekragenteil:** `ca. ½ zulegen wie an Stegnaht` — hälftige Zulage am Umlegekragenteil.

### S.337 — Halsnaher breiter Schalkragen mit Kragensteg (2)

*Quelle: `s337_codex_v2_mit_pruefstellen.md`*

- **Zulage Kragenkante:** `an der Kragenkante legt man den jeweils halben Betrag zu` — hälftige Zulage an der Kragenkante.
- **Kragenkante-Zugabe:** `Am Beleg Roll- plus Verstürzweite an der Kragenkante anzeichnen` — addierte Zugabe aus Roll- und Verstürzweite.

### S.338 — Breiter Reverskragen mit Rückteil-Anlage (1)

*Quelle: `s338_codex_v2_mit_pruefstellen.md`*

- **Kragenbruch-Beginn:** `Den Beginn des Kragenbruchs (Krb) 0 bis 1 cm oberhalb des obersten Knopfes bestimmen (hier 0 cm)` — Lage relativ zum obersten Knopf.
- **hStegB:** `hStegB = sStegB + 0,5` — hintere Stegbreite aus der seitlichen Stegbreite.
- **Schwellenwert Kragenbreite:** `breiter als ½ Schulter` — Bedingung für die Rückteil-Anlage.

### S.339 — Breiter Reverskragen mit Rückteil-Anlage (2)

*Quelle: `s339_codex_v2_mit_pruefstellen.md`*

- **Stegbreiten-Verdopplung:** `Am seitlichen Halsloch 2× die sStegB nach oben abtragen, an der hM 2× die hStegB (= sStegB + 0,5 cm)` — doppelte Steg- bzw. hintere Stegbreite für die Rückteil-Anlage.
- **Anlege-Linie:** `Die natürliche Schulterbreite halbieren und von dort 1 cm nach unten abtragen` — Anlegepunkt-Bestimmung über die halbe Schulterbreite abzüglich 1 cm.

### S.340 — Halsnaher breiter Reverskragen mit Kragensteg

*Quelle: `s340_codex_v2_mit_pruefstellen.md`*

- **Reversbeginn-Öffnung:** `Am Reversbeginn nur ca. die Hälfte der Rollweite öffnen` — Öffnungsmaß als halbe Rollweite.
- **Reverskante-Zugabe:** `An Kragenkante und Kragenabstich die Roll- plus die Verstürzweite anzeichnen` — addierte Zugabe.
- **Zulage Umlegekragenteil:** `ca. ½ zulegen wie an Stegnaht` — hälftige Zulage.

### S.342 — Einfache Kapuzen-Grundformen ohne Abnäher

*Quelle: `s342_codex_v2_mit_pruefstellen.md`*

- **Halslochverbreiterung Schulter:** `wie an der Schulter + 0,5 bis 1,5 cm` — Verbreiterung des Halslochs relativ zur Schulter.
- **Halslochvertiefung:** `ca. ½ wie an der Schulter` — Vertiefung des Halslochs als Hälfte des Schulter-Betrags.
- **SuLi-Abstand:** `Die Schulterlinie (SuLi) im Abstand von ca. ⅖ bis ⅘ vHlL parallel über die uLi zeichnen` — Bemessung der Schulterlinie relativ zur vHlL.
- **oLi-Abstand:** `Darüber die obere Linie (oLi) im Abstand von ⅓ des unteren Abstands (⅓ von hier ⅗ vHlL) parallel zur SuLi zeichnen` — Bemessung der oberen Linie als Drittel des SuLi-Abstands.
- **Rechenbeispiel SuLi:** `⅖ bis ⅘ vHlL → (⅗); 14,4 cm · 3 : 5 = 8,6 cm` — konkretes Rechenbeispiel.
- **Rechenbeispiel oLi:** `Abstand zur oLi: ⅓ Abstand zur SuLi; 8,6 cm : 3 = 3,8 cm` — konkretes Rechenbeispiel.
- **KapH:** `Kapuzenhöhe (KapH) = ½ üKoU + 2 bis 5 cm` — Kapuzenhöhe berechnet aus dem halben Überkopfumfang.
- **KapT:** `Kapuzentiefe (KapT) = KapH – ca. 2 bis 6 cm` — Kapuzentiefe aus der Kapuzenhöhe.

### S.343 — Einfache Kapuzen-Grundformen mit Abnäher und mit Teilungsnaht

*Quelle: `s343_codex_v2_mit_pruefstellen.md`*

- **KapT (Variante mit Abnäher/Teilungsnaht):** `Kapuzentiefe (KapT) = KapH – ca. 4 bis 6 cm` — abweichender Bereich gegenüber der Grundform.
- **KapT (weitere Variante):** `Kapuzentiefe (KapT) = KapH – ca. 2 bis 6 cm` — wie Grundform.
- **KapH:** `Kapuzenhöhe (KapH) = ½ üKoU + 2 bis 5 cm` — wie Grundform.

### S.344 — Einfache Kapuzen-Grundform für Maschenware

*Quelle: `s344_codex_v2_mit_pruefstellen.md`*

- **Halslochverbreiterung Schulter:** `wie an der Schulter bis zum doppelten wie an der Schulter` — Verbreiterung relativ zur Schulter.
- **Halslochvertiefung:** `ca. ½ wie an der Schulter` — Vertiefung als Hälfte des Schulter-Betrags.
- **SuLi-Abstand:** `Die Schulterlinie (SuLi) im Abstand von ca. ⅖ bis ⅗ vHlL parallel über die uLi zeichnen` — Bemessung relativ zur vHlL.
- **oLi-Abstand:** `Darüber die obere Linie (oLi) im Abstand von ⅓ des unteren Abstands (⅓ von hier ⅖ vHlL) parallel zur SuLi zeichnen` — Bemessung als Drittel des SuLi-Abstands.
- **Rechenbeispiel SuLi:** `⅖ bis ⅗ vHlL → (½); 12,8 cm : 2 = 6,4 cm` — konkretes Rechenbeispiel.
- **Rechenbeispiel oLi:** `Abstand zur oLi: ⅓ Abstand zur SuLi; 6,4 cm : 3 = 2,1 cm` — konkretes Rechenbeispiel.
- **KapH:** `Kapuzenhöhe (KapH) = ½ üKoU + 0 bis 3 cm` — abweichender Bereich für Maschenware.
- **KapT:** `Kapuzentiefe (KapT) = KapH – ca. 2 bis 6 cm` — Kapuzentiefe aus der Kapuzenhöhe.

### S.345 — Sehr eng anliegende Kapuze ohne und mit Abnäher für Maschenware

*Quelle: `s345_codex_v2_mit_pruefstellen.md`*

- **KapT:** `Kapuzentiefe (KapT) = KapH – ca. 4 bis 6 cm` — Kapuzentiefe aus der Kapuzenhöhe.
- **KapH:** `Kapuzenhöhe (KapH) = ½ üKoU + 0 cm` — Kapuzenhöhe ohne Zuschlag für die sehr eng anliegende Kapuze.

### S.346 — Kapuzen-Grundformen mit Abnäher in verschiedenen Weiten für alle Materialien

*Quelle: `s346_codex_v2_mit_pruefstellen.md`*

- **Halslochverbreiterung Schulter:** `wie an der Schulter bis zum doppelten wie an der Schulter` — Verbreiterung relativ zur Schulter.
- **Halslochvertiefung:** `ca. ½ wie an der Schulter` — Vertiefung als Hälfte des Schulter-Betrags.
- **SuLi-Abstand:** `Abstand zur SuLi: ca. ⅖ bis max. ⁹⁄₁₀ der vHlL` — Bemessung relativ zur vHlL.
- **oLi-Abstand:** `Abstand zur oLi = ⅓ Abstand zur SuLi` — Bemessung als Drittel des SuLi-Abstands.
- **KapH (Grundwert):** `Kapuzenhöhe (KapH) = ½ üKoU + 1 bis 5 cm` — Kapuzenhöhe aus dem halben Überkopfumfang.
- **KapT je Weiten-Variante:** `KapT = KapH – ca. 4 bis 6 cm` (□3, sehr schmal) — `KapT = KapH – ca. 3 bis 6 cm` (□4, etwas weiter) — `KapT = KapH – ca. 2 bis 6 cm` (□5, weit) — Kapuzentiefe aus der Kapuzenhöhe je nach gewünschter Ausschnittweite.
- **KapH je Weiten-Variante:** `KapH = ½ üKoU + 2 bis 5 cm` (□3, □4) — `KapH = ½ üKoU + 1 bis 5 cm` (□5) — Kapuzenhöhe je Variante.
- **Ausschnitt-Weitenanteil der vHlL:** `ca. ⅖ der vHlL` (□3, sehr schmal) — `ca. ⅗ der vHlL` (□4, etwas weiter) — `ca. ⅘ der vHlL` (□5, weit) — Anteil der vHlL für die Kapuzenmittelnaht/Ausschnittweite je Variante.

### S.347 — Kapuzen-Grundformen mit Abnäher und verschiedenen Ausschnittgrößen für alle Materialien

*Quelle: `s347_codex_v2_mit_pruefstellen.md`*

- **SuLi-Abstand (erweiterter Bereich):** `mit den entsprechenden Abständen von ca. ⅖ bis max. ⁹⁄₁₀ vHlL für die gewünschten Kapuzengrößen` — Bemessung der Schulterlinie relativ zur vHlL über alle Ausschnittgrößen.
- **oLi-Abstand:** `Darüber die obere Linie (oLi) ist immer im Abstand von ⅓ des unteren Abstands parallel zur Su-Linie zu zeichnen` — allgemeine Formel: oLi-Abstand als Drittel des SuLi-Abstands.
- **KapH (Textschritt):** `Kapuzenhöhe (KapH) = ½ üKoU + 0 bis 1 cm` — Kapuzenhöhe für diese Konstruktion.
- **KapT:** `Kapuzentiefe (= KapH – 2 bis 6 cm)` — Kapuzentiefe aus der Kapuzenhöhe.
- **KapH (Diagrammangabe):** `Kapuzenhöhe (KapH) = ½ üKoU + 1 bis 5 cm` — abweichende Diagrammangabe zur Kapuzenhöhe.

### S.348 — Grundformen von hoch geschlossenen Kapuzen mit Verschluss für alle Materialien

*Quelle: `s348_codex_v2_mit_pruefstellen.md`*

- **KapT/KapH (kurzer Verschluss):** `Kapuzentiefe (KapT) = KapH – ca. 2 bis 6 cm` / `Kapuzenhöhe (KapH) = ½ üKoU + 1 bis 5 cm` — Formeln für die Kapuze mit kurzem Verschluss.
- **KapT/KapH (hoher Verschluss):** `Kapuzentiefe (KapT) = KapH – ca. 4 bis 6 cm` / `Kapuzenhöhe (KapH) = ½ üKoU + 2 bis 5 cm` — Formeln für die Kapuze mit hohem Verschluss.
- **SuLi-Abstand (hoher Verschluss, Konstruktion 1):** `Schulterlinie (SuLi) im Abstand von ca. ⅗ bis ⅘ vHlL über die untere Linie (uLi) zeichnen` — Bemessung relativ zur vHlL.
- **SuLi-Abstand (hoher Verschluss, Konstruktion 2):** `Schulterlinie (SuLi) ca. ⅖ bis ⅘ vHlL über die untere Linie (uLi) zeichnen` — Bemessung relativ zur vHlL.
- **Halslochverbreiterung Schulter:** `wie an der Schulter + 0,5 bis 1,5 cm` — Verbreiterung relativ zur Schulter.
- **Halslochvertiefung:** `ca. ½ wie an der Schulter` — Vertiefung als Hälfte des Schulter-Betrags.

### S.352 — Kapuzenvarianten mit Teilungsnähten (4) für alle Materialien

*Quelle: `s352_codex_v2_mit_pruefstellen.md`*

- **KapH:** `Kapuzenhöhe (KapH) = ½ üKoU` — Kapuzenhöhe als halber Überkopfumfang, ohne Zuschlag.
- **SuLi-/oLi-Abstand:** `ca. ⅖ bis ⅗ der vHlL` (SuLi-Abstand) / `⅓` (oLi-Abstand als Drittel des SuLi-Abstands) — Bemessung der Grundlinien.

---

### S.382 — Wiener Naht am taillierten Oberteil-Grundschnitt (1)

*Quelle: `s382_codex_transkription.md`*

- **Öffnung seitliches VT (Brustanpassung):** `um ca. 0,3 bis 0,7 cm` — Punkt ⑪: „Eine optimale Passform für eine stärkere Brust erhält man bei wenig elastischen Materialien durch das Öffnen des seitlichen Vorderteils um ca. 0,3 bis 0,7 cm."

### S.384 — Wiener Naht am taillierten Oberteil-Grundschnitt (3)

*Quelle: `s384_codex_transkription.md`*

- **Weitenreduzierung oberhalb der Brust:** `0 bis 0,7 cm Weite reduzieren` — Punkt ③: „Oberhalb der Brust bei Bedarf 0 bis 0,7 cm Weite reduzieren."
- **Zeichnungsbeschriftung Öffnungsbetrag:** `0 bis 0,7 cm öffnen` — Label an der Wiener Naht oberhalb der Brust, korrespondiert mit Punkt ③.

### S.385 — Wiener Naht am taillierten Oberteil-Grundschnitt (4)

*Quelle: `s385_codex_transkription.md`*

- **Zeichnungsbeschriftung Öffnungsbetrag:** `0 bis 0,7 cm öffnen` — Label am VT, entstehende Öffnung durch das Zulegen des Brustabnähers.
- **Öffnung des seitlichen VT (mind.):** `mindestens den Öffnungsbetrag des VT am BrP öffnen` — Punkt ⑬: „Das seitliche VT vom BrP zur Seitennaht einschneiden und mindestens den Öffnungsbetrag des VT am BrP öffnen, siehe Seite 377."

### S.386 — Wiener Naht am taillierten Oberteil-Grundschnitt (5)

*Quelle: `s386_codex_transkription.md`*

- **Weitenreduzierung oberhalb der Brust:** `0 bis 0,7 cm Weite reduzieren` — Punkt ②: „Oberhalb der Brust bei Bedarf 0 bis 0,7 cm Weite reduzieren."
- **Zeichnungsbeschriftung Öffnungsbetrag:** `0 bis 0,7 cm öffnen` — Label an der Wiener Naht, korrespondiert mit Punkt ②.

### S.387 — Wiener Naht am taillierten Oberteil-Grundschnitt (6)

*Quelle: `s387_codex_transkription.md`*

- **Zeichnungsbeschriftung Öffnungsbetrag:** `0 bis 0,7 cm öffnen` — Label an der Wiener Naht (aus Modellentwicklung S.386 übernommen).
- **Öffnung des seitlichen VT (mind.):** `mindestens den Öffnungsbetrag des VT am BrP öffnen` — Punkt ⑬: „Das seitliche VT vom BrP zur Seitennaht einschneiden und mindestens den Öffnungsbetrag des VT am BrP öffnen, siehe vorhergehende und Seite 377."

### S.407 — Prinzess-Form mit Taillennaht (2), saumweite Form

*Quelle: `s407_codex_transkription.md`*

- **Ausstellbetrag an der Seitennaht (Gesäßabnäher-Öffnung):** `an der SN jeweils die Hälfte der Öffnung ausstellen` — Punkt ②: „Den Gesäßabnäher in zwei Abnäher aufteilen, den seitlichen wie am VT am Saum öffnen und an der SN jeweils die Hälfte der Öffnung ausstellen."

### S.454 — Etuikleid (1), Vorderteil

*Quelle: `s454_meerjungfrau_codex_transkription.md`*

- **Weitenreduzierung unter dem Arm (ärmelloses Modell):** `um ca. 0,5 bis 0,7 cm jeweils an VT und RT reduziert` — Punkt 1: „... kann bei diesem engen, ärmellosen Modell die Weite unter dem Arm um ca. 0,5 bis 0,7 cm jeweils an VT und RT reduziert werden."
- **Ausschnitt-Weite am Brustansatz-Kreis:** `um 0,5 bis 0,7 cm reduzieren` — Zeichnungsbeschriftung: „Ausschnitt-Weite am Kreis um 0,5 bis 0,7 cm reduzieren".
- **Armausschnittweite (ärmellos):** `um ca. 0,7 cm reduzieren` — Zeichnungsbeschriftung: „Bei Modell ohne Ärmel die Armausschnittweite am Armloch um ca. 0,7 cm reduzieren".
- **Brustweite am VT (ärmellos):** `bis 0,7 cm reduzieren` — Zeichnungsbeschriftung: „Bei Modell ohne Ärmel die Brustweite am VT bis 0,7 cm reduzieren".

### S.455 — Etuikleid (2), Vorderteil mit Beleg- und Futterentwicklung

*Quelle: `s455_meerjungfrau_codex_transkription.md`*

- **Belegreduzierung an Schulter/Ausschnitt/SN:** `um ca. 0,2 cm ... an der unteren SN bis zu 0,4 cm entfernen` — Punkt 9: „An der Schulter, den Ausschnittkanten und der SN um ca. 0,2 cm, an der unteren SN bis zu 0,4 cm entfernen."
- **Futtersaum-Kürzung:** `um 2 cm kürzen` — Punkt 11: „Den Futtersaum um 2 cm kürzen."
- **Mehrweite am Taillenabnäher im Futter:** `je ca. 0,3 cm Mehrweite` — Zeichnungsbeschriftung, zu Punkt 12: „Am Taillenabnäher ... ausreichend Mehrweite am Futter hinzugeben."

### S.456 — Etuikleid (3), Rückteil mit Schlitz

*Quelle: `s456_meerjungfrau_codex_transkription.md`*

- **Schulterabnäher-Verkleinerung:** `um 1 cm in den Abnäher verschieben` — Punkt 16: „Schulterabnäher verkleinern: Die blaue Fläche mit dem Halsloch, der Schulter und der hM um 1 cm in den Abnäher verschieben (siehe Seite 374)."

### S.457 — Etuikleid (4), Rückteil mit Beleg- und Futterentwicklung

*Quelle: `s457_meerjungfrau_codex_transkription.md`*

- **Belegreduzierung an Schulter/Ausschnitt/SN (RT):** `um ca. 0,2 cm ... an der unteren SN bis zu 0,4 cm entfernen` — Punkt 23: „Beim Kopieren des Belegs an der Schulter, den Ausschnittkanten und der SN um ca. 0,2 cm, an der unteren SN bis zu 0,4 cm entfernen."
- **Mehrlänge Futter oberhalb Schlitz:** `ca. 1 cm Mehrlänge` — Punkt 24: „... muss es oberhalb des Schlitzes ca. 1 cm Mehrlänge erhalten."
- **Futterschlitz-Länge (RV):** `ca. 2 bis 3 cm länger` — Punkt 25: „Der Schlitz für den Reißverschluss ist im Futter ca. 2 bis 3 cm länger."
- **Nahtverschiebung im RV-Bereich:** `um ca. 0,5 cm nach innen gerückt` — Punkt 26: „Im Bereich des RV wird an Beleg und Futter die Naht um ca. 0,5 cm nach innen gerückt."
- **Futtersaum-Kürzung:** `um 2 cm kürzen` — Punkt 27: „Den Futtersaum um 2 cm kürzen."
- **Mehrweite an Taillenabnähern im Futter:** `ca. 0,6 cm Mehrweite` — Punkt 28: „An den Taillenabnähern ca. 0,6 cm Mehrweite in Futter hinzugeben."

### S.458 — Korsagen-Modellentwicklung (1)

*Quelle: `s458_codex_transkription.md`*

- **Taillenanhebung:** `um insgesamt ca. 1 bis 2 cm anheben` — Punkt ⑤: „Die Taillenlinie um insgesamt ca. 1 bis 2 cm anheben."
- **Teilungsnaht-Verschiebung (VT):** `Teilungsnaht um ca. 0,5 bis 1 cm verschieben` — Zeichnungsbeschriftung in ☐3.
- **Teilungsnaht-Verschiebung (RT, relativ zu VT):** `Teilungsnaht um ca. 1 cm mehr verschieben als vorne. Dadurch reduziert sich die Kantenweite.` — Zeichnungsbeschriftung in ☐3.
- **Weitenreduzierung hM/unter Schulterblatt:** `insgesamt um 0,5 bis 1,5 cm reduzieren` — Zeichnungsbeschriftung: „Weite an hM und unter dem Schulterblatt insgesamt um 0,5 bis 1,5 cm reduzieren".
- **Schulterbreite (Rechenfeld):** `½ SuB` — Zeichnungsbeschriftung in ☐4 (Reduzierflächen am Brustansatz).

### S.460 — Miederkorsage (1)

*Quelle: `s460_codex_transkription.md`*

- **Taillenlinien-Erhöhung:** `um 1 bis 2 cm erhöhen` — Punkt ①: „Die Taillenlinie und die Taillennähte um 1 bis 2 cm erhöhen."
- **Reduzierung Taillenabnäher (relativ zum neuen Abnäher):** `um diesen Betrag reduziert` — Punkt ③: „Entsprechend sollte der Taillenabnäher um diesen Betrag reduziert werden." (Betrag = Breite des neuen VT-Abnähers aus Punkt ②, bis zu 2 cm.)
- **Korsagenlänge an der SN:** `um ca. 4 bis 10 cm kürzer` — Punkt ⑧: „An der Seitennaht ist die Korsage deutlich kürzer (um ca. 4 bis 10 cm kürzer)."
- **Reduzierung obere Ausschnittkante:** `um ca. 0,5 bis 1 cm reduzieren` — Punkt ⑩: „Die obere Ausschnittkante um ca. 0,5 bis 1 cm reduzieren."
- **Addition der Abnäherinhalte:** `Die entstehenden Abnäherinhalte addieren (hellgrau) und den Betrag auf einen Abnäher in der Mitte und an die hM verteilen.` — Punkt ⑫.

### S.461 — Miederkorsage (2)

*Quelle: `s461_codex_transkription.md`*

- **Abtrennung an der hM (Schnürung):** `ca. 0,5 bis 1,5 cm abtrennen, so dass sich eine Lücke von bis zu 3 cm öffnet` — Punkt ⑯: „Man kann hierzu an der hM ca. 0,5 bis 1,5 cm abtrennen, so dass sich eine Lücke von bis zu 3 cm öffnet."

### S.537 — Konstruktionstabelle Oberteil

*Quelle: `s537_produktionsschnitt_codex_transkription.md`*

- **BrW (Brustweite):** `Körpermaße + Zugaben = BrW; anschließend ½` — Formular-/Rechenfeld zur Zeile BrU (Brustumfang).
- **TaW (Taillenweite):** `Körpermaße + Zugaben = TaW; anschließend ½` — Formular-/Rechenfeld zur Zeile TaU (Taillenumfang).
- **HüW (Hüftweite):** `Körpermaße + Zugaben = HüW; anschließend ½` — Formular-/Rechenfeld zur Zeile HüU (Hüftumfang).
- **AlT+ (Armlochtiefe mit Zugabe):** `Körpermaße + Zugaben = AlT+` — Formular-/Rechenfeld zur Zeile AlT (Armlochtiefe).
- **Kontrolle (Brustweiten-Kontrolle):** `Σ = ½ BrU` — Kontrollformel in den Proportionsmaßen.
- **hSuNL (hintere Schulternahtlänge):** `SuNL + Einhalteweite 0,5 cm bis 1 cm` — Rechenfeld hSuNL.
- **SuWi (korrigierter Schulterwinkel):** `SuWI - Auflockerung` — Rechenfeld SuWi (Schulterwinkel abzüglich Auflockerung).
- **Individuelle Balance (Differenz):** `VL - RüL =` — Formel zur Ermittlung der individuellen Balance aus Vorder- und Rückenlänge.
- **TaAf (Taillenausfall):** `gemessene TaB - ½ TaW =` — Berechnung des Taillenausfalls.
- **HüFb (Hüftfehlbetrag):** `gemessene HüB - ½ HüW =` — Berechnung des Hüftfehlbetrags.
- **Mehrweite im Armloch:** `vAlU + hAlU - AraU =` — Kontrollformel für die Armloch-Mehrweite.
- **Sollwert der Mehrweite:** `= 2 · Zugabe zur AlT (Toleranz +2 cm bis -1 cm) =` — Sollwertformel für die Armloch-Mehrweite (nur bei Oberteilen mit Brustabnähern).
