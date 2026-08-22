# Sprache — was hier drin gilt

Bedarfswissen — nur bei Bedarf lesen: `2_sprache_bedarf.md`

## Navigation — Regel

Diese Datei führt nur zu den direkten Unterordnern von `000_sprache/`.
Einzelne Fachdateien werden hier nicht aufgeführt. Sie gehören in die
Agentendatei des jeweiligen Unterordners.

Die Ladeliste dient der Navigation. Automatisch geladen werden nur die
angekreuzten Agentendateien.

## Navigation

- [x ] `10_gosslar/AGENT.md`
- [x ] `20_schnittmuster/AGENT.md`
- [x ] `30_lexikon/AGENT.md`

## Zweck

Die gemeinsame Sprache: *Abkürzungen*, *Zeichen*, *Begriffe*.

Diese Ebene liegt **unter allen anderen** — auch die Quelle wird mit ihr gelesen.
Sie benutzt keinen anderen Ordner und rechnet nichts.

Merksatz: Hier steht, **was ein Wort bedeutet** — nicht, **was man damit rechnet**.

## Grenze

| Nicht hier | Sondern |
|---|---|
| Maßnamen mit Rechenweg | `300_formeln/10_masse/` |
| Zahlenwerte, Größentabellen | `300_formeln/10_masse/10_massregister.md` |
| Buchseiten, Abschriften ganzer Kapitel | `100_quellen/` |
| Konstruktionsschritte und ihre Reihenfolge | `500_python/`, `700_schnitte/` |
| Begriff ohne Definition oder ohne Seitenzahl | `600_prozess/10_begriffe_offen.md` |

Ein Wort darf hier stehen, sobald es **im Buch vorkommt**. Was daraus gerechnet
wird, gehört nie hierher — auch nicht „nur als Hinweis".

## Nummernschlüssel

Die Zehner benennen die direkten Themenordner von `000_sprache/`:

| Ordner | Thema |
|---|---|
| `10_gosslar` | Gosslar-Begriffe, nach Buchkategorien geordnet |
| `20_schnittmuster` | Schnittmuster-, Zuschnitts- und Dressierzeichen |
| `30_lexikon` | Abkürzungen, Operanden und Sachwortverzeichnis |

Die Dateien innerhalb eines Themenordners werden in dessen `AGENT.md` geführt.
Zusammengehörige `.md`- und `.html`-Dateien liegen dort direkt nebeneinander.

Neues Thema → nächster freier Zehner.
**Eine vergebene Nummer wird nie neu belegt.**

## Form eines Eintrags

### Zwei Dateiarten, zwei Aufgaben

| Endung | Was es ist | Aufgabe |
|---|---|---|
| `.md` | Die Abschrift als Tabelle — lesbar für Mensch und Maschine | **gilt** |
| `.html` | Foto der Originalzeichen aus dem Buch, mit Erklärung daneben | **beweist** |

Das Bild ist im HTML als `base64` eingebettet. Die Datei läuft dadurch allein,
ohne Bilderordner — deshalb ist sie groß. Das ist Absicht, kein Versehen.

**Bei Widerspruch gilt das Bild.** Die `.md` ist die Abschrift, die `.html` zeigt
das Original.

### Abkürzung — eine Tabellenzeile

`| Kurzzeichen | Bedeutung |`

Neue Kurzzeichen werden nicht erfunden, sondern nach der Systematik in
`30_lexikon/10_abkuerzungen_systematik_eigenschaften_betraege_werte_operanden_aktionen.md` zusammengesetzt: Kleinbuchstabe für Richtung und Lage steht
**vorn**, Großbuchstabe für Betrag und Wert steht **hinten** — `AlT` = Armlochtiefe.

### Zeichen — eine Tabellenzeile plus Bild

`| Symbol | Bedeutung | Erklärung |` in der `.md`, dasselbe Zeichen im
zugehörigen `.html`.

### Begriff — Gosslar-Schema

```markdown
#### [Deutscher Name] ([English Name])
- **Definition:** Was ist das?
- **Position:** Wo ist es?
- **Breite/Länge/Tiefe:** Maße/Parameter
- **Formeln:** Verweis nach 300_formeln, hier keine Rechnung
- **Varianten:** Besonderheiten, Alternativen
- **Quelle:** Buch + Seite
```

`Quelle` ist **Pflichtfeld**. Ohne Seitenzahl ist der Eintrag kein Eintrag.

## Fertig-Regel

Ein Eintrag ist fertig, wenn:

1. er **im Buch belegt** ist — Buch und Seite stehen dabei,
2. seine Bedeutung dasteht, nicht seine Berechnung,
3. bei Zeichen: `.md` und `.html` beide vorhanden sind.

Ein `.html` ohne `.md` ist erlaubt, aber es ist immer eine **offene Stelle**, nie
ein fertiger Eintrag. **Nur eine fertige `.md` darf von anderen Ebenen zitiert
werden.**

Nicht raten, nicht aus Allgemeinwissen füllen — sonst steht Nicht-Hofenbitzer im
Glossar. Unbelegtes wandert nach `600_prozess/10_begriffe_offen.md` und wartet
dort auf die Buchseite.

## Offene Stellen

- `22_zuschnittszeichen.html` hat **keine `.md`** — die Zeichen liegen als Bild
  vor, die Abschrift fehlt. Sie bekommt dann `23_`.
- `10_gosslar/1_gosslar.md` — die Einträge tragen **keine Seitenzahl**, `Formeln`
  steht überall auf „Folgen". Nach der Fertig-Regel ist damit noch **kein**
  Eintrag fertig. Erst belegen, dann zitieren.

> Die Umbenennungen dieses Ordners (`10_abkuerzungen_systematik_eigenschaften_betraege_werte_operanden_aktionen.md`,
> `20_schnittmuster_symbole.md`) stehen repo-weit in
> `../2_atelier_bedarf.md` und werden hier nicht wiederholt.
