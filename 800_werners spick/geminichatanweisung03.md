# Gemini-Gespräch 3/4 — Körpergeometrie und visuelles Patchwork

> Gesprächsnotiz zur gemeinsamen Ideenentwicklung. Sie gehört zu den Dateien `geminichatanweisung01.md` bis `geminichatanweisung04.md` und hält Ideen fest, nicht bereits bewiesene Fachwahrheit.

## Ausgangslage

Werner entwickelt aus dem transkribierten Schnittmusterbuch von Guido Hofenbitzer, etwa 43 Körpermaßen, normalisierten Formeln und Bézier-Geometrie zunächst einen Rock. Er möchte langfristig über die Grenzen statischer Lehrbuchformeln hinausgehen und zusätzliche Messpunkte, Winkel und Körperformen berücksichtigen.

## Genannte technische Richtungen

Gemini nannte zunächst vier allgemeine Ansätze für neuartige Webprojekte:

- Local-First und CRDTs für lokale Daten und spätere Synchronisierung;
- räumliche oder Canvas-Oberflächen für visuelles Arbeiten;
- Berechnungen im Browser mit WebAssembly oder WebGPU;
- asynchrone Systeme aus spezialisierten Agenten.

Für die Schnittkonstruktion wurden anschließend drei Wege diskutiert.

### 1. Winkel- und Haltungskorrekturen

Hofenbitzer bleibt das Grundgerüst. Zusätzliche Angaben wie Schulterneigung, Beckenkippung oder Hohlkreuztiefe verändern Punkte und Bézier-Kontrollpunkte geometrisch.

### 2. Parametrisches Constraint-System

Statt ausschließlich nacheinander ausgeführter Formeln werden Bedingungen definiert, beispielsweise Winkel, Tangenten und Distanzen zwischen Punkten. Ein Solver berechnet das zusammenhängende Liniensystem bei Parameteränderungen neu.

### 3. Vereinfachtes 3D-Modell und Abwicklung

Aus Maßen und Winkeln entsteht ein vereinfachtes Körpernetz. Schnittlinien werden auf der Oberfläche definiert und Flächen anschließend in die 2D-Ebene abgewickelt. Als begrenztes Experiment wurde ein verformbares Hüftsegment beziehungsweise ein Kegelstumpf vorgeschlagen, nicht sofort ein vollständiger Körper.

Diese Richtung soll ungewöhnliche Proportionen besser behandeln, bei denen statistische Standardformeln an Grenzen kommen. Die im Gespräch genannten Beispiele – etwa gleiche Taille und Hüfte, ein Zylinder oder automatisch verschwindende Abnäher – sind Ideen und müssen fachlich und geometrisch geprüft werden.

## Werners zweistufige visuelle Bedienidee

### Stufe 1: vorhandene Bausteine auswählen

Jeder codierte Baustein erhält ein visuelles Gegenstück. Werner kann beispielsweise bestimmen:

- ob ein hinterer oder vorderer Abnäher verwendet wird;
- ob ein oder zwei Abnäher vorgesehen sind;
- ob ein Reißverschluss hinten oder seitlich sitzt;
- welche bereits implementierten Details Teil des neuen Schnittmusters werden.

Die Positionen sind zunächst fest im Baustein definiert. Die Oberfläche schaltet vorhandene und erlaubte Varianten ein oder aus; sie erfindet keine neue Konstruktion.

Als gemeinsame Zustandsbeschreibung wurde beispielsweise genannt:

```json
{
  "zipper": "back",
  "darts": [
    { "position": "front", "active": true }
  ]
}
```

Die visuelle Darstellung und die 2D-Konstruktion lesen dieselbe Auswahl. In ATELIER entspricht das dem Schnittauftrag und dem Patchwork-Modul.

### Stufe 2: Details frei parametrisieren

Später könnten Bausteine nicht nur ausgewählt, sondern entlang einer Oberfläche oder relativ zu einer Mitte verschoben werden, beispielsweise durch eine numerische Position. Das 3D-Modell und die 2D-Konstruktion müssten dieselbe Veränderung fachlich konsistent abbilden.

Diese Stufe erfordert genauere Körpergeometrie, Regeln für zulässige Positionen, Neuberechnung der Schnittgeometrie und eine Prüfung der Passform. Sie bleibt deshalb eine spätere Entwicklungs- und Forschungsstufe.

## Gesprächsergebnis

Stufe 1 ist der pragmatische Einstieg: vorhandene Codebausteine werden visuell ausgewählt und an fest erlaubten Positionen eingesetzt. Stufe 2 erweitert dieses Prinzip später um freie Parameter. Ein genaueres 3D-Körpermodell und eine Flächenabwicklung bleiben mögliche Forschungsrichtungen und werden nicht als bereits gelöste Grundlage behandelt.

## Gesprächsreihe

1. [`geminichatanweisung01.md`](geminichatanweisung01.md): gemeinsames Datenmodell
2. [`geminichatanweisung02.md`](geminichatanweisung02.md): Prinzipien modularer Software
3. **Diese Datei:** 3D-Idee und visuelles Patchwork
4. [`geminichatanweisung04.md`](geminichatanweisung04.md): Engineering Context und Repo-Butler
