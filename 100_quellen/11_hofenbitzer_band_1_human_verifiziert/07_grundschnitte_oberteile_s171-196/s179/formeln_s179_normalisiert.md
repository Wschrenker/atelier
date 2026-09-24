# Formeln s179 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s179.md`](formeln_s179.md) vermerkt, sind nur
zwei Stellen dieser Seite von Werner am Original bestätigt: die Abkürzung
`AlT+` (Formel 4) und die Formel `HlB : 3 + 1 cm` (Formel 2). Alle anderen
Formeln stehen deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit
der Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf auf ausdrücklichen
Wunsch Werners, kein Ersatz für die Bestätigung der übrigen Stellen.

Keine Python-Funktion, kein Engine-Vertrag und keine neue Fachregel werden
hier erzeugt.

## Formel 1 – Grundlinie und P1

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 1
- **Buchfassung:**
  ```text
  ☐3 Senkrechte Grundlinie rechts am Blattrand zeichnen und oben bei P1
  rechtwinklig ca. 20 cm abwinkeln.
  ```
- **Technische Formel:**
  ```text
  grundlinie_laenge ≈ 20 cm  (ca.)
  P1 = Eckpunkt im rechten Winkel am Ende der Grundlinie
  ```
- **Eingaben und Einheiten:** Blattrand als Bezug (keine Buch-Messgröße).
- **Ausgabe und Einheit:** Grundlinie (cm), Punkt `P1`.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` vor 20 cm
  erhalten – kein fester Betrag laut Buch.
- **Abhängigkeiten:** Ausgangspunkt für [[Formel 2]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 2 – Halslochbreite ab P1 (bestätigt)

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Von P1 sind HlB : 3 + 1 cm nach unten abzutragen.
  ```
- **Technische Formel:**
  ```text
  abstand_P1_P2 = HlB / 3 + 1 cm
  ```
- **Eingaben und Einheiten:** `HlB` (Halslochbreite, cm) – Herkunft dieses
  Maßes auf dieser Seite nicht angegeben (vermutlich Konstruktionstabelle
  einer anderen Seite, siehe Abhängigkeiten).
- **Ausgabe und Einheit:** `abstand_P1_P2` (cm), lotrecht ab `P1` nach unten;
  Zielpunkt (im Fließtext nicht ausdrücklich `P2` genannt, aber laut
  Schritt-Reihenfolge und späteren Verweisen „Von P2 ..." in Formel 3–5
  dieser Punkt).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Fester Rechenweg ohne
  `ca.` – Division durch 3, dann `+ 1 cm`, kein Spielraum laut Buchwortlaut.
- **Abhängigkeiten:** baut auf `P1` aus [[Formel 1]] auf; `HlB` selbst nicht
  auf dieser Seite hergeleitet.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Werner bestätigte am Original ausdrücklich nur die Formel selbst
    (`HlB : 3 + 1 cm`), nicht die Zuordnung des Zielpunkts zu „P2" – diese
    Zuordnung ist aus dem Fließtext erschlossen, nicht wörtlich belegt.

## Formel 3 – Modelllänge ab P2 → Saumlinie

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Von P2 die Modelllänge (MoL) nach unten abtragen. Von dort weit nach links
  abwinkeln → Saumlinie
  ```
- **Technische Formel:**
  ```text
  abstand_P2_Saumlinie = MoL
  ```
- **Eingaben und Einheiten:** `MoL` (Modelllänge, cm) – Herkunft nicht auf
  dieser Seite angegeben.
- **Ausgabe und Einheit:** Saumlinie (waagerecht, cm-Abstand ab `P2`).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – direkte
  Maßübertragung ohne Rechenoperation.
- **Abhängigkeiten:** baut auf `P2` aus [[Formel 2]] auf.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Herkunft von `MoL` nicht auf dieser Seite benannt.

## Formel 4 – Armlochtiefe mit Zugabe ab P2 → Brustlinie (Abkürzung bestätigt)

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Von P2 die Armlochtiefe mit Zugabe (AIT+) nach unten abtragen. Von dort
  weit nach links abwinkeln → Brustlinie
  ```
- **Technische Formel:**
  ```text
  abstand_P2_Brustlinie = AlT+
  ```
- **Eingaben und Einheiten:** `AlT+` (Armlochtiefe mit Zugabe, cm) – laut
  [`../s178/formeln_s178.md`](../s178/formeln_s178.md) (dort selbst noch
  unbestätigt) aus `AlT + Zugabe` auf Seite 178 gebildet.
- **Ausgabe und Einheit:** Brustlinie (waagerecht, cm-Abstand ab `P2`).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine eigene Rechnung
  auf dieser Seite – direkte Maßübertragung.
- **Abhängigkeiten:** [[Seite 178]] (Herkunft von `AlT+`); baut auf `P2` aus
  [[Formel 2]] auf.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Werner bestätigte am Original nur die Abkürzung `AlT+` selbst, nicht
    ihre Herkunft aus Seite 178 oder ihren konkreten Zahlenwert auf dieser
    Seite.

## Formel 5 – Rückenlänge ab P2 → Taillenlinie

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 5
- **Buchfassung:**
  ```text
  Von P2 die Rückenlänge (RüL) nach unten abtragen. Von dort weit nach links
  abwinkeln → Taillenlinie
  ```
- **Technische Formel:**
  ```text
  abstand_P2_Taillenlinie = RüL
  ```
- **Eingaben und Einheiten:** `RüL` (Rückenlänge, cm) – Herkunft nicht auf
  dieser Seite angegeben; laut Checkliste dieser Seite gegen „Maßtabelle ab
  Seite 19" und „Seite 174" zu kontrollieren.
- **Ausgabe und Einheit:** Taillenlinie (waagerecht, cm-Abstand ab `P2`).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – direkte
  Maßübertragung.
- **Abhängigkeiten:** baut auf `P2` aus [[Formel 2]] auf; Zielpunkt dieser
  Linie wird in Formel 6 als „P5" bezeichnet (Zuordnung nicht wörtlich
  belegt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Herkunft von `RüL` nicht auf dieser Seite benannt.

## Formel 6 – Hüfttiefe ab P5 → Hüftlinie

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Von P5 die Hüfttiefe (HüT) nach unten abtragen. Von dort weit nach links
  abwinkeln → Hüftlinie
  ```
- **Technische Formel:**
  ```text
  abstand_P5_Hueftlinie = HüT
  ```
- **Eingaben und Einheiten:** `HüT` (Hüfttiefe, cm) – Herkunft nicht auf
  dieser Seite angegeben.
- **Ausgabe und Einheit:** Hüftlinie (waagerecht, cm-Abstand ab `P5`).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – direkte
  Maßübertragung.
- **Abhängigkeiten:** setzt voraus, dass `P5` der Endpunkt der Taillenlinie
  aus [[Formel 5]] ist – diese Zuordnung ist aus der Schrittreihenfolge
  erschlossen, nicht wörtlich im Fließtext belegt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Zuordnung „P5 = Endpunkt der Taillenlinie" nicht wörtlich im Text
    belegt, nur durch Reihenfolge und spätere Verweise plausibel.

## Formel 7 – Taillierte hintere Mitte: Einzug an P5 und P3

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 7
- **Buchfassung:**
  ```text
  Von P5 und P3 jeweils 2 cm nach links abtragen (schlanke Figuren mit
  ausgeprägtem Hohlkreuz oder Figuren mit flachem Gesäß tragen hier jeweils
  2,5 bis 3 cm ab).
  ```
- **Technische Formel:**
  ```text
  einzug_P5 = einzug_P3 = 2 cm                      (Standardfigur)
  einzug_P5 = einzug_P3 ∈ [2,5 cm, 3 cm]             (Hohlkreuz / flaches Gesäß)
  ```
- **Eingaben und Einheiten:** Figurtyp (Auswahl: Standard / ausgeprägtes
  Hohlkreuz / flaches Gesäß).
- **Ausgabe und Einheit:** `einzug_P5`, `einzug_P3` (cm), neue Punkte links
  von `P5` bzw. `P3` auf Taillen- bzw. (vermutlich) Brustlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Auswahlregel nach
  Figurtyp erhalten; Bereich „2,5 bis 3 cm" bleibt Bereich, kein fester
  Default gewählt.
- **Abhängigkeiten:** `P3` und `P5` müssen aus vorherigen Schritten stammen
  ([[Formel 3]]–[[Formel 6]]), deren genaue Zuordnung im Fließtext nicht
  vollständig benannt ist; Vorstufe zu [[Formel 8]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Auf welcher Linie `P3` liegt, ist auf dieser Seite nicht ausdrücklich
    benannt (P3 wird nur hier und in Formel 8 erwähnt, nicht bei seiner
    Entstehung).

## Formel 8 – Taillierte hintere Mitte: Linienführung

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 8
- **Buchfassung:**
  ```text
  Die taillierte hintere Mitte von P2 über P7 nach P8 jeweils gerade bis zur
  Saumlinie zeichnen.
  ```
- **Technische Formel:**
  ```text
  taillierte_hM = Gerade(P2, P7, P8) bis Saumlinie
  ```
- **Eingaben und Einheiten:** Punkte `P2`, `P7`, `P8` (aus Formel 2 bzw.
  Formel 7 hergeleitet oder daraus benannt).
- **Ausgabe und Einheit:** Linienzug „taillierte hintere Mitte mit Naht"
  (geometrisch, keine eigene Maßeinheit).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – reine
  geometrische Verbindung.
- **Abhängigkeiten:** [[Formel 7]] (Herkunft von `P7`/`P8` nicht explizit
  benannt, vermutlich die in Formel 7 um 2 cm eingezogenen Punkte an `P5`
  bzw. `P3`, aber im Text nicht wörtlich so verknüpft).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Die Herleitung von `P7` und `P8` aus den Einzügen in Formel 7 ist
    plausibel, aber nicht wörtlich im Buchtext verknüpft.

## Formel 9 – Gerade hintere Mitte: Einzug an P6

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 9
- **Buchfassung:**
  ```text
  Alternativ kann für ein Oberteil ohne Naht an der hM die hM auch gerade
  gezeichnet werden. Hierzu von P6 an der Hüftlinie 2 cm nach links
  abtragen und
  ```
- **Technische Formel:**
  ```text
  einzug_P6 = 2 cm
  ```
- **Eingaben und Einheiten:** Punkt `P6` auf der Hüftlinie (Herkunft auf
  dieser Seite nicht benannt).
- **Ausgabe und Einheit:** neuer Punkt `P6a`, 2 cm links von `P6` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 2 cm ohne
  `ca.`; Alternative zur genähten Variante (Auswahl „ohne Naht an der hM").
- **Abhängigkeiten:** Alternative zu [[Formel 7]]/[[Formel 8]] (taillierte
  hM); Vorstufe zu [[Formel 10]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Herkunft von `P6` auf dieser Seite nicht benannt (vermutlich auf der in
    Formel 6 erzeugten Hüftlinie, aber nicht wörtlich verknüpft).

## Formel 10 – Gerade hintere Mitte: Linienführung über P6a

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 10
- **Buchfassung:**
  ```text
  die gerade hM von P2 über P6a in einer Geraden zeichnen.
  ```
- **Technische Formel:**
  ```text
  gerade_hM = Gerade(P2, P6a)
  ```
- **Eingaben und Einheiten:** Punkte `P2`, `P6a` (aus Formel 2 bzw. Formel 9).
- **Ausgabe und Einheit:** Linienzug „gerade hintere Mitte ohne Naht"
  (geometrisch, keine eigene Maßeinheit).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – reine
  geometrische Verbindung.
- **Abhängigkeiten:** [[Formel 9]]; Vorstufe zu [[Formel 11]] und
  [[Formel 12]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 11 – Gerade hM: Schnittpunkte P7/P8

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 11
- **Buchfassung:**
  ```text
  Es ergeben sich mit der geraden hM an der Taillenlinie und der Saumlinie
  die Schnittpunkte P7 und P8.
  ```
- **Technische Formel:**
  ```text
  P7_gerade = Schnitt(gerade_hM, Taillenlinie)
  P8_gerade = Schnitt(gerade_hM, Saumlinie)
  ```
- **Eingaben und Einheiten:** `gerade_hM` (aus Formel 10), Taillenlinie
  (Formel 5), Saumlinie (Formel 3).
- **Ausgabe und Einheit:** Punkte `P7`, `P8` der geraden hM-Variante
  (geometrisch).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – reine
  Schnittpunktbildung.
- **Abhängigkeiten:** [[Formel 10]], [[Formel 5]], [[Formel 3]]. Laut
  [`formeln_s179.md`](formeln_s179.md) (zeichnungsgebunden, `skizze_02`)
  sind diese Punkte in der Zeichnung farblich (rot) von den gleichnamigen
  `P7`/`P8` der taillierten hM ([[Formel 8]], dort dunkel) unterschieden –
  im Fließtext tragen beide Varianten dieselben Bezeichnungen.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Doppelbelegung der Punktnamen `P7`/`P8` für zwei geometrisch
    unterschiedliche Punkte (taillierte vs. gerade hM) laut s179.md keine
    OCR-Dopplung, sondern Original-Befund – für einen späteren Codevertrag
    müssten diese Punkte eindeutig unterschieden werden (z. B.
    `P7_taillierte_hM` / `P7_gerade_hM`).

## Formel 12 – Gemeinsamer Schnittpunkt an der Brustlinie

- **Quelle:** [`formeln_s179.md`](formeln_s179.md), Abschnitt 12
- **Buchfassung:**
  ```text
  An der Brustlinie ergeben sich für beide hM-Varianten jeweils ein eigener
  Schnittpunkte mit der jeweiligen hM. Der jeweilige Schnittpunkt dient als
  Ausgangspunkt für die weiteren Konstruktionsschnitte!
  ```
- **Technische Formel:**
  ```text
  P_brustlinie_taillierte_hM = Schnitt(taillierte_hM, Brustlinie)
  P_brustlinie_gerade_hM     = Schnitt(gerade_hM, Brustlinie)
  ```
- **Eingaben und Einheiten:** `taillierte_hM` (Formel 8), `gerade_hM`
  (Formel 10), Brustlinie (Formel 4).
- **Ausgabe und Einheit:** je ein Schnittpunkt pro hM-Variante an der
  Brustlinie (geometrisch); dient laut Buchtext als Ausgangspunkt weiterer,
  auf dieser Seite nicht enthaltener Konstruktionsschritte.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine eigene Rechnung
  – reine Schnittpunktbildung, je nach gewählter hM-Variante (Formel 8 oder
  Formel 9/10).
- **Abhängigkeiten:** [[Formel 8]], [[Formel 10]], [[Formel 4]]. Laut
  [`formeln_s179.md`](formeln_s179.md) (zeichnungsgebunden, `skizze_02`)
  trägt dieser Punkt in der Zeichnung die Nummer 9 (in beiden
  Farbvarianten) – im Fließtext nicht benannt. Ausgangspunkt für
  Konstruktionsschritte außerhalb dieser Seite (nicht Teil dieser
  Extraktion).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - OCR-Numerus-Fehler „ein eigener Schnittpunkte" (statt „Schnittpunkt")
    nicht am Original geprüft.
  - Die Benennung als „P9" stammt ausschließlich aus der Zeichnung, nicht
    aus dem Fließtext, und ist selbst noch nicht am Original bestätigt.
