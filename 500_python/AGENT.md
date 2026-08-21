# Python — was hier drin gilt

## Navigation — Regel

Diese Datei führt nur zu den direkten Unterordnern von `500_python/`.
Einzelne Fachdateien werden hier nicht aufgeführt. Sie gehören in die
Agentendatei des jeweiligen Unterordners.

Die Ladeliste dient der Navigation. Automatisch geladen werden nur die
angekreuzten Agentendateien.

## Navigation

- [ ] `10_rechnung/AGENT.md`

## Zweck

Die Konstruktionen als Code. Ein **Modul** ist ein Baustein, den **jedes** Kleid
benutzen kann.

Ein Modul bekommt Maße und gibt Geometrie zurück. Es liest keine Buchseite, es
fragt niemanden, es zeichnet nichts.

## Die eiserne Regel

**Ein Modul darf nie wissen, welches Kleid gerade gebaut wird.**

„Abnäher schließen" kennt Geometrie und sonst nichts. Universalität entsteht
nicht dadurch, dass man groß baut, sondern dadurch, **was ein Modul nicht wissen
darf**.

Das gilt auch für den **Ort**: ein Modul liegt hier und nie im Kleiderordner.
Der Ort ist die erste Form von „wissen, wozu man gehört". Ein Kleid **benutzt**
ein Modul — es **besitzt** keines.

Konkret: der Glockenrock gilt für jeden Kreisrock, den es je geben wird. Dass
Kleid v001 ihn gerade braucht, geht das Modul nichts an.

## Grenze

| Nicht hier | Sondern |
|---|---|
| Die Formel selbst, ihr Buchbeleg, ihr Prüfwert | `300_formeln/` |
| Wie ein Lot, ein Kreis, ein Versatz rechnet | `400_mathematik/` |
| Auswahl und Verknüpfung der Module für ein Kleid | `700_schnitte/<kleid>/` |
| Maßwerte einer Person oder Größe | kommen als **Parameter** herein, stehen nie im Code |

Kein Kleidname, keine `v001`-Konstante, kein „für das Brautkleid nehmen wir hier
2 cm". Sobald so ein Satz im Code steht, ist es kein Modul mehr.

## Nummernschlüssel — hier endet die Repo-Nummerierung

Die Nummern hören bei `10_rechnung` auf. **Alles darunter ist Python-Namensraum.**

```
500_python/
  10_rechnung/          ← letzte nummerierte Ebene
    rock/
      glockenrock.py
    oberteil/
```

Grund: `import 20_rock` ist ein **Syntaxfehler**. Python-Namen dürfen nicht mit
einer Ziffer beginnen. Deshalb gilt unterhalb von `10_rechnung`:

- kleine Buchstaben, Unterstriche, keine Ziffer am Anfang
- keine Umlaute — auch nicht in Bezeichnern
- die Bereiche heißen wie in `300_formeln`, nur ohne Nummer:
  `rock`, `oberteil`

Die Kürzel aus dem Maßregister werden **umlautfrei** geschrieben:
`RueB`, `gRueB`, `TaW`, `r_TaW`. Ein Kommentar nennt die Buchschreibweise.

Wie die Module innerhalb eines Bereichs zu ordnen sind, entscheidet sich, wenn
drei oder vier hier liegen — nach Körperbereich, nach Kleidungsstück, nach
Bauteil. **Vorher nicht festlegen.**

## Form eines Moduls

Drei Dateien, gleicher Name:

| Datei | Inhalt |
|---|---|
| `glockenrock.py` | die Konstruktion — reine Funktionen |
| `test_glockenrock.py` | die Prüfwerte des Buchs als Test |
| `glockenrock.md` | die Modul-Doku |

Die Modul-Doku nennt:

1. **Formel-Kennungen** — welche `F-<seite>-<lfd>` aus `300_formeln` dieses
   Modul umsetzt
2. **Seitenzahl** — jede Formel trägt ihre Buchquelle mit
3. **Prüfwerte** — die Beispielzahlen des Buchs, oder „keine im Buch"
4. **Mathematik** — welche Primitive es braucht
5. **Freigabestatus** — Transkript geprüft? Von Werner/Munkhuu freigegeben?

Jede Funktion nennt im Docstring die Formel-Kennung, die sie umsetzt. So findet
eine Korrektur am Buch später jede Stelle im Code.

## Konventionen

| Was | Festlegung |
|---|---|
| Einheit | intern **Millimeter**; cm-Eingaben am Eintritt umrechnen |
| Y-Achse | zeigt **nach unten** |
| Rundung | **spät** — intern ungerundet, erst bei Anzeige und Export |
| Funktionen | **rein**: gleiche Eingabe, gleiche Ausgabe. Kein Datei-Zugriff, kein Zufall, kein globaler Zustand |
| Rückgabe | Punkte und Polygone — **kein DXF, kein SVG**. Der Export ist eine eigene Sache |
| Prüfwert-Vergleich | relativ, **0,1 %** — die Regel steht in `300_formeln` |

## Fertig-Regel

Ein Modul ist fertig, wenn:

1. jede Formel darin eine **Kennung und Seitenzahl** trägt,
2. die **Prüfwerte des Buchs als Test laufen** — grün, mit der Toleranz aus
   `300_formeln`,
3. es **ohne Kleidwissen** auskommt,
4. der **Freigabestatus** der Buchseite in der Doku steht.

**Ohne Prüfwert kein Modul.** Nennt das Buch keine Beispielzahl, wird das im
Test ausdrücklich so vermerkt; ein selbst nachgerechneter Wert darf als
Regressionswert dienen, muss aber als **„nicht aus dem Buch"** gekennzeichnet
sein. Sonst wird später das Buch gegen den Code geprüft statt umgekehrt.

**Nicht vorsorglich verallgemeinern.** Erst das zweite Kleid zeigt, was wirklich
ein Parameter sein muss. Vorher ist es Raten.

## Offene Stellen

- Der Ordner ist **leer** — `10_rechnung/rock/` und `10_rechnung/oberteil/`
  enthalten nur `.gitkeep`. Erstes Modul laut Roadmap: Tellerrock S. 44.
- **Wohin der Export gehört** (DXF, SVG, PDF, JSON), ist nicht entschieden:
  eigener Bereich unter `10_rechnung/`, oder eine eigene Ebene. Solange offen:
  kein Konstruktionsmodul schreibt eine Datei.
- Python-Version, Testwerkzeug und ob ein Paket-Layout mit `__init__.py`
  gebraucht wird — noch nicht festgelegt. Entscheidet das erste Modul.
