---
name: hofenbitzer-page-ocr-verification
description: Use when preparing Hofenbitzer pages by OCR for Werner's verification.
version: 1.0.0
author: ATELIER
license: project-internal
metadata:
  hermes:
    tags: [hofenbitzer, ocr, source-verification, patternmaking]
    related_skills: []
---

# Hofenbitzer-Seiten per OCR vorbereiten

## Überblick

Dieser projektlokale Skill bereitet eine fotografierte Buchseite als
nachvollziehbare OCR-Rohfassung für Werners menschliche Prüfung vor. Er gilt für
`100_quellen/11_hofenbitzer_band_1_human_verifiziert/`.

Die verbindlichen Details liegen in zwei Dateien neben diesem Skill:

1. [`AGENT.md`](AGENT.md) – lokale Ordnung, Quellenstatus und Freigabegrenze;
2. [`OCR_WORKFLOW.md`](OCR_WORKFLOW.md) – vollständiger technischer Ablauf.

Beide Dateien müssen vor der Bearbeitung einer Seite geladen werden. Dieser
Skill ersetzt sie nicht.

## Wann verwenden

Verwenden, wenn eine Seite aus
`../20_hofenbitzer_band_1_bilder/01_Photos_hofenb_ba1_total/` per Mistral OCR in
den passenden Buchkategorie- und `sNNN`-Ordner übernommen werden soll.

Nicht verwenden, um:

- OCR ungeprüft als Buch- oder Fachwahrheit auszugeben;
- vorhandene Originalbilder zu verändern;
- fehlende Formeln, Beschriftungen oder Geometrie zu erfinden;
- eine Seite ohne Werners ausdrückliche Bestätigung als menschlich verifiziert
  zu kennzeichnen.

## Ablauf

1. **Regeln laden:** `AGENT.md` und `OCR_WORKFLOW.md` vollständig lesen.
   Abschluss: Zielkategorie, Seitenkennung und Freigabegrenze sind bekannt.
2. **Bild prüfen:** Originalbild nachweisen, EXIF-Orientierung kontrollieren und
   eine aufrechte Vorschau ansehen. Nachbarseiten oder abgeschnittene Bereiche
   vor der OCR erkennen. Abschluss: Die Besitzerseite ist vollständig und
   eindeutig abgegrenzt.
3. **Einmal OCR ausführen:** `mistral-ocr-latest` verwenden und Markdown sowie
   vollständiges Layout-JSON aus derselben API-Antwort erzeugen. Keine Secrets
   oder Base64-Bilder in Projektdateien schreiben. Abschluss: `ocr_sNNN.md` und
   `ocr_sNNN_raw.json` liegen im Zielordner.
4. **Artefakte trennen:** Erkannte Tabellen und Bildregionen gemäß
   `OCR_WORKFLOW.md` ablegen. Automatische Bounding Boxes am vollständigen Bild
   gegenprüfen und übersehene relevante Bereiche sichtbar offenlassen oder als
   belegte Ausschnitte ergänzen. Abschluss: Jede erzeugte Begleitdatei verweist
   auf dieselbe Besitzerseite.
5. **Status setzen:** Eine kurze `sNNN.md` mit Originalbild-Link, Arbeitslinks und
   `OCR-Rohfassung – noch nicht menschlich verifiziert` anlegen. Abschluss: Kein
   ungeprüfter Inhalt trägt einen Freigabestatus.
6. **Technisch prüfen:** Alle Links und Dateien auf Existenz prüfen,
   Skizzenausschnitte visuell kontrollieren und `git status --short` vollständig
   ansehen. Abschluss: Die Ausgabe liegt direkt im richtigen Zielordner und
   fremde Änderungen blieben unberührt.
7. **Werner vorlegen:** Wortlaut, Zahlen, Einheiten, Tabellen, Formeln und
   Zeichnungslabels einzeln am Buch bestätigen lassen. Abschluss: Nur
   ausdrücklich bestätigte Inhalte werden als menschlich verifiziert geführt.

## Erwartete Kerndateien

```text
sNNN/
├── sNNN.md
├── ocr_sNNN.md
├── ocr_sNNN_raw.json
├── tabellen_sNNN.md          # nur wenn vorhanden
├── skizzen_sNNN.json         # nur wenn vorhanden
├── skizzen_kontaktbogen.jpg  # nur wenn Skizzen geprüft werden
└── skizzen/                  # nur wenn Ausschnitte vorhanden
```

## Typische Fehler

1. **Nur im Temp-Ordner speichern:** Die fertigen Test- und Arbeitsartefakte
   gehören direkt in den passenden Zielordner.
2. **Zwei OCR-Aufrufe starten:** Markdown und JSON müssen aus derselben Antwort
   stammen.
3. **Nachbarseitentext übernehmen:** Besitzerseite vor der OCR visuell abgrenzen.
4. **Bounding Boxes für vollständig halten:** Das ganze Original gegen alle
   automatisch erkannten Ausschnitte prüfen.
5. **OCR still korrigieren:** Rohtext unverändert als Rohtext bewahren; belegte
   Korrekturen und menschliche Bestätigungen getrennt behandeln.
6. **Ordnername als Freigabe lesen:** `human_verifiziert` ersetzt Werners
   ausdrückliche Seitenprüfung nicht.

## Verifikationscheckliste

- [ ] `AGENT.md` und `OCR_WORKFLOW.md` wurden geladen.
- [ ] Originalbild und Zielseite stimmen überein.
- [ ] Seiteninhalt wurde nicht durch einen Zuschnitt abgeschnitten.
- [ ] OCR-Markdown und Layout-JSON stammen aus derselben Antwort.
- [ ] Tabellen und Bildregionen sind separat und nachvollziehbar abgelegt.
- [ ] Alle relativen Links existieren.
- [ ] Die Seite ist bis zur Bestätigung eindeutig als OCR-Rohfassung markiert.
- [ ] Keine fremden Arbeitsbaumänderungen wurden verändert.
