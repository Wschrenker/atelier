# Fachlich normalisierte Formeln — S. 444

Quelle der Normalisierung: `formeln_s444_digital_geprüft.md`
Originaltranskript: `s444_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 444

## HOF-B1-S444-F01 — Breite des ersten Knopfleisten-Einschlags

- **Fachlicher Zweck:** Die Breite des ersten Einschlags aus dem gemessenen Abstand zwischen vorderer Kante und Absteppnaht plus einer kleinen Zugabe bestimmen.
- **Quelle:** `formeln_s444_digital_geprüft.md`, Zeile 9; Originaltranskript `s444_digital_geprüft.md`, Zeile 36; Buchseite 444.
- **Originalbezeichnung:** erster Einschlag plus ca. `0,2 cm`
- **Normalisierte Bezeichnung:** `knopfleiste_erster_einschlag`

### Buchfassung

```text
5. □4+5 Den Abstand zwischen vorderer Kante und Abstepp-Naht messen und den ersten Einschlag + ca. 0,2 cm anzeichnen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `abstand_vordere_kante_absteppnaht` | gemessener Abstand zwischen vorderer Kante und Abstepp-Naht | variabel | cm |
| `einschlag_zugabe` | `ca. 0,2 cm` | ca. 0,2 | cm |

### Formel und Rechenschritte

```text
knopfleiste_erster_einschlag = abstand_vordere_kante_absteppnaht + einschlag_zugabe
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `knopfleiste_erster_einschlag` | Breite des ersten Einschlags | gemessener Abstand plus ca. 0,2 | cm |

- **Abhängigkeiten:** Gemessener Abstand zwischen vorderer Kante und Absteppnaht.
- **Gültigkeitsbereich:** Doppelt eingeschlagene und abgesteppte Knopfleiste der klassischen Hemdbluse auf S. 444.
- **Technische Randbedingung:** Der Zuschlag ist mit `ca.` als Näherungswert belegt und darf nicht als allgemeine exakte Konstante für andere Knopfleisten gelten.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine Toleranz um `0,2 cm`; die Beziehung selbst ist eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den gemessenen Abstand als positive Länge verlangen und den Näherungszuschlag separat parametrieren.
