# Konstruktionstabelle erstellen — S. 32–33

**Status:** Python-Vertrag umgesetzt; Buchbeispiel und Vertragsgrenzen grün.

## Zweck

Aus Körpermaßen und ausdrücklich gewählten Zugaben die Konstruktionsmaße des
geraden Rock-Grundschnitts bilden. Die Verteilung des Taillenausfalls wird als
Entscheidung erfasst und gegen ihre Summe geprüft.

## Belegte Ein- und Ausgaben

- Eingaben: `hueftumfang`, `taillenumfang`, `huefttiefe`, `modelllaenge`;
  alle vier Werte müssen endlich und größer als null sein.
- Entscheidungen: `hueftzugabe` im Buchbereich 2–3 cm,
  `taillenzugabe` im Buchbereich 1–2 cm sowie die gewählten Beträge für
  Hüftabstich und Abnäher.
- Fachbereiche: Hüftabstich `½ TaAf ± 1 cm`, vorderer Abnäher `0` oder
  `1,5–2,5 cm`, erster hinterer Abnäher höchstens `4,5 cm`; der zweite
  hintere Abnäher bleibt auf S. 33 exakt `0 cm`.
- Ausgaben: Hüftweite, Taillenweite, deren Hälften/Viertel,
  Taillenausfall und Ergebnis der Kontrollsumme.

Buchbeispiel:

```text
HüW = 97 cm + 3 cm = 100 cm; ½ = 50 cm; ¼ = 25 cm
TaW = 72 cm + 2 cm = 74 cm;  ½ = 37 cm; ¼ = 18,5 cm
TaAf = 50 cm - 37 cm = 13 cm
Kontrolle = 6,5 cm + 2,5 cm + 4 cm + 0 cm = 13 cm
```

## Direkte Belege

- [`s32.md`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/s32.md)
  · [`Foto`](../../../../100_quellen/20_hofenbitzer_band_1_bilder/1.1_Photos_hofenb_ba1_total/s32.jpg)
- [`s33.md`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/s33.md)
  · [`Foto`](../../../../100_quellen/20_hofenbitzer_band_1_bilder/1.1_Photos_hofenb_ba1_total/s33.jpg)
- [`formeln_s33.md`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s33.md)
- [`formeln_s33_normalisiert.md`](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s33_normalisiert.md):
  `HOF-B1-S033-F01`, `HOF-B1-S033-F02`, `HOF-B1-S033-F03`
- [`Prüfstellen S. 33`](../../../../100_quellen/10_hofenbitzer_band_1_digital/pruefstellen_nach_seiten/02_grundschnitte_roecke_s32-39/s033.md)

## Sprache und Mathematik

- [`Körper- und Konstruktionsmaße`](../../../../000_sprache/20_symbole_abkuerzungen/2.4_abkuerzungen_koerpermasse_konstruktionsmasse.md)
- [`Formelkürzel-Arbeitsbestand`](../../../../000_sprache/20_symbole_abkuerzungen/2.5_abkuerzungen_aus_formeln_band_1_geprueft_v1.md)
- [`Sachwortverzeichnis`](../../../../000_sprache/10_gosslar/1_sachwortverzeichnis.md)
- [`Numerik, Einheiten und Toleranzen`](../../../../400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md)
- [`Parameterketten und Neuberechnung`](../../../../400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md)

## Prüfgrenze

Die Quelle gibt keine automatische Auswahlregel für Zugaben oder
Abnäherverteilung: Die Figur soll beobachtet werden. Deshalb bleiben diese
Werte explizite Entscheidungen. Es wird nichts still geklemmt oder geraten.
cm→mm-Überläufe und nicht endliche abgeleitete Tabellenwerte stoppen typisiert.
Dieser Schritt erzeugt noch keine Schnittgeometrie.

`vollstaendig` bestätigt nur die rechnerische Kontrollsumme. Der grüne Teststand
ist eine digitale Vertragsprüfung, keine figürliche, physische oder
produktionsbezogene Freigabe.

## Nächster Schritt

Den Tabellenvertrag erst bei der konkreten Montage als geprüften Eingang für
das Grundgerüst verwenden.
