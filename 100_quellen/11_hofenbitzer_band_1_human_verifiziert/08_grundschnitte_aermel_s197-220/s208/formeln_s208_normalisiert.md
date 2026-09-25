# Formeln s208 – Normalisierung (Walking Skeleton)

Getrennt von `formeln_s208.md`. Jede Formel verlinkt auf ihre Stelle dort.
Seite 208 ist noch nicht menschlich verifiziert; entsprechend bleibt fast
jede Formel hier `offen` oder `gesperrt`. Kein Eintrag ist bereit für einen
Codevertrag.

## F1 – Mindestabstand Ärmelnaht–vÄBr

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 5, „Allgemeine
Bedingung“

**Buchfassung:**

```text
Je näher die Ärmelnaht am vorderen Ärmelbruch (vÄBr) liegt, desto geringer ist
der Dehnbetrag. Damit die Ärmelnaht wenig sichtbar bleibt, sollte der Abstand
zum vÄBr mindestens 1,5 cm betragen.
```

**Technische Formel:** `abstand(AN, vÄBr) ≥ 1,5 cm`

**Eingaben und Einheiten:** Abstand AN–vÄBr [cm]

**Ausgabe und Einheit:** Wahr/Falsch-Bedingung, kein Konstruktionswert

**Bereiche, Bedingungen und Auswahlentscheidungen:** Untergrenze 1,5 cm;
„sollte“ – Empfehlung, keine erkennbar harte Regel

**Abhängigkeiten:** F5 (Ärmelnaht 1,5–2,5 cm parallel zu vÄBr) erfüllt diese
Untergrenze bereits konstruktiv

**Status:** offen

**Offene Fragen:** Ist dies eine eigenständige Prüfregel für den Codevertrag
oder nur erläuternder Kontext zu F5? Am Original/durch Werner zu klären.

## F2 – Saumpunkt

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 5, „Saumpunkt“

**Buchfassung:**

```text
An der Saumlinie 2 bis 3 cm hochmessen und 1/2 ASaW zur Saumlinie abtragen →
Saum.
```

**Technische Formel:** `P_hoch = Saumlinie + Bereich(2, 3) cm` (Richtung
entlang der Saumlinie nach oben); `Saum = P_hoch` versetzt um `½ · ÄSaW`
zurück zur Saumlinie

**Eingaben und Einheiten:** ÄSaW (Ärmelsaumweite) [cm]; Bereich 2–3 cm

**Ausgabe und Einheit:** Punkt „Saum“ [cm-Koordinate]

**Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 2–3 cm ohne
Buchregel für einen festen Wert

**Abhängigkeiten:** ÄSaW stammt laut Text von „Seite 205“ („Weiterentwicklung
von Seite 205“) – nicht auf dieser Seite definiert

**Status:** offen

**Offene Fragen:** Herkunft und genaue Definition von ÄSaW; exakte
Abtragrichtung nur aus Zeichnung `skizzen/s208_skizze_02.png` ablesbar, dort
als „2 bis 3 cm“ / „½ ÄsW“ bestätigt sichtbar, aber nicht von Werner
freigegeben.

## F3 – Hinterer Ärmelbruch

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 5, „Hinterer
Ärmelbruch“

**Buchfassung:**

```text
An der Ellenbogenlinie hinten (rechts) 0,5 bis 1 cm einstellen. Von P8 über
die Einstellung weiter zum Saum zeichnen → hinterer Ärmelbruch.
```

**Technische Formel:** `P_einstellung = Ellenbogenlinie_hinten + Bereich(0,5, 1) cm`;
`hÄBr = Linie(P8 → P_einstellung → Saum)`

**Eingaben und Einheiten:** Bereich 0,5–1 cm; Punkt P8

**Ausgabe und Einheit:** Linie „hinterer Ärmelbruch“

**Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 0,5–1 cm ohne
festen Wert

**Abhängigkeiten:** Punkt P8 ist auf dieser Seite nicht definiert (vermutlich
Vorseite/Seite 205)

**Status:** gesperrt

**Offene Fragen:** Herkunft von P8 muss über die Seitenabhängigkeit geklärt
werden, bevor diese Formel eigenständig normalisiert werden kann.

## F4 – Vorderer Ärmelbruch (vÄBr)

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 5, „Vorderer
Ärmelbruch“

**Buchfassung:**

```text
An der Ellenbogenlinie vorne 0,5 bis 1 cm für die Formung des Ärmels
einstellen → vÄBr. Von Dort zum vÄP und zum vorderen Saum zeichnen.
```

**Technische Formel:** `vÄBr = Ellenbogenlinie_vorne + Bereich(0,5, 1) cm`;
Linie `vÄBr → vÄP → vorderer_Saum`

**Eingaben und Einheiten:** Bereich 0,5–1 cm

**Ausgabe und Einheit:** Punkt/Linie „vÄBr“

**Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 0,5–1 cm ohne
festen Wert; „für die Formung des Ärmels“ als fachlicher Auswahlspielraum

**Abhängigkeiten:** vorderer Saum aus F2

**Status:** offen

**Offene Fragen:** Auswahlkriterium innerhalb 0,5–1 cm nicht angegeben.

## F5 – Ärmelnaht parallel zu vÄBr

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 5, „Ärmelnaht
parallel zu vÄBr“

**Buchfassung:**

```text
Die Armelnaht (AN) 1,5 bis 2,5 cm parallel zum vABr zeichnen.
```

**Technische Formel:** `AN = Parallele(vÄBr, Bereich(1,5, 2,5) cm)`

**Eingaben und Einheiten:** Bereich 1,5–2,5 cm

**Ausgabe und Einheit:** Linie „Ärmelnaht (AN)“

**Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 1,5–2,5 cm ohne
festen Wert; Richtung (zu welcher Seite parallel) nur aus Zeichnung ablesbar

**Abhängigkeiten:** vÄBr aus F4; erfüllt Mindestabstand aus F1

**Status:** offen

## F6 – Nahtmarkierungen

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 5,
„Nahtmarkierungen“

**Buchfassung:**

```text
7 Nahtmarkierungen an die Armelnaht ca. 8 cm oberhalb und unterhalb der
Ellenbogenlinie anbringen.
```

**Technische Formel:** `Markierung_oben = Ellenbogenlinie + 8 cm` (entlang
AN); `Markierung_unten = Ellenbogenlinie − 8 cm` (entlang AN)

**Eingaben und Einheiten:** ca. 8 cm (Näherungswert, kein Bereich)

**Ausgabe und Einheit:** zwei Punkte auf der Ärmelnaht

**Bereiche, Bedingungen und Auswahlentscheidungen:** „ca.“ – ungefährer Wert,
kein exakter Fixwert laut Buchfassung

**Abhängigkeiten:** Ärmelnaht (AN) aus F5

**Status:** offen

**Offene Fragen:** Die vorangestellte Kreiszahl „7“ ist laut `s208.md`
(Prüfstelle 2) unzuverlässig erkannt; ihre tatsächliche Zahl ist ungeklärt.

## F7 – Überschneidungsbetrag (vÄN/hÄN)

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 6

**Buchfassung:**

```text
Am vABr entsteht bei diesem Ärmel ein sehr geringer Überschneidungsbetrag an
der Ellenbogenlinie. Um diese Strecke ist die vÄN kürzer als die hÄN.
```

**Technische Formel:** `vÄN = hÄN − Überschneidungsbetrag`

**Eingaben und Einheiten:** Überschneidungsbetrag [cm], auf dieser Seite ohne
Zahlenwert

**Ausgabe und Einheit:** vÄN [cm], relativ zu hÄN

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine – rein qualitative
Aussage auf dieser Seite

**Abhängigkeiten:** möglicher Zusammenhang mit F3/F4 (0,5–1 cm Einstellungen),
nicht belegt

**Status:** gesperrt

**Offene Fragen:** Kein Zahlenwert für den Überschneidungsbetrag auf s208
vorhanden; Herkunft ungeklärt.

## F8 – EW-Zuschlag auf hAchsel

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 7, Text und
Zeichnungsbeleg `skizzen/s208_skizze_01.png`

**Buchfassung:**

```text
Die hAchsel an der hinteren Armelkugel + EW (0,5 cm bis 1 cm) übertragen. Bei
kleiner EW ist 0,5 cm, bei großer EW ist 1 cm, bei mittlerer ist 0,7 cm zu
addieren.
```

Zeichnung (Beispielrechnung): `hAchsel 8,5 cm` … `8,5 cm + 0,7 cm = 9,5 cm`

**Technische Formel:** `Punkt21 = hAchsel + EW_Zuschlag`, mit
`EW_Zuschlag = 0,5 cm` (EW klein) `| 0,7 cm` (EW mittel) `| 1 cm` (EW groß)

**Eingaben und Einheiten:** hAchsel [cm] (Beispiel: 8,5 cm); EW-Kategorie
{klein, mittel, groß}

**Ausgabe und Einheit:** Punkt21-Maß [cm] (Beispiel: 9,5 cm)

**Bereiche, Bedingungen und Auswahlentscheidungen:** Auswahltabelle
EW-Kategorie → Zuschlag; Schwellenwerte zwischen „klein“, „mittel“, „groß“
nicht angegeben

**Abhängigkeiten:** möglicherweise dieselbe EW-Größe wie in F9 – nicht
bestätigt

**Status:** offen

**Offene Fragen:** Ab welchem EW-Wert gilt „klein“, „mittel“, „groß“? Ist „EW“
hier dieselbe Größe wie das „EW“ in F9, oder eine andere fachliche Größe mit
gleicher Abkürzung?

## F9 – SuP-Teilung und EW an der Ärmelkugel oben

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 7, Text (Zeile 63)
und Zeichnungsbeleg `skizzen/s208_skizze_01.png`

**Buchfassung (Fließtext):**

```text
Den SuP bei 1/2 im vorderen Bereich markieren. Somit ist hinten 1/2, also mehr
EW vorhanden.
```

**Buchfassung (Zeichnung, abweichend):**

```text
me = 2,6 cm
⅓ (Richtung vÄP) / ⅔ (Richtung hÄP)
EW = 2,6 cm + 0,7 cm = 3,3 cm
```

**Technische Formel:** ungeklärt – entweder `SuP` teilt `me (2,6 cm)` im
Verhältnis `1:1` (Fließtext-OCR) oder im Verhältnis `⅓ : ⅔` (Zeichnung);
`EW = me + 0,7 cm = 3,3 cm`

**Eingaben und Einheiten:** me = 2,6 cm; Zuschlag 0,7 cm

**Ausgabe und Einheit:** EW = 3,3 cm; Position SuP innerhalb der Strecke me

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine – feste Werte laut
Beispiel, aber Aufteilungsverhältnis widersprüchlich

**Abhängigkeiten:** möglicher Zusammenhang mit EW aus F8, nicht bestätigt

**Status:** gesperrt

**Offene Fragen:** ⅓/⅔ (Zeichnung) oder ½/½ (Fließtext-OCR)? Der Fließtext
„Somit ist hinten … mehr EW vorhanden“ ist mit ½/½ inhaltlich nicht
schlüssig, mit ⅓/⅔ dagegen konsistent – muss am Original entschieden werden
(Prüfstelle 3 in `s208.md`).

## F10 – vÄP-Kugelmaß (Punkt 20)

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 7, Text und
Zeichnungsbeleg

**Buchfassung:**

```text
Den gesamten vAlu auf der vorderen Armelkugel abtragen und oben einen Strich
markieren.
```

Zeichnung: `me = 14,4 cm` (bei vÄP)

**Technische Formel:** `Punkt20 = vordere_Ärmelkugel_Bogenmaß = me(vÄP)`
(Beispiel: 14,4 cm)

**Eingaben und Einheiten:** „vAlu“-Maß [cm], Beispielwert 14,4 cm

**Ausgabe und Einheit:** Punkt „20“ auf der vorderen Ärmelkugel

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine – fester
Beispielwert

**Abhängigkeiten:** keine erkennbare auf dieser Seite

**Status:** gesperrt

**Offene Fragen:** Bedeutung und korrekte Schreibweise von „vAlu“ ungeklärt
(Prüfstelle 4 in `s208.md`); ob 14,4 cm ein fester Sollwert oder nur ein
Beispielmaß der gezeigten Größe (G 38, PK 3) ist, ist offen.

## F11 – hÄP-Nahtlänge (Punkt 22)

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 7, Text und
Zeichnungsbeleg

**Buchfassung:**

```text
Von Dort die Armloch-Nahtlänge zwischen hAp und SuP an der hinteren oberen
Armelkugel abtragen und auch hier einen Strich markieren.
```

Zeichnung: `me = 13,8 cm` (bei hÄP)

**Technische Formel:** `Punkt22 = Punkt21 + Armloch_Nahtlänge(hÄP, SuP)`
(Beispiel: 13,8 cm)

**Eingaben und Einheiten:** Armloch-Nahtlänge [cm], Beispielwert 13,8 cm;
Ausgangspunkt Punkt21 (aus F8)

**Ausgabe und Einheit:** Punkt „22“

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine – fester
Beispielwert

**Abhängigkeiten:** Punkt21 aus F8

**Status:** offen

**Offene Fragen:** Ist 13,8 cm ein fester Sollwert oder nur Beispielmaß der
gezeigten Größe?

## F12 – Zweiter Knips

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 7, Text und
Zeichnungsbeleg (bei ㉓)

**Buchfassung:**

```text
Ein zweiter Knips wird 1 cm oberhalb des hAP markiert. Damit ist der hintere
Armelbereich eindeutig definiert.
```

**Technische Formel:** `Knips2 = hÄP + 1 cm` (Richtung oberhalb)

**Eingaben und Einheiten:** 1 cm (fester Wert)

**Ausgabe und Einheit:** Punkt „Knips2“

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine – fester Wert

**Abhängigkeiten:** hÄP

**Status:** offen

**Offene Fragen:** Zuordnung zur Kreiszahl ㉓ noch nicht von Werner
bestätigt.

## F13 – Oberarmweite-Kontrolle (OaW)

**Quelle:** [`formeln_s208.md`](formeln_s208.md), Abschnitt 7, Text und
Zeichnungsbeleg (bei ㉔)

**Buchfassung:**

```text
Die Oberamweite (OaW) auf der Hälfte zwischen SuP und Ellenbogenlinie
waagerecht kontrollieren.
```

Zeichnung: `OaW kontrollieren … 31 cm`

**Technische Formel:** `Kontrollpunkt = Mittelpunkt(SuP, Ellenbogenlinie)`;
`OaW = horizontale_Weite(Kontrollpunkt)` (Beispiel/Sollwert: 31 cm)

**Eingaben und Einheiten:** Position SuP, Ellenbogenlinie; Ergebnis 31 cm

**Ausgabe und Einheit:** OaW [cm] am Kontrollpunkt

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine – „kontrollieren“
deutet auf einen Soll-/Prüfwert, nicht zwingend auf eine Konstruktionsformel

**Abhängigkeiten:** SuP aus F9

**Status:** offen

**Offene Fragen:** Ist 31 cm ein fester Sollwert für diese Weite oder nur ein
Beispielmaß der gezeigten Größe (G 38, PK 3)? Dient die Kontrolle als
Prüfschritt oder als Eingabe für eine weitere Konstruktion?

---

**Zusammenfassung:** Keine der 13 erfassten Formeln trägt den Status
`normalisiert`. Die zentralen Blocker sind der ungeklärte SuP-Bruchwert
(F9, ⅓/⅔ vs. ½/½), die unklare Abkürzung „vAlu“ (F10) und mehrere über diese
Seite hinausreichende Abhängigkeiten (P8, ÄSaW – vermutlich Seite 205).
