# Fachlich normalisierte Formeln — S. 506

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s506.md`
Originaltranskript: `s506.md`
Buchseite: Hofenbitzer, Band 1, S. 506

Die Seite eröffnet den Abschnitt „Bade- und Unterwäsche: Slips, Pants, Shorts" und führt den **Grundschnitt Damenslip**, der laut `□1` „mit vier Körpermaßen konstruiert" wird (DOB-Größe 38): TaU 72 cm, HüU 97 cm, SiH 26 cm, HüT 21 cm. Aus diesem Grundschnitt entwickelt dieselbe Seite die Modellvarianten jugendlicher Slip, Tanga und String. Die extrahierten Kandidatenzeilen stammen aus den Konstruktionsschritten 2, 3, 5 und 13, aus den Beschriftungen der Grundkonstruktion `□2`, aus dem Beschreibungstext zu `□4+5` sowie aus den Beschriftungen und Schnittteil-Stempeln der Modellvarianten `□3` bis `□5`.

Die vier Formelblöcke dieser Datei gelten zugleich für den **Grundschnitt Herrenslip auf S. 507**. Das Buch erklärt dort ausdrücklich: „Die Konstruktion ist ähnlich wie für den Damenslip. Hier werden nur die Unterschiede beschrieben." Die Zeichnung `□7` wiederholt drei der vier Beziehungen wortgleich mit einem eigenen Maßsatz (Unisex-Größe S, Wäschegröße 4: HüU 96 cm, SiH 25 cm). Diese Wiederholungen sind nach der Regel aus `V3-J05` als Belege in den Blöcken unten geführt und erhalten keine eigenen IDs; ihr Rechenkontext ist jeweils getrennt ausgewiesen. Für S. 507 wurde deshalb keine eigene Normalisierungsdatei angelegt.

## HOF-B1-S506-F01 — Verlängerung über die Sitzhöhe hinaus

- **Fachlicher Zweck:** Die senkrechte Grundlinie oberhalb der abgetragenen Sitzhöhe um einen aus dem Hüftumfang abgeleiteten Betrag verlängern und damit die obere Begrenzung der Slipkonstruktion festlegen.
- **Quelle:** `formeln_s506.md`, Zeile 9; Originaltranskript `s506.md`, Zeile 19 (Schritt 2); Buchseite 506. Zeichnungsbeleg Damenslip: `formeln_s506.md`, Zeile 26 (`s506.md`, Zeile 42, `□2`). Zeichnungsbeleg String: `formeln_s506.md`, Zeile 48 (`s506.md`, Zeile 72). Zeichnungsbeleg Herrenslip: `formeln_s507.md`, Zeile 11 (`s507.md`, Zeile 48, `□7`).
- **Originalbezeichnung:** `HüU : 10 − 1 cm`
- **Normalisierte Bezeichnung:** `verlaengerung_ueber_sitzhoehe`

### Buchfassung

```text
2. Um HüU : 10 − 1 cm verlängern.
```

```text
- `HüU :10 − 1 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 (Damenslip) beziehungsweise 96 (Herrenslip) | cm |
| `teiler` | `: 10` | 10 | dimensionslos |
| `abzug` | `1 cm` | 1 | cm |

### Formel und Rechenschritte

```text
verlaengerung = (hueftumfang / 10) - abzug

Buchwerte Damenslip (HüU = 97 cm):
verlaengerung = (97 cm / 10) - 1 cm = 9,7 cm - 1 cm = 8,7 cm

Buchwerte Herrenslip S. 507 (HüU = 96 cm):
verlaengerung = (96 cm / 10) - 1 cm = 9,6 cm - 1 cm = 8,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `verlaengerung` | Verlängerung der Senkrechten oberhalb der Sitzhöhe | 8,7 (Damenslip) / 8,6 (Herrenslip) | cm |

- **Abhängigkeiten:** HüU aus der Maßtabelle `□1`. Vorausgehend Schritt 1: „Auf der Senkrechten SiH abtragen" — eine direkte Abtragung des Körpermaßes ohne Rechenoperation.
- **Gültigkeitsbereich:** Grundkonstruktion Damenslip, Schritt 2; übernommen für String (`□5`) und Herrenslip (`□7`).
- **Technische Randbedingung:** Das Buch druckt für diesen Schritt kein Ergebnis; die Zahlenwerte sind Rechenkontext aus dem gedruckten Maßsatz und keine Buchangaben. Der Betrag wird **auf** die Sitzhöhe aufgesetzt, ersetzt sie also nicht.
- **Offene Fragen oder Widersprüche:** Keine. Schritttext und alle drei Zeichnungsbeschriftungen stimmen wortgleich überein.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Abzug als festen Wert `1 cm` führen. Die Gesamthöhe der Senkrechten ab der Grundlinie ergibt sich technisch als `sitzhoehe + verlaengerung`; diese Summe ist im Buch nicht ausgeschrieben.

## HOF-B1-S506-F02 — Abtragung der halben Hüftbreite

- **Fachlicher Zweck:** Auf einer der abgewinkelten Linien die Breite des Slips aus dem Hüftumfang abtragen und damit die seitliche Begrenzung festlegen.
- **Quelle:** `formeln_s506.md`, Zeile 10; Originaltranskript `s506.md`, Zeile 20 (Schritt 3); Buchseite 506. Zeichnungsbeleg Damenslip: `formeln_s506.md`, Zeile 27 (`s506.md`, Zeile 43, `□2`, mit dem gewählten Abzug `2 cm`). Zeichnungsbeleg String: `formeln_s506.md`, Zeile 48 (`s506.md`, Zeile 72). Zeichnungsbeleg Herrenslip: `formeln_s507.md`, Zeile 9 (`s507.md`, Zeile 46, `□7`).
- **Originalbezeichnung:** Schritttext und String `HüU : 4 − 1 bis 2 cm`; Zeichnung `□2` `HüU :4 − 2 cm`.
- **Normalisierte Bezeichnung:** `slipbreite_aus_hueftumfang`

### Buchfassung

```text
3. Linien abwinkeln. Auf einer der Linien HüU : 4 − 1 bis 2 cm abtragen
```

```text
- `HüU :4 − 2 cm`
```

```text
String: `HüU :4 − 1 bis 2 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 (Damenslip) beziehungsweise 96 (Herrenslip) | cm |
| `teiler` | `: 4` | 4 | dimensionslos |
| `abzug` | `1 bis 2 cm` | 1 bis 2 | cm |

### Formel und Rechenschritte

```text
slipbreite = (hueftumfang / 4) - abzug
mit abzug aus dem Bereich 1 cm bis 2 cm

Buchwerte Damenslip (HüU = 97 cm):
slipbreite = (97 cm / 4) - abzug = 24,25 cm - (1 bis 2) cm = 23,25 bis 22,25 cm

Gewählter Wert der Zeichnung □2 (abzug = 2 cm):
slipbreite = 24,25 cm - 2 cm = 22,25 cm

Buchwerte Herrenslip S. 507 (HüU = 96 cm):
slipbreite = (96 cm / 4) - abzug = 24 cm - (1 bis 2) cm = 23 bis 22 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `slipbreite` | auf der abgewinkelten Linie abzutragende Breite | 22,25 (Damenslip, Zeichnung) | cm |

- **Abhängigkeiten:** HüU aus der Maßtabelle `□1`; die abzuwinkelnden Linien entstehen aus `HOF-B1-S506-F01`.
- **Gültigkeitsbereich:** Grundkonstruktion Damenslip, Schritt 3; übernommen für String (`□5`) und Herrenslip (`□7`).
- **Technische Randbedingung:** Der Schritttext sagt „Auf **einer** der Linien"; welche der beiden abgewinkelten Linien gemeint ist, geht nur aus der Zeichnung hervor. Der Abzug ist ein Bereich, kein fester Wert.
- **Offene Fragen oder Widersprüche:** Keine im Sinne eines Widerspruchs. Die Zeichnung `□2` des Damenslips setzt mit `− 2 cm` die obere Bereichsgrenze ein, ohne dass das Buch eine Auswahlregel nennt; String (`□5`) und Herrenslip (`□7`) beschriften weiterhin den vollen Bereich `− 1 bis 2 cm`. Der gewählte Wert ist deshalb als Beispielwahl ausgewiesen und nicht zur Regel erhoben.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Abzug als Parameter mit dem Bereich `1 bis 2 cm` und der Vorgabe `2 cm` (Buchbeispiel `□2`) führen. Nicht mit der Vorderhosenbreite `¼ HüU − 1 cm` der Hosenkonstruktionen zusammenlegen: Bezugsgröße und Konstruktionszweck sind verschieden.

## HOF-B1-S506-F03 — Abtragung auf der oberen Linie aus dem Taillenumfang

- **Fachlicher Zweck:** Auf der oberen Linie der Konstruktion die aus dem Taillenumfang abgeleitete Strecke abtragen und damit die Bundweite der Schnitthälfte festlegen.
- **Quelle:** `formeln_s506.md`, Zeile 15; Originaltranskript `s506.md`, Zeile 22 (Schritt 5); Buchseite 506. Zeichnungsbeleg Damenslip: `formeln_s506.md`, Zeile 25 (`s506.md`, Zeile 41, `□2`). Zeichnungsbeleg String: `formeln_s506.md`, Zeile 46 (`s506.md`, Zeile 70).
- **Originalbezeichnung:** `TaU : 4`
- **Normalisierte Bezeichnung:** `bundabtragung_aus_taillenumfang`

### Buchfassung

```text
5. Auf oberer Linie TaU : 4 abtragen.
```

```text
- `TaU :4`
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |
| `teiler` | `: 4` | 4 | dimensionslos |

### Formel und Rechenschritte

```text
bundabtragung = taillenumfang / 4

Buchwerte Damenslip (TaU = 72 cm):
bundabtragung = 72 cm / 4 = 18 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `bundabtragung` | auf der oberen Linie abzutragende Strecke | 18 | cm |

- **Abhängigkeiten:** TaU aus der Maßtabelle `□1`. Die obere Linie entsteht aus `HOF-B1-S506-F01`.
- **Gültigkeitsbereich:** Grundkonstruktion Damenslip, Schritt 5; übernommen für den String (`□5`).
- **Technische Randbedingung:** Das Buch druckt kein Ergebnis; der Wert `18 cm` ist Rechenkontext. Eine Bewegungs- oder Materialzugabe nennt der Schritt nicht — anders als beim elastischen Leggings-Bund gibt es hier keine prozentuale Reduzierung.
- **Abgrenzung — Herrenslip:** Der Herrenslip auf S. 507 wird ausdrücklich „mit zwei Körpermaßen konstruiert" (HüU und SiH) und führt keinen TaU. Die Beziehung `TaU : 4` fehlt daher in den Beschriftungen von `□7` folgerichtig; sie ist einer der Unterschiede, die der Vergleichssatz „Hier werden nur die Unterschiede beschrieben" abdeckt. Der Herrenslip legt die obere Begrenzung stattdessen über die direkten Werte `2 cm` (Schritt 5, von P3 nach links) und `20 cm` (Schritt 6, von P5 nach unten) fest; beides sind feste Einzelwerte ohne Rechenoperation.
- **Offene Fragen oder Widersprüche:** Keine. Schritttext und beide Zeichnungsbeschriftungen stimmen überein.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als reine Viertelung ohne Zugabe implementieren. Der Wert ist die Weite der Schnitthälfte an der oberen Linie, nicht der halbe oder volle Umfang.

## HOF-B1-S506-F04 — Symmetrische Abtragung der Schrittbreite

- **Fachlicher Zweck:** Unten an der linken Senkrechten die Schrittbreite festlegen, indem nach oben und nach unten jeweils derselbe aus dem Hüftumfang abgeleitete Betrag abgetragen wird.
- **Quelle:** `formeln_s506.md`, Zeile 20; Originaltranskript `s506.md`, Zeile 30 (Schritt 13); Buchseite 506. Zeichnungsbeleg Damenslip: `formeln_s506.md`, Zeile 28 (`s506.md`, Zeile 44, `□2`). Zeichnungsbeleg String: `formeln_s506.md`, Zeile 48 (`s506.md`, Zeile 72). Zeichnungsbeleg Herrenslip: `formeln_s507.md`, Zeile 11 (`s507.md`, Zeile 48, `□7`).
- **Originalbezeichnung:** `HüU : 40`
- **Normalisierte Bezeichnung:** `schrittabtragung_aus_hueftumfang`

### Buchfassung

```text
13. Unten an der linken Senkrechten um HüU : 40 nach oben und nach unten abtragen und wie an den Skizzen bemaßt abwinkeln.
```

```text
- `HüU :40`
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 (Damenslip) beziehungsweise 96 (Herrenslip) | cm |
| `teiler` | `: 40` | 40 | dimensionslos |

### Formel und Rechenschritte

```text
schrittabtragung = hueftumfang / 40

Buchwerte Damenslip (HüU = 97 cm):
schrittabtragung = 97 cm / 40 = 2,425 cm

Buchwerte Herrenslip S. 507 (HüU = 96 cm):
schrittabtragung = 96 cm / 40 = 2,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `schrittabtragung` | Abtragung nach oben und ebenso nach unten an der linken Senkrechten | 2,425 (Damenslip) / 2,4 (Herrenslip) | cm |

- **Abhängigkeiten:** HüU aus der Maßtabelle `□1`.
- **Gültigkeitsbereich:** Grundkonstruktion Damenslip, Schritt 13; übernommen für String (`□5`) und Herrenslip (`□7`). Zu `□4+5` hält das Buch fest, dass beim String „auch die Schrittnaht … schmaler" ist; ein abweichender Rechenweg ist dafür nicht gedruckt.
- **Technische Randbedingung:** Der Betrag wird **zweimal** abgetragen, nach oben und nach unten. Die Gesamtstrecke beträgt technisch `2 * schrittabtragung`, beim Damenslip also 4,85 cm; diese Summe ist im Buch nicht ausgeschrieben. Das anschließende Abwinkeln „wie an den Skizzen bemaßt" und die runde Formung der Schrittnaht (Schritt 14, `ca. 1 cm`) sind Linienkonstruktionen und von dieser Strecke zu trennen.
- **Offene Fragen oder Widersprüche:** Keine im Rechenweg. Der Schritttext verweist für das Abwinkeln auf die Skizzenbemaßung; welche der Beschriftungen dort gemeint ist, sagt der Text nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Wert einmal berechnen und symmetrisch nach oben und unten anwenden. Nicht runden: `97 / 40` ist mit 2,425 cm exakt darstellbar, eine Rundungsregel nennt die Quelle nicht.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 33 | 1 | `3 bis 4 cm` / `ca. 1 cm` (2×) — direkte Bemaßungen der Grundkonstruktion `□2` (Schritt 14) ohne benannte Eingabe und Rechenoperation |
| 38 | 1 | Beschreibungstext zu `□4+5` über das schmale, bändchenförmige RT und die schmalere Schrittnaht des Strings — qualitative Modellbeschreibung ohne Rechenbeziehung |
| 43 | 1 | `Jugendlicher Slip VT 1× G38` / `Jugendlicher Slip RT 1× G38` — Schnittteil-Stempel |
| 44 | 1 | `Slip G38 1× Schritt-Futter` — Schnittteil-Stempel |
| 45 | 1 | `ca. 8 cm` (2×) / `3 bis 5 cm` / `ca. 3 cm` (2×) sowie `SN`, `vM`, `hM` — direkte Bemaßungen und Linienbezeichnungen des jugendlichen Slips |
| 47 | 1 | String: `ca. 9 cm` / `ca. 6 cm` / `ca. 0,7 cm` / `1,5 cm` / `je 1,5 cm` / `½` (2×) — direkte Bemaßungen sowie zwei Halbierungsmarken ohne Bezugsstrecke |
| **Summe** | **6** | **2 Bemaßungszeilen der Grundkonstruktion und Modellvarianten + 1 qualitative Beschreibung + 2 Schnittteil-Stempel + 1 gemischte String-Bemaßungszeile** |

Zu den Schnittteil-Stempeln: `1×` ist eine Stückzahlangabe und `G38` die Größe. Sie werden wie in `V3-J01` bis `V3-S02` nicht als Rechenfaktoren geführt.

Zu den Halbierungsmarken in Zeile 47: Die beiden `½`-Marken der String-Zeichnung erhalten hier **keine** eigene ID, anders als die Marken auf S. 497 (`HOF-B1-S497-F04`, Status `offen`). Der Unterschied ist belegt: Auf S. 497 gibt es mit Schritt 5 („Hilfslinien von Halbierungen zu P3 und P4 zeichnen") einen Schritttext, der das Halbieren überhaupt als Konstruktionsschritt benennt; auf S. 506 nennt kein Schritt und keine Modellbeschreibung eine Halbierung, und die Marken stehen innerhalb einer Sammelzeile direkter Bemaßungen. Die Stelle bleibt als Prüfstelle vermerkt.

Zum jugendlichen Slip in Zeile 45: Der Beschreibungstext (`s506.md`, Zeile 56) nennt die Vertiefungen „ab der Grundlinie von P7 ca. 7 cm und ab P11 ca. 8 cm", die Zeichnung `□3` beschriftet dagegen zweimal `ca. 8 cm`. Beide Angaben sind direkte Werte und damit ohnehin ausgeschlossen; die Abweichung ist gedruckt und wird hier nur festgehalten, nicht ausgeglichen.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s506.md` enthält weitere rechenfähige oder bemaßte Angaben, die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen und deshalb nicht als Buchfassungen ergänzt wurden:

- die Maßtabelle `□1` mit TaU 72 cm, HüU 97 cm, SiH 26 cm und HüT 21 cm (Zeilen 11–14) — Eingaben von `HOF-B1-S506-F01` bis `F04`;
- Schritt 1 (`SiH` auf der Senkrechten abtragen) und Schritt 6 (`HüT` an der rechten Senkrechten nach unten abtragen und mit P5 verbinden) — direkte Abtragungen der Körpermaße (Zeilen 18 und 23);
- die Schritte 7 bis 12 mit den Verweisen „wie bemaßt" und „wie an den Skizzen bemaßt", der Parallelenabstand `1,5 cm` (Schritt 10) und die Weitermessung `1,5 bis 2 cm` (Schritt 11) (Zeilen 24–29);
- Schritt 14 (`ca. 1 cm` nach oben beziehungsweise unten) sowie die Schritte 15 bis 17 zu Hilfslinien, Beinausschnitten und der Zwickel-/Schrittfutterbegrenzung (Zeilen 31–34);
- die Beschriftungen der Grundkonstruktion `5 bis 7 cm`, `6 bis 8 cm`, `2 cm`, `2 bis 7 cm` (Länge der SN, Schritt 8), `je 1,5 cm`, `ca. 7 cm` und `½` (Zeilen 46–50);
- die Nahtzugabenbreite `0,5 bis 1 cm` sowie die Vertiefungen und Seitennahtlängen von jugendlichem Slip (`ca. 7 cm`, `ca. 8 cm`, `3 bis 5 cm`) und Tanga (`ca. 8 cm`, `ca. 9 cm`, `ca. 1 bis 2 cm`) (Zeilen 54, 56 und 58);
- die Linienbezeichnungen VT, RT, vM, hM, SN, HüT und SiH (Zeilen 40 und 45).

Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.

## Prüfhinweis zu S. 507 (Herrenslip)

Für S. 507 wurde nach der Regel gegen leere Ausgabedateien keine eigene Normalisierungsdatei angelegt: Die Seite erzeugt im verbindlichen Extrakt keine eigenständige Rechenformel. Von ihren sechs Kandidatenzeilen sind zwei in den Blöcken oben als Zeichnungsbelege abgebildet (`formeln_s507.md`, Zeilen 9 und 11), vier sind ausgeschlossen:

| Extraktzeile in `formeln_s507.md` | Anzahl | Ausschlussgrund |
|---|---:|---|
| 10 | 1 | `ca. 6 bis 7 cm` / `½` / `ca. 1 cm` (3×) / `3 cm` / `1 cm` / `6 bis 8 cm` / `5 bis 6 cm` — direkte Bemaßungen von `□7` und eine Halbierungsmarke ohne Bezugsstrecke |
| 12 | 1 | Formung VT: `4 bis 5 cm` / `8 bis 9 cm` / `+ ca. 0,7 cm` (2×) / `ca. 2 cm` — direkte Öffnungs- und Ausstellungswerte der Schritte 18 bis 22 |
| 13 | 1 | `3 bis 4 cm` (2×) sowie `Herrenslip sVT 2×-p G4`, `Herrenslip RT 1× G4`, `Herrenslip Einsatz 4×-p G4` — Bemaßung und Schnittteil-Stempel von `□8` |
| 14 | 1 | `Herrenslip sVT 2×-p G4`, `Herrenslip sRT 2×-p G4` (2×), `Herrenslip Einsatz 4×-p G4` — Schnittteil-Stempel von `□9` |
| **Summe** | **4** | **2 Bemaßungszeilen + 2 Zeilen mit Schnittteil-Stempeln** |

Weitere Angaben von `s507.md` liegen nicht als Kandidatenzeilen vor und wurden nicht ergänzt: die Maßtabelle `□7` mit HüU 96 cm und SiH 25 cm (Zeilen 11–12), die abweichenden Schritte 5 (`2 cm` von P3 nach links) und 6 (`20 cm` von P5 nach unten) (Zeilen 18–19), der Hinweis „P7 bis P10 sowie P17 können beim Herrenslip entfallen" (Zeile 21), die Schritte 17 bis 24 zur Formung des Vorderteils mit `3 cm` Einschnittlinie, `ca. 2 cm` Öffnung und `ca. 0,7 cm` Ausstellung (Zeilen 25–35) sowie die Angabe, dass die Bundansatzlänge „derselben Länge wie die Länge der Ansatznaht am Slip" entspricht (Zeile 37) — eine Gleichsetzung ohne bezifferte Rechenoperation.
