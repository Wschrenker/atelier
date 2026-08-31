# Fachlich normalisierte Formeln — S. 179

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/06_grundschnitte_oberteile_s171-196/formeln_s179.md`
Originaltranskript: `../Band_1_geprüft_v1/s179.md`
Buchseite: Hofenbitzer, Band 1, S. 179

## HOF-B1-S179-F01 — Vertikale Lage von P2 aus der Halslochbreite

- **Fachlicher Zweck:** Den Abstand von P1 nach unten aus einem Drittel der Halslochbreite plus 1 cm bestimmen.
- **Quelle:** `formeln_s179.md`, Zeile 14; Originaltranskript `s179.md`, Zeile 26; Buchseite 179.
- **Originalbezeichnung:** `HlB : 3 + 1 cm`
- **Normalisierte Bezeichnung:** `abstand_p1_p2`

### Buchfassung

```text
> ② Von P1 sind HlB : 3 + 1 cm nach unten abzutragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Beispiel | Einheit |
|---|---|---:|---|
| `halslochbreite` | HlB | 6,5 | cm |
| `konstante_zugabe_p2` | `1 cm` | 1 | cm |

### Formel und Rechenschritte

```text
abstand_p1_p2 = halslochbreite / 3 + konstante_zugabe_p2
exakter Kontextwert = 6,5 cm / 3 + 1 cm
                    = 3,166666... cm
```

### Ausgabe

| Technische Variable | Bedeutung | Exakter Kontextwert | Einheit |
|---|---|---:|---|
| `abstand_p1_p2` | vertikaler Abstand von P1 nach unten zu P2 | 3,166666… | cm |

- **Abhängigkeiten:** HlB aus der Konstruktionstabelle S. 178.
- **Gültigkeitsbereich:** Erste Linien des Grundgerüsts für Oberteil-Grundschnitte.
- **Technische Randbedingung:** Die Addition erfolgt nach der Drittelung; Richtung ist von P1 nach unten.
- **Offene Fragen oder Widersprüche:** Die Buchfassung enthält kein gerundetes Zahlenbeispiel und keine Rundungsregel.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern exakt rechnen; eine spätere Zeichenrundung nicht vorwegnehmen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s179.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Checklistenfrage zur Kontrolle der BrU-Maße; Prüfaufforderung, keine eigene Rechenformel |
| **Summe** | **1** | **1 Prüfaufforderung ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s179.md` enthält weitere feste Abtragsmaße und direkte Übertragungen von MoL, AIT+, RüL und HüT, die im verbindlichen Extrakt fehlen. Sie wurden nicht als neue Buchfassungen ergänzt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
