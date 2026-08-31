# Fachlich normalisierte Formeln — S. 86

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/03_modelle_roecke_s40-105/formeln_s86_codex_v2_digital_geprueft.md`
Originaltranskript: `../hofenbitzer_band_1_digital/03_modelle_roecke_s40-105/s86_codex_v2_digital_geprueft.md`
Buchseite: Hofenbitzer, Band 1, S. 86

## HOF-B1-S086-F01 — Hüftweite und Teilmaße

- **Fachlicher Zweck:** Die Hüftweite aus Hüftumfang und gewählter Zugabe sowie die halbe und viertel Hüftweite bestimmen.
- **Quelle:** `formeln_s86_codex_v2_digital_geprueft.md`, Zeile 9; Originaltranskript `s86_codex_v2_digital_geprueft.md`, Zeile 49; Buchseite 86.
- **Originalbezeichnung:** `HüU Hüftumfang + Zugabe = Hüftweite HüW`
- **Normalisierte Bezeichnung:** `hueftweite_faltenrock`

### Buchfassung

```text
| HüU Hüftumfang | 97 | + 2-3 3 = | Hüftweite HüW | 100 | 50 | 25 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU Hüftumfang | 97 | cm |
| `hueftzugabe` | gewählte Zugabe aus `2-3` | 3 | cm |

### Formel und Rechenschritte

```text
hueftweite = hueftumfang + hueftzugabe
            = 97 cm + 3 cm
            = 100 cm

halbe_hueftweite = hueftweite / 2
                  = 100 cm / 2
                  = 50 cm

viertel_hueftweite = hueftweite / 4
                    = 100 cm / 4
                    = 25 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftweite` | Hüftweite HüW | 100 | cm |
| `halbe_hueftweite` | halbe Hüftweite | 50 | cm |
| `viertel_hueftweite` | viertel Hüftweite | 25 | cm |

- **Abhängigkeiten:** `hueftumfang` und die innerhalb des Buchbereichs gewählte `hueftzugabe`.
- **Gültigkeitsbereich:** Konstruktionstabelle des Rundum-Faltenrocks auf S. 86, Größe 38.
- **Technische Randbedingung:** Alle Längen müssen in derselben Einheit vorliegen. Der Bereich `2-3` ist eine Auswahlvorgabe; im Buchbeispiel sind 3 cm gewählt.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zugabebereich und gewählten Wert getrennt führen; Teilmaße erst aus der berechneten Hüftweite bilden.

## HOF-B1-S086-F02 — Taillenweite und Teilmaße

- **Fachlicher Zweck:** Die Taillenweite aus Taillenumfang und gewählter Zugabe sowie die halbe und viertel Taillenweite bestimmen.
- **Quelle:** `formeln_s86_codex_v2_digital_geprueft.md`, Zeile 10; Originaltranskript `s86_codex_v2_digital_geprueft.md`, Zeile 50; Buchseite 86.
- **Originalbezeichnung:** `TaU Taillenumfang + Zugabe = Taillenweite TaW`
- **Normalisierte Bezeichnung:** `taillenweite_faltenrock`

### Buchfassung

```text
| TaU Taillenumfang | 72 | + 1-2 2 = | Taillenweite TaW | 74 | 37 | 18,5 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU Taillenumfang | 72 | cm |
| `taillenzugabe` | gewählte Zugabe aus `1-2` | 2 | cm |

### Formel und Rechenschritte

```text
taillenweite = taillenumfang + taillenzugabe
              = 72 cm + 2 cm
              = 74 cm

halbe_taillenweite = taillenweite / 2
                    = 74 cm / 2
                    = 37 cm

viertel_taillenweite = taillenweite / 4
                      = 74 cm / 4
                      = 18,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenweite` | Taillenweite TaW | 74 | cm |
| `halbe_taillenweite` | halbe Taillenweite | 37 | cm |
| `viertel_taillenweite` | viertel Taillenweite | 18,5 | cm |

- **Abhängigkeiten:** `taillenumfang` und die innerhalb des Buchbereichs gewählte `taillenzugabe`.
- **Gültigkeitsbereich:** Konstruktionstabelle des Rundum-Faltenrocks auf S. 86, Größe 38.
- **Technische Randbedingung:** Alle Längen müssen in derselben Einheit vorliegen. Der Bereich `1-2` ist eine Auswahlvorgabe; im Buchbeispiel sind 2 cm gewählt.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zugabebereich und gewählten Wert getrennt führen; Teilmaße erst aus der berechneten Taillenweite bilden.

## HOF-B1-S086-F03 — Taillenausfall und halber Taillenausfall

- **Fachlicher Zweck:** Den Taillenausfall aus halber Hüftweite und halber Taillenweite sowie dessen Hälfte bestimmen.
- **Quelle:** `formeln_s86_codex_v2_digital_geprueft.md`, Zeile 11; Originaltranskript `s86_codex_v2_digital_geprueft.md`, Zeile 51; Buchseite 86.
- **Originalbezeichnung:** `TaAf Taillenausfall = 1/2 HüW - 1/2 TaW`
- **Normalisierte Bezeichnung:** `taillenausfall_faltenrock`

### Buchfassung

```text
| TaAf Taillenausfall |  |  | 1/2 HüW - 1/2 TaW = | 13 | 6,5 |  |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `halbe_hueftweite` | 1/2 HüW | 50 | cm |
| `halbe_taillenweite` | 1/2 TaW | 37 | cm |

### Formel und Rechenschritte

```text
taillenausfall = halbe_hueftweite - halbe_taillenweite
                = 50 cm - 37 cm
                = 13 cm

halber_taillenausfall = taillenausfall / 2
                       = 13 cm / 2
                       = 6,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenausfall` | Taillenausfall TaAf | 13 | cm |
| `halber_taillenausfall` | Hälfte des Taillenausfalls | 6,5 | cm |

- **Abhängigkeiten:** `halbe_hueftweite` aus `HOF-B1-S086-F01` und `halbe_taillenweite` aus `HOF-B1-S086-F02`.
- **Gültigkeitsbereich:** Konstruktionstabelle des Rundum-Faltenrocks auf S. 86, Größe 38.
- **Technische Randbedingung:** Hüft- und Taillenweite müssen in derselben Einheit und für dieselbe Konstruktion vorliegen.
- **Offene Fragen oder Widersprüche:** Keine; `50 cm - 37 cm = 13 cm` und `13 cm / 2 = 6,5 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Taillenausfall aus den halben Weiten berechnen und die Tabellenhälfte als getrennte Ausgabe führen.

## HOF-B1-S086-F04 — Faltenabstand an der Hüfte

- **Fachlicher Zweck:** Den gleichmäßigen Faltenabstand an der Hüfte aus Hüftweite und Faltenanzahl bestimmen.
- **Quelle:** `formeln_s86_codex_v2_digital_geprueft.md`, Zeilen 17, 22 und 27; Originaltranskript `s86_codex_v2_digital_geprueft.md`, Zeilen 56–62; Buchseite 86.
- **Originalbezeichnung:** `Faltenabstand an der Hüfte (FaA_Hü) = HüW : Faltenanzahl (FaZ)`
- **Normalisierte Bezeichnung:** `faltenabstand_huefte`

### Buchfassung

```text
= HüW : Faltenanzahl (FaZ)
```

```text
= 100 cm : 22
```

```text
= 4,54 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftweite` | HüW | 100 | cm |
| `faltenanzahl` | FaZ | 22 | dimensionslos |

### Formel und Rechenschritte

```text
faltenabstand_huefte = hueftweite / faltenanzahl
                      = 100 cm / 22
                      = 4,545454... cm
Buchwert             = 4,54 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `faltenabstand_huefte` | Faltenabstand FaA_Hü | 4,54 | cm |

- **Abhängigkeiten:** `hueftweite` aus `HOF-B1-S086-F01` und festgelegte `faltenanzahl`.
- **Gültigkeitsbereich:** Rundum-Faltenrock auf S. 86 mit 22 gleichmäßig verteilten Falten.
- **Technische Randbedingung:** `faltenanzahl` muss größer als 0 und ganzzahlig sein. Der exakte Quotient ist für Folgeoperationen vorzuziehen.
- **Offene Fragen oder Widersprüche:** Der Buchwert `4,54 cm` ist auf zwei Dezimalstellen abgeschnitten; kaufmännisch gerundet wären es `4,55 cm`. Eine allgemeine Rundungsregel nennt die Quelle nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern mit voller Genauigkeit rechnen. Den Buchwert nur bei ausdrücklich gewünschter Buchreproduktion durch Abschneiden auf zwei Dezimalstellen erzeugen; die Rundungspolitik bleibt eine spätere technische Entscheidung.

## HOF-B1-S086-F05 — Faltenabstand an der Taille

- **Fachlicher Zweck:** Den gleichmäßigen Faltenabstand an der Taille aus Taillenweite und Faltenanzahl bestimmen.
- **Quelle:** `formeln_s86_codex_v2_digital_geprueft.md`, Zeilen 32, 37 und 42; Originaltranskript `s86_codex_v2_digital_geprueft.md`, Zeilen 64–70; Buchseite 86.
- **Originalbezeichnung:** `Faltenabstand an der Taille (FaA_Ta) = TaW : Faltenanzahl (FaZ)`
- **Normalisierte Bezeichnung:** `faltenabstand_taille`

### Buchfassung

```text
= TaW : Faltenanzahl (FaZ)
```

```text
= 74 cm : 22
```

```text
= 3,36 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenweite` | TaW | 74 | cm |
| `faltenanzahl` | FaZ | 22 | dimensionslos |

### Formel und Rechenschritte

```text
faltenabstand_taille = taillenweite / faltenanzahl
                      = 74 cm / 22
                      = 3,363636... cm
Buchwert             = 3,36 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `faltenabstand_taille` | Faltenabstand FaA_Ta | 3,36 | cm |

- **Abhängigkeiten:** `taillenweite` aus `HOF-B1-S086-F02` und dieselbe `faltenanzahl` wie bei `HOF-B1-S086-F04`.
- **Gültigkeitsbereich:** Rundum-Faltenrock auf S. 86 mit 22 gleichmäßig verteilten Falten.
- **Technische Randbedingung:** `faltenanzahl` muss größer als 0 und ganzzahlig sein. Der exakte Quotient ist für Folgeoperationen vorzuziehen.
- **Offene Fragen oder Widersprüche:** Der Buchwert `3,36 cm` ist auf zwei Dezimalstellen abgeschnitten. In diesem Beispiel entspricht das zugleich der kaufmännischen Rundung; eine allgemeine Rundungsregel nennt die Quelle nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern mit voller Genauigkeit rechnen und die Ausgabe-Rundung als ausdrücklich gewählte technische Regel behandeln.

## HOF-B1-S086-F06 — Falteninhalt aus der Faltentiefe

- **Fachlicher Zweck:** Den Falteninhalt einer Normalfalte als doppelte Faltentiefe bestimmen.
- **Quelle:** `formeln_s86_codex_v2_digital_geprueft.md`, Zeile 47; Originaltranskript `s86_codex_v2_digital_geprueft.md`, Zeile 92; Buchseite 86.
- **Originalbezeichnung:** `FaI = 2 x FaT`
- **Normalisierte Bezeichnung:** `falteninhalt_normalfalte`

### Buchfassung

```text
4. Anschließend wird ein Falteninhalt (FaI = 2 x FaT) markiert.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---|---|
| `faltentiefe` | FaT | nicht angegeben | cm |
| `faktor_falteninhalt` | 2 | 2 | dimensionslos |

### Formel und Rechenschritte

```text
falteninhalt = faktor_falteninhalt * faltentiefe
              = 2 * faltentiefe
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---|---|
| `falteninhalt` | Falteninhalt FaI | `2 x FaT` | cm |

- **Abhängigkeiten:** Gewählte `faltentiefe`.
- **Gültigkeitsbereich:** Markierung der Normalfalten des Rundum-Faltenrocks auf S. 86.
- **Technische Randbedingung:** Die Faltentiefe muss als nichtnegative Länge vorliegen.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Falteninhalt und Faltentiefe als verschiedene Größen führen; der Faktor 2 ist für diese Normalfalte belegt.

## HOF-B1-S086-F07 — Kontrolle der offenen Weite

- **Fachlicher Zweck:** Die erforderliche offene Stoffweite aus Faltenanzahl, Faltentiefe und Hüftweite kontrollieren.
- **Quelle:** `formeln_s86_codex_v2_digital_geprueft.md`, Zeilen 52, 57 und 62; Originaltranskript `s86_codex_v2_digital_geprueft.md`, Zeilen 104–110; Buchseite 86.
- **Originalbezeichnung:** `ofW = FaZ · FaT · 2 + HüW`
- **Normalisierte Bezeichnung:** `offene_weite_faltenrock`

### Buchfassung

```text
ofW = FaZ · FaT · 2 + HüW
```

```text
= 22 · 9,2 cm + 100 cm
```

```text
= 302,4 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `faltenanzahl` | FaZ | 22 | dimensionslos |
| `faltentiefe` | FaT | 9,2 | cm |
| `hueftweite` | HüW | 100 | cm |
| `faktor_falteninhalt` | 2 | 2 | dimensionslos |

### Formel und Rechenschritte

Wörtliche technische Umsetzung der allgemeinen Buchformel:

```text
offene_weite = faltenanzahl * faltentiefe * faktor_falteninhalt
               + hueftweite
             = 22 * 9,2 cm * 2 + 100 cm
             = 504,8 cm
```

Abweichende Rechnung gemäß der gedruckten Einsetzzeile und dem gedruckten Ergebnis:

```text
offene_weite = faltenanzahl * 9,2 cm + hueftweite
             = 22 * 9,2 cm + 100 cm
             = 302,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `offene_weite` | Kontrolle der offenen Weite ofW | 302,4 | cm |

- **Abhängigkeiten:** `faltenanzahl`, gewählte `faltentiefe`, Falteninhalt nach `HOF-B1-S086-F06` und `hueftweite` aus `HOF-B1-S086-F01`.
- **Gültigkeitsbereich:** Rundum-Faltenrock auf S. 86 mit 22 Normalfalten, 9,2 cm Faltentiefe und 100 cm Hüftweite.
- **Technische Randbedingung:** Alle Längen müssen in derselben Einheit vorliegen; Faltenanzahl und Faltentiefe dürfen nicht negativ sein.
- **Offene Fragen oder Widersprüche:** Die allgemeine Buchformel enthält den Faktor `· 2`; mit dem eingesetzten Wert `FaT = 9,2 cm` ergibt sie `504,8 cm`. Die gedruckte Einsetzzeile lässt den Faktor 2 weg und ergibt wie der gedruckte Ergebniswert `302,4 cm`. Ungeklärt ist, ob `9,2 cm` bereits der doppelte Falteninhalt statt der einfachen Faltentiefe bezeichnet oder ob Formel beziehungsweise Einsetzzeile fehlerhaft sind.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis geklärt ist, ob `9,2 cm` `FaT` oder bereits `FaI = 2 × FaT` bezeichnet und welche der beiden Rechnungen gelten soll.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s86_codex_v2_digital_geprueft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 12 | 1 | Leere Tabellenzeile für den gemessenen Bundumfang; weder Werte noch ausführbare Rechenbeziehung vorhanden |
| **Summe** | **1** | **1 unvollständige Kandidatenzeile ausgeschlossen** |
