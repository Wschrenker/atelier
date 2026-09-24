# Formeln s071 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s071.md`](formeln_s071.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle Regeln stehen
deshalb auf `offen`. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für
die Bestätigung.

## Formel 1 – Eckbehandlung an der Taillennaht

- **Quelle:** [`formeln_s071.md`](formeln_s071.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Sollen die Glocken direkt aus der Taille fallen, verbleibt die Ecke an der
  Taillennnaht.
  2 Durfen die Glocken welcher ab unterhalb der Taille fallen, wird die Ecke
  an der Taillennah ausgerundet.
  ```
- **Technische Formel:**
  ```text
  wenn fall_charakter == "direkt_aus_taille":
      ecke_taillennaht = unbehandelt  # Ecke bleibt spitz/erhalten
  sonst wenn fall_charakter == "weicher_unterhalb_taille":
      ecke_taillennaht = ausgerundet
  ```
- **Eingaben und Einheiten:** `fall_charakter` – kategoriale fachliche
  Auswahl (kein Maß, keine Einheit), zwei Ausprägungen laut Buchtext.
- **Ausgabe und Einheit:** `ecke_taillennaht` – kategoriales Konstruktions-
  ergebnis (unbehandelt vs. ausgerundet), kein Zahlenwert.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Binäre Auswahl je nach
  gewünschtem gestalterischem Effekt. Der Radius bzw. das Ausmaß der
  Ausrundung im Fall „ausgerundet" wird auf dieser Seite nicht beziffert.
- **Abhängigkeiten:** Bezieht sich auf dieselbe Taillennaht-Ecke wie die
  Saumerweiterungs-Konstruktion dieser Seite; keine Verlinkung zu anderen
  Seiten, da im Buchtext keine Quellenangabe vorhanden ist.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Die Punktnummer „2" ist laut [s071.md](s071.md) vermutlich ein OCR-Fehler
    (Foto zeigt vermutlich ⑤); am Original zu prüfen.
  - Kein Maß für den Ausrundungsradius im Fall „ausgerundet" angegeben.

## Formel 2 – Saumrundungen als Kreisbögen

- **Quelle:** [`formeln_s071.md`](formeln_s071.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die Saumrundungen können als Kreisbögen gezeichnet werden.
  ```
- **Technische Formel:**
  ```text
  saumrundung_kurve = kreisbogen(radius=?, mittelpunkt=?)
  ```
- **Eingaben und Einheiten:** Kein Radius, kein Mittelpunkt und keine sonstige
  Bemaßung im Buchtext angegeben.
- **Ausgabe und Einheit:** `saumrundung_kurve` – Kurventyp „Kreisbogen", keine
  Maßeinheit auf dieser Seite.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „können ... gezeichnet
  werden" – als Empfehlung/Konstruktionsmöglichkeit formuliert, kein
  verpflichtendes Verfahren laut Wortlaut.
- **Abhängigkeiten:** Betrifft dieselben Nähte wie Formel 3 (Saumkürzung
  wegen Schrägfadenlauf).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Radius/Mittelpunkt der Kreisbögen sind nicht spezifiziert; vermutlich aus
    der Zeichnung zu entnehmen (Skizzenausschnitte noch nicht extrahiert).

## Formel 3 – Saumkürzung an den Teilungsnähten

- **Quelle:** [`formeln_s071.md`](formeln_s071.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Wegen des schrägen Fadenlaufs der Nähte wird sich dort der Stoff, je nach
  Beschaffenheit, mehr oder weniger stark ausdehnen.
  3 Der Saum kann daher an den Teilungsnähten leicht gekürzt werden.
  ```
- **Technische Formel:**
  ```text
  saum_neu = saum_alt - delta_klein
  delta_klein = unspezifiziert  # "leicht", materialabhängig
  ```
- **Eingaben und Einheiten:** `saum_alt` (cm, Saumlänge an der jeweiligen
  Teilungsnaht); `delta_klein` ohne Zahlenwert, abhängig von der
  „Beschaffenheit" des Stoffs (Dehnverhalten im Schrägschnitt).
- **Ausgabe und Einheit:** `saum_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Kein fester Wert oder
  Bereich im Buchtext – ausdrücklich materialabhängige fachliche Auswahl
  („je nach Beschaffenheit mehr oder weniger stark"). Kein Default zu wählen.
- **Abhängigkeiten:** [[Formel 2]] (gleiche Nähte, gleicher Konstruktions-
  schritt: Kreisbogen zeichnen, dann ggf. kürzen).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kein Zahlenwert oder Bereich für „leicht gekürzt" angegeben; nicht
    plausibel zu ergänzen.
  - Die Punktnummer „3" ist laut [s071.md](s071.md) vermutlich ein OCR-Fehler
    (Foto zeigt vermutlich ⑥); am Original zu prüfen.

## Nicht normalisiert

Die in [`formeln_s071.md`](formeln_s071.md) unter „Nicht als Formel erfasst"
aufgeführten Stellen (Saumweiten-Verteilung auf 10 Nähte ohne Rechenwert,
allgemeiner Symmetriehinweis, Bild-/Teileverweise, nicht transkribierte
Zeichnungslabels wie „1/20 Saumerweiterung") werden hier nicht normalisiert,
da sie keine im Buchtext belegte Rechenbeziehung enthalten oder noch nicht aus
einer bestätigten Quelle vorliegen.
