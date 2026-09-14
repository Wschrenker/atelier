# 200_funktionen — Arbeitsregeln

## Ziel

Hier entsteht zuerst ein gerader Rock nach menschlich geprüftem Hofenbitzer-Wissen und den Verträgen aus `400_mathematik/`. Der Python-Code wird aus kleinen Modulen aufgebaut, die klare Anschlüsse besitzen und später zu Röcken, Oberteilen, Kleidern oder einem Brautkleid zusammengesetzt werden können.

## Direkte Kinder

- `10_grundschnitte_roecke_s32-39/` — aktiver Grundschnittbereich für den geraden Rock.
- `20_modelle_roecke_s40-105/` — spätere Rockmodelle; nur bei konkretem Auftrag laden.

Neue Ordner entstehen erst für einen tatsächlich benötigten, belegten Codebaustein. Keine leeren Ordner auf Vorrat.

## Grundlage eines Codebausteins

- Die fachlich geprüfte Buchregel und ihre Quellen liegen in `100_quellen/`.
- Benötigte Mathematik- und Geometrieverträge liegen in `400_mathematik/10_codevertraege/`.
- Der Modulordner besitzt die konkrete Zusammensetzung, Python-Funktion, Tests und bei Bedarf eine kurze Spec.
- Jedes Modul benennt Eingaben, Ausgaben, Einheiten, Abhängigkeiten, Fehlerfälle und Anschlussstellen.
- Quellen und Mathematik werden verlinkt und verwendet, nicht kopiert oder neu erfunden.

## Zwei-KI-Arbeitszug

1. Eine **koordinierende KI** grenzt einen einzelnen Codebaustein ab und erstellt einen Vorprompt mit Ziel, Quellen, Mathematikverträgen, erlaubtem Dateibereich, erwarteten Anschlüssen und bekannten offenen Punkten.
2. Die **codierende KI** führt zuerst nur die Bereitschaftsprüfung durch. Sie bestätigt, dass alle Zutaten vorhanden sind, oder nennt gezielt fehlende Quellen, Entscheidungen, Verträge oder Angaben.
3. Fehlendes wird von Werner mit KI-Unterstützung geklärt und aufbereitet. Ohne ausreichende Grundlage beginnt die Codierung nicht.
4. Danach erhält die codierende KI den Hauptprompt und implementiert ausschließlich den freigegebenen Baustein.
5. Sie liefert Code, betroffene Tests und einen Bericht über Änderungen, Ergebnisse, Grenzen und offene Punkte an die koordinierende KI zurück.
6. Die koordinierende KI prüft Diff, Tests und die Anschlussfähigkeit unabhängig, bevor der Baustein weiterverwendet wird.

Hermes und Claude können beide Code erstellen oder prüfen. Die Rollen werden pro Auftrag festgelegt; in einem gemeinsamen Arbeitsbaum schreibt immer nur eine KI gleichzeitig.

## Grenzen

- Zuerst den geraden Rock vollständig aus den benötigten Modulen zusammensetzen; spätere Kleidungsstücke bleiben außerhalb des aktiven Scopes.
- Fachlich ungeprüftes Wissen wird nicht als gültige Regel codiert.
- Eine offene Prüfstelle blockiert nur den davon abhängigen Baustein.
- Vorhandene Module und Verträge wiederverwenden, statt unverbundene Sonderlösungen zu bauen.
- Technische Tests beweisen keine fachliche Passform; digitale Prüfung, CLO, Nessel und Anprobe bleiben getrennt.
- Die Schutzregeln aus der obersten `AGENT.md` gelten vollständig.

## Ladeweise

Diese Datei lesen, dann nur das `AGENT.md` des aktiven direkten Kindes sowie die für den konkreten Baustein benannten Quellen, Mathematikverträge und die lokale Spec.
