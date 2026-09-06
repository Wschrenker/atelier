# Echter Glockenrock — Vollglocke/Tellerrock (S.44)

Quelle: Hofenbitzer, *Grundschnitte und Modellentwicklungen*, Band 1, 3. Auflage 2024.

Foto: `../Photos-3-001/20260617_160345.jpg`

Fotoabgleich: 2026-06-21 (Claude/Opus + Codex), inkl. zweitem Foto-gegen-Text-Durchgang.
Alle Zahlen und Formeln digit-für-digit gegen das Foto verifiziert (Berechnungsbox, NZg-Formel, Abb. ☐2).
**Status: fachlich freigegeben durch Werner/Munkhuu am 2026-06-21.**

---

## Prinzip

- Glockenröcke können aus einem oder mehreren Kreisringen oder Kreisringsegmenten gearbeitet werden.
- Der echte Glockenrock besteht aus einem **Vollkreisring** und wird deshalb auch Vollglocke oder
  Tellerrock genannt.
- Er umspielt die Hüften und bildet abhängig von Material und Saumweite weich fallende Glocken.
- Volants werden nach demselben Kreisringprinzip konstruiert; an die Stelle der Bundnaht tritt die
  Volant-Ansatznaht.

Wichtig: Halb- oder Viertelkreis auf der Seite bezeichnen die Schablonen-/Faltaufteilung beim Zuschnitt.
Das fertige Kleidungsstück muss einen vollständigen Kreisring bilden.

## Berechnungen — Beispiel

Gegeben:

- Taillenweite **TaW = 72 cm**
- Modelllänge **MoL = 50 cm**
- π wird im Buchbeispiel mit **3,14** eingesetzt.

Innerer Radius/Taillenkreis:

```text
rTaW = TaW : (2 × π)
     = 72 cm : (2 × 3,14)
     = 11,5 cm
```

Äußerer Radius/Saumkreis:

```text
rSaW = rTaW + MoL
     = 11,5 cm + 50 cm
     = 61,5 cm
```

Saumweite:

```text
SaW = 2 × π × rSaW
    = 2 × 3,14 × 61,5 cm
    = 386,2 cm
```

## 1. Konstruktion

1. Taillenweite und Rocklänge bestimmen und die Berechnungen durchführen.
2. Je nach Stoffbreite und Rocklänge einen halben oder einen viertel Kreisring konstruieren; der Stoff
   wird entsprechend doppelt oder vierfach in den Bruch gelegt. Die Konstruktion kann auf Schnittpapier
   oder direkt auf dem Stoff erfolgen.
3. Grundlinie des Kreises und Kreismittelpunkt bestimmen.
4. Um den Mittelpunkt einen Kreis mit dem inneren Radius **rTaW** zeichnen: Taillenkreis.
5. Um denselben Mittelpunkt einen Kreis mit dem äußeren Radius **rSaW** zeichnen: Saumkreis.
6. Rechtwinklig durch den Mittelpunkt eine zweite Linie bis zum äußeren Kreisbogen zeichnen:
   Seitenlinie.

## 2. Zuschnitt

- Abhängig von Stoffbreite und Rocklänge können zwei Kreisringteile zusammengenäht werden; dies ist
  für das Einnähen eines Reißverschlusses günstig.
- Ein Zuschnitt im Stoffbruch ist ebenfalls möglich.
- Wird ein vollständiger Kreisring aus einer ausreichend großen Stofffläche zugeschnitten, muss an der
  Taille ein Schlitz für den Reißverschluss berücksichtigt werden.
- Radiusformel bei einer solchen Naht-/Schlitzlösung:

```text
rTaW = (TaW + 2 × NZg) : (2 × π)
```

`NZg` ist dabei die gewählte Nahtzugabe als Parameter; S.44 schreibt keinen festen Zahlenwert dafür vor.

- Auch ein Zuschnitt mit einer 1/4-Schablone ist möglich, mit oder ohne Nähte.
- Am Ende muss immer ein voller Kreisring zusammengenäht sein.

### Gezeigte Falt-/Zuschnittvarianten

1. **Doppellagiger Zuschnitt (1 Stoffbruch):** Papier oder Stoff einmal gefaltet; Schablone „Echter
   Glockenrock 2×“.
2. **Vierlagiger Zuschnitt:** Papier oder Stoff zweimal gefaltet; Schablone „Echter Glockenrock 4×“.
   Die Bildunterschrift lautet „Vierlagiger Zuschnitt (4 Stoffbrüche)“.
3. Kanten können je nach Variante Seitenlinie, Stoffbruch oder Naht sein; vM und hM können als Stoffbruch
   oder Naht ausgeführt werden.

---

## Digitaler Verifikationsstand

- Alle Formeln, Konstruktionsschritte und Zuschnittregeln von S.44 sind lesbar erfasst.
- Der echte Glockenrock ist eindeutig ein **Vollkreisring**, nicht ein Viertelkreisring.
- `NZg` bleibt ein variabler Eingabewert; auf S.44 fehlt kein fester Wert.
- Das Buchbeispiel rechnet mit π = 3,14. Ob die Engine intern 3,14 oder höhere Präzision verwendet,
  ist eine dokumentierte Implementierungsentscheidung und keine offene Lesestelle.
- Keine implementierbare Stelle ist `UNLESBAR`.
- Abb. ☐2: der innere Kreis ist als „Länge der Ansatznaht (z.B. Bund, Passe, Saum), hier der Taillenweite (TaW)"
  beschriftet; die Radien sind rTaW/rSaW, Achsen „Grundlinie"/„Seitenlinie", der äußere Radius als
  „Rocklänge = MoL (oder Volantlänge)". Damit gilt die rTaW-Formel für jede Ansatznaht, nicht nur den Bund.
- Menschliche Freigabe am Buch: **erteilt durch Werner/Munkhuu am 2026-06-21**.
