# Formeln s194 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s194.md](s194.md)). Von den formel- und coderelevanten Stellen dieser Seite
sind bislang nur die sechs Punkte im Abschnitt „Vorab geklärte formel- und
coderelevante Stellen" von `s194.md` von Werner am Original bestätigt; die
Prüfstellen 3, 4 und 5 (Zugabentabelle ☐2, Zugabe-Boxen zu ☐3, Zeichnungswerte
in ☐3) sind ausdrücklich noch offen. Diese Extraktion wurde auf ausdrücklichen
Wunsch Werners trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker
übersprungen). Sie ersetzt keine spätere Bestätigung der noch offenen Stellen
und darf insgesamt nicht als menschlich verifiziert gelten. Innerhalb der
Extraktion ist bei jeder Stelle einzeln vermerkt, ob sie zu den sechs
bestätigten Punkten gehört oder unbestätigte OCR-/Bildlesung ist.

## 1. Konstruktionstabelle – bestätigte Maßzugaben (☐1)

Quelle: `s194.md`, Abschnitt „Vorab geklärte formel- und coderelevante
Stellen" (Zeilen 23–29); Rohtabelle in `tabellen_s194.md`, `tbl-0.md` (Zeilen
10–28), dort mit OCR-Lesefehlern (u. a. `201` statt `20,1`, `13,2`/`13,5` statt
`12,2`/`12,5`, `SuWL` statt `SuNL`). Die folgenden fünf Zeilen sind von Werner
am Original bestätigt; die OCR-Rohwerte sind damit für diese Zeilen ersetzt.

```text
AlT 20,1 + 1,3 = 21,4
```

```text
BrB 18,2 + 1,0 = 19,2
```

```text
SuB 12,2 + 0,3 = SuNL 12,5
```

```text
Kontrolle: 44 + 3 = 47
```

```text
hSuNL = SuNL + Einhalteweite
12,5 + 0,7 = 13,2
```

Hinweis: Die letzte Zeile (`hSuNL`) fehlt im OCR-Rohtext vollständig; an ihrer
Stelle liefert `tbl-0.md` eine lange, sinnlose Zahlenkette
(„0,3,5,7,9,…,1000"), siehe Anmerkung in `tabellen_s194.md`. Die
Formelbeziehung `hSuNL = SuNL + Einhalteweite` stammt daher ausschließlich aus
Werners Bestätigung am Original, nicht aus der OCR.

## 2. Zugabentabelle für Oberteil-Konstruktionen (☐2) – überwiegend unbestätigt

Quelle: `tabellen_s194.md`, `tbl-1.md` (Zeilen 36–45); Bildunterschrift
„☐2 Ausschnitt aus der Zugabentabelle" in `ocr_s194.md`, Zeile 19. Prüfstelle 3
in `s194.md` (Zeilen 88–90) ist noch offen; nur der letzte Zeilenwert ist über
die Liste „Vorab geklärte … Stellen" bestätigt.

```text
Passformklasse 9: BrU 18, TaU 12 - 20, HüU 10 - 20, AlT 4, RüB 2, ArD 5, BrB 2
```

```text
PK 9: SuB-Zugabe 0,9
```

Hinweis: Die Kopfzeilen der Rohtabelle sind erkennbar verschoben
(„HSU HSU HSU" statt der Spaltenköpfe); die obige Zuordnung
BrU/TaU/HüU/AlT/RüB/ArD/BrB übernimmt Prüfstelle 3 aus `s194.md` unverändert
und gilt selbst noch als unbestätigt. Nur der letzte Wert dieser Zeile ist laut
„Vorab geklärte … Stellen" bestätigt: `0,9` statt des OCR-Rohwerts `0,3`.

## 3. Zugabe-Boxen zu ☐3 (BrB/ArD/RüB) – unbestätigt

Quelle: `tabellen_s194.md`, `tbl-2.md`–`tbl-4.md` (Zeilen 47–66); Prüfstelle 4
in `s194.md` (Zeilen 91–93) ist noch offen.

```text
Zugabe zur BrB: PK 3 = 1,0 cm, PK 9 = 2,0 cm, Differenz = 1,0 cm
```

```text
Zugabe zum ArD: PK 3 = 1,5 cm, PK 9 = 5,0 cm, Differenz = 3,5 cm
```

```text
Zugabe zur RüB: PK 3 = 0,5 cm, PK 9 = 2,0 cm, Differenz = 1,5 cm
```

## 4. Zeichnung ☐3 „Schnittvergrößerung von PK3 nach PK9" – unbestätigt, zeichnungsgebunden

Quelle: `skizzen_s194.json`, Eintrag `skizzen[0]` (`sichtbare_labels`,
`bestaetigt: false`); Skizzenausschnitt
[`skizzen/s194_skizze_01.png`](skizzen/s194_skizze_01.png). Prüfstelle 5 in
`s194.md` (Zeilen 94–99) ist noch offen. Alle Werte sind vorläufige
KI-Ablesungen aus dem Bildausschnitt, nicht von der OCR-Text-Engine erkannt.

```text
① ½ = 0,5 cm
② ½ = 0,5 cm
⅓ = 1,2 cm
③ Rest 1 cm
① wie am VT 0,5 cm
⅔ = 2,3 cm
```

```text
Zugabe zur AlT: PK 3 = 1,3 cm, PK 9 = 4,0 cm, Differenz = 2,7 cm
```

```text
④ jeweils 2,7 cm nach unten (zweimal)
⑥ ⅔ = 2,3 cm
```

Hinweis: Bezugspunkte `vÄP`, `BrP`, `hÄP` sowie die Kreisnummern ①–⑦ sind
Beschriftungen ohne eigenen Rechenwert und hier nicht als Formel geführt.

## 5. Fließtext „1 OT-GS erweitern" – Rechenanweisungen (Punktnummern, keine Schritte)

Quelle: `ocr_s194.md`, Zeilen 53–65. Laut Konvention für Kapitel 04/06/07 sind
die Ziffern hier Punktnummern, keine Arbeitsschritte im engeren Sinn (siehe
`s194.md`, Anmerkungen). Prüfstelle 1 in `s194.md` (Zeile 82–84) betrifft den
Wortlaut, u. a. „Seitennahlt" (vermutlich „Seitennaht"); OCR-Schreibweise hier
unverändert übernommen.

```text
1 An VT und RT ca. 3 cm neben der vM bzw. hM in (oder direkt neben den) den
Halslöchern zum Saum einschneiden und jeweils die Hälfte der errechneten
Mehrweiten-Differenz zur BrB exakt waagerecht öffnen.
```

```text
3 Am seitlichen VT-Einschnitt wie am VT-Halsloch öffnen (hier 0,5 cm).
```

```text
4 Am seitlichen RT-Einschnitt den restlichen Differenzbetrag zur
RüB-Differenz öffnen (hier 1 cm).
```

```text
5 Das Armloch um die AlT-Differenz vertiefen und die neue Brustlinie zeichnen.
```

```text
6 Ein Drittel der ArD-Differenz an der Seitennahlt vom VT ausstellen.
```

```text
7 Zwei Drittel an der Seitennahlt vom RT ausstellen.
```

## Nicht als Formel erfasst

- Zeile 10–17 (Einleitungstext zu den zwei Konstruktionsmöglichkeiten und zum
  Prinzip des Erweiterns): keine Zahl, keine Rechenbeziehung.
- Punkt „2" (Zeilen 54–56, alternative Einschneidestelle am Halsloch/Schulter):
  Konstruktionsalternative ohne eigenen Zahlenwert.
- Zeile 67 („Die neuen Seitennähte parallel zu den alten Seitennähten
  zeichnen."): geometrische Anweisung ohne Zahlenwert.
- Bildunterschriften „☐1 Ausschnitt aus dem Maßsatz …" (Zeile 31) und
  „☐2 Ausschnitt aus der Zugabentabelle" (Zeile 19): reine
  Verweis-/Zuordnungsbeschreibungen ohne eigenen Zahlenwert.
