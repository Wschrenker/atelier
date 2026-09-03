# Fachlich normalisierte Formeln — S. 110

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s110.md`
Originaltranskript: `s110.md`
Buchseite: Hofenbitzer, Band 1, S. 110

## HOF-B1-S110-F01 — Höhenabstand der Hüftlinie von P4

- **Fachlicher Zweck:** Den nach oben abzutragenden Abstand von P4 zur Hüftlinie aus dem Hüftumfang bestimmen.
- **Quelle:** `formeln_s110.md`, Zeile 9; Originaltranskript `s110.md`, Zeile 31; Buchseite 110.
- **Originalbezeichnung:** `HüU : 20 + 3 cm`.
- **Normalisierte Bezeichnung:** `hueftlinienabstand_von_p4`

### Buchfassung

```text
7. Von P4 aus HüU : 20 + 3 cm nach oben abtragen und nach rechts abwinkeln. Von dort die Hüftlinie abwinkeln.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | variabel | cm |
| `konstante_hueftlinienzugabe` | `3 cm` | 3 | cm |

### Formel und Rechenschritte

```text
hueftlinienabstand = (hueftumfang / 20) + 3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftlinienabstand` | Abstand von P4 nach oben zur Hüftlinie | cm |

- **Abhängigkeiten:** HüU und der bereits konstruierte Punkt P4.
- **Gültigkeitsbereich:** Grundgerüst der Standardhose auf S. 110.
- **Technische Randbedingung:** Der skalare Betrag wird von P4 senkrecht nach oben abgetragen; das anschließende Abwinkeln ist eine geometrische Operation.
- **Offene Fragen oder Widersprüche:** Keine.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Betrag und Richtung trennen; zuerst den Wert berechnen, dann die senkrechte Punktkonstruktion ausführen.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 14 | 1 | Wiederholtes Zeichnungslabel der vollständig in Zeile 9 erhaltenen Beziehung; keine zusätzliche Evidenz |
| **Summe** | **1** | **1 Wiederholung** |
