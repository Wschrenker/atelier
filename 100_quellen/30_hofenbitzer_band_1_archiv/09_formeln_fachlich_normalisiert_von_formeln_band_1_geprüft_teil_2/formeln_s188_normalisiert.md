# Fachlich normalisierte Formeln — S. 188

Quelle der Normalisierung: `formeln_s188_digital_geprüft.md`
Originaltranskript: `s188_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 188
Extraktionsstand: v2

## HOF-B1-S188-F01 — Brustumfang mit Zugabe und Halbierung

- **Fachlicher Zweck:** Aus Brustumfang und Zugabe die Brustweite und deren Hälfte bestimmen.
- **Quelle:** `formeln_s188_digital_geprüft.md`, Zeile 9; Originaltranskript `s188_digital_geprüft.md`, Zeile 34; Buchseite 188.
- **Originalbezeichnung:** `BrU`, `BrW`, `½`
- **Normalisierte Bezeichnung:** `brustweite_und_halbe_brustweite`

### Buchfassung

```text
| BrU | Brustumfang | 88 | + 2 | BrW 90; ½ = 45 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustumfang` | BrU | 88 | cm |
| `brustweitenzugabe` | Zugabe | 2 | cm |

### Formel und Rechenschritte

```text
brustweite = brustumfang + brustweitenzugabe = 88 cm + 2 cm = 90 cm
halbe_brustweite = brustweite / 2 = 90 cm / 2 = 45 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `brustweite` | BrW | 90 | cm |
| `halbe_brustweite` | ½ BrW | 45 | cm |

- **Abhängigkeiten:** BrU und gewählte Zugabe der PK-1-Konstruktionstabelle.
- **Gültigkeitsbereich:** Enger Oberteil-Grundschnitt für elastische Materialien in PK 1 auf S. 188.
- **Technische Randbedingung:** Umfang und Zugabe müssen in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Keine; beide Druckergebnisse sind rechnerisch konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zuerst die Zugabe addieren, danach die fertige Brustweite halbieren.

## HOF-B1-S188-F02 — Taillenweite ohne Zugabe und Halbierung

- **Fachlicher Zweck:** Die Taillenweite ohne Zugabe übernehmen und halbieren.
- **Quelle:** `formeln_s188_digital_geprüft.md`, Zeile 10; Originaltranskript `s188_digital_geprüft.md`, Zeile 35; Buchseite 188.
- **Originalbezeichnung:** `TaU`, `TaW`, `½`
- **Normalisierte Bezeichnung:** `taillenweite_und_halbe_taillenweite`

### Buchfassung

```text
| TaU | Taillenumfang | 72 | + `---` | TaW 72; ½ = 36 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |
| `taillenweitenzugabe` | `---` | 0 | cm |

### Formel und Rechenschritte

```text
taillenweite = taillenumfang + taillenweitenzugabe = 72 cm + 0 cm = 72 cm
halbe_taillenweite = taillenweite / 2 = 72 cm / 2 = 36 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `taillenweite` | TaW | 72 | cm |
| `halbe_taillenweite` | ½ TaW | 36 | cm |

- **Abhängigkeiten:** TaU der Konstruktionstabelle.
- **Gültigkeitsbereich:** Enger Oberteil-Grundschnitt für elastische Materialien in PK 1 auf S. 188.
- **Technische Randbedingung:** `---` wird nur in dieser Tabellenzeile als keine Zugabe gelesen; daraus wird keine allgemeine Nullregel abgeleitet.
- **Offene Fragen oder Widersprüche:** Keine; die Halbierung ist konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die fehlende Zugabe als expliziten Tabellenwert `0 cm` modellieren, nicht als unbekannten Wert.

## HOF-B1-S188-F03 — Hüftweite ohne Zugabe und Halbierung

- **Fachlicher Zweck:** Aus Hüftumfang und Nullzugabe die Hüftweite und deren Hälfte bestimmen.
- **Quelle:** `formeln_s188_digital_geprüft.md`, Zeile 11; Originaltranskript `s188_digital_geprüft.md`, Zeile 36; Buchseite 188.
- **Originalbezeichnung:** `HüU`, `HüW`, `½`
- **Normalisierte Bezeichnung:** `hueftweite_und_halbe_hueftweite`

### Buchfassung

```text
| HüU | Hüftumfang | 97 | + 0 | HüW 97; ½ = 48,5 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `hueftweitenzugabe` | Zugabe | 0 | cm |

### Formel und Rechenschritte

```text
hueftweite = hueftumfang + hueftweitenzugabe = 97 cm + 0 cm = 97 cm
halbe_hueftweite = hueftweite / 2 = 97 cm / 2 = 48,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hueftweite` | HüW | 97 | cm |
| `halbe_hueftweite` | ½ HüW | 48,5 | cm |

- **Abhängigkeiten:** HüU und Hüftweitenzugabe der Konstruktionstabelle.
- **Gültigkeitsbereich:** Enger Oberteil-Grundschnitt für elastische Materialien in PK 1 auf S. 188.
- **Technische Randbedingung:** Die Nullzugabe bleibt ein expliziter Wert dieser Passformklasse.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Hüftweite vor der Halbierung vollständig bilden.

## HOF-B1-S188-F04 — Rückenbreite mit Zugabe

- **Fachlicher Zweck:** Die Rückenbreite um die Tabellenzugabe erhöhen.
- **Quelle:** `formeln_s188_digital_geprüft.md`, Zeile 16; Originaltranskript `s188_digital_geprüft.md`, Zeile 42; Buchseite 188.
- **Originalbezeichnung:** `RüB`, `RüB+`
- **Normalisierte Bezeichnung:** `rueckenbreite_mit_zugabe`

### Buchfassung

```text
| RüB | Rückenbreite (½) | 16,5 | + 0,1 | RüB+ 16,6 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_rueckenbreite` | RüB | 16,5 | cm |
| `rueckenbreitenzugabe` | Zugabe | 0,1 | cm |

### Formel und Rechenschritte

```text
rueckenbreite_mit_zugabe = halbe_rueckenbreite + rueckenbreitenzugabe
                           = 16,5 cm + 0,1 cm
                           = 16,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `rueckenbreite_mit_zugabe` | RüB+ | 16,6 | cm |

- **Abhängigkeiten:** Halbe RüB und Zugabe der PK-1-Tabelle.
- **Gültigkeitsbereich:** Konstruktionstabelle S. 188.
- **Technische Randbedingung:** Beide Werte sind halbe Breitenmaße in cm.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Zugabe nicht nochmals spiegeln oder verdoppeln.

## HOF-B1-S188-F05 — Armdurchmesser mit Zugabe und Teilwerten

- **Fachlicher Zweck:** ArD+ bilden und seine Viertel- und Drittelanteile bereitstellen.
- **Quelle:** `formeln_s188_digital_geprüft.md`, Zeile 17; Originaltranskript `s188_digital_geprüft.md`, Zeile 43; Buchseite 188.
- **Originalbezeichnung:** `ArD`, `ArD+`, `¼`, `⅓`
- **Normalisierte Bezeichnung:** `armdurchmesser_mit_zugabe_und_teilwerte`

### Buchfassung

```text
| ArD | Armdurchmesser | 9,3 | + 0,3 | ArD+ 9,6; ¼ = 2,4; ⅓ = 3,2 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser` | ArD | 9,3 | cm |
| `armdurchmesserzugabe` | Zugabe | 0,3 | cm |

### Formel und Rechenschritte

```text
armdurchmesser_mit_zugabe = 9,3 cm + 0,3 cm = 9,6 cm
viertel_armdurchmesser = 9,6 cm / 4 = 2,4 cm
drittel_armdurchmesser = 9,6 cm / 3 = 3,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser_mit_zugabe` | ArD+ | 9,6 | cm |
| `viertel_armdurchmesser` | ¼ ArD+ | 2,4 | cm |
| `drittel_armdurchmesser` | ⅓ ArD+ | 3,2 | cm |

- **Abhängigkeiten:** ArD und Zugabe der PK-1-Tabelle.
- **Gültigkeitsbereich:** Konstruktionstabelle S. 188 und die daraus lesbaren Teilwerte.
- **Technische Randbedingung:** Die Teilwerte werden aus ArD+ und nicht aus ArD gebildet.
- **Offene Fragen oder Widersprüche:** Keine; alle drei Ergebnisse sind exakt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** ArD+ einmal bilden und daraus alle Anteile ableiten.

## HOF-B1-S188-F06 — Brustbreite mit Zugabe

- **Fachlicher Zweck:** Die halbe Brustbreite um die Tabellenzugabe erhöhen.
- **Quelle:** `formeln_s188_digital_geprüft.md`, Zeile 18; Originaltranskript `s188_digital_geprüft.md`, Zeile 44; Buchseite 188.
- **Originalbezeichnung:** `BrB`, `BrB+`
- **Normalisierte Bezeichnung:** `brustbreite_mit_zugabe`

### Buchfassung

```text
| BrB | Brustbreite (½) | 18,2 | + 0,6 | BrB+ 18,8 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_brustbreite` | BrB | 18,2 | cm |
| `brustbreitenzugabe` | Zugabe | 0,6 | cm |

### Formel und Rechenschritte

```text
brustbreite_mit_zugabe = 18,2 cm + 0,6 cm = 18,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `brustbreite_mit_zugabe` | BrB+ | 18,8 | cm |

- **Abhängigkeiten:** Halbe BrB und Zugabe der PK-1-Tabelle.
- **Gültigkeitsbereich:** Konstruktionstabelle S. 188.
- **Technische Randbedingung:** Die Zugabe bezieht sich auf die bereits halbe Brustbreite.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Tabellenwert als halbes Breitenmaß erhalten.

## HOF-B1-S188-F07 — Kontrolle der halben Brustweite

- **Fachlicher Zweck:** Die Summe der Brustteilmaße samt Zugaben gegen die halbe Brustweite kontrollieren.
- **Quelle:** `formeln_s188_digital_geprüft.md`, Zeile 19; Originaltranskript `s188_digital_geprüft.md`, Zeile 45; Buchseite 188.
- **Originalbezeichnung:** `Kontrolle`, `Σ = ½ BrU`, `½ BrW`
- **Normalisierte Bezeichnung:** `kontrolle_halbe_brustweite_tabelle`

### Buchfassung

```text
| Kontrolle | Σ = ½ BrU | 44 | + 1 | ½ BrW 45 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_brustteilmass_summe` | Σ = ½ BrU | 44 | cm |
| `zugabensumme` | Zugabe | 1 | cm |
| `halbe_brustweite_soll` | ½ BrW | 45 | cm |

### Formel und Rechenschritte

```text
halbe_brustweite_kontrolle = halbe_brustteilmass_summe + zugabensumme
                            = 44 cm + 1 cm
                            = 45 cm
kontrolle_bestanden = (45 cm == halbe_brustweite_soll)
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `halbe_brustweite_kontrolle` | kontrollierte halbe Brustweite | 45 | cm |
| `kontrolle_bestanden` | Gleichheit mit ½ BrW | wahr | boolesch |

- **Abhängigkeiten:** RüB+, ArD+ und BrB+ der Konstruktionstabelle sowie `HOF-B1-S188-F01`.
- **Gültigkeitsbereich:** Summenkontrolle der PK-1-Konstruktionstabelle S. 188.
- **Technische Randbedingung:** Die Quelle druckt nur die Summen, nicht die vollständige Aufschlüsselung der drei Teilmaße in dieser Zeile.
- **Offene Fragen oder Widersprüche:** Keine; `16,6 + 9,6 + 18,8 = 45,0 cm` bestätigt zusätzlich den Sollwert.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Sowohl die gedruckte Summenrechnung als auch die Summe der drei Tabellenkomponenten prüfen.

## HOF-B1-S188-F08 — Gedruckter Taillenausfall

- **Fachlicher Zweck:** Den Taillenausfall aus gemessener Taillenbreite und halber Taillenweite bestimmen.
- **Quelle:** `formeln_s188_digital_geprüft.md`, Zeile 29; Originaltranskript `s188_digital_geprüft.md`, Zeile 74; Buchseite 188.
- **Originalbezeichnung:** `TaAf Taillenausfall`
- **Normalisierte Bezeichnung:** `taillenausfall_aus_gemessener_taillenbreite`

### Buchfassung

```text
- TaAf Taillenausfall: `gemessene TaB 44,3 − ½ TaW 36 = 8,6`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `gemessene_taillenbreite` | gemessene TaB | 44,3 | cm |
| `halbe_taillenweite` | ½ TaW | 36 | cm |

### Formel und Rechenschritte

```text
taillenausfall_laut_formel = 44,3 cm - 36 cm = 8,3 cm
gedrucktes_ergebnis = 8,6 cm
abweichung = 8,6 cm - 8,3 cm = 0,3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `taillenausfall_laut_formel` | rechnerisches Ergebnis der gedruckten Operanden | 8,3 | cm |
| `gedruckter_taillenausfall` | gedrucktes Ergebnis | 8,6 | cm |

- **Abhängigkeiten:** Gemessene TaB und `HOF-B1-S188-F02` für ½ TaW.
- **Gültigkeitsbereich:** Vorberechnungsfeld des engen Oberteil-Grundschnitts S. 188.
- **Technische Randbedingung:** Beide Wege müssen bis zur Quellenklärung getrennt erhalten bleiben.
- **Offene Fragen oder Widersprüche:** Die gedruckte Subtraktion ist falsch: `44,3 − 36 = 8,3`, nicht `8,6`. Es ist nicht belegt, ob ein Operand oder das Ergebnis fehlerhaft ist.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bevor Quelle oder fachliche Entscheidung den gültigen Wert festlegt.

## HOF-B1-S188-F09 — Hüftfehlbetrag

- **Fachlicher Zweck:** Den Hüftfehlbetrag als Differenz der gemessenen Hüftbreite zur halben Soll-Hüftweite bestimmen.
- **Quelle:** `formeln_s188_digital_geprüft.md`, Zeile 30; Originaltranskript `s188_digital_geprüft.md`, Zeile 75; Buchseite 188.
- **Originalbezeichnung:** `HüFb Hüftfehlbetrag`
- **Normalisierte Bezeichnung:** `hueftfehlbetrag`

### Buchfassung

```text
- HüFb Hüftfehlbetrag: `gemessene HüB 43,8 − ½ HüW 48,5 = −4,7`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `gemessene_hueftbreite` | gemessene HüB | 43,8 | cm |
| `halbe_hueftweite` | ½ HüW | 48,5 | cm |

### Formel und Rechenschritte

```text
hueftfehlbetrag = gemessene_hueftbreite - halbe_hueftweite
                 = 43,8 cm - 48,5 cm
                 = -4,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hueftfehlbetrag` | vorzeichenbehaftete Differenz | −4,7 | cm |

- **Abhängigkeiten:** Gemessene HüB und `HOF-B1-S188-F03` für ½ HüW.
- **Gültigkeitsbereich:** Vorberechnungsfeld des engen Oberteil-Grundschnitts S. 188.
- **Technische Randbedingung:** Das Vorzeichen bleibt erhalten; die spätere Verteilung wird getrennt behandelt.
- **Offene Fragen oder Widersprüche:** Keine; die Rechnung ist konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Differenz vorzeichenbehaftet speichern und nicht automatisch in einen Betrag umwandeln.

## HOF-B1-S188-F10 — Mehrweite im Armloch

- **Fachlicher Zweck:** Die vorhandene Armlochmehrweite aus vorderem und hinterem Armlochumfang abzüglich Armloch-Rundungsmaß bestimmen.
- **Quelle:** `formeln_s188_digital_geprüft.md`, Zeile 35; Originaltranskript `s188_digital_geprüft.md`, Zeile 77; Buchseite 188.
- **Originalbezeichnung:** `Mehrweite im Armloch`
- **Normalisierte Bezeichnung:** `armlochmehrweite_ist`

### Buchfassung

```text
- Mehrweite im Armloch: `vAlU + hAlU − AraU = [leer]`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderer_armlochumfang` | vAlU | nicht angegeben | cm |
| `hinterer_armlochumfang` | hAlU | nicht angegeben | cm |
| `armloch_rundungsmass` | AraU | nicht angegeben | cm |

### Formel und Rechenschritte

```text
armlochmehrweite_ist = vorderer_armlochumfang + hinterer_armlochumfang - armloch_rundungsmass
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `armlochmehrweite_ist` | vorhandene Mehrweite im Armloch | leer | cm |

- **Abhängigkeiten:** Am fertigen Grundschnitt gemessene Werte vAlU, hAlU und AraU.
- **Gültigkeitsbereich:** Nur Oberteile mit Brustabnäher laut S. 188.
- **Technische Randbedingung:** Alle drei Messwerte müssen am selben Schnittstand und in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Kein Zahlenbeispiel; die symbolische Beziehung ist vollständig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Kontrollrechnung nach der Geometrie ausführen, nicht als vorab bekannte Eingabe.

## HOF-B1-S188-F11 — Sollwert und Toleranz der Armlochmehrweite

- **Fachlicher Zweck:** Den Sollwert der Armlochmehrweite aus der doppelten Armlochtiefenzugabe und den gedruckten Toleranzbereich bilden.
- **Quelle:** `formeln_s188_digital_geprüft.md`, Zeile 36; Originaltranskript `s188_digital_geprüft.md`, Zeile 78; Buchseite 188.
- **Originalbezeichnung:** `Sollwert der Mehrweite`
- **Normalisierte Bezeichnung:** `armlochmehrweite_soll_und_toleranz`

### Buchfassung

```text
- Sollwert der Mehrweite: `2 · Zugabe zur AlT (Toleranz +2 cm bis −1 cm) = [leer]`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefenzugabe` | Zugabe zur AlT | 0,5 | cm |
| `untere_toleranz` | −1 cm | −1 | cm |
| `obere_toleranz` | +2 cm | 2 | cm |

### Formel und Rechenschritte

```text
armlochmehrweite_soll = 2 * armlochtiefenzugabe
                       = 2 * 0,5 cm
                       = 1,0 cm
armlochmehrweite_min = armlochmehrweite_soll - 1 cm = 0,0 cm
armlochmehrweite_max = armlochmehrweite_soll + 2 cm = 3,0 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `armlochmehrweite_soll` | Sollwert | 1,0 | cm |
| `armlochmehrweite_min` | untere Grenze nach −1 cm | 0,0 | cm |
| `armlochmehrweite_max` | obere Grenze nach +2 cm | 3,0 | cm |

- **Abhängigkeiten:** Zugabe zur AlT aus der Konstruktionstabelle und `HOF-B1-S188-F10` als Istwert.
- **Gültigkeitsbereich:** Nur Oberteile mit Brustabnäher laut S. 188.
- **Technische Randbedingung:** Die Grenzen sind nach Ergebnisgröße benannt, obwohl das Buch die Toleranz in der Reihenfolge `+2 cm bis −1 cm` druckt.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine Auswahl- oder Eingriffsregel innerhalb des Toleranzbereichs.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Sollwert und beide Grenzen getrennt liefern; den Istwert gegen das geschlossene Intervall prüfen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s188_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 24 | 1 | Die Balance `3,7` wird ohne Korrektur unverändert als `3,7` übernommen; Tabellen- und Kontrollwert ohne neue Rechenbeziehung |
| **Summe** | **1** | **1 unveränderte Tabellenübernahme ausgeschlossen** |
