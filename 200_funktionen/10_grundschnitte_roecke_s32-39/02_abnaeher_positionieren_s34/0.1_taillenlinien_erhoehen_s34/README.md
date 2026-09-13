# Erhöhte Taillenlinien — S. 34

**Status:** Python-Vertrag umgesetzt; Schritte 10–12 grün.

## Zweck

Aus P7, der Seitenrichtung und der Taillenrichtung P10 bilden. Die
Seitenlinien-Erhöhung wird mit `10–15 mm`, die vordere Abnähererhöhung mit
`5–7 mm` als ausdrückliche Eingabe geführt. Die hintere Erhöhung entsteht intern
ungerundet als exakt ein Drittel der Seitenlinien-Erhöhung.

## Belege

- [`s34.md`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/s34.md), Schritte 10–12
- [`Foto S. 34`](../../../../100_quellen/20_hofenbitzer_band_1_bilder/1.1_Photos_hofenb_ba1_total/s34.jpg)
- [`HOF-B1-S034-F02`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s34_normalisiert.md)
- [`Numerik`](../../../../400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md)
- [`Punkte und Vektoren`](../../../../400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md)

## Grenze

Die Buchangabe „ca. 6 cm nach links und rechts“ definiert keine exakte
Segmentlänge. Der Vertrag liefert deshalb P10 sowie parallele Richtungs- und
Erhöhungsdaten, aber keine erfundene Linienlänge. Nicht endliche, entartete oder
nicht rechtwinklige Geometrie stoppt typisiert.

## Prüfung

```text
python test_taillenlinien_erhoehen.py
```
