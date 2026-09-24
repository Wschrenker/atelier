# Formeln s086 – fototreue Extraktion (teilweise bestätigt, teilweise Walking Skeleton)

**Bereitschaftsstufe:** Die Seite trägt weiterhin den Status
`OCR-Rohfassung – noch nicht menschlich verifiziert` ([s086.md](s086.md)). Nur die
drei in [s086.md](s086.md) unter „Vorab geklärte formel- und coderelevante
Stellen" genannten Punkte (Indizes `FaA_Hü`/`FaA_Ta`, Relation
`FaI = 2 × FaT`, Zahlen `100 cm : 22 ≈ 4,55 cm` und `74 cm : 22 ≈ 3,36 cm`)
sind am Original bestätigt. Für alle übrigen formel- und coderelevanten Stellen
dieser Seite (Konstruktionstabelle, Kontrolle der offenen Weite, Bereichsangabe
zur Abnähtiefe) liegt noch keine Bestätigung vor.

Werner hat für diesen Durchlauf ausdrücklich angewiesen, die Bereitschaftsprüfung
für die unbestätigten Stellen zu überspringen ("formeln seite 86 überspringe
die blocker. das ist ein walking skeleton."). Diese Extraktion erfasst daher
**alle** formel- und coderelevanten Stellen der Seite, markiert aber jede
einzeln als **bestätigt** oder **unbestätigt (Walking Skeleton)**. Grundlage
sind ausschließlich [ocr_s086.md](ocr_s086.md) und [tabellen_s086.md](tabellen_s086.md);
eine eigene Prüfung der Zeichnung `img-0.jpeg` bzw. der Skizzenausschnitte fand
im Rahmen dieses Walking-Skeleton-Durchlaufs nicht statt.

## 1. Faltenabstand an der Hüfte (FaA_Hü) — bestätigt

Quelle: [ocr_s086.md](ocr_s086.md), Zeilen 34–40. Index `FaA_Hü` und Ergebnis
`≈ 4,55 cm` laut [s086.md](s086.md) am Original bestätigt.

Bestätigte Fassung:

```text
Faltenabstand an der Hüfte (FaA_Hü)
HüW : Faltenanzahl (FaZ)
100 cm : 22
≈ 4,55 cm
```

Rohe OCR-Fassung (zum Beleg mitgeführt, nicht stillschweigend korrigiert):

```text
Faltenabstand an der Hüfte (FaA_{N2})
- HüW : Faltenanzahl (FaZ)
- 100cm : 22
= 4,54 cm
```

Hinweis: Die OCR liest den Index als „N2" statt „Hü" und das Ergebnis als
„4,54 cm" statt „≈ 4,55 cm". Rechnerisch ergibt 100 : 22 = 4,5454…, also
gerundet 4,55 cm — das stützt die bestätigte Fassung, nicht die OCR-Rohziffer.

## 2. Faltenabstand an der Taille (FaA_Ta) — bestätigt

Quelle: [ocr_s086.md](ocr_s086.md), Zeilen 42–48. Index `FaA_Ta` und Ergebnis
`≈ 3,36 cm` laut [s086.md](s086.md) am Original bestätigt.

Bestätigte Fassung:

```text
Faltenabstand an der Taille (FaA_Ta)
TaW : Faltenanzahl (FaZ)
74 cm : 22
≈ 3,36 cm
```

Rohe OCR-Fassung (zum Beleg mitgeführt, nicht stillschweigend korrigiert):

```text
Faltenabstand an der Taille (FaA_{N2})
- TaW : Faltenanzahl (FaZ)
- 74cm : 22
= 3,76 cm
```

Hinweis: Die OCR liest den Index hier ebenfalls als „N2" (uneinheitlich zur
Zeile 56, siehe Abschnitt 4) und das Ergebnis als „3,76 cm" statt „≈ 3,36 cm".
Rechnerisch ergibt 74 : 22 = 3,3636…, also gerundet 3,36 cm — das stützt die
bestätigte Fassung, nicht die OCR-Rohziffer.

## 3. Falteninhalt (FaI) — bestätigt

Quelle: [ocr_s086.md](ocr_s086.md), Zeile 70 (Schritt 4 unter „2 Falten
markieren"). Relation und Symbol laut [s086.md](s086.md) am Original
bestätigt: `FaI = 2 × FaT` (Gleichheitszeichen).

Bestätigte Fassung:

```text
4 Anschließend wird ein Falteninhalt (FaI = 2 × FaT) markiert.
```

Rohe OCR-Fassung (zum Beleg mitgeführt, nicht stillschweigend korrigiert):

```text
4 Anschließend wird ein Falteninhalt (FaI ≈ 2 × FaT) markiert.
```

Hinweis: Die OCR liest hier ein Näherungszeichen „≈" statt des am Original
bestätigten Gleichheitszeichens „=". Die bestätigte Fassung wird als
Buchfassung geführt.

## 4. „1 Berechnungen" – Schrittliste — unbestätigt (Walking Skeleton)

Quelle: [ocr_s086.md](ocr_s086.md), Zeilen 50–56.

```text
### 1 Berechnungen
Faltenanzahl (FaZ) festlegen.
Faltentiefe (FaT) (an der Hüfte) festlegen.
Faltenabstände an der Hüfte FaA_{N2} und an der Taille FaA_{N} errechnen.
```

Hinweis: unbestätigt. Indizes hier unverändert wie im OCR-Rohtext (`N2`/`N`)
übernommen; diese Zeile war nicht Gegenstand der bisherigen Bestätigung in
[s086.md](s086.md), auch wenn sie inhaltlich auf die Abschnitte 1–2 verweist.

## 5. Eingabewert FaZ = 22 (Normalfalten an der Hüfte) — unbestätigt (Walking Skeleton)

Quelle: [ocr_s086.md](ocr_s086.md), Zeile 14.

```text
Bei diesem Modell ist die Anzahl der Normalfalten an der Hüfte 22.
```

Hinweis: unbestätigt. Wird in den Abschnitten 1, 2 und 7 (ofW-Kontrolle) als
`FaZ` bzw. als Zahl 22 weiterverwendet.

## 6. Bereich zur Abnähtiefe der Falten unterhalb der Taille — unbestätigt (Walking Skeleton)

Quelle: [ocr_s086.md](ocr_s086.md), Zeile 10.

```text
Die Falten werden unterhalb der Taille ca. 12 bis 20 cm lang abgenäht.
```

Hinweis: unbestätigt. Bereichsangabe (`ca. 12 bis 20 cm`), keine feste Zahl.

## 7. Kontrolle der offenen Weite (ofW) — unbestätigt (Walking Skeleton)

Quelle: [ocr_s086.md](ocr_s086.md), Zeilen 82–86 (LaTeX-Array-Block der OCR,
hier als fließender Text wiedergegeben).

```text
### Kontrolle der offenen Weite
ofW = FaZ · FaT · 2 + HüW
= 22 · 9,2cm + 100cm
= 302,4cm
```

Hinweis: unbestätigt. Der Beispielwert `FaT = 9,2 cm` ist nur aus diesem
Rechenbeispiel ablesbar und an keiner anderen Stelle der Seite als `FaT`
definiert oder bestätigt. Rechnerisch nachvollzogen: 22 · 9,2 = 202,4;
202,4 + 100 = 302,4 — stimmt mit dem gedruckten Ergebnis überein.

## 8. Konstruktionstabelle (Tabelle 1) — unbestätigt (Walking Skeleton)

Quelle: [tabellen_s086.md](tabellen_s086.md), Zeilen 13–15.

```text
HÜU | Hüftumfang | 97 | +2,-3 | 3 = | Hüftweite | HÜW | 100 | ½ 50 | ¼ 25
TaU | Taillenumfang | 72 | +1,-2 | 2 = | Taillenweite | TaW | 74 | ½ 37 | ¼ 18,5
TaAf | Taillenausfall | ½ HÜW - ½ TaW = | | | | | | 13 | ½ 6,5
```

Hinweis: unbestätigt. Die Zeile `gBuU | gem. Bundumfang | --- | + | --- = |
Bundumfang | BuU | --- | ½ ---` (Tabelle 1, Zeile 16) enthält für dieses
Modell nur Platzhalter ohne Werte und wird deshalb nicht als Formel geführt.
Der abweichende Tabellenkopf „Proportionshemmelse" (statt „Proportionsmaße")
ist bereits in [tabellen_s086.md](tabellen_s086.md) dokumentiert und wird hier
nicht erneut aufgelöst.

## Nicht als Formel erfasst

- Zeilen 8–9, 14 (erster Satz), 16, 18 (Fließtext zu Faltenarten, Lagenzahl
  des Stoffs „dreifach", „fünffach", „einfach"): beschreibende Aussagen ohne
  eigene Rechenbeziehung über die oben erfassten Stellen hinaus.
- Zeilen 22–26 (Hinweise zur Einzelanfertigung ohne Papierschnitt, Markieren,
  Ansetzen von Stoffbahnen): keine Zahl, keine Rechenbeziehung.
- Schrittliste „2 Falten markieren" (Zeilen 60–80) außer dem bereits erfassten
  Falteninhalt-Satz in Abschnitt 3: reine Handlungsanweisungen ohne eigene
  Zahl oder Rechenbeziehung.
- Zeilen 88–130 (Kontrollsatz „Alle Linien auf rechte Winkel und Parallelität
  kontrollieren" sowie die Textfetzen ab „Rundum / Modell"): Letztere gehören
  laut [s086.md](s086.md) nicht zu Seite 86, sondern zur mitfotografierten
  Nachbarseite, und werden hier nicht als Formel geführt.
