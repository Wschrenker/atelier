# Fachlich normalisierte Formeln — S. 494

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s494.md`
Originaltranskript: `s494.md`
Buchseite: Hofenbitzer, Band 1, S. 494

Die Seite eröffnet den Block „Sport · Wäsche · Unisex" mit dem Grundschnitt der einfachen Hose: einer hüftweiten Hose ohne Abnäher und ohne Verschluss, die durch einen Kordel- und/oder Gummibund an der Taille hält. Das Buch stellt sie ausdrücklich als von der Standardhose abweichend dar: „Es sind weniger Konstruktionsschritte erforderlich, sie weichen etwas von der Standardhose ab." Die extrahierten Kandidatenzeilen stammen aus der Konstruktionstabelle (`□2`) und aus den Konstruktionsschritten 2–4, 15 und 22. Die zugehörige Zeichnung `□3` liegt auf S. 495; die dort abgebildeten Beschriftungen sind in `formeln_s495_normalisiert.md` normalisiert.

## HOF-B1-S494-F01 — Kniehöhe aus der Schritthöhe

- **Fachlicher Zweck:** Die Kniehöhe der einfachen Hose als vier Zehntel der Schritthöhe bestimmen.
- **Quelle:** `formeln_s494.md`, Zeile 9; Originaltranskript `s494.md`, Zeile 50; Buchseite 494.
- **Originalbezeichnung:** `SrH : 10 · 4`.
- **Normalisierte Bezeichnung:** `kniehoehe_einfache_hose`

### Buchfassung

```text
| KnH | Kniehöhe | SrH : 10 · 4 | 32 |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `schritthoehe` | SrH | 80 | cm |

### Formel und Rechenschritte

```text
kniehoehe = (schritthoehe / 10) * 4
           = (80 cm / 10) * 4
           = 32 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `kniehoehe` | KnH | 32 | cm |

- **Abhängigkeiten:** SrH; der Wert 80 cm steht in der unmittelbar vorhergehenden Tabellenzeile des Originaltranskripts (`SrH = sTaH – SiH = 106 – 26`) und ist selbst nicht extrahiert.
- **Gültigkeitsbereich:** Konstruktionstabelle der einfachen Hose unisex, Größe 38, auf S. 494.
- **Technische Randbedingung:** Der Transkriptwert 80 cm dient nur als gekennzeichneter Rechenkontext; die Buchfassung bleibt auf die extrahierte KnH-Zeile beschränkt.
- **Offene Fragen oder Widersprüche:** Keine; der gedruckte Wert ist rechnerisch richtig.
- **Abgrenzung:** Die Beziehung ist wortgleich mit `HOF-B1-S109-F03` der Standardhose (`04_grundschnitte_hosen_s106-137/formeln_s109_normalisiert.md`). Sie erhält hier dennoch eine eigene ID, weil S. 494 eine eigene Konstruktionstabelle mit eigenem Maßsatz führt und die Seite keine Identität mit der Standardhose erklärt, sondern ausdrücklich Abweichungen ankündigt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Faktor als exakten Bruch `4/10` führen und erst bei der Ausgabe runden.

## HOF-B1-S494-F02 — Hinterhosenbreite als Grundwert

- **Fachlicher Zweck:** Den Grundwert der Hinterhosenbreite aus dem Viertel-Hüftumfang mit einem Zuschlag von 1 cm bestimmen.
- **Quelle:** `formeln_s494.md`, Zeile 19; Originaltranskript `s494.md`, Zeile 63; Buchseite 494.
- **Originalbezeichnung:** `¼ HüU +1 cm`.
- **Normalisierte Bezeichnung:** `hinterhosenbreite_grundwert_einfache_hose`

### Buchfassung

```text
| hHoB | Hinterhosenbreite | ¼ HüU +1 cm | ± +2 bis 3 | 25,2 → 26,5 |
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `viertel_hueftumfang` | ¼ HüU | 24,25 | cm |
| `breitenverschiebung` | `1 cm` | 1 | cm |

### Formel und Rechenschritte

```text
hinterhosenbreite_grundwert_exakt = 24,25 cm + 1 cm = 25,25 cm

gedruckter Wert = 25,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Exakt / gedruckt | Einheit |
|---|---|---|---|
| `hinterhosenbreite_grundwert` | hHoB vor Anwendung der Zugabe | 25,25 / 25,2 | cm |

- **Abhängigkeiten:** ¼ HüU = 24,25 cm aus der Hauptmaßtabelle des Originaltranskripts (`HüU = 97 cm`); die Tabellenzeile ist selbst nicht extrahiert.
- **Gültigkeitsbereich:** Konstruktionstabelle der einfachen Hose unisex, Größe 38, auf S. 494.
- **Technische Randbedingung:** Der Grundwert ist noch nicht die Konstruktionsbreite. Die Zugabe der vierten Tabellenspalte wird getrennt in `HOF-B1-S494-F03` behandelt.
- **Offene Fragen oder Widersprüche:** Das exakte Ergebnis endet auf `,25`, gedruckt ist `,2`. Die Quelle nennt keine Rundungs- oder Abschneideregel; exakte und gedruckte Werte bleiben getrennt. Dieselbe Abweichung ist bereits für die Standardhose in `HOF-B1-S109-F02` festgehalten.
- **Abgrenzung:** Die zugehörige vHoB-Zeile (`¼ HüU –1 cm`, `± +2 bis 2,5`, `23,2 → 25,5`) steht im Originaltranskript unmittelbar darüber (`s494.md`, Zeile 62), liegt aber nicht im Extrakt vor. Sie ist als Extraktionslücke vermerkt und wurde nicht als eigene Buchfassung ergänzt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Intern exakt rechnen; die Rundung nicht aus diesem Einzelbeispiel ableiten.

## HOF-B1-S494-F03 — Hinterhosenbreite mit Weiten-Zugabe

- **Fachlicher Zweck:** Die Konstruktions-Hinterhosenbreite der einfachen Hose durch eine Zugabe auf den Grundwert bestimmen.
- **Quelle:** `formeln_s494.md`, Zeile 19; Originaltranskript `s494.md`, Zeile 63; Buchseite 494.
- **Originalbezeichnung:** `± +2 bis 3` mit dem Ergebnis `25,2 → 26,5`.
- **Normalisierte Bezeichnung:** `hinterhosenbreite_mit_zugabe_einfache_hose`

### Buchfassung

```text
| hHoB | Hinterhosenbreite | ¼ HüU +1 cm | ± +2 bis 3 | 25,2 → 26,5 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hinterhosenbreite_grundwert` | hHoB laut Berechnungsspalte | 25,2 (gedruckt) / 25,25 (exakt) | cm |
| `hinterhosenbreiten_zugabe` | `+2 bis 3` | 2 bis 3 | cm |

### Formel und Rechenschritte

```text
allgemeine Form:
hinterhosenbreite_mit_zugabe = hinterhosenbreite_grundwert + hinterhosenbreiten_zugabe

Buchwerte nach der allgemeinen Form:
25,2 cm + 2 cm = 27,2 cm
25,2 cm + 3 cm = 28,2 cm

gedrucktes Ergebnis der Wertespalte:
25,2 cm → 26,5 cm     (entspricht + 1,3 cm)
```

### Ausgabe

| Technische Variable | Bedeutung | Gedruckt | Einheit |
|---|---|---:|---|
| `hinterhosenbreite_mit_zugabe` | Konstruktions-Hinterhosenbreite der einfachen Hose | 26,5 | cm |

- **Abhängigkeiten:** `HOF-B1-S494-F02`; gewählte Zugabe innerhalb des angegebenen Bereichs.
- **Gültigkeitsbereich:** Konstruktionstabelle der einfachen Hose unisex, Größe 38, auf S. 494.
- **Technische Randbedingung:** Zugabe und Ergebnis sind im Buch handschriftlich in Rot eingetragen (`s494.md`, Zeilen 65–66). Die Zugabe ist ein Bereich und muss als Modellparameter gewählt werden.
- **Offene Fragen oder Widersprüche:** **Widerspruch.** Der gedruckte Übergang `25,2 → 26,5` entspricht einer Zugabe von `1,3 cm` und liegt damit außerhalb des in derselben Zeile angegebenen Bereichs `+2 bis 3`. Die nicht extrahierte vHoB-Zeile derselben Tabelle ist dagegen konsistent (`23,2 → 25,5`, also `+ 2,3 cm` innerhalb von `+2 bis 2,5`). Die Quelle enthält keine Angabe, ob der Bereich, der Ausgangswert oder das Ergebnis unrichtig gedruckt ist; ein korrigierter Wert wurde nicht erfunden.
- **Status:** `gesperrt`
- **Hinweis für die spätere Python-Umsetzung:** Die allgemeine Form `Grundwert + Zugabe` ist implementierbar, das gedruckte Beispiel `26,5 cm` jedoch nicht daraus reproduzierbar. Den Buchwert `26,5 cm` nicht als Testerwartung verdrahten, solange der Widerspruch nicht durch die Quelle oder eine Fachentscheidung aufgelöst ist.

## HOF-B1-S494-F04 — Abtragung für den vorderen Hosenausschnitt

- **Fachlicher Zweck:** Den auf der Hüftlinie nach der Vorderhosenbreite zusätzlich abzutragenden Wert für den vorderen Hosenausschnitt bestimmen.
- **Quelle:** `formeln_s494.md`, Zeile 24; Originaltranskript `s494.md`, Zeile 84; Buchseite 494. Zeichnungsbeleg: `formeln_s495.md`, Zeile 14 (`s495.md`, Zeile 28).
- **Originalbezeichnung:** `vHoB : 4 + 0,5`.
- **Normalisierte Bezeichnung:** `vorderer_hosenausschnitt_einfache_hose`

### Buchfassung

```text
**2–4** Auf der Hüftlinie nacheinander die vHoB und vHoB : 4 + 0,5 abtragen, halbieren und die vHoM zeichnen.
```

```text
- `vHoB` / `vHoB : 4 + 0,5 cm`
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderhosenbreite` | vHoB | variabel | cm |
| `ausschnitt_zuschlag` | `0,5 cm` | 0,5 | cm |

### Formel und Rechenschritte

```text
abtrag_vorderer_hosenausschnitt = (vorderhosenbreite / 4) + 0,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abtrag_vorderer_hosenausschnitt` | nach der vHoB auf der Hüftlinie weiter abzutragender Wert | cm |

- **Abhängigkeiten:** vHoB der einfachen Hose. Der Berechnungsweg der vHoB (`¼ HüU –1 cm` mit Zugabe) steht im Originaltranskript, ist aber nicht extrahiert; siehe Abgrenzung in `HOF-B1-S494-F02`.
- **Gültigkeitsbereich:** Vorderhose des Grundschnitts der einfachen Hose auf S. 494 und S. 495.
- **Technische Randbedingung:** Die Abtragung erfolgt auf der Hüftlinie in derselben Richtung wie die vorangehende vHoB-Abtragung („nacheinander"). Der Schritttext auf S. 494 schreibt `0,5` ohne Einheit; die Zeichnungsbeschriftung auf S. 495 schreibt `0,5 cm`. Die Einheit cm ist damit durch die Quelle selbst belegt und nicht ergänzt.
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit. Anders als bei der Standardhose (`HOF-B1-S111-F01`) ist der Zuschlag hier ein fester Wert und kein figurabhängiger Bereich; S. 494 nennt keine Figurvarianten für diesen Schritt.
- **Abgrenzung:** Der Standardhosen-Schritt lautet `vHoB : 4 − 0 bis −0,5 cm` beziehungsweise `−0,5 bis −1 cm` oder `+0 bis +0,5 cm` und ist damit nicht wortgleich. Die einfache Hose erhält deshalb eine eigene ID und keinen Verweis auf `HOF-B1-S111-F01`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Betrag und Richtung trennen; den Zuschlag als festen Wert `0,5 cm` führen und nicht mit den figurabhängigen Bereichen der Standardhose vermischen.

## HOF-B1-S494-F05 — Halbierung der Hüftlinienstrecke zur Vorderhosen-Mitte

- **Fachlicher Zweck:** Die Vorderhosen-Mitte (`vHoM`, den Vorderhosenbruch) durch Halbierung der auf der Hüftlinie abgetragenen Gesamtstrecke bestimmen.
- **Quelle:** `formeln_s494.md`, Zeile 24; Originaltranskript `s494.md`, Zeile 84; Buchseite 494. Zeichnungsbeleg: `formeln_s495.md`, Zeile 22 (`s495.md`, Zeile 33).
- **Originalbezeichnung:** `halbieren und die vHoM zeichnen`; Zeichnungsmarken `½ · ½` an P4.
- **Normalisierte Bezeichnung:** `vorderhosenmitte_einfache_hose`

### Buchfassung

```text
**2–4** Auf der Hüftlinie nacheinander die vHoB und vHoB : 4 + 0,5 abtragen, halbieren und die vHoM zeichnen.
```

```text
- Halbierungsmarken `½ · ½` an P4 sowie `½ / ¼ / ½` am vorderen Hosenausschnitt
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `vorderhosenbreite` | vHoB | variabel | cm |
| `abtrag_vorderer_hosenausschnitt` | `vHoB : 4 + 0,5 cm` | aus `HOF-B1-S494-F04` | cm |

### Formel und Rechenschritte

```text
hueftlinienstrecke_gesamt = vorderhosenbreite + abtrag_vorderer_hosenausschnitt
abstand_vorderhosenmitte  = hueftlinienstrecke_gesamt / 2
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `abstand_vorderhosenmitte` | Abstand des Vorderhosenbruchs vom Anfangspunkt der Hüftlinienabtragung | cm |

- **Abhängigkeiten:** `HOF-B1-S494-F04` sowie die vHoB der einfachen Hose.
- **Gültigkeitsbereich:** Vorderhose des Grundschnitts der einfachen Hose, Konstruktionsschritte 2–4.
- **Technische Randbedingung:** Die vHoM ist laut `s495.md`, Zeile 24, mit dem Vorderhosen-Bruch gleichgesetzt; die Halbierung liefert einen Punkt, aus dem die Bruchlinie gezeichnet wird. Betrag und Linienkonstruktion sind zu trennen.
- **Offene Fragen oder Widersprüche:** S. 494 gibt nicht ausdrücklich an, **welche** Strecke halbiert wird. Grammatisch kann sich „halbieren" auf die Gesamtstrecke oder allein auf die zuletzt abgetragene Teilstrecke `vHoB : 4 + 0,5 cm` beziehen. Für die Gesamtstrecke spricht der gleich gebaute Schritt 11 der Standardhose (`s111.md`, Zeile 23: „Strecke von P7 bis P10 halbieren."), der ebenfalls die Summe aus vHoB und Ausschnittabtragung halbiert, sowie die Marke `½ · ½` an P4 auf S. 495. Beide Belege stammen jedoch aus einer anderen Seite beziehungsweise aus der Zeichnung und nicht aus dem Schritttext selbst.
- **Status:** `hypothetisch`
- **Hinweis für die spätere Python-Umsetzung:** Die Halbierung erst nach Bestätigung des Bezugs auf die Gesamtstrecke fest verdrahten; die Alternative — Halbierung nur der Ausschnitt-Teilstrecke — als abweichende Lesart im Modell vermerken.

## HOF-B1-S494-F06 — Mindest-Taillenweite der verschlusslosen Hose

- **Fachlicher Zweck:** Die untere Grenze der Taillenweite bestimmen, damit die Hose ohne Verschluss über die Hüfte gezogen werden kann.
- **Quelle:** `formeln_s494.md`, Zeile 34; Originaltranskript `s494.md`, Zeile 124; Buchseite 494. Zeichnungsbeleg: `formeln_s495.md`, Zeile 27 (`s495.md`, Zeile 38).
- **Originalbezeichnung:** `½ HüU + 2 cm` beziehungsweise `½ HüU + mind. 2 cm`.
- **Normalisierte Bezeichnung:** `taillen_mindestweite_einfache_hose`

### Buchfassung

```text
**22** Die Hose besitzt für das Anziehen keinen Verschluss zum Öffnen. Daher muss die Taillenweite so weit sein, dass die Hose über die Hüfte gezogen werden kann. Die TaW sollte mindestens dem ½ HüU + 2 cm entsprechen.
```

```text
- `+ hier weitermessen = ½ HüU + mind. 2 cm` (rot)
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `halber_hueftumfang` | ½ HüU | 48,5 | cm |
| `anziehzugabe` | `2 cm` | 2 | cm |

### Formel und Rechenschritte

```text
taillen_mindestweite = halber_hueftumfang + anziehzugabe

Bedingung: taillenweite >= taillen_mindestweite

Buchwerte der Konstruktionstabelle (HüU = 97 cm):
taillen_mindestweite = 48,5 cm + 2 cm = 50,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `taillen_mindestweite` | Mindestwert, den die konstruierte TaW erreichen muss | cm |

- **Abhängigkeiten:** ½ HüU aus der Hauptmaßtabelle; das Ergebnis der Taillenweiten-Kontrollmessung an der Konstruktion.
- **Gültigkeitsbereich:** Grundschnitt der einfachen Hose ohne Verschluss, S. 494 und S. 495.
- **Technische Randbedingung:** Die Beziehung ist eine Prüfbedingung, keine Konstruktionsabtragung. Sie wird gegen die gemessene Taillenweite geprüft; die Zeichnung auf S. 495 markiert die Messstelle mit `TaW zur Kontrolle messen +` und `+ hier weitermessen`, weil vorderes und hinteres Teilmaß zusammengezählt werden.
- **Offene Fragen oder Widersprüche:** Die beiden Buchstellen setzen das Wort „mindestens" unterschiedlich: Schritt 22 stellt die **Summe** unter den Vorbehalt („sollte mindestens … entsprechen"), die Zeichnungsbeschriftung stellt die **Zugabe** unter den Vorbehalt (`+ mind. 2 cm`). Rechnerisch ergibt sich in beiden Lesarten dieselbe untere Grenze von `½ HüU + 2 cm`; eine obere Grenze ist nicht belegt. Die Quelle nennt keine Regel, wie eine zu geringe Taillenweite auf die Erweiterungsschritte von S. 495 aufzuteilen ist.
- **Abgrenzung:** Die vier Erweiterungsschritte auf S. 495 (vM nicht einstellen, ca. 0,5 cm an P11, Gesäßwinkel 1° bis 2° senkrechter, vHoB und hHoB um bis zu 0,5 cm) liegen nicht im extrahierten Kandidatenbestand und sind hier nicht normalisiert.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Als Ungleichung `taillenweite >= 0.5 * hueftumfang + 2` implementieren und als Kontrolle nach der Konstruktion auswerten, nicht als Zuweisung an die TaW.

## Ausgeschlossene Kandidaten

| Extraktzeile | Anzahl | Ausschlussgrund |
|---|---:|---|
| 14 | 1 | `SaW`-Tabellenzeile: Bereichstabelle nach Hosenform (`Enge Hose 32 bis 40 · Standardhose 40 bis 48 · Weite Hose 48 bis 56`) mit dem gewählten Wert `50`; Auswahlangabe ohne Rechenoperation |
| 29 | 1 | Gewählter Gesäßwinkel `α = 77` in Schritt 15; Eingabewert ohne Berechnung |
| 39–40 | 2 | Redaktionelle Anmerkung des Transkripts zum fehlenden Gradzeichen; Notationshinweis, keine Buchformel |
| **Summe** | **4** | **1 Auswahltabelle + 1 Eingabewert + 2 redaktionelle Anmerkungszeilen** |

Zur ausgeschlossenen `SaW`-Zeile: Der gewählte Wert `50 cm` liegt im Bereich `48 bis 56` und damit in der Klasse „Weite Hose". Die Tabelle ordnet Bereiche zu, sie berechnet nichts; eine Auswahlregel innerhalb eines Bereichs nennt das Buch nicht. Der Wert `50` steht im Buch als ein über alle drei Zeilen gehender Eintrag.

Zum ausgeschlossenen Gesäßwinkel: Schritt 15 nennt `α = 77` einen „reduzierten" Winkel. Die zugehörige GeWi-Tabelle (`s494.md`, Zeilen 68–78) mit den Winkelwerten nach Sitzlänge und Gesäßform sowie der handschriftliche Rechenweg `82° -5° → 77°` liegen nicht im extrahierten Kandidatenbestand und wurden nicht als Buchfassung ergänzt. Dieselbe Behandlung hat bereits der gewählte Gesäßwinkel `84°` in `HOF-B1-S114`.

## Prüfhinweis zur Extraktionsgrenze

Das Originaltranskript `s494.md` enthält weitere rechenfähige Angaben, die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen und deshalb nicht als Buchfassungen ergänzt wurden:

- die Zeile `SrH | Schritthöhe | sTaH – SiH | 80` (Zeile 49) — Eingabe von `HOF-B1-S494-F01`;
- die Zeile `vHoB | Vorderhosenbreite | ¼ HüU –1 cm | ± +2 bis 2,5 | 23,2 → 25,5` (Zeile 62) — das Gegenstück zu `HOF-B1-S494-F02` und `F03`;
- die Halb- und Viertelwerte der Hauptmaßtabelle (Zeilen 29–34);
- die GeWi-Tabelle einschließlich `+1° bis +2°` für längs-elastischen Stoff (Zeilen 68–78);
- Schritt 10 (`um 1 cm parallel erweitern`), Schritt 11 (`2 cm ausstellen`), Schritt 14 (`hHB : 2 – 1 cm`) und Schritt 16 (`+ 1,5 cm`).

Besonders zu vermerken ist Schritt 14: Er nennt die Hinterhosenbreite abweichend `hHB`, während Tabelle, Schritt 13 und die Zeichnung auf S. 495 durchgehend `hHoB` schreiben. Beide Schreibweisen stehen so im Buch; die Beziehung `hHoB : 2 – 1 cm` liegt nicht im Extrakt vor und bleibt als Prüfstelle vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
