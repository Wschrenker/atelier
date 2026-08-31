# Fachlich normalisierte Formeln — S. 371

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/10_ausschnitte_s370-437/formeln_s371_codex_v2.md`
Originaltranskript: `../hofenbitzer_band_1_digital/10_ausschnitte_s370-437/s371_codex_v2.md`
Buchseite: Hofenbitzer, Band 1, S. 371

## HOF-B1-S371-F01 — Verkleinerung des Armdurchmessers für ein ärmelloses Oberteil

- **Fachlicher Zweck:** Den Armdurchmesser des Oberteil-Grundschnitts für das ärmellose Modell um den angegebenen Gesamtbetrag verkleinern.
- **Quelle:** `formeln_s371_codex_v2.md`, Zeile 9; Originaltranskript `s371_codex_v2.md`, Zeile 13; Buchseite 371.
- **Originalbezeichnung:** `Armdurchmesser (ArD+) um insgesamt ca. 1,5 cm verkleinert`
- **Normalisierte Bezeichnung:** `armdurchmesser_aermelloses_oberteil`

### Buchfassung

```text
3. Da es sich um ein Modell ohne Ärmel handelt, wird der Armdurchmesser (ArD+) um insgesamt ca. 1,5 cm verkleinert.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armdurchmesser_grundschnitt` | Armdurchmesser (ArD+) vor der Modelländerung | variabel | cm |
| `armdurchmesser_reduktion` | gesamte Verkleinerung | ca. 1,5 | cm |

### Formel und Rechenschritte

```text
armdurchmesser_modell = armdurchmesser_grundschnitt - armdurchmesser_reduktion
                       = armdurchmesser_grundschnitt - ca. 1,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---|---|
| `armdurchmesser_modell` | verkleinerter Armdurchmesser des ärmellosen Modells | Grundschnittwert minus ca. 1,5 | cm |

- **Abhängigkeiten:** Armdurchmesser des verwendeten Oberteil-Grundschnitts.
- **Gültigkeitsbereich:** Sehr lockeres, ärmelloses Oberteil in A- beziehungsweise Hängerform auf S. 371.
- **Technische Randbedingung:** `ca. 1,5 cm` ist ein ungefährer Gesamtbetrag; die Quelle legt keine Toleranz und keine Verteilung auf Vorder- und Rückenteil fest.
- **Offene Fragen oder Widersprüche:** Die konkrete geometrische Verteilung der Gesamtverkleinerung ist nicht belegt. Die skalare Reduktionsbeziehung selbst ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Gesamtbetrag als konfigurierbaren Näherungswert führen; seine geometrische Verteilung erst nach einem eigenen Quellenbeleg implementieren.

## Ausgeschlossene Kandidaten

Keine. Die einzige extrahierte Kandidatenzeile ist vollständig in einem Formelblock abgebildet.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript enthält außerhalb des verbindlichen Extrakts weitere feste Ausstell-, Verlängerungs- und Armloch-Auflockerungsbeträge. Sie sind nicht als zusätzliche Buchfassungen extrahiert und wurden hier nicht stillschweigend normalisiert. Der Abschluss von `M02` gilt für den vorhandenen extrahierten Kandidatenbestand.
