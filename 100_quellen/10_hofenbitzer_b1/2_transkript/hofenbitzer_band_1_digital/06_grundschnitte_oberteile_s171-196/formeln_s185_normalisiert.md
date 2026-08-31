# Fachlich normalisierte Formeln — S. 185

Quelle der Normalisierung: `formeln_s185.md`
Originaltranskript: `s185.md`
Buchseite: Hofenbitzer, Band 1, S. 185

## HOF-B1-S185-F01 — Taillenausfallanteil an den Seitennähten

- **Fachlicher Zweck:** Den an zwei Seitennähten eingestellten Gesamtbetrag bestimmen.
- **Quelle:** `formeln_s185.md`, Zeile 9; Originaltranskript `s185.md`, Zeile 15; Buchseite 185.
- **Originalbezeichnung:** `SN (2 × 1 cm) = 2,0 cm`
- **Normalisierte Bezeichnung:** `taillenausfall_seitennaehte`

### Buchfassung

```text
| 0 bis 2 cm | SN (2 × 1 cm) | 2,0 cm |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `anzahl_seitennaehte` | `2 ×` | 2 | dimensionslos |
| `einstellung_je_seitennaht` | je SN | 1 | cm |

### Formel und Rechenschritte

```text
taillenausfall_seitennaehte = anzahl_seitennaehte * einstellung_je_seitennaht
                             = 2 * 1 cm
                             = 2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `taillenausfall_seitennaehte` | gesamter Ausfallbetrag an beiden SN | 2 | cm |

- **Abhängigkeiten:** Gewählte Einstellung je Seitennaht.
- **Gültigkeitsbereich:** Aufteilung des TaAf beim Grundschnitt mit Hüftausfall.
- **Technische Randbedingung:** Der Gesamtbetrag muss innerhalb des gedruckten Bereichs 0 bis 2 cm liegen.
- **Offene Fragen oder Widersprüche:** Keine; `2 × 1 cm = 2 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einzelbetrag und Anzahl getrennt speichern.

## HOF-B1-S185-F02 — Kontrolle der Taillenausfallverteilung

- **Fachlicher Zweck:** Die verteilten Ausfallbeträge gegen den TaAf von 6,8 cm kontrollieren.
- **Quelle:** `formeln_s185.md`, Zeile 14; Originaltranskript `s185.md`, Zeilen 15–18; Buchseite 185.
- **Originalbezeichnung:** `Σ = Kontrolle TaAf = 6,8 cm`
- **Normalisierte Bezeichnung:** `kontrolle_taillenausfallverteilung`

### Buchfassung

```text
| Σ = Kontrolle TaAf | | 6,8 cm |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Extrakt | Einheit |
|---|---|---:|---|
| `ausfall_seitennaehte` | SN | 2 | cm |
| `seitlicher_hinterer_abnaeherinhalt` | shAbl | nicht extrahiert | cm |
| `hinterer_abnaeherinhalt` | hAbl | nicht extrahiert | cm |

### Formel und Rechenschritte

```text
kontrollsumme_taillenausfall = ausfall_seitennaehte + seitlicher_hinterer_abnaeherinhalt + hinterer_abnaeherinhalt
Buchergebnis = 6,8 cm

Kontextkontrolle im Originaltranskript, nicht Teil der Buchfassung:
2 cm + 2 cm + 2,8 cm = 6,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `kontrollsumme_taillenausfall` | Summe der drei Ausfallanteile | 6,8 | cm |

- **Abhängigkeiten:** `HOF-B1-S185-F01` sowie shAbl und hAbl.
- **Gültigkeitsbereich:** Verteilung des TaAf von S. 184/185.
- **Technische Randbedingung:** Jeder verteilte Anteil darf genau einmal summiert werden.
- **Offene Fragen oder Widersprüche:** Die Summanden shAbl und hAbl fehlen im verbindlichen Extrakt; der Rechenweg ist dort nicht vollständig ausführbar.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Blockieren, bis alle drei extrahierten Summanden vorliegen.

## HOF-B1-S185-F03 — Hüftausfall im Vorderteil

- **Fachlicher Zweck:** Den Hüftausfall aus dem vorderen Abnäherinhalt abzüglich 2 cm bestimmen.
- **Quelle:** `formeln_s185.md`, Zeile 19; Originaltranskript `s185.md`, Zeile 30; Buchseite 185.
- **Originalbezeichnung:** `HüAf = vAbl − 2 cm`
- **Normalisierte Bezeichnung:** `hueftausfall_vorderteil`

### Buchfassung

```text
> **Hüftausfall (HüAf) = vAbl − 2 cm = 3,2 cm − 2 cm = 1,2 cm**
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderer_taillenabnaeherinhalt` | vAbl | 3,2 | cm |
| `hueftausfall_abzug` | fester Abzug | 2 | cm |

### Formel und Rechenschritte

```text
hueftausfall = vorderer_taillenabnaeherinhalt - hueftausfall_abzug
              = 3,2 cm - 2 cm
              = 1,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hueftausfall` | HüAf im Vorderteil | 1,2 | cm |

- **Abhängigkeiten:** vAbl aus `HOF-B1-S184-F01`.
- **Gültigkeitsbereich:** Taillierter Oberteil-Grundschnitt mit Hüftausfall.
- **Technische Randbedingung:** Die Entscheidung, ob HüAf gezeichnet wird, ist im Originalkontext schwellenabhängig und nicht Teil dieser Buchfassung.
- **Offene Fragen oder Widersprüche:** Keine; die Rechnung stimmt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Berechnung und spätere Schwellenentscheidung getrennt modellieren.

## HOF-B1-S185-F04 — Gemeinsame Hüftbreite

- **Fachlicher Zweck:** Vorder- und Hinterhüftbreite zur gemeinsamen HüB addieren.
- **Quelle:** `formeln_s185.md`, Zeile 24; Originaltranskript `s185.md`, Zeile 38; Buchseite 185.
- **Originalbezeichnung:** `vHüB + hHüB = HüB`
- **Normalisierte Bezeichnung:** `gemeinsame_hueftbreite`

### Buchfassung

```text
> ㊸ vHüB und hHüB (ohne Hüftausfall) messen, addieren = HüB und in der Konstruktionstabelle (siehe rechts) den HüFb berechnen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vordere_hueftbreite` | vHüB ohne HüAf | variabel | cm |
| `hintere_hueftbreite` | hHüB ohne HüAf | variabel | cm |

### Formel und Rechenschritte

```text
gemeinsame_hueftbreite = vordere_hueftbreite + hintere_hueftbreite
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `gemeinsame_hueftbreite` | HüB | cm |

- **Abhängigkeiten:** Gemessene vHüB und hHüB.
- **Gültigkeitsbereich:** Hüftkontrolle des Grundschnitts mit Hüftausfall.
- **Technische Randbedingung:** Beide Breiten werden ohne Hüftausfall gemessen.
- **Offene Fragen oder Widersprüche:** Keine; Zahlenwerte folgen erst in der nächsten Formel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Messbedingung „ohne HüAf“ als Teil der Eingabedefinition erhalten.

## HOF-B1-S185-F05 — Hüftfehlbetrag und hälftige Ausstellung

- **Fachlicher Zweck:** Den signierten Hüftbreitenunterschied, seinen Fehlbetrag und den je Seitenlinie auszustellenden Halbwert bestimmen.
- **Quelle:** `formeln_s185.md`, Zeile 29; Originaltranskript `s185.md`, Zeilen 40–44; Buchseite 185.
- **Originalbezeichnung:** `HüFb = HüB − ½ HüW; −5,6 cm → 5,6 cm; ½ = 2,8 cm`
- **Normalisierte Bezeichnung:** `hueftfehlbetrag_und_seitliche_ausstellung`

### Buchfassung

```text
> **Hüft-Fehlbetrag (HüFb) = HüB − ½ HüW = 44,9 cm − 50,5 cm = −5,6 cm → 5,6 cm ; ½ = 2,8 cm**
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `gemeinsame_hueftbreite` | HüB | 44,9 | cm |
| `halbe_hueftweite` | ½ HüW | 50,5 | cm |

### Formel und Rechenschritte

```text
signierte_hueftdifferenz = gemeinsame_hueftbreite - halbe_hueftweite
                          = 44,9 cm - 50,5 cm
                          = -5,6 cm
hueftfehlbetrag = abs(signierte_hueftdifferenz) = 5,6 cm
ausstellung_je_seitenlinie = hueftfehlbetrag / 2 = 2,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `signierte_hueftdifferenz` | HüB − ½ HüW | −5,6 | cm |
| `hueftfehlbetrag` | positiver Ausstellungsbetrag | 5,6 | cm |
| `ausstellung_je_seitenlinie` | halber HüFb | 2,8 | cm |

- **Abhängigkeiten:** HüB aus `HOF-B1-S185-F04` und ½ HüW.
- **Gültigkeitsbereich:** Hüftausstellung des Grundschnitts mit Hüftausfall.
- **Technische Randbedingung:** Signierte Differenz und positiver Konstruktionsbetrag dürfen nicht verwechselt werden.
- **Offene Fragen oder Widersprüche:** Keine; alle Rechenschritte stimmen.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Rohdifferenz, Betrag und Halbwert getrennt ausgeben.

## HOF-B1-S185-F06 — Mehrweite im Armloch

- **Fachlicher Zweck:** Die Armlochmehrweite aus beiden Armlochumfängen abzüglich AraU berechnen.
- **Quelle:** `formeln_s185.md`, Zeile 50; Originaltranskript `s185.md`, Zeile 62; Buchseite 185.
- **Originalbezeichnung:** `vAlU + hAlU − AraU = 2,8`
- **Normalisierte Bezeichnung:** `mehrweite_im_armloch_gemessen`

### Buchfassung

```text
| Mehrweite im Armloch | vAlU 22,5 | + hAlU 24,8 | − AraU 44,5 | = 2,8 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderer_armlochumfang` | vAlU | 22,5 | cm |
| `hinterer_armlochumfang` | hAlU | 24,8 | cm |
| `armansatzumfang` | AraU | 44,5 | cm |

### Formel und Rechenschritte

```text
mehrweite_im_armloch = vorderer_armlochumfang + hinterer_armlochumfang - armansatzumfang
                      = 22,5 cm + 24,8 cm - 44,5 cm
                      = 2,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `mehrweite_im_armloch` | gemessene Mehrweite | 2,8 | cm |

- **Abhängigkeiten:** Gemessene vAlU, hAlU und AraU.
- **Gültigkeitsbereich:** Armlochkontrolle des taillierten Oberteil-Grundschnitts.
- **Technische Randbedingung:** Alle drei Umfänge müssen in derselben Einheit und entlang der vorgesehenen Linien gemessen werden.
- **Offene Fragen oder Widersprüche:** Keine; `22,5 + 24,8 − 44,5 = 2,8`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Messpfade vor der Rechnung validieren.

## HOF-B1-S185-F07 — Sollwert der Armlochmehrweite

- **Fachlicher Zweck:** Den Sollwert der Mehrweite aus der doppelten AIT-Zugabe bestimmen.
- **Quelle:** `formeln_s185.md`, Zeile 55; Originaltranskript `s185.md`, Zeilen 53–64; Buchseite 185.
- **Originalbezeichnung:** `2 · Zugabe zur AIT = 2,6; Toleranz +2 cm bis −1 cm`
- **Normalisierte Bezeichnung:** `sollwert_armlochmehrweite`

### Buchfassung

```text
| Sollwert der Mehrweite | = 2 · Zugabe zur AIT | (Toleranz +2 cm bis −1 cm) | | = 2,6 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `armlochtiefe_zugabe` | Zugabe zur AIT | 1,3 | cm |
| `toleranz_unterhalb` | `−1 cm` | 1 | cm |
| `toleranz_oberhalb` | `+2 cm` | 2 | cm |

### Formel und Rechenschritte

```text
sollwert_armlochmehrweite = 2 * armlochtiefe_zugabe = 2 * 1,3 cm = 2,6 cm
untere_toleranzgrenze = 2,6 cm - 1 cm = 1,6 cm
obere_toleranzgrenze = 2,6 cm + 2 cm = 4,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `sollwert_armlochmehrweite` | Sollwert | 2,6 | cm |
| `untere_toleranzgrenze` | kleinster tolerierter Wert | 1,6 | cm |
| `obere_toleranzgrenze` | größter tolerierter Wert | 4,6 | cm |

- **Abhängigkeiten:** AIT-Zugabe; Istwert aus `HOF-B1-S185-F06`.
- **Gültigkeitsbereich:** Armlochkontrolle des Beispiels auf S. 185.
- **Technische Randbedingung:** Die asymmetrische Toleranz wird nach resultierendem Wert benannt.
- **Offene Fragen oder Widersprüche:** Der Istwert 2,8 cm liegt innerhalb 1,6 bis 4,6 cm.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Soll-, Ist- und Toleranzwerte getrennt protokollieren.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s185.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 34 | 1 | Wiederholung von `5,6 cm : 2 = 2,8 cm` aus `F05` mit Konstruktionsanweisung |
| Zeile 39 | 1 | Tabellenkopf; Lesekontext, keine Rechenformel |
| Zeilen 44–45 | 2 | Wiederholungen des TaAf von S. 184 und des HüFb aus `F05` in der Berechnungstabelle |
| **Summe** | **4** | **3 Wiederholungen und 1 Tabellenkopf ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s185.md` enthält die im Extrakt fehlenden Verteilungszeilen `shAbl = 2,0 cm` und `hAbl = 2,8 cm`, Schwellenregeln für den HüAf sowie Proportionshinweise zum HüFb. Diese Stellen wurden nicht als neue Buchfassungen ergänzt. Die fehlenden Summanden halten nur `HOF-B1-S185-F02` offen; die übrigen extrahierten Formeln bleiben davon unberührt.
