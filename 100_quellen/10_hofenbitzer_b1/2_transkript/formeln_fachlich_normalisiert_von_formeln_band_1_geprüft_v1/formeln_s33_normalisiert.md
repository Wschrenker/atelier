# Fachlich normalisierte Formeln — S. 33

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s33.md`
Originaltranskript: `../Band_1_geprüft_v1/s33.md`
Buchseite: Hofenbitzer, Band 1, S. 33

## HOF-B1-S033-F01 — Taillenausfall aus Hüft- und Taillenweite

- **Fachlicher Zweck:** Gesamten Taillenausfall als Differenz zwischen halber Hüftweite und halber Taillenweite bestimmen.
- **Quelle:** `formeln_s33.md`, Zeilen 7–10; Originaltranskript `s33.md`, Zeilen 19–24 und 34–41; Buchseite 33.
- **Originalbezeichnung:** `½ HüW − ½ TaW`
- **Normalisierte Bezeichnung:** `taillenausfall`

### Buchfassung

```text
| ½ HüW − ½ TaW = | | 13 | 6,5 | |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `halbe_hueftweite` | ½ HüW | 50 | cm |
| `halbe_taillenweite` | ½ TaW | 37 | cm |

### Formel und Rechenschritte

```text
taillenausfall = halbe_hueftweite - halbe_taillenweite
                = 50 cm - 37 cm
                = 13 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenausfall` | Gesamter auf Hüftabstich und Abnäher zu verteilender Betrag | 13 | cm |

- **Abhängigkeiten:** `halbe_hueftweite`, `halbe_taillenweite`.
- **Gültigkeitsbereich:** Belegt für das Maßbeispiel des geraden Rock-Grundschnitts in Größe 38 auf S. 33.
- **Technische Randbedingung:** Beide Eingaben müssen in derselben Längeneinheit vorliegen.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Abweichung. Die Tabellenzeile nennt das Ergebnis nicht nochmals `TaAf`; die Zuordnung ergibt sich aus der unmittelbar anschließenden Hüftabstich-Tabelle und deren Kontrolle `Σ = TaAf`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Halbe Hüft- und Taillenweite als bereits zugabenhaltige Konstruktionsmaße verwenden; nicht mit den reinen Körpermaßen verwechseln.

## HOF-B1-S033-F02 — Kontrollsumme der Taillenausfall-Verteilung

- **Fachlicher Zweck:** Prüfen, dass Hüftabstich und Abnäherinhalte zusammen genau den Taillenausfall ergeben.
- **Quelle:** `formeln_s33.md`, Zeilen 12–15; Originaltranskript `s33.md`, Zeilen 34–41; Buchseite 33.
- **Originalbezeichnung:** `Kontrolle: Σ = TaAf`
- **Normalisierte Bezeichnung:** `kontrollsumme_taillenausfall`

### Buchfassung

```text
| Kontrolle: | Σ = TaAf | 13 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftabstich` | Hüftabstich | 6,5 | cm |
| `vorderer_abnaeherinhalt` | v. Abnäher | 2,5 | cm |
| `erster_hinterer_abnaeherinhalt` | 1. h. Abnäher | 4 | cm |
| `zweiter_hinterer_abnaeherinhalt` | 2. h. Abnäher, optional | 0 | cm |
| `taillenausfall` | TaAf | 13 | cm |

### Formel und Rechenschritte

```text
kontrollsumme_taillenausfall = hueftabstich
                              + vorderer_abnaeherinhalt
                              + erster_hinterer_abnaeherinhalt
                              + zweiter_hinterer_abnaeherinhalt
                              = 6,5 cm + 2,5 cm + 4 cm + 0 cm
                              = 13 cm

kontrollsumme_taillenausfall = taillenausfall
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `kontrollsumme_taillenausfall` | Summe aller verteilten Taillenausfall-Beträge | 13 | cm |
| `verteilung_ist_vollstaendig` | Kontrollaussage `Σ = TaAf` | wahr | boolesch |

- **Abhängigkeiten:** `HOF-B1-S033-F01` sowie alle in der gewählten Variante verwendeten Verteilungsbeträge.
- **Gültigkeitsbereich:** Variante auf S. 33 mit einem hinteren Abnäher; der zweite hintere Abnäher ist dort nicht verwendet.
- **Technische Randbedingung:** Ein nicht verwendeter optionaler Abnäher wird technisch mit `0 cm` in die Summe aufgenommen. Das ist eine Umsetzungsfestlegung; die Buchfassung zeigt dafür `---`.
- **Offene Fragen oder Widersprüche:** Keine; `6,5 + 2,5 + 4 = 13`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Kontrolle mit einer kleinen Längentoleranz ausführen, damit spätere Rundungen nicht zu falschen Fehlern führen; die Toleranz ist technisch festzulegen und keine Buchregel.

## HOF-B1-S033-F03 — Halbe Hüftweite mit Zugabe

- **Fachlicher Zweck:** Halbe Hüftweite des Grundgerüsts aus Hüftumfang und gewählter Zugabe bestimmen.
- **Quelle:** `formeln_s33.md`, Zeilen 17–20; Originaltranskript `s33.md`, Zeilen 11–24 und 58–63; Buchseite 33.
- **Originalbezeichnung:** `½ Hüftweite`
- **Normalisierte Bezeichnung:** `halbe_hueftweite`

### Buchfassung

```text
- Formel an der Taillenlinie: „½ Hüftweite = (HüU + Zg) : 2   (hier 50 cm)"
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `hueftzugabe` | Zg zum Hüftumfang | 3 | cm |
| `teilungszahl` | Halbierung | 2 | dimensionslos |

### Formel und Rechenschritte

```text
halbe_hueftweite = (hueftumfang + hueftzugabe) / teilungszahl
                  = (97 cm + 3 cm) / 2
                  = 50 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `halbe_hueftweite` | Halbe zugabenhaltige Hüftweite des Grundgerüsts | 50 | cm |

- **Abhängigkeiten:** `hueftumfang`, gewählte `hueftzugabe` und `teilungszahl`.
- **Gültigkeitsbereich:** Belegt für `HüU = 97 cm` und die auf S. 33 gewählte Hüftzugabe von `3 cm`.
- **Technische Randbedingung:** `teilungszahl` darf nicht `0` sein; Umfang und Zugabe müssen dieselbe Einheit tragen.
- **Offene Fragen oder Widersprüche:** Keine; `(97 + 3) / 2 = 50`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Zugabe als eigene Eingabe erhalten und nicht dauerhaft mit dem Körpermaß zu einem einzigen Wert verschmelzen.

## Ausgeschlossener Kandidat

| Quelle in `formeln_s33.md` | Ausschlussgrund |
|---|---|
| Zeilen 22–25 | Verifikationsnotiz der Transkription mit Wiederholungen der bereits oben normalisierten Rechnungen; administrativer Prüftext, keine zusätzliche Buchformel |
