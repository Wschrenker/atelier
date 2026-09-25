# Formeln s218 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe nicht erreicht:** Laut [s218.md](s218.md) ist
die Seite insgesamt noch **OCR-Rohfassung – noch nicht menschlich
verifiziert**. Keine der fünf Rechenschritte (Prüfstelle 2 in `s218.md`) ist
bislang am Original bestätigt. Außerdem ist Seite 218 laut `s218.md` nicht Teil
der drei Kapitel, für die der Formelextraktions-Prompt eigentlich vorgesehen
ist (`03_grundschnitte_roecke_s32-48/`, `04_modelle_roecke_s49-105/`,
`07_grundschnitte_oberteile_s171-196/`) — diese Extraktion wurde auf
ausdrücklichen Wunsch Werners trotzdem als Walking-Skeleton-Durchlauf erstellt
(beide Blocker übersprungen) und beruht ausschließlich auf
[ocr_s218.md](ocr_s218.md) und [skizzen_s218.json](skizzen_s218.json). Sie
ersetzt keine spätere Bestätigung am Original und darf nicht als menschlich
verifiziert gelten.

## 1. Neues Armloch (AlU) — Summe aus vorderem und hinterem Armloch

Quelle: [ocr_s218.md](ocr_s218.md), Zeilen 21–25 (Schritt 1, Teilschritt 1).
Zeichnungsgebunden bestätigt durch [skizzen_s218.json](skizzen_s218.json),
`skizze_01` (rote Kurve, Beschreibung „AlU = 24,2 cm + 26 cm = 50,2 cm").

```text
AlU = vorderes Armloch + hinteres Armloch
hier = 24,2 cm + 26 cm = 50,2 cm
```

## 2. Ärmelkugelumfang des vorhandenen Ärmels (Messwert)

Quelle: `ocr_s218.md`, Zeilen 27–29 (Schritt 1, Teilschritt 2).
Zeichnungsgebunden bestätigt durch `skizzen_s218.json`, `skizze_02`
(Beschriftung „ÄkU_ALT messen = 48,5 cm").

```text
2 Den Ärmelkugelumfang (ÄkUAC) des vorhandenen Ärmels messen und am Ärmel
notieren:
hier ÄkUACT = 48,5 cm
```

Hinweis: Der Rohtext schreibt den Variablennamen uneinheitlich (`ÄkUAC` in
Zeile 27, `ÄkUACT` in Zeile 29). Beide Schreibweisen unverändert erhalten; laut
Zeichnungsbeschriftung in `skizze_02` und laut `s218.md` (Prüfstelle 2) lautet
die gemeinte Größe vermutlich `ÄkU_ALT` — am Original zu bestätigen, hier nicht
still korrigiert.

## 3. Neuer Ärmelkugel-Umfang (ÄkU-NEU) berechnen

Quelle: `ocr_s218.md`, Zeilen 37–40 (Schritt 2).

```text
ÄkUABC = AlU · (100% + EW in %) : 100%
hier = 50,2 cm · (100% + 7%) : 100%
= 50,2 cm · 1,07
ÄkUABC = 53,7 cm
```

Hinweis: Der Rohtext nennt an anderer Stelle (Zeile 35) für dieselbe Größe den
Variablennamen `ÄkUADC` statt `ÄkUABC`. Beide Schreibweisen unverändert
erhalten; laut `s218.md` (Prüfstelle 2) vermutlich `ÄkU_NEU` gemeint — am
Original zu bestätigen.

## 4. Fehlweite berechnen

Quelle: `ocr_s218.md`, Zeilen 44–48 (Schritt 3).

```text
Fehlweite = ÄkUACT - ÄkUABC
hier = 48,5 cm - 53,7 cm
= -5,2 cm → Fehlweite = 5,2 cm
```

Hinweis: Das gedruckte Zwischenergebnis `-5,2 cm` wird im selben Satz auf
`Fehlweite = 5,2 cm` (Betrag, ohne Vorzeichen) umgestellt. Beide Fassungen
nebeneinander unverändert erhalten, nicht stillschweigend vereinheitlicht.

## 5. Schulterpolster-Öffnung an der Ärmelkugel — Öffnungsweite vorne

Quelle: `ocr_s218.md`, Zeilen 55–59 (Schritt 5, erster Teil). Zeichnungsgebunden
bestätigt durch `skizzen_s218.json`, `skizze_01` (Beschriftung „⅓
Schulterpolster-Erhöhung vorne hier 0,8 cm" sowie „Schulterpolster-Erhöhung =
2,5 cm").

```text
3 Die Kugel wird waagerecht um ca. ⅓ der Polstererhöhung geöffnet.
hier Öffnung = 2,5 cm : 3 = 0,8 cm
```

## 6. Schulterpolster-Öffnung an der Ärmelkugel — Mehrweite gesamt

Quelle: `ocr_s218.md`, Zeilen 61–65 (Schritt 5, zweiter Teil). Zeichnungsgebunden
bestätigt durch `skizzen_s218.json`, `skizze_01` (Beschriftung „⅔
Schulterpolster-Erhöhung hinten hier 1,7 cm").

```text
Diese Öffnung erzielt insgesamt ca. die doppelte Mehrweite an der linken und
an der rechten Ärmelkugel:
hier
2 · ⅓ SuPoE = ⅔ SuPoE → ⅔ von 2,5 cm = ca. 1,7 cm
```

## 7. Einschnittlinien in den Ärmel — Kapplänge an der Ärmelkugel

Zeichnungsgebundene geometrische Anweisung (kein Rechenausdruck mit
Variablen). Quelle: `ocr_s218.md`, Zeilen 52–53 (Schritt 4). Zeichnungsgebunden
bestätigt durch `skizzen_s218.json`, `skizze_02` (Punkt ③, Scheresymbol, „ca.
5 cm").

```text
2 Die Armelkugel bei ca. 5 cm kappen und
wie dargestellt, bis zum Saum einschneiden.
```

Hinweis: „Armelkugel" ist vermutlich ein OCR-Fehllesung für „Ärmelkugel";
Rohtext unverändert erhalten.

## Nicht als Formel erfasst

- `skizzen_s218.json`, `skizze_01`: „Armlochauflockerung hier 1,5 cm" (grüner
  Pfeil, VT) — isoliertes Maß ohne im Rohtext oder in der Skizzenbeschreibung
  genannte Rechenbeziehung.
- `skizzen_s218.json`, `skizze_01`: „hier 0,7 cm" (orangefarbene Kurve, RT) —
  isoliertes Maß ohne genannte Rechenbeziehung.
- `ocr_s218.md`, Zeile 11: „Armlochumfang (50,2 cm) … Ärmelkugelumfang
  (48,5 cm)" im Einleitungstext — reine Wiederholung der in Abschnitt 1/2 oben
  bereits erfassten Werte, keine eigene Formel.
- Bildunterschriften „□1 Armlochauflockerung und Schulterpolstererhöhung" und
  „□2 Ärmelanpassung für Armlochauflockerung und Schulterpolstererhöhung"
  (`ocr_s218.md`, Zeilen 3, 69; `skizzen_s218.json`) — reine
  Abbildungsbeschreibungen ohne Zahlenwert.
- Rundmarken- und Kästchenziffern ①–④, □1–□3 als isolierte Zifferlabels ohne
  eigene Rechenbeziehung.
- Rote Randverweis-Kästchen „207"/„208" (siehe `s218.md`) — Seitenverweise,
  keine Formel.
- Fragmente der mitfotografierten Nachbarseite 219 am Ende von `ocr_s218.md`
  (Zeilen 73–83) — gehören nicht zur Besitzerseite, siehe `s218.md`.
