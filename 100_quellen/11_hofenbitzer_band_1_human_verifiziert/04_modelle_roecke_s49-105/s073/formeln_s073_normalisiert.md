# Formeln s073 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s073.md`](formeln_s073.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle vier Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung.

## Formel 1 – Drehpunkt der Teile-Öffnung

- **Quelle:** [`formeln_s073.md`](formeln_s073.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Die Teile des Bahnenrocks werden zwischen den Teilungsnähten sehr weit
  geöffnet. Der Drehpunkt ist an der Taillennaht.
  ```
- **Technische Formel:**
  ```text
  rotationszentrum = punkt_auf(taillennaht)
  teile_geoeffnet  = spreizen(bahnenrock_teile, zentrum=rotationszentrum,
                               trennlinien=teilungsnaehte)
  ```
  Keine Rechengröße, nur geometrische Bedingung: Die Öffnung erfolgt als
  Drehung/Spreizung der Rockteile um einen Punkt auf der Taillennaht, die
  Spreizung nimmt zum Saum hin zu.
- **Eingaben und Einheiten:** Rockteile des Bahnenrocks (Ausgangsschnitt);
  Teilungsnähte als Trennlinien; kein Zahlenwert.
- **Ausgabe und Einheit:** geöffnete (gespreizte) Rockteile mit
  kegelförmiger Öffnung, Spitze am Drehpunkt auf der Taillennaht.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „sehr weit" – keine
  Zahl, kein Bereich im Buchtext angegeben.
- **Abhängigkeiten:** [[Formel 2]] (Öffnungsverhältnis Seitennaht zu
  Teilungsnähten setzt auf dieser Spreizoperation auf); [[Formel 3]]
  (Zielgeometrie Viertelkreis).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Exakte Position des Drehpunkts auf der Taillennaht (Anfang, Mitte o. Ä.)
    nicht spezifiziert.
  - „sehr weit" nicht quantifiziert.

## Formel 2 – Öffnungsbetrag-Verhältnis Seitennaht zu Teilungsnähten

- **Quelle:** [`formeln_s073.md`](formeln_s073.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Dabei ist an den Seitennähten die Hälfte des Öffnungsbetrags anzuzeichnen,
  der zwischen den Teilungsnähten geöffnet wird, d.h. in diesem Beispiel: 2/5
  zwischen den Schnitteilen und 1/5 (das ist die Hälfte) an der SN.
  ```
- **Technische Formel:**
  ```text
  oeffnung_seitennaht = 0,5 × oeffnung_teilungsnaht

  Beispiel im Buch:
  oeffnung_teilungsnaht_beispiel = 2/5
  oeffnung_seitennaht_beispiel   = 1/5
  ```
- **Eingaben und Einheiten:** `oeffnung_teilungsnaht` – Öffnungsbetrag an den
  Teilungsnähten (Einheit nicht spezifiziert, im Beispiel als Bruchanteil
  2/5 angegeben).
- **Ausgabe und Einheit:** `oeffnung_seitennaht` – Öffnungsbetrag an der
  Seitennaht, feste Regel „die Hälfte" des Teilungsnaht-Betrags.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „die Hälfte" ist eine
  feste Regel (kein `ca.`). Die Beispielwerte 2/5 und 1/5 gelten laut
  Buchtext ausdrücklich nur „in diesem Beispiel" – nicht als allgemeiner
  Standardwert zu verwenden.
- **Abhängigkeiten:** [[Formel 1]] (Spreizoperation, auf der dieses
  Verhältnis aufsetzt); [[Formel 3]] (Summe der Öffnungsbeträge bestimmt den
  erzielten Kreisanteil).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Bezugsgröße der Brüche 2/5 und 1/5 nicht spezifiziert (Anteil wovon –
    Kreisumfang, Gesamtöffnung, o. Ä. – bleibt offen).
  - Unklar, ob „die Hälfte" je einzelner Teilungsnaht oder von der Summe
    aller Teilungsnähte gilt.
  - OCR-Fehler „Seitennahen"/„Teilungsnahen"/„thisem" nicht am Original
    geprüft.

## Formel 3 – Rechter-Winkel-Bedingung für den Viertelkreis

- **Quelle:** [`formeln_s073.md`](formeln_s073.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Um einen Viertelkreis zu erzielen, können die Schnitteile so angeordnet
  werden, dass die neu angezeichnete Seitennaht im rechten Winkel zur vM bzw.
  hM verläuft.
  ```
- **Technische Formel:**
  ```text
  winkel(seitennaht_neu, bezugslinie) = 90°
  bezugslinie ∈ {vM, hM}
  ```
- **Eingaben und Einheiten:** neu angezeichnete Seitennaht (Linie);
  Bezugslinie vM oder hM.
- **Ausgabe und Einheit:** Zielbedingung 90° zwischen Seitennaht und
  Bezugslinie; bestimmt die Anordnung der Schnitteile für einen
  „echten" Viertelkreis.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Buchtext formuliert
  „können … angeordnet werden" – als Möglichkeit, nicht als zwingende
  Vorschrift. Zielwert selbst ist exakt 90°, kein Bereich.
- **Abhängigkeiten:** [[Formel 1]], [[Formel 2]] – Abnahmekriterium für die
  aus der Spreizung und dem Öffnungsverhältnis entstehende Zielgeometrie.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - „können" lässt offen, ob 90° zwingend oder nur eine von mehreren
    Anordnungsmöglichkeiten ist.
  - Die im Original grün hervorgehobene Textstelle (laut `s073.md`) wurde in
    diesem Durchlauf nicht bildlich, nur textlich erfasst.

## Formel 4 – Auswahlregel Taillennaht-Ausformung

- **Quelle:** [`formeln_s073.md`](formeln_s073.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Die Taillennaht schön rund ausformen oder für deutlich positionierte
  Glocken die Ecken an der Taillennaht belassen und nähen.
  ```
- **Technische Formel:**
  ```text
  wenn ziel = "gleichmäßige Rundung":
      taillennaht_neu = geglaettete_kurve(ecken_entfernt=true)
  wenn ziel = "deutlich positionierte Glocken":
      taillennaht_neu = ecken_beibehalten, vernaeht
  ```
- **Eingaben und Einheiten:** gewünschter gestalterischer Effekt (rund vs.
  eckig/deutlich positionierte Glocken); kein Zahlenwert.
- **Ausgabe und Einheit:** Form der neuen Taillennaht (glatte Kurve oder mit
  Ecken).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** reine Auswahlregel
  zwischen zwei im Buch genannten Alternativen; keine dritte Option benannt,
  kein Zahlenwert.
- **Abhängigkeiten:** baut auf den durch [[Formel 1]]/[[Formel 2]] geöffneten
  Teilen auf – die neue Taillennaht verläuft über die geöffneten Nähte.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - OCR-Schreibfehler „schon"/„Glücken" (statt „schön"/„Glocken") nicht am
    Original geprüft.
