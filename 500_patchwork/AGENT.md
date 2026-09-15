# 500_patchwork — Arbeitsregeln

## Aufgabe

`500_patchwork/` ist die visuelle Auswahl-Oberfläche, mit der Werner
entscheidet, welche code-technisch vorhandenen Bausteine ein Kleidungsstück
bekommt und wo sie sitzen (z. B. Reißverschluss seitlich/rückwärtig). Es ist
kein Ersatz für `300_messmodul/` (Körpermaße) und keine Konstruktionsengine.

## Status

Pilotumfang für den geraden Rock festgelegt. Noch kein Code, keine Oberfläche
und kein festgelegtes Datenformat; verbindlich sind die Entscheidungen in
`SPEC.md` und der Grundsatz "ehrlich zum Code".

## Direkte Kinder

- `README.md` — kurzer Überblick, wofür der Ordner steht.
- `SPEC.md` — Zweck, Datenfluss-Rolle, was das Modul können muss, offene
  Fragen.

## Ladeweise

1. Zuerst `PRODUKTZIEL.md`, `ARCHITEKTUR.md` und `DATENMODELL.md` im
   Repo-Wurzelordner lesen (`DATENMODELL.md` definiert u. a. `Bausteinvertrag`,
   das die offene Frage zum Baustein-Katalog in `SPEC.md` berührt).
2. Danach diese Datei und `SPEC.md`.
3. Erst danach, falls einschlägig, `300_messmodul/` ansehen (bestehendes
   Messmodul, dessen Stil und Datenformen als Orientierung dienen).

## Grenzen

- Nichts als wählbare Option zeigen, was im Code nicht tatsächlich existiert.
- Keine fachliche Variante ohne Buchbeleg erfinden; offene fachliche Fragen
  bleiben offen und werden nicht durch eine Vermutung geschlossen.
- Werner bestimmt Ordnerstruktur, Format und Umfang; nicht eigenständig
  erweitern oder umbenennen.
- Änderungen hier erst nach Absprache — dieser Ordner ist Diskussionsstand,
  kein freigegebener Vertrag.
