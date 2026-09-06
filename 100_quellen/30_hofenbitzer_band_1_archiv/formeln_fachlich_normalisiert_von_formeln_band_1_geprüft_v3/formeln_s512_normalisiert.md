# Fachlich normalisierte Formeln — S. 512

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s512.md`  
Originaltranskript: `s512.md`  
Buchseite: Hofenbitzer, Band 1, S. 512

Die Tabelle enthält einen eigenen Maßsatz für das Sweatshirt. Bereiche, leere Ergebnisse und Vorzeichenwidersprüche bleiben sichtbar.

## Formelblöcke

## HOF-B1-S512-F01 — Brustweite
**Quelle:** `formeln_s512.md`, Zeile 19; `s512.md`, Zeile 23.

#### Buchfassung
```text
| BrU | Brustumfang | 88 | + | 12 | = | BrW | 100 | ½ 50; ¼ 25 |
```

#### Formel und Rechenschritte
```text
brustweite = brustumfang + brustweite_zugabe = 88 cm + 12 cm = 100 cm
halb_brustweite = 50 cm; viertel_brustweite = 25 cm
```

- **Ausgabe:** BrW 100 cm; halbe BrW 50 cm; viertel BrW 25 cm.
- **Eingaben/Abhängigkeiten:** BrU 88 cm; Zugabe 12 cm.
- **Gültigkeitsbereich:** Sweatshirt, Größe 38.
- **Offene Fragen oder Widersprüche:** keine.
- **Status:** `normalisiert`
- **Hinweis für Python:** Zugabe als expliziten Parameter führen.

## HOF-B1-S512-F02 — Armlochtiefe
**Quelle:** `formeln_s512.md`, Zeile 20; `s512.md`, Zeile 26.

#### Buchfassung
```text
| AlT | Armlochtiefe | 20,1 | + | 1 bis 3 | = | AlT+ | 22,1 |  |
```

#### Formel und Rechenschritte
```text
armlochtiefe_plus = armlochtiefe + armlochtiefe_zugabe
                  = 20,1 cm + (1 bis 3 cm)
```

- **Ausgabe:** AlT+, rechnerischer Bereich 21,1 bis 23,1 cm; gedruckt 22,1 cm.
- **Status:** `offen`
- **Offene Fragen:** Die Auswahl der Zugabe `2 cm` ist nicht als Regel belegt.

## HOF-B1-S512-F03 — Armdurchmesser
**Quelle:** `formeln_s512.md`, Zeile 27; `s512.md`, Zeile 29.

#### Buchfassung
```text
| ArD | Armdurchmesser | 9,3 | + | 3 bis 4 | = | ArD+ | 12,8 | ½ 6,4 |
```

#### Formel und Rechenschritte
```text
armdurchmesser_plus = 9,3 cm + (3 bis 4 cm)
```

- **Ausgabe:** ArD+, gedruckt 12,8 cm; halber Druckwert 6,4 cm.
- **Status:** `offen`
- **Offene Fragen:** Der gedruckte Wert entspricht einer ausgewählten Zugabe von 3,5 cm; die Auswahlregel fehlt.

## HOF-B1-S512-F04 — Brustpunktabstand
**Quelle:** `formeln_s512.md`, Zeile 28; `s512.md`, Zeile 30.

#### Buchfassung
```text
| BrPA | Brustpunktabstand = BrU/10 | 8,8 | + | 0,6 | = | BrPA+ | 9,4 |  |
```

#### Formel und Rechenschritte
```text
brustpunktabstand_plus = 8,8 cm + 0,6 cm = 9,4 cm
```

- **Ausgabe:** BrPA+ 9,4 cm.
- **Status:** `normalisiert`
- **Hinweis für Python:** BrPA kann zusätzlich aus BrU/10 geprüft werden; die Buchfassung verwendet 8,8 cm als Eingabe.

## HOF-B1-S512-F05 — Schulternahtlänge
**Quelle:** `formeln_s512.md`, Zeile 29; `s512.md`, Zeile 31.

#### Buchfassung
```text
| SuB | Schulterbreite | 12,2 | + | 1 bis 3 | = | SuNL | 14,2 |  |
```

#### Formel und Rechenschritte
```text
schulternahtlaenge = 12,2 cm + (1 bis 3 cm)
```

- **Ausgabe:** SuNL, gedruckt 14,2 cm.
- **Status:** `offen`
- **Offene Fragen:** Die gedruckte Auswahl `+2 cm` ist nicht verallgemeinerbar.

## HOF-B1-S512-F06 — Schulterwinkel
**Quelle:** `formeln_s512.md`, Zeile 30; `s512.md`, Zeile 32.

#### Buchfassung
```text
| SuWi | Schulterwinkel (in Grad, °) | 20° | − Auflockerung | 0 bis 2° | = | SuWi− | 18° |  |
```

#### Formel und Rechenschritte
```text
schulterwinkel_reduziert = 20° - (0 bis 2°)
```

- **Ausgabe:** SuWi−, gedruckt 18°.
- **Status:** `offen`
- **Offene Fragen:** Die gedruckte Auflockerung `2°` ist nur ein Beispielwert.

## HOF-B1-S512-F07 — Abnäherinhalt
**Quelle:** `formeln_s512.md`, Zeile 35; `s512.md`, Zeile 35.

#### Buchfassung
```text
|  | Differenz VL − RüL | 3,7 | − | 3 bis 4 | = | Abnäherinhalt | 0,7 bis -0,3 |  |
```

#### Formel und Rechenschritte
```text
abnaeherinhalt = laengendifferenz_vl_ruecklaenge - (3 bis 4 cm)
                = 3,7 cm - (3 bis 4 cm)
                = 0,7 bis -0,3 cm
```

- **Ausgabe:** Abnäherinhalt 0,7 bis −0,3 cm.
- **Status:** `normalisiert`
- **Offene Fragen:** Auswahl innerhalb des Bereichs bleibt offen.

## HOF-B1-S512-F08 — Ärmellänge
**Quelle:** `formeln_s512.md`, Zeilen 36 und 48; `s512.md`, Zeilen 36 und 57.

#### Buchfassung
```text
| ArL | Armlänge | 60 | − | -4 | = | Ärmellänge ÄL | 56 |  |
- Ärmellänge = Armlänge − ⅔ Ärmelbündchen-Breite (hier: 60 cm − ⅔ · 6 cm = 60 cm − 4 cm = 56 cm)
```

#### Formel und Rechenschritte
```text
aermellaenge = armlaenge - (2 / 3 * aermelbuendchen_breite)
              = 60 cm - (2 / 3 * 6 cm)
              = 56 cm
```

- **Ausgabe:** ÄL 56 cm.
- **Status:** `normalisiert`
- **Hinweis für Python:** Die Vorzeichenannotation `-4` technisch als Abzug von 4 cm führen.

## HOF-B1-S512-F09 — Oberarmweite, unausgefüllte Zeile
**Quelle:** `formeln_s512.md`, Zeile 37; `s512.md`, Zeile 37.

#### Buchfassung
```text
| OaU | Oberarmumfang | 28 | + | --- | = | Oberarmweite OaW | --- |  |
```

- **Ausgabe:** keine.
- **Status:** `offen`
- **Offene Fragen:** Zugabe und Ergebnis fehlen; nichts ergänzen.

## HOF-B1-S512-F10 — Ärmelsaumweite
**Quelle:** `formeln_s512.md`, Zeile 38; `s512.md`, Zeile 38.

#### Buchfassung
```text
| HgU | Handgelenkumfang | 16 | − | 8 | = | Ärmelsaumweite ÄSaW | 24 |  |
```

#### Formel und Rechenschritte
```text
aermelsaumweite = 16 cm - 8 cm = 8 cm
```

- **Ausgabe:** gedruckt ÄSaW 24 cm.
- **Status:** `gesperrt`
- **Offene Fragen oder Widersprüche:** Das gedruckte Ergebnis passt zu `16 + 8`, nicht zum gedruckten Minuszeichen. Keine Reparatur ableiten.

## HOF-B1-S512-F11 — Armloch-Teilung
**Quelle:** `formeln_s512.md`, Zeile 53; `s512.md`, Zeile 64.

#### Buchfassung
```text
- ½ ArD+ − 1 cm / ½ ArD+
```

- **Ausgabe:** zwei nicht benannte Teilstrecken.
- **Status:** `offen`
- **Offene Fragen:** Referenzpunkt und genaue Zielstrecken fehlen.

## HOF-B1-S512-F12 — Modelllänge abzüglich Bundbreite
**Quelle:** `formeln_s512.md`, Zeile 58; `s512.md`, Zeile 67.

#### Buchfassung
```text
- Modelllänge − geplante Bundbreite (hier 57 cm − 6 cm = 51 cm)
```

#### Formel und Rechenschritte
```text
rumpflaenge_ohne_bund = 57 cm - 6 cm = 51 cm
```

- **Ausgabe:** 51 cm.
- **Status:** `normalisiert`
- **Hinweis für Python:** Bundbreite als gesonderte Eingabe führen.

### Ausgeschlossene Kandidaten

| Extraktbereich | Anzahl | Ausschlussgrund |
|---|---:|---|
| Zeilen 9 und 14 | 2 | Rubrik und handschriftliche Metadaten, keine Berechnung |
| Zeile 43 | 1 | Redaktionelle Tabellenanmerkung; die Folgen für ArL und HgU sind in F08/F10 dokumentiert |
| **Summe** | **3** | **Metadaten und Prüfnotiz ausgeschlossen** |
