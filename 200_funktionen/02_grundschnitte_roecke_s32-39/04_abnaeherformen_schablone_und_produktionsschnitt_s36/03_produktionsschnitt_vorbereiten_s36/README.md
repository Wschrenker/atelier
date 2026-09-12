# Produktionsschnitt vorbereiten — S. 36, Bild 2

## Zweck und ausführbarer Teilumfang

[vt_spiegeln.py](vt_spiegeln.py) spiegelt ausdrücklich gewählte VT-Punkte an
der vorderen Mitte. Original und Spiegelbild bleiben getrennte Punktfolgen.
Das ist ein Geometriebaustein, kein vollständiger Produktionsschnitt.

## Vertrag

- Eingabe: nichtleere Punktfolge mit `x_mm`, `y_mm`, zwei Punkte der vM und
  explizite endliche, nichtnegative `achsen_nulltoleranz_mm`.
- Intern: Millimeter, X nach rechts, Y nach unten, keine Rundung.
- Die vM ist eine unendliche Gerade, nicht nur das Segment ihrer Achsenpunkte.
- Ausgabe: unveränderliche `VtSpiegelung` mit Original, Spiegelpunkten in
  gleicher Reihenfolge, Achse, Toleranz und Quellenzuordnung S. 36 / Bild 2.
- Fehler: `GeometrieVertragError` (`ValueError`) bei leerer Folge,
  nichtendlichen Zahlen, zu kurzer Achse oder numerischem Überlauf.
- Die Nulltoleranz prüft nur die Achsenlänge. Kein Einrasten auf die Achse,
  keine Näh- oder Passformtoleranz. Tests verwenden `1e-9 mm` rein technisch.
- Abstandserhaltung, feste Achsenpunkte und doppelte Spiegelung werden geprüft.
  Spiegelung kehrt die Umlaufrichtung einer geordneten Kontur um. Der Baustein
  sortiert nicht um, schließt keine Kontur und entfernt keine doppelten Punkte.

## Geklärte Quellenabweichung: RV

Transkript `s36.md`, Zeile 41, ordnet RV der hM zu. Das Originalfoto zeigt RV
an den zusammengehörigen Seitennähten. **Werner bestätigt am Buch:**
„RV ist an der seiten naht bei VT und RT“.
Für diesen Schritt gilt deshalb: RV an der SN von VT und RT, nicht an der hM.
Das geschützte Transkript ist unverändert; dies ist der lokale Klärungsbeleg.

RV-Markierungen werden nicht automatisch zusammen mit der VT-Geometrie
verdoppelt. Ihre spätere Platzierung ist eine separate Produktionsoperation.

## Belege und Mathematik

- [Buchtext S. 36](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/s36.md), Abschnitt „Produktionsschnitt“.
- [Originalfoto S. 36, Bild 2](../../../../100_quellen/20_hofenbitzer_band_1_bilder/1.1_Photos_hofenb_ba1_total/s36.jpg): Bildnummer, VT-Spiegelung und RV-Lage
  abgeglichen. Keine vollständige neue Transkriptionsfreigabe.
- [Extrahierte Formelkandidaten](../../../../100_quellen/10_hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s36.md):
  Maßbeschriftungen, keine Rechenformel; nicht als Zugabenautomatik übernommen.
- [Fachkürzel](../../../../000_sprache/20_symbole_abkuerzungen/2.3_abkuerzungen_schnittbereiche_begriffe.md): VT, RT, vM, hM, SN, RV, NZg, SaEs.
- [Numerik](../../../../400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md),
  [Projektion](../../../../400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md),
  [Spiegelung](../../../../400_mathematik/20_codevertraege/30_transformationen.md): `P' = 2H - P`.

## Test und Aufruf

Im Schrittordner, ohne Zusatzpakete:

```bash
python -m unittest discover -s . -p 'test_*.py' -v
```

```python
from vt_spiegeln import Punkt2D, vt_punkte_spiegeln

# Rein technisches Beispiel, keine Hofenbitzer-Konstruktionsmaße.
ergebnis = vt_punkte_spiegeln(
    punkte=(Punkt2D(0, 0), Punkt2D(20, 30), Punkt2D(0, 60)),
    vm_oben=Punkt2D(0, 0), vm_unten=Punkt2D(0, 60),
    achsen_nulltoleranz_mm=1e-9,
)
```

[Lokales Prüfbeispiel](spiegelung_pruefbeispiel.png): Darstellung dieser
berechneten Punktfolgen, kein Schnittmuster und keine reale Figur. Die PNG
ist nach bestehender Git-Regel ignoriert und nicht Bestandteil eines Commits.

## Offene Produktionsgrenzen

- Vollständige Grundkontur einschließlich der Taillenform aus
  [S. 35](../../03_rueckteil_mit_zwei_abnaehern_s35/02_schnitt_fertigstellen_s35/README.md).
- Zusammenbau zu einer gültigen Schnittfläche; keine Polygonprüfung hier.
- Nahtzugaben, Saumeinschläge, Rückschnitte, Knipse und Bohrmarkierungen
  benötigen eigene Verträge; Breiten und Positionen werden hier nicht gewählt.
- Beschriftung, Ausgabeformate, CLO, Toile und Produktionsfreigabe folgen später.

**Status:** Punktspiegelung implementiert; Produktionsschnitt insgesamt offen.
