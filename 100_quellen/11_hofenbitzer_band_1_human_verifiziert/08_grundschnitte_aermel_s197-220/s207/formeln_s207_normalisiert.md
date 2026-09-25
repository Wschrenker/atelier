# Formeln – Seite 207 (normalisiert)

Getrennte technische Fassung zu [`formeln_s207.md`](formeln_s207.md). Die
Seite ist weiterhin `OCR-Rohfassung – noch nicht menschlich verifiziert`
([`s207.md`](s207.md)); jede Formel unten bleibt bis zur Bestätigung am
Original mindestens `offen`. Zwei Formeln stehen zusätzlich auf `gesperrt`,
weil der Buchwortlaut selbst unvollständig bzw. widersprüchlich überliefert
ist (siehe jeweils „Offene Fragen").

## Formel 1 — Saum: 2–3 cm hochmessen und ½ ASaW abtragen

**Quelle:** [`formeln_s207.md`](formeln_s207.md#saum-2–3-cm-hochmessen-und-½-asaw-abtragen).

**Buchfassung:**

```text
An der Saumlinie 2 bis 3 cm hochmessen und 1/2 ASaW zur Saumlinie abtragen
→ Saum.
```

**Technische Formel:** `Saumpunkt = Saumlinie + Δh (2–3 cm hochmessen)`,
davon ausgehend `SaumBreite_je_Seite = ASaW / 2`.

**Eingaben und Einheiten:** `Δh` (Bereich 2–3 cm), `ASaW` (Ärmelsaumweite,
cm) — auf dieser Seite nicht definiert.

**Ausgabe und Einheit:** Punkt/Linie „Saum" (cm-Lage relativ zur
Saumlinie).

**Bereiche, Bedingungen, Auswahlentscheidungen:** `Δh` bleibt Bereich
2–3 cm; keine Buchregel für einen festen Wert innerhalb dieses Bereichs.

**Abhängigkeiten:** `ASaW` stammt vermutlich aus einer Maßtabelle oder
Vorseite (z. B. Seite 205, laut Zeile 8 „Weiterentwicklung von Seite 205");
nur verlinken, sobald die Quelle bekannt ist.

**Status:** offen

**Offene Fragen:** Woher kommt `ASaW`? Keine feste Wahl innerhalb 2–3 cm
im Buch angegeben.

## Formel 2 — Hintere Ellenbogenlinie: 0,5–1 cm → hinterer Ärmelbruch

**Quelle:** [`formeln_s207.md`](formeln_s207.md#hintere-ellenbogenlinie-05-bis-1-cm-einstellen--hinterer-ärmelbruch).

**Buchfassung:**

```text
An der Ellenbogenlinie hinten (rechts) 0,5 bis 1 cm einstellen. Von P8 über
die Einstellung weiter zum Saum zeichnen → hinterer Ärmelbruch.
```

**Technische Formel:** `EinstellPunkt_hinten = Ellenbogenlinie_hinten − Δ`
(Δ = 0,5–1 cm); Kurve `hinterer Ärmelbruch = P8 → EinstellPunkt_hinten →
Saum`.

**Eingaben und Einheiten:** `P8` (Punkt aus vorheriger Konstruktion, nicht
auf dieser Seite definiert), `Δ` (Bereich 0,5–1 cm).

**Ausgabe und Einheit:** Kurve „hinterer Ärmelbruch".

**Bereiche, Bedingungen, Auswahlentscheidungen:** `Δ` bleibt Bereich, keine
Default-Wahl im Buch.

**Abhängigkeiten:** `P8` vermutlich aus Vorseite (205) oder früherem
Konstruktionsschritt dieser Seite; nur verlinken.

**Status:** offen

**Offene Fragen:** Herkunft von `P8` ungeklärt; keine feste Wahl innerhalb
0,5–1 cm im Buch angegeben.

## Formel 3 — Vordere Ellenbogenlinie: 0,5–1 cm → vorderer Ärmelbruch

**Quelle:** [`formeln_s207.md`](formeln_s207.md#vordere-ellenbogenlinie-05-bis-1-cm-einstellen--vorderer-ärmelbruch).

**Buchfassung (OCR-Rohtext, mit dokumentierter Lücke):**

```text
An der Ellenbogenlinie vorne 0,5 bis 1 cm für die Formung des Arzum VAP und
zum vorderen Saum zeichnen.
```

**Buchfassung (Werners unbestätigte Sichtlesung des Originals):**

```text
An der Ellenbogenlinie vorne 0,5 bis 1 cm für die Formung des Ärmels
einstellen → vÄBr. Von dort zum vÄP und zum vorderen Saum zeichnen.
```

**Technische Formel:** vermutlich analog zu Formel 2:
`EinstellPunkt_vorne = Ellenbogenlinie_vorne − Δ` (Δ = 0,5–1 cm); Kurve
`vorderer Ärmelbruch = EinstellPunkt_vorne → vÄP → Saum`. Ohne den fehlenden
Satzteil ist der Zwischenpunkt „vÄBr" nur aus Werners Sichtlesung
erschließbar, nicht aus dem OCR-Rohtext selbst.

**Eingaben und Einheiten:** `Δ` (Bereich 0,5–1 cm), Zielpunkte `vÄP`
(vorderer Ärmelpunkt), ggf. `vÄBr` (vorderer Ärmelbruch) — nur in der
unbestätigten Lesung genannt.

**Ausgabe und Einheit:** Kurve „vorderer Ärmelbruch".

**Bereiche, Bedingungen, Auswahlentscheidungen:** `Δ` bleibt Bereich, keine
Default-Wahl im Buch.

**Abhängigkeiten:** analoge Konstruktion zu Formel 2 (hintere
Ellenbogenlinie); `vÄP` vermutlich aus Abschnitt „Ärmelpunkte und
Oberarmweite" derselben Seite.

**Status:** gesperrt

**Offene Fragen:** Der OCR-Rohtext fehlt an einer entscheidenden Stelle
ersatzlos („…mels einstellen → vÄBr. Von dort"); ohne Bestätigung am
Original ist unklar, ob der Zwischenpunkt `vÄBr` tatsächlich existiert und
wie die Kurve genau verläuft.

## Formel 4 — Ärmelnaht (AN) parallel zum vABr durch TP

**Quelle:** [`formeln_s207.md`](formeln_s207.md#ärmelnaht-an-parallel-zum-vabr-durch-tp).

**Buchfassung:**

```text
Die Armelnaht (AN) parallel zum VABr durch den TP zum Saum zeichnen
(einfache Form).
```

**Technische Formel:** `ÄN = Gerade durch TP, parallel zu vÄBr, bis Saum`.

**Eingaben und Einheiten:** Punkt `TP`, Referenzlinie `vÄBr` (beide nicht
auf dieser Seite definiert).

**Ausgabe und Einheit:** Linie „Ärmelnaht (ÄN)".

**Bereiche, Bedingungen, Auswahlentscheidungen:** keine; Parallelverschiebung
ist eindeutig, sofern `TP` und `vÄBr` bekannt sind.

**Abhängigkeiten:** `TP` und `vÄBr` stammen aus früheren Konstruktionsschritten
(vermutlich Vorseite oder oberer Teil dieser Seite); nur verlinken.

**Status:** offen

**Offene Fragen:** keine inhaltliche Unklarheit in der Konstruktionsregel
selbst; Status bleibt offen wegen fehlender menschlicher Verifizierung der
Seite.

## Formel 5 — Nahtmarkierungen (Knipse) 6–8 cm um die Ellenbogenlinie

**Quelle:** [`formeln_s207.md`](formeln_s207.md#nahtmarkierungen-knipse-6–8-cm-um-die-ellenbogenlinie).

**Buchfassung:**

```text
Nahtmarkierungen (Knipse) an die Ärmelnaht 6 bis 8 cm oberhalb und
unterhalb der Ellenbogenlinie anbringen.
```

**Technische Formel:** `Knips_oben = Ellenbogenlinie + d` (entlang ÄN),
`Knips_unten = Ellenbogenlinie − d`, mit `d` im Bereich 6–8 cm.

**Eingaben und Einheiten:** Linie „Ellenbogenlinie", `d` (Bereich 6–8 cm).

**Ausgabe und Einheit:** zwei Punkte „Knips_oben"/„Knips_unten" auf der
Ärmelnaht.

**Bereiche, Bedingungen, Auswahlentscheidungen:** `d` bleibt Bereich, keine
Default-Wahl im Buch.

**Abhängigkeiten:** benötigt Ärmelnaht aus Formel 4 und Ellenbogenlinie aus
vorheriger Konstruktion.

**Status:** offen

**Offene Fragen:** keine inhaltliche Unklarheit; Status bleibt offen wegen
fehlender menschlicher Verifizierung der Seite.

## Formel 6 — Ärmelflächen spiegeln (vABr/hABr)

**Quelle:** [`formeln_s207.md`](formeln_s207.md#ärmelflächen-spiegeln-vabrhabr).

**Buchfassung:**

```text
Die Armelflachen an vABr und hABr nach außen spiegeln.
```

**Technische Formel:** `Ärmelfläche_gespiegelt = Spiegelung(Ärmelfläche,
Achse = vÄBr)` bzw. `Achse = hÄBr` (Spiegelung nach außen, je Ärmelseite).

**Eingaben und Einheiten:** Fläche „Ärmelfläche" (aus vorherigem
Konstruktionsschritt), Spiegelachsen `vÄBr`, `hÄBr`.

**Ausgabe und Einheit:** gespiegelte Ärmelfläche(n).

**Bereiche, Bedingungen, Auswahlentscheidungen:** keine; Spiegeloperation
ist geometrisch eindeutig, sofern Ausgangsfläche und Achse bekannt sind.

**Abhängigkeiten:** benötigt die „inneren (gefärbten) Ärmelflächen" aus
Abschnitt „7 Darstellung der Inneren Ärmelflächen" (Bildunterschrift □7,
`skizzen_s207.json`).

**Status:** offen

**Offene Fragen:** keine inhaltliche Unklarheit; Status bleibt offen wegen
fehlender menschlicher Verifizierung der Seite.

## Formel 7 — vAU auf die vordere Ärmelkugel abtragen

**Quelle:** [`formeln_s207.md`](formeln_s207.md#vau-auf-die-vordere-ärmelkugel-abtragen).

**Buchfassung:**

```text
Den gesamten vAU auf der vorderen Armelkugel abtragen und oben einen
Strich markieren.
```

**Technische Formel:** `Strichmarke_vorne = Punkt auf Kurve vÄk im
Bogenabstand vAU vom Kurvenanfang`.

**Eingaben und Einheiten:** `vAU` (Maßgröße, cm — auf dieser Seite nicht
definiert, vermutlich vorderer Armlochumfang aus Vorseite/Maßtabelle),
Kurve `vÄk`.

**Ausgabe und Einheit:** Strichmarke (Punkt) auf der Kurve `vÄk`.

**Bereiche, Bedingungen, Auswahlentscheidungen:** keine Bandbreite; fester
Bogenabstand `vAU`.

**Abhängigkeiten:** `vAU` und Kurve `vÄk` stammen aus vorherigem
Konstruktionsschritt oder Vorseite; nur verlinken.

**Status:** offen

**Offene Fragen:** Bezeichnung „vAU" selbst ist laut `s207.md` unsicher
(evtl. „vAlU" im Original) — Bedeutung der Abkürzung und ihr Wert sind ohne
Bestätigung am Original nicht sicher zu übernehmen.

## Formel 8 — hAchsel + EW-Additionsregel an die hintere Ärmelkugel

**Quelle:** [`formeln_s207.md`](formeln_s207.md#hachsel--ew-additionsregel-an-die-hintere-ärmelkugel)
und „EW-Rechenbeispiel" (Zeichnung `skizze_01`).

**Buchfassung:**

```text
Die hAchsel an der hinteren Armelkugel · EW (0,5 cm bis 1 cm) übertragen.
Bei kleiner EW ist 0,5 cm, bei großer EW ist 1 cm, bei mittlerer ist 0,7 cm
zu addieren.
```

```text
EW = 2,6 cm + 0,7 cm = 3,3 cm
```

**Technische Formel:** `Strichmarke_hinten = Punkt auf Kurve hÄk im
Bogenabstand hAchsel + EW_Zuschlag vom Kurvenanfang`, mit
`EW_Zuschlag = f(EW_Größe)`:
`EW_Zuschlag = 0,5 cm` (EW klein), `EW_Zuschlag = 0,7 cm` (EW mittel),
`EW_Zuschlag = 1 cm` (EW groß). Rechenbeispiel aus der Zeichnung:
`EW = 2,6 cm + 0,7 cm = 3,3 cm` — unabhängig nachgerechnet: `2,6 + 0,7 =
3,3`, arithmetisch korrekt.

**Eingaben und Einheiten:** `hAchsel` (cm, auf dieser Seite nicht
definiert), `EW_Größe` (Auswahl klein/mittel/groß), Kurve `hÄk`.

**Ausgabe und Einheit:** Strichmarke (Punkt) auf der Kurve `hÄk`.

**Bereiche, Bedingungen, Auswahlentscheidungen:** Dreistufige Auswahlregel
(klein → 0,5 cm, mittel → 0,7 cm, groß → 1 cm); keine Grenzwerte für
„klein"/„mittel"/„groß" auf dieser Seite definiert. Bereich bleibt erhalten,
kein Default.

**Abhängigkeiten:** `hAchsel` vermutlich aus derselben Quelle wie `vAchsel`
(vgl. s201, Formel 1); der Summand „2,6 cm" im Zeichnungsbeispiel ist ohne
weitere Herleitung auf dieser Seite.

**Status:** offen

**Offene Fragen:** Woher kommt der Summand „2,6 cm" im Rechenbeispiel? Wo
liegen die Grenzen zwischen „kleiner", „mittlerer" und „großer" EW? Das im
Fließtext als „\cdot" (Malpunkt) erkannte Zeichen zwischen „Armelkugel" und
„EW" ist laut `s207.md` vermutlich ein fehlgelesenes „+" — am Original zu
bestätigen.

## Formel 9 — Nahtlänge hAP–SuP an die hintere obere Ärmelkugel abtragen

**Quelle:** [`formeln_s207.md`](formeln_s207.md#nahtlänge-hap–sup-an-die-hintere-obere-ärmelkugel-abtragen).

**Buchfassung:**

```text
Von Dort die Nahtlänge zwischen hAP und SuP an der hinteren oberen
Armelkugel abtragen und auch hier einen Strich markieren.
```

**Technische Formel:** `Strichmarke_hinten_2 = Punkt auf Kurve hÄk im
Bogenabstand |hAP − SuP| (Nahtlänge) von der Strichmarke aus Formel 8`.

**Eingaben und Einheiten:** Nahtlänge zwischen `hAP` und `SuP` (cm, auf
dieser Seite nicht beziffert), Kurve `hÄk`.

**Ausgabe und Einheit:** Strichmarke (Punkt) auf der Kurve `hÄk`.

**Bereiche, Bedingungen, Auswahlentscheidungen:** keine Bandbreite; fester
Bogenabstand gleich der Nahtlänge `hAP–SuP`.

**Abhängigkeiten:** benötigt Strichmarke aus Formel 8 sowie Punkte `hAP`
und `SuP`, die auf dieser Seite selbst erst weiter unten (Formel 10)
eingeführt werden — Reihenfolge im Buch ist nicht rein linear.

**Status:** offen

**Offene Fragen:** Zahlenwert der Nahtlänge `hAP–SuP` ist auf dieser Seite
nicht angegeben; vermutlich aus Vorseite oder Maßtabelle zu übernehmen.

## Formel 10 — SuP-Anteil vorne (widersprüchlich: 1/2 vs. ⅓)

**Quelle:** [`formeln_s207.md`](formeln_s207.md#sup-anteil-vorne-12-widersprüchlich).

**Buchfassung (OCR-Rohtext):**

```text
Den SuP bei 1/2 im vorderen Bereich markieren. Somit ist hinten 1/2, also
mehr EW vorhanden.
```

**Buchfassung (Werners unbestätigte Sichtlesung des Originals):**

```text
Den SuP bei ⅓ im vorderen Bereich markieren.
```

**Technische Formel:** `SuP = Ellenbogenlinie_vorne_Anteil · Bezugsgröße`,
mit `Ellenbogenlinie_vorne_Anteil ∈ {1/2, 1/3}` je nach Lesung — die beiden
Lesungen führen zu unterschiedlichen Konstruktionsergebnissen (bei ⅓ vorne
bliebe rechnerisch ⅔ hinten statt „hinten 1/2" laut OCR-Satz, was auch zum
später im Text erwähnten Ergebnisbruch „⅔" passen würde, siehe `s207.md`).

**Eingaben und Einheiten:** Bezugsgröße (vermutlich EW oder ein
Kugelmaß, auf dieser Seite nicht eindeutig benannt), Anteilsfaktor `1/2`
oder `1/3`.

**Ausgabe und Einheit:** Punkt `SuP` (Lage im vorderen Bereich).

**Bereiche, Bedingungen, Auswahlentscheidungen:** kein Bereich, sondern ein
fester Bruchwert — aber zwei widersprüchliche Buchlesungen stehen zur
Wahl; keine davon ist bestätigt.

**Abhängigkeiten:** Ergebnis wirkt auf Formel 9 (Nahtlänge hAP–SuP) und auf
Formel 12 (OaW-Kontrolle über SuP).

**Status:** gesperrt

**Offene Fragen:** Welcher Bruch steht tatsächlich im Original, 1/2 oder
⅓? Laut `s207.md` (Prüfstelle 6) ist dies ein direkter Lesungswiderspruch,
keine bloße Unschärfe. Ohne Klärung am Original ist diese Formel nicht
codierbar.

## Formel 11 — Zweiter Knips 1 cm oberhalb hAP

**Quelle:** [`formeln_s207.md`](formeln_s207.md#zweiter-knips-1-cm-oberhalb-hap).

**Buchfassung:**

```text
Ein zweiter Knips wird 1 cm oberhalb des hAP markiert. Damit ist der
hintere Ärmelbereich eindeutig definiert.
```

**Technische Formel:** `Knips_2 = Punkt auf Kurve im Bogenabstand 1 cm von
hAP, Richtung Kugelspitze` (identisch zur bereits auf s201 dokumentierten
Formel „Knips 1 cm oberhalb hAP").

**Eingaben und Einheiten:** `hAP` (Punkt), Offset `1 cm` (fest).

**Ausgabe und Einheit:** Punkt `Knips_2`.

**Bereiche, Bedingungen, Auswahlentscheidungen:** fester Wert, keine
Bandbreite.

**Abhängigkeiten:** benötigt `hAP`; inhaltlich gleiche Regel wie auf s201
(dort als Formel 2 dokumentiert) — dort nur verlinken, nicht kopieren,
sobald beide Seiten menschlich verifiziert sind.

**Status:** offen

**Offene Fragen:** keine inhaltliche Unklarheit; Status bleibt offen wegen
fehlender menschlicher Verifizierung der Seite.

## Formel 12 — Kontrolle OaW auf der Hälfte zwischen SuP und Ellenbogenlinie

**Quelle:** [`formeln_s207.md`](formeln_s207.md#kontrolle-oaw-auf-der-hälfte-zwischen-sup-und-ellenbogenlinie).

**Buchfassung:**

```text
Die Oberarmweite (OaW) auf der Hälfte zwischen SuP und Ellenbogenlinie
waagerecht kontrollieren.
```

**Technische Formel:** `Kontrolllinie_Höhe = (Höhe(SuP) + Höhe(Ellenbogenlinie)) / 2`;
`OaW_Kontrolle = waagerechte Breite des Ärmels auf `Kontrolllinie_Höhe``.

**Eingaben und Einheiten:** Punkt `SuP`, Linie „Ellenbogenlinie".

**Ausgabe und Einheit:** `OaW_Kontrolle` (cm) auf der ermittelten Höhe.

**Bereiche, Bedingungen, Auswahlentscheidungen:** keine; exakte Halbierung
der Höhe zwischen `SuP` und Ellenbogenlinie.

**Abhängigkeiten:** benötigt `SuP` aus Formel 10 — und ist damit von deren
ungeklärtem Bruchwert (1/2 vs. ⅓) mitbetroffen, auch wenn die
Halbierungsregel selbst unabhängig davon eindeutig ist.

**Status:** offen

**Offene Fragen:** keine inhaltliche Unklarheit in der Halbierungsregel
selbst; die Lage von `SuP` hängt jedoch an der ungeklärten Formel 10.
