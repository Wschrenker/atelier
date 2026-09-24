# Formeln – s038 (normalisiert)

Technische Fassung zu [formeln_s038.md](formeln_s038.md). Jede Formel verweist
auf ihren Abschnitt dort. Buchfassung und technische Fassung bleiben getrennt.

## F1 – Taillenausfall (Textformel)

- **Quelle:** [formeln_s038.md](formeln_s038.md), Abschnitt 1.
- **Buchfassung:**

```text
TaAf = Taillenabtrennung - 1 / 2 BuW
= 50,7 cm - 43 cm
= 7,7 cm
```

- **Technische Formel:** `TaAf = Taillenabtrennung - 0.5 * X`, wobei `X` der im
  Buch mit „BuW" bezeichnete Wert ist, der zahlenmäßig 43 cm entspricht.
- **Eingaben und Einheiten:** `Taillenabtrennung = 50,7 cm` (an der Zeichnung
  gemessene Länge der gestrichelten Taillenabtrennung); `X = 43 cm`.
- **Ausgabe und Einheit:** `TaAf = 7,7 cm`.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine; Einzelrechnung für
  dieses Beispiel.
- **Abhängigkeiten:** `X = 43 cm` ist zahlengleich mit `1/2 BuU` aus F6. Siehe
  Widerspruch unten.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Die Rechnung `50,7 − 43 = 7,7` ist
  bestätigt. Nicht geklärt ist, ob „BuW" in der Buchfassung dieselbe Größe wie
  „BuU" (Bundumfang, Tabelle 1) meint oder eine eigene, hier nicht weiter
  belegte „Bundweite". Ohne diese Klärung bleibt offen, welchen Eingabewert
  eine spätere Implementierung tatsächlich verwenden müsste.

## F2 – Taillenausfall (Tabellenformel)

- **Quelle:** [formeln_s038.md](formeln_s038.md), Abschnitt 2.
- **Buchfassung:**

```text
TaAf = 1/2 HÜW - 1/2 TaW
```

- **Technische Formel:** `TaAf = 0.5 * HuW - 0.5 * TaW`.
- **Eingaben und Einheiten:** `HuW = 100 cm` (aus F4, bestätigt); `TaW` nicht
  besetzt (kein gewählter Zugabewert, siehe F5).
- **Ausgabe und Einheit:** `TaAf`, Einheit cm.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** hängt vollständig vom noch
  offenen `TaW` aus F5 ab.
- **Abhängigkeiten:** F4 (`HuW`), F5 (`TaW`).
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** Diese Tabellenzeile ist nicht
  bestätigt. Setzt man den bestätigten Wert `TaAf = 7,7 cm` aus F1 ein, ergibt
  sich rechnerisch `TaW = HuW - 2·TaAf = 100 - 15,4 = 84,6 cm`. Das liegt
  deutlich außerhalb des für `TaW` aus `TaU = 78` und Zugabebereich `+1–2`
  plausiblen Bereichs (79–80 cm). F1 und F2 widersprechen sich damit
  rechnerisch. Beide Fassungen bleiben nebeneinander stehen; keine wird als
  Beweis für die andere verwendet.

## F3 – Rechenbeispiel: Verteilung des Taillenausfalls

- **Quelle:** [formeln_s038.md](formeln_s038.md), Abschnitt 3.
- **Buchfassung:**

```text
Hüftabstich: 4,2 cm
VT-Abnäher: 1,0 cm
RT-Abnäher: 2,5 cm
```

- **Technische Formel:** `Hüftabstich_Beispiel + VT_Abnäher_Beispiel + RT_Abnäher_Beispiel = TaAf`.
- **Eingaben und Einheiten:** `4,2 cm`, `1,0 cm`, `2,5 cm`.
- **Ausgabe und Einheit:** Summe `7,7 cm`.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** laut Buchtext nur „eine
  mögliche Verteilung ... in diesem Beispiel"; keine feste Regel. Optional
  zwei hintere Abnäher statt einem.
- **Abhängigkeiten:** F1 (`TaAf`).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Unabhängig nachgerechnet:
  `4,2 + 1,0 + 2,5 = 7,7`, stimmt mit dem in F1 bestätigten `TaAf = 7,7 cm`
  überein. Diese Übereinstimmung ist aber kein Beleg für F2 und die einzelnen
  Beispielwerte selbst sind nicht bestätigt.

## F4 – Hüftweite (HüW)

- **Quelle:** [formeln_s038.md](formeln_s038.md), Abschnitt 4.
- **Buchfassung:**

```text
HüU = 97
Zugabebereich = +2–3, gewählt: 3
HüW = 100
1/2 HüW = 50
1/4 HüW = 25
```

- **Technische Formel:** `HuW = HuU + Zugabe_gewählt`.
- **Eingaben und Einheiten:** `HuU = 97 cm`; `Zugabe_gewählt = 3 cm` (aus
  Bereich `2–3 cm`).
- **Ausgabe und Einheit:** `HuW = 100 cm`; `0.5*HuW = 50 cm`; `0.25*HuW = 25 cm`.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Zugabebereich `2–3 cm`,
  hier mit `3 cm` belegt.
- **Abhängigkeiten:** wird in F2 als Eingabe verwendet.
- **Status:** normalisiert.
- **Offene Fragen oder Widersprüche:** keine.

## F5 – Taillenweite (TaW)

- **Quelle:** [formeln_s038.md](formeln_s038.md), Abschnitt 5.
- **Buchfassung:**

```text
TaU = 78
Zugabebereich = +1–2
TaW = —
1/2 TaW = —
1/4 TaW = —
```

- **Technische Formel:** `TaW = TaU + Zugabe`, `Zugabe ∈ [1 cm, 2 cm]`.
- **Eingaben und Einheiten:** `TaU = 78 cm`.
- **Ausgabe und Einheit:** `TaW ∈ [79 cm, 80 cm]`, kein fester Wert.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Zugabebereich `1–2 cm`
  ausdrücklich ohne gewählten Wert im Buch; kein Default ergänzt.
- **Abhängigkeiten:** Eingabe für F2.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Ohne Buchregel zur Wahl innerhalb des
  Bereichs bleibt `TaW` unbestimmt.

## F6 – Bundumfang (BuU)

- **Quelle:** [formeln_s038.md](formeln_s038.md), Abschnitt 6.
- **Buchfassung:**

```text
gBuU = 85
+ 1
BuU = 86
1/2 BuU = 43
```

- **Technische Formel:** `BuU = gBuU + 1`.
- **Eingaben und Einheiten:** `gBuU = 85 cm` (gemessener Bundumfang).
- **Ausgabe und Einheit:** `BuU = 86 cm`; `0.5*BuU = 43 cm`.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** feste Zugabe `+1 cm`,
  keine Wahl.
- **Abhängigkeiten:** zahlenmäßig identisch mit dem in F1 verwendeten Wert
  „BuW" = 43 cm; siehe offene Frage in F1.
- **Status:** normalisiert.
- **Offene Fragen oder Widersprüche:** keine für diese Zeile selbst.

## F7 – Kopfzeile „Kontrolle" (Tabelle 1)

- **Quelle:** [formeln_s038.md](formeln_s038.md), Abschnitt 7.
- **Buchfassung:**

```text
Kontrolle: 1/2 TaW = (Hü) + (Zg) = 2
```

- **Technische Formel:** nicht ableitbar.
- **Eingaben und Einheiten:** nicht ableitbar.
- **Ausgabe und Einheit:** nicht ableitbar.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** nicht ableitbar.
- **Abhängigkeiten:** unklar, evtl. zu F5 (`TaW`).
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** Die OCR-Fassung wirkt fehlerhaft oder
  unvollständig; ohne Prüfung am Original ist keine technische Formel
  ableitbar.

## F8 – Hüfttiefe und Bundabstände

- **Quelle:** [formeln_s038.md](formeln_s038.md), Abschnitt 8.
- **Buchfassung:**

```text
HüT = 20
BuA v = -6
BuA s = -3,5
BuA h = -2
```

- **Technische Formel:** definitorische Eingabewerte, keine Berechnung auf
  dieser Seite; dienen als Versatz vorne (`v`), seitlich (`s`) und hinten
  (`h`) zur Konstruktion der figurbedingten Bundlinie in der Zeichnung.
- **Eingaben und Einheiten:** `HuT = 20 cm`; `BuA_v = -6 cm`; `BuA_s = -3,5 cm`;
  `BuA_h = -2 cm`.
- **Ausgabe und Einheit:** Positionen der Bundlinie in der Zeichnung (kein
  Zahlenergebnis auf dieser Seite).
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** zeichnungsgebunden, siehe
  [skizzen_s038.json](skizzen_s038.json) und die Skizzenausschnitte.
- **Status:** normalisiert.
- **Offene Fragen oder Widersprüche:** keine.

## F9 – Hüftabstich und Abnäherverteilung (Tabelle 3)

- **Quelle:** [formeln_s038.md](formeln_s038.md), Abschnitt 9. Tabelle im
  Original diagonal durchgestrichen.
- **Buchfassung:**

```text
Hüftabstich = 1/2 TaAf ± 1
v. Abnäher = 0 oder 1,5 bis 2,5
1. h. Abnäher = bis 4,5
2. h. Abnäher = optional
Kontrolle: Σ = TaAf
```

- **Technische Formel:**
  - `Hüftabstich = 0.5 * TaAf ± 1`
  - `v_Abnäher = 0` **oder** `v_Abnäher ∈ [1,5 cm, 2,5 cm]`
  - `h1_Abnäher ≤ 4,5 cm` (Untergrenze im Buch nicht angegeben)
  - `h2_Abnäher`: optionale zweite Abnäherposition, keine Buchregel zur Größe
  - Kontrolle: `Σ(Hüftabstich, v_Abnäher, h1_Abnäher, h2_Abnäher) = TaAf`
- **Eingaben und Einheiten:** `TaAf` aus F1 (`7,7 cm`, mit offener Frage zur
  Variablenbenennung).
- **Ausgabe und Einheit:** `Hüftabstich ∈ [2,85 cm, 4,85 cm]` (aus
  `0,5·7,7 ± 1`); übrige Werte einzeln wie oben.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** `v. Abnäher` ist eine
  Auswahl zwischen `0` oder einem Bereich; `2. h. Abnäher` ist optional ohne
  Größenregel; die Kontrollzeile fordert Summengleichheit mit `TaAf`.
- **Abhängigkeiten:** F1 (`TaAf`).
- **Status:** teilweise normalisiert.
  - `Hüftabstich = 1/2 TaAf ± 1`: normalisiert (bestätigt).
  - `1. h. Abnäher = bis 4,5`: normalisiert (bestätigt), nur als Obergrenze
    ohne genannte Untergrenze.
  - `v. Abnäher = 0 oder 1,5 bis 2,5`: offen (nicht bestätigt).
  - `2. h. Abnäher = optional`: offen (nicht bestätigt).
  - `Kontrolle: Σ = TaAf`: offen (nicht bestätigt).
- **Offene Fragen oder Widersprüche:** Das bestätigte Rechenbeispiel
  (`Hüftabstich = 4,2 cm`, F3) liegt innerhalb des aus der bestätigten Formel
  berechneten Bereichs `[2,85 cm, 4,85 cm]` — konsistent, aber nur als
  Beobachtung, nicht als zusätzlicher Beleg vermerkt.
