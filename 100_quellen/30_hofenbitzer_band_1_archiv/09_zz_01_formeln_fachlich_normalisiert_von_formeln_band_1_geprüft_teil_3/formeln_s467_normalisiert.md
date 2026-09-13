# Fachlich normalisierte Formeln — S. 467

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s467.md`
Originaltranskript: `s467.md`
Buchseite: Hofenbitzer, Band 1, S. 467

## HOF-B1-S467-F01 — Verlängerung des hinteren Taschenbeutels aus der Biesentiefe

- **Fachlicher Zweck:** Den hinteren Taschenbeutel (hTb) so weit verlängern, dass die untere Naht des Taschenspiegels in der Biese versäubert werden kann.
- **Quelle:** `formeln_s467.md`, Zeile 14; Originaltranskript `s467.md`, Zeile 22; Buchseite 467.
- **Originalbezeichnung:** `Den hTb je nach Verarbeitung um 1 cm verlängern. Das entspricht 2× der Biesentiefe (0,5 cm)`
- **Normalisierte Bezeichnung:** `hinterer_taschenbeutel_verlaengerung_aus_biesentiefe`

### Buchfassung

```text
17. Den hTb je nach Verarbeitung um 1 cm verlängern. Das entspricht 2× der Biesentiefe (0,5 cm), um die untere TSp-Naht darin zu versäubern.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `biesentiefe` | Biesentiefe | 0,5 | cm |
| `biesen_lagen_faktor` | `2×` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
hinterer_taschenbeutel_verlaengerung = biesen_lagen_faktor * biesentiefe

Buchwerte:
hinterer_taschenbeutel_verlaengerung = 2 * 0,5 cm = 1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hinterer_taschenbeutel_verlaengerung` | Verlängerung des hinteren Taschenbeutels gegenüber der oberen Leistenkante | cm |

- **Abhängigkeiten:** Kopierte Grundkontur des hinteren Taschenbeutels bis zur oberen Leistenkante (Schritt 16) und die gewählte Biesentiefe.
- **Gültigkeitsbereich:** Versenkte Leistentasche der einfachen Jacke (Janker), Taschenkonstruktion Schritte 12–21.
- **Technische Randbedingung:** Der Faktor `2` bildet die beiden Lagen der Biese ab. Die Quelle nennt nur die Verarbeitungsvariante mit `0,5 cm` Biesentiefe; eine allgemeine Auswahlregel für andere Biesentiefen ist nicht belegt.
- **Offene Fragen oder Widersprüche:** `je nach Verarbeitung` bleibt unbestimmt. Das Buch nennt keine Aufzählung der Verarbeitungsvarianten und keine Bedingung, wann eine andere Verlängerung als `1 cm` gilt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Biesentiefe als Eingabe führen und den Buchwert `0,5 cm` nur als Vorgabewert setzen. `2 × 0,5 cm = 1 cm` ist rechnerisch konsistent und eignet sich als Regressionsprüfung.

## Ausgeschlossene Kandidaten

| Zeile in `formeln_s467.md` | Kandidat | Ausschlussgrund |
|---|---|---|
| 9 | `12. □5+6 Leiste der Tasche positionieren und` | Abbildungsverweis und Konstruktionsanweisung ohne Rechenoperation |
| 19 | `vorderer Taschenbeutel vTb 2× Fu Janker G 38` | Produktionsschnittteil mit Stückzahl-, Material- und Größenangabe |
| 20 | `hinterer Taschenbeutel hTb 2× Fu Janker G 38` | Produktionsschnittteil mit Stückzahl-, Material- und Größenangabe |
| 21 | `Taschenspiegel (TSp) 2× OSt Janker G 38` | Produktionsschnittteil mit Stückzahl-, Material- und Größenangabe |
| 22 | `Leiste (Le) 2× OSt + El Janker G 38` | Produktionsschnittteil mit Stückzahl-, Material- und Größenangabe |

**Summe:** 5 ausgeschlossene von 6 extrahierten Kandidatenzeilen.

## Prüfhinweise

1. Das `2×` in den Produktionsschnittteilen ist eine Stückzahl je Schnittteil, keine Rechenoperation. Es unterscheidet sich vom `2×` der Biesentiefe in Zeile 14, das dort einen Faktor bildet.
2. Im Originaltranskript stehen weitere Maße (`ca. 3 bis 4 cm`, `ca. 5 bis 10 cm`, `½ Leistenbreite`, `1 bis 1,5 cm NZg`), die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen. Sie wurden nicht stillschweigend als Buchfassungen ergänzt.
