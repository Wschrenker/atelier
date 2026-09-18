# Hofenbitzer Band 1 – menschlich verifiziert

## Zweck

Dieser Ordner führt die seitenweisen Arbeitsstände bis zur menschlich
verifizierten Fassung. Eine OCR-Rohfassung muss ausdrücklich als noch nicht
menschlich verifiziert markiert sein. Nur Inhalte, die Werner am Original
verstanden und bestätigt hat, gelten als menschlich verifiziert; OCR ist keine
Fachwahrheit.

## Weg einer Buchseite

Für jede neue OCR-Seite sind der projektlokale [`SKILL.md`](SKILL.md) und der
ausführliche [`OCR_WORKFLOW.md`](OCR_WORKFLOW.md) verbindlich zu laden und
auszuführen. Dadurch bleibt der Ablauf auch für KI-Systeme nutzbar, die keinen
persönlich installierten Hermes-Skill besitzen.

```text
Originalbild
→ OCR-Markdown + Layout-JSON
→ Tabellen, Formeln und Skizzenbereiche getrennt erfassen
→ Werner prüft Text, Werte, Formeln und Zeichnungslabels
→ menschlich verifizierte Seitenfassung
→ bei konkretem Engine-Bedarf: kleiner Konstruktionsvertrag außerhalb dieses Ordners
```

## Ordnung nach Buchseiten

- Die Buchkategorien bleiben die erste Ordnungsstufe und werden in Buchreihenfolge
  zweistellig benannt, zum Beispiel `00_vorspann_s1-3/`, `01_inhalt_s4-7/`,
  `02_herstellungspraxis_s8-31/` und `03_grundschnitte_roecke_s32-48/`.
- Darunter erhält jede Buchseite einen eigenen Ordner `sNNN/`; die maßgebliche
  Seitendatei darin heißt ebenfalls `sNNN.md`.
- Die zweistelligen Buchkategorien und die Quellenkennung `sNNN` sind in diesem
  Buchbestand bewusst semantische Ordnungskennungen. Sie bilden eine lokale
  Ausnahme von der allgemeinen tiefenabhängigen Nummerierung.
- Im Seitenordner liegen alle zugehörigen Arbeitsarten dieser Seite: Text,
  OCR-Rohdaten, Tabellen, fototreue und normalisierte Formeln sowie
  Skizzenbeschreibungen und Skizzenausschnitte.
- Es entstehen keine buchweiten Sammelordner nach Dateityp. Seitenübergreifende
  Inhalte werden von ihrer Besitzerseite aus verlinkt, nicht kopiert.
- Das vollständige Originalbild bleibt im zentralen Bildbestand. Der
  Seitenordner verweist eindeutig darauf und enthält nur nötige Ausschnitte.

Beispiel:

```text
03_grundschnitte_roecke_s32-48/
└── s033/
    ├── s033.md
    ├── ocr_s033_raw.json
    ├── formeln_s033.md
    ├── formeln_s033_normalisiert.md
    ├── tabellen_s033.md
    ├── skizzen_s033.json
    └── skizzen/
        └── s033_skizze_01.png
```

## Erfassung

- Das unveränderte Originalbild unter `../20_hofenbitzer_band_1_bilder/` bleibt
  der Beleg und wird verlinkt, nicht ersetzt.
- OCR-Markdown enthält die lesbare Rohabschrift. Layout-JSON bewahrt Modell,
  Blöcke, Bounding Boxes, Tabellen und Konfidenzen; keine Base64-Bilder in Git.
- Einfache Tabellen als Markdown, komplexe Tabellen nötigenfalls als HTML
  erfassen. Zahlen, Einheiten und Spaltenbedeutung einzeln prüfen.
- Formeln zuerst fototreu festhalten. LaTeX darf die Lesbarkeit verbessern;
  die fachlich normalisierte Formel bleibt davon getrennt.
- Skizzen als verlinktes Original plus verlustfreie PNG-Ausschnitte erfassen.
  Labels, Maße und Beziehungen strukturiert festhalten, Unsicheres offenlassen.

## Freigabegrenze

- Werner bestätigt Text, Tabellen, Formeln und Skizzenlabels. Eine Bestätigung
  gilt nur für den ausdrücklich geprüften Inhalt.
- OCR-Konfidenz, KI-Beschreibung und optische Plausibilität sind kein Beleg.
- Aus einer Skizze keine fehlende Geometrie, Kurve oder Fachregel erfinden.
- Erst nach Werners Bestätigung darf eine Seite als menschlich verifiziert gelten.

## Übergabe an die Engine

Die codierende KI erhält die verifizierte Seite, die nötigen Bildausschnitte und
einen begrenzten Vertrag mit Eingaben, Ausgaben, Einheiten, Formeln,
Geometrieoperationen, offenen Grenzen und Quellenverweisen. Engine-Code, Tests,
SVG, DXF und PDF bleiben außerhalb dieses Quellenordners.
