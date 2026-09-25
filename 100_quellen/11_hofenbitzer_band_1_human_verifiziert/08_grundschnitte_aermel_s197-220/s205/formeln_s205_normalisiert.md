# Formeln s205 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s205.md`](formeln_s205.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der Buchfassung.
Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung. Diese
Datei erzeugt keine Python-Funktion, keinen Engine-Vertrag und keine neue
Fachregel.

## F1 – Abstand vÄP–Brustlinie, nach oben abgetragen

- **Quelle:** [`formeln_s205.md`](formeln_s205.md), Abschnitt 1.
- **Buchfassung:**
  ```text
  2 ☐ 2 Den Abstand vom vÄP zur Brustlinie messen und
  ☐ 4 diesen Abstand (+ ¼ ArD+) am Ärmel von der Ärmelkugellinie nach oben abtragen.
  ```
- **Technische Formel:**
  ```text
  d1 = Abstand(vÄP, Brustlinie)                 # gemessen
  Variante A (OCR "+"): d_oben = d1 + ¼·ArD+
  Variante B (Foto "="): d1 = ¼·ArD+  (d1 wäre dann kein freies Messmaß, sondern durch ArD+ festgelegt)
  ```
- **Eingaben und Einheiten:** `d1` (cm, gemessener Abstand vÄP–Brustlinie); `ArD+` (cm, Maß aus einem anderen Kontext, auf dieser Seite nicht definiert).
- **Ausgabe und Einheit:** `d_oben` bzw. `d1` (cm), Abstand auf der Ärmelkugellinie nach oben.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; Rechenzeichen bestimmt die gesamte Formelstruktur (Addition vs. Gleichsetzung).
- **Abhängigkeiten:** `ArD+` nicht auf s205 definiert (vermutlich Vorseite oder Maßtabelle) — nicht ermittelt, nicht erfunden. Ausgangswert für F2, vermutlich auch für die ½/½-1cm-Konstruktion in F6 (unbestätigt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Rechenzeichen „+" (OCR) vs. „=" (Foto laut [s205.md](s205.md) Prüfstelle 5) ist ein echter inhaltlicher Widerspruch, keine reine Lesehilfe — bestimmt, ob `d1` und `¼ArD+` addiert oder gleichgesetzt werden.
  - Herkunft und Definition von `ArD+` unbekannt.

## F2 – Hintere Mitte – Abstand + 0,5 cm ab P3

- **Quelle:** [`formeln_s205.md`](formeln_s205.md), Abschnitt 2.
- **Buchfassung:**
  ```text
  3 Denselben Abstand + 0,5 cm an der hinteren Mitte von P3 nach unten abtragen.
  ```
- **Technische Formel:**
  ```text
  d_unten = d1 + 0,5 cm     # "denselben Abstand" = d1 aus F1, ab P3 nach unten
  ```
- **Eingaben und Einheiten:** `d1` (cm, aus F1).
- **Ausgabe und Einheit:** `d_unten` (cm), Abstand ab P3 nach unten an der hinteren Mitte.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Zuschlag „+ 0,5 cm", kein Bereich.
- **Abhängigkeiten:** F1 → F2. `P3` auf dieser Seite nicht definiert (vermutlich Vorseite).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Erbt die Unsicherheit aus F1 (welcher Wert genau „derselbe Abstand" ist).
  - `P3` nicht auf s205 definiert; Herkunft nicht ermittelt.

## F3 – üb = 2,7 cm

- **Quelle:** [`formeln_s205.md`](formeln_s205.md), Abschnitt 3.
- **Buchfassung:**
  ```text
  üb = 2,7 cm
  ```
- **Technische Formel:** `üb = 2,7 cm` (Beispielwert, nicht als allgemeine Formel erkennbar).
- **Eingaben und Einheiten:** keine erkennbare Eingabegröße auf dieser Seite; `üb` wirkt wie eine feste Bemaßung an vÄP auf der vorderen Linie.
- **Ausgabe und Einheit:** `üb` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine erkennbar.
- **Abhängigkeiten:** Eingabe für F4. Möglicher, aber unbestätigter Zusammenhang mit F1/F2 (gleicher Bereich der Zeichnung, keine textliche Verknüpfung belegt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Bedeutung von „üb" (vermutlich Abkürzung, z. B. „Überstand" o. ä.) nicht erläutert.
  - Ob `üb` mit dem in F1 gemessenen Abstand identisch ist, ist nicht belegt.

## F4 – üb + 0,5 cm = 3,2 cm

- **Quelle:** [`formeln_s205.md`](formeln_s205.md), Abschnitte 4 und 5.
- **Buchfassung:**
  ```text
  üb + 0,5 cm
  2,7 cm + 0,5 cm
  = 3,2 cm
  ```
  ```text
  0,5 cm
  ```
- **Technische Formel:** `wert4 = üb + 0,5 cm`.
- **Eingaben und Einheiten:** `üb` (cm, aus F3); Zuschlag `0,5 cm`.
- **Ausgabe und Einheit:** `wert4` (cm), Bemaßung am oberen Eckpunkt der „hintere Linie".
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Zuschlag, kein Bereich.
- **Abhängigkeiten:** F3 → F4.
- **Status:** offen. Rechenbeispiel unabhängig geprüft: `2,7 + 0,5 = 3,2` — stimmt mit der gedruckten Angabe überein.
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Geometrische Rolle von `wert4` (was genau von wo bis wo gemessen wird) nur aus der Zeichnungsposition erschlossen, nicht aus Fließtext belegt.

## F5 – ½ / ½ – 1 cm – Streckenlabels (Konvergenzpunkt ⑨)

- **Quelle:** [`formeln_s205.md`](formeln_s205.md), Abschnitt 6.
- **Buchfassung:**
  ```text
  ½
  ½ - 1 cm
  ```
- **Technische Formel:** nicht ableitbar — Bezugsgröße („das Ganze", von dem ½ bzw. ½ − 1 cm genommen wird) auf dieser Seite nicht benannt.
- **Eingaben und Einheiten:** unbekannt.
- **Ausgabe und Einheit:** unbekannt; vermutlich zwei bis vier Hilfspunkte zur Konstruktion des Konvergenzpunkts (Kreiszahl ⑨) bzw. eines Punkts auf ÄkLi.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine ableitbar.
- **Abhängigkeiten:** möglicher, aber unbestätigter Zusammenhang mit Maßen der Vorseite 204 (dort laut [s205.md](s205.md) u. a. „hAlU 13,8 cm", „hAP", „hAchsel 8,5 cm" sichtbar) — nicht kopiert, nur als offener Verdacht vermerkt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Bezugsgröße vollständig unklar; keine Rechenregel ableitbar, ohne eine Größe zu erfinden.

## F6 – vAchsel kopieren und einfügen → P10 = tP

- **Quelle:** [`formeln_s205.md`](formeln_s205.md), Abschnitt 7.
- **Buchfassung:**
  ```text
  ☐ 5 Die vÄchsel kopieren, am vÄP anlegen, so dass das Ende auf die um 0,5 cm erhöhte Ärmelkugellinie zu liegen kommt → P10 = tP.
  ```
- **Technische Formel:**
  ```text
  Ärmelkugellinie_erhöht = Ärmelkugellinie + 0,5 cm   # senkrechter Versatz
  vAchsel_kopie = Kopie(vAchsel), angelegt an vÄP
  P10 = Endpunkt(vAchsel_kopie) ∩ Ärmelkugellinie_erhöht
  tP := P10
  ```
- **Eingaben und Einheiten:** `vAchsel` (Kurve/Kontur, Herkunft nicht auf s205 definiert, laut Zeichnungslabel „kopieren und einfügen"); `Ärmelkugellinie` (Linie aus vorherigem Konstruktionsschritt); Zuschlag `0,5 cm`.
- **Ausgabe und Einheit:** Punkt `P10` = `tP` (Koordinate, cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Zuschlag `0,5 cm`, keine Bereichsangabe.
- **Abhängigkeiten:** Herkunft von `vAchsel` nicht auf s205 definiert (vermutlich Vorseite/anderer Schnittteil). `tP` ist Eingabe für F7 und F8.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Herkunft und genaue Form von `vAchsel` nicht ermittelt.

## F7 – Kurvenkonstruktion obere Ärmelkugel (oÄk)

- **Quelle:** [`formeln_s205.md`](formeln_s205.md), Abschnitt 9.
- **Buchfassung:**
  ```text
  ca. 1,2 cm
  ca. 1 cm
  ```
- **Technische Formel:** nicht ableitbar — die beiden `ca.`-Werte sind Bemaßungspfeile an der gezeichneten Kurve (vermutlich Kontrollabstand der Kurve von einer Hilfslinie/Diagonale), keine Rechenoperation im Buchtext angegeben.
- **Eingaben und Einheiten:** unbekannt; die Bezugslinie, von der `ca. 1,2 cm` bzw. `ca. 1 cm` gemessen werden, ist nur zeichnungsgebunden erkennbar (gestrichelte Diagonale im Bildausschnitt), nicht textlich benannt.
- **Ausgabe und Einheit:** Kurvenverlauf oÄk (cm-Bemaßung als Kontrollwert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` erhalten — kein fester Wert laut Buch.
- **Abhängigkeiten:** Kurve beginnt/endet an Punkten aus F6 und aus der Zeichnung (vÄP-Kopie, rechte obere Ecke). Nicht abschließend geklärt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob die beiden Werte als Tangenten-/Kurvenkontrollabstand einer Bézier-ähnlichen Konstruktion zu lesen sind, ist eine zeichnungsgebundene Interpretation, keine Buchregel.

## F8 – Kurvenkonstruktion untere Ärmelkugel (uÄk)

- **Quelle:** [`formeln_s205.md`](formeln_s205.md), Abschnitt 10.
- **Buchfassung:**
  ```text
  ca. ½
  ```
- **Technische Formel:** nicht ableitbar — Bezugsgröße für „ca. ½" nicht benannt.
- **Eingaben und Einheiten:** unbekannt.
- **Ausgabe und Einheit:** Kurvenverlauf uÄk (cm-Bemaßung als Kontrollwert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` erhalten.
- **Abhängigkeiten:** [[F6]] (Kurve beginnt bei tP); Bezugsgröße evtl. dieselbe wie in F5, nicht bestätigt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Bezugsgröße vollständig unklar.

## F9 – 0,5 cm – Abstand tP zu ÄkLi

- **Quelle:** [`formeln_s205.md`](formeln_s205.md), Abschnitt 8.
- **Buchfassung:**
  ```text
  0,5 cm
  ```
- **Technische Formel:** `Abstand(tP, ÄkLi) = 0,5 cm` (konsistent mit F6: `Ärmelkugellinie_erhöht = ÄkLi + 0,5 cm`).
- **Eingaben und Einheiten:** `ÄkLi` (Linie); Zuschlag `0,5 cm`.
- **Ausgabe und Einheit:** Lage von `tP` relativ zu `ÄkLi` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert, kein Bereich.
- **Abhängigkeiten:** [[F6]] — vermutlich derselbe Zuschlag, zweimal dargestellt (einmal an der Konstruktion in Zeichnung 1, einmal an tP in Zeichnung 2).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob dies exakt derselbe 0,5-cm-Zuschlag wie in F6/F4 ist oder eine eigenständige Bemaßung, ist aus der Bildposition plausibel, aber nicht textlich belegt.
