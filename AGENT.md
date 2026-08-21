# Atelier — oberste Ebene

Projekt: `jijge_bridal_engine_v2`
Arbeitsordner: `C:\ATELIER`
Stand: 2026-08-20

Bedarfswissen — nur bei Bedarf lesen: `2_atelier_bedarf.md`

## Regel dieser Datei

Was **mehrere Ordner** betrifft, steht hier.
Was **einen Ordner** betrifft, steht in dessen `AGENT.md`.

Zuerst wird diese `AGENT.md` gelesen. Danach werden nur die in der Ladeliste
angekreuzten Agentendateien gelesen. Nicht angekreuzte Dateien werden nicht
automatisch geladen.

## Ziel

Schnittmusterprogramm aus Formeln. Ausgabe: DXF, SVG, PDF, JSON.

Gleichrangiges zweites Ziel: Werner und Munkhuu verstehen jede Konstruktion,
die der Code ausführt. Fachbegriffe aus der Software-welt kursiv, Fachbegriffe und Gosslarbegriffe aus der Modewelt ist fett zu schreiben.

## Karte der Ebenen

Die Nummern folgen der Arbeitsrichtung. Die dritte Spalte ist bindend.

| Ordner | Zuständig für | Darf benutzen |
|---|---|---|
| `000_sprache` | Abkürzungen, Zeichen, Begriffe. Liegt unter allem — auch die Quelle wird damit gelesen. | — |
| `100_quellen` | Die Bücher. Unveränderlich, wird nur gelesen. | `000` |
| `300_formeln` | Was wir aus den Quellen ziehen: Maßregister und Konstruktionsformeln. | `000` `100` |
| `400_mathematik` | Primitive: Kurve, Lot, Spiegeln, Versatz, Drehung. **Modeblind** und deshalb ohne jede Abhängigkeit. | — |
| `500_python` | Konstruktionen als Code. Wiederverwendbar und **kleidblind**. | `300` `400` |
| `600_prozess` | Arbeitslisten und Offenes. Kein Inhalt, nur Buchhaltung. | — |
| `700_schnitte` | Die Kleider. Sie **benutzen** Module, sie besitzen keine. | `300` `400` `500` |
| `800_couture` | Die Aufträge. Ein Kleid mit den Maßen einer Braut, dazu die Ausgabe — PDF, DXF, SVG. | `700` und alles darunter |

`200` ist frei. Die Maßtabellen liegen in `300_formeln/10_masse/`.
`600_prozess` steht **neben** dem Fluss, nicht darin: es führt Buch, es liefert
nichts zu.

## Flussregel

**Sprache → Quelle → Formel → Mathematik → Python → Kleid.**

## Pflichtgrenzen

- Echte Kundenmaße bleiben lokal und werden nicht ins Repo übernommen.
- `#` ist die einmalige Freigabe für Commit und Push, Löschen und Verschieben,
  Downloads, destruktive Git-Aktionen sowie Veröffentlichung und Remote-Aktionen.
- Ohne `#` sind lokales Lesen und Schreiben sowie betroffene Tests erlaubt.
- Die Freigabe gilt nur für den unmittelbar besprochenen Arbeitsschritt.


## Ladeliste — Anweisung

Nur die **angekreuzten Agentendateien** automatisch laden. Nicht angekreuzt heißt: nicht laden.

## Ladeliste

- [x] `AGENT.md`
- [x] `000_sprache/AGENT.md`
- [x] `100_quellen/AGENT.md`
- [] `300_formeln/AGENT.md`
- [] `400_mathematik/AGENT.md`
- [] `500_python/AGENT.md`
- [] `600_prozess/AGENT.md`
- [] `700_schnitte/AGENT.md`
- [] `800_couture/AGENT.md`

---
Aktiv steuert: Wschrenker + Munkhuu
KI-Partner: Hermes, Claude, Codex — weitere situativ
