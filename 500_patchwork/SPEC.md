# Patchwork-Modul — Konzept

> Pilotentscheidungen für den geraden Rock sind festgehalten. Format und Technik
> der späteren Oberfläche bleiben offen.

## Zweck

Werner will am Bild eines Kleidungsstücks sehen, welche Bausteine dafür
code-technisch existieren, und per Klick/Verschieben entscheiden, welche
davon in dieses Schnittmuster einfließen — zum Beispiel: Reißverschluss
seitlich oder rückwärtig am Rock. Das ist eine fachliche/strukturelle
Entscheidung, keine Zahleneingabe.

## Rolle im Datenfluss

```text
Messmodul (300_messmodul)        Patchwork-Modul (500_patchwork)
  Körpermaße, Zahlen                Bausteinauswahl, Positionen
        \                                /
         \                              /
          Gemeinsame Eingabe fürs Schnittmusterprogramm
```

Beide Module sind gleichrangige Partner der Engine, keine Unter- oder
Vorstufe voneinander. Das Patchwork-Modul ersetzt keine Maßeingabe und die
Maßeingabe entscheidet nicht über Bausteine.

## Grund für das frühe Anlegen

`ARCHITEKTUR.md` verlangt: *"Ein Codesegment darf keine eigene Sonderwelt
bilden, die später nicht anschließbar ist."* Werner möchte nicht erst viel
Konstruktionscode schreiben und danach herausfinden, wie ein
Auswahl-Modul andockt. Dieser Ordner soll deshalb früh eine gemeinsame
Sprache/Schnittstelle vorbereiten, an die sich künftige Bausteine von Anfang
an halten — auch wenn heute noch kaum ein Baustein existiert, der das
hergibt.

## Grundprinzip: ehrlich zum Code

Das Modul erfindet keine Optionen. Es zeigt und erlaubt nur, was tatsächlich
implementiert ist:

- Ein Merkmal erscheint nur, wenn ein Baustein dafür existiert.
- Eine Position/Bahn ist nur wählbar, wenn der Code genau diese Positionen
  unterstützt (kein freies Ziehen ohne Grenzen).
- Fehlt ein Baustein (z. B. heute: Reißverschluss), wird nichts vorgetäuscht
  — entweder unsichtbar oder sichtbar als "noch nicht gebaut" markiert.
- Fachlich ungeprüftes Buchwissen wird nicht stillschweigend zur wählbaren
  Option; siehe Grenzen in `AGENT.md` und `ARCHITEKTUR.md`.

## Was das Modul können muss (aus dem Gespräch destilliert)

1. **Baustein-Katalog** — jeder anschlussfähige Baustein meldet, was er ist
   (z. B. "Reißverschluss"), für welches Kleidungsstück, welche Positionen/
   Bahnen erlaubt sind, ob optional oder Pflicht, und woher die Regel kommt
   (Quellenbezug).
2. **Visuelle Darstellung** — die erlaubten Bausteine und ihre Positionen
   werden am Kleidungsstück-Bild sichtbar, im Stil des Messmoduls
   (`300_messmodul/brautkleid-messmodul.html`).
3. **Auswahl als strukturiertes Ergebnis** — Klicks/Verschiebungen ergeben
   ein Objekt ("welcher Baustein, welche Position"), vergleichbar mit dem
   Messprofil, das das Messmodul heute schon erzeugt.
4. **Zusammenspiel mit dem Messmodul** — beide Ausgaben zusammen sind der
   Input, der die Engine "zündet" (Werners Wort).

## Erster Pilot: gerader Rock

- Das Dashboard bietet zunächst nur den geraden Rock an.
- Vorderteil und Rückenteil sind Pflicht; der Bund ist abwählbar.
- Die Rocklänge wird aus drei festen Werten gewählt. Die Werte werden erst aus dem fachlich geprüften Buchkontext festgelegt.
- Abnäher werden automatisch berechnet und sind nicht wählbar.
- Der Reißverschluss ist zunächst nur in der hinteren Mitte vorgesehen.
- Nicht codierte Möglichkeiten bleiben unsichtbar.

Der Reißverschluss darf erst erscheinen, wenn der zugehörige Codebaustein
tatsächlich vorhanden und mit dem Rock verbunden ist.

## Beispiel aus dem Gespräch

Reißverschluss am geraden Rock, im ersten Pilot nur in der hinteren Mitte. Heute existiert
dafür noch kein Baustein — nur ein Bund-Übertritt in
`300_messmodul/src/drafting/straight-skirt.js`. Das wäre ein Kandidat für den
ersten echten Eintrag im Baustein-Katalog, sobald der Reißverschluss-Baustein
selbst gebaut ist.

## Nicht-Ziel

- Kein Eingabeformular für Maße.
- Keine freie Zeichenfläche ohne Bezug zu vorhandenem Code.
- Keine fachliche Variante ohne Buchbeleg — außer Werner entscheidet das
  ausdrücklich als bewusste Abweichung.

## Offene Fragen

- Format des Baustein-Katalogs (JSON? Python-Dataclass analog zu den
  Codeverträgen unter `400_mathematik/10_codevertraege`? etwas Drittes?).
- Verhältnis zu `300_messmodul` im Code: eigenständige Anwendung, die sich
  später verbindet, oder von Anfang an ein gemeinsames Datenmodell?
- Welche drei Rocklängen sind durch den geprüften Buchkontext fachlich belegt?
