Wir extrahieren und normalisieren Formeln aus Hofenbitzer Band 1 unter
`100_quellen/11_hofenbitzer_band_1_human_verifiziert/`, genau eine Buchseite pro
Arbeitsgang.

Wenn Werner zum Beispiel `Formeln s038` schreibt, führe den folgenden Ablauf für
genau diese Seite aus.

## 1. Verbindlichen Kontext laden

Lies vollständig:

- `AGENT.md` im Repository-Wurzelordner;
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/AGENT.md`;
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/SKILL.md`;
- `100_quellen/11_hofenbitzer_band_1_human_verifiziert/OCR_WORKFLOW.md`.

Ermittle danach den tatsächlichen Kategorie- und Seitenordner `sNNN`. Dieser
Prompt gilt besonders für:

- `03_grundschnitte_roecke_s32-48/`;
- `04_modelle_roecke_s49-105/`;
- `07_grundschnitte_oberteile_s171-196/`.

Arbeite nicht an Nachbarseiten. Seitenübergreifende Abhängigkeiten nur verlinken,
nicht kopieren.

## 2. Bereitschaft prüfen

Lies im Seitenordner:

- `sNNN.md`;
- `ocr_sNNN.md`;
- vorhandene `tabellen_sNNN.md`;
- vorhandene `formeln_sNNN.md` und `formeln_sNNN_normalisiert.md`;
- die verlinkte Originalseite sowie nötige Skizzenausschnitte.

Die Formelarbeit darf beginnen, wenn alle formel- und coderelevanten Stellen für
die Seite am Original bestätigt und in `sNNN.md` dokumentiert sind. Die ganze
Seite muss dafür noch nicht vollständig menschlich verifiziert sein.

Bei einer offenen oder widersprüchlichen relevanten Stelle stoppen und nur den
Blocker nennen. Keine Formel plausibel ergänzen und keine neue Prüfstelle aus
einer freien Bildsuche erfinden.

## 3. Fototreu extrahieren

Erfasse alle coderelevanten Beziehungen der Seite:

- Formeln und Rechenbeispiele;
- Variablen, Zahlen, Brüche, Operatoren und Einheiten;
- Tabellenzeilen mit Eingabe, Operation oder Ergebnis;
- Bereiche, Grenzwerte, Bedingungen und Auswahlregeln;
- geometrische Beziehungen aus Text oder Zeichnung.

Nicht als Formel behandeln:

- bloße Bildnummern oder Seitenverweise;
- reine Stückzahlen und Produktionskennzeichen wie `1×` oder `2×-p`;
- isolierte Maße ohne Rechen- oder Auswahlbeziehung;
- OCR-Rauschen und ausdrücklich ausgeschlossene Fremdtexte.

Schreibe die fototreue Fassung nach:

`<Kategorie>/sNNN/formeln_sNNN.md`

Regeln:

1. Buchfassung mit Dezimalkommas, Vorzeichen, Bereichen, Einheiten und
   Variablennamen exakt erhalten.
2. Jede Stelle mit Quelle und Zeilenbereich aus OCR oder Tabelle belegen;
   zeichnungsgebundene Stellen zusätzlich als solche kennzeichnen.
3. Formeln in `text`-Codeblöcken schreiben; Hinweise außerhalb der Codeblöcke.
4. Gedruckte Rechenfehler oder Widersprüche nicht still berichtigen.
5. Eine bestehende Formeldatei gezielt aktualisieren, nicht doppelt anlegen.
6. Enthält die Seite keine Formel, keine leere Formeldatei erzeugen; den Befund
   knapp in `sNNN.md` dokumentieren.

## 4. Extraktion prüfen

Vor jeder Normalisierung sicherstellen:

- jede Buchfassung ist durch die bestätigte Seitenakte und die Quelle gedeckt;
- alle Formelstellen aus Text, Tabelle und relevanter Zeichnung sind erfasst;
- keine ausgeschlossenen Labels oder OCR-Schleifen wurden übernommen;
- `formeln_sNNN.md` ist nicht leer und enthält ausgeglichene Codeblöcke.

Bei einem Fehler zuerst die Extraktion berichtigen. Noch nicht normalisieren.

## 5. Getrennt normalisieren

Schreibe anschließend die technische Fassung nach:

`<Kategorie>/sNNN/formeln_sNNN_normalisiert.md`

Für jede eigenständige Formel angeben:

- **Quelle:** Link auf `formeln_sNNN.md` und genaue Stelle;
- **Buchfassung:** unverändert und vollständig in einem `text`-Codeblock;
- **Technische Formel:** eindeutige Variablen und Operationen;
- **Eingaben und Einheiten**;
- **Ausgabe und Einheit**;
- **Bereiche, Bedingungen und Auswahlentscheidungen**;
- **Abhängigkeiten** zu anderen Formeln oder Seiten;
- **Status:** `normalisiert`, `offen` oder `gesperrt`;
- **Offene Fragen oder Widersprüche**.

Normalisierungsregeln:

1. Buchfassung und technische Fassung strikt trennen.
2. Bereiche bleiben Bereiche; ohne Buchregel keinen festen Wert oder Default
   auswählen.
3. `ca.`, `bis`, Empfehlungen und fachliche Auswahlspielräume erhalten.
4. Gedruckte Beispiele unabhängig nachrechnen, aber nicht als Beweis für eine
   andere Buchformel verwenden.
5. Gedruckte Abweichungen sichtbar nebeneinander dokumentieren; Unklares erhält
   den Status `offen` oder `gesperrt`.
6. Keine Python-Funktion, kein Engine-Vertrag und keine neue Fachregel erzeugen.
7. Keine leere normalisierte Datei anlegen.

## 6. Abschluss prüfen

Nach dem Schreiben:

- jede Buchfassung bytegetreu mit `formeln_sNNN.md` vergleichen;
- Rechenbeispiele unabhängig prüfen;
- Quellenlinks, Codeblöcke und Statusfelder kontrollieren;
- sicherstellen, dass OCR-, Tabellen-, Bild-, Skizzen- und JSON-Dateien
  unverändert blieben;
- `git diff --check` und `git status --short` ausführen;
- fremde Änderungen nicht anfassen.

Berichte abschließend knapp:

```text
Seite: sNNN
Extraktion: erstellt / aktualisiert / keine Formel
Normalisierung: erstellt / aktualisiert / blockiert
Formeln: <Anzahl>
Offen oder gesperrt: <Anzahl und kurze Begründung>
Geänderte Dateien: <Pfade>
Bereit für einen späteren Codevertrag: ja / teilweise / nein
Gesamte Seite menschlich verifiziert: nein, sofern nicht separat bestätigt
```
