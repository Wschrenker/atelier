# Fachlich normalisierte Formeln — S. 448

Quelle der Normalisierung: `formeln_s448_digital_geprüft.md`
Originaltranskript: `s448_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 448

## HOF-B1-S448-F01 — Übertrittbreite der Knopfleiste

- **Fachlicher Zweck:** Die Übertrittbreite als halbe Leistenbreite bestimmen.
- **Quelle:** `formeln_s448_digital_geprüft.md`, Zeile 14; Originaltranskript `s448_digital_geprüft.md`, Zeile 22; Buchseite 448.
- **Originalbezeichnung:** `Übertrittbreite = ½ Leisten-Breite`
- **Normalisierte Bezeichnung:** `uebertrittbreite`

### Buchfassung

```text
2. Knopfleiste in gewünschter Breite (hier 4 cm) gestalten. Übertrittbreite = ½ Leisten-Breite an die vM zeichnen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `leistenbreite` | Leisten-Breite | hier 4 | cm |

### Formel und Rechenschritte

```text
uebertrittbreite = 0,5 * leistenbreite
uebertrittbreite = 0,5 * 4 cm
uebertrittbreite = 2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `uebertrittbreite` | Übertrittbreite an der vorderen Mitte | hier 2 | cm |

- **Abhängigkeiten:** Gewählte Leistenbreite.
- **Gültigkeitsbereich:** Verdeckte Knopfleiste der taillierten Bluse auf S. 448.
- **Technische Randbedingung:** `leistenbreite > 0`; an der vorderen Mitte wird die halbe Breite als Übertritt angesetzt.
- **Offene Fragen oder Widersprüche:** Keine; `½ × 4 cm = 2 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Positive Leistenbreite verlangen und mit `0.5` multiplizieren; den Buchwert `4 cm` als Seitenbeispiel, nicht als allgemeine Vorgabe führen.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s448_digital_geprüft.md`, Zeile 9 | 1 | Passformklassen- und Grundschnittangabe mit Seitenverweis `192+193`; Anwendungsbereich, keine Rechenformel |
| **Summe** | **1** | **1 Kontext-/Anwendungszeile ausgeschlossen** |
