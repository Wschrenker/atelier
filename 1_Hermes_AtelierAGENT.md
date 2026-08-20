# Atelier — oberste Ebene

Projekt: `jijge_bridal_engine_v2`
Arbeitsordner: `C:\ATELIER`
Stand: 2026-08-20 — Struktur umbenannt, Fundament im Aufbau.

## Regel dieser Datei

Was **zwei Ordner** betrifft, steht hier.
Was **einen Ordner** betrifft, steht in dessen `1_…AGENT.md`.
Was oben steht, wird unten nicht wiederholt.

Wer in einem Ordner arbeitet, liest dessen Agentendatei — nicht das ganze Repo.

## Ziel

Schnittmusterprogramm aus Formeln. Ausgabe: DXF, SVG, PDF, JSON.

Gleichrangiges zweites Ziel: Werner und Munkhuu verstehen jede Konstruktion,
die der Code ausführt.

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

- Niemand greift nach oben. Ein Ordner kennt nur, was in seiner Spalte steht.
- Der Sprung 500 → 700 ist die Grenze: darunter die **Maschine**, darüber das
  **Werkstück**. Die Maschine bleibt fest, die Werkstücke werden mehr.
- **Die eiserne Regel:** Ein Modul darf nie wissen, welches Kleid gerade gebaut
  wird. Das gilt auch für den Ort — ein Modul liegt in `500_python`, nie im
  Kleiderordner.
- Gebaut wird von unten, **ausgewählt von oben**: Was gebaut wird, entscheidet
  das Kleid — nicht das Inhaltsverzeichnis. Nichts entsteht auf Vorrat.
  Wenn das Kleid steht, ist der Scope zu.
- Nicht vorsorglich verallgemeinern. Erst das zweite Kleid zeigt, was wirklich
  ein Parameter sein muss.

## Namensregeln — im ganzen Repo gleich

- Erste Ebene: dreistellige Nummer, Unterstrich, kleiner Name — `300_formeln`
- Zweite Ebene: zweistellige Nummer, Unterstrich, kleiner Name — `10_masse`
- Keine Umlaute, keine Leerzeichen, keine Großbuchstaben.
  `ä→ae`, `ö→oe`, `ü→ue`, `ß→ss`
- Jeder Ordner trägt genau eine `1_Hermes_<ordner>AGENT.md` — Ordnername
  kleingeschrieben, nur `AGENT` in Versalien
- Versionen hinten, dreistellig — `10_kleid_v001`
- Eine vergebene Nummer wird nie neu belegt — auch nicht, wenn der Ordner
  wieder leer ist

## Kadenz pro Baustein

1. Seite lesen → neue Begriffe nach **Gosslar** (`000_sprache`)
2. Formeln wörtlich ablegen, **mit Seitenzahl** (`300_formeln`)
3. Beispielzahlen des Buchs notieren → **Prüfwerte**

Schritt 1–3 macht der Mensch. **Code kommt nie vor den Prüfwerten.**

Danach: Mathe → Python → Modul.
Dann: Kleid coden → CLO 3D ansehen → drucken → nähen.

Ein Baustein gilt erst als belegt, wenn die Buchseite von Werner oder Munkhuu
**am Buch freigegeben** ist.

## Zwei Dokumentationsebenen

- **Modul-Doku** — was rechnet dieses Modul, welche Seite, welche Prüfwerte.
  Entsteht beim Bauen von selbst.
- **Kleid-Anleitung** — wie entsteht dieses Kleid, Schritt für Schritt bis zur
  Naht. Eigenes Dokument, wird **parallel zum Bauen** geschrieben.
  Echtes Atelier-Werkzeug, auch für Munkhuu.

Der gemeinsame Stand liegt **im Repo, nicht im Chat**. Was nur im Gespräch
steht, ist verloren.

## Was hier nicht steht

| Frage | Steht in |
|---|---|
| Wie ein Begriff aufgenommen wird | `000_sprache` |
| Transkriptionsregeln, freigegeben vs. transkribiert | `100_quellen` |
| Formelnotation, Maßregister, Seitenbeleg | `300_formeln` |
| Signaturen und Einheiten der Primitive | `400_mathematik` |
| Modulschnitt, Stil, Tests gegen Prüfwerte | `500_python` |
| Was offen ist und wer dran ist | `600_prozess` |
| Aufbau eines Kleiderordners, `DEFINITION.md` und `ROADMAP.md` | `700_schnitte` |

Jede Ordner-Agentendatei hat dasselbe Gerüst:
**Zweck · Grenze · Nummernschlüssel · Form eines Eintrags · Fertig-Regel.**

Die **Grenze** ist der wichtigste Abschnitt — dort entstehen die Fehler,
nicht beim Zweck.

## Offen

- **Persönliche Daten:** entschieden — echte Kundenmaße bleiben lokal. `MASSE.md`
  unter `800_couture` wird über `.gitignore` vom Repo ferngehalten.
- **Export-Ort:** entschieden — die Exportmodule gehören nach `500_python`;
  erzeugte DXF-, SVG-, PDF- und JSON-Dateien liegen im jeweiligen
  `800_couture/<auftrag>/ausgabe/`-Ordner.
- **Prozesspfad:** entschieden — offene Aufgaben werden in `600_prozess`
  geführt.
- **Dateinamen gegen die Namensregel:**
  `000_sprache/10_abkuerzungen.md` (bereinigt) ·
  `000_sprache/20_schnittmuster_symbole.md` (bereinigt) ·
  `300_formeln/10_masse/10_massregister.md` (bereinigt) ·
  `300_formeln/20_rock/10_formel_rock_glocke.md` (bereinigt) ·
  `600_prozess/10_begriffe_offen.md` (bereinigt) ·
  vier Agentendateien mit großem Ordnernamen (`Quellen`, `Formeln`, `Python`,
  `Schnitte`) (bereinigt)

---
Aktiv steuert: Wschrenker + Munkhuu
KI-Partner: Hermes, Claude, Codex — weitere situativ
