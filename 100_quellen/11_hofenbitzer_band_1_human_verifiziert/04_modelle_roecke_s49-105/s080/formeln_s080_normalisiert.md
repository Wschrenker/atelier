# Formeln s080 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s080.md`](formeln_s080.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle vier Beziehungen
stehen deshalb auf `offen`. Dies ist ein Walking-Skeleton-Durchlauf, kein
Ersatz für die Bestätigung. Keine der vier Beziehungen enthält einen
Zahlenwert im Buchtext; es werden hier bewusst keine Defaultwerte oder
Schwellen ergänzt.

## Formel 1 – Faltenbruch-/Faltenanstoßlinie-Position

- **Quelle:** [`formeln_s080.md`](formeln_s080.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Der Abnäher der mittleren vorderen Teilungsnaht wird zur Öffnungsposition
  addiert und dort als Faltenbruch und Faltenanstoßlinie gezeichnet.
  ```
- **Technische Formel:**
  ```text
  position_faltenbruch = position_faltenanstosslinie
                        = position_oeffnung + betrag_abnaeher_mvtn
  ```
- **Eingaben und Einheiten:** `position_oeffnung` (Position der
  Bundfalten-Öffnung entlang der mittleren vorderen Teilungsnaht, cm oder
  Lineal-Position); `betrag_abnaeher_mvtn` (Abnäherbetrag der mittleren
  vorderen Teilungsnaht, cm).
- **Ausgabe und Einheit:** `position_faltenbruch` = `position_faltenanstosslinie`
  (cm bzw. Position), identische Linie unter zwei Namen im Buch.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – reine additive
  Beziehung ohne Zahlenwert oder Bereich im Buchtext.
- **Abhängigkeiten:** `betrag_abnaeher_mvtn` und `position_oeffnung` stammen
  aus dem 10-Bahnenrock-Grundschnitt („Modellentwicklung aus dem 10-Bahnenrock
  (13)", s080-Überschrift); genaue Quellseite auf s080 nicht benannt. Mögliche
  Verbindung zu [[Formel 4]] (dort verweist „wie im VT verschoben" vermutlich
  auf dieselbe Addition).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Herkunftsseite von `betrag_abnaeher_mvtn`/`position_oeffnung` (vermutlich
    Grundschnittseite des 10-Bahnenrocks) nicht ermittelt.
  - Ob die Addition als Streckenlänge auf derselben Linie oder als
    zweidimensionale Konstruktion gemeint ist, geht aus dem Wortlaut allein
    nicht eindeutig hervor; nur anhand der Zeichnung (□1/□2) zu klären.

## Formel 2 – Faltenlänge RT: Grenzwert bis knapp über die Hüftlinie

- **Quelle:** [`formeln_s080.md`](formeln_s080.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Am RT wird hier die Falte sehr lang bis knapp über die Hüftlinie
  abgenäht. Damit sitzt der Rock bis zur Hüfte sehr körperanliegend, da
  erst ab dort Weite hinzu kommt.
  ```
- **Technische Formel:**
  ```text
  ende_abgenaeht_RT ≈ position_hueftlinie - epsilon   (epsilon: "knapp", nicht quantifiziert)
  ```
- **Eingaben und Einheiten:** `position_hueftlinie` (Referenzlinie aus dem
  Grundschnitt, cm/Position); `epsilon` unbestimmt („knapp über").
- **Ausgabe und Einheit:** `ende_abgenaeht_RT` (cm/Position), oberes Ende der
  am RT abgenähten Falte.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „knapp über" bleibt
  unscharf – kein fester Wert oder Default laut Buch. Gilt ausdrücklich nur
  für den RT (Gegenstück zum VT, das laut Einleitung „direkt aus dem Bund
  aufspringen" kann, siehe „Nicht als Formel erfasst" in
  [`formeln_s080.md`](formeln_s080.md)).
- **Abhängigkeiten:** [[Formel 3]] (mögliche allgemeine Formulierung
  derselben oder einer verwandten Handlung, Verhältnis ungeklärt);
  `position_hueftlinie` ist eine Referenzlinie aus dem Grundschnitt, nicht auf
  s080 definiert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Distanz „knapp über" nicht quantifiziert; keine Schätzung als Formel
    ergänzt.

## Formel 3 – Faltenlänge allgemein: Grenzwert bis zum Falteninnenbruch

- **Quelle:** [`formeln_s080.md`](formeln_s080.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Den Nahtverlauf formen und die Falte bis zum Falteninnenbruch abnähen.
  ```
- **Technische Formel:**
  ```text
  ende_abgenaeht = position_falteninnenbruch
  ```
- **Eingaben und Einheiten:** `position_falteninnenbruch` (Konstruktionslinie
  der Falte, cm/Position; Herkunft vermutlich aus dem in Punkt 2 genannten
  Faltendach).
- **Ausgabe und Einheit:** `ende_abgenaeht` (cm/Position), Endpunkt der
  abgenähten Falte.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine – Bezug auf eine
  benannte Konstruktionslinie statt auf einen Zahlenwert.
- **Abhängigkeiten:** [[Formel 2]] – Verhältnis dieser allgemeinen Regel zur
  RT-spezifischen „bis knapp über die Hüftlinie"-Regel ist auf s080 nicht
  eindeutig geklärt (zwei Beschreibungen derselben Handlung oder zwei
  unterschiedliche Bezugslinien für VT/RT).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Verhältnis Punkt 4 (Formel 2) zu Punkt 5 (Formel 3) nicht eindeutig: gilt
    Punkt 5 zusätzlich, als Alternative, oder als generelle Nahtformung nach
    dem in Punkt 4 beschriebenen Grenzwert?

## Formel 4 – Abnäher RT: Auswahlregel für Verschiebung wie im VT

- **Quelle:** [`formeln_s080.md`](formeln_s080.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Der im RT verbleibende Abnäher wird dort genäht. Nur bei sehr kleinem
  Abnäher und wenn dieser für eine gute Passform entbehrlich ist, kann er
  wie im VT verschoben werden.
  ```
- **Technische Formel:**
  ```text
  WENN groesse(abnaeher_RT) sehr_klein
       UND entbehrlich_fuer_passform(abnaeher_RT)
  DANN abnaeher_RT verschieben (wie in Formel 1: addieren zur Öffnungsposition)
  SONST abnaeher_RT an Ort und Stelle nähen (Default)
  ```
- **Eingaben und Einheiten:** Größe des Abnähers RT (qualitativ, kein
  Zahlenwert); fachliche Einschätzung der Passform-Entbehrlichkeit
  (qualitativ).
- **Ausgabe und Einheit:** Konstruktionsentscheidung (kategorial): „genäht"
  vs. „verschoben wie im VT".
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „sehr klein" und „für
  eine gute Passform entbehrlich" sind fachliche Auswahlkriterien ohne
  Zahlenschwelle im Buchtext – keinen festen Schwellenwert ergänzen.
- **Abhängigkeiten:** [[Formel 1]] – „wie im VT verschoben" bezieht sich
  vermutlich auf die dort beschriebene additive Positionsbestimmung.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kein Schwellenwert für „sehr klein" im Buchtext angegeben; ob „wie im
    VT verschoben" tatsächlich identisch mit Formel 1 ist, nicht auf s080
    explizit bestätigt.
