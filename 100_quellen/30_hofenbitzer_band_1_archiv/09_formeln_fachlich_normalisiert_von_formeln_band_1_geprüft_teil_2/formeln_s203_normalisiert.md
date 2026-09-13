# Fachlich normalisierte Formeln — S. 203

Quelle der Normalisierung: `formeln_s203_digital_geprüft.md`
Originaltranskript: `s203_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 203
Extraktionsstand: v2

## HOF-B1-S203-F01 — Hinterer Ärmelpunkt mit Einhalteweitenanteil

- **Fachlicher Zweck:** Die auf die hintere Ärmelkurve zu übertragende Strecke aus hinterer Achsel und 20 Prozent der Einhalteweite bestimmen.
- **Quelle:** `formeln_s203_digital_geprüft.md`, Zeilen 9–10 und 30; Originaltranskript `s203_digital_geprüft.md`, Zeilen 27–28 und 67; Buchseite 203.
- **Originalbezeichnung:** `hAchsel`, `20% EW`, `hÄP`
- **Normalisierte Bezeichnung:** `uebertragungsstrecke_hinterer_aermelpunkt`

### Buchfassung

```text
- `8,6 cm + 1,3 cm · 0,20`
- `8,6 cm + 0,3 cm = 8,9 cm`
```

```text
hÄP — Die hAchsel + 20% der EW (0,3 cm) auf die hÄk übertragen → hinterer Ärmelpunkt = hÄP.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hintere_achselstrecke` | hAchsel | 8,6 | cm |
| `einhalteweite` | EW | 1,3 | cm |
| `einhalteweite_anteil_hinten` | 20 % | 0,20 | dimensionslos |

### Formel und Rechenschritte

```text
einhalteweitenanteil_exakt = 1,3 cm * 0,20 = 0,26 cm
gedruckter_einhalteweitenanteil = 0,3 cm
uebertragungsstrecke_exakt = 8,6 cm + 0,26 cm = 8,86 cm
fortsetzung_mit_gedrucktem_zwischenwert = 8,6 cm + 0,3 cm = 8,9 cm
gedrucktes_ergebnis = 8,9 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `einhalteweitenanteil_hinten` | 20 % EW | 0,3 gedruckt; 0,26 exakt | cm |
| `uebertragungsstrecke_hinten` | Strecke auf hÄk bis hÄP | 8,9 gedruckt; 8,86 exakt | cm |

- **Abhängigkeiten:** Einhalteweite aus `HOF-B1-S202-F02`; gemessene hAchsel.
- **Gültigkeitsbereich:** Ärmelpunkt des weiten Ärmel-Grundschnitts auf S. 203.
- **Technische Randbedingung:** Exakter Pfad und Fortsetzung vom gedruckten Zwischenwert getrennt erhalten.
- **Offene Fragen oder Widersprüche:** Der gedruckte Zwischenwert `0,3 cm` ist eine Rundung von `0,26 cm`; die anschließende Addition ist mit diesem Zwischenwert konsistent. Eine allgemeine Rundungsregel nennt die Quelle nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern den exakten Anteil verwenden; Buchdarstellung und Fortsetzung vom gedruckten Zwischenwert separat prüfbar halten.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s203_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 15 | 1 | Wiederholt `ÄSaW = OaW = 37 cm` aus `HOF-B1-S202-F01`; keine neue Rechenbeziehung |
| Zeile 20 | 1 | Isolierter gewählter Konstruktionswert `ÄSaW = 22 cm`; Eingabe beziehungsweise Zielwert ohne Berechnung |
| Zeile 25 | 1 | Direkte Übertragung der vAchsel auf die vordere Ärmelkurve; geometrische Punktdefinition ohne Berechnung |
| **Summe** | **3** | **1 Wiederholung + 1 Eingabewert + 1 direkte geometrische Übertragung** |
