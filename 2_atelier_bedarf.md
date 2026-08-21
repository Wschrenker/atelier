# Atelier — Bedarfswissen

Diese Datei wird nur gelesen, wenn die jeweilige Einzelregel für die Arbeit
benötigt wird. Der Pflichtkern steht in `AGENT.md`.

## Namensregeln — im ganzen Repo gleich

- Erste Ebene: dreistellige Nummer, Unterstrich, kleiner Name — `300_formeln`
- Zweite Ebene: zweistellige Nummer, Unterstrich, kleiner Name — `10_masse`
- Keine Umlaute, keine Leerzeichen, keine Großbuchstaben.
  `ä→ae`, `ö→oe`, `ü→ue`, `ß→ss`
- Jeder gesteuerte Ordner trägt genau eine `AGENT.md`.
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

## Aktuelle offene Punkte

- **Persönliche Daten:** Echte Kundenmaße bleiben lokal. `MASSE.md` unter
  `800_couture` wird über `.gitignore` vom Repo ferngehalten.
- **Export-Ort:** Exportmodule gehören nach `500_python`; erzeugte DXF-, SVG-,
  PDF- und JSON-Dateien liegen im jeweiligen
  `800_couture/<auftrag>/ausgabe/`-Ordner.
- **Prozesspfad:** Offene Aufgaben werden in `600_prozess` geführt.
- **Bereinigte Dateinamen:** Die aktuell bereinigten Namen und frühere
  Abweichungen stehen im Git-Verlauf und in den jeweiligen Ordner-Agenten.
