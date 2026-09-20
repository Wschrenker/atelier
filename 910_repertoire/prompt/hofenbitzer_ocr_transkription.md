Bereite Hofenbitzer Band 1, Seite XX per OCR für Werners spätere Prüfung vor
(Ordner `100_quellen/11_hofenbitzer_band_1_human_verifiziert`).

Lies zuerst vollständig und verbindlich:
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/AGENT.md`
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/SKILL.md`
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/OCR_WORKFLOW.md`

Führe den dort beschriebenen Ablauf für genau diese eine Seite aus:

1. Originalbild in `../20_hofenbitzer_band_1_bilder/01_Photos_hofenb_ba1_total/`
   nachweisen, der passenden Buchkategorie zuordnen, EXIF-Orientierung und
   vollständige Sichtbarkeit prüfen (Nachbarseite mitfotografiert?).
2. Einmal mit `mistral-ocr-latest` OCR ausführen (Werkzeug
   `C:\Users\Chromatic\AppData\Local\hermes\scripts\mistral_ocr.py`) und aus
   derselben Antwort `ocr_sXX.md` und `ocr_sXX_raw.json` erzeugen.
3. Erkannte Tabellen nach `tabellen_sXX.md`, erkannte Bildregionen nach
   `skizzen_sXX.json` + `skizzen/` trennen, Kontaktbogen erzeugen. Automatische
   Bounding Boxes gegen das vollständige Bild prüfen, übersehene Bereiche
   ergänzen.
4. `sXX.md` anlegen mit Status **„OCR-Rohfassung – noch nicht menschlich
   verifiziert"**, Links zu Originalbild und allen erzeugten Dateien, plus
   Abschnitten „Belege", „Anmerkungen zur OCR-Eingabe" und „Bekannte
   auffällige Stellen im Rohtext (noch nicht bestätigt)" – genau wie bei den
   bereits vorhandenen Seiten in diesem Ordner (z. B. s011, s012, s013).
5. Daraus eine Liste „Prüfstellen für Werner" ableiten (Wortlaut, Zahlen,
   Tabellen, Zeichnungslabels, alles was nur am Original zu klären ist) und
   mir am Ende genau diese Liste vorlegen, wie bisher auch.

Falls eine vorherige Seite noch nicht erfasst wurde: das macht nichts, ist
nicht Sache dieser Session – einfach nur die angegebene Seite bearbeiten.

Keine fremden, bereits geänderten Dateien im Repo anfassen; `git status
--short` vor Abschluss ansehen.
