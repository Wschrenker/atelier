# Fachlich normalisierte Formeln — S. 219

Quelle der Normalisierung: `formeln_s219_digital_geprüft.md`
Originaltranskript: `s219_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 219
Extraktionsstand: v2

## HOF-B1-S219-F01 — Senkrechter Öffnungsbetrag nach Schulterpolster-Mehrweite

- **Fachlicher Zweck:** Den verbleibenden senkrechten Öffnungsbetrag bestimmen, nachdem die durch die waagerechte Schulterpolster-Öffnung erzeugte Mehrweite von der Fehlweite abgezogen wurde.
- **Quelle:** `formeln_s219_digital_geprüft.md`, Zeilen 9 und 14; Originaltranskript `s219_digital_geprüft.md`, Zeilen 7–13; Buchseite 219.
- **Originalbezeichnung:** Öffnung, Fehlweite, ⅔ SuPoE
- **Normalisierte Bezeichnung:** `senkrechter_oeffnungsbetrag_nach_schulterpolster_mehrweite`

### Buchfassung

Allgemeine Beziehung:

```text
Öffnung = Fehlweite − ⅔ SuPoE
```

Buchrechnung:

```text
hier = 5,2 cm − 1,7 cm = 4,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `fehlweite` | Fehlweite | cm |
| `schulterpolster_mehrweite_beidseitig` | ⅔ SuPoE | cm |

### Formel und Rechenschritte

```text
senkrechter_oeffnungsbetrag = fehlweite - schulterpolster_mehrweite_beidseitig
gedruckte_einsetzung = 5,2 cm - 1,7 cm
gedruckte_operanden_ergeben = 3,5 cm
gedrucktes_ergebnis = 4,5 cm
exakter_zweidrittelweg = 5,2 cm - ((2 / 3) * 2,5 cm)
exakter_zweidrittelweg = 3,533333... cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `senkrechter_oeffnungsbetrag` | verbleibender senkrechter Öffnungsbetrag | cm |

- **Abhängigkeiten:** Positive Fehlweite aus `HOF-B1-S218-F03` und beidseitige Schulterpolster-Mehrweite aus `HOF-B1-S218-F04`.
- **Gültigkeitsbereich:** Fortsetzung der Ärmelanpassung von S. 218 für Schulterpolster-Erhöhung und Armlochauflockerung.
- **Technische Randbedingung:** Der Öffnungsbetrag darf erst umgesetzt werden, wenn der widersprüchliche Buchwert fachlich oder am physischen Buch geklärt ist.
- **Offene Fragen oder Widersprüche:** `5,2 cm − 1,7 cm` ergibt `3,5 cm`, nicht `4,5 cm`. Auch der exakte Zweidrittelwert aus `2,5 cm` führt zu rund `3,53 cm`. Damit widerspricht das gedruckte Ergebnis sowohl der gedruckten Einsetzung als auch dem exakten allgemeinen Weg.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Keine der möglichen Zahlen stillschweigend auswählen. Allgemeine Formel, Ergebnis aus gedruckten Operanden und gedrucktes Ergebnis getrennt erhalten, bis die Quelle und die fachliche Absicht geprüft sind.

## HOF-B1-S219-F02 — Fehlbetrag des nachgemessenen neuen Ärmelkugelumfangs

- **Fachlicher Zweck:** Die noch fehlende Nahtlänge der angepassten Ärmelkugel gegenüber dem gewünschten neuen Ärmelkugelumfang bestimmen.
- **Quelle:** `formeln_s219_digital_geprüft.md`, Zeilen 19 und 24; Originaltranskript `s219_digital_geprüft.md`, Zeilen 25–31; Buchseite 219.
- **Originalbezeichnung:** Fehlbetrag, ÄkU_NEU, nachgemessene neue ÄkU
- **Normalisierte Bezeichnung:** `fehlbetrag_neuer_aermelkugelumfang`

### Buchfassung

Allgemeine Beziehung:

```text
Fehlbetrag = ÄkU_NEU − nachgemessene neue ÄkU
```

Buchrechnung:

```text
hier = 53,7 cm − 52,5 cm = 1,2 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `aermelkugelumfang_neu_soll` | ÄkU_NEU | cm |
| `aermelkugelumfang_neu_gemessen` | nachgemessene neue ÄkU | cm |

### Formel und Rechenschritte

```text
fehlbetrag_aermelkugelumfang = aermelkugelumfang_neu_soll - aermelkugelumfang_neu_gemessen
fehlbetrag_aermelkugelumfang = 53,7 cm - 52,5 cm
fehlbetrag_aermelkugelumfang = 1,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `fehlbetrag_aermelkugelumfang` | noch fehlende Nahtlänge am neuen Ärmelkugelumfang | cm |

- **Abhängigkeiten:** Gewünschter neuer Ärmelkugelumfang aus S. 218 und nach der Anpassung über alle Öffnungen hinweg gemessener tatsächlicher Ärmelkugelumfang.
- **Gültigkeitsbereich:** Kontrollschritt nach der Ärmelanpassung auf S. 218–219.
- **Technische Randbedingung:** Beide Umfänge müssen entlang derselben Nahtlinie und mit derselben Messmethode bestimmt werden.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Unstimmigkeit; `53,7 − 52,5 = 1,2`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Soll- und Messwert getrennt erfassen. Die anschließend im Transkript beschriebene Verwendung der Hälfte des Fehlbetrags ist nicht Teil des verbindlichen Extrakts und darf hier nicht automatisch ergänzt werden.

## Ausgeschlossene Kandidaten

Keine. Alle 4 extrahierten Kandidatenzeilen sind in den beiden Formelblöcken abgebildet.

## Extraktionsgrenze

Das Originaltranskript beschreibt in Zeilen 35–37 die Erhöhung der Ärmelkugel und die Saumkürzung um jeweils `½ Fehlbetrag`; weitere Zeichnungslabels nennen unter anderem `½ von 4,5 cm`, `⅓ von 4,5 cm` und `0,6 cm`. Diese Beziehungen und Werte fehlen im verbindlichen Extrakt. Sie wurden nicht stillschweigend als Buchfassungen ergänzt und müssen bei Bedarf zuerst in der Extraktionsschicht geklärt werden.
