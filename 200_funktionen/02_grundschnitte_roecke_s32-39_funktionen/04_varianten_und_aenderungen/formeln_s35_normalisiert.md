# Fachlich normalisierte Formeln — S. 35

Quelle der Normalisierung: `formeln_s35.md`
Originaltranskript: `s35.md`
Buchseite: Hofenbitzer, Band 1, S. 35

## HOF-B1-S035-F01 — Kontrollsumme bei zwei hinteren Abnähern

- **Fachlicher Zweck:** Prüfen, dass Hüftabstich, vorderer Abnäher und zwei hintere Abnäher zusammen den Taillenausfall ergeben.
- **Quelle:** `formeln_s35.md`, Zeilen 7–10; Originaltranskript `s35.md`, Zeilen 20–30; Buchseite 35.
- **Originalbezeichnung:** `Kontrolle: Σ = TaAf`
- **Normalisierte Bezeichnung:** `kontrollsumme_taillenausfall_zwei_hintere_abnaeher`

### Buchfassung

```text
| Kontrolle: | Σ = TaAf | 13 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftabstich` | Hüftabstich | 6 | cm |
| `vorderer_abnaeherinhalt` | v. Abnäher | 1,5 | cm |
| `erster_hinterer_abnaeherinhalt` | 1. h. Abnäher | 3 | cm |
| `zweiter_hinterer_abnaeherinhalt` | 2. h. Abnäher | 2,5 | cm |
| `taillenausfall` | TaAf | 13 | cm |

### Formel und Rechenschritte

```text
kontrollsumme_taillenausfall_zwei_hintere_abnaeher = hueftabstich
                                                     + vorderer_abnaeherinhalt
                                                     + erster_hinterer_abnaeherinhalt
                                                     + zweiter_hinterer_abnaeherinhalt
                                                     = 6 cm + 1,5 cm + 3 cm + 2,5 cm
                                                     = 13 cm

kontrollsumme_taillenausfall_zwei_hintere_abnaeher = taillenausfall
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `kontrollsumme_taillenausfall_zwei_hintere_abnaeher` | Summe der vier Verteilungsbeträge | 13 | cm |
| `verteilung_ist_vollstaendig` | Kontrollaussage `Σ = TaAf` | wahr | boolesch |

- **Abhängigkeiten:** `HOF-B1-S033-F01` und die auf S. 35 gewählten Verteilungsbeträge.
- **Gültigkeitsbereich:** Beispielvariante auf S. 35 mit zwei hinteren Abnähern.
- **Technische Randbedingung:** Alle Summanden müssen dieselbe Längeneinheit tragen. Die Quelle fordert zusätzlich, dass die Summe der Abnäherinhalte beim Aufteilen erhalten bleibt.
- **Offene Fragen oder Widersprüche:** Keine; `6 + 1,5 + 3 + 2,5 = 13`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Dieselbe allgemeine Kontrollfunktion wie bei der Ein-Abnäher-Variante verwenden und die hinteren Abnäher als Liste behandeln.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s35.md` | Ausschlussgrund |
|---|---|
| Zeilen 12–15 | Zeichnungslabels; `TaU : 10` wiederholt die auf S. 34 normalisierte Positionsformel, die übrigen Werte sind einzelne Maße und Teilungsmarken |
| Zeilen 17–20 | administrative Verifikationsnotiz mit Wiederholung der oben normalisierten Kontrollsumme; keine zusätzliche Buchformel |
