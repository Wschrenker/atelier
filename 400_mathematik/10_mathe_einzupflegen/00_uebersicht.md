# Mathematik Uebersicht

Diese Uebersicht fasst den lokalen Ist-Stand der Mathematik-Notizen 01-14
(Bloecke 1-5) zusammen. Die Anker-Lesung erfolgte am 2026-06-19 gegen
`../src/geometry.js` und `../src/draft.js`. Genannte Code-Bezuege sind nur
lokale Befunde aus diesen Dateien; was dort nicht vorhanden ist, wird als
geplant oder offen markiert.

Die Uebersicht beschreibt mathematische und Software-methodische Bausteine,
keine fachlichen Hofenbitzer-Schnittregeln. Hofenbitzer-Werte, -Winkel,
-Zugaben und -Grenzen bleiben offen, solange sie nicht aus der Fachquelle
belegt und in Code umgesetzt sind.

## Gelesene Code-Anker

`../src/geometry.js`:

- `EPSILON` - Zeile 1
- `point(...)` - Zeilen 3-5
- `closePolygon(...)` - Zeilen 7-15
- `polygonArea(...)` - Zeilen 17-24
- `lineIntersection(...)` - Zeilen 26-34
- `offsetSegment(...)` - Zeilen 36-48
- `offsetPolygon(...)` - Zeilen 50-64
- `sampleQuadratic(...)` - Zeilen 66-77
- `translatePoints(...)` - Zeilen 89-91

`../src/draft.js`:

- `cmToMm(...)` - Zeile 3
- `requireMeasurement(...)` - Zeilen 5-7
- `dart(...)` - Zeilen 9-14
- `outline(...)` - Zeilen 16-32
- `piece(...)` - Zeilen 34-57
- `draftStraightSkirt(...)` - Zeilen 59-149
- Eingabevalidierung - Zeilen 76-80
- cm-nach-mm-Umrechnung der aktuellen Eingaben/Parameter - Zeilen 82-96
- Hilfswerte fuer den aktuellen Rock-Prototyp - Zeilen 97-101
- `metadata.constructionParameters` - Zeilen 113-122

## Blockstatus

- Block 1, Dateien 01-06: Grundgeometrie, Kurven, Offset, Orientierung und
  Einheiten; wesentliche Bausteine sind im aktuellen Code vorhanden.
- Block 2, Dateien 07-08: Geradenschnitt und Normalen; im Offset-Code
  vorhanden und Grundlage fuer die Nahtzugabe.
- Block 3, Dateien 09-10: Trigonometrie und Rotation; geplant, noch nicht im
  Code.
- Block 4, Dateien 11-12: kubische Bezier-Kurven, Splines, Kurvenlaenge und
  Passung; geplant, noch nicht im Code. Aktuell gibt es nur quadratische
  Kurvenabtastung ohne Laengenmessung.
- Block 5, Dateien 13-14: Parametrisierung und Neuberechnung; die Methode ist
  in `draft.js` vorhanden, die Hofenbitzer-Werte und -Regeln sind offen.

## Dateien 01-14

| Nr. | Datei | Thema | Genutzter Engine-Baustein |
| --- | --- | --- | --- |
| 01 | `01_koordinatensystem.md` | Koordinatensystem, X/Y-Achsen, Y-nach-unten-Konvention, Millimeter | `point(...)` in `geometry.js` Zeilen 3-5; `draftStraightSkirt(...)` in `draft.js` Zeilen 59-149 arbeitet mit Millimeterwerten, Tiefen/Laengen werden in Zeilen 84-85 gebildet; `sideWaist` nutzt `-sideUplift` in Zeile 18. |
| 02 | `02_punkte_und_vektoren.md` | Punkte, Vektoren, relative Konstruktion, Verschiebung von Punktmengen, Abnaeher als Dreieck | `point(...)` in `geometry.js` Zeilen 3-5; `translatePoints(...)` Zeilen 89-91; `dart(...)` in `draft.js` Zeilen 9-14; relative Punktbildung in `outline(...)` Zeilen 16-32. |
| 03 | `03_kurven_bezier.md` | Quadratische Bezier-Kurve, Kontrollpunkt, Abtastung in Segmentpunkte | `sampleQuadratic(...)` in `geometry.js` Zeilen 66-77; verwendet fuer die Seitenkurve in `draft.js` Zeilen 20-25. |
| 04 | `04_nahtzugabe_offset.md` | Parallelversatz, Offset-Segmente, Eckenbildung der Nahtzugabe | `offsetSegment(...)` in `geometry.js` Zeilen 36-48; `lineIntersection(...)` Zeilen 26-34; `offsetPolygon(...)` Zeilen 50-64; Aufruf fuer die Schnittlinie in `piece(...)` in `draft.js` Zeile 50. |
| 05 | `05_flaeche_und_orientierung.md` | Polygonflaeche, Vorzeichen, Orientierung und Offset-Richtung | `polygonArea(...)` in `geometry.js` Zeilen 17-24; Orientierung wird in `offsetPolygon(...)` Zeile 55 berechnet und an `offsetSegment(...)` in Zeilen 56-57 weitergegeben. |
| 06 | `06_einheiten_und_masshaltigkeit.md` | cm/mm-Umrechnung, Rundung, Export-Masshaltigkeit, Kontrollmass | `cmToMm(...)` in `draft.js` Zeile 3; Umrechnung der Eingaben/Parameter in Zeilen 82-96; `units: "mm"` in Zeile 110. Export-Masshaltigkeit und Kontrollquadrat sind in den gelesenen Ankern nicht belegt und bleiben offen. |
| 07 | `07_geraden_und_schnittpunkte.md` | Geradenformen, Schnittpunkt zweier Geraden, Determinante/2D-Kreuzprodukt, EPSILON-Fallback | `lineIntersection(...)` in `geometry.js` Zeilen 26-34; Nenner/Determinante in Zeile 29; EPSILON-Fallback in Zeile 30; Verwendung fuer Offset-Ecken in `offsetPolygon(...)` Zeilen 59-62. |
| 08 | `08_normalen_und_rechte_winkel.md` | Normalenvektoren, 90-Grad-Drehung, Einheitsnormale, Orientierungswahl | `offsetSegment(...)` in `geometry.js` Zeilen 36-48; Laenge mit `Math.hypot(...)` in Zeile 39; Null-/EPSILON-Fall in Zeile 40; Normalenkomponenten in Zeilen 42-43; Verwendung in `offsetPolygon(...)` Zeilen 56-57. |
| 09 | `09_trigonometrie_und_polarkoordinaten.md` | Sinus, Kosinus, Tangens, Polarkoordinaten, Grad/Radiant, Winkel-Konvention | Geplant, noch nicht im Code. In den gelesenen Ankern gibt es keine Funktion wie `pointFromAngle(...)` und keine Trigonometrie-Helfer; heutige Bezugspunkte sind nur `translatePoints(...)` in `geometry.js` Zeilen 89-91 und die vereinfachte `sideUplift`-Logik in `draft.js` Zeilen 18 und 96. |
| 10 | `10_rotation_und_abnaeher_verlegung.md` | Rotationsmatrix, Rotation um beliebigen Drehpunkt, translate-rotate-translate, Abnaeher-Verlegung | Geplant, noch nicht im Code. Es gibt keine `rotatePoint(...)`-/`rotatePointsAroundPivot(...)`-Funktion; vorhandener Verwandter ist `translatePoints(...)` in `geometry.js` Zeilen 89-91. `dart(...)` in `draft.js` Zeilen 9-14 erzeugt nur Abnaeher-Dreieckslinien, keine Rotation. |
| 11 | `11_bezier_kubisch_und_splines.md` | Kubische Bezier-Kurven, zwei Kontrollpunkte, Splines, G1-/C1-Stetigkeit | Geplant, noch nicht im Code. Aktuell vorhanden ist nur `sampleQuadratic(...)` in `geometry.js` Zeilen 66-77; eine kubische Abtastung oder Spline-Logik ist in den gelesenen Ankern nicht vorhanden. |
| 12 | `12_kurvenlaenge_und_passung.md` | Bogenlaenge, numerische Approximation, adaptive Unterteilung, Gauss-Legendre-Quadratur, Naht-Matching | Geplant, noch nicht im Code. `sampleQuadratic(...)` in `geometry.js` Zeilen 66-77 liefert Punkte, aber keine Laengenmessung; Funktionen wie `curveLength(...)`, adaptive Unterteilung, Quadratur oder Passungsiteration sind in den gelesenen Ankern nicht vorhanden. |
| 13 | `13_parametrische_masse_und_abhaengigkeitskette.md` | Parametrische Eingaben, Hilfsmasse, Abhaengigkeitskette, reine Berechnung, Zugaben als Parameter | Methode in `draft.js` vorhanden: `draftStraightSkirt(...)` Zeilen 59-149, `cmToMm(...)` Zeile 3, Umrechnungen Zeilen 82-96, Hilfswerte Zeilen 97-101, `metadata.constructionParameters` Zeilen 113-122. Der aktuelle Methodentext ist `Aldrich-inspired tailored skirt block` in Zeile 109; Hofenbitzer-Werte/Formeln sind offen. |
| 14 | `14_aenderung_und_neuberechnung.md` | Neuberechnung bei geaenderten Eingaben, Single Source of Truth, Groessentabellen, Plausibilitaetspruefung | Methode in `draft.js` vorhanden: `draftStraightSkirt(...)` Zeilen 59-149 berechnet aus Eingaben neu; `requireMeasurement(...)` Zeilen 5-7 und Nutzung in Zeilen 76-78; semantische Pruefungen in Zeilen 79-80. UI-Reaktivitaet/Dirty-Node-Tracking ist in den gelesenen Ankern nicht vorhanden; Hofenbitzer-Grenzen bleiben offen. |

## Offene Grenzen

- Trigonometrie, Rotation, kubische Bezier-Kurven, Kurvenlaenge und Passung
  sind geplante mathematische Grundlagen, aber noch nicht als Engine-Code in
  `geometry.js` oder `draft.js` umgesetzt.
- Die aktuelle Rockkonstruktion ist laut `draft.js` Zeile 109 ein
  Aldrich-inspirierter Prototyp. Hofenbitzer-Werte, -Formeln und
  Plausibilitaetsgrenzen duerfen daraus nicht abgeleitet werden.
- Export-Masshaltigkeit, Kontrollquadrat, UI-Reaktivitaet und weitere
  Vertrags-/Exportdateien wurden fuer diese Uebersicht nicht als Code-Anker
  ausgewertet; sie bleiben hier bewusst offen.
