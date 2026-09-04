# Modelle Röcke S. 40–105 — lokale Arbeitsregel

## Zweck und Grenze

Dieser Bereich ordnet Hofenbitzer Band 1, S. 40–105, nach wiederverwendbaren
Rockfunktionen statt nach einzelnen Buchseiten. Er ist eine Arbeits- und
Roadmapschicht für spätere fachliche Klärung und Implementierung.

Die hier abgelegten Buch- und Formeldokumente sind quellentreue Kopien. Dieser
Ordner erteilt keine fachliche Freigabe und enthält noch keinen Python-Code.

## Originalquelle

- Digitale Buchfassung:
  `C:\ATELIER\100_quellen\10_hofenbitzer_b1\1_hofenbitzer_band_1_digital\03_modelle_roecke_s40-105`
- Originalfotos:
  - S. 40–42: `C:\ATELIER\100_quellen\10_hofenbitzer_b1\2_bilder\1-43`
  - S. 43–105: `C:\ATELIER\100_quellen\10_hofenbitzer_b1\2_bilder\43-130`
- Seiten- und Modellbereich: gerader Bund, Rockformveränderungen, Glocken- und
  Hosenröcke, Taillenvertiefungen, Belege/Formbünde/Passen, Bahnen/Godets,
  Kräuselungen/Falten, Volants, Futter/Schlitze/Jeansrock sowie Wickel- und
  Drapiermodelle, S. 40–105.

## Direkte Unterordner

- `01_ausgangsschnitt_und_formveraenderung/` — Ausgangsform, Öffnen/Zulegen,
  Ausstellen, Kreis- und Hosenrockgrundlagen.
- `02_taille_bund_passe_und_verschluss/` — obere Kante, Belege, Bünde, Passen,
  Über-/Untertritte und Verschlüsse.
- `03_bahnen_teilungen_godets_und_einsaetze/` — Längsteilungen, Bahnen,
  eingesetzte/angeschnittene Godets und aus Bahnen abgeleitete Modelle.
- `04_falten_kraeuselungen_und_mehrweite/` — Kräuselfaktoren, Faltenarten,
  Faltenraster und Mehrweitenverteilung.
- `05_volants_stufen_und_saumerweiterung/` — Kreis-/Teilkreisvolants,
  Rüschen/Stufen und Saumweitenkonstruktionen.
- `06_futter_schlitze_taschen_und_produktionsschnitt/` — Futterableitung,
  Schlitz- und Taschenlösungen, Nahtzugaben, Markierungen und Schnittteile.
- `07_wickeln_drapieren_und_asymmetrie/` — Wickelteile, Drapieröffnungen,
  Wasserfallkanten und asymmetrische Konturen.
- `08_pruefung_und_kontrolle/` — zentrale Prüfstellen, kontrollbedürftige Seiten,
  Formelgrenzen und Symbollegende.

Jeder Funktionsordner enthält `quellenbelege/`, `mathematik/` und
`BILDVERWEISE.md`; `08_pruefung_und_kontrolle/` enthält zusätzlich `sprache/`.

## Provenienzregel

1. Jede Kopie behält den ursprünglichen Dateinamen.
2. `BILDVERWEISE.md` nennt den absoluten Pfad des Originalfotos; Fotos werden
   wegen Größe und eindeutiger SSOT nicht dupliziert.
3. Mehrfachkopien sind nur dort vorhanden, wo eine Seite mehrere Funktionen
   belegt. Die Originalquelle bleibt die einzige maßgebliche Fassung.
4. Die Mathematikdateien sind modeblinde Grundlagen. Ihre heutigen Codebezüge
   sind kein Beleg, dass die jeweilige Rockfunktion bereits implementiert ist.
5. `SPRACHE.md` ist ein abgeleiteter Arbeitsindex mit exakten Quellpfaden; die
   leere Gosslar-Datei wird nicht als Freigabe ausgelegt.

## Hier bearbeitbar

- lokale `README.md`, `SPRACHE.md`, `FORMELSTATUS.md` und `BILDVERWEISE.md`;
- neue, klar gekennzeichnete Prüfnotizen und spätere Roadmap-Dokumente;
- nach fachlicher Freigabe zukünftige Implementierungsartefakte in diesem
  Arbeitsbereich.

Quellenkopien in `quellenbelege/`, Mathematikkopien in `mathematik/` und die
Symbolkopie in `sprache/` bleiben als Belege unverändert. Ergänzungen stehen in
separaten lokalen Dateien.

## Ausdrücklich nicht verändern

- alles unter `C:\ATELIER\100_quellen`;
- die Sprach-SSOT unter `C:\ATELIER\000_sprache`;
- die Mathematik-SSOT unter `C:\ATELIER\400_mathematik`;
- offene Buchstellen durch Vermutung, stillschweigende Korrektur oder neue
  fachliche Regeln;
- fachliche Maße durch echte Kundenmaße ersetzen.

Kein Commit und kein Push aus dieser Aufbauarbeit.

## Arbeitsreihenfolge

Quelle/Bild → Prüfstellen → Sprache/Gosslar → Mathematik → vorhandene Formeln →
offene/widersprüchliche Stellen → erst danach kleinster fachlich freigegebener
Primitive.

## Nächster Arbeitsschritt

Zuerst `N1` auf S. 79 am physischen Buch klären. Danach die zehn Punkte aus
`00_pruefstellen.md`, die zusätzlichen Quellenkonflikte S. 43, 92 und 95–98
sowie die gesperrten Formelgruppen S. 86, 90 und 91 abarbeiten.

Vor einer Implementierung fehlen außerdem belastbare, quellenneutrale
Mathematikgrundlagen für Spiegelung an `vM`/`hM`, exakte Kreise/Kreisbögen und
das Aufschneiden, Trennen und Wiederzusammensetzen von Schnittflächen. Die
vorhandenen Mathematikkopien sind Arbeitsmaterial aus der Vorgänger-Engine und
kein Implementierungsbeleg.

Erst nach dokumentierter Freigabe darf ein kleinster Primitive geplant werden;
noch keinen Python-Code schreiben.
