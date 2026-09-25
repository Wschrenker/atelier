# Formeln s202 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert` ([s202.md](s202.md)).
Nur eine einzige Rechenstelle ist bisher von Werner am Original bestätigt
(siehe Abschnitt 3, „bereits bestätigte Stelle"). Diese Extraktion wurde auf
ausdrücklichen Wunsch Werners trotzdem als Walking-Skeleton-Durchlauf erstellt
(Blocker übersprungen) und beruht auf [`ocr_s202.md`](ocr_s202.md),
[`tabellen_s202.md`](tabellen_s202.md) und [`skizzen_s202.json`](skizzen_s202.json).
Sie ersetzt keine spätere Bestätigung der übrigen formelrelevanten Stellen am
Original und darf nicht als menschlich verifiziert gelten.

## 1. Konstruktionstabelle (Berechnungstabelle-Bezug)

Quelle: [`tabellen_s202.md`](tabellen_s202.md), Zeilen 10–19 (Rohtext, OCR,
mit Umlaut-Kodierungsfehlern `�`).

```text
ÄL | Ärmellänge | 60 ± 0 = Ärmellänge ÄL | 60
```

```text
OaU | Oberarmumfang | 28 + 9 = Oberarmweite OaW | 37
```

```text
HgU | Handgelenkumfang | 16 + --- = Saumweite �SaW | - OaW
```

Hinweis: Diese Zeile ist im Rohtext lückenhaft (fehlender zweiter Operand,
Zielfeld „- OaW" statt eines Zahlenwerts). Laut `s202.md` könnte die richtige
Lesung „ÄSaW | = OaW" lauten; nicht bestätigt, hier unverändert als Rohtext
belegt.

```text
AbH | Ärmlochhöhe | --- ... Ärmlochumfang | ÄlU | 43,5
```

```text
EW in % | Einhalteweite in % | 3 % | Einhalteweite in cm = ÄlU · Einhalteweite in % | EW in cm | 1,3 cm
```

```text
Ärmelkugelumfang = ÄlU + Einhalteweite in cm | ÄKLI | 44,6
```

Hinweis: Laut `s202.md` könnte die richtige Lesung „ÄKU 44,8" statt
„ÄKLI 44,6" sein; nicht bestätigt. Beide Fassungen werden hier nebeneinander
als Bildbeleg festgehalten, keine wird stillschweigend gewählt.

Hinweis: Die erste Tabellenzeile mit „Größe | 28" (laut `s202.md` eventuell
„38") sowie „PN | 5" (eventuell „PK") sind Bezeichnungs-/Größenfelder ohne
eigene Rechenbeziehung und werden hier nicht als Formel geführt.

## 2. Grundgerüst (Schritt 3–8)

Quelle: [`ocr_s202.md`](ocr_s202.md), Zeilen 24–32 (Schrittfließtext).

```text
3 Die OaW + 0 bis 2 cm waagerecht abtragen.
```

```text
4 Vorne den vAIU - 0 cm bis - 1 cm als Kreisbogen zeichnen.
```

```text
5 Die hintere Linie mit hAIU - 0 bis - 1 cm auf den Bogen abtragen und zeichnen. Dann vorne die vordere Linie auf den Schnittpunkt zeichnen.
```

```text
6 Vom Schnittpunkt (SuP) die ÄL
7 und 60% der ÄL abtragen.
8 Rechtwinklig die Saum-, Ellenbogen- und Seitenlinien abwinkeln.
```

Zeichnungsgebunden, Quelle: [`skizzen_s202.json`](skizzen_s202.json), Region
`img-1.jpeg` (Skizze 2, „□3 Grundgerüst"):

```text
60 % ÄL = 60 cm · 0,60 = 36 cm
```

Hinweis: Dieses gedruckte Rechenbeispiel verwendet den Tabellenwert
ÄL = 60 cm (Abschnitt 1) und ist rechnerisch stimmig (60 · 0,60 = 36). In
derselben Skizze steht zusätzlich ein Wert „37 cm" bei „ÄkLi/Ärmelkugellinie"
– ob dies derselbe Wert wie OaW = 37 cm ist oder eine eigene ÄkLi-Messung,
ist eine offene Prüfstelle (siehe Abschnitt 3).

## 3. Hilfslinien für die Ärmelkugel (Schritt 9–14)

Quelle: [`ocr_s202.md`](ocr_s202.md), Zeilen 34–41 (Schrittfließtext).

```text
9 ☐4 Die ÄkLi messen → = OaW + Zugabe
```

```text
10 und ÄkLi : 8 vom SuP nach vorne (links) abtragen.
```

```text
11 ÄkLi : 5 nach hinten (rechts) abtragen.
```

```text
12 Vorne auf der ÄkLi die ÄkLi : 12 markieren und zu P10 und
13 hinten ÄkLi : 14 abtragen und Hilfslinien zu P11 zeichnen.
```

```text
14 Von P10 und P11 auf die unteren Linien abwinkeln.
```

Zeichnungsgebunden, Quelle: [`skizzen_s202.json`](skizzen_s202.json), Region
`img-2.jpeg` (Skizze 3, „□4 Hilfslinien"):

```text
ÄkLi : 8 = 4,6 cm
ÄkLi : 5 = 7,4 cm
ÄkLi : 12 = 3,1 cm
ÄkLi : 14 = 2,4 cm
```

**Bereits bestätigte Stelle** (`s202.md`, Abschnitt „Vorab geklärte formel-
und coderelevante Stellen", bestätigt am 2026-09-24): Die vierte Zeile
`ÄkLi : 14 = 2,4 cm` ist als gedruckter Rechenfehler erkannt. Bildlesung der
Buchangabe: `37 cm : 14 = 2,4 cm`. Bestätigte fachliche Arbeitslesung:
`37 cm : 14 = 2,642857… cm ≈ 2,6 cm`. Der gedruckte Wert `2,4 cm` bleibt hier
unverändert als Bildbeleg stehen; die Bestätigung betrifft nur diese eine
Rechenstelle.

Hinweis zu den übrigen drei Werten: `4,6 cm`, `7,4 cm` und `3,1 cm` sind noch
nicht einzeln von Werner am Original bestätigt (offene Prüfstelle, `s202.md`
Punkt 3). Sie passen rechnerisch zu einem ÄkLi-Wert von 37 cm
(37 : 8 = 4,625 ≈ 4,6; 37 : 5 = 7,4; 37 : 12 = 3,08… ≈ 3,1), was mit dem
Bildbeleg der bereits bestätigten Stelle übereinstimmt; dies ist eine
Beobachtung, keine Bestätigung der Einzelwerte.

## 4. Ärmelkugelformen (Schritt 15)

Quelle: [`ocr_s202.md`](ocr_s202.md), Zeilen 43–47.

```text
15 ☐S Die vordere (vÄk) und hintere (hÄk) Ärmelkugel ungefähr über die Nitten der Winkellinien und mit Hilfe der Kurvenrichtungen formen.
```

Hinweis: Keine Rechenbeziehung – das Formen der Kurve erfolgt laut Buchtext
freihändig anhand von Bezugspunkten und Kurvenrichtungen, ohne angegebene
Formel. Hier nicht als Formel geführt; keine Kurve oder Geometrie wird
ergänzt. „Nitten" laut `s202.md` vermutlich OCR-Fehler für „Mitten"
(unbestätigt, unverändert übernommen).

## Nicht als Formel erfasst

- Schritt 1 (Zeile 21): Messanweisungen für vAlU, hAlU, vAchsel, hAchsel –
  reine Messvorgänge ohne Rechenbeziehung auf dieser Seite.
- Schritt 2 (Zeile 22): Verweist auf das Eintragen der Tabellenwerte, ohne
  eigene Rechenbeziehung über Abschnitt 1 hinaus.
- Skizze 1 (`img-0.jpeg`, „□1 Ärmloch"): Die dort beschrifteten Maße
  (vAlU 19,6 cm, hAlU 23,9 cm, vAchsel 4,5 cm, hAchsel 8,6 cm) sind isolierte
  Messwerte ohne erkennbare Rechenbeziehung auf dieser Seite.
- Vertikale Reiterbeschriftung „Weiter Ärmel für legere Modelle" und
  Seitenzahl „202": keine Formel.
- Mitfotografierter Streifen der Nachbarseite 203 („We / Kon / Struktur
  (vÄl) / 4,5 / 4,5", Zeilen 53–59): laut `s202.md` fremder Inhalt,
  ausgeschlossen.
