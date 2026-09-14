# ATELIER — Projektregeln

Arbeitsordner: `C:\ATELIER`

## Pflichtkontext

1. Zuerst [`PRODUKTZIEL.md`](PRODUKTZIEL.md) lesen.
2. Danach [`ARCHITEKTUR.md`](ARCHITEKTUR.md) lesen.
3. Bei Ordnerarbeit nur der `AGENT.md`-Kette entlang des tatsächlich bearbeiteten Pfads folgen.
4. Für einen Codeschritt nur die zugehörigen verifizierten Quellen, Verträge und die lokale Spec laden.

## Arbeitsfluss

```text
menschlich verifizierte Buchregel
→ fachlicher und mathematischer Vertrag
→ kleines wiederverwendbares Python-Codesegment
→ technische Tests
→ Zusammensetzung zum Kleidungsstück
→ DXF, SVG und maßstäbliche PDF
→ digitale und reale Fachprüfung
```

Eine offene Prüfstelle blockiert nur den Codeschritt, der von ihr abhängt. Fachlich ungeprüftes Wissen wird nicht als gültige Regel codiert.

## Verantwortung

- Werner bestimmt Produktziel, fachliche Lesart und menschliche Freigaben.
- Hermes bereitet begrenzte Arbeitsschritte vor, hält die Bereiche zusammen und prüft Ergebnisse unabhängig.
- Die codierende KI implementiert nur den freigegebenen Scope. Sie erfindet keine Fachregel und erweitert nicht selbstständig das Produktziel.

## Bereiche

- `000_sprache/`: Fachbegriffe, Abkürzungen und Symbole.
- `100_quellen/`: Buchdaten, Bilder, Formeln, Prüfstellen und Quellenstatus.
- `200_funktionen/`: verbindungsfähige Schnittmusterfunktionen und Tests.
- `400_mathematik/`: modeblinde Mathematik- und Geometriewerkzeuge.
- `800_werners spick/`: Orientierung und Denkmodelle; keine automatische Fachwahrheit.

## Grenzen

- Schritt für Schritt an einem begrenzten Codesegment arbeiten; nicht das ganze Buch oder Repository gleichzeitig aufarbeiten.
- Vorhandene Werkzeuge und Verträge wiederverwenden, statt unverbundene Sonderlösungen zu bauen.
- Fachquellen werden beim Codieren nicht verändert.
- Jede dauerhafte Antwort hat einen Besitzer; andere Stellen verlinken darauf, statt sie zu kopieren.
- Tests belegen nur technische Aussagen. CLO, Nessel und Anprobe liefern eigene fachliche und reale Nachweise.
- `#` ist die einmalige Freigabe für Commit und Push, Löschen und Verschieben, Downloads, destruktive Git-Aktionen sowie Veröffentlichung und Remote-Aktionen.
- Ohne `#` sind lokales Lesen und Schreiben sowie betroffene Tests erlaubt.
