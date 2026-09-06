# Fachlich normalisierte Formeln — S. 498

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s498.md`
Originaltranskript: `s498.md`
Buchseite: Hofenbitzer, Band 1, S. 498

Die Seite eröffnet den Grundschnitt der engen Jogginghose. Sie ist laut Buch „als Grundlage für lockere Hosen aus elastischem Material (z. B. die meisten Maschenwaren)" gedacht; der Schnitt „sitzt locker an Gesäß und Oberschenkel. Die Umfangsmaße werden aus diesem Grund nicht reduziert." Die extrahierten Kandidatenzeilen stammen aus den Konstruktionsschritten 3, 6, 8, 9 und 12 sowie aus der Konstruktionstabelle Hose. Anders als bei den Hosen der Tranchen `H01` bis `H06` wird die Breite hier nicht über vHoB und hHoB, sondern unmittelbar über Teilwerte des Hüftumfangs auf der Schrittlinie aufgebaut.

**Seitenübergreifender Zusammenhang:** Die zugehörige Zeichnung `□2` steht auf S. 499, die dortige Schrittzählung setzt mit Schritt 16 fort. Fünf Beschriftungen der Zeichnung wiederholen die hier normalisierten Beziehungen `F01` bis `F05` und sind in `formeln_s499_normalisiert.md` nach der Regel aus `V3-J05` als Belege ohne eigene ID geführt; sie sind bei den einzelnen Formeln als Zeichnungsbeleg vermerkt. Zwei Beziehungen der Zeichnung haben auf S. 498 keinen Schritttext und tragen deshalb eigene IDs auf S. 499: die Wadenhöhe `WaH = KnH : 2` (`HOF-B1-S499-F01`) und der Höhenabstand der Hüftlinie `HüU : 20 + 3 cm` (`HOF-B1-S499-F02`). Letzterer schließt die Lücke, dass die Schritte 8 und 9 dieser Seite die Hüftlinie voraussetzen, ohne dass ein Schritt sie anlegt.

## HOF-B1-S498-F01 — Halbe Saumweite

- **Fachlicher Zweck:** Den nach rechts und links von der Seitenlinie abzutragenden Anteil der Saumweite bestimmen.
- **Quelle:** `formeln_s498.md`, Zeile 9; Originaltranskript `s498.md`, Zeile 31; Buchseite 498. Zeichnungsbeleg: `formeln_s499.md`, Zeile 15 (`s499.md`, Zeile 20).
- **Originalbezeichnung:** `SaW : 2`.
- **Normalisierte Bezeichnung:** `halbe_saumweite_jogginghose`

### Buchfassung

```text
3. Die SaW : 2 nach rechts und links abtragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `saumweite` | SaW | 30 | cm |
| `teilungsfaktor` | `: 2` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
halbe_saumweite = saumweite / 2

Buchwert der Konstruktionstabelle (SaW = 30 cm):
halbe_saumweite = 30 cm / 2 = 15 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `halbe_saumweite` | je Seite von der Seitenlinie abzutragende Strecke auf der Saumlinie | 15 | cm |

- **Abhängigkeiten:** SaW aus der Konstruktionstabelle (`s498.md`, Zeile 86); die dortige Bereichszeile ist als Auswahlangabe ausgeschlossen, der gewählte Wert `30` ist Eingabe.
- **Gültigkeitsbereich:** Grundschnitt der engen Jogginghose, Konstruktionsschritt 3, Größe 38.
- **Technische Randbedingung:** Der Wert wird beidseitig abgetragen; die abgetragene Gesamtstrecke entspricht damit der SaW. Die Konstruktion hat an dieser Stelle keine Vorder-/Hinterteilung, deshalb ist der Halbwert und nicht ein Viertelwert die Abtragung.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Betrag und Richtung trennen und die Abtragung spiegelsymmetrisch zur Seitenlinie ausführen.

## HOF-B1-S498-F02 — Halbe Hüftbreite auf der Schrittlinie

- **Fachlicher Zweck:** Die auf der Schrittlinie nach rechts und links abzutragende Breite mit Bewegungszugabe bestimmen.
- **Quelle:** `formeln_s498.md`, Zeile 14; Originaltranskript `s498.md`, Zeile 34; Buchseite 498. Zeichnungsbeleg: `formeln_s499.md`, Zeile 10 (`s499.md`, Zeile 15).
- **Originalbezeichnung:** `HüU : 4 + 0 bis 2 cm`.
- **Normalisierte Bezeichnung:** `schrittlinienbreite_jogginghose`

### Buchfassung

```text
6. Auf dieser nach rechts und links HüU : 4 + 0 bis 2 cm abtragen und jeweils
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `breitenzugabe` | `0 bis 2 cm` | 0 bis 2 | cm |

### Formel und Rechenschritte

```text
allgemeine Form:
schrittlinienbreite = (hueftumfang / 4) + breitenzugabe

Buchwerte der Konstruktionstabelle (HüU = 97 cm):
untere Grenze = (97 cm / 4) + 0 cm = 24,25 cm
obere Grenze  = (97 cm / 4) + 2 cm = 26,25 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich | Einheit |
|---|---|---|---|
| `schrittlinienbreite` | je Seite auf der Schrittlinie abzutragende Strecke | 24,25 bis 26,25 | cm |

- **Abhängigkeiten:** HüU aus der Hauptmaßtabelle (`s498.md`, Zeile 62). Der dort ausgewiesene Viertelwert `24,25` bestätigt die Teilung.
- **Gültigkeitsbereich:** Grundschnitt der engen Jogginghose, Konstruktionsschritt 6, Größe 38.
- **Technische Randbedingung:** Die Zugabe ist ein Bereich und muss als Modellparameter gewählt werden. Das anschließende Abwinkeln zur Taillenlinie (Schritt 7) ist eine Linienkonstruktion und nicht Teil dieser Strecke.
- **Offene Fragen oder Widersprüche:** Das Buch nennt keine Regel, wie innerhalb von `0 bis 2 cm` zu wählen ist. Die Seite begründet die Weite allgemein damit, dass die Umfangsmaße wegen des lockeren Sitzes nicht reduziert werden; eine Zuordnung der Zugabe zu Material oder Figur fehlt.
- **Abgrenzung:** Der auf S. 494 und S. 497 verwendete Weg über `¼ HüU ± 1 cm` ist nicht wortgleich und wird nicht mit dieser Beziehung zusammengeführt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Zugabe als Bereich mit unterer und oberer Grenze führen und den gewählten Wert als Modellparameter übergeben; keine Vorbelegung aus diesem Beispiel ableiten.

## HOF-B1-S498-F03 — Verlängerung der Hüftlinie hinten

- **Fachlicher Zweck:** Die Verlängerung der Hüftlinie nach links, also am hinteren Teil, bestimmen.
- **Quelle:** `formeln_s498.md`, Zeile 19; Originaltranskript `s498.md`, Zeile 36; Buchseite 498. Zeichnungsbeleg: `formeln_s499.md`, Zeile 11 (`s499.md`, Zeile 16).
- **Originalbezeichnung:** `HüU : 10 + 0 bis 1 cm`.
- **Normalisierte Bezeichnung:** `hueftlinien_verlaengerung_hinten_jogginghose`

### Buchfassung

```text
8. Die HüLi links (hinten) um HüU : 10 + 0 bis 1 cm und
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `verlaengerungszugabe_hinten` | `0 bis 1 cm` | 0 bis 1 | cm |

### Formel und Rechenschritte

```text
allgemeine Form:
verlaengerung_hinten = (hueftumfang / 10) + verlaengerungszugabe_hinten

Buchwerte der Konstruktionstabelle (HüU = 97 cm):
untere Grenze = (97 cm / 10) + 0 cm = 9,7 cm
obere Grenze  = (97 cm / 10) + 1 cm = 10,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich | Einheit |
|---|---|---|---|
| `verlaengerung_hinten` | Verlängerung der Hüftlinie nach links (hinten) | 9,7 bis 10,7 | cm |

- **Abhängigkeiten:** HüU aus der Hauptmaßtabelle; die in Schritt 6 abgetragene Schrittlinienbreite als Ansatzpunkt der Verlängerung.
- **Gültigkeitsbereich:** Grundschnitt der engen Jogginghose, Konstruktionsschritt 8, Größe 38.
- **Technische Randbedingung:** Die Buchfassung schreibt `HüLi`; die Schritte 5 und 6 legen die Linie als Schrittlinie an. Beide Bezeichnungen stehen so im Buch und wurden nicht vereinheitlicht.
- **Offene Fragen oder Widersprüche:** Die Auswahl innerhalb von `0 bis 1 cm` ist nicht geregelt. Die Buchfassung ist ein Satzteil, dessen Verb `verlängern` erst in der Folgezeile (Schritt 9) steht; die Zeilen 8 und 9 gehören syntaktisch zusammen, tragen aber getrennte Rechenwege und sind deshalb als zwei Formeln geführt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Gemeinsam mit `HOF-B1-S498-F04` als Paar führen; hinten und vorne haben unterschiedliche Teiler und Zugabebereiche und dürfen nicht zusammengefasst werden.

## HOF-B1-S498-F04 — Verlängerung der Hüftlinie vorne

- **Fachlicher Zweck:** Die Verlängerung der Hüftlinie nach rechts, also am vorderen Teil, bestimmen.
- **Quelle:** `formeln_s498.md`, Zeile 20; Originaltranskript `s498.md`, Zeile 37; Buchseite 498. Zeichnungsbeleg: `formeln_s499.md`, Zeile 12 (`s499.md`, Zeile 17).
- **Originalbezeichnung:** `HüU : 20 + 1 bis 2 cm`.
- **Normalisierte Bezeichnung:** `hueftlinien_verlaengerung_vorne_jogginghose`

### Buchfassung

```text
9. rechts (vorne) um HüU : 20 + 1 bis 2 cm verlängern.
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `verlaengerungszugabe_vorne` | `1 bis 2 cm` | 1 bis 2 | cm |

### Formel und Rechenschritte

```text
allgemeine Form:
verlaengerung_vorne = (hueftumfang / 20) + verlaengerungszugabe_vorne

Buchwerte der Konstruktionstabelle (HüU = 97 cm):
untere Grenze = (97 cm / 20) + 1 cm = 5,85 cm
obere Grenze  = (97 cm / 20) + 2 cm = 6,85 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich | Einheit |
|---|---|---|---|
| `verlaengerung_vorne` | Verlängerung der Hüftlinie nach rechts (vorne) | 5,85 bis 6,85 | cm |

- **Abhängigkeiten:** HüU aus der Hauptmaßtabelle; `HOF-B1-S498-F03` als zugehörige hintere Verlängerung.
- **Gültigkeitsbereich:** Grundschnitt der engen Jogginghose, Konstruktionsschritt 9, Größe 38.
- **Technische Randbedingung:** Die vordere Verlängerung ist kleiner als die hintere; das entspricht der üblichen Verteilung der Schrittweite. Eine Begründung nennt das Buch an dieser Stelle nicht.
- **Offene Fragen oder Widersprüche:** Die Auswahl innerhalb von `1 bis 2 cm` ist nicht geregelt. Der Ausdruck `HüU : 20 + …` ist rechnerisch gleich gebaut wie der Höhenabstand der Hüftlinie auf S. 495 (`HOF-B1-S495-F01`) und wie der unbezeichnete Ausdruck auf S. 497 (`HOF-B1-S497-F03`), bemaßt hier aber eine waagerechte Verlängerung und wurde deshalb nicht mit ihnen zusammengeführt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Teiler `20` und Zugabebereich `1 bis 2 cm` getrennt von den Werten der hinteren Verlängerung führen.

## HOF-B1-S498-F05 — Halbe Wadenweite mit Zugabe

- **Fachlicher Zweck:** Die auf der Wadenlinie nach links und rechts abzutragende Strecke bestimmen.
- **Quelle:** `formeln_s498.md`, Zeile 25; Originaltranskript `s498.md`, Zeile 40; Buchseite 498. Zeichnungsbeleg: `formeln_s499.md`, Zeile 14 (`s499.md`, Zeile 19).
- **Originalbezeichnung:** `WaU : 2 + 0 bis 1 cm`.
- **Normalisierte Bezeichnung:** `wadenlinienbreite_jogginghose`

### Buchfassung

```text
12. Den WaU : 2 + 0 bis 1 cm nach links und rechts abtragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `wadenumfang` | WaU | 35 | cm |
| `wadenzugabe` | `0 bis 1 cm` | 0 bis 1 | cm |

### Formel und Rechenschritte

```text
allgemeine Form:
wadenlinienbreite = (wadenumfang / 2) + wadenzugabe

Buchwerte der Proportionsmaßtabelle (WaU = 35 cm):
untere Grenze = (35 cm / 2) + 0 cm = 17,5 cm
obere Grenze  = (35 cm / 2) + 1 cm = 18,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich | Einheit |
|---|---|---|---|
| `wadenlinienbreite` | je Seite auf der Wadenlinie abzutragende Strecke | 17,5 bis 18,5 | cm |

- **Abhängigkeiten:** WaU aus der Proportionsmaßtabelle (`s498.md`, Zeile 75); die Wadenlinie entsteht in Schritt 11 durch Abtragen der WaH von der Knielinie.
- **Gültigkeitsbereich:** Grundschnitt der engen Jogginghose, Konstruktionsschritt 12, Größe 38.
- **Technische Randbedingung:** Der Wert wird beidseitig abgetragen; die entstehende Gesamtweite an der Wadenlinie liegt damit zwischen `WaU` und `WaU + 2 cm`.
- **Offene Fragen oder Widersprüche:** Die Auswahl innerhalb von `0 bis 1 cm` ist nicht geregelt. Die Wadenhöhe WaH ist in der Konstruktionstabelle der Seite nicht ausgewiesen und liegt auch nicht im Extrakt vor.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Halbwert und Zugabe getrennt führen, damit sich die Zugabe bei einer Weitenkontrolle über die volle Wadenweite verdoppelt.

## HOF-B1-S498-F06 — Kniehöhe aus der Schritthöhe

- **Fachlicher Zweck:** Die Kniehöhe der Jogginghose als vier Zehntel der Schritthöhe bestimmen.
- **Quelle:** `formeln_s498.md`, Zeile 30; Originaltranskript `s498.md`, Zeile 82; Buchseite 498.
- **Originalbezeichnung:** `SrH : 10 · 4`.
- **Normalisierte Bezeichnung:** `kniehoehe_jogginghose`

### Buchfassung

```text
| KnH | Kniehöhe | SrH : 10 · 4 | 32 |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `schritthoehe` | SrH | 80 | cm |

### Formel und Rechenschritte

```text
kniehoehe = (schritthoehe / 10) * 4
          = (80 cm / 10) * 4
          = 32 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `kniehoehe` | KnH | 32 | cm |

- **Abhängigkeiten:** SrH; der Wert 80 cm steht in der unmittelbar vorhergehenden Tabellenzeile des Originaltranskripts (`SrH = sTaH – SiH = 106 – 26`, Zeile 81) und ist selbst nicht extrahiert.
- **Gültigkeitsbereich:** Konstruktionstabelle der Jogginghose unisex, Größe 38, auf S. 498. Die KnH wird in Schritt 10 zur Anlage der Knielinie verwendet.
- **Technische Randbedingung:** Der Transkriptwert 80 cm dient nur als gekennzeichneter Rechenkontext; die Buchfassung bleibt auf die extrahierte KnH-Zeile beschränkt.
- **Offene Fragen oder Widersprüche:** Keine; der gedruckte Wert ist rechnerisch richtig.
- **Abgrenzung:** Die Beziehung ist wortgleich mit `HOF-B1-S494-F01` (einfache Hose) und `HOF-B1-S109-F03` (Standardhose). Sie erhält hier dennoch eine eigene ID, weil S. 498 eine eigene Konstruktionstabelle mit eigenem Maßsatz führt und die Seite den Sporthosen-Grundschnitt ausdrücklich nur als **Alternative** für weite Jogginghosen nennt, also keine Identität erklärt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Faktor als exakten Bruch `4/10` führen und erst bei der Ausgabe runden.

## HOF-B1-S498-F07 — Hinterhosenbreite als unausgefüllte Tabellenzeile

- **Fachlicher Zweck:** Den Grundwert der Hinterhosenbreite aus dem Viertel-Hüftumfang mit einem Zuschlag von 1 cm bestimmen.
- **Quelle:** `formeln_s498.md`, Zeile 40; Originaltranskript `s498.md`, Zeile 95; Buchseite 498.
- **Originalbezeichnung:** `¼ HüU +1 cm`.
- **Normalisierte Bezeichnung:** `hinterhosenbreite_grundwert_jogginghose`

### Buchfassung

```text
| hHoB | Hinterhosenbreite | ¼ HüU +1 cm | ± [leer] | --- |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `viertel_hueftumfang` | ¼ HüU | 24,25 | cm |
| `breitenzuschlag` | `1 cm` | 1 | cm |

### Formel und Rechenschritte

```text
hinterhosenbreite_grundwert = viertel_hueftumfang + breitenzuschlag

Buchwerte der Hauptmaßtabelle (¼ HüU = 24,25 cm):
hinterhosenbreite_grundwert = 24,25 cm + 1 cm = 25,25 cm

Wertespalte der Buchfassung: `---` (nicht ausgefüllt)
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hinterhosenbreite_grundwert` | hHoB vor Anwendung einer Zugabe | 25,25 | cm |

- **Abhängigkeiten:** ¼ HüU = 24,25 cm aus der Hauptmaßtabelle (`s498.md`, Zeile 62).
- **Gültigkeitsbereich:** Konstruktionstabelle der Jogginghose unisex, Größe 38, auf S. 498.
- **Technische Randbedingung:** Die Zeile ist im Buch **nicht ausgefüllt**: Die Zugabespalte ist leer, die Wertespalte trägt `---`. Der Berechnungsweg ist gedruckt, ein Ergebnis nicht. Der berechnete Wert ist deshalb nur als Rechenkontext ausgewiesen und keine Buchangabe.
- **Offene Fragen oder Widersprüche:** Die Konstruktionsschritte 1 bis 15 dieser Seite verwenden hHoB nicht; die Breite entsteht dort über `HüU : 4 + 0 bis 2 cm` (`HOF-B1-S498-F02`) und die beiden Hüftlinien-Verlängerungen. Die Tabellenzeile gehört zum vorgedruckten Formular der Konstruktionstabelle Hose und wurde für die Jogginghose bewusst nicht gefüllt. Ob und wie sie für abgeleitete Modelle zu verwenden ist, sagt die Seite nicht.
- **Abgrenzung:** Die zugehörige vHoB-Zeile (`¼ HüU –1 cm`, ebenfalls unausgefüllt) steht im Originaltranskript unmittelbar darüber (`s498.md`, Zeile 94), liegt aber nicht im Extrakt vor. Sie ist als Extraktionslücke vermerkt und wurde nicht als eigene Buchfassung ergänzt. Der Berechnungsweg ist wortgleich mit `HOF-B1-S494-F02`; die dortige Zeile ist jedoch mit Zugabe und Ergebnis gefüllt und trägt den bekannten Widerspruch, der hier gerade nicht auftritt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Formel implementieren, aber nicht in den Konstruktionsweg der Jogginghose einbinden, solange keine Verwendung belegt ist. Keinen Zugabewert vorbelegen — die Zugabespalte ist im Buch leer.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 35 | 1 | `SaW`-Tabellenzeile: Bereichstabelle nach Hosenform (`Enge Hose 32 bis 40 · Standardhose 40 bis 48 · Weite Hose 48 bis 56`) mit dem gewählten Wert `30`; Auswahlangabe ohne Rechenoperation |
| **Summe** | **1** | **1 Auswahltabelle** |

Zur ausgeschlossenen `SaW`-Zeile: Der gewählte Wert `30 cm` liegt **unterhalb** aller drei gedruckten Bereiche; der niedrigste beginnt bei `32` für die enge Hose. Das Buch nennt dazu keine Begründung und keine Auswahlregel; die Zeile ordnet Bereiche zu und berechnet nichts. Der Wert `30` steht im Buch als ein über alle drei Zeilen gehender Eintrag (`s498.md`, Zeile 88). Dieselbe Behandlung hat die entsprechende Zeile auf S. 494 mit dem Wert `50`. Als Eingabe von `HOF-B1-S498-F01` ist der Wert dort ausgewiesen.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s498.md` enthält weitere rechenfähige Angaben, die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen und deshalb nicht als Buchfassungen ergänzt wurden:

- Schritt 1 (Senkrechte mit der Länge TaH), Schritt 2 (`um 6 bis 8 cm kürzen`), Schritt 4 (`1 bis 1,5 cm kürzen`), Schritt 5 (SiH abtragen), Schritt 10 (KnH abtragen), Schritt 11 (WaH abtragen), Schritt 3a (`ca. 3 cm` nach oben) und Schritt 14 (`1 bis 2 cm einstellen`) — Zeilen 29–44;
- die Zeile `SrH | Schritthöhe | sTaH – SiH | 80` (Zeile 81) — Eingabe von `HOF-B1-S498-F06`;
- die Halb- und Viertelwerte der Hauptmaßtabelle (Zeilen 61–62);
- die vHoB-Zeile `¼ HüU –1 cm` (Zeile 94);
- die GeWi-Tabelle einschließlich `+1° bis +2°` für längs-elastischen Stoff (Zeilen 99–106).

Zwei Besonderheiten der Seite sind gesondert zu vermerken:

1. **Schrittnummerierung:** Der Schritt `3a` steht im Buch zwischen den Schritten 12 und 13 und nicht in der Zählung nach Schritt 3. Das geprüfte Transkript hält dies in Zeilen 46–47 ausdrücklich fest; die Reihenfolge wurde nicht umgestellt.
2. **Falscher Seitenverweis:** Der Verweis „Sporthosen-Grundschnitt auf Seite 468" (Zeile 17) steht so im Buch; die Sporthose ist tatsächlich auf S. 496 abgebildet, ihr Grundschnitt auf S. 494. Der gedruckte Wortlaut bleibt unverändert; auf die Formeln dieser Seite wirkt der Fehler nicht.

Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
