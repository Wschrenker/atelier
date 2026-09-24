# Formeln – s046 (normalisiert, technische Fassung)

Diese Fassung trennt die Buchformeln von `formeln_s046.md` (fototreu) von
einer technischen Lesart. **Von den fünf erfassten Stellen ist bisher nur ein
Teilstück von Formel 3 bestätigt** – der Wortlaut „bis ca. 4 cm unterhalb der
Hüftlinie" (siehe `s046.md`, Abschnitt „Vorab geklärte formel- und
coderelevante Stellen"). Alle übrigen Stellen und Teilstücke stehen auf
`offen`, bis Werner sie am Original geprüft hat.

## Formel 1 – Ausstellen: Grenzwert der Saumerweiterung

**Quelle:** [formeln_s046.md](formeln_s046.md), Abschnitt 1
(→ [ocr_s046.md](ocr_s046.md), Zeile 9).

**Buchfassung:**

```text
knielange Röcke: maximale Erweiterung = ca. 2,5 cm
kurze Röcke: weniger ausstellen (keine Zahl genannt)
lange Röcke: mehr ausstellen (keine Zahl genannt)
```

**Technische Formel:**

```text
max_ausstellung(rocklaenge = knielang) = ca. 2,5 cm
```

**Eingaben und Einheiten:** `rocklaenge` – Kategorie (kurz/knielang/lang),
keine Zahleneinheit; das Bezugsmaß `ca. 2,5 cm` gilt nur für „knielang".

**Ausgabe und Einheit:** `max_ausstellung` – oberer Grenzwert der
Saumerweiterung beim Ausstellen, cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** Für „kurz" gilt laut
Buchtext ein kleinerer, für „lang" ein größerer Grenzwert als 2,5 cm – ohne
konkrete Zahl oder Bereichsgrenze. Keine Buchregel, ab welcher Rocklänge
„kurz"/„knielang"/„lang" beginnt.

**Abhängigkeiten:** Betrifft dieselbe Konstruktion wie Formel 2 (Einstellen),
gegenläufige Richtung an derselben Seitennaht (SN).

**Status:** offen

**Offene Fragen:** Zahlenwerte für „kurz" und „lang" sowie die
Rocklängen-Grenzen selbst sind im Buchtext nicht genannt und müssen am
Original geprüft werden, ob sie an anderer Stelle des Kapitels stehen.

## Formel 2 – Einstellen: Grenzwert der Saumverringerung

**Quelle:** [formeln_s046.md](formeln_s046.md), Abschnitt 2
(→ [ocr_s046.md](ocr_s046.md), Zeile 13).

**Buchfassung:**

```text
Verringerung der Saumweite durch Einstellen: bis zu 1,5 cm, an beiden SN
```

**Technische Formel:**

```text
max_einstellung_je_SN <= ca. 1,5 cm   (Lesart A: Grenzwert gilt je Seitennaht)
```

**Eingaben und Einheiten:** keine Eingabegröße; `1,5 cm` ist der gedruckte
Grenzwert selbst.

**Ausgabe und Einheit:** `max_einstellung_je_SN` – oberer Grenzwert der
Saumverringerung, cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich `0` bis `ca.
1,5 cm` je Seitennaht, keine Buchregel zur Auswahl eines konkreten Werts
innerhalb dieses Bereichs.

**Abhängigkeiten:** Betrifft dieselbe Konstruktion wie Formel 1 (Ausstellen),
gegenläufige Richtung an derselben Seitennaht (SN).

**Status:** offen

**Offene Fragen:** Unklar, ob „bis zu 1,5 cm … an beiden SN" den Grenzwert je
Seitennaht (Lesart A, oben) oder als Summe über beide Seitennähte gemeinsam
meint (Lesart B: `max_einstellung_gesamt <= ca. 1,5 cm`, aufgeteilt auf zwei
Nähte). Beide Lesarten fototreu möglich, keine davon ausgewählt.

## Formel 3 – Konstruktion der eingestellten Seitennaht (SN)

**Quelle:** [formeln_s046.md](formeln_s046.md), Abschnitt 3
(→ [ocr_s046.md](ocr_s046.md), Zeile 15).

**Buchfassung:**

```text
eingestellte SN: zunächst ca. 4 cm senkrecht,
dann schräg bis ca. 4 cm unterhalb der Hüftlinie
```

**Technische Formel:**

```text
strecke_senkrecht = ca. 4 cm
punkt_schraeg_ende = hueftlinie - ca. 4 cm   (unterhalb der Hüftlinie)
```

**Eingaben und Einheiten:** `hueftlinie` – Bezugslinie aus dem
Grundschnitt (Lage nicht auf dieser Seite definiert, sondern auf einer
Vorseite des Grundschnitts).

**Ausgabe und Einheit:** zwei Streckenmaße entlang der eingestellten
Seitennaht, cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext
erkennbar; beide Maße sind mit „ca." versehen.

**Abhängigkeiten:** Baut auf der Lage der Hüftlinie aus dem
Rock-Grundschnitt einer Vorseite auf (hier nicht kopiert, nur referenziert).

**Status je Teil:**

- `strecke_senkrecht = ca. 4 cm` — offen (nicht bestätigt).
- `punkt_schraeg_ende = hueftlinie - ca. 4 cm` — Wortlaut „bis ca. 4 cm
  unterhalb der Hüftlinie" bestätigt (s046.md); die Einordnung als zweiter
  Teil derselben Konstruktionsstrecke ist damit noch nicht gesondert
  bestätigt.

**Status (gesamt):** offen

**Offene Fragen:** Lage der „Hüftlinie" auf dieser Seite nicht selbst
definiert; Verlinkung zur besitzenden Vorseite noch offen.

## Formel 4 – Hosenrock: Innenbeinteil-Breite (Auswahlregel)

**Quelle:** [formeln_s046.md](formeln_s046.md), Abschnitt 4
(→ [ocr_s046.md](ocr_s046.md), Zeilen 29–31, 35–37).

**Buchfassung:**

```text
Innenbeinteil-Breite abhängig von Rockweite und Figurtyp:
gerade Röcke + normale/flache Gesäßfigur -> schmaleres Innenbeinteil
weite Röcke + tiefes (nach hinten gewölbtes) Gesäß -> breiteres Innenbeinteil
```

**Technische Formel:** Keine Rechenbeziehung. Reine Richtungsregel ohne
Zahlenwerte:

```text
innenbeinteil_breite steigt mit rockweite und gesaesstiefe
```

**Eingaben und Einheiten:** `rockweite` (gerade/weit), `gesaessform`
(normal/flach/tief), keine Zahleneinheiten im Buchtext.

**Ausgabe und Einheit:** `innenbeinteil_breite` – relative Richtung
(schmaler/breiter), keine Einheit oder Zahl gedruckt.

**Bereiche, Bedingungen und Auswahlentscheidungen:** Zwei benannte
Extremfälle (schmales vs. breites Innenbeinteil); kein Zwischenbereich und
keine Zahl im Buchtext.

**Abhängigkeiten:** Setzt einen gewählten Rock-Grundschnitt (Rockweite)
voraus; siehe Hinweis auf der Seite, dass „verschiedene Rock-Grundschnitte
verwendet werden" können.

**Status:** offen

**Offene Fragen:** Keine Zahlenwerte oder Bereichsgrenzen für
„schmaler"/„breiter" im Buchtext; fachliche Auswahlregel muss noch
formalisiert werden.

## Formel 5 – Sitzhöhe (SIH), Messdefinition

**Quelle:** [formeln_s046.md](formeln_s046.md), Abschnitt 5
(→ [ocr_s046.md](ocr_s046.md), Zeilen 45, 49, 53).

**Buchfassung:**

```text
SIH (Sitzhöhe) = Maß von der Sitzfläche über die seitliche Hüftkurve
                 bis zur Unterkante des Taillenmaßbandes
Messgerät: Lotband
Wirkung einer Längenzugabe auf SIH: Naht im Schritt sitzt tiefer
```

**Technische Formel:** Keine Rechenbeziehung, sondern eine Messvorschrift am
Körper:

```text
SIH = Koerpermass(Sitzflaeche -> seitliche_Hueftkurve -> Taillenmassband_Unterkante)
```

**Eingaben und Einheiten:** direkt am Körper mit dem Lotband gemessen, cm
(kein Zahlenbeispiel im Buchtext).

**Ausgabe und Einheit:** `SIH` – Sitzhöhe, cm.

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buchtext;
Zugabe zur SIH wird nur qualitativ beschrieben („bewirkt, dass die Naht im
Schritt etwas tiefer sitzt"), ohne Zahl oder Formel.

**Abhängigkeiten:** Laut Buchtext Voraussetzung für die Konstruktion des
Innenbeinteils (Formel 4 und Folgeseiten dieses Kapitels, hier nicht
kopiert, nur referenziert).

**Status:** offen

**Offene Fragen:** Kein Zahlenbeispiel für SIH im Buchtext; Zugabewert für
„Längenzugabe" nicht genannt.

## Zusammenfassung

Fünf Stellen erfasst, keine davon vollständig fachlich bestätigt – nur ein
Teilwortlaut in Formel 3 ist am Original bestätigt (s046.md). Alle fünf
stehen auf `offen`: zwei reine Grenzwerte (Formel 1, 2) mit fehlenden
Zahlenwerten für Randfälle, eine zweigeteilte Konstruktionsstrecke (Formel 3)
mit gemischtem Bestätigungsstand, eine reine Richtungsregel ohne Zahlen
(Formel 4) und eine Messdefinition ohne Zahlenbeispiel (Formel 5). Für einen
späteren Codevertrag muss Werner mindestens die in den „Offene Fragen"
genannten Werte und Lesarten am Original klären.
