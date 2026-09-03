# 05 Flaeche und Orientierung

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Eine geschlossene Kontur hat nicht nur eine Flaeche, sondern auch eine Laufrichtung: die Punkte koennen im Uhrzeigersinn oder gegen den Uhrzeigersinn angeordnet sein. Diese Richtung ist fuer Nahtzugaben wichtig, weil "aussen" auf der einen Seite der Linie liegt. Die Engine benutzt das Vorzeichen der Polygonflaeche, um diese Orientierung rechnerisch zu erkennen.

## Die Mathematik (Formeln sauber, nachvollziehbar)

Fuer ein geschlossenes Polygon mit Punkten `P0 ... P(n-1)` und `P(n) = P0` lautet die Shoelace-/Gauss-Formel:

```text
A = 1/2 * sum( x_i * y_(i+1) - x_(i+1) * y_i )
```

Der Betrag `abs(A)` ist die Flaeche. Das Vorzeichen enthaelt die Orientierung der Punktfolge. In einem klassischen X-rechts/Y-oben-System bedeutet ein Vorzeichen eine andere Laufrichtung als in einem Bildschirm-/SVG-aehnlichen X-rechts/Y-unten-System. Deshalb sollte die Engine nicht mit menschlichen Worten wie "Uhrzeigersinn" allein arbeiten, sondern konsequent mit dem berechneten Vorzeichen.

## Anwendung in der Schnittkonstruktion (Bezug zum geraden Rock / zum Code)

`../src/geometry.js` implementiert `polygonArea(points)` mit der Shoelace-Summe und verwendet das Ergebnis in `offsetSegment(...)`, um die Offset-Normale zu waehlen. Fuer den geraden Rock heisst das: Die Punktreihenfolge der Kontur muss stabil sein. Wenn spaeter ein Schnittteil andersherum sortiert wird, kann die Nahtzugabe nach innen statt nach aussen laufen. Ein Test sollte deshalb nicht nur Punkte, sondern auch Flaechenvorzeichen und Offset-Richtung pruefen.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- Wolfram MathWorld: "Shoelace Formula" - https://mathworld.wolfram.com/ShoelaceFormula.html - Abrufdatum: 2026-06-19. Belegt die Polygonflaechenformel ueber die Kreuzsummen.
- W3C: "Scalable Vector Graphics (SVG) 1.1 (Second Edition) - Coordinate Systems, Transformations and Units" - https://www.w3.org/TR/SVG11/coords.html - Abrufdatum: 2026-06-19. Belegt Koordinatensysteme und Achsen-/Transformationskontext; relevant fuer die Interpretation der Orientierung bei Y-nach-unten-Systemen.
- Lokaler Engine-Anker: `../src/geometry.js` - gelesen am 2026-06-19. Belegt `polygonArea(...)` und die Nutzung der Orientierung im Offset.
