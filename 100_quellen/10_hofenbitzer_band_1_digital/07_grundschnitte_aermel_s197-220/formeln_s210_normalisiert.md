# Fachlich normalisierte Formeln — S. 210

Quelle der Normalisierung: `formeln_s210_digital_geprüft.md`
Originaltranskript: `s210_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 210
Extraktionsstand: v2

Die vier Buchstellen belegen dieselbe Oberarmvergrößerung für zwei Ärmelvarianten. Sie bleiben als getrennte Buchfassungsblöcke unter einer technischen Formel-ID erhalten.

## HOF-B1-S210-F01 — Oberarmvergrößerung durch beidseitige Öffnung

- **Fachlicher Zweck:** Die gesamte Oberarmvergrößerung aus den gleich großen Öffnungen an beiden Ärmelseiten bestimmen.
- **Quelle:** `formeln_s210_digital_geprüft.md`, Zeilen 9, 14, 19 und 24; Originaltranskript `s210_digital_geprüft.md`, Zeilen 10, 37, 45 und 73; Buchseite 210.
- **Originalbezeichnung:** Oberarmvergrößerung, Mehrweite
- **Normalisierte Bezeichnung:** `oberarmvergroesserung_durch_zwei_seitenoeffnungen`

### Buchfassung

Erste Variante, Beschreibung:

```text
□1 Durch die Öffnung des Ärmels entsteht eine Vergrößerung der Oberarmweite, hier um z.B. `2× 1 cm = 2 cm`.
```

Erste Variante, Zeichnungslabel:

```text
- Öffnung jeweils um ½ Oberarmvergrößerung (hier `2× 1 cm = 2 cm Mehrweite`)
```

Zweite Variante, Beschreibung:

```text
□2 Wie oben entsteht durch die Öffnung des Ärmels eine Vergrößerung der Oberarmweite hier z.B. um `2× 1 cm = 2 cm`.
```

Zweite Variante, Zeichnungslabel:

```text
- Öffnung jeweils um ½ der Mehrweite am Oberarm (hier `2× 1 cm = 2 cm Mehrweite`)
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `oeffnung_je_aermelseite` | Öffnung jeweils um ½ Oberarmvergrößerung | 1 | cm |

### Formel und Rechenschritte

```text
oberarmvergroesserung = 2 * oeffnung_je_aermelseite
oberarmvergroesserung = 2 * 1 cm = 2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `oberarmvergroesserung` | gesamte zusätzliche Oberarmweite | 2 | cm |

- **Abhängigkeiten:** Zwei gleich große Öffnungen, je eine an jeder Ärmelseite.
- **Gültigkeitsbereich:** Die Beziehung ist sowohl für den weiten Ärmel mit unveränderter Einhalteweite als auch für den weiten Ärmel mit zusätzlich verringerter Einhalteweite belegt.
- **Technische Randbedingung:** Die beidseitigen Öffnungen müssen gleich groß sein. Die zusätzliche Veränderung der Ärmelkugelhöhe und Einhalteweite ist eine getrennte Konstruktion und wird durch diese Formel nicht berechnet.
- **Offene Fragen oder Widersprüche:** Keine für die gedruckte Verdopplung. Die Quelle gibt 1 cm nur als Beispiel an.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Öffnung je Seite als Eingabe führen; die Einhalteweiten-Variante getrennt auswählen.
