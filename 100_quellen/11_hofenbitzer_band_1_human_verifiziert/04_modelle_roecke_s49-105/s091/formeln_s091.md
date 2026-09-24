# Formeln s091 – fototreue Extraktion (teils Walking Skeleton)

**Bereitschaftsstufe:** Die Seite trägt weiterhin den Status
`OCR-Rohfassung – noch nicht menschlich verifiziert` ([s091.md](s091.md)). Für
diese Seite ist genau eine Formelstelle von Werner am Original bestätigt (siehe
[s091.md](s091.md), Abschnitt „Vorab geklärte formel- und coderelevante
Stellen“): die `SaW`-Formel. Alle übrigen hier erfassten Formeln aus derselben
Berechnungsbox (`r_AnW`, `r_SaW`, „innerer/äußerer Umfang“, `NZg`) sind **nicht**
bestätigt und wurden auf ausdrücklichen Wunsch Werners trotzdem als
Walking-Skeleton-Durchlauf erfasst (Blocker übersprungen). Sie ersetzen keine
spätere Bestätigung am Original und dürfen nicht als menschlich verifiziert
gelten.

Die OCR-Rohfassung ([ocr_s091.md](ocr_s091.md)) enthält keine der folgenden
Formeln als Text – alle stehen ausschließlich in der Berechnungsbox der
Zeichnung [`skizzen/s091_skizze_02.png`](skizzen/s091_skizze_02.png)
(zeichnungsgebunden). Diese Zeichnung ist bereits in
[skizzen_s091.json](skizzen_s091.json) als Besitzerseiten-Ausschnitt „img-1.jpeg“
katalogisiert.

## 1. Innerer Umfang (Definition, zeichnungsgebunden)

Quelle: `skizzen/s091_skizze_02.png`, Berechnungsbox, Bildbeschriftung rechts
neben dem inneren Kreis.

```text
innerer Umfang = ¼ Ansatzweite (AnW) + 2× NZg
```

## 2. Äußerer Umfang (Definition, zeichnungsgebunden)

Quelle: `skizzen/s091_skizze_02.png`, Berechnungsbox, Bildbeschriftung rechts
neben dem äußeren Kreis.

```text
äußerer Umfang = ¼ Saumweite (SaW) + 2× NZg
```

Hinweis: Die Zeichnung zeigt einen Viertelkreis-Ausschnitt (Punkte 2, 3, 4);
„Umfang“ bezieht sich in dieser Bildbeschriftung auf den vollen Kreisumfang, von
dem AnW bzw. SaW jeweils ein Viertel ausmachen.

## 3. Nahtzugabe NZg (zeichnungsgebunden)

Quelle: `skizzen/s091_skizze_02.png`, Berechnungsbox, senkrechte Bildbeschriftung
neben der gestrichelten Doppellinie am inneren Kreisausschnitt.

```text
NZg = 2 × 1 cm = 2 cm
```

## 4. Radius r_AnW (zeichnungsgebunden)

Quelle: `skizzen/s091_skizze_02.png`, Berechnungsbox, linke Spalte, erster
Rechenblock.

```text
r_AnW = (AnW + NZg) : (2 · π)  : 4
      = (118 cm + 2 cm) : (2 · 3,14) : 4
      = 4,8 cm
```

## 5. Radius r_SaW (zeichnungsgebunden)

Quelle: `skizzen/s091_skizze_02.png`, Berechnungsbox, linke Spalte, zweiter
Rechenblock.

```text
r_SaW = r_AnW      + VoB
      = 4,8 cm      + 20 cm
      = 24,8 cm
```

## 6. Saumweite SaW – Werner-bestätigt

Quelle: [s091.md](s091.md), Abschnitt „Vorab geklärte formel- und
coderelevante Stellen“ (Werner-bestätigt am Original); dieselbe Formel steht
auch in der Berechnungsbox `skizzen/s091_skizze_02.png`, linke Spalte, dritter
Rechenblock (zeichnungsgebunden).

```text
SaW = ((2 × π × r_SaW) − NZg) × 4 = 615 cm
```

Hinweis: Die Zeichnung setzt den Faktor „· 4“ typografisch direkt hinter
`− NZg`; die von Werner bestätigte Klammerung in `s091.md` gruppiert ihn jedoch
um den gesamten Ausdruck `(2 · π · r_SaW − NZg)`. Diese Klammerung wird hier
unverändert aus der Werner-Bestätigung übernommen (siehe Nachrechnung in
[formeln_s091_normalisiert.md](formeln_s091_normalisiert.md)). Der Faktor 4
steht im Zusammenhang mit der Bildbeschriftung „Volant 4× zuschneiden“ neben
dem roten Klammerpfeil in derselben Zeichnung (vier Vollkreise, siehe auch
Bildunterschrift ☐3 „Modell und Schnittkonstruktion für einen Volant aus vier
Vollkreisen“ in [s091.md](s091.md)).

## Nicht als Formel erfasst

- „Volant 4× zuschneiden“ (Berechnungsbox, skizze_02): Produktionskennzeichen
  einer Stückzahl, hier nur als Kontext zum Faktor 4 in Formel 6 erwähnt, nicht
  als eigene Formel geführt.
- „VT 1× OSt“ und „Volant 1× OSt“ (skizze_04, skizze_05): reine Stückzahl-
  /Produktionskennzeichen, ausgeschlossen.
- Schrittkennungen ⑤–⑧ und Randzahl „36“ (skizze_04, skizze_05): Schrittzählung
  bzw. Seitenrandzahl, keine Rechenbeziehung.
- Volantbreite (VoB)-Beschriftung selbst (skizze_02): reiner Maßpfeil ohne
  eigene Rechenbeziehung; der Wert 20 cm ist bereits über Formel 5 erfasst.
- Fließtext „An einem geraden Rock-Grundschnitt … Den Saum und die Ansatznaht
  formen.“ ([ocr_s091.md](ocr_s091.md), Zeilen 20–23): rein verbale
  Konstruktionsanleitung ohne Zahl oder Rechenbeziehung.
