# Formeln s039 – fototreue Extraktion (Walking Skeleton)

Quelle: [ocr_s039.md](ocr_s039.md), OCR-Rohfassung. Nur die mit „bestätigt“
gekennzeichnete Stelle ist am Original durch Werner geprüft (siehe
[s039.md](s039.md), Abschnitt „Vorab geklärte formel- und coderelevante
Stellen“). Alle übrigen Stellen stammen ausschließlich aus der OCR-Rohfassung
und sind noch nicht am Original bestätigt. Es wird nichts ergänzt, was nicht im
OCR-Text steht.

## 1. Bundlänge zu Taillenumfang

Quelle: ocr_s039.md, Zeile 17. Status: nur OCR, nicht bestätigt.

```text
Bundlänge ≈ Taillenumfang
```

Hinweis: „ca. dem Taillenumfang entsprechend“, kein fester Wert.

## 2. Bundbreite (Höhe des Rechtecks)

Quelle: ocr_s039.md, Zeile 19. Status: nur OCR, nicht bestätigt.

```text
Bundlänge ≈ Talz
Bundbreite = 2 bis 5 cm
```

Hinweis: „Talz“ steht so in der OCR-Rohfassung; ob das ein OCR-Fehler für
„TaU“ ist, ist ungeklärt und wird hier nicht still korrigiert. Bundbreite als
Bereich, kein fester Wert.

## 3. vM als Mitte der Bundlänge

Quelle: ocr_s039.md, Zeile 27. Status: nur OCR, nicht bestätigt.
Zeichnungsbezug: Bundrechteck, siehe img-0/img-1 bzw.
[skizzen_s039.json](skizzen_s039.json); Skizzenlabels selbst noch nicht erfasst.

```text
vM = Bundlänge : 2
```

## 4. Taillennahtlängen zu Taillenweite

Quelle: ocr_s039.md, Zeile 31 und 33. Status: nur OCR, nicht bestätigt.

```text
Nahtstrecken der vorderen Taillennaht und der hinteren Taillennaht
(jeweils ohne Abnäherinhalte) messen.
Die Taillennahtlängen entsprechen der halben Taillenweite.
```

Hinweis: Der Buchtext benennt hier weder „TaU“ noch, ob sich „die halbe
Taillenweite“ auf vordere und hintere Nahtlänge einzeln oder gemeinsam
bezieht; das wird hier nicht aufgelöst.

## 5. Überschneidungsbetrag / Taillenmehrweite (Sollbereich)

Quelle: ocr_s039.md, Zeile 45. Status: nur OCR, nicht bestätigt.

```text
Taillenmehrweite ≈ 1 bis 1,5 cm
```

## 6. Kontrolle der Taillenmehrweite (bestätigt)

Quelle: ocr_s039.md, Zeile 51–53; identisch übernommen aus
[s039.md](s039.md), Abschnitt „Vorab geklärte formel- und coderelevante
Stellen“. Status: **bestätigt** (Variable `hTaN` und diese Kontrollrechnung).

```text
= vTaN + hTaN − TaU : 2
= 19,7 + 17,5 cm − 36,0 cm
= 1,2 cm Einhalteweite
```

## 7. Fehlerschwelle der Taillenmehrweite

Quelle: ocr_s039.md, Zeile 55. Status: nur OCR, nicht bestätigt.

```text
Taillenmehrweite > 1,5 cm ⇒ Anzeichen für Fehler (z. B. Rockkonstruktion oder Fehlmessung)
```

Hinweis: Buchtext verlangt in diesem Fall, den Fehler zu identifizieren und zu
berichtigen; kein Rechenweg dafür angegeben.
