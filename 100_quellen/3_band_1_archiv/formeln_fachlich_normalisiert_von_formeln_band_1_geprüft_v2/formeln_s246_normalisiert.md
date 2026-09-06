# Fachlich normalisierte Formeln — S. 246–247

Quelle der Normalisierung: `formeln_s246_digital_geprüft.md`, zusätzlicher Anwendungsnachweis in `formeln_s247_digital_geprüft.md`
Originaltranskripte: `s246_digital_geprüft.md`, `s247_digital_geprüft.md`
Buchseiten: Hofenbitzer, Band 1, S. 246–247
Extraktionsstand: v2

## HOF-B1-S246-F01 — Saumeinschlag mit Rollweite am separaten Ärmelaufschlag

- **Fachlicher Zweck:** Den gesamten Saumeinschlag aus dem üblichen Saumeinschlag und der zusätzlichen Rollweite bestimmen.
- **Quelle:** `formeln_s246_digital_geprüft.md`, Zeile 14; Originaltranskript `s246_digital_geprüft.md`, Zeile 25; zusätzlicher wortgleicher Anwendungsnachweis in `formeln_s247_digital_geprüft.md`, Zeile 14, und `s247_digital_geprüft.md`, Zeile 26; Buchseiten 246–247.
- **Originalbezeichnung:** Saumeinschlag, Rollweite
- **Normalisierte Bezeichnung:** `saumeinschlag_mit_rollweite`

### Buchfassung

```text
6. Den üblichen Saumeinschlag von 3 cm und für das Herumführen an der Ärmellänge weitere 0,5 cm (Rollweite, siehe □3 Nahtdiagramm) addieren = 3,5 cm.
```

Zusätzlicher wortgleicher Anwendungsnachweis auf S. 247:

```text
6. Den üblichen Saumeinschlag von 3 cm und für das Herumführen an der Ärmellänge weitere 0,5 cm (Rollweite, siehe □3 Nahtdiagramm) addieren = 3,5 cm.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `saumeinschlag_ueblich` | üblicher Saumeinschlag | 3 | cm |
| `rollweite` | Rollweite | 0,5 | cm |

### Formel und Rechenschritte

```text
saumeinschlag_mit_rollweite = saumeinschlag_ueblich + rollweite
saumeinschlag_mit_rollweite = 3 cm + 0,5 cm
saumeinschlag_mit_rollweite = 3,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `saumeinschlag_mit_rollweite` | gesamter Saumeinschlag einschließlich Rollweite | cm |

- **Abhängigkeiten:** Üblicher Saumeinschlag und Rollweite für das Herumführen an der Ärmellänge.
- **Gültigkeitsbereich:** Separate Saumaufschläge am Zweinaht-Ärmel auf S. 246 und die besonderen Saumaufschläge auf S. 247; beide Seiten drucken dieselbe Beziehung.
- **Technische Randbedingung:** Der skalare Gesamtbetrag ist von seiner geometrischen Lage am Aufschlag zu trennen.
- **Offene Fragen oder Widersprüche:** Keine; `3 cm + 0,5 cm = 3,5 cm` ist rechnerisch konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Beide Eingaben als nichtnegative Längen führen und die Summe einmal als gemeinsame technische Regel für beide belegten Varianten implementieren.

## Ausgeschlossene Kandidaten

| Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s246_digital_geprüft.md`, Zeile 9 | 1 | Geometrische Spiegel- und Kopieranweisung; keine skalare Rechenausgabe |
| `formeln_s246_digital_geprüft.md`, Zeilen 19 und 24–25 | 3 | Produktions- und Zuschnittbeschriftungen mit Stückzahl, Material und Größe |
| `formeln_s247_digital_geprüft.md`, Zeile 9 | 1 | Geometrische Kopieranweisung; keine skalare Rechenausgabe |
| `formeln_s247_digital_geprüft.md`, Zeilen 19–20 und 25–26 | 4 | Produktions- und Zuschnittbeschriftungen für inneren und äußeren Aufschlag |
| **Summe** | **9** | **2 geometrische Methodenangaben + 7 Produktions-/Zuschnittzeilen** |

## Extraktionsgrenze

Die Transkripte nennen weitere Bereiche und Konstruktionsangaben, darunter Mehrweiten am Aufschlag sowie auf beiden Seiten etwa `0,5 cm` zusätzlichen Saumeinschlag in der Mitte. Diese Beziehungen fehlen als vollständige Buchfassungen im verbindlichen Extrakt und wurden nicht stillschweigend normalisiert. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
