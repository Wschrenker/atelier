# Fachlich normalisierte Formeln — S. 491

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s491.md`  
Originaltranskript: `s491.md`  
Buchseite: Hofenbitzer, Band 1, S. 491

Die Seite konstruiert den Cape-Grundschnitt. Sie erklärt nur die abweichenden Schritte und verweist für den Rest auf den Oberteil-Grundschnitt: „P1 bis P10 und P14 bis P16 sowie P19 bis P23 sind identisch mit dem Oberteil-GS bis Seite 179.“ Die extrahierten Kandidatenzeilen sind Bemaßungsbeschriftungen der Konstruktionszeichnung `□1`; ein begleitender Schritttext fehlt, weil die Schritte 11, 12 und 13 nur „bemaßt markieren“ lauten.

## HOF-B1-S491-F01 — Abtragung aus der Halslochbreite mit festem Zuschlag

- **Fachlicher Zweck:** Eine Strecke aus der Halslochbreite zuzüglich 0,5 cm bestimmen; nach der Lesart des identischen Oberteil-Grundschnitts die vordere Halslochtiefe von P20 nach unten.
- **Quelle:** `formeln_s491.md`, Zeile 9; Originaltranskript `s491.md`, Zeile 47; Buchseite 491.
- **Originalbezeichnung:** `HlB + 0,5 cm`
- **Normalisierte Bezeichnung:** `abtragung_aus_halslochbreite`

### Buchfassung

```text
- `HlB` / `HlB + 0,5 cm` / `HlB :3 + 1 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `halslochbreite` | HlB | cm |
| `halsloch_zuschlag` | `0,5 cm` | cm |

### Formel und Rechenschritte

```text
abtragung_aus_halslochbreite = halslochbreite + halsloch_zuschlag
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abtragung_aus_halslochbreite` | abzutragende Strecke aus der Halslochbreite | cm |

- **Abhängigkeiten:** HlB aus dem Maßsatz beziehungsweise der Konstruktionstabelle des zugrunde liegenden Oberteil-Grundschnitts.
- **Gültigkeitsbereich:** Grundkonstruktion des Capes, vorderer Halslochbereich.
- **Technische Randbedingung:** Der Zuschlag ist ein fester Wert, kein Bereich. Die Richtung der Abtragung ist auf S. 491 nicht angegeben.
- **Offene Fragen oder Widersprüche:** S. 491 nennt weder Ausgangspunkt noch Zielpunkt der Strecke. Die Zuordnung zur vorderen Halslochtiefe stützt sich auf `s181.md`, Zeile 32 („Von P20 nach unten HlB + 0,5 abtragen und zum HlP das vordere Halsloch formen“), also auf eine andere Buchseite. S. 491 erklärt P19 bis P23 ausdrücklich für identisch mit dem Oberteil-Grundschnitt, belegt die Zuordnung aber nicht selbst.
- **Status:** `hypothetisch`
- **Hinweis für die spätere Python-Umsetzung:** Die Rechnung ist eindeutig; die Zuordnung zu P20 erst nach Bestätigung der Seitenverknüpfung fest verdrahten.

## HOF-B1-S491-F02 — Brustbreite mit Cape-Zugabe

- **Fachlicher Zweck:** Die Konstruktionsbrustbreite des Capes aus der halben Brustbreite und einem Zugabenbereich bestimmen.
- **Quelle:** `formeln_s491.md`, Zeile 14; Originaltranskript `s491.md`, Zeile 49; Buchseite 491.
- **Originalbezeichnung:** `BrB + 2 bis 3 cm`
- **Normalisierte Bezeichnung:** `brustbreite_mit_cape_zugabe`

### Buchfassung

```text
- `½ BrB+ – 0,3 cm` / `BrB + 2 bis 3 cm` / `RüB + 1,5 bis 2 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `halbe_brustbreite` | BrB | cm |
| `brustbreiten_zugabe_cape` | `2 bis 3 cm` | cm |

### Formel und Rechenschritte

```text
brustbreite_mit_cape_zugabe = halbe_brustbreite + brustbreiten_zugabe_cape
```

Die Zugabe liegt laut Zeichnungsbeschriftung zwischen `2 cm` und `3 cm`.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `brustbreite_mit_cape_zugabe` | Brustbreite des Capes einschließlich Zugabe, im Buch als `BrB+` geführt | cm |

- **Abhängigkeiten:** BrB aus dem Maßsatz; gewählte Zugabe innerhalb des Bereichs.
- **Gültigkeitsbereich:** Grundkonstruktion des Capes.
- **Technische Randbedingung:** BrB ist bereits ein halbes Breitenmaß; die Zugabe gilt für den halben Schnitt. Die Zugabe ist ein Bereich und muss als Modellparameter gewählt werden.
- **Offene Fragen oder Widersprüche:** Die Beschriftung schreibt keine Ergebnisbezeichnung aus. Dass das Ergebnis das `BrB+` dieser Konstruktion ist, folgt aus der Schreibweise des Buches (`BrB + Zugabe = BrB+`, S. 177 und S. 178) und daraus, dass dieselbe Zeichnung `½ BrB+ – 0,3 cm` verwendet. Die Quelle legt keine Auswahlregel innerhalb des Bereichs fest.
- **Abgrenzung:** Die Cape-Zugabe von `2 bis 3 cm` liegt deutlich über den Brustbreiten-Zugaben der Passformklassen des Oberteil-Grundschnitts (`1` bis `1,2 cm`, S. 177 und S. 178). Sie ist eine eigene Angabe dieser Seite und wurde nicht aus den Passformklassen abgeleitet.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `brustbreiten_zugabe_cape` auf `2 bis 3 cm` begrenzen und nicht aus der Passformklassentabelle der Oberteile beziehen.

## HOF-B1-S491-F03 — Rückenbreite mit Cape-Zugabe

- **Fachlicher Zweck:** Die Konstruktionsrückenbreite des Capes aus der halben Rückenbreite und einem Zugabenbereich bestimmen.
- **Quelle:** `formeln_s491.md`, Zeile 14; Originaltranskript `s491.md`, Zeile 49; Buchseite 491.
- **Originalbezeichnung:** `RüB + 1,5 bis 2 cm`
- **Normalisierte Bezeichnung:** `rueckenbreite_mit_cape_zugabe`

### Buchfassung

```text
- `½ BrB+ – 0,3 cm` / `BrB + 2 bis 3 cm` / `RüB + 1,5 bis 2 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `halbe_rueckenbreite` | RüB | cm |
| `rueckenbreiten_zugabe_cape` | `1,5 bis 2 cm` | cm |

### Formel und Rechenschritte

```text
rueckenbreite_mit_cape_zugabe = halbe_rueckenbreite + rueckenbreiten_zugabe_cape
```

Die Zugabe liegt laut Zeichnungsbeschriftung zwischen `1,5 cm` und `2 cm`.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `rueckenbreite_mit_cape_zugabe` | Rückenbreite des Capes einschließlich Zugabe, im Buch als `RüB+` geführt | cm |

- **Abhängigkeiten:** RüB aus dem Maßsatz; gewählte Zugabe innerhalb des Bereichs.
- **Gültigkeitsbereich:** Grundkonstruktion des Capes.
- **Technische Randbedingung:** RüB ist bereits ein halbes Breitenmaß; die Zugabe gilt für den halben Schnitt.
- **Offene Fragen oder Widersprüche:** Wie bei `HOF-B1-S491-F02` schreibt die Beschriftung keine Ergebnisbezeichnung aus; die Zuordnung zu `RüB+` folgt der Schreibweise des Buches. Die Quelle legt keine Auswahlregel innerhalb des Bereichs fest.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `rueckenbreiten_zugabe_cape` auf `1,5 bis 2 cm` begrenzen.

## HOF-B1-S491-F04 — Armdurchmesser mit Cape-Zugabe

- **Fachlicher Zweck:** Den Konstruktionsarmdurchmesser des Capes aus dem Armdurchmesser und einem Zugabenbereich bestimmen.
- **Quelle:** `formeln_s491.md`, Zeile 15; Originaltranskript `s491.md`, Zeile 50; Buchseite 491.
- **Originalbezeichnung:** `ArD + 1,5 bis 2 cm` (2×)
- **Normalisierte Bezeichnung:** `armdurchmesser_mit_cape_zugabe`

### Buchfassung

```text
- `ArD + 1,5 bis 2 cm` (2×)
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `armdurchmesser` | ArD | cm |
| `armdurchmesser_zugabe_cape` | `1,5 bis 2 cm` | cm |

### Formel und Rechenschritte

```text
armdurchmesser_mit_cape_zugabe = armdurchmesser + armdurchmesser_zugabe_cape
```

Die Zugabe liegt laut Zeichnungsbeschriftung zwischen `1,5 cm` und `2 cm`.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `armdurchmesser_mit_cape_zugabe` | Armdurchmesser des Capes einschließlich Zugabe, im Buch als `ArD+` geführt | cm |

- **Abhängigkeiten:** ArD aus dem Maßsatz; gewählte Zugabe innerhalb des Bereichs.
- **Gültigkeitsbereich:** Grundkonstruktion des Capes.
- **Technische Randbedingung:** Der Vermerk `(2×)` der Extraktion bedeutet, dass die Beschriftung zweimal in der Zeichnung steht. Er ist eine Zählung der Beschriftung, kein Rechenfaktor und keine Verdoppelung des Maßes.
- **Offene Fragen oder Widersprüche:** S. 491 gibt nicht an, worauf sich die beiden Beschriftungen beziehen. Ob es sich um dieselbe Strecke in zwei Ansichten oder um zwei getrennte Abtragungen handelt, ist aus dem Extrakt nicht entscheidbar. Eine Teilung in `⅔` und `⅓`, wie sie der Oberteil-Grundschnitt für `ArD+` vorsieht (`HOF-B1-S180-F01`), ist auf S. 491 nicht belegt und wurde nicht ergänzt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `armdurchmesser_zugabe_cape` auf `1,5 bis 2 cm` begrenzen; die Zugabe einmal bilden und nicht doppelt anwenden.

## Bereits an anderer Stelle normalisierte Beziehungen

Zwei Beschriftungen der Seite wiederholen Beziehungen, die im Oberteil-Grundschnitt bereits normalisiert sind. Sie erhalten hier keine eigene Formel-ID und werden als Buchnachweis geführt.

| Beschriftung auf S. 491 | Extraktzeile | Bereits normalisiert als | Fundstelle |
|---|---:|---|---|
| `HlB :3 + 1 cm` | 9 | `HOF-B1-S179-F01` — vertikale Lage von P2 aus der Halslochbreite | `06_grundschnitte_oberteile_s171-196/formeln_s179_normalisiert.md` |
| `½ BrB+ – 0,3 cm` | 14 | `HOF-B1-S181-F01` — horizontale Lage des Brustpunkts | `06_grundschnitte_oberteile_s171-196/formeln_s181_normalisiert.md` |

Die Wiederverwendung ist durch S. 491 selbst gedeckt: die Seite erklärt P1 bis P10, P14 bis P16 und P19 bis P23 für identisch mit dem Oberteil-Grundschnitt. `½ BrB+ – 0,3 cm` bezieht sich auf S. 491 allerdings auf das `BrB+` dieser Seite, also auf `HOF-B1-S491-F02`, nicht auf die Passformklassenwerte von S. 178.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s491.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 20 | 1 | `2 bis 3 cm` (2×) — Bereichsangabe ohne benannte Eingabe und ohne benannte Ausgabe |
| Zeile 25 | 1 | `4 bis 6 cm` (2×) — Bereichsangabe ohne benannte Eingabe und ohne benannte Ausgabe |
| Zeile 26 | 1 | `1 cm bis 4 cm` (2×, an der Leiste) — Bereichsangabe zur Leiste des Armausgriffs ohne Rechenoperation |
| **Summe** | **3** | **3 reine Bereichsangaben ausgeschlossen** |

Ebenfalls nicht als eigene Formel geführt wird das isolierte `HlB` in Zeile 9. Es ist eine direkte Maßangabe ohne Rechenoperation und dient als Eingabe der Formeln `HOF-B1-S491-F01` und `HOF-B1-S179-F01`.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s491.md` enthält weitere rechenfähige und bemaßte Angaben, die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen und deshalb nicht als Buchfassungen ergänzt wurden:

- `BrT – 1 cm`, `VL – 1 cm` und `AlT + 1 bis 2 cm` (Zeile 48) — Beziehungen derselben Bauart wie die hier normalisierten;
- `SuWi – 2°` (Zeile 51) sowie Schritt 16, die einzige Winkelangabe der Seite;
- `auf Kreisbogen üt – 1 cm` (Zeile 52);
- `Zwischenraum mind. 15 cm` (Zeile 54) und die Leistenlänge `28 bis 32 cm` (Zeile 57, Schritt 31);
- `6 bis 7 cm` Ausstellung an Taillen- und Seitenlinie (Schritt 17);
- die Saumteilungen `⅓ / ⅓ / ⅓ / ½ / ⅓` (Zeile 64) und das Lot von der Hälfte der hinteren Saumlinie (Schritt 29);
- die Einzelwerte `0,7 cm`, `0,5 cm` und `2 cm` (Zeile 59).

Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
