# Couture — was hier drin gilt

## Zweck

Hier trifft der Schnitt auf einen **Menschen**.

Ein Ordner pro Auftrag: die **Maße der Braut**, das damit gerechnete Kleid und
die Dateien, die dabei herauskommen — **PDF zum Drucken**, DXF, SVG.

`700_schnitte` beschreibt das Kleid unabhängig von der Person. Hier bekommt es
Zahlen und wird eine Sache, die man zuschneiden kann.

## Grenze

| Nicht hier | Sondern |
|---|---|
| Wie das Kleid konstruiert ist, seine Entscheidungen | `700_schnitte/<kleid>/` |
| Module und Code | `500_python/` |
| Formeln und Buchbelege | `300_formeln/` |
| Was ein Maß bedeutet und wie es gemessen wird | `300_formeln/10_masse/10_MASSREGISTER.md` |

**Diese Ebene ist Endstation.** Nichts weiter unten greift je hier herein — kein
Modul, keine Formel, kein Kleid kennt einen Auftrag. Wer hier etwas findet, das
ein zweiter Auftrag auch bräuchte, hat es am falschen Ort abgelegt.

Und: hier wird **nichts von Hand nachgebessert**. Stimmt ein Maß nicht, wird das
Maß korrigiert und neu gerechnet — nie die erzeugte Datei.

## Nummernschlüssel

Ein Zehner pro Auftrag:

```
800_couture/
  10_<kundin>_<kleid>/
  20_<kundin>_<kleid>/
```

Der Ordnername nennt **wen** und **welches Kleid** — `10_munkhuu_kleid_v001`.
Die Fassung `v###` verweist auf den Stand in `700_schnitte`, aus dem gerechnet
wurde. **Eine vergebene Nummer wird nie neu belegt.**

## Form eines Eintrags

| Datei | Was sie ist |
|---|---|
| `MASSE.md` | die gemessenen Maße dieser Person |
| `ausgabe/` | die erzeugten Dateien — PDF, DXF, SVG |
| `PROTOKOLL.md` | Anproben, Änderungen, was beim Nähen anders kam — ab der ersten Anprobe |

### `MASSE.md`

- Kürzel **aus dem Maßregister**, nicht neu erfunden — `BrU`, `TaU`, `gRüL`
- gemessen **nach der Messanweisung** des Registers, nicht nach Gefühl
- **Datum** und **wer gemessen hat** stehen dabei
- beidseitig gemessene Maße mit beiden Werten, dann der Wert, mit dem gerechnet
  wird (Mittelwert oder der kleinere — was das Register sagt)
- ein nicht gemessenes Maß bleibt **leer**. Kein Tabellenwert als Ersatz, ohne
  dass es dabeisteht.

### `ausgabe/`

Jede Datei nennt im Namen oder im Kopf: **Kleid, Fassung, Datum**.
Beispiel: `kleid_v001_2026-09-03.pdf`.

## Fertig-Regel

| Was | Fertig, wenn |
|---|---|
| **Ein Maß** | nach der Anweisung des Registers gemessen, mit Datum und Namen |
| **Eine Ausgabe** | maßhaltig und rückverfolgbar: welches Kleid, welche Fassung, welches Datum |
| **Der Auftrag** | das Kleid sitzt |

**Kein PDF ohne Kontrollquadrat.** 50 × 50 mm auf dem Ausdruck — misst es nicht
50 mm, hat der Drucker skaliert und der ganze Schnitt ist falsch. Die Regel
dazu steht in `400_mathematik` (`06_einheiten_und_masshaltigkeit.md`).

Erzeugte Dateien lassen sich jederzeit neu rechnen und müssen nicht gesammelt
werden. **Eine Ausnahme:** die Datei, nach der wirklich **zugeschnitten** wurde,
wird aufgehoben. Sie ist der einzige Beleg dafür, was das fertige Kleid
tatsächlich war.

## Offene Stellen

- Der Ordner ist **leer** — der erste Auftrag entsteht, wenn Kleid v001 durch
  `700_schnitte` durch ist.
- **Persönliche Daten:** Maße einer Kundin gehören einer Person. Ob dieser
  Ordner ins Git kommt oder lokal bleibt, ist **nicht entschieden**. Bis dahin:
  keine echten Kundenmaße committen.
- Ob PDF und DXF ins Git gehören, hängt an derselben Entscheidung. Die Fotos
  sind über `.gitignore` schon draußen, Ausgabedateien nicht.
- Wer die Ausgabe **erzeugt**, ist noch offen — siehe `500_python`: dort ist
  noch nicht festgelegt, wo der Export liegt.
