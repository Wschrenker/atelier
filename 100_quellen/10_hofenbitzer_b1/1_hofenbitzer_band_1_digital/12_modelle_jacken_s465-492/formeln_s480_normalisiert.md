# Fachlich normalisierte Formeln — S. 480

Quelle der Normalisierung: `formeln_s480_codex_v2_digital_geprueft.md`
Originaltranskript: `s480_codex_v2_digital_geprueft.md`
Buchseite: Hofenbitzer, Band 1, S. 480

## HOF-B1-S480-F01 — Belegnahtverlängerung am Vorderteil als Faltentiefe

- **Fachlicher Zweck:** Die Verlängerung der Belegnaht am Vorderteil gleich der Verlängerung am Beleg und gleich der Tiefe der Belegfalte festlegen.
- **Quelle:** `formeln_s480_codex_v2_digital_geprueft.md`, Zeile 17; Originaltranskript `s480_codex_v2_digital_geprueft.md`, Zeile 40; Buchseite 480.
- **Originalbezeichnung:** `Verlängerung der Belegnaht um ca. 0,5 bis 1 cm wie am Beleg = Faltentiefe`.
- **Normalisierte Bezeichnung:** `belegnaht_verlaengerung_am_vt`

### Buchfassung

```text
- Verlängerung der Belegnaht um ca. 0,5 bis 1 cm wie am Beleg = Faltentiefe
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `belegnaht_verlaengerung_am_beleg` | Verlängerung der Belegnaht am Beleg | ca. 0,5 bis 1 | cm |

### Formel und Rechenschritte

```text
belegnaht_verlaengerung_am_vt = belegnaht_verlaengerung_am_beleg
faltentiefe_belegfalte = belegnaht_verlaengerung_am_vt

Damit:
faltentiefe_belegfalte = belegnaht_verlaengerung_am_vt = belegnaht_verlaengerung_am_beleg
                       = ca. 0,5 bis 1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `belegnaht_verlaengerung_am_vt` | Verlängerung der Belegnaht am Vorderteil | ca. 0,5 bis 1 | cm |
| `faltentiefe_belegfalte` | daraus entstehende Tiefe der Belegfalte | ca. 0,5 bis 1 | cm |

- **Abhängigkeiten:** Für dasselbe Modell gewählte Verlängerung der Belegnaht am Beleg.
- **Gültigkeitsbereich:** Produktionsschnitt der Rumpfteile des klassischen zweireihigen Blazers auf S. 480.
- **Technische Randbedingung:** Vorderteil und Beleg müssen um denselben Betrag verlängert werden. Der Betrag ist ein ungefährer Bereich; das Originaltranskript präzisiert die Auswahl nach Modelllänge, der verbindliche Extrakt selbst enthält diese Auswahlregel jedoch nicht.
- **Offene Fragen oder Widersprüche:** Keine innerhalb der extrahierten Beziehung. Die konkrete Auswahl innerhalb von `0,5 bis 1 cm` ist im Extrakt nicht bestimmt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einen gemeinsamen Parameter für Vorderteil und Beleg verwenden und denselben Wert als Faltentiefe ausgeben. Die modelllängenabhängige Auswahl erst implementieren, wenn sie in der Extraktionsschicht vollständig belegt ist.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s480_codex_v2_digital_geprueft.md`, Zeilen 9–12 | 4 | Schnittteil-, Stückzahl-, Material- und Größenbeschriftungen; Produktionsangaben, keine Berechnungen |
| **Summe** | **4** | **4 Produktionsbeschriftungen ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript enthält außerhalb des verbindlichen Extrakts die allgemeine Verlängerungsregel für Vorderteil und Beleg nach Modelllänge sowie Abstands-, Saumeinschlag- und Nahtzugabenwerte. Diese Stellen wurden nicht als zusätzliche Buchfassungen erzeugt. Die extrahierte Zeichnungsbeziehung belegt nur die Gleichheit von Vorderteil-, Belegverlängerung und Faltentiefe im Bereich von ca. `0,5 bis 1 cm`. Der Abschluss von `M08` gilt für den vorhandenen extrahierten Kandidatenbestand.
