# Formeln s060 – Normalisierung

**Vorbehalt:** Seite noch nicht menschlich verifiziert, Extraktion noch nicht
am Original bestätigt (siehe [formeln_s060.md](formeln_s060.md) und
[s060.md](s060.md)). Diese Normalisierung wurde auf Werners ausdrücklichen
Wunsch als Walking Skeleton vor der Bestätigung erstellt. Alle Formeln unten
sind daher zusätzlich zu ihrem fachlichen Status als „technisch vorläufig,
Buchbestätigung aussteht" zu behandeln.

## Formel 1 – Seitliche Breite des Taillenbelegs = Breite der Passe

- **Quelle:** [formeln_s060.md](formeln_s060.md), Abschnitt 1
- **Buchfassung:**

  ```text
  Der einfach geformte Taillenbeleg verstürzt nicht nur die obere Rockkante
  sondern auch den Knopfverschluss am Über- und Untertritt. Er muss also
  dieselbe seitliche Breite besitzen wie die Passe.
  ```

- **Technische Formel:** `breite_taillenbeleg_seitlich = breite_passe_seitlich`
- **Eingaben und Einheiten:** `breite_passe_seitlich` – seitliche Breite der
  Passe (am Über-/Untertritt des Knopfverschlusses), Einheit cm, auf dieser
  Seite nicht beziffert.
- **Ausgabe und Einheit:** `breite_taillenbeleg_seitlich` – seitliche Breite
  des Taillenbelegs, in cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Keine Zahl, sondern
  eine Gleichheitsbedingung. Gilt für die Konstruktion mit einfach geformtem
  Taillenbeleg, der den Knopfverschluss verstürzt.
- **Abhängigkeiten:** `breite_passe_seitlich` ist auf dieser Seite nicht
  quantifiziert (ergibt sich aus der frei gewählten Passenform, Schritt 3 im
  Abschnitt „Taillenvertiefung, Passe, Taillenbeleg und Futtersaum"). Bezug zu
  [[Formel 2]] unklar (siehe Offene Fragen).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Die Seite liefert keinen Zahlenwert für
  `breite_passe_seitlich`; die Formel ist als Beziehung normalisierbar, aber
  ohne Werners Bestätigung der Buchstelle nicht als gesichert zu behandeln.

## Formel 2 – Breite des Taillenbelegs an der Seitennaht = Breite des Knopfverschlusses

- **Quelle:** [formeln_s060.md](formeln_s060.md), Abschnitt 2
- **Buchfassung:**

  ```text
  4 Für die inneren Schnittteile den Taillenbeleg in der Breite des
  Knopfverschlusses an der Seitennaht und die Futtersaumkanten jeweils
  parallel zu den oberen und unteren Rockkanten einzeichnen.
  ```

- **Technische Formel:** `breite_taillenbeleg_seitennaht = breite_knopfverschluss`
- **Eingaben und Einheiten:** `breite_knopfverschluss` – Breite des
  Knopfverschlusses an der Seitennaht, Einheit cm, auf dieser Seite nicht
  beziffert (ergibt sich aus [[Formel 3]], Über- und Untertrittbreite).
- **Ausgabe und Einheit:** `breite_taillenbeleg_seitennaht` – Breite des
  Taillenbelegs an der Seitennaht, in cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Keine Zahl, sondern
  eine Gleichheitsbedingung für die inneren Schnittteile (Taillenbeleg).
  Zusätzliche geometrische Bedingung: Futtersaumkanten parallel zu oberer und
  unterer Rockkante (keine eigene Formel, nur Konstruktionsregel).
- **Abhängigkeiten:** [[Formel 3]] (Untertrittbreite als Teil der
  Knopfverschlussbreite). Möglicher Bezug zu [[Formel 1]] – siehe Offene
  Fragen.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Unklar, ob `breite_passe_seitlich`
  (Formel 1) und `breite_knopfverschluss` (hier) dieselbe Größe an derselben
  Stelle bezeichnen oder zwei unterschiedliche Maße sind, die zufällig
  übereinstimmen. Das Buch nennt beide Bedingungen getrennt, ohne sie
  ausdrücklich gleichzusetzen; nicht selbst zusammengeführt, sondern beide
  fototreu nebeneinander erfasst.

## Formel 3 – Mindestbreite des Untertritts

- **Quelle:** [formeln_s060.md](formeln_s060.md), Abschnitt 3
- **Buchfassung:**

  ```text
  8 einen identischen Untertritt an der linken Seitennaht der RT-Passe und
  dem RT-Taillenbeleg anzeichnen. Die Unterttittbreite muss die Knopflöcher
  innen vollständig hinterlegen (Breite: mind. doppelter Knopfdurchmesser).
  ```

- **Technische Formel:** `breite_untertritt_min = 2 * durchmesser_knopf`
- **Eingaben und Einheiten:** `durchmesser_knopf` – Knopfdurchmesser, Einheit
  cm, auf dieser Seite nicht beziffert.
- **Ausgabe und Einheit:** `breite_untertritt_min` – Mindestbreite des
  Untertritts an der linken Seitennaht (RT-Passe und RT-Taillenbeleg), in cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Untergrenze, kein fester
  Wert; „mind." bleibt als Mindestbedingung erhalten. Zusatzbedingung: Der
  Untertritt muss die Knopflöcher innen vollständig hinterlegen (Formel und
  qualitative Bedingung kombiniert).
- **Abhängigkeiten:** Wirkt auf [[Formel 2]] (Breite des Taillenbelegs an der
  Seitennaht = Breite des Knopfverschlusses).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Keine eigene Rechenprobe möglich, da
  kein konkreter Knopfdurchmesser auf der Seite angegeben ist. Die
  Schrittkennung am Abschnittsanfang ist laut s060.md unklar (Foto zeigt
  vermutlich „5", OCR schreibt „3"); betrifft nicht Schritt 8 selbst.
