# 06 Einheiten und Masshaltigkeit

## Worum geht's (Klartext, auch fuer Nicht-Mathematiker)

Ein Schnittmuster ist nur brauchbar, wenn 10 cm im Ausdruck wirklich 10 cm sind. Darum sollte die Engine intern eine eindeutige Einheit nutzen, hier Millimeter, und beim Export die Einheit sauber weitergeben. Ein Kontrollquadrat auf dem Ausdruck hilft, Druckskalierung sofort zu erkennen.

## Die Mathematik (Formeln sauber, nachvollziehbar)

Die grundlegende Umrechnung ist:

```text
1 cm = 10 mm
mm = cm * 10
cm = mm / 10
```

Rundung sollte spaet passieren. Wenn intern mehrfach auf ganze Millimeter oder Dezimalstellen gerundet wird, koennen sich kleine Fehler addieren. Besser ist: intern mit ungerundeten Zahlen rechnen, fuer Anzeige/Labels runden und beim Export die fuer das Zielformat noetige Genauigkeit setzen.

Ein Kontrollquadrat kann z.B. rechnerisch als vier Punkte erzeugt werden:

```text
(0, 0), (50, 0), (50, 50), (0, 50)
```

Bei Millimeter-Einheit muss dieses Quadrat im Ausdruck 50 mm x 50 mm messen.

## Anwendung in der Schnittkonstruktion (Bezug zum geraden Rock / zum Code)

`../src/draft.js` hat bereits `cmToMm(value) = value * 10` und baut den Rock in Millimetern auf. Diese Entscheidung sollte fuer Hofenbitzer beibehalten werden: fachliche Masse koennen in cm aus der Vorlage kommen, werden aber am Eintritt in die Engine nach mm umgerechnet. Fuer Export gilt: SVG/PDF/DXF muessen so geschrieben werden, dass die Ausgabe masshaltig ist. DXF sollte Millimeter als Zeichnungseinheit kennzeichnen; bei SVG/PDF muss Druckskalierung separat pruefbar bleiben.

Unsicher/zu pruefen: Die konkrete Export-Implementierung wurde hier nicht geaendert und nicht vollstaendig untersucht. Ob bereits ein Kontrollquadrat existiert und wie PDF/DXF aktuell Einheiten setzen, gehoert in eine spaetere Export-Pruefung.

## Quellen (pro Aussage: Titel + URL + Abrufdatum)

- W3C: "CSS Values and Units Module Level 4" - https://www.w3.org/TR/css-values-4/ - Abrufdatum: 2026-06-19. Belegt absolute Laengeneinheiten und die Umrechnung zwischen `cm` und `mm`.
- W3C: "Scalable Vector Graphics (SVG) 1.1 (Second Edition) - Coordinate Systems, Transformations and Units" - https://www.w3.org/TR/SVG11/coords.html - Abrufdatum: 2026-06-19. Belegt SVG-Koordinatensysteme, Einheiten und Transformationen fuer masshaltige Darstellung.
- Autodesk: "AutoCAD 2012 DXF Reference" - https://images.autodesk.com/adsk/files/autocad_2012_pdf_dxf-reference_enu.pdf - Abrufdatum: 2026-06-19. Belegt DXF-Systemvariablen/Einheiten wie `$INSUNITS`; relevant fuer Millimeter-Ausgabe.
- Lokaler Engine-Anker: `../src/draft.js` - gelesen am 2026-06-19. Belegt `cmToMm(...)` und die aktuelle interne Millimeter-Rechnung.
