# Fachlich normalisierte Formeln — S. 500

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s500.md`
Originaltranskript: `s500.md`
Buchseite: Hofenbitzer, Band 1, S. 500

Die Seite trägt drei Teile: die Bestimmung der prozentualen Materialdehnung mit einer durchgerechneten Beispielrechnung, den Schritttext 1 bis 15 des Leggings-Grundschnitts und die Konstruktionstabelle mit den reduzierten Körpermaßen. Die Zeichnung und die Schritte 16 bis 24 stehen auf S. 501.

Die Leggings ist der erste Grundschnitt des Bandes, dessen Umfangsmaße vor der Konstruktion um einen materialabhängigen Prozentsatz **reduziert** werden. Alle Streckenformeln dieser Seite rechnen deshalb mit dem reduzierten `HüU`, nicht mit dem gemessenen.

## HOF-B1-S500-F01 — Absolute Dehnung einer Materialprobe

- **Fachlicher Zweck:** Die in Zentimetern gemessene Dehnung einer Materialprobe als Differenz zwischen gedehnter und ungedehnter Breite bestimmen.
- **Quelle:** `formeln_s500.md`, Zeilen 19–21; Originaltranskript `s500.md`, Zeilen 33–35; Buchseite 500.
- **Originalbezeichnung:** `Dehnung = 23 cm − 20 cm = 3 cm`
- **Normalisierte Bezeichnung:** `dehnung_absolut`

### Buchfassung

```text
- Ausgangsbreite = 20 cm ≙ 100 %
- Dehnungsbreite = 23 cm
- Dehnung = 23 cm − 20 cm = 3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `ausgangsbreite` | Ausgangsbreite | 20 (Beispielwert) | cm |
| `dehnungsbreite` | Dehnungsbreite | 23 (Beispielwert) | cm |

### Formel und Rechenschritte

```text
dehnung_absolut = dehnungsbreite - ausgangsbreite

Buchwerte der Beispielrechnung:
dehnung_absolut = 23 cm - 20 cm = 3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `dehnung_absolut` | Längenzuwachs der Materialprobe in Schussrichtung beim Dehnen | cm |

- **Abhängigkeiten:** Keine Konstruktionsmaße. Beide Eingaben werden nach den Schritten 1 bis 3 der Seite am Material gemessen.
- **Gültigkeitsbereich:** Messung in Schussrichtung. Das Buch bindet die Messung ausdrücklich an eine Dehnkraft, die „ungefähr so groß sein sollte wie die gewünschte Kompression, die das Material beim Tragen auf den Körper ausüben soll".
- **Technische Randbedingung:** Die Dehnkraft ist damit qualitativ und nicht als Zahlenwert festgelegt. `dehnung_absolut` ist deshalb kein reproduzierbarer Materialkennwert, sondern das Ergebnis einer bewusst gewählten Trageeinstellung. `20 cm` und `23 cm` sind Beispielwerte, keine Vorgabewerte.
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit. Die Quelle nennt keine Probengröße und keine Messvorschrift für die Ausgangsbreite.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Zwischenwert von `HOF-B1-S500-F02` führen und die Beispielwerte nicht als Vorgabewerte übernehmen. Die Dehnkraft als dokumentierte, nicht berechenbare Eingangsbedingung mitführen.

## HOF-B1-S500-F02 — Prozentuale Dehnung des Materials

- **Fachlicher Zweck:** Die absolute Dehnung als Prozentsatz der Ausgangsbreite ausdrücken. Dieser Prozentsatz steuert die spätere Reduzierung sämtlicher Umfangsmaße.
- **Quelle:** `formeln_s500.md`, Zeilen 22–23; Originaltranskript `s500.md`, Zeilen 36–37; Buchseite 500.
- **Originalbezeichnung:** `Dehnung in % = (100 % · Dehnung) / Ausgangsbreite`
- **Normalisierte Bezeichnung:** `dehnung_prozent`

### Buchfassung

```text
- Dehnung in % = (100 % · Dehnung) / Ausgangsbreite
- = (100 % · 3 cm) / 20 cm = 15 %
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `dehnung_absolut` | Dehnung | 3 (Beispielwert) | cm |
| `ausgangsbreite` | Ausgangsbreite | 20 (Beispielwert) | cm |
| `prozentbasis` | `100 %` | 100 | Prozent |

### Formel und Rechenschritte

```text
dehnung_prozent = (100 * dehnung_absolut) / ausgangsbreite

Buchwerte der Beispielrechnung:
dehnung_prozent = (100 % * 3 cm) / 20 cm = 15 %
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `dehnung_prozent` | Materialabhängige Dehnung, bezogen auf die ungedehnte Breite | Prozent |

- **Abhängigkeiten:** `dehnung_absolut` aus `HOF-B1-S500-F01`; beide Werte stammen aus derselben Messung.
- **Gültigkeitsbereich:** Das Buch nennt zwei Bereiche, die auseinandergehalten werden müssen: die gemessene Dehnung „zwischen 5 % und 20 % — seltener auch mehr" (Transkriptzeile 13) und die daraus abgeleitete Reduzierung der Umfangsmaße (S. 501: „Reduzierung der notwendigen Umfangsmaße: 5 bis 20 %").
- **Technische Randbedingung:** `100 %` ist eine Bezugsgröße, kein Messwert; die Einheit `cm` kürzt sich heraus, das Ergebnis ist dimensionslos und wird als Prozentwert geführt. Der Bereich `5 % bis 20 %` ist eine Erfahrungsangabe der Quelle, keine Rechengrenze; „seltener auch mehr" schließt größere Werte ausdrücklich nicht aus.
- **Offene Fragen oder Widersprüche:** Die Quelle sagt nicht, ob der gemessene Dehnungsprozentsatz unverändert als Reduzierungsprozentsatz übernommen wird. Im durchgerechneten Beispiel stimmen beide überein (`15 %` gemessen, `15 %` reduziert auf S. 501), aber eine Regel wird nicht formuliert. Sie wird hier nicht ergänzt; siehe `HOF-B1-S501-F02`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Prozentwert, nicht als Faktor speichern, und die Umrechnung in den Faktor `(1 - p/100)` erst in der Reduzierungsformel vornehmen. Der Zusammenhang zwischen gemessener Dehnung und gewähltem Reduzierungsprozentsatz muss als eigene, belegpflichtige Entscheidung modelliert werden.

## HOF-B1-S500-F03 — Halbe Hosenbreite an der Schrittlinie

- **Fachlicher Zweck:** Den beidseitig von der Seitenlinie abzutragenden Abstand an der Schrittlinie aus dem reduzierten Hüftumfang bestimmen.
- **Quelle:** `formeln_s500.md`, Zeile 28; Originaltranskript `s500.md`, Zeile 50; Buchseite 500.
- **Originalbezeichnung:** `HüU : 4` (Schritt 6)
- **Normalisierte Bezeichnung:** `hosenbreite_schrittlinie_leggings`

### Buchfassung

```text
6. Auf dieser nach rechts und links HüU : 4 abtragen und jeweils
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang_reduziert` | HüU (reduziert) | 82,5 | cm |
| `viertelungsfaktor` | `: 4` | 4 | dimensionslos |

### Formel und Rechenschritte

```text
hosenbreite_je_seite = hueftumfang_reduziert / 4

Buchwert der Konstruktionstabelle (HüU 97 → 82,5 cm):
hosenbreite_je_seite = 82,5 cm / 4 = 20,6 cm (gedruckt gerundet; exakt 20,625 cm)
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hosenbreite_je_seite` | Abstand von der Seitenlinie nach rechts und nach links an der Schrittlinie | cm |

- **Abhängigkeiten:** Reduzierter `HüU` aus `HOF-B1-S501-F02`; die Schrittlinie aus Schritt 5 (reduzierte `SiH`, `HOF-B1-S501-F03`).
- **Gültigkeitsbereich:** Grundgerüst der Leggings. Der Wert gilt symmetrisch für Vorder- und Rückteil; die Konstruktion hat keine Seitennaht.
- **Technische Randbedingung:** Derselbe berechnete Betrag wird mit entgegengesetzten Richtungen abgetragen; das ist mit „nach rechts und links" belegt. Die Konstruktionstabelle druckt in der `¼`-Spalte `→ 20,6`; die Rundung von `20,625` auf `20,6` steht so im Buch, eine Rundungsregel wird nicht genannt.
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit.
- **Abgrenzung:** Die Jogginghose rechnet an derselben Stelle `HüU : 4 + 0 bis 2 cm` (S. 498, Schritt 6, `HOF-B1-S498-F02`), die Standardhose führt statt dessen getrennte `vHoB` und `hHoB`. Die Leggings hat keine Zugabe, weil die Weite bereits über die Dehnungsreduzierung des `HüU` eingestellt ist. Die Beziehungen bleiben getrennt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zwingend den reduzierten `HüU` einsetzen. Der gemessene `HüU` von 97 cm ergäbe 24,25 cm und damit eine um 3,6 cm zu weite Hose.

## HOF-B1-S500-F04 — Verlängerung der hinteren Hüftlinie

- **Fachlicher Zweck:** Die Hüftlinie nach hinten über die Hosenbreite hinaus verlängern, um den hinteren Hosenausschnitt anzulegen.
- **Quelle:** `formeln_s500.md`, Zeile 33; Originaltranskript `s500.md`, Zeile 52; Buchseite 500.
- **Originalbezeichnung:** `HüU : 10` (Schritt 8)
- **Normalisierte Bezeichnung:** `hinterer_hosenausschnitt_leggings`

### Buchfassung

```text
8. Die HüL links (hinten) um HüU : 10
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang_reduziert` | HüU (reduziert) | 82,5 | cm |
| `teilungsfaktor` | `: 10` | 10 | dimensionslos |

### Formel und Rechenschritte

```text
hinterer_hosenausschnitt = hueftumfang_reduziert / 10

Buchwert (HüU 97 → 82,5 cm):
hinterer_hosenausschnitt = 82,5 cm / 10 = 8,25 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hinterer_hosenausschnitt` | Verlängerung der Hüftlinie nach links (hinten) über die Hosenbreite hinaus | cm |

- **Abhängigkeiten:** Reduzierter `HüU`; die Hüftlinie („HüL" im Schritttext) und der linke Endpunkt der Schrittlinienbreite aus `HOF-B1-S500-F03`.
- **Gültigkeitsbereich:** Rückteil der Leggings. „Links" ist die Lageangabe der Zeichnung, „hinten" die fachliche Zuordnung; das Buch nennt beides in derselben Zeile.
- **Technische Randbedingung:** Die Verlängerung beginnt am äußeren Endpunkt der Schrittlinienstrecke, nicht an der Seitenlinie. Der Schritttext sagt das nicht ausdrücklich; die Reihenfolge der Schritte 6, 7 und 8 sowie die Zeichnung auf S. 501 legen es fest.
- **Offene Fragen oder Widersprüche:** Der Schritttext schreibt „HüL", die Zeichnung auf S. 501 und die Jogginghose auf S. 498 schreiben „HüLi". Beide Schreibweisen stehen so im Buch; sie bezeichnen dieselbe Linie.
- **Abgrenzung:** Die Jogginghose rechnet `HüU : 10 + 0 bis 1 cm` (S. 498, Schritt 8, `HOF-B1-S498-F03`). Der Leggings fehlt die Bereichszugabe. Der Unterschied ist gedruckt belegt und wurde nicht angeglichen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Richtung und Anschlusspunkt getrennt vom Betrag führen. Zusammen mit `HOF-B1-S500-F05` bildet dieser Wert das Paar aus hinterem und vorderem Hosenausschnitt.

## HOF-B1-S500-F05 — Verlängerung der vorderen Hüftlinie

- **Fachlicher Zweck:** Die Hüftlinie nach vorn über die Hosenbreite hinaus verlängern, um den vorderen Hosenausschnitt anzulegen.
- **Quelle:** `formeln_s500.md`, Zeile 34; Originaltranskript `s500.md`, Zeile 53; Buchseite 500.
- **Originalbezeichnung:** `HüU : 20 + 1 bis 2 cm` (Schritt 9)
- **Normalisierte Bezeichnung:** `vorderer_hosenausschnitt_leggings`

### Buchfassung

```text
9. und rechts (vorne) um HüU : 20 + 1 bis 2 cm verlängern.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang_reduziert` | HüU (reduziert) | 82,5 | cm |
| `teilungsfaktor` | `: 20` | 20 | dimensionslos |
| `ausschnittzugabe` | `+ 1 bis 2 cm` | 1 bis 2 | cm |

### Formel und Rechenschritte

```text
vorderer_hosenausschnitt = (hueftumfang_reduziert / 20) + ausschnittzugabe
mit ausschnittzugabe aus dem Bereich 1 cm bis 2 cm

Buchwert (HüU 97 → 82,5 cm):
untere Grenze = (82,5 cm / 20) + 1 cm = 4,125 cm + 1 cm = 5,125 cm
obere Grenze  = (82,5 cm / 20) + 2 cm = 4,125 cm + 2 cm = 6,125 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `vorderer_hosenausschnitt` | Verlängerung der Hüftlinie nach rechts (vorn) über die Hosenbreite hinaus | cm |

- **Abhängigkeiten:** Reduzierter `HüU`; der rechte Endpunkt der Schrittlinienbreite aus `HOF-B1-S500-F03`.
- **Gültigkeitsbereich:** Vorderteil der Leggings.
- **Technische Randbedingung:** Der Bereich `1 bis 2 cm` bleibt als Bereich erhalten. S. 499 und S. 501 nennen für Herren zusätzlich `+ ca. 0,7 cm`, jedoch beide Male an einer anderen Zeichnungsstelle und außerhalb des verbindlichen Extrakts; eine Verbindung zu diesem Bereich wird nicht hergestellt.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine Auswahlregel innerhalb des Bereichs `1 bis 2 cm` — weder nach Figur noch nach Geschlecht noch nach Material. Es wird keine erfunden.
- **Abgrenzung:** Die Jogginghose rechnet auf S. 498 in Schritt 9 wortgleich `HüU : 20 + 1 bis 2 cm` (`HOF-B1-S498-F04`). Die beiden Beziehungen bleiben dennoch getrennt, weil Jogginghose und Leggings verschiedene Grundschnitte mit verschiedenen Eingangsgrößen sind: die Jogginghose setzt den gemessenen `HüU` ein, die Leggings den reduzierten. Bei gleicher Formel ergeben sich dadurch verschiedene Werte.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Bereich als Intervall mit Vorgabewert `None` führen und die Auswahl erzwingen, statt eine Mitte zu unterstellen.

## HOF-B1-S500-F06 — Vorderhosenbreite der Konstruktionstabelle

- **Fachlicher Zweck:** Die Vorderhosenbreite aus dem Viertel-Hüftumfang mit festem Abzug bestimmen.
- **Quelle:** `formeln_s500.md`, Zeile 44; Originaltranskript `s500.md`, Zeile 87; Buchseite 500.
- **Originalbezeichnung:** `¼ HüU − 1 cm ±`
- **Normalisierte Bezeichnung:** `vorderhosenbreite_leggings_tabelle`

### Buchfassung

```text
| vHoB | Vorderhosenbreite | ¼ HüU − 1 cm ± | --- |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang_reduziert` | HüU (reduziert) | 82,5 | cm |
| `viertelungsfaktor` | `¼` | 4 | dimensionslos |
| `vhob_abzug` | `− 1 cm` | 1 | cm |
| `signierte_anpassung` | `±` | nicht eingetragen | cm |

### Formel und Rechenschritte

```text
vorderhosenbreite = (hueftumfang_reduziert / 4) - 1 cm + signierte_anpassung

Die Spalte "Wert" ist im Buch mit "---" ausgefüllt; die Zeile ist
in dieser Konstruktion nicht ausgerechnet. Rechnerisch ergäbe sich
mit dem reduzierten HüU = 82,5 cm und ohne Anpassung:
vorderhosenbreite = (82,5 cm / 4) - 1 cm = 20,625 cm - 1 cm = 19,625 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `vorderhosenbreite` | Breite des Vorderteils an der Schrittlinie | cm |

- **Abhängigkeiten:** Reduzierter `HüU`.
- **Gültigkeitsbereich:** Konstruktionstabelle der Leggings.
- **Technische Randbedingung:** Der eingeklammerte Rechenweg ist **nicht** die Konstruktion dieser Seite. Der Schritttext teilt die Weite in Schritt 6 gleichmäßig als `HüU : 4` nach beiden Seiten auf und kennt keine getrennten Vorder- und Hinterhosenbreiten. Der ausgerechnete Wert steht hier nur zur Kontrolle und ist nicht als Konstruktionswert zu verwenden.
- **Offene Fragen oder Widersprüche:** Die Spalte „Wert" trägt `---`. Das Buch füllt die Zeile also bewusst nicht aus; ebenso bleibt das Feld hinter `±` leer. Ob die Zeile bei der Leggings gar nicht gilt oder nur im gedruckten Beispiel nicht ausgefüllt wurde, sagt die Quelle nicht. Die Zeile ist als vorgedruckte Tabellenzeile des Formulars zu lesen, nicht als Rechenanweisung dieser Konstruktion.
- **Abgrenzung:** Wortgleich mit der Tabellenzeile der Jogginghose (`s498.md`, Zeile 94) und der Standardhose. Eigene ID, weil eigene Seite und eigene Eingangsgröße (reduzierter statt gemessener `HüU`).
- **Status:** `hypothetisch`
- **Hinweis für die spätere Python-Umsetzung:** Nicht in den Konstruktionsweg der Leggings aufnehmen. Als optionale, ausdrücklich abgeschaltete Tabellenzeile führen, solange kein Beleg für ihre Anwendung bei diesem Grundschnitt vorliegt.

## HOF-B1-S500-F07 — Hinterhosenbreite der Konstruktionstabelle

- **Fachlicher Zweck:** Die Hinterhosenbreite aus dem Viertel-Hüftumfang mit festem Zuschlag bestimmen.
- **Quelle:** `formeln_s500.md`, Zeile 45; Originaltranskript `s500.md`, Zeile 88; Buchseite 500.
- **Originalbezeichnung:** `¼ HüU + 1 cm ±`
- **Normalisierte Bezeichnung:** `hinterhosenbreite_leggings_tabelle`

### Buchfassung

```text
| hHoB | Hinterhosenbreite | ¼ HüU + 1 cm ± | --- |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang_reduziert` | HüU (reduziert) | 82,5 | cm |
| `viertelungsfaktor` | `¼` | 4 | dimensionslos |
| `hhob_zuschlag` | `+ 1 cm` | 1 | cm |
| `signierte_anpassung` | `±` | nicht eingetragen | cm |

### Formel und Rechenschritte

```text
hinterhosenbreite = (hueftumfang_reduziert / 4) + 1 cm + signierte_anpassung

Die Spalte "Wert" ist im Buch mit "---" ausgefüllt; die Zeile ist
in dieser Konstruktion nicht ausgerechnet. Rechnerisch ergäbe sich
mit dem reduzierten HüU = 82,5 cm und ohne Anpassung:
hinterhosenbreite = (82,5 cm / 4) + 1 cm = 20,625 cm + 1 cm = 21,625 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hinterhosenbreite` | Breite des Rückteils an der Schrittlinie | cm |

- **Abhängigkeiten:** Reduzierter `HüU`.
- **Gültigkeitsbereich:** Konstruktionstabelle der Leggings.
- **Technische Randbedingung:** Wie bei `HOF-B1-S500-F06` ist der ausgerechnete Wert nur Kontrolle. Die Summe `vHoB + hHoB = ½ HüU` bleibt erhalten, weil sich Abzug und Zuschlag von je `1 cm` aufheben; die Leggings-Konstruktion nutzt diese Aufteilung jedoch nicht.
- **Offene Fragen oder Widersprüche:** Wie bei `HOF-B1-S500-F06`: Wertspalte `---`, Anpassungsfeld leer, keine Aussage der Quelle zur Anwendung bei diesem Grundschnitt.
- **Abgrenzung:** Wortgleich mit der Tabellenzeile der Jogginghose (`HOF-B1-S498-F07`) und mit `¼ HüU + 1 cm` in `HOF-B1-S494-F02` der einfachen Sporthose. Eigene ID nach derselben Regel wie dort.
- **Status:** `hypothetisch`
- **Hinweis für die spätere Python-Umsetzung:** Wie `HOF-B1-S500-F06` nicht in den Konstruktionsweg aufnehmen. Wird die Zeile später doch aktiviert, ist zu prüfen, ob sie mit dem reduzierten oder mit dem gemessenen `HüU` rechnet — die Quelle sagt es nicht.

## HOF-B1-S500-F08 — Kniehöhe aus der Schritthöhe

- **Fachlicher Zweck:** Den Höhenabstand der Knielinie unterhalb der Schrittlinie aus der Schritthöhe bestimmen.
- **Quelle:** `formeln_s500.md`, Zeile 50; Originaltranskript `s500.md`, Zeile 90; Buchseite 500.
- **Originalbezeichnung:** `SrH : 10 · 4`
- **Normalisierte Bezeichnung:** `kniehoehe_leggings`

### Buchfassung

```text
| KnH | Kniehöhe | SrH : 10 · 4 | 32 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `schritthoehe` | SrH | 80 | cm |
| `teilungsfaktor` | `: 10` | 10 | dimensionslos |
| `vervielfachungsfaktor` | `· 4` | 4 | dimensionslos |

### Formel und Rechenschritte

```text
kniehoehe = (schritthoehe / 10) * 4

Buchwert der Konstruktionstabelle (SrH = 80 cm):
kniehoehe = (80 cm / 10) * 4 = 8 cm * 4 = 32 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kniehoehe` | Höhenabstand zwischen Schrittlinie und Knielinie | cm |

- **Abhängigkeiten:** `SrH` aus der Tabellenzeile `sTaH − SiH` (Wert 80). Diese Zeile liegt nicht im Extrakt.
- **Gültigkeitsbereich:** Konstruktionstabelle der Leggings; Schritt 10 trägt die `KnH` von der Schrittlinie nach unten ab.
- **Technische Randbedingung:** Der gedruckte Wert `32` ist mit `SrH = 80 cm` exakt und ohne Rundung getroffen. Die Reihenfolge `: 10` vor `· 4` ist für das Ergebnis gleichgültig; sie bleibt als Buchreihenfolge erhalten.
- **Offene Fragen oder Widersprüche:** **`SrH` ist mit dem unreduzierten `SiH` gerechnet.** Die Tabelle führt `SiH` als `→ 24,7` (reduziert), die `SrH`-Zeile gibt aber `80` an, was `106 − 26` mit der gemessenen `SiH` entspricht; mit der reduzierten `SiH` ergäbe sich `106 − 24,7 = 81,3` und daraus `KnH = 32,52`. Der Widerspruch steht in der Quelle. Er wird nicht aufgelöst, weil das Buch nirgends sagt, ob die Längenreduzierung auch in die `SrH` eingeht. Die `SrH`-Zeile liegt nicht im Extrakt; ihre Bewertung erfolgt hier nur als Prüfhinweis.
- **Abgrenzung:** Wortgleich mit `HOF-B1-S494-F01` (einfache Sporthose), der Tabellenzeile der Jogginghose (`HOF-B1-S498-F06`) und `HOF-B1-S109-F03` (Standardhose). Eigene ID nach der in `V3-S01` angewandten Regel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `SrH` als ausdrücklich benannten Eingang führen und im Aufruf festhalten, ob die reduzierte oder die gemessene `SiH` eingegangen ist. Das Buchbeispiel verwendet die gemessene.

## Ausgeschlossene Kandidaten

| Extraktzeile | Transkriptzeile | Anzahl | Ausschlussgrund |
|---|---:|---:|---|
| 9 | 27 | 1 | `Ausgangsbreite in cm ≙ 100 %` — Bezugsdefinition der Prozentrechnung, keine Rechenoperation mit benannter Ausgabe. Der Bezug ist in `HOF-B1-S500-F02` als `prozentbasis` erhalten. |
| 14 | 29 | 1 | `Dehnung in cm ≙ x %` — Platzhalterzeile des Messschemas; `x` ist die gesuchte, nicht eine gegebene Größe. Die Rechnung dazu steht in `HOF-B1-S500-F02`. |
| 39 | 72 | 1 | `| TaA | Taillenabstände | v 0 · r 0 · l 0 · h 0 |` — vier eingetragene Nullwerte des Formulars; Eingabewerte ohne Rechenoperation |
| **Summe** | — | **3** | **2 Definitions-/Schemazeilen + 1 Zeile eingetragener Nullwerte** |

## Abrechnung der Kandidatenzeilen

| | Anzahl |
|---|---:|
| Extrahierte Kandidatenzeilen | 14 |
| In Formelblöcken abgebildet | 11 |
| Ausgeschlossen | 3 |
| Erzeugte Formel-IDs | 8 |

Die elf abgebildeten Zeilen erzeugen acht IDs: Die fünf Zeilen der Beispielrechnung (Extraktzeilen 19–23) tragen gemeinsam `HOF-B1-S500-F01` und `F02`, weil sie einen zusammenhängenden Rechenweg mit Eingaben, Zwischenwert und Ergebnis bilden. Die übrigen sechs Zeilen tragen je eine ID.

## Prüfhinweise

1. **Reduzierte gegenüber gemessenen Maßen:** Die Konstruktionstabelle schreibt die Reduzierung mit einem Pfeil (`97 → 82,5`). Alle Streckenformeln dieser Seite (`F03`, `F04`, `F05`) setzen den Wert **hinter** dem Pfeil ein. Wird versehentlich der gemessene Wert eingesetzt, ist die Hose um rund 15 % zu weit. Die Reduzierung selbst ist auf S. 501 gerechnet (`HOF-B1-S501-F02`).
2. **`SrH` und `SiH` — offene Widersprüchlichkeit:** Siehe `HOF-B1-S500-F08`. Die Tabelle reduziert die `SiH` auf `24,7`, rechnet die `SrH` aber mit `26`. Beide Zahlen stehen gedruckt nebeneinander in derselben Tabelle.
3. **`OsU` und `KnU` in der Konstruktionstabelle:** Die Tabelle trägt für beide Maße den Wert `72` ein — denselben Wert wie der Taillenumfang. Die Kontrollen auf S. 501 rechnen dagegen mit `OsU = 55,5 cm` und `KnU = 34 cm`, und `55,5` ist auch der `OsU`-Wert der Jogginghosen-Tabelle auf S. 498. Die beiden `72`-Einträge sind damit sehr wahrscheinlich ein Übertragungsfehler der Tabellenspalte. Beide Zeilen liegen nicht im Extrakt; der Widerspruch ist hier nur vermerkt und wurde nicht korrigiert. Er ist in `HOF-B1-S501-F07` und `F08` erneut festgehalten.
4. **`RiU`-Zeile:** Die Tabelle trägt beim Ristumfang `→ 19,6` ein. `19,6` ist der auf S. 501 ausgerechnete reduzierte **Fesselumfang**, während die `FeU`-Zeile derselben Tabelle den unreduzierten Wert `23` trägt. Auch hier liegen beide Zeilen außerhalb des Extrakts; der Verdacht einer verrutschten Zeile ist vermerkt, nicht bereinigt.
5. **`SaW`-Zeile:** Die Saumweite der Leggings wird nicht aus der Bereichstabelle gewählt, sondern mit `FeU → 19,6` besetzt, also durch den reduzierten Fesselumfang. Das deckt sich mit Schritt 3 („Für die Saumweite den FeU : 2 nach rechts und links abtragen"). Die Zeile liegt nicht im Extrakt.
6. **Schritt `3a` außer der Reihe:** Der Schritt `3a` („An P3 jeweils ca. 3 cm nach oben abwinkeln") steht im Buch zwischen den Schritten 12 und 13, nicht nach Schritt 3 — dieselbe Eigenheit wie bei der Jogginghose auf S. 498. Sie ist eine Reihenfolgeangabe, keine Rechenbeziehung.
7. **Extraktionsgrenze:** Das Originaltranskript `s500.md` enthält weitere rechenfähige Angaben, die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen und deshalb nicht als Buchfassungen ergänzt wurden:
   - Schritt 2 (Zeile 46): `6 bis 8 cm` Kürzung unten an der Seitenlinie;
   - Schritt 3 (Zeile 47): `FeU : 2` — die Saumweite; als Zeichnungsbeschriftung auf S. 501 aber im Extrakt und dort als `HOF-B1-S501-F05` normalisiert;
   - Schritt 4 (Zeile 48): `1 bis 1,5 cm` Kürzung oben;
   - Schritt 12 (Zeile 56): `WaU : 2` — ebenfalls auf S. 501 im Extrakt und dort als `HOF-B1-S501-F06` normalisiert;
   - Schritt 3a (Zeile 57): `ca. 3 cm`; Schritt 14 (Zeile 59): `2 bis 3 cm` Einstellung an der Knielinie;
   - die Tabellenzeilen `TaU`, `HüU`, `sTaH`, `SiH`, `OsU`, `KnU`, `WaU`, `FeU`, `RiU`, `SrH` und `SaW` (Zeilen 69–91) mit ihren Halb- und Viertelwerten;
   - Zeile 93: der Verweis auf die Gesäßwinkeltabelle von S. 498.

   Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
