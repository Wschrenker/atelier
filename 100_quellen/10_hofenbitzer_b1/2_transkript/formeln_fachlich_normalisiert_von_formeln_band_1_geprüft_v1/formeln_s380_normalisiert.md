# Fachlich normalisierte Formeln — S. 380

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/10_ausschnitte_s370-437/formeln_s380_codex_v2.md`
Originaltranskript: `../Band_1_geprüft_v1/s380_codex_v2.md`
Buchseite: Hofenbitzer, Band 1, S. 380

## HOF-B1-S380-F01 — Rückenteil-Mehrweite aus nicht vollständig aufgenommenen Abnäherinhalten

- **Fachlicher Zweck:** Die vorhandenen Abnäherinhalte summieren und die entstehende Mehrweite aus der Differenz zum tatsächlich an der Teilungsnaht entfernten Betrag bestimmen.
- **Quelle:** `formeln_s380_codex_v2.md`, Zeile 9; Originaltranskript `s380_codex_v2.md`, Zeile 31; Buchseite 380.
- **Originalbezeichnung:** `3,5 cm` an der Naht entfernt gegenüber `2 cm + 2,7 cm = 4,7 cm` Abnäherinhalten; dadurch entsteht Mehrweite im RT.
- **Normalisierte Bezeichnung:** `rueckenteil_mehrweite_aus_abnaeherdifferenz`

### Buchfassung

```text
8. Im RT können beide Taillenabnäher in der Teilungsnaht aufgenommen werden. Dabei sollte der dort entfernte Abnäherinhalt nicht mehr als ca. 4 cm betragen. Hier wird deutlich weniger Weite (3,5 cm) an der Naht entfernt, als Abnäherinhalte (2 cm + 2,7 cm = 4,7 cm) im Grundschnitt vorhanden sind. Es entsteht somit Mehrweite im RT.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `abnaeherinhalt_1` | erster Abnäherinhalt im RT | 2 | cm |
| `abnaeherinhalt_2` | zweiter Abnäherinhalt im RT | 2,7 | cm |
| `entfernte_weite_teilungsnaht` | an der Naht entfernte Weite | 3,5 | cm |
| `empfohlene_obergrenze_entfernung` | nicht mehr als ca. 4 cm | ca. 4 | cm |

### Formel und Rechenschritte

```text
abnaeherinhalt_gesamt = abnaeherinhalt_1 + abnaeherinhalt_2
                       = 2 cm + 2,7 cm
                       = 4,7 cm

mehrweite_rueckenteil = abnaeherinhalt_gesamt - entfernte_weite_teilungsnaht
                       = 4,7 cm - 3,5 cm
                       = 1,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `abnaeherinhalt_gesamt` | Summe der vorhandenen Abnäherinhalte | 4,7 | cm |
| `mehrweite_rueckenteil` | gegenüber dem Grundschnitt verbleibende Mehrweite im RT | 1,2 | cm |

- **Abhängigkeiten:** Beide Abnäherinhalte des Rückenteils und tatsächlich an der Teilungsnaht entfernter Weitenbetrag.
- **Gültigkeitsbereich:** Alternative Englische Naht am taillierten Oberteil-Grundschnitt mit Aufnahme beider RT-Taillenabnäher auf S. 380.
- **Technische Randbedingung:** Der entfernte Abnäherinhalt soll laut Buch nicht mehr als ungefähr `4 cm` betragen. Die Mehrweite ist nur positiv, wenn weniger Weite entfernt wird, als Abnäherinhalt vorhanden ist.
- **Offene Fragen oder Widersprüche:** Keine. Die gedruckte Summe `4,7 cm` ist korrekt; die daraus folgende Mehrweite `1,2 cm` ist eine technische Ausrechnung der im Buch ausdrücklich beschriebenen Differenz, aber nicht als Zahl gedruckt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Summe und Differenz getrennt ausgeben und die ungefähre Obergrenze als prüfbare Warnschwelle, nicht als harte mathematische Identität modellieren.

## Ausgeschlossene Kandidaten

Keine. Die einzige extrahierte Kandidatenzeile ist vollständig in einem Formelblock abgebildet.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript enthält außerhalb des verbindlichen Extrakts weitere Lage-, Öffnungs- und Abnäher-Verschiebungsangaben. Sie wurden nicht als zusätzliche Buchfassungen erzeugt. Der Abschluss von `M02` gilt für den vorhandenen extrahierten Kandidatenbestand.
