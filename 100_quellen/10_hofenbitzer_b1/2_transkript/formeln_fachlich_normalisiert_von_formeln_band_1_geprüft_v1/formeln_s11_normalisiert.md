# Fachlich normalisierte Formeln — S. 11

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/01_grundlagen_s8-31/formeln_s11.md`
Originaltranskript: `../hofenbitzer_band_1_digital/01_grundlagen_s8-31/s11.md`
Buchseite: Hofenbitzer, Band 1, S. 11

## HOF-B1-S011-F01 — Figurinenhöhe im Maßstab 1:16

- **Fachlicher Zweck:** Höhe der im Buch verwendeten 8-teiligen Figurine aus der Körperhöhe der Normalfigur und dem Maßstab bestimmen.
- **Quelle:** `formeln_s11.md`, Zeilen 7–10; Originaltranskript `s11.md`, Zeile 45; Buchseite 11.
- **Originalbezeichnung:** `Länge`
- **Normalisierte Bezeichnung:** `figurinenhoehe_zeichnung`

### Buchfassung

```text
Die Höhe bei der in diesem Buch verwendeten 8-teiligen Figurine ist im **Maßstab 1:16** für eine Normalfigur mit der Körperhöhe 168 cm gestaltet (Länge = 168 cm : 16 = 10,5 cm).
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `koerperhoehe` | Körperhöhe | 168 | cm |
| `massstabsnenner` | Nenner des Maßstabs 1:16 | 16 | dimensionslos |

### Formel und Rechenschritte

```text
figurinenhoehe_zeichnung = koerperhoehe / massstabsnenner
                          = 168 cm / 16
                          = 10,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `figurinenhoehe_zeichnung` | Höhe der gezeichneten Figurine im Maßstab 1:16 | 10,5 | cm |

- **Abhängigkeiten:** `koerperhoehe`, `massstabsnenner`.
- **Gültigkeitsbereich:** Die Buchfassung belegt die Rechnung für eine Normalfigur mit `koerperhoehe = 168 cm` und den Maßstab `1:16`.
- **Technische Randbedingung:** Der Divisor `massstabsnenner` darf nicht `0` sein. Dies ist eine technische Rechenbedingung, keine zusätzliche Buchregel.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Abweichung. Die Buchfassung wechselt zwischen „Höhe“ und „Länge“; die Normalisierung verwendet für die Ausgabe einheitlich „Figurinenhöhe“.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Größenwert und Einheit getrennt führen; `10,5` wird im Python-Code als Dezimalwert `10.5` repräsentiert. Keine allgemeine Körperhöhe oder ein anderer Maßstab ist durch dieses Buchbeispiel validiert.

## HOF-B1-S011-F02 — Teillänge bei Achtelteilung

- **Fachlicher Zweck:** Höhe eines Achtels einer wirklichen Person aus deren Körperhöhe bestimmen.
- **Quelle:** `formeln_s11.md`, Zeilen 12–15; Originaltranskript `s11.md`, Zeile 47; Buchseite 11.
- **Originalbezeichnung:** `Teillänge`
- **Normalisierte Bezeichnung:** `teillaenge_achtel`

### Buchfassung

```text
Für eine wirkliche Person mit einer Körperhöhe von 168 cm hat also jedes Achtel optimalerweise eine Höhe von 21 cm (Teillänge = 168 cm : 8 = 21 cm).
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `koerperhoehe` | Körperhöhe | 168 | cm |
| `teilungszahl` | Achtelteilung | 8 | dimensionslos |

### Formel und Rechenschritte

```text
teillaenge_achtel = koerperhoehe / teilungszahl
                   = 168 cm / 8
                   = 21 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `teillaenge_achtel` | Höhe eines Achtels der wirklichen Person | 21 | cm |

- **Abhängigkeiten:** `koerperhoehe`, `teilungszahl`.
- **Gültigkeitsbereich:** Die Buchfassung belegt die Rechnung für eine wirkliche Person mit `koerperhoehe = 168 cm` und eine Achtelteilung.
- **Technische Randbedingung:** Der Divisor `teilungszahl` darf nicht `0` sein. Dies ist eine technische Rechenbedingung, keine zusätzliche Buchregel.
- **Offene Fragen oder Widersprüche:** Keine rechnerische oder sprachliche Abweichung innerhalb der extrahierten Formel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Konstante `8` nicht mit dem Maßstabsnenner `16` aus `HOF-B1-S011-F01` vermischen. Eine Verallgemeinerung auf andere Teilungszahlen wäre eine neue, nicht durch diese Buchfassung belegte Regel.
