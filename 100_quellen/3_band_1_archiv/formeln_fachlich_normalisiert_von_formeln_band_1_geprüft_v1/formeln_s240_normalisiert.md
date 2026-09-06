# Fachlich normalisierte Formeln — S. 240

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/08_aermel_varianten_s221-289/formeln_s240_codex_v2_digital_geprueft.md`
Originaltranskript: `../hofenbitzer_band_1_digital/08_aermel_varianten_s221-289/s240_codex_v2_digital_geprueft.md`
Buchseite: Hofenbitzer, Band 1, S. 240

## HOF-B1-S240-F01 — Zwei unbezeichnete Additionen am offenen Ärmelschlitz

- **Fachlicher Zweck:** Die beiden im Extrakt sichtbaren Additionen am Produktionsschnitt erhalten, ohne ihre nicht belegten geometrischen Referenten oder Einheiten zu erfinden.
- **Quelle:** `formeln_s240_codex_v2_digital_geprueft.md`, Zeilen 16–17; Originaltranskript `s240_codex_v2_digital_geprueft.md`, Zeilen 31–32; Buchseite 240.
- **Originalbezeichnung:** `2,5 + 1` und `3 + 1`
- **Normalisierte Bezeichnung:** `additionen_offener_aermelschlitz_referenten_offen`

### Buchfassung

```text
- 2,5 + 1
- 3 + 1
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `grundwert_1` | nicht bezeichnet | 2,5 | offen |
| `grundwert_2` | nicht bezeichnet | 3 | offen |
| `zuschlag_1` | nicht bezeichnet | 1 | offen |

### Formel und Rechenschritte

```text
zielwert_1 = grundwert_1 + zuschlag_1
           = 2,5 + 1
           = 3,5 [Einheit offen]

zielwert_2 = grundwert_2 + zuschlag_1
           = 3 + 1
           = 4 [Einheit offen]
```

### Ausgabe

| Technische Variable | Bedeutung | Rechnerischer Wert | Einheit |
|---|---|---:|---|
| `zielwert_1` | erster unbezeichneter Summenwert am Produktionsschnitt | 3,5 | offen |
| `zielwert_2` | zweiter unbezeichneter Summenwert am Produktionsschnitt | 4 | offen |

- **Abhängigkeiten:** Geometrische Bedeutung der drei Zahlen und ihre Einheit; beides fehlt im verbindlichen Extrakt.
- **Gültigkeitsbereich:** Zeichnungsangaben am Produktionsschnitt des Zweinahtärmels mit offenem Ärmelschlitz auf S. 240.
- **Technische Randbedingung:** Die beiden Additionen sind arithmetisch eindeutig, aber ohne belegte Referenten und Einheit nicht ausführbar in einer Schnittkonstruktion.
- **Offene Fragen oder Widersprüche:** Das Originaltranskript wiederholt nur dieselben unbezeichneten Zeichnungswerte. Aus dem Seitenkontext lässt sich nicht sicher ableiten, welche Schlitz-, Einschlag- oder Nahtzugabenmaße addiert werden. Die technische Fassung bildet deshalb ausschließlich die sichtbare Rechenstruktur ab.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis die Referenten und Einheiten anhand der Buchzeichnung oder einer ergänzten Extraktion belegt sind.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s240_codex_v2_digital_geprueft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 9–10, 28–29 und 34–35 | 6 | Schnittteil- und Zuschnittbeschriftungen von Ober-, Unter- und Futterärmel; `2×-p` bezeichnet Stückzahl und paarigen Zuschnitt, keine Berechnung |
| Zeile 11 | 1 | `Nahtende = Schlitzende` ist eine geometrische Deckungs- beziehungsweise Linienbezeichnung, keine aus Eingaben berechnete Formel |
| Zeilen 22–23 | 2 | Wiederholung der bereits in `HOF-B1-S235-F01` normalisierten Erhöhung `2 × Armloch-NZg + 0,5 cm`; keine neue Rechenbeziehung |
| **Summe** | **9** | **6 Produktions-/Zuschnittbeschriftungen, 1 geometrische Linienbezeichnung und 2 Wiederholungszeilen ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript beschreibt außerhalb des verbindlichen Extrakts das Kürzen des Futters um den Saumeinschlag, das Spiegeln beider Schlitzeinschläge und das Öffnen der Futtermehrlänge oberhalb des Schlitzes. Die Zeichnung nennt außerdem eine Futtermehrlänge von `1 bis 2 cm` und weitere Maßbereiche. Diese Beziehungen und Eingaben wurden nicht stillschweigend als Buchfassungen ergänzt. Die beiden extrahierten Additionen bleiben offen, bis ihre zeichnerischen Referenten belegt sind. Der Abschluss von S. 240 gilt für den vorhandenen extrahierten Kandidatenbestand.
