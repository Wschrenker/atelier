# Fachlich normalisierte Formeln — S. 297

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s297.md`  
Originaltranskript: `s297.md`  
Buchseite: Hofenbitzer, Band 1, S. 297

## HOF-B1-S297-F01 — Vordere Stegbreite aus hinterer Stegbreite

- **Fachlicher Zweck:** Die vordere Stegbreite gegenüber der hinteren Stegbreite verkleinern.
- **Quelle:** `formeln_s297.md`, Zeile 14; Originaltranskript `s297.md`, Zeile 45; Buchseite 297.
- **Originalbezeichnung:** `vordere Stegbreite = StegB − ca. 0,5 cm`
- **Normalisierte Bezeichnung:** `vordere_stegbreite`

### Buchfassung

```text
vordere Stegbreite = StegB − ca. 0,5 cm
```

### Eingaben und Rechenschritte

```text
vordere_stegbreite = stegbreite - stegbreiten_abzug
                     ≈ stegbreite - 0,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `vordere_stegbreite` | vordere Breite des angeschnittenen Stegs | cm |

- **Abhängigkeiten:** Hintere Stegbreite StegB.
- **Gültigkeitsbereich:** Einteiliger Steh-Umlegekragen mit geradem vorderen Kragenbruch.
- **Technische Randbedingung:** `ca. 0,5 cm` ist ein ungefährer Abzug.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Abzug als Parameter mit Näherungskennzeichnung führen.

## HOF-B1-S297-F02 — Kragenbreite aus Stegbreite

- **Fachlicher Zweck:** Die hintere Kragenbreite aus der hinteren Stegbreite bestimmen.
- **Quelle:** `formeln_s297.md`, Zeilen 19 und 24; Originaltranskript `s297.md`, Zeilen 47, 53 und 57; Buchseite 297.
- **Originalbezeichnung:** `KrB = StegB + 0,7 bis 1,5 cm`
- **Normalisierte Bezeichnung:** `kragenbreite_aus_stegbreite_steh_umlegekragen`

### Buchfassung

```text
KrB = StegB + 0,7 bis 1,5 cm
```

### Formel und Rechenschritte

```text
kragenbreite = stegbreite + kragen_zuschlag
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kragenbreite` | hintere Kragenbreite | cm |

- **Abhängigkeiten:** StegB und Zuschlagsbereich.
- **Gültigkeitsbereich:** Einteiliger Steh-Umlegekragen.
- **Technische Randbedingung:** Zuschlag `0,7 bis 1,5 cm` bleibt eine Auswahl.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zuschlag explizit übergeben.

## Ausgeschlossene Kandidaten

| Extraktzeilen | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Direkte Halsloch-Länge ohne eigene Berechnung |
| **Summe** | **1** | **Eingabelabel ausgeschlossen** |
