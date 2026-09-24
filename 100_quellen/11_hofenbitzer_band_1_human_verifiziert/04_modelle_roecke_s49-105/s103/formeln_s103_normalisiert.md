# Formeln s103 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s103.md`](formeln_s103.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle drei Regeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der
Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die
Bestätigung. Keine der drei Regeln nennt einen Zahlenwert — die Normalisierung
bildet deshalb die Beziehung ab, ohne einen festen Betrag oder Default zu
erfinden.

## Formel 1 – Gleichmäßiges Öffnen der Falteneinschnitte

- **Quelle:** [`formeln_s103.md`](formeln_s103.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Dann nacheinander alle Falteneinschnitte ungefähr gleich welt öffnen. Dabei möglichst alle im Grundschnitt vorhandenen Abnäher schließen.
  ```
- **Technische Formel:**
  ```text
  für alle Falteneinschnitte i = 1..n:
    öffnungsweite_i ≈ öffnungsweite_gesamt / n   (ungefähr gleich verteilt)
  ```
- **Eingaben und Einheiten:** Anzahl der Falteneinschnitte `n` (auf dieser
  Seite nicht beziffert); Gesamt-Öffnungsweite `öffnungsweite_gesamt` (cm, auf
  dieser Seite nicht angegeben).
- **Ausgabe und Einheit:** Einzel-Öffnungsweite je Falteneinschnitt `öffnungsweite_i`
  (cm), ungefähr gleich verteilt.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „ungefähr gleich weit"
  – keine exakte Gleichverteilung vorgeschrieben, kein Zahlenwert im
  Buchtext. Sekundäre Bedingung im selben Satz: möglichst alle im Grundschnitt
  vorhandenen Abnäher dabei schließen (eigenständiges Auswahlziel, hier nicht
  als eigene Formel geführt).
- **Abhängigkeiten:** setzt den vorhergehenden Schritt „Wasserfallkante
  öffnen, linken vorderen Abnäher schließen" voraus (nicht als eigene Formel
  extrahiert, siehe „Nicht als Formel erfasst" in `formeln_s103.md`).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Anzahl `n` der Falteneinschnitte auf dieser Seite nicht beziffert.
  - „ungefähr gleich" bleibt qualitativ, keine Toleranzangabe.

## Formel 2 – Faltenrückschnitt an P1 gerade abschneiden

- **Quelle:** [`formeln_s103.md`](formeln_s103.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die Faltenrückschnitte durch Zulegen und Zurückschneiden der Falten bestimmen. An P1 (Beginn der Übertritt-Kante) wird der Rückschnitt gerade abgeschnitten.
  ```
- **Technische Formel:**
  ```text
  rückschnittlinie = bestimmt_durch(zulegen, zurückschneiden der Falten)
  ab Punkt P1: rückschnittlinie = gerade  (P1 = Beginn Übertritt-Kante)
  ```
- **Eingaben und Einheiten:** Position `P1` (Beginn der Übertritt-Kante, auf
  dieser Seite nicht mit Koordinate oder Maß belegt); Faltenrückschnitt-Linie
  aus vorherigem Konstruktionsschritt.
- **Ausgabe und Einheit:** gerade Schnittkante ab `P1` (keine Maßeinheit, reine
  Geometrieregel).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Verfahren „Zulegen und
  Zurückschneiden" bleibt qualitativ, kein Zahlenwert. Ab `P1` ist die Kante
  laut Buchtext zwingend gerade – feste Regel, kein Spielraum.
- **Abhängigkeiten:** `P1` wird auf dieser Seite nur textlich benannt, nicht
  eigens vermessen; vermutlich in `skizzen/s103_skizze_02.png` markiert
  (Zeichnung hier nicht eigens ausgewertet, kein Geometriewert daraus
  übernommen).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Position von `P1` nicht separat aus der Zeichnung extrahiert.
  - „Zulegen und Zurückschneiden der Falten" nicht weiter quantifiziert.

## Formel 3 – Beleg-Breite für die Wasserfall-Kante

- **Quelle:** [`formeln_s103.md`](formeln_s103.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Für die Wasserfall-Kante muss ein Beleg konstruiert werden (hier in Gelb-Orange). Dazu wird oben der ursprüngliche Taillenverlauf verwendet und nach unten die Beleg-Kante so breit zum Saum gezeichnet, dass sie beim Umschlagen der Übertritt-Kante nicht direkt sichtbar wird.
  ```
- **Technische Formel:**
  ```text
  beleg_oberkante = ursprünglicher_taillenverlauf
  beleg_breite(zum_saum) = kleinste Breite, sodass gilt:
    sichtbar(übertritt_kante_umgeschlagen) = false
  ```
- **Eingaben und Einheiten:** oberer Bezug „ursprünglicher Taillenverlauf"
  (Kurve, aus Grundschnitt übernommen); unterer Bezug „Saum"; Bedingung
  „nicht direkt sichtbar beim Umschlagen der Übertritt-Kante".
- **Ausgabe und Einheit:** Beleg-Kante-Breite zum Saum (cm, auf dieser Seite
  nicht beziffert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Zahlenwert; die
  Auswahlregel ist eine Sichtbarkeitsbedingung, keine feste Maßangabe – Breite
  ist so zu wählen, dass die Bedingung erfüllt bleibt.
- **Abhängigkeiten:** Folgeschritt „Beleg kopieren und spiegeln" (nicht als
  eigene Formel geführt, reine Operation); Übertritt-Kante-Konstruktion selbst
  wird auf dieser Seite nicht hergeleitet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - „so breit … dass sie … nicht direkt sichtbar wird" bleibt qualitativ,
    keine messbare Schwelle angegeben.
  - Keine Aussage, ob die Regel unabhängig von Konfektionsgröße oder
    Stoffdicke gilt.
