# Fachlich normalisierte Formeln — S. 152

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s152.md`
Originaltranskript: `s152.md`
Buchseite: Hofenbitzer, Band 1, S. 152

## HOF-B1-S152-F01 — Saumeinschlag aus Aufschlagbreite

- **Fachlicher Zweck:** Den Saumeinschlag gegenüber der Aufschlagbreite verringern.
- **Quelle:** `formeln_s152.md`, Zeile 9; Originaltranskript `s152.md`, Zeile 63; Buchseite 152.
- **Originalbezeichnung:** `Saumeinschlag = Aufschlagbreite - 1 bis 2 cm`
- **Normalisierte Bezeichnung:** `saumeinschlag_aus_aufschlagbreite`

### Buchfassung

```text
- Saumeinschlag = Aufschlagbreite - 1 bis 2 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `aufschlagbreite` | Aufschlagbreite | variabel | cm |
| `saumeinschlag_abzug` | Abzug | 1 bis 2 | cm |

### Formel und Rechenschritte

```text
saumeinschlag = aufschlagbreite - saumeinschlag_abzug
saumeinschlag_abzug ∈ [1 cm, 2 cm]
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `saumeinschlag` | Breite des Saumeinschlags | cm |

- **Abhängigkeiten:** Gewählte Aufschlagbreite und ein Abzug innerhalb des angegebenen Bereichs.
- **Gültigkeitsbereich:** ⅞-Hose mit Miederbund und Saumaufschlägen.
- **Technische Randbedingung:** Der konkrete Wert innerhalb des Bereichs ist eine fachliche Auswahl; die Quelle nennt keine Auswahlregel.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Prüfung mit einem konkreten Aufschlagwert im Extrakt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereichsgrenzen validieren und den gewählten Abzug als Eingabe protokollieren.

## Ausgeschlossene Kandidaten

Keine. Die einzige extrahierte Kandidatenzeile bildet die oben dokumentierte Beziehung.
