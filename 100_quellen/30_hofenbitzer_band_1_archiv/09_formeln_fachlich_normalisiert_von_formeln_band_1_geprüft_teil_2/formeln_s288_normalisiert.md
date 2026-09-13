# Fachlich normalisierte Formeln — S. 288

Quelle der Normalisierung: `formeln_s288_digital_geprüft.md`
Originaltranskript: `s288_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 288
Extraktionsstand: v2

## HOF-B1-S288-F01 — Abnäherinhalt aus der Mehrlänge des Vorderteils

- **Fachlicher Zweck:** Den Abnäherinhalt bei übergroßer Vorderlänge durch Abzug eines Bereichs von der Differenz zwischen Vorder- und Rückenlänge bestimmen.
- **Quelle:** `formeln_s288_digital_geprüft.md`, Zeile 19; Originaltranskript `s288_digital_geprüft.md`, Zeilen 39–43; Buchseite 288.
- **Originalbezeichnung:** Differenz VL – RüL, Abnäherinhalt
- **Normalisierte Bezeichnung:** `abnaeherinhalt_aus_vorderlaengenmehrbetrag`

### Buchfassung

```text
Rechnung: `5,2 - 3 bis 4 = Abnäherinhalt 1,2 bis 2,2`
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `vorderlaenge` | VL, Vorderlänge | 46,8 | cm |
| `rueckenlaenge` | RüL, Rückenlänge | 41,6 | cm |
| `abzugsbetrag` | gedruckter Bereich `3 bis 4` | 3 bis 4 | cm |

### Formel und Rechenschritte

```text
laengendifferenz = vorderlaenge - rueckenlaenge
laengendifferenz = 46,8 cm - 41,6 cm = 5,2 cm

abnaeherinhalt = laengendifferenz - abzugsbetrag
abnaeherinhalt_max = 5,2 cm - 3 cm = 2,2 cm
abnaeherinhalt_min = 5,2 cm - 4 cm = 1,2 cm
abnaeherinhalt = 1,2 bis 2,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchergebnis | Einheit |
|---|---|---:|---|
| `abnaeherinhalt` | Bereich des durch Öffnen entstehenden Brustabnäherinhalts | 1,2 bis 2,2 | cm |

- **Abhängigkeiten:** Vorderlänge und Rückenlänge aus der Konstruktionstabelle sowie ein fachlich gewählter Abzugsbetrag im Bereich von `3 bis 4 cm`.
- **Gültigkeitsbereich:** Anpassung des Unisex-Oberteil-Grundschnitts für Damen auf S. 288, wenn die Vorderlänge mehr als `3 bis 4 cm` über der Rückenlänge liegt.
- **Technische Randbedingung:** Wegen der Subtraktion erzeugt der kleinere Abzugsbetrag die größere Ausgabegrenze. Die Grenzen werden technisch nach dem Ergebnis benannt und nicht in der gedruckten Operandenreihenfolge übernommen.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Unstimmigkeit: `46,8 − 41,6 = 5,2`, `5,2 − 3 = 2,2` und `5,2 − 4 = 1,2`. Die Quelle nennt keine Auswahlregel für einen konkreten Abzugsbetrag zwischen `3` und `4 cm`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Längendifferenz zuerst berechnen, den Abzugsbetrag explizit im Bereich `3 bis 4 cm` verlangen und negative Abnäherinhalte nicht ohne fachliche Regel zulassen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s288_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Beschreibender Seitenverweis `508 + 512`; Pluszeichen verbindet Buchseiten und ist kein Rechenoperator |
| Zeile 14 | 1 | Kopfzeile der Konstruktionstabelle mit Größen- und Passformklassenbereich; Metadaten statt Rechenbeziehung |
| **Summe** | **2** | **1 Seitenverweis + 1 Tabellenkopf** |

## Extraktionsgrenze

Das Originaltranskript enthält in Zeile 21 die Beziehung `½ Ärmelsaumweite`, in Zeile 27 die Bedingung zur Differenz von Vorder- und Rückenlänge und in den Tabellenzeilen 39–41 die Herleitung der Differenz `5,2 cm`. Nur die vollständig extrahierte Rechnung wurde als Buchfassung übernommen; die übrigen Stellen dienen ausschließlich als gekennzeichneter Kontext oder bleiben Extraktionslücken. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
