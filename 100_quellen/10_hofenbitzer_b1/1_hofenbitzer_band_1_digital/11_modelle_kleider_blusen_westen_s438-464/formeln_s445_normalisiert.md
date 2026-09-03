# Fachlich normalisierte Formeln — S. 445

Quelle der Normalisierung: `formeln_s445_digital_geprüft.md`
Originaltranskript: `s445_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 445

## HOF-B1-S445-F01 — Falteninhalt der Quetschfalte

- **Fachlicher Zweck:** Den Öffnungsbetrag beziehungsweise Falteninhalt der Quetschfalte aus dem doppelten Faltenabstand bestimmen.
- **Quelle:** `formeln_s445_digital_geprüft.md`, Zeile 10; Originaltranskript `s445_digital_geprüft.md`, Zeile 31; Buchseite 445.
- **Originalbezeichnung:** doppelter Faltenabstand (`Falteninhalt`)
- **Normalisierte Bezeichnung:** `quetschfalte_falteninhalt`

### Buchfassung

```text
13. Einschnitt für die Falte oben mit doppeltem Faltenabstand (= Falteninhalt) öffnen und die Quetschfalte fachgerecht markieren.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `faltenabstand` | Faltenabstand (FaA im Seitenkontext) | variabel | cm |

### Formel und Rechenschritte

```text
quetschfalte_falteninhalt = 2 * faltenabstand
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `quetschfalte_falteninhalt` | Öffnungsbetrag und Falteninhalt der Quetschfalte | doppelter Faltenabstand | cm |

- **Abhängigkeiten:** Fachlich festgelegter Faltenabstand.
- **Gültigkeitsbereich:** Quetschfalte in der Rückenteil-Passe der klassischen Hemdbluse auf S. 445.
- **Technische Randbedingung:** `faltenabstand > 0`; die Quelle belegt die Verdopplung für diese Quetschfalte.
- **Offene Fragen oder Widersprüche:** Keine innerhalb der extrahierten Beziehung; ein Zahlenbeispiel ist nicht angegeben.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Faltenabstand als positive Länge verlangen und den doppelten Wert als Falteninhalt beziehungsweise Öffnungsbetrag ausgeben.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s445_digital_geprüft.md`, Zeile 9 | 1 | Bildnummern-/Methodenverweis `□6+8` und qualitative Passenbearbeitung; keine skalare Rechenausgabe |
| **Summe** | **1** | **1 Bild-/Methodenverweis ausgeschlossen** |
