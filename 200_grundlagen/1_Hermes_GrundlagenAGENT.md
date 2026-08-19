# jijge_bridal_engine_v2
Arbeitsordner: C:\ATELIER

## Status (2026-08-17)



## Ziel
Vom Buch  Formeln und Gosslar für Kommunikation einpflegen

## Quelle
**Guido Hofenbitzer — Grundschnitte und Modellentwicklungen.
Schnittkonstruktion für Damenmode.** Europa-Lehrmittel.
Band 1 (3. Auflage 2024) und Band 2 (Noch nicht transskripiert und im desktop). Auch andere Bücher werden zum Einsatz kommen. 

Das Buch ist die einzige fachliche Quelle der Engine. Jede Konstruktion,
jede Formel und jeder Prüfwert stammt daraus und trägt eine Seitenzahl.
Transkripte und Fotos liegen unter `100_quellen/110_hofenbitzer/`.




## Grundlagen zuerst
Bedarfsgetrieben heißt: keine **Modelle** auf Vorrat bauen.
Es heißt **nicht**, die Grundlagen zu überspringen.

Vor der ersten Konstruktion werden eingepflegt:
1. **Abkürzungen und Maße** (S. 9, 11–15) — das Vokabular für alles Weitere
2. **Standards und Zeichen** (S. 21–31) — Linienarten, Nahtzugaben, Knipse,
   Bohrlöcher, Beschriftung
3. **Größentabelle** (S. 20) — liefert die Zahlen für jeden Test

Grund: die Begriffe müssen verstanden sein, die Konstruktion baut darauf auf,
und die Formeln sollen von Anfang an nachvollziehbar sein.

**Die Schnittzeichen sind kein Lernmaterial, sondern eine Ausgabe-Anforderung.**
Knips, Bohrloch, Fadenlauf, Stoffbruch und Beschriftung müssen am Ende im DXF
und im PDF stehen, sonst ist der Schnitt nicht produktionsfähig.

## Quellen-Disziplin
Jedes aus einem Transkript übernommene Stück nimmt **seine Seitenzahl mit**.
Grund: die Transkripte haben offene Stellen — vermutete Buchfehler, unlesbare
Passagen, Doppel-Transkription S. 438/439.
Korrekturen müssen später alle Kopien finden.
Ein Baustein gilt erst dann als belegt, wenn die Seite von Werner/Munkhuu
am Buch freigegeben ist.




## Die eiserne Regel
**Ein Modul darf nie wissen, welches Kleid gerade gebaut wird.**
„Abnäher schließen" kennt Geometrie und sonst nichts.
Universalität entsteht nicht dadurch, dass man groß baut, sondern dadurch,
was ein Modul nicht wissen darf.

Daraus folgt die Schichtung:
- **Geometrie** und **Ausgabe** wissen nichts von Mode.
- **Konstruktion** weiß nichts von DXF.
- **Kleid** kennt Module — aber kein Modul kennt das Kleid.



## Arbeitsweise pro Buchseite
1. Seite lesen → neue Begriffe nach **Gosslar**
2. Formeln wörtlich ablegen




Schritt 1–3 macht der Mensch. **Code kommt nie vor den Prüfwerten.**

## Sprache
Jeder Fachbegriff, den eine KI verwendet und der nicht in **Gosslar** steht,
ist ein fehlender Glossareintrag — kein Wissensdefizit des Menschen.
Solche Begriffe wandern nach `200_grundlagen/888_BEGRIFFE_OFFEN.md`.
Begriffe werden beim ersten Gebrauch in einem Halbsatz miterklärt.

> Die Nummern-Ordnung gilt fürs ganze Repo und steht deshalb oben in
> `1_Hermes_AtelierAGENT.md`.



## Arbeitsteilung mit der KI
- **Mathe vorcoden: ja.** Kurve durch Punkte, Spiegeln, Zirkelschlag, Drehen,
  Schnittpunkte, Lot, Parallelversatz. Modeblind, ungefährlich.
- **Konstruktionen vorcoden: nein.** Sonst steht der Code vor dem Prüfwert,
  und das Buch wird gegen den Code geprüft statt umgekehrt.
- Beim Transkribieren erzeugt die KI **strukturierte Formeln, keinen Code**:
  Eingangsmaße, Ergebnis, Seitenzahl, Beispielzahl.




Der gemeinsame Stand liegt **im Repo, nicht im Chat**: Kleid-Definition,
Roadmap und Modulstatus sind Dateien. Nur so kann jede KI kalt einsteigen.






## Phase jetzt
1. ✅ **Kleid v001** definiert → `400_pattern/kleid_v001/DEFINITION.md`
2. ✅ Roadmap abgeleitet → `400_pattern/kleid_v001/ROADMAP.md`
3. ✅ Transkripte in Git gesichert (Fotos bleiben draußen)
4. 🔄 Grundlagen Block 1: Abkürzungen und Maße (S. 9, 11–15)
5. ⬜ Grundlagen Block 2: Standards und Zeichen (S. 21–31)
6. ⬜ Grundlagen Block 3: Größentabelle (S. 20)
7. ⬜ Erstes Modul: Tellerrock S. 44

## Nächster Schritt
Werner prüft Block 1

---
Aktiv steuert: Wschrenker + Munkhuu
KI-Partner: Hermes, Claude, Codex — weitere situativ
