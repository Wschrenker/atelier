# Formeln – Seite 201 (normalisiert)

Getrennte technische Fassung zu [`formeln_s201.md`](formeln_s201.md). Die
Seite ist weiterhin `OCR-Rohfassung – noch nicht menschlich verifiziert`
([`s201.md`](s201.md)); jede Formel unten bleibt bis zur Bestätigung am
Original `offen`, auch wenn die geometrische Operation selbst eindeutig
lesbar ist.

## Formel 1 — Übertrag vAchsel/hAchsel auf die Kugelkurven

**Quelle:** [`formeln_s201.md`](formeln_s201.md#übertrag-vachselhachsel-auf-die-kugelkurven)
und Abschnitt „hAchsel-Wert"/„vAchsel-Wert" (Zeichnung `skizze_02`).

**Buchfassung:**

```text
An der unteren Armelkurve die vAchsel auf die vAk übertragen → vorderer
Armelpunkt = vAP.
Die hAchsel auf die hAk übertragen → hinterer Armelpunkt = hAP.
```

**Technische Formel:** `vAP = Punkt auf Kurve vÄk im Bogenabstand vAchsel von tP`;
`hAP = Punkt auf Kurve hÄk im Bogenabstand hAchsel von tP`.

**Eingaben und Einheiten:** `vAchsel = 4,1 cm`, `hAchsel = 7,3 cm` (nur aus
Zeichnung `skizze_02` bekannt, nicht im Fließtext), Kurven `vÄk`, `hÄk`.

**Ausgabe und Einheit:** Punkte `vAP`, `hAP` (Lage auf der jeweiligen Kurve).

**Bereiche, Bedingungen, Auswahlentscheidungen:** keine Bandbreite im Buch
angegeben; beide Werte erscheinen als feste Beispielzahlen.

**Abhängigkeiten:** Kurven `vÄk`/`hÄk` stammen aus Abschnitt 4
„Ärmelkugelformen" derselben Seite bzw. aus der vorangehenden
Ärmelgrundkonstruktion (vermutlich Seite 200, nur verlinken, nicht
kopieren).

**Status:** offen

**Offene Fragen:** Herkunft der Werte 4,1 cm / 7,3 cm ungeklärt — feste
Buchkonstante für dieses Modell oder aus einem Körpermaß abgeleitet? Keine
Formel auf dieser Seite zeigt ihre Berechnung.

## Formel 2 — Knips 1 cm oberhalb hAP

**Quelle:** [`formeln_s201.md`](formeln_s201.md#knips-abstand-oberhalb-hap)
und „Knips 1 cm (Punkt 16)".

**Buchfassung:**

```text
Ein zweiter Knips wird 1 cm oberhalb des hAP markiert.
```

**Technische Formel:** `Knips_2 = Punkt auf Kurve im Bogenabstand 1 cm von hAP, Richtung Kugelspitze`.

**Eingaben und Einheiten:** `hAP` (Punkt), Offset `1 cm` (fest).

**Ausgabe und Einheit:** Punkt `Knips_2` (= Punkt 16 in der Zeichnung).

**Bereiche, Bedingungen, Auswahlentscheidungen:** fester Wert, keine
Bandbreite.

**Abhängigkeiten:** benötigt `hAP` aus Formel 1.

**Status:** offen

**Offene Fragen:** keine inhaltliche Unklarheit; Status bleibt offen allein
wegen fehlender menschlicher Verifizierung der Seite.

## Formel 3 — Bezeichnung SuP = P5

**Quelle:** [`formeln_s201.md`](formeln_s201.md#bezeichnung-sup--p5).

**Buchfassung:**

```text
Der SuP ist hier der Konstruktionspunkt P5.
```

**Technische Formel:** `SuP ≡ P5` (Punktalias, kein Rechenwert).

**Eingaben und Einheiten:** keine.

**Ausgabe und Einheit:** keine.

**Bereiche, Bedingungen, Auswahlentscheidungen:** keine.

**Abhängigkeiten:** Bezug zu Punkt „P5" stammt nicht von dieser Seite;
Ursprung offen, nur verlinken sobald die Quellseite bekannt ist.

**Status:** offen

**Offene Fragen:** Auf welcher Seite/in welchem Abschnitt wird „P5"
definiert? Ohne diesen Bezug ist die Aliasangabe nicht in eine Engine-Regel
übersetzbar.

## Formel 4 — Halbierung Saumlinie und ½ ÄSaW

**Quelle:** [`formeln_s201.md`](formeln_s201.md#halbierung-saumlinie-und-äsaw-antrag)
und „Halbe Ärmelsaumweite (Punkt 17)".

**Buchfassung:**

```text
Die Saumlinie halbieren und von dort jeweils die 1/2 Armelsaumweite (ASaW)
nach links und rechts abtragen.
```

**Technische Formel:** `SaumPunkt_links = SaumMitte − ÄSaW / 2`;
`SaumPunkt_rechts = SaumMitte + ÄSaW / 2` (entlang der Saumlinie).

**Eingaben und Einheiten:** `ÄSaW` (Ärmelsaumweite, cm) — Wert auf dieser
Seite nicht definiert.

**Ausgabe und Einheit:** zwei Punkte auf der Saumlinie (cm-Abstand von der
Saummitte).

**Bereiche, Bedingungen, Auswahlentscheidungen:** exakte Halbierung, keine
Bandbreite angegeben.

**Abhängigkeiten:** `ÄSaW` stammt vermutlich aus einer Maßtabelle oder
einer anderen Seite; hier nur als Eingabegröße referenziert, nicht
hergeleitet.

**Status:** offen

**Offene Fragen:** Woher kommt `ÄSaW` (Maßvorgabe, andere Formel, andere
Seite)?

## Formel 5 — Kontrolle Oberarmweite (OaW)

**Quelle:** [`formeln_s201.md`](formeln_s201.md#kontrolle-oaw-mit-abweichung)
und „Kontrolle der Oberarmweite (Punkt 20)".

**Buchfassung:**

```text
Die OaW kontrollieren (hier 0,2 cm geringer als geplant).
```

```text
Kontrolle der Oberarmweite (28,8 cm)
```

**Technische Formel:** `Abweichung = OaW_Konstruktion − OaW_geplant`;
Buchbeispiel: `Abweichung = −0,2 cm`. Unabhängig nachgerechnet (nicht als
Buchformel, nur als Plausibilitätsprüfung): wenn `OaW_Konstruktion = 28,8 cm`
aus der Zeichnung dieselbe Kontrolle meint, ergäbe sich
`OaW_geplant = 29,0 cm`.

**Eingaben und Einheiten:** `OaW_Konstruktion` (cm), `OaW_geplant` (cm) —
`OaW_geplant` nicht auf dieser Seite definiert.

**Ausgabe und Einheit:** `Abweichung` (cm).

**Bereiche, Bedingungen, Auswahlentscheidungen:** keine Toleranzgrenze im
Buch angegeben, nur ein Beispielwert.

**Abhängigkeiten:** `OaW_geplant` vermutlich aus Maßtabelle; Bezug zu
anderer Seite nicht hergeleitet.

**Status:** offen

**Offene Fragen:** Meinen der Fließtext-Wert „0,2 cm" und der
Zeichnungswert „28,8 cm" dieselbe Kontrolle? Das Buch stellt diese
Verknüpfung nicht ausdrücklich her — von Werner am Original zu bestätigen.

## Formel 6 — Lage Punkt 15 (Ärmelkugel)

**Quelle:** [`formeln_s201.md`](formeln_s201.md#lage-punkt-15) (Zeichnung
`skizze_01`).

**Buchfassung:**

```text
15: besser knapp oberhalb der Hälfte (½)
```

**Technische Formel:** `P15 = Punkt auf der Kugelkurve knapp oberhalb der
Hälfte zwischen den beiden Winkellinien-Endpunkten` (qualitative Regel,
kein fester Faktor).

**Eingaben und Einheiten:** Winkellinien-Endpunkte der Kugelkurve (keine
Zahlenwerte).

**Ausgabe und Einheit:** Punkt `P15` (Lage auf der Kurve).

**Bereiche, Bedingungen, Auswahlentscheidungen:** „knapp oberhalb der
Hälfte" ist ein fachlicher Auswahlspielraum ohne festen Prozentsatz; bleibt
als Bereich erhalten, kein Default setzen.

**Abhängigkeiten:** keine zu anderen Formeln dieser Seite.

**Status:** offen

**Offene Fragen:** Keine inhaltliche Unklarheit über den Spielraum selbst,
aber wie „knapp oberhalb" für eine Engine quantifiziert werden soll, ist
eine fachliche Auswahlentscheidung, keine Buchformel — bewusst nicht
festgelegt.
