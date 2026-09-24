# Formeln s086 – Normalisierung (teilweise bestätigt, teilweise Walking Skeleton)

**Achtung:** Wie in [`formeln_s086.md`](formeln_s086.md) vermerkt, ist nur ein
Teil der Seite am Original bestätigt (Abschnitte 1–3 dort: Indizes `FaA_Hü`/
`FaA_Ta`, Relation `FaI = 2 × FaT` samt Gleichheitszeichen, die beiden
Divisionsergebnisse `≈ 4,55 cm`/`≈ 3,36 cm`). Alle übrigen
Formeln unten stammen ausschließlich aus der OCR-Rohfassung und stehen deshalb
auf `offen`, unabhängig von ihrer inhaltlichen Klarheit. Dies ist ein
Walking-Skeleton-Durchlauf auf ausdrücklichen Wunsch Werners
("formeln seite 86 überspringe die blocker. das ist ein walking skeleton."),
kein Ersatz für die noch ausstehende Bestätigung.

Die fototreuen Abschnitte 4 („1 Berechnungen" – Schrittliste) und 5
(Eingabewert `FaZ = 22`) aus [`formeln_s086.md`](formeln_s086.md) werden hier
nicht als eigene Formel geführt, sondern als Eingabe in den Formeln 1, 2 und 8
unten wiederverwendet.

## Formel 1 – Faltenabstand an der Hüfte (FaA_Hü)

- **Quelle:** [`formeln_s086.md`](formeln_s086.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Faltenabstand an der Hüfte (FaA_Hü)
  HüW : Faltenanzahl (FaZ)
  100 cm : 22
  ≈ 4,55 cm
  ```
- **Technische Formel:**
  ```text
  FaA_Hü = HüW / FaZ
  ```
- **Eingaben und Einheiten:** `HüW` = 100 cm, `FaZ` = 22 (dimensionslos,
  Anzahl Normalfalten an der Hüfte).
- **Ausgabe und Einheit:** `FaA_Hü` ≈ 4,55 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Ergebnis ist gerundet
  (Näherungszeichen „≈"); 100 / 22 = 4,5454… wird nicht als exakter Bruch
  geführt.
- **Abhängigkeiten:** `HüW` und `FaZ` sind allgemeine Größen aus der
  Konstruktionstabelle bzw. dem Modelltext ([[Formel 5]], [[Formel 8]] für
  weitere Verwendung von `FaZ`); [[Formel 2]] verwendet dieselbe Struktur für
  die Taille.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Bestätigt ist nur die konkrete Zahlenrelation `100 cm : 22 ≈ 4,55 cm`
    selbst (laut [s086.md](s086.md)); dass `HüW` und `FaZ` als
    wiederverwendbare Variablen mit denselben Werten auch anderswo auf der
    Seite gelten (z. B. in Formel 8), ist nicht gesondert bestätigt.

## Formel 2 – Faltenabstand an der Taille (FaA_Ta)

- **Quelle:** [`formeln_s086.md`](formeln_s086.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Faltenabstand an der Taille (FaA_Ta)
  TaW : Faltenanzahl (FaZ)
  74 cm : 22
  ≈ 3,36 cm
  ```
- **Technische Formel:**
  ```text
  FaA_Ta = TaW / FaZ
  ```
- **Eingaben und Einheiten:** `TaW` = 74 cm, `FaZ` = 22 (dimensionslos).
- **Ausgabe und Einheit:** `FaA_Ta` ≈ 3,36 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Ergebnis gerundet;
  74 / 22 = 3,3636… wird nicht als exakter Bruch geführt.
- **Abhängigkeiten:** [[Formel 1]] (gleiche Struktur, Hüfte statt Taille);
  `TaW` und `FaZ` aus Konstruktionstabelle bzw. Modelltext ([[Formel 6]],
  [[Formel 8]]).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Wie bei Formel 1: nur die konkrete Zahlenrelation ist bestätigt, nicht
    die allgemeine Wiederverwendbarkeit von `TaW`/`FaZ` als Tabellenvariablen.

## Formel 3 – Falteninhalt (FaI)

- **Quelle:** [`formeln_s086.md`](formeln_s086.md), Abschnitt 3
- **Buchfassung:**
  ```text
  4 Anschließend wird ein Falteninhalt (FaI = 2 × FaT) markiert.
  ```
- **Technische Formel:**
  ```text
  FaI = 2 * FaT
  ```
- **Eingaben und Einheiten:** `FaT` (cm), Faltentiefe an der Hüfte (auf
  dieser Seite nur als Beispielwert 9,2 cm in [[Formel 8]] belegt, sonst
  freier Eingabewert).
- **Ausgabe und Einheit:** `FaI` (cm), Falteninhalt.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; feste
  Verhältnisrelation.
- **Abhängigkeiten:** `FaT` als Eingabewert für [[Formel 8]] (ofW-Kontrolle,
  dort mit Beispielwert 9,2 cm).
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Die OCR-Rohzeile verwendet statt des am Original bestätigten
    Gleichheitszeichens ein Näherungszeichen (`FaI ≈ 2 × FaT`); die
    bestätigte Fassung mit `=` wird hier geführt.

## Formel 4 – Abnähtiefe der Falten unterhalb der Taille (Bereich)

- **Quelle:** [`formeln_s086.md`](formeln_s086.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Die Falten werden unterhalb der Taille ca. 12 bis 20 cm lang abgenäht.
  ```
- **Technische Formel:**
  ```text
  abnaehtiefe ∈ [ca. 12 cm, ca. 20 cm]
  ```
- **Eingaben und Einheiten:** keine (Bereichsangabe ohne weitere Eingabe).
- **Ausgabe und Einheit:** `abnaehtiefe` (cm), Länge des Abnähens unterhalb
  der Taille.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich bleibt Bereich,
  `ca.` erhalten; kein fester Wert oder Default im Buchtext.
- **Abhängigkeiten:** keine erkennbare Rechenverknüpfung zu anderen Formeln
  dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Unbestätigt (Walking Skeleton); keine Auswahlregel für einen konkreten
    Wert innerhalb des Bereichs im Buchtext erkennbar.

## Formel 5 – Hüftweite aus Hüftumfang und Zugabe (HÜW)

- **Quelle:** [`formeln_s086.md`](formeln_s086.md), Abschnitt 8, erste Zeile
- **Buchfassung:**
  ```text
  HÜU | Hüftumfang | 97 | +2,-3 | 3 = | Hüftweite | HÜW | 100 | ½ 50 | ¼ 25
  ```
- **Technische Formel:**
  ```text
  HÜW = HÜU + zugabe_gewaehlt
  zugabe_gewaehlt ∈ {+2 .. -3}, hier gewählt: 3
  halb_HÜW = HÜW / 2
  viertel_HÜW = HÜW / 4
  ```
- **Eingaben und Einheiten:** `HÜU` = 97 cm (Hüftumfang, Körpermaß);
  `zugabe_gewaehlt` = 3 cm (aus dem Zugabebereich `+2` bis `-3`).
- **Ausgabe und Einheit:** `HÜW` = 100 cm; `halb_HÜW` = 50 cm; `viertel_HÜW`
  = 25 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Zugabebereich `+2,-3`
  in der Tabellenzeile angegeben, gedruckt aber mit gewähltem Wert `3`
  aufgelöst (Endergebnis `100`); der Bereich selbst bleibt als Kontext
  erhalten, ohne dass hier eine eigene Auswahlregel für andere Größen
  dokumentiert ist.
- **Abhängigkeiten:** `HÜW` wird in [[Formel 1]] und [[Formel 8]] verwendet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Unbestätigt (Walking Skeleton); außerdem trägt die Tabellenkopfzeile laut
    [tabellen_s086.md](tabellen_s086.md) einen abweichenden, nicht
    aufgelösten Wortlaut („Proportionshemmelse" statt „Proportionsmaße").

## Formel 6 – Taillenweite aus Taillenumfang und Zugabe (TaW)

- **Quelle:** [`formeln_s086.md`](formeln_s086.md), Abschnitt 8, zweite Zeile
- **Buchfassung:**
  ```text
  TaU | Taillenumfang | 72 | +1,-2 | 2 = | Taillenweite | TaW | 74 | ½ 37 | ¼ 18,5
  ```
- **Technische Formel:**
  ```text
  TaW = TaU + zugabe_gewaehlt
  zugabe_gewaehlt ∈ {+1 .. -2}, hier gewählt: 2
  halb_TaW = TaW / 2
  viertel_TaW = TaW / 4
  ```
- **Eingaben und Einheiten:** `TaU` = 72 cm (Taillenumfang, Körpermaß);
  `zugabe_gewaehlt` = 2 cm (aus dem Zugabebereich `+1` bis `-2`).
- **Ausgabe und Einheit:** `TaW` = 74 cm; `halb_TaW` = 37 cm; `viertel_TaW`
  = 18,5 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** wie Formel 5, Bereich
  `+1,-2` mit gedrucktem gewähltem Wert `2` aufgelöst.
- **Abhängigkeiten:** `TaW` wird in [[Formel 2]] und [[Formel 7]] verwendet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Unbestätigt (Walking Skeleton); gleicher Tabellenkopf-Vorbehalt wie
    Formel 5.

## Formel 7 – Taillenausfall (TaAf)

- **Quelle:** [`formeln_s086.md`](formeln_s086.md), Abschnitt 8, dritte Zeile
- **Buchfassung:**
  ```text
  TaAf | Taillenausfall | ½ HÜW - ½ TaW = | | | | | | 13 | ½ 6,5
  ```
- **Technische Formel:**
  ```text
  TaAf = HÜW/2 - TaW/2
  halb_TaAf = TaAf / 2
  ```
- **Eingaben und Einheiten:** `HÜW` = 100 cm, `TaW` = 74 cm (aus [[Formel 5]]
  und [[Formel 6]]).
- **Ausgabe und Einheit:** `TaAf` = 13 cm; `halb_TaAf` = 6,5 cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; feste
  Rechenvorschrift. Rechnerisch nachvollzogen: 100/2 − 74/2 = 50 − 37 = 13 —
  stimmt mit dem gedruckten Ergebnis überein.
- **Abhängigkeiten:** [[Formel 5]], [[Formel 6]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Unbestätigt (Walking Skeleton), obwohl rechnerisch konsistent mit den
    Eingaben.

## Formel 8 – Kontrolle der offenen Weite (ofW)

- **Quelle:** [`formeln_s086.md`](formeln_s086.md), Abschnitt 7
- **Buchfassung:**
  ```text
  ### Kontrolle der offenen Weite
  ofW = FaZ · FaT · 2 + HüW
  = 22 · 9,2cm + 100cm
  = 302,4cm
  ```
- **Technische Formel:**
  ```text
  ofW = FaZ * FaT * 2 + HüW
  ```
- **Eingaben und Einheiten:** `FaZ` = 22 (dimensionslos, s. [[Formel 1]]);
  `FaT` = 9,2 cm (nur als Beispielwert in diesem Rechenbeispiel belegt);
  `HüW` = 100 cm (s. [[Formel 5]]).
- **Ausgabe und Einheit:** `ofW` = 302,4 cm (offene Weite).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; feste
  Kontrollformel. Rechnerisch nachvollzogen: 22 · 9,2 = 202,4;
  202,4 + 100 = 302,4 — stimmt mit dem gedruckten Ergebnis überein.
- **Abhängigkeiten:** [[Formel 1]] (`FaZ`), [[Formel 5]] (`HüW`); `FaT` ist
  auf dieser Seite sonst nicht als fester Wert definiert (vgl. [[Formel 3]]).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Unbestätigt (Walking Skeleton).
  - `FaT = 9,2 cm` ist nur aus diesem Rechenbeispiel ablesbar; kein anderer
    Buchsatz auf der Seite legt diesen Wert als Faltentiefe für das Modell
    fest.
