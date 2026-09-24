# Formeln s185 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert` ([s185.md](s185.md)).
Diese Extraktion wurde auf ausdrücklichen Wunsch Werners trotzdem als
Walking-Skeleton-Durchlauf erstellt (Blocker übersprungen) und beruht
überwiegend auf [`ocr_s185.md`](ocr_s185.md) und [`tabellen_s185.md`](tabellen_s185.md).
Sie ersetzt keine spätere Bestätigung der noch offenen formelrelevanten
Stellen am Original und darf insoweit nicht als menschlich verifiziert
gelten.

**Ausnahme:** Vier Zahlenwerte sind bereits von Werner am Original bestätigt
(s185.md, Abschnitt „Vorab geklärte formel- und coderelevante Stellen"). Sie
werden unten an ihrer Stelle ausdrücklich als bestätigt gekennzeichnet; alles
Übrige bleibt unbestätigte OCR-Rohfassung.

## 1. Aufteilung des Taillenausfalls (Tabelle)

Quelle: [`tabellen_s185.md`](tabellen_s185.md), Tabelle 1 (`tbl-0.md`); Kontext
[`ocr_s185.md`](ocr_s185.md), Zeile 6–12 (Abschnitt „1 Taillierung des
Taillenausfalls" – Abschnittsnummer laut s185.md unbestätigt, Original
vermutlich „**12** Aufteilung des Taillenausfalls").

```text
0 bis 2 cm  SN     2 × 1 cm  = 2,0 cm
1 bis 3 cm  shAbl            = 2,0 cm
2 bis 4 cm  hAbl             = 2,8 cm
T = Kontrolle TaAf           = 6,8 cm
```

Hinweise:
- Zeile 1 **von Werner am Original bestätigt**: „2 × 1 cm = 2,0 cm" (s185.md,
  „Vorab geklärte..."). Die OCR-Tabelle selbst zeigt an dieser Stelle „2 =
  1 cm" (vermutlich OCR-Fehllesung von „×" als „=").
- Zeilen 2 und 3 zeigen in der OCR-Tabelle keinen Operator/Faktor in der
  mittleren Spalte (nur Kürzel `shAbl` bzw. `hAbl` und Ergebnis) – möglicher
  Spaltenverlust der OCR, nicht ergänzt.
- Die Ergebniszeile „T = Kontrolle TaAf … 6,8 cm" entspricht rechnerisch der
  Summe der drei Zeilen darüber (2,0 + 2,0 + 2,8 = 6,8); dies ist eine reine
  Beobachtung der OCR-Zahlen, keine bestätigte Buchregel.

## 2. Hüftausfall (HüAf) im Vorderteil

Quelle: [`ocr_s185.md`](ocr_s185.md), Zeile 24–28 (Formel) sowie Zeile 32–38
(Bereichsregeln).

```text
Hüftausfall (HüAf)
= vAbl -2cm
= 3,2cm - 2cm
= 1,2cm
```

```text
Ist der Hüftausfall kleiner als 0,5 cm, wird er nicht gezeichnet.

Liegt er zwischen 0,5 und 1 cm kann er ggf. vernachlässigt werden.

Entsteht bei der Berechnung ein Minobetrag, wird kein Hüftausfall gezeichnet.

In allen diesen Fällen, entsteht der taillierte Oberteil-Grundschnitt ohne
Hüftausfall auf Seite 186.
```

Hinweis: „Minobetrag" (Zeile 36) unverändert aus der OCR übernommen, vermutlich
„Minusbetrag" – nicht still korrigiert. Noch nicht am Original bestätigt
(s185.md, Prüfstelle 5).

## 3. Hüft-Fehlbetrag (HüFb)

Quelle: [`ocr_s185.md`](ocr_s185.md), Zeile 42–48 (Formel), Zeile 52
(Bereichsregeln) und Zeile 54 (Anwendung).

```text
4b HÜB und hHÜB (ohne Hüftausfall) messen, addieren = HÜB und in der
Konstruktionstabelle (siehe rechts) den HüFb berechnen:

Hüft-Fehlbetrag (HüFb)
= HUB - 1/2HüW
= 44,9cm - 50,5cm
= -5,6cm → 5,6cm 1/2 = 2,8cm
```

```text
Beträgt der Hüft-Fehlbetrag weniger als 2 cm, ist der HüU unterproportional.
Beträgt der HüFb mehr als 8 cm, ist der HüU überproportional. In beiden
Fällen könnte es sich um ein Figurproblem handeln (siehe Band 2).
```

```text
Jeweils den halben HUFb (hier 5,6 cm; :2 = 2,8 cm) an den Seitenlinien in
Hufthöhe ausstellen.
```

Hinweis: Der letzte Rechenschritt „5,6 cm : 2 = 2,8 cm" ist **von Werner am
Original bestätigt** (s185.md, „Vorab geklärte..."). Der übrige Teil der
Formel (insbesondere „HüB 44,9 − ½ HüW 50,5 = −5,6" sowie die
Bereichsregeln) ist noch nicht bestätigt (s185.md, Prüfstelle 5 und 6).

## 4. Kontrolltabelle TaB/HüB (gemessen − ½ Weite)

Quelle: [`tabellen_s185.md`](tabellen_s185.md), Tabelle 3 (`tbl-2.md`).

```text
genossene TaB  42,8  - � TaW  36    - 6,8
genossene H�B  44,9  - � H�W  50,5  - -5,6
```

Hinweis: „�" (U+FFFD) unverändert wie in `tabellen_s185.md` übernommen – dort
vermutete Lesart „gemessene TaB 42,8 – ½ TaW 36 = 6,8" und „gemessene HüB
44,9 – ½ HüW 50,5 = −5,6" („genossene" vermutlich OCR-Fehllesung von
„gemessene"). Die zweite Zeile entspricht zahlenmäßig der Formel in Abschnitt
3 (HüFb); ob beide Stellen dieselbe Rechnung oder unabhängige Belege sind,
ist offen. Noch nicht am Original bestätigt (s185.md, Prüfstelle 10).

## 5. Kontrolle der Oberbrustbreite

Quelle: [`ocr_s185.md`](ocr_s185.md), Zeile 65 (Fließtext); zusätzlich
zeichnungsgebunden aus `skizzen/s185_skizze_01.png` laut
[s185.md](s185.md), Prüfstelle 11.

```text
4a Die Strecke zwischen vM und Armloch messen und mit der halben
Oberbrustbreite vergleichen.
```

```text
Kontrolle = ½ oBrB + 0 bis 1,5 cm
```

Hinweis: Die zweite Zeile ist eine Beschriftung der Konstruktionszeichnung
(`skizzen/s185_skizze_01.png`), nicht im OCR-Fließtext enthalten; Quelle ist
die Prüfstellen-Liste in `s185.md`, dort selbst noch unbestätigt (Prüfstelle
11).

## 6. Mehrweite im Armloch

Quelle: [`ocr_s185.md`](ocr_s185.md), Zeile 69–73; [`tabellen_s185.md`](tabellen_s185.md),
Tabelle 4 (`tbl-3.md`), erste Zeile.

```text
Beide Armlochkurven messen und addieren. Hiervon den am Körper gemessenen
Armansatzumfang (AraU) absenen. Die Differenz ist die Mehrzeiten im Armloch.
```

```text
vAlU 22,5 + hAlU 24,8 - AraU 44,5 = 2,8 cm
```

Hinweis: **Von Werner am Original bestätigt** (s185.md, „Vorab geklärte...").
Die OCR-Tabelle (`tbl-3.md`) zeigt an dieser Stelle abweichend „haAu 22,5 +
haU 24,5 - hAu 44,5 + 2,8" (andere Kürzel, Zahlenwert 24,5 statt 24,8) –
Werners Bestätigung ersetzt die OCR-Lesung an dieser Zeile. „absenen" (Zeile
71) unverändert aus der OCR übernommen, im Original „abziehen"; „Mehrzeiten"
unverändert übernommen, im Original „Mehrweite" (s185.md, Prüfstelle 8).

## 7. Sollwert der Mehrweite im Armloch

Quelle: [`ocr_s185.md`](ocr_s185.md), Zeile 71 (Bereichsregel) und Zeile 75
(Tabellenüberschrift „Sollwert der Mehrweite"); [`tabellen_s185.md`](tabellen_s185.md),
Tabelle 4, Hinweis zur von der OCR nicht erfassten zweiten Zeile.

```text
Sie sollte min- bis zweifachen der destens dem ein- bis zweifachen der
Zugabe zur AIT entsprechen (siehe Auszug der Konstruktionstabelle unten).
```

```text
Sollwert der Mehrweite = 2 × Zugabe zur AlT (Toleranz +2 cm bis −1 cm)
= 2 × 1,3 = 2,6 cm
Nur bei Oberteilen mit Brustabnäher!
```

Hinweis: Die Rechnung „2 × 1,3 = 2,6 cm" ist **von Werner am Original
bestätigt** (s185.md, „Vorab geklärte..."). Diese zweite Tabellenzeile fehlt
in der OCR-Ausgabe von `tbl-3.md` vollständig; Wortlaut und Toleranzangabe
stammen aus `tabellen_s185.md` (dort als Werners Ergänzung zur OCR-Lücke
dokumentiert) und sind über die genannte Rechnung hinaus noch nicht separat
am Original bestätigt. Die erste Bereichsregel („min- bis zweifachen der
destens...") enthält laut s185.md (Prüfstelle 8) eine vermutlich doppelt
erfasste OCR-Passage („bis zweifachen der" zweimal ineinander verschachtelt)
– unverändert übernommen, nicht bereinigt.

## Nicht als Formel erfasst

- Tabelle 2 (`tbl-1.md`, [`tabellen_s185.md`](tabellen_s185.md)): reine
  Legende „TaAf = Taillenausfall", „HüFb = Hüftfehlbetrag" ohne Rechenwert.
- Abschnitt „2 Hintere Taillenabnäher" ([`ocr_s185.md`](ocr_s185.md), Zeile
  16–18): Konstruktionsanweisungen ohne Zahl/Rechenbeziehung.
- „4a Den HüAf senkrecht bis zur Saumlinie zeichnen." (Zeile 30): reine
  Zeichenanweisung, keine Rechenbeziehung.
- „Hüftbögen formen und die Seitennähte weiter senkrecht nach unten zur
  Saumlinie zeichnen." (Zeile 55): reine Zeichenanweisung.
- „Bei unerwünschter Mehrweite kann diese dort z.B. durch eine Englische
  Naht reduziert werden (siehe S. 376)." (Zeile 67): Verweis ohne eigene
  Rechenbeziehung.
- Vertikaler Reiter „Taillierter Oberteil-Grundschnitt": laut
  [[hofenbitzer-reiter-unwichtig]] keine Prüfstelle.
- Platzhalterkästen und Figurinen-Labels in `skizzen/s185_skizze_02.png`
  (BrP, vÄP, hÄP, VT, RT, „Konstruktionstabelle hier aufkleben!"): reine
  Bezeichnungen ohne Rechenbeziehung.
