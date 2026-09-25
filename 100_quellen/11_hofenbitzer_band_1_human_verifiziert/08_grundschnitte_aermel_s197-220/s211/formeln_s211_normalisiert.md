# Formeln s211 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s211.md`](formeln_s211.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Beide Formeln stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der Buchfassung.
Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung.

## Formel 1 – Ärmelkugel vergrößern (Einhalteweite erhöhen)

- **Quelle:** [`formeln_s211.md`](formeln_s211.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Die Kugel um ca. ¼ der fehlenden EW erhöhen (hier 0,4 cm)

  Öffnung um ca. ½ der fehlenden EW (hier 0,7 cm)
  ```
- **Technische Formel:**
  ```text
  ew_fehlend = ew_soll - ew_ist        (ew_fehlend > 0)

  delta_kugelhoehe = ca. 1/4 * ew_fehlend   (hier: ew_fehlend ≈ 1,6 cm → 0,4 cm)
  delta_oeffnung_je_seite = ca. 1/2 * ew_fehlend  (hier ≈ 0,7 cm, je linker und
                                                    rechter Kugelseite an Punkt ①)
  ```
- **Eingaben und Einheiten:** `ew_ist` (cm, aktuelle Einhalteweite des
  angepassten Ärmels), `ew_soll` (cm, benötigte Einhalteweite) – beide nicht auf
  dieser Seite definiert, nur die Differenz `ew_fehlend` wird hier verwendet.
- **Ausgabe und Einheit:** `delta_kugelhoehe` (cm, Zugabe an Punkt ② der
  Ärmelkugel), `delta_oeffnung_je_seite` (cm, Öffnungsmaß je Schnittpunkt ① auf
  beiden Kugelseiten).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` vor beiden
  Faktoren erhalten – kein fester Betrag laut Buch. Das Rechenbeispiel „hier
  0,4 cm" bzw. „hier 0,7 cm" ist nur für den abgebildeten Musterfall (schmaler
  Ärmel, G 38, PK 3) angegeben; daraus folgt rechnerisch `ew_fehlend ≈ 1,6 cm`
  (0,4 cm ÷ ¼), was mit `0,7 cm ≈ ½ · 1,6 cm` konsistent ist (½ · 1,6 = 0,8 cm,
  Buchwert 0,7 cm liegt knapp darunter – Rundungsdifferenz nicht aufgelöst,
  nicht still korrigiert). Nicht spezifiziert: ob `delta_oeffnung_je_seite`
  einmal insgesamt oder tatsächlich je Kugelseite einzeln angesetzt wird (Skizze
  zeigt den Wert an beiden Punkten ①, siehe Buchfassung).
- **Abhängigkeiten:** `ew_ist`/`ew_soll` nicht auf s211 hergeleitet, vermutlich
  auf einer Vorseite definiert (nicht ermittelt); [[Formel 2]] als Spiegelfall
  (überschüssige statt fehlende EW); Konstruktionsschritt „Einschnitte an der
  Kugel wie auf Seite 117, ☐1" (Absatz 4, `ocr_s211.md` Zeile 19) als
  vorgelagerter, nicht kopierter Verweis.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Rechnerische Rundungsdifferenz zwischen ¼- und ½-Beispielwert (0,4 cm →
    ew_fehlend 1,6 cm vs. 0,7 cm → ew_fehlend 1,4 cm) nicht am Original geklärt.
  - Ob die ½-Zugabe je Seite einzeln oder in Summe gilt, ist aus der
    Buchfassung nicht eindeutig.

## Formel 2 – Ärmelkugel verkleinern (Einhalteweite verringern)

- **Quelle:** [`formeln_s211.md`](formeln_s211.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die Kugel um ca. ¼ der überschüssigen EW verkürzen (hier 0,25 cm)

  Zulegen um ca. ½ der überschüssigen EW (hier 0,5 cm)
  ```
- **Technische Formel:**
  ```text
  ew_ueberschuss = ew_ist - ew_soll        (ew_ueberschuss > 0)

  delta_kugelhoehe = ca. 1/4 * ew_ueberschuss   (hier: ew_ueberschuss ≈ 1,0 cm
                                                  → 0,25 cm; Vorzeichen: Kürzung)
  delta_zulegen_je_seite = ca. 1/2 * ew_ueberschuss  (hier ≈ 0,5 cm, je linker
                                                        und rechter Kugelseite
                                                        an Punkt ①)
  ```
- **Eingaben und Einheiten:** `ew_ist` (cm, aktuelle Einhalteweite des
  angepassten Ärmels), `ew_soll` (cm, benötigte Einhalteweite) – wie bei
  Formel 1 nicht auf dieser Seite definiert.
- **Ausgabe und Einheit:** `delta_kugelhoehe` (cm, Kürzung an Punkt ② der
  Ärmelkugel), `delta_zulegen_je_seite` (cm, Zulegemaß je Schnittpunkt ① auf
  beiden Kugelseiten).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` vor beiden
  Faktoren erhalten. Rechenprobe: `0,25 cm ÷ ¼ = 1,0 cm` und
  `0,5 cm ÷ ½ = 1,0 cm` – hier stimmen beide Beispielwerte konsistent auf
  `ew_ueberschuss ≈ 1,0 cm` überein (anders als bei Formel 1). Nicht
  spezifiziert, ob `delta_zulegen_je_seite` je Seite einzeln oder insgesamt
  gilt.
- **Abhängigkeiten:** [[Formel 1]] als Spiegelfall (fehlende statt
  überschüssige EW); `ew_ist`/`ew_soll` wie dort nicht auf s211 hergeleitet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob `delta_zulegen_je_seite` je Seite einzeln oder in Summe gilt, ist aus
    der Buchfassung nicht eindeutig.
  - Die zusätzliche, nur in der Skizze sichtbare Kugelhöhen-Angabe „ca. 5 cm"
    (siehe `formeln_s211.md`, Abschnitt 2) hat keinen erkennbaren Rechenbezug
    zu dieser Formel und wurde deshalb nicht einbezogen.
