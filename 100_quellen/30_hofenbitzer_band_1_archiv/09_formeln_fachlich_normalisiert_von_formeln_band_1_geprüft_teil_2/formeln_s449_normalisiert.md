# Fachlich normalisierte Formeln — S. 449

Quelle der Normalisierung: `formeln_s449_digital_geprüft.md`
Originaltranskript: `s449_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 449

## HOF-B1-S449-F01 — Breitenaufbau der verdeckten Knopfleiste

- **Fachlicher Zweck:** Den ersten Einschlag und zwei alternative Breiten der verdeckten Knopflochleiste aus der Knopfleistenbreite bestimmen.
- **Quelle:** `formeln_s449_digital_geprüft.md`, Zeilen 9–10 und 15; Originaltranskript `s449_digital_geprüft.md`, Zeilen 15–16 und 18; Buchseite 449.
- **Originalbezeichnung:** `1×` beziehungsweise `2× die Knopfleisten-Breite − 0,2 cm`
- **Normalisierte Bezeichnung:** `verdeckte_knopfleiste_breitenaufbau`

### Buchfassung

```text
3. □3 Die Knopfleisten-Breite 1× an die vKa zeichnen → 1. Einschlag.
4. Dann 2× die Knopfleisten-Breite − 0,2 cm anzeichnen → Knopfloch-Leiste. Damit ist die Knopfloch-Leiste schmaler und somit nicht sichtbar.
```

```text
6. Alternativ 1× die Knopfleisten-Breite − 0,2 cm anzeichnen. Damit ist die Knopfleiste 5-lagig (□4.2). Wichtig bei weißen, transparenten Stoffen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `knopfleistenbreite` | Knopfleisten-Breite | variabel | cm |
| `verdeckungsabzug` | `0,2 cm` | 0,2 | cm |
| `aufbauvariante` | vierlagig oder alternativ fünflagig | explizite Auswahl | dimensionslos |

### Formel und Rechenschritte

```text
erster_einschlag = knopfleistenbreite

Vierlagige Variante:
knopflochleiste_breite = (2 * knopfleistenbreite) - 0,2 cm

Fünflagige Alternative:
knopflochleiste_breite = knopfleistenbreite - 0,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `erster_einschlag` | Breite des ersten Einschlags | einfache Knopfleistenbreite | cm |
| `knopflochleiste_breite` | anzuzeichnende Breite der verdeckten Knopflochleiste | abhängig von der gewählten Variante | cm |

- **Abhängigkeiten:** Gewählte Knopfleistenbreite und ausdrücklich gewählte vier- oder fünflagige Variante.
- **Gültigkeitsbereich:** Verdeckte Knopfleiste der taillierten Bluse auf S. 449.
- **Technische Randbedingung:** `knopfleistenbreite > 0,2 cm`; die beiden Wege sind Varianten und dürfen nicht addiert oder automatisch vermischt werden.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Unklarheit. Die Quelle nennt keine automatische Auswahlregel zwischen vier- und fünflagigem Aufbau; die fünflagige Variante wird für weiße, transparente Stoffe empfohlen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Varianten als expliziten Parameter modellieren. Den Abzug `0.2` erst nach der Multiplikation anwenden und die Positivitätsbedingung der Ergebnisbreite prüfen.
