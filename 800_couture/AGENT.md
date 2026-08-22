# Couture — was hier drin gilt

## Navigation — Regel

Diese Datei führt nur zu den direkten Unterordnern von `800_couture/`.
Einzelne Fachdateien werden hier nicht aufgeführt. Sie gehören in die
Agentendatei des jeweiligen Unterordners.

Die Ladeliste dient der Navigation. Automatisch geladen werden nur die
angekreuzten Agentendateien.

## Navigation

- [ ] `10_luna_flow/AGENT.md`

## Zweck

Hier trifft der Schnitt auf einen **Menschen**.

Ein Ordner pro Auftrag: die **Maße der Braut** und das damit gerechnete Kleid.
Als spätere Ausgabeformate sind **PDF, DXF, SVG und JSON** vorgesehen. Wie sie
genau erzeugt und wo sie abgelegt werden, ist noch offen.

`700_schnitte` beschreibt das Kleid unabhängig von der Person. Hier bekommt es
Zahlen und wird eine Sache, die man zuschneiden kann.

## Grenze

| Nicht hier | Sondern |
|---|---|
| Wie das Kleid konstruiert ist, seine Entscheidungen | `700_schnitte/<kleid>/` |
| Module und Code | `500_python/` |
| Formeln und Buchbelege | `300_formeln/` |
| Was ein Maß bedeutet und wie es gemessen wird | `300_formeln/10_masse/10_massregister.md` |

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
| Ausgabe — Form und Ablage noch offen | Ziel: PDF, DXF, SVG und JSON |
| `PROTOKOLL.md` | Anproben, Änderungen, was beim Nähen anders kam — ab der ersten Anprobe |

### `MASSE.md`

- Kürzel **aus dem Maßregister**, nicht neu erfunden — `BrU`, `TaU`, `gRüL`
- gemessen **nach der Messanweisung** des Registers, nicht nach Gefühl
- **Datum** und **wer gemessen hat** stehen dabei
- beidseitig gemessene Maße mit beiden Werten, dann der Wert, mit dem gerechnet
  wird (Mittelwert oder der kleinere — was das Register sagt)
- ein nicht gemessenes Maß bleibt **leer**. Kein Tabellenwert als Ersatz, ohne
  dass es dabeisteht.

### Ausgabe — noch offen

PDF, DXF, SVG und JSON geben der Roadmap die Richtung. Dateiaufbau, technische
Erzeugung, Benennung und Ablage werden erst am ersten realen Exportfall
festgelegt.

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

- `10_luna_flow/` ist als erster Auftragsordner angelegt. Fachdateien liegen
  dort noch nicht.
- **Persönliche Daten:** Echte Kundenmaße bleiben lokal. `MASSE.md` wird über
  `.gitignore` vom Repo ferngehalten; im Repo werden keine echten Maße abgelegt.
- PDF, DXF, SVG und JSON sind als Ziel bekannt. Ort und Aufbau der Exportmodule
  sowie die Ablage der erzeugten Dateien sind noch nicht entschieden.
- Offene Aufgaben werden nicht hier, sondern in `600_prozess` geführt.
