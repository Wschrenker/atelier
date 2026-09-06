# 400_mathematik — lokale Arbeitsregeln

## Aufgabe

Dieser Ordner besitzt die **modeblinde Mathematik** für die späteren Python-Funktionen in `../200_funktionen/`. Er beschreibt Rechenwege und geometrische Verträge, aber keine unbelegten Hofenbitzer-Werte oder Schnittregeln.

## Abhängigkeiten

```text
100_quellen (Buchfassung und normalisierte Fachformeln)
  → 400_mathematik (allgemeine Rechen- und Geometrieverträge)
  → 200_funktionen (fachlicher Ablauf und Python-Implementierung)
```

- Fachwerte, Zugaben, Grenzwerte und Auswahlregeln kommen aus `100_quellen/`.
- `400_mathematik/` darf technische Konventionen und modeblinde Geometrie festlegen.
- `200_funktionen/` verlinkt nur die Verträge, die ein konkreter Arbeitsschritt wirklich benötigt.
- Python-Code wird nicht vorsorglich in diesem Ordner angelegt.

## Direkte Kinder

- `00_uebersicht.md` — Einstieg, Status und Arbeitsweise.
- `20_codevertraege/` — ausführbare, Python-nahe Verträge für wiederverwendbare mathematische Primitive.
- `90_recherche/` — bestehende mathematische Recherche 01–14; die alten JavaScript-Anker sind nur historische Befunde.

## Ladeweise

1. Zuerst diese Datei und `00_uebersicht.md` lesen.
2. Danach nur den in `200_funktionen/` verlinkten Vertrag aus `20_codevertraege/` laden.
3. Die ausführlichen Recherchedateien nur bei Herleitung, Prüfung oder Erweiterung öffnen.

## Harte Grenzen

- Keine Buchregel aus allgemeiner Mathematik ableiten.
- Keine gerundeten Anzeigezahlen als interne Rechenwerte weiterverwenden.
- Keine stillen Fallback-Punkte bei mehrdeutiger oder entarteter Geometrie erzeugen.
- Nahtlinie, Schnittlinie und genähter Zustand bleiben getrennte Geometrien.
- Ein Vertrag ist erst `bereit`, wenn Eingaben, Ausgaben, Sonderfälle, Invarianten und Prüffälle feststehen.
