# ATELIER — Roadmap und Kontextlandkarte

## Zweck

Diese Datei zeigt den Weg vom verständlichen Engineering Context bis zum geprüften geraden Rock. Sie erklärt, welche Markdown-Datei welche Aufgabe besitzt, wo sie liegt und wann sie geladen wird.

## Wichtigkeitsstufen

- **A — verbindlich:** bestimmt Ziel, Regeln, Verträge oder Fachwahrheit; vor abhängiger Arbeit lesen.
- **B — arbeitsbezogen:** wird nur für das gerade bearbeitete Modul oder den Baustein geladen.
- **C — unterstützend:** hilft beim Verstehen und Erinnern, ist aber keine automatische Projekt- oder Fachwahrheit.

## Grundsatz für neue KI-Sessions

Nicht alle Dateien bilden einen einzigen globalen Kontext.

```text
kleiner globaler Pflichtkontext
+ AGENT.md-Kette des bearbeiteten Pfads
+ lokale Spec und Verträge
+ nur die benötigten verifizierten Quellen
```

So besitzt jede Session ein gemeinsames Gedächtnis, ohne mit dem ganzen Repository überladen zu werden.

## Kontextlandkarte

### Globaler Pflichtkontext

| Wichtigkeit | Datei und Ort | Aufgabe |
|---|---|---|
| A | [`AGENT.md`](AGENT.md) | Oberste Arbeitsregeln, Verantwortung, Grenzen, Bereichskarte und Ladereihenfolge. Muss kurz bleiben und nur direkte Bereiche nennen. |
| A | [`PRODUKTZIEL.md`](PRODUKTZIEL.md) | Beschreibt, welches nutzbare Produkt entstehen soll und was ausdrücklich nicht Teil des Endprogramms ist. |
| A | [`ARCHITEKTUR.md`](ARCHITEKTUR.md) | Beschreibt Schichten, Datenfluss und Abhängigkeiten vom Körpermaß bis zur Ausgabe. |
| A | [`DATENMODELL.md`](DATENMODELL.md) | Verbindlicher gemeinsamer Vertrag für Maße, Entscheidungen, Berechnungen, Geometrie, Herkunft und Validierung. |
| B | [`ROADMAP.md`](ROADMAP.md) | Diese Orientierung: Reihenfolge der Arbeit, Dokumentrollen und Nachweisstufen. Sie ersetzt keine lokale Spec. |
| B | [`Benennung der Stufen, Ordner und Dateien.md`](Benennung%20der%20Stufen,%20Ordner%20und%20Dateien.md) | Verbindliche Benennungslogik für neue Stufen, Ordner und Dateien; nur bei Struktur- oder Benennungsarbeit laden. |

### Fach- und Mathematikkontext

| Wichtigkeit | Datei und Ort | Aufgabe |
|---|---|---|
| A | `100_quellen/10_hofenbitzer_band_1_digital/AGENT.md` | Schützt die digitalen Buchquellen und legt fest, welche Ableitungen dort zulässig sind. |
| A | passende `sNNN.md` und `formeln_sNNN_normalisiert.md` unter `100_quellen/` | Liefern den menschlich geprüften Buchbeleg für den konkreten Codeschritt. Nur die benötigten Seiten laden. |
| B | `400_mathematik/AGENT.md` | Regelt den Bereich der fachunabhängigen Mathematik und Geometrie. |
| B | `400_mathematik/Uebersicht.md` | Führt zu den vorhandenen Mathematikthemen und verhindert doppelte Lösungen. |
| A | passende Dateien in `400_mathematik/10_codevertraege/` | Definieren die mathematischen und geometrischen Verträge, die der Code tatsächlich einhalten muss. |
| C | passende Dateien in `400_mathematik/20_recherche/` | Erklären und untersuchen Mathematik; sie werden erst durch einen bestätigten Codevertrag verbindlich. |

### Rock und Konstruktionsbausteine

| Wichtigkeit | Datei und Ort | Aufgabe |
|---|---|---|
| A | `200_funktionen/AGENT.md` | Regelt Bausteinaufbau, Zwei-KI-Arbeitszug, Prüfgrenzen und Fokus auf den geraden Rock. |
| A | `200_funktionen/10_grundschnitte_roecke_s32-39/AGENT.md` | Lokale Regeln und direkte Gliederung des Rock-Grundschnitts. |
| A | `200_funktionen/10_grundschnitte_roecke_s32-39/spec_gerader_rock.md` | Beschreibt den vollständigen Pilotumfang, seine Eingaben, Ergebnisse, Grenzen und Abnahme. |
| B | untergeordnete `AGENT.md` im aktiven Rockschritt | Benennen nur die direkten Kinder und Grenzen des gerade bearbeiteten Konstruktionsabschnitts. |
| B | untergeordnete `README.md` im aktiven Baustein | Beschreiben Zweck, Quelle, Ein- und Ausgabe, Status und nächsten Schritt dieses einzelnen Bausteins. Sie dürfen keine globale Regel duplizieren. |

### Messmodul

| Wichtigkeit | Datei und Ort | Aufgabe |
|---|---|---|
| A | `300_messmodul/AGENT.md` | Regelt den Bereich, seine direkten Kinder, die Grenze zwischen Körpermaß und Beobachtung sowie die Übergabe an `DATENMODELL.md`. |
| A | `300_messmodul/SPEC.md` | Legt für den Rock-Pilot Maß-IDs, Einheiten, Pflichtwerte, Validierung und die Übergabe des Personenprofils fest. |

Der vorhandene Code wird beim Pilot über eine kleine `SPEC.md` an den gemeinsamen Vertrag angeschlossen; kein vorsorglicher Detailbestand.

### Patchwork-Modul

| Wichtigkeit | Datei und Ort | Aufgabe |
|---|---|---|
| A | `500_patchwork/AGENT.md` | Regelt den visuellen Auswahlbereich und verhindert, dass nicht vorhandene Bausteine als Option erscheinen. |
| B | `500_patchwork/README.md` | Gibt Werner und neuen Sessions einen kurzen Überblick über den Ordner. |
| A | `500_patchwork/SPEC.md` | Beschreibt Auswahl, erlaubte Positionen, Datenfluss und offene Entscheidungen. Vor Codebeginn muss sie an einem realen Rockbaustein konkretisiert werden. |

### Gesprächs- und Denknotizen

Diese vier Dateien gehören zusammen. Sie halten die Entwicklung der Ideen fest, sind aber kein Pflichtkontext und keine automatische Fachwahrheit.

| Wichtigkeit | Datei und Ort | Aufgabe |
|---|---|---|
| C | [`800_werners spick/geminichatanweisung01.md`](800_werners%20spick/geminichatanweisung01.md) | Gespräch 1/4: gemeinsames Datenmodell; die verbindliche Fassung liegt in `DATENMODELL.md`. |
| C | [`800_werners spick/geminichatanweisung02.md`](800_werners%20spick/geminichatanweisung02.md) | Gespräch 2/4: allgemeine Prinzipien modularer Software und mögliche Werkzeuge. |
| C | [`800_werners spick/geminichatanweisung03.md`](800_werners%20spick/geminichatanweisung03.md) | Gespräch 3/4: zusätzliche Körpergeometrie, 3D-Forschung und zweistufige visuelle Patchwork-Idee. |
| C | [`800_werners spick/geminichatanweisung04.md`](800_werners%20spick/geminichatanweisung04.md) | Gespräch 4/4: Engineering Context, Zwei-KI-Rollen, Prüfwerkzeuge und Repo-Butler. |
| C | Dateien unter `800_werners spick/` | Erklären Begriffe und Denkmodelle für Werner; sie sind Orientierung, keine Fachfreigabe. |

## Roadmap zum geraden Rock

### 1. Globalen Context verstehen und stabilisieren

- [ ] Werner prüft `PRODUKTZIEL.md`, `ARCHITEKTUR.md` und `DATENMODELL.md` in eigenen Worten.
- [ ] Widersprüche und unverständliche Begriffe werden gemeinsam geklärt.
- [ ] Globale Dateien bleiben knapp; lokale Einzelheiten wandern nicht in den Pflichtkontext.

**Ergebnis:** Werner kann Ziel, Datenfluss und Grenzen gegenüber KI und Schneiderin erklären.

### 2. Fachlichen Kontext des Rocks prüfen

- [ ] Für Seiten 32–39 werden nur die benötigten Buchseiten, Formeln und offenen Prüfstellen bestimmt.
- [ ] Werner trennt Buchaussage, eigene Entscheidung, KI-Deutung und offene Frage.
- [ ] Nur abhängige Bausteine werden durch offene Prüfstellen blockiert.

**Ergebnis:** Jeder geplante Codeschritt besitzt einen auffindbaren und menschlich verantworteten Fachbeleg.

### 3. Vertikalen Pilotvertrag festlegen

- [ ] Das Messmodul erhält nur den für den geraden Rock nötigen Vertrag.
- [ ] Die Rock-Spec benennt die benötigten Bausteine und gemeinsamen Datenobjekte.
- [ ] Das Patchwork-Modul bildet zunächst nur tatsächlich vorhandene Rockbausteine und feste erlaubte Positionen ab.
- [ ] Ein vollständiger Beispielauftrag wird vom Personenprofil bis zum erwarteten Schnittteil beschrieben.

**Ergebnis:** Ein kleiner, vollständiger Weg durch Messmodul, Rockbausteine und Patchwork ist vor dem Codieren prüfbar.

### 4. Rockbausteine einzeln codieren

Für jeden Baustein gilt:

1. Koordinierende KI erstellt den begrenzten Vorprompt.
2. Codierende KI prüft zuerst Quellen, Verträge und fehlende Entscheidungen.
3. Erst danach entstehen Python-Code und betroffene Tests.
4. Koordinierende KI prüft Diff, Tests und Anschlussfähigkeit unabhängig.
5. Werner entscheidet offene fachliche Fragen.

**Ergebnis:** Kleine, getestete und über Verträge verbindungsfähige Konstruktionsbausteine.

### 5. Geraden Rock zusammensetzen

- [ ] Personenprofil und Schnittauftrag werden validiert.
- [ ] Vorder- und Rückenteil, Abnäher, Hüftbogen und weitere nötige Rockschritte werden verbunden.
- [ ] Anschlusskanten, Maße, Einheiten, Provenienz und Fehlerzustände werden geprüft.
- [ ] Das Patchwork-Modul kann nur vorhandene und erlaubte Varianten wählen.

**Ergebnis:** Ein reproduzierbarer digitaler Konstruktionsstand für den vollständigen geraden Rock.

### 6. Ausgabe und Nachweise trennen

- [ ] SVG, DXF und maßstäbliche PDF entstehen aus demselben Konstruktionsstand.
- [ ] Technische Tests prüfen Code, Daten und Geometrie.
- [ ] CLO prüft die digitale Wirkung.
- [ ] Nessel und Anprobe prüfen das reale Ergebnis.
- [ ] Abweichungen werden der richtigen Ursache zugeordnet: Quelle, Entscheidung, Formel, Code, Material oder Verarbeitung.

**Ergebnis:** Ein technisch und praktisch bewerteter Pilot, nicht nur eine bestandene Test-Suite.

### 7. Arbeitsweise auswerten

Nach dem Pilot wird geprüft:

- War der Kontext für jede KI auffindbar und klein genug?
- Waren Arbeitspakete passend bemessen?
- Haben Messmodul, Patchwork und Rock dieselben Datenverträge verstanden?
- Welche manuellen Prüfungen lassen sich künftig deterministisch automatisieren?
- Welche Markdown-Dateien waren nötig, doppelt oder fehlend?
- Welche Erkenntnisse gelten nur für den Rock und welche global?

**Ergebnis:** Erst aus dem realen Pilot werden die nächsten Architektur- und Dokumententscheidungen abgeleitet.

## Aktueller nächster Schritt

Werner prüft den vollständigen Pilotauftrag in `spec_gerader_rock.md`. Danach werden für den ersten begrenzten Codebaustein nur die benötigten Quellen, Mathematikverträge und offenen Fachentscheidungen bestimmt.
