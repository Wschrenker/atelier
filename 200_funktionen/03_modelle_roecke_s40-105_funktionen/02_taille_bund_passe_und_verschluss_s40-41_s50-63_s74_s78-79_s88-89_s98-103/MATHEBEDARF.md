# Mathematikbedarf — Taille, Bund, Passe und Verschluss

Stand: 2026-09-06

Prüfumfang: aktive Transkriptionen S. 40–41, 50–63, 74, 78–79, 88–89 und 98–103; vorhandene Formeldateien; Mathematik-Recherche 01–14.

## Ergebnis

Die allgemeinen Mathematikbausteine sind jetzt ausreichend vorbereitet. Der Hauptengpass für Python liegt nicht mehr bei zusätzlicher Schulmathematik, sondern bei:

1. noch nicht normalisierten Fachformeln;
2. nicht algorithmisch bestimmten Formulierungen wie „optisch parallel“, „schön ausformen“ oder „nach Bedarf“;
3. der Abhängigkeit vom bereits konstruierten Rock-/Bund-Ausgangsschnitt S. 32–39;
4. der späteren Auswahl einer robusten 2D-Geometrieimplementierung für Flächenteilung und Nahtzugaben.

## Zuordnung der Schrittgruppen

| Schrittordner | Seiten/Funktion | Benötigte allgemeine Primitiven | Fachlicher Stand |
|---|---|---|---|
| 01–04 | gerader Bund, Über-/Untertritt, Verschluss | Einheiten; Pfadlänge und Positionen; Teilung linearer Strecken; Markierungen | S. 40 hat eine normalisierte Knopflochformel. S. 41 enthält weitere klare Längenbeziehungen, aber noch keine aktive Formeldatei/Normalisierung. Ausgangsbund S. 38–39 ist Voraussetzung. |
| 05–08 | Taillenvertiefung und Beleglinie | Punkte, Projektion, Kurven, Pfadabstand, Parameterketten | Prozentregel S. 52 ist normalisiert. Gemessene `BuA` sind Eingaben. „Leicht geschwungen“ und „optisch parallel“ sind noch keine eindeutige Kurvenregel. |
| 09–19 | Abnäher schließen, Weite reduzieren, Formbund abtrennen | Rotation/Spiegelung; Keile schließen; Kurven; Flächenteilung; genähter Zustand | Abnäherschluss ist geometrisch abdeckbar. Welche Konturseite bewegt wird und wie nach dem Schließen ausgeformt wird, muss pro Schritt fachlich festgelegt werden. Viele Zahlen liegen nur als Kandidaten vor. |
| 20–32 | Produktionsschnitt, Passe, Innenbund, Futter, Miederbund | Spiegelung; Kopieren; Flächenteilung/-vereinigung; variable Offsets; Markierungen | Vieles ist Produktionsmetadatum oder manuelle Gestaltung. Asymmetrische linke/rechte Teile müssen getrennt bleiben. Nahtzugaben unterscheiden sich kantenweise. |
| 33–36 | Passen-/Ballon-/Faltenteil | Rotation/Öffnen; Keile spreizen; Kurven; Flächenteilung; Längen; Parameterketten | Formeln S. 79, 88 und 89 sind normalisiert. Lage, Anzahl und Öffnungsrichtung der Schnitte bleiben Bestandteil der Fachfunktion. |
| 37–39 | Formbund/Passe, Knopfleiste, Schlitz | Flächenteilung; Spiegelung; variable Offsets; rechte Winkel; Markierungen | Allgemeine Geometrie ist vorbereitet. Taschenform, Passenform und Nahtausformung enthalten freie Gestaltung und dürfen nicht erfunden werden. |
| 40–42 | großer Übertritt und Bund am Wickelrock | Spiegelung; Pfadlängenübertragung; Flächenteilung; Markierungen | S. 101–102 besitzen Formelkandidaten, aber keine Normalisierung. Der asymmetrische Ausgangsschnitt muss vor der Bundableitung feststehen. |

## Benötigte Mathematikverträge

Die Verträge `60_polygone_und_offsets.md` und `65_flaechen_teilen_vereinigen_und_kopieren.md` besitzen bereits eindeutige Ergebnis-/Fehlerverträge, bleiben aber bis zur Wahl und Prüfung einer robusten Topologieimplementierung auf Status `offen`. Die übrigen hier verlinkten allgemeinen Primitive sind als `bereit` gekennzeichnet.

- [`10_numerik_einheiten_und_toleranzen.md`](/400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md)
- [`20_punkte_vektoren_geraden_und_projektion.md`](/400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md)
- [`30_transformationen.md`](/400_mathematik/20_codevertraege/30_transformationen.md)
- [`50_bezierkurven.md`](/400_mathematik/20_codevertraege/50_bezierkurven.md)
- [`60_polygone_und_offsets.md`](/400_mathematik/20_codevertraege/60_polygone_und_offsets.md)
- [`65_flaechen_teilen_vereinigen_und_kopieren.md`](/400_mathematik/20_codevertraege/65_flaechen_teilen_vereinigen_und_kopieren.md)
- [`70_messen_passung_und_markierungen.md`](/400_mathematik/20_codevertraege/70_messen_passung_und_markierungen.md)
- [`75_keile_schliessen_und_oeffnen.md`](/400_mathematik/20_codevertraege/75_keile_schliessen_und_oeffnen.md)
- [`80_parameterketten_und_neuberechnung.md`](/400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md)

Kreis- und Bogengeometrie ist im Gesamtbestand vorbereitet, wird für diese Schrittgruppe aber nicht pauschal benötigt.

## Was keine eigene Mathematikprimitive ist

- Beschriftung, Stückzahl, Stoffart, Einlage, Fadenlauf und Datum;
- Näh- und Bügelhinweise;
- Wahl von Knopf, Haken, Öse oder Reißverschluss;
- freie Modellform ohne messbare Konstruktionsregel;
- visuelle Bewertung „harmonisch“, „schön“ oder „modellgerecht“.

Diese Angaben können Metadaten, Benutzerentscheidung oder manueller Prüfschritt sein. Sie werden nicht in Scheingeometrie übersetzt.

## Belegte fachliche Prüfpunkte

- `s41.md` verwendet für `TaU` einmal „Bundumfang“ und einmal „Taillenumfang“; vor dem Vertrag muss eine eindeutige Parameterbezeichnung gewählt werden.
- Die Normalisierung zu S. 52 bildet die seitlichen `+10 %` ab, aber der in `s51.md` belegte Höchstzuschlag von `1 cm` ist darin noch nicht vollständig gebunden.
- `s50.md` nennt `1–1,5 cm` Taillenmehrweite am halben Rock, `s52.md` mindestens `0,5–1 cm`; daraus darf ohne eindeutig zugeordneten Grundschnitt keine gemeinsame Konstante entstehen.
- `s55.md` schreibt „2/3 ca. 3/4“; `s54.md` belegt die verständliche Lesung als Bereich `2/3 bis 3/4`. Die Normalisierung muss diese Lesung ausdrücklich sichern.
- `s63.md` fordert ein „etwas engeres“ Taillenband ohne Betrag.
- `s78.md` beschriftet eine Öffnung mit „1/2 der anderen Öffnungen“, ohne den Referenten im Text eindeutig zu bestimmen.
- `s79.md` fordert Reduktion der Teilweite ohne Betrag.
- `s103.md` fordert „ungefähr gleich“ geöffnete Einschnitte ohne Toleranz oder Priorität gegenüber vollständigem Abnäherschluss.

## Offene Gates vor konkretem Python

1. Den genauen Ausgangsvertrag des geraden Rocks/Bundes aus S. 32–39 festlegen.
2. S. 41 sowie die tatsächlich benötigten Kandidaten der nächsten Seite fachlich normalisieren. Formelextrakte fehlen außerdem für S. 50, 58, 61, 74, 99 und 103; vorhandene Extrakte sind auf Vollständigkeit zu prüfen.
3. Für jeden gewählten Schritt festlegen, welche Linien Naht-, Schnitt-, Bruch-, Trenn- oder Markierungslinien sind.
4. Bei „ausformen“ entweder eine belegte Kurvenregel angeben oder den Schritt ausdrücklich manuell/visuell lassen.
5. Erst dann genau einen Schritt als kleinste Python-Funktion mit Quellenbeispiel und Invarianten bauen.

## Empfohlener erster vertikaler Schnitt

Nicht der ganze 42-Schritte-Ordner auf einmal. Zuerst **01 Bund mit Über- und Untertritt S. 40**, sobald der Ausgangsbund S. 38–39 als Eingabe verfügbar ist:

```text
Ausgangsbund übernehmen
→ Verschlussposition festlegen
→ Über-/Untertritt verlängern
→ Knopfloch aus normalisierter Formel berechnen
→ Markierungen entlang der Bundstrecke setzen
→ TaU-/Bundlänge und belegte Verschlusspositionen prüfen; keine allgemeine Symmetrie von Über- und Untertritt annehmen
```

Danach kann S. 41 dieselben Primitiven wiederverwenden, sobald seine Beziehungen normalisiert sind.
