# Formeln s091 – Normalisierung (teils Walking Skeleton)

**Achtung:** Wie in [`formeln_s091.md`](formeln_s091.md) vermerkt, ist nur
Formel 6 (`SaW`) von Werner am Original bestätigt. Die Formeln 1–5 stammen aus
derselben Zeichnung, sind aber nicht bestätigt und stehen deshalb auf `offen` –
unabhängig davon, dass sie sich intern widerspruchsfrei nachrechnen lassen.
Formel 6 erhält `normalisiert`, weil ihre Buchfassung ausdrücklich von Werner
bestätigt wurde. Dies ist im Übrigen ein Walking-Skeleton-Durchlauf, kein
Ersatz für die noch fehlende Bestätigung der Formeln 1–5.

## Formel 1 – Innerer Umfang (Definition)

- **Quelle:** [`formeln_s091.md`](formeln_s091.md), Abschnitt 1
- **Buchfassung:**
  ```text
  innerer Umfang = ¼ Ansatzweite (AnW) + 2× NZg
  ```
- **Technische Formel:**
  ```text
  u_innen = AnW / 4 + 2 * NZg
  ```
- **Eingaben und Einheiten:** `AnW` (cm, Ansatzweite), `NZg` (cm,
  Nahtzugabe je Kante).
- **Ausgabe und Einheit:** `u_innen` (cm), innerer Kreisumfang.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; reine Definition.
- **Abhängigkeiten:** [[Formel 3]] (`NZg`), [[Formel 4]] (verwendet `AnW` und
  `NZg` in gleicher Rolle, aber andere Rechenrichtung).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht von Werner am Original bestätigt.
  - Bezug „¼“ zur Viertelkreis-Konstruktion (Punkte 2, 3, 4) plausibel, aber
    nicht als eigene Buchaussage geprüft.

## Formel 2 – Äußerer Umfang (Definition)

- **Quelle:** [`formeln_s091.md`](formeln_s091.md), Abschnitt 2
- **Buchfassung:**
  ```text
  äußerer Umfang = ¼ Saumweite (SaW) + 2× NZg
  ```
- **Technische Formel:**
  ```text
  u_aussen = SaW / 4 + 2 * NZg
  ```
- **Eingaben und Einheiten:** `SaW` (cm, Saumweite), `NZg` (cm, Nahtzugabe je
  Kante).
- **Ausgabe und Einheit:** `u_aussen` (cm), äußerer Kreisumfang.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; reine Definition.
- **Abhängigkeiten:** [[Formel 3]] (`NZg`), [[Formel 6]] (`SaW`, dort jedoch als
  Ergebnis einer anderen Rechnung ermittelt, nicht aus `u_aussen` rückgerechnet).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht von Werner am Original bestätigt.
  - Verhältnis dieser Definition zu Formel 6 (`SaW`-Berechnung über `r_SaW`)
    nicht als zusammenhängende Herleitung im Buch belegt, nur als zwei
    getrennt stehende Bildbeschriftungen in derselben Berechnungsbox.

## Formel 3 – Nahtzugabe NZg

- **Quelle:** [`formeln_s091.md`](formeln_s091.md), Abschnitt 3
- **Buchfassung:**
  ```text
  NZg = 2 × 1 cm = 2 cm
  ```
- **Technische Formel:**
  ```text
  NZg = 2 * 1 cm = 2 cm
  ```
- **Eingaben und Einheiten:** fester Wert 1 cm je Kante.
- **Ausgabe und Einheit:** `NZg` (cm), Gesamt-Nahtzugabe.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Wert, kein
  Bereich, kein `ca.`.
- **Abhängigkeiten:** wird in [[Formel 1]], [[Formel 2]], [[Formel 4]] und
  [[Formel 6]] verwendet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht von Werner am Original bestätigt.

## Formel 4 – Radius r_AnW

- **Quelle:** [`formeln_s091.md`](formeln_s091.md), Abschnitt 4
- **Buchfassung:**
  ```text
  r_AnW = (AnW + NZg) : (2 · π)  : 4
        = (118 cm + 2 cm) : (2 · 3,14) : 4
        = 4,8 cm
  ```
- **Technische Formel:**
  ```text
  r_AnW = (AnW + NZg) / (2 * pi) / 4
  ```
- **Eingaben und Einheiten:** `AnW` = 118 cm (Ansatzweite, Beispielwert),
  `NZg` = 2 cm.
- **Ausgabe und Einheit:** `r_AnW` (cm), innerer Radius der Berechnungsbox.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; Buch verwendet
  hier `π ≈ 3,14` als gerundeten Wert.
- **Abhängigkeiten:** [[Formel 3]] (`NZg`); Ergebnis wird in [[Formel 5]]
  weiterverwendet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht von Werner am Original bestätigt.
  - Unabhängige Nachrechnung: (118 + 2) / (2 · 3,14) / 4 = 120 / 6,28 / 4 ≈
    19,108 / 4 ≈ 4,777 cm – stimmt mit dem gedruckten Ergebnis 4,8 cm überein
    (Rundung auf eine Nachkommastelle).
  - `AnW` = 118 cm ist auf dieser Seite nur als Zahl in der Rechnung sichtbar,
    keine Definition dieses Werts (z. B. als Körpermaß) auf s091 selbst
    gefunden.

## Formel 5 – Radius r_SaW

- **Quelle:** [`formeln_s091.md`](formeln_s091.md), Abschnitt 5
- **Buchfassung:**
  ```text
  r_SaW = r_AnW      + VoB
        = 4,8 cm      + 20 cm
        = 24,8 cm
  ```
- **Technische Formel:**
  ```text
  r_SaW = r_AnW + VoB
  ```
- **Eingaben und Einheiten:** `r_AnW` (cm, aus Formel 4), `VoB` = 20 cm
  (Volantbreite, Beispielwert).
- **Ausgabe und Einheit:** `r_SaW` (cm), äußerer Radius der Berechnungsbox.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; `VoB` als fester
  Beispielwert ohne erkennbaren Bereich auf dieser Seite.
- **Abhängigkeiten:** [[Formel 4]] (`r_AnW`); Ergebnis wird in [[Formel 6]]
  weiterverwendet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Nicht von Werner am Original bestätigt.
  - Nachrechnung stimmt: 4,8 + 20 = 24,8 cm.
  - Ob `VoB` = 20 cm ein festes Buchbeispiel oder ein frei wählbarer
    Modellwert ist, ist aus s091 allein nicht zu entscheiden.

## Formel 6 – Saumweite SaW

- **Quelle:** [`formeln_s091.md`](formeln_s091.md), Abschnitt 6; Werner-bestätigt
  am Original (siehe [s091.md](s091.md), Abschnitt „Vorab geklärte formel- und
  coderelevante Stellen“).
- **Buchfassung:**
  ```text
  SaW = ((2 × π × r_SaW) − NZg) × 4 = 615 cm
  ```
- **Technische Formel:**
  ```text
  SaW = ((2 * pi * r_SaW) - NZg) * 4
  ```
- **Eingaben und Einheiten:** `r_SaW` (cm, aus Formel 5), `NZg` (cm, aus
  Formel 3), Faktor 4 (Anzahl der Vollkreise/Volantteile lt. Bildunterschrift
  ☐3 „ein Volant aus vier Vollkreisen“).
- **Ausgabe und Einheit:** `SaW` (cm), Gesamt-Saumweite des Volants.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Beispielrechnung mit
  festen Zahlenwerten (`r_SaW` = 24,8 cm, `NZg` = 2 cm); Faktor 4 gilt
  ausdrücklich für die Variante „vier Vollkreise“, nicht allgemein für eine
  beliebige Glockenanzahl (Fließtext auf s091 nennt nur „Entsprechend der
  gewünschten Anzahl an Glocken …“, ohne diese Formel für andere Anzahlen zu
  wiederholen).
- **Abhängigkeiten:** [[Formel 5]] (`r_SaW`), [[Formel 3]] (`NZg`); Bezug zu
  [[Formel 2]] („äußerer Umfang“-Definition) inhaltlich naheliegend, aber nicht
  als durchgehende Herleitung im Buch belegt.
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:**
  - Unabhängige Nachrechnung: (2 · 3,14 · 24,8 − 2) · 4 = (155,744 − 2) · 4 =
    153,744 · 4 = 614,976 cm ≈ 615 cm – stimmt mit dem gedruckten Ergebnis
    überein (Rundung).
  - Die Klammerung des Faktors 4 ist im Foto der Berechnungsbox typografisch
    mehrdeutig (`· 4` steht direkt hinter `− NZg`, siehe Hinweis in
    [`formeln_s091.md`](formeln_s091.md), Abschnitt 6); die Nachrechnung stützt
    eindeutig die von Werner bestätigte Klammerung `((2πr_SaW) − NZg) × 4`, da
    nur diese Reihenfolge exakt 615 cm ergibt.
  - Nur diese eine Formel ist bestätigt; Formeln 1–5 (Eingabewerte und
    Zwischenschritte) bleiben `offen`.
