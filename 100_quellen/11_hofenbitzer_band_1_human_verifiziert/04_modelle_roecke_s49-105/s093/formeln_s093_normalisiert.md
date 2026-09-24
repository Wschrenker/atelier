# Formeln s093 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s093.md`](formeln_s093.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle sieben Formeln
stehen deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Doppelter Schlitz-Einschlag an Seitennähten

- **Quelle:** [`formeln_s093.md`](formeln_s093.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Wird das Rockfutter bzw. ein Futterrock aus einer geraden oder ausgestellten
  Rockform gearbeitet, sollte für mehr Schrittweite zusätzlich ein offener
  Schlitz in die Seitennähte gearbeitet werden. Der doppelte Schlitz-Einschlag
  wird z.B. mit 2 × 2 cm angezeichnet.
  ```
- **Technische Formel:**
  ```text
  schlitz_einschlag_je_seite ≈ 2 cm  (Beispielwert, „z.B.")
  schlitz_einschlag_gesamt   = 2 × schlitz_einschlag_je_seite ≈ 4 cm
  ```
- **Eingaben und Einheiten:** keine – Wert ist ein im Buch genanntes Beispiel,
  kein aus anderen Größen abgeleiteter Wert.
- **Ausgabe und Einheit:** `schlitz_einschlag_je_seite` (cm), `schlitz_einschlag_gesamt` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** gilt nur, wenn ein
  Schlitz in die Seitennaht für mehr Schrittweite gearbeitet wird (gerade oder
  ausgestellte Rockform). „z.B." erhalten – kein fester Pflichtwert.
- **Abhängigkeiten:** möglicher Zusammenhang mit [[Formel 6]] (2 cm + 2 cm an
  der Seitennaht in der Produktionsschnitt-Zeichnung ☐7), da dieselbe
  Seitenschlitz-Konstruktion dort beispielhaft ausgeführt scheint. Nicht als
  Beweis verwendet – nur als Beobachtung dokumentiert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob sich „doppelter Schlitz-Einschlag" auf zwei Einschläge à 2 cm oder auf
    einen Gesamteinschlag von 2 cm handelt, ist aus „2 × 2 cm" nicht restlos
    eindeutig; hier als zwei Einschläge à 2 cm gelesen.
  - Verweis auf Seite 32, 46 (Rockformen) nicht aufgelöst.

## Formel 2 – RV-Schlitz-Nahtverschiebung nach innen

- **Quelle:** [`formeln_s093.md`](formeln_s093.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Am RV-Schlitz die Naht um 0,5 cm nach innen verschieben.
  ```
- **Technische Formel:**
  ```text
  position_naht_neu = position_naht_alt - 0,5 cm  (Richtung: nach innen)
  ```
- **Eingaben und Einheiten:** `position_naht_alt` (cm), Nahtlinie am RV-Schlitz.
- **Ausgabe und Einheit:** `position_naht_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 0,5 cm, kein
  „ca." in der Zeichnung (anders als die wortgleiche Formulierung mit „ca."
  auf [[s059]] und [[s092]], siehe Abhängigkeiten).
- **Abhängigkeiten:** wortgleiche Verschiebung „0,5 cm nach innen" bereits
  dokumentiert für die linke Seitennaht auf
  [`../s059/formeln_s059.md`](../s059/formeln_s059.md) (Formel 3, dort „ca. 0,5 cm")
  und für hM auf
  [`../s092/formeln_s092.md`](../s092/formeln_s092.md) (Formel 3, dort ebenfalls
  „ca. 0,5 cm") – nur verlinkt, nicht kopiert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Zeichnung nennt „0,5 cm" ohne „ca.", während s059 und s092 denselben Wert
    im Fließtext mit „ca." nennen – am Original zu prüfen, ob dies ein
    bewusster Unterschied oder eine Auslassung ist.
  - Bezugsrichtung „nach innen" nicht geometrisch präzisiert (bezogen worauf).

## Formel 3 – RV-Schlitz-Nahtzugabe

- **Quelle:** [`formeln_s093.md`](formeln_s093.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Hier kommt 1 cm Nahtzugabe hinzu.
  ```
- **Technische Formel:**
  ```text
  naht_mit_zugabe = naht_ohne_zugabe + 1 cm
  ```
- **Eingaben und Einheiten:** `naht_ohne_zugabe` (cm), Nahtlinie am RV-Schlitz
  nach der Verschiebung aus [[Formel 2]].
- **Ausgabe und Einheit:** `naht_mit_zugabe` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 1 cm, kein
  Bereich.
- **Abhängigkeiten:** [[Formel 2]] (gleiche Nahtlinie, gleiche Bildstelle);
  vergleichbare 1-cm-Nahtzugabe am RV-Schlitz bereits dokumentiert in
  [`../s092/formeln_s092.md`](../s092/formeln_s092.md) (Formel 4) – nur
  verlinkt, nicht kopiert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 4 – Schlitzende an der SN nach unten verschieben

- **Quelle:** [`formeln_s093.md`](formeln_s093.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Das Schlitzende für den RV an der SN um ca. 2 bis 3 cm nach unten verschieben
  ```
- **Technische Formel:**
  ```text
  position_schlitzende_neu = position_schlitzende_alt - delta  (Richtung: nach unten)
  delta ∈ [ca. 2 cm, ca. 3 cm]
  ```
- **Eingaben und Einheiten:** `position_schlitzende_alt` (cm), Lage des
  Schlitzendes an der Seitennaht.
- **Ausgabe und Einheit:** `position_schlitzende_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „2 bis 3 cm"
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** vergleichbare „ca. 2 bis 3 cm"-Verlängerung/-Verschiebung
  am Schlitzende bereits dokumentiert in
  [`../s059/formeln_s059.md`](../s059/formeln_s059.md) (Formel 4, dort
  „verlängert" statt „nach unten verschoben") und in
  [`../s092/formeln_s092.md`](../s092/formeln_s092.md) (Formel 5, dort ebenfalls
  „verlangern") – nur verlinkt, nicht kopiert; ob „nach unten verschieben" und
  „verlängern" dieselbe geometrische Operation meinen, ist hier nicht
  entschieden.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Zwei blaue Schrittkreise `4` (links und rechts) für dieselbe Textangabe –
    unklar, ob beide Seiten des Schlitzes identisch um denselben Betrag
    verschoben werden oder ob je Seite ein eigener Wert innerhalb des Bereichs
    gewählt wird.

## Formel 5 – NZg-Unterschied rechtes RT-Futter

- **Quelle:** [`formeln_s093.md`](formeln_s093.md), Abschnitt 5
- **Buchfassung:**
  ```text
  linkes RT-Futter
  1× Fu
  (rechtes RT-Futter ohne verschobene SN und mit 2 cn NZg)
  ```
- **Technische Formel:**
  ```text
  rechtes_RT_Futter.seitennaht_verschoben = false
  rechtes_RT_Futter.nzg_seitennaht = 2 cm  (Druckform „2 cn")
  linkes_RT_Futter.seitennaht_verschoben  = true  (siehe Formel 2)
  ```
- **Eingaben und Einheiten:** keine – Bauteilbeschriftung, kein
  Rechenschritt aus anderen Größen.
- **Ausgabe und Einheit:** Nahtzugabe `nzg_seitennaht` (cm) am rechten
  RT-Futter.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** gilt nur für das
  rechte RT-Futter (asymmetrisch zum linken, wegen des einseitigen
  RV-Schlitzes an der linken Seitennaht, vgl. OCR-Zeile 34).
- **Abhängigkeiten:** [[Formel 2]] (die dort beschriebene Nahtverschiebung
  betrifft nur die linke Seite; die rechte Seite erhält stattdessen die
  Nahtzugabe aus dieser Formel).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Druckschreibweise „2 cn" statt vermutlich „2 cm" – am Original zu prüfen,
    ob es sich um einen Druck- oder OCR-naher Lesefehler handelt (Fototreue:
    Ausschnitt zeigt gedruckten Text, kein OCR-Artefakt).

## Formel 6 – Seitennaht-Zugabe 2 cm + 2 cm

- **Quelle:** [`formeln_s093.md`](formeln_s093.md), Abschnitt 6
- **Buchfassung:**
  ```text
  2 cm   2 cm
  ```
- **Technische Formel:**
  ```text
  nzg_links_der_naht  = 2 cm
  nzg_rechts_der_naht = 2 cm
  ```
- **Eingaben und Einheiten:** keine – Maßangabe direkt in der Zeichnung.
- **Ausgabe und Einheit:** Nahtzugabe (cm) je Seite der Seitennaht, an drei
  Stellen der Produktionsschnitt-Zeichnung.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert 2 cm je
  Seite, kein Bereich.
- **Abhängigkeiten:** möglicher Zusammenhang mit [[Formel 1]] (Beispielwert
  „2 × 2 cm" im Fließtext) – nicht als Beweis verwendet, nur als Beobachtung.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Widerspruch zur bisherigen Zählung in [s093.md](s093.md) (dort nur zwei
    Schrittkreise `6`, im Bild aber drei gleich beschriftete Stellen mit
    „2 cm 2 cm" und Kreis `6` erkennbar) – am Original zu klären, hier nicht
    aufgelöst.

## Formel 7 – Saumzugabe am unteren Rand

- **Quelle:** [`formeln_s093.md`](formeln_s093.md), Abschnitt 7
- **Buchfassung:**
  ```text
  2 bis 4 cm
  1 bis 4 cm
  ```
- **Technische Formel:**
  ```text
  saumzugabe_aussen ∈ [2 cm, 4 cm]
  saumzugabe_innen  ∈ [1 cm, 4 cm]
  ```
- **Eingaben und Einheiten:** keine – Maßangabe direkt in der Zeichnung, an
  drei Stellen des unteren Saumrands wiederholt.
- **Ausgabe und Einheit:** Saumzugabe (cm), zwei gestaffelte Bereiche je
  Saumstelle.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** beide Bereiche bleiben
  Bereiche, kein fester Default gewählt; Bedeutung der beiden gestaffelten
  Maße (z. B. Umschlag vs. Ansteppzugabe) aus der Zeichnung allein nicht
  eindeutig.
- **Abhängigkeiten:** keine auf dieser Seite ermittelt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Fachliche Bedeutung der beiden gestaffelten Bereiche (2–4 cm und 1–4 cm)
    an derselben Saumstelle nicht geklärt.
