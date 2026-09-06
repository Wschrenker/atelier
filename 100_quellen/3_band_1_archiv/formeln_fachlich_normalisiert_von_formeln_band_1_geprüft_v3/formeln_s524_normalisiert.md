# Fachlich normalisierte Formeln — S. 524

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s524.md`  
Originaltranskript: `s524.md`  
Buchseite: Hofenbitzer, Band 1, S. 524

Die Seite ergänzt den engen Oberteil-Grundschnitt zum Body-Grundschnitt Variante 1. Die Beziehungen betreffen die verbleibende halbe Taillenweite, die verbleibende halbe Hüftweite und den Abstand `HüW : 10` unterhalb der Hüftlinie.

## HOF-B1-S524-F01 — Verbleibende halbe Taillenweite

- **Fachlicher Zweck:** Die Summe aus vorderer und hinterer Taillenweite auf ungefähr die halbe Taillenweite begrenzen.
- **Quelle:** `formeln_s524.md`, Zeile 14; Originaltranskript `s524.md`, Zeile 33; Buchseite 524.
- **Originalbezeichnung:** `vTaW + hTaW = ca. ½ TaW`.
- **Normalisierte Bezeichnung:** `body_halbe_taillenweite_verbleibend`

### Buchfassung
```text
- vTaW + hTaW = ca. ½ TaW
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `vordere_taillenweite` | vTaW | variabel | cm |
| `hintere_taillenweite` | hTaW | variabel | cm |
| `halber_taillenumfang` | ½ TaW | variabel | cm |

### Formel und Rechenschritte
```text
verbleibende_taillenweite = vordere_taillenweite + hintere_taillenweite
verbleibende_taillenweite ≈ halber_taillenumfang
```

### Ausgabe
| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `verbleibende_taillenweite` | Summe der Taillenweiten von VT und RT | cm |

- **Abhängigkeiten:** vTaW, hTaW und TaW des weitenreduzierten Grundschnitts.
- **Gültigkeitsbereich:** Body-Grundschnitt Variante 1, Maschenware.
- **Offene Fragen oder Widersprüche:** `ca.` bezeichnet eine Näherung; eine Toleranz oder Verteilung auf VT und RT ist nicht angegeben.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Näherungs-/Kontrollbedingung führen, nicht als starre Gleichung mit automatisch verteilter Weite.

## HOF-B1-S524-F02 — Verbleibende halbe Hüftweite

- **Fachlicher Zweck:** Die Summe aus vorderer und hinterer Hüftbreite auf ungefähr die halbe Hüftweite abstimmen.
- **Quelle:** `formeln_s524.md`, Zeile 19; Originaltranskript `s524.md`, Zeile 36; Buchseite 524.
- **Originalbezeichnung:** `vHüB + hHüB = ca. ½ HüW`.
- **Normalisierte Bezeichnung:** `body_halbe_hueftweite_verbleibend`

### Buchfassung
```text
- vHüB + hHüB = ca. ½ HüW
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `vordere_hueftbreite` | vHüB | variabel | cm |
| `hintere_hueftbreite` | hHüB | variabel | cm |
| `halbe_hueftweite` | ½ HüW | variabel | cm |

### Formel und Rechenschritte
```text
verbleibende_hueftweite = vordere_hueftbreite + hintere_hueftbreite
verbleibende_hueftweite ≈ halbe_hueftweite
```

### Ausgabe
| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `verbleibende_hueftweite` | Summe der Hüftbreiten von VT und RT | cm |

- **Abhängigkeiten:** vHüB, hHüB und HüW des weitenreduzierten Grundschnitts.
- **Gültigkeitsbereich:** Body-Grundschnitt Variante 1, Maschenware.
- **Offene Fragen oder Widersprüche:** `ca.` bezeichnet eine Näherung; die Seite legt keine Toleranz fest.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Kontrollbedingung modellieren; einen verbleibenden Fehlbetrag nicht ohne weitere Buchregel verteilen.

## HOF-B1-S524-F03 — Abstand unterhalb der Hüftlinie

- **Fachlicher Zweck:** Eine Parallele unterhalb der Hüftlinie im Abstand eines Zehntels der Hüftweite anlegen.
- **Quelle:** `formeln_s524.md`, Zeile 19; Originaltranskript `s524.md`, Zeile 37; Buchseite 524.
- **Originalbezeichnung:** `HüW : 10`.
- **Normalisierte Bezeichnung:** `body_abstand_unter_hueftlinie`

### Buchfassung
```text
- HüW : 10
```

### Eingaben
| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `hueftweite` | HüW | variabel | cm |
| `zehntel_faktor` | `10` | 10 | dimensionslos |

### Formel und Rechenschritte
```text
abstand_unter_hueftlinie = hueftweite / 10
```

### Ausgabe
| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abstand_unter_hueftlinie` | Abstand der Parallele unter der Hüftlinie | cm |

- **Abhängigkeiten:** HüW des Grundschnitts.
- **Gültigkeitsbereich:** Body-Grundschnitt Variante 1, Schritt 4.
- **Offene Fragen oder Widersprüche:** Kein eingesetzter Buchwert vorhanden.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Abstand als Längenwert berechnen und senkrecht zur Hüftlinie anlegen.

## Ausgeschlossene Kandidaten

Keine: Die drei extrahierten Beziehungen sind als Formelbestand abgebildet. Modell-, Maß- und Konstruktionsangaben ohne Rechenoperation wurden nicht als zusätzliche Formel aufgenommen.
