# Fachlich normalisierte Formeln — S. 306

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/09_kragen_kapuzen_taschen_s290-369/formeln_s306.md`
Originaltranskript: `../hofenbitzer_band_1_digital/09_kragen_kapuzen_taschen_s290-369/s306.md`
Buchseite: Hofenbitzer, Band 1, S. 306

## HOF-B1-S306-F01 — Teilungsanteile der Einschnittabstände am runden Volantkragen

- **Fachlicher Zweck:** Den hinteren und die übrigen Einschnittabstände an der Kragenkante aus der geplanten Anzahl der Einschnitte bestimmen.
- **Quelle:** `formeln_s306.md`, Zeile 9; Originaltranskript `s306.md`, Zeile 30; Buchseite 306.
- **Originalbezeichnung:** `hinterer Abstand = 1 : (geplante Einschnitte * 2 + 1)`; alle anderen Abstände `2/13`.
- **Normalisierte Bezeichnung:** `einschnittabstandsanteile_runder_volantkragen`

### Buchfassung

```text
- Runder Volantkragen: hinterer Abstand des Einschnitts an der Kragenkante = 1 : (geplante Einschnitte * 2 + 1); hier 1 : (6 Einschnitte * 2 + 1) = 1/13. Alle anderen Abstaende sind doppelt so weit entfernt = 2/13.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `anzahl_einschnitte` | geplante Einschnitte | 6 | dimensionslos |
| `gewicht_hinterer_abstand` | einfacher hinterer Abstand | 1 | dimensionslos |
| `gewicht_uebriger_abstand` | doppelte übrige Abstände | 2 | dimensionslos |

### Formel und Rechenschritte

```text
teilungsnenner = anzahl_einschnitte * 2 + 1
                = 6 * 2 + 1
                = 13

hinterer_abstandsanteil = 1 / teilungsnenner
                         = 1 / 13

uebriger_abstandsanteil = 2 / teilungsnenner
                         = 2 / 13
                         = 2 * hinterer_abstandsanteil
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---|---|
| `hinterer_abstandsanteil` | Anteil des hinteren Einschnittabstands an der zugrunde gelegten Kragenkante | `1/13` | dimensionslos |
| `uebriger_abstandsanteil` | Anteil jedes übrigen Einschnittabstands | `2/13` | dimensionslos |

- **Abhängigkeiten:** Geplante Anzahl der Einschnitte an der Kragenkante.
- **Gültigkeitsbereich:** Runder Volantkragen beziehungsweise Harlekin-Kragen mit sechs geplanten Einschnitten auf S. 306.
- **Technische Randbedingung:** Die Anzahl der Einschnitte muss eine positive ganze Zahl sein; der hintere Abstand wird einfach, jeder übrige Abstand doppelt gewichtet.
- **Offene Fragen oder Widersprüche:** Keine; Nenner, hinterer Anteil und doppelte übrige Anteile sind rechnerisch konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Anteile als exakte Brüche führen und erst bei der Multiplikation mit einer konkreten Kragenkantenlänge in ein Längenmaß umrechnen.

## HOF-B1-S306-F02 — Teilungsanteile der Einschnittabstände am V-Ausschnitt-Volantkragen

- **Fachlicher Zweck:** Den hinteren und die übrigen Einschnittabstände an der Kragenkante für den Volantkragen am V-Ausschnitt aus der geplanten Anzahl der Einschnitte bestimmen.
- **Quelle:** `formeln_s306.md`, Zeile 10; Originaltranskript `s306.md`, Zeile 31; Buchseite 306.
- **Originalbezeichnung:** `hinterer Abstand = 1 : (geplante Einschnitte * 2 + 1)`; alle anderen Abstände `2/17`.
- **Normalisierte Bezeichnung:** `einschnittabstandsanteile_volantkragen_v_ausschnitt`

### Buchfassung

```text
- Volantkragen am V-Ausschnitt: hinterer Abstand des Einschnitts an der Kragenkante = 1 : (geplante Einschnitte * 2 + 1); hier 1 : (8 Einschnitte * 2 + 1) = 1/17. Alle anderen Abstaende sind doppelt so weit entfernt = 2/17.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `anzahl_einschnitte` | geplante Einschnitte | 8 | dimensionslos |
| `gewicht_hinterer_abstand` | einfacher hinterer Abstand | 1 | dimensionslos |
| `gewicht_uebriger_abstand` | doppelte übrige Abstände | 2 | dimensionslos |

### Formel und Rechenschritte

```text
teilungsnenner = anzahl_einschnitte * 2 + 1
                = 8 * 2 + 1
                = 17

hinterer_abstandsanteil = 1 / teilungsnenner
                         = 1 / 17

uebriger_abstandsanteil = 2 / teilungsnenner
                         = 2 / 17
                         = 2 * hinterer_abstandsanteil
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---|---|
| `hinterer_abstandsanteil` | Anteil des hinteren Einschnittabstands an der zugrunde gelegten Kragenkante | `1/17` | dimensionslos |
| `uebriger_abstandsanteil` | Anteil jedes übrigen Einschnittabstands | `2/17` | dimensionslos |

- **Abhängigkeiten:** Geplante Anzahl der Einschnitte an der Kragenkante.
- **Gültigkeitsbereich:** Volantkragen am V-Ausschnitt mit acht geplanten Einschnitten auf S. 306.
- **Technische Randbedingung:** Die Anzahl der Einschnitte muss eine positive ganze Zahl sein; der hintere Abstand wird einfach, jeder übrige Abstand doppelt gewichtet.
- **Offene Fragen oder Widersprüche:** Keine; Nenner, hinterer Anteil und doppelte übrige Anteile sind rechnerisch konsistent.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Dieselbe parametrisierte Teilungsfunktion wie beim runden Volantkragen verwenden; nur die geplante Einschnittzahl unterscheidet die beiden Buchbeispiele.

## Ausgeschlossene Kandidaten

Keine. Beide extrahierten Kandidatenzeilen sind jeweils vollständig in einem Formelblock abgebildet.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript nennt außerhalb des verbindlichen Extrakts Halslochverbreiterung, Kragenbreite und Produktionsschnitt-Abstände als Eingabebereiche oder Zeichnungsangaben. Sie sind keine weiteren aus Eingaben berechneten Beziehungen und wurden nicht als zusätzliche Buchfassungen erzeugt. Der Abschluss von `K03` gilt für den vorhandenen extrahierten Kandidatenbestand.
