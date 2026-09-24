# Formeln normalisiert – s033

Technische Fassung zu [formeln_s033.md](formeln_s033.md). Alle Buchfassungen
sind dort fototreu belegt und laut [s033.md](s033.md) am Original bestätigt.
Diese Datei erzeugt keine Python-Funktion, keinen Engine-Vertrag und keine
neue Fachregel.

## F1 – Hüftweite (HüW)

- **Quelle:** [formeln_s033.md](formeln_s033.md), Abschnitt „Tabelle 1 – Hauptmaße und Zugaben", Zeile 1.
- **Buchfassung:**
  ```text
  HüU | Hüftumfang | 97 | +2–3; gewählt 3 | = | Hüftweite | HüW | 100 | ½ 50 | ¼ 25
  ```
- **Technische Formel:** `HüW = HüU + Zugabe_HüW`; `½HüW = HüW / 2`; `¼HüW = HüW / 4`.
- **Eingaben und Einheiten:** `HüU` (Hüftumfang, cm, Körpermaß); `Zugabe_HüW` (cm, Bereich 2–3, im Beispiel gewählt 3).
- **Ausgabe und Einheit:** `HüW`, `½HüW`, `¼HüW` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `Zugabe_HüW ∈ [2; 3] cm`. Das Buch nennt keine Regel, nach der innerhalb des Bereichs gewählt wird — nur den Beispielwert 3.
- **Abhängigkeiten:** Eingabe für F3 (TaAf) und F9 (Grundgerüst-Konstruktion).
- **Status:** normalisiert. Rechenbeispiel geprüft: `97 + 3 = 100`; `100 / 2 = 50`; `100 / 4 = 25` — stimmt mit dem Buch überein.
- **Offene Fragen:** Auswahlregel für den Zugabewert innerhalb `[2; 3]` fehlt im Buch.

## F2 – Taillenweite (TaW)

- **Quelle:** [formeln_s033.md](formeln_s033.md), Abschnitt „Tabelle 1 – Hauptmaße und Zugaben", Zeile 2.
- **Buchfassung:**
  ```text
  TaU | Taillenumfang | 72 | +1–2; gewählt 2 | = | Taillenweite | TaW | 74 | ½ 37 | ¼ 18,5
  ```
- **Technische Formel:** `TaW = TaU + Zugabe_TaW`; `½TaW = TaW / 2`; `¼TaW = TaW / 4`.
- **Eingaben und Einheiten:** `TaU` (Taillenumfang, cm, Körpermaß); `Zugabe_TaW` (cm, Bereich 1–2, im Beispiel gewählt 2).
- **Ausgabe und Einheit:** `TaW`, `½TaW`, `¼TaW` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `Zugabe_TaW ∈ [1; 2] cm`. Keine Buchregel für die Auswahl innerhalb des Bereichs.
- **Abhängigkeiten:** Eingabe für F3 (TaAf).
- **Status:** normalisiert. Rechenbeispiel geprüft: `72 + 2 = 74`; `74 / 2 = 37`; `74 / 4 = 18,5` — stimmt.
- **Offene Fragen:** Auswahlregel für den Zugabewert innerhalb `[1; 2]` fehlt im Buch.

## F3 – Taillenausfall (TaAf)

- **Quelle:** [formeln_s033.md](formeln_s033.md), Abschnitt „Tabelle 1 – Hauptmaße und Zugaben", Zeile 3.
- **Buchfassung:**
  ```text
  TaAf | Taillenausfall | ½ HÜW - ½ TaW = | | | | | | 13 | ½ 6,5
  ```
- **Technische Formel:** `TaAf = ½HüW − ½TaW`; `½TaAf = TaAf / 2`.
- **Eingaben und Einheiten:** `½HüW` (cm, aus F1); `½TaW` (cm, aus F2).
- **Ausgabe und Einheit:** `TaAf`, `½TaAf` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine, feste Differenz.
- **Abhängigkeiten:** F1, F2 → F3. F3 ist Eingabe für F4 (Hüftabstich) und F8 (Kontrolle).
- **Status:** normalisiert. Rechenbeispiel geprüft: `50 − 37 = 13`; `13 / 2 = 6,5` — stimmt.
- **Offene Fragen:** keine.

## F4 – Hüftabstich

- **Quelle:** [formeln_s033.md](formeln_s033.md), Abschnitt „Tabelle 3 – Abstiche und Abnäher", Zeile 1.
- **Buchfassung:**
  ```text
  Hüftabstich | ½ TaAf ± 1 | 6,5
  ```
- **Technische Formel:** `Hüftabstich = ½TaAf ± 1`, Bereich `[½TaAf − 1; ½TaAf + 1]`.
- **Eingaben und Einheiten:** `½TaAf` (cm, aus F3).
- **Ausgabe und Einheit:** `Hüftabstich` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich `[5,5; 7,5]` cm (mit `½TaAf = 6,5`). Der gedruckte Beispielwert `6,5` liegt genau bei `½TaAf`, also ohne Abweichung durch `±1`. Das Buch nennt keine Regel, wann eine Abweichung angewendet wird.
- **Abhängigkeiten:** F3 → F4. F4 ist Eingabe für F8 (Kontrolle).
- **Status:** normalisiert. Rechenbeispiel liegt im Bereich, stimmt mit dem Buch überein.
- **Offene Fragen:** Auswahlregel für die Abweichung `±1` fehlt.

## F5 – Vorderer Abnäher (v. Abnäher)

- **Quelle:** [formeln_s033.md](formeln_s033.md), Abschnitt „Tabelle 3 – Abstiche und Abnäher", Zeile 2.
- **Buchfassung:**
  ```text
  v. Abnäher | 0 oder 1,5 bis 2,5 | 2,5
  ```
- **Technische Formel:** `v.Abnäher ∈ {0} ∪ [1,5; 2,5]`.
- **Eingaben und Einheiten:** keine (fachliche Auswahl, kein Rechenwert).
- **Ausgabe und Einheit:** `v.Abnäher` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Auswahl zwischen `0` (kein Abnäher) oder Bereich `[1,5; 2,5]` cm. Beispielwert `2,5` = oberes Bereichsende. Keine Buchregel, wann `0` statt des Bereichs gewählt wird.
- **Abhängigkeiten:** Eingabe für F8 (Kontrolle).
- **Status:** normalisiert (Bereich fototreu erfasst).
- **Offene Fragen:** fachliche Auswahlregel zwischen `0` und Bereich fehlt.

## F6 – Erster hinterer Abnäher (1.h. Abnäher)

- **Quelle:** [formeln_s033.md](formeln_s033.md), Abschnitt „Tabelle 3 – Abstiche und Abnäher", Zeile 3.
- **Buchfassung:**
  ```text
  1.h. Abnäher | bis 4,5 | 4
  ```
- **Technische Formel:** `1.h.Abnäher ≤ 4,5`.
- **Eingaben und Einheiten:** keine (fachliche Auswahl).
- **Ausgabe und Einheit:** `1.h.Abnäher` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** oberer Grenzwert `4,5` cm; unterer Grenzwert im Buch nicht genannt. Beispielwert `4`.
- **Abhängigkeiten:** Eingabe für F8 (Kontrolle).
- **Status:** normalisiert (Bereich fototreu erfasst, oberer Grenzwert eindeutig).
- **Offene Fragen:** unterer Grenzwert des Bereichs fehlt im Buch.

## F7 – Zweiter hinterer Abnäher (2.h. Abnäher)

- **Quelle:** [formeln_s033.md](formeln_s033.md), Abschnitt „Tabelle 3 – Abstiche und Abnäher", Zeile 4.
- **Buchfassung:**
  ```text
  2.h. Abnäher | optional | ---
  ```
- **Technische Formel:** keine feste Formel; `optional`, im Beispiel kein Wert eingetragen.
- **Eingaben und Einheiten:** keine.
- **Ausgabe und Einheit:** `2.h.Abnäher` (cm), im Beispiel nicht verwendet.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** rein optional, keine Wertegrenzen im Buch angegeben.
- **Abhängigkeiten:** Eingabe für F8 (Kontrolle), dort im Beispiel als `0` behandelt.
- **Status:** offen. Kein Wertebereich im Buch angegeben.
- **Offene Fragen:** Wertebereich und Auswahlbedingung für den optionalen zweiten hinteren Abnäher fehlen vollständig.

## F8 – Kontrolle (Σ = TaAf)

- **Quelle:** [formeln_s033.md](formeln_s033.md), Abschnitt „Tabelle 3 – Abstiche und Abnäher", Zeile 5.
- **Buchfassung:**
  ```text
  Kontrolle: | Σ = TaAf | 13
  ```
- **Technische Formel:** `Hüftabstich + v.Abnäher + 1.h.Abnäher + 2.h.Abnäher = TaAf`.
- **Eingaben und Einheiten:** `Hüftabstich` (F4), `v.Abnäher` (F5), `1.h.Abnäher` (F6), `2.h.Abnäher` (F7) — alle cm.
- **Ausgabe und Einheit:** Kontrollsumme gegen `TaAf` (cm, aus F3).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine eigene; die Kontrollgleichung schränkt die gewählten Werte aus F4–F7 faktisch aufeinander ein.
- **Abhängigkeiten:** F3, F4, F5, F6, F7 → F8.
- **Status:** normalisiert. Rechenbeispiel geprüft: `6,5 + 2,5 + 4 + 0 = 13`, mit `2.h.Abnäher = 0` — stimmt mit dem gedruckten `13` überein.
- **Offene Fragen:** Das Buch nennt keine Rechenregel, wie die Bereichswerte aus F4–F6 im Einzelfall so gewählt werden, dass die Summe exakt `TaAf` ergibt.

## F9 – Grundgerüst-Punktkonstruktion

- **Quelle:** [formeln_s033.md](formeln_s033.md), Abschnitt „Grundgerüst-Konstruktion (Text, zeichnungsgebunden)"; zeichnungsgebunden über [skizzen/s033_skizze_01.png](skizzen/s033_skizze_01.png).
- **Buchfassung:**
  ```text
  1 (□3) P1 ist links oben am Blattrand.
  Von P1 die Modelllänge (MoL) als eine Senkrechte nach unten zeichnen → vordere Mitte (vM).
  Am unteren Ende ist P2.
  Von P1 nach rechts die Taillenlinie abwinkeln (rechtwinklig eine Linie zeichnen).
  Von P2 nach rechts die Saumlinie abwinkeln.
  Von P1 nach unten die Hüfttiefe (HüT) abtragen → P3 und nach rechts die Hüftlinie abwinkeln.
  Auf der Taillenlinie von P1 die halbe Hüftweite (aus dem Maßsatz) abtragen → P4.
  Auf der Saumlinie nach rechts ebenfalls ½ HüW abtragen → P5.
  P4 und P5 verbinden → hintere Mitte (hM).

  6 P6 ist der Schnittpunkt mit der Hüftlinie.
  Die Taillenlinie halbieren → P7.
  Die Saumlinie halbieren → P8. P7 und P8 verbinden → Seitenlinie.
  P9 ist der Schnittpunkt von Seitenlinie und Hüftlinie.
  ```
- **Technische Formel** (P1 als Ursprung `(0,0)`, x nach rechts, y nach unten):
  ```text
  P1 = (0, 0)
  P2 = P1 + (0, MoL)                        # vM = Strecke P1–P2
  Taillenlinie = Gerade durch P1, rechtwinklig zu vM
  Saumlinie    = Gerade durch P2, rechtwinklig zu vM
  P3 = P1 + (0, HüT)
  Hüftlinie = Gerade durch P3, parallel zu Taillenlinie/Saumlinie
  P4 = P1 + (½HüW, 0)                       # auf Taillenlinie
  P5 = P2 + (½HüW, 0)                       # auf Saumlinie
  hM = Strecke P4–P5
  P6 = Schnittpunkt(hM, Hüftlinie)
  P7 = Mittelpunkt(P1, P4)                  # Taillenlinie halbiert
  P8 = Mittelpunkt(P2, P5)                  # Saumlinie halbiert
  Seitenlinie = Strecke P7–P8
  P9 = Schnittpunkt(Seitenlinie, Hüftlinie)
  ```
- **Eingaben und Einheiten:** `MoL` (Modelllänge, cm, Tabelle 2); `HüT` (Hüfttiefe, cm, Tabelle 2); `½HüW` (cm, aus F1).
- **Ausgabe und Einheit:** Punkte `P1`–`P9` und Linien `vM`, `Taillenlinie`, `Saumlinie`, `Hüftlinie`, `hM`, `Seitenlinie` als Koordinaten/Strecken (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; feste geometrische Konstruktion.
- **Abhängigkeiten:** F1 (½HüW); Tabelle 2 (MoL, HüT).
- **Status:** normalisiert. Konstruktionsschritte sind eindeutig aus dem Text ableitbar.
- **Offene Fragen:** Der Text sagt bei P5 „Auf der Saumlinie nach rechts ebenfalls ½ HüW abtragen", ohne den Ausgangspunkt erneut zu nennen; hier als Fortsetzung von P2 gelesen, da die Saumlinie von P2 ausgeht. Bei einem späteren Codevertrag gegen die Zeichnung gegenprüfen.
