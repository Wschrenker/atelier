# Formeln — Echter Glockenrock, Vollglocke (Tellerrock), S. 44

**Quelle:** Hofenbitzer Band 1, S. 44
**Foto:** `hofenbitzer/43-130/20260617_160345.jpg`
**Transkript:** `hofenbitzer/transskript/s44_glockenrock.md`
**Begriffe:** siehe `gosslar_kontext/MASSREGISTER.md`

Stand: 2026-08-18 · Status: **Formeln und Prüfwerte erfasst, Modul noch nicht gebaut**
Fachliche Freigabe durch Werner/Munkhuu: **steht aus**

---

## Was das Buch sagt

> Glockenröcke können aus einem oder mehreren Kreisringen oder aus
> Kreisringsegmenten gearbeitet werden.
> Der echte Glockenrock besteht aus einem Vollkreisring (Vollglocke,
> Tellerrock). Er umspielt die Hüften und hat weich fallende Glocken am Saum —
> je nach verwendetem Material und Saumweite.
> Genauso werden auch Volants konstruiert. Anstelle der Bundnaht gibt es hier
> die Volant-Ansatznaht.

Der Schnitt besteht aus **zwei konzentrischen Kreisen**: dem Taillenkreis
(innen) und dem Saumkreis (außen). Sonst nichts. Kein Abnäher, keine Kurve
durch Punkte, keine Figurkorrektur.

---

## F-44-1 · Taillenradius

- **Ergebnis:** `r_TaW` — Innenradius des Kreisrings
- **Eingang:** `TaW` — Taillenweite
- **Formel:** `r_TaW = TaW : (2 · π)`
- **Quelle:** S. 44, Berechnungskasten ❶
- **Prüfwert:** `72 cm : (2 · 3,14) = 11,5 cm` ✅ nachgerechnet: 11,4649 → 11,5
- **Mathematik:** Division, π

---

## F-44-2 · Saumradius

- **Ergebnis:** `r_SaW` — Außenradius des Kreisrings
- **Eingang:** `r_TaW`, `MoL` (Rocklänge, alternativ Volantlänge)
- **Formel:** `r_SaW = r_TaW + MoL`
- **Quelle:** S. 44, Berechnungskasten ❶
- **Prüfwert:** `11,5 cm + 50 cm = 61,5 cm` ✅ nachgerechnet, stimmt
- **Mathematik:** Addition

---

## F-44-3 · Saumweite

- **Ergebnis:** `SaW` — Umfang des Saumkreises
- **Eingang:** `r_SaW`
- **Formel:** `SaW = 2 · π · r_SaW`
- **Quelle:** S. 44, Berechnungskasten ❶
- **Prüfwert:** `2 · 3,14 · 61,5 cm = 386,2 cm` ✅ nachgerechnet: 386,22
- **Mathematik:** Multiplikation, π

---

## F-44-4 · Taillenradius mit Nahtzugabe (voller Kreisring)

- **Ergebnis:** `r_TaW` — Innenradius, wenn der Rock als **kompletter**
  Kreisring zugeschnitten wird
- **Eingang:** `TaW`, `NZg` — Nahtzugabe
- **Formel:** `r_TaW = (TaW + 2 · NZg) : (2 · π)`
- **Quelle:** S. 44, Abschnitt „Zuschnitt", ❑3+4
- **Prüfwert:** keine im Buch
- **Mathematik:** Multiplikation, Addition, Division, π
- **Warum:** Beim vollen Kreisring muss in der Taille ein **Schlitz für den
  Reißverschluss** berücksichtigt werden. Die Zugabe an beiden Schlitzkanten
  vergrößert den nötigen Innenumfang.

---

## ⚠️ π — die erste bewusste Abweichung

**Das Buch rechnet mit π = 3,14.**

| Formel | mit 3,14 | mit exaktem π | Differenz |
|---|---|---|---|
| r_TaW bei TaW 72 | 11,465 cm | 11,459 cm | 0,006 cm |
| SaW bei r_SaW 61,5 | 386,22 cm | 386,42 cm | 0,20 cm |

**Festlegung für die Engine:** wir rechnen mit **exaktem π** und prüfen die
Buchwerte mit einer Toleranz von **±0,25 cm**.

Grund: 0,2 cm auf 3,86 m Saum sind in der Fertigung bedeutungslos, aber ein
exakter Vergleich würde jeden Test rot färben und wir würden einen Fehler
suchen, der keiner ist.

**Diese Abweichung ist bewusst und muss so bleiben.** Wenn ein Test später
knapp scheitert, ist π der erste Verdächtige.

---

## Konstruktionsschritte (S. 44)

1. Taillenweite und Rocklänge bestimmen, Berechnungen durchführen.
2. Grundlinie des Kreises und Kreis-Mittelpunkt bestimmen.
3. Kreis mit dem inneren Radius `r_TaW` → **Taillenkreis**.
4. Kreis mit dem äußeren Radius `r_SaW` um denselben Mittelpunkt → **Saumkreis**.
5. Rechtwinklig durch den Mittelpunkt eine zweite Linie zum äußeren Kreisbogen
   → **Seitenlinie**.

## Mathematik, die dieses Modul braucht

| Primitive | wofür |
|---|---|
| Kreis um Mittelpunkt mit Radius | Taillenkreis, Saumkreis |
| Lot / rechter Winkel durch Punkt | Seitenlinie |
| Kreisbogen-Segment | Halb- und Viertelschnitt |

Das ist alles. **Drei Primitive, keine Kurvenanpassung.** Deshalb eignet sich
diese Seite als erstes Modul der Engine.

---

## Zuschnitt-Varianten (S. 44)

| Variante | Lagen | Stoffbrüche | Teile |
|---|---|---|---|
| ❑3 Doppellagig | 2 | 1 (vM oder hM) | Echter Glockenrock 2× |
| ❑4 Vierlagig | 4 | 4 (vM + hM als Stb oder Naht, Seitenlinie als Stb oder Naht) | Echter Glockenrock 4× |

Regeln aus dem Buch:
- Je nach Stoffbreite und Rocklänge müssen **zwei Kreisringe aneinandergenäht**
  werden — was für das Einnähen eines Reißverschlusses ohnehin günstiger ist.
- Der komplette Kreisring geht nur, wenn die Stofffläche groß genug ist.
- **Am Ende muss immer ein voller Kreisring zusammengenäht sein.**

---

## ⚠️ Offener Punkt: Saumweite bei Brautlänge

Der Buchfall rechnet mit `MoL = 50 cm` → Saumweite 3,86 m.

Bei bodenlang, z.B. `MoL = 105 cm`:
`r_SaW = 11,5 + 105 = 116,5` → `SaW = 2 · π · 116,5 ≈ 732 cm`

**7,3 Meter Saumweite.** Das ist eine Material- und Kostenentscheidung, keine
Konstruktionsfrage — aber sie muss vor dem Zuschnitt fallen.
`MoL` bleibt bis dahin ein offener Parameter (siehe `kleid_v001/DEFINITION.md`).
