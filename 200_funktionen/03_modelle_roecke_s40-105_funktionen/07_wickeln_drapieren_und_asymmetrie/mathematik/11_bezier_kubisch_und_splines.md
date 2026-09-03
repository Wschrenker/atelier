# 11 Bezier kubisch und Splines

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

`03_kurven_bezier.md` beschreibt die quadratische Bezier-Kurve: Startpunkt,
ein Kontrollpunkt, Endpunkt. Eine kubische Bezier-Kurve erweitert das um einen
zweiten Kontrollpunkt. Dadurch kann man Anfangs- und Endrichtung getrennt
formen. Das ist fuer weiche Schnittlinien interessant, weil ein
Halsausschnitt, Armloch, eine Aermelkugel oder eine Hueftkurve oft nicht nur
"irgendwie rund" sein sollen, sondern an beiden Enden passend aus einer
Nachbarlinie herauslaufen muessen. [Q1], [Q2], [Q3]

Ein Spline ist hier keine neue Zauberformel, sondern eine Kette mehrerer
Bezier-Stuecke. Jedes Stueck beschreibt einen kurzen Kurvenabschnitt; an den
Uebergaengen legt man fest, wie glatt diese Stuecke zusammenlaufen. [Q4],
[Q5]

Wichtig fuer die Engine-Ehrlichkeit: Im aktuellen Code ist kubische Bezier
noch nicht umgesetzt. `src/geometry.js` enthaelt heute nur
`sampleQuadratic(start, control, end, steps = 6)`, also quadratische Abtastung
in Liniensegmente. Diese Datei ist Recherche fuer eine spaetere Erweiterung,
nicht Dokumentation von bereits vorhandenem Code.

## Die Mathematik (Formeln sauber, nachvollziehbar)

Die allgemeine Bezier-Kurve mit Kontrollpunkten `P0 ... Pn` wird in
Bernstein-Form geschrieben als: [Q1], [Q2]

```text
B(t) = sum(i=0..n) binom(n, i) * (1 - t)^(n - i) * t^i * P_i
0 <= t <= 1
```

Fuer die kubische Bezier-Kurve gilt `n = 3`. Mit Startpunkt `P0`,
Kontrollpunkt `C1 = P1`, Kontrollpunkt `C2 = P2` und Endpunkt `P3` lautet die
Formel: [Q2], [Q6]

```text
B(t) =
  (1 - t)^3       * P0
  + 3(1 - t)^2 t * C1
  + 3(1 - t) t^2 * C2
  + t^3           * P3
0 <= t <= 1
```

Eine einfache Abtastung funktioniert wie bei `03_kurven_bezier.md`: Man waehlt
eine Anzahl `n` von Segmenten und berechnet Punkte bei festen Parameterwerten:
[Q2], [Q7]

```text
t_i = i / n,  i = 0, 1, ..., n
P_i_sample = B(t_i)
```

Die Punkte werden anschliessend als Polygonlinie verbunden. Mehr Segmente
geben meistens eine bessere Annaeherung, erzeugen aber mehr Punkte. Eine
adaptive Unterteilung kann dort feiner teilen, wo die Kurve staerker gekruemmt
ist, und dort grober bleiben, wo sie fast gerade ist. [Q7], [Q8]

Der Unterschied zu quadratisch ist die Zahl der Formhebel:

```text
quadratisch: P0, C,  P2   -> ein Kontrollpunkt
kubisch:     P0, C1, C2, P3 -> zwei Kontrollpunkte
```

Kubische Kurven sind in Computergraphik und Vektorformaten sehr verbreitet;
SVG beschreibt kubische Bezier-Segmente mit Startpunkt, Endpunkt und zwei
Kontrollpunkten. Quadratische und kubische Bezier-Kurven sind beide ueblich,
aber fuer komplexere Formen werden oft mehrere niedrige Kurvenstuecke
zusammengesetzt. [Q3], [Q7]

Die Tangenten an den Enden einer kubischen Bezier-Kurve ergeben sich aus der
Ableitung: [Q2], [Q5]

```text
B'(t) =
  3(1 - t)^2       * (P1 - P0)
  + 6(1 - t)t      * (P2 - P1)
  + 3t^2           * (P3 - P2)

B'(0) = 3 * (P1 - P0)
B'(1) = 3 * (P3 - P2)
```

Damit zeigen die Strecken `P0 -> P1` und `P2 -> P3` die Start- und Endtangente
der Kurve an. Praktisch heisst das: Die beiden inneren Kontrollpunkte wirken
wie Tangenten-Griffe an Anfang und Ende. [Q1], [Q5]

Bei einer Verkettung zweier kubischer Bezier-Stuecke, zum Beispiel

```text
erstes Stueck:  P0, P1, P2, P3
zweites Stueck: P3, P4, P5, P6
```

gibt es verschiedene Glattheitsstufen: [Q4], [Q5]

```text
C0 / G0: P3 ist gemeinsamer End-/Startpunkt.
G1:      P2, P3, P4 liegen auf einer Linie; die Tangentenrichtung passt.
C1:      Die Ableitungen am Uebergang sind gleich.
         Bei zwei kubischen Stuecken gleicher Parametrisierung heisst das:
         P4 = 2 * P3 - P2
```

`G1` sorgt geometrisch fuer keinen sichtbaren Knick, laesst aber
unterschiedliche "Geschwindigkeit" in der Parametrisierung zu. `C1` ist
strenger: Richtung und Ableitungsbetrag passen zusammen. [Q4], [Q5]

## Anwendung in der Schnittkonstruktion (ehrlich: heute quadratisch vs. geplant kubisch/Passung)

Heute: `src/geometry.js` kann quadratische Bezier-Kurven mit
`sampleQuadratic(...)` in kurze Segmente abtasten. Eine kubische Funktion wie
`sampleCubic(...)` gibt es aktuell nicht. Auch Splines, G1-/C1-Pruefung und
automatische Tangenten-Griffe sind heute nicht im Code.

Geplant: Kubische Bezier-Kurven koennen spaeter fuer Halsausschnitt, Armloch,
Aermelkugel und gegebenenfalls Hueftkurven genutzt werden, wenn ein einzelner
quadratischer Kontrollpunkt nicht genug Formfreiheit bietet. Die mathematische
Aufgabe waere dann:

```text
1. fachlich belegte Punkte aus Hofenbitzer uebernehmen,
2. daraus P0, C1, C2, P3 bestimmen,
3. die Kurve in Segmente abtasten,
4. die Segmente fuer Anzeige, Export und Laengenrechnung verwenden.
```

Unsicher/zu pruefen: Diese Datei legt keine Kontrollpunktpositionen fuer
Hofenbitzer fest. Ob Halsausschnitt, Armloch, Aermelkugel oder Hueftkurve mit
kubischen Bezier-Stuecken, Kreisbogen, B-Splines oder einer anderen Kurvenform
besser beschrieben werden, muss spaeter aus der fachlichen Vorlage und aus
Testausdrucken entschieden werden.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- [Q1] Belegt: Bezier-Kurve als Bernstein-Bezier-Kurve aus `n + 1`
  Kontrollpunkten; Endpunkte, Tangenten an den ersten/letzten Kontrollpolygon-
  Strecken; niedrige Kurvenstuecke statt hoher Grade.
  Titel: "Bezier Curve -- from Wolfram MathWorld".
  URL: https://mathworld.wolfram.com/BezierCurve.html.
  Abrufdatum: 2026-06-19.
- [Q2] Belegt: allgemeine explizite Bezier-Formel mit Binomialkoeffizienten,
  Bernstein-Basispolynomen und Ableitungsformel.
  Titel: "Bezier curve".
  URL: https://en.wikipedia.org/wiki/B%C3%A9zier_curve.
  Abrufdatum: 2026-06-19.
- [Q3] Belegt: SVG-Pfade enthalten Linien, kubische und quadratische
  Bezier-Kurven; ein kubisches SVG-Segment hat Startpunkt, Endpunkt und zwei
  Kontrollpunkte; mehrere Koordinatensaetze koennen eine Polybezier bilden.
  Titel: "Paths - SVG 1.1 (Second Edition)".
  URL: https://www.w3.org/TR/SVG11/paths.html.
  Abrufdatum: 2026-06-19.
- [Q4] Belegt: Composite Bezier Curve / Bezier Spline als Reihe von
  Bezier-Kurven; C0, C1 und G1-Stetigkeit an Uebergaengen.
  Titel: "Composite Bezier curve".
  URL: https://en.wikipedia.org/wiki/Composite_B%C3%A9zier_curve.
  Abrufdatum: 2026-06-19.
- [Q5] Belegt: Ableitung einer Bezier-Kurve, Endtangenten an erster/letzter
  Kontrollpolygon-Strecke, C0/G1/C1-Bedingungen beim Verbinden zweier
  Bezier-Kurven.
  Titel: "Derivatives of a Bezier Curve".
  URL: https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/Bezier/bezier-der.html.
  Abrufdatum: 2026-06-19.
- [Q6] Belegt: kubische Bezier-Definition in einer Kreisbogens-Approximation
  mit vier Punkten.
  Titel: "Composite Bezier curve - Approximating circular arcs".
  URL: https://en.wikipedia.org/wiki/Composite_B%C3%A9zier_curve.
  Abrufdatum: 2026-06-19.
- [Q7] Belegt: Bezier-Kurven sind in Computergraphik fuer glatte Kurven
  verbreitet; quadratische und kubische Kurven sind die haeufigen niedrigen
  Grade; Abtastung durch viele Punkte ist die einfache Raster-/Polygon-
  Naeherung; adaptive rekursive Unterteilung ist eine uebliche Methode.
  Titel: "Bezier curve - Applications".
  URL: https://en.wikipedia.org/wiki/B%C3%A9zier_curve.
  Abrufdatum: 2026-06-19.
- [Q8] Belegt: de-Casteljau-Unterteilung zerlegt eine Bezier-Kurve bei einem
  Parameterwert in zwei Bezier-Kurven desselben Grades; wiederholte
  Unterteilung ist moeglich.
  Titel: "Subdividing a Bezier Curve".
  URL: https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/Bezier/bezier-sub.html.
  Abrufdatum: 2026-06-19.
