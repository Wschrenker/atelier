# Geraden und Schnittpunkte

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Eine Nahtzugabe entsteht in der Engine nicht dadurch, dass eine Kante einfach
ein bisschen laenger gemalt wird. Jede Polygonkante wird erst zu einer
parallel verschobenen Geraden. Die neue Ecke ist dann der Schnittpunkt zweier
benachbarter verschobener Geraden. Genau dafuer ist `lineIntersection(a, b, c,
d)` in `src/geometry.js` da: Die Funktion nimmt zwei Punktpaare, betrachtet
die dadurch bestimmten unendlich langen Geraden und berechnet deren
Schnittpunkt.

Wichtig: Mathematisch wird hier eine Geraden-Geraden-Aufgabe geloest, keine
Segment-Segment-Kollision. Wenn der berechnete Parameter ausserhalb des
urspruenglichen Segments liegt, wird die Gerade gedanklich verlaengert. Das
passt zur Eckenbildung bei Offset-Polygonen, muss aber von echten
Schnittregeln oder Konstruktionsmassen getrennt bleiben. [Q1], [Q3], [Q4]

## Die Mathematik (Formeln sauber, nachvollziehbar)

Eine Gerade durch zwei Punkte `A = (a_x, a_y)` und `B = (b_x, b_y)` kann in
Parameterform geschrieben werden:

```text
d = B - A = (b_x - a_x, b_y - a_y)
L(t) = A + t d,  t in R
```

Fuer ein Segment waere `0 <= t <= 1` zusaetzlich zu pruefen. Fuer eine
unendlich lange Gerade ist `t` nicht auf diesen Bereich beschraenkt. Genau
diese Unterscheidung erklaert, warum eine Linie bis zu einem Eckpunkt
verlaengert werden kann. [Q1], [Q3], [Q4]

Alternativ kann eine Gerade in Koordinatenform beschrieben werden:

```text
a x + b y + c = 0
```

Der Schnitt zweier Geraden in Koordinatenform ist ein lineares
Gleichungssystem:

```text
a1 x + b1 y + c1 = 0
a2 x + b2 y + c2 = 0
```

Mit der Cramerschen Regel steht im Nenner die Determinante

```text
D = a1 b2 - a2 b1
```

Ist `D != 0`, gibt es genau einen Schnittpunkt. Ist `D = 0`, gibt es keine
eindeutige Loesung: Die Geraden sind parallel verschieden oder sie liegen
aufeinander und haben unendlich viele gemeinsame Punkte. [Q2], [Q3], [Q4]

In der Engine ist die gleiche Idee in der Parameterform umgesetzt. Fuer

```text
erste Gerade:  P(t) = A + t r
zweite Gerade: Q(u) = C + u s
r = B - A
s = D - C
```

gilt mit dem 2D-Kreuzprodukt

```text
cross(p, q) = p_x q_y - p_y q_x
```

der Parameter

```text
t = cross(C - A, s) / cross(r, s)
P = A + t r
```

Der Nenner `cross(r, s)` ist dieselbe Orientierung-/Flaechen-Determinante in
Vektorform. Wenn er `0` ist, sind die Richtungsvektoren kollinear; fuer die
Schnittpunktberechnung heisst das: kein eindeutiger Schnittpunkt. [Q1], [Q2],
[Q3]

Numerisch sollte in Gleitkomma-Code nicht blind auf exakt `0` getestet werden.
Die aktuelle Engine nutzt deshalb `EPSILON = 1e-8` und behandelt
`Math.abs(divisor) < EPSILON` als parallel oder fast parallel. Das ist eine
typische Implementationsidee, aber die konkrete Groesse von `EPSILON` ist ein
Engineering-Parameter und keine mathematische Konstante. Unsicher/zu pruefen:
Ob ein absoluter Grenzwert `1e-8` fuer alle spaeteren Massstaebe stabil genug
ist, haengt von den Koordinatenbereichen der Engine ab. [Q2], [Q5], [Q6]

## Anwendung in der Schnittkonstruktion (Bezug zum Code: lineIntersection, offsetSegment, Eckenbildung bei der Nahtzugabe)

Der Code-Anker in `src/geometry.js` passt direkt zur obigen Formel:

```text
ab = B - A
cd = D - C
divisor = cross(ab, cd)
t = cross(C - A, cd) / divisor
return A + t ab
```

`lineIntersection()` prueft keinen Parameterbereich `0 <= t <= 1`. Dadurch
schneidet die Engine die benachbarten Offset-Geraden auch dann, wenn sich die
urspruenglichen endlichen Segmente erst nach Verlaengerung treffen. Das ist
fuer Offset-Ecken bei Nahtzugaben wesentlich: `offsetSegment()` erzeugt
verschobene Kanten, und `offsetPolygon()` bildet daraus die Ecke, indem es je
zwei Nachbarsegmente als Geraden schneidet.

Bei `Math.abs(divisor) < EPSILON` gibt `lineIntersection()` aktuell `B`
zurueck. Mathematisch ist das kein belegter Schnittpunkt, sondern eine
Fallback-Entscheidung der Engine fuer parallele, deckungsgleiche oder
numerisch fast parallele Geraden. Diese Unterscheidung sollte in spaeteren
Implementationsentscheidungen sichtbar bleiben.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- [Q1] Belegt: 2D-Gerade als `A + t d`, 2D-Kreuzprodukt
  `cross(a,b) = a_x b_y - a_y b_x`, Schnittparameter
  `t = cross(a2-a1,d2) / cross(d1,d2)`, Kreuzprodukt als Orientierung/Flaeche.
  Titel: "Basic Geometry - Algorithms for Competitive Programming".
  URL: https://cp-algorithms.com/geometry/basic-geometry.html.
  Abrufdatum: 2026-06-19.
- [Q2] Belegt: Geraden in Koordinatenform, Loesung des 2x2-Systems mit
  Cramerscher Regel, Nenner-Determinante, Sonderfall `D = 0`, EPS-Vergleich in
  einer Beispielimplementierung.
  Titel: "Intersection Point of Lines - Algorithms for Competitive Programming".
  URL: https://cp-algorithms.com/geometry/lines-intersection.html.
  Abrufdatum: 2026-06-19.
- [Q3] Belegt: Geraden-Geraden-Schnittpunkt per Determinanten aus je zwei
  Punkten, Nenner `0` bei parallelen oder deckungsgleichen Geraden,
  Unterschied zwischen unendlich langer Gerade und Segment.
  Titel: "Line-line intersection".
  URL: https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection.
  Abrufdatum: 2026-06-19.
- [Q4] Belegt: Schnitt zweier Geraden als Cramersche-Regel-Formel und
  Segmentpruefung ueber Parameter `0 <= s,t <= 1`.
  Titel: "Intersection (geometry)".
  URL: https://en.wikipedia.org/wiki/Intersection_(geometry).
  Abrufdatum: 2026-06-19.
- [Q5] Belegt: Gleitkommazahlen sind endliche Naeherungen reeller Zahlen;
  Rundungsfehler sind charakteristisch fuer Floating-Point-Rechnung.
  Titel: "What Every Computer Scientist Should Know About Floating-Point Arithmetic".
  URL: https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html.
  Abrufdatum: 2026-06-19.
- [Q6] Belegt: Geometrische Algorithmen koennen durch ungenaue
  Gleitkommarechnung falsche oder widerspruechliche Entscheidungen treffen;
  robuste Geometrie trennt Praedikate und Konstruktionen und nutzt bei Bedarf
  exaktere Arithmetik.
  Titel: "CGAL 6.2 - Manual: Robustness Issues".
  URL: https://doc.cgal.org/latest/Manual/devman_robustness.html.
  Abrufdatum: 2026-06-19.
