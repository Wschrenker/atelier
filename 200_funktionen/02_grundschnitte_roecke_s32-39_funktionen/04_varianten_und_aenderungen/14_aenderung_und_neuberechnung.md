# 14 Aenderung und Neuberechnung

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Der Vorteil einer parametrischen Konstruktion ist nicht nur, dass man Werte eingibt. Der eigentliche Vorteil ist: Wenn ein Eingabe-Mass geaendert wird, muessen alle davon abhaengigen Werte automatisch neu entstehen. Die Konstruktion bleibt dieselbe Methode, aber sie passt sich an andere Koerpermasse, Groessentabellen oder Zugaben an. Damit das verlaesslich bleibt, darf jedes Mass nur eine Quelle der Wahrheit haben und muss vor der Berechnung plausibel geprueft werden.

## Die Mathematik / Methode (sauber, nachvollziehbar)

Eine reaktive oder wiederholbare Berechnung folgt dem Abhaengigkeitsgraphen:

```text
Aenderung eines Eingabeknotens
  -> abhaengige Hilfsmasse markieren
  -> abhaengige Punkte/Linien markieren
  -> in gueltiger Reihenfolge neu berechnen
```

Tabellenkalkulationen zeigen dieses Prinzip sehr klar: Aus den Abhaengigkeiten wird eine Berechnungskette erstellt; wenn Eingabedaten geaendert werden, werden direkte und indirekte Abhaengige als neu zu berechnen markiert. In einem Schnittmusterprogramm kann man dasselbe Prinzip entweder inkrementell machen oder einfacher die ganze Konstruktion mit den neuen Eingaben erneut ausfuehren.

"Eine Quelle der Wahrheit" bedeutet: Ein Wert wie `hip_cm` wird nicht an mehreren Stellen separat gespeichert und spaeter manuell synchronisiert. Stattdessen gibt es eine autoritative Eingabe, und alle Varianten wie `hip_mm`, `hip_with_ease_mm` oder `side_hip_point` werden daraus abgeleitet.

Plausibilitaet besteht aus zwei Ebenen:

```text
syntaktisch: Zahl vorhanden, endlich, positiv
semantisch: fachlich sinnvoll, z.B. hipCm > waistCm, lengthCm > waistToHipCm
```

Die semantischen Regeln muessen zur Schnittmethode passen. Allgemeine Software-Quellen koennen das Prinzip belegen, aber nicht entscheiden, welche Hofenbitzer-Grenzen fachlich richtig sind.

## Anwendung in der Schnittkonstruktion (Methode vorhanden vs. Werte offen; Uebergabepunkt zu Hofenbitzer Stufe 2)

`../src/draft.js` ist bereits eine parametrisierte Neuberechnung: `draftStraightSkirt(...)` nimmt ein Eingabeobjekt und erzeugt daraus jedes Mal ein neues Dokument mit Stuecken, Nahtlinien, Schnittlinien, Abnaehern und internen Linien. Das ist derzeit keine UI-Reaktivitaet mit Dirty-Node-Tracking, aber methodisch reicht der reine Funktionsaufruf: Neue Eingaben hinein, neu berechnetes Ergebnis heraus.

Die Validierung ist ebenfalls schon angelegt. `requireMeasurement(name, value)` verlangt endliche positive Zahlen. Danach prueft `draft.js` semantische Grenzen wie `hipCm > waistCm` und `lengthCm > waistToHipCm`. Das passt zur Methode, ersetzt aber nicht die fachliche Pruefung der echten Hofenbitzer-Parameter.

Fuer Groessentabellen bedeutet Parametrik: Eine einzige Konstruktion kann mehrfach mit verschiedenen Eingabe-Saetzen laufen. Die Unterschiede entstehen aus den Eingaben, nicht aus kopierten und manuell veraenderten Schnittdateien. Hofenbitzer Stufe 2 muss spaeter liefern, welche Hilfsmasse, Zugaben und Grenzen wirklich gelten.

Unsicher/zu pruefen: Welche Plausibilitaetsregeln ueber positiv, Huefte groesser Taille und Laenge groesser Huefttiefe hinaus fachlich noetig sind, ist offen. Diese Regeln duerfen nicht aus allgemeiner CAD-/Software-Literatur abgeleitet werden.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- Microsoft Learn: "Excel Recalculation" - https://learn.microsoft.com/en-us/office/client-developer/excel/excel-recalculation - Abrufdatum: 2026-06-19. Belegt Dependency Tree, Calculation Chain, Dirty Cells und automatische/manuelle Neuberechnung abhaengiger Werte.
- Onshape Help: "Variable" - https://cad.onshape.com/help/Content/PartStudio/variable.htm - Abrufdatum: 2026-06-19. Belegt Variablen in CAD-Ausdruecken, Platzierung/Reihenfolge in der Feature-Liste und automatische Aktualisierung von Operationen, die Variablen verwenden.
- React Docs: "Sharing State Between Components" - https://react.dev/learn/sharing-state-between-components - Abrufdatum: 2026-06-19. Belegt das Prinzip "single source of truth" fuer eindeutig gehoerende Zustandswerte und das Vermeiden doppelter Speicherung.
- OWASP Cheat Sheet Series: "Input Validation Cheat Sheet" - https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html - Abrufdatum: 2026-06-19. Belegt fruehe Eingabevalidierung sowie syntaktische und semantische Validierung, inklusive Bereichspruefungen.
- Lokaler Engine-Anker: `../src/draft.js` - gelesen am 2026-06-19. Belegt `draftStraightSkirt(...)` als erneute Berechnung aus Eingaben, `requireMeasurement(...)` und die vorhandenen Plausibilitaetspruefungen.
- Lokaler Engine-Anker: `../src/contract.js` - gelesen am 2026-06-19. Belegt die Weitergabe der Masse in ein Pattern-Dokument und den aktuellen Prototyp-Status vor Hofenbitzer-Verifikation.
