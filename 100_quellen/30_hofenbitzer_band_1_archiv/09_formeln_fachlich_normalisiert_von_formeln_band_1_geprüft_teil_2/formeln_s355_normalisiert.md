# Fachlich normalisierte Formeln — S. 355

Quelle der Normalisierung: `formeln_s355_digital_geprüft.md`
Originaltranskript: `s355_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 355
Extraktionsstand: v2

## HOF-B1-S355-F01 — Taschentiefe für das Hineingreifen mit der Hand

- **Fachlicher Zweck:** Für Taschen, in denen eine Hand Platz haben soll, die Taschentiefe ungefähr an der Eingriffslänge ausrichten.
- **Quelle:** `formeln_s355_digital_geprüft.md`, Zeile 9; Originaltranskript `s355_digital_geprüft.md`, Zeile 11; Buchseite 355.
- **Originalbezeichnung:** Taschentiefe, Eingriffslänge
- **Normalisierte Bezeichnung:** `taschentiefe_aus_eingriffslaenge`

### Buchfassung

```text
Die Taschengröße ist natürlich abhäng vom Zweck und dem zu verstauenden Inhalt (□2+5+10+20). Für Taschen, in denen eine Hand Platz haben soll, gilt □3+4: Die Taschentiefe entspricht ungefähr der Eingriffslänge. Bei zu schmalen Taschen wird es ansonsten schwierig, den Inhalt wieder herauszunehmen. □4: Eine Schrägstellung des Eingriffs kann das Hineingreifen in die Tasche ergonomisch erleichtern.
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `eingriffslaenge` | Eingriffslänge | cm |

### Formel und Rechenschritte

```text
taschentiefe ≈ eingriffslaenge
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `taschentiefe` | ungefähr erforderliche Taschentiefe für eine Handtasche | cm |

- **Abhängigkeiten:** Eine für Hand und Verwendungszweck gewählte `eingriffslaenge`.
- **Gültigkeitsbereich:** Taschen, in denen eine Hand Platz haben soll; nicht als allgemeine Proportionsregel für alle Taschenformen belegt.
- **Technische Randbedingung:** Beide Längen müssen in derselben Einheit vorliegen. `ungefähr` kennzeichnet eine Gestaltungsrichtlinie, keine exakte Gleichheit; Ergonomie, Eingriffswinkel und zu verstauender Inhalt bleiben zusätzliche Anforderungen.
- **Offene Fragen oder Widersprüche:** Kein Widerspruch. Die Quelle nennt keine Toleranz und keine Auswahlregel für eine Abweichung zwischen Taschentiefe und Eingriffslänge.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Richtwert oder prüfbare Empfehlung modellieren, nicht als harte Gleichheitsbedingung. Eine konkrete Abweichung muss fachlich als eigene Eingabe festgelegt werden.

## Ausgeschlossene Kandidaten

Keine. Die einzige extrahierte Kandidatenzeile ist als Buchfassung abgebildet; die darin enthaltenen Bildnummernverweise werden nicht als eigene Additionen interpretiert.

## Extraktionsgrenze

Das Originaltranskript enthält Modellnummern, Halbierungsmarkierungen und qualitative Hinweise zu Position, Verschluss und Eingriffswinkel. Sie bilden keine weiteren vollständigen Rechenbeziehungen und wurden nicht als zusätzliche Buchfassungen erfunden. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
