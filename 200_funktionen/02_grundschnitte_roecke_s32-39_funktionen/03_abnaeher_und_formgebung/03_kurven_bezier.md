# 03 Kurven Bezier

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Viele Schnittlinien sind keine harten Geraden: Seitennaht, Hueftbogen, Armloch oder Ausschnitt sollen weich laufen. Eine quadratische Bezier-Kurve beschreibt so eine weiche Linie mit drei Punkten: Start, Kontrollpunkt und Ende. Die Engine kann die Kurve in kurze Liniensegmente abtasten, damit Exportformate und Polygonfunktionen damit arbeiten koennen.

## Die Mathematik (Formeln sauber, nachvollziehbar)

Eine quadratische Bezier-Kurve mit Start `P0`, Kontrollpunkt `P1` und Ende `P2` lautet:

```text
B(t) = (1 - t)^2 * P0 + 2 * (1 - t) * t * P1 + t^2 * P2
0 <= t <= 1
```

Dabei ist `t = 0` der Startpunkt und `t = 1` der Endpunkt. Fuer eine Abtastung in `n` Segmente berechnet man Punkte bei:

```text
t = i / n, i = 0, 1, ..., n
```

Die entstehenden Punkte bilden eine Polygonlinie, die die Kurve naeherungsweise darstellt. Mehr Segmente bedeuten meist glattere Kurve, aber auch mehr Punkte.

Unterschiede: Ein Kreisbogen ist ueber Mittelpunkt/Radius/Winkel definiert; eine Bezier-Kurve wird durch Kontrollpunkte gezogen/geformt. Ein Spline besteht typischerweise aus mehreren Kurvenstuecken mit gemeinsamen Anschlussbedingungen. Eine einzelne quadratische Bezier-Kurve ist daher einfach und gut steuerbar, aber nicht automatisch eine exakte fachliche Kurve.

## Anwendung in der Schnittkonstruktion (Bezug zum geraden Rock / zum Code)

`../src/geometry.js` enthaelt `sampleQuadratic(start, control, end, steps = 6)` und verwendet genau die quadratische Bezier-Formel. `../src/draft.js` nutzt diese Abtastung fuer die Seitenlinie zwischen Taille und Huefte beim Rock. Fuer Hofenbitzer muss spaeter entschieden werden, ob die dort gezeichneten Kurven mit quadratischen Beziers ausreichend beschreibbar sind oder ob bestimmte Kurven mehr Segmente, kubische Beziers oder eine fachlich definierte Kreisbogen-/Spline-Loesung brauchen.

Unsicher/zu pruefen: Die konkrete Kontrollpunktwahl fuer Hofenbitzer-Kurven darf nicht aus dem Bauch erfolgen. Sie gehoert in die spaetere Transkription/Pruefung der Buchseiten oder in dokumentierte Konstruktionsregeln.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- Wolfram MathWorld: "Bezier Curve" - https://mathworld.wolfram.com/BezierCurve.html - Abrufdatum: 2026-06-19. Belegt die mathematische Bezier-Definition.
- W3C: "Scalable Vector Graphics (SVG) 1.1 (Second Edition) - Paths" - https://www.w3.org/TR/SVG11/paths.html - Abrufdatum: 2026-06-19. Belegt SVG-Pfadbefehle fuer quadratische Bezier-Kurven, kubische Bezier-Kurven und elliptische Boegen.
- Lokaler Engine-Anker: `../src/geometry.js` - gelesen am 2026-06-19. Belegt die konkrete Abtastfunktion `sampleQuadratic(...)`.
- Lokaler Engine-Anker: `../src/draft.js` - gelesen am 2026-06-19. Belegt die aktuelle Verwendung einer quadratischen Kurve fuer die Rock-Seitenlinie.
