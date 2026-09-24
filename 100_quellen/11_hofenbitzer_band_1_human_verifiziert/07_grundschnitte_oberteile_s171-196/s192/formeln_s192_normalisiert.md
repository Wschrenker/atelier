# Formeln s192 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s192.md`](formeln_s192.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Beide Formeln stehen
deshalb auf `offen`. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für
die Bestätigung.

## Formel 1 – VT: maximale Hüftausfall-Entfernung an der SN

- **Quelle:** [`formeln_s192.md`](formeln_s192.md), Abschnitt 1
- **Buchfassung:**
  ```text
  9 ☐4 Beim VT maximal den halben Hüftausfall an der SN entfernen.

  maximal den ½ Hüftausfall an SN entfernen

  Grundlage ist der taillierte OT-GS mit Hüftausfall G 38 PK 5
  ```
- **Technische Formel:**
  ```text
  entfernung_SN_VT ≤ 0,5 * huftausfall_VT
  ```
- **Eingaben und Einheiten:** `huftausfall_VT` (cm), Hüftausfall des
  Ausgangsschnitts „taillierter OT-GS mit Hüftausfall G 38 PK 5" (Größe und
  Passform nicht auf dieser Seite hergeleitet, nur als Grundlage benannt).
- **Ausgabe und Einheit:** `entfernung_SN_VT` (cm), an der SN entfernte
  Weite am Vorderteil.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „maximal" ist eine
  Obergrenze, kein fester Wert laut Buch; jeder Wert zwischen 0 und der
  Hälfte des Hüftausfalls ist zulässig. Kein Default gewählt.
- **Abhängigkeiten:** `huftausfall_VT` stammt aus dem referenzierten
  Grundschnitt „G 38 PK 5", dessen Herleitung nicht auf s192 liegt, nur zu
  verlinken, sobald die Quellseite bekannt ist. Steht in Bezug zu Punkt 8
  („Sämtliche Taillenabnäher reduzieren oder streichen", nicht als eigene
  Formel geführt) und zu ☐2/☐3 als Vergleichspaar mit/ohne Hüftausfall.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Fließtext-Punkt 9 ist mit „☐4" beschriftet, das wortgleiche
    Zeichnungslabel steht laut `skizzen_s192.json` aber im linken
    Schnittteil „☐2", nicht im rechten „☐4". Nicht aufgelöst.
  - Herkunft und genaue Berechnung von `huftausfall_VT` selbst sind auf
    dieser Seite nicht dokumentiert.

## Formel 2 – RT: Hüftweite

- **Quelle:** [`formeln_s192.md`](formeln_s192.md), Abschnitt 2
- **Buchfassung:**
  ```text
  10 Das RT an der Hüfte 1 cm weiter.

  neue Hüftlinie
  + 1 cm
  ```
- **Technische Formel:**
  ```text
  huefte_RT_neu = huefte_RT_alt + 1 cm
  ```
- **Eingaben und Einheiten:** `huefte_RT_alt` (cm), Hüftweite des
  Rückenteils vor dieser Änderung.
- **Ausgabe und Einheit:** `huefte_RT_neu` (cm), Hüftweite des Rückenteils
  an der neuen Hüftlinie.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert „1 cm"
  ohne „ca." laut Buchwortlaut – kein Spielraum. Die Operation (Addition)
  ist aus dem Wort „weiter" sowie dem benachbarten Zeichnungslabel „+ 1 cm"
  neben „neue Hüftlinie" erschlossen, nicht wörtlich als „addieren" o. Ä.
  im Buchtext belegt.
- **Abhängigkeiten:** Zeichnungslabel „+ 1 cm" in `skizzen_s192.json`
  unmittelbar bei „neue Hüftlinie" stützt die Lesart, ersetzt aber nicht die
  fehlende Verbform im Fließtext.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Fließtext-Satz „Das RT an der Hüfte 1 cm weiter." ist unvollständig
    (fehlendes Verb, bereits in `s192.md` vermerkt); ob „weiter machen",
    „weiter stellen" oder ein anderes Wort gedruckt steht, ist am Original
    zu prüfen.
  - Ob sich „1 cm" auf die gesamte Hüftweite, auf eine Seite (halbe
    Hüftweite) oder auf die Verschiebung der SN-Position bezieht, ist aus
    dem Wortlaut nicht eindeutig.
