# 500_patchwork — Arbeitsregeln

## Aufgabe

`500_patchwork/` ist die visuelle Auswahl-Oberfläche, mit der Werner
entscheidet, welche code-technisch vorhandenen Bausteine ein Kleidungsstück
bekommt und wo sie sitzen (z. B. Reißverschluss seitlich/rückwärtig). Es ist
kein Ersatz für `300_messmodul/` (Körpermaße) und keine Konstruktionsengine.

## Status

Konzeptphase. Kein Code, keine Oberfläche, kein festgelegtes Datenformat.
Bevor hier programmiert wird, muss geklärt sein, welchen Baustein das Modul
zuerst abbildet — sonst fehlt der Bezug, den `SPEC.md` unter "ehrlich zum
Code" verlangt.

## Direkte Kinder

- `README.md` — kurzer Überblick, wofür der Ordner steht.
- `SPEC.md` — Zweck, Datenfluss-Rolle, was das Modul können muss, offene
  Fragen.

## Ladeweise

1. Zuerst `PRODUKTZIEL.md` und `ARCHITEKTUR.md` im Repo-Wurzelordner lesen.
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
