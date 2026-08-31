# Fachlich normalisierte Formeln — S. 368

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s368_codex_v2.md`
Originaltranskript: `../Band_1_geprüft_v1/s368_codex_v2.md`
Buchseite: Hofenbitzer, Band 1, S. 368

## HOF-B1-S368-F01 — Nahtzugabe als halbe Paspelbreite

- **Fachlicher Zweck:** Die Nahtzugabe an der Paspel aus der vorgesehenen Paspelbreite bestimmen.
- **Quelle:** `formeln_s368_codex_v2.md`, Zeile 30; Originaltranskript `s368_codex_v2.md`, Zeile 89; Buchseite 368.
- **Originalbezeichnung:** `NZg = ½ Paspelbreite`
- **Normalisierte Bezeichnung:** `nahtzugabe_halbe_paspelbreite`

### Buchfassung

```text
- `NZg = ½ Paspelbreite`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `paspelbreite` | Paspelbreite | variabel; im Seitenkontext ca. 1 | cm |
| `anteil_nahtzugabe` | ½ | 0,5 | dimensionslos |

### Formel und Rechenschritte

```text
nahtzugabe_paspel = paspelbreite * 0,5

Seitenbeispiel aus dem Originalkontext:
nahtzugabe_paspel = 1 cm * 0,5
                     = 0,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `nahtzugabe_paspel` | Nahtzugabe an der Paspel | halbe Paspelbreite; im Seitenbeispiel 0,5 | cm |

- **Abhängigkeiten:** Vorgesehene Paspelbreite.
- **Gültigkeitsbereich:** Pattentasche mit unten liegender Paspel auf S. 368.
- **Technische Randbedingung:** Paspelbreite und Nahtzugabe müssen in derselben Längeneinheit geführt werden. Der Kontextwert `ca. 1 cm` steht im Originaltranskript, aber nicht im verbindlichen extrahierten Formelblock; er ist deshalb nur eine gekennzeichnete Kontextkontrolle.
- **Offene Fragen oder Widersprüche:** Keine; die Halbierungsbeziehung ist eindeutig. Der ungefähre Kontextwert liefert nur ein Beispiel und keine feste Paspelbreite.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Paspelbreite als Eingabe führen und die Nahtzugabe exakt mit dem Faktor `0.5` berechnen.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s368_codex_v2.md`, Zeilen 9–11 | 3 | Schnittteil-, Material- und Zuschnittbeschriftungen; `1×` bezeichnet die Stückzahl, keine Berechnung |
| `formeln_s368_codex_v2.md`, Zeile 16 | 1 | Bildverweis `□2+3`; das Pluszeichen verbindet Abbildungsnummern und ist kein Rechenoperator |
| `formeln_s368_codex_v2.md`, Zeilen 21–24 | 4 | Schnittteil-, Material- und Zuschnittbeschriftungen; keine Rechenformeln |
| `formeln_s368_codex_v2.md`, Zeile 29 | 1 | Schnittteil- und Zuschnittbeschriftung der Paspel; keine Rechenformel |
| **Summe** | **9** | **8 Produktions-/Zuschnittbeschriftungen und 1 Bildverweis ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript enthält außerhalb des verbindlichen Extrakts weitere feste Maße, Versätze, Nahtzugaben und Kopier- beziehungsweise Spiegelanweisungen für Brustleisten- und Pattentaschen. Sie beschreiben Eingaben oder geometrische Konstruktionsschritte, bilden im Extrakt aber keine weiteren vollständigen Rechenbeziehungen. Der Abschluss von `M01` gilt für den vorhandenen extrahierten Kandidatenbestand.
