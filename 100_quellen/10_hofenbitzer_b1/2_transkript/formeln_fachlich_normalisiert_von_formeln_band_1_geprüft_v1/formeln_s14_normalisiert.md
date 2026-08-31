# Fachlich normalisierte Formeln — S. 14

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s14.md`
Originaltranskript: `../Band_1_geprüft_v1/s14.md`
Buchseite: Hofenbitzer, Band 1, S. 14

Die extrahierte Kandidatenzeile `formeln_s14.md`, Zeile 9, ist eine Messanweisung ohne Rechenformel und wird nicht normalisiert.

## HOF-B1-S014-F01 — Rückenbreite aus gemessener Rückenbreite

- **Fachlicher Zweck:** Die für die Schnittkonstruktion verwendete Rückenbreite aus der gemessenen Rückenbreite bestimmen.
- **Quelle:** `formeln_s14.md`, Zeile 14; Originaltranskript `s14.md`, Zeile 37; Buchseite 14.
- **Originalbezeichnung:** `RüB`
- **Normalisierte Bezeichnung:** `rueckenbreite`

### Buchfassung

```text
Die RüB ist vergleichsweise sicher, wie oben beschrieben, zu bestimmen: **RüB = gRüB : 2**
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Einheit |
|---|---|---|---|
| `gemessene_rueckenbreite` | gemessene Rückenbreite | `gRüB` | cm |
| `halbierungsfaktor` | Halbierung | — | dimensionslos |

### Formel und Rechenschritte

```text
rueckenbreite = gemessene_rueckenbreite / halbierungsfaktor
halbierungsfaktor = 2
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `rueckenbreite` | Rückenbreite für die Schnittkonstruktion | `RüB` | cm |

- **Abhängigkeiten:** `gemessene_rueckenbreite`, `halbierungsfaktor`.
- **Gültigkeitsbereich:** Die Formel gilt für die auf S. 14 beschriebene Bestimmung der Rückenbreite aus `gRüB`.
- **Technische Randbedingung:** Der feste Divisor `2` ist ungleich `0`.
- **Offene Fragen oder Widersprüche:** Keine innerhalb der extrahierten Formel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Buchkürzel und technische Variablen getrennt abbilden; Längenwerte mit Einheit führen.

## HOF-B1-S014-F02 — Armdurchmesser aus Oberarmumfang

- **Fachlicher Zweck:** Den Armdurchmesser aus dem Oberarmumfang berechnen.
- **Quelle:** `formeln_s14.md`, Zeile 19; Originaltranskript `s14.md`, Zeile 39; Buchseite 14.
- **Originalbezeichnung:** `ArD`
- **Normalisierte Bezeichnung:** `armdurchmesser`

### Buchfassung

```text
Der ArD ist sicherer aus dem Oberarmumfang (OaU, siehe folgende Seite) zu berechnen: **ArD = OaU · 0,6 – 7,5 cm**
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Wert in der Buchfassung | Einheit |
|---|---|---|---:|---|
| `oberarmumfang` | Oberarmumfang | `OaU` | variabel | cm |
| `oberarm_faktor` | Faktor für den Oberarmumfang | — | 0,6 | dimensionslos |
| `armdurchmesser_abzug` | fester Abzug | — | 7,5 | cm |

### Formel und Rechenschritte

```text
armdurchmesser = (oberarmumfang * oberarm_faktor) - armdurchmesser_abzug
oberarm_faktor = 0,6
armdurchmesser_abzug = 7,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `armdurchmesser` | Armdurchmesser für die Schnittkonstruktion | `ArD` | cm |

- **Abhängigkeiten:** `oberarmumfang`, `oberarm_faktor`, `armdurchmesser_abzug`.
- **Gültigkeitsbereich:** Die Formel ist auf S. 14 als alternative Bestimmung des Armdurchmessers angegeben.
- **Technische Randbedingung:** `oberarmumfang` und `armdurchmesser_abzug` müssen in derselben Längeneinheit vorliegen.
- **Offene Fragen oder Widersprüche:** Keine innerhalb der extrahierten Formel; ein Zahlenbeispiel ist nicht angegeben.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `0,6` als Dezimalwert `0.6` und `7,5` als `7.5` repräsentieren; keine Rundungsregel ergänzen.

## HOF-B1-S014-F03 — Brustbreite aus Brustumfang, Rückenbreite und Armdurchmesser

- **Fachlicher Zweck:** Die Brustbreite als verbleibende Teilstrecke des halben Brustumfangs bestimmen.
- **Quelle:** `formeln_s14.md`, Zeile 24; Originaltranskript `s14.md`, Zeile 41; Buchseite 14.
- **Originalbezeichnung:** `BrB`
- **Normalisierte Bezeichnung:** `brustbreite`

### Buchfassung

```text
Die BrB kann nun mit Hilfe des gemessenen Brustumfangs (BrU) berechnet werden: **BrB = BrU : 2 – RüB – ArD**
```

### Eingaben

| Technische Variable | Buchbegriff | Buchkürzel | Einheit |
|---|---|---|---|
| `brustumfang` | gemessener Brustumfang | `BrU` | cm |
| `rueckenbreite` | Rückenbreite | `RüB` | cm |
| `armdurchmesser` | Armdurchmesser | `ArD` | cm |
| `halbierungsfaktor` | Halbierung des Brustumfangs | — | dimensionslos |

### Formel und Rechenschritte

```text
brustbreite = (brustumfang / halbierungsfaktor) - rueckenbreite - armdurchmesser
halbierungsfaktor = 2
```

### Ausgabe

| Technische Variable | Bedeutung | Buchkürzel | Einheit |
|---|---|---|---|
| `brustbreite` | Brustbreite für die Schnittkonstruktion | `BrB` | cm |

- **Abhängigkeiten:** `brustumfang`, `rueckenbreite`, `armdurchmesser`, `halbierungsfaktor`; `rueckenbreite` kann nach `HOF-B1-S014-F01`, `armdurchmesser` nach `HOF-B1-S014-F02` bestimmt werden.
- **Gültigkeitsbereich:** Die Formel ist Teil der alternativen Bestimmung von `RüB`, `ArD` und `BrB` auf S. 14.
- **Technische Randbedingung:** Alle Eingaben müssen in derselben Längeneinheit vorliegen; der feste Divisor `2` ist ungleich `0`.
- **Offene Fragen oder Widersprüche:** Die Buchfassung nennt den gemessenen Brustumfang im Text `BrU`; auf derselben Seite wird im Fließtext auch `gBrU` verwendet. Die Normalisierung übernimmt für diese Formel das ausdrücklich gesetzte Kürzel `BrU`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Auswertungsreihenfolge durch Klammern erhalten und keine automatische Korrektur negativer Ergebnisse ergänzen.
