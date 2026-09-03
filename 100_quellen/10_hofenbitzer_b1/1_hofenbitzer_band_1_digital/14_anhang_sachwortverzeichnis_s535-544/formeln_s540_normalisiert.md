# Fachlich normalisierte Formeln — S. 540

Quelle der Normalisierung: `formeln_s540_digital_geprüft.md`
Originaltranskript: `s540_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 540

## HOF-B1-S540-F01 — Brustbreite aus der ganzen Brustbreite

- **Fachlicher Zweck:** Das halbe Konstruktionsmaß der Brustbreite aus der ganzen gemessenen Brustbreite bestimmen.
- **Quelle:** `formeln_s540_digital_geprüft.md`, Zeile 9; Originaltranskript `s540_digital_geprüft.md`, Zeile 19; Buchseite 540.
- **Originalbezeichnung:** `BrB = gBrB : 2`.
- **Normalisierte Bezeichnung:** `brustbreite_aus_ganzer_brustbreite`

### Buchfassung

```text
| BrB | Brustbreite | Konstruktionsmaß, vorderer Armansatz bis Mitte zwischen den Brustspitzen; BrB = gBrB : 2 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `ganze_brustbreite` | gBrB | variabel | cm |

### Formel und Rechenschritte

```text
brustbreite = ganze_brustbreite / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `brustbreite` | BrB | cm |

- **Abhängigkeiten:** Gemessene gBrB.
- **Gültigkeitsbereich:** Abkürzungs- und Maßdefinition auf S. 540.
- **Technische Randbedingung:** gBrB und BrB müssen dieselbe Einheit verwenden.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als einfache Halbierung ohne zusätzliche Zugabe implementieren.

## HOF-B1-S540-F02 — Brusttiefe aus der ganzen Brusttiefe

- **Fachlicher Zweck:** Die Brusttiefe nach Abzug der Halslochbreite aus der ganzen gemessenen Brusttiefe bestimmen.
- **Quelle:** `formeln_s540_digital_geprüft.md`, Zeile 10; Originaltranskript `s540_digital_geprüft.md`, Zeile 20; Buchseite 540.
- **Originalbezeichnung:** `BrT = gBrT − HlB`.
- **Normalisierte Bezeichnung:** `brusttiefe_aus_ganzer_brusttiefe`

### Buchfassung

```text
| BrT | Brusttiefe | gBrT wird vom 7. HW am Hals vorbei zur Brustspitze gemessen; BrT = gBrT − HlB |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `ganze_brusttiefe` | gBrT | variabel | cm |
| `halslochbreite` | HlB | variabel | cm |

### Formel und Rechenschritte

```text
brusttiefe = ganze_brusttiefe - halslochbreite
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `brusttiefe` | BrT | cm |

- **Abhängigkeiten:** gBrT und HlB; HlB kann nach `HOF-B1-S540-F04` bestimmt werden.
- **Gültigkeitsbereich:** Abkürzungs- und Maßdefinition auf S. 540.
- **Technische Randbedingung:** gBrT wird entsprechend der gedruckten Messbeschreibung vom 7. Halswirbel zur Brustspitze gemessen.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Messgröße gBrT und das abgeleitete Konstruktionsmaß BrT getrennt führen.

## HOF-B1-S540-F03 — Brustweite mit Weitenzugabe

- **Fachlicher Zweck:** Die Brustweite aus Brustumfang und Weitenzugabe bestimmen.
- **Quelle:** `formeln_s540_digital_geprüft.md`, Zeile 15; Originaltranskript `s540_digital_geprüft.md`, Zeile 22; Buchseite 540.
- **Originalbezeichnung:** `BrU + Wzg`.
- **Normalisierte Bezeichnung:** `brustweite_mit_weitenzugabe`

### Buchfassung

```text
| BrW | Brustweite | Brustumfang plus Weitenzugabe (BrU + Wzg) |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustumfang` | BrU | variabel | cm |
| `brust_weitenzugabe` | Wzg | explizite Auswahl | cm |

### Formel und Rechenschritte

```text
brustweite = brustumfang + brust_weitenzugabe
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `brustweite` | BrW | cm |

- **Abhängigkeiten:** BrU und fachlich gewählte Wzg.
- **Gültigkeitsbereich:** Abkürzungs- und Maßdefinition auf S. 540.
- **Technische Randbedingung:** Körpermaß und Zugabe müssen in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Die Auswahl der Wzg ist nicht Teil dieser Formel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Wzg als explizite Eingabe und nicht als versteckte Konstante führen.

## HOF-B1-S540-F04 — Halslochbreite aus dem Halsansatzumfang

- **Fachlicher Zweck:** Die Halslochbreite aus einem Sechstel des Halsansatzumfangs plus 0,5 cm bestimmen.
- **Quelle:** `formeln_s540_digital_geprüft.md`, Zeile 20; Originaltranskript `s540_digital_geprüft.md`, Zeile 32; Buchseite 540.
- **Originalbezeichnung:** `HaU : 6 + 0,5 cm`.
- **Normalisierte Bezeichnung:** `halslochbreite_aus_halsansatzumfang`

### Buchfassung

```text
| HlB | Halslochbreite | Konstruktionsmaß, ist ½ Halsdurchmesser (Breite des Halslochs) HaU : 6 + 0,5 cm |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halsansatzumfang` | HaU | variabel | cm |
| `halsloch_zugabe` | `0,5 cm` | 0,5 | cm |

### Formel und Rechenschritte

```text
halslochbreite = (halsansatzumfang / 6) + 0,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `halslochbreite` | HlB | cm |

- **Abhängigkeiten:** HaU.
- **Gültigkeitsbereich:** Abkürzungs- und Maßdefinition auf S. 540.
- **Technische Randbedingung:** Division durch 6 vor Addition von 0,5 cm.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Divisor und Zugabe als belegte Konstanten sichtbar halten.

## HOF-B1-S540-F05 — Hüftweite mit Weitenzugabe

- **Fachlicher Zweck:** Die Hüftweite aus Hüftumfang und Weitenzugabe bestimmen.
- **Quelle:** `formeln_s540_digital_geprüft.md`, Zeile 25; Originaltranskript `s540_digital_geprüft.md`, Zeile 37; Buchseite 540.
- **Originalbezeichnung:** `HüU + Wzg`.
- **Normalisierte Bezeichnung:** `hueftweite_mit_weitenzugabe`

### Buchfassung

```text
| HüW | Hüftweite | Hüftumfang plus Weitenzugabe für die Hüfte (HüU + Wzg) |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | variabel | cm |
| `hueft_weitenzugabe` | Wzg | explizite Auswahl | cm |

### Formel und Rechenschritte

```text
hueftweite = hueftumfang + hueft_weitenzugabe
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftweite` | HüW | cm |

- **Abhängigkeiten:** HüU und fachlich gewählte Wzg.
- **Gültigkeitsbereich:** Abkürzungs- und Maßdefinition auf S. 540.
- **Technische Randbedingung:** Körpermaß und Zugabe müssen in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Die Auswahl der Wzg ist nicht Teil dieser Formel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Wzg als explizite Eingabe führen.

## HOF-B1-S540-F06 — Rückenbreite aus der ganzen Rückenbreite

- **Fachlicher Zweck:** Das halbe Konstruktionsmaß der Rückenbreite aus der ganzen gemessenen Rückenbreite bestimmen.
- **Quelle:** `formeln_s540_digital_geprüft.md`, Zeile 30; Originaltranskript `s540_digital_geprüft.md`, Zeile 51; Buchseite 540.
- **Originalbezeichnung:** `RüB = gRüB : 2`.
- **Normalisierte Bezeichnung:** `rueckenbreite_aus_ganzer_rueckenbreite`

### Buchfassung

```text
| RüB | Rückenbreite | Konstruktionsmaß, Strecke von hM bis hinteren Armansatz; RüB = gRüB : 2 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `ganze_rueckenbreite` | gRüB | variabel | cm |

### Formel und Rechenschritte

```text
rueckenbreite = ganze_rueckenbreite / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `rueckenbreite` | RüB | cm |

- **Abhängigkeiten:** Gemessene gRüB.
- **Gültigkeitsbereich:** Abkürzungs- und Maßdefinition auf S. 540.
- **Technische Randbedingung:** gRüB und RüB müssen dieselbe Einheit verwenden.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als einfache Halbierung ohne zusätzliche Zugabe implementieren.

## HOF-B1-S540-F07 — Taillenweite mit Weitenzugabe

- **Fachlicher Zweck:** Die Taillenweite aus Taillenumfang und Weitenzugabe bestimmen.
- **Quelle:** `formeln_s540_digital_geprüft.md`, Zeile 35; Originaltranskript `s540_digital_geprüft.md`, Zeile 61; Buchseite 540.
- **Originalbezeichnung:** `TaU + Wzg`.
- **Normalisierte Bezeichnung:** `taillenweite_mit_weitenzugabe`

### Buchfassung

```text
| TaW | Taillenweite | Taillenumfang plus Weitenzugabe an der Taille (TaU + Wzg) |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | variabel | cm |
| `taillen_weitenzugabe` | Wzg | explizite Auswahl | cm |

### Formel und Rechenschritte

```text
taillenweite = taillenumfang + taillen_weitenzugabe
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `taillenweite` | TaW | cm |

- **Abhängigkeiten:** TaU und fachlich gewählte Wzg.
- **Gültigkeitsbereich:** Abkürzungs- und Maßdefinition auf S. 540.
- **Technische Randbedingung:** Körpermaß und Zugabe müssen in derselben Einheit vorliegen.
- **Offene Fragen oder Widersprüche:** Die Auswahl der Wzg ist nicht Teil dieser Formel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Wzg als explizite Eingabe führen.

## HOF-B1-S540-F08 — Vorderlänge aus der ganzen Vorderlänge

- **Fachlicher Zweck:** Die Vorderlänge nach Abzug der Halslochbreite aus der ganzen gemessenen Vorderlänge bestimmen.
- **Quelle:** `formeln_s540_digital_geprüft.md`, Zeile 40; Originaltranskript `s540_digital_geprüft.md`, Zeile 68; Buchseite 540.
- **Originalbezeichnung:** `VL = (gVL − HlB)`.
- **Normalisierte Bezeichnung:** `vorderlaenge_aus_ganzer_vorderlaenge`

### Buchfassung

```text
| VL | Vorderlänge | Konstruktionsmaß, Balancemaß, gVL wird vom 7. Halswirbel am sHa vorbei über die Brustspitze zur Unterkante Taillenband gemessen; VL = (gVL − HlB) |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `ganze_vorderlaenge` | gVL | variabel | cm |
| `halslochbreite` | HlB | variabel | cm |

### Formel und Rechenschritte

```text
vorderlaenge = ganze_vorderlaenge - halslochbreite
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `vorderlaenge` | VL | cm |

- **Abhängigkeiten:** gVL und HlB; HlB kann nach `HOF-B1-S540-F04` bestimmt werden.
- **Gültigkeitsbereich:** Abkürzungs- und Maßdefinition auf S. 540.
- **Technische Randbedingung:** gVL ist entsprechend der gedruckten Messbeschreibung zu erfassen; der Abzug erfolgt danach einmalig.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** gVL und VL getrennt führen und den HlB-Abzug nicht doppelt anwenden.

## Prüfhinweis zu Wiederholungen

Die acht Definitionen wiederholen teilweise Beziehungen aus Maßtabellen und früheren Konstruktionsseiten. S. 540 erweitert ihren Beleg jedoch um allgemeine Mess- und Bedeutungsdefinitionen des Abkürzungsverzeichnisses. Deshalb bleiben sie als seitenlokale Formel-IDs erhalten; frühere Zahlenbeispiele werden nicht dupliziert.
