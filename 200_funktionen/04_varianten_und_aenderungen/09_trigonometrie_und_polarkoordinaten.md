# Trigonometrie und Polarkoordinaten

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Trigonometrie ist die Mathematik hinter schraegen Richtungen: Wenn eine
Konstruktionslinie nicht nur "nach rechts" oder "nach unten" laufen soll,
sondern mit einer bestimmten Laenge und einem bestimmten Winkel, zerlegt man
diese Richtung in einen X-Anteil und einen Y-Anteil. Sinus, Kosinus und Tangens
beschreiben diese Verhaeltnisse am rechtwinkligen Dreieck. [Q1], [Q2]

Polarkoordinaten sind dieselbe Idee als Punktkonstruktion: Statt einen Punkt
direkt als `(x, y)` zu notieren, beschreibt man ihn relativ zu einem Startpunkt
durch `Laenge` und `Winkel`. Das ist fuer spaetere Schraeglinien, Schulter-
schraegen, Ausstellungen oder andere Richtungs-Konstruktionen nuetzlich, ohne
hier fachliche Schnittmasse festzulegen. [Q3], [Q4]

## Die Mathematik (Formeln sauber, nachvollziehbar)

In einem rechtwinkligen Dreieck werden die Seiten relativ zum betrachteten
Winkel `alpha` benannt:

```text
sin(alpha) = Gegenkathete / Hypotenuse
cos(alpha) = Ankathete    / Hypotenuse
tan(alpha) = Gegenkathete / Ankathete
```

Die Tangens-Formel gilt auch als `tan(alpha) = sin(alpha) / cos(alpha)`,
solange `cos(alpha) != 0`. [Q1], [Q2]

In der Standard-Konvention der Mathematik zeigt `x` nach rechts, `y` nach
oben, der Winkel `alpha` startet an der positiven X-Achse und positive Winkel
drehen gegen den Uhrzeigersinn. Dann laesst sich ein Endpunkt aus Startpunkt,
Laenge und Winkel so berechnen: [Q3], [Q4], [Q5]

```text
dx = Laenge * cos(alpha)
dy = Laenge * sin(alpha)

X_neu = X_start + dx
Y_neu = Y_start + dy
```

Mit Polarkoordinaten `(r, alpha)` ist das dieselbe Umrechnung nach kartesischen
Koordinaten: [Q3], [Q4]

```text
x = r * cos(alpha)
y = r * sin(alpha)
```

Praktisch wichtig ist die Einheit des Winkels. In Mathematikquellen werden
Winkel oft in Grad oder Radiant angegeben; im Code rechnen JavaScript-
Funktionen wie `Math.sin()`, `Math.cos()` und `Math.tan()` mit Radiant. Die
Umrechnung lautet: [Q6], [Q7], [Q8], [Q9]

```text
alpha_rad  = alpha_grad * pi / 180
alpha_grad = alpha_rad  * 180 / pi
```

Die Achsenrichtung muss zur Engine passen. `01_koordinatensystem.md` und der
aktuelle `draft.js`-Anker beschreiben die praktische Engine-Konvention als
X nach rechts und Y nach unten. SVG beschreibt diese Bildschirm-Konvention
ebenfalls als Ursprung oben links, positive X-Achse nach rechts und positive
Y-Achse nach unten. [Q10], [Q11]

Wenn man einen mathematischen Winkel `alpha_math` aus einem Y-nach-oben-System
in ein Y-nach-unten-System uebernimmt, muss das Vorzeichen der Y-Komponente
bewusst entschieden werden. Eine haeufige Umrechnung lautet dann:

```text
X_neu = X_start + Laenge * cos(alpha_math)
Y_neu = Y_start - Laenge * sin(alpha_math)
```

Unsicher/zu pruefen: Fuer die Engine muss noch verbindlich festgelegt werden,
ob kuenftige Winkel fachlich als mathematische Winkel (X-Achse, gegen den
Uhrzeigersinn, Y nach oben) eingegeben werden oder direkt als Engine-Winkel
(X-Achse, Y nach unten) gelten. Ohne diese Festlegung koennen gleiche Gradwerte
visuell in entgegengesetzte Richtungen zeigen. [Q3], [Q10], [Q11]

## Anwendung in der Schnittkonstruktion (ehrlich: heute vs. geplant)

Trigonometrie und Rotation sind im aktuellen Code noch nicht umgesetzt. Der
heutige Code besitzt in `src/geometry.js` `translatePoints(...)` als reine
Verschiebung, aber keine Funktion fuer `pointFromAngle(...)`, `rotatePoint(...)`
oder `rotatePoints(...)`. In `src/draft.js` wird `sideUplift` als einfache
Y-Verschiebung der Seiten-Taille verwendet; `dart(...)` erzeugt Dreieckslinien
fuer Abnaeher, aber keine trigonometrische oder rotierende Konstruktion.
[Q11]

Geplant ist diese Mathematik als Fundament fuer kuenftige Funktionen, zum
Beispiel Schulterschraegen bei Oberteilen, schraege Konstruktionslinien,
Richtungen beim Ausstellen und spaeter Glockenroecke. Die Methode beschreibt
nur, wie ein Punkt aus Laenge und Winkel berechnet wird; sie legt keine
Hofenbitzer-Schnittregeln, keine Winkelwerte und keine Konstruktionsmasse fest.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- [Q1] Belegt: Sinus, Kosinus und Tangens als Seitenverhaeltnisse im
  rechtwinkligen Dreieck; Tangens als Gegenkathete durch Ankathete und als
  `sin/cos`.
  Titel: "Trigonometry".
  URL: https://en.wikipedia.org/wiki/Trigonometry.
  Abrufdatum: 2026-06-19.
- [Q2] Belegt: Sinus und Kosinus am rechtwinkligen Dreieck; Tangens als
  Verhaeltnis von Gegenkathete zu Ankathete.
  Titel: "Sine and cosine".
  URL: https://en.wikipedia.org/wiki/Sine_and_cosine.
  Abrufdatum: 2026-06-19.
- [Q3] Belegt: Polarkoordinaten als Abstand vom Pol plus Winkel zur
  Bezugsrichtung; Winkel-Konventionen in Grad/Radiant und Bezug zur Richtung.
  Titel: "Polar coordinate system".
  URL: https://en.wikipedia.org/wiki/Polar_coordinate_system.
  Abrufdatum: 2026-06-19.
- [Q4] Belegt: Umrechnung von Polarkoordinaten nach kartesischen Koordinaten
  mit `x = r cos(phi)` und `y = r sin(phi)`.
  Titel: "Polar coordinate system - Converting between polar and Cartesian coordinates".
  URL: https://en.wikipedia.org/wiki/Polar_coordinate_system#Converting_between_polar_and_Cartesian_coordinates.
  Abrufdatum: 2026-06-19.
- [Q5] Belegt: Ein Vektor mit Laenge `r` und Winkel `phi` zur X-Achse hat
  Endpunktkoordinaten `x = r cos(phi)` und `y = r sin(phi)`.
  Titel: "Rotation matrix".
  URL: https://en.wikipedia.org/wiki/Rotation_matrix.
  Abrufdatum: 2026-06-19.
- [Q6] Belegt: Radiant-Grad-Umrechnung, insbesondere
  `rad = grad * pi / 180` und `grad = rad * 180 / pi`.
  Titel: "Radian".
  URL: https://en.wikipedia.org/wiki/Radian.
  Abrufdatum: 2026-06-19.
- [Q7] Belegt: `Math.sin()` erwartet einen Winkel in Radiant.
  Titel: "Math.sin() - JavaScript | MDN".
  URL: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/sin.
  Abrufdatum: 2026-06-19.
- [Q8] Belegt: `Math.cos()` erwartet einen Winkel in Radiant; `Math.tan()`
  ist separat in [Q9] belegt.
  Titel: "Math.cos() - JavaScript | MDN".
  URL: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/cos.
  Abrufdatum: 2026-06-19.
- [Q9] Belegt: `Math.tan()` erwartet einen Winkel in Radiant.
  Titel: "Math.tan() - JavaScript | MDN".
  URL: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/tan.
  Abrufdatum: 2026-06-19.
- [Q10] Belegt: SVG-Initialkoordinaten mit Ursprung oben links, X nach rechts,
  Y nach unten; Transformationen koennen verschieben und rotieren.
  Titel: "Scalable Vector Graphics (SVG) 1.1 - Coordinate Systems, Transformations and Units".
  URL: https://www.w3.org/TR/SVG11/coords.html.
  Abrufdatum: 2026-06-19.
- [Q11] Lokaler Engine-Anker: `../src/geometry.js`, `../src/draft.js` und
  `01_koordinatensystem.md` - gelesen am 2026-06-19. Belegt den aktuellen
  Ist-Zustand: `translatePoints(...)` vorhanden, keine Trigonometrie- oder
  Rotationsfunktion; `sideUplift` als vereinfachte Y-Loesung.
