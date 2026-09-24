# Formeln s090 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s090.md](s090.md)). Nur die in `s090.md` vorab geklärten Stellen
(Radiusvariablen `r_AnW`, `r_SaW` sowie die Gruppierung der SaW-Formel für □2)
sind bislang von Werner am Original bestätigt; alle übrigen Stellen dieser
Seite sind ungeprüft. Diese Extraktion wurde auf ausdrücklichen Wunsch Werners
trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker übersprungen) und
beruht auf [`ocr_s090.md`](ocr_s090.md) sowie den Berechnungsboxen in
[`skizzen/s090_skizze_02.png`](skizzen/s090_skizze_02.png) (□1) und
[`skizzen/s090_skizze_03.png`](skizzen/s090_skizze_03.png) (□2). Sie ersetzt
keine spätere Bestätigung der übrigen formelrelevanten Stellen am Original und
darf nicht als menschlich verifiziert gelten.

## 1. Volant aus einem Vollkreis (□1) – Radius- und Saumweitenberechnung

Quelle: Berechnungsbox in
[`skizzen/s090_skizze_02.png`](skizzen/s090_skizze_02.png), zeichnungsgebunden.
Dieser Rechenweg erscheint laut [s090.md](s090.md) nicht als eigener OCR-Text
in `ocr_s090.md`.

```text
r_AnW = AnW : (2 · π)
      = 118 cm : (2 · 3,14)
      = 18,8 cm

r_SaW = r_AnW + VoB
      = 18,8 cm + 20 cm
      = 38,8 cm

SaW = 2 · π · r_SaW
    = 2 · 3,14 · 38,8 cm
    = 244 cm
```

Zusätzliche Beschriftungen derselben Box (Bildbeleg, ungeprüft): „innerer
Umfang = Ansatzweite (AnW)", „äußerer Umfang = Saumweite (SaW)",
„Volantbreite (VoB)", „Volant 1× zuschneiden".

## 2. Volant aus zwei Vollkreisen (□2) – Radius- und Saumweitenberechnung

Quelle: `ocr_s090.md`, Zeilen 39–51 (Abschnitt „Berechnungen"), zusätzlich als
Bildbeleg die Berechnungsbox in
[`skizzen/s090_skizze_03.png`](skizzen/s090_skizze_03.png), zeichnungsgebunden.

```text
r_awW = (AnW + NZg) : (2 · π) : 2
      = (118 cm + 2 cm) : (2 · 3,14) : 2
      = 9,6 cm

r_SaW = r_awW + VoB
      = 9,6 cm + 20 cm
      = 29,6 cm

SaW = (2 · π · r_SaW) − NZg · 2
    = (2 · 3,14 · 29,6 cm) − 2 cm · 2
    = 368 cm
```

Hinweis: Die OCR-Schreibweise „r_awW" ist unverändert aus `ocr_s090.md`
übernommen. Die Berechnungsbox in `s090_skizze_03.png` zeigt an derselben
Stelle eindeutig „r_AnW" (Bildbeleg); laut [s090.md](s090.md) hat Werner
bereits die Variablennamen `r_AnW` und `r_SaW` am Original bestätigt. Die
Klammerung der SaW-Zeile ist wie gedruckt mehrdeutig (ließe sich auch als
`(2 · π · r_SaW) − (NZg · 2)` lesen); laut [s090.md](s090.md) hat Werner die
Gruppierung `((2 × π × r_SaW) − NZg) × 2 = 368 cm` bereits als eindeutig
bestätigt.

Zusätzliche Beschriftungen derselben Box (Bildbeleg, ungeprüft): „innerer
Umfang = ½ Ansatzweite (AnW) + 2× NZg", „äußerer Umfang = ½ Saumweite (SaW) +
2× NZg", „NZg = 2×1 cm = 2 cm", „Volant 2× zuschneiden".

## 3. Nahtzugabe bei mehreren Kreisringen

Quelle: `ocr_s090.md`, Zeile 37.

```text
2 × 1 cm = 2 cm
```

Hinweis: Bezieht sich laut Fließtext auf die Nahtzugabe, die zur Ansatzweite
addiert werden muss, wenn mehrere Kreisringe eingeschnitten und
zusammengenäht werden. Das Ergebnis „2 cm" entspricht dem `NZg` aus Formel 2.

## Nicht als Formel erfasst

- Schritte 1–4 unter „Volants durch Kreiskonstruktion" (Zeilen 30–33 in
  `ocr_s090.md`): Handlungsanweisungen ohne eigene Rechenbeziehung.
- Bildunterschriften □1 und □2 (Zeilen 10, 55–57 in `ocr_s090.md`): reine
  Modellbezeichnungen ohne Zahlenwert.
- Fließtext zu Volant-Herkunft und -Gestaltung (Zeilen 14–24 in
  `ocr_s090.md`): keine Zahl, keine Rechenbeziehung.
- Textfetzen der Nachbarseite (Zeilen 63–77 in `ocr_s090.md`): laut
  [s090.md](s090.md) nicht Inhalt dieser Seite.
