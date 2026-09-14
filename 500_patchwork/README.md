# 500_patchwork

Das Patchwork-Modul ist die visuelle Oberfläche, auf der Werner sieht, welche
Bausteine für ein Kleidungsstück code-technisch vorhanden sind, und
entscheidet, welche davon verwendet werden und wo sie sitzen — zum Beispiel:
Reißverschluss seitlich oder rückwärtig am Rock.

Es ist **kein Maß-Eingabeformular** — das bleibt Aufgabe von
[`300_messmodul`](../300_messmodul). Das Patchwork-Modul liefert die
strukturelle Entscheidung (welcher Baustein, welche Lage); das Messmodul
liefert die Körpermaße. Beides zusammen ist der Input, der das künftige
Schnittmusterprogramm startet.

**Status: Konzeptphase.** Es existiert noch kein Code, keine Oberfläche und
kein festgelegtes Datenformat. Dieser Ordner hält fest, worum es geht und was
das Modul können muss, damit späterer Konstruktionscode von Anfang an darauf
passt, statt nachträglich umgebaut zu werden.

- [`SPEC.md`](SPEC.md) — Zweck, Grundprinzip und offene Fragen.
- [`AGENT.md`](AGENT.md) — Arbeitsregeln für diesen Ordner.
