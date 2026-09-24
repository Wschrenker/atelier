# Formeln s190 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s190.md`](formeln_s190.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle sieben Formeln
stehen deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Hinterer Saum rechtwinklig zur hM

- **Quelle:** [`formeln_s190.md`](formeln_s190.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Der hintere Saum wird immer rechtwinklig zur hM gezeichnet.
  ```
- **Technische Formel:**
  ```text
  winkel(hinterer_saum, hM) = 90°
  ```
- **Eingaben und Einheiten:** Referenzlinie `hM` (hintere Mitte).
- **Ausgabe und Einheit:** Ausrichtung des hinteren Saums, Winkel in Grad
  (90° zur hM).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert „immer“ –
  kein Spielraum, kein `ca.` laut Buchwortlaut.
- **Abhängigkeiten:** setzt `hM` als bereits konstruierte Referenzlinie
  voraus (Grundkonstruktion vermutlich auf einer früheren Seite dieses
  Kapitels, hier nicht benannt – nur zu verlinken, sobald bekannt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unklar, ob diese Anweisung zur ersten der vier blauen Kreiszahlen gehört
    oder zu einer anderen (siehe Prüfstelle 2 in `s190.md`).

## Formel 2 – Hintere Seitennaht unterhalb der Hüfte parallel zur hM

- **Quelle:** [`formeln_s190.md`](formeln_s190.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Unterhalb der Hüfte verläuft eine verlangerte hintere Seitennaht parallel
  zur hinteren Mitte.
  ```
- **Technische Formel:**
  ```text
  für Bereich unterhalb(Hüftlinie): richtung(hintere_seitennaht) ∥ hM
  ```
- **Eingaben und Einheiten:** Referenz `Hüftlinie` (Bereichsgrenze),
  Referenzrichtung `hM`.
- **Ausgabe und Einheit:** Verlauf/Richtung der hinteren Seitennaht unterhalb
  der Hüftlinie (parallel zu `hM`).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Gültigkeitsbereich
  „unterhalb der Hüfte“ – die Hüftlinie selbst ist auf dieser Seite nicht mit
  einem Zahlenwert definiert.
- **Abhängigkeiten:** Hüftlinien-Definition vermutlich auf einer anderen
  Seite der Grundkonstruktion (nicht kopiert, nur zu verlinken, sobald
  bekannt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - OCR-Schreibweise „verlangerte“ (vermutlich „verlängerte“) nicht geprüft.
  - Bezugsseite für „Hüfte“/Hüftlinie nicht ermittelt.

## Formel 3 – Seitennähte auf gleiche Länge

- **Quelle:** [`formeln_s190.md`](formeln_s190.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Die Seitennahte werden auf die gleiche Länge gebracht.
  ```
- **Technische Formel:**
  ```text
  länge(hintere_seitennaht) = länge(vordere_seitennaht)
  ```
- **Eingaben und Einheiten:** Länge der hinteren Seitennaht (cm), Länge der
  vorderen Seitennaht (cm), jeweils vor Angleichung.
- **Ausgabe und Einheit:** angeglichene Seitennahtlänge (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine numerische
  Toleranz im Buchtext genannt; welche Seite an welche angepasst wird, ist
  nicht spezifiziert.
- **Abhängigkeiten:** [[Formel 1]] und [[Formel 2]] (gleicher
  Saumverlauf-Abschnitt, gleiche Schnittteile).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Referenzrichtung der Angleichung (welche Naht wird an welche angepasst)
    nicht eindeutig.
  - OCR-Schreibweise „Seitennahte“ (vermutlich „Seitennähte“) nicht geprüft.

## Formel 4 – Vorderer Saum an der vM verlängert

- **Quelle:** [`formeln_s190.md`](formeln_s190.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Den vorderen Saum an der vM um 0,5 cm verlangern und wie skizziert formen.
  ```
- **Technische Formel:**
  ```text
  saum_vorne_neu = saum_vorne_alt + 0,5 cm   (an Punkt vM)
  ```
- **Eingaben und Einheiten:** `saum_vorne_alt` (cm) an vM.
- **Ausgabe und Einheit:** `saum_vorne_neu` (cm); zusätzliche Formgebung laut
  Zeichnung (nicht quantifiziert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 0,5 cm,
  kein `ca.`. Der Zusatz „wie skizziert formen“ verlangt eine Kurvenform aus
  der Zeichnung, die hier nicht in Zahlen vorliegt.
- **Abhängigkeiten:** Formkurve aus `skizzen/s190_skizze_02.png` (☐5-Bereich);
  visuelle Abhängigkeit, nicht in dieser Formel quantifiziert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Genaue Kurvenform „wie skizziert“ nicht aus dem Text ableitbar.
  - OCR-Schreibweise „verlangern“ (vermutlich „verlängern“) nicht geprüft.

## Formel 5 – Brustabnäher-Bezugsmaß BrU:20 (zeichnungsgebunden)

- **Quelle:** [`formeln_s190.md`](formeln_s190.md), Abschnitt 5
- **Buchfassung:**
  ```text
  BrU:20 – 1 bis + 1 cm
  ```
- **Technische Formel:**
  ```text
  maß = BrU / 20 + delta
  delta ∈ [-1 cm, +1 cm]
  ```
- **Eingaben und Einheiten:** `BrU` (Brustumfang, vermutlich cm) – Herkunft
  und genaue Definition auf dieser Seite nicht vorhanden.
- **Ausgabe und Einheit:** `maß` (cm); welche Strecke am Schnittteil damit
  gemeint ist (z. B. Abnäherbreite oder -tiefe), ist ohne Bildprüfung nicht
  gesichert.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „-1 bis +1 cm“
  um `BrU/20` bleibt Bereich, kein fester Wert gewählt.
- **Abhängigkeiten:** `BrU` als Körpermaß vermutlich aus einer
  Grundmaßtabelle außerhalb dieser Seite (nicht kopiert, nur zu verlinken,
  sobald bekannt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Notation „BrU:20“ als Division interpretiert – am Original zu prüfen.
  - Bedeutung der Ausgabegröße (welche Strecke) nicht gesichert.
  - Zusammenhang mit der benachbarten, isoliert erfassten Angabe „ca. 1 cm“
    ungeklärt (siehe `formeln_s190.md`, „Nicht als Formel erfasst“).

## Formel 6 – Zweites Schnittteil, Bezug „wie seitlich“ (zeichnungsgebunden)

- **Quelle:** [`formeln_s190.md`](formeln_s190.md), Abschnitt 6
- **Buchfassung:**
  ```text
  wie seitlich + 0,5 cm
  ```
- **Technische Formel:**
  ```text
  wert_neu = wert_seitlich + 0,5 cm
  ```
- **Eingaben und Einheiten:** `wert_seitlich` (cm) – Bezugsgröße, vermutlich
  von der entsprechenden Seitennaht-Konstruktion übernommen.
- **Ausgabe und Einheit:** `wert_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Zuschlag
  0,5 cm, kein `ca.`.
- **Abhängigkeiten:** möglicher Bezug zu [[Formel 4]] (gleicher Zuschlag
  0,5 cm wie beim vorderen Saum) – nicht gesichert. Laut `ocr_s190.md` Zeile
  11 sind die Rückteile beider Varianten identisch; ob das den Bezug
  „seitlich“ hier erklärt, ist offen.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Referenzgröße „seitlich“ (welche Naht, welcher Punkt) nicht eindeutig
    benannt.
  - Zusammenhang mit Formel 4 nicht am Original bestätigt.

## Formel 7 – Modelllänge frei wählbar

- **Quelle:** [`formeln_s190.md`](formeln_s190.md), Abschnitt 7
- **Buchfassung:**
  ```text
  Die Modelllänge kann jeweils beliebig gewählt werden.
  ```
- **Technische Formel:**
  ```text
  modelllänge = frei wählbarer Parameter (kein berechneter Wert)
  ```
- **Eingaben und Einheiten:** keine (externer Nutzerparameter, cm).
- **Ausgabe und Einheit:** `modelllänge` (cm), von außen vorgegeben.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Einschränkung im
  Buchtext genannt.
- **Abhängigkeiten:** wirkt sich vermutlich auf den „4 Saumverlauf“-Abschnitt
  aus, in dem „der Schnitt auf die benötigte Länge gebracht“ wird (siehe
  `ocr_s190.md`, Zeile 25) – [[Formel 1]] ff.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
