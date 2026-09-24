# Formeln s045 (normalisiert)

Walking-Skeleton-Durchlauf auf Werners ausdrücklichen Wunsch: Alle drei
Einträge stehen auf `offen`, weil s045 noch nicht menschlich verifiziert ist
und keine formel- oder coderelevante Stelle dieser Seite bisher am Original
bestätigt wurde (siehe [`formeln_s045.md`](formeln_s045.md)). Kein Eintrag ist
bereit für einen Codevertrag.

## 1. Taillenradius (r_TaW)

- **Quelle:** [formeln_s045.md, Abschnitt „Berechnungen-Kasten"](formeln_s045.md#berechnungen-kasten-berechnungen-1-rechts-auf-der-seite-unter-2)
- **Buchfassung:**
  ```text
  r_TaW = TaW : π
        = 72 cm : 3,14
        = 22,9 cm
  ```
- **Technische Formel:** `r_TaW = TaW / π`
- **Eingaben und Einheiten:** `TaW` (Taillenweite) [cm]; `π` als Konstante,
  im Buch mit `3,14` angenähert
- **Ausgabe und Einheit:** `r_TaW` (Taillenradius) [cm]
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine angegeben; `TaW`
  und `MoL` (s. unten) sind das gedruckte Zahlenbeispiel, keine allgemeine
  Bereichsangabe.
- **Abhängigkeiten:** Eingang für „2. Saumradius (r_SaW)" auf dieser Seite.
  Zum Vergleich auf s044 (Vollglocke) vermutlich `r_TaW = TaW / (2 · π)` —
  nur verlinken, sobald s044 bestätigt ist.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Ob der einfache Faktor `π` (statt
  `2 · π` wie bei der Vollglocke) tatsächlich so gedruckt ist, ist am
  Original zu bestätigen (siehe `formeln_s045.md`). Geometrisch ist ein
  einfacher Faktor `π` für einen Halbkreisbogen plausibel (halber Umfang
  `π · r` statt `2 · π · r`), das ersetzt aber keine Bestätigung des
  gedruckten Wortlauts. Nachrechnung des Beispiels: `72 : 3,14 = 22,93 cm`,
  im Buch auf `22,9 cm` gerundet — stimmt überein, beweist aber nicht,
  welche Formel gedruckt ist.

## 2. Saumradius (r_SaW)

- **Quelle:** [formeln_s045.md, Abschnitt „Berechnungen-Kasten"](formeln_s045.md#berechnungen-kasten-berechnungen-1-rechts-auf-der-seite-unter-2)
- **Buchfassung:**
  ```text
  r_SaW = r_TaW + MoL
        = 22,9 cm + 50 cm
        = 72,9 cm
  ```
- **Technische Formel:** `r_SaW = r_TaW + MoL`
- **Eingaben und Einheiten:** `r_TaW` (Taillenradius) [cm], `MoL`
  (Modelllänge/Rocklänge, im Buch auch „Volantlänge" genannt) [cm]
- **Ausgabe und Einheit:** `r_SaW` (Saumradius) [cm]
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine angegeben; `MoL`
  wird an keiner Stelle dieser Seite selbst definiert oder abgegrenzt.
- **Abhängigkeiten:** Eingang aus „1. Taillenradius (r_TaW)"; Eingang für
  „3. Saumweite (SaW)". `MoL` vermutlich seitenübergreifend definiert (z. B.
  Rocklänge/Modelllänge aus einer Maßtabelle) — nur verlinken, sobald dort
  bestätigt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Bedeutung und Herkunft von `MoL` ist
  auf dieser Seite nicht definiert und noch nicht bestätigt. Nachrechnung:
  `22,9 + 50 = 72,9 cm` — stimmt mit dem gedruckten Zwischenergebnis überein.

## 3. Saumweite (SaW)

- **Quelle:** [formeln_s045.md, Abschnitt „Berechnungen-Kasten"](formeln_s045.md#berechnungen-kasten-berechnungen-1-rechts-auf-der-seite-unter-2)
- **Buchfassung:**
  ```text
  SaW = π · r_SaW
      = 3,14 · 72,9 cm
      = 229 cm
  ```
- **Technische Formel:** `SaW = π · r_SaW`
- **Eingaben und Einheiten:** `r_SaW` (Saumradius) [cm]; `π` als Konstante,
  im Buch mit `3,14` angenähert
- **Ausgabe und Einheit:** `SaW` (Saumweite) [cm]
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine angegeben.
- **Abhängigkeiten:** Eingang aus „2. Saumradius (r_SaW)". Zum Vergleich auf
  s044 (Vollglocke) vermutlich `SaW = 2 · π · r_SaW` — nur verlinken, sobald
  s044 bestätigt ist.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Derselbe Faktor-π-Vorbehalt wie bei
  „1. Taillenradius (r_TaW)". Nachrechnung mit dem gerundeten Zwischenwert:
  `3,14 · 72,9 = 228,906 cm`, im Buch auf `229 cm` gerundet — stimmt bis auf
  Rundung überein. Mit dem ungerundeten `r_TaW` (`22,9299… cm`) ergibt sich
  `228,997… cm`, also noch näher an `229 cm`. Das bestätigt nur die
  arithmetische Konsistenz des Beispiels, nicht den gedruckten Wortlaut der
  Formel.

## Nicht erfasst

- Der Fließtext zu ☐1 („Die Fläche des mäßig weiten Rocks besteht nur aus
  einem halben Kreisring …") beschreibt nur die geometrische Idee, keine
  eigene Rechenbeziehung.
- Die Konstruktions- und Zuschnittschritte (Abschnitte „1 Konstruktion" und
  „2 Zuschnitt") sind Handlungsanweisungen ohne Rechen- oder
  Auswahlformel.
- Keine Tabelle vorhanden (`tabellen_s045.md` existiert nicht, siehe
  `s045.md`).
