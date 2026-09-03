# Fachlich normalisierte Formeln — S. 146

Quelle der Normalisierung: `formeln_s146.md`
Originaltranskript: `s146.md`
Buchseite: Hofenbitzer, Band 1, S. 146

## HOF-B1-S146-F01 — Saumweiten-Differenz der Bundfaltenhose

- **Fachlicher Zweck:** Die insgesamt zu reduzierende Saumweite aus gemessener und gewünschter Saumweite bestimmen.
- **Quelle:** `formeln_s146.md`, Zeile 9; Originaltranskript `s146.md`, Zeile 41; Buchseite 146.
- **Originalbezeichnung:** `SaW-Differenz = gemessene SaW - gewünschte SaW`
- **Normalisierte Bezeichnung:** `saumweiten_differenz_bundfaltenhose`

### Buchfassung

```text
- SaW-Differenz = gemessene SaW - gewünschte SaW = 54 cm - 34 cm = 20 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite_gemessen` | gemessene SaW | 54 | cm |
| `saumweite_gewuenscht` | gewünschte SaW | 34 | cm |

### Formel und Rechenschritte

```text
saumweiten_differenz = saumweite_gemessen - saumweite_gewuenscht
                      = 54 cm - 34 cm
                      = 20 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweiten_differenz` | insgesamt zu reduzierende Saumweite | 20 | cm |

- **Abhängigkeiten:** Gemessene und gewünschte Saumweite; die gemessene Saumweite ist in `HOF-B1-S146-F02` belegt.
- **Gültigkeitsbereich:** Modellentwicklung der Bundfaltenhose in Karottenform.
- **Technische Randbedingung:** Ein positives Ergebnis bezeichnet hier einen Abtrag beziehungsweise eine Reduzierung. Die im Transkript genannte Verteilung `¼ von 20 cm, hier 5 cm (zweimal)` ist als Buchangabe, aber nicht als eigene extrahierte Formel erhalten.
- **Offene Fragen oder Widersprüche:** Die Quelle legt nicht fest, wie die zwei seitlichen Beträge geometrisch auf Vorder- und Hinterhose verteilt werden.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Das Vorzeichen semantisch als Reduktionsfall kennzeichnen und die Verteilung auf die Schnittlinien getrennt modellieren.

## HOF-B1-S146-F02 — Gemessene Saumweite aus Vorder- und Hinterhose

- **Fachlicher Zweck:** Die gemessene gesamte Saumweite aus vorderer und hinterer Saumweite bestimmen.
- **Quelle:** `formeln_s146.md`, Zeile 14; Originaltranskript `s146.md`, Zeile 43; Buchseite 146.
- **Originalbezeichnung:** `gemessene SaW = vSaW + hSaW`
- **Normalisierte Bezeichnung:** `saumweite_gemessen_bundfaltenhose`

### Buchfassung

```text
- gemessene SaW = vSaW + hSaW = 25 cm + 29 cm = 54 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite_vorderhose` | vSaW | 25 | cm |
| `saumweite_hinterhose` | hSaW | 29 | cm |

### Formel und Rechenschritte

```text
saumweite_gemessen = saumweite_vorderhose + saumweite_hinterhose
                    = 25 cm + 29 cm
                    = 54 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `saumweite_gemessen` | gesamte gemessene Saumweite | 54 | cm |

- **Abhängigkeiten:** Gemessene Saumweiten der Vorder- und Hinterhose; Ausgabe ist Eingabe für `HOF-B1-S146-F01`.
- **Gültigkeitsbereich:** Modellentwicklung der Bundfaltenhose in Karottenform.
- **Technische Randbedingung:** Beide Teilweiten müssen an derselben Saumlinie des zu vermessenden Schnittes bestimmt werden.
- **Offene Fragen oder Widersprüche:** Keine; `25 cm + 29 cm = 54 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorder- und Hinterhosenanteil getrennt protokollieren und erst danach zur gemessenen Gesamtweite summieren.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s146.md` / `formeln_s147.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| S. 146, Zeilen 19–21 | 3 | Produktionsschnittteil- und Materialangaben für Paspelstreifen, Rückteil-Taschenbeutel und Patte; keine Rechenoperation |
| S. 147, Zeilen 9–18 | 10 | Produktionsschnittteil-, Oberstoff-, Futter- und Einschnittangaben; keine Rechenoperation |
| **Summe** | **13** | **Produktions- und Zuschnittangaben ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s146.md` enthält zusätzlich die Verteilungsangabe `¼ von 20 cm, hier 5 cm (zweimal)` in Zeile 40. Sie ist im Extrakt als Kandidat nicht als eigenständige Rechenzeile übernommen und wird deshalb hier nicht als separate Buchformel normalisiert. Die Konstruktionsanweisung zur Verteilung bleibt als Kontext der Saumweiten-Differenz sichtbar.
