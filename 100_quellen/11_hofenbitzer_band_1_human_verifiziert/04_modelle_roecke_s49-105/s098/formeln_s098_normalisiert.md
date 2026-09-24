# Formeln s098 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s098.md`](formeln_s098.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Beide Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Tascheneingriff-Verlängerung über die Seitennaht

- **Quelle:** [`formeln_s098.md`](formeln_s098.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Tascheneingriff formen und 0,5 cm über die Seitennaht verlangern, um mehr
  Eingriffweite zu bekommen.
  ```
- **Technische Formel:**
  ```text
  tascheneingriff_ende_neu = seitennaht_position + delta
  delta = 0,5 cm
  ```
- **Eingaben und Einheiten:** `seitennaht_position` (cm, Lage der Seitennaht
  am Tascheneingriff); `delta` = 0,5 cm.
- **Ausgabe und Einheit:** `tascheneingriff_ende_neu` (cm), verlängerte
  Eingriffskante des Swing-Pockets.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert „0,5 cm"
  ohne `ca.` – kein Spielraum laut Buchwortlaut. Zweck laut Buch: „um mehr
  Eingriffweite zu bekommen" (Folge, keine eigene Messgröße).
- **Abhängigkeiten:** keine weiteren Seiten- oder Formelverweise auf s098
  selbst.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nicht spezifiziert, ob die 0,5 cm nur am oberen oder auch am unteren Ende
    des Tascheneingriffs angesetzt werden, und auf welcher Teilkante
    (Vorderteil oder Taschenbeutel) gemessen wird.

## Formel 2 – Position und Grundform der hinteren Spatentasche

- **Quelle:** [`formeln_s098.md`](formeln_s098.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die hintere Spatentasche aus einem Quadrat zeichnen (Seite 363). Darauf
  achten, dass die Ta-sche nicht zu Klein gerät, da sie doppelt abgestept und
  die In-nengroße dadurch kleiner wird. Sie sollte zwischen hM und SN, aber
  etwas nähr zur Seiten-naht liegen (hier ist eine klass-sche Form gezeigt).
  ```
- **Technische Formel:**
  ```text
  spatentasche_grundform = quadrat(seite_363)
  position(spatentasche) ∈ [hM, SN], näher an SN als an hM
  ```
- **Eingaben und Einheiten:** Quadratmaß der Spatentasche – auf Seite 363
  definiert, hier nicht kopiert; Bezugslinien `hM` (hintere Mitte) und `SN`
  (Seitennaht) am Rückteil.
- **Ausgabe und Einheit:** Positionierte Spatentaschen-Grundform (Lage
  zwischen hM und SN, keine Maßangabe für den Abstand).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „zwischen hM
  und SN" bleibt Bereich, kein fester Abstand oder Default gewählt; Zusatz
  „etwas näher zur Seitennaht" ist eine qualitative Tendenzangabe ohne
  Zahlenwert. Bedingung: Tasche darf wegen doppelter Absteppung nicht zu klein
  ausfallen (Innengröße schrumpft durch die Absteppung).
- **Abhängigkeiten:** Quadratmaß und -konstruktion auf Seite 363 (nicht auf
  s098 selbst enthalten, nur verlinkt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Quadratmaß von Seite 363 nicht Teil dieser Extraktion; ohne diese Angabe
    ist die Formel nicht eigenständig auswertbar.
  - „Etwas näher zur Seitennaht" ist nicht quantifiziert (kein Abstand, kein
    Verhältnis).
