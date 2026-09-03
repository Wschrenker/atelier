# Fachlich normalisierte Formeln — S. 509

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s509.md`
Originaltranskript: `s509.md`
Buchseite: Hofenbitzer, Band 1, S. 509

Die Seite trägt den vollständigen Shirt-Grundschnitt: Teil 1 die Rumpf-Konstruktion (Schritte 1 bis 12, Zeichnung `□3`), Teil 2 die Ärmel-Konstruktion (Schritte 13 bis 20, Zeichnung `□4`). Die Konstruktionstabelle mit allen Eingangsmaßen steht auf S. 508.

Besonderheit der Konstruktion: VT und RT werden **deckungsgleich** konstruiert; sie unterscheiden sich nur an Halsloch und Schulter. Der Ärmel wird direkt an das Rumpfteil konstruiert, seine Weite hängt damit unmittelbar an der Größe des Armlochs.

Vier Kandidatenzeilen sind extrahiert: zwei Schritttexte (Schritt 7 und Schritt 16) und zwei Zeilen mit Zeichnungsbeschriftungen. Sie tragen drei Rechenbeziehungen und erhalten drei Formel-IDs; eine Beschriftung ist Zeichnungsbeleg zu einer Formel derselben Seite und erhält keine zweite ID. Ausgeschlossen wurde keine Zeile.

## HOF-B1-S509-F01 — Abtragung des halben Armdurchmessers (Schritt 7)

- **Fachlicher Zweck:** Von P6 aus die Breite des angeschnittenen Ärmelansatzes abtragen und damit den seitlichen Endpunkt P7 der Brustlinie festlegen.
- **Quelle:** `formeln_s509.md`, Zeile 9; Originaltranskript `s509.md`, Zeile 20; Buchseite 509.
- **Originalbezeichnung:** `½ Armdurchmesser+ (ArD+)`
- **Normalisierte Bezeichnung:** `abtragung_halber_armdurchmesser_plus`

### Buchfassung

```text
7. Von P6 den ½ Armdurchmesser+ (ArD+) abtragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser_plus` | ArD+ | 10,8 (Konstruktionstabelle S. 508) | cm |
| `halbierungsfaktor` | `½` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
abtragung_p6_p7 = armdurchmesser_plus / 2

Buchwert der Konstruktionstabelle auf S. 508 (ArD+ = 10,8 cm):
abtragung_p6_p7 = 10,8 cm / 2 = 5,4 cm
```

Die Tabelle auf S. 508 rechnet dieses Teilmaß in der Spalte `Teilmaß` bereits vor (`½ = 5,4`); es ist dort als `HOF-B1-S508-F02` geführt.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abtragung_p6_p7` | Strecke von P6 zu P7 auf der Brustlinie, Breite des Ärmelansatzes | cm |

- **Abhängigkeiten:** `HOF-B1-S508-F01` und `HOF-B1-S508-F02`. Vorgelagert: P6 entsteht aus der Abtragung der `¼ Brustweite` von P4 (`HOF-B1-S509-F02`).
- **Gültigkeitsbereich und Randbedingungen:** Rumpf-Konstruktion, Zeichnung `□3`. Der Schritt setzt die Richtung nicht selbst, sondern folgt der Sammelanweisung der Seite: Die Grundlinien werden „nach links" abgewinkelt, die Konstruktion läuft von der Mitte nach außen. Die Zeichnungsbeschriftung `¼ Brustweite` / `½ ArD+` / `Brustlinie` (Extraktzeile 14) belegt, dass beide Strecken hintereinander auf der Brustlinie liegen.
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit. Der Schritttext nennt keinen Zielpunkt; P7 ist erst über Schritt 8 („Von P7 nach oben abwinkeln") als Endpunkt dieser Abtragung belegt.
- **Zeichnungsbeleg:** Die Beschriftung `½ ArD+` in Extraktzeile 14 (`formeln_s509.md`) wiederholt diese Beziehung und erhält nach der in `V3-J05` festgelegten Regel keine zweite ID.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Weil VT und RT deckungsgleich konstruiert werden, ist die halbe Ärmelansatzbreite für beide Teile dieselbe. Die Kette `ArD → ArD+ → ½ ArD+` nicht abkürzen: Die Weitenzugabe wirkt hier auf den Rumpf und über `HOF-B1-S509-F03` zugleich auf die Ärmelkugel.

## HOF-B1-S509-F02 — Abtragung der Viertel-Brustweite (Schritt 6)

- **Fachlicher Zweck:** Von P4 aus die halbe Rumpfbreite bis zum Armlochpunkt P6 abtragen und damit die Weite des Rumpfteils festlegen.
- **Quelle:** `formeln_s509.md`, Zeile 14; Originaltranskript `s509.md`, Zeile 48; Buchseite 509.
- **Originalbezeichnung:** `¼ Brustweite`
- **Normalisierte Bezeichnung:** `abtragung_viertel_brustweite`

### Buchfassung

```text
- `¼ Brustweite` / `½ ArD+` / `Brustlinie`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustweite` | BrW | 96 (Konstruktionstabelle S. 508) | cm |
| `teiler` | `¼` | 4 | dimensionslos |

### Formel und Rechenschritte

```text
abtragung_p4_p6 = brustweite / 4

Buchwert der Konstruktionstabelle auf S. 508 (BrW = 96 cm, ¼-Spalte 24):
abtragung_p4_p6 = 96 cm / 4 = 24 cm
```

Die Brustweite entsteht auf S. 508 aus `BrU 88 cm + 8 cm Zugabe`; diese Tabellenzeile liegt nicht im Extrakt.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abtragung_p4_p6` | Strecke von P4 zu P6 auf der Brustlinie, halbe Rumpfbreite | cm |

- **Abhängigkeiten:** `BrW` aus den Hauptmaßen der Konstruktionstabelle auf S. 508. Nachgelagert: `HOF-B1-S509-F01` trägt ab P6 weiter.
- **Gültigkeitsbereich und Randbedingungen:** Rumpf-Konstruktion, Zeichnung `□3`. Weil VT und RT deckungsgleich sind, ist `¼ BrW` zugleich die halbe Breite **eines** Schnittteils; die volle Brustweite verteilt sich auf zwei deckungsgleiche Hälften mit je `¼ BrW` beidseits. Die Weitenklasse steckt vollständig in der Brustweitenzugabe: `ca. 6 bis 12 cm` für das T-Shirt, `ca. 10 bis 16 cm` für das Sweatshirt (S. 508, Fließtext, nicht extrahiert).
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit.
- **Fundstelle ohne Schritttext im Extrakt:** Der zugehörige Schritttext steht im Transkript als Schritt 6 („Von P4 die ¼ Brustweite (BrW, hier 24 cm) abtragen.", `s509.md`, Zeile 19), ist dort aber **nicht** als Kandidatenzeile extrahiert. Belegt ist die Beziehung im Extrakt allein über die Zeichnungsbeschriftung, die deshalb hier eine eigene ID trägt — dieselbe Behandlung wie `HOF-B1-S501-F05` und `F06` in `V3-S03`. Wird der Extrakt später um Schritt 6 ergänzt, ist die ID **nicht** zu verdoppeln, sondern die neue Zeile als Schritttextbeleg hierher zu führen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Brustweitenzugabe als Modellparameter mit den beiden belegten Bereichen führen und den Beispielwert `+ 8 cm` als Vorgabe. Er liegt in beiden Bereichen und trennt T-Shirt und Sweatshirt daher nicht.

## HOF-B1-S509-F03 — Ärmelkugelbreite auf dem Kreisbogen (Schritt 16)

- **Fachlicher Zweck:** Auf dem Kreisbogen um den Ärmelpunkt ab P6 die um 1 cm verminderte halbe Ärmelansatzbreite abtragen und damit P16 als Formpunkt der Ärmelkugel festlegen.
- **Quelle:** `formeln_s509.md`, Zeile 19; Originaltranskript `s509.md`, Zeile 57; Buchseite 509.
- **Originalbezeichnung:** `½ Armdurchmesser+ (ArD+) − 1 cm`
- **Normalisierte Bezeichnung:** `aermelkugelbreite_ab_p6`

### Buchfassung

```text
16. Einen Kreisbogen um den ÄP durch P6 zeichnen und darauf ab P6 ½ Armdurchmesser+ (ArD+) − 1 cm abtragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser_plus` | ArD+ | 10,8 (Konstruktionstabelle S. 508) | cm |
| `halbierungsfaktor` | `½` | 2 | dimensionslos |
| `kugelabzug` | `− 1 cm` | 1 | cm |

### Formel und Rechenschritte

```text
aermelkugelbreite = (armdurchmesser_plus / 2) - kugelabzug

Buchwert der Konstruktionstabelle auf S. 508 (ArD+ = 10,8 cm):
aermelkugelbreite = (10,8 cm / 2) - 1 cm = 5,4 cm - 1 cm = 4,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `aermelkugelbreite` | Bogenstrecke von P6 zu P16 auf dem Kreisbogen um den Ärmelpunkt | cm |

- **Abhängigkeiten:** `HOF-B1-S508-F01`, `HOF-B1-S508-F02` und `HOF-B1-S509-F01` — P6 ist derselbe Punkt, von dem aus Schritt 7 den ungekürzten halben Armdurchmesser abträgt. `ÄP` entsteht in Schritt 8 als Viertelpunkt der halbierten und geviertelten Strecke von P7 zu P8.
- **Gültigkeitsbereich und Randbedingungen:** Ärmel-Konstruktion, Zeichnung `□4`. Die abgetragene Strecke liegt auf einem **Kreisbogen** um `ÄP` durch P6, ist also eine Bogenlänge und keine Gerade. Die Beschriftung `Kreisbogen` in der Zeichnung bestätigt das. Der Radius ist durch P6 festgelegt und wird nicht gerechnet.
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit. Der Abzug `1 cm` steht als fester Einzelwert ohne Bereich und ohne Begründung; die Quelle nennt keine Abhängigkeit von Größe oder Armlochweite. Er ist unverändert übernommen. Offen bleibt, ob die Angabe als Bogenlänge oder als Sehnenlänge gemeint ist — bei diesem Radius ist der Unterschied klein, die Quelle entscheidet ihn aber nicht; eine Festlegung wurde nicht erfunden.
- **Zeichnungsbeleg:** Die Beschriftung `½ ArD+ −1 cm` in Extraktzeile 24 (`formeln_s509.md`, Transkriptzeile 77) wiederholt diese Beziehung und erhält keine zweite ID.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Strecke als Bogenmaß auf dem Kreis um `ÄP` mit Radius `|ÄP P6|` ansetzen und die offene Bogen-/Sehnen-Frage im Modell kennzeichnen. Der Zusammenhang „größeres Armloch → weiterer Ärmel" (S. 508) läuft über genau diese Kette; `1 cm` ist der einzige Wert, der ihn dämpft.

## Zeichnungsbelege ohne eigene ID

| Extraktzeile | Beschriftung | Ziel-ID | Schritttext |
|---|---|---|---|
| Zeile 14 (Transkriptzeile 48) | `½ ArD+` | `HOF-B1-S509-F01` | S. 509, Schritt 7 |
| Zeile 24 (Transkriptzeile 77) | `½ ArD+ −1 cm` | `HOF-B1-S509-F03` | S. 509, Schritt 16 |

Beide Beschriftungen stehen auf derselben Seite wie ihr Schritttext. Sie sind nicht ausgeschlossen: Die Rechenbeziehungen sind vollständig und rechenfähig, sie sind nur bereits unter der ID des Schritttextes geführt.

Die dritte Angabe der Extraktzeile 14, `Brustlinie`, ist eine Linienbezeichnung ohne Rechenoperation und trägt keine Formel.

## Ausgeschlossene Kandidaten

Keine. Alle vier extrahierten Kandidatenzeilen sind in Formelblöcken abgebildet: drei tragen eigene IDs, zwei Beschriftungen sind Belege zu Formeln derselben Seite.

## Prüfhinweise

1. **Deckungsgleiches VT und RT:** Die Seite hält ausdrücklich fest, dass abweichend von anderen Oberteil-Grundschnitten „das VT und das RT deckungsgleich konstruiert" werden und sich nur an Halsloch und Schulter unterscheiden. Für die drei hier normalisierten Beziehungen gibt es deshalb **keine** getrennten Vorder- und Rückteilwerte. Das ist der wesentliche Unterschied zu den Oberteil-Grundschnitten aus `06_grundschnitte_oberteile_s171-196/` und darf bei einer späteren Zusammenführung nicht eingeebnet werden.
2. **Drei Halsloch-Beziehungen ohne Extraktzeile:** `HlB : 3` (Schritt 1), `HlB + 0,5 cm` (Schritt 9, hinten) und `HlB + 2,5 cm` (Schritt 11, vorne) sind vollständige Rechenbeziehungen mit der Eingabe `HlB = 6,5 cm` aus der Konstruktionstabelle. Sie stehen sowohl im Schritttext als auch in der Beschriftungsliste `□3`, liegen aber **nicht** im verbindlichen Extrakt und wurden deshalb nicht als Buchfassungen ergänzt. Sie sind die auffälligste Lücke dieser Seite: Ohne sie ist der Halsausschnitt — der einzige Unterschied zwischen VT und RT — rechnerisch nicht abgebildet. Siehe Prüfhinweis 6.
3. **Gedruckte Doppelung in Schritt 9:** Das Wort „Halslochbreite" steht dort zweimal hintereinander (schwarz im Fließtext, grün als Formelbezug), und das Verb lautet „antragen" statt „abtragen". Beides ist so gedruckt, im Transkript als Anmerkung festgehalten und ohne Wirkung auf die Rechenbeziehung.
4. **Schritte 18 und 19 sind ein Satz:** „Ellenbogenlinie bei ½ und die Oberarmweite bei ¼ der Ärmelmitte abwinkeln und kontrollieren." Der Satz läuft im Druck über zwei Zeilen, die Ziffern 18 und 19 stehen jeweils am Zeilenanfang. Es sind zwei Teilungen **derselben** Bezugsstrecke (Ärmelmitte), nicht zwei aufeinander aufbauende Schritte. Die Zeile liegt nicht im Extrakt; die Beschriftungen `Ellenbogenlinie` mit `½` und `½ Oberarmweite (OaW)` mit `¼` in der Zeichnung `□4` bestätigen die Lesart. Ergänzt wurde sie nicht.
5. **Die Oberarmweite ist Kontrollmaß, nicht Konstruktionsmaß:** Schritt 19 verlangt, die Oberarmweite zu „kontrollieren"; die Zeile `OaU` der Konstruktionstabelle auf S. 508 ist mit `+ ---` und `---` bewusst leer. Die Ärmelweite entsteht also aus der Konstruktion (`HOF-B1-S509-F01` und `F03`) und wird gegen den gemessenen Oberarmumfang nur geprüft — dieselbe Art von Beziehung wie die Weitenkontrollen `HOF-B1-S501-F07` und `F08`. Eine Korrekturmaßnahme für den Fall einer Verletzung nennt die Quelle nicht; sie wurde nicht ergänzt.
6. **Extraktionsgrenze:** Das Originaltranskript `s509.md` enthält weitere rechenfähige Beziehungen, die im verbindlichen Extrakt fehlen und deshalb nicht als Buchfassungen ergänzt wurden:
   - Zeile 11 bis 13 und 45: `HlB : 3` (Schritt 1), `MoL` und `AlT+` als Abtragungen (Schritte 3 und 4), `RüL` (Schritt 5);
   - Zeile 19: Schritt 6 mit `¼ Brustweite` — die Schritttextfundstelle zu `HOF-B1-S509-F02`;
   - Zeile 23: „Diese Strecke halbieren und vierteln → ÄP bei ¼" (Schritt 8) — die einzige Festlegung des Ärmelpunkts;
   - Zeile 25 und 33: `HlB + 0,5 cm` und `HlB + 2,5 cm` (Schritte 9 und 11), siehe Prüfhinweis 2;
   - Zeile 27 und 29: `SuNL` am Schulterwinkel `SuWi+` sowie die Armlochformung über `½ AlT+` und `¼ AlT+` (Schritt 9);
   - Zeile 31: `1 bis 2 cm` Schulterverschiebung (Schritt 10);
   - Zeile 37: `0 bis 1,5 cm` Einstellung an Taillen- und Saumlinie (Schritt 12);
   - Zeile 54 bis 57: Armlängenverlängerung (Schritt 13), `2 cm` tiefer für die Ärmelmitte (Schritt 14), `½ Ärmelsaumweite` (Schritt 15);
   - Zeile 58: „die Länge des Armlochs vom ÄP aus übertragen" (Schritt 17) — die Messübertragung, die zusammen mit `EW = 0 cm` von S. 508 die Ärmelkugellänge festlegt;
   - Zeile 62 und 63: die Teilungen `½` und `¼` der Ärmelmitte (Schritte 18 und 19), siehe Prüfhinweis 4;
   - Zeile 71 und 72: `Armlänge (60 cm)`, `Ärmellänge kurz (22 cm)`, `ca. 2 cm`.

   Der Extrakt deckt damit 3 von rund 15 rechenfähigen Beziehungen der Seite ab. Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt; der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
