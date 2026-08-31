# Fachlich normalisierte Formeln — S. 452

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/11_modelle_kleider_blusen_westen_s438-464/formeln_s452.md`
Originaltranskript: `../hofenbitzer_band_1_digital/11_modelle_kleider_blusen_westen_s438-464/s452.md`
Buchseite: Hofenbitzer, Band 1, S. 452

## HOF-B1-S452-F01 — Abstand der Unterbrustnaht vom Brustpunkt

- **Fachlicher Zweck:** Den Abstand der Unterbrustnaht vom Brustpunkt für das Brustteil des Empire-Kleids bestimmen.
- **Quelle:** `formeln_s452.md`, Zeile 9; Originaltranskript `s452.md`, Zeile 12; Buchseite 452.
- **Originalbezeichnung:** `Abstand vom BrP` mit den Alternativen `ca. ½ BrB - 2 cm` oder `uBrA`.
- **Normalisierte Bezeichnung:** `unterbrustnaht_abstand_vom_brustpunkt`

### Buchfassung

```text
1. □2 Das Brustteil an der Unterbrust-Naht abtrennen. Der Abstand vom BrP ist je nach Brustgröße ca. ½ BrB - 2 cm oder uBrA. Das Rockteil abtrennen, die SN einstellen, den Brustabnäher schließen und die Ausschnitte formen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `brustbreite` | BrB | variabel | cm |
| `unterbrustabstand` | uBrA | variabel | cm |
| `abzugsbetrag` | `2 cm` | 2 | cm |
| `berechnungsweg` | Auswahl je nach Brustgröße | `brustbreite` oder `unterbrustabstand` | dimensionslos |

### Formel und Rechenschritte

```text
Weg A:
unterbrustnaht_abstand_vom_brustpunkt = ca. (0,5 * brustbreite) - 2 cm

Weg B:
unterbrustnaht_abstand_vom_brustpunkt = unterbrustabstand
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `unterbrustnaht_abstand_vom_brustpunkt` | Abstand der Unterbrustnaht vom Brustpunkt | abhängig vom gewählten Buchweg | cm |

- **Abhängigkeiten:** Brustbreite `BrB` für Weg A oder gemessener Unterbrustabstand `uBrA` für Weg B; ausdrücklich gewählter Berechnungsweg.
- **Gültigkeitsbereich:** Brustteil des Trägerkleids im Empire-Stil auf S. 452.
- **Technische Randbedingung:** Das Buch stellt beide Wege als Alternativen dar. `ca.` kennzeichnet Weg A als Näherung. Ohne belegte Schwelle darf der Weg nicht automatisch aus einer Brustgröße abgeleitet werden.
- **Offene Fragen oder Widersprüche:** Die Quelle sagt nur „je nach Brustgröße“ und nennt keine Grenze oder Auswahlregel zwischen den beiden Wegen. Die beiden Beziehungen selbst sind eindeutig; die Auswahl muss bis zu einem weiteren Beleg von außen vorgegeben werden.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Beide Wege als ausdrücklich auswählbare Varianten implementieren. Keine Schwelle für die Brustgröße erfinden; bei Weg A den Näherungscharakter erhalten und bei Weg B den Messwert `uBrA` direkt verwenden.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s452.md`, Zeile 14 | 1 | Schnittteil- und Zuschnittbeschriftungen mit `2×` und `1×`; Produktionsangaben, keine Berechnung |
| `formeln_s452.md`, Zeile 19 | 1 | Fotozuordnungs- und Provenienzzeile; keine Rechenformel |
| **Summe** | **2** | **1 Produktionsbeschriftung und 1 Provenienzzeile ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript nennt außerhalb des verbindlichen Extrakts auf S. 452 weitere Reduzierbereiche für Ausschnitt-, Armloch- und Brustweite sowie konstruktive Gleichheitsanforderungen an Faltenlinien. Diese Stellen wurden nicht als zusätzliche Buchfassungen erzeugt. Der Abschluss von `M07` gilt für den vorhandenen extrahierten Kandidatenbestand.
