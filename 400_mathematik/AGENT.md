# Mathematik — was hier drin gilt

## Navigation — Regel

Diese Datei führt nur zu den direkten Unterordnern von `400_mathematik/`.
Einzelne Fachdateien werden hier nicht aufgeführt. Sie gehören in die
Agentendatei des jeweiligen Unterordners.

Die Ladeliste dient der Navigation. Automatisch geladen werden nur die
angekreuzten Agentendateien.

## Navigation

- [x ] `10_mathe_einzupflegen/AGENT.md`

## Zweck

Die **Primitive**: Punkt, Gerade, Schnittpunkt, Lot, Normale, Kreis, Kurve,
Parallelversatz, Drehung, Fläche.

Diese Ebene ist **modeblind**. Sie kennt keinen Abnäher, keine Nahtzugabe und
keinen Hofenbitzer-Wert — sie rechnet mit Punkten und Zahlen. Deshalb hat sie
als einzige Ebene **keine Abhängigkeit**: sie benutzt keinen anderen Ordner.

Und sie ist die einzige Ebene, deren Quelle **nicht das Buch** ist.

## Grenze

| Nicht hier | Sondern |
|---|---|
| Was ein Abnäher ist | `000_sprache/` |
| Welchen Wert eine Zugabe hat, Winkel, Grenzen aus der Mode | `300_formeln/` |
| Der ausführende Code, Module, Tests | `500_python/` |
| Entscheidungen eines Kleides | `700_schnitte/` |

**Faustprobe:** Streiche aus einem Eintrag jedes Modewort. Bleibt er vollständig,
gehört er hierher. Fehlt danach etwas, gehört er nach `300_formeln`.

Konkret: „Nahtzugabe" heißt hier **Parallelversatz mit Abstand `s`**. Dass
dieser Abstand 1 cm beträgt, steht woanders.

Aus fremdem Code und aus DXF-Dateien darf **keine Schnittregel** abgeleitet
werden. DXF ist Export- und Vergleichsformat, sonst nichts.

## Quellenregel — hier gilt eine andere als überall sonst

Überall sonst im Repo gilt: Seitenzahl aus dem Buch. Hier nicht.

Geometrie ist nicht modespezifisch, das Buch ist dafür keine Quelle. Ein
Eintrag belegt sich stattdessen mit **nachprüfbarer Fachliteratur**:
Titel + URL + Abrufdatum, pro Aussage.

Daraus folgt die zweite Besonderheit: **Mathematik darf vorgecodet werden.**
Sie ist modeblind und deshalb ungefährlich. Konstruktionen dagegen nie — dort
stünde sonst der Code vor dem Prüfwert.

Ein Verweis auf vorhandenen Code ist **keine Quelle**. Er belegt nur, was die
Engine heute tut — nicht, dass es richtig ist.

## Nummernschlüssel

| Ordner | Inhalt |
|---|---|
| `10_mathe_einzupflegen` | Halde: 15 Notizen aus der Vorgänger-Engine, noch nicht eingepflegt |

In der Halde laufen die Dateien fortlaufend zweistellig (`00_uebersicht`,
`01_`–`14_`) und sind in fünf Blöcke gruppiert — das ist eine **Lernreihenfolge**,
kein Themenschlüssel.

Die Zielordnung entsteht erst beim Einpflegen. **Vorher nicht festlegen** — erst
wenn sichtbar ist, welche Primitive die Module wirklich rufen, zeigt sich, wie
sie zu bündeln sind.

## Form eines Eintrags

Vier Abschnitte, in dieser Reihenfolge:

```markdown
# <Nr> <Thema>

## Worum geht's (Klartext, auch für Nicht-Mathematiker)
## Die Mathematik (Formeln sauber, nachvollziehbar)
## Anwendung in der Schnittkonstruktion
## Quellen (pro Aussage: Titel + URL + Abrufdatum)
```

- **Worum geht's** — der Absatz, den Werner und Munkhuu lesen. Ohne Formel.
- **Die Mathematik** — Formeln als Codeblock, mit benannten Größen.
- **Anwendung** — wo die Konstruktion sie braucht, und ein Teil
  **Grenzen/unsicher**: wo das Verfahren bricht (konkave Ecken, Selbstschnitte,
  fast parallele Geraden, Länge null).
- **Quellen** — jede Aussage einzeln belegt.

Der Teil *Grenzen/unsicher* ist Pflicht. Ein Primitive ohne benannte Grenze
sieht fertiger aus, als es ist.

## Feste Konventionen

Sie gelten für **jedes** Primitive und dürfen nie pro Funktion wechseln:

| Was | Festlegung | Steht in |
|---|---|---|
| Einheit | intern **Millimeter**; cm-Werte am Eintritt umrechnen (`mm = cm · 10`) | `06_` |
| Y-Achse | zeigt **nach unten** — „nach unten" ist `+dy` | `01_` |
| Rundung | **spät** runden: intern ungerundet rechnen, erst für Anzeige und Export | `06_` |
| Numerik | Sonderfälle abfangen: Länge null, fast parallele Geraden (`EPSILON`) | `04_`, `07_`, `08_` |
| Nullpunkt | Rock/Hose oben links, Oberteil 7. HW — **Projektannahme, noch nicht am Buch geprüft** | `01_` |

## Fertig-Regel

Ein Eintrag ist fertig, wenn:

1. die **Formel** dasteht — nicht nur der Name des Verfahrens,
2. mindestens eine **nachprüfbare Quelle** mit Abrufdatum dabei ist,
3. die **Grenzen** benannt sind: wo bricht das Verfahren,
4. er **ohne ein einziges Modewort** auskommt.

## Offene Stellen

- Alle 15 Notizen liegen noch in der Halde und beziehen sich auf die
  **Vorgänger-Engine** (`../src/geometry.js`, `../src/draft.js`, JavaScript).
  Diese Dateien gibt es in diesem Repo nicht. Beim Einpflegen: Code-Anker
  streichen oder auf `500_python` umschreiben.
- Der dort beschriebene Rock-Prototyp ist **Aldrich-inspiriert**, nicht
  Hofenbitzer. Daraus darf keine Schnittregel übernommen werden.
- Blöcke 3–5 (`09_`–`14_`: Trigonometrie, Rotation, kubische Bézier, Kurvenlänge
  und Passung, Parametrik) sind geplant, aber nirgends umgesetzt.
- Die Nullpunkt-Konvention stammt aus einem Chat-Auftrag, nicht aus dem Buch —
  gegen Hofenbitzer Band 1/2 zu prüfen.
- Namensregel: die Wurzel bestimmt `90_` als Halde, der Ordner heißt aber
  `10_mathe_einzupflegen`. Entweder Ordner zurückbenennen oder die Regel oben
  streichen.
