# 12 Kurvenlaenge und Passung

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Bei geraden Linien ist die Laenge einfach der Abstand zwischen zwei Punkten.
Bei einer Kurve muss man entlang der Kurve messen. Das ist fuer Schnittmuster
wichtig, weil zwei Nahtstrecken nicht nur optisch zusammenpassen muessen: Wenn
eine Armloch-Kurve und eine Aermelkugel-Kurve zusammengenaeht werden sollen,
braucht die Engine spaeter eine Methode, um die Kurvenlaengen zu vergleichen
und eine Ziel-Laenge zu treffen. [Q1], [Q2], [Q8]

Wichtig fuer die Engine-Ehrlichkeit: Aktuell gibt es im Code keine
Kurvenlaengenmessung und keine Passungsberechnung. `sampleQuadratic(...)`
tastet nur eine quadratische Kurve in Punkte ab. Diese Punkte koennte man
spaeter als Polygonlinie messen, aber die Engine macht das heute noch nicht.

## Die Mathematik (Formeln sauber, nachvollziehbar)

Eine parametrisierte ebene Kurve wird als

```text
r(t) = (x(t), y(t)),  a <= t <= b
```

geschrieben. Ihre Bogenlaenge ist das Integral der Geschwindigkeit: [Q1],
[Q2]

```text
L = integral(a..b) sqrt( x'(t)^2 + y'(t)^2 ) dt
```

Fuer eine Bezier-Kurve setzt man `x(t)` und `y(t)` aus der Bezier-Formel ein.
Die Ableitung einer Bezier-Kurve kann aus den Kontrollpunkt-Differenzen
gebildet werden; fuer eine kubische Bezier-Kurve gilt zum Beispiel: [Q3],
[Q4]

```text
B'(t) =
  3(1 - t)^2  * (P1 - P0)
  + 6(1 - t)t * (P2 - P1)
  + 3t^2      * (P3 - P2)
```

Die Laenge der kubischen Kurve ist damit formal: [Q1], [Q3]

```text
L = integral(0..1) |B'(t)| dt
  = integral(0..1) sqrt( Bx'(t)^2 + By'(t)^2 ) dt
```

Fuer allgemeine kubische Bezier-Kurven gibt es keine einfache universelle
geschlossene Formel fuer diese Laenge. Es gibt Spezialklassen wie
Pythagorean-Hodograph-Kurven, bei denen Bogenlaenge in geschlossener Form
zugaenglich ist; normale kubische Bezier-Kurven fallen aber nicht automatisch
in diese Spezialklasse. Deshalb ist numerische Approximation der praktische
Standardweg. [Q5], [Q6], [Q7]

Die einfachste Approximation ist die Polygonlaenge. Man tastet die Kurve an
mehreren Stellen ab und addiert die Abstaende aufeinanderfolgender Punkte:
[Q2], [Q7]

```text
t_i = i / n
S_i = B(t_i)

L_approx =
  sum(i=0..n-1) distance(S_i, S_(i+1))

distance(A, B) =
  sqrt( (B_x - A_x)^2 + (B_y - A_y)^2 )
```

Mit groesserem `n` wird die Polygonlinie meistens genauer, kostet aber mehr
Rechenzeit und erzeugt mehr Punkte. Adaptive Unterteilung verbessert das:
Flache Kurvenabschnitte koennen grob bleiben, stark gekruemmte Abschnitte
werden weiter unterteilt. [Q7], [Q9]

Als vertiefte numerische Methode kann Gauss-Legendre-Quadratur verwendet
werden. Sie approximiert ein Integral durch gewichtete Funktionswerte an
speziellen Stuetzstellen: [Q10], [Q11]

```text
integral(-1..1) f(x) dx ~= sum(i=1..n) w_i * f(x_i)
```

Fuer Bezier-Bogenlaenge ist `f(t) = |B'(t)|`. Da Bezier-Parameter ueblich auf
`0..1` laufen, muss das Integrationsintervall passend transformiert werden.
[Q10], [Q11]

Das Passungsproblem laesst sich mathematisch als Zielwertproblem formulieren.
Wenn eine Kurve eine Ziel-Laenge `L_ziel` haben soll, definiert man eine
Fehlerfunktion:

```text
F(parameter) = Laenge(Kurve(parameter)) - L_ziel
```

Gesucht ist ein Parameterwert mit:

```text
F(parameter) = 0
```

Solche Gleichungen werden numerisch mit iterativen Nullstellensuchverfahren
geloest, zum Beispiel Bisektion, Sekantenverfahren oder Newton-aehnlichen
Verfahren. [Q12]

## Anwendung in der Schnittkonstruktion (ehrlich: heute quadratisch vs. geplant kubisch/Passung)

Heute: Die Engine hat nur `sampleQuadratic(...)`. Das erzeugt eine Folge von
Punkten, aber keine Laenge. Es gibt heute keine Funktion wie
`curveLength(...)`, keine adaptive Unterteilung, keine Gauss-Legendre-
Quadratur und keine automatische Anpassung von Kontrollpunkten an eine
Ziel-Laenge.

Geplant fuer Oberteile: Halsausschnitt, Armloch und Aermelkugel koennen als
Kurven modelliert werden. Fuer Passung waere der mathematische Ablauf:

```text
1. Kurve definieren, z.B. kubische Bezier-Stuecke.
2. Kurve numerisch messen.
3. Ziel-Laenge festlegen.
4. Kontrollpunkt(e) iterativ verschieben.
5. Nach jeder Verschiebung neu messen.
6. Stoppen, wenn |Laenge - Ziel-Laenge| <= Toleranz.
```

Fuer das Naht-Matching ohne Einhalteweite lautet die Zielbedingung:

```text
Laenge(Armloch-Kurve) = Laenge(Aermelkugel-Kurve)
```

Allgemeiner kann die Zielbedingung auch eine fachlich belegte Differenz
zulassen:

```text
Laenge(Aermelkugel) = Laenge(Armloch) + fachlich belegte Mehrweite
```

Unsicher/zu pruefen: Ob Hofenbitzer fuer die Aermelkugel exakt gleiche Laenge
oder eine Einhalteweite verlangt, darf hier nicht erfunden werden. Diese Datei
belegt nur die mathematische Methode: Kurvenlaenge messen, Zielwert
vergleichen, Kontrollpunkte iterativ anpassen.

Genauigkeit vs. Rechenaufwand: Eine grobe Polygonlaenge ist schnell, aber
ungenauer. Viele Segmente oder adaptive Unterteilung verbessern die
Approximation, kosten aber mehr Rechenzeit. Gauss-Legendre-Quadratur kann fuer
glatte Integranden sehr effizient sein, ist aber komplexer zu implementieren.
[Q7], [Q10], [Q11]

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- [Q1] Belegt: Bogenlaenge als Integral ueber die Norm der Ableitung,
  insbesondere fuer `r(t) = (x(t), y(t))` die Formel
  `integral sqrt(x'(t)^2 + y'(t)^2) dt`.
  Titel: "Arc Length -- from Wolfram MathWorld".
  URL: https://mathworld.wolfram.com/ArcLength.html.
  Abrufdatum: 2026-06-19.
- [Q2] Belegt: Bogenlaenge als Integral der Geschwindigkeit; alternativ als
  Grenzwert von Polygonketten; numerische Integration, wenn keine geschlossene
  Formel vorliegt.
  Titel: "Arc length".
  URL: https://en.wikipedia.org/wiki/Arc_length.
  Abrufdatum: 2026-06-19.
- [Q3] Belegt: Ableitungsformel einer allgemeinen Bezier-Kurve und explizite
  Ableitung der kubischen Bezier-Kurve.
  Titel: "Bezier curve".
  URL: https://en.wikipedia.org/wiki/B%C3%A9zier_curve.
  Abrufdatum: 2026-06-19.
- [Q4] Belegt: Die Ableitung einer Bezier-Kurve ist wieder eine Bezier-Kurve
  niedrigeren Grades mit Kontrollpunkten aus skalierten Kontrollpunkt-
  Differenzen.
  Titel: "Derivatives of a Bezier Curve".
  URL: https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/Bezier/bezier-der.html.
  Abrufdatum: 2026-06-19.
- [Q5] Belegt: Fuer kubische und hoehere Bezier-Kurven gibt es keine
  allgemeine geschlossene Bogenlaengenformel fuer alle moeglichen
  Kontrollpunkte; numerische Verfahren wie Legendre-Gauss und Polygon-
  Approximation werden praktisch verwendet.
  Titel: "A Primer on Bezier Curves".
  URL: https://pomax.github.io/bezierinfo/#arclength.
  Abrufdatum: 2026-06-19.
- [Q6] Belegt: Geschlossene Bogenlaenge ist fuer viele Kurven schwierig; selbst
  einfache Kurven wie Ellipsen haben keine elementare geschlossene
  Umfangsformel; Pythagorean-Hodograph-Kurven sind eine Spezialklasse mit
  geschlossener Bogenlaenge.
  Titel: "Pythagorean hodograph curve".
  URL: https://en.wikipedia.org/wiki/Pythagorean_hodograph_curve.
  Abrufdatum: 2026-06-19.
- [Q7] Belegt: Einfache Bezier-Approximation durch viele nahe Punkte und eine
  Folge von Liniensegmenten; adaptive rekursive Unterteilung bei Bedarf.
  Titel: "Bezier curve - Applications".
  URL: https://en.wikipedia.org/wiki/B%C3%A9zier_curve.
  Abrufdatum: 2026-06-19.
- [Q8] Belegt: Armscye/Armloch als Stoffkante, an die der Aermel genaeht wird;
  die Armscye-Laenge ist die Gesamtlaenge dieser Kante. Fachliche Details zur
  Aermel-Passung bleiben gegen Hofenbitzer zu pruefen.
  Titel: "Armscye".
  URL: https://en.wikipedia.org/wiki/Armscye.
  Abrufdatum: 2026-06-19.
- [Q9] Belegt: de-Casteljau-Unterteilung erzeugt zwei Bezier-Kurven desselben
  Grades und kann wiederholt angewendet werden; fuer Rendern und Kurvendesign
  nutzbar.
  Titel: "Subdividing a Bezier Curve".
  URL: https://pages.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/Bezier/bezier-sub.html.
  Abrufdatum: 2026-06-19.
- [Q10] Belegt: Gauss-Legendre-Quadratur approximiert Integrale ueber `[-1,1]`
  durch gewichtete Funktionswerte an Legendre-Stuetzstellen; Intervalle
  koennen transformiert werden.
  Titel: "Gauss-Legendre quadrature".
  URL: https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature.
  Abrufdatum: 2026-06-19.
- [Q11] Belegt: Legendre-Gauss-Quadratur fuer Bezier-Bogenlaenge und
  Transformation des Intervalls von Bezier-Parametern auf das
  Quadraturintervall.
  Titel: "A Primer on Bezier Curves".
  URL: https://pomax.github.io/bezierinfo/#arclength.
  Abrufdatum: 2026-06-19.
- [Q12] Belegt: Nullstellensuche als numerische Loesung von Gleichungen
  `f(x)=0`; iterative Methoden liefern Naeherungen.
  Titel: "Root-finding algorithm".
  URL: https://en.wikipedia.org/wiki/Root-finding_algorithm.
  Abrufdatum: 2026-06-19.
