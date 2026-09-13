# Fachlich normalisierte Formeln — S. 171

Quelle der Normalisierung: `formeln_s171_digital_geprüft.md`
Originaltranskript: `s171_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 171
Extraktionsstand: v2

## HOF-B1-S171-F01 — Mindestweite der halben Taille

- **Fachlicher Zweck:** Die gewünschte halbe Taillenweite der historischen Hose mindestens aus drei Vierteln des Hüftumfangs bestimmen.
- **Quelle:** `formeln_s171_digital_geprüft.md`, Zeile 9; Originaltranskript `s171_digital_geprüft.md`, Zeile 19; Buchseite 171.
- **Originalbezeichnung:** `gewünschte ½ TaW = mind. ¾ HüU`
- **Normalisierte Bezeichnung:** `mindestweite_halbe_taille_historische_hose`

### Buchfassung

```text
- gewünschte ½ TaW = mind. ¾ HüU
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | nicht angegeben | cm |
| `anteil_hueftumfang` | ¾ | 3/4 | dimensionslos |

### Formel und Rechenschritte

```text
mindestweite_halbe_taille = hueftumfang * (3 / 4)
gewuenschte_halbe_taillenweite >= mindestweite_halbe_taille
```

Die technische Ungleichung bildet das gedruckte `mind.` ab; die Buchfassung mit Gleichheitszeichen bleibt unverändert.

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `mindestweite_halbe_taille` | kleinste gewünschte halbe Taillenweite | nicht angegeben | cm |

- **Abhängigkeiten:** Hüftumfang.
- **Gültigkeitsbereich:** Historische Schnittform zu □2 auf S. 171.
- **Technische Randbedingung:** Der Hüftumfang muss positiv sein; alle Längen müssen dieselbe Einheit verwenden.
- **Offene Fragen oder Widersprüche:** Keine für die Mindestbeziehung. Die Quelle gibt keinen konkreten Hüftumfang und keine Auswahlregel für eine größere gewünschte Taillenweite an.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Mindestbedingung prüfen; eine größere gewünschte halbe Taillenweite bleibt eine ausdrücklich zu liefernde Eingabe.

## HOF-B1-S171-F02 — Unbezeichneter Mindestbetrag aus einem Viertel Hüftumfang

- **Fachlicher Zweck:** Den auf zwei Schnittzeichnungen wiederholten Mindestbetrag aus einem Viertel des Hüftumfangs plus 1 cm erhalten, ohne seinen im Extrakt nicht bezeichneten geometrischen Referenten zu erfinden.
- **Quelle:** `formeln_s171_digital_geprüft.md`, Zeilen 19 und 34; Originaltranskript `s171_digital_geprüft.md`, Zeilen 60 und 82; Buchseite 171.
- **Originalbezeichnung:** `mind. ¼ HüU + 1 cm`
- **Normalisierte Bezeichnung:** `unbezeichneter_mindestbetrag_hueftumfang_viertel`

### Buchfassung

```text
- mind. ¼ HüU + 1 cm
```

```text
- mind. ¼ HüU + 1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | nicht angegeben | cm |
| `fester_zuschlag` | 1 cm | 1 | cm |

### Formel und Rechenschritte

```text
unbezeichneter_mindestbetrag = (hueftumfang / 4) + fester_zuschlag
                              = (hueftumfang / 4) + 1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `unbezeichneter_mindestbetrag` | Mindestwert einer in den Zeichnungen nicht bezeichneten Strecke oder Position | nicht angegeben | cm |

- **Abhängigkeiten:** Hüftumfang.
- **Gültigkeitsbereich:** Historische Pluderhose zu □7 und modernisierte Pluderhose zu □8 auf S. 171; beide Zeichnungen tragen denselben Ausdruck.
- **Technische Randbedingung:** Der Hüftumfang muss positiv sein; alle Längen müssen dieselbe Einheit verwenden. Die Rechnung ist ausführbar, darf aber ohne geometrischen Referenten nicht konstruktiv angewendet werden.
- **Offene Fragen oder Widersprüche:** Das extrahierte Textinventar belegt nicht, welche Strecke oder Position mit diesem Mindestbetrag bestimmt wird. Die zweite Buchfassung ist keine bloße Wiederholung: Sie belegt die Anwendung desselben Ausdrucks auch auf der modernisierten Schnittentwicklung.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis der geometrische Referent anhand des Buchbilds oder einer ergänzten Extraktion eindeutig belegt ist.

## HOF-B1-S171-F03 — Unbezeichneter Bereich aus einem Achtel Hüftumfang

- **Fachlicher Zweck:** Den unbezeichneten Wertebereich aus einem Achtel des Hüftumfangs plus 2 bis 3 cm als zwei Grenzen erhalten.
- **Quelle:** `formeln_s171_digital_geprüft.md`, Zeile 24; Originaltranskript `s171_digital_geprüft.md`, Zeile 69; Buchseite 171.
- **Originalbezeichnung:** `⅛ HüU + 2 bis 3 cm`
- **Normalisierte Bezeichnung:** `unbezeichneter_bereich_hueftumfang_achtel`

### Buchfassung

```text
- ⅛ HüU + 2 bis 3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | nicht angegeben | cm |
| `zuschlag_untere_grenze` | 2 cm | 2 | cm |
| `zuschlag_obere_grenze` | 3 cm | 3 | cm |

### Formel und Rechenschritte

```text
unbezeichneter_bereich_untere_grenze = (hueftumfang / 8) + 2 cm
unbezeichneter_bereich_obere_grenze  = (hueftumfang / 8) + 3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `unbezeichneter_bereich_untere_grenze` | kleinere Grenze des unbezeichneten Konstruktionsmaßes | nicht angegeben | cm |
| `unbezeichneter_bereich_obere_grenze` | größere Grenze des unbezeichneten Konstruktionsmaßes | nicht angegeben | cm |

- **Abhängigkeiten:** Hüftumfang und Auswahl eines Zuschlags zwischen 2 cm und 3 cm.
- **Gültigkeitsbereich:** Historische Pluderhose zu □7 auf S. 171.
- **Technische Randbedingung:** Der Hüftumfang muss positiv sein; alle Längen müssen dieselbe Einheit verwenden. Eine spätere Anwendung muss einen Wert innerhalb des belegten Bereichs ausdrücklich wählen.
- **Offene Fragen oder Widersprüche:** Der geometrische Referent des Ergebnisses und die Regel zur Auswahl zwischen 2 cm und 3 cm fehlen im extrahierten Textinventar.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis der geometrische Referent belegt ist; danach beide Grenzen ausgeben und keine unbelegte automatische Auswahl ergänzen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s171_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 14, 29 und 39 | 3 | Maßstabsbeschriftung `Maßstab 1:10`; Verhältnis der Buchzeichnung, keine Konstruktionsberechnung |
| **Summe** | **3** | **3 Maßstabsbeschriftungen ausgeschlossen** |
