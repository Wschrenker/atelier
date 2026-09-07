# Prüfstellen nach Buchseiten

Dieser Ordner ist eine **abgeleitete Arbeitsansicht** aus den archivierten Prüfstellen-Zusammenzügen. Für jede betroffene Buchseite gibt es genau eine Datei `sNNN.md`, in der Formel- und Text-Prüfstellen gemeinsam stehen.

**Die sieben Originaldateien liegen unverändert im Archiv.**

Dieser Ordner wird **erzeugt, nicht von Hand gepflegt**. Wer einen Prüfstellen-Status ändert, ändert ihn in der Quelle im Archiv und erzeugt die Ansicht anschließend neu:

```text
python 600_prozess/werkzeuge/pruefstellen_ansicht_bauen.py             Probelauf
python 600_prozess/werkzeuge/pruefstellen_ansicht_bauen.py --schreiben
```

Der Probelauf meldet, welche Seitendateien sich ändern würden, ohne etwas zu schreiben. Von Hand geänderte Dateien gehen beim nächsten Lauf verloren.

## Sortierregel

- Buchkategorie, dann Buchseite aufsteigend.
- Mehrseitige Punkte stehen auf jeder im Eintragskopf oder in der Quellüberschrift genannten Seite; ihr Wortlaut bleibt unverändert.
- Einträge, deren Quellkopf ausdrücklich keine Seitenangabe enthält, stehen in [`ohne_eindeutige_seitenzuordnung.md`](ohne_eindeutige_seitenzuordnung.md).
- Die beiden freien Notizdateien `Drei verschiedene Sachen, der Reihe.txt` und `Unbenannt.txt` wurden nicht zerlegt; sie bleiben unverändert im archivierten Formel-Quellordner.

## Umfang

- Seitendateien: **471**
- Formel-Prüfabschnitte: **82**
- Seitenblöcke mit offenen Formelfragen: **183** mit **541** einzelnen Formeln
- Text-Prüfstellen erste Zweitprüfung: **128**
- D-Punkte Transkriptabweichungen: **509**
- A/B/C-Punkte Buchprüfung: **366**
- Einträge ohne eindeutige Seitenzuordnung: **11**

## Buchkategorien

- [`00_vorspann_s1-7/`](00_vorspann_s1-7/) — Vorspann, S. 1–7: 3 Seitendateien
- [`01_grundlagen_s8-31/`](01_grundlagen_s8-31/) — Grundlagen, S. 8–31: 15 Seitendateien
- [`02_grundschnitte_roecke_s32-39/`](02_grundschnitte_roecke_s32-39/) — Grundschnitte Röcke, S. 32–39: 6 Seitendateien
- [`03_modelle_roecke_s40-105/`](03_modelle_roecke_s40-105/) — Modelle Röcke, S. 40–105: 51 Seitendateien
- [`04_grundschnitte_hosen_s106-137/`](04_grundschnitte_hosen_s106-137/) — Grundschnitte Hosen, S. 106–137: 30 Seitendateien
- [`05_modelle_hosen_s138-170/`](05_modelle_hosen_s138-170/) — Modelle Hosen, S. 138–170: 30 Seitendateien
- [`06_grundschnitte_oberteile_s171-196/`](06_grundschnitte_oberteile_s171-196/) — Grundschnitte Oberteile, S. 171–196: 23 Seitendateien
- [`07_grundschnitte_aermel_s197-220/`](07_grundschnitte_aermel_s197-220/) — Grundschnitte Ärmel, S. 197–220: 23 Seitendateien
- [`08_aermel_varianten_s221-289/`](08_aermel_varianten_s221-289/) — Ärmel-Varianten, S. 221–289: 65 Seitendateien
- [`09_kragen_kapuzen_taschen_s290-369/`](09_kragen_kapuzen_taschen_s290-369/) — Kragen, Kapuzen und Taschen, S. 290–369: 75 Seitendateien
- [`10_ausschnitte_s370-437/`](10_ausschnitte_s370-437/) — Ausschnitte, S. 370–437: 49 Seitendateien
- [`11_modelle_kleider_blusen_westen_s438-464/`](11_modelle_kleider_blusen_westen_s438-464/) — Modelle Kleider, Blusen, Westen, S. 438–464: 26 Seitendateien
- [`12_modelle_jacken_s465-492/`](12_modelle_jacken_s465-492/) — Modelle Jacken, S. 465–492: 26 Seitendateien
- [`13_sportswear_waesche_unisex_s493-534/`](13_sportswear_waesche_unisex_s493-534/) — Sportswear, Wäsche, Unisex, S. 493–534: 42 Seitendateien
- [`14_anhang_sachwortverzeichnis_s535-544/`](14_anhang_sachwortverzeichnis_s535-544/) — Anhang und Sachwortverzeichnis, S. 535–544: 7 Seitendateien

## Quellen

- Formel-Prüfabschnitte: [`prüfstelle_formel_zusammenzug/00_pruefstellen_formeln_band_1.md`](../../30_hofenbitzer_band_1_archiv/prüfstelle_formel_zusammenzug/00_pruefstellen_formeln_band_1.md)
- Offene Fragen in normalisierten Formeln: [`prüfstelle_formel_zusammenzug/01_offene_fragen_normalisierte_formeln.md`](../../30_hofenbitzer_band_1_archiv/prüfstelle_formel_zusammenzug/01_offene_fragen_normalisierte_formeln.md)
- Text-Prüfstellen der ersten Zweitprüfung: [`prüfstelle_text_zusammenzug/00_pruefstellen_text_band_1_zusammenzug.md`](../../30_hofenbitzer_band_1_archiv/prüfstelle_text_zusammenzug/00_pruefstellen_text_band_1_zusammenzug.md)
- Abweichungen der Transkription vom Foto (D): [`prüfstelle_text_zusammenzug/01_abweichungen_transkript_vom_foto.md`](../../30_hofenbitzer_band_1_archiv/prüfstelle_text_zusammenzug/01_abweichungen_transkript_vom_foto.md)
- Buchfehler aus dem Archiv-Prüfstand (A/B/C): [`prüfstelle_text_zusammenzug/02_buchfehler_aus_dem_archiv.md`](../../30_hofenbitzer_band_1_archiv/prüfstelle_text_zusammenzug/02_buchfehler_aus_dem_archiv.md)
