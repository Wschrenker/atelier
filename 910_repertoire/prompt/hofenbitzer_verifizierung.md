Wir verifizieren Hofenbitzer Band 1 unter
`100_quellen/11_hofenbitzer_band_1_human_verifiziert/`, genau eine Seite pro
Arbeitsgang.

Wenn Werner zum Beispiel `prüfen s100` schreibt, führe den folgenden Ablauf für
genau diese Seite aus.

## 1. Verbindlichen Kontext laden

Lies zuerst vollständig:

- `AGENT.md` im Repository-Wurzelordner;
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/AGENT.md`;
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/SKILL.md`;
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/OCR_WORKFLOW.md`.

Ermittle danach den tatsächlichen Kategorie- und Seitenordner `sXXX`. Arbeite
nicht an Nachbarseiten. Das unveränderte Originalbild ist der Beleg; OCR ist nur
eine Rohabschrift.

## 2. Prüfstellen ermitteln

Lies für die angegebene Seite:

- `sXXX.md` als maßgebliche Liste der bereits bekannten auffälligen oder offenen
  Stellen;
- `ocr_sXXX.md`;
- vorhandene `tabellen_sXXX.md` und `formeln_sXXX.md`;
- vorhandene Skizzenhinweise und das verlinkte Originalbild, soweit sie für eine
  bestehende Prüfstelle nötig sind.

Erfinde aus einer freien Bildsuche keine zusätzlichen Prüfstellen. Eine weitere
Abweichung darf nur ergänzt werden, wenn Originalbild, genaue Position,
gedruckter Wortlaut und Gegenlesung eindeutig sind. Unsicheres bleibt offen.

## 3. Ausgabe im Chat

Ändere in dieser ersten Phase noch keine Datei. Gib zuerst eine nummerierte,
leicht beantwortbare Liste aus. Jede Prüfstelle erhält genau dieses Schema:

```text
1. Kurztitel der Prüfstelle
   Fundstelle: ocr_sXXX.md:Zeile oder tabellen_sXXX.md:Zeile
   Stelle auf der Seite: Spalte/Absatz/Tabelle/Zeichnung, möglichst genau
   OCR: „exakter vorhandener Wortlaut"
   KI-Vorschlag: „exakter vorgeschlagener Wortlaut"
   Bildbefund: eindeutig / nicht sicher lesbar / Konflikt
```

Regeln für diese Liste:

- Dateipfad und genaue Zeilennummern immer angeben, damit Werner die Stelle
  sofort findet.
- OCR-Wortlaut exakt zitieren, nicht zusammenfassen.
- Einen KI-Vorschlag nur geben, wenn er am Original eindeutig lesbar oder durch
  Werners bereits dokumentierten Handbefund belegt ist.
- Bei Unsicherheit schreiben: `KI-Vorschlag: keiner – offen lassen`.
- Text, Zahlen, Einheiten, Rechenzeichen, Tabellenwerte und Zeichnungslabels
  getrennt behandeln, wenn Werner sie getrennt entscheiden können muss.
- Keine lange Einleitung und keine Wiederholung des gesamten Seitentextes.

Am Ende immer dieses Antwortschema anzeigen:

```text
1 KI                 = KI-Vorschlag ist richtig
1 OCR                = OCR ist richtig
1 ÄNDERN: ...        = Werners genauer Wortlaut
1 OFFEN              = noch nicht entscheidbar
REST = KI            = alle nicht genannten Punkte mit eindeutigem
                       KI-Vorschlag übernehmen
SEITE GEPRÜFT        = Werner hat zusätzlich die ganze Seite selbst gelesen
                       und geprüft
```

Ein Beispiel für eine kurze Antwort ist:

```text
1 KI
3 OCR
5 ÄNDERN: Separater Futterrock
REST = KI
SEITE GEPRÜFT
```

## 4. Werners Antwort auswerten

- `KI`: vorgeschlagenen Wortlaut übernehmen.
- `OCR`: bestehenden OCR-Wortlaut unverändert lassen und als bestätigt werten.
- `ÄNDERN`: ausschließlich Werners angegebenen Wortlaut übernehmen.
- `OFFEN`: nichts ändern und die Prüfstelle offen lassen.
- `REST = KI`: nur die nicht einzeln genannten Punkte übernehmen, die einen
  **eindeutigen** KI-Vorschlag besitzen. Punkte ohne sicheren KI-Vorschlag
  bleiben offen.
- Ohne `REST = KI` sind nicht genannte Punkte **nicht bestätigt**.
- Eine leere oder mehrdeutige Antwort ist keine Zustimmung.

Wenn eine Nummer oder Korrektur nicht eindeutig zuordenbar ist, stelle genau
eine kurze Rückfrage und ändere bis zur Klärung nichts an diesem Punkt.

## 5. Änderungen ausführen

Nach einer eindeutigen Antwort:

1. Wortlaut nur in `ocr_sXXX.md` berichtigen.
2. Tabellenkorrekturen zusätzlich beziehungsweise stattdessen in
   `tabellen_sXXX.md` berichtigen.
3. Formelstellen nur in der dafür vorgesehenen Formeldatei berichtigen und die
   bestätigte Buchfassung von einer späteren fachlichen Normalisierung trennen.
4. Keine JSON-Datei verändern – auch `skizzen_sXXX.json` nicht. Bestätigungen
   ausschließlich in `sXXX.md` dokumentieren.
5. Den Prüfstatus und die erledigten beziehungsweise offenen Stellen in
   `sXXX.md` knapp und nachvollziehbar aktualisieren.

Die Seite darf nur dann als **menschlich verifiziert** markiert werden, wenn:

- alle vorhandenen Prüfstellen geklärt sind; und
- Werner ausdrücklich `SEITE GEPRÜFT` geschrieben hat.

Das Auflösen der aufgezählten Prüfstellen allein bestätigt nicht automatisch
den übrigen Seitentext.

## 6. Abschluss prüfen und knapp berichten

Nach dem Schreiben:

- geänderte Stellen erneut mit Werners Antwort abgleichen;
- sicherstellen, dass JSON-Rohdateien unverändert sind;
- alle offenen Punkte nennen;
- `git status --short` vollständig prüfen und fremde Änderungen nicht anfassen;
- im Chat kurz berichten: übernommen, unverändert bestätigt, offen und
  Seitenstatus.
