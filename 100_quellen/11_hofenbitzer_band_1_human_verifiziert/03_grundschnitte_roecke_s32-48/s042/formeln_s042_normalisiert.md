# Fachlich normalisierte Formeln — S. 42

Quelle der Normalisierung: `formeln_s042.md`
Originaltranskript: `s042.md`
Buchseite: Hofenbitzer, Band 1, S. 42

> Walking-Skeleton-Durchgang auf Werners ausdrücklichen Wunsch. Für s042
> fehlt noch die vorab geklärte Formel-/Codeprüfung (kein Abschnitt „Vorab
> geklärte formel- und coderelevante Stellen" in `s042.md`). Alle Stellen
> unten sind deshalb `offen`, unabhängig von der fachlichen Klarheit des
> Wortlauts. Kein Status wird hier als `normalisiert` geführt.

## HOF-B1-S042-F01 — Dritteln des Rocks in sechs Bahnen

- **Fachlicher Zweck:** Lage der Öffnungslinien für die Saumerweiterung
  festlegen: VT und RT werden jeweils gedrittelt, zusammen ergeben sich sechs
  Bahnen.
- **Quelle:** `formeln_s042.md`, Abschnitt 1; `ocr_s042.md`, Zeilen 26 und 28.
- **Originalbezeichnung:** „dritteln", „6 Bahnen".
- **Normalisierte Bezeichnung:** `anzahl_bahnen_gesamt`

### Buchfassung

```text
[...] die den gesamten vorderen und den gesamten hinteren Rock jeweils
dritteln [...]. Diese Linien teilen den gesamten Rock in insgesamt 6 Bahnen.
```

### Technische Formel

```text
anzahl_bahnen_vorderteil = 3
anzahl_bahnen_rueckteil = 3
anzahl_bahnen_gesamt = anzahl_bahnen_vorderteil + anzahl_bahnen_rueckteil
                      = 6
```

### Eingaben und Einheiten

Keine Maßeingabe; reine Stückzahl (Anzahl gleich breiter Rockabschnitte je
Rockhälfte, gespiegelt an vM/hM). Einheit: dimensionslos (Anzahl).

### Ausgabe und Einheit

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `anzahl_bahnen_gesamt` | Gesamtzahl der Erweiterungs-Bahnen (VT + RT) | Anzahl |

### Bereiche, Bedingungen und Auswahlentscheidungen

Das Buch nennt als Alternative die Zehn-Bahnen-Variante (Seite 65) als
„noch harmonischer". Hier auf S. 42 wird nur die Sechs-Bahnen-Variante
beschrieben; keine Buchregel auf dieser Seite, wann welche Variante zu wählen
ist.

### Abhängigkeiten

- Kapitel „Rock-Modelle", S. 64 (Sechs-Bahnen-Rock) und S. 65
  (Zehn-Bahnen-Rock) — nur verlinkt, nicht kopiert.
- `formeln_s043.md`, Abschnitt „Berechnung des Öffnungsbetrags": dort wird
  `anzahl_bahnen_gesamt` als „Erweiterungsstellen" im Nenner verwendet
  (`Öffnungsbetrag = gewünschte Saumerweiterung : Erweiterungsstellen`,
  Beispiel `48 cm : 6 = 8 cm`). Die Identität `Erweiterungsstellen = 6 =
  anzahl_bahnen_gesamt` ist inhaltlich naheliegend, aber nicht als eine
  gemeinsame Buchvariable bestätigt.

### Status

`offen` — inhaltlich eindeutig, aber noch nicht von Werner am Original
bestätigt (Formel-/Codeprüfung für s042 steht aus).

### Offene Fragen oder Widersprüche

Keine sachliche Unklarheit im Text; offen ist ausschließlich die fehlende
Werner-Bestätigung.

## HOF-B1-S042-F02 — Vorderer Abnäher: Verschiebung zur Öffnungslinie und Mindestlänge

- **Fachlicher Zweck:** Neue Lage und Mindestlänge des vorderen
  Abnäherschenkels nach der Verschiebung zur Öffnungslinie festlegen.
- **Quelle:** `formeln_s042.md`, Abschnitt 2; `ocr_s042.md`, Zeilen 32–33.
- **Originalbezeichnung:** „Öffnungslinie ist die neue Abnahermitte",
  „mindestens 3 cm oberhalb der Huflinie".
- **Normalisierte Bezeichnung:** `abnaehermitte_vorne_neu`,
  `abnaeherschenkel_laenge_vorne_min_abstand_hueftlinie`

### Buchfassung

```text
3 Den vorderen Abnaherinhalt messen und zur Öffnungslinie hin verschiben. Die
Öffnungslinie ist die neue Abnahermitte.
4 Den Abnaherinhalt anzeichen und die Abnaherschenkel bis mindestens 3 cm
oberhalb der Huflinie zeichnen.
```

### Technische Formel

Keine Rechenoperation mit Zahlenwert für die Verschiebung selbst (reine
Lagezuweisung: `abnaehermitte_vorne_neu = position(oeffnungslinie_vorne)`).
Für die Schenkellänge nennt das Buch nur eine untere Grenze:

```text
abstand_abnaeherschenkelende_zur_hueftlinie_vorne >= 3 cm
```

### Eingaben und Einheiten

- `oeffnungslinie_vorne`: Position (aus F01 abgeleitete Konstruktionslinie).
- `abnaeherinhalt_vorne`: Winkel-/Breitenmaß des ursprünglichen vorderen
  Abnähers (Wert auf dieser Seite nicht beziffert).
- Einheit für den Grenzwert: `cm`.

### Ausgabe und Einheit

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abnaehermitte_vorne_neu` | neue Lage der Abnähermitte vorne | Position (keine Zahl) |
| `abstand_abnaeherschenkelende_zur_hueftlinie_vorne` | Mindestabstand Schenkelende zur Hüftlinie | cm |

### Bereiche, Bedingungen und Auswahlentscheidungen

Untergrenze `>= 3 cm`; keine Obergrenze im Buch genannt.

### Abhängigkeiten

`oeffnungslinie_vorne` aus F01 (Dritteln); Hüftlinie aus dem geraden
Rock-Grundschnitt (Vorseiten dieser Kategorie, hier nicht verlinkt, da keine
gemeinsame Quelle bestätigt ist).

### Status

`offen` — Grenzwert eindeutig lesbar, aber Werner-Bestätigung fehlt.

### Offene Fragen oder Widersprüche

Zahlenwert des ursprünglichen `abnaeherinhalt_vorne` auf dieser Seite nicht
angegeben (vermutlich aus dem geraden Grundschnitt übernommen); keine
Obergrenze für den Schenkelabstand genannt.

## HOF-B1-S042-F03 — Hinterer Abnäherinhalt: Addition zweier Abnäher, gleiche Länge wie vorne

- **Fachlicher Zweck:** Inhalt und Länge des neuen hinteren Abnähers nach
  Verschiebung zur Einschnittlinie festlegen.
- **Quelle:** `formeln_s042.md`, Abschnitt 3; `ocr_s042.md`, Zeile 34.
- **Originalbezeichnung:** „werden beiden Abnaherinhalte addiert", „in
  derselben Länge wie vorne".
- **Normalisierte Bezeichnung:** `abnaeherinhalt_hinten_neu`,
  `abnaeherlaenge_hinten_neu`

### Buchfassung

```text
5 Den hinteren Abnaherinhalt ebenso zur Einschnittlinie verschieben. Sind zwei
Abnaher im RT vorhanden, werden beiden Abnaherinhalte addiert. Den neuen
Abnaher in derselben Länge wie vorne einzeichnen.
```

### Technische Formel

```text
wenn anzahl_abnaeher_rueckteil_alt == 2:
    abnaeherinhalt_hinten_neu = abnaeherinhalt_hinten_1 + abnaeherinhalt_hinten_2
sonst:
    abnaeherinhalt_hinten_neu = abnaeherinhalt_hinten_1   # Buch nennt diesen Fall auf s042 nicht ausdrücklich

abnaeherlaenge_hinten_neu = abnaeherlaenge_vorne_neu
```

### Eingaben und Einheiten

- `abnaeherinhalt_hinten_1`, `abnaeherinhalt_hinten_2`: Winkel-/Breitenmaße
  der ursprünglichen hinteren Abnäher (Werte auf dieser Seite nicht
  beziffert).
- `abnaeherlaenge_vorne_neu`: Ergebnis aus F02 (auf dieser Seite ebenfalls
  ohne Zahlenwert).

### Ausgabe und Einheit

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abnaeherinhalt_hinten_neu` | neuer, addierter hinterer Abnäherinhalt | wie Eingaben (auf s042 keine Einheit beziffert) |
| `abnaeherlaenge_hinten_neu` | neue Länge des hinteren Abnähers | wie `abnaeherlaenge_vorne_neu` |

### Bereiche, Bedingungen und Auswahlentscheidungen

Addition nur ausdrücklich für den Fall „zwei Abnäher im RT vorhanden"
beschrieben. Die Seiteneinleitung (Zeile 18) bestätigt, dass der gerade
Rock-Grundschnitt ursprünglich zwei Abnäher im RT hat und beim
saumerweiterten Schnitt nur einer übrig bleibt — der Fall „nur ein
RT-Abnäher" ist auf s042 also der Zielzustand nach dieser Formel, nicht ein
alternativer Ausgangsfall.

### Abhängigkeiten

`einschnittlinie_hinten` aus F01; `abnaeherlaenge_vorne_neu` aus F02.

### Status

`offen` — Rechenregel eindeutig lesbar, aber Werner-Bestätigung fehlt und
keine Zahlenwerte auf dieser Seite vorhanden.

### Offene Fragen oder Widersprüche

Keine Zahlenwerte für `abnaeherinhalt_hinten_1/2` auf s042. Der
Sonderfall „nur ein Abnäher im RT" ist textlich nicht behandelt, siehe oben.

## HOF-B1-S042-F04 — Hinterrock-Saumöffnung um denselben Betrag wie vorne

- **Fachlicher Zweck:** Öffnungsbetrag am Saum des Hinterrocks aus dem
  Öffnungsbetrag des Vorderrocks ableiten.
- **Quelle:** `formeln_s042.md`, Abschnitt 4; `ocr_s042.md`, Zeilen 43–44.
- **Originalbezeichnung:** „Um denselben Betrag wird der Hinterrock am Saum
  geöffnet."
- **Normalisierte Bezeichnung:** `oeffnungsbetrag_hinten`

### Buchfassung

```text
7 Der vordere Abnaher wird zugelegt. Für noch mehr Saumweite kann an der
Abnaherspitze auch mehr geöffnet werden. Der Drehpunkt ZP ist jetzt an der
Taille.
8 Um denselben Betrag wird der Hinterrock am Saum geöffnet. Der Drehpunkt ZP
ist in thisem Fall die neue Abnaherspitze.
```

### Technische Formel

```text
oeffnungsbetrag_hinten = oeffnungsbetrag_vorne
```

### Eingaben und Einheiten

`oeffnungsbetrag_vorne`: Öffnungsmaß am Saum, das beim Zulegen des vorderen
Abnähers entsteht (Einheit vermutlich `cm`, auf s042 nicht beziffert).

### Ausgabe und Einheit

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `oeffnungsbetrag_hinten` | Öffnungsmaß am Saum des Hinterrocks | wie `oeffnungsbetrag_vorne` |

### Bereiche, Bedingungen und Auswahlentscheidungen

„Für noch mehr Saumweite kann an der Abnäherspitze auch mehr geöffnet
werden" — das Buch lässt eine größere Öffnung als fachliche Auswahl offen,
ohne Obergrenze zu nennen. Für diesen Spielraum bleibt unklar, ob
`oeffnungsbetrag_hinten = oeffnungsbetrag_vorne` dann noch gilt oder nur für
den Grundfall gemeint ist.

### Abhängigkeiten

Drehpunkt vorne: Taille. Drehpunkt hinten: neue Abnäherspitze aus F03.
Eingang für F05 (halber Öffnungsbetrag an der Seitennaht).

### Status

`offen` — Kernregel eindeutig, aber Werner-Bestätigung fehlt; zusätzlich
offene Frage zum Verhältnis von „mehr öffnen" (Zeile 43) zu „denselben
Betrag" (Zeile 44).

### Offene Fragen oder Widersprüche

Gilt „denselben Betrag" auch, wenn vorne mehr als der ursprüngliche
Abnäherinhalt geöffnet wird? Auf s042 nicht ausdrücklich geklärt.

## HOF-B1-S042-F05 — Seitennaht-Zugabe: halber Öffnungsbetrag

- **Fachlicher Zweck:** Zugabe an der Seitennaht aus dem Öffnungsbetrag
  ableiten, um Vorder- und Hinterrock am Saum tangential zu verbinden.
- **Quelle:** `formeln_s042.md`, Abschnitt 5; `ocr_s042.md`, Zeile 45.
- **Originalbezeichnung:** „jeweils der halbe Öffnungsbetrag".
- **Normalisierte Bezeichnung:** `seitennaht_zugabe`

### Buchfassung

```text
9 An den Seitennähten wird jeweils der halbe Öffnungsbetrag angezeichnet und
die neue Seitennaht gerade als Tangente auf den Hüftbogen gezeichnet.
```

### Technische Formel

```text
seitennaht_zugabe = oeffnungsbetrag / 2
```

### Eingaben und Einheiten

`oeffnungsbetrag`: aus F04 (`oeffnungsbetrag_vorne` = `oeffnungsbetrag_hinten`);
Einheit vermutlich `cm`, auf s042 nicht beziffert.

### Ausgabe und Einheit

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `seitennaht_zugabe` | Zugabe je Seitennaht am Saum | wie `oeffnungsbetrag` |

### Bereiche, Bedingungen und Auswahlentscheidungen

Keine zusätzliche Bedingung im Text; die Seitennaht wird danach „gerade als
Tangente auf den Hüftbogen" neu gezeichnet — eine geometrische
Konstruktionsanweisung ohne weiteren Zahlenwert.

### Abhängigkeiten

`oeffnungsbetrag` aus F04. `formeln_s043.md` beschreibt denselben
Sachverhalt bildlich als „je ein halber Keil an den beiden Seitennähten" —
inhaltlich passend, aber nicht als gemeinsame Variable bestätigt.

### Status

`offen` — Rechenregel eindeutig lesbar, aber Werner-Bestätigung fehlt.

### Offene Fragen oder Widersprüche

Keine sachliche Unklarheit im Text; offen ist ausschließlich die fehlende
Werner-Bestätigung.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidat | Ausschlussgrund |
|---|---|---|
| `formeln_s042.md`, „Nicht erfasst" | Schritt 2 „Abnäher verschieben" | reine Abschnittsüberschrift ohne Rechen-/Auswahlbeziehung |
| `formeln_s042.md`, „Nicht erfasst" | Schritt 6 „Vorder- und Hinterrock werden getrennt" | Konstruktionsschritt ohne Zahl oder Bereich |
| `formeln_s042.md`, „Nicht erfasst" | Schritt 10 „Abnäher immer noch groß genug" | qualitative Aussage ohne Zahlen-/Auswahlbeziehung |
| `formeln_s042.md`, „Nicht erfasst" | Kennzeichnungen `①②③④⑤⑥`, `AbI me`, `üb` | unsichere/rein referenzierende Zeichnungslabels |
| **Summe** | **4 Kategorien** | **kein eigenständiger Formel-/Code-Bereich** |

## Prüfhinweis

Alle fünf Stellen sind inhaltlich klar lesbar, aber keine ist in `s042.md`
als von Werner am Original bestätigt dokumentiert (Abschnitt „Vorab geklärte
formel- und coderelevante Stellen" fehlt). Diese Normalisierung ist ein
Walking-Skeleton-Durchgang: sie zeigt die spätere Vertragsform, ersetzt aber
nicht die fachliche Bestätigung. Vor einem Codevertrag muss Werner
mindestens F01–F05 am Original bestätigen; zusätzlich offen: die Zahlenwerte
zu `abnaeherinhalt_vorne`/`abnaeherinhalt_hinten_1/2` und die Frage zu F04
(„mehr öffnen" vs. „denselben Betrag").
