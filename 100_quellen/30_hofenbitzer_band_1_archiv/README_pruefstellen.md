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

Nicht von dieser Entscheidung betroffen sind Bindestriche **innerhalb von
Wörtern** (D81 „Schlitz-Beleg", D181 „vorde-ren", D208 „Kragen-Kante").
Das ist eine andere Frage: dort geht es um Worttrennung und Umbruch, nicht
um den Strichtyp.

**Lesehinweis bei gedruckten Wortfehlern — 2026-09-08, Werner.** Wo ein im
Buch gedruckter Wortfehler fototreu übernommen wird, steht dahinter
`[sic: <richtige Form>]`. Die Datei bleibt damit ein Abbild des Buches und
ist trotzdem lesbar. Erste Anwendung: D32, S.162.

## Bisher erledigt

**2026-09-08 — 19 D-Punkte, reine Typografie.** Seiten 108, 112, 114, 146,
152, 153, 156, 157, 159, 161, 162, 166, 168, 170 und 290:

D7, D8, D15, D24, D32, D34, D36, D37, D56, D57, D61, D62, D77, D79, D80,
D147, D151, D152, D156.

Zurückgestellt: **D81** (S.165, „Schlitz-Beleg"). Der Punkt sagt, im Druck
stünden „Schlitz" und „Beleg" auf zwei Zeilen ohne Trennstrich — daraus geht
nicht hervor, ob das eine umbrochene Beschriftung oder zwei eigenständige
sind. Das entscheidet sich am Foto.
