# 20_codevertraege — lokale Arbeitsregeln

## Rolle

Diese Dateien sind die ausführbare Brücke zwischen mathematischer Recherche und Python-Code. Jede Datei besitzt nur allgemeine Geometrie; fachliche Hofenbitzer-Werte bleiben außerhalb.

## Direkte Kinder

- `00_format_und_status.md` — verbindliches Vertragsschema.
- `10_numerik_einheiten_und_toleranzen.md` — Zahlen- und Einheitspolitik.
- `20_punkte_vektoren_geraden_und_projektion.md` — lineare Grundgeometrie.
- `30_transformationen.md` — Verschieben, Drehen, Spiegeln, Skalieren.
- `40_kreise_und_boegen.md` — Kreis- und Bogengeometrie.
- `50_bezierkurven.md` — quadratische und kubische Kurven.
- `60_polygone_und_offsets.md` — Konturen und Parallelversatz.
- `65_flaechen_teilen_vereinigen_und_kopieren.md` — Abtrennen, Anschneiden, Kopieren und Wegschneiden.
- `70_messen_passung_und_markierungen.md` — Längen- und Nahtzuordnung.
- `75_keile_schliessen_und_oeffnen.md` — starres Schließen und Öffnen von Abnähern, Falten- und Drapierschnitten.
- `80_parameterketten_und_neuberechnung.md` — reine Berechnung und Abhängigkeiten.

## Regeln

- Nur die für den aktiven Funktionsschritt benötigte Datei laden.
- Python-Signaturen sind Zielverträge, kein Beleg für vorhandenen Code.
- Jeder Sonderfall muss sichtbar beendet werden: Ergebniszustand oder typisierter Fehler.
- Änderungen an Konventionen müssen gegen alle betroffenen Verträge geprüft werden.
