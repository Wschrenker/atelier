# Fachlich normalisierte Formeln — S. 129

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/formeln_s129.md`
Originaltranskript: `../Band_1_geprüft_v1/s129.md`
Buchseite: Hofenbitzer, Band 1, S. 129

## HOF-B1-S129-F01 — Vorderer Hosenausschnitt der weiterreduzierten engen Hose

- **Fachlicher Zweck:** Den vorderen Hosenausschnitt aus der reduzierten Vorderhosenbreite mit einem wählbaren Abzug bestimmen.
- **Quelle:** `formeln_s129.md`, Zeile 19; Originaltranskript `s129.md`, Zeile 40; Buchseite 129.
- **Originalbezeichnung:** `vHoB : 4 -0 bis -0,7 (-0,7)`
- **Normalisierte Bezeichnung:** `vorderer_hosenausschnitt_weiterreduzierte_enge_hose`

### Buchfassung

```text
- vHoB : 4 -0 bis -0,7 (-0,7)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderhosenbreite_reduziert` | vHoB | 20,8 | cm |
| `abzug_vorderer_hosenausschnitt` | 0 bis 0,7 cm | gewählt 0,7 | cm |

### Formel und Rechenschritte

```text
vorderer_hosenausschnitt_max = (vorderhosenbreite_reduziert / 4) - 0 cm
                              = (20,8 cm / 4) - 0 cm
                              = 5,2 cm
vorderer_hosenausschnitt_min = (vorderhosenbreite_reduziert / 4) - 0,7 cm
                              = 4,5 cm
Buchwahl                     = 4,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich im Buchbeispiel | Einheit |
|---|---|---:|---|
| `vorderer_hosenausschnitt` | Viertelbetrag der Vorderhosenbreite nach Abzug | 4,5 bis 5,2; gewählt 4,5 | cm |

- **Abhängigkeiten:** Reduzierte Vorderhosenbreite aus dem reduzierten Hüftumfang; Tabellenwert auf S. 128.
- **Gültigkeitsbereich:** Vorderhose der weiterreduzierten engen Hose auf S. 129.
- **Technische Randbedingung:** Die gedruckte Reihenfolge führt vom größeren Ergebnis bei Abzug 0 zum kleineren Ergebnis bei Abzug 0,7 cm; die Grenzen sind nach dem Ergebnis benannt.
- **Offene Fragen oder Widersprüche:** Keine; die Klammer kennzeichnet die im Buch gewählte Abzugsvariante 0,7 cm.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Abzug innerhalb des belegten Bereichs validieren und Ergebnisgrenzen numerisch sortieren.

## HOF-B1-S129-F02 — Hinterer Hosenausschnitt der weiterreduzierten engen Hose

- **Fachlicher Zweck:** Den hinteren Hosenausschnitt aus der reduzierten Hinterhosenbreite mit einem wählbaren Zuschlag bestimmen.
- **Quelle:** `formeln_s129.md`, Zeile 51; Originaltranskript `s129.md`, Zeile 74; Buchseite 129.
- **Originalbezeichnung:** `hHoB : 4 +0,5 bis 1 cm (0,7), übertragen`
- **Normalisierte Bezeichnung:** `hinterer_hosenausschnitt_weiterreduzierte_enge_hose`

### Buchfassung

```text
- hHoB : 4 +0,5 bis 1 cm (0,7), übertragen
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hinterhosenbreite_reduziert` | hHoB | 22,8 | cm |
| `zuschlag_hinterer_hosenausschnitt` | 0,5 bis 1 cm | gewählt 0,7 | cm |

### Formel und Rechenschritte

```text
hinterer_hosenausschnitt_min = (hinterhosenbreite_reduziert / 4) + 0,5 cm
                              = (22,8 cm / 4) + 0,5 cm
                              = 6,2 cm
hinterer_hosenausschnitt_max = (hinterhosenbreite_reduziert / 4) + 1 cm
                              = 6,7 cm
Buchwahl                     = (22,8 cm / 4) + 0,7 cm
                              = 6,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wertebereich im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hinterer_hosenausschnitt` | Viertelbetrag der Hinterhosenbreite nach Zuschlag | 6,2 bis 6,7; gewählt 6,4 | cm |

- **Abhängigkeiten:** Reduzierte Hinterhosenbreite aus dem reduzierten Hüftumfang; Tabellenwert auf S. 128.
- **Gültigkeitsbereich:** Hinterhose der weiterreduzierten engen Hose auf S. 129.
- **Technische Randbedingung:** Die Klammer kennzeichnet den gewählten Zuschlag; `übertragen` ist eine Konstruktionsanweisung und kein weiterer Rechenschritt.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zuschlag als wählbaren Parameter führen und die Übertragung geometrisch getrennt von der Maßberechnung ausführen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s129.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 9 und 36 | 2 | Zeichnungslabels `TaU : 4`; reine, doppelte Teilwertbeschriftung ohne bezeichnete Ausgabe |
| Zeile 14 | 1 | `HüU : 20 +3 cm`; Wiederholung des bereits als offen erfassten Ausdrucks `HOF-B1-S125-F01`, weiterhin ohne geometrischen Referenten |
| Zeilen 24–26 | 3 | Knieweitenbetrag und Wadenweitenbetrag sind Wiederholungen von `HOF-B1-S128-F03` und `F04`; Wadenhöhe ist Wiederholung von `HOF-B1-S123-F01` |
| Zeile 31 | 1 | Saumweitenbetrag; Wiederholung der Beziehung aus `HOF-B1-S124-F04`, hier als reines Zeichnungslabel |
| Zeile 41 | 1 | Bereich `9 - 12 cm` ohne Rechenoperator, Bezug oder bezeichnete Ausgabe; Konstruktionsmaß |
| Zeile 46 | 1 | Gewählter Gesäßwinkel `α = 76°`; Eingabewert, keine berechnete Formel |
| **Summe** | **9** | **7 Wiederholungen oder Labels und 2 Eingabewerte ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s129.md` enthält weitere formelartige Konstruktionsangaben, die nicht vollständig im verbindlichen Extrakt vertreten sind, insbesondere die vordere Taillenlinie mit Zugabe in den Zeilen 31–34, die Sitzhöhenreduzierung in Zeile 36, die Zusammensetzung der gemessenen Oberschenkelweite in Zeile 51, die hintere Taillenlinie mit Gegenrechnung der Vorderhosenzugabe und Abnäherinhalt in den Zeilen 64–66 sowie Nahtübertragungen und beidseitige Zugaben in den Zeilen 77–80. Sie wurden nicht stillschweigend normalisiert. Der Abschluss von `H03` gilt für den vorhandenen extrahierten Kandidatenbestand.
