# Fachlich normalisierte Formeln — S. 125

Quelle der Normalisierung: `formeln_s125.md`
Originaltranskript: `s125.md`
Buchseite: Hofenbitzer, Band 1, S. 125

## HOF-B1-S125-F01 — Unbezeichneter Hüftumfangs-Ausdruck

- **Fachlicher Zweck:** Einen in der Zeichnung verwendeten Betrag aus einem Zwanzigstel des Hüftumfangs plus 3 cm berechnen; der geometrische Bezug ist in der extrahierten Zeile nicht bezeichnet.
- **Quelle:** `formeln_s125.md`, Zeile 9; Originaltranskript `s125.md`, Zeile 12; Buchseite 125.
- **Originalbezeichnung:** `HüU : 20 + 3 cm`
- **Normalisierte Bezeichnung:** `unbezeichneter_betrag_hueftumfang_zwanzigstel`

### Buchfassung

```text
- HüU : 20 + 3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 | cm |
| `fester_zuschlag` | 3 cm | 3 | cm |

### Formel und Rechenschritte

```text
unbezeichneter_betrag = (hueftumfang / 20) + fester_zuschlag
                       = (97 cm / 20) + 3 cm
                       = 7,85 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `unbezeichneter_betrag` | geometrischer Bezug in der Zeichnung nicht belegt | 7,85 | cm |

- **Abhängigkeiten:** Hüftumfang.
- **Gültigkeitsbereich:** Zeichnung des Grundgerüsts der engen Hose auf S. 125; der genaue Zielpunkt oder die Strecke ist nicht bezeichnet.
- **Technische Randbedingung:** Die Rechnung ist ausführbar, darf aber ohne geometrischen Referenten nicht konstruktiv angewendet werden.
- **Offene Fragen oder Widersprüche:** Es fehlt die belegte Aussage, welche Strecke oder Position mit dem Ergebnis bestimmt wird.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bis der geometrische Referent aus Buchbild oder ergänzter Extraktion eindeutig belegt ist.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s125.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Zeichnungswiederholung des normalen vorderen Hosenausschnitts aus `HOF-B1-S124-F01` |
| Zeile 19 | 1 | Zeichnungswiederholung der vorderen Taillenlinienformel aus `HOF-B1-S124-F05`; `+1` ist der gewählte Wert im Bereich 0 bis 2 cm |
| Zeile 24 | 1 | Zeichnungswiederholung des Saumbetrags aus `HOF-B1-S124-F04` |
| **Summe** | **3** | **3 Wiederholungen ausgeschlossen** |
