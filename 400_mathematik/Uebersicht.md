# Mathematik — Übersicht

## Zweck

`400_mathematik` bereitet allgemeine Mathematik so vor, dass spätere Arbeitsschritte in `200_funktionen` daraus kleine, testbare Python-Primitiven bauen können. Die Fachquelle bleibt `100_quellen`; Mathematik und Code bestätigen niemals eigenständig eine Hofenbitzer-Regel.

## Bestand

| Bereich | Rolle | Status |
|---|---|---|
| `10_codevertraege/` | Einheitliche Verträge mit Formeln, Fehlerfällen, Invarianten und Prüffällen | aktive Grundlage für neue Python-Arbeit; Einzelstatus im jeweiligen Vertrag |
| `20_recherche/` | Erklärende Recherche zu Koordinaten, Vektoren, Kurven, Offset, Rotation, Kurvenlänge und Parametrik | fachlich nützlich; alte JS-Codeanker nicht mehr aktuell |

Die in den Recherchedateien genannten Dateien `geometry.js`, `draft.js` und `contract.js` sind im aktiven Repository `C:\ATELIER` nicht vorhanden. Ihre damaligen Codebefunde sind historische Orientierung, kein heutiger Implementierungsstatus.

## Aktive technische Konventionen

- interne Längeneinheit: Millimeter;
- X-Achse nach rechts, Y-Achse nach unten;
- Punkte und Vektoren werden semantisch getrennt;
- Winkel tragen ihre Einheit im Namen; öffentliche Gradwerte werden vor Trigonometrie in Radiant umgerechnet;
- Toleranzen werden nach Zweck benannt und nicht als ein universelles `EPSILON` versteckt;
- unklare Geometrie liefert einen typisierten Zustand oder Fehler, keinen erfundenen Ersatzpunkt.

## Vertragsfamilien

| Datei | Beantwortet |
|---|---|
| `10_codevertraege/01_numerik_einheiten_und_toleranzen.md` | Wie werden Zahlen, Einheiten, Winkel und Näherungen behandelt? |
| `10_codevertraege/02_punkte_vektoren_geraden_und_projektion.md` | Wie werden Punkte gesetzt, geteilt, projiziert und Geraden geschnitten? |
| `10_codevertraege/03_transformationen.md` | Wie werden Teile verschoben, gedreht, gespiegelt und skaliert? |
| `10_codevertraege/04_kreise_und_boegen.md` | Wie werden Kreis-/Bogenkonstruktionen und ihre Schnittpunkte beschrieben? |
| `10_codevertraege/05_bezierkurven.md` | Wie werden Kurven ausgewertet, geteilt, abgeflacht und gemessen? |
| `10_codevertraege/06_polygone_und_offsets.md` | Wie werden Konturen geprüft und Nahtzugaben robust erzeugt? |
| `10_codevertraege/07_flaechen_teilen_vereinigen_und_kopieren.md` | Wie werden Bund, Passe, Beleg und andere Teilflächen geometrisch getrennt oder verbunden? |
| `10_codevertraege/08_messen_passung_und_markierungen.md` | Wie werden Nahtlängen, Positionen und Knipse übertragen? |
| `10_codevertraege/09_keile_schliessen_und_oeffnen.md` | Wie werden Abnäher, Falten- und Drapierschnitte starr geschlossen oder geöffnet? |
| `10_codevertraege/09_zz_01_parameterketten_und_neuberechnung.md` | Wie bleiben Fachparameter, Abhängigkeiten und Neuberechnung nachvollziehbar? |

## Arbeitsweise pro Funktionsschritt

1. Buchseite, Bild und Prüfstellen in `100_quellen` prüfen.
2. Fachformel und Auswahlregel bestimmen; Unklares offen lassen.
3. Nur die benötigten Verträge aus `10_codevertraege` verlinken.
4. Kleinste reine Python-Funktion in der aktiven Funktionsscheibe bauen.
5. Vertragsprüffälle, Quellenbeispiel und geometrische Invarianten testen.
6. Ausgabe visuell und später am realen Schnitt prüfen.

## Nicht vorsorglich bauen

Keine vollständige CAD-Bibliothek, keinen allgemeinen Constraint-Solver und keine 3D-Geometrie vor dem ersten belegten Bedarf. Fehlende Primitiven werden am realen Funktionsschritt ergänzt.
