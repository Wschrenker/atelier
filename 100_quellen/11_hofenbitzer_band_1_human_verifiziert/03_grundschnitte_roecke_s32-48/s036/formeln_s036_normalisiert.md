# Fachlich normalisierte Formeln — S. 36

Quelle der Normalisierung: `formeln_s036.md`
Originaltranskript: `s036.md`
Buchseite: Hofenbitzer, Band 1, S. 36

Alle drei Stellen sind zeichnungsgebundene Bereichsangaben ohne begleitende
Rechenoperation. Es gibt keine Formel im engeren Sinn, sondern je einen
zulässigen Bereich für eine Nahtzugabe-Breite an einer bestimmten Schnittkante.

## HOF-B1-S036-F01 — Nahtzugabe-Breite Seitennaht (SN)

- **Fachlicher Zweck:** Zulässigen Bereich der Nahtzugabe-Breite an der
  Seitennaht (SN) von Vorderteil und Rückteil benennen.
- **Quelle:** `formeln_s036.md`, Abschnitt „Zeichnung img-2.jpeg" und „Zeichnung
  img-3.jpeg"; Zeichnungsbeschriftung auf `skizzen/s036_skizze_03.png` und
  `skizzen/s036_skizze_04.png`; Bestätigung in `s036.md`, Zeilen 19–24.
- **Originalbezeichnung:** `1–3`, auf der VT-Zeichnung zusätzlich mit „NZg-Breite"
  bezeichnet.
- **Normalisierte Bezeichnung:** `nahtzugabe_breite_seitennaht`

### Buchfassung

```text
1–3
```

### Technische Formel

Keine Rechenbeziehung. `1–3` benennt einen zulässigen Wertebereich; das Buch
wählt keinen festen Wert oder Default.

```text
nahtzugabe_breite_seitennaht ist ein Wert im Bereich [1, 3]
```

### Eingaben und Einheiten

Keine Eingabegröße; der Bereich selbst ist die gedruckte Angabe. Keine Einheit
an der Zahl gedruckt (bestätigt in `s036.md`, Zeilen 22–23: keine Einheit wird
ergänzt).

### Ausgabe und Einheit

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `nahtzugabe_breite_seitennaht` | zulässiger Bereich der Nahtzugabe-Breite an SN | im Buch nicht angegeben |

### Bereiche, Bedingungen und Auswahlentscheidungen

Bereich `1` bis `3`. Keine Buchregel, nach der innerhalb dieses Bereichs ein
konkreter Wert gewählt wird.

### Abhängigkeiten

Gilt für die Seitennaht (SN) an Vorderteil und Rückteil des geraden
Rock-Produktionsschnitts (S. 36); vergleichbar mit den Grundschnitt-Nahtlinien
auf früheren Seiten dieser Kategorie, aber hier nicht verlinkt, da keine
gemeinsame Quelle bestätigt ist.

### Status

`offen` — Bereich ohne gedruckte Einheit und ohne Auswahlregel; für einen
späteren Codevertrag müssen Einheit und Auswahlkriterium fachlich bestätigt
werden.

### Offene Fragen oder Widersprüche

Keine Einheit gedruckt. Keine Regel, nach der innerhalb von `1–3` ein
konkreter Wert gewählt wird.

## HOF-B1-S036-F02 — Nahtzugabe-Breite hintere Mitte (hM)

- **Fachlicher Zweck:** Zulässigen Bereich der Nahtzugabe-Breite an der
  hinteren Mitte (hM) des Rückteils benennen.
- **Quelle:** `formeln_s036.md`, Abschnitt „Zeichnung img-3.jpeg";
  Zeichnungsbeschriftung auf `skizzen/s036_skizze_04.png`; Bestätigung in
  `s036.md`, Zeilen 19–24.
- **Originalbezeichnung:** `1–2`.
- **Normalisierte Bezeichnung:** `nahtzugabe_breite_hintere_mitte`

### Buchfassung

```text
1–2
```

### Technische Formel

Keine Rechenbeziehung. `1–2` benennt einen zulässigen Wertebereich.

```text
nahtzugabe_breite_hintere_mitte ist ein Wert im Bereich [1, 2]
```

### Eingaben und Einheiten

Keine Eingabegröße. Keine Einheit an der Zahl gedruckt (bestätigt in
`s036.md`, Zeilen 22–23: keine Einheit wird ergänzt).

### Ausgabe und Einheit

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `nahtzugabe_breite_hintere_mitte` | zulässiger Bereich der Nahtzugabe-Breite an hM | im Buch nicht angegeben |

### Bereiche, Bedingungen und Auswahlentscheidungen

Bereich `1` bis `2`. Keine Buchregel zur Auswahl eines konkreten Werts.

### Abhängigkeiten

Gilt für die Kante hM ausschließlich am Rückteil des geraden
Rock-Produktionsschnitts (S. 36). Die entsprechende Kante am Vorderteil (vM)
trägt stattdessen die Beschriftung „vM-Bruchlinie, Symmetrielinie" ohne eigene
Nahtzugabe-Angabe, da das Vorderteil dort im Bruch zugeschnitten wird.

### Status

`offen` — Bereich ohne gedruckte Einheit und ohne Auswahlregel.

### Offene Fragen oder Widersprüche

Keine Einheit gedruckt. Keine Regel, nach der innerhalb von `1–2` ein
konkreter Wert gewählt wird.

## HOF-B1-S036-F03 — Nahtzugabe-Breite Saum (Saumeinschlag)

- **Fachlicher Zweck:** Zulässigen Bereich des Saumeinschlags am unteren Rand
  von Vorderteil und Rückteil benennen.
- **Quelle:** `formeln_s036.md`, Abschnitt „Zeichnung img-2.jpeg" und
  „Zeichnung img-3.jpeg"; Zeichnungsbeschriftung auf
  `skizzen/s036_skizze_03.png` (dort zusätzlich mit „Saumeinschlag SaEs"
  bezeichnet) und `skizzen/s036_skizze_04.png`; Bestätigung in `s036.md`,
  Zeilen 19–24.
- **Originalbezeichnung:** `2 bis 5`.
- **Normalisierte Bezeichnung:** `saumeinschlag_breite`

### Buchfassung

```text
2 bis 5
```

### Technische Formel

Keine Rechenbeziehung. `2 bis 5` benennt einen zulässigen Wertebereich.

```text
saumeinschlag_breite ist ein Wert im Bereich [2, 5]
```

### Eingaben und Einheiten

Keine Eingabegröße. Keine Einheit an der Zahl gedruckt (bestätigt in
`s036.md`, Zeilen 22–23: keine Einheit wird ergänzt).

### Ausgabe und Einheit

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `saumeinschlag_breite` | zulässiger Bereich des Saumeinschlags | im Buch nicht angegeben |

### Bereiche, Bedingungen und Auswahlentscheidungen

Bereich `2` bis `5`, im Buch mit dem Wort „bis" statt Bindestrich gedruckt
(fototreu erhalten, siehe `formeln_s036.md`). Keine Buchregel zur Auswahl
eines konkreten Werts.

### Abhängigkeiten

Gilt für den Saum (unteren Rand) an Vorderteil und Rückteil des geraden
Rock-Produktionsschnitts (S. 36).

### Status

`offen` — Bereich ohne gedruckte Einheit und ohne Auswahlregel.

### Offene Fragen oder Widersprüche

Keine Einheit gedruckt. Keine Regel, nach der innerhalb von `2 bis 5` ein
konkreter Wert gewählt wird.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidat | Ausschlussgrund |
|---|---|---|
| `formeln_s036.md`, Abschnitt „Nicht erfasst" | `2 cm` | isoliertes Maß ohne erkennbare Rechen- oder Auswahlbeziehung |
| `formeln_s036.md`, Abschnitt „Nicht erfasst" | `1×` | reines Produktionskennzeichen (Zuschnittanzahl) |
| `formeln_s036.md`, Abschnitt „Nicht erfasst" | `2×-p` | reines Produktionskennzeichen (Zuschnittanzahl, gespiegelt) |
| **Summe** | **3** | **1 isoliertes Maß und 2 Produktionskennzeichen ausgeschlossen** |

## Prüfhinweis

Die Seite enthält keinen Fließtext- oder Tabellenbeleg für die drei Bereiche;
sie sind ausschließlich als Zeichnungsbeschriftung sichtbar und wurden bereits
vor dieser Normalisierung von Werner am Original bestätigt (`s036.md`, Zeilen
19–24). Ohne gedruckte Einheit und ohne Auswahlregel bleiben alle drei Stellen
`offen`; ein Codevertrag ist erst nach fachlicher Klärung von Einheit und
Auswahlkriterium möglich.
