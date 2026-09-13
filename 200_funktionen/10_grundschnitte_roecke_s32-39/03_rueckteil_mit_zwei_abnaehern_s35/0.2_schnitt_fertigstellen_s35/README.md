# Schnitt fertigstellen — S. 35

## Aktueller Schritt

[Interaktive Kurvenansicht](kurvenansicht.html): Taille und Hüfte für VT/RT
getrennt einstellen, Ausgangsform vergleichen und offene Nahtlängen ablesen.
**Werners Freigabe:** „ja. einstellbare kurven entwickeln und mir zeigen.“
Kurvenfamilie und Reglerbereiche sind unsere digitale Entscheidung, keine
zusätzliche Hofenbitzer-Formel. Die visuelle Auswahl steht noch aus.

## Ausführbarer Vertrag

- [kurven.py](kurven.py): zwei C1-verbundene kubische Bézierkurven je freiem
  Taillenabschnitt. Anker bleiben fest; `durchhang_mm >= 0` senkt den
  Abschnittsmittelpunkt gegenüber seiner Sehne ab. Endtangenten waagrecht.
- Hüftbogen: monotone Kubik von oberem Seitenpunkt zur Hüftlinie, dort
  senkrechter Anschluss; expliziter dimensionsloser `0 < form <= 0.5`.
- Adaptive Messung: Sehnensumme und Kontrollpolygonsumme begrenzen die
  Kurvenlänge; `fehler_mm` begrenzt Intervallbreite und Abflachungsabstand.
  Technische Genauigkeit, keine Näh- oder Passformtoleranz.
- [grundkontur.py](grundkontur.py): geschlossene **Arbeits-Papierkontur** aus
  diesen Kurven, geraden Abnähermundkanten, Mitte und Saum. Lokale aufrechte
  Teile, Mitte `(0,0)` links, SN rechts, Millimeter und Y nach unten.
  Ungeformte Abnäher bleiben interne Linien; kein Abnäherdach/Trueing.
- Ungültige/entartete/nichtendliche Geometrie stoppt mit `KurvenVertragError`.
  Kein Einrasten, keine still gewählten fehlenden Fachparameter.

## Prüfbeispiel und Ansicht

`arbeitsbeispiel()` montiert vorhandene S.-33/34/35-Funktionen unverändert.
Die ausdrücklich gewählten neutralen Beispielmaße stehen in dieser Funktion
und in der Ansicht; kein Kundinnenprofil, kein vollständig identischer
Buchdatensatz. VT und RT haben jeweils lokale Mitte links; die Ansicht
spiegelt nur die Darstellung des RT. Beide Halbteile erscheinen gleich skaliert.

[ansicht_erzeugen.py](ansicht_erzeugen.py) erzeugt aus
[kurvenansicht.vorlage.html](kurvenansicht.vorlage.html) die Offline-HTML.
Regler wählen in Python berechnete Geometrie, keine zweite JS-Kurvenformel.
`kurvenansicht.html` ist ausschließlich die reproduzierbare Generatorausgabe.
Regler ändern keine Datei; Auswahlwerte lassen sich im Textfeld ablesen.

Im Schrittordner, ohne Zusatzpakete:

```bash
python -m unittest discover -s . -p 'test_*.py' -v
python ansicht_erzeugen.py
```

## Belege und Mathematik

- [S. 35, Schritte 22–23](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/s35.md): geschwungene Taille und getrennte Teile; keine eindeutigen Kontrollpunkte.
- [Originalfoto](../../../../100_quellen/20_hofenbitzer_band_1_bilder/1.1_Photos_hofenb_ba1_total/s35.jpg).
- [Béziervertrag](../../../../400_mathematik/20_codevertraege/50_bezierkurven.md).
- [Messen und Passung](../../../../400_mathematik/20_codevertraege/70_messen_passung_und_markierungen.md).

## Nächste Grenze

Zuerst die Kurven visuell wählen. Danach Abnäher schließen/ausformen und
Taillenverlauf sowie Nahtpaarung ausgleichen. Erst darauf Zugaben,
Saumeinschläge, Rückschnitte und Produktionsmarkierungen aus S. 36 / ab S. 22.
Taillenlänge ohne Mundkante ist **kein genähter Taillenumfang**. Keine
Produktionsfreigabe, kein maßstäblicher Zuschnitt, keine CLO-/Toile-Prüfung.
