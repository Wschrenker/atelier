# jijge_bridal_engine_v2
Arbeitsordner: C:\ATELIER

## Status (2026-08-17)

Repo steht, Fundament noch leer.

## Ziel
Schnittmusterprogramm aus Formeln. Ausgabe: DXF, SVG, PDF, JSON.
Gleichrangiges zweites Ziel: Werner und Munkhuu verstehen jede Konstruktion,
die der Code ausführt.

## Versionen
- **Engine:** eine Ziffer — `v1`, `v2`, `v3`. Aktuell **v2**.
- **Kleider:** drei Ziffern — `v001`, `v002`, `v003`.
- **Module:** noch offen, evtl. `v01`. Nicht dringend.

## Die Ordnung: die Nummer sagt die Art, der Name sagt die Sache

### Ordner — sie folgen der Arbeitsrichtung

| Ordner | Inhalt |
|---|---|
| `100_quellen` | Bücher. Unveränderlich, wird nur gelesen. |
| `200_grundlagen` | Was wir aus den Quellen ziehen: Sprache, Zeichen, Maße. |
| `300_module` | Konstruktionen. Wiederverwendbar und **kleidblind**. |
| `400_pattern` | Die Kleider. Sie **benutzen** Module, sie besitzen keine. |

Die Reihenfolge ist der Fluss der Arbeit:
**Quelle → Grundlage → Modul → Kleid.**
Hunderterschritte lassen Platz für Ebenen dazwischen.

### Dateien — in jedem Ordner nach demselben Schlüssel

| Nummer | Art |
|---|---|
| `1` | Agentenanweisung — was gilt hier drin |
| `10er` | Zeichen und Sprache |
| `20er` | Maße |
| `30er` | Formeln und Konstruktion |
| `888` | zu bearbeiten, offen, Test |
| `999` | Glossar und Ablage |

**Lücken sind Absicht.** Zwischen zwei Arten bleibt Platz; innerhalb einer Art
darf dicht nummeriert werden (10, 11, 12, 13).

### Die Kontenplan-Regel

Die Ordnung ist wie ein Kontenplan gebaut und wird auch so behandelt:

| Regel | Bedeutung |
|---|---|
| Die Nummer trägt die Bedeutung | man findet, ohne zu lesen |
| **Eine Nummer wird nie umgewidmet** | wenn `20` einmal „Maße" heißt, heißt sie das für immer |
| **Es wird nie umnummeriert** | Neues bekommt eine freie Nummer — deshalb die Lücken |
| Derselbe Schlüssel überall | jeder Ordner liest sich gleich |

Falsch einsortiert wird durch eine **neue Nummer** geheilt, nicht durch
Verschieben und Umnummerieren. Eine Ordnung, in der Nummern wandern, versteht
nach einem Jahr niemand mehr.

### Die eine Ausnahme: `1000_übergabe`

Der Dateischlüssel oben gilt in den **Arbeitsordnern 100–400**.

`1000_übergabe` ist kein Arbeitsordner, sondern eine **Zeitachse**, und hat
deshalb einen eigenen Schlüssel:

| Nummer | Arbeitsordner 100–400 | `1000_übergabe` |
|---|---|---|
| `777` | — | Vergangenheit — **warum** wir etwas entschieden haben |
| `888` | zu bearbeiten, offen, Test | Gegenwart — woran wir **jetzt** arbeiten |
| `999` | Glossar und Ablage | Zukunft — was im Raum steht, **nicht entschieden** |

Diese Ausnahme steht hier und nur hier — direkt neben der Regel, die sie
bricht. **Ungeschriebene Ausnahmen sind die, die Ordnungen kaputtmachen.**

### Jeder Ordner trägt seine eigene `1_…AGENT.md`
Sie sagt, **was hier drin gilt** — nicht, was im ganzen Projekt gilt.
Wer in einem Ordner arbeitet, liest dessen Agentendatei, nicht das ganze Repo.
Was oben steht, wird unten **nicht wiederholt**.

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

## Nicht vorsorglich verallgemeinern
Erst das zweite Kleid zeigt, was wirklich ein Parameter sein muss.

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

## Zwei Dokumentationsebenen
- **Modul-Doku** — was rechnet dieses Modul, welche Seite, welche Prüfwerte.
  Entsteht beim Bauen von selbst.
- **Kleid-Anleitung** — wie entsteht dieses Kleid, Schritt für Schritt bis zur
  Naht. Eigenes Dokument, wird **parallel zum Bauen** geschrieben.
  Echtes Atelier-Werkzeug, auch für Munkhuu.

## Arbeitsteilung mit der KI
- **Skill = Arbeitsweise. Datei = Können.** Was die KI baut, landet als Datei
  im Repo, mit Test, committet — nicht nur im Skill-Speicher.

### Rollen
Die Rollen wechseln, die Konstellation bleibt.
- **Leader** — führt, entscheidet Reihenfolge, committet.
- **Coder** — baut Module und Tests, entscheidet keinen Scope, meldet nach oben.

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

---
Aktiv steuert: Wschrenker + Munkhuu
KI-Partner: Hermes, Claude, Codex — weitere situativ
