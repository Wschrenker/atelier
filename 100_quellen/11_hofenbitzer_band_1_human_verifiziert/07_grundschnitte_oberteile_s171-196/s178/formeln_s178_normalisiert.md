# Formeln s178 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s178.md`](formeln_s178.md) vermerkt, trägt die
Seite weiterhin den Status `OCR-Rohfassung – noch nicht menschlich
verifiziert`. Nur die vier in [s178.md](s178.md) unter „Vorab geklärte … Stellen"
genannten Werte sind von Werner am Original bestätigt. Dies ist ein
Walking-Skeleton-Durchlauf, kein Ersatz für die vollständige Bestätigung der
Seite.

## Formel 1 – Brustweite, Taillenweite, Hüftweite mit Zugabe

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 1
- **Buchfassung:**
  ```text
  BrU | Brustumfang | 88 | + | 6 = | BrW | 94 | ½ 48
  TaU | Taillenumfang | 68 | + | 4 = | TaW | 72 | ½ 36
  HüU | Hüftumfang | 97 | + | 4 = | HüW | 101 | ½ 50,5
  ```
- **Technische Formel:**
  ```text
  BrW = BrU + Zugabe_BrU   (Zugabe_BrU = 6)
  TaW = TaU + Zugabe_TaU   (Zugabe_TaU = 4)
  HüW = HüU + Zugabe_HüU   (Zugabe_HüU = 4)
  halb(x) = x / 2
  ```
- **Eingaben und Einheiten:** `BrU`, `TaU`, `HüU` (cm, Körpermaße);
  `Zugabe_BrU`, `Zugabe_TaU`, `Zugabe_HüU` (cm, aus Zugabentabelle ab Seite
  176, hier als Zahlenwerte für PK 3 / Größe 38 abgedruckt).
- **Ausgabe und Einheit:** `BrW`, `TaW`, `HüW` (cm) sowie deren Halbwerte (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Zugabewerte sind laut
  Fließtext modell- und passformklassenabhängig (Zugabentabelle ab Seite 176),
  hier nur als konkrete Instanz für PK 3 dokumentiert, nicht als feste
  Buchkonstante.
- **Abhängigkeiten:** Zugabentabelle/Passformklassentabelle ab Seite 176
  (nicht kopiert, nur verlinkt); [[Formel 6]] (Kontrollrechnung nutzt ½ BrW).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nur `BrW = 94` und `½ BrW = 47` sind über Werners Bestätigung
    (`AlT 20,1 + 1,3 = AlT+ 21,4` u. a., siehe [s178.md](s178.md)) gedeckt;
    `TaW`, `HüW` und deren Halbwerte sind unbestätigt.
  - OCR-Rohfassung von Tabelle 1 zeigt `½ 48` statt der bestätigten 47 – als
    abweichende Rohfassungsstelle dokumentiert, nicht aufgelöst.

## Formel 2 – Armlochtiefe (AlT / AlT+)

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 2
- **Buchfassung:**
  ```text
  AlT 20,1 + 1,3 = AlT+ 21,4
  ```
- **Technische Formel:**
  ```text
  AlT+ = AlT + Zugabe_AlT   (Zugabe_AlT = 1,3)
  ```
- **Eingaben und Einheiten:** `AlT` (cm, Armlochtiefe); `Zugabe_AlT` = 1,3 cm.
- **Ausgabe und Einheit:** `AlT+` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `Zugabe_AlT` laut
  Fließtext passformklassenabhängig aus Zugabentabelle ab Seite 176; hier
  konkreter Wert für PK 3.
- **Abhängigkeiten:** Zugabentabelle ab Seite 176 (nicht kopiert, nur
  verlinkt).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - OCR-Rohfassung zeigt stattdessen `AlT+ 21,8` (rechnerisch nicht
    schlüssig); diese Abweichung ist durch Werners Bestätigung aufgelöst und
    hier nur zur Nachvollziehbarkeit mitgeführt.

## Formel 3 – Rückenbreite (RüB / RüB+)

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 3
- **Buchfassung:**
  ```text
  RüB | Rückenbreite (½) | 16,5 | + | 0,5 = | RüB+ | 17
  ```
- **Technische Formel:**
  ```text
  RüB+ = RüB + Zugabe_RüB   (Zugabe_RüB = 0,5)
  ```
- **Eingaben und Einheiten:** `RüB` (cm, halbe Rückenbreite); `Zugabe_RüB` =
  0,5 cm.
- **Ausgabe und Einheit:** `RüB+` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext
  angegeben.
- **Abhängigkeiten:** Zugabentabelle ab Seite 176 (vermutlich, nicht auf
  dieser Seite bestätigt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.

## Formel 4 – Armdurchmesser (ArD / ArD+) mit Viertel- und Drittelwert

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 4
- **Buchfassung:**
  ```text
  ArD | Armdurchmesser | 9,3 | + | 1,5 = | ArD+ | 10,8 | ¼ 2,7 ⅓ 3,6
  ```
- **Technische Formel:**
  ```text
  ArD+ = ArD + Zugabe_ArD   (Zugabe_ArD = 1,5)
  viertel(ArD+) = ArD+ / 4
  drittel(ArD+) = ArD+ / 3
  ```
- **Eingaben und Einheiten:** `ArD` (cm, Armdurchmesser); `Zugabe_ArD` = 1,5
  cm.
- **Ausgabe und Einheit:** `ArD+` (cm) sowie dessen Viertel- und Drittelwert
  (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext
  angegeben; unklar, wofür Viertel- und Drittelwert im weiteren Verlauf der
  Konstruktion verwendet werden (auf dieser Seite nicht erläutert).
- **Abhängigkeiten:** Zugabentabelle ab Seite 176 (vermutlich); spätere
  Konstruktionsschritte außerhalb dieser Seite (nicht ermittelt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - Verwendungszweck von Viertel-/Drittelwert auf dieser Seite nicht benannt.

## Formel 5 – Brustbreite (BrB / BrB+)

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 5
- **Buchfassung:**
  ```text
  BrB | Brustbreite (½) | 18,2 | + | 1 = | BrB+ | 19,2
  ```
- **Technische Formel:**
  ```text
  BrB+ = BrB + Zugabe_BrB   (Zugabe_BrB = 1)
  ```
- **Eingaben und Einheiten:** `BrB` (cm, halbe Brustbreite); `Zugabe_BrB` = 1
  cm.
- **Ausgabe und Einheit:** `BrB+` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext
  angegeben.
- **Abhängigkeiten:** Zugabentabelle ab Seite 176 (vermutlich).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.

## Formel 6 – Kontrolle Σ = ½ BrU

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Kontrolle: Σ = ½ BrU | 44 | + | 3 = | ½ BrW | 47
  ```
- **Technische Formel:**
  ```text
  Σ = 44   (Summe unbenannter Teilstrecken, Zusammensetzung auf dieser Seite nicht aufgeschlüsselt)
  ½ BrW_kontrolle = Σ + 3
  Kontrollbedingung: ½ BrW_kontrolle == ½ BrW   (aus Formel 1)
  ```
- **Eingaben und Einheiten:** `Σ` (cm, Summe, Herleitung auf dieser Seite
  nicht dokumentiert); Zuschlag 3 cm.
- **Ausgabe und Einheit:** `½ BrW_kontrolle` (cm), Kontrollwert gegen `½ BrW`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Kontrollrechnung, kein
  Konstruktionswert; dient nur dem Abgleich mit Formel 1.
- **Abhängigkeiten:** [[Formel 1]] (½ BrW als Vergleichswert); Zusammensetzung
  von `Σ` aus vermutlich RüB, ArD-Viertel und BrB (Formeln 3–5), auf dieser
  Seite nicht explizit erläutert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Herkunft/Zusammensetzung von `Σ = 44` aus den übrigen Tabellenwerten nicht
    explizit im Buchtext dieser Seite benannt.
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt,
    obwohl der Kontrollwert 47 mit dem bestätigten ½ BrW übereinstimmt.

## Formel 7 – Schulterbreite und Schulternahtlänge vorn (SuB / SuNL)

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 7
- **Buchfassung:**
  ```text
  SuB | Schulterbreite | 12,2 | + | 0,3 = | SuNL | 12,5
  ```
- **Technische Formel:**
  ```text
  SuNL = SuB + Zugabe_SuB   (Zugabe_SuB = 0,3)
  ```
- **Eingaben und Einheiten:** `SuB` (cm, Schulterbreite); `Zugabe_SuB` = 0,3
  cm.
- **Ausgabe und Einheit:** `SuNL` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext
  angegeben.
- **Abhängigkeiten:** [[Formel 8]] (SuNL ist Eingabe der hinteren
  Schulternahtlänge).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.

## Formel 8 – Hintere Schulternahtlänge (hSuNL)

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 8
- **Buchfassung:**
  ```text
  hSuNL = SuNL + Einhalteweite
  12,5 + 0,7 = 13,2
  ```
- **Technische Formel:**
  ```text
  hSuNL = SuNL + Einhalteweite   (Einhalteweite = 0,7, im Bereich 0,5 bis 1 cm)
  ```
- **Eingaben und Einheiten:** `SuNL` (cm, aus Formel 7); `Einhalteweite` (cm),
  hier 0,7 cm verwendet.
- **Ausgabe und Einheit:** `hSuNL` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Einhalteweite laut
  OCR-Rohfassung allgemein „0,5 cm bis 1 cm", hier mit 0,7 cm konkret
  verrechnet; Bereichsangabe als Auswahlspielraum erhalten, kein fester
  Default für andere Fälle abgeleitet.
- **Abhängigkeiten:** [[Formel 7]] (Eingabe `SuNL`).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Ob 0,7 cm ein fester Buchwert für diese Größe/PK ist oder eine freie Wahl
    innerhalb des Bereichs 0,5–1 cm, ist aus dieser Seite allein nicht
    eindeutig – die Bereichsangabe bleibt deshalb dokumentiert.

## Formel 9 – Schulterwinkel (SuWi)

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 9
- **Buchfassung:**
  ```text
  SuWi | Schulterwinkel (in Grad, °) | 20° - Alf- lockenrig | - | --- = | SuWi | 20°
  ```
- **Technische Formel:**
  ```text
  SuWi = 20°   (Herkunft/Modifikation aus Buchtext nicht auflösbar)
  ```
- **Eingaben und Einheiten:** keine eindeutig bestimmbar.
- **Ausgabe und Einheit:** `SuWi` = 20° (Grad).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** nicht bestimmbar.
- **Abhängigkeiten:** keine ermittelt.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - OCR-Textstück „Alf- lockenrig" ist nicht als deutsches Fachwort auflösbar;
    möglicherweise OCR-Rauschen einer Bildunterschrift oder eines
    Sonderbegriffs. Ohne Prüfung am Original nicht normalisierbar.

## Formel 10 – Balance (RüL, VL, individuelle und korrigierte Balance, Toleranz)

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 10
- **Buchfassung:**
  ```text
  RüL | Rückenlänge (waagerechte Taille) | 41,6 | ± | --- = | RüL | 41,6
  VL | Vorderlänge (waagerechte Taille) | 45,3 | ± | --- = | VL | 45,3
  Differenz VL - RüL = | Individuelle Balance = | 3,7 | korrigierte Balance = |   |   | 3,7
  Bal | optimale Balance aus Maßtabelle | 3,5 | Optimale und korrigierte Balance müssten jetzt sehr ähnlich sein. (x 1 cm Toleranz, nur wenn kein Figurproblem zu beobachten ist)
  ```
  ```text
  Die Differenz von 0,2 cm zwischen individueller und optimaler Balance liegt
  innerhalb der Toleranz und wird vernachlässigt. Somit werden die RüL und die
  VL unkorrigiert verwendet.
  ```
- **Technische Formel:**
  ```text
  individuelle_Balance = VL - RüL
  korrigierte_Balance = individuelle_Balance + Korrektur   (Korrektur = 0 in diesem Beispiel, da unkorrigiert)
  toleranzpruefung: |korrigierte_Balance - Bal| <= Toleranz   (Toleranz laut Rohfassung „x 1 cm", vermutlich ± 1 cm)
  ```
- **Eingaben und Einheiten:** `RüL`, `VL` (cm, Rücken-/Vorderlänge
  waagerechte Taille); `Bal` (cm, optimale Balance aus Maßtabelle).
- **Ausgabe und Einheit:** `individuelle_Balance`, `korrigierte_Balance` (cm);
  boolesches Toleranzergebnis.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Toleranzbedingung „nur
  wenn kein Figurproblem zu beobachten ist" – fachliche Auswahlbedingung, hier
  nicht automatisch entscheidbar. Toleranzbreite selbst unklar (`x 1 cm` in
  OCR-Rohfassung).
- **Abhängigkeiten:** keine weiteren auf dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieses Abschnitts ist von Werner am Original bestätigt.
  - „x 1 cm Toleranz" ist vermutlich eine OCR-Wiedergabe von „± 1 cm
    Toleranz"; fototreu mit „x" übernommen, nicht aufgelöst.
  - Ob und wie eine Korrektur (Spalte „Korrekturen") tatsächlich angewendet
    wird, wenn die Toleranz überschritten ist, ist auf dieser Seite nicht
    beschrieben (hier: `--- ` = keine Korrektur nötig).

## Formel 11 – Taillenumfall und Hüftfeldbetrag (TaAf, HüFb)

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 11
- **Buchfassung:**
  ```text
  TaAf | Taillenumfall | gemessene TaB | - ½ TaW | =
  HüFb | Hüftfeldbetrag | gemessene HüB | - ½ HüW | =
  ```
- **Technische Formel:**
  ```text
  TaAf = gemessene_TaB - halb(TaW)
  HüFb = gemessene_HüB - halb(HüW)
  ```
- **Eingaben und Einheiten:** `gemessene_TaB`, `gemessene_HüB` (cm, am Körper
  gemessen, auf dieser Seite nicht näher erläutert); `TaW`, `HüW` (cm, aus
  Formel 1).
- **Ausgabe und Einheit:** `TaAf`, `HüFb` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Zahlenwerte auf
  dieser Seite; laut Fließtext werden beide „erst im Laufe der Konstruktion"
  berechnet.
- **Abhängigkeiten:** [[Formel 1]] (`TaW`, `HüW`); spätere
  Konstruktionsschritte außerhalb dieser Seite (nicht ermittelt, welche
  Seite).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - `TaB`/`HüB` (Taillenballance/Hüftballance o. Ä.) auf dieser Seite nicht
    definiert – Abkürzung nicht aufgelöst.
  - Kein Zahlenbeispiel auf dieser Seite vorhanden.

## Formel 12 – Mehrweite im Armloch

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 12
- **Buchfassung:**
  ```text
  Mehrweite im Armloch |   | VAIU + hAIU | - AraU | =
  ```
- **Technische Formel:**
  ```text
  Mehrweite_Armloch = VAlU + hAlU - AraU   (Abkürzungen wie im Buchtext, nicht sicher aufgelöst)
  ```
- **Eingaben und Einheiten:** `VAlU`, `hAlU`, `AraU` (cm, vermutlich
  vorderer/hinterer Armlochumfang und ein Referenzmaß; auf dieser Seite nicht
  definiert).
- **Ausgabe und Einheit:** `Mehrweite_Armloch` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Zahlenwerte auf
  dieser Seite.
- **Abhängigkeiten:** [[Formel 13]] (Sollwert der Mehrweite als Vergleichswert
  für dieses Ergebnis).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Abkürzungen `VAlU`, `hAlU`, `AraU` sind OCR-Lesarten und auf dieser Seite
    nicht definiert; Bedeutung nicht sicher, nicht geraten.
  - Kein Zahlenbeispiel auf dieser Seite vorhanden.

## Formel 13 – Sollwert der Mehrweite

- **Quelle:** [`formeln_s178.md`](formeln_s178.md), Abschnitt 13
- **Buchfassung:**
  ```text
  Sollwert der Mehrweite = 2 × Zugabe zur AlT
  ```
- **Technische Formel:**
  ```text
  Sollwert_Mehrweite = 2 * Zugabe_AlT   (Zugabe_AlT wie in Formel 2)
  ```
- **Eingaben und Einheiten:** `Zugabe_AlT` (cm, aus Formel 2, hier 1,3 cm).
- **Ausgabe und Einheit:** `Sollwert_Mehrweite` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** OCR-Rohfassung nennt
  zusätzlich einen Toleranzbereich „+2 cm bis -1 cm" und den Hinweis „Nur bei
  Oberteilen mit Brustabnäher!" – beides nicht Teil von Werners Bestätigung,
  hier als unbestätigter Zusatz nebeneinander dokumentiert.
- **Abhängigkeiten:** [[Formel 2]] (`Zugabe_AlT`); [[Formel 12]] (Vergleich
  mit tatsächlicher `Mehrweite_Armloch`).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nur die Operatorform `= 2 × Zugabe zur AlT` ist bestätigt. Toleranzbereich
    „+2 cm bis -1 cm" und die Bedingung „Nur bei Oberteilen mit
    Brustabnäher!" stammen unbestätigt aus der OCR-Rohfassung.
  - OCR-Rohfassung zeigt statt „×" ein „-"; diese Abweichung ist durch Werners
    Bestätigung des Operators aufgelöst.
