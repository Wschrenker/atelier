# 02 Punkte und Vektoren

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Ein Punkt beschreibt eine Stelle im Schnitt, ein Vektor beschreibt eine Richtung mit Laenge. Damit kann man fachliche Angaben wie "von Punkt A 20 cm nach unten" eindeutig rechnen. Linien bestehen in der Engine praktisch aus Start- und Endpunkt. Ganze Punktmengen, etwa ein Schnittteil oder eine Abnaeherfigur, koennen mit demselben Vektor verschoben werden.

## Die Mathematik (Formeln sauber, nachvollziehbar)

Fuer zwei Punkte `A = (Ax, Ay)` und `B = (Bx, By)` ist der Vektor von A nach B:

```text
v = B - A = (Bx - Ax, By - Ay)
```

Eine relative Positionierung von A aus lautet:

```text
P = A + v = (Ax + vx, Ay + vy)
```

Eine Gerade oder ein Liniensegment zwischen A und B kann parametrisch geschrieben werden:

```text
L(t) = A + t * (B - A), 0 <= t <= 1
```

Eine Verschiebung einer Punktmenge `{P1, P2, ...}` um einen Vektor `v` ist:

```text
Pi' = Pi + v
```

Ein Abnaeher ist geometrisch ein Dreieck: eine Basis an der Schnittlinie, deren Breite die Abnaeher-Tiefe ist, und eine Spitze in Richtung Abnaeher-Laenge. Das ist nur die Geometrieform, nicht die fachliche Regel fuer Tiefe oder Laenge.

## Anwendung in der Schnittkonstruktion (Bezug zum geraden Rock / zum Code)

`../src/geometry.js` stellt mit `point(x, y)` den Grundtyp bereit und mit `translatePoints(points, dx, dy)` die Verschiebung von Punktmengen. `../src/draft.js` verwendet relative Konstruktion, z.B. Punkte fuer Taille, Huefte und Saum aus Breiten- und Tiefenwerten. Die Funktion `dart(centerX, intake, length)` beschreibt einen Abnaeher als Dreieck: links/rechts je `intake / 2` um die Mitte und Spitze bei der angegebenen Laenge. Fuer den geraden Rock duerfen spaeter nur die Hofenbitzer-Masse/Regeln die Werte liefern; die Mathematik hier sagt nur, wie daraus Punkte werden.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- OpenStax: "Calculus Volume 3, 2.1 Vectors in the Plane" - https://openstax.org/books/calculus-volume-3/pages/2-1-vectors-in-the-plane - Abrufdatum: 2026-06-19. Belegt Vektoren in Komponentenform, Addition und skalare Vielfache.
- W3C: "Scalable Vector Graphics (SVG) 1.1 (Second Edition) - Paths" - https://www.w3.org/TR/SVG11/paths.html - Abrufdatum: 2026-06-19. Belegt die Darstellung von Linien/Pfaden als Punktfolgen und Kurvenbefehle.
- Lokaler Engine-Anker: `../src/geometry.js` - gelesen am 2026-06-19. Belegt `point(...)` und `translatePoints(...)`.
- Lokaler Engine-Anker: `../src/draft.js` - gelesen am 2026-06-19. Belegt die aktuelle Abnaeher-Geometrie als Dreieck, ohne fachliche Massregel.
