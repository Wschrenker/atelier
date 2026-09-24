# Formeln s182 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s182.md`](formeln_s182.md) vermerkt, ist nur die
Rechenbeispiel-Stelle in Formel 1 von Werner am Original bestätigt
(Kürzel `HüB`/`HüW`, Rechnung `47,3 − 50,5 = −3,2` und Halbierung auf `1,6`).
Auch bei Formel 1 bleibt die allgemeine Vorzeichen-/Richtungsregel
(„anstellen“ bei positivem vs. negativem HüFb) ungeklärt, deshalb steht auch
diese Formel auf `offen`. Die Formeln 2–6 sind vollständig unbestätigte
geometrische Beziehungen. Dies ist ein Walking-Skeleton-Durchlauf, kein
Ersatz für die Bestätigung.

## Formel 1 – Hüft-Fehlbetrag (HüFb)

- **Quelle:** [`formeln_s182.md`](formeln_s182.md), Abschnitt 1
- **Buchfassung:**
  ```text
  ☐ vHüB und hHüB messen und addieren = HÜB. Die ½ HüW aus der Konstruktionstabelle entnehmen und dort den Hüft-Fehlbetrag berechnen (siehe Tabelle rechts):

  gemessene HÜB | 47,3 | - ½ HÜW | 50,5 | = | -3,2

  Hüft-Fehlbetrag (HüFb)
  = HUB - ½ Huw
  = 47,3cm -50,5cm
  = -3,2cm → 3,2cm ½ = 1,6cm

  Von den Seitenlinien an der Hüfte den ½ Hüft-Fehlbetrag (hier 1,6 cm) anstellen und die neue Hüftlinie rechtwinklig zur hM zeichnen.
  ```
- **Technische Formel:**
  ```text
  HueB = vHueB + hHueB
  HueFb = HueB - (HueW / 2)
  anstellwert_je_seitenlinie = abs(HueFb) / 2
  ```
- **Eingaben und Einheiten:** `vHueB` (cm, vordere Hüftbreite gemessen),
  `hHueB` (cm, hintere Hüftbreite gemessen), `HueW` (cm, Hüftweite aus der
  Konstruktionstabelle, im Rechenbeispiel bereits als `½ HüW = 50,5` cm
  eingesetzt — ob `HueW` selbst oder schon `HueW/2` aus der Tabelle
  entnommen wird, ist aus dem Wortlaut nicht eindeutig, siehe unten).
- **Ausgabe und Einheit:** `HueFb` (cm, kann negativ sein);
  `anstellwert_je_seitenlinie` (cm, im Beispiel 1,6 cm), angetragen an
  vorderer und neuer hinterer Seitenlinie am Punkt „29“ (laut Zeichnung
  beidseitig gleich).
- **Bereiche, Bedingungen und Auswahlentscheidungen:**
  - Kein Bereich oder `ca.` im Buchtext dieser Stelle; die Werte 47,3 / 50,5 /
    −3,2 / 1,6 stehen als konkretes Rechenbeispiel, keine allgemeine
    Formvariable im Buch selbst benannt (Buchstaben `HÜB`/`HüW` sind Kürzel,
    keine mit Formvariablen deklarierten Größen).
  - Unklar, ob in der Konstruktionstabelle bereits `½ HüW` oder `HüW` steht
    (Buchtext nennt „Die ½ HüW aus der Konstruktionstabelle entnehmen“ –
    das spricht dafür, dass `½ HüW` direkt tabelliert ist).
  - Unklar, wie mit dem Vorzeichen von `HueFb` bei der Anstellrichtung
    umzugehen ist, wenn `HueFb` positiv statt negativ wäre (im vorliegenden
    Beispiel ist `HueFb` negativ und wird laut Zeichnung an beiden
    Seitenlinien nach innen angestellt/eingenommen – die allgemeine Regel für
    den positiven Fall steht nicht auf dieser Seite).
- **Abhängigkeiten:** `HueW`/`½ HueW` stammt aus einer Konstruktionstabelle,
  die nicht auf s182 selbst liegt (laut `s182_skizze_03.png` soll sie auf dem
  VT-Musterteil „hier aufkleben“ – Quellseite der Tabelle nicht ermittelt).
  Der halbierte Betrag fließt in die geometrische Beziehung „neue Hüftlinie
  rechtwinklig zur hM“ (Formel 5) ein.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nur das konkrete Zahlenbeispiel (47,3 / 50,5 / −3,2 / 1,6) ist von Werner
    bestätigt, nicht die allgemeine Formel oder Vorzeichenregel.
  - Ob `HueW` oder bereits `HueW/2` aus der Konstruktionstabelle kommt, ist
    unklar.
  - Anstellrichtung bei positivem `HueFb` ist auf dieser Seite nicht
    geregelt.
  - OCR-Schreibweisen „HUB“/„Huw“ uneinheitlich groß-/kleingeschrieben,
    unverändert übernommen.

## Formel 2 – Vorderes Armloch

- **Quelle:** [`formeln_s182.md`](formeln_s182.md), Abschnitt 2
- **Buchfassung:**
  ```text
  ☐6b Das vordere Armloch vom vSuP zur SN formen. Dabei verläuft die Kurve in der Regel seitlich am vAP vorbei.
  ```
- **Technische Formel:**
  ```text
  armloch_vorne = kurve(von=vSuP, bis=SN, ueber_naehe_von=vAP)
  ```
- **Eingaben und Einheiten:** Punkte `vSuP`, `SN`, `vAP` (Lage in der
  Konstruktion, keine eigenen Maßzahlen auf dieser Seite).
- **Ausgabe und Einheit:** Kurvenverlauf des vorderen Armlochs (Geometrie,
  keine Länge/Einheit benannt).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „in der Regel“ –
  fachlicher Spielraum, keine feste Passregel; kein Zahlenwert für den
  Abstand zu `vAP`.
- **Abhängigkeiten:** Punktlage von `vSuP`, `vAP` aus vorhergehenden
  Konstruktionsschritten (nicht auf s182 selbst hergeleitet).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - „in der Regel seitlich … vorbei“ ist keine geometrisch eindeutige Regel.

## Formel 3 – Hinteres Armloch

- **Quelle:** [`formeln_s182.md`](formeln_s182.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Das hintere Armloch vom hSuP über P17 und hAP zur SN formen. zu den Schulternähten verlaufen die Armlöcher nahezu rechtwinklig.
  ```
- **Technische Formel:**
  ```text
  armloch_hinten = kurve(von=hSuP, ueber=[P17, hAP], bis=SN)
  winkel(armloch_hinten, schulternaht) ≈ 90°  (nahezu rechtwinklig)
  ```
- **Eingaben und Einheiten:** Punkte `hSuP`, `P17`, `hAP`, `SN` (Lage, keine
  Maßzahlen auf dieser Seite).
- **Ausgabe und Einheit:** Kurvenverlauf des hinteren Armlochs; Näherungswinkel
  zur Schulternaht (≈ 90°, keine exakte Gradzahl im Buch).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „nahezu rechtwinklig“
  bleibt Näherung, kein fester Gradwert gewählt.
- **Abhängigkeiten:** [[Formel 2]] (beide bilden zusammen das Armloch,
  Schritt „7 Armlöcher zeichnen“); Punktlage `hSuP`, `P17`
  (Schulterblattlinie), `hAP` aus vorhergehenden Konstruktionsschritten.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kleinschreibung „zu den Schulternähten“ nach Satzpunkt am Original zu
    prüfen (siehe [s182.md](s182.md), Prüfstelle 6).

## Formel 4 – Neue Seitenlinie am RT

- **Quelle:** [`formeln_s182.md`](formeln_s182.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Am RT die neue Seitenlinie parallel zur geraden hM zeichnen.
  ```
- **Technische Formel:**
  ```text
  neue_seitenlinie_RT ∥ hM
  ```
- **Eingaben und Einheiten:** Referenzlinie `hM` (hintere Mitte, gerade).
- **Ausgabe und Einheit:** `neue_seitenlinie_RT` (Geometrie, Parallelitätsbedingung, keine eigene Maßzahl).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Feste geometrische
  Bedingung (parallel), kein Zahlenwert, kein Spielraum laut Wortlaut.
- **Abhängigkeiten:** Ausgangspunkt der neuen Seitenlinie ist Punkt „27“ in
  der Zeichnung; hängt am Ergebnis von Formel 1 (Anstellwert an der Hüfte),
  da die Seitenlinie dort durch den neuen Punkt „29“ läuft.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 5 – Neue Hüftlinie

- **Quelle:** [`formeln_s182.md`](formeln_s182.md), Abschnitt 5
- **Buchfassung:**
  ```text
  und die neue Hüftlinie rechtwinklig zur hM zeichnen.
  ```
- **Technische Formel:**
  ```text
  neue_hueftlinie ⟂ hM
  ```
- **Eingaben und Einheiten:** Referenzlinie `hM`; Lage über den
  Anstellpunkten „29“ (Ergebnis von Formel 1).
- **Ausgabe und Einheit:** `neue_hueftlinie` (Geometrie, Rechtwinkligkeitsbedingung).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Feste geometrische
  Bedingung (rechtwinklig), kein Zahlenwert.
- **Abhängigkeiten:** [[Formel 1]] (Anstellwert 1,6 cm bestimmt die Lage der
  Linie an den Seitenlinien, Punkt „30“ in der Zeichnung).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Der zugrundeliegende Anstellwert (Formel 1) ist nur als konkretes
    Beispiel bestätigt, die allgemeine Formel nicht.

## Formel 6 – Seitennähte, Saum und neue Quer-Linien

- **Quelle:** [`formeln_s182.md`](formeln_s182.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Die Seitennähte gerade vom Armloch über die Anstellungen an der Hüfte zum Saum zeichnen.
  Die neue Brust-, Taillen und Saumlinie jeweils rechtwinklig zur hM auf die Schnittpunkte mit der neuen Seitennaht zeichnen.
  ```
- **Technische Formel:**
  ```text
  seitennaht = gerade(von=armloch_punkt, ueber=hueft_anstellpunkt, bis=saum_punkt)
  neue_brustlinie   ⟂ hM   (bis Schnittpunkt mit seitennaht)
  neue_taillenlinie ⟂ hM   (bis Schnittpunkt mit seitennaht)
  neue_saumlinie    ⟂ hM   (bis Schnittpunkt mit seitennaht)
  ```
- **Eingaben und Einheiten:** Referenzlinie `hM`; Punkte des Armlochs
  (Formeln 2–3), Hüft-Anstellpunkte „29“ (Formel 1), Ausgangslinien Brust-,
  Taillen- und Saumlinie (keine eigenen Maßzahlen auf dieser Seite).
- **Ausgabe und Einheit:** Neue Seitennaht sowie neue Brust-, Taillen- und
  Saumlinie (Geometrie, keine Länge/Einheit benannt); Schnittpunkte an den
  vier mit „32“ markierten Stellen in der Zeichnung.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Feste geometrische
  Bedingungen (gerade Linie, rechtwinklig), kein Zahlenwert, kein Spielraum
  laut Wortlaut.
- **Abhängigkeiten:** [[Formel 1]] (Hüft-Anstellpunkte), [[Formel 2]],
  [[Formel 3]] (Armlochpunkte als Startpunkt der Seitennaht).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Lage der ursprünglichen (alten) Brust-, Taillen- und Saumlinie, auf die
    sich „neue … Linie“ bezieht, ist nicht Teil dieser Seite und daher nicht
    referenzierbar.
