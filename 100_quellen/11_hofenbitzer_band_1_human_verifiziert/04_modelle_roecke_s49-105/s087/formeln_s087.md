# Formeln s087 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s087.md](s087.md)). Werner bestätigte am Original bislang nur die
Überschrift „Faltenabstand an der Taille reduzieren" sowie die Variable
`FaA_Ta` (siehe [s087.md](s087.md), Abschnitt „Vorab geklärte formel- und
coderelevante Stellen"). Alle übrigen hier erfassten Stellen – insbesondere
sämtliche ausschließlich zeichnungsgebundenen Werte – sind nicht bestätigt.
Diese Extraktion wurde auf ausdrücklichen Wunsch Werners trotzdem als
Walking-Skeleton-Durchlauf erstellt (Blocker übersprungen: „formeln seite 87
überspringe die blocker. das ist ein walking skeleton."). Sie ersetzt keine
spätere Bestätigung der formelrelevanten Stellen am Original und darf nicht
als menschlich verifiziert gelten.

Die Zeichnungsstellen stammen aus
[`skizzen/s087_skizze_01.png`](skizzen/s087_skizze_01.png) („☐2 Falten
einzeichnen", siehe [skizzen_s087.json](skizzen_s087.json)). Die Bounding Box
dieses Ausschnitts stammt aus derselben OCR-Antwort wie `ocr_s087_raw.json`.

## 1. Faltenabstand an der Taille – Zielwert FaA_Ta

Quelle: `ocr_s087.md`, Zeile 22 (Überschrift, OCR-Fassung „# 3 Falten Falten
in der Falte reduzieren", von Werner am Original korrigiert zu
„Faltenabstand an der Taille reduzieren") und Zeile 24 (Schrittfließtext);
zusätzlich zeichnungsgebunden: `skizzen/s087_skizze_01.png` (Label „FaA_Ta"
am oberen Rand der Faltenspalten, Kreis ⑦ links und Kreis ⑦/① rechts, sowie
Beschriftung „Taillenlinie = Taillennaht = Faltenansatznaht").

```text
2 An der Taillenlinie die Faltenabstände auf den FaA., verringern.
```

Hinweis: Werner bestätigte am Original ausdrücklich nur die Überschrift
„Faltenabstand an der Taille reduzieren" und die Variable `FaA_Ta`. Der
übrige Wortlaut dieses Satzes (inklusive der OCR-Schreibweise „FaA.,") ist
nicht eigens bestätigt. Die OCR-Schreibweise wird hier unverändert
wiedergegeben, nicht still korrigiert.

## 2. Faltenabstand an der Hüftlinie – Bezugsgröße FaA_HU (nur Zeichnung)

Quelle: ausschließlich zeichnungsgebunden, `skizzen/s087_skizze_01.png`,
Label „Falten-abstand FaA_HU" (Kreis ③), unterhalb der Beschriftung
„Faltentiefe" (Kreis ②), links im Bild auf Höhe der rechts beschrifteten
„Hüftlinie".

```text
Falten-
abstand
FaA_HU
```

Hinweis: Im OCR-Text von s087 kommt `FaA_HU` nicht vor; diese Stelle ist
ausschließlich zeichnungsgebunden und bislang nicht am Original bestätigt.

## 3. Nahtzugabe an der Taillennaht – ca. 2 bis 3 cm (nur Zeichnung)

Quelle: ausschließlich zeichnungsgebunden, `skizzen/s087_skizze_01.png`,
Beschriftung oben im Bild, zwischen der linken „FaA_Ta"-Spalte und der
Markierung ⑥ am rechten Bildrand, oberhalb der Gesamtbeschriftung „offene
Weite".

```text
zunächst ca. 2 bis 3 cm NZg an der Taillennaht
```

Hinweis: Ausschließlich zeichnungsgebunden, nicht im OCR-Fließtext von s087
enthalten und nicht am Original bestätigt. „NZg" ist auf dieser Seite nicht
ausgeschrieben; die Abkürzung wird hier nicht aufgelöst.

## Nicht als Formel erfasst

- Zeichnungslabel „offene Weite" (oberer Bildrand, `skizzen/s087_skizze_01.png`):
  benannte Gesamtstrecke ohne angegebenen Zahlenwert und ohne Rechen- oder
  Auswahlbeziehung auf dieser Seite.
- Zeichnungslabel „Faltentiefe" (Kreise ② und ⑤, `skizzen/s087_skizze_01.png`):
  benannte Strecke ohne angegebenen Zahlenwert.
- Zeichnungslabel „Falteninhalt" (Kreis ④, `skizzen/s087_skizze_01.png`) und
  OCR-Zeile 26 („Den Falteninhalt mit Legepfeilen … markieren"): benannte
  Strecke bzw. Markieranweisung ohne Zahlenwert oder Rechenbeziehung.
- Zeichnungslabel „VT+RT 1× OSt" (Mitte, `skizzen/s087_skizze_01.png`):
  Teile-/Produktionskennzeichen, ausdrücklich ausgeschlossen.
- OCR-Zeile 20 („☐ 3 Für eine rationelle Fertigung kann eine Schablone …"):
  Beschreibung ohne Zahl oder Rechenbeziehung.
- OCR-Zeile 25 („4 Nähte bis zur gewünschten Tiefe formen. Die endgültige
  Form entsteht bei Maßkleidung durch Abstecken bei der Anprobe."): „gewünschte
  Tiefe" ist keine im Buch angegebene Zahl oder Bereichsregel, sondern ein
  Verweis auf die Anprobe.
- OCR-Zeile 28 („1 Beim Zusammennähen von Stoffstreifen …"): Verarbeitungsregel
  ohne Zahl.
- Abschnitte „Anprobe" (Zeilen 32–37) und „Verarbeitungshinweise" (Zeilen
  41–45): ausschließlich Verarbeitungsanweisungen ohne Zahlen oder
  Rechenbeziehungen.
- Die in [s087.md](s087.md) bereits dokumentierte Unsicherheit der
  Schrittkennungen (OCR `2`, `4` vs. Foto-Kreisziffern `7`, `8`, `9`) wird
  hier nicht erneut als eigene Formel geführt, da sie keine Rechenbeziehung
  betrifft.
