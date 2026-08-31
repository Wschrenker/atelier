# Fachlich normalisierte Formeln — S. 409

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s409_codex_v2.md`
Originaltranskript: `../Band_1_geprüft_v1/s409_codex_v2.md`
Buchseite: Hofenbitzer, Band 1, S. 409

## HOF-B1-S409-F01 — Ganze Taillennahtlänge des Rückenteils aus ihrer halben Länge

- **Fachlicher Zweck:** Die für die rückwärtige Taillenblende zu berücksichtigende ganze Taillennahtlänge aus der Länge einer halben Rückenteil-Taillennaht bestimmen.
- **Quelle:** `formeln_s409_codex_v2.md`, Zeile 19; Originaltranskript `s409_codex_v2.md`, Zeile 36; Buchseite 409.
- **Originalbezeichnung:** `2× Länge der halben Taillennaht am RT`.
- **Normalisierte Bezeichnung:** `ganze_taillennahtlaenge_rueckenteil`

### Buchfassung

```text
- 2× Länge der halben Taillennaht am RT
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `halbe_taillennahtlaenge_rueckenteil` | Länge der halben Taillennaht am RT | variabel | Längeneinheit |
| `verdopplungsfaktor` | `2×` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
ganze_taillennahtlaenge_rueckenteil = verdopplungsfaktor * halbe_taillennahtlaenge_rueckenteil
                                     = 2 * halbe_taillennahtlaenge_rueckenteil
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `ganze_taillennahtlaenge_rueckenteil` | zweifache Länge der halben Taillennaht am RT | variabel | gleiche Längeneinheit wie die Eingabe |

- **Abhängigkeiten:** Gemessene Länge der halben Taillennaht am Rückenteil.
- **Gültigkeitsbereich:** Entwicklung der Taillenblenden mit angeschnittenen Bindebändern für die Wickel-Form auf S. 409.
- **Technische Randbedingung:** Der Faktor `2` ist nur anwendbar, wenn die gemessene Strecke tatsächlich eine Hälfte der gesamten rückwärtigen Taillennaht darstellt. Die Quelle nennt keinen Zahlenwert und keine konkrete Längeneinheit.
- **Offene Fragen oder Widersprüche:** Keine. Die Beziehung ist als Verdopplung eindeutig; ein Zahlenbeispiel ist nicht gedruckt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Eine Längengröße einheitenstabil mit dem dimensionslosen Faktor `2` multiplizieren; keine feste Einheit oder einen nicht gedruckten Zahlenwert einsetzen.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s409_codex_v2.md`, Zeile 9 | 1 | Bildnummernverweis `□4+5` und Konstruktionsanweisung für Rückschnitte; das Pluszeichen verbindet Bildnummern und ist kein Rechenoperator |
| `formeln_s409_codex_v2.md`, Zeile 14 | 1 | Schnittteil- und Zuschnittbeschriftungen mit `1×` und `2×-p`; Produktionsangaben, keine Berechnung |
| `formeln_s409_codex_v2.md`, Zeile 20 | 1 | `2× übertragen` ist eine direkte Übertragungsanweisung ohne bezeichnete berechnete Ausgabe |
| `formeln_s409_codex_v2.md`, Zeile 25 | 1 | Produktionsbeschriftung `2×-p / 3`; Stückzahl, Zuschnittart und Schnittteilnummer, keine Berechnung |
| **Summe** | **4** | **4 Bildverweis-, Produktions- oder Übertragungszeilen ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript enthält außerhalb des verbindlichen Extrakts weitere Maße und Beziehungen, darunter `2,2` und `wie am VT hier 4,4`, die gesamte Taillennaht am VT sowie eine Bindebandlänge von `50 cm`. Der Extrakt bildet daraus nur die Verdopplung der halben RT-Taillennaht vollständig als Beziehung ab. Die übrigen Stellen wurden nicht als zusätzliche Buchfassungen erzeugt. Der Abschluss von `M04` gilt für den vorhandenen extrahierten Kandidatenbestand.
