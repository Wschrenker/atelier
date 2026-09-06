# Fachlich normalisierte Formeln — S. 112

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s112.md`
Originaltranskript: `s112.md`
Buchseite: Hofenbitzer, Band 1, S. 112

## HOF-B1-S112-F01 — Halb- und Viertelpunkte der unteren Hilfsstrecke

- **Fachlicher Zweck:** Auf der unteren Hilfsstrecke zur Schrittlinie die Halb- und Viertelpunkte für die Formung des vorderen Hosenausschnitts bestimmen.
- **Quelle:** `formeln_s112.md`, Zeile 9; Originaltranskript `s112.md`, Zeile 15; Buchseite 112.
- **Originalbezeichnung:** `untere Strecke zur Schrittlinie halbieren und vierteln`.
- **Normalisierte Bezeichnung:** `hilfsstrecke_halb_und_viertelpunkte`

### Buchfassung

```text
□3+3a Die vM-Naht als Hilfslinie verlängern und die untere Strecke zur Schrittlinie halbieren und vierteln.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `untere_hilfsstrecke` | untere Strecke der verlängerten vM-Naht bis zur Schrittlinie | variabel | cm |

### Formel und Rechenschritte

```text
halbe_hilfsstrecke = untere_hilfsstrecke / 2
viertel_hilfsstrecke = untere_hilfsstrecke / 4
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `halbe_hilfsstrecke` | Abstand zum Halbpunkt | cm |
| `viertel_hilfsstrecke` | Abstand zum Viertelpunkt | cm |

- **Abhängigkeiten:** Verlängerte vM-Hilfslinie und ihr Schnitt mit der Schrittlinie.
- **Gültigkeitsbereich:** Detailkonstruktion des vorderen Hosenausschnitts auf S. 112.
- **Technische Randbedingung:** Die Bruchteile beziehen sich auf dieselbe untere Strecke; `□3+3a` ist ein Abbildungsverweis und keine Addition.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine numerische Streckenlänge, die geometrische Teilungsbeziehung ist jedoch eindeutig.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Punkte entlang der vorhandenen Strecke parametrisch bei `1/4` und `1/2` platzieren.

## HOF-B1-S112-F02 — Taillenstrecke der Vorderhose

- **Fachlicher Zweck:** Die auf der erhöhten Taillenlinie abzutragende Strecke aus Viertel-Taillenumfang, gewünschtem Abnäherinhalt und gewünschter Einhalteweite bestimmen.
- **Quelle:** `formeln_s112.md`, Zeile 14; Originaltranskript `s112.md`, Zeile 29; Buchseite 112.
- **Originalbezeichnung:** `TaU : 4 + gewünschter Abnäherinhalt + gewünschte Einhalteweite`.
- **Normalisierte Bezeichnung:** `taillenstrecke_vorderhose`

### Buchfassung

```text
21. Von P20 werden TaU : 4 + gewünschter Abnäherinhalt + gewünschte Einhalteweite auf die erhöhte Taillenlinie abgetragen.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | variabel | cm |
| `abnaeherinhalt` | gewünschter Abnäherinhalt | explizite Auswahl | cm |
| `einhalteweite` | gewünschte Einhalteweite | explizite Auswahl | cm |

### Formel und Rechenschritte

```text
taillenstrecke_vorderhose = (taillenumfang / 4) + abnaeherinhalt + einhalteweite
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `taillenstrecke_vorderhose` | von P20 auf der erhöhten Taillenlinie abzutragende Strecke | cm |

- **Abhängigkeiten:** TaU sowie fachlich gewählte Werte für Abnäherinhalt und Einhalteweite.
- **Gültigkeitsbereich:** Erste Variante der Vorderhosen-Taillennaht auf S. 112.
- **Technische Randbedingung:** Alle drei Längen werden addiert; die zweite, frei geformte Variante ist kein Rechenweg dieser Formel.
- **Offene Fragen oder Widersprüche:** Die Auswahlregeln für Abnäherinhalt und Einhalteweite sind nicht Teil der extrahierten Buchfassung.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Beide Gestaltungswerte als Pflichtparameter führen und die Konstruktionsvariante explizit wählen lassen.

## Ausgeschlossene Kandidaten

| Extraktzeilen | Anzahl | Ausschlussgrund |
|---|---:|---|
| 19 | 1 | Unvollständiges Zeichnungslabel `TaU : 4`; bereits als Operand der vollständigen Beziehung in Zeile 14 vertreten |
| 24 | 1 | Begriffsdefinition von Vorderhosenbruch und Fadenlauf; keine skalare Berechnung |
| **Summe** | **2** | **1 unvollständige Wiederholung + 1 Definition** |
