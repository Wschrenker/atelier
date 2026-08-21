# Kleider — was hier drin gilt

## Navigation — Regel

Diese Datei führt nur zu den direkten Unterordnern von `700_schnitte/`.
Einzelne Fachdateien werden hier nicht aufgeführt. Sie gehören in die
Agentendatei des jeweiligen Unterordners.

Die Ladeliste dient der Navigation. Automatisch geladen werden nur die
angekreuzten Agentendateien.

## Navigation

- [ ] `10_kleid_v001/AGENT.md`

## Zweck

Ein Ordner pro Kleid.

Ein Kleid ist eine **Auswahl und Verknüpfung von Modulen** — plus die
Entscheidungen, die nur dieses Kleid betreffen.

Es besitzt keine Konstruktion. Braucht ein Kleid etwas, das es noch nicht gibt,
entsteht das als **Modul** in `500_python` und wird von hier aus **benutzt**.

## Grenze

| Nicht hier | Sondern |
|---|---|
| Wiederverwendbare Konstruktionen, Code | `500_python/` |
| Formeln und ihr Buchbeleg | `300_formeln/` |
| Geometrie-Primitive | `400_mathematik/` |
| Begriffe und Kürzel | `000_sprache/` |

Was hier liegen **darf**: Entscheidungen, Auswahl, Reihenfolge, Status, die Maße
dieser Kundin, die Anleitung zu diesem Kleid.

Faustprobe: Würde ein zweites Kleid dieselbe Zeile brauchen, gehört sie nicht
hierher, sondern nach unten.

## Nummernschlüssel

| Teil | Bedeutung |
|---|---|
| `10_`, `20_`, `30_` … | zählt die **Kleider** |
| `v001`, `v002` … | zählt die **Fassungen** desselben Kleides |

`10_kleid_v001` — die Nummer bleibt beim Kleid, die Fassung wandert im
Ordnernamen mit. Ein zweites Kleid bekommt `20_`. **Eine vergebene Nummer wird
nie neu belegt.**

## Form eines Eintrags — zwei Pflichtdateien

| Datei | Was sie ist |
|---|---|
| `DEFINITION.md` | das **Scope-Dokument**. Was hier nicht steht, wird nicht gebaut. |
| `ROADMAP.md` | der **Modulstatus**. Der Punkt, an dem eine KI kalt einsteigt. |

Beide sind Dateien und **nicht Chat**. Was nur im Gespräch steht, ist verloren.

Ab dem ersten fertigen Modul kommt eine dritte dazu:

| Datei | Was sie ist |
|---|---|
| `ANLEITUNG.md` | die **Kleid-Anleitung** — Schritt für Schritt bis zur Naht, parallel zum Bauen geschrieben. Echtes Atelier-Werkzeug, auch für Munkhuu. |

### Was in `DEFINITION.md` steht

1. **Die Idee** — in zwei Sätzen, ohne Fachsprache
2. **Die Quellen** — je Teil: Buchseite, Bezeichnung im Buch, Foto
3. **Entscheidungen** — Tabelle `Entscheidung | Festlegung | Status`,
   jede Zeile entweder ✅ entschieden oder ⬜ offen
4. **Die offenen Punkte mit Gewicht** — mit ihren Folgen durchgerechnet
   (`MoL` → Saumweite 3,9 m / 5,8 m / 7,3 m)
5. **⚠️ Was am Buch zu prüfen ist** — Fachnähte und Verarbeitungen,
   mit Buchstelle oder ausdrücklich `?`
6. **Was bewusst draußen bleibt** — vertagt, nicht verworfen

Ein `?` ist ein gültiger Eintrag. Eine erfundene Seitenzahl nicht.

### Was in `ROADMAP.md` steht

Fünf Teile, in dieser Reihenfolge:

| Teil | Inhalt |
|---|---|
| **A** | Grundlagen — vor jeder Konstruktion |
| **B** | Mathematik — modeblind, darf vorgecodet werden |
| **C** | Konstruktion — die Module |
| **D** | Ausgabe und Wirklichkeit — DXF, PDF, CLO 3D, drucken, nähen |
| **E** | Parallel mitlaufend — Anleitung, offene Begriffe |

Jede Zeile trägt: **Nummer · Modul · Quelle · hängt an · Status · Quellenlage.**

Legende: ✅ fertig · 🔄 läuft · ⬜ offen · 🔒 blockiert

🔒 heißt: technisch machbar, aber die Quelle ist ungeklärt oder das Vormodul
fehlt. Kein Grund zur Sorge — nur kein Startpunkt.

Dazu am Ende zwei Abschnitte: **der kritische Pfad** und **die Blockaden, die
der Mensch auflösen muss**. Gelöste Blockaden werden durchgestrichen, nicht
gelöscht — die Entscheidung bleibt sichtbar.

## Fertig-Regel

| Was | Fertig, wenn |
|---|---|
| **Definition** | jede Zeile der Entscheidungstabelle ✅ oder ausdrücklich ⬜ ist |
| **Roadmap-Eintrag** | sein Modul in `500_python` liegt, die Prüfwerte grün sind und die Buchseite **freigegeben** ist |
| **Kleid** | es **genäht** ist |

CLO 3D zeigt Plausibilität — **es beweist nichts.** Der Beweis ist die Naht.

## Die Reihenfolge

Erst die Definition, dann die Roadmap, dann die Module.

Eine unscharfe Definition erzeugt eine unscharfe Roadmap — und damit offenen
Scope. **Wenn das Kleid steht, ist der Scope zu.**

## Offene Stellen

- `10_kleid_v001/DEFINITION.md` ist **Entwurf** und wartet auf Werners Freigabe
- Offen darin: `MoL` (Kostenentscheidung), Größe und Maße, Lage des
  Reißverschlusses, Futter, Nahtzugaben
- Fachnähte 7–10 tragen `?` statt einer Buchseite
- `ROADMAP.md` verweist bei E2 auf `600_prozess/10_begriffe_offen.md` — offene
  Aufgaben und Begriffskandidaten werden dort geführt
- `ANLEITUNG.md` gibt es noch nicht — sie beginnt mit C1
