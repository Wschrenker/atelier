# Fachlich normalisierte Formeln — S. 114

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s114.md`
Originaltranskript: `s114.md`
Buchseite: Hofenbitzer, Band 1, S. 114

## HOF-B1-S114-F01 — Hinterer Hosenausschnitt nach Gesäßform

- **Fachlicher Zweck:** Den Abtrag für den hinteren Hosenausschnitt aus der Hinterhosenbreite und der gewählten Gesäßform bestimmen.
- **Quelle:** `formeln_s114.md`, Zeilen 9 und 14; Originaltranskript `s114.md`, Zeilen 27 und 31; Buchseite 114.
- **Originalbezeichnung:** `hHoB : 4` mit gesäßformabhängigem Abzug oder Zuschlag.
- **Normalisierte Bezeichnung:** `hinterer_hosenausschnitt_nach_gesaessform`

### Buchfassung

```text
hHoB : 4 − 0,5 bis −1 cm
```

```text
hHoB : 4 + 0,5 bis +1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hinterhosenbreite` | hHoB | variabel | cm |
| `gesaessform` | stark oder flach | explizite Auswahl | dimensionslos |
| `ausschnitt_anpassung` | gesäßformabhängiger Bereich | explizite Auswahl | cm |

### Formel und Rechenschritte

```text
basisabtrag = hinterhosenbreite / 4
abtrag_hinterer_hosenausschnitt = basisabtrag + ausschnitt_anpassung

Starkes Gesäß: -1 cm <= ausschnitt_anpassung <= -0,5 cm
Flaches Gesäß: 0,5 cm <= ausschnitt_anpassung <= 1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abtrag_hinterer_hosenausschnitt` | von P24 nach rechts abzutragender Wert | cm |

- **Abhängigkeiten:** hHoB und ausdrücklich gewählte Gesäßform samt Wert innerhalb ihres Bereichs.
- **Gültigkeitsbereich:** Hinterhose des Standardhosen-Grundschnitts auf S. 114.
- **Technische Randbedingung:** Ein kleinerer Abtrag vergrößert laut Seitenkontext den hinteren Hosenausschnitt; ein größerer Abtrag verkleinert ihn.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine Schwellenwerte für die Klassifikation und keine Auswahlregel innerhalb der Bereiche. Der normale Grundwert `hHoB : 4` steht nur im Transkriptkontext und nicht als eigener Buchfassungsblock im Extrakt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Gesäßform und signierten Anpassungswert getrennt validieren; den nicht extrahierten Normalfall nicht als zusätzliche Buchfassung ausgeben.

## Ausgeschlossene Kandidaten

| Extraktzeilen | Anzahl | Ausschlussgrund |
|---|---:|---|
| 19 | 1 | Gewählter Gesäßwinkel `84°`; Eingabewert ohne Berechnung |
| 20 | 1 | Gleichsetzung von oberem Hinterhosenbruch und hinterer Bügelkante; geometrische Begriffsdefinition |
| **Summe** | **2** | **1 Eingabewert + 1 Definition** |
