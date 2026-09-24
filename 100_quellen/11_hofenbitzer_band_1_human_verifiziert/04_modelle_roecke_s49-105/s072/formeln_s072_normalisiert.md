# Formeln s072 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s072.md`](formeln_s072.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Beide Formeln stehen
deshalb auf `offen`. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für
die Bestätigung.

## Formel 1 – Abnäher-Schließung Vorderteil

- **Quelle:** [`formeln_s072.md`](formeln_s072.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Die Teile des saumerweiterten Bahnenrocks werden an den Teilungsnähten wieder aneinandergelegt. Es konnen damit die Abnaher im Vorderteil, wie hier, ganz zugelegt werden.
  ```
- **Technische Formel:**
  ```text
  abnaeher_vt_neu = 0   (wenn Teilungsnähte aneinandergelegt werden)
  ```
- **Eingaben und Einheiten:** keine explizite Maßangabe im Buchtext; die
  Operation setzt eine vorhandene Abnäherbreite im Vorderteil vor dem
  Zusammenlegen voraus (`abnaeher_vt_alt`, Einheit vermutlich cm, im Text nicht
  genannt).
- **Ausgabe und Einheit:** `abnaeher_vt_neu` = 0 (vollständig geschlossen),
  keine Einheit im Buchtext genannt.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Formulierung „wie hier“
  – laut Buch ein konkretes Beispiel dieses Modells, kein ausdrücklich
  allgemeingültiger Automatismus. Ob eine vollständige Schließung immer
  zutrifft oder nur bei ausreichender Saumerweiterung, ist aus dem Wortlaut
  nicht eindeutig.
- **Abhängigkeiten:** Ausgangsteile sind „die Teile des saumerweiterten
  Bahnenrocks“ (10-Bahnenrock, Vorseiten dieser Kategorie) – dort nicht
  erfasst, nur zu verlinken, sobald bekannt. Siehe auch [[Formel 2]] (gleicher
  Konstruktionsschritt, gegenüberliegendes Teil).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kein Zahlenwert für die Ausgangs-Abnäherbreite oder für eine Bedingung,
    wann „ganz“ statt teilweise geschlossen wird.
  - OCR-Wortlaut weicht laut [s072.md](s072.md) wahrscheinlich vom Fototext ab
    („damit“ statt „dabei“, fehlende Umlaute) – nicht am Original geprüft.

## Formel 2 – Abnäher-Summierung Rückteil

- **Quelle:** [`formeln_s072.md`](formeln_s072.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Da im Rückteil die Abnaher grober sind, werden diese nicht ganz zugelegt. Die entstehenden Restabnaher werden addiert und zu einem einzigen Abnaher in der Mitte des Rückteils gezeichnet.
  ```
- **Technische Formel:**
  ```text
  abnaeher_rt_gesamt = Summe(restabnaeher_i, i = 1..n)
  ```
- **Eingaben und Einheiten:** `restabnaeher_i` (cm, im Buchtext nicht
  beziffert) – die nach unvollständigem Zulegen im Rückteil verbleibenden
  Restabnäher; `n` (Anzahl der Restabnäher) im Buchtext nicht genannt.
- **Ausgabe und Einheit:** `abnaeher_rt_gesamt` (cm, im Buchtext nicht
  beziffert), ein einziger Abnäher, positioniert in der Mitte des Rückteils.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Zahlenwerte oder
  Grenzen im Buchtext. Die Auswahlregel „nicht ganz zugelegt, weil größer“
  bleibt qualitativ – kein Schwellenwert genannt, ab dem ein Abnäher als „zu
  groß“ zum vollständigen Zulegen gilt.
- **Abhängigkeiten:** [[Formel 1]] (gleicher Konstruktionsschritt,
  gegenüberliegendes Teil); Ausgangsteile aus dem saumerweiterten Bahnenrock
  (Vorseiten dieser Kategorie, dort nicht erfasst).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Keine Zahlenwerte für einzelne Restabnäher oder deren Anzahl `n`.
  - Position „in der Mitte des Rückteils“ nicht geometrisch präzisiert (Bezug
    zur hM oder zu anderen Referenzlinien unklar).
  - OCR-Wortlaut weicht laut [s072.md](s072.md) wahrscheinlich vom Fototext ab
    („grober“ statt „größer“, fehlender Umlaut in „Restabnäher“) – nicht am
    Original geprüft.
