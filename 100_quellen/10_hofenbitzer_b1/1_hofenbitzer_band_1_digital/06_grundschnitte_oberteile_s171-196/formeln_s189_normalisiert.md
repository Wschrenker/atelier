# Fachlich normalisierte Formeln — S. 189

Quelle der Normalisierung: `formeln_s189_digital_geprüft.md`
Originaltranskript: `s189_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 189
Extraktionsstand: v2

## HOF-B1-S189-F01 — Taillenausfall und gedrucktes Ergebnis

- **Fachlicher Zweck:** Den Taillenausfall aus gemessener vorderer und hinterer Taillenbreite sowie der halben Taillenweite bestimmen.
- **Quelle:** `formeln_s189_digital_geprüft.md`, Zeilen 14–16; Originaltranskript `s189_digital_geprüft.md`, Zeilen 34–36; Buchseite 189.
- **Originalbezeichnung:** `Taillenausfall (TaAf)`
- **Normalisierte Bezeichnung:** `taillenausfall_enger_oberteilgrundschnitt`

### Buchfassung

```text
`= vTaB + hTaB − ½ TaW`  
`= 44,6 cm − 36 cm`  
`= 7,8 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `gemessene_taillenbreite` | vTaB + hTaB | 44,6 | cm |
| `halbe_taillenweite` | ½ TaW | 36 | cm |

### Formel und Rechenschritte

```text
taillenausfall_laut_formel = gemessene_taillenbreite - halbe_taillenweite
                            = 44,6 cm - 36 cm
                            = 8,6 cm
gedrucktes_ergebnis = 7,8 cm
abweichung = 8,6 cm - 7,8 cm = 0,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `taillenausfall_laut_formel` | rechnerisches Ergebnis der gedruckten Operanden | 8,6 | cm |
| `gedruckter_taillenausfall` | gedrucktes Ergebnis | 7,8 | cm |

- **Abhängigkeiten:** Messung von vTaB und hTaB sowie ½ TaW aus der Konstruktionstabelle.
- **Gültigkeitsbereich:** Seitliche Taillierung des engen Oberteil-Grundschnitts auf S. 189.
- **Technische Randbedingung:** Formelpfad und Druckergebnis bleiben bis zur Quellenklärung getrennt.
- **Offene Fragen oder Widersprüche:** `44,6 − 36 = 8,6`, nicht `7,8`. Zusätzlich nennt S. 188 für einen anderen gemessenen TaB-Wert `44,3 − 36 = 8,6`, obwohl dies `8,3` ergibt. Kein Pfad belegt eindeutig den beabsichtigten Wert.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Nicht automatisieren, bevor die gültigen Operanden und das Ergebnis fachlich geklärt sind.

## HOF-B1-S189-F02 — Hüftfehlbetrag und hälftige Seitenanstellung

- **Fachlicher Zweck:** Den Hüftfehlbetrag und den auf jede Seitenlinie zu verteilenden halben Betrag bestimmen.
- **Quelle:** `formeln_s189_digital_geprüft.md`, Zeilen 21–23; Originaltranskript `s189_digital_geprüft.md`, Zeilen 44–46; Buchseite 189.
- **Originalbezeichnung:** `Hüft-Fehlbetrag (HüFb)`
- **Normalisierte Bezeichnung:** `hueftfehlbetrag_und_haelftige_seitenanstellung`

### Buchfassung

```text
`= vHüB + hHüB − ½ HüW`  
`= 43,8 cm − 48,5 cm`  
`= −4,7 cm → 4,7 cm ½ = 2,4 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `gemessene_hueftbreite` | vHüB + hHüB | 43,8 | cm |
| `halbe_hueftweite` | ½ HüW | 48,5 | cm |

### Formel und Rechenschritte

```text
hueftfehlbetrag = 43,8 cm - 48,5 cm = -4,7 cm
positiver_hueftfehlbetrag = abs(-4,7 cm) = 4,7 cm
exakte_anstellung_je_seite = 4,7 cm / 2 = 2,35 cm
gedruckte_anstellung_je_seite = 2,4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hueftfehlbetrag` | vorzeichenbehaftete Differenz | −4,7 | cm |
| `anstellung_je_seite` | positiver halber Fehlbetrag | 2,4 gedruckt; 2,35 exakt | cm |

- **Abhängigkeiten:** Messung von vHüB und hHüB sowie ½ HüW aus der Konstruktionstabelle.
- **Gültigkeitsbereich:** Hüftweitenkorrektur des engen Oberteil-Grundschnitts auf S. 189.
- **Technische Randbedingung:** Der halbe Fehlbetrag wird laut Folgeschritt an beiden Seitenlinien hinzugegeben.
- **Offene Fragen oder Widersprüche:** Die gedruckten `2,4 cm` sind eine Rundung von exakt `2,35 cm`; eine allgemeine Rundungsregel nennt die Quelle nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern `2,35 cm` erhalten und eine Zeichenrundung erst nach einer gesondert belegten Rundungsregel anwenden.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s189_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Checklistenfrage zur Kontrolle der BrU-Maße; Prüfaufforderung, keine Rechenformel |
| Zeile 28 | 1 | Bildnummernverweis `□3 + 5` und Anwendung des bereits in `HOF-B1-S189-F02` enthaltenen halben Hüftfehlbetrags |
| Zeile 33 | 1 | Isoliertes Zeichnungslabel `HlB : 3 + 1 cm`; direkte Übernahme der bereits vollständig normalisierten Grundgerüstformel `HOF-B1-S179-F01` |
| Zeilen 38–40 | 3 | Zeichnungslabels `¼`, `⅓` und `⅔ ArD+`; direkte Teilwertübernahmen aus der Konstruktionstabelle beziehungsweise Wiederholung von `HOF-B1-S180-F01` |
| Zeilen 45–46 | 2 | `BrB+` ist eine direkte Maßübertragung; `½ BrB+ − 0,3 cm` wiederholt die Grundgerüstbeziehung aus `HOF-B1-S181-F02` ohne neuen Operanden oder neue Auswahlregel |
| Zeile 51 | 1 | `RüB+` wird unverändert aus der Konstruktionstabelle abgetragen |
| Zeile 56 | 1 | Brustweitenkontrolle wiederholt `HOF-B1-S180-F02`; keine neue Beziehung |
| Zeile 61 | 1 | Unbezeichnetes Zeichnungslabel `VL − 1 cm`; geometrischer Zielreferent fehlt im Extrakt und die Beziehung ist bereits im früheren Oberteilblock belegt |
| Zeile 66 | 1 | Unvollständig interpunktiertes Zeichnungslabel zur Addition von vTaB und hTaB; Summe ist vollständig in `HOF-B1-S189-F01` enthalten |
| Zeile 71 | 1 | Unvollständig interpunktiertes Zeichnungslabel zur Addition von vHüB und hHüB; Summe ist vollständig in `HOF-B1-S189-F02` enthalten |
| **Konkrete Extraktzeilen** | **12** | **12 Prüf-, Verweis-, Übertragungs- oder Wiederholungszeilen ausgeschlossen** |
| Inventardifferenz | 1 | Der Gesamtindex weist für S. 189 `19` Kandidatenzeilen aus; die elf `text`-Blöcke des Extrakts enthalten nach den ausgewiesenen Quellzeilen nur 18 konkrete Kandidatenzeilen. Die Differenz ist keine zusätzliche Buchzeile. |
| **Abrechnung laut Gesamtindex** | **13** | **12 konkrete Ausschlüsse + 1 offen ausgewiesene Zähldifferenz** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript enthält die vollständigen Konstruktionssätze zu Taillen- und Hüftbreitenmessung in den Zeilen 30 und 40 sowie den Verteilungsschritt in Zeile 48. Der verbindliche Extrakt enthält davon nur die Rechnungen beziehungsweise das Bildverweis-Fragment. Es wurde keine zusätzliche Buchfassung aus dem Transkript erzeugt. Die bestehende Zähldifferenz zwischen Gesamtindex und Extrakt bleibt sichtbar und wird nicht als erfundene Kandidatenzeile ausgegeben.
