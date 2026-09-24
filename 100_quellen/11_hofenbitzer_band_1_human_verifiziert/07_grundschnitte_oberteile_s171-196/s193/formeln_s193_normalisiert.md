# Formeln s193 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s193.md`](formeln_s193.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle Formeln stehen
deshalb auf `offen` bzw. `gesperrt`, unabhängig von der inhaltlichen
Klarheit der Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein
Ersatz für die Bestätigung.

## Formel 1 – Schulterverbreiterung VT

- **Quelle:** [`formeln_s193.md`](formeln_s193.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Vor dem Einzeichnen der Armlöcher die Schulter am VT um 1/10
  Armloch-Verbreiterung verbreitern.
  ```
- **Technische Formel:**
  ```text
  schulter_VT_neu = schulter_VT_alt + (1/10) * armloch_verbreiterung
  ```
- **Eingaben und Einheiten:** `schulter_VT_alt` (cm); `armloch_verbreiterung`
  (cm) — Beispielwert 4 cm für den halben Schnitt, siehe [[Formel 9]].
- **Ausgabe und Einheit:** `schulter_VT_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Bruch 1/10,
  kein Spielraum im Wortlaut.
- **Abhängigkeiten:** [[Formel 9]] (Beispielwert für `armloch_verbreiterung`).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt (Prüfstelle 1
    in `s193.md`).
  - Unklar, ob „Armloch-Verbreiterung" hier den halben Schnitt (4 cm, wie im
    Beispieltext) oder den ganzen Schnitt (ca. 8–8,5 cm) meint.

## Formel 2 – Hintere Schulternahtlänge angleichen

- **Quelle:** [`formeln_s193.md`](formeln_s193.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die hintere Schulternahltänge angleichen. Sie entspricht der vorderen SuNL
  + Einhalteweite (0,5 bis 1 cm).
  ```
- **Technische Formel:**
  ```text
  schulternahtlaenge_hinten = schulternahtlaenge_vorne + einhalteweite
  einhalteweite ∈ [0,5 cm, 1 cm]
  ```
- **Eingaben und Einheiten:** `schulternahtlaenge_vorne` (SuNL, cm).
- **Ausgabe und Einheit:** `schulternahtlaenge_hinten` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich „0,5 bis 1 cm"
  bleibt Bereich, kein fester Default.
- **Abhängigkeiten:** keine auf dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - OCR-Schreibweise „Schulternahltänge" nicht bestätigt (Prüfstelle 5 in
    `s193.md`, vermutlich „Schulternahtlänge").
  - Abkürzung „SuNL" hier als Schulternaht-Länge gelesen, nicht am Original
    geprüft.

## Formel 3 – Brustbreite ausstellen (vorderes Armloch)

- **Quelle:** [`formeln_s193.md`](formeln_s193.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Die Brustbreite um mind. 1/4 Armloch-Verbreiterung am vorderen Armloch
  ausstellen (hier ergibt sie sich, bei der Formung über die Mitte der
  Öffnung).
  ```
- **Technische Formel:**
  ```text
  brustbreite_neu = brustbreite_alt + delta
  delta ≥ (1/4) * armloch_verbreiterung   (mind., keine Obergrenze im Text)
  ```
- **Eingaben und Einheiten:** `brustbreite_alt` (cm); `armloch_verbreiterung`
  (cm) — Beispielwert 4 cm, siehe [[Formel 9]].
- **Ausgabe und Einheit:** `brustbreite_neu` (cm), Ausstellung am vorderen
  Armloch.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** nur Untergrenze
  „mind. 1/4" benannt; der tatsächliche Betrag „ergibt sich ... bei der
  Formung über die Mitte der Öffnung" — laut Buchwortlaut ein
  Konstruktionsergebnis, kein fester Rechenwert.
- **Abhängigkeiten:** [[Formel 9]]; Ergebniswert wird in [[Formel 6]] als
  „derselbe Betrag wie am vorderen Armloch" weiterverwendet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Wie der tatsächliche Ausstellbetrag aus „Formung über die Mitte der
    Öffnung" geometrisch bestimmt wird, ist textlich nicht präzisiert.

## Formel 4 – Rückenbreite vergrößern (hinteres Armloch)

- **Quelle:** [`formeln_s193.md`](formeln_s193.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Am hinteren Armloch wird die Rückenbreite vergrößert, wie auf Seite 191
  beschrieben, um bis zu 1/4 der Armlochverbreiterung.
  ```
- **Technische Formel:**
  ```text
  ruckenbreite_neu = ruckenbreite_alt + delta
  delta ≤ (1/4) * armloch_verbreiterung   (bis zu, keine Untergrenze im Text)
  ```
- **Eingaben und Einheiten:** `ruckenbreite_alt` (cm); `armloch_verbreiterung`
  (cm) — Beispielwert 4 cm, siehe [[Formel 9]].
- **Ausgabe und Einheit:** `ruckenbreite_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** nur Obergrenze
  „bis zu 1/4" benannt.
- **Abhängigkeiten:** Verfahren „wie auf Seite 191 beschrieben" liegt nicht
  auf s193, nur zu verlinken, sobald erfasst; Ergebniswert wird in
  [[Formel 7]] als „derselbe Betrag wie am hinteren Armloch" weiterverwendet.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Verfahren von Seite 191 ist nicht Teil dieser Extraktion.

## Formel 5 – Ärmelpunkte verschieben

- **Quelle:** [`formeln_s193.md`](formeln_s193.md), Abschnitt 5
- **Buchfassung:**
  ```text
  Die Ärmelpunkte um 3/4 der Armlochvertiefung nach unten verschieben.
  ```
- **Technische Formel:**
  ```text
  aermelpunkt_neu = aermelpunkt_alt - (3/4) * armlochvertiefung   (Richtung: nach unten)
  ```
- **Eingaben und Einheiten:** `armlochvertiefung` (cm) — Beispielwert 2,5 cm,
  siehe [[Formel 9]].
- **Ausgabe und Einheit:** `aermelpunkt_neu` (Position, cm-Verschiebung).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Bruch 3/4, kein
  Spielraum im Wortlaut.
- **Abhängigkeiten:** [[Formel 9]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 6 – Seitennaht vorne an der Hüfte ausstellen

- **Quelle:** [`formeln_s193.md`](formeln_s193.md), Abschnitt 6
- **Buchfassung:**
  ```text
  Für gerade Seitennähte wird vorne an der Hüfte derselbe Betrag wie am
  vorderen Armloch ausgestellt und die Naht gerade zum Saum gezeichnet.
  ```
- **Technische Formel:**
  ```text
  huefte_vorne_ausstellung = delta   (delta aus Formel 3, vorderes Armloch)
  huefte_vorne_neu = huefte_vorne_alt + huefte_vorne_ausstellung
  ```
- **Eingaben und Einheiten:** `delta` (cm) aus [[Formel 3]].
- **Ausgabe und Einheit:** `huefte_vorne_neu` (cm); Naht gerade zum Saum
  gezeichnet (geometrische Zusatzbedingung, nicht beziffert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** kein eigener
  Zahlenwert — direkte Übernahme des Betrags aus Formel 3.
- **Abhängigkeiten:** [[Formel 3]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - „Derselbe Betrag" — exakte geometrische Übertragungsrichtung (z. B.
    entlang der Taillenlinie) nicht spezifiziert.

## Formel 7 – Seitennaht hinten an der Hüfte ausstellen

- **Quelle:** [`formeln_s193.md`](formeln_s193.md), Abschnitt 7
- **Buchfassung:**
  ```text
  Hinten wird an der Hüfte derselbe Betrag wie am hinteren Armloch + 1 cm
  ausgestellt und die Naht gerade gezeichnet.
  ```
- **Technische Formel:**
  ```text
  huefte_hinten_ausstellung = delta + 1 cm   (delta aus Formel 4, hinteres Armloch)
  huefte_hinten_neu = huefte_hinten_alt + huefte_hinten_ausstellung
  ```
- **Eingaben und Einheiten:** `delta` (cm) aus [[Formel 4]]; fester Zuschlag
  1 cm.
- **Ausgabe und Einheit:** `huefte_hinten_neu` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** fester Zuschlag
  „+ 1 cm", kein Bereich.
- **Abhängigkeiten:** [[Formel 4]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.

## Formel 8 – Taillierung der Seitennaht (Reihenfolgebedingung)

- **Quelle:** [`formeln_s193.md`](formeln_s193.md), Abschnitt 8
- **Buchfassung:**
  ```text
  Eine leichte Taillierung der SN (hier gestrichelt dargestellt) erfolgt bei
  Bedarf erst nach der Geradestellung der SN.
  ```
- **Technische Formel:**
  ```text
  taillierung_SN erlaubt, wenn geradestellung_SN abgeschlossen == true
  taillierung_SN optional ("bei Bedarf")
  ```
- **Eingaben und Einheiten:** keine (reine Reihenfolge-/Auswahlbedingung,
  kein Zahlenwert auf dieser Seite).
- **Ausgabe und Einheit:** —
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Ausführungsreihenfolge
  zwingend, Ausführung selbst optional.
- **Abhängigkeiten:** [[Formel 6]], [[Formel 7]] (Geradestellung der SN).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kein Maß für die Taillierung selbst auf dieser Seite angegeben.

## Formel 9 – Beispielwerte Armlochvertiefung, -verbreiterung und -auflockerung

- **Quelle:** [`formeln_s193.md`](formeln_s193.md), Abschnitt 9
- **Buchfassung:**
  ```text
  Für den legeren Jacken- bzw. Mantel-Grundschnitt wird hier der halbe
  Schnitt mit einer Armlochverbreiterung von 4 cm erweitert. Für den ganzen
  Schnitt beträgt die Erweiterung somit ca. 8 bis 8,5 cm, wenn man die
  Mehrweite an der hM hinzumisst.

  Die Armlochvertiefung beträgt 2,5 cm. Die Armloch-Auflockerung vorne ist
  hier 2,5 cm und hinten 1,5 cm.
  ```
- **Technische Formel:**
  ```text
  armloch_verbreiterung_halb = 4 cm
  armloch_verbreiterung_ganz ≈ 8 bis 8,5 cm
      (≈ 2 * armloch_verbreiterung_halb + mehrweite_hM, mehrweite_hM nicht beziffert)
  armlochvertiefung = 2,5 cm
  armloch_auflockerung_vorne = 2,5 cm
  armloch_auflockerung_hinten = 1,5 cm
  ```
- **Eingaben und Einheiten:** — (dies sind Modellbeispielwerte für G38, PK7
  aus PK3, keine abgeleiteten Größen).
- **Ausgabe und Einheit:** Basiswerte (cm) für [[Formel 1]], [[Formel 3]],
  [[Formel 4]], [[Formel 5]].
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „ca. 8 bis 8,5 cm"
  bleibt Bereich. Unabhängig nachgerechnet: 2 × 4 cm = 8 cm, liegt am
  unteren Rand des angegebenen Bereichs; die unbezifferte „Mehrweite an der
  hM" erklärt vermutlich die restliche Differenz zum oberen Bereichsende
  (bis 0,5 cm). Dies ist eine eigene Nachrechnung, kein Beleg für eine
  andere Buchformel.
- **Abhängigkeiten:** wird verwendet von [[Formel 1]], [[Formel 3]],
  [[Formel 4]], [[Formel 5]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - „Mehrweite an der hM" nicht beziffert.

## Formel 10 – Saumkürzung rechtwinklig zur Seitennaht

- **Quelle:** [`formeln_s193.md`](formeln_s193.md), Abschnitt 10
- **Buchfassung:**
  ```text
  10 Die Saume werden rechtwinklig zur SN abgewinkelt, wobei die Kürzungen
  an VT und RT jeweils identisch sein müssen.
  ```
- **Technische Formel:**
  ```text
  winkel(saumlinie, SN) = 90°
  kuerzung_VT = kuerzung_RT   (Bedingung: identisch)
  ```
- **Eingaben und Einheiten:** keine Maßangabe auf dieser Seite.
- **Ausgabe und Einheit:** Saumlinienverlauf an VT und RT (geometrische
  Bedingung, keine Längenangabe).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Gleichheitsbedingung
  zwischen VT- und RT-Kürzung; rechter Winkel zur SN.
- **Abhängigkeiten:** möglicher Bezug zu [[Formel 11]] (Schemafigur, Zahl
  „14"), nicht bestätigt.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Die vorangestellte Ziffer steht im OCR-Rohtext als „10"; laut offener
    Prüfstelle 3 in `s193.md` zeigt das Original an dieser Stelle den blauen
    Kreispunkt „14". Nicht still korrigiert.

## Formel 11 – Schemafigur zu „Optimierung der Saumform" (zeichnungsgebunden)

- **Quelle:** [`formeln_s193.md`](formeln_s193.md), Abschnitt 11
  (`skizzen_s193.json`, Region `img-1.jpeg`)
- **Buchfassung:**
  ```text
  Stilisierte Körperfigur mit drei waagerechten Maßpfeilen von links (88, 72,
  97) zu Kästchen rechts (14 [rot], sowie zweimal --- [unausgefüllt]); links
  außen eine senkrechte Klammer mit der Zahl 168.
  ```
- **Technische Formel:** nicht gebildet — keine textlich benannte
  Zuordnung von Zahl zu Bedeutung vorhanden.
- **Eingaben und Einheiten:** unklar (möglich, aber nicht bestätigt: 88/72/97
  als Körper- oder Konfektionsmaße, 168 als Körpergröße; keine Einheiten im
  Bild genannt).
- **Ausgabe und Einheit:** unklar; zwei Kästchen im Original offenbar
  unausgefüllt.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** —
- **Abhängigkeiten:** möglicher, nicht bestätigter Bezug zu [[Formel 10]]
  (Zahl „14").
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:**
  - Diese Region stammt allein aus der Bildbeschreibung in
    `skizzen_s193.json`, nicht aus einer eigenen Bildprüfung dieser
    Extraktion.
  - Ohne bestätigte Label-Zuordnung am Original wird hier keine Geometrie
    oder Fachregel erfunden (siehe `AGENT.md`, Freigabegrenze). Erst nach
    Werners Bestätigung der in `s193.md` (Prüfstelle 6) gelisteten Labels
    normalisierbar.
