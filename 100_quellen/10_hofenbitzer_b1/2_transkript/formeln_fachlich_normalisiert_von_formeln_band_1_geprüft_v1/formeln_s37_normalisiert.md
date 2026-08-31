# Fachlich normalisierte Formeln — S. 37

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s37.md`
Originaltranskript: `../Band_1_geprüft_v1/s37.md`
Buchseite: Hofenbitzer, Band 1, S. 37

## HOF-B1-S037-F01 — Größerer Hüftabstich bei breiter Hüfte

- **Fachlicher Zweck:** Den größeren seitlichen Hüftabstich für eine breite Hüfte und ein eher flaches Gesäß aus dem halben Taillenausfall und einem Zuschlag bestimmen.
- **Quelle:** `formeln_s37.md`, Zeilen 7–10; Originaltranskript `s37.md`, Zeilen 40–41; Buchseite 37.
- **Originalbezeichnung:** `Berechnung des größeren Hüftabstichs`
- **Normalisierte Bezeichnung:** `hueftabstich_breite_huefte`

### Buchfassung

```text
- Berechnung des größeren Hüftabstichs: `TaAf :2 + 0,5 bis + 1,5 cm`.
```

### Eingaben

| Technische Variable | Buchbegriff | Wertebereich | Einheit |
|---|---|---:|---|
| `taillenausfall` | TaAf | nicht festgelegt | cm |
| `hueftform_korrektur` | Zuschlag bei breiter Hüfte | 0,5 bis 1,5 | cm |

### Formel und Rechenschritte

```text
hueftabstich_breite_huefte = (taillenausfall / 2) + hueftform_korrektur

untere Grenze = (taillenausfall / 2) + 0,5 cm
obere Grenze  = (taillenausfall / 2) + 1,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftabstich_breite_huefte` | Größerer seitlicher Hüftabstich für die beschriebene Figurform | cm |

- **Abhängigkeiten:** `taillenausfall` und fachlich gewählte `hueftform_korrektur`; Fortführung der Taillenausfall-Verteilung aus Tranche `R01`.
- **Gültigkeitsbereich:** Die auf S. 37 beschriebene Figur mit breiter Hüfte und eher flachem Gesäß.
- **Technische Randbedingung:** Der Zuschlag muss im belegten Bereich `0,5 bis 1,5 cm` liegen. Taillenausfall und Zuschlag müssen dieselbe Längeneinheit tragen.
- **Offene Fragen oder Widersprüche:** Die Quelle belegt nicht, wie der konkrete Zuschlag innerhalb des Bereichs gewählt wird.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Figurform und Zuschlag als sichtbare fachliche Eingaben führen; keine automatische Auswahl aus Umfangsmaßen ableiten.

## HOF-B1-S037-F02 — Kleiner Hüftabstich bei starkem Gesäß

- **Fachlicher Zweck:** Den kleineren seitlichen Hüftabstich für ein stärker ausgeprägtes Gesäß und eine eher schmale Hüfte aus dem halben Taillenausfall und einem Abzug bestimmen.
- **Quelle:** `formeln_s37.md`, Zeilen 12–15; Originaltranskript `s37.md`, Zeilen 42–44; Buchseite 37.
- **Originalbezeichnung:** `Berechnung für den kleinen Hüftabstich`
- **Normalisierte Bezeichnung:** `hueftabstich_starkes_gesaess`

### Buchfassung

```text
- Berechnung für den kleinen Hüftabstich: `TaAf :2 - 0,5 bis - 1,5 cm`.
```

### Eingaben

| Technische Variable | Buchbegriff | Wertebereich | Einheit |
|---|---|---:|---|
| `taillenausfall` | TaAf | nicht festgelegt | cm |
| `hueftform_korrektur` | Abzug bei starkem Gesäß | 0,5 bis 1,5 | cm |

### Formel und Rechenschritte

```text
hueftabstich_starkes_gesaess = (taillenausfall / 2) - hueftform_korrektur

obere Ergebnisgrenze  = (taillenausfall / 2) - 0,5 cm
untere Ergebnisgrenze = (taillenausfall / 2) - 1,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftabstich_starkes_gesaess` | Kleinerer seitlicher Hüftabstich für die beschriebene Figurform | cm |

- **Abhängigkeiten:** `taillenausfall` und fachlich gewählte `hueftform_korrektur`; der verbleibende Taillenausfall wird nach der Buchbeschreibung stärker auf die hinteren Abnäher verteilt.
- **Gültigkeitsbereich:** Die auf S. 37 beschriebene Figur mit stärker ausgeprägtem Gesäß und eher schmaler Hüfte.
- **Technische Randbedingung:** Der Abzug muss im belegten Bereich `0,5 bis 1,5 cm` liegen. Das Ergebnis darf technisch nicht negativ werden; diese Schutzbedingung ist keine ausdrückliche Buchregel.
- **Offene Fragen oder Widersprüche:** Die Quelle belegt nicht, wie der konkrete Abzug innerhalb des Bereichs gewählt wird.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Abzug nicht als negatives Eingabemaß speichern, sondern als positiven Betrag, der in der Formel subtrahiert wird.
