# Prozess — was hier drin gilt

## Zweck

Buchhaltung. **Kein Wissen.**

Hier steht, was offen ist und wer dran ist. Diese Ebene liefert nichts zu — sie
steht **neben** dem Fluss, nicht darin.

Probe: Löscht man diesen Ordner, wird keine Formel falsch und kein Modul kaputt.
Man weiß nur nicht mehr, was noch fehlt. Alles, was diese Probe nicht besteht,
gehört woanders hin.

## Grenze

| Nicht hier | Sondern |
|---|---|
| Der fertige Begriff mit Definition und Seite | `000_sprache/30_gosslar_test.md` |
| Die fertige Formel | `300_formeln/` |
| Fachfrage **zu einer bestimmten Formel** | bleibt als ⚠️ **bei der Formel** |
| Modulstatus eines Kleides | `700_schnitte/<kleid>/ROADMAP.md` |
| Prüfstand der Transkripte (A/B/C/D) | `100_quellen/…/band_1/README.md` |

Die härteste Regel dieser Ebene: **keine doppelte Buchführung.**

Hier steht nur, was **noch nirgends** hingehört. Sobald ein Eintrag seinen
richtigen Ort hat, wird er dort geführt — nicht zusätzlich hier. Zwei Listen
über dieselbe Sache laufen immer auseinander, und dann glaubt man der falschen.

## Nummernschlüssel

Eine Liste pro Datei, in Zehnern:

| Nummer | Liste |
|---|---|
| `10_` | Begriffe offen — Kandidaten für Gosslar |

Neue Art von Offenheit → nächster freier Zehner (`20_`, `30_`).
**Eine vergebene Nummer wird nie neu belegt.**

## Form eines Eintrags

Jede Liste führt zwei Tabellen — getrennt danach, **was fehlt**:

**1. Bereit** — hat Definition und Seitenzahl, kann sofort umziehen:

`| Begriff | Kurzdefinition | Quelle | Status |`

**2. Braucht noch eine Buchseite** — wird gebraucht, ist aber unbelegt:

`| Begriff | wo ich ihn benutzt habe | fehlt |`

Regeln für beide:

- Neue Kandidaten kommen **unten** dazu, **mit Datum**
- Ein `?` in der Spalte *fehlt* ist ein gültiger Eintrag
- **Nicht raten, nicht aus Allgemeinwissen füllen** — sonst steht
  Nicht-Hofenbitzer im Glossar der Hofenbitzer-Engine

## Fertig-Regel

Ein Eintrag ist hier fertig, wenn er **verschwindet**.

Erledigt heißt nicht abgehakt, sondern **umgezogen**: die Zeile wird gelöscht,
sobald der Eintrag an seinem richtigen Ort steht — mit Definition und
Seitenzahl. Wer die Zeile löscht, prüft vorher das Ziel.

Deshalb wächst eine Liste hier nicht mit Häkchen voll. Sie wird kürzer, wenn
gearbeitet wird.

**Ausnahme:** eine gelöste Blockade in einer Roadmap wird durchgestrichen, nicht
gelöscht — dort ist die Entscheidung selbst die Information. Hier nicht.

## Was hierher gehört

- Begriffe, die eine KI benutzt hat und die in Gosslar fehlen
- Fragen an Werner und Munkhuu, die zu keiner einzelnen Datei gehören
- Entscheidungen, die anstehen und mehrere Ordner betreffen
- Arbeitsstände, die über Ordnergrenzen laufen (die Grundlagen-Blöcke)

## Offene Stellen

- `10_BEGRIFFE_OFFEN.md` steht in Versalien — gegen die Namensregel der Wurzel
- Die Liste verweist auf `1_Hermes_AtelierAGENT.md`, Abschnitt „Sprache" —
  diesen Abschnitt gibt es dort nicht mehr, er stand zuletzt in
  `300_formeln`. Verweis nachziehen.
- 11 Begriffe stehen auf **bereit** und könnten sofort nach Gosslar umziehen —
  sie tun es nur nicht.
- Die Grundlagen-Blöcke (S. 9/11–15, S. 21–31, S. 20) und der Projektstand
  „Phase jetzt" haben hier ihren Ort, liegen aber noch außerhalb des Repos im
  Scratchpad.
