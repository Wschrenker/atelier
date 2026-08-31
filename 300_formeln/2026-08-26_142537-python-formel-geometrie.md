# Python-Formel- und Geometrieebene — Vorbereitungsplan

> **Für Hermes:** Erst nach Bestätigung umsetzen. Rohtranskripte und laufende Quellordner-Umorganisation nicht verändern.

**Ziel:** Eine nachvollziehbare Rechenkette von geprüfter Buchformel über normalisierte Formel und Python-Funktion bis zu neutraler Schnittgeometrie schaffen.

**Architektur:** Die Markdown-Transkripte unter `100_quellen/` bleiben fachliche Quelle. `300_formeln/` wird die Normalisierung und Provenienz tragen. `400_mathematik/` bleibt modeblinde Geometrie. `500_python/` berechnet reine Geometrie; Exporte werden später getrennt ergänzt. Ein erstes T-Shirt dient als vertikaler Testfall, nicht als Anlass für eine vorweggenommene Universal-Engine.

**Technik:** Python 3.11, Millimeter intern, `pytest` für Prüfungen; SVG zuerst zur Sichtprüfung. DXF/PDF und externe Pakete erst beim ersten tatsächlich benötigten Exportfall festlegen.

---

## Aktueller Kontext

- Die Rohformelsammlung liegt unter:
  `100_quellen/10_hofenbitzer_b1/2_transkript/hofenbitzer_band_1_digital/`.
- Der Index nennt derzeit 183 Dateien und 905 Formelzeilen; weitere Formeln kommen hinzu.
- Die Quelle ist noch in Bewegung. Deshalb keine automatische Massenübersetzung.
- `500_python/10_rechnung/` ist bewusst leer und soll erst nach vollständiger Quellenfreigabe beginnen.
- `300_formeln/AGENT.md` und seine Fachordner sind im aktuellen Arbeitsbaum als gelöscht sichtbar; das ist vor jeder Einrichtung mit dem laufenden Arbeitsstand abzugleichen, nicht stillschweigend wiederherzustellen.
- Der Arbeitsbaum enthält umfangreiche laufende Umbenennungen, Löschungen und neue Extraktionsdateien. Diese Änderungen werden nicht bereinigt, zurückgesetzt oder mit dieser Vorbereitung vermischt.

## Vorgehen

1. **Quellaufnahme stabilisieren**
   - Den Formelindex als Eingangsliste verwenden.
   - Jede Formel später mit `Formel-ID`, Band, Seite, Quelldatei und Quellenzeile versehen.
   - Rohformel immer unverändert zitieren.
   - Status unterscheiden: roh, digital geprüft, fachlich freigegeben, offen/widersprüchlich.

2. **Normalisierungsschicht aufbauen**
   - Fachliche Formeln in `300_formeln/` ablegen, getrennt nach Maßregister, Oberteil, Rock usw.
   - Einheit, Abkürzungen, Operatoren, Rundung und Sonderfälle dokumentieren.
   - Buchfehler/Widersprüche nur markieren, nie still korrigieren; z. B. `BuW` versus `BuU` als offene Quellenabweichung führen.
   - Erst kleine, freigegebene Formelgruppe übernehmen; keine 905 Zeilen auf einmal.

3. **Python-Grundgerüst anlegen**
   - Erst nach vorhandener/erneuerter Eingangssperre in `300_formeln/` beginnen.
   - Unter `500_python/10_rechnung/` nur fachlich benannte, reine Module anlegen.
   - Jede Funktion erhält Docstring mit Formel-ID und Seitenquelle.
   - Eingaben in Millimeter; Konversion am Rand; keine Dateiausgabe aus Rechenmodulen.
   - Fehlende Maße, negative Ausfälle, Division durch null und unzulässige Geometrie typisiert behandeln.

4. **Neutrales Geometriemodell**
   - Zuerst Punkte, Linien, Kurven, Polygone und einfache Kontrollen in `400_mathematik/` klären.
   - Konstruktion und Geometrieexport strikt trennen.
   - Eine neutrale Geometrie muss unabhängig von Kleidname, Person und Ausgabeformat sein.

5. **Erster vertikaler Produktfall**
   - Nicht mit „allen Kleidern“ beginnen, sondern mit einem belegten **Oberteil-Grundschnitt**.
   - Daraus ein einfaches T-Shirt als erste Schnittzusammenstellung erzeugen.
   - Danach kontrolliert erweitern: V-Ausschnitt, weitere Ausschnittformen, Ärmel, Längen und andere Modellentwicklungen.
   - Jede Erweiterung als eigene, prüfbare Transformation; der Grundschnitt bleibt unverändert.

6. **Ausgabe in sicherer Reihenfolge**
   - Zuerst SVG aus der neutralen Geometrie für Bildschirm- und Sichtprüfung.
   - Danach DXF für CLO/CAD.
   - Danach PDF mit Maßstab, Kachel-/Seitenlogik und Kontrollquadrat für 1:1-Ausdruck.
   - JSON nur als nachvollziehbare Geometrie-/Metadatenablage, falls der erste reale Fall sie benötigt.

7. **Prüfung**
   - Buchbeispiele als `pytest`-Prüfwerte übernehmen.
   - Zusätzlich mathematische Invarianten prüfen: Einheiten, geschlossene Konturen, Endlichkeit, keine Selbstschnitte, definierte Naht-/Schnittkanten.
   - SVG visuell prüfen, anschließend Export und 1:1-Druck prüfen.
   - Erst danach Toile/physische Passform prüfen. Digitale und physische Freigabe getrennt dokumentieren.

## Voraussichtliche Dateien

Zunächst nur als Zielstruktur, nicht vorsorglich alle Ordner anlegen:

- `300_formeln/AGENT.md` und zuständige Formel-Fachordner — Normalisierung/Provenienz
- `400_mathematik/<modul>.md` — modeblinde Primitive und Grenzen
- `500_python/10_rechnung/<bereich>/<modul>.py` — reine Berechnung/Konstruktion
- `500_python/10_rechnung/<bereich>/test_<modul>.py` — Buch- und Invariantentests
- `500_python/10_rechnung/<bereich>/<modul>.md` — Formelkennungen, Quellen, Status
- später eigener Exportbereich für SVG/DXF/PDF, sobald der erste Exportfall die Ablage bestätigt

## Risiken und bewusste Grenzen

- **Hauptblocker:** Quelle und Extraktion sind noch nicht abgeschlossen; deshalb noch keine belastbare Python-Funktion aus unvollständigen Daten.
- `300_formeln/` ist im aktuellen Arbeitsbaum nicht stabil vorhanden; Wiederherstellung/Neuaufbau muss separat gegen die laufenden Änderungen entschieden werden.
- Ein T-Shirt ist ein guter erster Schnitt, aber kein Beweis für die gesamte Hofenbitzer-Systematik.
- `shapely`, `ezdxf`, `svgwrite` und `reportlab` werden nicht vorab sämtlich installiert. Abhängigkeiten erst mit echtem Bedarf und verifiziertem Export festlegen.
- Keine Formel wird direkt in DXF, SVG oder PDF codiert.

## Erster Umsetzungsschritt nach Bestätigung

1. laufende Quelländerungen nur lesend einfrieren/erfassen;
2. die fachliche Eingangssperre für eine kleine, vollständig belegte Formelgruppe definieren;
3. die Normalisierungsstruktur für diese Gruppe herstellen;
4. **noch keinen T-Shirt-Code schreiben**, bis ein konkreter Grundschnitt mit Buchseiten, Abkürzungen und Prüfwerten vollständig belegt ist.

## Validierung

- Pfade der tatsächlich benutzten Quelldateien existieren.
- Formel-ID verweist eindeutig auf Seite und Quellenzeile.
- Rohformel und normalisierte Formel sind beide erhalten.
- Python-Testwerte stammen entweder aus dem Buch oder sind ausdrücklich als externe Regressionswerte markiert.
- `git diff --check` und fokussierte Tests laufen nur für die tatsächlich geänderten Dateien.
- Keine Rohquelle, laufende Umbenennung oder fremde uncommitted Änderung wird überschrieben.
