# Formeln s176 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s176.md`](formeln_s176.md) vermerkt, ist von
dieser Seite bisher nur die Spaltenfolge und Gruppenüberschrift von Tabelle 2
bestätigt; alle Zahlenwerte bleiben unbestätigt. Alle vier Formeln stehen
deshalb auf `offen`. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für
die Bestätigung.

## Formel 1 – Rechenbeispiel PK5 (BrW-Zugabe)

- **Quelle:** [`formeln_s176.md`](formeln_s176.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Die Ziffern einer Passformklasse (PK) geben die jeweilige die Zugabe für den halben Brustumfang an; hier z.B. für eine enge Jacke:

  PK5 2 × 5 cm = 10 cm BrW-Zugabe
  ```
- **Technische Formel:**
  ```text
  BrW_Zugabe_Beispiel = PK_ziffer_faktor × 5 cm
  mit PK_ziffer_faktor = 2 (für PK5, unbenannter Faktor im Beispiel)
  ```
  Beobachtung (nicht als allgemeine Buchregel behauptet): Für alle Zeilen in
  Tabelle 2 (Formel 3) gilt `BrU-Spalte = 2 × Passformklasse`, was mit diesem
  Beispiel (2 × 5 = 10 für PK5) übereinstimmt. Nur ein Beispiel im Fließtext
  belegt, keine explizite allgemeine Formel im Buchtext gefunden.
- **Eingaben und Einheiten:** Passformklasse (dimensionslos, hier 5); Faktor
  „2" (Herkunft/Einheit im Buchtext nicht benannt).
- **Ausgabe und Einheit:** BrW-Zugabe = 10 cm (für PK5, laut Beispiel).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Bereichsangabe im
  Beispiel; fester Beispielwert für PK5.
- **Abhängigkeiten:** [[Formel 3]] (Tabelle 2, BrU-Spalte, Zeile PK5 = 10,
  deckungsgleich mit diesem Rechenbeispiel).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Widerspruch: Fließtext nennt „Zugabe für den halben Brustumfang", der
    identische Wert 10 cm steht in Tabelle 2 aber in der Spaltengruppe
    „Zugaben (für den ganzen Schnitt)" (OCR-Rohüberschrift). Nicht aufgelöst.
  - Ob der Faktor „2" allgemein (für jede PK) oder nur im Beispiel gilt, ist
    aus dem Buchtext selbst nicht ausdrücklich als Regel formuliert.

## Formel 2 – Auswahltabelle Passformklasse → Anwendung/Modelle

- **Quelle:** [`formeln_s176.md`](formeln_s176.md), Abschnitt 2
- **Buchfassung:** siehe Tabelle 1 in `formeln_s176.md`, Abschnitt 2
  (unverändert aus `tabellen_s176.md` zitiert).
- **Technische Formel:**
  ```text
  Anwendung(PK), Modell_Woche_Kleid_Bluse(PK), Modell_Jacke(PK), Modell_Weste_Mantel(PK)
  = Nachschlagewerte aus Tabelle 1, Zeile PK (PK ∈ {0..10})
  ```
- **Eingaben und Einheiten:** Passformklasse PK (ganzzahlig, 0–10).
- **Ausgabe und Einheit:** Textkategorien (Anwendung, Modellbezeichnungen je
  Sparte); keine physikalische Einheit.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Zeilen PK 1, 2, 4, 6, 8,
  10 sind in der OCR-Rohfassung leer; vermutlich (nicht bestätigt) gilt für
  diese die Anwendung/Modelle der jeweils vorherigen benannten Zeile
  (verbundene Zellen im Original).
- **Abhängigkeiten:** keine zu anderen Formeln dieser Seite; ggf. Bezug zu
  Modellseiten anderer Kategorien (nicht ermittelt).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Leerzeilen-Interpretation (verbundene Zellen) ist unbestätigte Vermutung
    aus `s176.md`, Prüfstelle 6.
  - OCR-Wortlaute „Rademoden"/„Grund, Nieder" wahrscheinlich fehlerhaft
    (vermutlich „Bademoden"/„Dirndl, Mieder"), am Original zu prüfen.

## Formel 3 – Zugabentabelle (Passformklasse → Zugabenwerte)

- **Quelle:** [`formeln_s176.md`](formeln_s176.md), Abschnitt 3
- **Buchfassung:** siehe Tabelle 2 in `formeln_s176.md`, Abschnitt 3
  (Rohzitat plus bestätigte Spaltenkorrektur).
- **Technische Formel:**
  ```text
  Eingabe: Passformklasse PK ∈ {0..10}
  Ausgabe (cm), Spalten in bestätigter Reihenfolge:
    BrU(PK), TaU(PK), HüU(PK), AlT(PK), RüB(PK), ArD(PK), BrB(PK), SuB(PK)
    = Nachschlagewerte aus Tabelle 2, Zeile PK
  Beobachtung: BrU(PK) = 2 × PK (siehe Formel 1)
  ```
- **Eingaben und Einheiten:** Passformklasse PK (ganzzahlig, 0–10).
- **Ausgabe und Einheit:** acht Zugabewerte in cm je PK; mehrere Spalten
  (TaU, HüU teils, AlT teils) sind im Buch als Bereich („4 - 6" etc.) statt
  Einzelwert angegeben.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereiche bleiben
  Bereiche (z.B. TaU bei PK5: „8 - 12"); kein fester Wert oder Default gewählt.
  AlT bei PK0 „0 - 0,5", BrB bei PK0 „0 - 0,4" ebenfalls Bereiche.
- **Abhängigkeiten:** [[Formel 1]] (BrU-Spalte deckt sich mit Rechenbeispiel
  PK5); [[Formel 4]] (Piktogramm-Beispiel PK5, Zugabewerte 10/10/7 liegen in
  bzw. an den Grenzen der PK5-Zeile: BrU=10 exakt, TaU=8–12 enthält 10,
  HüU=6–8 enthält 7 — als Beobachtung, nicht als Bestätigung).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Zahlenwert dieser Tabelle ist von Werner am Original bestätigt; nur
    die Spaltenbezeichnungen selbst sind bestätigt.
  - Bedeutung der Spalte „AlT" (vermutlich Armlochtiefe, Abkürzung nicht
    aufgelöst) und „SuB" (Bedeutung nicht ermittelt) offen.
  - Warum die zweite Spaltengruppen-Überschrift „BrW-Zugaben (für ½ Schnitt)"
    lautet, obwohl sie laut bestätigter Spaltenfolge auch RüB, ArD, BrB, SuB
    umfasst (nicht nur BrW/BrU), ist ungeklärt.

## Formel 4 – Piktogramm-Beispiel Größe 38, PK5 (zeichnungsgebunden)

- **Quelle:** [`formeln_s176.md`](formeln_s176.md), Abschnitt 4
- **Buchfassung:** siehe Zitate in `formeln_s176.md`, Abschnitt 4
  (Bildbeschreibung, Bildunterschrift ☐1, Ziffernlegende 2–8).
- **Technische Formel:**
  ```text
  Körpermaße (Größe 38): KöH=168 cm, BrU=88 cm, TaU=72 cm, HüU=97 cm  [Ziffern 2-5, Lesart]
  Zugabewerte (PK5, enge Jacke): BrU-Zugabe=10 cm, TaU-Zugabe=10 cm, HüU-Zugabe=7 cm  [Ziffern 6-8, Lesart]
  vierter Wert "5" nicht eindeutig zugeordnet (evtl. PK-Kennzahl statt Zugabewert)
  ```
- **Eingaben und Einheiten:** Körpermaße in cm (KöH, BrU, TaU, HüU).
- **Ausgabe und Einheit:** Zugabewerte in cm (BrU, TaU, HüU laut Legende).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; Einzelbeispiel
  für eine konkrete Größe (38) und Passformklasse (PK5).
- **Abhängigkeiten:** [[Formel 3]] (Zugabewerte liegen konsistent in bzw. an
  den Grenzen der PK5-Zeile von Tabelle 2 — Beobachtung, keine Bestätigung).
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Zuordnung der vier Zahlen 168/88/72/97 und der vier Werte 5/10/10/7 zu den
    Ziffern 1–8 stammt allein aus einer Bildbeschreibung, nicht aus eigener
    Bildprüfung; Status `gesperrt`, bis das Original bzw. der Skizzenausschnitt
    `skizzen/s176_skizze_01.png` regulär (Prüfstelle 5 in `s176.md`) bestätigt
    ist.
  - Vier Zugabewerte stehen drei benannten Zugabe-Ziffern (6, 7, 8) gegenüber;
    ungeklärt, welcher Wert entfällt oder ob eine vierte Zugabeziffer fehlt.
