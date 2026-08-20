# 13 Parametrische Masse und Abhaengigkeitskette

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Parametrisch heisst: Ein Schnitt wird nicht als feste Zeichnung gespeichert, sondern als Berechnung aus Eingabewerten. Aendert sich ein Mass, werden alle davon abhaengigen Hilfsmasse, Punkte und Linien wieder ausgerechnet. Wichtig ist die Trennung in drei Schichten: Eingabe-Masse, berechnete Hilfsmasse und daraus gebildete Konstruktionspunkte. Diese Datei beschreibt nur die Software-/CAD-Methode, nicht die fachlichen Hofenbitzer-Schnittformeln.

## Die Mathematik / Methode (sauber, nachvollziehbar)

Die Parametrisierung kann als gerichteter Abhaengigkeitsgraph beschrieben werden. Jeder Knoten ist ein Wert; jede gerichtete Kante bedeutet: "B braucht A".

```text
Eingabe-Masse  ->  berechnete Hilfsmasse  ->  Konstruktionspunkte
```

Ein solcher Graph muss fuer eine normale Vorwaertsberechnung azyklisch sein, also ein DAG. Dann kann man eine topologische Reihenfolge bilden: Alle Vorgaenger eines Knotens werden berechnet, bevor der Knoten selbst berechnet wird.

```text
taille_cm
hip_cm
ease_hip_cm
  -> hip_with_ease_mm
  -> side_hip_point
  -> side_curve
```

Die einzelne Berechnung sollte als reine Funktion formuliert sein:

```text
output = f(input_1, input_2, ...)
```

Gleiche Eingaben sollen gleiche Ergebnisse liefern. Das macht die Konstruktion testbar, reproduzierbar und vergleichbar gegen Referenzseiten.

Zugaben wie `ease` sind eigene Parameter, nicht versteckte Konstanten. Sie gehoeren fachlich getrennt neben die Koerpermasse:

```text
Koerpermass: hip_cm
Zugabe:      hip_ease_cm
Hilfsmass:   hip_with_ease_mm = cmToMm(f(hip_cm, hip_ease_cm))
```

Beispiel/Platzhalter -- echte Werte kommen aus Hofenbitzer (Stufe 2), hier NICHT als verbindliche Schnittregel:

```text
brustbreite_hilfe  = f(brustumfang, zugabe, weitere_parameter)
rueckenbreite_hilfe = g(brustumfang, rueckenmass, zugabe, weitere_parameter)
punkt_B            = h(brustbreite_hilfe, koordinatenkonvention)
```

Diese Namen illustrieren nur das Prinzip "Hilfsmass haengt von Eingaben ab, Punkt haengt von Hilfsmass ab". Es werden keine konkreten Brustbreiten-, Rueckenbreiten- oder Rockformeln aus dem Netz uebernommen.

## Anwendung in der Schnittkonstruktion (Methode vorhanden vs. Werte offen; Uebergabepunkt zu Hofenbitzer Stufe 2)

Die Methode ist im Code bereits vorhanden. `../src/draft.js` nimmt Eingabe-Masse wie `waistCm`, `hipCm`, `waistToHipCm` und `lengthCm`, rechnet sie mit `cmToMm(...)` in Millimeter um und leitet daraus Hilfswerte wie Breiten, Abnaeherparameter und Punkte ab. Die Funktion gibt ein deterministisches Schnitt-Dokument zurueck: gleiche Eingaben ergeben denselben Rock-Prototyp.

Der offene Punkt ist fachlich, nicht methodisch: `draft.js` kennzeichnet die aktuelle Methode als "Aldrich-inspired tailored skirt block". Die spaeteren Hofenbitzer-Werte und -Formeln muessen aus Stufe 2 kommen und duerfen nicht aus allgemeiner Parametrik-Literatur erfunden werden.

`constructionParameters` liegen im gelesenen Code aktuell in `draft.js` unter `metadata.constructionParameters`. `../src/contract.js` uebernimmt die Koerpermasse in `measurementsMm` und markiert die Quelle als Aldrich-Prototyp; ein eigenes `constructionParameters`-Mapping ist dort in der gelesenen Datei nicht sichtbar. Das ist ein Code-Befund, keine Aenderung.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- Python Software Foundation: "graphlib - Functionality to operate with graph-like structures" - https://docs.python.org/3/library/graphlib.html - Abrufdatum: 2026-06-19. Belegt topologische Sortierung, die Bedingung eines gerichteten azyklischen Graphen und die Reihenfolge "Vorgaenger vor Nachfolger".
- Microsoft Learn: "Excel Recalculation" - https://learn.microsoft.com/en-us/office/client-developer/excel/excel-recalculation - Abrufdatum: 2026-06-19. Belegt Dependency Tree, Calculation Chain und Recalculation als praktisches Modell fuer abhaengige Formeln.
- Onshape Help: "Variable" - https://cad.onshape.com/help/Content/PartStudio/variable.htm - Abrufdatum: 2026-06-19. Belegt CAD-Variablen, Nutzung in Dimensionen/Ausdruecken und automatische Aktualisierung abhaengiger Operationen.
- React Docs: "Keeping Components Pure" - https://react.dev/learn/keeping-components-pure - Abrufdatum: 2026-06-19. Belegt das Prinzip reiner Funktionen: gleiche Eingaben, gleiche Ausgabe, keine Mutation vorhandener Werte.
- Lokaler Engine-Anker: `../src/draft.js` - gelesen am 2026-06-19. Belegt die aktuelle parametrische Berechnung, `cmToMm(...)`, `requireMeasurement(...)`, `metadata.constructionParameters` und den Aldrich-Prototyp-Status.
- Lokaler Engine-Anker: `../src/contract.js` - gelesen am 2026-06-19. Belegt `measurementsMm` und die Kennzeichnung "Not yet verified against Hofenbitzer"; kein sichtbares `constructionParameters`-Mapping in dieser Datei.
