# Formeln — Maßberechnungen S. 11–15

**Quelle:** Hofenbitzer Band 1, S. 11, 13, 14
**Transkript:** `100_quellen/10_hofenbitzer_b1/2_transkript/band_1/s11-15_rohtranskription.md`
**Begriffe:** siehe `300_formeln/10_masse/10_massregister.md`

Stand: 2026-08-19 · Status: **strukturiert, noch kein Code**

---

## Format

Jede Formel wird so abgelegt — das ist das Format, das die KI beim
Transkribieren erzeugt und aus dem später der Code entsteht:

- **Ergebnis** — was kommt heraus, welche Art von Maß
- **Eingang** — welche Maße gehen hinein
- **Formel** — wörtlich wie im Buch
- **Quelle** — Seitenzahl
- **Prüfwert** — Beispielzahl des Buchs, oder „keine im Buch"
- **Mathematik** — welche Primitive nötig sind

---

## F-14-1 · Rückenbreite

- **Ergebnis:** `RüB` — Konstruktionsmaß
- **Eingang:** `gRüB` — gemessen
- **Formel:** `RüB = gRüB : 2`
- **Quelle:** S. 14, Position 15
- **Prüfwert:** keine im Buch
- **Mathematik:** Division

---

## F-14-2 · Armdurchmesser aus Messung

- **Ergebnis:** `ArD` — Konstruktionsmaß
- **Eingang:** `gArD` links und rechts — gemessen
- **Formel:** `ArD = Durchschnitt(gArD links, gArD rechts)`
- **Quelle:** S. 14, Position 16
- **Prüfwert:** keine im Buch
- **Mathematik:** Mittelwert

---

## F-14-3 · Armdurchmesser aus Oberarmumfang (Alternative)

- **Ergebnis:** `ArD` — Konstruktionsmaß
- **Eingang:** `OaU` — gemessen
- **Formel:** `ArD = OaU · 0,6 – 7,5 cm`
- **Quelle:** S. 14, roter Kasten „Alternative Bestimmung von RüB, ArD und BrB"
- **Prüfwert:** keine im Buch
- **Mathematik:** Multiplikation, Subtraktion
- **Hinweis:** Das Buch nennt diesen Weg **sicherer** als die Messung,
  weil `gArD` schwer zu messen ist.

---

## F-14-4 · Brustbreite aus Messung

- **Ergebnis:** `BrB` — Konstruktionsmaß
- **Eingang:** `gBrB` — gemessen
- **Formel:** `BrB = gBrB : 2`
- **Quelle:** S. 14, Position 17
- **Prüfwert:** keine im Buch
- **Mathematik:** Division

---

## F-14-5 · Brustbreite aus Brustumfang (Alternative)

- **Ergebnis:** `BrB` — Konstruktionsmaß
- **Eingang:** `BrU`, `RüB`, `ArD`
- **Formel:** `BrB = BrU : 2 – RüB – ArD`
- **Quelle:** S. 14, roter Kasten
- **Prüfwert:** keine im Buch
- **Mathematik:** Division, Subtraktion
- **Hinweis:** Das Buch weist ausdrücklich darauf hin, dass die **Summe der
  waagerechten Teilstrecken (RüB + ArD + BrB) einige Zentimeter größer sein
  kann als der gemessene BrU** — weil der BrU schräg und direkt gemessen wird,
  die Teilstrecken aber waagerecht am Papierstreifen.
  Die Formel ist damit keine exakte Identität, sondern eine Näherung.
  → **Offener Punkt P2 im Maßregister:** welcher Weg ist Standard?

---

## F-13-1 · Korrektur der Taillenschräglage

- **Ergebnis:** `RüL`, `VL` — Konstruktionsmaße
- **Eingang:** `gRüL`, `gVL`, beobachtete Schräglage in cm
- **Formel:** wörtlich im Buch nur als Beispiel formuliert:
  > „Liegt z.B. das Taillenband hinten sichtbar um 1 cm tiefer als vorne
  > (–1 cm), muss die RüL um 1 cm reduziert werden, weil eigentlich dort das
  > Taillenband 1 cm höher liegen müsste – also die gemessene RüL hier um 1 cm
  > zu lang ist."
- **Quelle:** S. 13, grauer Kasten rechte Spalte
- **Prüfwert:** hinten 1 cm tiefer → `RüL = gRüL – 1 cm`
- **Mathematik:** Addition/Subtraktion
- **⚠️ Offen:** Das Buch gibt **keine allgemeine Formel**, nur dieses Beispiel
  und die Regel „beide Werte müssen so vorliegen, als seien sie zu einem
  waagerecht liegenden Taillenband gemessen worden".
  Die Verallgemeinerung (Vorzeichen, Verhalten der VL, was bei Schräglage
  nach vorn) muss aus der Maßtabelle S. 16–19 kommen.
  **Nicht raten — Seite erst einpflegen.**

---

## F-11-1 · Achtelteilung der Körperhöhe

- **Ergebnis:** Teillänge eines Achtels am realen Körper
- **Eingang:** `KöH`
- **Formel:** `Teillänge = KöH : 8`
- **Quelle:** S. 11
- **Prüfwert:** `168 cm : 8 = 21 cm` ✅ nachgerechnet, stimmt
- **Mathematik:** Division

---

## F-11-2 · Figurinenhöhe im Buchmaßstab

- **Ergebnis:** Höhe der gezeichneten Figurine
- **Eingang:** `KöH`
- **Formel:** `Figurinenhöhe = KöH : 16` (Maßstab 1:16)
- **Quelle:** S. 11
- **Prüfwert:** `168 cm : 16 = 10,5 cm` ✅ nachgerechnet, stimmt
- **Mathematik:** Division
- **⚠️ Offen:** Formulierung im Buch ist missverständlich —
  siehe Punkt P3 im Maßregister. Für die Engine ohne Bedeutung
  (reine Zeichenkonvention), für das Verständnis aber relevant.

---

## Zusammenfassung: welche Mathematik dieser Block braucht

Nur die vier Grundrechenarten und den Mittelwert.
**Keine Geometrie-Primitive nötig.**

Das ändert sich beim ersten Konstruktionsmodul (S. 44) —
dort kommen Kreis und Kreisbogen dazu.
