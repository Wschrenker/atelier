# Fachlich normalisierte Formeln — S. 109

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s109.md`
Originaltranskript: `s109.md`
Buchseite: Hofenbitzer, Band 1, S. 109

## HOF-B1-S109-F01 — Halbe und viertel Umfangsmaße

- **Fachlicher Zweck:** Taillen-, Hüft- und Bundumfang in Halb- und Viertelmaße für die Hosenkonstruktion teilen.
- **Quelle:** `formeln_s109.md`, Zeilen 14–16; Originaltranskript `s109.md`, Zeilen 57–59; Buchseite 109.
- **Originalbezeichnung:** `½` und `¼` von TaU, HüU und BuU.
- **Normalisierte Bezeichnung:** `umfangsteilwerte_hose`

### Buchfassung

```text
| TaU | Taillenumfang | 72 | ½ = 36; ¼ = 18 |
| HüU | Hüftumfang | 97 | ½ = 48,5; ¼ = 24,25 |
| BuU | Bundumfang | — | ½ = —; ¼ = — |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |
| `hueftumfang` | HüU | 97 | cm |
| `bundumfang` | BuU | nicht eingetragen | cm |

### Formel und Rechenschritte

```text
halber_umfang = umfang / 2
viertel_umfang = umfang / 4

TaU: 72 cm / 2 = 36 cm; 72 cm / 4 = 18 cm
HüU: 97 cm / 2 = 48,5 cm; 97 cm / 4 = 24,25 cm
BuU: Formel vorhanden; kein Buchwert eingetragen
```

### Ausgabe

| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `halber_taillenumfang` | ½ TaU | 36 | cm |
| `viertel_taillenumfang` | ¼ TaU | 18 | cm |
| `halber_hueftumfang` | ½ HüU | 48,5 | cm |
| `viertel_hueftumfang` | ¼ HüU | 24,25 | cm |
| `halber_bundumfang` | ½ BuU | nicht eingetragen | cm |
| `viertel_bundumfang` | ¼ BuU | nicht eingetragen | cm |

- **Abhängigkeiten:** Der jeweils verwendete ganze Umfang.
- **Gültigkeitsbereich:** Konstruktionstabelle der Standardhose, Größe 38, auf S. 109.
- **Technische Randbedingung:** Leere BuU-Felder bleiben unbekannt und dürfen nicht als null interpretiert werden.
- **Offene Fragen oder Widersprüche:** Keine; die vier eingetragenen Teilwerte sind rechnerisch richtig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Eine gemeinsame Teilungsfunktion verwenden, Ergebnisse aber unter maßspezifischen Namen speichern.

## HOF-B1-S109-F02 — Vorder- und Hinterhosenbreite

- **Fachlicher Zweck:** Vorder- und Hinterhosenbreite aus dem Viertel-Hüftumfang durch eine gegenläufige Verschiebung von 1 cm bestimmen.
- **Quelle:** `formeln_s109.md`, Zeilen 21–22; Originaltranskript `s109.md`, Zeilen 74–75; Buchseite 109.
- **Originalbezeichnung:** `¼ HüU −1 cm` und `¼ HüU +1 cm`.
- **Normalisierte Bezeichnung:** `vorder_und_hinterhosenbreite_standardhose`

### Buchfassung

```text
| vHoB | Vorderhosenbreite | ¼ HüU −1 cm | — | 23,2 |
| hHoB | Hinterhosenbreite | ¼ HüU +1 cm | — | 25,2 |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `viertel_hueftumfang` | ¼ HüU | 24,25 | cm |
| `breitenverschiebung` | `1 cm` | 1 | cm |

### Formel und Rechenschritte

```text
vorderhosenbreite_exakt = 24,25 cm - 1 cm = 23,25 cm
hinterhosenbreite_exakt = 24,25 cm + 1 cm = 25,25 cm

gedruckter Wert vHoB = 23,2 cm
gedruckter Wert hHoB = 25,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Exakt / gedruckt | Einheit |
|---|---|---|---|
| `vorderhosenbreite` | vHoB | 23,25 / 23,2 | cm |
| `hinterhosenbreite` | hHoB | 25,25 / 25,2 | cm |

- **Abhängigkeiten:** ¼ HüU aus `HOF-B1-S109-F01`.
- **Gültigkeitsbereich:** Konstruktionstabelle der Standardhose, Größe 38, auf S. 109.
- **Technische Randbedingung:** Die Verschiebung verkleinert vHoB und vergrößert hHoB um denselben Betrag; die exakte Summe bleibt ½ HüU.
- **Offene Fragen oder Widersprüche:** Beide exakten Ergebnisse enden auf `,25`, gedruckt ist jeweils `,2`. Die Quelle nennt keine Rundungs- oder Abschneideregel; exakte und gedruckte Werte bleiben getrennt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern exakt rechnen und eine spätere Rundungsregel nicht aus diesem Einzelbeispiel ableiten.

## HOF-B1-S109-F03 — Kniehöhe aus der Schritthöhe

- **Fachlicher Zweck:** Die Kniehöhe als vier Zehntel der Schritthöhe bestimmen.
- **Quelle:** `formeln_s109.md`, Zeile 27; Originaltranskript `s109.md`, Zeile 94; Buchseite 109.
- **Originalbezeichnung:** `SrH :10 · 4`.
- **Normalisierte Bezeichnung:** `kniehoehe_standardhose`

### Buchfassung

```text
| KnH | Kniehöhe | SrH :10 · 4 | 32 |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `schritthoehe` | SrH | 80 | cm |

### Formel und Rechenschritte

```text
kniehoehe = (schritthoehe / 10) * 4
           = (80 cm / 10) * 4
           = 32 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `kniehoehe` | KnH | 32 | cm |

- **Abhängigkeiten:** SrH; der Wert 80 cm steht in der unmittelbar vorhergehenden Tabellenzeile des Originaltranskripts.
- **Gültigkeitsbereich:** Konstruktionstabelle der Standardhose, Größe 38, auf S. 109.
- **Technische Randbedingung:** Der Transkriptwert 80 cm dient nur als gekennzeichneter Rechenkontext; die Buchfassung bleibt auf die extrahierte KnH-Zeile beschränkt.
- **Offene Fragen oder Widersprüche:** Keine; der gedruckte Wert ist rechnerisch richtig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Faktor als exakten Bruch `4/10` führen und erst bei der Ausgabe runden.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Beschreibender Abbildungsverweis zu Hosenformen und Sitzlängen; keine Rechenbeziehung |
| **Summe** | **1** | **1 Sichtungs-/Kontextzeile** |
