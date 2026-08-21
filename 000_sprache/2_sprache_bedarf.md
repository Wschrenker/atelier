# Sprache — Bedarfswissen

Diese Datei wird nur gelesen, wenn die Einzelregeln von `000_sprache` für die
konkrete Arbeit benötigt werden. Der Pflichtkern steht in
`AGENT.md`.

## Aufgabe der Ebene

`000_sprache` hält die gemeinsame Sprache für das gesamte Atelier:

- Abkürzungen und Operanden
- Schnittmuster-Symbole
- belegte Modebegriffe

Hier steht, **was ein Wort oder Zeichen bedeutet** — nicht, wie daraus
berechnet oder programmiert wird.

## Arbeitskadenz

1. Begriff oder Zeichen im Buch finden.
2. Buch und Seitenzahl festhalten.
3. Die Bedeutung in der passenden Datei von `000_sprache` eintragen.
4. Rechenweg und Maßberechnung nach `300_formeln` verweisen.
5. Erst nach fachlicher Prüfung darf eine andere Ebene den Eintrag zitieren.

Nicht aus Allgemeinwissen ergänzen. Unbelegtes bleibt offen, bis die
Buchstelle geprüft ist.

## Dokumentarten

| Bereich | Pflichtdokument | Zusatz / Beleg |
|---|---|---|
| `10_gosslar/` | `1_gosslar.md` | Glossar-Eintrag mit Quelle und Seite |
| `20_schnittmuster/` | `.md`-Tabelle | zugehöriges `.html` zeigt das Originalzeichen |
| `30_lexikon/` | `10_abkuerzungen_systematik_eigenschaften_betraege_werte_operanden_aktionen.md` | Systematik für Kurzzeichen und Operanden |

Bei Schnittmuster-Symbolen gilt: Die `.md` ist die lesbare Abschrift, das
`.html` ist der Bildbeleg. Bei Widerspruch gilt der Bildbeleg.

## Was nicht hierher gehört

| Frage | Zuständig |
|---|---|
| Maßname mit Rechenweg oder Maßtabelle | `300_formeln/10_masse/` |
| Buchseite oder vollständige Abschrift | `100_quellen/` |
| Primitive und Geometrie | `400_mathematik/` |
| Python, Tests und Ausführung | `500_python/` |
| kleidspezifische Entscheidung | `700_schnitte/` |
| offene Arbeitsfrage | `600_prozess/` |

## Fertig-Regel

Ein Spracheintrag ist erst fertig, wenn:

- die Bedeutung eindeutig beschrieben ist,
- Buch und Seitenzahl feststehen,
- keine Rechnung als Definition getarnt ist,
- bei einem Symbol die erforderliche `.md`-Abschrift und der `.html`-Beleg
  vorhanden sind.

Nur fertige `.md`-Einträge dürfen von anderen Ebenen zitiert werden.
