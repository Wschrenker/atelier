# Fachlich normalisierte Formeln — S. 38

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s38.md`
Originaltranskript: `../Band_1_geprüft_v1/s38.md`
Buchseite: Hofenbitzer, Band 1, S. 38

## HOF-B1-S038-F01 — Hüftweite und Teilweiten mit Zugabe

- **Fachlicher Zweck:** Hüftweite aus Hüftumfang und Zugabe sowie deren halbe und viertel Teilweite für den Rock-Grundschnitt bestimmen.
- **Quelle:** `formeln_s38.md`, Zeilen 7–13; Originaltranskript `s38.md`, Zeilen 26–31; Buchseite 38.
- **Originalbezeichnung:** `Hüftweite HüW = 100; 1/2 = 50; 1/4 = 25`
- **Normalisierte Bezeichnung:** `hueftweite_mit_zugabe`

### Buchfassung

```text
| Hauptmaße (Kennmaße) | HüU | Hüftumfang | 97 | `+ 2-3`, handschriftlich `3` | Hüftweite `HüW` = 100; `1/2` = 50; `1/4` = 25 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `hueftzugabe` | gewählte Zugabe | 3 | cm |
| `halbierungsfaktor` | 1/2 | 2 | dimensionslos |
| `viertelungsfaktor` | 1/4 | 4 | dimensionslos |

### Formel und Rechenschritte

```text
hueftweite = hueftumfang + hueftzugabe
            = 97 cm + 3 cm
            = 100 cm

halbe_hueftweite = hueftweite / halbierungsfaktor
                  = 100 cm / 2
                  = 50 cm

viertel_hueftweite = hueftweite / viertelungsfaktor
                    = 100 cm / 4
                    = 25 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftweite` | Zugabenhaltige Hüftweite | 100 | cm |
| `halbe_hueftweite` | Hälfte der Hüftweite | 50 | cm |
| `viertel_hueftweite` | Viertel der Hüftweite | 25 | cm |

- **Abhängigkeiten:** `hueftumfang` und gewählte `hueftzugabe`.
- **Gültigkeitsbereich:** Maßbeispiel des geraden Rocks mit tiefer Bundposition auf S. 38.
- **Technische Randbedingung:** Die Quelle nennt einen Zugabenbereich von `2 bis 3 cm`; im Beispiel ist handschriftlich `3 cm` gewählt. Die Divisoren dürfen nicht `0` sein.
- **Offene Fragen oder Widersprüche:** Keine; `97 + 3 = 100`, `100 / 2 = 50` und `100 / 4 = 25`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Körpermaß und Zugabe getrennt speichern; Halb- und Viertelwerte aus der vollständigen Hüftweite ableiten.

## HOF-B1-S038-F02 — Taillenausfall aus halber Hüft- und Taillenweite

- **Fachlicher Zweck:** Taillenausfall als Differenz zwischen halber Hüftweite und halber Taillenweite festlegen.
- **Quelle:** `formeln_s38.md`, Zeilen 7–13; Originaltranskript `s38.md`, Zeilen 26–31; Buchseite 38.
- **Originalbezeichnung:** `1/2 HüW - 1/2 TaW =`
- **Normalisierte Bezeichnung:** `taillenausfall_natuerliche_taille`

### Buchfassung

```text
| Hauptmaße (Kennmaße) | TaAf | Taillenausfall |  |  | Formelzeile `1/2 HüW - 1/2 TaW =` |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `halbe_hueftweite` | 1/2 HüW | 50 | cm |
| `halbe_taillenweite` | 1/2 TaW | nicht eingetragen | cm |

### Formel und Rechenschritte

```text
taillenausfall_natuerliche_taille = halbe_hueftweite - halbe_taillenweite
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenausfall_natuerliche_taille` | Taillenausfall an der natürlichen Taillenlinie | nicht eingetragen | cm |

- **Abhängigkeiten:** `halbe_hueftweite` aus `HOF-B1-S038-F01` und eine zugabenhaltige `halbe_taillenweite`.
- **Gültigkeitsbereich:** Tabellenbezug zur natürlichen Taille; der tiefere Bund wird auf derselben Seite gesondert aus der gemessenen Taillenabtrennung berechnet.
- **Technische Randbedingung:** Beide Eingaben müssen dieselbe Längeneinheit tragen.
- **Offene Fragen oder Widersprüche:** Für `TaW` und den Ergebniswert sind in der Buchfassung keine Zahlen eingetragen. Das verhindert nur die Beispielrechnung, nicht die eindeutige allgemeine Beziehung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Diesen Wert nicht mit dem gesonderten Taillenausfall an der figurbedingten Bundposition aus `HOF-B1-S038-F05` vermischen.

## HOF-B1-S038-F03 — Bundumfang und halber Bundumfang

- **Fachlicher Zweck:** Bundumfang aus gemessenem Bundumfang und Zugabe sowie dessen halben Wert bestimmen.
- **Quelle:** `formeln_s38.md`, Zeilen 7–13; Originaltranskript `s38.md`, Zeilen 26–31; Buchseite 38.
- **Originalbezeichnung:** `gBuU 85; + 1; BuU = 86; 1/2 = 43`
- **Normalisierte Bezeichnung:** `bundumfang_mit_zugabe`

### Buchfassung

```text
| Hauptmaße (Kennmaße) | gBuU | gem. Bundumfang | 85 | handschriftlich `+ 1 =` | Bundumfang `BuU` = 86; `1/2` = 43 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `gemessener_bundumfang` | gBuU | 85 | cm |
| `bundzugabe` | handschriftliche Zugabe | 1 | cm |
| `halbierungsfaktor` | 1/2 | 2 | dimensionslos |

### Formel und Rechenschritte

```text
bundumfang = gemessener_bundumfang + bundzugabe
            = 85 cm + 1 cm
            = 86 cm

halber_bundumfang = bundumfang / halbierungsfaktor
                   = 86 cm / 2
                   = 43 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `bundumfang` | Zugabenhaltiger Umfang an der figurbedingten Bundposition | 86 | cm |
| `halber_bundumfang` | Hälfte des zugabenhaltigen Bundumfangs | 43 | cm |

- **Abhängigkeiten:** `gemessener_bundumfang` und gewählte `bundzugabe`.
- **Gültigkeitsbereich:** Maßbeispiel der figurbedingten tieferen Bundposition auf S. 38.
- **Technische Randbedingung:** Umfang und Zugabe müssen dieselbe Einheit tragen; der Halbierungsfaktor darf nicht `0` sein.
- **Offene Fragen oder Widersprüche:** Keine; `85 + 1 = 86` und `86 / 2 = 43`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `gBuU` als Körpermessung und `BuU` als zugabenhaltiges Konstruktionsmaß getrennt führen.

## HOF-B1-S038-F04 — Kontrollsumme der Verteilung am tiefen Bund

- **Fachlicher Zweck:** Prüfen, dass Hüftabstich und gewählte Abnäherinhalte zusammen den Taillenausfall an der tiefen Bundposition ergeben.
- **Quelle:** `formeln_s38.md`, Zeilen 15–18; Originaltranskript `s38.md`, Zeilen 43–51; Buchseite 38.
- **Originalbezeichnung:** `Kontrolle Σ = TaAf`
- **Normalisierte Bezeichnung:** `kontrollsumme_taillenausfall_tiefer_bund`

### Buchfassung

```text
| Kontrolle | `Σ = TaAf` |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Beispiel | Einheit |
|---|---|---:|---|
| `hueftabstich` | Hüftabstich | 4,2 | cm |
| `vorderer_abnaeherinhalt` | VT-Abnäher | 1,0 | cm |
| `erster_hinterer_abnaeherinhalt` | RT-Abnäher | 2,5 | cm |
| `zweiter_hinterer_abnaeherinhalt` | optionaler zweiter hinterer Abnäher | 0 | cm |
| `taillenausfall_tiefer_bund` | TaAf | 7,7 | cm |

### Formel und Rechenschritte

```text
kontrollsumme_taillenausfall_tiefer_bund = hueftabstich
                                           + vorderer_abnaeherinhalt
                                           + erster_hinterer_abnaeherinhalt
                                           + zweiter_hinterer_abnaeherinhalt
                                           = 4,2 cm + 1,0 cm + 2,5 cm + 0 cm
                                           = 7,7 cm

kontrollsumme_taillenausfall_tiefer_bund = taillenausfall_tiefer_bund
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Beispiel | Einheit |
|---|---|---:|---|
| `kontrollsumme_taillenausfall_tiefer_bund` | Summe der verteilten Beträge | 7,7 | cm |
| `verteilung_ist_vollstaendig` | Kontrollaussage `Σ = TaAf` | wahr | boolesch |

- **Abhängigkeiten:** `taillenausfall_tiefer_bund` aus der auf S. 38 gezeigten Berechnung sowie alle gewählten Verteilungsbeträge.
- **Gültigkeitsbereich:** Beispielverteilung auf S. 38; ein zweiter hinterer Abnäher ist optional.
- **Technische Randbedingung:** Ein nicht verwendeter optionaler Abnäher wird technisch mit `0 cm` berücksichtigt. Alle Summanden müssen dieselbe Einheit tragen.
- **Offene Fragen oder Widersprüche:** Keine in der Kontrollsumme; `4,2 + 1,0 + 2,5 = 7,7`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Dieselbe allgemeine Summenprüfung wie in `R01` verwenden; die konkrete Anzahl hinterer Abnäher variabel halten.

## HOF-B1-S038-F05 — Taillenausfall an der tiefen Bundposition

- **Fachlicher Zweck:** Taillenausfall an der figurbedingten Bundposition als Differenz zwischen gemessener halber Taillenabtrennung und halbem Bundumfang bestimmen.
- **Quelle:** `formeln_s38.md`, Zeilen 20–25; Originaltranskript `s38.md`, Zeilen 57–67; Buchseite 38.
- **Originalbezeichnung:** `TaAf = Taillenabtrennung - 1/2 BuW`
- **Normalisierte Bezeichnung:** `taillenausfall_tiefer_bund`

### Buchfassung

```text
TaAf = Taillenabtrennung - 1/2 BuW
     = 50,7 cm             - 43 cm
     = 7,7 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `halbe_taillenabtrennung` | gesamte Taillenabtrennung des halben Schnitts | 50,7 | cm |
| `halber_bundwert_buch` | 1/2 BuW | 43 | cm |
| `halber_bundumfang_hypothese` | 1/2 BuU aus der Maßtabelle | 43 | cm |

### Formel und Rechenschritte

```text
Buchfassung:
taillenausfall_tiefer_bund = halbe_taillenabtrennung - halber_bundwert_buch
                            = 50,7 cm - 43 cm
                            = 7,7 cm

Hypothetische technische Lesart der Transkriptanmerkung:
taillenausfall_tiefer_bund = halbe_taillenabtrennung - halber_bundumfang_hypothese
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenausfall_tiefer_bund` | An der figurbedingten Bundposition zu verteilender Ausfall | 7,7 | cm |

- **Abhängigkeiten:** Gemessene `halbe_taillenabtrennung`; bei der hypothetischen Lesart `halber_bundumfang` aus `HOF-B1-S038-F03`.
- **Gültigkeitsbereich:** Maßbeispiel des geraden Rocks mit figurbedingter tiefer Bundposition auf S. 38.
- **Technische Randbedingung:** Beide Längen müssen dieselbe Einheit tragen. Die hypothetische Ersetzung von `BuW` durch `BuU` darf erst nach fachlicher Entscheidung implementiert werden.
- **Offene Fragen oder Widersprüche:** Im Buch steht `1/2 BuW`; der Zahlenwert `43 cm` entspricht jedoch `1/2 BuU` aus der Maßtabelle. Das Originaltranskript markiert `BuW` als Druckfehler, die Normalisierung darf den Buchwortlaut aber nicht stillschweigend ersetzen.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Keine produktive Formel freigeben, bevor entschieden ist, ob `BuW` im Buch eine eigene Größe bezeichnet oder als Druckfehler für `BuU` behandelt wird.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s38.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 10 | 1 | Tabellenzeile zur Taillenweite mit nicht ausgefüllten Halb- und Viertelwerten (`---`); keine zusätzliche berechenbare Beziehung neben `HOF-B1-S038-F02` |
| Zeile 29 | 1 | Zeichnungslabel `1/2 Hüftweite = (HüU + Zg) :2`; inhaltliche Wiederholung von `HOF-B1-S038-F01` auf derselben Buchseite |
| **Summe** | **2** | **2 ausgeschlossene Kandidatenzeilen** |
