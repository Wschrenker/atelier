# Prüfstellen im Archiv — Geschichte und Kontrolle

Stand: 2026-09-08

## Wofür dieser Ordner da ist

Hier liegen die Prüfstellen **vollständig und dauerhaft**. Kein Punkt wird
gelöscht, auch keiner, der abgearbeitet ist. Wer wissen will, was an einer
Buchseite einmal beanstandet wurde und wie es ausgegangen ist, liest hier.

Die Arbeitsansicht unter

```text
100_quellen/10_hofenbitzer_band_1_digital/pruefstellen_nach_seiten/
```

zeigt dagegen nur, **was noch offen ist**. Erledigte Punkte stehen dort seit
dem 2026-09-08 nur noch als Zählzeile:

```text
*1 erledigt (D7) — Wortlaut in der Archivquelle.*
```

Damit bleibt eine geprüfte Seite von einer nie angeschauten unterscheidbar,
ohne dass die Seite mit abgeschlossenen Punkten volläuft.

## Die zwei Richtungen

Beide Sorten liegen in [`prüfstelle_text_zusammenzug/`](prüfstelle_text_zusammenzug/):

- **D-Punkte** — [`01_abweichungen_transkript_vom_foto.md`](prüfstelle_text_zusammenzug/01_abweichungen_transkript_vom_foto.md).
  Das Buch ist in Ordnung, **unsere Transkription weicht ab**. Diese Punkte
  sind abarbeitbar: die Seitendatei wird fototreu berichtigt.
- **A/B/C-Punkte** — [`02_buchfehler_aus_dem_archiv.md`](prüfstelle_text_zusammenzug/02_buchfehler_aus_dem_archiv.md).
  Die Transkription gilt als fototreu, der Verdacht richtet sich gegen die
  **gedruckte Seite**. Diese Punkte kann nur Werner am Buch entscheiden.

Ein D-Punkt und ein A-Punkt beschreiben oft dieselbe Stelle aus den zwei
Richtungen. Wird der D-Punkt abgearbeitet, steht der gedruckte Fehler danach
fototreu in der Datei — und der A-Punkt bleibt offen, bis das Buch geprüft ist.

Dazu kommen die Formel-Prüfstellen in
[`prüfstelle_formel_zusammenzug/`](prüfstelle_formel_zusammenzug/).

## Wie ein Punkt erledigt wird

1. Die Stelle wird vorgelegt: was steht in der Datei, was steht im Buch.
2. Die Seitendatei `sNNN.md` wird auf die gedruckte Form gebracht. Gedeckt ist
   das durch die dritte Ausnahme in
   [`10_hofenbitzer_band_1_digital/AGENT.md`](../10_hofenbitzer_band_1_digital/AGENT.md).
   Ein im Buch gedruckter Fehler wird dabei **mit übernommen**, nicht geglättet.
3. Der Punkt bekommt hier im Archiv den Status `erledigt <Datum>` und darunter
   einen Vermerk, der den Eingriff wörtlich festhält.
4. Die Ansicht wird neu erzeugt:

```text
python 600_prozess/werkzeuge/pruefstellen_ansicht_bauen.py             Probelauf
python 600_prozess/werkzeuge/pruefstellen_ansicht_bauen.py --schreiben
```

Ohne Schritt 3 gilt die Berichtigung als nicht erfolgt. Die Statuszeile im
Archiv ist der einzige Nachweis; die Ansicht ist erzeugt und beweist nichts.

## Stehende Entscheidungen

Damit dieselbe Frage nicht an jeder Seite neu gestellt wird.

**Strichtypen — 2026-09-08, Werner.** Überall der **ASCII-Bindestrich** `-`.
Kein Halbgeviertstrich `–`, kein Geviertstrich `—`, kein mathematisches
Minuszeichen `−` — weder im Satz, noch in Zahlenbereichen, noch in
Rechenzeilen. Das deckt sich mit dem Buch: die Strichtypen-Punkte sagen
nahezu durchweg, dass im Druck der Bindestrich steht und unser Transkript
den langen Strich gesetzt hat.

Zwei belegte Gegenstellen bleiben ausgenommen: **D24** (S.146, SaW-Rechnung)
und **D62** (S.152, Saumeinschlag). Dort nennt der Punkt den langen Strich
ausdrücklich als gedruckte Form.

**Durchgeführt am 2026-09-08.** Zwei Läufe über alle Seitentranskriptionen:

| | Dateien | Ersetzungen |
|---|---:|---:|
| Seiten, die ein Strichtypen-Punkt nennt | 61 | 293 |
| übrige Seiten | 190 | 884 |
| **gesamt** | **251** | **1177** |

Übrig sind danach genau die drei Striche der beiden Ausnahmen: zwei in
`s146.md`, einer in `s152.md`. Betroffen waren nur die `sNNN.md`; die
Formeldateien wurden nicht angefasst.

Nicht von dieser Entscheidung betroffen sind Bindestriche **innerhalb von
Wörtern** (D81 „Schlitz-Beleg", D181 „vorde-ren", D208 „Kragen-Kante").
Das ist eine andere Frage: dort geht es um Worttrennung und Umbruch, nicht
um den Strichtyp.

**Lesehinweis bei gedruckten Wortfehlern — 2026-09-08, Werner.** Wo ein im
Buch gedruckter Wortfehler fototreu übernommen wird, steht dahinter
`[sic: <richtige Form>]`. Die Datei bleibt damit ein Abbild des Buches und
ist trotzdem lesbar. Erste Anwendung: D32, S.162.

**Hervorgehobene Kästen - 2026-09-08, Werner.** Ein im Buch grau oder farbig
hinterlegter Kasten bekommt eine Kopfzeile, sein Inhalt steht darunter als
Blockzitat:

```text
**Grau hinterlegter Kasten:**

> Der Taillen- und der Hüftumfang ist bei allen Figuren identisch.
```

So ist von außen zu sehen, wo der Kasten anfängt und wo er aufhört. Im Bestand
stehen daneben noch die älteren Formen `[Kasten, grau hinterlegt:]` (S.11),
`[Grau hinterlegter Kasten:]` (S.12) und die Variante mit Kastentitel auf S.438.
Reichweite: ganzer Band. Erste Anwendung: S.37.

**Punktnummern in den Zeichnungen - 2026-09-08, Werner.** Die blauen
Kreisziffern in den Konstruktionszeichnungen werden in der Seitendatei mit
erfasst, je Zeichnung getrennt, unter den Zeichnungs-Beschriftungen. Sie sind
der Faden zwischen Text und Bild und werden für die Schritte in
`200_funktionen` gebraucht.

Zwei Fälle sind ausdrücklich zu vermerken, weil sie sonst falsch gelesen
werden: dieselbe Nummer kann **in zwei Zeichnungen** stehen, und sie kann
**innerhalb einer Zeichnung mehrfach** stehen. Beides wird ausgeschrieben
(`(zweimal)`), nicht zusammengezogen. Nummern, die neben einer Tabelle oder
einem Bildrand stehen und nur mit einer Linie in die Zeichnung zeigen, werden
dort vermerkt, wo sie stehen. Erste Anwendung: S.35.

**Doppelpunkt als Rechenzeichen in Zeichnungen - 2026-09-08, Werner.** In
Zeichnungsbeschriftungen wird der Doppelpunkt **mit Leerzeichen** gesetzt:
`TaU : 10`. Im Druck steht er in der Skizze eng (`TaU:10`), aber so klein,
dass der Abstand nicht zu beurteilen ist. Die geschriebene Form ist deshalb
einheitlich die mit Leerzeichen. Reichweite: alle Zeichnungsbeschriftungen im
ganzen Band, auch die noch nicht angeschauten. Im Fließtext bleibt die
gedruckte Form stehen.

## Bisher erledigt

**2026-09-08 - Foto-Zeile auf den heutigen Bildordner umgestellt.** Die Zeile
`Foto:` zeigte in elf Seitendateien noch auf `Photos-3-001 ...`, einen Ordner,
den es im Repo nicht mehr gibt. Sie zeigt jetzt auf
`100_quellen/20_hofenbitzer_band_1_bilder/1.1_Photos_hofenb_ba1_total/sNN.jpg`;
der alte Kameradateiname steht als `(Kameradatei ...)` dahinter und bleibt
damit als Beleg erhalten. Betroffen: s32-s36, s39 und s40-s44. Werner hat den
Schreibschutz dafür am 2026-09-08 ausdrücklich aufgehoben.

**2026-09-08 - S.34, Zeichnungs-Beschriftung berichtigt.** In `s34.md` stand
unter den Beschriftungen zu ☐5 „¼ wie bei P10". Im Foto steht eindeutig
„½ wie bei P10", und Schritt (11) derselben Seite sagt ebenfalls ½
(„0,5 bis 0,7 cm ca. ½ Erhöhung an der Seitenlinie"). Werner hat die
Berichtigung entschieden; ein D-Punkt lag dazu nicht vor. Die Stelle ist beim
Bildabgleich zu S.35 aufgefallen, weil die entsprechende Beschriftung dort
„½ wie bei P10" und „½ wie nach P10" lautet.

**2026-09-08 - S.35 nach Bildabgleich ergänzt.** Werner hat die Punkte
einzeln entschieden. In `s35.md`: der Unsicherheitsvermerk an der
Bildunterschrift ☐6 gestrichen (die Klammer `(Grün ☐4)` steht so im Buch, das
Grün meint die Figur aus ☐4 auf S.34); der rote Seitenverweis `37`
nachgetragen; die Zeichnungs-Beschriftungen vollständig gemacht - es fehlten
das Maß `3,0 cm` und die Beschriftung `1. h. Abnäher` - und die Punktnummern
je Zeichnung aufgenommen. Offen bleibt: ob die Unterstreichungen in den
Bildunterschriften ☐8 und ☐9 (`einem` / `zwei`) mitgeschrieben werden.

**2026-09-08 — 19 D-Punkte, reine Typografie.** Seiten 108, 112, 114, 146,
152, 153, 156, 157, 159, 161, 162, 166, 168, 170 und 290:

D7, D8, D15, D24, D32, D34, D36, D37, D56, D57, D61, D62, D77, D79, D80,
D147, D151, D152, D156.

**2026-09-08 — 27 Strichtypen-Punkte** über die stehende Entscheidung:
D35, D100, D149, D159, D185, D186, D220, D244, D245, D306, D307, D322, D325,
D379, D405, D428, D458, D469, D497, D498, D501, D504, D543, D589, D598, D613,
D617.

**2026-09-08 — D34 und A127 am Buch geprüft: gegenstandslos.** Werner hat
S.159 aufgeschlagen: dort steht durchgehend „Hot-Pants" mit Bindestrich, auch
in der Bildunterschrift □1 und im Randregister. Die Beanstandung trifft nicht
zu; die am selben Tag vorgenommene Änderung wurde zurückgedreht. Beide Punkte
bleiben mit diesem Befund stehen — geprüft und nichts gefunden ist etwas
anderes als nie angeschaut.

Zurückgestellt: **D81** (S.165, „Schlitz-Beleg"), **D181** (S.297,
„vorde-ren") und **D208** (S.322, „Kragen-Kante"). Alle drei betreffen den
Bindestrich **innerhalb** eines Wortes, also Worttrennung und Umbruch — nicht
den Strichtyp. Die stehende Entscheidung deckt sie nicht ab; das entscheidet
sich am Foto.
