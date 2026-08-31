# Kleid Lumière — Roadmap

Stand: 2026-08-31

Diese Datei ist der **Modulstatus**. Sie ist der Punkt, an dem eine KI kalt
einsteigen kann.

Legende: ✅ fertig · 🔄 läuft · ⬜ offen · 🔒 blockiert

---

## Teil A — Grundlagen

| # | Modul | Quelle | Modul im Code | Status | Freigabe Buch |
|---:|---|---|---|:--:|---|
| A1 | Abkürzungen und Maße | S. 9, 11–15 | — | ⬜ | ⬜ am Buch prüfen |
| A2 | Standards und Schnittzeichen | S. 21–31 | — | 🔒 | ⬜ **Layernamen im DXF sind frei gewählt** |
| A3 | Größentabelle | S. 20 | `masse/groessentabelle.py` | ✅ | ⬜ am Buch prüfen |

**A2 blockiert D1.** Bis die Schnittzeichen verifiziert sind, tragen die
DXF-Ebenen selbstgewählte Namen (`SCHNITTKANTE`, `ABNAEHER`, `FADENLAUF`, …)
und keine Norm-Behauptung.

---

## Teil B — Mathematik (modeblind)

| # | Primitive | Funktion | Status |
|---:|---|---|:--:|
| B1 | Kreis um Mittelpunkt mit Radius | `geometrie.kreisbogen` | ✅ |
| B2 | Lot / rechter Winkel | `geometrie.normale` | ✅ |
| B3 | Kreisbogen-Segment | `geometrie.kreisbogen` | ✅ |
| B4 | Drehen um Punkt | `geometrie.drehe` | ✅ |
| B5 | Spiegeln an Achse | `geometrie.spiegle_senkrecht` | ✅ |
| B6 | Kurve durch gegebene Punkte | `geometrie.glatte_kurve` | ✅ |
| B7 | **Parallelversatz (Nahtzugaben)** | — | ⬜ |
| B8 | Schnittpunkt Linie/Linie | `geometrie.schnitt_gerade_gerade` | ✅ |
| B9 | Länge entlang Kurve | `geometrie.polylinie_laenge` | ✅ |

B7 fehlt und wird erst mit dem Produktionsschnitt (C11) gebraucht.

---

## Teil C — Konstruktion

| # | Modul | Quelle | Modul im Code | Status | Quellenlage |
|---:|---|---|---|:--:|---|
| C1 | Rock-Grundgerüst | S. 33–35 | `rock/gerader_rock.py` | ✅ | geprüft, Freigabe offen |
| C2 | Saumerweiterter Rock | S. 42–43 | `rock/saumerweitert.py` | ✅ | geprüft, Freigabe offen |
| C3 | Oberteil-Grundgerüst | S. 177–181 | `oberteil/grundgeruest.py` | ✅ | geprüft, Freigabe offen |
| C4 | Tailliertes Oberteil, Taillenabnäher | S. 184–185 | `oberteil/tailliert.py` | ✅ | geprüft, Freigabe offen |
| C5 | **Brustabnäher öffnen** | S. 184 ㉖/㉗ | Winkel berechnet, nicht ausgeschnitten | 🔒 | **Li26 unklar** |
| C6 | Abnäherverlegung in Drapierfalten | S. 423 ❑7, ❑8a | — | 🔒 | roh, keine Zahlen |
| C7 | Asymmetrisches Wickeloberteil | S. 423 ❑8, ❑8b | `bauen.py`, Modellparameter | 🔄 | roh |
| C8 | Taillennaht Rock an Oberteil | S. 406–407, 438–439 | Kontrolle in `bauen.py` | 🔄 | roh |
| C9 | Ausschnitt + Beleg | ? | — | 🔒 | Seite unbekannt |
| C10 | Armloch fertigstellen | ? | — | 🔒 | Seite unbekannt |
| C11 | Produktionsschnitt + Nahtzugaben | S. 36, 92–97 | — | 🔒 | B7 fehlt |
| C12 | Echter Glockenrock (Prüfwert) | S. 44 | `rock/glocke.py` | ✅ | **fachlich freigegeben 2026-06-21** |

C8 ist grün gerechnet, aber nicht gelesen: `bauen.py` prüft, dass Oberteil-
und Rocktaille auf 0,01 cm zusammenpassen. Wie die Naht *verarbeitet* wird,
steht auf S. 406–407 / 438–439 und ist noch roh.

---

## Teil D — Ausgabe und Wirklichkeit

| # | Schritt | Status |
|---:|---|:--:|
| D1 | DXF-Export | ✅ `ausgabe/kleid_lumiere_gr38.dxf`, 6 Teile, mm, R12 |
| D2 | PDF zum Drucken (Kacheln) | ⬜ |
| D3 | CLO 3D ansehen | ⬜ |
| D4 | Drucken | ⬜ hängt an D2 und C11 |
| D5 | Nähen | ⬜ |

**D1 ist ohne Nahtzugaben.** Das DXF zeigt Netto-Schnittkanten. Vor D4 muss
C11 laufen.

---

## Teil E — Parallel mitlaufend

| # | Dokument | Status |
|---:|---|:--:|
| E1 | `ANLEITUNG.md` | ⬜ beginnt, wenn C5 entschieden ist |
| E2 | `600_prozess/10_begriffe_offen.md` | ⬜ |

---

## Prüfwerte

`500_python/10_rechnung/test_buchwerte.py` — 12 Tests, alle grün.
Nachgerechnete Buchbeispiele: S.20 · S.44 (rTaW/rSaW/SaW und NZg-Formel) ·
S.177 (BrW-Kontrolle) · S.178 (zwei Buchfehler, bewusst nicht übernommen) ·
S.184/185 (me 2,2 · vAbl 3,2 · TaB 42,8 · TaAf 6,8) · S.33 · S.35 · S.43.

---

## Blockaden, die Werner auflösen muss

| # | Blockade | betrifft |
|---:|---|---|
| P1 | **Li26 auf S.184 Abb. ❑8b** — welche Linie, und wo liegt der geöffnete Abnäher? | C5, C6, C7 |
| P2 | Lässt S.184 ㉝ („Schulterabnäher am Armloch zulegen") sich mit Abb. ❑8c vereinbaren, die den Abnäher zeigt? | C4 |
| P3 | Schnittzeichen S. 21–31 verifizieren → DXF-Ebenen | A2, D1 |
| P4 | Freigabe S. 33–35, 42–43, 177–181, 184–185 | C1–C4 |
| P5 | Fachnähte 5–10 aus `DEFINITION.md`: welche Buchseiten? | C9, C10 |
| P6 | Saumerweiterung 90 cm am Stoff prüfen — Seiden-Crêpe-Satin fällt anders als Taft | C2 |
