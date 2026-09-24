# Formeln s096 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie [`formeln_s096.md`](formeln_s096.md) beruht auch diese
Normalisierung ausschließlich auf der OCR-Rohfassung. Kein Punkt ist von
Werner am Original bestätigt. Auf ausdrücklichen Wunsch Werners als
Walking-Skeleton-Durchlauf erstellt (Blocker übersprungen). Kein Status hier
darf als „normalisiert und bestätigt" gelesen werden — beide Formeln bleiben
`offen`.

## Formel 1 – Futter-Rockteil: Saumkürzung

**Quelle:** [formeln_s096.md](formeln_s096.md), Abschnitt 1.

**Buchfassung:**

```text
Den Futtersaum um 2 cm kürzen.
```

**Technische Formel:**

```text
saum_neu_cm = saum_alt_cm - 2
```

**Eingaben und Einheiten:**

- `saum_alt_cm` — Ausgangssaumlänge des Futter-Rockteils, Einheit cm. Auf
  dieser Seite nicht angegeben (kein Wert im Buchtext genannt).
- Kürzungsbetrag: `2 cm` (fest, aus der Buchfassung).

**Ausgabe und Einheit:**

- `saum_neu_cm` — neue Saumlänge des Futter-Rockteils nach Kürzung, Einheit cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:**

- Fester Wert `2 cm`, keine Bereichsangabe, kein „ca." im Buchtext.
- Gilt laut Buchfassung für das Futter-Rockteil dieses Modells (Rockfutter für
  engen Rock mit verdecktem Schlitz).

**Abhängigkeiten:**

- Formal ähnlich zu [`formeln_s059_normalisiert.md`](../s059/formeln_s059_normalisiert.md)
  Formel 2 „Futter-Rockteile – Saumkürzung" (dort ebenfalls 2 cm), aber
  eigenständige Buchstelle auf einer anderen Seite. Nicht gegenseitig als
  Beleg verwenden.
- Bezug zur Ausgangs-Rockteil-Kontur, die laut Buchtext auf Seite 52
  beschrieben ist (Weitenreduzierung der oberen Rockkante); auf s096 selbst
  nicht mit Zahlen belegt.

**Status:** offen

**Offene Fragen oder Widersprüche:**

- Unklar, welcher der fünf Schrittkennungen `①`–`⑤` dieser Satz zuzuordnen
  ist (bekannte OCR-Lücke, siehe `s096.md`).
- Ausgangssaumlänge (`saum_alt_cm`) ist auf dieser Seite nicht angegeben;
  ohne diesen Wert ist die Formel nicht auswertbar.
- Kein Punkt am Original bestätigt.

## Formel 2 – Futteransatznaht: Verschiebung am RV-Schlitz

**Quelle:** [formeln_s096.md](formeln_s096.md), Abschnitt 2.

**Buchfassung:**

```text
An der SN vom Futter verschiebt man die Futteransatznaht am RV-Schlitz um ca.
0,5 cm nach Innen, weil das Futter neben den an der hM befindlichen Zähnchen
auf das RV-Band genäht wird (siehe Seite 59).
```

**Technische Formel:**

```text
position_futteransatznaht_neu = position_SN - verschiebung_cm
  (Richtung: nach Innen, d. h. weg von der Zähnchenreihe des RV-Bands)
```

**Eingaben und Einheiten:**

- `position_SN` — Ausgangsposition der Seitennaht (SN) am RV-Schlitz des
  Futters. Auf dieser Seite nicht mit Zahl belegt.
- `verschiebung_cm ≈ 0,5` — Näherungswert laut Buchfassung („ca.").

**Ausgabe und Einheit:**

- `position_futteransatznaht_neu` — Lage der Futteransatznaht relativ zur SN
  am RV-Schlitz, Einheit cm (Verschiebungsbetrag).

**Bereiche, Bedingungen und Auswahlentscheidungen:**

- „ca." bleibt erhalten: kein fester Wert, sondern ein Näherungsbereich um
  0,5 cm.
- Begründung im Buchtext (Zähnchen des RV-Bands an der hM) ist eine
  fachliche Bedingung, keine eigene Zahl.

**Abhängigkeiten:**

- Buchtext verweist selbst auf Seite 59. Dort [`formeln_s059.md`](../s059/formeln_s059.md)
  Abschnitt 3 „Linke Seitennaht – RV-Schlitz-Verschiebung" nennt ebenfalls
  „ca. 0,5 cm nach innen", jedoch an der linken Seitennaht des Rocks (nicht
  der SN vom Futter). Beide Stellen bleiben getrennt dokumentiert und werden
  nicht gegenseitig als Beleg verwendet, da unklar ist, ob es sich um
  dieselbe Maßangabe oder zwei unabhängige Buchregeln handelt.

**Status:** offen

**Offene Fragen oder Widersprüche:**

- Verhältnis zur strukturell ähnlichen Stelle auf s059 (Abschnitt 3) ungeklärt:
  gleiche Regel an zwei Modellen oder Zufall gleicher Rundungswert?
- Schrittkennung „7"/„⑦" am Original nicht bestätigt (bekannte OCR-Lücke,
  siehe `s096.md`).
- Ausgangsposition der SN nicht quantifiziert.
- Kein Punkt am Original bestätigt.
