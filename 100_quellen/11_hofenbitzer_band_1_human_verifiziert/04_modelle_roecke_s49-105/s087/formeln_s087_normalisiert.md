# Formeln s087 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s087.md`](formeln_s087.md) vermerkt, ist mit
Ausnahme der Überschrift und der Variable `FaA_Ta` keine Stelle dieser Seite
von Werner am Original bestätigt. Alle drei Formeln stehen deshalb auf
`offen`, unabhängig von der inhaltlichen Klarheit der jeweiligen
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Faltenabstand an der Taille (Zielwert FaA_Ta)

- **Quelle:** [`formeln_s087.md`](formeln_s087.md), Abschnitt 1
- **Buchfassung:**
  ```text
  2 An der Taillenlinie die Faltenabstände auf den FaA., verringern.
  ```
- **Technische Formel:**
  ```text
  faltenabstand_taillenlinie = FaA_Ta
  ```
- **Eingaben und Einheiten:** `FaA_Ta` (cm) – Zielwert für den Faltenabstand
  an der Taillenlinie. Herkunft/Berechnung von `FaA_Ta` selbst ist auf dieser
  Seite nicht angegeben.
- **Ausgabe und Einheit:** `faltenabstand_taillenlinie` (cm), Abstand
  zwischen den Falten auf Höhe der Taillenlinie/Taillennaht.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Kein Bereich, sondern
  ein Zielwert („verringern auf"). Kein Rechenweg zu `FaA_Ta` im Buchtext
  dieser Seite angegeben.
- **Abhängigkeiten:** möglicher Bezug zu [[Formel 2]] (`FaA_HU`) als
  Ausgangswert vor der Reduzierung – im Buchtext auf dieser Seite jedoch
  nicht ausdrücklich verbunden, daher hier nicht als Rechenbeziehung
  angenommen.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nur Überschrift und Variablenname `FaA_Ta` sind von Werner am Original
    bestätigt, nicht der volle Satzwortlaut.
  - Wie `FaA_Ta` ermittelt wird (Maßtabelle, Konstruktionsregel oder Verweis
    auf eine andere Seite), ist auf s087 nicht angegeben.
  - Ob sich „verringern auf den FaA_Ta" auf jede einzelne Falte oder auf den
    Gesamtabstand über alle Falten bezieht, ist aus dem Wortlaut nicht
    eindeutig.

## Formel 2 – Faltenabstand an der Hüftlinie (Bezugsgröße FaA_HU)

- **Quelle:** [`formeln_s087.md`](formeln_s087.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Falten-
  abstand
  FaA_HU
  ```
- **Technische Formel:**
  ```text
  faltenabstand_hueftlinie = FaA_HU
  ```
- **Eingaben und Einheiten:** `FaA_HU` (cm) – benannte Bezugsgröße,
  ausschließlich aus der Zeichnung entnommen.
- **Ausgabe und Einheit:** `faltenabstand_hueftlinie` (cm), Abstand
  zwischen den Falten auf Höhe der Hüftlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – auf dieser
  Seite ist weder ein Zahlenwert noch eine Rechenvorschrift für `FaA_HU`
  angegeben.
- **Abhängigkeiten:** möglicher Bezug zu [[Formel 1]] (`FaA_Ta`); vermutlich
  ist `FaA_HU` der Ausgangsabstand auf Höhe der Hüftlinie, der zur Taille hin
  auf `FaA_Ta` reduziert wird. Diese Verbindung ist eine Vermutung aus der
  Zeichnungsanordnung, nicht durch Buchtext auf s087 belegt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Formel ist von Werner am Original bestätigt.
  - `FaA_HU` kommt im OCR-Fließtext von s087 nicht vor; unklar, ob die Größe
    auf einer anderen Seite hergeleitet oder definiert wird.
  - Der vermutete Zusammenhang zu `FaA_Ta` (Reduzierung von Hüfte zu Taille)
    ist nicht als Buchregel belegt und wird hier ausdrücklich nicht als
    Formel angenommen.

## Formel 3 – Nahtzugabe an der Taillennaht

- **Quelle:** [`formeln_s087.md`](formeln_s087.md), Abschnitt 3
- **Buchfassung:**
  ```text
  zunächst ca. 2 bis 3 cm NZg an der Taillennaht
  ```
- **Technische Formel:**
  ```text
  nzg_taillennaht ∈ [ca. 2 cm, ca. 3 cm]  (zunächst, vor Anprobe)
  ```
- **Eingaben und Einheiten:** keine externe Eingabe; Bereichsvorgabe direkt
  in der Zeichnung.
- **Ausgabe und Einheit:** `nzg_taillennaht` (cm), anfängliche Nahtzugabe an
  der Taillennaht.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „2 bis 3 cm"
  bleibt Bereich, kein fester Default gewählt. „zunächst" deutet auf eine
  spätere Anpassung bei der Anprobe hin (vergleiche OCR-Zeile 25: „Die
  endgültige Form entsteht bei Maßkleidung durch Abstecken bei der
  Anprobe."), ohne dass diese Seite die Anpassung selbst quantifiziert.
- **Abhängigkeiten:** thematischer Bezug zur allgemeinen Anprobe-Anweisung
  (OCR-Zeile 25 und Abschnitt „Anprobe", Zeilen 32–37), dort jedoch ohne
  eigene Zahl.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Formel ist von Werner am Original bestätigt.
  - Abkürzung „NZg" wird auf dieser Seite nicht aufgelöst.
  - Unklar, ob sich der Bereich auf jede Falte einzeln oder auf die gesamte
    Taillennaht bezieht.
