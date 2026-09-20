Wir klären vorab nur die formel- und coderelevanten Stellen einer Hofenbitzer-Seite unter
`100_quellen/11_hofenbitzer_band_1_human_verifiziert/`.

Dieser Prompt ist eigenständig und läuft vor der vollständigen Seitenverifizierung.
Er bestätigt niemals automatisch die ganze Seite.

Wenn Werner zum Beispiel `Formelprüfung s100` schreibt, bearbeite genau diese Seite.

## 1. Kontext und Seite laden

Lies vollständig:

- `AGENT.md` im Repository-Wurzelordner;
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/AGENT.md`;
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/SKILL.md`;
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/OCR_WORKFLOW.md`.

Lies danach im tatsächlichen Seitenordner `sXXX.md`, `ocr_sXXX.md` sowie vorhandene
Tabellen- und Formeldateien. Ziehe Skizzen und das Originalbild nur für konkrete
formel- oder coderelevante Stellen hinzu. Arbeite nicht an Nachbarseiten.

## 2. Nur relevante Prüfstellen auswählen

Aufnehmen:

- Formeln, Rechenbeispiele und Tabellenwerte;
- Variablen, Abkürzungen, Zahlen, Einheiten, Brüche und Rechenzeichen;
- Eingaben, Ausgaben und Abhängigkeiten einer Berechnung;
- Bereiche, Grenzwerte, Bedingungen, Auswahlregeln und Ausnahmen;
- geometrische Anweisungen und Zeichnungslabels, die eine Konstruktion bestimmen;
- Begleittext, wenn er die Bedeutung oder Anwendung einer Formel beziehungsweise
  späteren Python-Funktion verändert.

Nicht aufnehmen:

- reine Rechtschreibung und allgemeine Textfehler ohne fachliche Auswirkung;
- Bildunterschriften und Layoutfragen ohne Einfluss auf Formel oder Konstruktion;
- allgemeine Seitentexte, die keine Eingabe, Regel, Grenze oder Operation festlegen.

Nicht jedes Maß und nicht jedes `=` ist automatisch eine Formel. Eine Stelle ist nur
dann coderelevant, wenn sie eine spätere Eingabe, Berechnung, Entscheidung,
Geometrieoperation oder Prüfung beeinflusst.

## 3. Prüfstellen im Chat ausgeben

In dieser ersten Phase keine Datei ändern. Gib eine nummerierte Liste aus:

```text
1. [FORMEL / CODE-REGEL / GRENZE / GEOMETRIE] Kurztitel
   Fundstelle: ocr_sXXX.md:Zeile oder tabellen_sXXX.md:Zeile
   Stelle auf der Seite: möglichst genaue Position
   OCR: „exakter vorhandener Wortlaut"
   KI-Vorschlag: „exakter vorgeschlagener Wortlaut"
   Coderelevanz: kurze konkrete Auswirkung
   Bildbefund: eindeutig / nicht sicher lesbar / Konflikt
```

Regeln:

- Immer genaue Datei- und Zeilenangaben nennen.
- OCR-Wortlaut exakt zitieren.
- Einen KI-Vorschlag nur bei eindeutigem Bildbeleg oder bereits dokumentiertem
  Handbefund geben; sonst `KI-Vorschlag: keiner – offen lassen`.
- Buchfassung und spätere technische Normalisierung nicht vermischen.
- Keine Formel verbessern, ergänzen oder mathematisch glätten.
- Keine vollständige Seitenverifizierung vortäuschen.

Am Ende dieses Antwortschema anzeigen:

```text
1 KI                    = KI-Vorschlag ist richtig
1 OCR                   = OCR ist richtig
1 ÄNDERN: ...           = Werners genauer Wortlaut
1 OFFEN                 = noch nicht entscheidbar
REST = KI               = übrige eindeutige KI-Vorschläge übernehmen
CODEPUNKTE GEPRÜFT      = Werner hat alle aufgelisteten Codepunkte geprüft
```

## 4. Antwort auswerten und schreiben

- `KI`, `OCR`, `ÄNDERN`, `OFFEN` und `REST = KI` genauso auswerten wie angegeben.
- Ohne `REST = KI` sind nicht genannte Punkte nicht bestätigt.
- Punkte ohne sicheren KI-Vorschlag bleiben auch mit `REST = KI` offen.
- Bei Mehrdeutigkeit genau eine kurze Rückfrage stellen.

Nach eindeutiger Antwort:

1. bestätigte Textkorrekturen in `ocr_sXXX.md` eintragen;
2. bestätigte Tabellenkorrekturen in `tabellen_sXXX.md` eintragen;
3. eine vorhandene fototreue Formeldatei nur berichtigen, nicht normalisieren;
4. keine JSON-Datei verändern, auch `skizzen_sXXX.json` nicht;
5. Entscheidungen in `sXXX.md` unter
   `## Vorab geklärte formel- und coderelevante Stellen` dokumentieren;
6. allgemeine Prüfstellen nicht löschen und den Seitenstatus nicht auf
   `menschlich verifiziert` setzen.

Dieser Prompt erstellt noch keine Formelextraktion, Normalisierung, technische
Definition oder Python-Funktion. Er bereitet nur die belastbare Quellengrundlage vor.

## 5. Abschluss

Wenn `CODEPUNKTE GEPRÜFT` vorliegt und keine relevante Stelle offen ist, melde:

```text
Formel-/Codeprüfung: abgeschlossen
Bereit für Formel-Extraktion: ja
Gesamte Seite menschlich verifiziert: nein
```

Andernfalls nenne nur die verbleibenden Blocker. Prüfe die geänderten Stellen erneut,
lasse alle JSON-Dateien unverändert, sieh `git status --short` vollständig an und
fasse das Ergebnis knapp zusammen.
