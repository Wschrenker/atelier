# Fachlich normalisierte Formeln — S. 302

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s302.md`  
Originaltranskript: `s302.md`  
Buchseite: Hofenbitzer, Band 1, S. 302

## HOF-B1-S302-F01 — Seitliche Einschnittöffnung aus Kragenbreite und Steghöhe

- **Fachlicher Zweck:** Die Öffnung der beiden seitlichen Einschnitte am Umlegekragen aus der Differenz zwischen Kragenbreite und Steghöhe bestimmen.
- **Quelle:** `formeln_s302.md`, Zeile 7–10 (Buchfassung Zeile 39); Originaltranskript `s302.md`, Zeile 39; Buchseite 302.
- **Originalbezeichnung:** `½ der Differenz zwischen Kragenbreite (KrB) und Steghöhe (StegH)`.
- **Normalisierte Bezeichnung:** `seitliche_einschnittoeffnung_aus_kragenbreite_und_steghoehe`

### Buchfassung

```text
11. Die Öffnung der beiden seitlichen Einschnitte ist ca. ½ der Differenz zwischen Kragenbreite (KrB) und Steghöhe (StegH), hier 4,5 cm − 3 cm = 1,5 cm → ½ = 0,7 cm.
```

### Formel und Rechenschritte

```text
seitliche_einschnittoeffnung = (kragenbreite - steghoehe) / 2
```

Buchwerte:

```text
kragenbreite - steghoehe = 4,5 cm - 3 cm = 1,5 cm
exakte_halbe_differenz = 1,5 cm / 2 = 0,75 cm
```

Der Buchwert `0,7 cm` weicht vom exakten Ergebnis `0,75 cm` ab. Eine Rundungs- oder Abbruchregel ist nicht angegeben.

### Ausgabe

| Technische Variable | Bedeutung | Wert im Buchbeispiel | Einheit |
|---|---|---:|---|
| `seitliche_einschnittoeffnung` | Öffnung je seitlichem Einschnitt | 0,7 gedruckt; 0,75 exakt | cm |

- **Abhängigkeiten:** Kragenbreite KrB und Steghöhe StegH.
- **Gültigkeitsbereich:** Anliegender Umlegekragen mit innenliegendem Kragensteg; beide seitlichen Einschnitte.
- **Technische Randbedingung:** Die Öffnung wird als halbe Differenz interpretiert; eine konkrete Rundung darf nicht stillschweigend ergänzt werden.
- **Offene Fragen oder Widersprüche:** `1,5 cm / 2 = 0,75 cm`, nicht `0,7 cm`. Die Quelle nennt keine Rundungsregel.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Erst Rundungsentscheidung fachlich klären; exakten Wert `0,75 cm` und Buchwert `0,7 cm` getrennt speichern.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 12–15 | 1 | Hochstellungs-, Halsloch- und Steghöhenangaben ohne eigenständige Zielberechnung |
| 17–20 | 1 | Stegnaht-, Abstands- und Maßlabels ohne eigenständige Zielberechnung |
| 22–25 | 1 | Kragenabstich und gewünschte Kragenbreite als direkte Eingaben |
| 27–30 | 1 | Drittel- und Halslochmaß als direkte Konstruktionsangaben |
| 32–35 | 1 | Mess- und Öffnungslabels ohne belegte Eingabe-Ausgabe-Beziehung |
| **Summe** | **5** | **Eingabe-, Maß- und Konstruktionsangaben ausgeschlossen** |
