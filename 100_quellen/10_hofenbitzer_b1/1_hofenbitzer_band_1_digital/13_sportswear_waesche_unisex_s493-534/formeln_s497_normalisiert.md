# Fachlich normalisierte Formeln — S. 497

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s497.md`
Originaltranskript: `s497.md`
Buchseite: Hofenbitzer, Band 1, S. 497

Die Seite führt im Block „Sport · Wäsche · Unisex" den Grundschnitt der Boxershorts, einer sehr einfachen Unisex-Shorts, die laut `□1` „nur mit drei Körpermaßen konstruiert" wird: TaU 72 cm, HüU 97 cm und SiH 26 cm. Der Bund ist ohne Verschluss. Die extrahierten Kandidatenzeilen stammen aus den Konstruktionsschritten 2–3 und 4, aus den Beschriftungen der Grundkonstruktionszeichnung `□2`, aus den Schnittteil-Stempeln der Zeichnungen `□3` und `□4` sowie aus der redaktionellen Anmerkung des Transkripts. Die Seite verweist einleitend auf S. 494, führt jedoch einen eigenen, kürzeren Maßsatz und eigene Konstruktionsschritte und erklärt keine Identität mit dem Grundschnitt der einfachen Hose.

## HOF-B1-S497-F01 — Schrittlinien-Abtragung zu P3

- **Fachlicher Zweck:** Die auf der Schrittlinie abzutragende Grundbreite der Boxershorts bestimmen, die nach oben zur Taillenlinie abgewinkelt wird und den Punkt P3 ergibt.
- **Quelle:** `formeln_s497.md`, Zeile 9; Originaltranskript `s497.md`, Zeile 27; Buchseite 497. Zeichnungsbeleg: `formeln_s497.md`, Zeile 19 (`s497.md`, Zeile 55).
- **Originalbezeichnung:** `¼ HüU + 1 cm` beziehungsweise `¼ HüU +1 cm`.
- **Normalisierte Bezeichnung:** `schrittlinien_grundbreite_boxershorts`

### Buchfassung

```text
**2–3** Auf der Schrittlinie ¼ HüU + 1 cm abtragen und nach oben zur Taillenlinie abwinkeln → P3
```

```text
- `¼ HüU +1 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `viertel_hueftumfang` | ¼ HüU | 24,25 | cm |
| `breitenzuschlag` | `1 cm` | 1 | cm |

### Formel und Rechenschritte

```text
schrittlinien_grundbreite = viertel_hueftumfang + breitenzuschlag

Buchwerte der Maßtabelle (HüU = 97 cm):
schrittlinien_grundbreite = 24,25 cm + 1 cm = 25,25 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `schrittlinien_grundbreite` | auf der Schrittlinie abzutragende Strecke bis P3 | 25,25 | cm |

- **Abhängigkeiten:** HüU aus der Maßtabelle `□1` (`s497.md`, Zeile 16). Ein Viertelwert ist auf S. 497 nicht ausgewiesen; er wurde aus dem gedruckten HüU gebildet und ist als Rechenkontext gekennzeichnet, nicht als Buchwert.
- **Gültigkeitsbereich:** Grundschnitt der Boxershorts, Konstruktionsschritte 2–3, DOB-Größe 38.
- **Technische Randbedingung:** Der Wert ist eine Abtragung auf der Schrittlinie, keine fertige Hosenbreite. Das anschließende Abwinkeln nach oben zur Taillenlinie ist eine Linienkonstruktion und von der Strecke zu trennen.
- **Offene Fragen oder Widersprüche:** Keine. Schritttext und Zeichnungsbeschriftung stimmen überein.
- **Abgrenzung:** Die Beziehung ist wortgleich mit `HOF-B1-S494-F02` (einfache Hose) und `HOF-B1-S109-F02` (Standardhose), dort jeweils als Hinterhosenbreite. Auf S. 497 ist sie keine hHoB, sondern eine Abtragung an einem Schnitt ohne getrennte Vorder- und Hinterhosenbreite; sie erhält deshalb eine eigene ID.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Zuschlag als festen Wert `1 cm` führen. Das Ergebnis ist die Eingabe von `HOF-B1-S497-F02`; beide Strecken liegen hintereinander auf derselben Linie.

## HOF-B1-S497-F02 — Weitermessen zu P4

- **Fachlicher Zweck:** Die nach P3 auf derselben Linie zusätzlich abzutragende Strecke als ein Drittel der zuvor gemessenen Strecke bestimmen.
- **Quelle:** `formeln_s497.md`, Zeile 14; Originaltranskript `s497.md`, Zeile 29; Buchseite 497. Zeichnungsbeleg: `formeln_s497.md`, Zeile 20 (`s497.md`, Zeile 56). Redaktionelle Anmerkung: `s497.md`, Zeilen 87–89.
- **Originalbezeichnung:** Schritttext `⅓ von ¼ HüU + cm1`; Zeichnung `⅓ von ¼ HüU +1 cm`.
- **Normalisierte Bezeichnung:** `weitermessung_boxershorts`

### Buchfassung

```text
**4** und ⅓ von ¼ HüU + cm1 weitermessen.
```

```text
- `⅓ von ¼ HüU +1 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `schrittlinien_grundbreite` | `¼ HüU +1 cm` aus `HOF-B1-S497-F01` | 25,25 | cm |
| `teilungsfaktor` | `⅓` | 1/3 | dimensionslos |

### Formel und Rechenschritte

```text
weitermessung = schrittlinien_grundbreite / 3
              = (viertel_hueftumfang + 1 cm) / 3

Rechenkontext mit den Maßen der Seite (HüU = 97 cm):
weitermessung = 25,25 cm / 3 = 8,4166… cm
```

### Ausgabe

| Technische Variable | Bedeutung | Exakt | Einheit |
|---|---|---:|---|
| `weitermessung` | nach P3 zusätzlich abzutragende Strecke bis P4 | 8,4166… | cm |

- **Abhängigkeiten:** `HOF-B1-S497-F01`.
- **Gültigkeitsbereich:** Grundschnitt der Boxershorts, Konstruktionsschritt 4, DOB-Größe 38.
- **Technische Randbedingung:** Das Buch druckt für diesen Schritt kein Ergebnis; der Zahlenwert ist nur als Rechenkontext ausgewiesen und keine Buchangabe. Eine Rundungsregel nennt die Quelle nicht.
- **Offene Fragen oder Widersprüche:** **Satzfehler in der Quelle.** Der Schritttext schreibt `+ cm1` statt `+1 cm`. Die Anmerkung des geprüften Transkripts (`s497.md`, Zeilen 87–89) hält dies ausdrücklich als Satzfehler fest und belegt die richtige Form über die Beschriftung der Zeichnung `□2`. Zahl und Einheit sind damit durch die Quelle selbst geklärt und nicht ergänzt; die fehlerhafte Buchfassung bleibt unverändert stehen.
- **Abgrenzung — geprüfte und verworfene Lesart:** `⅓ von ¼ HüU +1 cm` ließe sich grammatisch auch als `(¼ HüU) / 3 + 1 cm` lesen, was 9,0833 cm ergäbe. Dagegen sprechen zwei Belege der Seite selbst: Schritt 4 beginnt mit „und … weitermessen" und bezieht sich damit auf die unmittelbar zuvor in Schritt 2–3 gemessene Strecke; und die Zeichnung `□2` beschriftet die beiden aneinandergrenzenden Teilstrecken als `¼ HüU +1 cm` und `⅓ von ¼ HüU +1 cm`, benennt die erste also wörtlich als Bezugsgröße der zweiten. Die verworfene Lesart ist hier nur festgehalten und nicht als zweite Buchfassung geführt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Faktor als exakten Bruch `1/3` führen und erst bei der Ausgabe runden. Die Gesamtstrecke von P2 bis P4 beträgt `(4/3) * (viertel_hueftumfang + 1 cm)`.

## HOF-B1-S497-F03 — Unbezeichneter Ausdruck `HüU : 20 + 3 cm`

- **Fachlicher Zweck:** Nicht bestimmbar. Der Ausdruck steht als Bemaßung in der Zeichnung `□2`, ohne dass Schritttext oder Beschriftung die zugehörige Strecke benennen.
- **Quelle:** `formeln_s497.md`, Zeile 21; Originaltranskript `s497.md`, Zeile 57; Buchseite 497.
- **Originalbezeichnung:** `HüU : 20 + 3 cm`.
- **Normalisierte Bezeichnung:** `unbezeichneter_ausdruck_s497`

### Buchfassung

```text
- `HüU : 20 + 3 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `zuschlag` | `3 cm` | 3 | cm |

### Formel und Rechenschritte

```text
wert = (hueftumfang / 20) + zuschlag

Rechenkontext mit den Maßen der Seite (HüU = 97 cm):
wert = (97 cm / 20) + 3 cm = 4,85 cm + 3 cm = 7,85 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `wert` | nicht benannte Strecke der Zeichnung `□2` | cm |

- **Abhängigkeiten:** HüU aus der Maßtabelle `□1`.
- **Gültigkeitsbereich:** Zeichnung `□2` der Boxershorts-Grundkonstruktion; genauer nicht eingrenzbar.
- **Technische Randbedingung:** Die Rechenoperation ist eindeutig, ihr geometrischer Referent nicht.
- **Offene Fragen oder Widersprüche:** Auf S. 497 fehlt die Angabe, welche Strecke der Ausdruck bemaßt. Die Schritte 1 bis 12 nennen ihn nicht; die Beschriftungsliste führt `Taillenlinie/-Naht`, `Hüftlinie`, `Schrittlinie` und `Saumlinie/-Kante` getrennt und ohne zugeordneten Rechenweg. Auf S. 495 ist die wortgleiche Beziehung als Höhenabstand der Hüftlinie belegt (`HOF-B1-S495-F01`); dieser Referent stammt jedoch von einer anderen Seite und wurde nicht auf S. 497 übertragen. Dieselbe Behandlung hat bereits der unbezeichnete Ausdruck `HüU : 20 + 3 cm` auf S. 125 in Tranche `H02`.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Die Rechnung ist implementierbar, die Zuordnung zu einer Konstruktionsgröße nicht. Erst nach Klärung am Buch oder durch Fachentscheidung an eine benannte Größe binden.

## HOF-B1-S497-F04 — Halbierungsmarken der Hilfslinien

- **Fachlicher Zweck:** Die Ausgangspunkte der in Schritt 5 gezeichneten Hilfslinien zu P3 und P4 als Halbierungen bestimmen.
- **Quelle:** `formeln_s497.md`, Zeile 22; Originaltranskript `s497.md`, Zeile 58; Buchseite 497. Zugehöriger Schritttext: `s497.md`, Zeile 31 (Schritt 5), selbst nicht extrahiert.
- **Originalbezeichnung:** `½` (zwei Halbierungsmarken).
- **Normalisierte Bezeichnung:** `halbierungsmarken_boxershorts`

### Buchfassung

```text
- `1 cm` (Ausstellung an der Hüfte) · `½` (zwei Halbierungsmarken)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `bezugsstrecke` | nicht benannt | — | cm |
| `teilungsfaktor` | `½` | 1/2 | dimensionslos |

### Formel und Rechenschritte

```text
halbierungspunkt = bezugsstrecke / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `halbierungspunkt` | Ausgangspunkt einer Hilfslinie zu P3 beziehungsweise P4 | cm |

- **Abhängigkeiten:** Ungeklärt; abhängig von der nicht benannten Bezugsstrecke.
- **Gültigkeitsbereich:** Grundkonstruktion der Boxershorts, Zeichnung `□2` und Schritt 5.
- **Technische Randbedingung:** Der Teilungsfaktor ist eindeutig, die Bezugsstrecke nicht. Die Zeichnung trägt zwei Marken, der Schritttext spricht im Plural von „Halbierungen".
- **Offene Fragen oder Widersprüche:** Schritt 5 lautet nur „Hilfslinien von Halbierungen zu P3 und P4 zeichnen" und nennt keine halbierte Strecke; die Zeichnung setzt die Marken ohne Bezugsbeschriftung. Naheliegend sind die beiden in Schritt 2–3 und Schritt 4 abgetragenen Teilstrecken, doch belegt das weder der Schritttext noch die Beschriftungsliste. Anders als bei `HOF-B1-S494-F05`, wo der Schritttext das Halbieren unmittelbar an genannte Abtragungen anschließt, fehlt hier jeder Bezugssatz; der Status ist deshalb `offen` und nicht `hypothetisch`.
- **Abgrenzung:** Der auf derselben Extraktzeile stehende Wert `1 cm` (Ausstellung an der Hüfte, Schritt 6) ist ein fester Einzelwert ohne Rechenoperation und wurde nach derselben Regel wie die Ausstellungswerte auf S. 495 nicht als Formel geführt.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, solange die Bezugsstrecke unbelegt ist. Die Halbierung erst nach Klärung am Buch an eine benannte Strecke binden.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 27–28 | 2 | `Boxershorts 2×-p OSt G38` und `Boxershorts Bund 2×-p OSt G38` — Schnittteil-Stempel der Produktionsschnittzeichnung `□3` |
| 33–34 | 2 | `Boxershorts rechtes VT 1× OSt G38` und `Boxershorts linkes VT 1× OSt G38` — Schnittteil-Stempel der Herrenvariante `□4` |
| 39 und 44 | 2 | Redaktionelle Anmerkung des geprüften Transkripts zum Satzfehler `+ cm1`; Notationshinweis, keine Buchformel |
| **Summe** | **6** | **4 Schnittteil-Stempel + 2 redaktionelle Anmerkungszeilen** |

Zu den Schnittteil-Stempeln: `2×-p` und `1×` sind Stückzahl- und Zuschnittangaben, `OSt` das Oberstoff-Kürzel und `G38` die Größe. Sie werden wie in `V3-J01` bis `V3-S01` nicht als Rechenfaktoren geführt.

Zur redaktionellen Anmerkung: Die beiden Zeilen sind keine eigene Buchformel, belegen aber die richtige Schreibweise von Schritt 4 und sind deshalb in `HOF-B1-S497-F02` als Quellennachweis vermerkt. Dieselbe Behandlung hat bereits die Anmerkung zum fehlenden Gradzeichen auf S. 494.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s497.md` enthält weitere rechenfähige oder bemaßte Angaben, die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen und deshalb nicht als Buchfassungen ergänzt wurden:

- die Maßtabelle `□1` mit TaU 72 cm, HüU 97 cm und SiH 26 cm (Zeilen 15–17) — Eingaben von `HOF-B1-S497-F01` bis `F03`;
- Schritt 1 mit der Reduzierung der SiH um eine Taillenvertiefung (Zeile 25) und die zugehörige Beschriftung `SiH – 0 bis – 4 cm` (Zeile 52);
- die Modelllänge `Länge (12 bis 25 cm)` (Zeile 51);
- Schritt 8 und die Beschriftung `3 bis 4 cm` zur Verlängerung der kurzen Hilfslinie (Zeilen 37 und 59);
- Schritt 11 (`ca. 0,2 cm` hoch an P3), Schritt 12 (`ca. 3 cm` auf der Taillen-Linie) und die Beschriftung `ca. 3 cm` (Zeilen 43, 45 und 54);
- die Saumbeschriftungen `ca. 2 cm` / `ca. 2 cm` (Zeile 60);
- die Maße der Herrenvariante `0,5 cm` / `je ca. 2,5 cm` / `ca. 3 cm` (Zeile 83).

Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
