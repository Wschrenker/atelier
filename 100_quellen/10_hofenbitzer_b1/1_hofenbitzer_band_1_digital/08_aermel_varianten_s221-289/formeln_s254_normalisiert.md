# Fachlich normalisierte Formeln — S. 254

Quelle der Normalisierung: `formeln_s254_digital_geprüft.md`
Originaltranskript: `s254_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 254
Extraktionsstand: v2

## HOF-B1-S254-F01 — Ärmelkurvenlängen nach Armlochvertiefung

- **Fachlicher Zweck:** Die vordere gemessene Armlochstrecke direkt auf die Ärmelkurve übertragen und die hintere gemessene Armlochstrecke um die gewählte Einhalteweite vergrößern.
- **Quelle:** `formeln_s254_digital_geprüft.md`, Zeilen 20–22; Originaltranskript `s254_digital_geprüft.md`, Zeilen 53–55; Buchseite 254.
- **Originalbezeichnung:** EW, me, üb
- **Normalisierte Bezeichnung:** `aermelkurvenlaengen_nach_armlochvertiefung`

### Buchfassung

```text
- EW = 0,5 bis 1 cm
- üb = 7,9 cm
- üb = 12,6 cm + 0,7 = 13,3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `armlochstrecke_vorne_gemessen` | vordere Strecke, im Bild mit `me` bezeichnet | 7,9 | cm |
| `armlochstrecke_hinten_gemessen` | hintere Strecke, im Bild mit `me` bezeichnet | 12,6 | cm |
| `einhalteweite_hinten` | EW | 0,5 bis 1; gewählt 0,7 | cm |

### Formel und Rechenschritte

```text
aermelkurvenlaenge_vorne = armlochstrecke_vorne_gemessen
aermelkurvenlaenge_vorne = 7,9 cm

aermelkurvenlaenge_hinten = armlochstrecke_hinten_gemessen + einhalteweite_hinten
aermelkurvenlaenge_hinten = 12,6 cm + 0,7 cm
aermelkurvenlaenge_hinten = 13,3 cm
```

Aus dem gedruckten Bereich der Einhalteweite folgt für die hintere Ärmelkurvenlänge:

```text
aermelkurvenlaenge_hinten = 13,1 bis 13,6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchergebnis | Einheit |
|---|---|---:|---|
| `aermelkurvenlaenge_vorne` | auf die vordere Ärmelkurve zu übertragende Länge | 7,9 | cm |
| `aermelkurvenlaenge_hinten` | einschließlich EW zu formende hintere Ärmelkurvenlänge | 13,3 | cm |

- **Abhängigkeiten:** Die neu geformten und ausgemessenen vorderen und hinteren Armlochstrecken sowie eine fachlich gewählte Einhalteweite innerhalb des gedruckten Bereichs.
- **Gültigkeitsbereich:** Aufgelockerte Ärmelanlage mit Armlochvertiefung und Schulterpolster-Erhöhung auf S. 254; die Armlochvergrößerung und das Ausmessen müssen abgeschlossen sein.
- **Technische Randbedingung:** `me` und `üb` werden im Extrakt nicht ausgeschrieben. Ihre technische Zuordnung folgt der Bildreihenfolge und der Konstruktionsanweisung im Originaltranskript: vorne wird die gemessene Länge direkt übertragen, hinten kommt die EW hinzu. Eine automatische Auswahlregel für die EW ist nicht belegt.
- **Offene Fragen oder Widersprüche:** Keine Rechenwidersprüche; `12,6 cm + 0,7 cm = 13,3 cm`. Die Bedeutung der Bildkürzel `me` und `üb` sollte vor einer sprachlichen Übernahme ins Maßregister fachlich bestätigt werden.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Vorder- und Hinterstrecke getrennt führen; nur zur Hinterstrecke eine explizit gewählte und gegen `0,5 bis 1 cm` geprüfte Einhalteweite addieren.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s254_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Seitenverweis `248 + 250`; Pluszeichen verbindet Buchseiten und ist kein Rechenoperator |
| Zeilen 14–15 | 2 | Isolierte gemessene Werte `me = 7,9 cm` und `me = 12,6 cm`; Eingaben der vollständigen Übertragungsbeziehung in Zeilen 20–22 |
| **Summe** | **3** | **1 Seitenverweis + 2 Eingabewerte** |

## Extraktionsgrenze

Das Originaltranskript enthält weitere rechnerisch strukturierte Konstruktionsangaben, insbesondere die Armlochverbreiterung als `½ bis der ganzen Armlochvertiefung`, ihre Verteilung mit `⅓` vorne und `⅔` hinten, die Anpassung der Ärmelnähte um `½ bis ¾ Armlochvertiefung` sowie Bereiche für die Saumerweiterung. Diese Stellen fehlen als vollständige Buchfassungen im verbindlichen Extrakt und wurden nicht stillschweigend normalisiert. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
