# jijge_bridal_engine_v2
Arbeitsordner: C:\ATELIER

## Status (2026-08-17)

Repo steht, Fundament noch leer.

## Ziel
Schnittmusterprogramm aus Formeln. Ausgabe: DXF, SVG, PDF, JSON.
Gleichrangiges zweites Ziel: Werner und Munkhuu verstehen jede Konstruktion,
die der Code ausführt.

## Quelle
**Guido Hofenbitzer — Grundschnitte und Modellentwicklungen.
Schnittkonstruktion für Damenmode.** Europa-Lehrmittel.
Band 1 (3. Auflage 2024) und Band 2 (Noch nicht transskripiert und im desktop).

Das Buch ist die einzige fachliche Quelle der Engine. Jede Konstruktion,
jede Formel und jeder Prüfwert stammt daraus und trägt eine Seitenzahl.
Transkripte und Fotos liegen unter `hofenbitzer/`.

## Versionen
- **Engine:** eine Ziffer — `v1`, `v2`, `v3`. Aktuell **v2**.
- **Kleider:** drei Ziffern — `v001`, `v002`, `v003`.
- **Module:** noch offen, evtl. `v01`. Nicht dringend.

## Weg
Nicht das ganze Buch bauen. **Ein Kleid definieren** → daraus folgt die Roadmap
→ daraus folgt, welche Buchseiten Quelle sind.

Pro Baustein: **Transkript → Mathe → Python → Modul**
Dann: Kleid coden → CLO 3D ansehen → drucken → nähen.

## Grundlagen zuerst
Bedarfsgetrieben heißt: keine **Modelle** auf Vorrat bauen.
Es heißt **nicht**, die Grundlagen zu überspringen.

Vor der ersten Konstruktion werden eingepflegt:
1. **Abkürzungen und Maße** (S. 9, 11–15) — das Vokabular für alles Weitere
2. **Standards und Zeichen** (S. 21–31) — Linienarten, Nahtzugaben, Knipse,
   Bohrlöcher, Beschriftung
3. **Größentabelle** (S. 20) — liefert die Zahlen für jeden Test

Grund: die Begriffe müssen verstanden sein, die Konstruktion baut darauf auf,
und die Formeln sollen von Anfang an nachvollziehbar sein.

**Die Schnittzeichen sind kein Lernmaterial, sondern eine Ausgabe-Anforderung.**
Knips, Bohrloch, Fadenlauf, Stoffbruch und Beschriftung müssen am Ende im DXF
und im PDF stehen, sonst ist der Schnitt nicht produktionsfähig.

## Bauen von unten, auswählen von oben
Die Baureihenfolge bleibt down-to-up: Geometrie trägt Konstruktion,
Konstruktion trägt Kleid.
Was gebaut wird, entscheidet aber das Kleid — nicht das Inhaltsverzeichnis.
Nichts entsteht auf Vorrat. Wenn das Kleid steht, ist der Scope zu.

**Das Repo wächst organisch.** Ordner entstehen, wenn das erste Stück Inhalt
sie braucht — nicht vorher. Leere Ordner sind bewusst gelöscht worden.

## Die eiserne Regel
**Ein Modul darf nie wissen, welches Kleid gerade gebaut wird.**
„Abnäher schließen" kennt Geometrie und sonst nichts.
Universalität entsteht nicht dadurch, dass man groß baut, sondern dadurch,
was ein Modul nicht wissen darf.

Daraus folgt die Schichtung:
- **Geometrie** und **Ausgabe** wissen nichts von Mode.
- **Konstruktion** weiß nichts von DXF.
- **Kleid** kennt Module — aber kein Modul kennt das Kleid.

Nicht vorsorglich verallgemeinern. Erst das zweite Kleid zeigt, was wirklich
ein Parameter sein muss.

## Arbeitsweise pro Buchseite
1. Seite lesen → neue Begriffe nach **Gosslar**
2. Formeln wörtlich ablegen, **mit Seitenzahl**
3. Beispielzahlen des Buchs notieren → **Prüfwerte**
3.5 **Mathematik eruieren** — welche Primitive braucht diese Formel?
   Fehlende bauen (modeblind: Kurve, Spiegeln, Zirkelschlag, Drehen,
   Schnittpunkt, Lot, Parallelversatz)
4. **Python-Code generieren** aus Formel + Mathematik.
   Eine Funktion pro Konstruktionsschritt, Seitenzahl im Kommentar.
   **Modular abspeichern.**
5. **Test definieren und umsetzen** — rechnet die Buchzahlen nach.
   **Tests abspeichern.** Grün = Seite ist drin.

Schritt 1–3 macht der Mensch. **Code kommt nie vor den Prüfwerten.**

## Sprache
Jeder Fachbegriff, den eine KI verwendet und der nicht in **Gosslar** steht,
ist ein fehlender Glossareintrag — kein Wissensdefizit des Menschen.
Solche Begriffe wandern nach `gosslar_kontext/BEGRIFFE_OFFEN.md`.
Begriffe werden beim ersten Gebrauch in einem Halbsatz miterklärt.

## Zwei Dokumentationsebenen
- **Modul-Doku** — was rechnet dieses Modul, welche Seite, welche Prüfwerte.
  Entsteht beim Bauen von selbst.
- **Kleid-Anleitung** — wie entsteht dieses Kleid, Schritt für Schritt bis zur
  Naht. Eigenes Dokument, wird **parallel zum Bauen** geschrieben.
  Echtes Atelier-Werkzeug, auch für Munkhuu.

## Arbeitsteilung mit der KI
- **Mathe vorcoden: ja.** Kurve durch Punkte, Spiegeln, Zirkelschlag, Drehen,
  Schnittpunkte, Lot, Parallelversatz. Modeblind, ungefährlich.
- **Konstruktionen vorcoden: nein.** Sonst steht der Code vor dem Prüfwert,
  und das Buch wird gegen den Code geprüft statt umgekehrt.
- Beim Transkribieren erzeugt die KI **strukturierte Formeln, keinen Code**:
  Eingangsmaße, Ergebnis, Seitenzahl, Beispielzahl.
- **Skill = Arbeitsweise. Datei = Können.** Was die KI baut, landet als Datei
  im Repo, mit Test, committet — nicht nur im Skill-Speicher.

### Rollen
Die Rollen wechseln, die Konstellation bleibt.
- **Leader** — führt, entscheidet Reihenfolge, committet.
- **Coder** — baut Module und Tests, entscheidet keinen Scope, meldet nach oben.

Der gemeinsame Stand liegt **im Repo, nicht im Chat**: Kleid-Definition,
Roadmap und Modulstatus sind Dateien. Nur so kann jede KI kalt einsteigen.

### Eigene Agenten
Ein Agent (Ordner + `.md`) wird erst gebaut, **nachdem die Sache zweimal von
Hand gemacht wurde.** Vorher kodiert man eine Vermutung statt eines Könnens —
derselbe Fehler wie ein Modul, das zu viel weiß.

Kandidaten, weil sie sich oft wiederholen werden:
- „Buchseite einpflegen" (der Fünfschritt oben)
- „Modul anlegen"
- „Prüfwerte aus einer Seite ziehen"

## Drei Prüftore
1. **Buchzahlen** — beweisen, dass richtig gerechnet wird.
2. **CLO 3D** — zeigt, ob es plausibel aussieht. Beweist nichts:
   ein in sich stimmiger, aber falscher Abnäher simuliert sauber.
3. **Genäht** — beweist die Wahrheit.

Keines ersetzt das andere.

## Quellen-Disziplin
Jedes aus einem Transkript übernommene Stück nimmt **seine Seitenzahl mit**.
Grund: die Transkripte haben offene Stellen — vermutete Buchfehler, unlesbare
Passagen, Doppel-Transkription S. 438/439.
Korrekturen müssen später alle Kopien finden.
Ein Baustein gilt erst dann als belegt, wenn die Seite von Werner/Munkhuu
am Buch freigegeben ist.

## Phase jetzt
1. ✅ **Kleid v001** definiert → `kleid_v001/DEFINITION.md`
2. ✅ Roadmap abgeleitet → `kleid_v001/ROADMAP.md`
3. ✅ Transkripte in Git gesichert (Fotos bleiben draußen)
4. 🔄 Grundlagen Block 1: Abkürzungen und Maße (S. 9, 11–15)
5. ⬜ Grundlagen Block 2: Standards und Zeichen (S. 21–31)
6. ⬜ Grundlagen Block 3: Größentabelle (S. 20)
7. ⬜ Erstes Modul: Tellerrock S. 44

## Nächster Schritt
Werner prüft Block 1 — besonders die offenen Punkte in
`gosslar_kontext/MASSREGISTER.md`.

---
Aktiv steuert: Wschrenker + Munkhuu
KI-Partner: Hermes, Claude, Codex — weitere situativ
