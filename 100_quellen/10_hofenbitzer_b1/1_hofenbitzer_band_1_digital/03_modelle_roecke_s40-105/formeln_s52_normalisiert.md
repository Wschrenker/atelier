# Fachlich normalisierte Formeln — S. 52

Quelle der Normalisierung: `formeln_s52_codex_v2_digital_geprueft.md`
Originaltranskript: `s52_codex_v2_digital_geprueft.md`
Buchseite: Hofenbitzer, Band 1, S. 52

## HOF-B1-S052-F01 — Seitliche Taillenvertiefung mit 10 Prozent Zuschlag

- **Fachlicher Zweck:** Die seitliche Taillenvertiefung bei einer kleinen vereinfachten Taillenvertiefung durch einen Zuschlag von 10 Prozent bestimmen.
- **Quelle:** `formeln_s52_codex_v2_digital_geprueft.md`, Zeile 9; Originaltranskript `s52_codex_v2_digital_geprueft.md`, Zeilen 25–27 und 56; Buchseite 52.
- **Originalbezeichnung:** `seitliche Taillenvertiefung bis 4 cm + 10% = 4,4 cm`
- **Normalisierte Bezeichnung:** `seitliche_taillenvertiefung_klein`

### Buchfassung

```text
- seitliche Taillenvertiefung bis 4 cm + 10% = 4,4 cm.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenvertiefung_vorne_hinten` | Taillenvertiefung an vM und hM | 4 | cm |
| `seitlicher_zuschlag` | zusätzlicher Betrag an der Seitennaht | 10 | Prozent |

### Formel und Rechenschritte

```text
seitliche_taillenvertiefung = taillenvertiefung_vorne_hinten * (1 + seitlicher_zuschlag / 100)
                             = 4 cm * (1 + 10 / 100)
                             = 4,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `seitliche_taillenvertiefung` | Vertiefungsbetrag an der Seitennaht | 4,4 | cm |

- **Abhängigkeiten:** Gewählte kleine `taillenvertiefung_vorne_hinten`.
- **Gültigkeitsbereich:** Vereinfachte kleine Taillenvertiefung bis 4 cm auf S. 52; die Buchfassung zeigt den Grenzwert mit 4 cm.
- **Technische Randbedingung:** Die Ausgangsvertiefung muss in Zentimetern vorliegen und darf in dieser Buchregel höchstens 4 cm betragen. Der Zuschlag ist dimensionslos als Prozentwert zu verwenden.
- **Offene Fragen oder Widersprüche:** Keine für das Zahlenbeispiel. Eine über diese kleine Taillenvertiefung hinausgehende allgemeine Regel ist aus dieser Buchfassung nicht abzuleiten.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Prozentwert vor der Multiplikation durch 100 teilen und den Gültigkeitsbereich bis einschließlich 4 cm ausdrücklich prüfen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s52_codex_v2_digital_geprueft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Bildverweis `□4+5` und Konstruktionsanweisung für eine Belegbreite von 4 bis 6 cm; das Pluszeichen verbindet Bildnummern, die Breite ist ein gewählter Eingabebereich und keine berechnete Formel |
| **Summe** | **1** | **1 Fehlklassifikation ausgeschlossen** |
