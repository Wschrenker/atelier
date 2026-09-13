# Fachlich normalisierte Formeln — S. 237

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/08_aermel_varianten_s221-289/formeln_s237_codex_v2_digital_geprueft.md`
Originaltranskript: `../hofenbitzer_band_1_digital/08_aermel_varianten_s221-289/s237_codex_v2_digital_geprueft.md`
Buchseite: Hofenbitzer, Band 1, S. 237

## HOF-B1-S237-F01 — Mindestabstand des untersten Knopfes vom Saum

- **Fachlicher Zweck:** Den Mindestabstand des untersten Ärmelknopfes vom Saum aus dem Knopfdurchmesser bestimmen.
- **Quelle:** `formeln_s237_codex_v2_digital_geprueft.md`, Zeile 15; Originaltranskript `s237_codex_v2_digital_geprueft.md`, Zeile 50; Buchseite 237.
- **Originalbezeichnung:** `Abstand vom Saum mind. 2 × Knopfdurchmesser`
- **Normalisierte Bezeichnung:** `mindestabstand_unterster_aermelknopf_zum_saum`

### Buchfassung

```text
- Abstand vom Saum mind. 2 × Knopfdurchmesser
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `knopfdurchmesser` | Knopfdurchmesser | nicht angegeben | cm |
| `mindestfaktor` | `2 ×` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
mindestabstand_unterster_aermelknopf_zum_saum = mindestfaktor * knopfdurchmesser
                                                = 2 * knopfdurchmesser
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---|---|
| `mindestabstand_unterster_aermelknopf_zum_saum` | kleinster zulässiger Abstand vom Saum | `2 × Knopfdurchmesser` | cm |

- **Abhängigkeiten:** Durchmesser des verwendeten Ärmelknopfes.
- **Gültigkeitsbereich:** Blazer-Zweinahtärmel mit echtem geknöpftem Schlitz auf S. 237.
- **Technische Randbedingung:** Knopfdurchmesser und Abstand müssen in derselben Längeneinheit geführt werden; der tatsächliche Abstand darf den berechneten Mindestwert überschreiten.
- **Offene Fragen oder Widersprüche:** Keine; die Buchfassung gibt eine eindeutige Mindestbeziehung ohne Zahlenbeispiel an.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Mindestbedingung `abstand >= 2 * knopfdurchmesser` prüfen, nicht als festen Abstand erzwingen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s237_codex_v2_digital_geprueft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 9–10 und 20–21 | 4 | Zweimal wiederholte Schnittteil- und Zuschnittbeschriftungen von Ober- und Unterärmel; `2×-p` bezeichnet Stückzahl und paarigen Zuschnitt, keine Berechnung |
| **Summe** | **4** | **4 Produktions-/Zuschnittbeschriftungen ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript nennt außerhalb des verbindlichen Extrakts identische Schlitzhöhen und Einschlagbreiten, eine Kürzung der Untertritt-Saumkante um `0,2 cm` sowie eine mögliche Vorverlegung der Ärmelnaht um etwa `2 bis 3 cm`. Das sind direkte Konstruktions-, Änderungs- oder Eingabeangaben; sie wurden nicht als zusätzliche Buchfassungen erzeugt. Der Abschluss von S. 237 gilt für den vorhandenen extrahierten Kandidatenbestand.
