# Formeln s206 – Normalisierung (Walking Skeleton, offen)

**Status: Walking Skeleton – keine Stelle ist am Original bestätigt.** Alle
Einträge tragen daher `Status: offen`. Diese Datei ersetzt keine
Werner-Prüfung und keinen späteren Codevertrag.

Seite 206 liegt in `08_grundschnitte_aermel_s197-220/`, einer Kategorie, die
im AGENT.md nicht zu den drei ausdrücklich benannten Formel-Kategorien
gehört. Die Normalisierung entsteht auf Werners Wunsch als Walking Skeleton.

---

## 1. Saum-Konstruktion

**Quelle:** [`formeln_s206.md`](formeln_s206.md), Abschnitt 1.

**Buchfassung:**

```text
An der Saumlinie 2 bis 3 cm hochmessen und 1/2 ÄSaW zur Saumlinie abtragen → Saum.
```

**Technische Formel:**

```text
h_hoch ∈ [2 cm, 3 cm]        # hochmessen an der Saumlinie
s_ab = ÄSaW / 2               # Abtrag zur Saumlinie
```

Wie `h_hoch` und `s_ab` geometrisch zum Punkt/zur Linie „Saum" zusammenwirken,
ist aus dem Fließtext allein nicht eindeutig ableitbar (zeichnungsabhängig).

**Eingaben und Einheiten:**
- `ÄSaW` – Bedeutung nicht belegt (vermutlich eine Ärmel-Saumweite), Einheit cm.
- Bereich 2 bis 3 cm (dimensionslos benannt, cm implizit).

**Ausgabe und Einheit:** Lage der Linie/des Punkts „Saum" im Schnittbild, cm.

**Bereiche, Bedingungen, Auswahlentscheidungen:**
- 2 bis 3 cm bleibt Bereich, kein fester Wert oder Default ohne Buchregel.
- Zusätzliche, nicht quantifizierte Auswahlregel: „Die ÄSaW kann/sollte bei
  unelastischen Materialien hierbei etwas größer ausfallen." – keine Zahl,
  daher kein einsetzbarer Wert, nur als fachlicher Hinweis vermerkt.
- Zeichnungsgebundenes Rechenbeispiel (skizze_01, `geprueft: false`):
  `1/2 ÄsW 13 cm`. Nicht nachgerechnet, da `ÄsW` nicht sicher mit `ÄSaW`
  gleichgesetzt werden kann und der Bezugswert von ÄSaW/ÄsW aus dieser Seite
  nicht hervorgeht.

**Abhängigkeiten:**
- Bezug „Weiterentwicklung von Seite 205" – Punkte P8/P10 stammen von dort;
  zu verlinken, sobald Seite 205 bearbeitet ist, nicht zu kopieren.
- Möglicher Zusammenhang zwischen `ÄSaW` (Fließtext) und `ÄsW`
  (Skizzenbeschreibung skizze_01) – ungeklärt.

**Status:** offen

**Offene Fragen oder Widersprüche:**
- Bedeutung und Herkunft von `ÄSaW` nicht belegt.
- OCR-Rohtext zeigt „A5aW" statt „ÄSaW" (eigene, unbestätigte Lesung) und
  „ÄsW" in der Skizzenbeschreibung – möglicherweise dieselbe Abkürzung,
  möglicherweise nicht.
- Geometrische Verknüpfung von „hochmessen" und „abtragen" zum Punkt „Saum"
  nicht aus dem Text ableitbar.

---

## 2. Ellenbogen-Einstellung hinten

**Quelle:** [`formeln_s206.md`](formeln_s206.md), Abschnitt 2.

**Buchfassung:**

```text
An der Ellenbogenlinie hinten (rechts) 0,5 bis 1 cm einstellen. Von P8 über die Einstellung weiter zum Saum zeichnen → hinterer Ärmelbruch.
```

**Technische Formel:**

```text
e ∈ [0,5 cm, 1 cm]   # Einstellung an der Ellenbogenlinie hinten
```

Die daraus resultierende Linie (P8 über den Einstellungspunkt zum Saum) ist
eine geometrische Verbindung ohne weitere Rechenoperation.

**Eingaben und Einheiten:** Bereich 0,5 bis 1 cm; Bezugspunkt P8 (aus Seite 205).

**Ausgabe und Einheit:** Verlauf des „hinteren Ärmelbruchs" im Schnittbild.

**Bereiche, Bedingungen, Auswahlentscheidungen:** 0,5 bis 1 cm bleibt Bereich.

**Abhängigkeiten:** Punkt P8 aus Seite 205 (verlinken, nicht kopieren).

**Status:** offen

**Offene Fragen oder Widersprüche:** Keine über die generelle
Nicht-Verifikation der Seite hinaus.

---

## 3. Ärmelnaht-Einstellung ohne Abnäher – Grenzwert

**Quelle:** [`formeln_s206.md`](formeln_s206.md), Abschnitt 3.

**Buchfassung:**

```text
An beiden Ärmelnähten maximal 4 cm einstellen.
```

**Technische Formel:**

```text
e_naht ≤ 4 cm   # Einstellung je Ärmelnaht (beidseitig)
```

**Eingaben und Einheiten:** Obergrenze 4 cm; kein Mindestwert genannt.

**Ausgabe und Einheit:** eingestellte Nahtlinie je Ärmelnaht, cm.

**Bereiche, Bedingungen, Auswahlentscheidungen:** Nur Obergrenze fixiert
(„maximal"); konkrete Wahl innerhalb 0–4 cm bleibt fachliche Entscheidung,
im Buch nicht weiter spezifiziert.

**Abhängigkeiten:** Gilt für die Variante „Ärmel ohne Abnäher" (Abschnitt 7
der Seite); zeichnungsgebundener Beleg skizze_04 (`geprueft: false`).

**Status:** offen

**Offene Fragen oder Widersprüche:** Keine über die generelle
Nicht-Verifikation der Seite hinaus.

---

## 4. Nahtlängen-Ausgleich

**Quelle:** [`formeln_s206.md`](formeln_s206.md), Abschnitt 4.

**Buchfassung:**

```text
Die längere (hintere) Ärmelnaht messen und auf die kürzere (vordere) Ärmelnaht übertragen.
```

**Technische Formel:**

```text
Länge(Ärmelnaht_vorn_neu) = Länge(Ärmelnaht_hinten)
# gilt unter der im Buchtext genannten Bedingung: hintere Naht ist länger
```

**Eingaben und Einheiten:** Länge der hinteren Ärmelnaht (aus vorheriger
Konstruktion, cm); Länge der vorderen Ärmelnaht (aus vorheriger Konstruktion,
cm).

**Ausgabe und Einheit:** angepasste Länge der vorderen Ärmelnaht, cm.

**Bereiche, Bedingungen, Auswahlentscheidungen:** Buchtext benennt die
hintere Naht ausdrücklich als die längere; die Regel setzt diese Bedingung
voraus und ist nicht als allgemeiner Vergleich (`falls länger, dann …`)
formuliert.

**Abhängigkeiten:** Setzt die vorherige Konstruktion beider Ärmelnähte
derselben Seite voraus (Abschnitt 7, Variante ohne Abnäher).

**Status:** offen

**Offene Fragen oder Widersprüche:** Keine über die generelle
Nicht-Verifikation der Seite hinaus.
