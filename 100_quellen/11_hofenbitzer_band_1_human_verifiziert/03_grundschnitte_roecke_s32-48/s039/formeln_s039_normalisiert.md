# Formeln s039 – Normalisierung (Walking Skeleton)

Grundlage: [formeln_s039.md](formeln_s039.md). Nur Position 6 stützt sich auf
eine am Original bestätigte Stelle ([s039.md](s039.md)); alle anderen
Positionen sind vorläufig aus der OCR-Rohfassung übernommen und noch nicht am
Original bestätigt. Kein Python, kein Engine-Vertrag, keine neue Fachregel.

## 1. Bundlänge zu Taillenumfang

- **Quelle:** [formeln_s039.md](formeln_s039.md#1-bundlänge-zu-taillenumfang)
- **Buchfassung:**
  ```text
  Bundlänge ≈ Taillenumfang
  ```
- **Technische Formel:** `Bundlaenge ≈ TaU`
- **Eingaben und Einheiten:** `TaU` (Taillenumfang) in cm
- **Ausgabe und Einheit:** `Bundlaenge` in cm
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Näherung („ca.“), kein
  fester Zuschlag oder Faktor angegeben.
- **Abhängigkeiten:** Grundlage für Position 3 (vM).
- **Status:** offen
- **Offene Fragen:** Nicht am Original bestätigt. Verhältnis zu Position 2
  („Bundlänge ≈ Talz“) ungeklärt.

## 2. Bundbreite und zweite Bundlängen-Angabe

- **Quelle:** [formeln_s039.md](formeln_s039.md#2-bundbreite-höhe-des-rechtecks)
- **Buchfassung:**
  ```text
  Bundlänge ≈ Talz
  Bundbreite = 2 bis 5 cm
  ```
- **Technische Formel:** `Bundlaenge ≈ Talz` (Bedeutung von „Talz“ ungeklärt);
  `Bundbreite ∈ [2 cm, 5 cm]`
- **Eingaben und Einheiten:** unklar, ob „Talz“ = `TaU` oder eine andere Größe
- **Ausgabe und Einheit:** `Bundbreite` in cm (Bereich)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** `Bundbreite` als
  Bereich 2–5 cm erhalten, kein Default wählen.
- **Abhängigkeiten:** ggf. Duplikat von Position 1.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** „Talz“ ist kein an anderer Stelle
  benanntes Kürzel dieser Seite. Ob es sich um einen OCR-Fehler für „TaU“
  handelt, um eine Nachbarseiten-Übernahme oder um eine andere Buchgröße,
  ist ungeklärt und wird hier nicht geraten.

## 3. vM als Mitte der Bundlänge

- **Quelle:** [formeln_s039.md](formeln_s039.md#3-vm-als-mitte-der-bundlänge)
- **Buchfassung:**
  ```text
  vM = Bundlänge : 2
  ```
- **Technische Formel:** `vM_Position = Bundlaenge / 2`
- **Eingaben und Einheiten:** `Bundlaenge` in cm
- **Ausgabe und Einheit:** `vM_Position` in cm (Abstand ab Bundanfang)
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine; Begründung im
  Buch: Symmetrie von rechter und linker Körperseite.
- **Abhängigkeiten:** Position 1/2 (Bundlänge); zeichnungsgebunden
  (Bundrechteck, siehe skizzen_s039.json, Labels nicht erfasst).
- **Status:** offen
- **Offene Fragen:** Nicht am Original bestätigt.

## 4. Taillennahtlängen zu Taillenweite

- **Quelle:** [formeln_s039.md](formeln_s039.md#4-taillennahtlängen-zu-taillenweite)
- **Buchfassung:**
  ```text
  Nahtstrecken der vorderen Taillennaht und der hinteren Taillennaht
  (jeweils ohne Abnäherinhalte) messen.
  Die Taillennahtlängen entsprechen der halben Taillenweite.
  ```
- **Technische Formel:** nicht eindeutig aufstellbar (siehe offene Fragen)
- **Eingaben und Einheiten:** Nahtstrecken vorn/hinten in cm, ohne
  Abnäherinhalte
- **Ausgabe und Einheit:** unklar
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine angegeben
- **Abhängigkeiten:** vermutlich zu `TaU` (Position 1) und zu `vTaN`/`hTaN`
  (Position 6), aber Buchtext nennt an dieser Stelle keine Symbole.
- **Status:** offen
- **Offene Fragen:** Bezieht sich „die halbe Taillenweite“ auf vordere und
  hintere Nahtlänge je einzeln oder auf beide zusammen? Nicht am Original
  bestätigt.

## 5. Überschneidungsbetrag / Taillenmehrweite (Sollbereich)

- **Quelle:** [formeln_s039.md](formeln_s039.md#5-überschneidungsbetrag--taillenmehrweite-sollbereich)
- **Buchfassung:**
  ```text
  Taillenmehrweite ≈ 1 bis 1,5 cm
  ```
- **Technische Formel:** `Taillenmehrweite ∈ [1 cm, 1,5 cm]` (Sollbereich,
  keine Berechnungsvorschrift)
- **Eingaben und Einheiten:** –
- **Ausgabe und Einheit:** `Taillenmehrweite` in cm
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Bereich als Erwartungswert
  für eine korrekt sitzende Konstruktion, kein fester Wert.
- **Abhängigkeiten:** Position 6 (dort berechneter Wert 1,2 cm liegt
  innerhalb dieses Bereichs); Position 7 (Fehlerschwelle).
- **Status:** offen
- **Offene Fragen:** Nicht am Original bestätigt.

## 6. Kontrolle der Taillenmehrweite

- **Quelle:** [formeln_s039.md](formeln_s039.md#6-kontrolle-der-taillenmehrweite-bestätigt),
  bestätigt in [s039.md](s039.md).
- **Buchfassung:**
  ```text
  = vTaN + hTaN − TaU : 2
  = 19,7 + 17,5 cm − 36,0 cm
  = 1,2 cm Einhalteweite
  ```
- **Technische Formel:** nicht eindeutig – siehe Widerspruch unten. Wörtlich
  mit „:“ als Division gelesen: `Kontrolle = vTaN + hTaN - (TaU / 2)`.
- **Eingaben und Einheiten:** `vTaN` = 19,7 cm, `hTaN` = 17,5 cm,
  `TaU` = 36,0 cm
- **Ausgabe und Einheit:** `Taillenmehrweite` („Einhalteweite“) in cm
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine; reine
  Kontrollrechnung.
- **Abhängigkeiten:** Position 5 (Sollbereich), Position 7 (Fehlerschwelle).
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Unabhängig nachgerechnet ergibt die
  wörtliche Formel `vTaN + hTaN - (TaU : 2)` = 19,7 + 17,5 − 18,0 = **19,2 cm**,
  nicht die gedruckten 1,2 cm. Nur wenn man das „: 2“ ganz wegließe
  (`vTaN + hTaN - TaU` = 19,7 + 17,5 − 36,0 = 1,2 cm) stimmt das Ergebnis mit
  dem gedruckten Beispiel überein. Das Beispiel selbst ist damit **kein
  Beleg** dafür, dass „: 2“ wegzulassen ist (Regel 4: gedrucktes Beispiel
  nicht als Beweis für eine andere Formel verwenden) – es zeigt nur, dass
  Formel und Beispiel wie gedruckt nicht zusammenpassen. Mögliche Erklärungen
  (keine davon gewählt): Übersetzungs-/Satzfehler im Buch, OCR-Fehler bei
  „: 2“, oder „TaU“ bezeichnet an dieser Stelle bereits eine halbierte Größe.
  Werners Bestätigung deckt nur ab, dass dieser Wortlaut so im Original
  steht – nicht, dass die Formel algebraisch zum Beispiel passt. Status daher
  trotz bestätigtem Wortlaut `offen`, bis Werner die Diskrepanz am Original
  klärt.

## 7. Fehlerschwelle der Taillenmehrweite

- **Quelle:** [formeln_s039.md](formeln_s039.md#7-fehlerschwelle-der-taillenmehrweite)
- **Buchfassung:**
  ```text
  Taillenmehrweite > 1,5 cm ⇒ Anzeichen für Fehler (z. B. Rockkonstruktion oder Fehlmessung)
  ```
- **Technische Formel:** `wenn Taillenmehrweite > 1,5 cm: Fehleranzeichen`
- **Eingaben und Einheiten:** `Taillenmehrweite` in cm (aus Position 6)
- **Ausgabe und Einheit:** boolesches Fehlersignal, keine Zahl
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Schwelle 1,5 cm; Buch gibt
  keine automatische Korrektur vor, nur „identifizieren und berichtigen“.
- **Abhängigkeiten:** Position 5 und 6.
- **Status:** offen
- **Offene Fragen:** Nicht am Original bestätigt.
