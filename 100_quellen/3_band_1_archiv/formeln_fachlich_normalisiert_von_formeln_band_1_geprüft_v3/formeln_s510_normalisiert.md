# Fachlich normalisierte Formeln — S. 510

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s510.md`
Originaltranskript: `s510.md`
Buchseite: Hofenbitzer, Band 1, S. 510

Die Seite schließt den Shirt-Grundschnitt mit Teil 3, der **Optimierung des Vorderteils** für Figuren mit größerer Vorderlänge. Sie zeigt den Tabellenausschnitt `□5 Ausschnitt der Konstruktionstabelle mit größerer Vorderlänge`, die Schritte 1 bis 7 der Abnäher-Konstruktion und die Zeichnung `□6`.

Die Optimierung gilt laut Seitentext „für alle Konstruktionen dieser Art von Shirt-Grundschnitten, bei denen die Vorderlänge (VL) nicht in der Konstruktion verwendet wird". Sie fügt die überschüssige Mehrlänge des Vorderteils nachträglich als Brustabnäher in der Seitennaht ein.

Eine einzige Kandidatenzeile ist extrahiert: die Abnäherinhaltszeile des Tabellenausschnitts. Sie trägt zwei Rechenbeziehungen und erhält zwei Formel-IDs. Ausgeschlossen wurde keine Zeile.

Bezugsgrößen des Tabellenausschnitts (nicht extrahiert, hier nur als Eingabewerte zitiert): `RüL = 41,6 cm`, `VL = 46,8 cm`, Größe 38, Modell T-Shirt.

## HOF-B1-S510-F01 — Differenz aus Vorderlänge und Rückenlänge bei größerer Vorderlänge

- **Fachlicher Zweck:** Die Mehrlänge des Vorderteils gegenüber dem Rückenteil für das zweite Zahlenbeispiel bestimmen, in dem die Optimierung tatsächlich nötig wird.
- **Quelle:** `formeln_s510.md`, Zeile 9; Originaltranskript `s510.md`, Zeile 29; Buchseite 510.
- **Originalbezeichnung:** `Differenz VL − RüL`
- **Normalisierte Bezeichnung:** `laengendifferenz_vt_rt_grosse_vl`

### Buchfassung

```text
|  | Differenz VL − RüL | 5,2 − 3 bis 4 | Abnäherinhalt 1,2 bis 2,2 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderlaenge` | VL (waagerechte Taille) | 46,8 | cm |
| `rueckenlaenge` | RüL (waagerechte Taille) | 41,6 | cm |

### Formel und Rechenschritte

```text
laengendifferenz = vorderlaenge - rueckenlaenge

Buchwerte des Tabellenausschnitts (VL = 46,8 cm, RüL = 41,6 cm):
laengendifferenz = 46,8 cm - 41,6 cm = 5,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `laengendifferenz` | Mehrlänge der Vorderlänge gegenüber der Rückenlänge | cm |

- **Abhängigkeiten:** `VL` und `RüL` aus dem Tabellenausschnitt `□5`, beide an der **waagerechten** Taille gemessen. Beide Zeilen stehen selbst nicht im Extrakt.
- **Gültigkeitsbereich und Randbedingungen:** Gilt für alle Shirt-Grundschnitte dieser Art, in denen die Vorderlänge nicht als Konstruktionsmaß verwendet wird. Die Differenz ist eine Kontrollgröße, keine Abtragung.
- **Offene Fragen oder Widersprüche:** Keine. `46,8 − 41,6 = 5,2` geht exakt auf. Die Rückenlänge ist mit `41,6 cm` dieselbe wie auf S. 508; verändert ist allein die Vorderlänge (`45,3 → 46,8 cm`). Der Ausschnitt zeigt damit dieselbe Figurgröße mit stärker gewölbter Brust — S. 508 beschreibt genau diesen Fall („Für Damen mit sehr großer Brust passt diese Konstruktion nicht optimal").
- **Abgrenzung:** Wortgleich mit `HOF-B1-S508-F05`. Beide behalten eine eigene ID; die Begründung steht in Prüfhinweis 1.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Nicht als zweite Formel implementieren, sondern als **zweiter Testfall** derselben Rechnung führen. Die beiden Beispiele decken zusammen die Fallunterscheidung ab: `3,7 cm` ohne und `5,2 cm` mit Optimierung.

## HOF-B1-S510-F02 — Abnäherinhalt bei größerer Vorderlänge

- **Fachlicher Zweck:** Den Inhalt des Brustabnähers bestimmen, um den das eingeschnittene Vorderteil geöffnet wird.
- **Quelle:** `formeln_s510.md`, Zeile 9; Originaltranskript `s510.md`, Zeile 29; Buchseite 510.
- **Originalbezeichnung:** `5,2 − 3 bis 4 → Abnäherinhalt 1,2 bis 2,2`
- **Normalisierte Bezeichnung:** `abnaeherinhalt_brustabnaeher_grosse_vl`

### Buchfassung

```text
|  | Differenz VL − RüL | 5,2 − 3 bis 4 | Abnäherinhalt 1,2 bis 2,2 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `laengendifferenz` | Differenz VL − RüL | 5,2 | cm |
| `laengenausgleich` | `− 3 bis 4` | 3 bis 4 | cm |

### Formel und Rechenschritte

```text
abnaeherinhalt = laengendifferenz - laengenausgleich

Bereichsgrenzen mit dem Buchwert der Differenz (5,2 cm):
abnaeherinhalt = 5,2 cm - 4 cm = 1,2 cm   (Abzug 4 cm, untere Grenze)
abnaeherinhalt = 5,2 cm - 3 cm = 2,2 cm   (Abzug 3 cm, obere Grenze)

Gedrucktes Ergebnis: 1,2 bis 2,2 cm
```

Der gedruckte Ergebnisbereich ist aufsteigend geschrieben und dreht die Reihenfolge des Abzugsbereichs damit um: Der größere Abzug ergibt den kleineren Abnäherinhalt.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abnaeherinhalt` | Öffnungsmaß des eingeschnittenen Vorderteils, Inhalt des Brustabnähers in der Seitennaht | cm |

- **Abhängigkeiten:** `HOF-B1-S510-F01`. Nachgelagert: Schritt 4 der Optimierung („Das VT dort einschneiden und um den Abnäherinhalt nach unten verschieben").
- **Gültigkeitsbereich und Randbedingungen:** Der Abzug `3 bis 4 cm` ist der Anteil der Längendifferenz, den der Grundschnitt ohne Abnäher bereits aufnimmt; nur der Überschuss wird als Abnäher abgeführt. Die Quelle nennt keine Auswahlregel innerhalb des Bereichs.
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit — beide Bereichsgrenzen gehen exakt auf. Die Zeichnung `□6` beschriftet die Öffnung dagegen mit `hier um ca. 2 cm Abnäherinhalt öffnen`. `2 cm` liegt im Bereich `1,2 bis 2,2 cm`, entspricht aber keiner der beiden Grenzen und ist damit ein gewählter Wert innerhalb des Bereichs. Die Quelle nennt keine Auswahlregel; sie wurde nicht ergänzt. Die Zeichnungsbeschriftung liegt nicht im Extrakt.
- **Abgrenzung:** Wortgleich mit `HOF-B1-S508-F06`, dort jedoch **ohne** gedrucktes Ergebnis. Erst hier druckt das Buch den Ergebnisbereich aus und macht die Rechnung damit vollständig nachprüfbar. Beide behalten eine eigene ID; siehe Prüfhinweis 1.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Der Abnäherinhalt ist das einzige Maß, das die gesamte Optimierung steuert — alle sieben Schritte hängen daran. Als Intervall führen und den in der Zeichnung gewählten Wert als frei setzbaren Punkt innerhalb des Intervalls, nicht als abgeleitete Größe.

## Ausgeschlossene Kandidaten

Keine. Die einzige extrahierte Kandidatenzeile ist eine vollständige Rechenbeziehung und trägt zwei Formel-IDs.

## Prüfhinweise

1. **Eigene IDs trotz wortgleicher Beziehung zu S. 508:** `Differenz VL − RüL` und der Abnäherinhalt stehen auf beiden Seiten. Sie erhalten hier dennoch eigene IDs, aus drei Gründen: S. 510 führt einen **eigenen Maßsatz** (`VL = 46,8 cm` statt `45,3 cm`) in einem eigenen, eigens bezeichneten Tabellenausschnitt `□5`; sie druckt als einzige der beiden Seiten ein **Ergebnis** (`1,2 bis 2,2 cm`), wo S. 508 die Spalte leer lässt; und sie ist die Seite, auf der der Wert konstruktiv **verwendet** wird (Schritt 4). Das ist dieselbe Regel wie in `V3-S03`, wo wortgleiche Beziehungen mit eigenen Maßsätzen getrennte IDs behalten. Ein Zeichnungsbeleg im Sinne von `V3-J05` liegt gerade nicht vor: Der Tabellenausschnitt wiederholt die Zeile von S. 508 nicht, sondern rechnet sie mit anderen Eingaben neu. Beide Dateien sind gegenseitig verlinkt.
2. **Zwei Beispiele, eine Fallunterscheidung:** S. 508 ergibt `−0,3 bis 0,7 cm` und damit „um die 0 cm" — der Grundschnitt genügt ohne Optimierung. S. 510 ergibt `1,2 bis 2,2 cm` — die Optimierung wird ausgeführt. Die Schwelle zwischen beiden Fällen ist **nicht** gedruckt: Das Buch nennt weder einen Grenzwert noch eine Regel, ab welchem Abnäherinhalt die Optimierung nötig wird. Die Lücke ist benannt und nicht durch einen erfundenen Schwellwert geschlossen.
3. **Die Vorderlänge ist erst hier Konstruktionsmaß:** Der Seitentext hält zweimal fest, dass die Vorderlänge im Grundschnitt „bislang nicht als Konstruktionsmaß verwendet worden ist" und hier nachträglich verwendet wird. Der Grundschnitt auf S. 509 ist davon unberührt; die Optimierung ist ein nachgelagerter Arbeitsgang am fertigen Vorderteil und verändert keine der Beziehungen `HOF-B1-S509-F01` bis `F03`.
4. **Abnäherlänge wird gemessen, nicht gerechnet:** Die Schritte 5 und 6 kürzen den Abnäher „um 2 bis 4 cm" und übertragen die Länge des unteren Schenkels durch **Messen** auf den oberen (Zeichnungsbeschriftungen `Abnäherlänge me` und `Abnäherlänge üb`). Beide Schenkel sind damit gleich lang, aber ihre Länge ist keine Formel, sondern das Ergebnis einer Konstruktion. Die Zeilen liegen nicht im Extrakt und wurden nicht als Formeln ergänzt.
5. **Doppelt gedruckter Abschnittstext:** Die Erläuterung „Diese Optimierung gilt für alle Konstruktionen …" steht auf der Seite zweimal, einmal als Vorspann (Transkriptzeilen 13 bis 15) und einmal als Einleitung des Schrittteils (Zeilen 35 bis 37), mit leicht abweichendem Wortlaut. Beide Fassungen sagen dasselbe; die Doppelung ist so gedruckt und berührt keine Formel.
6. **Extraktionsgrenze:** Das Originaltranskript `s510.md` enthält weitere rechenfähige Beziehungen, die im verbindlichen Extrakt fehlen und deshalb nicht als Buchfassungen ergänzt wurden:
   - Zeile 39: Schritt 1, `Brusttiefe (BrT)` von der oberen Grundlinie nach unten abtragen — `BrT = 28,1 cm` aus der Konstruktionstabelle S. 508;
   - Zeile 40: Schritt 2, `Brustpunktabstand+ (BrPA+)` von der vM ins VT abtragen → BrP — die einzige Verwendung von `HOF-B1-S508-F04` im ganzen Kapitel;
   - Zeile 43: Schritt 5, „Den Abnäher um 2 bis 4 cm kürzen";
   - Zeile 44: Schritt 6, die Längenübertragung des Abnäherschenkels;
   - Zeile 52: die Zeichnungsbeschriftung `hier um ca. 2 cm Abnäherinhalt öffnen`.

   Besonders die Schritte 1 und 2 sind vollständige Abtragungen mit benannten Eingaben; ohne sie ist der Brustpunkt `BrP` — der Drehpunkt der gesamten Optimierung — im Extrakt nicht belegt. Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
