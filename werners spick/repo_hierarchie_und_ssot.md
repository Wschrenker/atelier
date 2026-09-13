# ATELIER: Hierarchie, SSOT und Arbeitskette

> **Status:** Denk- und Ordnungsmodell aus dem Gespräch mit Werner. Noch keine automatisch geltende Repository-Regel und noch kein Auftrag zur Umstrukturierung.

## 1. Zweck

Dieses Modell soll drei Dinge ermöglichen:

1. Werner und Hermes behalten den Überblick über das Repository.
2. Menschen und Agenten arbeiten nach sichtbaren Regeln oder ändern diese bewusst mit Werner.
3. Jede Arbeit bleibt auf das erfolgreiche Ziel ausgerichtet: ein fachlich und technisch verlässliches Schnittmusterprogramm.

Es soll Drift verhindern, ohne das Repository mit gleichlautenden Markdown-Dateien zu überladen.

---

## 2. Grundhaltung und Rollen

Werner betrachtet Wahrheit als eine **temporäre Schnittstelle einer Wahrnehmung**. Daraus folgt Verantwortung: Eine festgelegte Wahrheit darf sich ändern, aber nicht unbemerkt und nicht durch einen Agenten allein.

### Instanzen

1. **Werner** bestimmt Richtung, Priorität und fachliche Wahrheit. Er nimmt reale Ergebnisse ab und kann geltende Wahrheiten gemeinsam mit Hermes ändern.
2. **Hermes** hält Übersicht und Gedächtnis, findet die zuständige SSOT, schneidet kleine Arbeitsaufträge, promptet Claude Code, prüft dessen Änderungen unabhängig und achtet auf das Zusammenspiel des gesamten Repositorys.
3. **Claude Code in VS Code** konzentriert sich auf den begrenzten Codeauftrag, führt die verlangten Tests aus und berichtet zurück. Claude entscheidet weder allein über Architektur noch über fachliche Wahrheit.
4. **Tests** belegen einen technischen Zustand innerhalb der getesteten Grenzen.
5. **CLO 3D und Nessel** prüfen, bestätigen oder korrigieren die fachliche Wirklichkeit.
6. **Git** hält nachvollziehbar fest, was wann tatsächlich geändert und als technischer Stand akzeptiert wurde.

### Schutzregeln

- Idee ist nicht gleich Entscheidung.
- Entscheidung ist nicht gleich Arbeitsauftrag.
- Geänderter Code ist nicht gleich geprüfter Code.
- Technisch grüner Code ist nicht gleich fachlich bestätigte Wirklichkeit.
- Eine neue fachliche Wahrheit braucht Werner.
- Commit, Push, Löschen, Verschieben, Downloads, destruktive Git-Aktionen und Veröffentlichung benötigen Werners einmaliges `#` für genau den besprochenen Schritt.

---

## 3. Vorgeschlagene Ordnerebenen

`C:\ATELIER` ist das Dach und die einzige aktive Repository-Heimat. Die Nummernwörter sind Adressen zur Orientierung, keine mathematischen Werte.

| Physische Stufe | Werners Name | Beispiel | Aufgabe |
|---:|---|---|---|
| Dach | **ATELIER** | `C:\ATELIER` | Repository, oberste Regeln und globale Navigation |
| 1 | **Hunderter** | `200_funktionen` | großer Verantwortungs- oder Wissensbereich |
| 2 | **Zehner** | `10_hofenbitzer_band_1_digital` | zusammenhängende Hauptgruppe innerhalb eines Hunderters |
| 3 | **Einer** | `01_grundlagen_s8-31` | begrenzter fachlicher Abschnitt oder Arbeitsbereich |
| 4 | **Zehntel oder Dateien** | `0.20_<name>` oder direkt benannte Dateien | Unterfunktion, Arbeitsschritt oder fertiger Blattknoten |
| 5 | **Hundertstel oder Dateien** | `0.010_<name>` oder direkt benannte Dateien | kleinste notwendige Unterteilung oder fertiger Blattknoten |

### Benennungsregeln für das Modell

- Eine Ebene wird nur angelegt, wenn sie eine echte fachliche oder technische Grenze besitzt.
- Wenn Dateien auf Ebene 3 oder 4 verständlich und eindeutig liegen können, ist keine tiefere Ordnerebene nötig.
- `0.20`, `0.34`, `0.010` und `0.034` sind feste Ordnungsadressen. Sie sollten nicht mit Varianten wie `0.2` oder `0.01` gemischt werden.
- Ein Ordnername erklärt den fachlichen Inhalt; die Nummer erklärt nur die Stellung.
- Die bestehende Struktur wird nicht allein wegen dieses Denkmodells umbenannt oder verschoben.

### Aktueller beobachteter Stand

Im heutigen Arbeitsbaum existiert bereits eine fünfstufige Form, zum Beispiel:

```text
C:\ATELIER
└── 200_funktionen
    └── 02_grundschnitte_roecke_s32-39
        └── 01_gerader_rock_konstruktionstabelle_und_grundgeruest_s32-33
            └── 01_konstruktionstabelle_erstellen_s32-33
                ├── README.md
                ├── konstruktionstabelle.py
                └── test_konstruktionstabelle.py
```

Der vorgeschlagene Zehner `10_hofenbitzer_band_1_digital` und der Einer `01_grundlagen_s8-31` wurden bei der Prüfung noch nicht als vorhandene Pfade gefunden. Werner hat bereits erkannt, dass dafür Änderungen im Repository nötig sein könnten. Dieses Dokument entscheidet diese Umstrukturierung noch nicht.

---

## 4. Markdown-Dateien: Frage, Eigenschaft, Korrelation und Ebene

Grundsatz: **Eine Frage hat einen Besitzer.** Andere Dateien wiederholen seine Antwort nicht, sondern verlinken auf ihn.

| Datei | Sie beantwortet die Frage | Eigenschaft / Autorität | Korreliert direkt mit | Empfohlene Ordnerebene |
|---|---|---|---|---|
| **`SOUL.md`** | Wie arbeiten Werner, Hermes und Claude sicher, ehrlich und verantwortlich zusammen? | stabiler Haltungs- und Schutzvertrag; keine fachliche oder technische SSOT | `AGENT.md`, `HERMES.md`, `CLAUDE.md` | nur ATELIER-Dach |
| **`LADELISTE.md`** | Was muss dieser Chat oder Arbeiter für genau seine Aufgabe lesen? | oberster Navigator; enthält Pfade und Auswahl, aber keine kopierte Fachwahrheit | alle nachfolgenden Dokumente | nur ATELIER-Dach |
| **`AGENT.md`** | Welche Grenzen, Zuständigkeiten und direkten Kinder gelten in diesem Ordner? | verbindliche Arbeitsregel innerhalb ihres Ordners; kurz und hierarchiebezogen | übergeordnetes `AGENT.md`, `LADELISTE.md`, lokale SSOT/`SCOPE.md` | Dach sowie Hunderter, Zehner oder Einer, wenn dort eigene Grenzen gelten |
| **`README.md`** | Was ist dieser Ordner, wo beginnt man und wohin zeigen die wichtigsten Links? | Orientierung, keine neue Wahrheit | lokales `AGENT.md`, SSOT, `SPEC.md`, Code und Tests | auf Struktur- oder Blattebenen, wenn Orientierung nötig ist |
| **fachliche SSOT** | Was gilt für diese konkrete fachliche Frage aktuell? | genau ein Besitzer pro Frage; Änderungen nur bewusst mit Werner | Quellenregister, `DECISIONS.md`, `SPEC.md`, `LEARNINGS.md` | niedrigste Ebene, die den ganzen Geltungsbereich besitzt; meist Hunderter, Zehner oder Einer |
| **`DECISIONS.md`** | Was wurde von Werner entschieden, warum, für welchen Bereich und was wurde dadurch ersetzt? | Entscheidungsregister; alte Entscheidungen als ersetzt markieren statt heimlich löschen | SSOT, `SCOPE.md`, `LEARNINGS.md`, Git | am niedrigsten gemeinsamen Besitzer der Entscheidung; global nur bei globaler Wirkung |
| **`IDEAS.md`** | Welche Ideen existieren, sind aber noch kein aktiver Auftrag? | Parkplatz; nicht bindend, nicht automatisch Teil des Scopes | `DECISIONS.md`, `SCOPE.md`, `LEARNINGS.md` | Dach für bereichsübergreifende Ideen, sonst beim fachlichen Besitzer |
| **`SCOPE.md`** | Woran arbeiten wir jetzt bewusst, was gehört dazu und was ausdrücklich nicht? | zeitlich aktiver Grenzvertrag; verhindert Scope-Ausweitung | `DECISIONS.md`, SSOT, eine oder mehrere `SPEC.md`, `HANDOFF.md` | meist Hunderter, Zehner oder Einer; genau dort, wo der Arbeitszug beginnt |
| **`SPEC.md`** oder `spec_<name>.md` | Was muss ein konkretes Werkstück leisten und woran wird es akzeptiert? | ausführbarer Bau- und Akzeptanzvertrag; darf SSOT und Scope nicht überschreiben | SSOT, `SCOPE.md`, Quellen, `PROMPT_<id>.md`, Tests | meist Einer, Zehntel oder Blattordner |
| **`HERMES.md`** | Wie übersetzt Hermes gültige Wahrheit in Aufträge und wie prüft und integriert Hermes Ergebnisse? | Hermes-Adapter; Prozessregeln, keine eigene Fachwahrheit | `SOUL.md`, `AGENT.md`, `SCOPE.md`, `SPEC.md`, `PROMPT_<id>.md` | vorzugsweise einmal am ATELIER-Dach; lokal nur bei echter Sonderregel |
| **`CLAUDE.md`** | Wie soll Claude Code grundsätzlich in diesem Repository arbeiten? | Claude-Adapter; technische Grundgrenzen, keine zweite Architektur-SSOT | `SOUL.md`, `AGENT.md`, `PROMPT_<id>.md` | vorzugsweise einmal am ATELIER-Dach; konkrete Arbeit steht im Prompt |
| **`PROMPT_<id>.md`** | Was genau hat Hermes Claude für diese Ausführung beauftragt? | unveränderter Übergabebeleg mit Basis, Scope, Verboten und Tests; keine Ergebniswahrheit | `SPEC.md`, Git-Basis, `REPORT_<id>.md` | beim konkreten Werkstück, meist Einer, Zehntel oder Blattordner |
| **`REPORT_<id>.md`** | Was behauptet Claude geändert, getestet, nicht getan oder offengelassen zu haben? | Rückmeldung eines Arbeiters; bis zur unabhängigen Prüfung unbestätigt | passender Prompt, Diff, Tests, Hermes-Prüfung | direkt neben dem zugehörigen Prompt |
| **`LEARNINGS.md`** | Was wurde durch Fehler, Tests, CLO 3D, Nessel oder Arbeit beobachtet und gelernt? | Laborbuch; Beobachtung mit Beleg und Gültigkeitsgrad, keine automatische Entscheidung | Quellen/Artefakte, `DECISIONS.md`, SSOT, `SPEC.md` | beim niedrigsten fachlichen Besitzer; nur echte bereichsweite Erkenntnisse höher ziehen |
| **Quellen- oder Belegregister** | Worauf stützt sich eine Behauptung genau? | Provenienz: Buch, Seite, Bild, Transkription, Formel, Messung oder reales Ergebnis | SSOT, `SPEC.md`, `LEARNINGS.md`, Prüfprotokoll | beim Quellenbesitzer; Arbeitsdateien verlinken nur darauf |
| **`VERIFICATION.md`** oder datiertes Prüfprotokoll | Was wurde auf welchem Git-Stand tatsächlich geprüft und mit welchem Ergebnis? | zeitgebundener Nachweis; nennt Commit/Working-Tree-Basis und Prüfgrenze | Tests, Prompt/Report, Git, CLO 3D, Nessel | nur für bedeutende Integrations- oder Realprüfungen, nahe beim Werkstück |
| **`HANDOFF.md`** | Wo stehen wir jetzt, was ist blockiert und was ist der nächste kleinste Schritt? | kurze Brücke in die nächste Session; verweist auf Wahrheit, kopiert sie nicht | `LADELISTE.md`, aktiver `SCOPE.md`, aktive `SPEC.md`, Git | zunächst genau einmal am Dach oder in `600_prozess`; lokale Handoffs erst bei echtem Bedarf |

### Was nicht in jede Ebene kopiert wird

Nicht jeder Ordner braucht `SOUL.md`, `HERMES.md`, `CLAUDE.md`, `DECISIONS.md`, `IDEAS.md`, `SCOPE.md`, `SPEC.md`, `LEARNINGS.md` und `HANDOFF.md`.

Ein normaler Blattordner kann vollständig sein mit:

```text
README.md
<funktion>.py
<test_funktion>.py
```

Weitere Markdown-Dateien kommen nur hinzu, wenn ihre eigene Frage dort wirklich beantwortet werden muss.

---

## 5. Arbeitsfluss und Korrelation der Dateien

```text
Werner im aktuellen Chat
    │
    ├── neue, noch nicht aktive Idee ──────────────> IDEAS.md
    │
    └── bewusste Entscheidung ─────────────────────> DECISIONS.md
                                                        │
                                                        v
SOUL.md ── schützt die Zusammenarbeit          fachliche SSOT
                                                        │
                                                        v
                                                   SCOPE.md
                                                        │
                                                        v
                                                     SPEC.md
                                                        │
                                                        v
                                               PROMPT_<id>.md
                                                        │
                                                        v
                                                   Claude Code
                                                        │
                                                        v
                                               REPORT_<id>.md
                                                        │
                                                        v
                                     Hermes: Diff + Tests + Regeln prüfen
                                                        │
                              ┌─────────────────────────┴──────────────────────┐
                              v                                                v
                    technisch bestätigt                         fachlich/real noch offen
                              │                                                │
                              v                                                v
                         CLO 3D / Nessel ───────────────> LEARNINGS.md
                              │                                                │
                              └──────── Werner entscheidet Änderung ──────────┘
                                                        │
                                                        v
                                              `#` für Git-Commit
                                                        │
                                                        v
                                                 Git-Checkpoint
                                                        │
                                                        v
                                                   HANDOFF.md
```

### Git als Nachweisschicht

Git ist keine fachliche Entscheidungsinstanz. Git beantwortet andere Fragen:

| Git-Teil | Frage |
|---|---|
| Working Tree | Woran wird gerade gearbeitet und was ist noch Kandidat? |
| Diff | Was wurde gegenüber dem letzten Stand genau verändert? |
| Commit | Welcher technische Zustand wurde bewusst festgehalten? |
| Branch | Welche Entwicklungsrichtung ist getrennt aktiv? |
| Historie | Wie und wann entstand ein früherer Zustand? |
| Tag, nur bei echtem Bedarf | Welcher feste Stand gehört zu einem bestimmten CLO- oder Nessel-Versuch? |

---

## 6. Ladeliste statt Alleslesen

Die vorgeschlagene `C:\ATELIER\LADELISTE.md` ist sinnvoll, wenn sie ein **selektiver Wegweiser** bleibt. Sie darf keine zweite Sammlung aller Regeln werden.

### Minimaler Start einer neuen Hermes-Session

1. aktuellen Auftrag von Werner lesen;
2. `C:\ATELIER\AGENT.md` lesen;
3. `SOUL.md` und `LADELISTE.md` lesen;
4. in der Ladeliste genau einen aktiven Hunderter/Zehner/Einer auswählen;
5. entlang dieses Pfades nur die zuständigen lokalen `AGENT.md` lesen;
6. aktiven `SCOPE.md`, die zuständige SSOT und die konkrete `SPEC.md` lesen;
7. `HANDOFF.md` und live Git-Stand prüfen;
8. weitere Quellen oder `LEARNINGS.md` nur laden, wenn die konkrete Aufgabe sie benötigt.

### Für Claude Code

Claude erhält nicht das gesamte Repository als gedanklichen Auftrag, sondern:

1. die nötigen globalen Grenzen aus `CLAUDE.md`;
2. die lokale `AGENT.md`-Kette des Arbeitsortes;
3. den einen `PROMPT_<id>.md`;
4. die darin direkt verlinkte `SPEC.md`, SSOT und nötigen Quellen;
5. den erlaubten Datei-Scope und die verlangten Tests.

### Beispiel einer schlanken Ladeliste

```markdown
# Ladeliste

## Immer
- [ ] `AGENT.md`
- [ ] `SOUL.md`
- [ ] `HANDOFF.md`

## Aktiver Arbeitsweg
- [ ] `200_funktionen/AGENT.md`
- [ ] `<aktiver_zehner>/AGENT.md`
- [ ] `<aktiver_einer>/AGENT.md`
- [ ] `<aktiver_scope>/SCOPE.md`
- [ ] `<aktives_werkstueck>/spec_<name>.md`

## Nur wenn der Auftrag es braucht
- [ ] Quellenregister
- [ ] `LEARNINGS.md`
- [ ] früherer Prompt und Report
- [ ] Prüfprotokoll
```

Die Liste muss Pfade aus dem **aktuellen Dateisystem** enthalten. Veraltete Pfade werden korrigiert; Inhalte werden nicht in die Ladeliste kopiert.

---

## 7. Regeln gegen Überorganisation

Das Modell ist hilfreich, solange folgende Grenzen gelten:

1. **Eine Datei besitzt genau eine Hauptfrage.**
2. **Eine fachliche Frage besitzt genau eine SSOT.**
3. **Andere Dateien verlinken, statt Wahrheit zu duplizieren.**
4. **Keine leere Pflichtdatei nur wegen eines Schemas.**
5. **Keine neue Ordnerebene ohne echte Grenze.**
6. **Ein Prompt-/Report-Paar nur für einen echten Claude-Arbeitsauftrag, nicht für jedes Gespräch.**
7. **Ein Learning braucht eine konkrete Beobachtung und einen Beleg.**
8. **Eine Idee bleibt geparkt, bis Werner sie aktiviert.**
9. **Ein Handoff bleibt kurz und nennt nur Stand, Grenzen und nächsten Schritt.**
10. **Die Ladeliste steuert Lesekosten; sie wird nicht selbst zur zweiten SSOT.**
11. **Umstrukturierung und Umbenennung erfolgen später als eigener, geprüfter Schritt und benötigen bei Verschiebungen Werners `#`.**

### Stop-Signal

Überorganisation beginnt, wenn mehr Zeit in das Pflegen der Dokumentstruktur als in einen belegbaren Weg

```text
Quelle → fachliche Klärung → SPEC → Code → Test → CLO 3D → Nessel
```

fließt.

---

## 8. Bewertung des Modells

### Hilfreich

- Die Hunderter-, Zehner-, Einer-, Zehntel- und Hundertstel-Sprache gibt Werner eine visuelle Adresse für jeden Arbeitsort.
- Die Rollen Werner → Hermes → Claude Code sind eindeutig.
- Scope, Spec, Prompt und Report machen jeden Auftrag vorwärts und rückwärts lesbar.
- Ideas und Learnings schützen vor Verlust, ohne automatisch neue Wahrheit zu erzeugen.
- Die Ladeliste verhindert, dass jeder Chat und jeder Arbeiter alle Markdown-Dateien lesen muss.
- Git und reale Prüfungen machen aus bloßen Behauptungen überprüfbare Zustände.

### Gefahr

- Zu viele lokale Kopien derselben Regeln erzeugen mehr Drift statt weniger.
- Starre Nummernstufen können fachlich sinnlose Zwischenordner erzwingen.
- Handoff, Scope, Spec und Entscheidungen können sich widersprechen, wenn ihre Zuständigkeiten nicht sauber bleiben.
- Prompt- und Reportarchive können das Repo aufblasen, wenn jede Kleinigkeit dauerhaft aufgehoben wird.

### Entscheidungsvorschlag

Das Denkmodell ist **nicht grundsätzlich überorganisiert**. Für dieses große, quellenreiche Schnittmusterprojekt ist es hilfreich, wenn wir es **bedarfsgesteuert** einführen:

1. zuerst oberste Rollen, Fragen und Ladeliste festlegen;
2. dann nur an einem realen Arbeitsweg erproben;
3. keine flächige Umstrukturierung des gesamten Repositorys vor dem Pilot;
4. nach dem ersten Weg `Quelle → Rock → Code → Test → CLO 3D → Nessel` prüfen, welche Dateien tatsächlich geholfen haben;
5. erst danach das Modell auf weitere Hunderter und Zehner ausweiten.

So bleibt die Dokumentation ein Steuerungswerkzeug für das Schnittmusterprogramm und wird nicht selbst zum Hauptprodukt.
