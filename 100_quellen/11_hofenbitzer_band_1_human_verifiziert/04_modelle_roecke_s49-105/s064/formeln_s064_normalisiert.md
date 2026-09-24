# Formeln s064 – Normalisierung

**Status der Seite:** OCR-Rohfassung, noch nicht menschlich verifiziert.
Normalisierung wie die Extraktion ohne Warten auf Bestätigung erstellt
("walking skeleton"); vorläufig, muss nach Werners Prüfung erneut
gegengelesen werden. Kein Eintrag ist reif für einen Codevertrag.

## F1 – Bahnenzahl-Verdopplung

- **Quelle:** [formeln_s064.md](formeln_s064.md), Abschnitt 1.
- **Buchfassung:**

```text
Es ergeben sich im halben Vorderrock und im halben Hinterrock jeweils die entsprechenden Schnittteile für den halben Rock, zusammen 3 bzw. 4 Bahnen, sowie für den ganzen Rock 6 bzw. 8 Bahnen.
```

- **Technische Formel:** `Bahnenzahl_ganz = 2 * Bahnenzahl_halb`
- **Eingaben und Einheiten:** `Bahnenzahl_halb` (Anzahl, dimensionslos) —
  gedruckt nur die zwei Fälle `3` (6-Bahnenrock) und `4` (8-Bahnenrock).
- **Ausgabe und Einheit:** `Bahnenzahl_ganz` (Anzahl, dimensionslos) — gedruckt
  `6` bzw. `8`.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Nur die zwei gedruckten
  Modellfälle belegt (6- und 8-Bahnenrock). Keine allgemeine Formel für andere
  Bahnenzahlen aus dem Text ableitbar; der Text erwähnt 10- und 12-Bahnenrock
  nur als Empfehlung ohne eigene Konstruktionsangabe auf dieser Seite.
- **Abhängigkeiten:** keine zu anderen Seiten.
- **Status:** normalisiert (für die zwei gedruckten Fälle).
- **Offene Fragen oder Widersprüche:** siehe [F5](#f5--widerspruch-bahnenzahl-im-halben-rock-vs-teilung-in-f4).

## F2a – Gleichteilung an Hüfte und Saum, 6-Bahnenrock (Text)

- **Quelle:** [formeln_s064.md](formeln_s064.md), Abschnitt 2 (nur im
  Skizzenausschnitt lesbar, nicht im OCR-Rohtext).
- **Buchfassung:**

```text
Die sechs Teilungsnähte unterteilen den Rock in sechs gleich breite Bahnen an der Hüfte und am Saum.
```

- **Technische Formel:** `Bahnbreite_Hüfte = Hüftweite / 6`,
  `Bahnbreite_Saum = Saumweite / 6`
- **Eingaben und Einheiten:** `Hüftweite` [cm], `Saumweite` [cm] (Begriffe aus
  Schritt 2 der Seite, dort nicht mit Zahlenwert belegt).
- **Ausgabe und Einheit:** `Bahnbreite_Hüfte` [cm], `Bahnbreite_Saum` [cm].
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine über "gleich breit"
  hinaus gedruckt.
- **Abhängigkeiten:** verwandt mit [F3a](#f3a--querschnitt-taillenumfang-gleichteilung-6-bahnenrock),
  die dieselbe Gleichteilungsidee an einer anders benannten Umfangsgröße
  zeigt (siehe [F5](#f5--widerspruch-bahnenzahl-im-halben-rock-vs-teilung-in-f4)
  und offene Frage unten).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Die Formel selbst ist eindeutig; als
  offen markiert, weil der zugrundeliegende Satz nicht im OCR-Rohtext,
  sondern nur im Skizzenausschnitt steht und noch nicht am Original bestätigt
  ist.

## F2b – Gleichteilung an Hüfte und Saum, 8-Bahnenrock (Text)

- **Quelle:** [formeln_s064.md](formeln_s064.md), Abschnitt 2
  (`ocr_s064.md`, Zeile 24).
- **Buchfassung:**

```text
Die acht Teilungsnähte unterteilen den Rock in acht gleich breite Schnittteile an der Hüfte und am Saum.
```

- **Technische Formel:** `Bahnbreite_Hüfte = Hüftweite / 8`,
  `Bahnbreite_Saum = Saumweite / 8`
- **Eingaben und Einheiten:** `Hüftweite` [cm], `Saumweite` [cm].
- **Ausgabe und Einheit:** `Bahnbreite_Hüfte` [cm], `Bahnbreite_Saum` [cm].
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine über "gleich breit"
  hinaus gedruckt.
- **Abhängigkeiten:** verwandt mit [F3b](#f3b--querschnitt-taillenumfang-gleichteilung-8-bahnenrock).
- **Status:** offen (analog zu F2a — Satz noch nicht am Original bestätigt;
  hier zusätzlich noch nicht durch Werner geprüft, da die ganze Seite offen
  ist).
- **Offene Fragen oder Widersprüche:** keine über den allgemeinen
  Verifikationsvorbehalt der Seite hinaus.

## F3a – Querschnitt Taillenumfang, Gleichteilung, 6-Bahnenrock

- **Quelle:** [formeln_s064.md](formeln_s064.md), Abschnitt 3, Feld ☐2.
- **Buchfassung:**

```text
☐2 Querschnitt (6-Bahnenrock): Taillenumfang in 6 gleiche Abschnitte geteilt, je 1/6
```

- **Technische Formel:** `Abschnittsbreite = Taillenumfang / 6`
- **Eingaben und Einheiten:** `Taillenumfang` [cm] (Beschriftung laut
  Zeichnung; kein Zahlenwert gedruckt).
- **Ausgabe und Einheit:** `Abschnittsbreite` [cm], 6 gleiche Abschnitte.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** siehe [F2a](#f2a--gleichteilung-an-hüfte-und-saum-6-bahnenrock-text)
  und offene Frage unten.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Die Zeichnung beschriftet den
  geteilten Umfang als `Taillenumfang`, während der zugehörige Text (F2a) von
  Gleichteilung "an der Hüfte und am Saum" spricht. Ob `Taillenumfang` in
  dieser Zeichnung dieselbe Größe wie `Hüftweite` meint oder eine eigene,
  hier nicht erklärte Bezugsgröße ist, ist auf dieser Seite nicht geklärt.

## F3b – Querschnitt Taillenumfang, Gleichteilung, 8-Bahnenrock

- **Quelle:** [formeln_s064.md](formeln_s064.md), Abschnitt 3, Feld ☐5.
- **Buchfassung:**

```text
☐5 Querschnitt (8-Bahnenrock): Taillenumfang in 8 gleiche Abschnitte geteilt, je 1/8
```

- **Technische Formel:** `Abschnittsbreite = Taillenumfang / 8`
- **Eingaben und Einheiten:** `Taillenumfang` [cm].
- **Ausgabe und Einheit:** `Abschnittsbreite` [cm], 8 gleiche Abschnitte.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** siehe [F2b](#f2b--gleichteilung-an-hüfte-und-saum-8-bahnenrock-text).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** wie bei [F3a](#f3a--querschnitt-taillenumfang-gleichteilung-6-bahnenrock)
  (Begriff `Taillenumfang` vs. `Hüfte`/`Saum`).

## F4a – ☐3 VT-Teilung, 6-Bahnenrock

- **Quelle:** [formeln_s064.md](formeln_s064.md), Abschnitt 4, Feld ☐3.
- **Buchfassung:**

```text
☐3 (6-Bahnenrock), VT: Teilung an Hüfte und Saum 1/3 (vM-seitig) zu 2/3 (SN-seitig)
```

- **Technische Formel:** `VT_Teil_vM = VT_Breite * 1/3`,
  `VT_Teil_SN = VT_Breite * 2/3` (gleiches Verhältnis an Hüftlinie und
  Saumlinie).
- **Eingaben und Einheiten:** `VT_Breite` [cm] an Hüfte bzw. Saum (aus dem
  Rock-Grundschnitt, nicht auf dieser Seite hergeleitet).
- **Ausgabe und Einheit:** `VT_Teil_vM` [cm], `VT_Teil_SN` [cm].
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine gedruckt.
- **Abhängigkeiten:** `VT_Breite` stammt aus dem Rock-Grundschnitt (andere
  Quelle, hier nicht verlinkt, da Seite unbekannt); siehe außerdem
  [F5](#f5--widerspruch-bahnenzahl-im-halben-rock-vs-teilung-in-f4).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** siehe F5.

## F4b – ☐3 RT-Teilung, 6-Bahnenrock

- **Quelle:** [formeln_s064.md](formeln_s064.md), Abschnitt 4, Feld ☐3.
- **Buchfassung:**

```text
☐3 (6-Bahnenrock), RT: Teilung an Hüfte und Saum 2/3 (SN-seitig) zu 1/3 (hM-seitig)
```

- **Technische Formel:** `RT_Teil_SN = RT_Breite * 2/3`,
  `RT_Teil_hM = RT_Breite * 1/3`
- **Eingaben und Einheiten:** `RT_Breite` [cm] an Hüfte bzw. Saum.
- **Ausgabe und Einheit:** `RT_Teil_SN` [cm], `RT_Teil_hM` [cm].
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine gedruckt.
- **Abhängigkeiten:** `RT_Breite` aus dem Rock-Grundschnitt; siehe F5.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** siehe F5.

## F4c – ☐6 VT-Teilung, 8-Bahnenrock

- **Quelle:** [formeln_s064.md](formeln_s064.md), Abschnitt 4, Feld ☐6.
- **Buchfassung:**

```text
☐6 (8-Bahnenrock), VT: Teilung an Hüfte und Saum 1/2 zu 1/2
```

- **Technische Formel:** `VT_Teil_1 = VT_Breite * 1/2`,
  `VT_Teil_2 = VT_Breite * 1/2`
- **Eingaben und Einheiten:** `VT_Breite` [cm] an Hüfte bzw. Saum.
- **Ausgabe und Einheit:** `VT_Teil_1` [cm], `VT_Teil_2` [cm].
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine gedruckt.
- **Abhängigkeiten:** `VT_Breite` aus dem Rock-Grundschnitt.
- **Status:** offen (Seite noch nicht verifiziert).
- **Offene Fragen oder Widersprüche:** keine über den allgemeinen
  Verifikationsvorbehalt hinaus.

## F4d – ☐6 RT-Teilung, 8-Bahnenrock

- **Quelle:** [formeln_s064.md](formeln_s064.md), Abschnitt 4, Feld ☐6.
- **Buchfassung:**

```text
☐6 (8-Bahnenrock), RT: Teilung an Hüfte und Saum 1/2 zu 1/2
```

- **Technische Formel:** `RT_Teil_1 = RT_Breite * 1/2`,
  `RT_Teil_2 = RT_Breite * 1/2`
- **Eingaben und Einheiten:** `RT_Breite` [cm] an Hüfte bzw. Saum.
- **Ausgabe und Einheit:** `RT_Teil_1` [cm], `RT_Teil_2` [cm].
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine gedruckt.
- **Abhängigkeiten:** `RT_Breite` aus dem Rock-Grundschnitt.
- **Status:** offen (Seite noch nicht verifiziert).
- **Offene Fragen oder Widersprüche:** keine über den allgemeinen
  Verifikationsvorbehalt hinaus.

## F5 – Widerspruch: Bahnenzahl im "halben Rock" vs. Teilung in F4

- **Quelle:** [formeln_s064.md](formeln_s064.md), Abschnitt 5.
- **Buchfassung:** siehe F1 (Textstelle "zusammen 3 bzw. 4 Bahnen") im
  Gegensatz zu den in F4a–F4d gezeigten Teilungen.
- **Technische Formel:** keine (Gegenüberstellung, keine eigene Rechnung).
- **Eingaben und Einheiten:** entfällt.
- **Ausgabe und Einheit:** entfällt.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** entfällt.
- **Abhängigkeiten:** F1, F4a, F4b.
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** F1 nennt für den halben Rock (VT + RT)
  3 Bahnen beim 6-Bahnenrock. F4a/F4b zeigen je eine Teilung von VT und von
  RT in je 2 Teilbreiten, zusammen 4 Teilbreiten. Ob sich diese 4 gezeichneten
  Teilbreiten (z. B. durch Zuschnitt im Stoffbruch an `vM-StB`/`hM-StB`) zu
  den 3 im Text genannten Bahnen zusammensetzen, ist auf dieser Seite nicht
  erklärt und wird hier nicht selbst hergeleitet.
