# Formeln s171 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s171.md`](formeln_s171.md) vermerkt, ist außer der
Schreibweise `HüU` keine Stelle dieser Seite von Werner am Original bestätigt.
Alle zehn Formeln stehen deshalb auf `offen`, unabhängig von der inhaltlichen
Klarheit der Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz
für die Bestätigung. Bekannte Abkürzungen (`HüU`, `SiH`, `TaW`, `SaW`, `Stb`)
sind bereits in `000_sprache/20_symbole_abkuerzungen/` geführt und werden hier
nur referenziert, nicht neu festgelegt.

## Formel A – Taillenweite/Hüftumfang-Mindestbezug

- **Quelle:** [`formeln_s171.md`](formeln_s171.md), Abschnitt A
- **Buchfassung:**
  ```text
  gewünschte ½ TaW = mind. ¼ HüU
  ```
- **Technische Formel:**
  ```text
  0,5 * TaW_gewuenscht ≥ 0,25 * HüU
  ```
- **Eingaben und Einheiten:** `TaW_gewuenscht` (cm, gewünschte Taillenweite),
  `HüU` (cm, Hüftumfang; siehe `02_zzb_abkuerzungen_koerpermasse_konstruktionsmasse.md`).
- **Ausgabe und Einheit:** Prüfergebnis (erfüllt/nicht erfüllt) für die halbe
  gewünschte Taillenweite, keine eigenständige Ausgabegröße.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Buchwortlaut nutzt „="
  zusammen mit „mind." (mindestens) – widersprüchlich, ob eine Gleichheit oder
  eine Untergrenze gemeint ist. Als Bereich mit Untergrenze erhalten, kein
  fester Wert gewählt.
- **Abhängigkeiten:** keine weiteren auf dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite außer der Schreibweise `HüU` ist von Werner am
    Original bestätigt.
  - „=" und „mind." widersprechen sich wörtlich; unklar, ob eine echte
    Gleichung oder eine Mindestbedingung gemeint ist.

## Formel B – Saumweite, halbe

- **Quelle:** [`formeln_s171.md`](formeln_s171.md), Abschnitt B
- **Buchfassung:**
  ```text
  ½ gewünschte SaW
  ```
- **Technische Formel:**
  ```text
  SaW_halbe = 0,5 * SaW_gewuenscht
  ```
- **Eingaben und Einheiten:** `SaW_gewuenscht` (cm, gewünschte Saumweite;
  siehe `02_zzc_abkuerzungen_aus_formeln_band_1_geprueft_v1.md`).
- **Ausgabe und Einheit:** `SaW_halbe` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine erkennbar; reine
  Halbierung für die Halbschnitt-Darstellung.
- **Abhängigkeiten:** keine weiteren auf dieser Seite; Bezug zur Gesamtseite
  (allgemeines Schema) unklar, da kein Gleichheitszeichen oder Zielgröße im
  Buchtext steht.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ohne Gleichheitszeichen ist unklar, ob dies eine vollständige Formel oder
    nur eine Maßbeschriftung im Schema ist.

## Formel C – Bundweite-Mindestmaß

- **Quelle:** [`formeln_s171.md`](formeln_s171.md), Abschnitt C
- **Buchfassung:**
  ```text
  mind. ¼ HüU + 1 cm
  ```
- **Technische Formel:**
  ```text
  bundweite_halbschnitt ≥ 0,25 * HüU + 1 cm
  ```
- **Eingaben und Einheiten:** `HüU` (cm, Hüftumfang).
- **Ausgabe und Einheit:** `bundweite_halbschnitt` (cm), obere Breite des
  Hosenteils (☐7 VT+RT bzw. ☐8 VT) am Bund.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „mind." erhalten – keine
  Obergrenze im Buch angegeben.
- **Abhängigkeiten:** identischer Wortlaut auf ☐7 und ☐8 (siehe
  [[Formel D]], [[Formel G]], [[Formel H]] – gleiche Zeichnungen).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt außer der Schreibweise `HüU` ist von Werner am Original
    bestätigt.
  - Unklar, ob sich das Maß auf den Halbschnitt (wie abgebildet) oder den
    vollen Umfang bezieht; aus der Zeichnung (Halbschnitt mit `Stb`) plausibel,
    aber nicht im Buchtext ausdrücklich benannt.

## Formel D – Hosenlänge mit optionaler Rafflänge

- **Quelle:** [`formeln_s171.md`](formeln_s171.md), Abschnitt D
- **Buchfassung:**
  ```text
  gewünschte Hosenlänge, ggf. + Rafflänge
  ```
- **Technische Formel:**
  ```text
  hosenlaenge_schnitt = Hosenlaenge_gewuenscht + (Rafflaenge, falls vorhanden)
  ```
- **Eingaben und Einheiten:** `Hosenlaenge_gewuenscht` (cm); `Rafflaenge` (cm,
  optional, nur falls die Hose am Saum gerafft/gebunden wird, siehe
  Fließtext „Der Saum wird mit einer Kordel gerafft und über der Wade oder am
  Fußgelenk gebunden").
- **Ausgabe und Einheit:** `hosenlaenge_schnitt` (cm), SN-Länge des Schnittteils.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ggf.` (gegebenenfalls)
  erhalten – Zuschlag nur bei geraffter Ausführung, kein fester Betrag im
  Buch angegeben.
- **Abhängigkeiten:** identischer Wortlaut auf ☐7 und ☐8; Rafflänge selbst ist
  auf dieser Seite nicht beziffert.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Betrag der „Rafflänge" nicht auf dieser Seite angegeben.

## Formel E – Seitenhöhe am Zwickel/Schlitz (nur ☐7)

- **Quelle:** [`formeln_s171.md`](formeln_s171.md), Abschnitt E
- **Buchfassung:**
  ```text
  SiH + ca. 6 bis 12 cm
  ```
- **Technische Formel:**
  ```text
  hoehe_seite = SiH + delta
  delta ∈ [ca. 6 cm, ca. 12 cm]
  ```
- **Eingaben und Einheiten:** `SiH` (cm, Sitzhöhe; siehe
  `02_zzb_abkuerzungen_koerpermasse_konstruktionsmasse.md`).
- **Ausgabe und Einheit:** `hoehe_seite` (cm), Höhe der markierten Strecke an
  der rechten Seite von ☐7.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „6 bis 12 cm"
  bleibt Bereich, kein fester Default gewählt.
- **Abhängigkeiten:** [[Formel F]] (gleiche Zeichnung, angrenzendes Dreieck).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nur zeichnungsgebunden, kein Beleg im Fließtext.

## Formel F – Zwickelbreite am Bein (nur ☐7)

- **Quelle:** [`formeln_s171.md`](formeln_s171.md), Abschnitt F
- **Buchfassung:**
  ```text
  ⅛ HüU + 2 bis 3 cm
  ```
- **Technische Formel:**
  ```text
  breite_zwickel = 0,125 * HüU + delta
  delta ∈ [2 cm, 3 cm]
  ```
- **Eingaben und Einheiten:** `HüU` (cm, Hüftumfang).
- **Ausgabe und Einheit:** `breite_zwickel` (cm), Basisbreite des kleinen
  Dreiecks zwischen den beiden `Stb`-Linien.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „2 bis 3 cm"
  bleibt Bereich, kein fester Default gewählt; kein „ca." vor dem Bereich
  (anders als bei Formel E).
- **Abhängigkeiten:** [[Formel E]] (gleiche Zeichnung).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nur zeichnungsgebunden, kein Beleg im Fließtext.
  - Bezug des Dreiecks zur restlichen Konstruktion (Zwickel vs. Beinabschluss)
    nicht in Textform erläutert.

## Formel G – Seitliche Erweiterung, Höhe (☐8 VT und RT)

- **Quelle:** [`formeln_s171.md`](formeln_s171.md), Abschnitt G
- **Buchfassung:**
  ```text
  ca. 6 bis 12 cm
  ```
- **Technische Formel:**
  ```text
  erweiterung_hoehe ∈ [ca. 6 cm, ca. 12 cm]
  ```
- **Eingaben und Einheiten:** keine Bezugsgröße angegeben; absoluter Bereich.
- **Ausgabe und Einheit:** `erweiterung_hoehe` (cm), vertikale Ausdehnung der
  seitlichen Erweiterung auf VT und RT von ☐8.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich bleibt Bereich.
  Identischer Wert auf VT und RT eingezeichnet.
- **Abhängigkeiten:** [[Formel C]] (gleiche Zeichnung ☐8), [[Formel H]]
  (angrenzendes Maß an derselben Seitenlinie).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nur zeichnungsgebunden, kein Beleg im Fließtext.
  - Bezugsbasis des Maßes (z. B. ab welchem Punkt gemessen) nicht benannt.

## Formel H – Seitliche Erweiterung, Tiefe (☐8 VT und RT)

- **Quelle:** [`formeln_s171.md`](formeln_s171.md), Abschnitt H
- **Buchfassung:**
  ```text
  ca. 3 bis 6 cm
  ```
- **Technische Formel:**
  ```text
  erweiterung_tiefe ∈ [ca. 3 cm, ca. 6 cm]
  ```
- **Eingaben und Einheiten:** keine Bezugsgröße angegeben; absoluter Bereich.
- **Ausgabe und Einheit:** `erweiterung_tiefe` (cm), horizontale Ausdehnung der
  seitlichen Erweiterung auf VT und RT von ☐8.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich bleibt Bereich.
  Identischer Wert auf VT und RT eingezeichnet.
- **Abhängigkeiten:** [[Formel G]] (gleiche Zeichnung, gleiche Stelle).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nur zeichnungsgebunden, kein Beleg im Fließtext.

## Formel I – Zusätzliche Saumweite, Vorderteil (nur ☐8 VT)

- **Quelle:** [`formeln_s171.md`](formeln_s171.md), Abschnitt I
- **Buchfassung:**
  ```text
  ½ zusätzliche SaW
  ```
- **Technische Formel:**
  ```text
  zusatz_saum_vt = 0,5 * SaW_zusatz
  ```
- **Eingaben und Einheiten:** `SaW_zusatz` (cm, zusätzliche/erweiterte
  Saumweite gegenüber dem Standard-Hosengrundschnitt).
- **Ausgabe und Einheit:** `zusatz_saum_vt` (cm), am Saum des Vorderteils
  zuzugebende Weite.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Zahlenwert für
  `SaW_zusatz` selbst auf dieser Seite angegeben.
- **Abhängigkeiten:** [[Formel J]] (gleiche Logik am Rückteil, andere
  Anteilsgröße ¼ statt ½).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nur zeichnungsgebunden, kein Beleg im Fließtext.
  - Warum VT ½ und RT ¼ der zusätzlichen Saumweite erhält (statt je ½ oder je
    ¼), ist aus dem Bild allein nicht begründet.

## Formel J – Zusätzliche Saumweite, Rückteil (nur ☐8 RT)

- **Quelle:** [`formeln_s171.md`](formeln_s171.md), Abschnitt J
- **Buchfassung:**
  ```text
  ¼ zusätzliche SaW
  ```
- **Technische Formel:**
  ```text
  zusatz_saum_rt = 0,25 * SaW_zusatz
  ```
- **Eingaben und Einheiten:** `SaW_zusatz` (cm, wie Formel I).
- **Ausgabe und Einheit:** `zusatz_saum_rt` (cm), am Saum des Rückteils
  zuzugebende Weite.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein Zahlenwert für
  `SaW_zusatz` selbst auf dieser Seite angegeben.
- **Abhängigkeiten:** [[Formel I]] (gleiche Logik am Vorderteil, andere
  Anteilsgröße ½ statt ¼); zusammen ergeben VT- und RT-Anteil ¾ statt eines
  vollen Bezugs – siehe offene Frage.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Nur zeichnungsgebunden, kein Beleg im Fließtext.
  - ½ (VT) + ¼ (RT) ergibt ¾ von `SaW_zusatz`, nicht die vollen 1 (bzw. ½ je
    Halbschnittseite); ob ein vierter Anteil an anderer Stelle (z. B. Zwickel)
    verplant ist, ist auf dieser Seite nicht erkennbar.
