# Fachlich normalisierte Formeln — S. 47

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/03_modelle_roecke_s40-105/formeln_s47.md`
Originaltranskript: `../hofenbitzer_band_1_digital/03_modelle_roecke_s40-105/s47.md`
Buchseite: Hofenbitzer, Band 1, S. 47

## HOF-B1-S047-F01 — Breitenbereich des vorderen Innenbeinteils

- **Fachlicher Zweck:** Den an der vorderen Mitte nach außen und oben abzutragenden Breitenbereich des Innenbeinteils aus dem Hüftumfang bestimmen.
- **Quelle:** `formeln_s47.md`, Zeile 23; Originaltranskript `s47.md`, Zeile 37; Buchseite 47.
- **Originalbezeichnung:** `HüU :8 - 1,5 bis - 2 cm`
- **Normalisierte Bezeichnung:** `breitenbereich_vorderes_innenbeinteil`

### Buchfassung

```text
2. An der vM wird HüU :8 - 1,5 bis - 2 cm nach außen und nach oben abgetragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | nicht angegeben | cm |
| `abzug_vorne_klein` | kleiner Abzug | 1,5 | cm |
| `abzug_vorne_gross` | großer Abzug | 2 | cm |

### Formel und Rechenschritte

```text
breite_vorderes_innenbeinteil_obere_grenze = hueftumfang / 8 - 1,5 cm
breite_vorderes_innenbeinteil_untere_grenze = hueftumfang / 8 - 2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---|---|
| `breite_vorderes_innenbeinteil_untere_grenze` | kleinere Breite des angegebenen Bereichs | `HüU :8 - 2 cm` | cm |
| `breite_vorderes_innenbeinteil_obere_grenze` | größere Breite des angegebenen Bereichs | `HüU :8 - 1,5 cm` | cm |

- **Abhängigkeiten:** Gemessener `hueftumfang`.
- **Gültigkeitsbereich:** Vorderes Innenbeinteil des geraden oder saumerweiterten Hosenrocks auf S. 47.
- **Technische Randbedingung:** Der Hüftumfang und beide Abzüge müssen in derselben Längeneinheit vorliegen; die untere Grenze darf die obere Grenze nicht überschreiten.
- **Offene Fragen oder Widersprüche:** Keine. Die Buchreihenfolge `- 1,5 bis - 2 cm` läuft sprachlich von der größeren zur kleineren Ergebnisbreite; die technische Fassung benennt die Grenzen nach ihrem Ergebniswert.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Bereich als zwei Grenzen führen und die konkrete Wahl innerhalb des Bereichs nicht ohne weitere Fachregel automatisieren.

## HOF-B1-S047-F02 — Breitenbereich des hinteren Innenbeinteils

- **Fachlicher Zweck:** Den an der hinteren Mitte nach außen und oben abzutragenden Breitenbereich des Innenbeinteils aus dem Hüftumfang bestimmen.
- **Quelle:** `formeln_s47.md`, Zeile 24; Originaltranskript `s47.md`, Zeile 38; Buchseite 47.
- **Originalbezeichnung:** `HüU :8 + 2 bis + 3 cm`
- **Normalisierte Bezeichnung:** `breitenbereich_hinteres_innenbeinteil`

### Buchfassung

```text
3. An der hM wird HüU :8 + 2 bis + 3 cm nach außen und nach oben abgetragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | nicht angegeben | cm |
| `zugabe_hinten_klein` | kleine Zugabe | 2 | cm |
| `zugabe_hinten_gross` | große Zugabe | 3 | cm |

### Formel und Rechenschritte

```text
breite_hinteres_innenbeinteil_untere_grenze = hueftumfang / 8 + 2 cm
breite_hinteres_innenbeinteil_obere_grenze  = hueftumfang / 8 + 3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---|---|
| `breite_hinteres_innenbeinteil_untere_grenze` | kleinere Breite des angegebenen Bereichs | `HüU :8 + 2 cm` | cm |
| `breite_hinteres_innenbeinteil_obere_grenze` | größere Breite des angegebenen Bereichs | `HüU :8 + 3 cm` | cm |

- **Abhängigkeiten:** Gemessener `hueftumfang`.
- **Gültigkeitsbereich:** Hinteres Innenbeinteil des geraden oder saumerweiterten Hosenrocks auf S. 47.
- **Technische Randbedingung:** Der Hüftumfang und beide Zugaben müssen in derselben Längeneinheit vorliegen; die untere Grenze darf die obere Grenze nicht überschreiten.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Bereich als zwei Grenzen führen und die konkrete Wahl innerhalb des Bereichs von Figurtyp und Rockweite abhängig lassen, bis dafür eine belegte Auswahlregel vorliegt.

## HOF-B1-S047-F03 — Halbes Bezugsmaß plus 0,5 am hinteren Innenbeinteil

- **Fachlicher Zweck:** Die auf der Zeichnung am hinteren Innenbeinteil oben und unten angegebene Teilungs- und Zugabebeziehung erhalten.
- **Quelle:** `formeln_s47.md`, Zeile 17; Originaltranskript `s47.md`, Zeile 32; Buchseite 47.
- **Originalbezeichnung:** `1/2 + 0,5`
- **Normalisierte Bezeichnung:** `halbes_bezugsmass_plus_zugabe_hinteres_innenbeinteil`

### Buchfassung

```text
- `1/2 + 0,5` (am hinteren Innenbeinteil, oben und unten).
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `bezugsmass` | nicht benanntes Ganzes zu `1/2` | nicht angegeben | offen |
| `zugabe_hinten` | nicht benannte Zugabe | 0,5 | offen |

### Formel und Rechenschritte

```text
zielmass_hinteres_innenbeinteil = bezugsmass / 2 + zugabe_hinten
zugabe_hinten                    = 0,5 [Einheit offen]
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---|---|
| `zielmass_hinteres_innenbeinteil` | oben und unten markiertes Maß am hinteren Innenbeinteil | `1/2 + 0,5` | offen |

- **Abhängigkeiten:** Ein in der extrahierten Buchfassung nicht benanntes Bezugsmaß.
- **Gültigkeitsbereich:** Zeichnungsangabe am hinteren Innenbeinteil oben und unten auf S. 47.
- **Technische Randbedingung:** Bezugsgröße, Bedeutung der Halbierung und Einheit der Zugabe müssen vor einer Implementierung belegt werden.
- **Offene Fragen oder Widersprüche:** Die Buchfassung nennt weder das zu halbierende Maß noch die Einheit von `0,5`. Die technische Gleichung bildet nur die sichtbare Rechenstruktur ab und ist nicht ausführbar.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bevor Bezugsgröße und Einheit anhand der Buchzeichnung oder einer weiteren belegten Textstelle geklärt sind.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s47.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 9–12 | 4 | Zeichnungslabels mit den vier Grenzwerten; dieselben Beziehungen sind in den vollständigen Konstruktionssätzen der Zeilen 23–24 bereits als Formelblöcke abgebildet |
| Zeile 22 | 1 | Bildverweis `□4+5` und Eingabebereich für eine Konstruktionsanweisung; das Pluszeichen verbindet Bildnummern, der Sitzhöhenbereich ist keine aus Eingaben berechnete Formel |
| **Summe** | **5** | **4 Wiederholungen und 1 Fehlklassifikation ausgeschlossen** |
