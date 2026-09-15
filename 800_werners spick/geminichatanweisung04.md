# Gemini-Gespräch 4/4 — Engineering Context und Repo-Butler

> Gesprächsnotiz zur gemeinsamen Ideenentwicklung. Sie gehört zu den Dateien `geminichatanweisung01.md` bis `geminichatanweisung04.md` und ist keine zusätzliche Projektanweisung.

## Werners Anliegen

Eine codierende KI braucht neben dem eigentlichen Auftrag weitere Informationen: Programmiersprache, Ein- und Ausgabeformate, Grenzen, Tests, Abnahme und die Stellung des neuen Codes im Gesamtsystem. Der Kontext soll so vorbereitet sein, dass begrenzte KI-Sessions konsistente und anschlussfähige Ergebnisse liefern.

## Fachbegriffe für das „Drumherum“

Der Gesamtvorgang kann als **Context Engineering** im Rahmen einer spezifikationsgestützten Entwicklung verstanden werden.

### Steuerung und Anweisungen

- `.cursorrules`, `CLAUDE.md` oder `AGENT.md`: lokale Projektregeln und Arbeitsweisen für KI-Agenten;
- `SYSTEM_PROMPT`: grundlegende Rollen- und Verhaltensanweisung.

### Spezifikation und Anforderungen

- `SPEC.md` oder `REQUIREMENTS.md`: funktionale Anforderungen;
- `ARCHITECTURE.md`: Systemaufbau, Modulgrenzen, Technik und Abhängigkeiten.

### Schnittstellen und Datenformate

- `INTERFACE.md`, `API.md` oder ein Schema: verbindliche Ein- und Ausgabeformate;
- `CONVENTIONS.md` oder `STYLEGUIDE.md`: Benennung, Formate und Dateistruktur.

### Absicherung und Prüfung

- Guardrails oder Constraints: Grenzen und Verbote;
- Abnahmekriterien oder `TEST_PLAN.md`: erwartete Ergebnisse und Prüfungen;
- `AUDIT.md` oder Tracing: Nachvollziehbarkeit von Entscheidungen und Änderungen.

### Kontextmethoden

- Context Window Optimization: nur die für den Auftrag nötigen Dokumente laden;
- In-Context Learning: konkrete Ein- und Ausgabebeispiele für die KI bereitstellen.

Diese Namen sind mögliche Dokumentrollen. Sie verlangen nicht automatisch je eine eigene Datei.

## Große Wissensbestände

Gigabyte an Quellen sollen nicht vollständig in eine KI-Session geladen werden. Die KI erhält:

- kurze Schemata und Verträge;
- kleine passende Beispieldaten;
- nur die Quellen, die der aktuelle Baustein wirklich benötigt.

Große Datenbestände bleiben in ihrer geeigneten Ablage. Schnittstellen und Verweise machen den benötigten Ausschnitt auffindbar.

## Begrenzte Coding-Sessions

Ein möglicher Ablauf lautet:

1. Aufgabe und benötigten Kontext lesen;
2. Bereitschaft prüfen und Fehlendes nennen;
3. begrenzten Baustein implementieren;
4. Tests und andere passende Prüfungen ausführen;
5. Ergebnis und Grenzen berichten;
6. nur bei gesondertem Auftrag committen.

Kleine Arbeitspakete und einheitliche Verträge fördern Qualität und Konsistenz, garantieren sie aber nicht allein.

## Zwei Rollen und zwei Prüfebenen

### Codierende KI

Sie implementiert das freigegebene Modul und die zugehörigen Tests.

### Koordinierende oder prüfende KI

Sie prüft den Auftrag gegen Projektregeln, Architektur, Datenverträge und lokale Spezifikation. Danach kontrolliert sie Diff, Testergebnisse, Anschlussfähigkeit und offene Punkte.

### Deterministische Werkzeuge

Compiler, Typprüfung, Linter, Tests, Linkprüfer und Abhängigkeitsanalysen beantworten exakte technische Fragen zuverlässiger als eine KI.

Der gewünschte Ablauf ist:

```text
Kontext und begrenzter Auftrag
→ codierende KI
→ deterministische Prüfungen
→ unabhängige KI-Prüfung
→ menschliche Fachentscheidung
```

Ein automatischer Rücklauf vom Reviewer zum Coder ist möglich, ersetzt aber keine menschliche Fachfreigabe.

## Der schlanke Repo-Butler

Beim Umbenennen, Verschieben oder Löschen können unbekannte Verweise brechen. Der Repo-Butler kombiniert deshalb mehrere Werkzeuge:

### LSP und Refactoring-Werkzeuge

Sie verstehen Symbole und Imports unterstützter Programmiersprachen und können viele Referenzen beim Umbenennen aktualisieren. Freitext, Markdown und dynamische Pfade werden dadurch nicht vollständig erfasst.

### Abhängigkeitsgraph oder Repo-Karte

Eine leichte Karte zeigt, welche Dateien andere Dateien importieren oder verlinken. Tree-Sitter oder ähnliche Parser können dabei helfen.

### Statische Link- und Pfadprüfungen

Kleine lokale Skripte oder Git-Hooks erkennen tote Markdown-Links, fehlende Dateien, ungültige Imports oder Typbrüche.

### Praktischer Ablauf

1. Vor einer Änderung alle bekannten Verweise und Abhängigkeiten suchen.
2. Umbenennungen oder Verschiebungen kontrolliert durchführen.
3. Referenzen gemeinsam aktualisieren.
4. Alte Pfade erneut suchen und technische Prüfungen ausführen.
5. Den Diff vor einer Freigabe kontrollieren.

Eine kleine KI kann komplexe Umordnungen unterstützen, sollte dafür aber nicht nur den Dateibaum, sondern auch Zweck und Beziehungen der betroffenen Dateien erhalten.

## Gesprächsergebnis

ATELIER braucht ein schlankes Engineering-Context-Gerüst, begrenzte Arbeitspakete, eine Rollenaufteilung zwischen Koordination und Codierung sowie deterministische Kontrollen. Bestehende Dokumentrollen dürfen mehrere Aufgaben bündeln; zusätzliche Dateien entstehen nur bei einem konkreten Bedarf.

## Gesprächsreihe

1. [`geminichatanweisung01.md`](geminichatanweisung01.md): gemeinsames Datenmodell
2. [`geminichatanweisung02.md`](geminichatanweisung02.md): Prinzipien modularer Software
3. [`geminichatanweisung03.md`](geminichatanweisung03.md): 3D-Idee und visuelles Patchwork
4. **Diese Datei:** Engineering Context und Repo-Butler
