# Fachlich normalisierte Formeln — S. 391

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/10_ausschnitte_s370-437/formeln_s391_codex_v2.md`
Originaltranskript: `../hofenbitzer_band_1_digital/10_ausschnitte_s370-437/s391_codex_v2.md`
Buchseite: Hofenbitzer, Band 1, S. 391

## HOF-B1-S391-F01 — Saumerweiterung an jeder Seitennaht

- **Fachlicher Zweck:** Die gesamte Erweiterung an einer Seitennaht aus den beidseitigen Ausstellbeträgen bestimmen.
- **Quelle:** `formeln_s391_codex_v2.md`, Zeilen 9 und 14; Originaltranskript `s391_codex_v2.md`, Zeilen 32 und 35; Buchseite 391.
- **Originalbezeichnung:** `4 cm an jeder Naht`; an den Seitennahtkanten jeweils `2 cm`.
- **Normalisierte Bezeichnung:** `saumerweiterung_je_seitennaht`

### Buchfassung

```text
= 4 cm an jeder Naht:
```

```text
8. an den SN: 2 · 2 cm = 4 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `ausstellbetrag_je_seitennahtkante` | Ausstellbetrag an jeder Seite der SN | 2 | cm |
| `anzahl_seitennahtkanten` | beide Kanten einer Seitennaht | 2 | dimensionslos |

### Formel und Rechenschritte

```text
saumerweiterung_je_seitennaht = anzahl_seitennahtkanten * ausstellbetrag_je_seitennahtkante
                               = 2 * 2 cm
                               = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `saumerweiterung_je_seitennaht` | gesamte Erweiterung an einer Seitennaht | 4 | cm |

- **Abhängigkeiten:** Ausstellbetrag an jeder der beiden Kanten einer Seitennaht.
- **Gültigkeitsbereich:** Saumerweiterung des ausgestellten Modells mit Flankennähten auf S. 391.
- **Technische Randbedingung:** Die allgemeine Herleitung `24 cm Saumerweiterung : 6 Nähte` steht nur im Originaltranskript und fehlt im verbindlichen Formel-Extrakt. Die Normalisierung bildet deshalb ausschließlich die extrahierte Seitennahtrechnung ab.
- **Offene Fragen oder Widersprüche:** Keine. `2 · 2 cm = 4 cm` ist rechnerisch konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ausstellbetrag je Nahtkante und Anzahl der beteiligten Kanten parametrieren; die nicht extrahierte Gesamtverteilung über sechs Nähte nicht als Buchfassung implementieren.

## HOF-B1-S391-F02 — Vorderteil-Saumerweiterung nach Entfernen des Hüftausfalls

- **Fachlicher Zweck:** Den am Vorderteil noch anzuzeichnenden Ausstellbetrag nach Abzug des durch den entfernten Hüftausfall entstehenden Weitenanteils berechnen und gleichmäßig auf zwei Kanten verteilen.
- **Quelle:** `formeln_s391_codex_v2.md`, Zeile 15; Originaltranskript `s391_codex_v2.md`, Zeile 36; Buchseite 391.
- **Originalbezeichnung:** `Ausstellbetrag minus Hüftausfall = 4 cm - 1 cm = 2 · 1,5 cm = 3 cm`.
- **Normalisierte Bezeichnung:** `vorderteil_ausstellbetrag_nach_hueftausfall`

### Buchfassung

```text
9. am Vorderteil: Ausstellbetrag minus Hüftausfall (kommt durch Entfernen im VT als Weite hinzu) = 4 cm - 1 cm = 2 · 1,5 cm = 3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `geplanter_ausstellbetrag_je_naht` | Ausstellbetrag | 4 | cm |
| `entfernter_hueftausfall` | Hüftausfall, der durch Entfernen im VT als Weite hinzukommt | 1 | cm |
| `anzahl_vorderteilkanten` | zwei Kanten am Vorderteil | 2 | dimensionslos |

### Formel und Rechenschritte

```text
vorderteil_ausstellbetrag_gesamt = geplanter_ausstellbetrag_je_naht - entfernter_hueftausfall
                                  = 4 cm - 1 cm
                                  = 3 cm

vorderteil_ausstellbetrag_je_kante = vorderteil_ausstellbetrag_gesamt / anzahl_vorderteilkanten
                                    = 3 cm / 2
                                    = 1,5 cm

kontrolle = anzahl_vorderteilkanten * vorderteil_ausstellbetrag_je_kante
           = 2 * 1,5 cm
           = 3 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `vorderteil_ausstellbetrag_gesamt` | am Vorderteil noch anzuzeichnender gesamter Ausstellbetrag | 3 | cm |
| `vorderteil_ausstellbetrag_je_kante` | Ausstellbetrag an jeder der beiden Vorderteilkanten | 1,5 | cm |

- **Abhängigkeiten:** Geplanter Ausstellbetrag je Naht, durch Entfernen als Weite hinzukommender Hüftausfall und zwei Vorderteilkanten.
- **Gültigkeitsbereich:** Vorderteil des ausgestellten Modells mit Flankennähten und vereinfacht entferntem Hüftausfall auf S. 391.
- **Technische Randbedingung:** Der Hüftausfall wird in diesem Modell laut Buch entfernt und sein Betrag deshalb vom noch anzuzeichnenden Ausstellbetrag abgezogen.
- **Offene Fragen oder Widersprüche:** Keine. Sowohl `4 cm - 1 cm = 3 cm` als auch `2 · 1,5 cm = 3 cm` sind rechnerisch konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Abzug und anschließende symmetrische Verteilung als zwei getrennte Rechenschritte ausgeben; den Hüftausfall nicht erneut als zusätzliche Saumweite addieren.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s391_codex_v2.md`, Zeile 20 | 1 | Zeichnungslabel `messen = 1 cm`; der Wert ist bereits als Hüftausfall in `HOF-B1-S391-F02` enthalten und liefert keine zusätzliche Rechenbeziehung |
| **Summe** | **1** | **1 wiederholtes Mess- und Eingabelabel ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Die allgemeine Verteilung `24 cm Saumerweiterung : 6 Nähte`, der unveränderte Ausstellbetrag von `4 cm` am Rückteil und mehrere geometrische Übertragungs- und Formungsregeln stehen nur im Originaltranskript. Sie wurden nicht als zusätzliche Buchfassungen erzeugt. Der Abschluss von `M03` gilt für den vorhandenen extrahierten Kandidatenbestand.
