# Formeln – s043 (normalisiert, technische Fassung)

Diese Fassung trennt die Buchformeln von `formeln_s043.md` (fototreu) von
einer technischen Lesart. **Von den fünf erfassten Stellen ist bisher nur das
Zahlenbeispiel** `48 cm : 6 = 8 cm` **(Formel 2, Teil) am Original bestätigt**
(siehe `s043.md`, Abschnitt „Vorab geklärte formel- und coderelevante
Stellen"). Alle übrigen Stellen stehen auf `offen`, bis Werner sie am
Original geprüft hat.

## Formel 1 – Saumerweiterung im Beispiel

**Quelle:** [formeln_s043.md](formeln_s043.md), Abschnitt 1
(→ [ocr_s043.md](ocr_s043.md), Zeile 8).

**Buchfassung:**

```text
6 Keile · 6 cm Öffnung = 36 cm Saumerweiterung
```

**Technische Formel:**

```text
saumerweiterung_gesamt = anzahl_keile * oeffnung_je_keil
```

**Eingaben und Einheiten:** `anzahl_keile` – Anzahl, dimensionslos (Beispiel:
6); `oeffnung_je_keil` – cm (Beispiel: 6 cm).

**Ausgabe und Einheit:** `saumerweiterung_gesamt` – cm (Beispiel: 36 cm).

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine; das Beispiel
nennt feste Werte, keine Buchregel zur Wahl von `anzahl_keile` oder
`oeffnung_je_keil`.

**Abhängigkeiten:** Gleiche Grundbeziehung wie Formel 2, dort nach
`oeffnung_je_keil` aufgelöst statt nach `saumerweiterung_gesamt`. Siehe
„Beobachtete Übereinstimmung" unten zum Wert `oeffnung_je_keil = 6 cm` und
Formel 3.

**Status:** offen

**Nachgerechnet:** `6 · 6 cm = 36 cm` – stimmt mit dem gedruckten Beispiel
überein.

**Offene Fragen:** Nicht bestätigt; unabhängig von Formel 2 zu behandeln
(Rechenbeispiel, kein Beleg für eine andere Buchformel).

## Formel 2 – Berechnung des Öffnungsbetrags für eine gewünschte Saumerweiterung

**Quelle:** [formeln_s043.md](formeln_s043.md), Abschnitt 2
(→ [ocr_s043.md](ocr_s043.md), Zeilen 12–13).

**Buchfassung:**

```text
Öffnungsbetrag = gewünschte Saumerweiterung : Erweiterungsstellen
Beispiel: 48 cm : 6 = 8 cm
```

**Technische Formel:**

```text
oeffnungsbetrag = gewuenschte_saumerweiterung / erweiterungsstellen
```

**Eingaben und Einheiten:** `gewuenschte_saumerweiterung` – cm (Beispiel:
48 cm); `erweiterungsstellen` – Anzahl, dimensionslos (Beispiel: 6).

**Ausgabe und Einheit:** `oeffnungsbetrag` – cm je Erweiterungsstelle
(Beispiel: 8 cm).

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine; freie Eingabe
von `gewuenschte_saumerweiterung`, `erweiterungsstellen` laut Textabsatz auf
dieser Seite mit 6 vorbelegt („sechs Erweiterungsstellen").

**Abhängigkeiten:** Kehrwert-Beziehung zu Formel 1. Siehe „Beobachtete
Übereinstimmung" unten zum Wert `oeffnung_je_keil = 6 cm` aus Formel 1/3.

**Status je Teil:**

- Allgemeine Formel `Öffnungsbetrag = gewünschte Saumerweiterung :
  Erweiterungsstellen` — nicht bestätigt.
- Zahlenbeispiel `48 cm : 6 = 8 cm`, inklusive Bestätigung, dass nach
  „Beispiel:" kein zusätzliches Gleichheitszeichen steht — bestätigt
  (s043.md).

**Status (gesamt):** offen

**Nachgerechnet:** `48 cm : 6 = 8 cm` – stimmt.

**Offene Fragen:** Ob `erweiterungsstellen` immer 6 ist oder von der
Rockweite/Anzahl der Keile abhängt, ist im Buchtext dieser Seite nicht
gesondert geregelt (nur für das Beispiel dieser Seite mit 6 Stellen).

## Formel 3 – Öffnen und Ausstellen am Saum (VT, zeichnungsgebunden)

**Quelle:** [formeln_s043.md](formeln_s043.md), Abschnitt 3
(→ [skizzen_s043.json](skizzen_s043.json), Skizze 01;
`skizzen/s043_skizze_01.png`).

**Buchfassung:**

```text
VT, Punkt 8 (Verhältnis 2/3 zur vM-Seite : 1/3 zur SN-Seite): öffnen hier 6 cm
VT, Punkt 9 (an der SN, Verhältnis 1/3): ausstellen hier 3 cm
```

**Technische Formel:**

```text
oeffnen_betrag(VT) = 6 cm   (an Punkt 8, Teilverhältnis 2/3 : 1/3)
ausstellen_betrag(VT) = 3 cm   (an Punkt 9, SN)
```

**Eingaben und Einheiten:** keine Variable; feste, aus der Zeichnung
abgelesene cm-Werte.

**Ausgabe und Einheit:** zwei Streckenmaße zur Konstruktion der geöffneten
und ausgestellten Saumlinie, cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine; feste Werte ohne
Bereichsangabe.

**Abhängigkeiten:** `oeffnen_betrag(VT) = 6 cm` ist zahlenmäßig identisch mit
`oeffnung_je_keil` aus Formel 1. Formel 4 überträgt beide Werte unverändert
auf das RT.

**Status:** offen

**Offene Fragen:** Nicht bestätigt; Bezugsgröße der Verhältnisse `2/3`/`1/3`
(wovon genau die Anteile sind) ist aus der Beschriftung allein nicht
eindeutig.

## Formel 4 – Öffnungsbetrag nach hinten übertragen (zeichnungsgebunden)

**Quelle:** [formeln_s043.md](formeln_s043.md), Abschnitt 4
(→ [skizzen_s043.json](skizzen_s043.json), Skizze 01;
`skizzen/s043_skizze_01.png`).

**Buchfassung:**

```text
½ der Öffnung ausstellen
Öffnungsbetrag nach hinten übertragen
```

**Technische Formel:**

```text
oeffnen_betrag(RT) = oeffnen_betrag(VT) = 6 cm      (öffnen wie vorne)
ausstellen_betrag(RT) = ausstellen_betrag(VT) = 3 cm  (ausstellen wie vorne)
```

**Eingaben und Einheiten:** `oeffnen_betrag(VT)`, `ausstellen_betrag(VT)` aus
Formel 3, cm.

**Ausgabe und Einheit:** identische Streckenmaße für das RT, cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext
erkennbar.

**Abhängigkeiten:** Baut unmittelbar auf Formel 3 auf (VT-Werte).

**Status:** offen

**Offene Fragen:** Die genaue Bedeutung von „½ der Öffnung ausstellen" und
„Öffnungsbetrag nach hinten übertragen" (welche Konstruktionslinie, welche
Rechenoperation) ist aus der Beschriftung allein nicht auflösbar und muss am
Original geklärt werden.

## Formel 5 – Abnäherlänge RT (zeichnungsgebunden)

**Quelle:** [formeln_s043.md](formeln_s043.md), Abschnitt 5
(→ [skizzen_s043.json](skizzen_s043.json), Skizze 01;
`skizzen/s043_skizze_01.png`).

**Buchfassung:**

```text
RT, zwischen Punkt 11 und Punkt 12 (Bruchverhältnis ½ : ½ am Bund): 12 bis 15 cm
```

**Technische Formel:**

```text
abnaeherlaenge(RT) = 12 bis 15 cm
```

**Eingaben und Einheiten:** keine Variable; Bereich direkt aus der Zeichnung.

**Ausgabe und Einheit:** `abnaeherlaenge` – cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich `12` bis
`15 cm`, keine Buchregel zur Auswahl eines konkreten Werts.

**Abhängigkeiten:** Bezieht sich vermutlich auf den Textschritt „RT-Abnäher
verschieben ... auf die optimale Länge gekürzt" ([ocr_s043.md](ocr_s043.md),
Zeilen 15–17), der im Fließtext selbst keine Zahl nennt.

**Status:** offen

**Offene Fragen:** Ob Punkt 11–Punkt 12 die Bundlinie oder eine andere Strecke
meint, und ob „optimale Länge" (Textschritt) mit diesem Bereich
gleichzusetzen ist, hat Werner am Original zu prüfen.

## Beobachtete Übereinstimmung zwischen Text und Skizze (nicht aufgelöst)

Der Text nennt `oeffnung_je_keil = 6 cm` (Formel 1) und „sechs
Erweiterungsstellen" (Formel 2); die Skizze beschriftet an der einzigen
sichtbaren Erweiterungsstelle (VT, Punkt 8) denselben Wert „öffnen hier
6 cm" (Formel 3). Fototreu als Beobachtung festgehalten, nicht als
bestätigter Zusammenhang: ob die Zeichnung exakt eine der sechs
Erweiterungsstellen des Textbeispiels zeigt, entscheidet Werner.

## Zusammenfassung

Fünf Stellen erfasst, keine davon vollständig bestätigt – nur das
Zahlenbeispiel `48 cm : 6 = 8 cm` (Formel 2, Teil) ist am Original bestätigt.
Formel 1 und 2 sind Rechenbeispiele bzw. eine allgemeine Kehrwertformel aus
dem Fließtext; Formel 3–5 stammen ausschließlich aus Skizze 01 und waren in
der vorherigen Extraktionsfassung noch nicht erfasst. Für einen späteren
Codevertrag muss Werner mindestens die Bezugsgrößen der Verhältnisse
(„2/3"/„1/3", „½ : ½"), die Bedeutung von „Öffnungsbetrag nach hinten
übertragen" und den Bereich „12 bis 15 cm" am Original klären.
