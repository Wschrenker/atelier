# OCR-Arbeitsablauf für eine Hofenbitzer-Buchseite

## Zweck

Dieser Ablauf gilt, wenn eine Seite aus dem zentralen Bildbestand per Mistral OCR
für die spätere menschliche Prüfung vorbereitet wird. Die OCR-Ausgabe ist eine
Rohfassung und wird niemals allein zur Fachwahrheit.

## Eingabe und Ziel

- Originalbilder: `../20_hofenbitzer_band_1_bilder/01_Photos_hofenb_ba1_total/`
- OCR-Werkzeug: `C:\Users\Chromatic\AppData\Local\hermes\scripts\mistral_ocr.py`
- Ziel: der zur Seitenzahl passende Buchkategorie- und Seitenordner in diesem
  Bestand, zum Beispiel Seite 35 unter
  `03_grundschnitte_roecke_s32-48/s035/`.
- Bildnamen dürfen ungepolstert sein (`s35.jpg`); Seitenordner und Dateien werden
  dreistellig benannt (`s035`, `s035.md`).

Die Ergebnisse werden **direkt im Zielordner** abgelegt, nicht nur in einem
temporären Ordner. Temporäre Drehungen, Zuschnitte und Kontaktbögen dürfen
zusätzlich unter dem lokalen Temp-Verzeichnis entstehen.

## Verbindlicher Ablauf

### 1. Quelle und Ziel prüfen

1. Die lokale `AGENT.md` und diesen Ablauf lesen.
2. Das Originalbild für genau die angeforderte Seite nachweisen.
3. Die Seitenzahl der passenden Buchkategorie zuordnen.
4. Prüfen, ob der Seitenordner bereits besteht, damit keine vorhandene Arbeit
   überschrieben wird.
5. Das Originalbild niemals verändern, verschieben oder ersetzen.

### 2. Bild vor der OCR ansehen

1. EXIF-Orientierung und Bildmaße prüfen.
2. Eine aufrechte temporäre Vorschau erzeugen und visuell kontrollieren.
3. Prüfen, ob die vollständige Buchseite sichtbar ist und ob eine Nachbarseite
   mitfotografiert wurde.
4. Nur wenn nötig einen temporären Seitenzuschnitt erzeugen. Vor der OCR
   ausdrücklich prüfen, dass dadurch kein Text, keine Tabelle, keine Formel und
   keine Zeichnungsbeschriftung der Besitzerseite abgeschnitten wurde.
5. Bei einem ungeeigneten oder unvollständigen Foto stoppen und den Mangel
   melden; keinen fehlenden Inhalt ergänzen.

### 3. Mistral OCR ausführen

Das Mistral-Modell `mistral-ocr-latest` wird mit folgenden Bedingungen genutzt:

- Tabellenformat: Markdown;
- keine Base64-Bilder in den gespeicherten Artefakten;
- Originalbild oder kontrollierter temporärer Zuschnitt als Eingabe;
- API-Schlüssel nur über die vorhandene Hermes-Umgebung laden und niemals
  ausgeben oder in Projektdateien schreiben.

Das vorhandene Werkzeug schreibt standardmäßig nur OCR-Markdown. Für diesen
Bestand muss dieselbe OCR-Antwort zusätzlich vollständig als Layout-JSON
gesichert werden. Dazu in einem Python-Lauf die Funktionen `process(source)` und
`render_markdown(result)` aus `mistral_ocr.py` verwenden und beide Ausgaben
speichern:

```text
ocr_sNNN.md
ocr_sNNN_raw.json
```

Nicht zwei unabhängige OCR-Aufrufe für Markdown und JSON starten: Beide Dateien
müssen aus derselben API-Antwort stammen.

### 4. Begleitdateien aus derselben OCR-Antwort erzeugen

Wenn die Layout-Antwort entsprechende Blöcke enthält:

- erkannte Tabellen nach `tabellen_sNNN.md` übernehmen;
- erkannte Bildregionen mit ihren Original-Pixelkoordinaten in
  `skizzen_sNNN.json` dokumentieren;
- die Bildregionen verlustfrei unter `skizzen/sNNN_skizze_01.png` usw. ablegen;
- zur schnellen Sichtkontrolle einen `skizzen_kontaktbogen.jpg` erzeugen.

Die Bounding Boxes beziehen sich auf die Pixelorientierung der OCR-Eingabe.
Ausschnitte danach entsprechend der EXIF-Orientierung aufrecht drehen. Das
vollständige Originalbild bleibt trotzdem der maßgebliche Beleg.

Automatisch erkannte Bildregionen sind nur Vorschläge. Das vollständige Bild
gegen die Ausschnitte prüfen. Eine vom OCR-Modell übersehene relevante Tabelle,
Formel oder Zeichnung als zusätzlichen Ausschnitt erfassen und ihre Herkunft
sichtbar dokumentieren. Keine Beschriftung oder Geometrie erfinden.

### 5. Seitenstatus anlegen

Im Seitenordner eine kurze `sNNN.md` als Einstieg anlegen. Sie enthält:

- Seitentitel oder Thema, soweit sicher aus dem Bild ersichtlich;
- den deutlich sichtbaren Status
  `OCR-Rohfassung – noch nicht menschlich verifiziert`;
- den relativen Link zum unveränderten Originalbild;
- Links auf OCR-Markdown, Layout-JSON, Tabellen und Skizzenartefakte;
- den Hinweis, dass Text, Werte, Formeln und Zeichnungslabels erst durch Werner
  freigegeben werden.

Der Ordnername `human_verifiziert` ist keine automatische Seitenfreigabe. Erst
Werners ausdrückliche Prüfung macht den betreffenden Inhalt menschlich
verifiziert.

### 6. Technisch verifizieren

Vor Abschluss prüfen:

1. `sNNN.md` und alle erzeugten Dateien liegen im richtigen Zielordner.
2. Der Link zum Originalbild sowie alle Begleitlinks existieren.
3. Markdown und JSON stammen aus derselben OCR-Antwort.
4. Das JSON enthält die erwartete Seite sowie vorhandene Tabellen-, Bild- und
   Layoutblöcke.
5. Alle Skizzenausschnitte sind aufrecht und gehören zur Besitzerseite.
6. Nachbarseitentext wurde nicht als Inhalt der Besitzerseite übernommen.
7. OCR-Fehler, Kästchen, Schrittzahlen und grafische Labels wurden nicht still
   korrigiert oder als bestätigt ausgegeben.
8. `git status --short` vollständig ansehen; keine fremden Änderungen anfassen.

## Erwartete Struktur

```text
03_grundschnitte_roecke_s32-48/
└── s035/
    ├── s035.md
    ├── ocr_s035.md
    ├── ocr_s035_raw.json
    ├── tabellen_s035.md
    ├── skizzen_s035.json
    ├── skizzen_kontaktbogen.jpg
    └── skizzen/
        ├── s035_skizze_01.png
        ├── s035_skizze_02.png
        └── s035_skizze_03.png
```

Nicht vorhandene Inhaltsarten müssen nicht durch leere Dateien vorgetäuscht
werden.

## Menschliche Prüfung danach

OCR liefert nur eine günstige Rohabschrift. Werner prüft anschließend am Buch:

- vollständigen Wortlaut und Absatzfolge;
- Zahlen, Maße, Einheiten und Schrittkennungen;
- Tabellenstruktur und Tabellenwerte;
- Formeln und Rechenzeichen;
- sämtliche Zeichnungslabels und ihre Zuordnung.

Nur ausdrücklich bestätigte Inhalte werden in der Seitenfassung als menschlich
verifiziert bezeichnet. Unsicheres bleibt offen; aus OCR-Konfidenz oder
Plausibilität entsteht keine Bestätigung.
