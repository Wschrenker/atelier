# Fachlich normalisierte Formeln — S. 37

Quelle der Normalisierung: `formeln_s037.md`
Originaltranskript: `s037.md`
Buchseite: Hofenbitzer, Band 1, S. 37

Walking Skeleton auf Werners ausdrücklichen Wunsch: `s037.md` enthält noch
keinen Abschnitt „Vorab geklärte formel- und coderelevante Stellen". Beide
Formeln unten sind unverändert aus der OCR-Rohfassung übernommen und **nicht
am Original bestätigt**; sie erhalten Status `offen`.

## HOF-B1-S037-F01 — Größerer Hüftabstich bei breiter Hüfte

- **Fachlicher Zweck:** Den Hüftabstich für Figuren mit breiter Hüfte und
  flacherem Gesäß (□3) gegenüber dem Grundwert ½ TaAf vergrößert bestimmen.
- **Quelle:** `formeln_s037.md`, Abschnitt F0; `ocr_s037.md` Z.29, Z.31-32.
  Noch nicht bestätigt.
- **Originalbezeichnung:** `TaAf :2 + 0,5 bis + 1,5 cm`.
- **Normalisierte Bezeichnung:** `hueftabstich_breite_huefte`

### Buchfassung

```text
Berechnung des größeren Hüftabstichs:
TaAf :2 + 0,5 bis + 1,5 cm
```

### Technische Formel

```text
hueftabstich_breite_huefte = (taillenausfall / 2) + zuschlag, zuschlag ∈ [0,5; 1,5] cm
```

### Eingaben und Einheiten

| Variable | Bedeutung | Einheit |
|---|---|---|
| `taillenausfall` (TaAf) | Taillenausfall, siehe `formeln_s033.md` Tabelle 1 | cm |
| `zuschlag` | zusätzlicher Betrag, fachlich zu wählen | cm |

### Ausgabe und Einheit

| Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftabstich_breite_huefte` | Hüftabstich bei breiter Hüfte | cm |

### Bereiche, Bedingungen und Auswahlentscheidungen

Gilt für Figuren mit breiter Hüfte und flacherem Gesäß (□3). `zuschlag` liegt
im Bereich `0,5 bis 1,5 cm`; keine Buchregel wählt innerhalb des Bereichs
einen festen Wert.

### Abhängigkeiten

Setzt `taillenausfall` (TaAf) voraus, definiert in `formeln_s033.md`, Tabelle 1
(`TaAf = ½ HüW − ½ TaW`). Verwandt, aber nicht gleichgesetzt: die Grundformel
`Hüftabstich = ½ TaAf ± 1` aus `formeln_s033.md` (Tabelle 3) und
`formeln_s034.md` (F5); dort andere Bereichsgrenzen. Ebenfalls verwandt, aber
nicht gleichgesetzt: die Hüftrundungs-Variante „starke Hüftrundung:
TaAf : 2 + 1 bis +1,5 cm" in `formeln_s034.md`, F7 — dort geht es um die
seitliche Rundung der Hüfte, hier um die Hüftbreite gegenüber dem Gesäß.

### Status

`offen` — nicht am Original bestätigt.

### Offene Fragen oder Widersprüche

Ob dieser Bereich (`+0,5 bis +1,5`) dieselbe fachliche Anpassung meint wie die
auf `formeln_s034.md`, F7 für „starke Hüftrundung" gedruckte Variante (`+1 bis
+1,5`), oder eine eigenständige, von der Hüftbreite statt der Hüftrundung
abhängige Regel ist, ist nicht entschieden.

## HOF-B1-S037-F02 — Kleinerer Hüftabstich bei stärkerem Gesäß

- **Fachlicher Zweck:** Den Hüftabstich für Figuren mit stärker ausgeprägtem
  Gesäß und flacheren seitlichen Hüftrundungen (□4) gegenüber dem Grundwert
  ½ TaAf verkleinert bestimmen.
- **Quelle:** `formeln_s037.md`, Abschnitt F1; `ocr_s037.md` Z.34, Z.36-37.
  Noch nicht bestätigt.
- **Originalbezeichnung:** `TaAf :2 - 0,5 bis - 1,5 cm`.
- **Normalisierte Bezeichnung:** `hueftabstich_staerkeres_gesaess`

### Buchfassung

```text
Berechnung für den kleinen Hüftabstich:
TaAf :2 - 0,5 bis - 1,5 cm
```

### Technische Formel

```text
hueftabstich_staerkeres_gesaess = (taillenausfall / 2) - abschlag, abschlag ∈ [0,5; 1,5] cm
```

### Eingaben und Einheiten

| Variable | Bedeutung | Einheit |
|---|---|---|
| `taillenausfall` (TaAf) | Taillenausfall, siehe `formeln_s033.md` Tabelle 1 | cm |
| `abschlag` | abzuziehender Betrag, fachlich zu wählen | cm |

### Ausgabe und Einheit

| Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftabstich_staerkeres_gesaess` | Hüftabstich bei stärker ausgeprägtem Gesäß | cm |

### Bereiche, Bedingungen und Auswahlentscheidungen

Gilt für Figuren mit stärker ausgeprägtem Gesäß (□4). `abschlag` liegt im
Bereich `0,5 bis 1,5 cm`; keine Buchregel wählt innerhalb des Bereichs einen
festen Wert. Das Buch nennt zusätzlich, dass hinten oft zwei Abnäher nötig
sind und der Hüftbogen flacher gezeichnet wird; das bleibt Text und wird
nicht als eigene Formel geführt.

### Abhängigkeiten

Setzt `taillenausfall` (TaAf) voraus, definiert in `formeln_s033.md`,
Tabelle 1. Verwandt, aber nicht gleichgesetzt: Grundformel
`Hüftabstich = ½ TaAf ± 1` (`formeln_s033.md` Tabelle 3, `formeln_s034.md`
F5) und die Hüftrundungs-Variante „flache Hüftrundung: TaAf : 2 − 1 bis
−1,5 cm" in `formeln_s034.md`, F7.

### Status

`offen` — nicht am Original bestätigt.

### Offene Fragen oder Widersprüche

Wie bei F01: Verhältnis zur Hüftrundungs-Formel in `formeln_s034.md`, F7
(dort `−1 bis −1,5` statt `−0,5 bis −1,5`) ist ungeklärt.

## Prüfhinweis

Beide fototreu erfassten Formelstellen sind nicht am Original bestätigt und
werden hier mit Status `offen` geführt. Für einen späteren Codevertrag reicht
der aktuelle Stand nicht aus.
