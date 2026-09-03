# Fachlich normalisierte Formeln — S. 501

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s501.md`
Originaltranskript: `s501.md`
Buchseite: Hofenbitzer, Band 1, S. 501

Die Seite ist die zweite Seite des Leggings-Grundschnitts. Sie trägt den Bund für den Gummitunnel, die beiden Weitenkontrollen und die Schritte 16 bis 24, vor allem aber die **durchgerechnete Reduzierung der Körpermaße** — den Teil, den der Schritttext auf S. 500 nur ankündigt. Dazu kommt die Grundschnittzeichnung mit ihren Beschriftungen.

Alle zehn extrahierten Kandidatenzeilen sind Rechenbeziehungen; keine ist ausgeschlossen. Neun Formel-IDs entstehen, drei Beschriftungen sind Belege zu bereits auf S. 500 normalisierten Formeln.

## HOF-B1-S501-F01 — Reduzierung des Taillenumfangs

- **Fachlicher Zweck:** Den Taillenumfang für den Bund mit Gummitunnel um einen eigenen, kleineren Prozentsatz als die übrigen Umfangsmaße reduzieren.
- **Quelle:** `formeln_s501.md`, Zeilen 9 und 14; Originaltranskript `s501.md`, Zeilen 13 und 29; Buchseite 501.
- **Originalbezeichnung:** `TaU − 0 bis −5 %`
- **Normalisierte Bezeichnung:** `taillenumfang_reduziert_leggings`

### Buchfassung

```text
- TaU − 0 bis −5 %

- TaU − 0 bis −5 % = 72 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenumfang_gemessen` | TaU | 72 (Konstruktionstabelle S. 500) | cm |
| `taillenreduzierung_prozent` | `0 bis 5 %` | 0 bis 5 | Prozent |

### Formel und Rechenschritte

```text
taillenumfang_reduziert = taillenumfang_gemessen * (1 - taillenreduzierung_prozent / 100)
mit taillenreduzierung_prozent aus dem Bereich 0 % bis 5 %

Buchwert (TaU = 72 cm), gedrucktes Ergebnis:
taillenumfang_reduziert = 72 cm

Das gedruckte Ergebnis entspricht dem Prozentsatz 0 %:
72 cm * (1 - 0/100) = 72 cm
Die obere Bereichsgrenze ergäbe:
72 cm * (1 - 5/100) = 72 cm * 0,95 = 68,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `taillenumfang_reduziert` | Weite des Bundes mit Gummitunnel an der Taillenlinie | cm |

- **Abhängigkeiten:** Gemessener `TaU` aus der Konstruktionstabelle auf S. 500.
- **Gültigkeitsbereich:** Bund für Gummitunnel, Zeichnung `□2`. Das Buch stellt diese Zeile ausdrücklich unter die Überschrift „Reduzierung der notwendigen Umfangsmaße: 5 bis 20 %", gibt ihr aber den abweichenden Bereich `0 bis 5 %`.
- **Technische Randbedingung:** Der `TaU` wird **nicht** mit dem allgemeinen Dehnungsprozentsatz reduziert. Die Quelle nennt keinen Grund; fachlich naheliegend ist der Gummizug, der die Weite selbst einstellt. Diese Erklärung ist nicht belegt und daher nicht Teil der Normalisierung.
- **Offene Fragen oder Widersprüche:** Die Zeile steht unter einer Überschrift, deren Bereich (`5 bis 20 %`) sie nicht einhält. Der Widerspruch ist gedruckt und bleibt erhalten. Ferner nennt die Quelle keine Auswahlregel innerhalb von `0 bis 5 %`; im Beispiel ist erkennbar `0 %` gewählt, ohne dass das gesagt wird.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als eigenen Prozentsatz führen, getrennt vom Umfangs- und vom Längenprozentsatz. Der Vorgabewert darf nicht der allgemeine Dehnungswert sein; das Buchbeispiel arbeitet hier mit `0 %`.

## HOF-B1-S501-F02 — Reduzierung der Umfangsmaße um den Dehnungsprozentsatz

- **Fachlicher Zweck:** Die für die Konstruktion benötigten Umfangsmaße um die materialabhängige Dehnung verkleinern, damit die Leggings im getragenen, gedehnten Zustand am Körper anliegt.
- **Quelle:** `formeln_s501.md`, Zeilen 15–17; Originaltranskript `s501.md`, Zeilen 30–32; Buchseite 501.
- **Originalbezeichnung:** `HüU − 15 %: 97 cm · 0,85 = 82,5 cm` und die gleichgebauten Zeilen für `WaU` und `FeU`.
- **Normalisierte Bezeichnung:** `umfangsmass_reduziert_leggings`

### Buchfassung

```text
- HüU − 15 %: 97 cm · 0,85 = 82,5 cm
- WaU − 15 %: 35 cm · 0,85 = 29,8 cm
- FeU − 15 %: 23 cm · 0,85 = 19,6 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `umfangsmass_gemessen` | HüU / WaU / FeU | 97 / 35 / 23 | cm |
| `umfangsreduzierung_prozent` | `− 15 %` (Bereich `5 bis 20 %`) | 15 | Prozent |
| `reduzierungsfaktor` | `· 0,85` | 0,85 | dimensionslos |

### Formel und Rechenschritte

```text
reduzierungsfaktor      = 1 - (umfangsreduzierung_prozent / 100)
umfangsmass_reduziert   = umfangsmass_gemessen * reduzierungsfaktor

Buchwerte bei 15 % Reduzierung (Faktor 0,85):
HüU: 97 cm * 0,85 = 82,45 cm → gedruckt 82,5 cm
WaU: 35 cm * 0,85 = 29,75 cm → gedruckt 29,8 cm
FeU: 23 cm * 0,85 = 19,55 cm → gedruckt 19,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `umfangsmass_reduziert` | Für die Konstruktion einzusetzender, um die Dehnung verkleinerter Umfang | cm |

- **Abhängigkeiten:** `dehnung_prozent` aus `HOF-B1-S500-F02`; die gemessenen Umfangsmaße aus der Konstruktionstabelle auf S. 500. Von dieser Formel hängen `HOF-B1-S500-F03`, `F04`, `F05` sowie `HOF-B1-S501-F04`, `F05` und `F06` ab.
- **Gültigkeitsbereich:** Bereich `5 bis 20 %` nach der Überschrift der Quelle; S. 500 ergänzt „seltener auch mehr". Die drei gedruckten Zeilen verwenden denselben Prozentsatz für alle drei Maße.
- **Technische Randbedingung:** Die Quelle rechnet über den Faktor `0,85` und nicht über eine Subtraktion; beide Wege sind gleichwertig. Alle drei gedruckten Ergebnisse sind auf eine Nachkommastelle **aufgerundet** (`82,45 → 82,5`, `29,75 → 29,8`, `19,55 → 19,6`). Eine Rundungsregel nennt die Quelle nicht; die exakten und die gedruckten Werte bleiben deshalb getrennt geführt.
- **Offene Fragen oder Widersprüche:**
  1. Die Quelle sagt nicht ausdrücklich, dass der gemessene Dehnungsprozentsatz aus `HOF-B1-S500-F02` als Reduzierungsprozentsatz zu verwenden ist. Im Buch stimmen beide Beispiele mit `15 %` überein, eine Regel wird aber nicht formuliert. Sie wird hier nicht ergänzt.
  2. Der `TaU` folgt dieser Formel nicht, sondern hat mit `HOF-B1-S501-F01` einen eigenen, kleineren Bereich.
  3. Für `OsU` und `KnU` ist keine Reduzierung angegeben; die Kontrollen `F07` und `F08` vergleichen gegen die **gemessenen** Werte.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als eine Funktion über einer Liste von Maßen implementieren, nicht als drei Einzelformeln. Gemessenen und reduzierten Wert getrennt speichern, damit die Kontrollen auf S. 501 weiterhin gegen den gemessenen Wert prüfen können. Ungerundet weiterrechnen und erst in der Ausgabe runden.

## HOF-B1-S501-F03 — Reduzierung des Längenmaßes Sitzhöhe

- **Fachlicher Zweck:** Die Sitzhöhe um einen eigenen, kleineren Prozentsatz als die Umfangsmaße verkleinern, weil das Material in Längsrichtung weniger stark beansprucht wird.
- **Quelle:** `formeln_s501.md`, Zeile 22; Originaltranskript `s501.md`, Zeile 36; Buchseite 501.
- **Originalbezeichnung:** `SiH − 5 %: 26 cm · 0,95 = 24,7 cm`
- **Normalisierte Bezeichnung:** `sitzhoehe_reduziert_leggings`

### Buchfassung

```text
- SiH − 5 %: 26 cm · 0,95 = 24,7 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `sitzhoehe_gemessen` | SiH | 26 | cm |
| `laengenreduzierung_prozent` | `− 5 %` (Bereich `0 bis 5 %`) | 5 | Prozent |
| `reduzierungsfaktor` | `· 0,95` | 0,95 | dimensionslos |

### Formel und Rechenschritte

```text
reduzierungsfaktor    = 1 - (laengenreduzierung_prozent / 100)
sitzhoehe_reduziert   = sitzhoehe_gemessen * reduzierungsfaktor

Buchwert:
sitzhoehe_reduziert = 26 cm * 0,95 = 24,7 cm (exakt, ohne Rundung)
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `sitzhoehe_reduziert` | Für Schritt 5 auf S. 500 einzusetzende, verkürzte Sitzhöhe | cm |

- **Abhängigkeiten:** Gemessene `SiH` aus der Konstruktionstabelle auf S. 500. Schritt 5 dort verlangt ausdrücklich „die (reduzierte) SiH".
- **Gültigkeitsbereich:** Bereich `0 bis 5 %` nach der Überschrift „Reduzierung des Längenmaßes: 0 bis 5 %". Die Überschrift steht im Singular und nennt nur die `SiH`; ein zweites Längenmaß ist nicht reduziert.
- **Technische Randbedingung:** Der Reduzierungspfeil `−5 %` der Zeichnung (Transkriptzeile 49) bestätigt, dass dieser Prozentsatz für Längenmaße gilt und der Pfeil `−15 %` für Umfangsmaße. Beide Pfeile stehen nebeneinander in derselben Zeichnung.
- **Offene Fragen oder Widersprüche:** Die `sTaH` (106 cm, Schritt 1 auf S. 500) wird **nicht** reduziert, obwohl sie ein Längenmaß ist. Die Quelle sagt nicht, warum. Zusätzlich rechnet die Tabellenzeile `SrH = sTaH − SiH` auf S. 500 mit `80`, also mit der **unreduzierten** `SiH` von 26 cm; mit der reduzierten `SiH` ergäbe sich `81,3`. Dieser Widerspruch ist unter `HOF-B1-S500-F08` festgehalten. Die Quelle löst ihn nicht auf.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als eigenen, dritten Prozentsatz neben Umfangs- und Taillenprozentsatz führen. Bei der `SrH`-Berechnung ausdrücklich entscheiden und dokumentieren, welche `SiH` eingeht — das Buchbeispiel verwendet dort die gemessene, in Schritt 5 dagegen die reduzierte.

## HOF-B1-S501-F04 — Höhenabstand der Hüftlinie

- **Fachlicher Zweck:** Den Höhenabstand der Hüftlinie aus dem reduzierten Hüftumfang und einem festen Zuschlag bestimmen.
- **Quelle:** `formeln_s501.md`, Zeile 27 (Teilangabe der Zeile); Originaltranskript `s501.md`, Zeile 41; Buchseite 501.
- **Originalbezeichnung:** `HüU : 20 + 3 cm`
- **Normalisierte Bezeichnung:** `hueftlinienabstand_leggings`

### Buchfassung

```text
- HüU : 10; HüU : 20 + 1 bis 2 cm; HüU : 20 + 3 cm; HüU : 4; WaU : 2; FeU : 2
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang_reduziert` | HüU (reduziert) | 82,5 | cm |
| `teilungsfaktor` | `: 20` | 20 | dimensionslos |
| `konstante_hueftlinienzugabe` | `+ 3 cm` | 3 | cm |

### Formel und Rechenschritte

```text
hueftlinienabstand = (hueftumfang_reduziert / 20) + 3 cm

Buchwert (HüU 97 → 82,5 cm):
hueftlinienabstand = (82,5 cm / 20) + 3 cm = 4,125 cm + 3 cm = 7,125 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftlinienabstand` | Höhenabstand zwischen Schrittlinie und Hüftlinie im Grundgerüst | cm |

- **Abhängigkeiten:** Reduzierter `HüU` aus `HOF-B1-S501-F02`.
- **Gültigkeitsbereich:** Grundgerüst der Leggings, Grundschnittzeichnung auf S. 501.
- **Technische Randbedingung:** Die Beschriftung nennt weder Ausgangs- noch Zielpunkt. Die Lesart „von der Schrittlinie nach oben" stützt sich auf die Zeichnung und auf die gleichnamigen Beziehungen auf S. 110 und S. 495, nicht auf einen Schritttext dieser Konstruktion.
- **Offene Fragen oder Widersprüche:** Wie bei der Jogginghose fehlt der Konstruktionsschritt: Die Schritte 1 bis 15 auf S. 500 bauen keine Hüftlinie, obwohl die Schritte 8 und 9 sie mit „Die HüL links (hinten) …" bereits voraussetzen und die Zeichnung sie als `HüLi` beschriftet. Die Fehlstelle wird benannt, nicht geschlossen.
- **Abgrenzung:** Wortgleich mit `HOF-B1-S110-F01`, `HOF-B1-S495-F01` und `HOF-B1-S499-F02`. Eigene ID, weil die Leggings ein eigener Grundschnitt ist und — anders als alle genannten — mit dem **reduzierten** `HüU` rechnet. Bei gleicher Formel ergibt sich hier `7,125 cm` statt `7,85 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Betrag und Richtung trennen. Der Eingang ist zwingend der reduzierte `HüU`; die Verwechslung mit der gleichnamigen Formel der Jogginghose ist die naheliegendste Fehlerquelle dieser Tranche.

## HOF-B1-S501-F05 — Halbe Saumweite an der Saumlinie

- **Fachlicher Zweck:** Den beidseitig von der Seitenlinie abzutragenden Saumabstand aus dem reduzierten Fesselumfang bestimmen.
- **Quelle:** `formeln_s501.md`, Zeile 27 (Teilangabe der Zeile); Originaltranskript `s501.md`, Zeile 41; Buchseite 501. Der zugehörige Schritttext steht als Schritt 3 auf `s500.md`, Zeile 47, liegt dort aber nicht im Extrakt.
- **Originalbezeichnung:** `FeU : 2`
- **Normalisierte Bezeichnung:** `saumabstand_leggings`

### Buchfassung

```text
- HüU : 10; HüU : 20 + 1 bis 2 cm; HüU : 20 + 3 cm; HüU : 4; WaU : 2; FeU : 2
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `fesselumfang_reduziert` | FeU (reduziert) | 19,6 | cm |
| `halbierungsfaktor` | `: 2` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
saumabstand_je_seite = fesselumfang_reduziert / 2

Buchwert (FeU 23 → 19,6 cm):
saumabstand_je_seite = 19,6 cm / 2 = 9,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `saumabstand_je_seite` | Abstand von der Seitenlinie nach rechts und nach links an der Saumlinie | cm |

- **Abhängigkeiten:** Reduzierter `FeU` aus `HOF-B1-S501-F02`.
- **Gültigkeitsbereich:** Grundgerüst der Leggings; die Saumlinie liegt nach Schritt 2 um `6 bis 8 cm` oberhalb des unteren Endes der Seitenlinie.
- **Technische Randbedingung:** Derselbe Betrag wird symmetrisch in beide Richtungen abgetragen; belegt durch Schritt 3 auf S. 500 („nach rechts und links abtragen"). Die Konstruktionstabelle auf S. 500 setzt die Saumweite folgerichtig mit `FeU → 19,6` an, statt sie aus der Bereichstabelle für Hosenformen zu wählen.
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit.
- **Abgrenzung:** Die Jogginghose rechnet `SaW : 2` (S. 498, Schritt 3, `HOF-B1-S498-F01`) aus einer frei gewählten Saumweite. Die Leggings leitet den Wert stattdessen aus einem Körpermaß ab; die Beziehungen bleiben getrennt.
- **Fundstellenhinweis:** Der Schritttext auf S. 500 ist nicht extrahiert. Der Beleg dieser Formel ist deshalb allein die Zeichnungsbeschriftung auf S. 501, und die ID trägt die Seitenzahl 501. Wird der S.-500-Extrakt später um Schritt 3 ergänzt, ist die ID **nicht** zu verdoppeln, sondern die neue Zeile als Schritttextbeleg hierher zu führen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zwingend den reduzierten `FeU` einsetzen. Der gemessene Wert von 23 cm ergäbe eine um 3,4 cm zu weite Saumöffnung.

## HOF-B1-S501-F06 — Halbe Wadenweite an der Wadenlinie

- **Fachlicher Zweck:** Den beidseitig von der Seitenlinie abzutragenden Abstand an der Wadenlinie aus dem reduzierten Wadenumfang bestimmen.
- **Quelle:** `formeln_s501.md`, Zeile 27 (Teilangabe der Zeile); Originaltranskript `s501.md`, Zeile 41; Buchseite 501. Der zugehörige Schritttext steht als Schritt 12 auf `s500.md`, Zeile 56, liegt dort aber nicht im Extrakt.
- **Originalbezeichnung:** `WaU : 2`
- **Normalisierte Bezeichnung:** `wadenabstand_leggings`

### Buchfassung

```text
- HüU : 10; HüU : 20 + 1 bis 2 cm; HüU : 20 + 3 cm; HüU : 4; WaU : 2; FeU : 2
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `wadenumfang_reduziert` | WaU (reduziert) | 29,8 | cm |
| `halbierungsfaktor` | `: 2` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
wadenabstand_je_seite = wadenumfang_reduziert / 2

Buchwert (WaU 35 → 29,8 cm):
wadenabstand_je_seite = 29,8 cm / 2 = 14,9 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `wadenabstand_je_seite` | Abstand von der Seitenlinie nach rechts und nach links an der Wadenlinie | cm |

- **Abhängigkeiten:** Reduzierter `WaU` aus `HOF-B1-S501-F02`; die Wadenlinie aus Schritt 11 auf S. 500 (`WaH` unterhalb der Knielinie, siehe `HOF-B1-S501-F09`).
- **Gültigkeitsbereich:** Grundgerüst der Leggings, Vorder- und Rückteil gleich.
- **Technische Randbedingung:** Symmetrische Abtragung, belegt durch Schritt 12 auf S. 500 („nach links und rechts abtragen").
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit.
- **Abgrenzung:** Die Jogginghose rechnet `WaU : 2 + 0 bis 1 cm` (S. 498, Schritt 12, `HOF-B1-S498-F05`). Der Leggings fehlt die Bereichszugabe, weil die Weite bereits über die Dehnungsreduzierung eingestellt ist. Der Unterschied ist gedruckt belegt.
- **Fundstellenhinweis:** Wie bei `HOF-B1-S501-F05` ist der Schritttext auf S. 500 nicht extrahiert; die ID trägt deshalb die Seitenzahl 501 und ist bei einer späteren Nachextraktion von S. 500 nicht zu verdoppeln.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zwingend den reduzierten `WaU` einsetzen.

## HOF-B1-S501-F07 — Kontrolle der Oberschenkelweite

- **Fachlicher Zweck:** Nach der Konstruktion prüfen, dass die fertige Oberschenkelweite den gemessenen Oberschenkelumfang nicht überschreitet, damit die Leggings dort tatsächlich anliegt.
- **Quelle:** `formeln_s501.md`, Zeile 28; Originaltranskript `s501.md`, Zeile 42; Buchseite 501. Schritttext: Schritt 16, Transkriptzeile 17.
- **Originalbezeichnung:** `OsW kontrollieren = 51 cm → < OsU (55,5 cm) ✓`
- **Normalisierte Bezeichnung:** `kontrolle_oberschenkelweite_leggings`

### Buchfassung

```text
- OsW kontrollieren = 51 cm → < OsU (55,5 cm) ✓
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `oberschenkelweite_konstruiert` | OsW | 51 | cm |
| `oberschenkelumfang_gemessen` | OsU | 55,5 | cm |
| `messhoehe_unter_schrittlinie` | `ca. 5 cm` | 5 | cm |

### Formel und Rechenschritte

```text
Prüfbedingung:
oberschenkelweite_konstruiert <= oberschenkelumfang_gemessen

gemessen an einer Waagerechten ca. 5 cm unterhalb der Schrittlinie.

Buchwerte:
51 cm <= 55,5 cm  ->  erfüllt (im Buch mit "✓" bestätigt)
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kontrolle_oberschenkelweite_erfuellt` | Wahrheitswert der Prüfbedingung | dimensionslos |

- **Abhängigkeiten:** Die konstruierte Weite ergibt sich aus dem fertigen Grundgerüst und ist keine eigene Formel der Quelle; `OsU` ist ein gemessenes Körpermaß.
- **Gültigkeitsbereich:** Messhöhe „ca. 5 cm unterhalb der Schrittlinie" nach Schritt 16.
- **Technische Randbedingung:** Dies ist eine **Prüfbedingung**, keine Abtragung — dieselbe Art von Beziehung wie die Mindest-Taillenweite `HOF-B1-S494-F06`. Der Vergleich läuft gegen den **gemessenen**, nicht gegen einen reduzierten `OsU`; das ist folgerichtig, weil die Kontrolle die anliegende Passform sichert. Das Buch schreibt „höchstens", die Zeichnung schreibt „<"; die Normalisierung übernimmt das ausformulierte „höchstens" als `<=`.
- **Offene Fragen oder Widersprüche:** **Der eingesetzte `OsU`-Wert widerspricht der Konstruktionstabelle auf S. 500.** Die Tabelle trägt dort `OsU = 72` ein, die Kontrolle rechnet mit `55,5`. `55,5` ist zugleich der `OsU`-Wert der Jogginghosen-Tabelle auf S. 498 für dieselbe Größe 38 und damit der plausible Wert; die Tabellenzeile auf S. 500 wiederholt dagegen den Taillenumfang `72`. Der Widerspruch ist gedruckt und wird nicht aufgelöst, weil die Quelle keine Korrektur enthält. Mit dem Tabellenwert `72` wäre die Kontrolle wirkungslos. Die `OsU`-Zeile der S.-500-Tabelle liegt nicht im Extrakt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Nachprüfung nach dem Aufbau des Grundgerüsts implementieren, nicht als Konstruktionsschritt. Bei Verletzung keine automatische Korrektur vornehmen — die Quelle gibt keine an — sondern melden. Der `OsU`-Wert muss ausdrücklich aus dem Maßsatz kommen und nicht aus der widersprüchlichen Tabellenzeile.

## HOF-B1-S501-F08 — Kontrolle der Knieweite

- **Fachlicher Zweck:** Nach der Konstruktion prüfen, dass die fertige Knieweite den gemessenen Knieumfang nicht überschreitet.
- **Quelle:** `formeln_s501.md`, Zeile 29; Originaltranskript `s501.md`, Zeile 43; Buchseite 501. Schritttext: Schritt 17, Transkriptzeile 18.
- **Originalbezeichnung:** `KnW kontrollieren = 33,2 cm → < KnU (34 cm) ✓`
- **Normalisierte Bezeichnung:** `kontrolle_knieweite_leggings`

### Buchfassung

```text
- KnW kontrollieren = 33,2 cm → < KnU (34 cm) ✓
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `knieweite_konstruiert` | KnW | 33,2 | cm |
| `knieumfang_gemessen` | KnU | 34 | cm |

### Formel und Rechenschritte

```text
Prüfbedingung:
knieweite_konstruiert <= knieumfang_gemessen

gemessen an der Knielinie.

Buchwerte:
33,2 cm <= 34 cm  ->  erfüllt (im Buch mit "✓" bestätigt)
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kontrolle_knieweite_erfuellt` | Wahrheitswert der Prüfbedingung | dimensionslos |

- **Abhängigkeiten:** Die konstruierte Knieweite ergibt sich aus dem fertigen Grundgerüst; `KnU` ist ein gemessenes Körpermaß.
- **Gültigkeitsbereich:** Messung an der Knielinie nach Schritt 17.
- **Technische Randbedingung:** Prüfbedingung wie `HOF-B1-S501-F07`, ebenfalls gegen den gemessenen Wert. Der Abstand zur Grenze ist mit `0,8 cm` hier deutlich knapper als bei der Oberschenkelkontrolle (`4,5 cm`); die Knieweite ist damit die bindende Kontrolle dieses Grundschnitts.
- **Offene Fragen oder Widersprüche:** **Derselbe Widerspruch wie bei `HOF-B1-S501-F07`:** Die Konstruktionstabelle auf S. 500 trägt `KnU = 72` ein, die Kontrolle rechnet mit `34`. Die Jogginghosen-Tabelle auf S. 498 lässt die `KnU`-Zeile leer, liefert also keinen Vergleichswert. `34 cm` ist für Größe 38 der fachlich plausible Knieumfang, `72` wiederholt erneut den Taillenumfang. Die Quelle enthält keine Korrektur; der Widerspruch bleibt bestehen. Die `KnU`-Zeile der S.-500-Tabelle liegt nicht im Extrakt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Wie `HOF-B1-S501-F07` als meldende Nachprüfung führen. Weil der Abstand zur Grenze klein ist, sollte die Prüfung mit den ungerundeten Zwischenwerten laufen; die gedruckten `33,2` und `34` sind gerundete Angaben.

## HOF-B1-S501-F09 — Wadenhöhe aus der Kniehöhe

- **Fachlicher Zweck:** Den Höhenabstand der Wadenlinie unterhalb der Knielinie aus der Kniehöhe bestimmen.
- **Quelle:** `formeln_s501.md`, Zeile 34; Originaltranskript `s501.md`, Zeile 46; Buchseite 501.
- **Originalbezeichnung:** `WaH = KnH : 2`
- **Normalisierte Bezeichnung:** `wadenhoehe_leggings`

### Buchfassung

```text
- WaH = KnH : 2; KnH; TaH; SiH
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `kniehoehe` | KnH | 32 (Konstruktionstabelle S. 500) | cm |
| `halbierungsfaktor` | `: 2` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
wadenhoehe = kniehoehe / 2

Buchwert der Konstruktionstabelle auf S. 500 (KnH = 32 cm):
wadenhoehe = 32 cm / 2 = 16 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `wadenhoehe` | Höhenabstand zwischen Knielinie und Wadenlinie im Grundgerüst | cm |

- **Abhängigkeiten:** `KnH` aus `HOF-B1-S500-F08`, diese aus `SrH = sTaH − SiH`.
- **Gültigkeitsbereich:** Grundgerüst der Leggings; Schritt 11 auf S. 500 trägt die `WaH` von der Knielinie aus nach unten ab.
- **Technische Randbedingung:** Die weiteren Angaben derselben Extraktzeile (`KnH`, `TaH`, `SiH`) sind Maßbezeichnungen der Zeichnung ohne eigene Rechenoperation. `KnH` ist auf S. 500 als `HOF-B1-S500-F08` normalisiert, `TaH` und `SiH` sind Körpermaße; `SiH` geht reduziert ein (`HOF-B1-S501-F03`).
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit. Die Konstruktionstabelle auf S. 500 führt keine `WaH`-Zeile; diese Beschriftung ist die einzige Fundstelle der Wadenhöhen-Berechnung für die Leggings.
- **Abgrenzung:** Wortgleich mit `HOF-B1-S499-F01` der Jogginghose. Beide bleiben getrennt, weil Jogginghose und Leggings verschiedene Grundschnitte mit eigener Schrittfolge sind und keine der Seiten eine Identität erklärt. Anders als bei den Umfangsformeln ergeben beide hier denselben Wert, weil `KnH` in beiden Konstruktionen `32 cm` beträgt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `WaH` als abgeleiteten Wert aus `KnH` führen. Die Wadenlinie liegt bei `KnH + WaH` unterhalb der Schrittlinie.

## Zeichnungsbelege zu Schritten auf S. 500

Die Extraktzeile 27 fasst sechs Zeichnungsbeschriftungen in einer Zeile zusammen. Drei davon wiederholen Schritte, deren Text auf S. 500 steht und dort als Kandidatenzeile extrahiert und normalisiert ist. Sie erhalten nach der in `V3-J05` festgelegten Regel keine zweite ID.

| Beschriftung auf S. 501 | Schritttext auf S. 500 | Normalisiert als |
|---|---|---|
| `HüU : 4` | Schritt 6 | `HOF-B1-S500-F03` — Halbe Hosenbreite an der Schrittlinie |
| `HüU : 10` | Schritt 8 | `HOF-B1-S500-F04` — Verlängerung der hinteren Hüftlinie |
| `HüU : 20 + 1 bis 2 cm` | Schritt 9 | `HOF-B1-S500-F05` — Verlängerung der vorderen Hüftlinie |

Die drei übrigen Angaben derselben Zeile erhalten eigene IDs, weil sie im S.-500-Extrakt nicht vorkommen: `HüU : 20 + 3 cm` (`F04`, im Schritttext von S. 500 überhaupt nicht enthalten) sowie `FeU : 2` (`F05`) und `WaU : 2` (`F06`), deren Schritttext auf S. 500 zwar im Transkript steht, dort aber nicht extrahiert ist.

Die Zusammenführung ist durch die Seiten selbst gedeckt: Die Zeichnung auf S. 501 gehört zum Grundschnitt, dessen Schritte 1 bis 15 auf S. 500 stehen, und S. 501 setzt die Zählung mit Schritt 16 fort.

## Ausgeschlossene Kandidaten

Keine. Alle zehn extrahierten Kandidatenzeilen sind Rechenbeziehungen und in Formelblöcken abgebildet.

## Abrechnung der Kandidatenzeilen

| | Anzahl |
|---|---:|
| Extrahierte Kandidatenzeilen | 10 |
| In Formelblöcken abgebildet | 10 |
| Ausgeschlossen | 0 |
| Erzeugte Formel-IDs | 9 |

Die Zuordnung im Einzelnen: Zeile 9 und Zeile 14 tragen gemeinsam `F01`; die Zeilen 15–17 tragen gemeinsam `F02`; Zeile 22 trägt `F03`; Zeile 27 trägt `F04`, `F05` und `F06` sowie drei Belege zu S. 500; Zeile 28 trägt `F07`; Zeile 29 trägt `F08`; Zeile 34 trägt `F09`.

## Prüfhinweise

1. **Drei verschiedene Prozentsätze:** Die Seite führt drei getrennte Reduzierungen, die nicht vermischt werden dürfen — Umfangsmaße `5 bis 20 %` (`F02`, im Beispiel 15 %), Taillenumfang `0 bis 5 %` (`F01`, im Beispiel 0 %), Längenmaß Sitzhöhe `0 bis 5 %` (`F03`, im Beispiel 5 %). Die Zeichnung bestätigt die Trennung mit zwei Reduktionspfeilen: `−15 %` für Umfang, `−5 %` für Länge.
2. **Kontrollen rechnen gegen gemessene Werte:** `OsU` und `KnU` werden nicht reduziert. Das ist fachlich stimmig — die Kontrolle sichert, dass die konstruierte Weite den Körper nicht überschreitet — steht aber nirgends ausdrücklich in der Quelle.
3. **⚠️ Zwei widersprüchliche Körpermaße:** Die Konstruktionstabelle auf S. 500 trägt `OsU = 72` und `KnU = 72` ein, die Kontrollen auf dieser Seite rechnen mit `55,5` und `34`. Beide Tabellenwerte wiederholen den Taillenumfang und sind sehr wahrscheinlich ein Übertragungsfehler der Spalte. Ebenso trägt die `RiU`-Zeile dort `→ 19,6`, den reduzierten Fesselumfang, während die `FeU`-Zeile den unreduzierten Wert `23` führt. Keine dieser Tabellenzeilen liegt im Extrakt; die Widersprüche sind vermerkt, nicht bereinigt.
4. **`SiH` doppelt geführt:** Die reduzierte `SiH` (24,7 cm) geht in Schritt 5 auf S. 500 ein, die `SrH`-Zeile derselben Tabelle rechnet aber mit der unreduzierten `SiH` (26 cm). Beide Zahlen stehen gedruckt in derselben Tabelle. Siehe `HOF-B1-S500-F08` und `HOF-B1-S501-F03`.
5. **Rundung:** Alle drei Umfangsreduzierungen sind auf eine Nachkommastelle aufgerundet (`82,45 → 82,5`, `29,75 → 29,8`, `19,55 → 19,6`), die Längenreduzierung trifft mit `24,7` exakt. Eine Rundungsregel nennt die Quelle nicht; exakte und gedruckte Werte bleiben getrennt. Dieselbe Behandlung wie bei den Umfangsteilwerten in `V3-H01`.
6. **`TaH` ohne Reduzierung:** Schritt 1 auf S. 500 zeichnet die Seitenlinie mit der Länge `TaH`, und die Tabelle führt `sTaH = 106` unreduziert. Die Längenreduzierung von `0 bis 5 %` betrifft ausweislich der Überschrift nur „das Längenmaß" im Singular, also die `SiH`. Ob die `TaH` bewusst ausgenommen ist, sagt die Quelle nicht.
7. **Extraktionsgrenze:** Das Originaltranskript `s501.md` enthält weitere bemaßte Angaben, die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen und deshalb nicht als Buchfassungen ergänzt wurden:
   - Zeile 44: `Für Herren + ca. 0,7 cm`;
   - Zeile 45: die Bruchangaben `½`, `¼` und `½` am vorderen Hosenausschnitt mit den Symbolen `♀` und `♂`;
   - Zeile 47: `1 bis 1,5 cm` (Kürzung oben, Schritt 4) · `2 bis 3 cm` (Einstellung an der Knielinie, Schritt 14) · `ca. 1 cm` (Einstellung der vM, Schritt 18) · `3 cm` (Einstellung der Gesäßnaht, Schritt 21; Ausstellung an P3a, Schritt 3a) · `5 cm` (Messhöhe der Oberschenkelkontrolle, Schritt 16) · `6 bis 8 cm` (Kürzung unten, Schritt 2);
   - Zeile 12: die Halbierungsmarke `½` am Bund für den Gummitunnel.

   Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
