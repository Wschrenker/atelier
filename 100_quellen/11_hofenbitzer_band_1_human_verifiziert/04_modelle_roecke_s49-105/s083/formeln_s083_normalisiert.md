# Formeln s083 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s083.md`](formeln_s083.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle drei Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Falteninhalt einer Kellerfalte

- **Quelle:** [`formeln_s083.md`](formeln_s083.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Bei einer Kellerfalte beträgt der Falteninhalt die 4-fache Faltentiefe.
  ```
- **Technische Formel:**
  ```text
  faltentiefe_gesamt = 4 * faltentiefe
  ```
- **Eingaben und Einheiten:** `faltentiefe` (cm), frei gewählte Eingabegröße
  laut Buchtext Zeile 15 („gewünschter … Faltentiefe“) – kein fester Wert auf
  dieser Seite.
- **Ausgabe und Einheit:** `faltentiefe_gesamt` (cm), im Buch „Falteninhalt“,
  in der Zeichnung mit `FaI` beschriftet.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Bereich, kein
  `ca.` – fester Faktor „4-fache“ laut Buchwortlaut. `faltentiefe` selbst
  bleibt frei wählbar (siehe Eingaben).
- **Abhängigkeiten:** [[Formel 2]] (gleiche Bezugsgröße `faltentiefe` auf
  derselben Seite, andere Anwendung an der Faltenboden-Naht).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Die Zeichnung zeigt vier `FaT`-Segmente mit `FaI`-Gesamtspanne nur beim
    VT-Teil; ob dieselbe 4-fache Beziehung auch bei den RT-Teilstücken
    (sRT, Faltenboden, hRT) gilt, ist auf dieser Seite nicht mit einer
    eigenen `FaI`-Beschriftung belegt (dort jeweils nur einzelne
    `FaT`-Segmente sichtbar).
  - „gewündlicher Faltenhöhe“ in Zeile 15 ist eine erkannte OCR-Verlesung von
    „gewünschter“ (siehe s083.md); am Original nicht bestätigt.

## Formel 2 – Teilungslinie für die Faltenboden-Naht

- **Quelle:** [`formeln_s083.md`](formeln_s083.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die Teilung für eine Naht erfolgt immer an der Faltentiefe.
  ```
- **Technische Formel:**
  ```text
  position_teilungslinie = faltentiefe  (gemessen ab Faltenkante)
  ```
- **Eingaben und Einheiten:** `faltentiefe` (cm), dieselbe Eingabegröße wie in
  [[Formel 1]].
- **Ausgabe und Einheit:** `position_teilungslinie` (cm), Lage der
  Trennlinie zwischen Hauptteil und separatem Faltenboden.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „immer“ laut Buchtext –
  keine Ausnahme oder Bereich angegeben. Bezugspunkt („ab Faltenkante“) ist in
  der technischen Formel ergänzt, im Buchwortlaut nicht explizit benannt.
- **Abhängigkeiten:** [[Formel 1]] (gemeinsame Eingabegröße `faltentiefe`);
  gilt nur für die Variante mit separatem Faltenboden (RT), siehe [[Formel 3]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Der genaue Bezugspunkt der Teilung (ab Faltenkante, ab Teilungsnaht o. ä.)
    ist aus dem Buchwortlaut nicht eindeutig, nur aus der Zeichnungslage der
    einzelnen `FaT`-Segmente erschlossen.

## Formel 3 – Schnittteilanzahl je Variante

- **Quelle:** [`formeln_s083.md`](formeln_s083.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Das VT wird in einem Schnittteil, das RT wird in drei Schnittteilen
  zugeschnitten.
  ```
- **Technische Formel:**
  ```text
  anzahl_schnittteile(VT) = 1
  anzahl_schnittteile(RT) = 3   // sRT + Faltenboden + hRT
  ```
- **Eingaben und Einheiten:** Teiltyp (`VT` oder `RT`) als Auswahl, keine
  Maßeinheit.
- **Ausgabe und Einheit:** Anzahl Schnittteile (dimensionslos, Stück).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** feste Werte laut
  Buchtext für die auf dieser Seite gezeigte Faltenboden-Variante des RT;
  keine Bereichsangabe. Gilt ausdrücklich für die im Buchtext beschriebene
  Zuschnittvariante mit separatem Faltenboden.
- **Abhängigkeiten:** [[Formel 2]] (die Teilung, die die drei RT-Schnittteile
  erzeugt); Zeichnungsbeschriftungen `1× OSt` (VT), `2×-p OSt` (sRT), `2x OSt`
  (Faltenboden), `1× OSt` (hRT) in `skizzen/s083_skizze_02.png` als
  zeichnungsgebundener Beleg, nicht weiter gedeutet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Die Bedeutung der Stückzahl-Kürzel `2×-p OSt` und `2x OSt` (z. B. „im
    Stoffbruch“, „paarig“) ist auf dieser Seite nicht erläutert und wurde
    nicht gedeutet.
