# Rotation und Abnaeher-Verlegung

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Eine Rotation dreht einen Punkt oder eine ganze Punktgruppe um einen festen
Drehpunkt. Im Unterschied zur Verschiebung bleibt der Drehpunkt fest, waehrend
alle anderen Punkte auf Kreisbahnen um diesen Drehpunkt laufen. Mathematisch
wird eine 2D-Rotation mit Sinus und Kosinus beschrieben. [Q1], [Q2]

Fuer Schnittkonstruktion ist das methodisch wichtig, sobald ein Teil eines
Schnitts um einen Punkt geklappt werden soll: zum Beispiel beim spaeteren
Schliessen oder Verlegen eines Abnaehers oder beim Ausstellen von Weite. Das
ist hier nur die mathematische Methode. Fachliche Regeln, Zielpositionen und
Masse gehoeren spaeter zur Hofenbitzer-Transkription, nicht in diese Datei.

## Die Mathematik (Formeln sauber, nachvollziehbar)

Eine Drehung um den Ursprung `(0, 0)` mit Winkel `theta` wird in der
Standard-Konvention der Mathematik durch die Rotationsmatrix beschrieben:
[Q1], [Q2]

```text
[ cos(theta)  -sin(theta) ]
[ sin(theta)   cos(theta) ]
```

Auf einen Punkt `P = (x, y)` angewendet ergibt das:

```text
x_rot = x * cos(theta) - y * sin(theta)
y_rot = x * sin(theta) + y * cos(theta)
```

In dieser Standard-Konvention bedeutet ein positiver Winkel eine Drehung gegen
den Uhrzeigersinn in einem rechtshaendigen Koordinatensystem mit Y nach oben.
Andere Konventionen, zum Beispiel Bildschirm-/SVG-Koordinaten mit Y nach unten,
koennen die sichtbare Drehrichtung umkehren. Deshalb muss die Winkelkonvention
in der Engine dieselbe sein wie in `09_trigonometrie_und_polarkoordinaten.md`.
[Q1], [Q3], [Q4]

Eine Rotation um einen beliebigen Drehpunkt `O = (ox, oy)` ist keine neue
Formel, sondern eine Verkettung aus drei Schritten: zum Ursprung verschieben,
rotieren, zurueck verschieben. [Q3], [Q5], [Q6]

```text
x0 = x - ox
y0 = y - oy

xr = x0 * cos(theta) - y0 * sin(theta)
yr = x0 * sin(theta) + y0 * cos(theta)

x_neu = ox + xr
y_neu = oy + yr
```

Als Transformationsfolge:

```text
P_neu = O + R(theta) * (P - O)
```

Diese Form ist genau die Rechenidee "translate zum Ursprung -> rotieren ->
zurueck translieren". Allgemein lassen sich affine Transformationen als
Kombination aus linearer Transformation und Translation beschreiben; Rotation
und Translation sind typische Bausteine solcher Transformationen. [Q5], [Q6]

Eine Rotation ist eine starre Bewegung: Abstaende zum Drehpunkt bleiben gleich.
Das folgt daraus, dass Rotationsmatrizen orthogonal sind und geometrisch
Euclidean rotations beschreiben. Fuer Schnittteile bedeutet das: Wird eine
Punktgruppe um denselben Drehpunkt gedreht, veraendert die Rotation die Form
nicht, sondern nur ihre Lage und Richtung. [Q1], [Q7]

Fuer eine ganze Schnittkante oder ein Schnittteil wird die Punktformel auf
jeden Punkt angewendet:

```text
for each P in punkte:
  P_neu = O + R(theta) * (P - O)
```

Unsicher/zu pruefen: Welche Punkte fachlich zu welchem rotierenden Teil
gehoeren, welcher Drehpunkt verwendet wird und welcher Zielwinkel gilt, ist
keine allgemeine Mathematikfrage. Diese Entscheidungen muessen spaeter aus der
Schnittmethode belegt werden.

## Anwendung in der Schnittkonstruktion (ehrlich: heute vs. geplant)

Rotation ist im aktuellen Code noch nicht umgesetzt. `src/geometry.js` besitzt
mit `translatePoints(points, dx, dy)` die Verschiebe-Schwester der Rotation:

```text
P' = P + (dx, dy)
```

Eine Funktion wie `rotatePoint(...)` oder `rotatePointsAroundPivot(...)` gibt
es derzeit nicht. `src/draft.js` erzeugt Abnaeher aktuell mit `dart(...)` als
Dreieckslinien, schliesst oder verlegt aber keinen Abnaeher. Auch
`sideUplift` ist eine vereinfachte Schraegloesung ueber einen Y-Versatz, keine
Rotation. [Q8]

Geplant ist Rotation als Fundament fuer kuenftige Funktionen:
Abnaeher-Verlegung, ausgestellte oder Glockenroecke und Schulterschraegen bei
Oberteilen. Beim Abnaeher-Schliessen wuerde mathematisch ein Teil des
Schnitts um einen Drehpunkt, etwa den Abnaeherpunkt beziehungsweise bei
Oberteilen den Brustpunkt, rotiert, bis die relevante Abnaeherkante anliegt.
Die allgemeine Schnitttechnik, dass ein Abnaeher um seinen Fokus rotiert bzw.
per slash-and-spread/pin-and-pivot verlegt werden kann, ist belegt; die
konkrete Hofenbitzer-Regel ist hier aber noch offen. [Q9]

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- [Q1] Belegt: 2D-Rotationsmatrix, Formeln
  `x' = x cos(theta) - y sin(theta)` und
  `y' = x sin(theta) + y cos(theta)`, positive Drehrichtung in der genannten
  Standard-Konvention und Orthogonalitaet von Rotationsmatrizen.
  Titel: "Rotation matrix".
  URL: https://en.wikipedia.org/wiki/Rotation_matrix.
  Abrufdatum: 2026-06-19.
- [Q2] Belegt: Vektorrotation in `R^2` mit Matrix
  `[cos(theta) -sin(theta); sin(theta) cos(theta)]` und Hinweis auf
  unterschiedliche Konventionen fuer Achsen- vs. Objektrotation.
  Titel: "Rotation Matrix -- from Wolfram MathWorld".
  URL: https://mathworld.wolfram.com/RotationMatrix.html.
  Abrufdatum: 2026-06-19.
- [Q3] Belegt: Rotation um beliebigen Punkt als Abfolge: Punkt zum Ursprung
  verschieben, um den Ursprung rotieren, zurueck verschieben.
  Titel: "Maths - Rotation about Any Point".
  URL: https://www.euclideanspace.com/maths/geometry/affine/aroundPoint/.
  Abrufdatum: 2026-06-19.
- [Q4] Belegt: SVG-/Bildschirm-Koordinaten mit Ursprung oben links, X nach
  rechts, Y nach unten; Transformationsoperationen wie Translation und
  Rotation.
  Titel: "Scalable Vector Graphics (SVG) 1.1 - Coordinate Systems, Transformations and Units".
  URL: https://www.w3.org/TR/SVG11/coords.html.
  Abrufdatum: 2026-06-19.
- [Q5] Belegt: Affine Transformationen als Komposition linearer
  Transformationen und Translationen; Beispiele umfassen Translation und
  Rotation.
  Titel: "Affine transformation".
  URL: https://en.wikipedia.org/wiki/Affine_transformation.
  Abrufdatum: 2026-06-19.
- [Q6] Belegt: Transformationen koennen in SVG als Matrizen, Translation,
  Rotation, Skalierung usw. verschachtelt werden; der Effekt ist kumulativ.
  Titel: "Coordinate Systems, Transformations and Units - SVG 1.1".
  URL: https://www.w3.org/TR/SVG11/coords.html#EstablishingANewUserSpace.
  Abrufdatum: 2026-06-19.
- [Q7] Belegt: Rotation als Isometrie/starrer Abstandserhalt in der
  euklidischen Geometrie.
  Titel: "Rotation (mathematics)".
  URL: https://en.wikipedia.org/wiki/Rotation_(mathematics).
  Abrufdatum: 2026-06-19.
- [Q8] Lokaler Engine-Anker: `../src/geometry.js` und `../src/draft.js` -
  gelesen am 2026-06-19. Belegt den aktuellen Ist-Zustand:
  `translatePoints(...)` vorhanden, keine Rotationsfunktion; `dart(...)` als
  Abnaeher-Dreieck, `sideUplift` als einfache Y-Loesung.
- [Q9] Belegt: Ein Abnaeher kann um seinen Fokus rotiert bzw. mit
  slash-and-spread oder pin-and-pivot verlegt werden; fachliche Quelle nur als
  allgemeiner Kontext, Hofenbitzer-Regeln bleiben offen.
  Titel: "Dart (sewing)".
  URL: https://en.wikipedia.org/wiki/Dart_(sewing).
  Abrufdatum: 2026-06-19.
