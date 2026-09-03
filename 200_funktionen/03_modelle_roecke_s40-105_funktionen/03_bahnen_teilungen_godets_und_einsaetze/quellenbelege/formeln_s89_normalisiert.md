# Fachlich normalisierte Formeln — S. 89

Quelle der Normalisierung: `formeln_s89_digital_geprüft.md`
Originaltranskript: `s89_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 89
Extraktionsstand: v2

## HOF-B1-S089-F01 — Faltentiefe als halber Falteninhalt

- **Fachlicher Zweck:** Die Faltentiefe am Anfang des Faltenteils als Hälfte des Falteninhalts bestimmen.
- **Quelle:** `formeln_s89_digital_geprüft.md`, Zeile 9; Originaltranskript `s89_digital_geprüft.md`, Zeile 32; Buchseite 89.
- **Originalbezeichnung:** `einen halben Falteninhalt (≙ FaT)`
- **Normalisierte Bezeichnung:** `faltentiefe_aus_falteninhalt`

### Buchfassung

```text
9. □4 Am VT und am RT jeweils einen halben Falteninhalt (≙ FaT) in entsprechender Höhe anzeichnen → Falteninnennaht.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---|---|
| `falteninhalt` | Falteninhalt FaI | nicht angegeben | cm |
| `anteil_faltentiefe` | halber Falteninhalt | 1/2 | dimensionslos |

### Formel und Rechenschritte

```text
faltentiefe = falteninhalt * anteil_faltentiefe
             = falteninhalt / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---|---|
| `faltentiefe` | Faltentiefe FaT | `½ FaI` | cm |

- **Abhängigkeiten:** Ein zuvor bestimmter `falteninhalt`, auf S. 88 im Buchbeispiel durch `HOF-B1-S088-F02` belegt.
- **Gültigkeitsbereich:** Anfang und Ende des Faltenteils sowie die Anschlüsse an VT und RT des Passenrocks auf S. 89.
- **Technische Randbedingung:** `falteninhalt` muss als nichtnegative Länge vorliegen.
- **Offene Fragen oder Widersprüche:** Keine. Die zwei weiteren extrahierten Sätze wiederholen dieselbe Halbierungsbeziehung an anderen Stellen des Faltenteils.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Die Faltentiefe einmal aus dem Falteninhalt ableiten und an den drei beschriebenen geometrischen Positionen wiederverwenden.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s89_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Wiederholung von `HOF-B1-S089-F01` am Beginn des separaten Faltenteils; keine neue Rechenbeziehung |
| Zeile 19 | 1 | Wiederholung derselben halben Falteninhalt-/Faltentiefe-Beziehung am Ende des Faltenteils |
| **Summe** | **2** | **2 Wiederholungen ausgeschlossen** |
