# Formeln s061 – Normalisierung (Passen mit Knopfverschluss (2))

Alle Stellen dieser Seite sind zeichnungsgebunden und bisher **nicht** durch
Werner am Original bestätigt. Status entsprechend `offen`, nicht `normalisiert`.

## 1. Taillenbeleg – Weiten- und Breiten-Reduzierung

- **Quelle:** [formeln_s061.md](formeln_s061.md), Abschnitt 1
- **Buchfassung:**

  ```text
  Taillenbelege mit Weiten- und Breiten-Reduzierung um ca. 0,2 cm sowie
  Nahtzugaben und Markierungen für die Produktions-Schnittteile
  ```

- **Technische Formel:**

  ```text
  Weite_Taillenbeleg_reduziert = Weite_Taillenbeleg_ausgangswert − Δ
  Breite_Taillenbeleg_reduziert = Breite_Taillenbeleg_ausgangswert − Δ
  Δ ≈ 0,2 cm
  ```

- **Eingaben und Einheiten:** Weite_Taillenbeleg_ausgangswert (cm),
  Breite_Taillenbeleg_ausgangswert (cm) — beide seitenübergreifend definiert,
  nicht auf s061 selbst.
- **Ausgabe und Einheit:** Weite_Taillenbeleg_reduziert (cm),
  Breite_Taillenbeleg_reduziert (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `ca.` bleibt erhalten,
  kein fester Wert; Δ ist ein ungefährer Reduktionsbetrag, kein Bereich mit
  Ober-/Untergrenze.
- **Abhängigkeiten:** Bezug auf Rock- bzw. Passen-Ausgangsmaße von s061 selbst
  (VT-Taillenbeleg, RT-Taillenbeleg) sowie ggf. auf die Grundschnittkonstruktion
  anderer Seiten; nicht auf dieser Seite hergeleitet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Ausgangswert von Weite/Breite nicht auf
  dieser Seite angegeben; Text nur im Bildausschnitt sichtbar und nicht durch
  Werner bestätigt.

## 2. RV-Schlitz – Nahtverschiebung am Futter

- **Quelle:** [formeln_s061.md](formeln_s061.md), Abschnitt 2
- **Buchfassung:**

  ```text
  Am RV-Schlitz die Naht um 0,5 cm nach innen verschieben, weil das Futter
  neben den Zähnchen auf das RV-Band genäht wird. Hier kommt nur 1 cm
  Nahtzugabe hinzu.
  ```

- **Technische Formel:**

  ```text
  Position_Naht_RV_Schlitz_Futter = Position_Naht_original − 0,5 cm (Richtung: nach innen)
  Nahtzugabe_RV_Schlitz_Futter = 1 cm
  ```

- **Eingaben und Einheiten:** Position_Naht_original (cm, Bezugslinie nicht auf
  dieser Seite definiert); Richtungsangabe „nach innen“.
- **Ausgabe und Einheit:** Position_Naht_RV_Schlitz_Futter (cm),
  Nahtzugabe_RV_Schlitz_Futter (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** gilt ausdrücklich nur
  lokal am RV-Schlitz des Futters, nicht als allgemeine Nahtzugabe der Seite;
  Begründung im Buch: Futter wird neben den Zähnchen auf das RV-Band genäht.
- **Abhängigkeiten:** setzt eine allgemeine Nahtzugabe-Regel für das Futter
  voraus, gegen die diese 1 cm eine ausdrückliche Ausnahme bildet; diese
  allgemeine Regel ist auf s061 nicht sichtbar.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** die sonst auf dieser Seite geltende
  Standard-Nahtzugabe ist nicht dokumentiert, daher lässt sich der Kontrast
  „nur 1 cm“ nicht quantitativ einordnen; Text nicht durch Werner bestätigt.

## 3. Schlitzende – Verschiebung am Futter

- **Quelle:** [formeln_s061.md](formeln_s061.md), Abschnitt 3
- **Buchfassung:**

  ```text
  Schlitzende für das Futter an der SN ca. 2 bis 3 cm nach unten verschieben
  ```

- **Technische Formel:**

  ```text
  Position_Schlitzende_Futter_SN = Position_Schlitzende_original + Δ (Richtung: nach unten)
  Δ ∈ [2 cm, 3 cm] (ca.)
  ```

- **Eingaben und Einheiten:** Position_Schlitzende_original (cm, Bezugslinie
  nicht auf dieser Seite definiert).
- **Ausgabe und Einheit:** Position_Schlitzende_Futter_SN (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich [2 cm, 3 cm]
  bleibt Bereich, kein fester Wert oder Default; `ca.` erhalten; Auswahl
  innerhalb des Bereichs ist fachliche Entscheidung, nicht auf dieser Seite
  festgelegt.
- **Abhängigkeiten:** SN (Seitennaht) als Bezugslinie; Bezug zur allgemeinen
  Futterkonstruktion, nicht auf s061 hergeleitet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine, aber Text nur im Bildausschnitt
  sichtbar und nicht durch Werner bestätigt.

## 4. Futtersaumkante – Doppelmaß

- **Quelle:** [formeln_s061.md](formeln_s061.md), Abschnitt 4
- **Buchfassung:**

  ```text
  Futtersaumkante
  2 cm
  2 cm
  ```

- **Technische Formel:** nicht gebildet — die Bedeutung der beiden
  aufeinanderfolgenden Maße ist aus der Zeichnung allein nicht eindeutig
  bestimmbar (z. B. zweifach umgelegter Saum vs. zwei getrennte Zugaben).
- **Eingaben und Einheiten:** zwei Maße von je 2 cm, Bezug unklar.
- **Ausgabe und Einheit:** offen.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine erkennbar.
- **Abhängigkeiten:** Futtersaumkante von Hüftrock-mit-Passe-Futterteilen
  (RT-Futter und VT-Futter), beide identisch.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** Bedeutung der zwei gestapelten 2-cm-Maße
  nicht aus dem Bildausschnitt herleitbar; keine Auswahlregel plausibel
  ergänzt. Muss am Original bzw. mit Werner geklärt werden, bevor eine
  technische Formel gebildet werden kann.
