# Kleid Lumière — was hier drin gilt

Ein Kleid mit **asymmetrischem Wickeloberteil, offenem V-Rücken und
saumerweitertem A-Linien-Rock**. Referenzgröße 38.

## Reihenfolge beim Einsteigen

1. `DEFINITION.md` — was gebaut wird und **welche Zahl woher kommt**
2. `ROADMAP.md` — Modulstatus und die Blockaden für Werner
3. `bauen.py` — die Auswahl und Verknüpfung der Module
4. `ausgabe/protokoll.txt` — was der letzte Lauf gerechnet hat

## Grenze

Dieser Ordner **besitzt keine Konstruktion**. `bauen.py` wählt Module aus
`500_python/10_rechnung/` aus und trifft nur die Entscheidungen, die dieses
Kleid betreffen. Sie stehen alle als Konstanten oben in `bauen.py` und sind in
`DEFINITION.md` begründet.

Faustprobe: Würde ein zweites Kleid dieselbe Zeile brauchen, gehört sie nach
`500_python`.

## Bauen

```
python 700_schnitte/20_kleid_lumiere/bauen.py
```

Ergebnis: `ausgabe/kleid_lumiere_gr38.dxf` (6 Schnittteile, Millimeter,
**ohne Nahtzugaben**) und `ausgabe/protokoll.txt`.

## Die eine Stelle, an der der Schnitt bewusst unfertig ist

Der **Brustabnäher ist nicht ausgeschnitten**. Eingezeichnet sind nur die
Brustabnäher-Linie und der BrP, mit dem gerechneten Winkel als Text auf dem
Teil. Grund: S.184 Schritt ㉖/㉗ (Li26) ist aus dem Transkript nicht eindeutig
lesbar. Siehe `DEFINITION.md`, Abschnitt „Der offene Punkt mit Gewicht".

Bevor dieses Kleid genäht wird, muss Werner diese Buchstelle prüfen.
