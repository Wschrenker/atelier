# Formeln – s054 (normalisiert)

Technische Fassung zu [formeln_s054.md](formeln_s054.md). Walking-Skeleton-
Durchgang: alle formel- und coderelevanten Stellen der Seite sind erfasst,
aber nur die in [s054.md](s054.md) genannte Stelle ist am Original bestätigt
(`Status: normalisiert`). Alle anderen Stellen stehen auf `Status: offen`, bis
Werner sie am Buch bestätigt.

## F1 – Zusätzliche Weitenreduzierung an der Seitennaht bei unebener Hüftform

- **Quelle:** [formeln_s054.md](formeln_s054.md#1-zusätzliche-weitenreduzierung-an-der-seitennaht-bei-unebener-hüftform)
- **Buchfassung:**
  ```text
  … muss etwas mehr Weite an der Seitennaht reduziert werden (hier z.B. 1 cm).
  ```
- **Technische Formel:** `SeitennahtReduzierungZusatz = ca. 1 cm` (Beispielwert
  für den Fall einer unebenen Hüftform mit „Delle" zwischen Taille und Hüfte)
- **Eingaben und Einheiten:** keine explizite Eingangsgröße auf dieser Seite;
  gilt zusätzlich zur regulären Seitennaht-Reduzierung
- **Ausgabe und Einheit:** `SeitennahtReduzierungZusatz` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** nur als Beispiel „hier
  z. B." markiert, kein fester Wert; gilt für unebene Hüftform
- **Abhängigkeiten:** ergänzt die allgemeine Auswahlregel F2 (Seitennaht vs.
  hintere Abnäher)
- **Status:** normalisiert
- **Offene Fragen oder Widersprüche:** Die OCR-Rohfassung
  ([ocr_s054.md](ocr_s054.md), Zeile 75) liest „7 cm" statt des von Werner am
  Original bestätigten Werts „1 cm" – vermutlicher OCR-Lesefehler. Beide
  Fassungen bleiben nebeneinander dokumentiert (siehe
  [formeln_s054.md](formeln_s054.md#1-zusätzliche-weitenreduzierung-an-der-seitennaht-bei-unebener-hüftform)).

## F2 – Auswahlregel: Mehrweite bevorzugt an der Seitennaht entfernen (Schwellenwert ca. 5 cm)

- **Quelle:** [formeln_s054.md](formeln_s054.md#2-schwellenwert-mehrweite-an-der-oberen-rockkante-ab-ca-5-cm)
- **Buchfassung:**
  ```text
  Erfahrungsgemäß entfernt man bei einem Rock mit einer Taillenvertiefung ab
  ca. 5 cm die Mehrweite an der oberen Rockkante besser an den Seitennähten.
  ```
- **Technische Formel:** `wenn Taillenvertiefung >= ca. 5 cm: Mehrweite bevorzugt an Seitennähten entfernen`
- **Eingaben und Einheiten:** `Taillenvertiefung` (cm, auf dieser Seite nicht
  selbst definiert – vermutlich Vorseiten-Größe, nur verlinken)
- **Ausgabe und Einheit:** Auswahlentscheidung (Ort der Weitenreduzierung:
  Seitennaht)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Schwellenwert „ca. 5 cm"
  wörtlich erhalten, keine Obergrenze genannt; Formulierung „erfahrungsgemäß …
  besser" ist eine fachliche Empfehlung, keine zwingende Regel
- **Abhängigkeiten:** ergänzt durch F3 (Sonderfall Hohlkreuz/Gesäß) und F1
  (Beispielwert für die unebene Hüftform)
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine

## F3 – Bedingung: zusätzliche Reduzierung an den hinteren Abnähern

- **Quelle:** [formeln_s054.md](formeln_s054.md#3-bedingung-zusätzliche-reduzierung-an-den-hinteren-abnähern)
- **Buchfassung:**
  ```text
  Nur bei starkem Hohlkreuz und rundem, tiefen Gesäß sollte auch Weite an den
  hinteren Abnähern reduziert werden, um an dieser Stelle mit den dann
  vergrößerten Abnähern die rundere Gesäßform abzubilden.
  ```
  ```text
  Weiten-Reduzierungen für obige Figur auch an den hinteren Abnähern vornehmen
  (hier nicht gezeichnet).
  ```
- **Technische Formel:** `wenn Hohlkreuz = stark UND Gesaessform = rund_tief: hintereAbnaeherInhalt += Weitenreduzierung`
- **Eingaben und Einheiten:** Ausprägung `Hohlkreuz` (kategorial: normal /
  stark), `Gesaessform` (kategorial, u. a. rund/tief) – auf dieser Seite nicht
  weiter quantifiziert
- **Ausgabe und Einheit:** Erhöhung von `hintereAbnaeherInhalt` (cm, Größe
  selbst nicht auf dieser Seite definiert)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** ausdrücklich „nur bei"
  formulierte Bedingung, kein Zahlenwert für die Reduzierung selbst genannt;
  in der zugehörigen Skizze (☐3) nicht grafisch ausgeführt
- **Abhängigkeiten:** Sonderfall zu F2; Betrag/Verfahren der Abnäher-Vergrößerung
  nicht auf dieser Seite definiert
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine

## F4 – Regel: vorderer Abnäher entfällt

- **Quelle:** [formeln_s054.md](formeln_s054.md#4-regel-vorderer-abnäher-entfällt)
- **Buchfassung:**
  ```text
  Der vordere Abnäher entfällt ganz, da vorne die Rockkante unter der
  Bauchwölbung, bzw. unter dem seitlichen Hüftknochen liegt und ein Abnäher
  dort überflüssig ist.
  ```
- **Technische Formel:** `vAbnInhalt = 0`
- **Eingaben und Einheiten:** keine
- **Ausgabe und Einheit:** `vAbnInhalt` (cm)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** gilt für diesen
  Modelltyp (Hüftrock mit großer Taillenvertiefung); keine Fallunterscheidung
  genannt
- **Abhängigkeiten:** Bei nur einem Abnäher im Grundschnitt verweist der
  Buchtext für einen weiteren hinteren Abnäher auf „Seite 35"
  ([ocr_s054.md](ocr_s054.md), Zeilen 88–90) – nur verlinken, nicht Teil dieser
  Seite
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine
