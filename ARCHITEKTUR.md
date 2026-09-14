# Architektur

## Zweck

Die Architektur legt fest, aus welchen Schichten das Schnittmusterprogramm besteht und wie die Daten von den Körpermaßen bis zur fertigen Schnittmusterdatei fließen.

## Datenfluss

```text
1. Eingabe
   Körpermaße + gewünschtes Kleidungsstück + Wahlwerte
        ↓
2. Fachwissen
   menschlich verifizierte Hofenbitzer-Regeln
   + branchenübliche Schnittmusterstandards
        ↓
3. Mathematik
   allgemeine Berechnungen und Geometriewerkzeuge
        ↓
4. Konstruktionsbausteine
   kleine wiederverwendbare Python-Funktionen
   für Weiten, Punkte, Linien, Kurven, Abnäher usw.
        ↓
5. Kleidungsstück-Zusammensetzung
   verbindet passende Bausteine zu Rock, Oberteil,
   Ärmel, Kleid oder später Brautkleid
        ↓
6. Prüfung
   Maße, Anschlussstellen und Geometrie kontrollieren;
   bei fachlich offenen oder unmöglichen Fällen stoppen
        ↓
7. Schnittmuster-Aufbereitung
   Nahtzugaben, Saum, Knipse, Fadenlauf,
   Beschriftungen und Zuschnittangaben ergänzen
        ↓
8. Ausgabe
   DXF + SVG + maßstäbliche PDF
```

## Grundregeln

- Python ist die zentrale Programmiersprache für Berechnung und Konstruktion.
- Die fertige Software arbeitet ohne KI.
- Fachwissen, Mathematik und Programmcode bleiben getrennt, aber verbunden.
- Jede Python-Funktion besitzt klar definierte Eingaben und Ausgaben.
- Wiederkehrende Konstruktionen werden als gemeinsame Werkzeuge gebaut.
- Kleidungsstücke werden aus diesen Werkzeugen zusammengesetzt.
- Fachlich ungeprüftes Buchwissen wird nicht als gültige Regel codiert.
- Ein Codesegment darf keine eigene Sonderwelt bilden, die später nicht anschließbar ist.
- Ausgabeformate verwenden dieselbe geprüfte Schnittmustergeometrie; sie berechnen das Kleidungsstück nicht jeweils neu.
- KI hilft beim Aufbereiten, Codieren und Prüfen, gehört aber nicht zum ausführbaren Endprogramm.
