# Hüftabstich nach Proportionen — S. 37

## Vertrag

[`hueftabstich.py`](hueftabstich.py) berechnet ausschließlich den Hüftabstich
für die ausdrücklich gewählte Figurform. Alle Ein- und Ausgaben in **mm**.

- `taillenausfall_mm`: TaAf des halben Schnitts, aus zugabenhaltiger halber
  Hüftweite minus halber Taillenweite; unverändert aus S. 33 übernehmen.
- `figurform`: `BREITE_HUEFTE_FLACHES_GESAESS` oder
  `SCHMALE_HUEFTE_STARKES_GESAESS`; kein Standard und keine Umfangsdiagnose.
- `hueftform_korrektur_mm`: ausdrücklich gewählter positiver Betrag, **5–15 mm**.
- Ausgabe: `Hueftabstich` mit Eingaben, `hueftabstich_mm` und Provenienz
  (verwendete Formel-ID, Fachentscheidungen, Mathematikverträge, Version).

| Figurform | Formel-ID | Rechnung |
|---|---|---|
| Breite Hüfte, eher flaches Gesäß | HOF-B1-S037-F01 | TaAf / 2 + Korrektur |
| Schmale Hüfte, starkes Gesäß | HOF-B1-S037-F02 | TaAf / 2 − Korrektur |

Technische Schutzgrenzen, **keine zusätzlichen Buchregeln**: endliche
`int`/`float`-Werte ohne `bool`, TaAf > 0 und 0 ≤ Hüftabstich ≤ TaAf.
Grenzwerte 0 und TaAf sind nur rechnerisch zulässig, keine Passformfreigabe.
Typisierte Fehler statt Klemmen, Runden oder Ersatzwerten; fehlende
Schlüsselwortargumente liefern Python-`TypeError`, leere Fachentscheidungen
`EntscheidungFehltError`.

## Belege und Seitenabdeckung

- [Transkript S. 37](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/s37.md),
  [Originalfoto](../../../../100_quellen/20_hofenbitzer_band_1_bilder/1.1_Photos_hofenb_ba1_total/s37.jpg),
  [Extrakt](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s37.md),
  [Normalisierung](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s37_normalisiert.md).
- Bildbefund: □3 bestätigt Plus und 0,5–1,5 cm; □4 bestätigt Minus und
  denselben Betragsbereich. Formelwortlaut stimmt; alte Transkript-Zeilenverweise
  in Extrakt/Normalisierung sind versetzt, heute stehen die Formeln in Zeile 44/46.
- [Prüfstellen S. 37](../../../../100_quellen/10_hofenbitzer_band_1_digital/pruefstellen_nach_seiten/02_grundschnitte_roecke_s32-39/s037.md):
  beide Auswahlfragen bleiben im Quellenbestand offen. Hier durch explizite
  Fachentscheidungen abgegrenzt, nicht als automatische Auswahl gelöst.
- Sprache: [TaAf-Abkürzung](../../../../000_sprache/20_symbole_abkuerzungen/2.5_abkuerzungen_aus_formeln_band_1_geprueft_v1.md),
  [Sachwortregister](../../../../000_sprache/10_gosslar/1_sachwortverzeichnis.md).
  Dessen Eintrag „Proportionen von Hüfte und Taille“ verweist auf S. 36;
  Arbeitsbeleg hier ist das Foto S. 37. Das Originalregister bleibt unverändert.
- Mathematik: [Numerik/Einheiten](../../../../400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md),
  [Parameterketten/Provenienz](../../../../400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md).

| Weitere Buchanweisung | Behandlung |
|---|---|
| Gleiche Umfänge, unterschiedliche Figuren; Normal-/Sondergrößen | Fachlicher Kontext, keine Formwahl aus Umfängen |
| □1–4: Querschnittslinien symbolisieren Abnäherinhalte | Keine realen Abnäherlängen daraus ableiten |
| Starkes Gesäß: größere hintere Inhalte, oft zwei Abnäher; auch bei Normalfigur möglich | Keine automatische Anzahl oder Verteilung |
| □1/5/6: normale, runde, flache seitliche Hüftform | Visuell/fachlich ausformen; keine belegten Kurvenparameter |
| □7: Delle überspielen, nicht nachzeichnen | Manueller Formhinweis, keine automatische Kurve |
| Miederhinweis und Vermutungen zu Fettpolstern/Einschnürung | Kein Rechenauftrag; keine gesicherte Ursachenregel |

## Übergabegrenze

Die vorhandene [S.33-Tabelle](../../01_gerader_rock_konstruktionstabelle_und_grundgeruest_s32-33/01_konstruktionstabelle_erstellen_s32-33/konstruktionstabelle.py)
begrenzt ihre eigene Abstichwahl auf ±10 mm; die
[S.34-Verteilung](../../02_abnaeher_positionieren_s34/02_taillenausfall_aufteilen_s34/taillenausfall_aufteilen.py)
verwendet für ihre Varianten 10–15 mm. Keine dieser Grenzen wird global erweitert.
Dieser Baustein übernimmt nur TaAf und berechnet den S.37-Abstich separat.
Die vollständige Montage mit Abnäherverteilung und neu berechneter Geometrie ist
noch offen. Kein bestehendes Tabellenergebnis nachträglich überschreiben.

## Ausführen und prüfen

Im Schrittordner: `python -m unittest discover -s . -p 'test_*.py' -v`.
[Tests](test_hueftabstich.py): beide Formeln und Bereichsenden, Pflichtentscheidungen,
Zahlen-/Ergebnisgrenzen, ungerundete Neuberechnung und S.33-TaAf-Übergabe.

```python
from hueftabstich import Figurform, hueftabstich_berechnen

# Technisches Beispiel, keine auf S. 37 gedruckten Zahlen oder Maßempfehlung.
for figur in Figurform:
    ergebnis = hueftabstich_berechnen(
        taillenausfall_mm=130.0, figurform=figur, hueftform_korrektur_mm=15.0,
    )
    print(figur.value, ergebnis.hueftabstich_mm)
# breite_huefte_flaches_gesaess 80.0
# schmale_huefte_starkes_gesaess 50.0
```

**Prüfstand:** 7 lokale Tests und insgesamt 88 Kapiteltests in 10 Schrittordnern
bestanden; `compileall`, Links und das obige Beispiel ebenfalls geprüft.
**Nächster fachlicher Schritt:** Korrektur an der Figur wählen. Hüftkurve,
digitaler Gesamtschnitt, CLO, Toile und Produktionsfreigabe sind nicht nachgewiesen.
