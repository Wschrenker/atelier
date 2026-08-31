# Fachlich normalisierte Formeln — S. 127

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/04_grundschnitte_hosen_s106-137/formeln_s127.md`
Originaltranskript: `../Band_1_geprüft_v1/s127.md`
Buchseite: Hofenbitzer, Band 1, S. 127

## HOF-B1-S127-F01 — Hintere Taillenlinienlänge der engen Hose

- **Fachlicher Zweck:** Den auf der neuen hinteren Taillenlinie abzutragenden Betrag bestimmen.
- **Quelle:** `formeln_s127.md`, Zeile 9; Originaltranskript `s127.md`, Zeilen 8–10; Buchseite 127.
- **Originalbezeichnung:** `TaU : 4 − 1 cm + Abnäherinhalt + 1 bis 3 cm`
- **Normalisierte Bezeichnung:** `hintere_taillenlinienlaenge_enge_hose`

### Buchfassung

```text
35. Von P34 aus TaU : 4 − 1 cm + Abnäherinhalt + 1 bis 3 cm auf der neuen Taillenlinie abtragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |
| `vorderer_ausgleichsabzug` | −1 cm | 1 | cm |
| `abnaeherinhalt_hinten` | Abnäherinhalt | nicht angegeben | cm |
| `hintere_zugabe` | 1 bis 3 cm | wählbar | cm |

### Formel und Rechenschritte

```text
hintere_taillenlinienlaenge = (taillenumfang / 4)
                              - vorderer_ausgleichsabzug
                              + abnaeherinhalt_hinten
                              + hintere_zugabe
Buchbasis = 18 cm - 1 cm + abnaeherinhalt_hinten + 1 bis 3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hintere_taillenlinienlaenge` | Betrag ab P34 auf der neuen Taillenlinie | nicht vollständig beziffert | cm |

- **Abhängigkeiten:** Taillenumfang, gewählter Abnäherinhalt und hintere Zugabe.
- **Gültigkeitsbereich:** Hinterhose der engen Hose auf S. 127.
- **Technische Randbedingung:** Der feste Abzug von 1 cm gleicht laut Originaltranskript die zuvor an der Vorderhose addierte 1-cm-Zugabe aus.
- **Offene Fragen oder Widersprüche:** Keine; Abnäherinhalt und hintere Zugabe müssen fachlich gewählt werden.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ausgleichsabzug, Abnäherinhalt und Zugabe getrennt führen; die beiden 1-cm-Beträge dürfen nicht automatisch gegeneinander gekürzt werden.

## HOF-B1-S127-F02 — Hosenausschnitt der engen Hose

- **Fachlicher Zweck:** Den gesamten Hosenausschnitt einer engen Hose für eine Normalfigur mittlerer Größe bestimmen.
- **Quelle:** `formeln_s127.md`, Zeilen 14 und 19; Originaltranskript `s127.md`, Zeilen 34–44; Buchseite 127.
- **Originalbezeichnung:** `HüU : 6 (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_enge_hose`

### Buchfassung

```text
HüU : 6 (± 1 cm)
```

```text
= 16,2 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `toleranz` | ±1 cm | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_exakt = hueftumfang / 6
                       = 97 cm / 6
                       = 16,1666... cm
Buchwert              = 16,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hosenausschnitt` | Hosenausschnitt der engen Hose | 16,2 ± 1 | cm |

- **Abhängigkeiten:** Hüftumfang.
- **Gültigkeitsbereich:** Enge Hose für eine Normalfigur mittlerer Größe.
- **Technische Randbedingung:** Der Quotient wird im Buch auf eine Dezimalstelle zu `16,2 cm` gerundet; die Toleranz ist ein Bereich um diesen Wert.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Exakten Quotienten intern erhalten und Buchrundung sowie Toleranz getrennt anwenden.

## HOF-B1-S127-F03 — Hosenausschnitt bei flachem Gesäß

- **Fachlicher Zweck:** Den Hosenausschnitt der engen Hose bei flachem Gesäß reduzieren.
- **Quelle:** `formeln_s127.md`, Zeile 24; Originaltranskript `s127.md`, Zeilen 46–48; Buchseite 127.
- **Originalbezeichnung:** `16,2 cm − 1 cm = 15,2 cm (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_enge_hose_flaches_gesaess`

### Buchfassung

```text
16,2 cm − 1 cm = 15,2 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_basis` | Buchwert aus F02 | 16,2 | cm |
| `korrektur_flaches_gesaess` | ca. 1 cm weniger | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_flaches_gesaess = hosenausschnitt_basis - korrektur_flaches_gesaess
                                 = 16,2 cm - 1 cm
                                 = 15,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hosenausschnitt_flaches_gesaess` | angepasster Hosenausschnitt | 15,2 ± 1 | cm |

- **Abhängigkeiten:** Gerundeter Basiswert aus `HOF-B1-S127-F02`.
- **Gültigkeitsbereich:** Enge Hose für eine Figur mit flachem Gesäß.
- **Technische Randbedingung:** Die Rechnung verwendet den gerundeten Buchwert 16,2 cm.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Für Buchreproduktion vom gerundeten Basiswert ausgehen; exakte technische Strategie später festlegen.

## HOF-B1-S127-F04 — Hosenausschnitt bei starkem Gesäß

- **Fachlicher Zweck:** Den Hosenausschnitt der engen Hose bei starkem Gesäß vergrößern.
- **Quelle:** `formeln_s127.md`, Zeile 29; Originaltranskript `s127.md`, Zeilen 50–52; Buchseite 127.
- **Originalbezeichnung:** `16,2 cm + 1 cm = 17,2 cm (± 1 cm)`
- **Normalisierte Bezeichnung:** `hosenausschnitt_enge_hose_starkes_gesaess`

### Buchfassung

```text
16,2 cm + 1 cm = 17,2 cm (± 1 cm)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hosenausschnitt_basis` | Buchwert aus F02 | 16,2 | cm |
| `korrektur_starkes_gesaess` | ca. 1 cm mehr | 1 | cm |

### Formel und Rechenschritte

```text
hosenausschnitt_starkes_gesaess = hosenausschnitt_basis + korrektur_starkes_gesaess
                                 = 16,2 cm + 1 cm
                                 = 17,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hosenausschnitt_starkes_gesaess` | angepasster Hosenausschnitt | 17,2 ± 1 | cm |

- **Abhängigkeiten:** Gerundeter Basiswert aus `HOF-B1-S127-F02`.
- **Gültigkeitsbereich:** Enge Hose für eine Figur mit starkem Gesäß.
- **Technische Randbedingung:** Die Rechnung verwendet den gerundeten Buchwert 16,2 cm.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Figurkorrektur mit explizitem Vorzeichen führen.

## HOF-B1-S127-F05 — Gesamte Oberschenkelweite

- **Fachlicher Zweck:** Die gesamte Oberschenkelweite aus Vorder- und Hinterhosenanteil bilden.
- **Quelle:** `formeln_s127.md`, Zeile 39; Originaltranskript `s127.md`, Zeile 66; Buchseite 127.
- **Originalbezeichnung:** `Oberschenkelweite (= vOsW + hOsW)`
- **Normalisierte Bezeichnung:** `oberschenkelweite_gesamt`

### Buchfassung

```text
- Oberschenkelweite (= vOsW + hOsW)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `vordere_oberschenkelweite` | vOsW | nicht angegeben | cm |
| `hintere_oberschenkelweite` | hOsW | nicht angegeben | cm |

### Formel und Rechenschritte

```text
oberschenkelweite_gesamt = vordere_oberschenkelweite + hintere_oberschenkelweite
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `oberschenkelweite_gesamt` | gemessene gesamte Oberschenkelweite | nicht angegeben | cm |

- **Abhängigkeiten:** Gemessene Vorder- und Hinterhosenweite etwa 5 cm unterhalb der Schrittlinie.
- **Gültigkeitsbereich:** Kontrolle der engen Hose auf S. 127.
- **Technische Randbedingung:** Beide Teilweiten müssen auf derselben Höhe und in derselben Einheit gemessen werden.
- **Offene Fragen oder Widersprüche:** Keine; das Originaltranskript fordert anschließend 1 bis 4 cm Mehrweite gegenüber dem Oberschenkelumfang, diese Kontrollbeziehung fehlt im extrahierten Formelbestand.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Messhöhe gemeinsam speichern und die fehlende Mehrweitenkontrolle erst nach Ergänzung der Extraktionsschicht implementieren.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s127.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 34 | 1 | Zeichnungswiederholung von `HOF-B1-S127-F01` |
| Zeile 44 | 1 | Wadenhöhe `WaH = KnH : 2`; identische Wiederholung von `HOF-B1-S123-F01` |
| **Summe** | **2** | **2 Wiederholungen ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s127.md` nennt in den Zeilen 26 und 28 die Kontrollen `Oberschenkelweite = Oberschenkelumfang + mindestens 1 bis 4 cm` und `Wadenweite = Wadenumfang + mindestens 1 bis 2 cm`. Diese Beziehungen fehlen im extrahierten Formelbestand und wurden nicht stillschweigend normalisiert.
