# Formeln s048 – normalisiert (Walking Skeleton)

**Hinweis:** Seite s048 ist noch nicht von Werner am Original bestätigt
(`s048.md` steht auf „OCR-Rohfassung – noch nicht menschlich verifiziert").
Diese Normalisierung dient ausdrücklich als Verfahrens-Durchstich (walking
skeleton) durch Extraktion → Normalisierung, nicht als Freigabe. Alle
Formeln erhalten deshalb vorerst den Status `gesperrt`, unabhängig davon, ob
die Buchformel selbst inhaltlich klar ist. Erst nach Werners Bestätigung der
Textstellen kann der Status auf `normalisiert`/`offen` wechseln.

## 1. Hüftweitenzugabe bei mäßiger Kräuselweite

**Quelle:** [formeln_s048.md](formeln_s048.md), Abschnitt „Hüftweitenzugabe bei
mäßiger Kräuselweite".

**Buchfassung:**

```text
Für den Rock mit mäßiger Kräuselweite werden ab ca. 5 cm am halben Rock, also insgesamt 10 cm Hüftweite hinzu gegeben.
```

**Technische Formel:**

```text
Hüftweitenzugabe_gesamt = 2 · Hüftweitenzugabe_halb
```

**Eingaben und Einheiten:**

- `Hüftweitenzugabe_halb`: Zugabe am halben Rock, ca. 5 cm (cm), Richtwert
  („ab ca.").

**Ausgabe und Einheit:**

- `Hüftweitenzugabe_gesamt`: Zugabe am ganzen Rock, ca. 10 cm (cm).

**Bereiche, Bedingungen und Auswahlentscheidungen:**

- „ab ca. 5 cm" ist ein Richtwert, kein fester Wert; die Buchfassung nennt
  keine Obergrenze oder Schrittweite.
- Gilt für „mäßige Kräuselweite"; keine im Buchtext definierte Abgrenzung,
  ab wann Kräuselweite nicht mehr „mäßig" ist.

**Abhängigkeiten:** Grenzfall zu Formel 5 (Mindest-Kräuselfaktor für weite
Röcke/Ballonrock) – der Buchtext trennt beide Fälle nicht durch einen
expliziten Schwellenwert.

**Status:** gesperrt (Seite nicht bestätigt).

**Offene Fragen oder Widersprüche:** Kein Kriterium im Buchtext, wann ein Rock
noch „mäßige" statt „weite" Kräuselweite hat – Übergang zu Kräuselfaktor
2 (Formel 5) bleibt unscharf.

---

## 2. Mindest-Kräuselfaktor für weite Röcke und Ballon-Rock

**Quelle:** [formeln_s048.md](formeln_s048.md), Abschnitt „Mindest-Kräuselfaktor
für weite Röcke und Ballon-Rock".

**Buchfassung:**

```text
Für weite Röcke und den Ballon-Rock benötigt man je nach Stoffqualität mindestens den Kräuselfaktor 2 (siehe unten). Die Ansatzweite für die Berechnung ist hierbei die Bundweite.
```

**Technische Formel:**

```text
Kräuselfaktor ≥ 2   (Ansatzweite = Bundweite)
```

**Eingaben und Einheiten:**

- `Bundweite`: Ansatzweite für die Berechnung (cm).
- `Kräuselfaktor`: dimensionslos, Untergrenze 2, oberes Ende offen
  ("je nach Stoffqualität").

**Ausgabe und Einheit:** kein direkter Zahlenwert; Untergrenze für den in
Formel 3–5 (Kräuselfaktor 1,5/2/3) verwendeten Faktor bei diesem Rocktyp.

**Bereiche, Bedingungen und Auswahlentscheidungen:**

- Untergrenze 2, kein Maximalwert im Buchtext.
- Auswahl des konkreten Faktors „je nach Stoffqualität" – fachliche
  Ermessensentscheidung, keine feste Regel.

**Abhängigkeiten:** Setzt den zulässigen Bereich für Kräuselfaktor in Formel 4
(Kräuselfaktor 2) und Formel 5 (Kräuselfaktor 3) als Anwendungsfälle „weiter
Rock"/"Ballon-Rock". Formel 3 (Kräuselfaktor 1,5) liegt außerhalb dieser
Untergrenze und gehört laut Buchtext nicht zu diesem Rocktyp.

**Status:** gesperrt (Seite nicht bestätigt).

**Offene Fragen oder Widersprüche:** Keine obere Grenze und kein Kriterium
für die stoffabhängige Wahl zwischen Kräuselfaktor 2 und 3 im Buchtext.

---

## 3. ☐4 Kräuselfaktor 1,5

**Quelle:** [formeln_s048.md](formeln_s048.md), Abschnitt „☐4 Kräuselfaktor
1,5".

**Buchfassung:**

```text
Nahtlänge (NL) Rock = Bundnaht · 1,5
```

**Technische Formel:**

```text
NL_Rock = Bundnaht_Länge · 1,5
```

**Eingaben und Einheiten:**

- `Bundnaht_Länge`: Länge der Bundnaht/Ansatznaht (cm).

**Ausgabe und Einheit:**

- `NL_Rock`: Nahtlänge/offene Weite (ofW) des zu kräuselnden Schnittteils (cm).

**Bereiche, Bedingungen und Auswahlentscheidungen:** fester Faktor 1,5, laut
Buchtext für „weite Röcke und Ballon-Rock" nicht ausreichend (siehe Formel 2,
Untergrenze 2).

**Abhängigkeiten:** Gleiche Formstruktur wie Formel 4 und 5 (Kräuselfaktor 2
bzw. 3), nur mit anderem Faktor. Zeichnungsgebunden zu
`skizzen/s048_skizze_04.png`.

**Status:** gesperrt (Seite nicht bestätigt).

**Offene Fragen oder Widersprüche:** keine.

---

## 4. ☐5 Kräuselfaktor 2

**Quelle:** [formeln_s048.md](formeln_s048.md), Abschnitt „☐5 Kräuselfaktor 2".

**Buchfassung:**

```text
Nahtlänge (NL) Rock = Bundnaht · 2
```

**Technische Formel:**

```text
NL_Rock = Bundnaht_Länge · 2
```

**Eingaben und Einheiten:**

- `Bundnaht_Länge`: Länge der Bundnaht/Ansatznaht (cm).

**Ausgabe und Einheit:**

- `NL_Rock`: Nahtlänge/offene Weite (ofW) des zu kräuselnden Schnittteils (cm).

**Bereiche, Bedingungen und Auswahlentscheidungen:** fester Faktor 2, laut
Formel 2 die genannte Untergrenze für weite Röcke/Ballon-Rock.

**Abhängigkeiten:** Gleiche Formstruktur wie Formel 3 und 5. Instanz der
Untergrenze aus Formel 2. Zeichnungsgebunden zu
`skizzen/s048_skizze_05.png`.

**Status:** gesperrt (Seite nicht bestätigt).

**Offene Fragen oder Widersprüche:** keine.

---

## 5. ☐6 Kräuselfaktor 3

**Quelle:** [formeln_s048.md](formeln_s048.md), Abschnitt „☐6 Kräuselfaktor 3".

**Buchfassung:**

```text
Nahtlänge (NL) Rock = Bundnaht · 3
```

**Technische Formel:**

```text
NL_Rock = Bundnaht_Länge · 3
```

**Eingaben und Einheiten:**

- `Bundnaht_Länge`: Länge der Bundnaht/Ansatznaht (cm).

**Ausgabe und Einheit:**

- `NL_Rock`: Nahtlänge/offene Weite (ofW) des zu kräuselnden Schnittteils (cm).

**Bereiche, Bedingungen und Auswahlentscheidungen:** fester Faktor 3, oberes
im Buchtext gezeigtes Beispiel; kein ausdrücklicher Maximalwert genannt.

**Abhängigkeiten:** Gleiche Formstruktur wie Formel 3 und 4. Zeichnungsgebunden
zu `skizzen/s048_skizze_06.png`.

**Status:** gesperrt (Seite nicht bestätigt).

**Offene Fragen oder Widersprüche:** keine.
