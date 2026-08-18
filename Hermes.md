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

## Arbeitsteilung mit der KI
- **Mathe vorcoden: ja.** Kurve durch Punkte, Spiegeln, Zirkelschlag, Drehen,
  Schnittpunkte, Lot, Parallelversatz. Modeblind, ungefährlich.
- **Konstruktionen vorcoden: nein.** Sonst steht der Code vor dem Prüfwert,
  und das Buch wird gegen den Code geprüft statt umgekehrt.
- Beim Transkribieren erzeugt die KI **strukturierte Formeln, keinen Code**:
  Eingangsmaße, Ergebnis, Seitenzahl, Beispielzahl.
- **Skill = Arbeitsweise. Datei = Können.** Was die KI baut, landet als Datei
  im Repo, mit Test, committet — nicht nur im Skill-Speicher.

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
1. **Kleid v001** definieren
2. Roadmap ableiten: Modulliste, Reihenfolge, Quellseiten, Prüfwerte
3. Transkripte in Git sichern (Fotos bleiben draußen)
4. Mathe-Primitive nach Bedarf aus Schritt 3.5
5. Modul 1 durchziehen: gerader Rock S. 32–36 — einziger freigegebener Fels

## Nächster Schritt
Kleid **v001** festzurren.

---
Aktiv steuert: Wschrenker + Munkhuu
KI-Partner: Hermes, Claude, Codex — weitere situativ