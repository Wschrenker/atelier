# Formeln – s044 (normalisiert, technische Fassung)

Diese Fassung trennt die Buchformeln von `formeln_s044.md` (fototreu, noch
nicht menschlich geprüft) von einer technischen Lesart. **Keine der Formeln
dieser Seite ist bisher von Werner am Original bestätigt** – bestätigt ist
bislang nur die Variablenbezeichnung `r_SaW` (siehe `s044.md`, Abschnitt
„Vorab geklärte formel- und coderelevante Stellen"). Alle Status stehen daher
auf `offen` oder `gesperrt`, bis Werner die Werte, den Rechenweg und den
Widerspruch bei `r_TaW` am Buch geprüft hat.

## Formel 1 – innerer Radius (Taillenradius), Berechnungen-Kasten

**Quelle:** [formeln_s044.md](formeln_s044.md), Abschnitt „Berechnungen-Kasten"
(→ [ocr_s044.md](ocr_s044.md), Zeilen 18–22).

**Buchfassung:**

```text
r_TaW = TaW : (2 · π)
      = 72 cm : (2 · 3,14)
      = 11,5 cm
```

**Technische Formel:** `r_TaW = TaW / (2 * pi)`

**Eingaben und Einheiten:**
- `TaW` – Taillenweite, cm (Buchbeispiel: 72 cm)
- `pi` – im Buch als `3,14` verwendet (keine Bestätigung, ob generell auf
  2 Nachkommastellen gerundet oder Systemkonstante gemeint ist)

**Ausgabe und Einheit:** `r_TaW` – innerer Radius (Taillenradius), cm

**Bereiche, Bedingungen, Auswahlentscheidungen:** keine im Buchtext erkennbar.

**Abhängigkeiten:** Ausgabe `r_TaW` ist Eingabe für Formel 2. Steht neben
Formel 4 (gleiche Zielgröße `r_TaW`, andere Eingaben) – siehe Widerspruch dort.

**Status:** offen

**Offene Fragen:** Nachrechnung `72 / (2·3,14) = 11,4649…` rundet auf
11,5 cm – deckt sich mit dem Buchwert, aber die Rundungsregel selbst ist
nicht bestätigt. Werner muss TaW = 72 cm und π = 3,14 am Original bestätigen.

## Formel 2 – äußerer Radius (Saumradius)

**Quelle:** [formeln_s044.md](formeln_s044.md), Abschnitt „Berechnungen-Kasten"
(→ [ocr_s044.md](ocr_s044.md), Zeilen 18–22).

**Buchfassung:**

```text
r_SaW = r_TaW + MoL
      = 11,5 cm + 50 cm
      = 61,5 cm
```

**Technische Formel:** `r_SaW = r_TaW + MoL`

**Eingaben und Einheiten:**
- `r_TaW` – Ausgabe von Formel 1, cm
- `MoL` – Rocklänge (laut Skizzenbeschriftung ☐2: „Rocklänge = MoL (oder
  Volantlänge)"), cm (Buchbeispiel: 50 cm)

**Ausgabe und Einheit:** `r_SaW` – äußerer Radius (Saumradius), cm.
Variablenname `r_SaW` ist von Werner bestätigt (siehe `s044.md`); die
Formel selbst noch nicht.

**Bereiche, Bedingungen, Auswahlentscheidungen:** `MoL` kann laut
Skizzenbeschriftung auch als Volantlänge gelesen werden – keine Buchregel
dazu, wann welche Lesart gilt.

**Abhängigkeiten:** benötigt `r_TaW` aus Formel 1. Ausgabe ist Eingabe für
Formel 3.

**Status:** offen

**Offene Fragen:** MoL = 50 cm und die Alternative „Volantlänge" am Original
bestätigen lassen.

## Formel 3 – Saumweite

**Quelle:** [formeln_s044.md](formeln_s044.md), Abschnitt „Berechnungen-Kasten"
(→ [ocr_s044.md](ocr_s044.md), Zeilen 18–22).

**Buchfassung:**

```text
SaW = 2 · π · r_SaW
    = 2 · 3,14 · 61,5 cm
    = 386,2 cm
```

**Technische Formel:** `SaW = 2 * pi * r_SaW`

**Eingaben und Einheiten:** `r_SaW` – Ausgabe von Formel 2, cm; `pi = 3,14`
wie in Formel 1.

**Ausgabe und Einheit:** `SaW` – Saumweite (Umfang des Saumkreises), cm

**Bereiche, Bedingungen, Auswahlentscheidungen:** keine im Buchtext
erkennbar.

**Abhängigkeiten:** benötigt `r_SaW` aus Formel 2 (mittelbar also `r_TaW`
aus Formel 1).

**Status:** offen

**Offene Fragen:** Nachrechnung mit dem gerundeten Buchwert `r_SaW = 61,5 cm`
ergibt `2 · 3,14 · 61,5 = 386,22 cm`, gerundet 386,2 cm – deckt sich mit dem
Buch. Mit dem ungerundeten Zwischenwert (`r_SaW ≈ 61,4649 cm`) ergäbe sich
`≈ 386,0 cm`. Das Buch rechnet also mit dem bereits gerundeten Zwischenwert
weiter (Rundungskette) – keine Abweichung, aber die Rundungsregel selbst ist
nicht bestätigt.

## Formel 4 – innerer Radius mit Nahtzugabe, Abschnitt „2 Zuschnitt"

**Quelle:** [formeln_s044.md](formeln_s044.md), Abschnitt „Formel im Abschnitt
„2 Zuschnitt"" (→ [ocr_s044.md](ocr_s044.md), Zeile 44).

**Buchfassung:**

```text
r_TaW = (TaW + 2 · NZg) : (2 · π)
```

**Technische Formel:** `r_TaW = (TaW + 2 * NZg) / (2 * pi)`

**Eingaben und Einheiten:**
- `TaW` – Taillenweite, cm
- `NZg` – Nahtzugabe, cm (kein Wert im Buch angegeben)
- `pi = 3,14` wie oben

**Ausgabe und Einheit:** `r_TaW` – innerer Radius (Taillenradius), cm

**Bereiche, Bedingungen, Auswahlentscheidungen:** Der umgebende Text
(☐3 „müssen … zwei Kreisringe aneinander genäht werden … günstiger für das
Einnahen eines Reißverschlusses" / „muss dann ein Schlitz für den
Reißverschluss berücksichtigt werden") legt nahe, dass diese Fassung für den
Zuschnitt als kompletter Kreisring mit Reißverschlussschlitz gilt, während
Formel 1 für den einfachen halben/viertel Kreisring im Stoffbruch (ohne
zusätzliche Naht an der Taille) stehen könnte. Das ist eine plausible Lesart
des Fließtexts, aber keine von Werner bestätigte Buchregel.

**Abhängigkeiten:** liefert dieselbe Zielgröße `r_TaW` wie Formel 1, mit
zusätzlichem Term `2 · NZg`.

**Status:** gesperrt

**Offene Fragen oder Widersprüche:** Zwei unterschiedliche Formeln für
`r_TaW` auf derselben Seite (ohne vs. mit `2 · NZg`). Ungeklärt, ob beide so
im Buch stehen, für welchen Zuschnitt-Fall welche gilt, und welcher Wert für
`NZg` vorgesehen ist. Diese Formel ist bereits in `formeln_s044.md` als
klärungsbedürftig markiert. Nicht als Beweis für oder gegen Formel 1
verwendbar.

## Zusammenfassung

Vier Formeln erfasst, keine bisher fachlich bestätigt. Formeln 1–3 sind
`offen` (Werte/Rechenweg unbestätigt, aber kein erkennbarer Widerspruch).
Formel 4 ist `gesperrt` wegen des ungeklärten Widerspruchs zu Formel 1. Für
einen späteren Codevertrag muss Werner mindestens Formel 1–3 bestätigen und
den Widerspruch bei Formel 4 auflösen.
