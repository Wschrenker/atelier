# Formeln s094 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s094.md`](formeln_s094.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Beide Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der Buchfassung.
Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung.

## Formel 1 – Futterkürzung am Saum

- **Quelle:** [`formeln_s094.md`](formeln_s094.md), Abschnitt 1
- **Buchfassung:**
  ```text
  5 Das Futter um ca. 2 cm kürzen.
  ```
- **Technische Formel:**
  ```text
  saum_futter_neu = saum_futter_alt - delta
  delta ≈ 2 cm  (ca.)
  ```
- **Eingaben und Einheiten:** `saum_futter_alt` (cm), Saumkante des zuvor
  konstruierten Futterteils; `delta` ≈ 2 cm.
- **Ausgabe und Einheit:** `saum_futter_neu` (cm), gekürzte Futter-Saumkante.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` vor dem Wert
  erhalten – kein fester Betrag laut Buch.
- **Abhängigkeiten:** Setzt das aus Schritt 1–4 konstruierte Futterteil voraus
  (Schritt 1 verweist auf die Weitenreduzierung ab Seite 50, hier nicht
  kopiert, nur verlinkt). Vergleichbare Saumkürzungen um feste bzw. ungefähre
  cm-Werte finden sich auf s059 (Formel 2 und Formel 4 dort).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Unklar, ob `delta` einmalig am gesamten Saum oder je Teilstück (z.B.
    getrennt für vM/hM-Anteile) abgezogen wird.

## Formel 2 – Einschlag-Spiegelung bei der Futterkonstruktion

- **Quelle:** [`formeln_s094.md`](formeln_s094.md), Abschnitt 2
- **Buchfassung:**
  ```text
  4 Da beide Einschläge nach innen gebügelt werden, müssen bei der
  Futterkonstruktion beide Einschläge nach innen gespiegelt und entfernt werden.
  ```
- **Technische Formel:**
  ```text
  einschlag_gespiegelt = spiegeln(einschlag, achse = buegelkante_innen)
  futterteil_neu = futterteil_alt - einschlag_gespiegelt
  ```
  (geometrische Operation: Spiegelung der Einschlagfläche nach innen,
  anschließend Entfernen dieser Fläche aus dem Futterzuschnitt; kein
  numerischer Maß-Rechenwert im Wortlaut.)
- **Eingaben und Einheiten:** `einschlag` (Flächen-/Kantengeometrie des
  Schlitz- bzw. Saumeinschlags am Oberstoff, keine Einheit im Buchtext
  benannt); `buegelkante_innen` als Spiegelachse.
- **Ausgabe und Einheit:** `futterteil_neu` (Geometrie), Futterteil ohne
  gespiegelte Einschlagfläche.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Betrifft laut Wortlaut
  „beide Einschläge" – gemeint sind vermutlich Schlitzeinschlag und
  Saumeinschlag (siehe Seitentext „Der Schlitzeinschlag und der Saumeinschlag
  sind mit einer Briefecke gearbeitet."); auf dieser Seite nicht eindeutig
  benannt, welche zwei Einschläge konkret gemeint sind.
- **Abhängigkeiten:** Baut auf Schritt 3 („Schlitzeinschläge für den Rock
  anzeichnen", [[Formel 1]] vorgelagert) auf; betrifft dieselbe
  Futterkonstruktion wie Formel 1.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Welche zwei Einschläge genau gemeint sind (Schlitz- und Saumeinschlag oder
    beide Schlitzeinschläge links/rechts) ist aus dem Wortlaut dieser Seite
    allein nicht eindeutig.
  - Kein Zahlenwert vorhanden; die Formel bildet nur die geometrische
    Operation ab, keine messbare Größe.
