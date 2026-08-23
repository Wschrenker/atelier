# Kleid v001 — Roadmap

Stand: 2026-08-23 · nach sauberem Neustart aus `DEFINITION.md`

Diese Datei ist der **Modulstatus**. Sie ist der Punkt, an dem eine KI kalt
einsteigen kann — Leader wie Coder.

Legende: ✅ fertig · 🔄 läuft · ⬜ offen · 🔒 blockiert

---

## Teil A — Grundlagen (vor jeder Konstruktion)

| # | Modul | Quelle | Status | Freigabe Buch |
|---:|---|---|:--:|---|
| A1 | Abkürzungen und Maße | S. 9, 11–15 | 🔒 | ⬜ am Buch prüfen |
| A2 | Standards und Schnittzeichen | S. 21–31 | 🔒 | ⬜ am Buch prüfen |
| A3 | Größentabelle | S. 20 | 🔒 | ⬜ am Buch prüfen |

Für A1–A3 gibt es noch keine Formeldateien. Zuerst werden die genannten Seiten,
Abkürzungen und Werte am Buch verifiziert. Auch `HaU`/`HdU` gilt wieder als
offen, bis der Buchbeleg eindeutig ist.

**A3** liefert die Zahlen für jeden Test. Ohne A3 gibt es keine Prüfwerte
außer den wenigen, die in den Konstruktionsseiten selbst stehen.

---

## Teil B — Mathematik (modeblind, darf vorgecodet werden)

| # | Primitive | gebraucht von | Status |
|---:|---|---|:--:|
| B1 | Kreis um Mittelpunkt mit Radius | C1 | ⬜ |
| B2 | Lot / rechter Winkel durch Punkt | C1 | ⬜ |
| B3 | Kreisbogen-Segment | C1 | ⬜ |
| B4 | Drehen um Punkt | C4 (Abnäherverlegung) | ⬜ |
| B5 | Spiegeln an Achse | C3 (gespiegelter GS) | ⬜ |
| B6 | Kurve durch gegebene Punkte | C3 | ⬜ |
| B7 | Parallelversatz | C7 (Nahtzugaben) | ⬜ |
| B8 | Schnittpunkt Linie/Kreis, Kreis/Kreis | C3 | ⬜ |
| B9 | Länge entlang Kurve | C5 (Nahtlängen abgleichen) | ⬜ |

Welche Primitive ein Modul benötigt, wird erst aus seiner freigegebenen Formel
abgeleitet. Es gibt derzeit keine aktive Modulauswahl.

---

## Teil C — Konstruktion

| # | Modul | Quelle | hängt an | Status | Quellenlage |
|---:|---|---|---|:--:|---|
| C1 | **Tellerrock** | S. 44 | A1, A3, B1–B3 | 🔒 | Transkript vorhanden; Seite und Formel nicht freigegeben |
| C2 | Ausgabe SVG (Sichtprüfung) | — | C1 | 🔒 | kein Modul vorhanden |
| C3 | Oberteil-Grundgerüst | S. 172–183 | A1, A3, B5–B8 | 🔒 | Quellenprüfung offen |
| C4 | Oberteil-Abnäher | S. 184–187 | C3, B4 | 🔒 | Quellenprüfung offen |
| C5 | Abnäherverlegung in Falten | S. 423 ❑7, ❑8a | C4, B4, B9 | 🔒 | Quellenprüfung offen |
| C6 | **Asymmetrisches Wickeloberteil** | S. 423 ❑8, ❑8b | C5 | 🔒 | roh |
| C7 | Taillennaht Rock an Oberteil | S. 406–407, 438–439 | C1, C6 | 🔒 | roh, **Konflikt C1 offen** |
| C8 | Ausschnitt + Beleg | ? | C6 | 🔒 | Seite unbekannt |
| C9 | Armloch fertigstellen | ? | C6 | 🔒 | Seite unbekannt |
| C10 | Rückennaht + Reißverschluss | S. 44 + ? | C7 | 🔒 | teilweise |
| C11 | Produktionsschnitt + Nahtzugaben | S. 36, 92–97 | C7–C10 | 🔒 | gemischt |

🔒 heißt: technisch machbar, aber die Quelle ist noch nicht geklärt oder das
Vormodul fehlt. Kein Grund zur Sorge — nur kein Startpunkt.

---

## Teil D — Ausgabe und Wirklichkeit

| # | Schritt | hängt an | Status |
|---:|---|---|:--:|
| D1 | DXF-Export mit Fadenlauf, Knips, Bohrloch, Beschriftung | A2, C11 | ⬜ |
| D2 | PDF zum Drucken (Kacheln) | C11 | ⬜ |
| D3 | **CLO 3D ansehen** — digitale Plausibilität und Avatar-Passform | C11 | ⬜ |
| D4 | Drucken | D2 | ⬜ |
| D5 | **Nähen** — beweist die Wahrheit | D4 | ⬜ |

---

## Teil E — Parallel mitlaufend

| # | Dokument | Status |
|---:|---|:--:|
| E1 | Kleid-Anleitung (Schritt für Schritt bis zur Naht) | ⬜ ab C1 mitschreiben |
| E2 | `600_prozess/10_begriffe_offen.md` — Begriffskandidaten | ⬜ ab Seitenprüfung |

---

## Der kritische Pfad

```
A1 ──► A3 ──► B1-B3 ──► C1 (Tellerrock) ──► C2 (SVG ansehen)
                                    │
A1 ──► B5-B8 ──► C3 ──► C4 ──► C5 ──► C6 ──► C7 ──► C11 ──► D
```

Der technische Pfad beginnt erst, wenn A1, A3 und die jeweilige
Konstruktionsseite verifiziert sind. Bis dahin bleibt jede Konstruktion
blockiert; es wird kein früherer Versuch als Abkürzung benutzt.

---

## Blockaden, die Werner auflösen muss

| # | Blockade | betrifft |
|---:|---|---|
| P1 | Bedeutung und mögliche Namenskollision `HaU`/`HdU` am Buch verifizieren | A1, alle Module |
| P2 | Welcher Weg zur Brustbreite ist Standard? | C3 |
| — | Fachnähte 7–10 aus `DEFINITION.md`: welche Buchseiten? | C8, C9 |
| — | Konflikt S. 438/439 (doppelt und abweichend transkribiert) | C7 |
| — | Rocklänge und zugehöriges Buchkürzel verifizieren und festlegen | C1, spätestens vor D4 |
| — | Fachliche Freigabe S. 44, S. 172–187, S. 423 | C1, C3, C6 |
