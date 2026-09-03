# Fachlich normalisierte Formeln — S. 535

Quelle der Normalisierung: `formeln_s535_digital_geprüft.md`
Originaltranskript: `s535_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 535

## HOF-B1-S535-F01 — Armdurchmesser mit Zugabe und Halbwert

- **Fachlicher Zweck:** Den Armdurchmesser um eine gewählte Zugabe erweitern und den halben Konstruktionswert bereitstellen.
- **Quelle:** `formeln_s535_digital_geprüft.md`, Zeile 9; Originaltranskript `s535_digital_geprüft.md`, Zeile 47; Buchseite 535.
- **Originalbezeichnung:** `ArD + Zugabe = ArD+; ½`.
- **Normalisierte Bezeichnung:** `armdurchmesser_mit_zugabe_und_halbwert`

### Buchfassung

```text
| ArD | Armdurchmesser + Zugabe | ArD+; ½ |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser` | ArD | variabel | cm |
| `armdurchmesser_zugabe` | Zugabe | explizite Auswahl | cm |

### Formel und Rechenschritte

```text
armdurchmesser_mit_zugabe = armdurchmesser + armdurchmesser_zugabe
halber_armdurchmesser_mit_zugabe = armdurchmesser_mit_zugabe / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `armdurchmesser_mit_zugabe` | ArD+ | cm |
| `halber_armdurchmesser_mit_zugabe` | ½ ArD+ | cm |

- **Abhängigkeiten:** ArD und die fachlich gewählte Zugabe.
- **Gültigkeitsbereich:** Leeres Konstruktionsformular für ein Shirt auf S. 535.
- **Technische Randbedingung:** Erst die Zugabe zum ganzen Armdurchmesser addieren, danach halbieren.
- **Offene Fragen oder Widersprüche:** Das Formular nennt keinen Zugabewert und keine Auswahlregel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ganze und halbe Größe getrennt ausgeben; die Zugabe als Pflichtparameter führen.

## HOF-B1-S535-F02 — Brustpunktabstand mit Zugabe

- **Fachlicher Zweck:** Den Brustpunktabstand aus einem Zehntel des Brustumfangs und einer gewählten Zugabe berechnen.
- **Quelle:** `formeln_s535_digital_geprüft.md`, Zeile 10; Originaltranskript `s535_digital_geprüft.md`, Zeile 48; Buchseite 535.
- **Originalbezeichnung:** `Brustpunktabstand = BrU/10 + Zugabe`.
- **Normalisierte Bezeichnung:** `brustpunktabstand_mit_zugabe`

### Buchfassung

```text
| BrPA | Brustpunktabstand = BrU/10 + Zugabe | BrPA+ |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustumfang` | BrU | variabel | cm |
| `brustpunktabstand_zugabe` | Zugabe | explizite Auswahl | cm |

### Formel und Rechenschritte

```text
brustpunktabstand_mit_zugabe = (brustumfang / 10) + brustpunktabstand_zugabe
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `brustpunktabstand_mit_zugabe` | BrPA+ | cm |

- **Abhängigkeiten:** BrU und die fachlich gewählte Zugabe.
- **Gültigkeitsbereich:** Leeres Konstruktionsformular für ein Shirt auf S. 535.
- **Technische Randbedingung:** Die Division durch 10 erfolgt vor der Addition der Zugabe.
- **Offene Fragen oder Widersprüche:** Das Formular nennt keinen Zugabewert und keine Auswahlregel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Divisor 10 als belegte Konstante und die Zugabe als gesonderte Eingabe führen.

## HOF-B1-S535-F03 — Abnäherinhalt aus der Längendifferenz

- **Fachlicher Zweck:** Den Abnäherinhalt aus der Differenz von Vorder- und Rückenlänge sowie einer signierten fachlichen Korrektur bestimmen.
- **Quelle:** `formeln_s535_digital_geprüft.md`, Zeile 15; Originaltranskript `s535_digital_geprüft.md`, Zeile 53; Buchseite 535.
- **Originalbezeichnung:** `Differenz VL − RüL ±; Abnäherinhalt`.
- **Normalisierte Bezeichnung:** `abnaeherinhalt_aus_laengendifferenz`

### Buchfassung

```text
|  | Differenz VL − RüL ± | Abnäherinhalt |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderlaenge` | VL | variabel | cm |
| `rueckenlaenge` | RüL | variabel | cm |
| `abnaeherinhalt_korrektur` | `±` | variabel, signiert | cm |

### Formel und Rechenschritte

```text
laengendifferenz = vorderlaenge - rueckenlaenge
abnaeherinhalt = laengendifferenz + abnaeherinhalt_korrektur
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `laengendifferenz` | Differenz VL − RüL | cm |
| `abnaeherinhalt` | korrigierter Abnäherinhalt | cm |

- **Abhängigkeiten:** VL, RüL und eine fachlich bestimmte signierte Korrektur.
- **Gültigkeitsbereich:** Leeres Konstruktionsformular für ein Shirt auf S. 535.
- **Technische Randbedingung:** `±` wird als vorzeichenbehaftete Eingabe modelliert; ein positiver Wert vergrößert, ein negativer verkleinert den Abnäherinhalt.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt weder Wert noch Ermittlungsregel der Korrektur.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Korrektur nie stillschweigend mit null belegen; sie muss fachlich gesetzt werden.
