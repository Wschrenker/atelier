# Formeln s186 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s186.md](s186.md)). Nur die dort unter „Vorab geklärte formel- und
coderelevante Stellen" gelisteten Einzelpunkte sind von Werner am Original
bestätigt (Plus-/Gleichheitszeichen bei `ArD+`, die beiden Formeltexte
`TaB − ½ TaW` und `HüB − ½ HüW`, das Zeichen `ν₂ = ½`, die Rechnung
`4,5 cm : 2 = 2,25 cm ≈ 2,3 cm` sowie `46,5 − 50,5 = −4` in der kleinen
Tabelle). Alle übrigen Kürzel, Bezeichnungen, Zahlenwerte und Zeichnungslabels
dieser Seite sind laut den offenen Prüfstellen 1–7 in `s186.md` noch **nicht**
bestätigt. Diese Extraktion wurde auf ausdrücklichen Wunsch Werners trotzdem
als Walking-Skeleton-Durchlauf erstellt (Blocker übersprungen) und beruht auf
[`ocr_s186.md`](ocr_s186.md), [`tabellen_s186.md`](tabellen_s186.md) und dem
Skizzenausschnitt [`skizzen/s186_skizze_01.png`](skizzen/s186_skizze_01.png).
Sie ersetzt keine spätere Bestätigung der offenen Stellen und darf nicht als
menschlich verifiziert gelten.

## 1. Konstruktionstabelle – Grundmaß + Zugabe = Konstruktionsmaß

Quelle: `tabellen_s186.md`, Tabelle 1 (`tbl-0.md`), Zeilen 11–21.

```text
KOH  Körperhöhe                168
BHJ  Brustumfang                88  6 →  BrW    94   ½ 47
TAU  Taillenumfang              72  4 →  TaW    76   ½ 38
HGU  Haftumfang                 97  4 →  HüW   101   ½ 50,5
ALT  Armüschnärh               201  1,3 → ALT+  21,4
HUT  Hüftnerh                   21              Brut  Modelllänge  95
BFT  Brusthefe als blüden      28,1             Hüb   Häldischbreite  6,5
RUB  Rückenbreite (½)          16,5  0,5 → RUB+  17
ArD  Armdurchmesser             9,3  1,5 → ArD+  10,8  ¼ 4,7  1½ 3,6
BrB  Brustbreite (½)           18,2  1   → BrB+  19,2
—    Kontrolle Σ = ½ BrU        44  3   → ½ BrW  47
```

Hinweise:

- Die Kürzel- und Bezeichnungsspalte ist laut `s186.md` überwiegend verlesen
  (Prüfstelle 2) und hier unverändert aus der OCR übernommen; keine Korrektur.
- Das OCR-Zeichen „→" steht in dieser Tabelle für zwei getrennte, im Original
  unterschiedene Rechenzeichen (Plus und Gleich), siehe `s186.md`,
  Anmerkungen zur OCR-Eingabe.
- Für `ArD+ = 10,8 cm` ist laut `s186.md` (Vorab geklärte Stellen) am Original
  bestätigt: `¼ = 2,7 cm` und `⅓ = 3,6 cm`. Die OCR-Rohwerte „¼ 4,7" und
  „1½ 3,6" in der letzten Spalte weichen davon ab und werden hier zusätzlich
  als Rohbeleg stehen gelassen, nicht ersetzt.
- Alle übrigen Bruchteilspalten (½ 47 / ½ 38 / ½ 50,5 / ½ 47) sind noch nicht
  einzeln am Original bestätigt (Prüfstelle 2).
- Zeile „ALT 201 1,3 → ALT+ 21,4": Grundwert „201" wirkt im Vergleich zu den
  übrigen Werten unplausibel groß; fototreu unverändert aus der OCR
  übernommen, nicht korrigiert.

## 2. Taillenbreite (TaB) = vTaB + hTaB

Quelle: `ocr_s186.md`, Zeilen 29–30 (Schritt 9, Fließtext) und Skizze
`skizzen/s186_skizze_01.png` (Label „vTaB + hTaB = TaB" auf der Taillenlinie,
zeichnungsgebunden).

```text
Die Abstände an der Taillenlinie von der vlk zur Seiten-linie messen - vTaB
und von der Seitenlinie zur hA messen - hTaB.
Beide addieren = Taillenbreite (TaB)
```

```text
vTaB + hTaB = TaB
```

Hinweis: „vlk" und „hA" sind laut `s186.md` (Prüfstelle 3) vermutlich „vM" und
„hM"; hier unverändert aus der OCR übernommen, nicht korrigiert.

## 3. Taillenausfall (TaAf)

Quelle: `ocr_s186.md`, Zeilen 32–36.

```text
Taillenausfall (TaAf)

= TaB − ½ TaW
= 46,2 cm − 38,5 cm
= 7,7 cm
```

Hinweis: Die Formel steht in der OCR-Rohfassung als `\(= \mathrm{TAB} - 1\%
\mathrm{TaW}\)`; die Schreibweise „½" ist laut `s186.md` (Vorab geklärte
Stellen: „Die Formeln lauten `TaB − ½ TaW` …") am Original bestätigt und hier
verwendet. Die Zahlenwerte 46,2 cm und 38,5 cm stehen unverändert wie in der
OCR.

## 4. Verteilung des Taillenausfalls (Schritt 9, Beispielrechnung)

Quelle: `ocr_s186.md`, Zeilen 40–48 (Fließtext und Aufzählung) sowie Skizze
`skizzen/s186_skizze_01.png` (Bereichsangaben und Beispielwerte an den vier
Abnähern/Nähten, zeichnungsgebunden).

```text
Die Taille an den Seitenlinien um 1 cm erhöhen und dort jeweils 0 bis 2 cm
einstellen und die oberen Seitennähte (SN) gerade zu den Armbüchern zeichnen.
Den Taillen-ausfall auf die entsprechenden Abnäherpositionen am Schnitt
verteilen und die Abnäher zeichnen.

Bei diesem Beispiel:

1 SN 2×1cm = 2cm
2 vAbI = 2 cm
3 optional shAbI hier = 0 cm
4 hAbI = 3,7 cm
Summe des Ausfalls = 7,7 cm
```

```text
vAbI:  0 bis maximal 2,5 cm      (Beispielwert: 2 cm)
an SN: ca. 0 bis 2 cm            (Beispielwert: je 1 cm beidseitig)
shAbI: ca. 0 bis 3 cm            (Beispielwert: 0 cm)
hAbI:  ca. 2 bis 4,5 cm          (Beispielwert: 3,7 cm)
SN 2×1cm = 2cm + vAbI 2cm + shAbI 0cm + hAbI 3,7cm = Summe des Ausfalls 7,7cm
```

Hinweise:

- Die Bereichsangaben `vAbI 0 bis maximal 2,5 cm`, `an SN ca. 0 bis 2 cm`,
  `shAbI ca. 0 bis 3 cm`, `hAbI ca. 2 bis 4,5 cm` stammen aus dem
  Skizzenausschnitt, nicht aus dem OCR-Fließtext; direkt am Bild abgelesen.
  Laut `s186.md` (Prüfstelle 6) sind sie noch nicht am Original bestätigt.
- Die Beispielsumme `2 + 2 + 0 + 3,7 = 7,7 cm` entspricht dem TaAf-Ergebnis
  aus Abschnitt 3; unabhängig nachgerechnet, siehe
  [`formeln_s186_normalisiert.md`](formeln_s186_normalisiert.md).
- Die eingekreisten Zahlen 1–4 vor jeder Aufzählungszeile stehen laut
  `s186.md` im Rohtext nur als einfache Ziffern ohne Kreis-Symbol; laut
  Prüfstelle 4 noch zu bestätigen, ob im Original ein Kreissymbol steht.

## 5. Hüftbreite (HüB) = vHüB + hHüB

Quelle: `ocr_s186.md`, Zeile 52 (Schritt 10, Fließtext) und Skizze
`skizzen/s186_skizze_01.png` (Label „+ hHüB = HüB" auf der Hüftlinie,
zeichnungsgebunden).

```text
V HUB und hHUB messen und addieren = Hufbreite (HUB).
```

```text
vHüB + hHüB = HüB
```

Hinweis: OCR-Schreibweisen „V HUB", „hHUB", „Hufbreite (HUB)" unverändert
übernommen, nicht korrigiert; die Skizze selbst beschriftet die Punkte klar
als `vHüB` und `hHüB` mit Ergebnis `HüB`.

## 6. Hüft-Fehlbetrag (HüFb)

Quelle: `ocr_s186.md`, Zeilen 55–59.

```text
Hüft-Fehlbetrag (HüFb)

= HüB − ½ HüW
= 46,5 cm − 51 cm
= −4,5 cm → 4,5 cm   ν₂ = 2,2 cm
```

```text
Jeweils den halben HüFb (hier 2,2 cm) an den Seitenlinien ausstellen.
```

Hinweise:

- Die Formel steht in der OCR-Rohfassung als `\(= \mathrm{HUB} - 1\%
  \mathrm{HUW}\)`; die Schreibweise „½" ist laut `s186.md` (Vorab geklärte
  Stellen) am Original bestätigt.
- `ν₂` ist laut `s186.md` (Vorab geklärte Stellen) als Zeichen für „½"
  bestätigt, hier also `ν₂ = ½ HüFb`.
- Der Zahlenwert „2,2 cm" steht so in der OCR-Rohfassung und im
  nachfolgenden Fließtextsatz zweimal übereinstimmend; unverändert
  übernommen. Werner hat unabhängig davon in `s186.md` (Vorab geklärte
  Stellen) vermerkt: „Rechnerisch gilt 4,5 cm : 2 = 2,25 cm ≈ 2,3 cm" – diese
  Abweichung zwischen gedrucktem Wert und Nachrechnung wird nicht still
  aufgelöst, siehe [`formeln_s186_normalisiert.md`](formeln_s186_normalisiert.md).
- Die Skizze beschriftet den Wert an beiden Seitenlinien der Hüftlinie
  übereinstimmend mit „2,2 cm" (zweimal, an den Kreiszahlen 42).

## 7. Kleine Kontrolltabelle (TaAf/HüFb)

Quelle: `tabellen_s186.md`, Tabelle 2 (`tbl-1.md`) und Tabelle 3 (`tbl-2.md`).
Laut `s186.md` (Anmerkungen zur OCR-Eingabe) handelt es sich im gedruckten
Buch um eine einzige zusammenhängende Tabelle, die die OCR in zwei Blöcke
aufgespalten hat.

```text
TaAf   Taillenumfang
HüFb   Häldischbetrag

Brustmenge (A)     46    → ½ TaW  38    → 8
Armückmenge (AB)   46,5  → ½ HüW  50,5  → 4
```

Hinweise:

- Die Bezeichnungen „Taillenumfang", „Häldischbetrag", „Brustmenge (A)" und
  „Armückmenge (AB)" wirken laut `s186.md` (Bekannte auffällige Stellen)
  verlesen (vermutlich „Taillenausfall", „Hüftfehlbetrag", „gemessene TaB",
  „gemessene HüB"); hier unverändert aus der OCR übernommen.
- Für die zweite Zeile ist laut `s186.md` (Vorab geklärte Stellen) am
  Original bestätigt: `46,5 − 50,5 = −4` (Ergebnisspalte trägt im Original
  ein Minuszeichen, das die OCR als „4" ohne Vorzeichen wiedergegeben hat).
  Das Vorzeichen der ersten Zeile (`46 − 38 = 8`) ist nicht Teil dieser
  Bestätigung und bleibt offen.

## 8. Weitere Maßangaben aus der Zeichnung (ohne eigene Formel)

Quelle: Skizze `skizzen/s186_skizze_01.png`, zeichnungsgebunden, nicht im
OCR-Fließtext.

```text
Abnäher 1,5 cm zulegen
Doppelknips an hÄP 1 cm nach oben markieren
ca. 12 cm   (Abnäherlänge vAbI, senkrecht ab Taillenlinie Richtung Saum)
ca. 13 bis 16 cm   (Abnäherlänge hAbI, senkrecht ab Taillenlinie Richtung Saum)
```

Hinweis: Diese vier Werte sind eigenständige Konstruktionsmaße ohne erkennbare
Rechenbeziehung zu den übrigen Formeln dieser Seite; als Rohwerte erfasst,
laut `s186.md` (Prüfstelle 6) noch nicht am Original bestätigt.

## Nicht als Formel erfasst

- Kreiszahlen 35–43 in der Zeichnung: reine Punkt-/Schrittmarkierungen ohne
  eigenen Zahlenwert.
- Punktlabels BrP, vÄP, hÄP sowie die Linienbezeichnungen (Brustlinie,
  Taillenlinie, Hüftlinie, Saumlinie, Seitenlinie, hintere Armlinie,
  Schulterblattlinie, hintere Abnähermitte, hintere Mitte (hM), vM):
  Bezeichnungen ohne Rechenbeziehung.
- Bildunterschrift „☐2 Taillierung am Oberteil-GS ohne Hüftausfall" und
  Ausschnittstitel „☐1 Ausschnitt aus der Konstruktionsabelle (TaU der
  Größe 38 nach der Größentabelle)": Bildverweise ohne Zahlenwert.
- `ocr_s186.md`, Zeile 21–23 (Fließtext zum Vergleich mit Seite 184 und zur
  Entstehung der Taillierung ab P31): erklärender Text ohne eigene
  Rechenbeziehung auf dieser Seite.
- `ocr_s186.md`, Zeile 63 („Hüftbögen formen, dann die Seitennähte nach unten
  senkrecht zur Saumlinie zeichnen."): Konstruktionsanweisung ohne Zahlenwert.
