# Formeln s088 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s088.md`](formeln_s088.md) vermerkt, ist nur
Formel 4 von Werner am Original bestätigt. Die Formeln 1–3 stehen deshalb auf
`offen`, unabhängig von der inhaltlichen Klarheit der Buchfassung. Dies ist
ein Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung der übrigen
Stellen.

## Formel 1 – Tascheneingriff-Zugabe

- **Quelle:** [`formeln_s088.md`](formeln_s088.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Ca.0,5 cm Weite in den Tascheneingriff geben und den Taschenbeutel formen.
  ```
- **Technische Formel:**
  ```text
  weite_tascheneingriff_neu = weite_tascheneingriff_alt + delta
  delta ≈ 0,5 cm  (ca.)
  ```
- **Eingaben und Einheiten:** `weite_tascheneingriff_alt` (cm); `delta` ≈
  0,5 cm.
- **Ausgabe und Einheit:** `weite_tascheneingriff_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` erhalten – kein
  fester Betrag laut Buch.
- **Abhängigkeiten:** Wirkt auf den Taschenbeutel, der im selben Schritt
  geformt wird; genaue Bezugslinie am Original zu bestätigen.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt (außer
    Formel 4).
  - Unklar, auf welche Bezugskante sich die Zugabe genau bezieht (nur
    „Tascheneingriff" benannt, keine Bemaßungslinie im Text beschrieben).

## Formel 2 – Anzahl der Falteninhalte aus Anzahl der geplanten Falten

- **Quelle:** [`formeln_s088.md`](formeln_s088.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Es sind insgesamt 11 Falten geplant. Zwei Faltentiefen (das ist ein
  Falteninhalt) sind jeweils am mittleren VT und mittleren RT angeschnitten.
  10 Falteninhalte benötigt man demnach am Faltenteil (9 ganze und zwei halbe
  Falteninhalte an den Enden), siehe folgende Seite.
  ```
- **Technische Formel:**
  ```text
  anzahl_falteninhalte = f(anzahl_falten)
  anzahl_falten = 11
  anzahl_falteninhalte = 10  (9 ganze + 2 halbe an den Enden)
  ```
- **Eingaben und Einheiten:** `anzahl_falten` (Stück, dimensionslos).
- **Ausgabe und Einheit:** `anzahl_falteninhalte` (Stück, dimensionslos);
  dient als Nenner in [[Formel 4]].
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Feste Werte laut Buch
  (11 → 10), aber die Umrechnungsregel selbst ist aus dem Wortlaut nicht
  eindeutig algebraisch herleitbar.
- **Abhängigkeiten:** Nenner von [[Formel 4]] (`FaI = Σ FaI : Zahl der
  Falteninhalte`); Verweis auf „folgende Seite" (s089), dort ggf. weitere
  Erläuterung.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Der Wortlaut nennt „11 Falten" und „10 Falteninhalte, davon 9 ganze und
    zwei halbe an den Enden" nebeneinander, ohne eine allgemeine Rechenregel
    (z. B. `anzahl_falteninhalte = anzahl_falten - 1`) explizit zu benennen;
    ob dieser Zusammenhang auf andere Faltenzahlen übertragbar ist, ist aus
    dem Buchtext allein nicht sicher.

## Formel 3 – Verbleibender Stoff für Falteninhalte (Σ FaI)

- **Quelle:** [`formeln_s088.md`](formeln_s088.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Die vorhandene Stoffbreite (StB) ist 92 cm.
  Die geschlossene Weite (geW) des Faltenteils (für vorne und hinten)
  beträgt 32 cm.

  Σ FaI = StB - 2 · 1 cm NZg - geW

  = 92 cm - 2 cm - 32 cm

  = 58 cm
  ```
- **Technische Formel:**
  ```text
  Σ_FaI = StB - 2 * NZg - geW
  NZg = 1 cm  (Nahtzugabe je Seite, zweimal abgezogen)
  ```
- **Eingaben und Einheiten:** `StB` = 92 cm (Stoffbreite); `geW` = 32 cm
  (geschlossene Weite des Faltenteils vorne+hinten); `NZg` = 1 cm
  (Nahtzugabe).
- **Ausgabe und Einheit:** `Σ_FaI` (cm), hier 58 cm; dient als Zähler in
  [[Formel 4]].
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Alle Werte im
  gedruckten Beispiel fest (kein `ca.`); nachgerechnet: 92 - 2·1 - 32 = 58,
  stimmt mit der gedruckten Zwischensumme „92 cm - 2 cm - 32 cm = 58 cm"
  überein.
- **Abhängigkeiten:** Zähler von [[Formel 4]]. `StB` und `geW` sind
  modellspezifische Vorgaben dieser Seite, keine allgemeine Konstante.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - „NZg" (Nahtzugabe) wird hier zweimal mit je 1 cm angesetzt; ob das für
    zwei Kanten des Faltenteils steht oder eine andere Bedeutung hat, ist am
    Original zu bestätigen.

## Formel 4 – Falteninhalt (FaI)

- **Quelle:** [`formeln_s088.md`](formeln_s088.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Falteninhalt

  FaI = Σ FaI : Zahl der Falteninhalte

  = 58 cm : 10

  = 5,8 cm
  ```
  (Bestätigte Buchfassung; OCR-Schreibweise „Zohl" durch die von Werner
  bestätigte Fassung „Zahl" ersetzt — siehe
  [`formeln_s088.md`](formeln_s088.md), Abschnitt 4.)
- **Technische Formel:**
  ```text
  FaI = Σ_FaI / anzahl_falteninhalte
  ```
- **Eingaben und Einheiten:** `Σ_FaI` (cm, aus Formel 3); `anzahl_falteninhalte`
  (Stück, aus Formel 2).
- **Ausgabe und Einheit:** `FaI` (cm), hier 5,8 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Fester Rechenweg laut
  Buch, kein Spielraum; nachgerechnet: 58 / 10 = 5,8, stimmt mit der
  gedruckten Beispielrechnung überein.
- **Abhängigkeiten:** [[Formel 2]] (liefert `anzahl_falteninhalte`),
  [[Formel 3]] (liefert `Σ_FaI`).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Die Formel selbst ist von Werner bestätigt; ihre beiden Eingaben
    (`Σ_FaI` aus Formel 3, `anzahl_falteninhalte` aus Formel 2) sind es
    nicht. Für eine spätere Codeumsetzung müssen Formel 2 und Formel 3
    zusätzlich am Original bestätigt werden.
