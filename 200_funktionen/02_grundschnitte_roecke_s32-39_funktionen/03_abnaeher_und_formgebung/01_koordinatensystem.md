# 01 Koordinatensystem

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Ein Schnittmusterprogramm braucht ein festes X/Y-System, sonst bedeutet "20 cm nach unten" einmal Plus und einmal Minus. Fuer die Engine ist wichtig: ein Punkt hat Koordinaten in Millimetern, die X-Achse laeuft waagerecht, die Y-Achse muss projektweit gleich interpretiert werden. In SVG- und Bildschirmkoordinaten liegt der Ursprung oft oben links, X zeigt nach rechts und Y zeigt nach unten. Fuer Rock/Hose ist "oben links" als Nullpunkt eine sinnvolle Projektkonvention; fuer Oberteile nennt der Auftrag "oben hinten am 7. Halswirbel" als Konvention, fachlich aber noch gegen die Buchquelle zu pruefen.

## Die Mathematik (Formeln sauber, nachvollziehbar)

Ein Punkt ist `P = (x, y)`. Eine Verschiebung um `dx` und `dy` ergibt:

```text
P' = (x + dx, y + dy)
```

Wenn die Y-Achse nach unten zeigt, bedeutet "nach unten" rechnerisch `+dy`. Wenn die Y-Achse nach oben zeigt, waere dieselbe fachliche Bewegung `-dy`. Diese Entscheidung darf nicht pro Funktion wechseln.

Einheiten werden intern als Millimeter gefuehrt. Die einfache Umrechnung lautet:

```text
mm = cm * 10
```

## Anwendung in der Schnittkonstruktion (Bezug zum geraden Rock / zum Code)

`../src/draft.js` arbeitet bereits so, als ob positive Y-Werte nach unten laufen: Laengen, Huefttiefe und Saumtiefe werden als positive Y-Koordinaten aufgebaut; ein "sideUplift" ist dagegen negativ. `../src/geometry.js` kennt nur Punkte und Rechenoperationen, deshalb muss `draft.js` die Achsenkonvention sauber einhalten. Fuer den geraden Rock sollte die spaetere Hofenbitzer-Transkription deshalb zuerst in dieselbe Millimeter- und Y-nach-unten-Konvention uebersetzt werden, bevor Formeln in Code gehen.

Unsicher/zu pruefen: Die textilfachlichen Nullpunkte "oben links fuer Rock/Hose" und "7. Halswirbel fuer Oberteile" stammen aus dem Werner-Auftrag, nicht aus einer hier belegten Webquelle. Sie duerfen als Projektkonvention notiert werden, sollten aber gegen Hofenbitzer Band 1/2 geprueft werden.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- W3C: "Scalable Vector Graphics (SVG) 1.1 (Second Edition) - Coordinate Systems, Transformations and Units" - https://www.w3.org/TR/SVG11/coords.html - Abrufdatum: 2026-06-19. Belegt Koordinatensysteme, Einheiten und Transformationen in SVG; relevant fuer Ursprung/Achsen im Export.
- W3C: "CSS Values and Units Module Level 4" - https://www.w3.org/TR/css-values-4/ - Abrufdatum: 2026-06-19. Belegt absolute Laengeneinheiten und die Beziehung von `cm` und `mm`.
- Lokaler Engine-Anker: `../src/draft.js` - gelesen am 2026-06-19. Belegt die aktuelle Engine-Konvention mit Millimetern und positiver Y-Richtung nach unten.
- Projektvorgabe Werner-Auftrag: "Mathematik-Recherche fuer die Schnittkonstruktion" - Chat-Auftrag vom 2026-06-19, keine Web-URL. Belegt die gewuenschten Nullpunkt-Konventionen als Projektannahme; fachlich unsicher/zu pruefen.
