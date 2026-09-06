# Fachlich normalisierte Formeln — S. 221

Quelle der Normalisierung: `formeln_s221_digital_geprüft.md`
Originaltranskript: `s221_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 221
Extraktionsstand: v2

## HOF-B1-S221-F01 — Falteninhalt des simulierten Ärmelaufschlags

- **Fachlicher Zweck:** Den Falteninhalt des als Biese simulierten Ärmelaufschlags aus der doppelten Biesentiefe bestimmen.
- **Quelle:** `formeln_s221_digital_geprüft.md`, Zeile 14; Originaltranskript `s221_digital_geprüft.md`, Zeile 21; Buchseite 221.
- **Originalbezeichnung:** Biesentiefe, Falteninhalt
- **Normalisierte Bezeichnung:** `falteninhalt_aermelaufschlag`

### Buchfassung

```text
6. An den oberen Aufschlag 2× die Biesentiefe (= Falteninhalt) anzeichnen.
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `biesentiefe` | Biesentiefe | cm |

### Formel und Rechenschritte

```text
falteninhalt_aermelaufschlag = 2 * biesentiefe
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `falteninhalt_aermelaufschlag` | anzuzeichnender Falteninhalt am oberen Aufschlag | cm |

- **Abhängigkeiten:** Fachlich gewählte Biesentiefe.
- **Gültigkeitsbereich:** Kurzer Ärmel mit als Biese simuliertem Aufschlag auf S. 221.
- **Technische Randbedingung:** Der Betrag wird am oberen Aufschlag angezeichnet; die Richtung und Lage bleiben geometrische Konstruktionsangaben.
- **Offene Fragen oder Widersprüche:** Keine in der extrahierten Beziehung; ein Zahlenbeispiel ist nicht gedruckt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Biesentiefe als positive Länge verlangen und den doppelten Betrag als Falteninhalt ausgeben.

## HOF-B1-S221-F02 — Anzeichnungsbetrag für den echten Ärmelaufschlag

- **Fachlicher Zweck:** Den nach unten anzuzeichnenden Betrag aus der doppelten Aufschlagbreite bestimmen.
- **Quelle:** `formeln_s221_digital_geprüft.md`, Zeile 19; Originaltranskript `s221_digital_geprüft.md`, Zeile 28; Buchseite 221.
- **Originalbezeichnung:** Aufschlagbreite
- **Normalisierte Bezeichnung:** `anzeichnungsbetrag_echter_aermelaufschlag`

### Buchfassung

```text
8. 2× die Aufschlagbreite nach unten anzeichnen.
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `aufschlagbreite` | Aufschlagbreite | cm |

### Formel und Rechenschritte

```text
anzeichnungsbetrag_echter_aermelaufschlag = 2 * aufschlagbreite
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `anzeichnungsbetrag_echter_aermelaufschlag` | nach unten anzuzeichnender Gesamtbetrag | cm |

- **Abhängigkeiten:** Fachlich gewählte Aufschlagbreite.
- **Gültigkeitsbereich:** Kurzer Ärmel mit echtem Ärmelaufschlag auf S. 221.
- **Technische Randbedingung:** Die Richtung „nach unten“ gehört zur Geometrie; der skalare Betrag ist das Doppelte der Aufschlagbreite.
- **Offene Fragen oder Widersprüche:** Keine in der extrahierten Beziehung; ein Zahlenbeispiel ist nicht gedruckt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Betrag und geometrische Richtung getrennt modellieren.

## HOF-B1-S221-F03 — Saumeinschlag unter dem echten Ärmelaufschlag

- **Fachlicher Zweck:** Den Saumeinschlag aus der Aufschlagbreite abzüglich eines ungefähren Zentimeters bestimmen.
- **Quelle:** `formeln_s221_digital_geprüft.md`, Zeile 24; Originaltranskript `s221_digital_geprüft.md`, Zeile 74; Buchseite 221.
- **Originalbezeichnung:** Saum-Einschlag (SaEs), Aufschlagbreite
- **Normalisierte Bezeichnung:** `saumeinschlag_echter_aermelaufschlag`

### Buchfassung

```text
- Saum-Einschlag (SaEs) = Aufschlagbreite - ca. 1 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `aufschlagbreite` | Aufschlagbreite | — | cm |
| `ungefaehrer_abzug` | ca. 1 cm | ca. 1 | cm |

### Formel und Rechenschritte

```text
saumeinschlag = aufschlagbreite - ungefaehrer_abzug
ungefaehrer_abzug = ca. 1 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `saumeinschlag` | Breite des Saumeinschlags unter dem echten Aufschlag | cm |

- **Abhängigkeiten:** Fachlich gewählte Aufschlagbreite.
- **Gültigkeitsbereich:** Echter Ärmelaufschlag auf S. 221.
- **Technische Randbedingung:** Der Abzug ist mit `ca.` nur näherungsweise festgelegt; die Quelle nennt weder Toleranz noch Auswahlregel.
- **Offene Fragen oder Widersprüche:** Kein Rechenwiderspruch. Die zulässige Abweichung vom Richtwert `1 cm` ist nicht belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Abzug als expliziten, fachlich gewählten Näherungswert führen und nicht unsichtbar auf exakt `1 cm` festschreiben.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s221_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 9 | 1 | Abbildungsnummern `□1` und `□4+5` mit Nahtdiagramm-Verweis; das Pluszeichen verbindet Abbildungen und ist keine Rechenoperation |
| **Summe** | **1** | **1 Bildverweis** |

## Extraktionsgrenze

Das Originaltranskript enthält weitere Längen- und Konstruktionsangaben, darunter `Ärmellänge + Bieseninhalt` in Zeile 19. Diese Beziehung fehlt als vollständige Buchfassung im verbindlichen Extrakt und wurde nicht stillschweigend normalisiert. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
