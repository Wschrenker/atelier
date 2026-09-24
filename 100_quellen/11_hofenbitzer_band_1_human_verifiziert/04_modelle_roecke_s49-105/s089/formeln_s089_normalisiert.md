# Formeln s089 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s089.md`](formeln_s089.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Halber Falteninhalt an VT und RT (Markierung)

- **Quelle:** [`formeln_s089.md`](formeln_s089.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Am VT und am RT jeweils einen halben Falteninhalt (± FaT) in entsprechender
  Höhe anzeichnen → Falteninnennaht.
  ```
- **Technische Formel:**
  ```text
  markierung_VT_RT = 0,5 * FaI
  markierung_VT_RT ≙ FaT
  ```
- **Eingaben und Einheiten:** `FaI` (Falteninhalt, cm) – auf dieser Seite nicht
  selbst definiert, nur verwendet.
- **Ausgabe und Einheit:** Markierungspunkt „in entsprechender Höhe" an VT und
  RT für die Falteninnennaht (cm-Position, Bezugslinie nicht spezifiziert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Kein Zahlenwert für
  `FaI` selbst auf dieser Seite; nur die Halbierungsbeziehung. Zeichen „±"
  (OCR) vs. vermutlich „≙" (Original) nicht bereinigt – siehe offene Fragen.
- **Abhängigkeiten:** [[Formel 2]] (gleiche Beziehung, angewendet auf das
  separate Faltenteil-Bauteil statt auf VT/RT); `FaI`-Definition selbst liegt
  vermutlich auf einer anderen Seite (nicht ermittelt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob am Original „≙" (Entsprechungszeichen) oder tatsächlich „±" steht, ist
    ungeklärt (s089.md vermutet einen OCR-Fehler).
  - „Entsprechende Höhe" ist keine quantifizierte Bezugsgröße.

## Formel 2 – Beginn des Faltenteils mit halbem Falteninhalt

- **Quelle:** [`formeln_s089.md`](formeln_s089.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Am Faltenteil mit der anderen Hälfte des Falteninhalts = Faltentiefe (FaT)
  beginnen → Falteninnennaht.
  Das erste Faltensegment ansetzen.
  ```
- **Technische Formel:**
  ```text
  segment_1_breite = 0,5 * FaI
  segment_1_breite = FaT
  ```
- **Eingaben und Einheiten:** `FaI` (cm), siehe Formel 1.
- **Ausgabe und Einheit:** Startbreite des ersten Faltensegments am
  Faltenteil (cm), zugleich Ausgangspunkt für die Falteninnennaht.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Hier steht im
  Buchtext ein Gleichheitszeichen „=", kein „±"/„≙" wie in Formel 1 – beide
  Schreibweisen nebeneinander stehen lassen, nicht vereinheitlichen.
- **Abhängigkeiten:** [[Formel 1]] (gleiche Halbierungsbeziehung); [[Formel 3]]
  (Fortsetzung nach dem ersten Segment).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Verhältnis der unterschiedlichen Zeichen „±"/„≙" (Formel 1) zu „="
    (Formel 2) für dieselbe fachliche Beziehung ungeklärt.

## Formel 3 – Ganzer Falteninhalt je Folgesegment

- **Quelle:** [`formeln_s089.md`](formeln_s089.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Daran einen ganzen Falteninhalt zeichnen.

  So fortfahren, bis alle Faltensegmente angesetzt sind.
  ```
- **Technische Formel:**
  ```text
  segment_n_breite = FaI   (für n = 2 … letztes Folgesegment)
  ```
- **Eingaben und Einheiten:** `FaI` (cm).
- **Ausgabe und Einheit:** Breite jedes Folgesegments nach dem ersten
  Halbsegment (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Anzahl der
  Faltensegmente ist auf dieser Seite nicht als Zahl oder Formel angegeben,
  nur als Wiederholungsanweisung „bis alle … angesetzt sind". Die Zeichnung
  zeigt zusätzlich ein Zwischenmaß „FaA" zwischen den FaI-Segmenten, dessen
  Bedeutung hier nicht erklärt wird – kein Wert oder Fachregel dafür
  angenommen.
- **Abhängigkeiten:** [[Formel 2]] (erstes Segment); [[Formel 4]] (Abschluss);
  [[Formel 5]] (Randbedingung Stoffbreite, die die tatsächliche Segmentzahl
  begrenzen dürfte, aber hier nicht verrechnet wird).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Bedeutung von „FaA" (Zeichnung) nicht auf dieser Seite erklärt.
  - Anzahl der Faltensegmente nicht quantifiziert.

## Formel 4 – Abschluss des Faltenteils mit halbem Falteninhalt

- **Quelle:** [`formeln_s089.md`](formeln_s089.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Das Faltenteil nach dem letzten Faltensegment wieder mit einem halben
  Falteninhalt = Faltentiefe (FaT) beenden → Falteninnennaht.
  ```
- **Technische Formel:**
  ```text
  segment_letzte_breite = 0,5 * FaI
  segment_letzte_breite = FaT
  ```
- **Eingaben und Einheiten:** `FaI` (cm).
- **Ausgabe und Einheit:** Breite des abschließenden Halbsegments am
  Faltenteil (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Symmetrisch zu Formel 2
  (gleiche Halbierung, gleiches Gleichheitszeichen „=" im Buchtext).
- **Abhängigkeiten:** [[Formel 2]] (spiegelbildliches Gegenstück am Anfang);
  [[Formel 3]] (vorausgehende Folgesegmente).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 5 – Randbedingung: vorhandene Stoffbreite (nur zeichnungsgebunden)

- **Quelle:** [`formeln_s089.md`](formeln_s089.md), Abschnitt 5
  (zeichnungsgebunden, keine Textquelle auf dieser Seite)
- **Buchfassung:**
  ```text
  Faltenteil 2×-p OSt
  vorhandene Stoffbreite 92 cm
  ```
- **Technische Formel:**
  ```text
  breite_gesamt(Faltenteil) <= 92 cm
  ```
  wobei `breite_gesamt` sich aus den Segmentbreiten der Formeln 2–4 ergeben
  dürfte; die genaue Summenbildung (Anzahl Folgesegmente, Rolle von „FaA")
  ist hier nicht belegt und wird nicht ergänzt.
- **Eingaben und Einheiten:** Segmentbreiten aus Formel 2–4 (cm, nicht
  vollständig quantifiziert).
- **Ausgabe und Einheit:** Obergrenze der Gesamtbreite des zusammengesetzten
  Faltenteils, 92 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Fester Zahlenwert „92
  cm" ohne „ca." im Bildzitat; ob dies eine harte Grenze oder nur die Angabe
  der tatsächlich verwendeten Stoffbahn ist, bleibt offen.
- **Abhängigkeiten:** [[Formel 2]], [[Formel 3]], [[Formel 4]] (Summanden der
  Gesamtbreite).
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ausschließlich zeichnungsgebundener Beleg, keine Textquelle auf s089.
  - Keine Formel für die Gesamtbreite aus dem Buch selbst ableitbar; die hier
    gezeigte Ungleichung ist eine Randbedingung aus der Beschriftung, keine
    vom Buch angegebene Rechenformel – deshalb `gesperrt` statt `offen`.
