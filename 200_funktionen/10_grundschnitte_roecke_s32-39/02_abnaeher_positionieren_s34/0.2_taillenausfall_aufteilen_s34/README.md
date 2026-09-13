# Taillenausfall aufteilen — S. 34

**Status:** Python-Vertrag umgesetzt; Schritte 13–15 grün.

## Zweck

Den Taillenausfall in Hüftabstich, vorderen Abnäher und hinteren Restbetrag
aufteilen. Die Hüftform wird ausdrücklich gewählt; bei flacher oder starker
Hüftrundung bleibt auch die Korrektur `10–15 mm` eine sichtbare Entscheidung.

## Belege

- [`s34.md`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/s34.md), Schritte 13–15
- [`Foto S. 34`](../../../../100_quellen/20_hofenbitzer_band_1_bilder/1.1_Photos_hofenb_ba1_total/s34.jpg)
- [`HOF-B1-S034-F01/F03/F04`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s34_normalisiert.md)
- [`Parameterketten`](../../../../400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md)

## Grenze

Der vordere Inhalt wird nicht aus der Figur geraten. Der Vertrag akzeptiert die
Vereinigung der belegten Angaben: `0 mm` oder `10–25 mm`. Der hintere Inhalt ist
der reine Restbetrag. Über `45 mm` meldet der Status, dass S. 35 mit zwei
hinteren Abnähern erforderlich ist; eine Aufteilung wird hier nicht erfunden.

## Prüfung

```text
python test_taillenausfall_aufteilen.py
```
