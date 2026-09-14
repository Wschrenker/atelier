# 400_mathematik — Arbeitsregeln

## Aufgabe

`400_mathematik/` besitzt die modeblinden Mathematik- und Geometrieverträge für wiederverwendbare Python-Funktionen. Fachregeln und Werte aus Hofenbitzer bleiben in `100_quellen/`; der ausführbare Schnittmustercode entsteht in `200_funktionen/`.

## Direkte Kinder

- `Uebersicht.md` — Zweck, Konventionen und vorhandene Vertragsfamilien.
- `10_codevertraege/` — aktive Verträge für Mathematik- und Geometriewerkzeuge.
- `20_recherche/` — Herleitungen und historische Recherche; keine aktuelle Codewahrheit.

## Ladeweise

1. Diese Datei und `Uebersicht.md` lesen.
2. Danach nur den für den aktuellen Funktionsschritt benötigten Vertrag aus `10_codevertraege/` laden.
3. `20_recherche/` nur öffnen, wenn eine Herleitung geprüft oder ein Vertrag ergänzt werden muss.

## Grenzen

- Keine Buchregel, Zugabe oder fachliche Auswahl aus allgemeiner Mathematik ableiten.
- Keine stillen Annahmen oder Ersatzpunkte bei unklarer beziehungsweise unmöglicher Geometrie erzeugen.
- Nahtlinie, Schnittlinie und genähter Zustand bleiben getrennt.
- Neue Werkzeuge nur am nachgewiesenen Bedarf eines konkreten Funktionsschritts entwickeln.
- Fachlich ungeprüfte Quellen blockieren nur die davon abhängige Umsetzung.
