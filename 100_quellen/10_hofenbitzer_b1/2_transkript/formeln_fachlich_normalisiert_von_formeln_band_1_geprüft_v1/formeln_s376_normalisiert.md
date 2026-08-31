# Fachlich normalisierte Formeln — S. 376

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s376_codex_v2.md`
Originaltranskript: `../Band_1_geprüft_v1/s376_codex_v2.md`
Buchseite: Hofenbitzer, Band 1, S. 376

## HOF-B1-S376-F01 — Gesamte Saumerweiterung über sechs Nähte

- **Fachlicher Zweck:** Die gesamte Saumerweiterung des Modells aus der Erweiterung je Naht und der Anzahl der beteiligten Nähte berechnen.
- **Quelle:** `formeln_s376_codex_v2.md`, Zeile 9; Originaltranskript `s376_codex_v2.md`, Zeile 41; Buchseite 376.
- **Originalbezeichnung:** `Erweiterung = 4,5 cm · 6 Nähte = 27 cm`
- **Normalisierte Bezeichnung:** `gesamte_saumerweiterung_englische_naehte`

### Buchfassung

```text
**Erweiterung = 4,5 cm · 6 Nähte = 27 cm**
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `erweiterung_je_naht` | Erweiterung der Saumweite an jeder Naht | 4,5 | cm |
| `anzahl_naehte` | Nähte am gesamten Modell | 6 | dimensionslos |

### Formel und Rechenschritte

```text
gesamte_saumerweiterung = erweiterung_je_naht * anzahl_naehte
                         = 4,5 cm * 6
                         = 27 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `gesamte_saumerweiterung` | gesamte zusätzliche Saumweite des Modells | 27 | cm |

- **Abhängigkeiten:** Erweiterungsbetrag je Naht und Anzahl der erweiterten Nähte.
- **Gültigkeitsbereich:** Englische Nähte am taillierten Oberteil-Grundschnitt mit identischer Saumerweiterung an sechs Nähten auf S. 376.
- **Technische Randbedingung:** Der Betrag `4,5 cm` gilt je vollständiger Naht; der Originalkontext leitet ihn aus beidseitig jeweils `2,25 cm` Ausstellbetrag ab, diese Vorstufe fehlt jedoch im verbindlichen Extrakt.
- **Offene Fragen oder Widersprüche:** Keine; Multiplikation und Druckergebnis sind rechnerisch konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Erweiterungsbetrag und Nahtanzahl parametrieren; die nicht extrahierte beidseitige Verteilung nicht ohne separaten Quellenbeleg implementieren.

## Ausgeschlossene Kandidaten

Keine. Die einzige extrahierte Kandidatenzeile ist vollständig in einem Formelblock abgebildet.

## Prüfhinweis zur Extraktionsgrenze

Der Originaltext nennt vor der extrahierten Gesamtformel einen Ausstellbetrag von `2,25 cm` an jeder Seite einer Naht und daraus `4,5 cm` Erweiterung je Naht. Diese Herleitung fehlt im verbindlichen Extrakt und wurde nicht als zusätzliche Buchfassung erzeugt. Der Abschluss von `M02` gilt für den vorhandenen extrahierten Kandidatenbestand.
