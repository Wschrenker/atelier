# Fachlich normalisierte Formeln — S. 468

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s468.md`
Originaltranskript: `s468.md`
Buchseite: Hofenbitzer, Band 1, S. 468

## HOF-B1-S468-F01 — Saumzugabe aus Saumeinschlag und Nahtzugabe

- **Fachlicher Zweck:** Die insgesamt am Saum von Vorder- und Rückteil zuzugebende Strecke aus Saumeinschlag und Nahtzugabe bestimmen.
- **Quelle:** `formeln_s468.md`, Zeile 21; Originaltranskript `s468.md`, Zeile 21; Buchseite 468.
- **Originalbezeichnung:** `SaEs + NZg = 4 + 1 cm`
- **Normalisierte Bezeichnung:** `saumzugabe_aus_saumeinschlag_und_nahtzugabe`

### Buchfassung

```text
- `SaEs + NZg = 4 + 1 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `saumeinschlag` | `SaEs` (Saumeinschlag) | 4 | cm |
| `nahtzugabe_saum` | `NZg` (Nahtzugabe) | 1 | cm |

### Formel und Rechenschritte

```text
saumzugabe_gesamt = saumeinschlag + nahtzugabe_saum

Buchwerte:
saumzugabe_gesamt = 4 cm + 1 cm = 5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `saumzugabe_gesamt` | Gesamte Zugabe am Saum unterhalb der Jackenlänge (Saumkante) | cm |

- **Abhängigkeiten:** Fertige Jackenlänge beziehungsweise Saumkante des Produktionsschnitts der Rumpfteile (□7).
- **Gültigkeitsbereich:** Einfache Jacke (Janker), G 38; Variante mit eckigem Kantenabstich und angeschnittenem Beleg.
- **Technische Randbedingung:** Der Summenwert `5 cm` ist die rechnerische Auswertung der beiden gedruckten Summanden. Das Buch druckt in der extrahierten Zeile nur die Summanden, keinen Gesamtwert.
- **Offene Fragen oder Widersprüche:** Keine. Die Buchzeile nennt beide Summanden vollständig; sie werden im Originaltranskript als `SaEs 4 cm` und `NZg 1 cm` einzeln bestätigt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Saumeinschlag und Nahtzugabe getrennt führen, weil sie im Produktionsschnitt als zwei parallele Linien angezeichnet werden. Der Abstand `ca. 0,3 cm` vor der vorderen Kante gehört zur Linienführung, nicht zur Summe.

## Ausgeschlossene Kandidaten

| Zeile in `formeln_s468.md` | Kandidat | Ausschlussgrund |
|---|---|---|
| 9 | `VT 2×-p OSt + El, Janker, G 38` | Produktionsschnittteil mit Stückzahl-, Material- und Größenangabe |
| 10 | `RT 1× OSt, Janker, G 38` | Produktionsschnittteil mit Stückzahl-, Material- und Größenangabe |
| 11 | `hBe 1× OSt + El, Janker, G 38` | Produktionsschnittteil mit Stückzahl-, Material- und Größenangabe |
| 16 | `Verlängerung der Belegnaht um ca. 0,5 bis 1 cm = Faltentiefe` | Begriffszuweisung eines Zugabenbereichs ohne berechnete Ausgabe |

**Summe:** 4 ausgeschlossene von 5 extrahierten Kandidatenzeilen.

## Prüfhinweise

1. `4 cm + 1 cm = 5 cm` ist rechnerisch konsistent und wird durch die Einzelbeschriftungen `SaEs 4 cm` und `NZg 1 cm` im Originaltranskript gestützt.
2. **Zeile 16:** `Verlängerung der Belegnaht um ca. 0,5 bis 1 cm = Faltentiefe` benennt die Faltentiefe als Zugabe, führt aber keine Rechenoperation aus. Sie bleibt deshalb ausgeschlossen — wie die vergleichbaren Zugabenzeilen auf S. 157.
3. Das Originaltranskript nennt zu dieser Zeile eine Auswahlregel (Schritt 23: längeres Modell `1 cm`, kürzeres Modell `0,5 cm`), die im verbindlichen Extrakt nicht als Kandidatenzeile vorliegt. Sie wurde nicht als Buchfassung ergänzt.
4. **Extraktionsgrenze:** Weitere Maße des Transkripts (`für das Futter an der SN + 0 bis 0,5 cm`, `an der hM + 0 bis 0,5 cm`, `4 bis 6 cm`, `Abstand ca. 0,3 cm`) stehen nicht im Extrakt und wurden nicht normalisiert.
