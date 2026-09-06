# Fachlich normalisierte Formeln — S. 298

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s298.md`  
Originaltranskript: `s298.md`  
Buchseite: Hofenbitzer, Band 1, S. 298

## HOF-B1-S298-F01 — Kragenbreite aus Stegbreite beim zweiteiligen Kragen

- **Fachlicher Zweck:** Die Kragenbreite über dem angesetzten Steg bestimmen.
- **Quelle:** `formeln_s298.md`, Zeilen 14, 25 und 30; Originaltranskript `s298.md`, Zeilen 28, 43, 53 und 57; Buchseite 298.
- **Originalbezeichnung:** `KrB = StegB + 0,7 bis 1,5 cm`
- **Normalisierte Bezeichnung:** `kragenbreite_aus_stegbreite_zweiteilig`

### Buchfassung

```text
KrB = StegB + 0,7 bis 1,5 cm
```

### Formel und Rechenschritte

```text
kragenbreite = stegbreite + kragen_zuschlag
```

Der Bereich `0,7 bis 1,5 cm` bleibt unverändert als Eingabe.

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `kragenbreite` | Kragenbreite des zweiteiligen Steh-Umlegekragens | cm |

- **Abhängigkeiten:** StegB und Zuschlag.
- **Gültigkeitsbereich:** Zweiteilige Umlegekragen mit angesetztem Steg.
- **Technische Randbedingung:** `KrB + 0 bis 0,4 cm` ist eine zusätzliche Konstruktionsangabe, nicht automatisch Teil der Grundformel.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Grundkragenbreite und zusätzliche Kragenkantenöffnung getrennt modellieren.

## Ausgeschlossene Kandidaten

| Extraktzeilen | Anzahl | Ausschlussgrund |
|---|---:|---|
| 22, 35–39, 45, 53, 57 | 2 | Konstruktionsschritte, direkte Teilungen und Maßlabels ohne eigenständige Rechenbeziehung |
| **Summe** | **2** | **Konstruktions- und Eingabeangaben ausgeschlossen** |
