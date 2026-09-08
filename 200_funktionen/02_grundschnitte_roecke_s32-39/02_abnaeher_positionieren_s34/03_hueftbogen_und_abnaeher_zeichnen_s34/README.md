# Hüftbogen und Abnäher — S. 34

**Status:** Python-Vertrag umgesetzt; Schritte 16–18 grün.

## Zweck

Die beiden Hüftbogen-Endpunkte, die vordere Abnähermitte über `TaU : 10`, die
hintere Abnähermitte als echten Mittelpunkt sowie Abnäherschenkel und -spitzen
konstruieren. Alle Werte bleiben intern ungerundet in Millimetern.

## Belege

- [`s34.md`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/s34.md), Schritte 16–18
- [`Foto S. 34`](../../../../100_quellen/20_hofenbitzer_band_1_bilder/1.1_Photos_hofenb_ba1_total/s34.jpg)
- [`HOF-B1-S034-F05`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s34_normalisiert.md)
- [`Punkte und Vektoren`](../../../../400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md)

## Vertrag und Grenze

- Hüftabstich wird an P10 exakt halbiert.
- Vordere Länge: `80–100 mm`; hintere Länge: `130–160 mm`.
- Inhalte werden symmetrisch auf beide Schenkel verteilt.
- `0 mm` Inhalt erzeugt keinen Scheinabnäher.
- Über `45 mm` hinten stoppt zugunsten der Konstruktion auf S. 35.
- Die körperabhängige Hüftbogenkurve bleibt `offen_bis_s36`; die Taillennaht
  bleibt `offen_bis_s35`. Der Vertrag erfindet keine Kurve.

## Prüfung

```text
python test_hueftbogen_und_abnaeher.py
```
