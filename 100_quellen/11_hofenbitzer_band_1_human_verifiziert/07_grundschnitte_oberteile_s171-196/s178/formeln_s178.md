# Formeln s178 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s178.md](s178.md)). Nur die vier in s178.md unter „Vorab geklärte formel- und
coderelevante Stellen" gelisteten Werte sind von Werner am Original bestätigt
(AlT/AlT+, hSuNL, Sollwert der Mehrweite, ½ BrW). Alle übrigen Werte dieser
Extraktion stammen unbestätigt aus [`tabellen_s178.md`](tabellen_s178.md) bzw.
[`ocr_s178.md`](ocr_s178.md). Diese Extraktion wurde auf ausdrücklichen Wunsch
Werners trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker
übersprungen). Sie ersetzt keine spätere vollständige Bestätigung der
formelrelevanten Stellen am Original und darf nicht als menschlich verifiziert
gelten.

Diese Datei ersetzt die frühere, rein mechanisch gezogene Fassung (ungefilterte
Zeilen mit Rechenzeichen) durch eine nach Rechenbeziehung geordnete fototreue
Extraktion.

## 1. Brustweite, Taillenweite, Hüftweite mit Zugabe

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 1 (`tbl-0.md`), Zeilen
12–14.

```text
BrU | Brustumfang | 88 | + | 6 = | BrW | 94 | ½ 48
TaU | Taillenumfang | 68 | + | 4 = | TaW | 72 | ½ 36
HüU | Hüftumfang | 97 | + | 4 = | HüW | 101 | ½ 50,5
```

Hinweis zu ½ BrW: Werner bestätigte am Original `BrW 94; ½ = 47`
([s178.md](s178.md)). Die OCR-Rohfassung von Tabelle 1 zeigt stattdessen
`½ 48`; Tabelle 3 (Kontrollzeile Σ = ½ BrU) zeigt bereits in der OCR-Rohfassung
`½ BrW = 47`, also übereinstimmend mit Werners Bestätigung. Der Wert `48` in
Tabelle 1 wird hier als abweichende OCR-Rohfassungsstelle unverändert
mitgeführt, nicht still korrigiert.

Hinweis zu TaU: Laut Fließtext (`ocr_s178.md`, Zeile 29) ist der verwendete
TaU „hier um 4 cm kleiner als in der Größentabelle für die Größe 38" – reine
Erläuterung zum Ausgangswert, keine eigene Rechenbeziehung.

## 2. Armlochtiefe (AlT / AlT+)

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 2 (`tbl-1.md`), Zeile
18; Bestätigung in [s178.md](s178.md) unter „Vorab geklärte … Stellen".

Bestätigte Buchfassung:

```text
AlT 20,1 + 1,3 = AlT+ 21,4
```

Abweichende OCR-Rohfassung (unbestätigt, nicht als Buchwert verwendet):

```text
AlT | Armlochtiefe | 20,1 | + | 1,3 = | AlT+ | 21,8
```

## 3. Rückenbreite (RüB / RüB+)

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 3 (`tbl-2.md`), Zeile
25. Unbestätigt.

```text
RüB | Rückenbreite (½) | 16,5 | + | 0,5 = | RüB+ | 17
```

## 4. Armdurchmesser (ArD / ArD+) mit Viertel- und Drittelwert

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 3 (`tbl-2.md`), Zeile
27. Unbestätigt.

```text
ArD | Armdurchmesser | 9,3 | + | 1,5 = | ArD+ | 10,8 | ¼ 2,7 ⅓ 3,6
```

## 5. Brustbreite (BrB / BrB+)

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 3 (`tbl-2.md`), Zeile
28. Unbestätigt.

```text
BrB | Brustbreite (½) | 18,2 | + | 1 = | BrB+ | 19,2
```

## 6. Kontrolle Σ = ½ BrU

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 3 (`tbl-2.md`), Zeile
29. Unbestätigt, stimmt aber zahlenmäßig mit dem bestätigten ½ BrW aus
Abschnitt 1 überein.

```text
Kontrolle: Σ = ½ BrU | 44 | + | 3 = | ½ BrW | 47
```

## 7. Schulterbreite und Schulternahtlänge vorn (SuB / SuNL)

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 4 (`tbl-3.md`), Zeile
33. Unbestätigt.

```text
SuB | Schulterbreite | 12,2 | + | 0,3 = | SuNL | 12,5
```

## 8. Hintere Schulternahtlänge (hSuNL)

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 4 (`tbl-3.md`), Zeile
34; Bestätigung in [s178.md](s178.md) unter „Vorab geklärte … Stellen".

Bestätigte Buchfassung:

```text
hSuNL = SuNL + Einhalteweite
12,5 + 0,7 = 13,2
```

OCR-Rohfassung derselben Zeile (Einhalteweite als Bereich beschrieben, Rechenzeichen unklar abgesetzt):

```text
hSuNL | hintere Schulternahtlänge | SuNL - Einhalteweite 0,5 cm bis 1 cm | + | 0,7 = | hSuNL | 13,2
```

Hinweis: Die OCR-Zeile nennt „0,5 cm bis 1 cm" als Bereich für die
Einhalteweite allgemein; der hier tatsächlich verrechnete Wert ist 0,7 cm.

## 9. Schulterwinkel (SuWi)

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 4 (`tbl-3.md`), Zeile
35. Unbestätigt, OCR erkennbar gestört.

```text
SuWi | Schulterwinkel (in Grad, °) | 20° - Alf- lockenrig | - | --- = | SuWi | 20°
```

Hinweis: „Alf- lockenrig" ist keine erkennbare deutsche Fachbezeichnung;
OCR-Rauschen vermutet, aber nicht korrigiert oder aufgelöst.

## 10. Balance (RüL, VL, individuelle und korrigierte Balance, Toleranzregel)

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 5 (`tbl-4.md`), Zeilen
42–45; dazu Fließtext `ocr_s178.md`, Zeile 43. Unbestätigt.

```text
RüL | Rückenlänge (waagerechte Taille) | 41,6 | ± | --- = | RüL | 41,6
VL | Vorderlänge (waagerechte Taille) | 45,3 | ± | --- = | VL | 45,3
Differenz VL - RüL = | Individuelle Balance = | 3,7 | korrigierte Balance = |   |   | 3,7
Bal | optimale Balance aus Maßtabelle | 3,5 | Optimale und korrigierte Balance müssten jetzt sehr ähnlich sein. (x 1 cm Toleranz, nur wenn kein Figurproblem zu beobachten ist)
```

```text
Die Differenz von 0,2 cm zwischen individueller und optimaler Balance liegt
innerhalb der Toleranz und wird vernachlässigt. Somit werden die RüL und die
VL unkorrigiert verwendet.
```

Hinweis: „x 1 cm Toleranz" in der Tabellenzeile ist vermutlich eine
OCR-Wiedergabe von „± 1 cm Toleranz"; hier fototreu mit „x" übernommen, nicht
still korrigiert.

## 11. Taillenumfall und Hüftfeldbetrag (TaAf, HüFb)

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 6 (`tbl-5.md`), Zeilen
52–53; dazu Fließtext `ocr_s178.md`, Zeile 45. Unbestätigt, ohne Zahlenbeispiel
auf dieser Seite.

```text
TaAf | Taillenumfall | gemessene TaB | - ½ TaW | =
HüFb | Hüftfeldbetrag | gemessene HüB | - ½ HüW | =
```

```text
Die Berechnungen TaAf und HüFb werden erst im Laufe der Konstruktion für den
Oberteil-Grundschnitt vorgenommen.
```

## 12. Mehrweite im Armloch

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 6 (`tbl-5.md`), Zeile
54. Unbestätigt, ohne Zahlenbeispiel; Abkürzungen `VAlU`/`hAlU`/`AraU` nicht
anderweitig auf dieser Seite aufgelöst.

```text
Mehrweite im Armloch |   | VAIU + hAIU | - AraU | =
```

## 13. Sollwert der Mehrweite

Quelle: [`tabellen_s178.md`](tabellen_s178.md), Tabelle 6 (`tbl-5.md`), Zeile
55; Bestätigung in [s178.md](s178.md) unter „Vorab geklärte … Stellen".

Bestätigte Buchfassung:

```text
Sollwert der Mehrweite = 2 × Zugabe zur AlT
```

Abweichende OCR-Rohfassung (unbestätigt, nicht als Buchwert verwendet):

```text
Sollwert der Mehrweite |   | = 2 - Zugabe zur AlT (Toleranz +2 cm bis -1 cm) = |   |  | Nur bei Oberteilen mit Brustabnäher!
```

Der Toleranzbereich „+2 cm bis -1 cm" sowie der Hinweis „Nur bei Oberteilen mit
Brustabnäher!" sind nicht Teil von Werners Bestätigung und bleiben unbestätigt.

## Nicht als Formel erfasst

- Tabelle 1, Zeile 11 (KöH Körperhöhe 168): reiner Körpermaßwert ohne
  Rechenbeziehung.
- Tabelle 2, Zeilen 19–20 (HüT, MoL, BrT, HlB): reine Maßwerte ohne
  Rechenbeziehung.
- Tabelle 6, Zeilen 49–51 (oBrB, oBrA, uBrU, uBrA): alle Werte `---`, auf
  dieser Seite nicht ausgefüllt.
- Bildunterschriften und Schrittnummerierung (`☐1a`–`☐1d`, `☐2`) sowie reine
  Modell-/Kapitelbezeichnungen: keine Zahl, keine Rechenbeziehung.
