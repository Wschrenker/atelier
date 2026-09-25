# Formeln s212 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s212.md`](formeln_s212.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt, und alle Stellen stammen
aus direkter Bildlesung der Skizzenausschnitte statt aus OCR-Text (auf s212
lieferte die OCR keinen brauchbaren Text). Alle Formeln stehen deshalb auf
`offen`, unabhängig von der inhaltlichen Klarheit der Buchfassung. Dies ist ein
Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung.

## Formel 1 – Ärmelpunkte neu bestimmen (Vertiefung)

- **Quelle:** [`formeln_s212.md`](formeln_s212.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Ärmelpunkte neu bestimmen:
  um ¾ der Armlochvertiefung die Punkte nach unten versetzen
  ```
- **Technische Formel:**
  ```text
  punkt_y_neu = punkt_y_alt + (3/4) * armlochvertiefung
  ```
  (Vorzeichen/Richtung „nach unten" abhängig vom verwendeten
  Koordinatensystem; hier als Betrag notiert.)
- **Eingaben und Einheiten:** `punkt_y_alt` (cm), Position der betroffenen
  Ärmelpunkte; `armlochvertiefung` (cm), auf dieser Seite nicht selbst
  beziffert – Bezugsgröße vermutlich aus einer früheren Seite (Titel verweist
  „ab Seite 191").
- **Ausgabe und Einheit:** `punkt_y_neu` (cm), neue Position der Ärmelpunkte.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Faktor „¾" ohne
  `ca.` – kein Spielraum laut Buchwortlaut für den Faktor selbst; die
  Eingangsgröße `armlochvertiefung` bleibt aber unbeziffert.
- **Abhängigkeiten:** [[Formel 3]] (Bereich „½ bis ganze
  Armloch-Vertiefung", möglicherweise dieselbe Bezugsgröße
  `armlochvertiefung`); Ursprung der Armlochvertiefung liegt auf einer
  früheren, nicht verlinkten Seite (ab Seite 191 laut Einleitungstext).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Welche konkreten Punkte („Ärmelpunkte") betroffen sind (vÄP, hÄP oder
    andere) ist im Bildausschnitt nicht eindeutig einem Punktnamen
    zugeordnet.
  - Herkunft und Wert von `armlochvertiefung` liegt nicht auf s212.

## Formel 2 – Armloch-Verbreiterung = vordere + hintere Verbreiterung

- **Quelle:** [`formeln_s212.md`](formeln_s212.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Armloch-Verbreiterung = vordere + hintere Verbreiterung
  ```
  mit den benachbarten, nicht explizit zugeordneten Bruchangaben „1/3" und
  „2/3".
- **Technische Formel:**
  ```text
  armloch_verbreiterung_gesamt = armloch_verbreiterung_vorne + armloch_verbreiterung_hinten
  ```
- **Eingaben und Einheiten:** `armloch_verbreiterung_vorne` (cm),
  `armloch_verbreiterung_hinten` (cm).
- **Ausgabe und Einheit:** `armloch_verbreiterung_gesamt` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Default-Aufteilung
  gewählt. Die im Bild sichtbaren Angaben „1/3" (VT-Seite) und „2/3"
  (RT-Seite) legen nahe, dass `armloch_verbreiterung_vorne` = 1/3 und
  `armloch_verbreiterung_hinten` = 2/3 der Gesamtverbreiterung sein könnten,
  dies steht aber nicht als Fließtext im Bild und wird hier **nicht** als
  feste Regel übernommen.
- **Abhängigkeiten:** [[Formel 7]] (nutzt vermutlich dieselbe Gesamtgröße als
  „die ganze Armlochverbreiterung" bzw. „½ Armloch-Verbreiterung" im
  Ärmelgrundschnitt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Zuordnung von „1/3"/„2/3" zu vorderer/hinterer Verbreiterung ungeklärt
    (siehe auch Prüfstelle 2, s212.md).

## Formel 3 – Bereich „½ bis ganze Armloch-Vertiefung"

- **Quelle:** [`formeln_s212.md`](formeln_s212.md), Abschnitt 3
- **Buchfassung:**
  ```text
  ½ bis ganze Armloch-Vertiefung
  ```
- **Technische Formel:**
  ```text
  verschiebung ∈ [0,5 * armlochvertiefung, 1,0 * armlochvertiefung]
  ```
- **Eingaben und Einheiten:** `armlochvertiefung` (cm), auf s212 nicht
  beziffert.
- **Ausgabe und Einheit:** `verschiebung` (cm), Bereich ohne festen Wert.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „½ bis ganze"
  bleibt Bereich; kein Default gewählt. Kein Buchtext auf dieser Seite
  erklärt, wovon die konkrete Wahl innerhalb des Bereichs abhängt.
- **Abhängigkeiten:** [[Formel 1]] (gleiche Bezugsgröße
  `armlochvertiefung`); [[Formel 7]] (Punkt 1 links in
  `s212_skizze_02.png` verweist über einen Pfeil auf denselben Bereich).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kein erklärender Fließtext im Bildausschnitt gefunden, der die Wahl
    innerhalb des Bereichs begründet.

## Formel 4 – Beschriftung „1 cm"

- **Quelle:** [`formeln_s212.md`](formeln_s212.md), Abschnitt 4
- **Buchfassung:**
  ```text
  1 cm
  ```
- **Technische Formel:**
  ```text
  delta = 1 cm
  ```
  (Anwendung/Richtung unbekannt.)
- **Eingaben und Einheiten:** keine erkennbar – isoliertes Maß.
- **Ausgabe und Einheit:** unbekannt.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Bereich, fester
  Wert „1 cm", aber ohne erkennbaren Bezug.
- **Abhängigkeiten:** möglicherweise zu [[Formel 1]] (vÄP-Verschiebung), da
  räumlich benachbart – nicht belegt.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ohne begleitenden Fließtext ist unklar, ob „1 cm" überhaupt eine
    eigenständige Rechenbeziehung ist oder nur eine Maßlinienbeschriftung
    ohne Formelcharakter; Status deshalb `gesperrt` statt `offen`.

## Formel 5 – ½ Taillenweite

- **Quelle:** [`formeln_s212.md`](formeln_s212.md), Abschnitt 5
- **Buchfassung:**
  ```text
  ½ Taillenweite messen
  ½ TaW = 44,6
  ```
- **Technische Formel:**
  ```text
  halbe_taillenweite = taillenweite / 2
  ```
- **Eingaben und Einheiten:** `taillenweite` (cm), Körper-/Modellmaß.
- **Ausgabe und Einheit:** `halbe_taillenweite` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – Halbierung ist
  fest.
- **Abhängigkeiten:** keine erkennbare Abhängigkeit zu anderen Formeln dieser
  Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nachrechnung des Beispiels: 44,6 * 2 = 89,2 cm für `taillenweite` – intern
    konsistent mit der Formel `halbe_taillenweite = taillenweite / 2`, aber
    kein Beleg für den Wert 89,2 cm selbst, da dieser auf s212 nicht
    ausgeschrieben steht.
  - Nur beim RT-Teil mit Zahlenwert versehen, beim VT-Teil nicht – Grund
    unklar.

## Formel 6 – ½ Hüftweite

- **Quelle:** [`formeln_s212.md`](formeln_s212.md), Abschnitt 6
- **Buchfassung:**
  ```text
  ½ Hüftweite messen
  ½ HüW = 56,1
  ```
- **Technische Formel:**
  ```text
  halbe_hueftweite = hueftweite / 2
  ```
- **Eingaben und Einheiten:** `hueftweite` (cm), Körper-/Modellmaß.
- **Ausgabe und Einheit:** `halbe_hueftweite` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – Halbierung ist
  fest.
- **Abhängigkeiten:** keine erkennbare Abhängigkeit zu anderen Formeln dieser
  Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nachrechnung des Beispiels: 56,1 * 2 = 112,2 cm für `hueftweite` – intern
    konsistent mit der Formel `halbe_hueftweite = hueftweite / 2`, aber kein
    Beleg für den Wert 112,2 cm selbst, da dieser auf s212 nicht
    ausgeschrieben steht.
  - Nur beim RT-Teil mit Zahlenwert versehen, beim VT-Teil nicht – Grund
    unklar.

## Formel 7 – Ärmelgrundschnitt – neue ÄkLi (Kugellinie)

- **Quelle:** [`formeln_s212.md`](formeln_s212.md), Abschnitt 7
- **Buchfassung:**
  ```text
  ½ Armloch-Verbreiterung
  die ganze Armlochverbreiterung
  wie vorne
  ```
- **Technische Formel:**
  ```text
  punkt2_verschiebung = 0,5 * armloch_verbreiterung_gesamt
  punkt3_verschiebung = 1,0 * armloch_verbreiterung_gesamt
  punkt1_rechts = wie_punkt1_links  (Regel "wie vorne", nicht auf s212 definiert)
  ```
- **Eingaben und Einheiten:** `armloch_verbreiterung_gesamt` (cm), siehe
  [[Formel 2]].
- **Ausgabe und Einheit:** neue Positionen der Punkte 1 (links/rechts), 2 und
  3 entlang der Linie „neue ÄkLi" (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Bereiche –
  Punkt 2 erhält die Hälfte, Punkt 3 die volle Armloch-Verbreiterung laut
  Buchbeschriftung. Richtung/Achse der Verschiebung nicht auf dieser Seite
  spezifiziert.
- **Abhängigkeiten:** [[Formel 2]] (`armloch_verbreiterung_gesamt`);
  [[Formel 3]] (Punkt 1 links nutzt laut Pfeil den Bereich „½ bis ganze
  Armloch-Vertiefung"); die Regel „wie vorne" für Punkt 1 rechts verweist auf
  eine frühere, nicht auf s212 vorliegende Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Referenzseite für „wie vorne" nicht ermittelt.
  - Ob Punkt 2 und Punkt 3 auf derselben Achse wie Punkt 1 liegen oder eine
    eigene geometrische Konstruktion benötigen, ist aus der Beschriftung
    allein nicht eindeutig.
