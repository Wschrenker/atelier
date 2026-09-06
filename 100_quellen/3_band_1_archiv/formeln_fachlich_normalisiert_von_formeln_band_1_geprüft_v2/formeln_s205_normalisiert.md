# Fachlich normalisierte Formeln — S. 205

Quelle der Normalisierung: `formeln_s205_digital_geprüft.md`
Originaltranskript: `s205_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 205
Extraktionsstand: v2

## HOF-B1-S205-F01 — Hinterer Hilfsabstand zur Ärmelkugel

- **Fachlicher Zweck:** Den hinteren Hilfsabstand durch Addition von 0,5 cm zum gemessenen vorderen Abstand bestimmen.
- **Quelle:** `formeln_s205_digital_geprüft.md`, Zeile 19; Originaltranskript `s205_digital_geprüft.md`, Zeile 23; Buchseite 205.
- **Originalbezeichnung:** `üb`, `üb + 0,5 cm`
- **Normalisierte Bezeichnung:** `hinterer_hilfsabstand_aermelkugel`

### Buchfassung

```text
- `2,7 cm + 0,5 cm = 3,2 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderer_hilfsabstand` | üb | 2,7 | cm |
| `erhoehung_hinten` | Zuschlag | 0,5 | cm |

### Formel und Rechenschritte

```text
hinterer_hilfsabstand = 2,7 cm + 0,5 cm = 3,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `hinterer_hilfsabstand` | Abstand von P3 nach unten | 3,2 | cm |

- **Abhängigkeiten:** Der Ausgangsabstand wird zwischen vÄP und Brustlinie gemessen und entspricht laut Transkript ¼ ArD+.
- **Gültigkeitsbereich:** Hilfslinien für die Ärmelkugel des schmalen Ärmel-Grundschnitts S. 205.
- **Technische Randbedingung:** Der Messwert 2,7 cm ist eine Eingabe aus der konkreten Konstruktion; die Addition ist allgemein `gemessener_abstand + 0,5 cm`.
- **Offene Fragen oder Widersprüche:** Keine; die Rechnung ist exakt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den gemessenen vorderen Abstand explizit übergeben und für die hintere Hilfslinie 0,5 cm addieren.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s205_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Direkte geometrische Übertragung von ¼ ArD+ auf den Ärmel; keine neue Berechnung im Extrakt |
| Zeile 14 | 1 | Isolierter Messwert `üb = 2,7 cm`; derselbe Wert ist Operand der vollständig extrahierten Addition |
| Zeile 24 | 1 | Kopieren der vAchsel und Punktdefinition `P10 = tP`; geometrische Übertragung ohne Rechenoperation |
| **Summe** | **3** | **2 direkte geometrische Übertragungen/Punktdefinitionen + 1 isolierter Eingabewert** |

## Extraktionslücke

Die allgemeine Anweisung `denselben Abstand + 0,5 cm` steht im Originaltranskript unmittelbar vor der extrahierten Einsetzrechnung, wurde aber nicht selbst extrahiert. Die technische Verallgemeinerung ist deshalb als Kontext gekennzeichnet; die Buchfassung bleibt auf die exakte extrahierte Rechnung beschränkt.
