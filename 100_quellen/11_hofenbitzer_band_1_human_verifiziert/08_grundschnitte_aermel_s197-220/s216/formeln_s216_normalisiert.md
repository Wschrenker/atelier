# Formeln s216 – Normalisierung (Walking Skeleton, offen)

**Status: Walking Skeleton – keine Stelle ist am Original bestätigt.** Alle
Einträge tragen daher `Status: offen`. Diese Datei ersetzt keine
Werner-Prüfung und keinen späteren Codevertrag.

Seite 216 liegt in `08_grundschnitte_aermel_s197-220/`, einer Kategorie, die
im AGENT.md nicht zu den drei ausdrücklich benannten Formel-Kategorien
gehört. Die Normalisierung entsteht auf Werners Wunsch als Walking Skeleton.

---

## 1. Schulterpolster-Erhöhung (Definition als Messdifferenz)

**Quelle:** [`formeln_s216.md`](formeln_s216.md), Abschnitt 1.

**Buchfassung:**

```text
Über das Schulterpolster wird von Nadel zu Nadel gemessen. Dann nimmt man das Schulterpolster ab und misst dieselbe Strecke ohne Schulterpolster. Die Differenz beider Maße ist die benötigte Schulterpolster-Erhöhung.
```

**Technische Formel:**

```text
SPE = M_mit_Polster - M_ohne_Polster
```

**Eingaben und Einheiten:**
- `M_mit_Polster` – Strecke Nadel zu Nadel über dem aufgelegten Schulterpolster, cm.
- `M_ohne_Polster` – dieselbe Strecke ohne Schulterpolster, cm.

**Ausgabe und Einheit:** `SPE` – Schulterpolster-Erhöhung, cm.

**Bereiche, Bedingungen, Auswahlentscheidungen:** Keine; exakte Messdifferenz
ohne Näherung.

**Abhängigkeiten:** Basiswert für die Abschnitte 2–6 dieser Seite (alle
folgenden Formeln beziehen sich auf `SPE`).

**Status:** offen

**Offene Fragen oder Widersprüche:** Keine über die generelle
Nicht-Verifikation der Seite hinaus.

---

## 2. Waagerechte Öffnung am Ärmelkugelansatz

**Quelle:** [`formeln_s216.md`](formeln_s216.md), Abschnitt 2.

**Buchfassung (Fließtext):**

```text
An der waagerechten Öffnungen um ca. (1/2) Schulterpolster-Erhöhung = ungebahre Polsterdicke öffnen.
```

**Buchfassung (Zeichnung, skizze_07):**

```text
Polsterdicke oder ca. 1/3 Schulterpolster-Erhöhung öffnen
```

**Technische Formel (zwei nicht deckungsgleiche Lesarten):**

```text
Ö_waag ≈ SPE / 2   # Fließtext; laut Fließtext ≈ Polsterdicke ("ungefähre", eigene Lesung)
Ö_waag ≈ SPE / 3   # Zeichnung; laut Zeichnung = Polsterdicke
```

**Eingaben und Einheiten:** `SPE` aus Formel 1, cm.

**Ausgabe und Einheit:** `Ö_waag` – waagerechte Öffnung am Ärmelkugelansatz, cm.

**Bereiche, Bedingungen, Auswahlentscheidungen:** Beide Fassungen sind mit
„ca." markiert, bleiben also Näherungen, kein fester Wert ohne Buchregel.

**Abhängigkeiten:** Bezugspunkt ist die Kappung „ca. 5 cm" an der
Ärmelkugelspitze (Kreis 4, `formeln_s216.md`, „Nicht erfasst"), von dort aus
gemessen laut Zeichnung.

**Status:** offen

**Offene Fragen oder Widersprüche:**
- Fließtext nennt `SPE / 2`, die Zeichnung an derselben Stelle `SPE / 3`;
  Widerspruch nicht aufgelöst, beide Werte stehenlassen (siehe `s216.md`,
  Prüfstelle 3).
- Ob „= Polsterdicke" (Zeichnung) und „= ungefähre Polsterdicke" (Fließtext,
  eigene Lesung von „ungebahre") dieselbe Aussage treffen, ist nicht belegt.

---

## 3. Senkrechte Öffnung unterhalb vÄP

**Quelle:** [`formeln_s216.md`](formeln_s216.md), Abschnitt 3.

**Buchfassung (Fließtext):**

```text
Fur einen proportional ausgewogenen Armel jeweils die halbe waagerechte Öffnung (1/2) Polsterdicke auch senkrecht öffnen.
```

**Buchfassung (Zeichnung, skizze_07):**

```text
öffnen um ca. 1/6 Schulterpolster-Erhöhung (= 1/2 Polsterdicke)
```

**Technische Formel:**

```text
Ö_senk = Ö_waag / 2   # Fließtext, als Ableitung aus Formel 2
Ö_senk ≈ SPE / 6       # Zeichnung, direkt in Bruchteilen von SPE angegeben
```

**Eingaben und Einheiten:** `Ö_waag` (Formel 2) bzw. `SPE` (Formel 1), cm.

**Ausgabe und Einheit:** `Ö_senk` – senkrechte Öffnung unterhalb vÄP, cm.

**Bereiche, Bedingungen, Auswahlentscheidungen:** „ca." bei der
Zeichnungsangabe; keine feste Auswahl ohne weitere Buchregel.

**Abhängigkeiten:** Formel 2 (Ö_waag bzw. SPE).

**Status:** offen

**Offene Fragen oder Widersprüche:**
- Beobachtung, nicht aufgelöst: `SPE/6` ist genau die Hälfte von `SPE/3`
  (der Zeichnungs-Lesart aus Formel 2), passt also intern zur Zeichnung,
  nicht aber zwingend zur Fließtext-Lesart `SPE/2` aus Formel 2. Keine
  eigene Auflösung, nur Beobachtung für Werners Prüfung.
- Beide Fassungen nennen „= 1/2 Polsterdicke" als Ergebnis; ob das für beide
  Bruchangaben (`SPE/2`-Ableitung und `SPE/6`) gleichermaßen gilt, ist nicht
  belegt.

---

## 4. Saum-Öffnung (Bezug auf Folgeseite)

**Quelle:** [`formeln_s216.md`](formeln_s216.md), Abschnitt 4.

**Buchfassung (Fließtext):**

```text
Am Saum kann (wie auf folgender Seite) derselbe Betrag geöffnet werden (hier allerdings ohne Öffnung dargestellt).
```

**Buchfassung (Zeichnung, skizze_07):**

```text
ggf. max. wie oben öffnen für Saum-Erweiterung
1/2  1/2   (Beschriftung „üb" links, „me" rechts der Ärmelunternaht)
```

**Technische Formel:**

```text
Ö_saum ≤ Ö_senk     # "derselbe Betrag", als Maximum, laut Zeichnung
Ö_saum = Ö_saum_üb + Ö_saum_me, mit Ö_saum_üb = Ö_saum_me = Ö_saum / 2   # Aufteilung auf beide Seiten der Unternaht
```

**Eingaben und Einheiten:** `Ö_senk` (Formel 3), cm.

**Ausgabe und Einheit:** `Ö_saum` – Saum-Öffnung, cm; aufgeteilt in zwei
Hälften an den Beschriftungen „üb" und „me".

**Bereiche, Bedingungen, Auswahlentscheidungen:** „ggf." und „max." markieren
eine fachliche Wahlmöglichkeit, kein fester Wert. Auf Seite 216 selbst „ohne
Öffnung dargestellt" (laut Fließtext).

**Abhängigkeiten:** Genaue Regel steht laut Fließtext auf Seite 217 (noch
nicht bearbeitet); hier nur verlinkt, nicht kopiert, sobald diese Seite
vorliegt.

**Status:** offen

**Offene Fragen oder Widersprüche:**
- Bedeutung von „üb" und „me" (Zeichnungsbeschriftung) nicht belegt.
- Konkrete Regel für Seite 217 fehlt noch; diese Formel bleibt bis dahin
  unvollständig.

---

## 5. Teilungsverhältnis der Schulterpolster-Erhöhung auf VT/RT

**Quelle:** [`formeln_s216.md`](formeln_s216.md), Abschnitt 5.

**Buchfassung (Zeichnung, skizze_05 und skizze_06):**

```text
1/3 Schulterpolster-Erhöhung vorne
2/3 Schulterpolster-Erhöhung hinten
```

**Technische Formel:**

```text
E_vorne  = SPE / 3
E_hinten = SPE * 2/3
```

**Eingaben und Einheiten:** `SPE` aus Formel 1, cm.

**Ausgabe und Einheit:** `E_vorne`, `E_hinten` – Anteil der
Schulterpolster-Erhöhung an VT bzw. RT, cm.

**Bereiche, Bedingungen, Auswahlentscheidungen:** Fester Bruchteil laut
beiden Zeichnungen, kein Bereich.

**Abhängigkeiten:** Formel 1 (`SPE`). Gilt laut Zeichnung sowohl für die
Variante „geringe Erhöhung" (☐4) als auch für „größere Erhöhung mit
Schulterverbreiterung" (☐5); bei Letzterer zusätzlich Formel 6.

**Status:** offen

**Offene Fragen oder Widersprüche:** Keine über die generelle
Nicht-Verifikation der Seite hinaus.

---

## 6. Schulterverbreiterung bei größerer Erhöhung

**Quelle:** [`formeln_s216.md`](formeln_s216.md), Abschnitt 6.

**Buchfassung:**

```text
D5 Bei einer größeren Erhöhung kann gleichzeitig eine leichte Schulter-Verbreiterung von wenigen Millimetern am VT und am RT identisch vorgenommen werden.
```

**Technische Formel:**

```text
B_Schulter_VT = B_Schulter_RT   # identisch an VT und RT
B_Schulter ∈ "wenige mm"         # kein Zahlenbereich im Buchtext
```

**Eingaben und Einheiten:** Kein numerischer Eingabewert im Fließtext; nur
die qualitative Angabe „wenige Millimeter".

**Ausgabe und Einheit:** `B_Schulter` – zusätzliche Schulterverbreiterung an
VT und RT, mm (Einheit aus dem Text übernommen, kein cm wie sonst auf dieser
Seite).

**Bereiche, Bedingungen, Auswahlentscheidungen:** „kann … vorgenommen
werden" – fachliche Auswahloption, kein Pflichtschritt; „wenige Millimeter"
bleibt unbezifferter Bereich, kein Default ohne Buchregel.

**Abhängigkeiten:** Nur bei der Variante „größere Erhöhung" (☐5, Formel 5);
entspricht der unbezifferten dritten Teilfläche (Kreis 3) in skizze_06.

**Status:** offen

**Offene Fragen oder Widersprüche:** Kein Zahlenwert für „wenige
Millimeter" im Buch angegeben; auch die Zeichnung (Kreis 3) trägt keine
Bezifferung.
