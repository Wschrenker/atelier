# Fachlich normalisierte Formeln — S. 495

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s495.md`
Originaltranskript: `s495.md`
Buchseite: Hofenbitzer, Band 1, S. 495

Die Seite zeigt die Zeichnung `□3` zum Grundschnitt der einfachen Hose und die vier Schritte, mit denen eine zu geringe Taillenweite nachträglich erweitert wird. Der Schritttext der Konstruktion steht auf S. 494. Die extrahierten Kandidatenzeilen sind ausschließlich Beschriftungen der Zeichnung, getrennt nach Vorderteil (VT) und Rückteil (RT). Zwei Beschriftungen tragen eigene Rechenbeziehungen dieser Zeichnung; drei weitere gehören zu Formeln, deren Schritttext auf S. 494 steht und die dort normalisiert sind.

## HOF-B1-S495-F01 — Höhenabstand der Hüftlinie

- **Fachlicher Zweck:** Den Abstand zur Hüftlinie aus dem Hüftumfang und einem festen Zuschlag bestimmen.
- **Quelle:** `formeln_s495.md`, Zeile 15; Originaltranskript `s495.md`, Zeile 29; Buchseite 495.
- **Originalbezeichnung:** `HüU : 20 + 3 cm`.
- **Normalisierte Bezeichnung:** `hueftlinienabstand_einfache_hose`

### Buchfassung

```text
- `HüU : 20 + 3 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | variabel | cm |
| `konstante_hueftlinienzugabe` | `3 cm` | 3 | cm |

### Formel und Rechenschritte

```text
hueftlinienabstand = (hueftumfang / 20) + 3 cm

Buchwert der Konstruktionstabelle auf S. 494 (HüU = 97 cm):
hueftlinienabstand = (97 cm / 20) + 3 cm = 4,85 cm + 3 cm = 7,85 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftlinienabstand` | Höhenabstand zwischen Schrittlinie und Hüftlinie im Grundgerüst | cm |

- **Abhängigkeiten:** HüU aus der Konstruktionstabelle auf S. 494.
- **Gültigkeitsbereich:** Grundgerüst der einfachen Hose, Vorderteil der Zeichnung `□3`.
- **Technische Randbedingung:** Der eingesetzte Wert `HüU = 97 cm` stammt aus der Konstruktionstabelle der Nachbarseite und dient nur als gekennzeichneter Rechenkontext; S. 495 druckt kein Ergebnis.
- **Offene Fragen oder Widersprüche:** Die Beschriftung nennt weder Ausgangs- noch Zielpunkt der Strecke. Sie steht in der Zeichnung zwischen Schritt- und Hüftlinie, der Schritttext auf S. 494 führt den Schritt jedoch nicht eigens auf; er ist Teil des summarisch gefassten Schritts 1 („Alle Längenmaße abtragen").
- **Abgrenzung:** Die Beziehung ist wortgleich mit `HOF-B1-S110-F01` der Standardhose (`04_grundschnitte_hosen_s106-137/formeln_s110_normalisiert.md`), wo sie ausdrücklich „von P4 aus nach oben" abgetragen wird. Sie erhält hier eine eigene ID, weil S. 494 und S. 495 keine Identität mit der Standardhose erklären, sondern ausdrücklich Abweichungen ankündigen, und weil die Punktnummerierung dieser Seite (`1–22`) eine eigene ist.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Betrag und Richtung trennen; die Zuordnung zu einem konkreten Punkt der eigenen Punktfolge dieser Seite nicht aus der Standardhose übernehmen.

## HOF-B1-S495-F02 — Halbe Hosenbeinweite an der Saumlinie

- **Fachlicher Zweck:** Den beidseitig vom Vorderhosenbruch abzutragenden Saumabstand aus der gesamten Saumweite bestimmen.
- **Quelle:** `formeln_s495.md`, Zeile 16; Originaltranskript `s495.md`, Zeile 30; Buchseite 495.
- **Originalbezeichnung:** `SaW : 4 – 0,5 cm` (an beiden Hosenbeinhälften).
- **Normalisierte Bezeichnung:** `saumabstand_einfache_hose`

### Buchfassung

```text
- `SaW : 4 – 0,5 cm` (an beiden Hosenbeinhälften)
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `saumweite` | SaW | 50 (Konstruktionstabelle S. 494) | cm |
| `saum_abzug` | `0,5 cm` | 0,5 | cm |

### Formel und Rechenschritte

```text
saumabstand_je_seite = (saumweite / 4) - 0,5 cm

Buchwert der Konstruktionstabelle auf S. 494 (SaW = 50 cm):
saumabstand_je_seite = (50 cm / 4) - 0,5 cm = 12,5 cm - 0,5 cm = 12 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `saumabstand_je_seite` | Abstand vom Vorderhosenbruch nach rechts und nach links an der Saumlinie | cm |

- **Abhängigkeiten:** Gewählte SaW aus der Konstruktionstabelle auf S. 494 und der bereits konstruierte Vorderhosenbruch (`HOF-B1-S494-F05`).
- **Gültigkeitsbereich:** Vorderteil des Grundschnitts der einfachen Hose, Zeichnung `□3`.
- **Technische Randbedingung:** Derselbe berechnete Betrag wird symmetrisch in beide Richtungen abgetragen; das ist mit „an beiden Hosenbeinhälften" belegt. Der eingesetzte Wert `SaW = 50 cm` stammt aus der Tabelle der Nachbarseite und dient nur als gekennzeichneter Rechenkontext; S. 495 druckt kein Ergebnis.
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit.
- **Abgrenzung:** Die Standardhose rechnet an derselben Stelle mit `SaW : 4 − 1 cm` (`HOF-B1-S111-F02`). Der Abzug der einfachen Hose ist mit `0,5 cm` halb so groß; beide Beziehungen sind nicht wortgleich und bleiben getrennt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Einen Betrag berechnen und geometrisch mit entgegengesetzten Richtungsvektoren anwenden; den Abzug `0,5 cm` nicht mit dem Standardhosenwert `1 cm` verwechseln.

## Bereits auf S. 494 normalisierte Beziehungen

Drei Beschriftungen der Zeichnung gehören zu Konstruktionsschritten, deren Schritttext auf S. 494 steht. Sie sind dort normalisiert, erhalten hier keine eigene Formel-ID und werden als Zeichnungsbeleg geführt.

| Beschriftung auf S. 495 | Extraktzeile | Normalisiert als | Fundstelle |
|---|---:|---|---|
| `vHoB` / `vHoB : 4 + 0,5 cm` | 14 | `HOF-B1-S494-F04` — Abtragung für den vorderen Hosenausschnitt | `formeln_s494_normalisiert.md` |
| Halbierungsmarken `½ · ½` an P4 | 22 | `HOF-B1-S494-F05` — Halbierung der Hüftlinienstrecke zur Vorderhosen-Mitte | `formeln_s494_normalisiert.md` |
| `+ hier weitermessen = ½ HüU + mind. 2 cm` | 27 | `HOF-B1-S494-F06` — Mindest-Taillenweite der verschlusslosen Hose | `formeln_s494_normalisiert.md` |

Die Zusammenführung ist durch die Seiten selbst gedeckt: Die Bildunterschrift `□3` auf S. 495 gehört zum Grundschnitt, dessen Schritte 1 bis 22 auf S. 494 stehen; die Punktnummern `1–22` der Zeichnung entsprechen diesen Schritten. Die Zeichnung liefert dabei zwei Angaben, die der Schritttext nicht hat: die Einheit `cm` hinter `0,5` in Schritt 2–4 und die Halbierungsmarken an P4.

Die in Zeile 22 mit erfasste Marke `½ / ¼ / ½` am vorderen Hosenausschnitt ist keine Rechenbeziehung mit benannter Eingabe und Ausgabe. Sie beschreibt die Formgebung der vorderen Ausschnittkurve zu P9, für die S. 494 in Schritt 9 nur „wie skizziert" angibt, und wurde nicht normalisiert.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | `VT` / `vM` / `vHoM = Vorderhosen-Mitte (-Bruch)` — Begriffsdefinition und Linienbezeichnung ohne Rechenoperation |
| 17 | 1 | `0,5 bis 1 cm` (an P8, Taille) · `0 bis 1 cm` (beidseits an der Knielinie, P7) — Bereichsangaben ohne benannte Eingabe und ohne benannte Ausgabe |
| 32 | 1 | `α = 77°` (an P15) — gewählter Gesäßwinkel; Eingabewert ohne Berechnung, zugleich Wiederholung von Schritt 15 auf S. 494 |
| 33 | 1 | `2 cm` (Ausstellung an P11) · `1 cm` (beidseits an Knielinie und Saumlinie) — feste Einzelwerte der Schritte 10 und 11 ohne Rechenoperation |
| **Summe** | **4** | **1 Definition + 1 Bereichsangabe + 1 Eingabewert + 1 Zeile fester Einzelwerte** |

Zum ausgeschlossenen Winkel: Die Zeichnung schreibt `α = 77°` mit Gradzeichen, Schritt 15 auf S. 494 schreibt `α = 77` ohne. Der Unterschied ist eine Notationsabweichung des Buches und ändert den Wert nicht; das Transkript hält ihn ausdrücklich fest.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s495.md` enthält weitere rechenfähige und bemaßte Angaben, die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen und deshalb nicht als Buchfassungen ergänzt wurden:

- die vier Erweiterungsschritte für eine zu geringe Taillenweite (Zeilen 11–14): `an der vM nicht einstellen`, `ca. 0,5 cm weiter ausstellen` an P11, `Gesäßwinkel um 1° bis 2° senkrechter`, `vHoB und hHoB um jeweils bis zu 0,5 cm vergrößern`;
- `sTaH – Kürzung der SiH für Taillenvertiefung` und `SiH – 0 bis – 4 cm (für Taillenvertiefung)` (Zeilen 25–26);
- `4 bis 8 cm` beidseits an der Saumlinie, P5 (Zeile 32);
- `hHoB : 2 – 1 cm` (Zeile 41) — die Hinterhosen-Entsprechung zu `HOF-B1-S494-F04`;
- `übertragen + 1,5 cm` (Zeile 45) und `Messung übertragen – 0,5 bis – 1 cm` (Zeile 47).

Die vier Erweiterungsschritte sind fachlich der Gegenpart zu `HOF-B1-S494-F06`: Sie beschreiben, was zu tun ist, wenn die Mindest-Taillenweite nicht erreicht wird. Sie bleiben als Prüfstellen für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
