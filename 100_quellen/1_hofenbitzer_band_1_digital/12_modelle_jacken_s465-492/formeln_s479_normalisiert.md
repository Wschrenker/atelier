# Fachlich normalisierte Formeln — S. 479

Quelle der Normalisierung: `formeln_s479_codex_v2_digital_geprueft.md`
Originaltranskript: `s479_codex_v2_digital_geprueft.md`
Buchseite: Hofenbitzer, Band 1, S. 479

## HOF-B1-S479-F01 — Belegnahtverlängerung am Beleg als Faltentiefe

- **Fachlicher Zweck:** Die Verlängerung der Belegnaht am Vorderteilbeleg gleich der Verlängerung am Vorderteil und gleich der Tiefe der Belegfalte festlegen.
- **Quelle:** `formeln_s479_codex_v2_digital_geprueft.md`, Zeile 10; Originaltranskript `s479_codex_v2_digital_geprueft.md`, Zeile 63; Buchseite 479.
- **Originalbezeichnung:** `Verlängerung der Belegnaht um ca. 0,5 bis 1 cm wie am VT = Faltentiefe`.
- **Normalisierte Bezeichnung:** `belegnaht_verlaengerung_am_beleg`

### Buchfassung

```text
- Verlängerung der Belegnaht um ca. 0,5 bis 1 cm wie am VT = Faltentiefe
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `belegnaht_verlaengerung_am_vt` | Verlängerung der Belegnaht am VT | ca. 0,5 bis 1 | cm |

### Formel und Rechenschritte

```text
belegnaht_verlaengerung_am_beleg = belegnaht_verlaengerung_am_vt
faltentiefe_belegfalte = belegnaht_verlaengerung_am_beleg

Damit:
faltentiefe_belegfalte = belegnaht_verlaengerung_am_beleg = belegnaht_verlaengerung_am_vt
                       = ca. 0,5 bis 1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `belegnaht_verlaengerung_am_beleg` | Verlängerung der Belegnaht am Vorderteilbeleg | ca. 0,5 bis 1 | cm |
| `faltentiefe_belegfalte` | daraus entstehende Tiefe der Belegfalte | ca. 0,5 bis 1 | cm |

- **Abhängigkeiten:** Für dasselbe Modell gewählte Verlängerung der Belegnaht am Vorderteil.
- **Gültigkeitsbereich:** Vorderteilbeleg des klassischen zweireihigen Blazers auf S. 479.
- **Technische Randbedingung:** Beleg und Vorderteil müssen um denselben Betrag verlängert werden. Der Betrag ist ein ungefährer Bereich; die Quelle nennt auf dieser Seite keine Auswahlregel innerhalb von `0,5 bis 1 cm`.
- **Offene Fragen oder Widersprüche:** Keine. Die Auswahl des konkreten Betrags innerhalb des Bereichs bleibt eine Modellentscheidung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einen gemeinsamen Parameter für Vorderteil und Beleg verwenden und denselben Wert als Faltentiefe ausgeben; nur Werte im belegten Näherungsbereich zulassen, ohne eine Auswahlregel zu erfinden.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s479_codex_v2_digital_geprueft.md`, Zeile 9 | 1 | Schnittteil-, Stückzahl-, Material- und Größenbeschriftung; Produktionsangabe, keine Berechnung |
| **Summe** | **1** | **1 Produktionsbeschriftung ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript nennt außerhalb des verbindlichen Extrakts unter anderem die Reduzierung der Belege an der Schulter um ca. `0,2 cm`, Roll- und Verstürzweite sowie weitere Kragen- und Belegmaße. Diese Stellen wurden nicht als zusätzliche Buchfassungen erzeugt. Der Abschluss von `M08` gilt für den vorhandenen extrahierten Kandidatenbestand.
