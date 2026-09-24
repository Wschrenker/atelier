# Normalisierte Formeln – s063

Technische Fassung zu [formeln_s063.md](formeln_s063.md). Alle Stellen sind
laut [s063.md](s063.md) OCR-Rohfassung, noch nicht menschlich verifiziert.
Diese Normalisierung entstand als Walking Skeleton auf ausdrücklichen Wunsch
(Werner: „überspringe die Blocker"); kein Status hier gilt als bestätigt.

## 1. Nahtabstand am hinteren Miederbeleg (RV-Ansatz)

**Quelle:** [formeln_s063.md](formeln_s063.md), Abschnitt 1.

**Buchfassung:**

```text
Am vorbereiteten hinteren Miederbeleg wird an der hM, dort wo der
Reißverschluss eingearbeitet wird, ca. 0,5 bis 1 cm entfernt, um den Beleg
auf das Reißverschlussband anzunähen.
```

**Technische Formel:**

```text
Nahtabstand_hM = Bereich(0,5 cm, 1 cm)
```

**Eingaben und Einheiten:** hM (hintere Mitte, Referenzlinie am Miederbeleg),
Einheit cm.
**Ausgabe und Einheit:** Abstand der neuen Naht von hM, in cm.
**Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich 0,5–1 cm; gilt
nur an der Stelle, an der der Reißverschluss eingearbeitet wird. Kein fester
Wert im Buch gewählt.
**Abhängigkeiten:** Vorbereitung des hinteren Miederbelegs auf „vorhergehenden
Seiten" (im Buch nicht namentlich benannt, nicht nachverfolgt).
**Status:** offen — Seite nicht menschlich verifiziert; zusätzlich Bereich
ohne gewählten Wert.
**Offene Fragen:** Welche Seite genau mit „vorhergehende Seiten" gemeint ist,
bleibt offen.

## 2. Rockfutter – Saumkürzung und Einschlag

**Quelle:** [formeln_s063.md](formeln_s063.md), Abschnitt 2.

**Buchfassung:**

```text
Für das Futter werden am Saum 2 cm gekürzt und mit 2 x 2 cm Einschlägen
versehen.
```

**Technische Formel:**

```text
Futter_Saumkürzung = 2 cm
Futter_Einschlag = 2 x 2 cm
```

**Eingaben und Einheiten:** Ausgangssaumlänge des Futters (im Buchtext nicht
beziffert), Einheit cm.
**Ausgabe und Einheit:** Gekürzte Saumlänge des Futters bzw. Einschlagmaß, in
cm.
**Bereiche, Bedingungen und Auswahlentscheidungen:** feste Werte, keine
Bereiche.
**Abhängigkeiten:** keine im Buchtext genannten.
**Status:** offen — Seite nicht menschlich verifiziert; zusätzlich ist
unklar, gegenüber welcher Bezugslänge die 2 cm gekürzt werden.
**Offene Fragen oder Widersprüche:** Bezugsgröße der Kürzung (z. B.
Oberstoffsaum) wird im Buchtext auf dieser Seite nicht genannt; nicht
ergänzt.

## 3. Rockfutter – Naht und Schlitzende am RV-Schlitz

**Quelle:** [formeln_s063.md](formeln_s063.md), Abschnitt 3.

**Buchfassung:**

```text
Am RV-Schlitz die Naht um ca. 0,5 cm nach innen verschieben und das
Schlitzende um ca. 2 bis 3 cm verlängern (Seite 92).
```

**Technische Formel:**

```text
Naht_Verschiebung_innen ≈ 0,5 cm
Schlitzende_Verlaengerung = Bereich(2 cm, 3 cm)
```

**Eingaben und Einheiten:** ursprüngliche Nahtlinie und Schlitzende am
Rockfutter, Einheit cm.
**Ausgabe und Einheit:** neue Nahtlinie (nach innen verschoben) und neue
Schlitzendlänge, in cm.
**Bereiche, Bedingungen und Auswahlentscheidungen:** Verschiebung ca. 0,5 cm
(Näherungswert, kein Bereich angegeben); Verlängerung als Bereich 2–3 cm ohne
gewählten Wert.
**Abhängigkeiten:** Buchtext verweist ausdrücklich auf Seite 92 (nicht
verifiziert, nur verlinkt).
**Status:** offen — Seite nicht menschlich verifiziert; zusätzlich Bereich
ohne gewählten Wert und ungeprüfter Seitenverweis.
**Offene Fragen:** Inhalt und Übereinstimmung mit Seite 92 nicht geprüft.

## 4. Miederbeleg – Naht am Reißverschlussschlitz (Verweis ohne eigenen Wert)

**Quelle:** [formeln_s063.md](formeln_s063.md), Abschnitt 4.

**Buchfassung:**

```text
Wie am Miederbeleg wird am Reißverschlussschlitz die Naht nach innen
verschoben (siehe auch Seiten 59 + 61).
```

**Technische Formel:**

```text
Naht_Verschiebung_innen(Miederbeleg) = siehe Seiten 59 + 61
```

**Eingaben und Einheiten:** keine auf dieser Seite bezifferten Eingaben.
**Ausgabe und Einheit:** keine auf dieser Seite bezifferte Ausgabe.
**Bereiche, Bedingungen und Auswahlentscheidungen:** keine auf dieser Seite;
gleiche Operation wie Abschnitt 3, aber eigener Anwendungsort (Miederbeleg
statt Rockfutter).
**Abhängigkeiten:** Wert ausdrücklich auf den Seiten 59 und 61 verortet; hier
nicht kopiert.
**Status:** gesperrt — kein eigener Zahlenwert auf dieser Seite, Wert hängt
von unverifizierten Fremdseiten ab.
**Offene Fragen:** Ob der Wert von Seite 59/61 mit Abschnitt 3 dieser Seite
(0,5 cm) übereinstimmt, ist ungeprüft.
