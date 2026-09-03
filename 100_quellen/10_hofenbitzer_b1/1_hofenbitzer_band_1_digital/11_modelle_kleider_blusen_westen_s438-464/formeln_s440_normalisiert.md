# Fachlich normalisierte Formeln — S. 440

Quelle der Normalisierung: `formeln_s440_digital_geprüft.md`
Originaltranskript: `s440_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 440

## HOF-B1-S440-F01 — Öffnungsbetrag für eine Biese

- **Fachlicher Zweck:** Den Öffnungsbetrag an der eingeschnittenen Biesenkante aus der Biesentiefe bestimmen.
- **Quelle:** `formeln_s440_digital_geprüft.md`, Zeile 14; Originaltranskript `s440_digital_geprüft.md`, Zeile 42; Buchseite 440.
- **Originalbezeichnung:** doppelte Biesentiefe (`BiT`)
- **Normalisierte Bezeichnung:** `biesenkanten_oeffnungsbetrag`

### Buchfassung

```text
9. □2+4+5 Die Biesenkante einschneiden und um die doppelte Biesentiefe (BiT) öffnen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `biesentiefe` | Biesentiefe (BiT) | variabel | cm |

### Formel und Rechenschritte

```text
biesenkanten_oeffnungsbetrag = 2 * biesentiefe
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `biesenkanten_oeffnungsbetrag` | Öffnungsbetrag an der Biesenkante | doppelte Biesentiefe | cm |

- **Abhängigkeiten:** Fachlich gewählte Biesentiefe `BiT`.
- **Gültigkeitsbereich:** Knopfleiste mit Biese der Bluse mit Schulterpasse auf S. 440.
- **Technische Randbedingung:** `biesentiefe > 0`; der Öffnungsbetrag wird rechtwinklig zur eingeschnittenen Biesenkante angewendet.
- **Offene Fragen oder Widersprüche:** Keine innerhalb der extrahierten Beziehung. Die Quelle nennt auf dieser Seite keinen Zahlenwert für `BiT`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Biesentiefe als positive Länge verlangen und den doppelten Betrag als Öffnungsweite ausgeben.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s440_digital_geprüft.md`, Zeile 9 | 1 | Passformklassen- und Grundschnittangabe mit Seitenverweis `192+193`; Anwendungsbereich, keine Rechenformel |
| **Summe** | **1** | **1 Kontext-/Anwendungszeile ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript nennt außerhalb des verbindlichen Extrakts unter anderem die Übertrittbreite als halbe Leistenbreite sowie einen Einschlag aus Leistenbreite minus ca. `0,1 bis 0,2 cm`. Diese Beziehungen wurden nicht als Buchfassungen erfunden. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
