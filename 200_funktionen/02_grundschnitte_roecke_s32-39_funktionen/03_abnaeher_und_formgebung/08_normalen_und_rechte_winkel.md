# Normalen und rechte Winkel

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Eine Normale ist die Richtung, die rechtwinklig zu einer Linie steht. In der
Schnittkonstruktion braucht man sie, um eine Kante um einen Abstand nach links
oder rechts zu verschieben. Genau das macht `offsetSegment(a, b, distance,
orientation)` in `src/geometry.js`: Aus der Kantenrichtung wird eine
Einheitsnormale berechnet, und beide Endpunkte werden um `distance` in dieser
Normalenrichtung verschoben.

Das Thema ist rein mathematisch-methodisch: Es sagt, wie man eine rechte
Richtung, eine Einheitsnormale und eine Orientierung berechnet. Es legt keine
fachlichen Nahtzugaben, Schnittregeln oder Konstruktionsmasse fest.

## Die Mathematik (Formeln sauber, nachvollziehbar)

Fuer eine Kante mit Richtungsvektor

```text
d = (dx, dy) = (b_x - a_x, b_y - a_y)
```

erhaelt man senkrechte Vektoren durch eine Drehung um 90 Grad:

```text
links  / +90 Grad: n_l = (-dy,  dx)
rechts / -90 Grad: n_r = ( dy, -dx)
```

Die Drehmatrix fuer +90 Grad ist

```text
[ 0 -1 ]
[ 1  0 ]
```

und macht aus `(x, y)` den Vektor `(-y, x)`. Die Gegenrichtung `(y, -x)` ist
die Rotation um -90 Grad. [Q1], [Q2]

Warum diese Vektoren wirklich rechtwinklig sind, zeigt das Skalarprodukt:

```text
d dot n_l = dx*(-dy) + dy*dx = 0
d dot n_r = dx*dy + dy*(-dx) = 0
```

Allgemein gilt fuer nichtverschwindende Vektoren: Wenn `a dot b = 0`, stehen
sie orthogonal, also im rechten Winkel. [Q1], [Q3]

Damit der Verschiebeabstand unverfaelscht bleibt, braucht die Engine keine
beliebig lange Normale, sondern eine Einheitsnormale mit Laenge `1`. Fuer

```text
len = sqrt(dx^2 + dy^2)
```

gilt bei `len != 0`:

```text
unit_left  = (-dy / len,  dx / len)
unit_right = ( dy / len, -dx / len)
```

Diese Normalen haben Laenge `1`; deshalb verschiebt `unit_normal * distance`
die Kante genau um `distance`. Ein Nullvektor kann nicht normalisiert werden.
Die Engine behandelt diesen Grenzfall mit `length < EPSILON`. [Q1], [Q4], [Q5]

Die klassische Steigungsregel ist ebenfalls korrekt, aber fuer Code weniger
robust. Hat eine Gerade die Steigung

```text
m1 = dy / dx
```

und ist weder senkrecht noch waagrecht, dann hat eine senkrechte Gerade die
Steigung

```text
m2 = -1 / m1
```

Das entspricht `m1 * m2 = -1`. Grenzfall: Eine waagrechte Gerade hat Steigung
`0`, eine senkrechte Gerade hat undefinierte Steigung; diese beiden Richtungen
sind trotzdem rechtwinklig. Die Vektorvariante mit Rotation, Skalarprodukt und
Laenge vermeidet die Division durch `dx` und deckt diese Grenzfaelle sauberer
ab, solange der Kantenvektor nicht die Laenge `0` hat. [Q6], [Q7], [Q3]

Das 2D-"Kreuzprodukt" ist die z-Komponente des 3D-Kreuzprodukts zweier
2D-Vektoren:

```text
cross(a, b) = a_x b_y - a_y b_x
```

Sein Betrag entspricht der Flaeche des von `a` und `b` aufgespannten
Parallelogramms; sein Vorzeichen unterscheidet die Orientierung: positive
Werte fuer Drehung gegen den Uhrzeigersinn, negative fuer Drehung im
Uhrzeigersinn. Fuer Normalen ist das nuetzlich, weil "links" und "rechts" einer
Kante keine Laengenfrage, sondern eine Orientierungsfrage sind. [Q1]

## Anwendung in der Schnittkonstruktion (Bezug zum Code: lineIntersection, offsetSegment, Eckenbildung bei der Nahtzugabe)

`offsetSegment()` liest die Kantenrichtung aus:

```text
dx = b.x - a.x
dy = b.y - a.y
length = hypot(dx, dy)
```

Dann wird eine der beiden Normalenrichtungen gewaehlt:

```text
direction = orientation >= 0 ? 1 : -1
nx = direction *  dy / length
ny = direction * -dx / length
```

Ohne den Faktor `direction` ist `(dy / length, -dx / length)` die
Einheitsnormale aus der -90-Grad-Drehung. Der Faktor kehrt die Normale um,
wenn die Polygonorientierung es verlangt. Anschliessend werden beide Endpunkte
um `distance` verschoben:

```text
A' = A + distance * (nx, ny)
B' = B + distance * (nx, ny)
```

So entstehen parallele Offset-Segmente. Die eigentliche Ecke der Nahtzugabe
entsteht danach nicht in `offsetSegment()`, sondern in `lineIntersection()`:
Benachbarte Offset-Segmente werden als Geraden geschnitten. Daher ist
`08_normalen_und_rechte_winkel.md` das methodische Fundament fuer die
Offset-Segmente, waehrend `07_geraden_und_schnittpunkte.md` das Fundament fuer
die Eckbildung ist.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- [Q1] Belegt: Skalarprodukt in Koordinaten, Orthogonalitaet bei
  Skalarprodukt `0`, Norm/Laenge, 2D-Kreuzprodukt
  `cross(a,b) = a_x b_y - a_y b_x`, Orientierungsvorzeichen und 90-Grad-
  Rotation `(-y,x)` im Zusammenhang mit dem 2D-Kreuzprodukt.
  Titel: "Basic Geometry - Algorithms for Competitive Programming".
  URL: https://cp-algorithms.com/geometry/basic-geometry.html.
  Abrufdatum: 2026-06-19.
- [Q2] Belegt: 2D-Rotationsmatrix, neue Koordinaten nach Rotation,
  insbesondere die Matrizen fuer 90 Grad und 270 Grad.
  Titel: "Rotation matrix".
  URL: https://en.wikipedia.org/wiki/Rotation_matrix.
  Abrufdatum: 2026-06-19.
- [Q3] Belegt: Geometrische Definition des Skalarprodukts
  `a dot b = ||a|| ||b|| cos(theta)` und daraus `a dot b = 0` bei
  `theta = 90 Grad`.
  Titel: "Dot product".
  URL: https://en.wikipedia.org/wiki/Dot_product.
  Abrufdatum: 2026-06-19.
- [Q4] Belegt: Euklidische Norm `||a|| = sqrt(a1^2 + a2^2 + a3^2)`,
  Normierung eines nichtverschwindenden Vektors durch Division durch seine
  Laenge, Nullvektor kann nicht normalisiert werden.
  Titel: "Euclidean vector".
  URL: https://en.wikipedia.org/wiki/Euclidean_vector.
  Abrufdatum: 2026-06-19.
- [Q5] Belegt: Normale als senkrechter Vektor; Einheitsnormale als Normale der
  Laenge `1`.
  Titel: "Normal (geometry)".
  URL: https://en.wikipedia.org/wiki/Normal_(geometry).
  Abrufdatum: 2026-06-19.
- [Q6] Belegt: Steigung `m = Delta y / Delta x`, vertikale Gerade mit
  undefinierter Steigung, waagrechte Gerade mit Steigung `0`, senkrechte
  Geraden mit Steigungsprodukt `-1` bzw. horizontal/vertikal als Sonderfall.
  Titel: "Slope".
  URL: https://en.wikipedia.org/wiki/Slope.
  Abrufdatum: 2026-06-19.
- [Q7] Belegt: In einer Herleitung zum Lot auf eine Gerade wird die
  senkrechte Steigung als negativer Kehrwert der Ausgangssteigung verwendet.
  Titel: "Distance from a point to a line".
  URL: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line.
  Abrufdatum: 2026-06-19.
