# Grundgerüst zeichnen — S. 33

**Status:** Python-Vertrag umgesetzt; P1–P9 und Geometriegrenzen grün.

## Zweck

Das rechteckige Grundgerüst P1–P9 aus Modelllänge, Hüfttiefe und halber
Hüftweite erzeugen. Es ist Referenzgeometrie, noch kein fertiger Schnitt.

## Geometrischer Vertrag

Engine-Koordinaten: X nach rechts, Y nach unten; intern Millimeter.
Mit P1 als Ursprung gilt:

```text
P2 = (0, Modelllänge)
P3 = (0, Hüfttiefe)
P4 = (½ Hüftweite, 0)
P5 = (½ Hüftweite, Modelllänge)
P6 = (½ Hüftweite, Hüfttiefe)
P7 = Mittelpunkt(P1, P4)
P8 = Mittelpunkt(P2, P5)
P9 = Schnittpunkt(P7–P8, P3–P6)
```

Buchbeispiel in Millimetern:

```text
P1 (0,0)     P2 (0,500)   P3 (0,210)
P4 (500,0)   P5 (500,500) P6 (500,210)
P7 (250,0)   P8 (250,500) P9 (250,210)
```

## Direkte Belege

- [`s33.md`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/s33.md)
- [`Foto S. 33`](../../../../100_quellen/20_hofenbitzer_band_1_bilder/1.1_Photos_hofenb_ba1_total/s33.jpg)
- [`formeln_s33_normalisiert.md`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s33_normalisiert.md),
  insbesondere `HOF-B1-S033-F03`

## Sprache und Mathematik

- [`Körper- und Konstruktionsmaße`](../../../../000_sprache/20_symbole_abkuerzungen/2.4_abkuerzungen_koerpermasse_konstruktionsmasse.md)
- [`Numerik, Einheiten und Toleranzen`](../../../../400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md)
- [`Punkte, Geraden und Projektion`](../../../../400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md)
- [`Parameterketten und Neuberechnung`](../../../../400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md)

## Invarianten und Grenze

- Breite oben und unten ist jeweils exakt die halbe Hüftweite.
- Höhe von P1 bis P2 ist die Modelllänge; P3 liegt in Hüfttiefe.
- Taillen-, Hüft- und Saumlinie sind parallel; vM, Seitenlinie und hM stehen
  rechtwinklig dazu.
- P7 und P8 halbieren; P9 ist der echte Geradenschnitt.
- Hüfttiefe muss endlich und größer als null sein; Modelllänge und halbe
  Hüftweite müssen endlich und größer als die lokale Nullvektortoleranz
  `1e-9 mm` sein. Die Hüfttiefe darf die Modelllänge nicht überschreiten.
- Nicht endliche Punkte, entartete Geraden und nicht eindeutige Geradenschnitte
  stoppen typisiert.
- Richtungen werden vor Kreuz- und Skalarprodukten skaliert; berechnete
  Zwischenwerte und P9 müssen endlich bleiben.
- Abnäher, Taillenerhöhung, Hüftbogen und Produktionsschnitt gehören nicht in
  diesen Schritt.

Der grüne Teststand ist eine digitale Vertragsprüfung. Er bestätigt keine
visuelle, physische oder produktionsbezogene Freigabe des Schnitts.

## Technische Prüfung

Im Schrittordner ausführen:

```text
python test_grundgeruest.py
```

Geprüft werden die Buchpunkte P1–P9, die Halbierungen, der Geradenschnitt,
Parallelität und Rechtwinkligkeit, die Lage von P9, die Fehlergrenzen und die
Provenienz.

## Nächster Schritt

Keine Erweiterung in diesem Schritt; Abnäher, Kurven und Produktionskontur
beginnen erst in den folgenden belegten Gruppen.
