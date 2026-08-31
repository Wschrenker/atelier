# Fachlich normalisierte Formeln — S. 180

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s180.md`
Originaltranskript: `../Band_1_geprüft_v1/s180.md`
Buchseite: Hofenbitzer, Band 1, S. 180

## HOF-B1-S180-F01 — Aufteilung des Armdurchmessers zwischen hinterer und vorderer Seite

- **Fachlicher Zweck:** ArD+ in zwei Drittel für den hinteren Bereich und ein Drittel für den vorderen Bereich teilen.
- **Quelle:** `formeln_s180.md`, Zeilen 14 und 19; Originaltranskript `s180.md`, Zeilen 16 und 22; Buchseite 180.
- **Originalbezeichnung:** `⅔ ArD+` und `⅓ ArD+ (den restlichen ArD+)`
- **Normalisierte Bezeichnung:** `armdurchmesser_aufteilung_grundgeruest`

### Buchfassung

```text
> ⑪ Von P10 nach links ⅔ Armdurchmesser+ (ArD+) aus der Konstruktionstabelle ablesen und abtragen.
```

```text
> ⑬ Von P12 nach links ⅓ ArD+ (den restlichen ArD+) aus der Konstruktionstabelle abtragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert auf S. 178 | Einheit |
|---|---|---:|---|
| `armdurchmesser_mit_zugabe` | ArD+ | 10,8 | cm |

### Formel und Rechenschritte

```text
hinterer_armdurchmesser_anteil = (2 / 3) * armdurchmesser_mit_zugabe
                               = (2 / 3) * 10,8 cm
                               = 7,2 cm
vorderer_armdurchmesser_anteil = (1 / 3) * armdurchmesser_mit_zugabe
                               = (1 / 3) * 10,8 cm
                               = 3,6 cm
kontrolle = 7,2 cm + 3,6 cm = 10,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Beispiel | Einheit |
|---|---|---:|---|
| `hinterer_armdurchmesser_anteil` | Strecke P10–P11 | 7,2 | cm |
| `vorderer_armdurchmesser_anteil` | Strecke P12–P13 | 3,6 | cm |

- **Abhängigkeiten:** ArD+ aus `HOF-B1-S178-F06`.
- **Gültigkeitsbereich:** Brustweitenaufteilung im Grundgerüst aller Oberteil-Grundschnitte.
- **Technische Randbedingung:** Beide Strecken werden nach links abgetragen; der zweite Anteil ist ausdrücklich der Rest von ArD+.
- **Offene Fragen oder Widersprüche:** Keine; beide Anteile ergänzen sich exakt zu ArD+.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Beide Strecken aus demselben ArD+-Wert berechnen und ihre Summe als Invariante prüfen.

## HOF-B1-S180-F02 — Kontrolle der halben Brustweite im gezeichneten Grundgerüst

- **Fachlicher Zweck:** Gemessene vordere und hintere Brustweite gegen die halbe BrW kontrollieren.
- **Quelle:** `formeln_s180.md`, Zeile 29; Originaltranskript `s180.md`, Zeilen 30 und 37; Buchseite 180.
- **Originalbezeichnung:** `vBrW + hBrW = ½ BrW`
- **Normalisierte Bezeichnung:** `kontrolle_gezeichnete_halbe_brustweite`

### Buchfassung

```text
- Kontroll-Beschriftung: „Kontrolle der BrW" sowie „vBrW + hBrW = ½ BrW" mit „vBrW" und „hBrW".
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vordere_brustweite_gemessen` | vBrW, Strecke P14–P12 | variabel | cm |
| `hintere_brustweite_gemessen` | hBrW, Strecke P11–P9 | variabel | cm |
| `halbe_brustweite` | ½ BrW | variabel | cm |

### Formel und Rechenschritte

```text
brustweiten_kontrollsumme = vordere_brustweite_gemessen + hintere_brustweite_gemessen
kontrolle_bestanden = (brustweiten_kontrollsumme == halbe_brustweite)
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `brustweiten_kontrollsumme` | Summe aus vBrW und hBrW | cm |
| `kontrolle_bestanden` | Gleichheit mit ½ BrW | boolesch |

- **Abhängigkeiten:** Gezeichnete Strecken vBrW/hBrW und ½ BrW aus der Konstruktionstabelle.
- **Gültigkeitsbereich:** Kontrolle nach dem Abtragen der Brustweite auf S. 180.
- **Technische Randbedingung:** Die beiden gezeichneten Strecken müssen in derselben Einheit und auf derselben Schnittseite gemessen werden.
- **Offene Fragen oder Widersprüche:** Das Beispiel enthält keine gemessenen Zahlenwerte. Auf S. 178 ist ½ BrW selbst widersprüchlich; für dieses PK-3-Beispiel bleibt deshalb die Wahl des gültigen Kontrollwerts durch `HOF-B1-S178-F08` gesperrt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Gleichheit erst prüfen, nachdem ein gültiger ½-BrW-Sollwert feststeht.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s180.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | RüB+ wird unverändert aus der Konstruktionstabelle abgetragen; Konstruktionsanweisung ohne neue Rechenbeziehung |
| Zeile 24 | 1 | BrB+ wird unverändert aus der Konstruktionstabelle abgetragen; Konstruktionsanweisung ohne neue Rechenbeziehung |
| **Summe** | **2** | **2 direkte Maßübertragungen ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s180.md` enthält zusätzlich den frei gewählten Zwischenraum von ca. 7 bis 10 cm sowie die genaue Messanweisung für vBrW und hBrW. Der Zwischenraum ist ein Eingabebereich und keine aus anderen Größen berechnete Formel; die Messpfade wurden nur als Bedeutung der extrahierten Kontrollgrößen verwendet. Es wurde keine zusätzliche Buchfassung erzeugt.
