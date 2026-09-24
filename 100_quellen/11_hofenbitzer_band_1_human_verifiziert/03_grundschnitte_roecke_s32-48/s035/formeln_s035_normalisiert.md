# Fachlich normalisierte Formeln — S. 35

Quelle der Normalisierung: `formeln_s035.md`
Originaltranskript: `s035.md`
Buchseite: Hofenbitzer, Band 1, S. 35

Nur F3 (Abnähermitte 1. h. Abnäher) ist von Werner am Original bestätigt. Alle
übrigen Stellen stammen aus der OCR-Rohfassung bzw. der erkannten Tabelle und
sind noch nicht bestätigt; sie erhalten Status `offen`, auch wenn eine
technische Formel bereits sauber formulierbar wäre.

## HOF-B1-S035-F01 — Schwellenregel zweiter hinterer Abnäher

- **Quelle:** `formeln_s035.md`, Abschnitt F1; ocr_s035.md Z.7. Wiederholt die
  in `formeln_s034.md`, F6 angekündigte Regel („siehe folgende Seite").
- **Normalisierte Bezeichnung:** `braucht_zweiten_hinteren_abnaeher`

### Buchfassung

```text
Da hier der Betrag für den hinteren Abnäher mehr als 4,5 cm beträgt, muss der
Betrag auf zwei Abnäher im Rückteil aufgeteilt werden.
```

### Technische Formel

```text
braucht_zweiten_hinteren_abnaeher = (abnaeherinhalt_hinten_gesamt > 4.5 cm)
```

### Eingaben und Einheiten

| Variable | Bedeutung | Einheit |
|---|---|---|
| `abnaeherinhalt_hinten_gesamt` | Gesamtinhalt des hinteren Abnähers vor Aufteilung | cm |

### Ausgabe und Einheit

| Variable | Bedeutung | Einheit |
|---|---|---|
| `braucht_zweiten_hinteren_abnaeher` | Auswahlentscheidung: ein oder zwei hintere Abnäher | boolesch |

### Bereiche, Bedingungen und Auswahlentscheidungen

Schwelle `4,5 cm`, gedruckt als „mehr als" (echte Ungleichung, nicht „ab").

### Abhängigkeiten

Gehört fachlich zu `formeln_s034.md`, F6 (dieselbe Regel, dort als
Vorankündigung). Besitzerformel ist bislang keine der beiden Seiten
eindeutig zugeordnet; bis zur Klärung hier als eigener Eintrag geführt.

### Status

`offen` — inhaltlich nicht bestätigt; außerdem Verhältnis zu `formeln_s034.md`
F6 (Duplikat oder Fortsetzung) ungeklärt.

### Offene Fragen oder Widersprüche

Ob `formeln_s034.md` F6 und dieser Eintrag eine einzige Buchregel oder zwei
getrennte Formulierungen derselben Regel sind, ist nicht entschieden.

## HOF-B1-S035-F02 — Inhalt des 2. hinteren Abnähers relativ zum 1. hinteren Abnäher

- **Quelle:** `formeln_s035.md`, Abschnitt F2; ocr_s035.md Z.9.
- **Normalisierte Bezeichnung:** `abnaeherinhalt_2h`

### Buchfassung

```text
Der Inhalt des 2. h. Abnähers sollte ca. 0,5 bis 1 cm geringer sein als der
Inhalt des (hinteren) 1. RT-Abnähers.
```

### Technische Formel

```text
abnaeherinhalt_2h = abnaeherinhalt_1h − delta, delta ∈ [0.5, 1] cm (ca.)
```

### Eingaben und Einheiten

| Variable | Bedeutung | Einheit |
|---|---|---|
| `abnaeherinhalt_1h` | Inhalt des 1. hinteren Abnähers | cm |
| `delta` | Differenzbetrag, fachlich zu wählen | cm |

### Ausgabe und Einheit

| Variable | Bedeutung | Einheit |
|---|---|---|
| `abnaeherinhalt_2h` | Inhalt des 2. hinteren Abnähers | cm |

### Bereiche, Bedingungen und Auswahlentscheidungen

`delta` liegt im Bereich `0,5 bis 1 cm`, als `ca.` gedruckt. Keine Buchregel,
die innerhalb dieses Bereichs einen festen Wert wählt.

### Abhängigkeiten

Setzt `abnaeherinhalt_1h` voraus (Tabelle, vgl. HOF-B1-S035-F05).

### Status

`offen` — inhaltlich nicht bestätigt.

### Offene Fragen oder Widersprüche

Keine.

## HOF-B1-S035-F03 — Abnähermitte des 1. hinteren Abnähers (bestätigt)

- **Quelle:** `formeln_s035.md`, Abschnitt F3; ocr_s035.md Z.10. Bestätigt in
  `s035.md`, Abschnitt „Vorab geklärte formel- und coderelevante Stellen".
- **Normalisierte Bezeichnung:** `position_abnaehermitte_1h`

### Buchfassung

```text
Die Abnähermitte des 1. h. Abnähers liegt bei ca. ⅓ der Hüftlinie + 0 bis 1 cm
von der hM nach links abgetragen.
```

### Technische Formel

```text
position_abnaehermitte_1h = (huefflinie / 3) + zuschlag, zuschlag ∈ [0, 1] cm (ca.)
```

Abgetragen von hM (hintere Mitte) nach links.

### Eingaben und Einheiten

| Variable | Bedeutung | Einheit |
|---|---|---|
| `huefflinie` | Länge der Hüftlinie (Bezugsgröße) | cm |
| `zuschlag` | zusätzlicher Betrag, fachlich zu wählen | cm |

### Ausgabe und Einheit

| Variable | Bedeutung | Einheit |
|---|---|---|
| `position_abnaehermitte_1h` | Abstand der Abnähermitte von hM, nach links abgetragen | cm |

### Bereiche, Bedingungen und Auswahlentscheidungen

`⅓ der Hüftlinie` ist als `ca.` gedruckt (kein exakter Drittelwert
vorgeschrieben). `zuschlag` liegt im Bereich `0 bis 1 cm`; keine Buchregel
zur Auswahl eines festen Werts innerhalb des Bereichs.

### Abhängigkeiten

Setzt die Hüftlinie als Bezugsgröße voraus (Quelle auf dieser Seite nicht
definiert; vermutlich Grundschnittgröße aus einer früheren Seite dieser
Kategorie — nicht verlinkt, da keine gemeinsame Quelle bestätigt ist).

### Status

`normalisiert`

### Offene Fragen oder Widersprüche

Keine.

## HOF-B1-S035-F04 — Erhöhung der Taillenlinie und Abnähermitte des 2. hinteren Abnähers

- **Quelle:** `formeln_s035.md`, Abschnitt F4; ocr_s035.md Z.11.
- **Normalisierte Bezeichnung:** `position_abnaehermitte_2h`

### Buchfassung

```text
Die Erhöhung der Taillenlinie für den 2. h. Abnäher erfolgt wie für den
vorderen Abnäher. Die Abnähermitte liegt in der Mitte zwischen Hüftbogen und
Abnäherschenkel des 1. h. Abnähers.
```

### Technische Formel

```text
erhoehung_taillenlinie_2h = erhoehung_taillenlinie_vorderer_abnaeher   [Bezugsregel ungeklärt]
position_abnaehermitte_2h = mitte(huefftbogen_position, abnaeherschenkel_1h_position)
```

### Eingaben und Einheiten

| Variable | Bedeutung | Einheit |
|---|---|---|
| `erhoehung_taillenlinie_vorderer_abnaeher` | Erhöhungsregel des vorderen Abnähers (Quellformel nicht bestätigt) | cm |
| `huefftbogen_position` | Position des Hüftbogens | cm/Punkt |
| `abnaeherschenkel_1h_position` | Position des Abnäherschenkels des 1. h. Abnähers | cm/Punkt |

### Ausgabe und Einheit

| Variable | Bedeutung | Einheit |
|---|---|---|
| `erhoehung_taillenlinie_2h` | Taillenlinienerhöhung für den 2. hinteren Abnäher | cm |
| `position_abnaehermitte_2h` | Abnähermitte des 2. hinteren Abnähers | cm/Punkt |

### Bereiche, Bedingungen und Auswahlentscheidungen

Keine gedruckten Zahlenwerte auf dieser Seite; beide Teilregeln verweisen auf
andere Konstruktionsschritte.

### Abhängigkeiten

`erhoehung_taillenlinie_vorderer_abnaeher` verweist vermutlich auf eine
Formel wie `formeln_s034.md`, F3, aber die Übereinstimmung ist nicht
bestätigt und wird hier nicht angenommen. `huefftbogen_position` und
`abnaeherschenkel_1h_position` setzen vorherige Konstruktionsschritte voraus,
die auf s035 nicht dokumentiert sind.

### Status

`offen` — Quellformel für die Erhöhungsregel nicht identifiziert; inhaltlich
nicht bestätigt.

### Offene Fragen oder Widersprüche

Welche Formel „wie für den vorderen Abnäher" konkret meint, ist ungeklärt.

## HOF-B1-S035-F05 — Tabelle Hüftabstich und Abnäherinhalte

- **Quelle:** `formeln_s035.md`, Abschnitt F5; tabellen_s035.md Z.5-10. Gleiche
  Formelstruktur wie `formeln_s034.md`, F5 (dort bereits normalisiert unter
  einem eigenen Eintrag dieser Kategorie).
- **Normalisierte Bezeichnung:** `hueftabstich`, `abnaeherinhalt_vorne`,
  `abnaeherinhalt_1h`, `abnaeherinhalt_2h`

### Buchfassung

```text
Hüftabstich:      ½ TaAf ± 1        Beispiel: 6
v. Abnäher:        0 oder 1,5 bis 2,5   Beispiel: 1,5
1.h. Abnäher:      bis 4,5          Beispiel: 3
2.h. Abnäher:      optional         Beispiel: 2,5
Kontrolle:         Σ = TaAf         Beispiel: 13
```

### Technische Formel

```text
hueftabstich = (taillenausfall / 2) ± 1 cm
abnaeherinhalt_vorne ∈ {0} ∪ [1.5, 2.5] cm
abnaeherinhalt_1h ≤ 4.5 cm
abnaeherinhalt_2h: optional
Kontrolle: abnaeherinhalt_vorne + abnaeherinhalt_1h + abnaeherinhalt_2h = taillenausfall   [unbestätigt, siehe Widerspruch]
```

### Eingaben und Einheiten

| Variable | Bedeutung | Einheit |
|---|---|---|
| `taillenausfall` (TaAf) | Taillenausfall (Bezugsgröße) | cm |

### Ausgabe und Einheit

| Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftabstich` | Hüftabstich | cm |
| `abnaeherinhalt_vorne` | Inhalt des vorderen Abnähers | cm |
| `abnaeherinhalt_1h` | Inhalt des 1. hinteren Abnähers | cm |
| `abnaeherinhalt_2h` | Inhalt des 2. hinteren Abnähers | cm |

### Bereiche, Bedingungen und Auswahlentscheidungen

`hueftabstich` als Bereich `± 1 cm` um `½ TaAf`. `abnaeherinhalt_vorne`
entweder `0` oder Bereich `1,5 bis 2,5 cm`. `abnaeherinhalt_1h` bis `4,5 cm`
(vgl. HOF-B1-S035-F01 zur Schwelle). `abnaeherinhalt_2h` optional, kein
gedruckter Bereich. Keine Buchregel, die innerhalb der Bereiche einen festen
Wert wählt.

### Abhängigkeiten

Gleiche Formelstruktur wie `formeln_s034.md`, F5. `abnaeherinhalt_1h` hängt
mit HOF-B1-S035-F01 zusammen, `abnaeherinhalt_2h` mit HOF-B1-S035-F02.

### Status

`offen` — Tabelle inhaltlich nicht bestätigt; zusätzlich rechnerischer
Widerspruch im gedruckten Zahlenbeispiel (siehe unten).

### Offene Fragen oder Widersprüche

Das gedruckte Zahlenbeispiel (Hüftabstich 6; Abnäherinhalte 1,5 / 3 / 2,5;
Kontrolle 13) erfüllt weder `abnaeherinhalt_vorne + abnaeherinhalt_1h +
abnaeherinhalt_2h = hueftabstich` (1,5+3+2,5=7≠6) noch die auf `formeln_s034.md`
belegte Kontrollbeziehung `2 × hueftabstich = taillenausfall` (2×6=12≠13).
Nicht als Beweis für eine andere Buchformel verwendet; fototreu unverändert
dokumentiert.

## Bestätigte Zeichnungsbereiche ohne zugeordnete Formel

- **Quelle:** `formeln_s035.md`, Abschnitt „Bestätigte Zeichnungsbereiche ohne
  zugeordnete Formel"; bestätigt in `s035.md`, Abschnitt „Vorab geklärte
  formel- und coderelevante Stellen".

### Buchfassung

```text
8 bis 10 cm
12 bis 14 cm
13 bis 16 cm
```

### Technische Formel

Keine. Ohne erkennbare Zuordnung zu einer Variablen oder einem
Konstruktionsschritt auf dieser Seite lässt sich kein technischer Bereich
benennen.

### Eingaben und Einheiten, Ausgabe und Einheit

Nicht ermittelbar ohne Zuordnung.

### Bereiche, Bedingungen und Auswahlentscheidungen

`8 bis 10 cm` und `13 bis 16 cm` sind zahlengleich mit den bestätigten
Abnäherlängen vorne/hinten aus `formeln_s034.md`, F10 und F12 — dort bereits
mit Status geführt. Eine Identität wird hier nicht angenommen. `12 bis 14 cm`
hat keine erkennbare Entsprechung auf s034.

### Abhängigkeiten

Möglich, aber nicht bestätigt: `formeln_s034.md`, F10 (`8 bis 10 cm`) und F12
(`13 bis 16 cm`).

### Status

`gesperrt` — Zuordnung zu einer Variablen fehlt vollständig; vor jeder
Normalisierung muss Werner am Original klären, welche Strecke die drei
Bereiche jeweils bezeichnen.

### Offene Fragen oder Widersprüche

Welchem Konstruktionsschritt auf s035 die drei Bereiche zugeordnet sind, ist
ungeklärt. Mögliche Dopplung mit `formeln_s034.md` F10/F12 ungeklärt.

## Nicht normalisiert (fototreu erfasst, keine eigenständige Formel)

- HOF-B1-S035-F06 (Seitennaht-/Abnäherspitzenverschiebung, `formeln_s035.md`
  F6): reine Verschiebungsangaben ohne Eingabe-Ausgabe-Struktur; für einen
  späteren Codevertrag als optionale Gestaltungsregel relevant, hier noch
  nicht normalisiert.
- HOF-B1-S035-F07 (Schenkellängenregel nach Verschiebung, `formeln_s035.md`
  F7): Konsistenzregel ohne Zahlenwert; für einen späteren Codevertrag als
  Nebenbedingung zu HOF-B1-S035-F06 relevant, hier noch nicht normalisiert.

## Prüfhinweis

Von sieben fototreu erfassten Stellen ist nur eine (F3) am Original
bestätigt und wird hier als `normalisiert` geführt. Alle übrigen Stellen
bleiben `offen` oder `gesperrt`, bis Werner sie am Original bestätigt oder
ausdrücklich ausschließt. Für einen späteren Codevertrag reicht aktuell nur
HOF-B1-S035-F03.
