# Entscheidungen vor dem Ausformen

Diese Datei hält die Antworten und Entscheidungen zur Liste
`C:\Users\Chromatic\Desktop\Was vor dem Ausformen geklärt sein.txt` fest.

Wir gehen die Punkte nacheinander durch. Eine Aussage gilt erst dann als entschieden,
wenn Werner sie ausdrücklich bestätigt hat. Vorschläge der KI sind keine Entscheidung.

## Arbeitsgrundsatz – entschieden

`200_funktionen` ist vor dem Coden zunächst eine begehbare Arbeitskarte durch das
Hofenbitzer-Buch. Die vielen kleinen Ordner teilen die große Menge unterschiedlicher
Prüfstellen in beherrschbare fachliche Einheiten. So kann eine Einheit vollständig
geklärt und danach abgeschlossen werden, ohne ungeklärte Stellen im Gesamtbestand zu
übersehen.

Ein Ordner bedeutet nicht automatisch, dass dafür eigener Python-Code entstehen muss.
Er hält zunächst sichtbar, dass die fachliche Einheit existiert und geprüft werden muss.
Erst nach der Klärung wird entschieden, ob sie:

- eigenen Python-Code benötigt,
- durch einen allgemeinen Geometriebaustein abgedeckt wird,
- ein dokumentierter manueller Konstruktionsschritt bleibt,
- nur Erklärung oder Kontrolle ist,
- oder keine eigenständige Funktion darstellt.

## Status

- **offen** – noch nicht besprochen oder entschieden
- **in Klärung** – besprochen, aber noch nicht entschieden
- **entschieden** – von Werner bestätigt
- **am Buch prüfen** – Entscheidung benötigt zuerst das gedruckte Buch
- **erledigt** – vereinbarte Arbeit wurde geprüft abgeschlossen
- **geparkt** – bewusst nicht im aktuellen Arbeitsabschnitt
- **verschoben** – aus dieser Liste heraus, wird an anderer Stelle weitergeführt

---

# A – Entscheidungen zur Arbeits- und Ordnerordnung

## 01 – Sprache zentral oder im Schritt?

**Status:** entschieden

**Entscheidung:**

`000_sprache` bleibt die maßgebliche Sprach-SSOT. In `200_funktionen`
werden nur die für den jeweiligen Arbeitsschritt relevanten Sprachelemente
mit Verweisen und lokalen offenen Fragen aufgeführt. Definitionen werden dort
nicht dupliziert.

**Begründung und Folge für das Repo:**

Die Begriffe, Symbole und Abkürzungen bleiben zentral gepflegt und können dadurch
nicht zwischen mehreren Funktionsordnern auseinanderlaufen. Ein Arbeitsschritt
bleibt trotzdem verständlich, weil er seine benötigten Sprachelemente und deren
zentrale Fundstellen nennt. Bis die weitere Ordnerordnung entschieden ist, wird
in `200_funktionen` noch nichts geändert.

## 02 – Was wird aus Schritten ohne Formel?

**Status:** entschieden

**Entscheidung:**

Schritte ohne Formel bleiben in der Arbeitskarte sichtbar. Für sie wird weder
eine Formel erfunden noch automatisch eigener Python-Code vorgesehen. Nach der
fachlichen Klärung werden sie als manueller Konstruktionsschritt, allgemeiner
Geometriebaustein, Erklärung oder Kontrolle beziehungsweise als keine
eigenständige Funktion eingeordnet.

**Begründung und Folge für das Repo:**

Auch ein Schritt ohne Formel kann für die vollständige Konstruktion oder deren
Prüfung notwendig sein. Seine sichtbare Einordnung verhindert Lücken, ohne aus
jedem Buchschritt künstlich eine programmierte Funktion zu machen. Bis zur
fachlichen Klärung bleibt der zugehörige Ordner als Teil der Arbeitskarte
erhalten.

## 03 – Startpunkt: Kapitel 02 oder 03?

**Status:** entschieden

**Entscheidung:**

Die Arbeit beginnt mit Kapitel 02, `Grundschnitte Röcke`, Seiten 32–39.
Kapitel 03 folgt anschließend als Anwendung und Veränderung des erarbeiteten
Rock-Grundschnitts.

**Begründung und Folge für das Repo:**

Kapitel 02 ist der kleinere und fachlich vorgelagerte Abschnitt. An ihm kann der
vollständige Arbeitsablauf erstmals überschaubar erprobt werden. Die Modelle in
Kapitel 03 benötigen einen Ausgangs- beziehungsweise Grundschnitt und bauen daher
sinnvoll auf Kapitel 02 auf. Die erste vollständige Bearbeitung in
`200_funktionen` richtet sich somit auf Kapitel 02; Kapitel 03 wartet bis dahin.

## 04 – Wie sieht ein fertiger Schritt-Ordner aus?

**Status:** entschieden

**Entscheidung:**

Ein Schritt-Ordner ist die kleinste Arbeitsebene in `200_funktionen` und steht
für eine konkrete Tätigkeit oder Prüfung aus dem Buch. Er gilt als fachlich
fertig, wenn der Schritt vollständig verstanden, belegt und eingeordnet ist.
Eigener Python-Code ist dafür nicht zwingend erforderlich.

**Pflichtbestandteile:**

- Zweck des Arbeitsschritts
- genaue Buchseiten und Bildnummern
- relevante Prüfstellen und ihr Stand
- Verweise auf benötigte Begriffe, Symbole und Abkürzungen in `000_sprache`
- Verweise auf vorhandene Formeln und benötigte Mathematik
- Einordnung nach Entscheidung 02: eigener Code, allgemeiner Geometriebaustein,
  manueller Schritt, Erklärung oder Kontrolle beziehungsweise keine eigene Funktion
- offene Fragen oder die ausdrückliche Feststellung, dass keine offen sind
- fachlicher Abschlussstatus

**Optionale Bestandteile:**

- Python-Code
- Tests
- erzeugte Schnittgrafiken oder andere Prüfergebnisse

## 05 – Bildverweise auf die Bildnummer verfeinern

**Status:** entschieden

**Entscheidung:**

Jeder Bildverweis nennt die Buchseite, die gedruckte Bildnummer, das zugehörige
Originalfoto sowie den technischen und fachlichen Prüfstatus. Fehlt eine
Bildnummer oder ist sie nicht eindeutig lesbar, wird der Verweis als
`am Buch prüfen` markiert. Eine Bildnummer wird niemals geraten.

**Folge für das Repo:**

Bestehende und neue Bildverweise werden bei ihrer fachlichen Bearbeitung um die
gedruckte Bildnummer ergänzt. Die Originalbilder bleiben unverändert in
`100_quellen`; `200_funktionen` enthält nur eindeutige Verweise und den jeweiligen
Prüfstatus.

## 06 – Bildverweise auf die Schritt-Ebene verschieben

**Status:** entschieden

**Entscheidung:**

Der genaue Bildverweis wird dem jeweiligen Schritt-Ordner zugeordnet. Zeigt ein
Bild mehrere Vorgänge, darf es in mehreren Schritt-Ordnern verlinkt werden. Das
Originalbild bleibt dabei einmalig in `100_quellen`; in `200_funktionen` werden
keine Bildkopien angelegt.

**Folge für das Repo:**

Bestehende Bildverweise auf der Ebene einer größeren Funktionsgruppe werden bei
der fachlichen Bearbeitung auf die zugehörigen Schritt-Ordner verteilt. Eine
übergeordnete Bildliste darf nur als Übersicht dienen und wird nicht zu einer
zweiten inhaltlichen SSOT. Bis zur späteren Umsetzung wird in `200_funktionen`
nichts verschoben oder gelöscht.

## 07 – Bleiben Gruppen zweistufig?

**Status:** entschieden

**Entscheidung:**

Funktionsgruppen dürfen zweistufig bleiben, wenn das Buch dort keine sinnvoll
trennbaren Arbeitsschritte enthält. Die Funktionsgruppe ist dann selbst die
kleinste Arbeitseinheit. Unterordner werden nicht allein für eine einheitliche
Optik angelegt.

**Begründung und Ausnahmen:**

Die im Ausgangspunkt genannte Zahl 62 ist überholt. Im aktuellen Bestand wurden
43 Funktionsgruppen ohne darunterliegende Schritt-Ebene gefunden. Ob diese
Gruppen jeweils berechtigt zweistufig sind, wird bei der fachlichen Bearbeitung
anhand des Buches geprüft. Enthält eine Gruppe mehrere unterscheidbare Tätigkeiten
oder Prüfungen, erhält sie eine Schritt-Ebene; andernfalls bleibt sie zweistufig.

## 08 – Kapitel 01 Grundlagen ohne Schrittebene – Absicht?

**Status:** entschieden

**Entscheidung:**

Kapitel 01, Grundlagen auf den Seiten 8–31, erhält keine künstliche Kapitel- und
Schrittstruktur in `200_funktionen`. Es bleibt als zentrale Grundlage außerhalb
der funktionalen Arbeitskarte. Benötigte Regeln werden aus den jeweiligen
Schritt-Ordnern eindeutig auf ihre zentrale Fundstelle zurückverwiesen.

**Begründung und Folge für das Repo:**

Kapitel 01 beschreibt überwiegend querschnittliche Grundlagen wie Maßnehmen,
Maßtabellen und allgemeine Konstruktionsstandards, nicht eine zusammenhängende
Schnittkonstruktion. Die 46 Quelldateien bleiben in `100_quellen`; die neun
vorbereiteten Themenbereiche in `000_sprache/30_grundlagen_s8-31` werden später
fachlich eingeordnet. Enthaltene Formeln und Messregeln müssen dennoch einzeln
geprüft und ihrem richtigen zentralen Bereich zugeordnet werden.

---

# B – Am gedruckten Buch zu klären

## 09 – S. 79, Arbeitsschritt 6: fehlendes Wort

**Status:** erledigt

**Befund und Entscheidung:**

Werner hat den gedruckten Arbeitsschritt geprüft und bestätigt:
„An den Formbundteilen die Teilweite reduzieren.“ Das zuvor als `UNLESBAR`
markierte Wort lautet eindeutig `Teilweite`. Die aktive Transkription und der
aktive Prüfstellen-Zusammenzug werden entsprechend berichtigt; Archivfassungen
bleiben als historische Belege unverändert.

## 10 – S. 274 und S. 276: Schritt 1 fehlt

**Status:** erledigt

**Befund und Entscheidung:**

Werner hat im gedruckten Buch auf beiden Seiten bestätigt: Vor der ersten
Anweisung stehen die beiden Markierungen ① und ④. Die Anweisung zur Bestimmung
der Schnittpunkte an VT und RT gilt gemeinsam für die Arbeitspunkte 1 und 4;
danach folgt Arbeitspunkt 2. Schritt 1 fehlt somit weder auf Seite 274 noch auf
Seite 276. Die Schreibweise `1+4` in den aktiven Transkriptionen bildet diese
gemeinsame Anweisung ab.

## 11 – S. 416: Nummern springen

**Status:** erledigt

**Befund und Entscheidung:**

Werner hat die gedruckte Seite geprüft und bestätigt: Die Ziffern 1 bis 8 auf
S. 416 sind Messpunkte am Körper, keine Arbeitsschritte. Die Zeilen „3./4.“ und
„6./7.“ stehen im Buch tatsächlich zusammengefasst; die Transkription gibt das
richtig wieder. Auch die Angabe „an fünf Stellen“ steht so im Buch: gemessen
werden die fünf Körpervertiefungen 1 bis 5, während 6 und 7 Standardbeträge sind
und 8 das Rückteil betrifft. Die Zählung springt somit nicht, und es fehlen keine
Punkte im Transkript.

**Folge für das Repo:**

An `s416.md` wird nichts geändert. Der Ordner
`200_funktionen/10_ausschnitte_s370-437/20_naht_und_ausschnitt_optimierung_an_der_brust_s416`
erhält keine Schrittebene und bleibt nach Entscheidung 07 zweistufig. Die Ziffern
werden bei der fachlichen Bearbeitung als Messpositionen geführt, so wie in den
Kapiteln 04, 06 und 07.

## 12 – S. 122: zwei Zählungen durcheinander

**Status:** erledigt

**Befund und Entscheidung:**

Werner hat die gedruckte Seite geprüft und vier Punkte bestätigt:

1. Die ersten beiden Ziffern 1. und 2. sind die **zwei Methoden** der
   Taillenvertiefung, also eine Vorbemerkung, und keine Arbeitsanweisung.
2. Die zweite Zählung läuft im Druck **durchgehend von 1 bis 7**. Sie wird nur
   durch die Absätze zu 1/1, 3/4, 2/3, 3/5 und 1/2 sowie durch die
   Bildunterschriften zu □1 und □2 unterbrochen.
3. Die Ziffern 1 bis 7 sind hier **Arbeitsschritte**, nicht Punktnummern. S. 122
   ist damit eine bestätigte Ausnahme von der sonst für Kapitel 04 geltenden
   Lesart. Die in der Bildunterschrift zu □3 genannten Punktnummern 6 und 7
   bleiben davon unberührt.
4. Der Bildverweis in Schritt 4 lautet im Buch **□2**, nicht □1.

**Folge für das Repo:**

Die aktive Transkription `s122.md` wird in Schritt 4 von □1 auf □2 berichtigt
und erhält den Vermerk der physischen Buchprüfung; Archivfassungen bleiben als
historische Belege unverändert. Weil auf S. 122 echte Arbeitsschritte vorliegen,
erhält `200_funktionen/04_grundschnitte_hosen_s106-137/04_taillenvertiefung_huefthose_s120-122`
bei der fachlichen Bearbeitung nach Entscheidung 07 eine Schrittebene. Die zwei
Methoden aus der Vorbemerkung werden dabei nicht als Schritte geführt.

## 13 – S. 171: Ziffern sind vermutlich Varianten, keine Schritte

**Status:** erledigt

**Befund und Entscheidung:**

Werner hat die gedruckte Seite geprüft und bestätigt:

1. Die Ziffern 1 bis 5 sind **fünf Tunnelzug-Varianten** zur Auswahl und keine
   Arbeitsschritte. Zusätzlicher Befund: unter der Aufzählung steht eine
   Zeichnung, die die zugehörigen Arbeitsschritte skizziert. Diese Zeichnung
   wird bei der fachlichen Bearbeitung ausgewertet.
2. Die beiden Ordner
   `200_funktionen/05_modelle_hosen_s138-170/18_sarouelhose_haremshose_pluderhose_s170`
   und `200_funktionen/06_grundschnitte_oberteile_s171-196/01_sarouelhose_fortsetzung_s171`
   **bleiben vorerst leer**. Es wird jetzt nichts angelegt.
3. Die fünf Tunnelzug-Querschnitte gehören zur **Bildnummer □6**, der großen
   Skizze unten rechts, dort fast ganz rechts.
4. `sindvielfältig` ohne Leerzeichen und `Schitt` statt `Schritt` sind
   **Druckfehler im Buch**. Die fototreue Übernahme bleibt richtig.

**Folge für das Repo:**

In `s171.md` wird die Zuordnung der Tunnelzug-Querschnitte zu □6 sowie die
Bestätigung der beiden Druckfehler als Prüfvermerk ergänzt. Der wörtliche
Buchtext bleibt unverändert. Die beiden Funktionsordner bleiben leer; ihre
Einordnung nach Entscheidung 02 erfolgt erst bei der fachlichen Bearbeitung.

## 14 – Zehn Kapitel-Prüfstellen, 605 Zeilen

**Status:** entschieden

**Bestand am 2026-09-06:**

Die zehn einzelnen Kapiteldateien sind ins Archiv gewandert und liegen dort als
historischer Beleg unter
`100_quellen/30_hofenbitzer_band_1_archiv/prüfstellen text/` mit zusammen 605
Zeilen. Die aktive Fassung ist
`100_quellen/10_hofenbitzer_band_1_digital/prüfstelle_text_zusammenzug/00_pruefstellen_text_band_1_zusammenzug.md`
mit 15 Kapitelabschnitten (00 bis 14) und 127 Einträgen: 93 A (vermuteter
Buchfehler), 12 B (unlesbar), 1 C (dateiübergreifender Konflikt) und 21 N (aus
den Transkripten nachgetragen). Vor der Sitzung vom 2026-09-06 waren vier
Einträge aufgelöst: A1, B1, N1 und A32.

**Entscheidung:**

1. Der Zusammenzug ist ab jetzt die **maßgebliche Fassung, die SSOT für
   Text-Prüfstellen**. Eine zweite Fassung wird nicht wieder angelegt.

   **Berichtigung vom 2026-09-06, nach dem Befund zu Punkt 20:** Diese Aussage
   war zu weit gefasst. Der Zusammenzug ist die SSOT für die Prüfstellen, die er
   **enthält** — er ist aber nicht der vollständige Bestand. Beim Lesen der
   archivierten README-Stände kam heraus, dass er nur die Prüfstellen der
   **ersten** digitalen Zweitprüfung führt. Die 24 späteren Nachprüfungsrunden
   sind nie eingeflossen: 354 A-Punkte, 3 B-Punkte, 2 C-Punkte und die gesamte
   Kategorie D mit 509 Punkten fehlen. Der Zusammenzug kennt 127 von rund 995
   Prüfstellen.

   Die Kategorie D ist inzwischen übernommen, siehe Punkt 20. Die fehlenden A-,
   B- und C-Punkte sind noch nachzurechnen und einzuordnen; erst danach ist der
   Satz „der Zusammenzug ist die SSOT" wieder uneingeschränkt richtig.

   **Fortschreibung vom 2026-09-06 – der Bestand ist vollständig, die SSOT ist
   dreiteilig.** Die A-, B- und C-Punkte sind nachgerechnet, siehe Punkt 20.
   Werner hat entschieden, sie als eigene Datei danebenzulegen statt sie
   einzusortieren. Die maßgebliche Fassung der Text-Prüfstellen besteht damit
   aus **drei Dateien** im Ordner `prüfstelle_text_zusammenzug`:

   | Datei | Inhalt | Punkte | Richtung |
   |---|---|---:|---|
   | `00_pruefstellen_text_band_1_zusammenzug.md` | erste Zweitprüfung, A/B/C/N | 127 | Buch prüfen |
   | `01_abweichungen_transkript_vom_foto.md` | Kategorie D aus 24 Nachprüfungen | 509 | Datei berichtigen |
   | `02_buchfehler_aus_dem_archiv.md` | A/B/C aus 24 Nachprüfungen | 366 | Buch prüfen |

   Zusammen 1.002 Einträge unter 995 Nummern; die Differenz sind die sieben
   doppelt vergebenen A-Nummern A330 bis A336. Damit ist nachgewiesen, dass aus
   dem archivierten Prüfstand nichts mehr aussteht. Keine der drei Dateien ist
   für sich allein die SSOT — bei der Arbeit an einer Buchseite sind alle drei
   heranzuziehen.
2. Die toten Verweise auf den Ordner `prüfstellen text` werden **entfernt**.
   Betroffen waren der Kopftext, ein Hinweis im Vorspann-Abschnitt und zehn
   `Quelle:`-Zeilen. Sie zeigten ins Leere, weil der Ordner beim Umräumen ins
   Archiv verschoben wurde. An ihrer Stelle steht jetzt der Herkunftsvermerk auf
   die frühere Kategoriedatei ohne Verlinkung.

   **Vollständigkeit nachgewiesen:** Die zehn Archivdateien enthalten 115
   Einträge. Alle 115 stehen im Zusammenzug. Dazu kommen dort zwölf spätere
   Ergänzungen: A90 bis A93, die vier zusätzlich gefundenen Prüfstellen, sowie
   N14 bis N21 aus dem Vorspann. 115 plus 12 ergibt die 127 Einträge. Es ist
   nichts verloren gegangen.
3. Die offenen Punkte werden **arbeitsbegleitend** abgearbeitet, also jeweils die
   Punkte des Kapitels, das gerade in `200_funktionen` ausgeformt wird. Sie werden
   nicht vorab am Stück durchgegangen. Das passt zu Entscheidung 03: für
   Kapitel 02, Grundschnitte Röcke, enthält der Zusammenzug **keinen einzigen
   Eintrag**; der Start ist damit nicht durch Prüfstellen blockiert.

   **Präzisierung durch Werner am 2026-09-06 – seitenweise, nicht kreuz und quer:**
   Alles, was zu **einer Buchseite** aufgekommen ist, wird gemeinsam vorgelegt und
   gemeinsam entschieden, solange das Buch auf dieser Seite aufgeschlagen ist.
   Werner blättert nicht für einzelne Punkte vor und zurück. Der Grund ist
   fachlich: nur mit der ganzen Seite vor Augen entsteht der Zusammenhang, aus dem
   heraus er überhaupt entscheiden, gewichten und Vorrang vergeben kann. Aus
   einzelnen aus dem Zusammenhang gerissenen Punkten entsteht das nicht.

   Daraus folgt für die Vorbereitung: Die Prüfstellen werden Werner **nach Buchseite
   gebündelt** vorgelegt, quer über Text- und Formel-Prüfstellen hinweg, und nicht
   in der Reihenfolge, in der sie in den Listen stehen.

   Ebenso gilt: **vor dem Python** wird geprüft, was aufgekommen ist. Erst wenn eine
   Seite beziehungsweise ein Arbeitsschritt geklärt und definiert ist, wird dafür
   gecodet.

4. Die A-Punkte werden **nicht** in „nur Schreibfehler" und „Formelfehler"
   getrennt. Werner hat entschieden, diese Unterscheidung vorerst nicht
   einzuführen. Alle A-Punkte bleiben gleichrangig in einer Liste.

**Am 2026-09-06 zusätzlich aufgelöst:**

Werner hat vier weitere A-Punkte als Druckfehler im Buch bestätigt. Sie sind im
Zusammenzug als erledigt gekennzeichnet; die fototreuen Übernahmen in den
Transkriptionen bleiben unverändert.

- **A7** — S.89, Bildunterschrift ☐5: `Produktionsssschnitt` mit drei „s"
- **A12** — S.102, Einleitungstext: `mit mit` doppelt
- **A13** — S.103, Bildunterschrift □6: `Poduktionsschnitt` ohne „r"
- **A37** — S.207, S.208 und S.211: `Oberamweite` ohne „r", vier Vorkommen

Zusammen mit A14 und A15 aus Entscheidung 13 und den sieben Vorspann-Punkten aus
Entscheidung 17 sind damit **17 der 127 Einträge aufgelöst, 110 bleiben offen**.
Ein weiterer Punkt, N20, steht als in Klärung.

## 16 – S. 7 ist nicht eigenständig transkribiert

**Status:** erledigt

**Befund:**

Überholt. Mit Commit `d628afa` vom 2026-09-06 ist S. 7 eigenständig als
`100_quellen/10_hofenbitzer_band_1_digital/00_vorspann_s1-7/s7.md` transkribiert,
162 Zeilen, Quelle `s07.jpg`. Die Datei enthält das Inhaltsverzeichnis für
Modelle Kleider/Blusen/Weste, Modelle Jacken, Sportswear/Wäsche/Unisex sowie
Anhang und Sachwortverzeichnis, dazu die Zeichenschablonen-Abbildung.

## 17 – S. 4–6 fehlen in der aktiven digitalen Fassung

**Status:** erledigt

**Befund:**

Ebenfalls überholt. Derselbe Commit hat S. 4, S. 5 und S. 6 eigenständig
transkribiert. Der Ordner `00_vorspann_s1-7` enthält damit lückenlos `s1.md` bis
`s7.md`.

**Offen geblieben ist nur der Inhalt:**

Beim Transkribieren sind acht Prüfstellen angefallen, N14 bis N21 im
Text-Zusammenzug. Alle betreffen **gedruckte Seitenverweise im
Inhaltsverzeichnis**, die nicht zur tatsächlichen Buchseite passen. Die
Transkription ist an jeder Stelle fototreu.

**Am 2026-09-06 seitenweise vorgelegt und geklärt:**

- **S. 5 – N14 bis N19, alle sechs aufgelöst.** Werner hat bestätigt, dass die
  Seitenzahlen so gedruckt sind. Es sind Druckfehler im Buch: die fehlende Zahl
  bei „Weite an erprobtem Oberteil-Grundschnitt reduzieren", die drei um 10 zu
  hohen Zahlen 236/238/239 statt 226/228/229, die 256 statt 246/247 und die
  dreifache 250 statt 250/251/252.
- **S. 6 – N20 bleibt in Klärung.** Werner vermutet, dass sich die
  Kragen-Modellnummern 35-38 und 38-39 absichtlich überschneiden, weil die
  zugehörige Abbildung dieselbe Stelle für beide Systeme zeigt. Er will das nicht
  festlegen, solange er im Kragen-Thema nicht tiefer drin ist. Der Punkt wird bei
  der Bearbeitung von Kapitel 09, S. 290–369, endgültig entschieden.
- **S. 7 – N21 aufgelöst.** Die 450 steht so im Buch und ist ein Druckfehler; das
  Jacken-Kapitel läuft von S. 465 bis S. 492.

An den Transkriptionen ändert sich nichts, sie bleiben fototreu.

---

# C – Quellenordnung

## 18 – Drei Index-Dateien liegen doppelt

**Status:** entschieden

**Grundsatzentscheidung – der Archivordner ist Geschichte:**

`100_quellen/30_hofenbitzer_band_1_archiv` enthält **historische Belege**. Der
Ordner wird nicht mehr bearbeitet: keine Dubletten auflösen, keine Dateinamen
richtigstellen, keine toten Verweise reparieren. Er bleibt so liegen, wie er ist.
Diese Festlegung gilt für den gesamten Archivordner und damit auch für alle
weiteren Listenpunkte, die dort etwas beanstanden.

**Befund am 2026-09-06 – zur Einordnung, ohne Handlungsbedarf:**

Der Ausgangsbefund ist überholt. Doppelt liegt nur **eine** Datei, und die beiden
Fassungen sind nicht byte-identisch:
`00_index_normalisierte_formeln_band_1_v1.md` (719 Zeilen, 68 Links, alle tot)
und `00_ind1ex_normalisierte_formeln_band_1_v1.md` (719 Zeilen, keine Links).
Inhaltlich sind sie gleich; der Dateiname der zweiten hat eine `1` mitten im Wort
„index", wie auch `READM1E.md` im selben Ordner. Von v2 und v3 gibt es je nur eine
Fassung.

Nicht doppelt sind die vier gleichnamigen `00_index_formeln_band_1.md`. Es sind
vier eigenständige Indizes in vier Ordnern: die digitale Formelsammlung mit 542
Zeilen sowie die drei geprüften Bestände v1, v2 und v3 mit 194, 129 und 137
Zeilen. Sie gehören zu Punkt 19 und dürfen nicht als Dubletten behandelt werden.

**Entscheidung:** Es wird nichts gelöscht, nichts umbenannt und nichts repariert.

## 19 – v1, v2 und v3 zu einer vollständigen Liste zusammenführen

**Status:** erledigt

**Befund am 2026-09-06 – die Zusammenführung ist bereits geschehen:**

Die Warnung der Ausgangsliste war berechtigt und ist zugleich schon eingelöst.
Das Umräumen hat v1, v2 und v3 vollständig in den aktiven Bestand überführt.

| Bestand | Seiten |
|---|---|
| Archiv v1 | 68 |
| Archiv v2 | 47 |
| Archiv v3 | 73 |
| zusammen | 188 |
| aktiv in `100_quellen/10_hofenbitzer_band_1_digital` | 188 |

- Die Überschneidung zwischen v1, v2 und v3 beträgt **null**. Es sind tatsächlich
  verschiedene Buchseiten und keine Versionen derselben Sache.
- Seiten, die **nur** im Archiv stehen: keine.
- Seiten, die **nur** aktiv stehen: keine.

**Der Inhalt ist unversehrt:**

Alle 188 Paare wurden verglichen. Die Zeilenzahl stimmt bei jedem einzelnen Paar
überein, ohne eine Ausnahme. Die inhaltlichen Unterschiede sind ausschließlich
angepasste Dateinamen-Verweise aus der Umbenennung, zum Beispiel
`formeln_s171_digital_geprüft.md` zu `formeln_s171.md` und
`formeln_s235_codex_v2_digital_geprueft.md` zu `formeln_s235.md`. Es fehlt keine
Formel, keine Zeile und kein Prüfvermerk.

**Entscheidung:**

Es wird nichts zusammengeführt, weil nichts mehr zusammenzuführen ist. Der aktive
Ordner ist die vollständige Liste. Das Archiv bleibt nach Entscheidung 18 als
historischer Beleg unangetastet.

**Nebenbefund für Punkt 22:**

Aktiv liegen 425 rohe Formeldateien, davon sind 188 normalisiert. Offen bleiben
damit 237 Seiten.

## 20 – Zwei README-Stände mit demselben Datum

**Status:** erledigt – Kategorie D sowie A, B und C übernommen

**Befund am 2026-09-06 – es sind keine zwei Stände:**

Die beiden Dateien liegen in
`100_quellen/30_hofenbitzer_band_1_archiv/prüfstellen text/`. Sie sind nicht
dieselbe Sache in zwei Fassungen, sondern eine Prüfung und ihre Fortschreibung.

| Datei | Zeilen | Inhalt |
|---|---|---|
| `README_stand_2026-08-30.md` | 436 | erste digitale Zweitprüfung: 89 A, 13 B, 2 C |
| `README_stand_2026-08-30_v2.md` | 6255 | dieselbe Prüfung plus 24 weitere Nachprüfungsrunden: 447 A, 15 B, 3 C und **509 D** |

Der kleine Stand deckt sich fast genau mit dem Text-Zusammenzug, 89 gegenüber 93
A-Punkten. Der Zusammenzug stammt also aus dieser ersten Runde. Aus dem großen
Stand fehlen im Zusammenzug **354 A-Punkte, 3 B-Punkte, 2 C-Punkte und alle 509
D-Punkte**.

**Die Kategorie D ist eine eigene Sorte Prüfstelle:**

Wörtlich aus dem Prüfstand: „Abweichungen der v3-Transkription vom Foto — im
Digitalisat zu korrigieren. Zu korrigieren ist hier nicht das Buch, sondern die
Seitendatei." Bei A prüft Werner das Buch. Bei D ist das Buch in Ordnung und
**unsere eigene Transkription ist falsch**.

**Entscheidung und erledigte Arbeit:**

Der Archivgrundsatz aus Entscheidung 18 gilt hier **nicht**. Bei den
Index-Dateien war der Inhalt nachweislich in den aktiven Bestand übergegangen,
hier nachweislich nicht. Die 509 D-Punkte wurden deshalb aus dem Archiv in den
aktiven Bestand übernommen, nach Buchseite sortiert, als
`100_quellen/10_hofenbitzer_band_1_digital/prüfstelle_text_zusammenzug/01_abweichungen_transkript_vom_foto.md`.

Ergebnis des maschinellen Abgleichs gegen die heutigen Seitendateien:

| Urteil | Anzahl |
|---|---|
| nachweislich noch offen | 297 |
| maschinell als behoben eingestuft | 29 |
| unklar, Beleg zu dünn | 57 |
| nicht maschinell prüfbar | 126 |
| gesamt | 509 |

Die 29 „behoben" sind unzuverlässig. Eine Handprobe an D118 zeigte eine
Fehleinstufung, und in der gesamten Git-Historie gibt es **keinen Commit, der
je eine D-Berichtigung angewendet hätte**. Praktisch ist von allen 509 Punkten
als offen auszugehen.

Verteilung über die Kapitel:

| Kapitel | Punkte | davon offen | Seiten |
|---|---:|---:|---:|
| 04 Grundschnitte Hosen | 17 | 7 | 10 |
| 05 Modelle Hosen | 87 | 49 | 24 |
| 09 Kragen, Kapuzen und Taschen | 204 | 123 | 55 |
| 12 Modelle Jacken | 57 | 29 | 16 |
| 13 Sportswear, Wäsche, Unisex | 135 | 89 | 42 |

Die Kapitel 02 und 03, mit denen die Arbeit nach Entscheidung 03 beginnt, sind
vollständig frei von D-Punkten. Der Start ist also nicht blockiert.

**Die A-, B- und C-Punkte, nachgerechnet am 2026-09-06:**

Die 354 fehlenden A-Punkte sowie B10, B14, B15, C2 und C3 wurden nach derselben
Methode nachgerechnet wie die D-Punkte. Werner hat entschieden, sie **nicht** in
den Zusammenzug einzusortieren, sondern als eigene Datei danebenzulegen:
`100_quellen/10_hofenbitzer_band_1_digital/prüfstelle_text_zusammenzug/02_buchfehler_aus_dem_archiv.md`,
nach Buchseite gebündelt.

359 Nummern in 366 Einträgen. Ergebnis des maschinellen Abgleichs gegen die
heutigen Seitendateien:

| Urteil | Anzahl |
|---|---:|
| steht unverändert in der Seitendatei | 146 |
| teilweise wiedergefunden | 95 |
| im Digitalisat geglättet | 54 |
| teils geglättet | 9 |
| Digitalisat weicht ab | 38 |
| maschinell nicht prüfbar | 24 |
| gesamt | 366 |

Verteilung über die Kapitel:

| Kapitel | Punkte | Seiten |
|---|---:|---:|
| 04 Grundschnitte Hosen | 18 | 7 |
| 05 Modelle Hosen | 67 | 24 |
| 09 Kragen, Kapuzen und Taschen | 133 | 51 |
| 12 Modelle Jacken | 41 | 16 |
| 13 Sportswear, Wäsche, Unisex | 105 | 40 |

Wie bei den D-Punkten sind die Kapitel 02 und 03 frei. Der Start bleibt
unblockiert.

**Drei Befunde aus dem Nachrechnen:**

1. **101 Punkte stehen nicht mehr so in der Datei** — 54 geglättet, 9 teils
   geglättet, 38 im Wortlaut abweichend. Der Prüfstand führt sie als fototreu
   übernommen; das trifft heute nicht mehr zu. Handproben: S.506 „jenach" steht
   als „je nach", S.168 „Hüftlinie,wie" als „Hüftlinie, wie", S.309 „Halsoch"
   als „Halsloch", S.517 „Hälte" als „Hälfte", S.341 „Reversragen" als
   „Reverskragen". Werner hat entschieden, diese Punkte **mitzuführen und zu
   kennzeichnen**, nicht auszulagern. Ob an diesen Stellen am Buch geprüft oder
   die Seitendatei fototreu berichtigt wird, ist bei der Kapitelarbeit zu
   entscheiden. Sachlich berühren sie Kategorie D.

2. **A330 bis A336 sind im Prüfstand doppelt vergeben** — im 15. Durchgang für
   S.487–S.491, im 16. für S.341–S.346. Sieben Nummern, vierzehn verschiedene
   Punkte. Werner hat entschieden: beide behalten ihre Nummer, dahinter steht in
   Klammern der Durchgang. Neue Nummern werden nicht vergeben, damit die
   Rückverfolgung zum Prüfstand eindeutig bleibt.

3. **C3 und N20 sind derselbe Fall** — die doppelt vergebene Modellnummer 38 auf
   S.304 und S.305. N20 steht im Zusammenzug seit dem 2026-09-06 als in Klärung
   und ist der Bearbeitung von Kapitel 09 zugewiesen. Der aktive Bestand führt
   die 38 weiterhin doppelt. Beide sind zusammen zu entscheiden.

**Von Hand geprüft, weil maschinell nicht zu fassen:**

- **B10 ist offen.** Das Kürzel für Einlage steht als `EI` (großes i) statt `El`
  an 18 Stellen in sieben aktiven Seitendateien: `s118.md`, `s144.md`, `s147.md`,
  `s149.md`, `s160.md`, `s163.md`, `s169.md` — alle in den Kapiteln 04 und 05.
  In den übrigen Kapiteln steht durchgehend das richtige `El`. Das ist mehr, als
  der Prüfstand meldete; dort waren nur `s147.md` und `s149.md` benannt.
- **B14** — S.309: „üb" ist inzwischen erfasst, „me" fehlt weiterhin. Am Buch
  beziehungsweise an der Abkürzungsseite S.31 zu klären.
- **B15** — S.325: Die rote Zahl am vorderen Kragensteg ist für □1 weiterhin
  nicht geführt. Am Buch nachzulesen.
- **C2** — betrifft allein den Altbestand und ist dort erledigt.

## 21 – 257 offene Fragen in normalisierten Formeln

**Status:** verschoben – aus dieser Liste heraus, siehe unten

**Bestand am 2026-09-06:**

Die offenen Fragen aus den normalisierten Formeldateien wurden zusammengezogen
und nach Buchseite gebündelt als
`100_quellen/10_hofenbitzer_band_1_digital/prüfstelle_formel_zusammenzug/01_offene_fragen_normalisierte_formeln.md`.

541 Formeln aus 183 Dateien führen die Zeile „Offene Fragen oder Widersprüche".
Davon 243 zu klären, 65 Anmerkung, 233 geklärt. Die Zahl 257 aus der Überschrift
ist nicht nachvollziehbar; sie wäre bei Gelegenheit zu berichtigen.

**Entscheidung von Werner am 2026-09-06 – verschoben:**

Der Punkt ist **aus dieser Liste heraus**. Er liegt jetzt im Ordner
`prüfstelle_formel_zusammenzug`, in dem ohnehin noch weitere Dinge zu
verifizieren sind. Dort wird er zusammen mit ihnen abgearbeitet, nicht mehr als
eigener Vorab-Punkt.

Die Vorab-Klärung ist damit an dieser Stelle abgeschlossen. Entschieden ist über
die 243 zu klärenden Fragen selbst noch nichts.

## 22 – 239 Formeldateien sind noch nicht normalisiert

**Status:** entschieden

**Bestand am 2026-09-06:**

425 Buchseiten haben eine Formeldatei `formeln_s<Seite>.md`. Für **188** davon
gibt es eine normalisierte Fassung `formeln_s<Seite>_normalisiert.md`, für
**237** nicht. Die Überschrift nennt 239; die Differenz von zwei ist nicht
geklärt und praktisch ohne Bedeutung. Umgekehrt gibt es keine normalisierte
Datei ohne Rohfassung — es fehlt also nichts, es ist nur noch nicht aufbereitet.

**Entscheidung von Werner am 2026-09-06 – im laufenden Python-Gang, nicht vorab:**

Die 237 Seiten werden **nicht** vorab am Stück normalisiert. Jede Seite wird dann
aufbereitet, wenn sie im laufenden Python-Gang an die Reihe kommt. Das ist
dieselbe Arbeitsweise wie bei den Prüfstellen nach Entscheidung 14: nicht die
Liste abarbeiten, sondern das Kapitel, das gerade ausgeformt wird.

Damit ist die Normalisierung kein eigener Arbeitsgang vor dem Coden mehr,
sondern Teil davon.

**Was daraus folgt:**

Die 188 vorhandenen normalisierten Dateien sind ein Vorsprung, kein Maßstab. Wo
eine fehlt, wird sie im Gang erstellt; wo eine da ist, wird sie gelesen und ihre
offenen Fragen mit erledigt, siehe
`100_quellen/10_hofenbitzer_band_1_digital/prüfstelle_formel_zusammenzug/01_offene_fragen_normalisierte_formeln.md`.

Anzumerken ist, dass fünf der vorhandenen normalisierten Dateien nur eine
Kurzfassung sind — `formeln_s345`, `s346`, `s348`, `s514` und `s515`, alle aus
der Extraktionswelle v3. Ihnen fehlen Eingabe- und Ausgabetabellen, offene
Fragen und der Python-Hinweis; s514 und s515 enthalten überhaupt keine Formel.
Sie sind im Gang wie nicht normalisierte Seiten zu behandeln.

## 23 – 79 Formeldateien tragen alte Namen

**Status:** erledigt

**Worum es ging:**

Die Formeldateien hießen nicht einheitlich. An den Namen hing jeweils der
Arbeitsgang oder der Modellname: `formeln_s100_digital_geprüft.md`,
`formeln_s51_codex_v2_digital_geprueft.md`, `formeln_s44_glockenrock.md`,
`formeln_s8.1.md`. Für Menschen lesbar, aber jede Datei anders benannt. Von
einer Buchseite ließ sich nicht auf den Dateinamen schließen und umgekehrt auch
nicht.

**Erledigt durch den Commit `72d843b` vom 2026-09-06:**

Der Commit „chore: Hofenbitzer-Dateinamen vereinheitlichen" hat **393 Dateien
umbenannt**, davon **171 Formeldateien** und 222 Seitentexte. Alle 171
Formeldateien tragen seither das Muster `formeln_s<Seite>.md` beziehungsweise
`formeln_s<Seite>_normalisiert.md`; keine einzige weicht davon ab.

Nachgeprüft am 2026-09-06: In den Kapitelordnern 00 bis 14 von
`100_quellen/10_hofenbitzer_band_1_digital/` gibt es **keinen alten Formelnamen
mehr**. Erst dadurch ließ sich der Bestand für Punkt 22 überhaupt gegenrechnen —
425 Seiten mit Formeldatei, 188 davon normalisiert.

**Was bewusst außen vor bleibt:**

Im Ordner `99_pruefstellen_vom_archiv` liegen 96 Dateien mit den alten
Sammelnamen wie `s99-104_codex_v2_mit_pruefstellen.md` und
`Formeln_S448-544.md`. Das sind Tranchen über mehrere Buchseiten, keine
Einzelseiten; sie ließen sich nur nach einer Aufteilung in das Muster
überführen. Weitere 188 liegen im Archiv `30_hofenbitzer_band_1_archiv` und
werden nach dem Archivgrundsatz nicht angefasst.

**Zur Zahl 79:**

Sie ist nicht nachvollziehbar. Umbenannt wurden 171 Formeldateien. Ob die 79
eine frühere Teilmenge war, ist nicht mehr zu erkennen — dieselbe Lage wie bei
den 257 in Punkt 21 und den 239 in Punkt 22.

---

# D – Ordnerstruktur in `200_funktionen`

**Alle sechs Punkte hat Werner am 2026-09-06 geparkt.** Sie kommen im
laufenden Gang dran, wenn die betroffenen Ordner tatsächlich bearbeitet
werden — nicht vorab am Stück. Der Befund bleibt bestehen, entschieden ist
noch nichts.

## 24 – 125 echte Nummernkollisionen

**Status:** geparkt – kommt im laufenden Gang dran

**Entscheidung:**

**Betroffene Kapitel und Vorgehen:**

## 25 – 16 Seitenzahl-Dubletten

**Status:** geparkt – kommt im laufenden Gang dran

**Entscheidung:**

## 26 – 25 Ordner ohne Seitenzahl im Namen

**Status:** geparkt – kommt im laufenden Gang dran

**Entscheidung:**

## 27 – Zwei Nummernlücken

**Status:** geparkt – kommt im laufenden Gang dran

**Entscheidung:**

## 28 – Zwei Gruppen beginnen mit 00 statt 01

**Status:** geparkt – kommt im laufenden Gang dran

**Entscheidung:**

## 29 – Leere Ordner sind nicht durch Git versioniert

**Status:** geparkt – kommt im laufenden Gang dran

**Entscheidung zur dauerhaften Sicherung der Arbeitskarte:**

---

# Bereits in der Ausgangsliste als erledigt gemeldet

Diese Angaben werden nicht ungeprüft zu aktuellen Entscheidungen erklärt. Sie bleiben
hier als Ausgangsbefund und können bei Bedarf im Repo verifiziert werden.

- Dritte Ordnerschicht ergänzt, wo sie fehlte.
- Geprüft, wo laut Buch keine Schrittebene hingehört.
- Bestand der Seitentexte, Formeldateien, Normalisierungen, Einzelformeln und
  Kapitel-Prüfstellen aufgenommen.
- Vier zusätzliche Prüfstellen gefunden.

# Nächster Listenpunkt

Die Vorab-Liste ist durch. Kein Punkt steht mehr offen.

Werner prüft die Prüfstellen **Stück für Stück**, jeweils zu der Buchseite,
die gerade bearbeitet wird. Es geht weiter mit dem Ausformen von Kapitel 02,
Grundschnitte Röcke, nach Entscheidung 03.
