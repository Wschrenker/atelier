# Fachlich normalisierte Formeln — S. 218

Quelle der Normalisierung: `formeln_s218_digital_geprüft.md`
Originaltranskript: `s218_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 218
Extraktionsstand: v2

## HOF-B1-S218-F01 — Umfang des neuen Armlochs

- **Fachlicher Zweck:** Den Umfang des erweiterten neuen Armlochs aus vorderer und hinterer Armlochkurve bestimmen.
- **Quelle:** `formeln_s218_digital_geprüft.md`, Zeilen 9 und 14; Originaltranskript `s218_digital_geprüft.md`, Zeilen 17–21; Buchseite 218.
- **Originalbezeichnung:** AlU, vorderes Armloch, hinteres Armloch
- **Normalisierte Bezeichnung:** `armlochumfang_neu`

### Buchfassung

Allgemeine Beziehung:

```text
   AlU = vorderes Armloch + hinteres Armloch
```

Buchbeispiel:

```text
   hier = 24,2 cm + 26 cm = 50,2 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `armlochkurve_vorne` | vorderes Armloch | cm |
| `armlochkurve_hinten` | hinteres Armloch | cm |

### Formel und Rechenschritte

```text
armlochumfang_neu = armlochkurve_vorne + armlochkurve_hinten
armlochumfang_neu = 24,2 cm + 26 cm
armlochumfang_neu = 50,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `armlochumfang_neu` | Umfang des erweiterten neuen Armlochs | cm |

- **Abhängigkeiten:** Die vordere und hintere Armlochkurve müssen am geänderten Oberteil-Grundschnitt gemessen sein.
- **Gültigkeitsbereich:** Ärmelanpassung an ein vergrößertes Armloch mit gleichzeitiger Einstellung der Einhalteweite.
- **Technische Randbedingung:** Beide Messstrecken müssen am selben neuen Armloch und entlang der späteren Nahtlinie gemessen werden.
- **Offene Fragen oder Widersprüche:** Keine in der extrahierten Beziehung; `24,2 + 26 = 50,2` ist rechnerisch richtig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorderen und hinteren Messwert getrennt speichern und ihre Summe als Eingabe für `HOF-B1-S218-F02` ausgeben.

## HOF-B1-S218-F02 — Neuer Ärmelkugelumfang mit Einhalteweite

- **Fachlicher Zweck:** Den gewünschten neuen Ärmelkugelumfang aus neuem Armlochumfang und prozentualer Einhalteweite bestimmen.
- **Quelle:** `formeln_s218_digital_geprüft.md`, Zeilen 24, 29, 34 und 39; Originaltranskript `s218_digital_geprüft.md`, Zeilen 29–39; Buchseite 218.
- **Originalbezeichnung:** ÄkU_NEU, AlU, EW in %
- **Normalisierte Bezeichnung:** `aermelkugelumfang_neu_mit_einhalteweite`

### Buchfassung

Allgemeine Beziehung:

```text
ÄkU_NEU = AlU · (100% + EW in %) : 100%
```

Buchrechnung:

```text
hier = 50,2 cm · (100% + 7%) : 100%
```

```text
= 50,2 cm · 1,07
```

```text
ÄkU_NEU = 53,7 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `armlochumfang_neu` | AlU | cm |
| `einhalteweite_prozent` | EW in % | % |

### Formel und Rechenschritte

```text
aermelkugelumfang_neu = armlochumfang_neu * ((100 + einhalteweite_prozent) / 100)
aermelkugelumfang_neu = 50,2 cm * ((100 + 7) / 100)
aermelkugelumfang_neu = 50,2 cm * 1,07
aermelkugelumfang_neu = 53,714 cm
buchwert_aermelkugelumfang_neu = 53,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `aermelkugelumfang_neu` | gewünschter neuer Ärmelkugelumfang einschließlich Einhalteweite | cm |

- **Abhängigkeiten:** `armlochumfang_neu` aus `HOF-B1-S218-F01`; fachlich gewählte Einhalteweite passend zur Stoffqualität.
- **Gültigkeitsbereich:** Prozentuale Bestimmung der Einhalteweite. Das Transkript nennt eine Bestimmung in Zentimetern nur als Alternative, ohne dafür eine extrahierte Formel zu liefern.
- **Technische Randbedingung:** `einhalteweite_prozent` muss als Prozentwert eingegeben werden; `7` bedeutet 7 %.
- **Offene Fragen oder Widersprüche:** Das exakte Ergebnis ist `53,714 cm`, gedruckt sind `53,7 cm`. Die Stelle ist rechnerisch konsistent; eine allgemeine Rundungsregel ist nicht belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Exakten Wert und Buchwert getrennt erhalten; ohne fachlich freigegebene Rundungsregel nicht pauschal auf eine Dezimalstelle runden.

## HOF-B1-S218-F03 — Fehlweite zwischen alter und gewünschter Ärmelkugel

- **Fachlicher Zweck:** Die für die Ärmelanpassung auszugleichende Differenz zwischen vorhandenem und gewünschtem Ärmelkugelumfang bestimmen.
- **Quelle:** `formeln_s218_digital_geprüft.md`, Zeilen 44, 49 und 54; Originaltranskript `s218_digital_geprüft.md`, Zeilen 41–49; Buchseite 218.
- **Originalbezeichnung:** Fehlweite, ÄkU_ALT, ÄkU_NEU
- **Normalisierte Bezeichnung:** `aermelkugel_fehlweite`

### Buchfassung

Allgemeine Beziehung:

```text
Fehlweite = ÄkU_ALT − ÄkU_NEU
```

Buchrechnung:

```text
hier = 48,5 cm − 53,7 cm
```

```text
= −5,2 cm → Fehlweite = 5,2 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `aermelkugelumfang_alt` | ÄkU_ALT | cm |
| `aermelkugelumfang_neu_buchwert` | ÄkU_NEU | cm |

### Formel und Rechenschritte

```text
differenz_alt_minus_neu = aermelkugelumfang_alt - aermelkugelumfang_neu_buchwert
differenz_alt_minus_neu = 48,5 cm - 53,7 cm
differenz_alt_minus_neu = -5,2 cm
fehlweite = abs(differenz_alt_minus_neu)
fehlweite = 5,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `differenz_alt_minus_neu` | vorzeichenbehaftete Differenz gemäß gedruckter Gleichung | cm |
| `fehlweite` | positiver, auszugleichender Differenzbetrag gemäß gedrucktem Pfeil | cm |

- **Abhängigkeiten:** Vorhandener gemessener Ärmelkugelumfang und gewünschter neuer Ärmelkugelumfang aus `HOF-B1-S218-F02`.
- **Gültigkeitsbereich:** Der gedruckte Fall behandelt einen vorhandenen Ärmelkugelumfang, der kleiner als der gewünschte neue Umfang ist.
- **Technische Randbedingung:** Die Buchfassung verwendet `Fehlweite` zunächst für die negative Differenz und nach dem Pfeil für deren positiven Betrag. Beide Größen müssen technisch getrennt bleiben.
- **Offene Fragen oder Widersprüche:** Die Rechnung `48,5 − 53,7 = −5,2` ist richtig. Der Übergang zum positiven Betrag ist gedruckt, aber nicht als allgemeine Betragsformel notiert; für den belegten Fall ist die Bedeutung eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorzeichenbehaftete Differenz und positiven Öffnungsbedarf getrennt ausgeben; die Betragsbildung nicht als Beleg für alle nicht gedruckten Vorzeichenfälle verallgemeinern.

## HOF-B1-S218-F04 — Schulterpolster-Öffnung und dadurch erzeugte Mehrweite

- **Fachlicher Zweck:** Die waagerechte Öffnung als Drittel der Schulterpolster-Erhöhung und die dadurch beidseitig erzeugte gesamte Mehrweite bestimmen.
- **Quelle:** `formeln_s218_digital_geprüft.md`, Zeilen 59 und 64; Originaltranskript `s218_digital_geprüft.md`, Zeilen 56–66; Buchseite 218.
- **Originalbezeichnung:** Öffnung, SuPoE, ⅓ Schulterpolster-Erhöhung, ⅔ SuPoE
- **Normalisierte Bezeichnung:** `schulterpolster_oeffnung_und_mehrweite`

### Buchfassung

Öffnung im Buchbeispiel:

```text
hier Öffnung = 2,5 cm : 3 = 0,8 cm
```

Beidseitig erzeugte Mehrweite:

```text
2 · ⅓ SuPoE = ⅔ SuPoE → ⅔ von 2,5 cm = ca. 1,7 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `schulterpolster_erhoehung` | SuPoE, Schulterpolster-Erhöhung | cm |

### Formel und Rechenschritte

```text
waagerechte_oeffnung = schulterpolster_erhoehung / 3
waagerechte_oeffnung = 2,5 cm / 3
waagerechte_oeffnung_exakt = 0,833333... cm
buchwert_waagerechte_oeffnung = 0,8 cm
mehrweite_beidseitig = 2 * (schulterpolster_erhoehung / 3)
mehrweite_beidseitig = (2 / 3) * schulterpolster_erhoehung
mehrweite_beidseitig = (2 / 3) * 2,5 cm
mehrweite_beidseitig = 1,666666... cm
buchwert_mehrweite_beidseitig = ca. 1,7 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `waagerechte_oeffnung` | Öffnungsbetrag an einer Seite der waagerechten Ärmelkugelöffnung | cm |
| `mehrweite_beidseitig` | gesamte durch linke und rechte Öffnung erzeugte Mehrweite | cm |

- **Abhängigkeiten:** Gemessene Schulterpolster-Erhöhung. Die Beziehung entspricht fachlich dem bereits auf S. 216 extrahierten Drittelansatz, wird hier aber durch eine eigene Einsetzrechnung und die beidseitige Gesamtwirkung erweitert.
- **Gültigkeitsbereich:** Ärmelanpassung für Schulterpolster-Erhöhung und Armlochauflockerung auf S. 218–219.
- **Technische Randbedingung:** Die Öffnung wird links und rechts wirksam; deshalb wird das Drittel für die gesamte Mehrweite verdoppelt.
- **Offene Fragen oder Widersprüche:** `2,5 : 3` ergibt periodisch `0,8333…`; `⅔ · 2,5` ergibt `1,6666…`. Die Buchwerte `0,8 cm` und `ca. 1,7 cm` sind rechnerisch plausible Näherungen, ohne dass eine allgemeine Rundungsregel belegt ist.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Exakte Drittelwerte intern bewahren und gedruckte Näherungen nur als Buchwerte ausgeben.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s218_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 19 | 1 | Gemessener vorhandener Ärmelkugelumfang `ÄkU_ALT = 48,5 cm`; Eingabewert ohne Berechnung |
| Zeile 69 | 1 | Schulterpolster-Erhöhung `2,5 cm`; Eingabewert ohne Berechnung |
| Zeile 74 | 1 | Wiederholung der bereits in `HOF-B1-S218-F01` erhaltenen vollständigen Armlochsumme |
| Zeile 79 | 1 | Wiederholung des gemessenen vorhandenen Ärmelkugelumfangs; Eingabewert ohne Berechnung |
| **Summe** | **4** | **3 Eingabe-/Messwertzeilen + 1 Rechenwiederholung** |

## Extraktionsgrenze

Die Transkription enthält weitere Zeichnungslabels und Arbeitsanweisungen, unter anderem die einzelnen Drittel-/Zweidrittel-Beschriftungen sowie die Kapphöhe von ca. `5 cm`. Sie wurden nicht als zusätzliche Buchfassungen erfunden. Normalisiert wurde ausschließlich der vorhandene extrahierte Kandidatenbestand.
