# Fachlich normalisierte Formeln — S. 504

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s504.md`
Originaltranskript: `s504.md`
Buchseite: Hofenbitzer, Band 1, S. 504

Die Seite entwickelt aus der Leggings die Damen-Longpants mit Nahtabtrennungen, die „durch die Nahtabtrennungen einen übergezogenen Tanga" imitiert; das Innenbein erhält gegenüber dem Leggings-Schnitt etwas mehr Länge. Der verbindliche Extrakt enthält genau eine Kandidatenzeile: die gesammelten Beschriftungen des vergrößerten Detailkreises zur Zeichnung `□2`. Von den dort aufgeführten Angaben trägt nur die Kette `messen (2×) → übertragen → übertragen + ca. 1 cm` eine Rechenoperation; sie gehört zu den Konstruktionsschritten 4 und 5, deren Schritttext selbst nicht extrahiert ist. Der Maßsatz stammt aus der Konstruktionstabelle der Leggings auf S. 500.

## HOF-B1-S504-F01 — Verlängerung von hM und vM aus der gemessenen Leggings-Länge

- **Fachlicher Zweck:** Die hintere und die vordere Mitte des Longpants-Schnitts gerade so weit verlängern, wie die entsprechende Kante der Leggings ab der Hüftlinie misst, zuzüglich eines Längenzuschlags für das mehrlängige Innenbein.
- **Quelle:** `formeln_s504.md`, Zeile 9; Originaltranskript `s504.md`, Zeile 42; Buchseite 504, vergrößerter Detailkreis zur Zeichnung `□2`. Zugehöriger Schritttext: `s504.md`, Zeilen 18–19 (Schritte 4 und 5), selbst nicht extrahiert. Weitere Beschriftung derselben Kette: `s504.md`, Zeile 41, ebenfalls nicht extrahiert.
- **Originalbezeichnung:** `messen (2×)`, `übertragen`, `übertragen + ca. 1 cm`
- **Normalisierte Bezeichnung:** `mittenverlaengerung_longpants`

### Buchfassung

```text
- Vergrößerter Detailkreis: HüL, SrLi, vM, messen (2×), übertragen, übertragen + ca. 1 cm, ca. 2,5 cm, Punkte 4–10
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `gesaessnahtlaenge_leggings` | Gesäßnaht der Leggings ab der HüLi | am Schnitt gemessen | cm |
| `hosenausschnittlaenge_leggings` | vorderer Hosenausschnitt der Leggings ab der HüLi | am Schnitt gemessen | cm |
| `laengenzuschlag` | `ca. 1 cm` | ca. 1 | cm |

### Formel und Rechenschritte

```text
verlaengerung_hm = gesaessnahtlaenge_leggings + laengenzuschlag
verlaengerung_vm = hosenausschnittlaenge_leggings + laengenzuschlag
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `verlaengerung_hm` | gerade Verlängerung der hinteren Mitte ab der Hüftlinie | cm |
| `verlaengerung_vm` | gerade Verlängerung der vorderen Mitte ab der Hüftlinie | cm |

- **Abhängigkeiten:** Beide Eingangslängen werden am gepunktet eingezeichneten Leggings-Schnitt abgegriffen (`HOF-B1-S500-F01` bis `F08` und `HOF-B1-S501-F01` bis `F09` liefern diesen Schnitt). Es sind gemessene Schnittgrößen, keine Körpermaße; das Buch beziffert sie nicht.
- **Gültigkeitsbereich:** Modellentwicklung der Damen-Longpants, Schritte 4 und 5, Zeichnung `□2` mit vergrößertem Detailkreis; Punkte 4–10.
- **Technische Randbedingung:** Der Zuschlag ist mit `ca.` als Näherungswert gedruckt und nicht als exakter Betrag zu führen. Beide Verlängerungen sind gerade Strecken ab der Hüftlinie; das anschließende Abwinkeln der halben Schrittbreite (Schritt 6) ist eine Linienkonstruktion und von dieser Strecke zu trennen.
- **Offene Fragen oder Widersprüche:** Keine innerhalb der Zeile. Schritttext und Detailkreis stimmen überein: Der Schritttext sagt „jeweils von der HüLi aus messen … und um diesen Betrag + ca. 1 cm die hM und vM gerade verlängern", der Detailkreis zeigt `messen` zweimal und `übertragen` einmal ohne und einmal mit dem Zuschlag. Welche der beiden Mitten den Zuschlag erhält, ist damit nicht getrennt ausgewiesen; der Schritttext nennt beide gemeinsam, und die Seite begründet die Mehrlänge einleitend am Innenbein.
- **Abgrenzung:** Die übrigen Angaben derselben Kandidatenzeile sind keine eigenen Rechenbeziehungen und erhalten keine ID: `HüL`, `SrLi` und `vM` sind Linienbezeichnungen, `Punkte 4–10` ist eine Punktaufzählung, und `ca. 2,5 cm` ist die feste halbe Schrittbreite aus Schritt 6 — ein direkter Näherungswert ohne benannte Eingabe, nach derselben Regel wie die Ausstellungswerte auf S. 495 nicht als Formel geführt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Beide Eingangslängen als am Schnitt gemessene Größen führen und den Zuschlag als konfigurierbaren Näherungswert mit Vorgabe `1 cm`. Nicht mit der Längenreduzierung `−5 %` der Leggings verrechnen; diese ist bereits im gemessenen Schnitt enthalten.

## Ausgeschlossene Kandidaten

Keine. Die einzige extrahierte Kandidatenzeile ist in `HOF-B1-S504-F01` abgebildet. Die nicht rechenfähigen Bestandteile derselben Zeile sind dort unter **Abgrenzung** einzeln begründet.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s504.md` enthält weitere rechenfähige oder bemaßte Angaben, die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen und deshalb nicht als Buchfassungen ergänzt wurden:

- Schritt 2 mit der Breite der Tanga-Abtrennung `ca. 3,5 bis 5 cm` und die gleichlautende Beschriftung (Zeilen 16 und 37);
- Schritt 6 mit der halben Schrittbreite `ca. 2,5 cm` und die gleichlautende Beschriftung (Zeilen 20 und 38);
- Schritt 11 mit der Kniekorrektur `0 bis 1 cm` und die gleichlautende Beschriftung (Zeilen 25 und 39);
- die Schritte 9 und 10, in denen die Längen der Beinausschnitte an VT und RT ab der Hüftlinie gemessen und auf die geformten Kurven übertragen werden, sowie Schritt 12 (vordere Innenbeinnaht messen und auf die hintere übertragen) — reine Übertragungen ohne Zuschlag (Zeilen 23, 24 und 26);
- die Modelllänge `z. B. 77 bis 85 cm` und die Beschriftung `neue Modell-Länge` (Zeilen 35 und 40);
- die Beschriftungskette `messen / übertragen / übertragen + ca. 1 cm / wie vorne` außerhalb des Detailkreises (Zeile 41), inhaltsgleich mit der abgebildeten Zeile;
- die Reduktionspfeile `−15 %` und `−5 %` (Zeile 44), die auf `HOF-B1-S501-F02` und `HOF-B1-S501-F03` verweisen;
- die Linienbezeichnungen HüLi, SrLi, KnLi, WaLi, hM, vM und SN sowie das Symbol ♀ am vorderen Hosenausschnitt (Zeilen 34–36 und 43).

Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
