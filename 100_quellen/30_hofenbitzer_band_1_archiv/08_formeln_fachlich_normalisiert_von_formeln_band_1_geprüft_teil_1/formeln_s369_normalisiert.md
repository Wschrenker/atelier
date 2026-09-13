# Fachlich normalisierte Formeln — S. 369

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/09_kragen_kapuzen_taschen_s290-369/formeln_s369_codex_v2.md`
Originaltranskript: `../hofenbitzer_band_1_digital/09_kragen_kapuzen_taschen_s290-369/s369_codex_v2.md`
Buchseite: Hofenbitzer, Band 1, S. 369

## HOF-B1-S369-F01 — Verlängerung um die doppelte Leistenbreite

- **Fachlicher Zweck:** Den Verlängerungsbetrag des durchgehenden Schnittteils für die rationelle Innentasche aus der Leistenbreite bestimmen.
- **Quelle:** `formeln_s369_codex_v2.md`, Zeile 17; Originaltranskript `s369_codex_v2.md`, Zeile 42; Buchseite 369.
- **Originalbezeichnung:** `um 2× Leistenbreite nach oben verlängern`
- **Normalisierte Bezeichnung:** `verlaengerung_doppelte_leistenbreite`

### Buchfassung

```text
1. Für das durchgehende Schnittteil die Leiste (dunkelgrün) mit dem Taschenbeutel kopieren und um 2× Leistenbreite nach oben verlängern.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `leistenbreite` | Leistenbreite | variabel | cm |
| `verlaengerungsfaktor` | 2× | 2 | dimensionslos |

### Formel und Rechenschritte

```text
verlaengerungsbetrag = leistenbreite * verlaengerungsfaktor
                      = leistenbreite * 2
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---|---|
| `verlaengerungsbetrag` | Verlängerung des durchgehenden Schnittteils nach oben | doppelte Leistenbreite | cm |

- **Abhängigkeiten:** Festgelegte Leistenbreite der Innentasche.
- **Gültigkeitsbereich:** Rationelle Innentasche beziehungsweise Brusttasche mit schmaler Leiste auf S. 369.
- **Technische Randbedingung:** Die Verlängerung erfolgt in der Konstruktion nach oben; die Richtung ist Geometrie und nicht Teil des skalaren Längenwerts.
- **Offene Fragen oder Widersprüche:** Keine; Faktor, Bezugsmaß und Verlängerungsrichtung sind eindeutig angegeben.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Betrag mit Faktor `2` berechnen und anschließend als gerichtete Verschiebung nach oben auf das kopierte Schnittteil anwenden.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s369_codex_v2.md`, Zeilen 9–12 | 4 | Schnittteil-, Material- und Zuschnittbeschriftungen; `1×` bezeichnet die Stückzahl, keine Berechnung |
| `formeln_s369_codex_v2.md`, Zeile 22 | 1 | Direkte Übertragung einer Taschenbeuteltiefe mit Faktor `1×`; keine neue Rechenbeziehung |
| `formeln_s369_codex_v2.md`, Zeile 27 | 1 | Schnittteil- und paarige Zuschnittbeschriftung; `2×-p` bezeichnet Stückzahl und paarigen Zuschnitt, keine Berechnung |
| `formeln_s369_codex_v2.md`, Zeile 32 | 1 | Schnittteil- und Zuschnittbeschriftung; keine Rechenformel |
| `formeln_s369_codex_v2.md`, Zeile 37 | 1 | Zeichnungslabel, das die bereits in `HOF-B1-S369-F01` vollständig belegte doppelte Leistenbreite wiederholt |
| **Summe** | **8** | **6 Produktions-/Zuschnittbeschriftungen, 1 direkte Maßübertragung und 1 Wiederholung ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript enthält außerhalb des verbindlichen Extrakts weitere Nahtzugaben, Eingriffs- und Lagebereiche sowie die Verdopplung einer Biesenbreite von `0,5 cm` auf eine Öffnung von `1 cm`. Diese Angaben wurden nicht als zusätzliche Buchfassungen erzeugt, weil sie im extrahierten Formelbestand fehlen. Die einmalige Taschenbeuteltiefe ist eine direkte Maßübertragung; das Zeichnungslabel `2× Leistenbreite` wiederholt die bereits vollständig extrahierte Verlängerungsanweisung. Der Abschluss von `M01` gilt für den vorhandenen extrahierten Kandidatenbestand.
