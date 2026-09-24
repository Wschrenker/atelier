# Formeln s101 – Wickelrock (2), normalisiert

Walking Skeleton: Basiert auf der noch nicht menschlich verifizierten
Extraktion [formeln_s101.md](formeln_s101.md). Status aller Punkte daher
`offen`, bis Werner die Formel- und Codeprüfstellen am Original bestätigt
hat.

## Formel 1 – Bund: Abstandsübertragung SN–Kantenmarkierung

- **Quelle:** [formeln_s101.md](formeln_s101.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Am Rock-VT den Abstand von der SN zur Kantenmarkierung messen.
  Am Bund diesen Betrag von der SN in Richtung vM entfernen. Dieser wird
  hier nicht benötigt.
  ```
- **Technische Formel:** `abstand_bund_sn_vm = abstand_vt_sn_kantenmarkierung`
  (Kopierbeziehung: ein am Rock-Vorderteil gemessener Abstand wird am Bund
  von der SN in Richtung vM als derselbe Betrag angetragen)
- **Eingaben und Einheiten:** `abstand_vt_sn_kantenmarkierung` – am Rock-VT
  gemessener Abstand SN→Kantenmarkierung; Einheit nicht angegeben (vermutlich
  cm, wie auf den übrigen Seiten dieser Kategorie üblich)
- **Ausgabe und Einheit:** `abstand_bund_sn_vm` – Antragspunkt am Bund, von
  SN in Richtung vM; gleiche Einheit wie Eingabe
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine
- **Abhängigkeiten:** verweist auf „gerader Bund" (☐2, laut Skizzenbeschriftung
  „übertragen (siehe ☐2)" – dieser Vertrag liegt auf einer anderen Seite
  dieser Kategorie und wird hier nur verlinkt, nicht kopiert)
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Unklar, worauf sich „Dieser wird hier
  nicht benötigt." bezieht (siehe Hinweis in formeln_s101.md). Kein
  Zahlenwert im Buchtext; die eigentliche Maßzahl stammt von einer anderen,
  hier nicht extrahierten Seite (Rock-VT-Schnitt).

## Formel 2 – Kantenabstich: Beleg oder Einschlag

- **Quelle:** [formeln_s101.md](formeln_s101.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die Übertrittkante muss bei einem runden Kantenabstich mit einem Beleg
  verarbeitet sein. Ein gerader Kantenabstich kann auch mit einem Einschlag
  (angeschnittener Beleg) gearbeitet werden.
  ```
- **Technische Formel:** Auswahlregel, keine Rechenformel:
  - `kantenabstich == "rund"` → `verarbeitung = "Beleg"` (zwingend)
  - `kantenabstich == "gerade"` → `verarbeitung ∈ {"Beleg", "Einschlag"}`
    (Einschlag zusätzlich möglich)
- **Eingaben und Einheiten:** `kantenabstich` – Kategorie „rund" oder
  „gerade", keine Einheit
- **Ausgabe und Einheit:** `verarbeitung` – Kategorie, keine Einheit
- **Bereiche, Bedingungen und Auswahlentscheidungen:** siehe technische
  Formel; „Einschlag" ist ausdrücklich als angeschnittener Beleg definiert
- **Abhängigkeiten:** keine weiteren auf dieser Seite
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine inhaltliche Unklarheit, aber
  noch nicht menschlich am Original bestätigt

## Formel 3 – Beleg-/Einschlagbreite

- **Quelle:** [formeln_s101.md](formeln_s101.md), Abschnitt 3
- **Buchfassung:**
  ```text
  ☐4 Die Beleg-(Einschlag-)Breite kann nach Wunsch gewählt werden, sollte
  aber so breit sein, dass beim Aufklappen der Wickelkante das Futter oder
  die innere Belegkante nicht direkt sichtbar wird.
  ```
- **Technische Formel:** keine Rechenformel; freie Auswahl mit qualitativer
  Nebenbedingung: `beleg_breite` frei wählbar, mit
  `beleg_breite ≥ mindestbreite_unsichtbarkeit` (Mindestbreite selbst nicht
  beziffert)
- **Eingaben und Einheiten:** `beleg_breite` – frei gewählt, Einheit nicht
  angegeben (vermutlich cm)
- **Ausgabe und Einheit:** keine numerische Ausgabe; Auswahlentscheidung
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „ca."-artiger
  fachlicher Auswahlspielraum ohne festen Wert oder Default – bewusst nicht
  ergänzt
- **Abhängigkeiten:** keine weiteren auf dieser Seite
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Buch nennt keinen Zahlenwert oder
  keine Mindestbreite; kein Default aus dem Buchtext ableitbar

## Formel 4 – Futter-Saum kürzen und Saumeinschlag

- **Quelle:** [formeln_s101.md](formeln_s101.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Für das Futter wird der Saum um 2 cm gekürzt und mit 2×2 cm
  Saumeinschlägen versehen. Ebenso am RT-Futter.
  NZg und SaEs anzeichnen.
  ```
- **Technische Formel:**
  `saumlaenge_futter = saumlaenge_rock − 2 cm`
  (gilt gleichermaßen für VT-Futter und RT-Futter); zusätzlich
  `saumeinschlag_futter = 2 cm × 2 cm`
- **Eingaben und Einheiten:** `saumlaenge_rock` – Saumlänge des
  Rock-Außenstoffs, Einheit cm (nicht auf dieser Seite hergeleitet, sondern
  Bezugsgröße von anderer Stelle)
- **Ausgabe und Einheit:** `saumlaenge_futter` in cm;
  `saumeinschlag_futter` als Breite×Tiefe in cm×cm
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; feste
  Buchwerte (2 cm Kürzung, 2×2 cm Einschlag)
- **Abhängigkeiten:** `saumlaenge_rock` stammt von einer anderen, hier nicht
  extrahierten Stelle (Rock-VT/RT-Schnitt); NZg (Nahtzugabe) und SaEs
  (Saumeinschlag) als Kennzeichnungen, keine eigene Formel
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Laut formeln_s101.md unklar, ob „NZg
  und SaEs anzeichnen." noch zu Schritt ⑪ gehört oder ein eigener
  unmarkierter Satz ist – am Original zu prüfen.
