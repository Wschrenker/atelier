# Formeln s216 – fototreue Extraktion (noch nicht menschlich verifiziert)

**Status: Walking Skeleton – OCR-/Eigenlesung, noch nicht von Werner bestätigt.**

Seite 216 gehört zu `08_grundschnitte_aermel_s197-220/`, einer Kategorie, für
die der Formelextraktions-Prompt laut `AGENT.md` nicht ausdrücklich benannt
ist (dort nur `03_grundschnitte_roecke_s32-48/`, `04_modelle_roecke_s49-105/`,
`07_grundschnitte_oberteile_s171-196/`). Diese Datei entsteht auf Werners
ausdrücklichen Wunsch als Walking Skeleton ("tue es bitte #"), obwohl weder
die Kategorie-Zuordnung noch die einzelnen Stellen bereits am Original
bestätigt sind. Alle Angaben unten sind entsprechend vorläufig.

`s216.md` hatte ursprünglich vermerkt, die Seite enthalte keine eigene
Formel (Prüfstelle 8 dort). Bei genauerem Abgleich mit der Definition dieses
Prompts (Bereiche, Grenzwerte, Bedingungen, geometrische Beziehungen) enthält
der Fließtext und die Zeichnung ☐6 jedoch mehrere quantifizierte
Konstruktionsangaben. Diese werden hier erfasst; rein narrative
Konstruktionsschritte ohne Zahlenbezug (z. B. „Die Kugelnaht außen über die
Öffnungen formen") bleiben außen vor.

## 1. Schulterpolster-Erhöhung (Definition als Messdifferenz)

Quelle: [`ocr_s216.md`](ocr_s216.md), Zeile 45 (Abschnitt „1 Bestimmung der
Schulterpolster-Erhöhung").

```text
Über das Schulterpolster wird von Nadel zu Nadel gemessen. Dann nimmt man das Schulterpolster ab und misst dieselbe Strecke ohne Schulterpolster. Die Differenz beider Maße ist die benötigte Schulterpolster-Erhöhung.
```

## 2. Waagerechte Öffnung am Ärmelkugelansatz

Quelle: [`ocr_s216.md`](ocr_s216.md), Zeile 57 (Abschnitt „3 Ärmelanpassung
für identische Einhalteweite").

```text
An der waagerechten Öffnungen um ca. (1/2) Schulterpolster-Erhöhung = ungebahre Polsterdicke öffnen.
```

Hinweis: „ungebahre" ist eigene, unbestätigte Lesung; vermutlich „ungefähre"
(siehe `s216.md`, „Bekannte auffällige Stellen im Rohtext").

Zusätzlicher, zeichnungsgebundener Beleg (eigene Lesung des Bildausschnitts,
`geprueft: false` laut [`skizzen_s216.json`](skizzen_s216.json), skizze_07,
Label ☐6, Kreise 6/7 oben, waagerechter Pfeil oberhalb der vÄP-Linie):

```text
Polsterdicke oder ca. 1/3 Schulterpolster-Erhöhung öffnen
```

Widerspruch: Fließtext nennt „1/2 Schulterpolster-Erhöhung", die Zeichnung an
derselben Stelle „1/3 Schulterpolster-Erhöhung". Bereits in `s216.md`,
Prüfstelle 3, vermerkt. Beide Fassungen bleiben hier unverändert
nebeneinander stehen.

## 3. Senkrechte Öffnung unterhalb vÄP

Quelle: [`ocr_s216.md`](ocr_s216.md), Zeile 58.

```text
Fur einen proportional ausgewogenen Armel jeweils die halbe waagerechte Öffnung (1/2) Polsterdicke auch senkrecht öffnen.
```

Zusätzlicher, zeichnungsgebundener Beleg (eigene Lesung, `geprueft: false`
laut `skizzen_s216.json`, skizze_07, Kreis 7 unterhalb der vÄP-Linie,
senkrechter Pfeil):

```text
öffnen um ca. 1/6 Schulterpolster-Erhöhung (= 1/2 Polsterdicke)
```

## 4. Saum-Öffnung (Bezug auf Folgeseite)

Quelle: [`ocr_s216.md`](ocr_s216.md), Zeile 58.

```text
Am Saum kann (wie auf folgender Seite) derselbe Betrag geöffnet werden (hier allerdings ohne Öffnung dargestellt).
```

Zusätzlicher, zeichnungsgebundener Beleg (eigene Lesung, `geprueft: false`
laut `skizzen_s216.json`, skizze_07, unterer Bildbereich):

```text
ggf. max. wie oben öffnen für Saum-Erweiterung
1/2  1/2   (Beschriftung „üb" links, „me" rechts der Ärmelunternaht)
```

Abhängigkeit: „wie auf folgender Seite" verweist auf Seite 217 (noch nicht
bearbeitet); nur zu verlinken, sobald diese Seite vorliegt, nicht zu
kopieren.

## 5. Teilungsverhältnis der Schulterpolster-Erhöhung auf VT/RT

Zeichnungsgebundener Beleg (eigene Lesung, `geprueft: false` laut
`skizzen_s216.json`), gleichlautend in zwei Zeichnungen:

Skizze 05 (☐4 „Geringe Schulterpolster-Erhöhung"):

```text
1/3 Schulterpolster-Erhöhung vorne
2/3 Schulterpolster-Erhöhung hinten
```

Skizze 06 (☐5 „Größere Schulterpolster-Erhöhung mit Schulterverbreiterung"),
dieselbe 1/3-zu-2/3-Aufteilung an VT/RT, zusätzlich eine dritte, in der
Zeichnung nicht bezifferte Teilfläche (Kreismarkierung 3) für die
Schulterverbreiterung:

```text
1/3 Schulterpolster-Erhöhung vorne
2/3 Schulterpolster-Erhöhung hinten
```

## 6. Schulterverbreiterung bei größerer Erhöhung

Quelle: [`ocr_s216.md`](ocr_s216.md), Zeile 50 (Abschnitt „2
Schulterpolster-Erhöhung am Schnitt").

```text
D5 Bei einer größeren Erhöhung kann gleichzeitig eine leichte Schulter-Verbreiterung von wenigen Millimetern am VT und am RT identisch vorgenommen werden.
```

Hinweis: „D5" ist OCR-Rohtext für die im Original vermutlich als Kreis „2"
stehende Markierung (siehe `s216.md`, „Bekannte auffällige Stellen im
Rohtext"). Kein Zahlenwert für „wenige Millimeter" im Text; entspricht der
unbezifferten dritten Teilfläche (Kreis 3) in Skizze 06, siehe Abschnitt 5
oben.

## Nicht erfasst

- „Die Armelkugel bei ca. 5 cm kappen" (Zeile 55): isoliertes Maß ohne
  Rechen- oder Auswahlbeziehung zu anderen Werten dieser Seite; dient nur als
  Schnittpunkt, von dem aus die Öffnungen in Abschnitt 2–3 oben gemessen
  werden (Kreis 4 in Skizze 07).
- Rein narrative Konstruktionsanweisungen ohne Zahlenbezug (z. B. „Die
  Kugelnaht außen über die Öffnungen formen. Die Kugel erhält für das Polster
  die nötige Breite und Mehrlänge.", Zeile 59).
- Die Kästchen- und Kreisnummerierungen selbst (☐1–☐6, Kreise 1–8) sind
  Bezeichner, keine Formeln.

## Offene Prüfung

Keine der obigen Stellen ist am Original bestätigt. Vor jeder Normalisierung
über den Walking-Skeleton-Stand hinaus müssen sie wie in `s216.md`,
Prüfstellen 1–7, von Werner geprüft werden – insbesondere der Widerspruch
„1/2" (Fließtext) vs. „1/3" (Zeichnung) bei der waagerechten Öffnung
(Abschnitt 2 oben) und die eigene Lesung der Zeichenausschnitte skizze_05,
skizze_06 und skizze_07, die noch nicht in `skizzen_s216.json` als geprüft
markiert sind.
