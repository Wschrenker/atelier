# 04 Nahtzugabe Offset

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Die Nahtlinie ist die eigentliche Konstruktionslinie. Die Schnittlinie liegt darum herum in einem festen Abstand: der Nahtzugabe. Rechnerisch ist das ein Parallelversatz der Kontur. Bei geraden Segmenten ist das einfach; an Ecken muss die Engine entscheiden, wo sich die verschobenen Nachbarsegmente treffen.

## Die Mathematik (Formeln sauber, nachvollziehbar)

Ein Segment von `A = (Ax, Ay)` nach `B = (Bx, By)` hat Richtung:

```text
d = B - A = (dx, dy)
L = sqrt(dx^2 + dy^2)
```

Eine senkrechte Einheitsnormale ist:

```text
n1 = ( dy / L, -dx / L )
n2 = ( -dy / L, dx / L )
```

Welche Normale nach aussen zeigt, haengt von der Polygon-Orientierung ab. Ein Segment-Offset mit Abstand `s` ist:

```text
A' = A + s * n
B' = B + s * n
```

An einer Ecke werden die zwei verschobenen Geraden der angrenzenden Segmente geschnitten. Der Schnittpunkt wird zur neuen Ecke. Bei parallelen oder fast parallelen Geraden ist der Schnitt numerisch instabil; dann braucht man eine robuste Sonderbehandlung.

## Anwendung in der Schnittkonstruktion (Bezug zum geraden Rock / zum Code)

`../src/geometry.js` bildet genau diese vereinfachte Offset-Logik ab: `offsetSegment(...)` verschiebt ein Segment entlang einer Normale, `lineIntersection(...)` schneidet benachbarte Offset-Linien, `offsetPolygon(...)` erzeugt daraus die versetzte Kontur. Fuer einen geraden Rock ist das ein guter erster mathematischer Baustein fuer gleichmaessige Nahtzugaben.

Grenzen/unsicher: Das aktuelle Verfahren ist eine einfache miterartige Polygonloesung. Fuer konkave Stellen, sehr grosse Zugaben, Selbstschnitte, Rundungen oder unterschiedliche Eckenarten koennen robustere Verfahren noetig sein, z.B. Clipping/Buffering oder Straight-Skeleton-basierte Polygon-Offsets. Aus DXF-Referenzen darf dabei keine Schnittregel abgeleitet werden; DXF ist nur Export-/Vergleichsformat.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- CGAL: "2D Straight Skeleton and Polygon Offsetting" - https://doc.cgal.org/latest/Straight_skeleton_2/index.html - Abrufdatum: 2026-06-19. Belegt Polygon-Offsetting als eigenstaendiges geometrisches Problem und die Nutzung von Straight Skeletons fuer Offset-Konturen.
- Wolfram MathWorld: "Line-Line Intersection" - https://mathworld.wolfram.com/Line-LineIntersection.html - Abrufdatum: 2026-06-19. Belegt die mathematische Bestimmung von Schnittpunkten zweier Geraden.
- Wolfram MathWorld: "Shoelace Formula" - https://mathworld.wolfram.com/ShoelaceFormula.html - Abrufdatum: 2026-06-19. Belegt die Flaechenformel, deren Vorzeichen als Orientierungsinformation fuer Offset-Richtung genutzt werden kann.
- Lokaler Engine-Anker: `../src/geometry.js` - gelesen am 2026-06-19. Belegt `offsetSegment(...)`, `lineIntersection(...)` und `offsetPolygon(...)`.
