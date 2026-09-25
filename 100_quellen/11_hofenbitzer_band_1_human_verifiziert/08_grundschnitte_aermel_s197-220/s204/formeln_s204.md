# Formeln s204 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert` ([s204.md](s204.md)).
Kein einziger formel- oder coderelevanter Punkt ist bisher von Werner am
Original bestätigt. Diese Extraktion wurde auf ausdrücklichen Wunsch Werners
trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker übersprungen).

Zusätzlich gehört die Buchkategorie `08_grundschnitte_aermel_s197-220` nicht zu
den drei Kategorien (`03_grundschnitte_roecke_s32-48`,
`04_modelle_roecke_s49-105`, `07_grundschnitte_oberteile_s171-196`), für die
laut `AGENT.md` eine gesonderte Formelextraktion vorgeschrieben ist. Diese Datei
entsteht als Ausnahme auf Werners ausdrückliche Anweisung, nicht weil die
Kategorieliste in `AGENT.md` geändert wurde.

Grundlage sind [`ocr_s204.md`](ocr_s204.md), [`tabellen_s204.md`](tabellen_s204.md)
sowie eine eigene Bildsichtung von [`skizzen/s204_skizze_01.png`](skizzen/s204_skizze_01.png)
und [`skizzen/s204_skizze_02.png`](skizzen/s204_skizze_02.png). Die Bildsichtung
ersetzt keine Werner-Bestätigung, macht aber zeichnungsgebundene Werte direkt
nachvollziehbar (unten einzeln gekennzeichnet).

## 1. Konstruktionstabelle (tbl-0)

Quelle: [`tabellen_s204.md`](tabellen_s204.md), Zeilen 9–18 (OCR-Rohextrakt aus
`ocr_s204_raw.json`, Tabelle `tbl-0.md`).

```text
Konstruktionstabelle | Name | Größe 28
Maßangaben in cm Ärmel | Datum | Modell Schmaler Ärmel | Pb 3
AlH | [ärmischhöhe] | 17,2 | | | ärmischumfang | AlU | 41,2
Zugaben aus der Berechnungstabelle für Ärmelkonstruktionen
ÄL | Ärmellänge | 60 | ± 10 | Ärmellänge | ÄL | 60
OaU | Oberarmumfang | 28 | ± 2,5 | Oberarmweite | OaW | 30,5
HgU | Handgelenkumfang | 16 | ± 5 | Saumweite | SaW | 21
EW in % | Einhalteweite in % | 8 % | Einhalteweite in cm ≙ AlU ≙ Einhalteweite in % | | | EW in cm | 3,3 cm
| | | Ärmelkugelumfang ≙ AlU ≙ Einhalteweite in cm | | | ÄkU | 44,5
```

Hinweise:

- „Größe 28" laut OCR, s204.md-Prüfstelle 1 vermerkt einen vermuteten Lesefehler
  (Foto zeigt optisch „38"); unverändert aus OCR übernommen, nicht korrigiert.
- „Pb 3" unverändert aus OCR übernommen; s204.md vermutet „PK 3".
- Die Zeile zu „AlH"/„17,2" ist laut s204.md-Prüfstelle 1 auf dem Foto
  eigenständig als „AhH | Armlochhöhe | 17,2" zu lesen, mit einer zusätzlichen,
  in der OCR-Zeile fehlenden rechten Tabellenhälfte. Die hier zitierte
  OCR-Zeile enthält bereits ein „AlU | 41,2" am rechten Rand; ob das die
  fehlende Spalte ist oder eine eigene, im Foto getrennte Angabe, ist ungeklärt.
- „± 10" bei ÄL laut OCR; s204.md-Prüfstelle 1 vermerkt „± 0" auf dem Foto.
- Das Zeichen „≙" in den beiden Rechenzeilen ist ein OCR-Symbol für eine nicht
  eindeutig erkannte Verknüpfung (vermutlich „+" oder „="); unverändert
  übernommen.
- Nachrechnung (nicht Bestandteil der Buchfassung, siehe Abschnitt 4 der
  Normalisierung): 28 + 2,5 = 30,5; 16 + 5 = 21; 41,2 · 0,08 = 3,296 ≈ 3,3;
  41,2 + 3,3 = 44,5 — alle vier Werte passen zur Lesart „+".

## 2. Grundgerüst zeichnen – Ellenbogenlinie (60 % ÄL)

Quelle: [`ocr_s204.md`](ocr_s204.md), Zeile 23 (Schrittfließtext, Abschnitt „2.
Grundgerüst zeichnen"); zeichnungsgebunden zusätzlich in
[`skizzen/s204_skizze_02.png`](skizzen/s204_skizze_02.png) (❑3 „Grundgerüst",
Schrittmarke ②) bestätigt.

```text
60% der AL abtragen, Dort abwinkeln → Ellenbogenlinie.
```

Zeichnungsbeschriftung (eigene Bildsichtung, ❑3):

```text
60% ÄL
60 cm · 0,60 = 36 cm
```

Hinweis: OCR schreibt „AL", die Skizze und die durchgehende Kürzelkonvention der
Seite (s. s204.md, Anmerkungen) belegen „ÄL". Das Rechenbeispiel „60 cm · 0,60 =
36 cm" in der Zeichnung stimmt mit dem Tabellenwert ÄL = 60 überein.

## 3. Grundgerüst zeichnen – hintere Linie (½ OaW + Korrekturbetrag)

Quelle: [`ocr_s204.md`](ocr_s204.md), Zeile 24; zeichnungsgebunden zusätzlich in
[`skizzen/s204_skizze_02.png`](skizzen/s204_skizze_02.png) (❑3, Schrittmarke ①,
oben).

```text
Auf der Schulterlinie \(1/2\) OaW \(\times 0,5\) bis 0,7 abtragen ( \(\times
0,5\) bis 0,7 cm ist ein Korrekturbetrag) \(\rightarrow\) hintere Linie.
```

Zeichnungsbeschriftung (eigene Bildsichtung, ❑3):

```text
½ OaW + 0,5 bis 0,7
(hier 15,9)
```

Widerspruch: Der OCR-Fließtext schreibt „×" (Mal-Operator) vor „0,5 bis 0,7",
die Zeichnung zeigt sichtbar „+". Nachrechnung mit OaW = 30,5 (Tabelle,
Abschnitt 1): ½ · 30,5 = 15,25; 15,25 + 0,5 = 15,75; 15,25 + 0,7 = 15,95 — beide
Werte liegen nahe am Beispielwert „hier 15,9". Eine Multiplikation (15,25 × 0,5
= 7,625; 15,25 × 0,7 = 10,675) passt nicht zum Beispielwert. Dieser Abgleich
ersetzt keine Werner-Bestätigung des Fließtexts.

## 4. Grundgerüst zeichnen – Ärmelkugellinien-Kontrollbereich (AlH-Anteil)

Quelle: [`ocr_s204.md`](ocr_s204.md), Zeile 25; zeichnungsgebunden zusätzlich in
[`skizzen/s204_skizze_02.png`](skizzen/s204_skizze_02.png) (❑3, Schrittmarken
④–⑥).

```text
Auf der vorderen Linie die AlH abtragen. Von Dort \(1/2\) AlH nach oben messen
und ein weiteres Mal \(1/2\) AlH nach oben abtragen. Dies ist der Bereich der
optimalen Armelkugellinie.
```

Zeichnungsbeschriftung (eigene Bildsichtung, ❑3):

```text
AlH (hier 17,2 cm)
1/10 AlH (hier 1,7)
1/10 AlH = Kontrollbereich → Bereich der optimalen Ärmelkugellinien-Position
Ärmelkugellinie (ÄkLi)
```

Widerspruch (bereits in s204.md, Prüfstelle 2, vermerkt): Der OCR-Fließtext
schreibt zweimal „1/2 AlH", die Zeichnung beschriftet den Kontrollbereich
sichtbar mit „1/10 AlH" und dem Beispielwert „1,7". Nachrechnung: 17,2 : 10 =
1,72 ≈ 1,7 (passt zu „1/10"); 17,2 : 2 = 8,6 (passt nicht zum Beispielwert
„1,7"). Dieser Abgleich ersetzt keine Werner-Bestätigung des Fließtexts.

## 5. Grundgerüst zeichnen – Ärmelkugellinie auf der vorderen Linie

Quelle: [`ocr_s204.md`](ocr_s204.md), Zeile 26; zeichnungsgebunden zusätzlich in
[`skizzen/s204_skizze_02.png`](skizzen/s204_skizze_02.png) (❑3, oben rechts,
Schrittmarke ③).

```text
Rechts an der Schulterlinie auf die vordere Linie \(1/2\) AkU \(\sim 1\) cm
abtragen. Dort sollte die Armelkugellinie (AkLi) liegen. Mathematisch exakter
ware es, \(48\%\) AkU abzutragen.
```

Zeichnungsbeschriftung (eigene Bildsichtung, ❑3):

```text
½ ÄkU – 1 cm
exakter: 48% ÄkU = 44,5 cm · 0,48 = 21,4 cm
```

Hinweis: OCR „\(\sim 1\) cm" liest sich als „– 1 cm" (Zeichnung bestätigt den
Bindestrich/Minus). Nachrechnung mit ÄkU = 44,5 (Tabelle, Abschnitt 1): 44,5 ·
0,48 = 21,36 ≈ 21,4 (passt zum Zeichnungswert); ½ · 44,5 – 1 = 21,25 (nahe, aber
nicht identisch mit 21,4 – das ist die im Buch selbst benannte „exaktere"
Alternative, kein Widerspruch, sondern zwei nebeneinanderstehende Methoden).

## 6. Korrekturabschnitt – Armlochkontrolle (ArD)

Quelle: [`ocr_s204.md`](ocr_s204.md), Zeile 42 (dritter Punkt der
Korrektur-Reihenfolge).

```text
3. Armloch kontrollieren: ArD = OaU: 10 · 6 - 7,5 cm Das Armloch am
Oberteil-Grundschnitt ggf. verbreitern (ArD nach messen und berechnen sowie die
AlT am Körper nachmessen). Dann den AlU neu messen, den AkU neu berechnen und
die Diagonale am Ärmel neu abtragen → die AkLi wird tiefer.
```

Hinweis: Die Formel „ArD = OaU: 10 · 6 - 7,5 cm" ist in dieser Form nicht
eindeutig lesbar (Reihenfolge Doppelpunkt/Punkt ungewöhnlich, keine Klammern).
Keine eigene Bildsichtung möglich, da dieser Text nicht in einem der beiden
Skizzenausschnitte liegt, sondern im Fließtext. Unverändert aus OCR übernommen,
nicht stillschweigend berichtigt oder aufgelöst. „ArD" und „AlT" werden auf
dieser Seite sonst nicht definiert; vermutlich Querverweis auf eine
Berechnungsformel des Oberteil-Grundschnitts (nicht diese Seite, nicht
kopiert).

## Nicht als Formel erfasst

- Zeile 13 „□1 Konstruktionstabelle mit Hilfe der Berechnungstabelle auf Seite
  199 aufstellen": Verweis auf eine andere Seite, keine eigene Formel hier.
- Zeilen 17–18 „□2 Die Teilstrecken des Armloschumfangs wie skizziert
  ausmessen…" / „□1 In der Konstruktionstabelle die Ärmellänge, Oberarmweite,
  Ärmelsaumweite und die gewünschte Einhalteweite … bestimmen": Handlungsschritte
  ohne eigenen Rechenausdruck.
- Zeile 22 „Die AL senkrecht abtragen…": reine Linienbezeichnung ohne
  Rechenbeziehung (Bezugsgröße für Abschnitt 2).
- Zeile 28 „Die Achsellinie sollte im Kontrollbereich liegen (eine kleine
  Überschreitung der Grenzbereiche von wenigen Millimetern ist möglich).":
  qualitative Toleranzaussage ohne Zahlenwert.
- Zeile 30 „Liegt P5 Innerhalb des optimalen Bereichs, wird die ÄkLi
  abgewinkelt und aus P3 die hintere Linie abgewinkelt.": Konstruktionsschritt
  ohne eigenen Rechenausdruck.
- Zeilen 34–36 (drei Gründe für zu hohe ÄkLi): Fließtext ohne Zahlenwerte.
- Zeilen 40–41 (Korrekturschritte 1–2): enthalten „1/2 AkU – 1 cm" bzw.
  „Diagonale neu abtragen", jedoch als Wiederholung derselben Beziehung aus
  Abschnitt 5 im Korrekturkontext, hier nicht doppelt als eigene Formel
  geführt.
- Skizze `s204_skizze_01.png` (❑2 „Armloch eines taillierten
  Oberteil-Grundschnitt"): Maßangaben vAllU 14,4 cm, hAllU 13,8 cm, vAchsel
  4,5 cm, hAchsel 8,5 cm, me = 2,7 cm sind Bezugsmaße einer anderen
  Konstruktion (Oberteil-Armloch), auf s204 nicht in eine eigene
  Rechenbeziehung der Ärmelkonstruktion eingebunden; Kürzel „vAllU"/„hAllU"
  laut s204.md unsicher gelesen. Nicht als eigene Formel dieser Seite geführt,
  nur als Bezugsskizze vermerkt.
- Schrittmarken ①–⑦ (blaue Kreiszahlen in den Skizzen): reine
  Zuordnungsmarken zu Textschritten, keine Formeln.
- „2.0.0" (Zeile 50) und die Fragment-Zeilen 52–62: laut s204.md
  OCR-Fehllesung der Seitenzahl bzw. mitfotografierter Text der Nachbarseite
  205 – nicht Inhalt dieser Seite.
