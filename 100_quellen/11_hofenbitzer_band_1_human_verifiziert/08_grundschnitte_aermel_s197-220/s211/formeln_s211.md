# Formeln s211 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert` ([s211.md](s211.md)).
Kein einziger formel- oder coderelevanter Punkt ist bisher von Werner am
Original bestätigt, insbesondere nicht die dort offenen Prüfstellen 3 und 8
(Zahlenwerte und Bruchangaben in den unteren Skizzen; Frage, ob die Seite
überhaupt eine Formel enthält). Diese Extraktion wurde auf ausdrücklichen
Wunsch Werners trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker
übersprungen) und ersetzt keine spätere Bestätigung der formelrelevanten
Stellen am Original.

`s211.md` vermerkte bislang „keine eigene Formel im Sinne der
Formelextraktion". Dieser Befund wird hier revidiert: Zwei zahlenbasierte,
zeichnungsgebundene Rechenbeziehungen wurden gefunden – nicht im
Schrittfließtext, sondern ausschließlich als Bildbeschriftung von
[`skizzen/s211_skizze_04.png`](skizzen/s211_skizze_04.png) und
[`skizzen/s211_skizze_05.png`](skizzen/s211_skizze_05.png). Der OCR-Lauf hat auf
dieser Seite keine Bildregionen erkannt (`images: []`); die folgenden Stellen
stammen daher aus direkter Sichtprüfung der beiden Skizzenausschnitte, nicht
aus `ocr_s211.md` selbst, auch wenn derselbe Wortlaut zusätzlich lose im
OCR-Fließtext (Absätze 7 und 8) auftaucht.

Anmerkung zu Lesarten: Die eigene Bildprüfung liest in beiden Skizzen deutlich
„ÄkLi" (nicht „ÄkLJ") und „schmaler Ärmel / G 38 / PK 3" auf drei Zeilen (nicht
„schnaler Ärmel G.38 PK.3"). Das deckt sich mit dem in `s211.md` bereits
vermerkten OCR-Verdacht (Prüfstelle 5), ist aber weiterhin keine Bestätigung
durch Werner am Original – nur ein Abgleich mit dem fotografierten Bildausschnitt.

## 1. Ärmelkugel vergrößern (Einhalteweite erhöhen) – Skizze 04

Quelle: [`skizzen/s211_skizze_04.png`](skizzen/s211_skizze_04.png)
(zeichnungsgebunden, Bildunterschriften am Punkt ② und an den beiden Punkten
①), lose auch als Fließtext in `ocr_s211.md`, Zeilen 29–30 (Absatz 7).

```text
Die Kugel um ca. ¼ der fehlenden EW erhöhen (hier 0,4 cm)

Öffnung um ca. ½ der fehlenden EW (hier 0,7 cm)
```

Kontext auf derselben Skizze (Teilebezeichnung, kein eigener Rechenwert):

```text
ÄkLi
schmaler Ärmel
G 38
PK 3
ca. 5 cm bis 10 cm
□4 Ärmel vergrößern
```

Hinweis: „ca. 5 cm bis 10 cm" markiert auf der Skizze die Lage der
Scheren-/ZP-Schnittpunkte an den Seitennähten (Abstand von der Achsellinie),
nicht die Größe der Kugel- oder Öffnungs-Zugabe selbst; hier als Kontext
mitgeführt, nicht als eigene Formel gewertet (vgl. Prüfstelle 3 in `s211.md`).

## 2. Ärmelkugel verkleinern (Einhalteweite verringern) – Skizze 05

Quelle: [`skizzen/s211_skizze_05.png`](skizzen/s211_skizze_05.png)
(zeichnungsgebunden, Bildunterschriften am Punkt ② und an den beiden Punkten
①), lose auch als Fließtext in `ocr_s211.md`, Zeilen 37–38 (Absatz 8).

```text
Die Kugel um ca. ¼ der überschüssigen EW verkürzen (hier 0,25 cm)

Zulegen um ca. ½ der überschüssigen EW (hier 0,5 cm)
```

Kontext auf derselben Skizze (Teilebezeichnung, kein eigener Rechenwert):

```text
ÄkLi
schmaler Ärmel
G 38
PK 3
ca. 5 cm bis 10 cm
□5 Ärmel verkleinern
```

Zusätzlich nur in der Skizze sichtbar, nicht im OCR-Text erfasst: ein separater
Doppelpfeil mit der Bezeichnung „ca. 5 cm" über die volle Kugelhöhe (zwischen
Schulterpunkt und ÄkLi-Linie). Kein Rechenbezug erkennbar, daher nicht als
Formel geführt, nur als Anmerkung für Werner festgehalten.

## Nicht als Formel erfasst

- `ocr_s211.md`, Zeile 40 (isoliertes „☐2" zwischen den Skizze-05-Zeilen):
  taucht in der Skizze selbst nicht auf; vermutlich OCR-Störung aus Absatz 2
  weiter oben, nicht still entfernt, aber nicht in die Formel übernommen.
- Absätze 1, 3, 5, 6, 9, 10 (Zeilen 8–9, 14–15, 21–23, 25–27, 47–51): reine
  Konstruktionsanweisungen bzw. Übungs-/Reiterüberschriften ohne Zahlen- oder
  Rechenbeziehung.
- Absatz 4 (Zeilen 17–19) mit dem Verweis „Seite 117, ☐1": Konstruktionshinweis
  ohne eigenen Zahlenwert auf dieser Seite; Querverweis, keine Formel.
- Skizzen 01–03 (ÄSaW-Abnäher-Varianten „verringern/vergrößern/maximieren"):
  laut Bildbeschreibung in `skizzen_s211.json` Silhouetten mit Abnäherlinien,
  aber ohne dort sichtbare Zahlenwerte; nicht in Formeln aufgenommen.
