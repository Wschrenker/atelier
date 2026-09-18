# Tabellen s019 (OCR-Rohfassung)

Aus dem Layout-JSON der Mistral-OCR (`ocr_s019_raw.json`, Blöcke `tbl-0` bis
`tbl-10`). Die Seite ist eine ausfüllbare Maßtabelle (Formular); nahezu der
gesamte Seiteninhalt besteht aus diesen elf Tabellenblöcken plus wenigen
Fließtextzeilen dazwischen (siehe `ocr_s019.md`).

## tbl-0 – Kopf: Name/Datum, Körpermaße, KöH, gBrU, TaU, HüU

|  Maßtabelle Maße in cm | Name |   |
| --- | --- | --- |
|  | Datum |  |
|   |   | Körpermaße | Bemerkungen: |
|  KöH | Körperhöhe |   |   |
|  gBrU | gemessener Brustumfang |   |
|  TaU | Taillenumfang waagerecht |   | ½ | ¼ |
|  HüU | Hüftumfang waagerecht |   | ½ | ¼ |

**Auffällig:** Im Foto stehen „Maßtabelle" (groß, linke Spalte) und „Maße in
cm" (klein, darunter) als zwei getrennte Beschriftungen; die OCR hat sie zu
einer Zellenzeile zusammengezogen. Gegen das Original prüfen, ob das die
Kopfzeile korrekt wiedergibt oder ob „Maßtabelle" eher eine eigene
Seitenüberschrift außerhalb der Tabelle ist.

## tbl-1 – Bundumfang, Bundabstände

|  BuU | Bundumfang |   | ½ | ¼ |   |
| --- | --- | --- | --- | --- | --- |
|  BuA | Bundabstände → Ta-Band | v | h | r | l  |

## tbl-2 – Taillenhöhen

|  TaH | Taillenhöhen vom Boden zum Taillen-Band | v | h | optimale | mTaH  |
| --- | --- | --- | --- | --- | --- |
|   |   | r | l |   | sTaH  |

**Auffällig:** Die OCR gibt „Taillen Band" ohne Bindestrich wieder; im Foto
steht vermutlich „Taillen-Band" wie sonst im Buch üblich. Am Original prüfen.

## tbl-3 – Halslochbreite, Rückenlänge, Brusttiefe, Vorderlänge

|  HaU | Halsansatzumfang |   | HaU : 6 + 0,5 cm = |   | Halslochbreite | HlB |   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  gRüL | gemessene Rückenlänge |   | ± Taillenschräglage hinten |   | = Rückenlänge | RüL |   |
|  gBrT | gemessene Brusttiefe | r | l | ∅ | gBrT − HlB = | Brusttiefe | BrT  |
|  gVL | gemessene Vorderlänge | r | l | ∅ | gVL − HlB = |   |   |
|   |   |   | ± Taillenschräglage vorne |   | = Vorderlänge | VL |   |

**Auffällig:** Die OCR schreibt die Kürzel-Spalte in den beiden mittleren
Zeilen als „hIB" (Kleinbuchstabe h, Großbuchstabe I) statt wie in der
Kopfzeile als „HlB" (Halslochbreite). Vermutlich dieselbe l/I-Verwechslung
wie bei „AlT"/„ALT" auf Seite 9 (siehe `tabellen_s009.md`). Am Original
klären, ob überall „HlB" gedruckt ist.

## tbl-4 – Armlochtiefe, Rückenbreite, Armdurchmesser, Brustbreite, Brustumfang

|  gAlT | gemessene Armlochtiefe |   | Kontrolle: (KöH + BrU) :10 − 6 cm = |   |   | Armlochtiefe | AlT |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  gRüB | gemessene Rückenbreite |   |   | gRüB : 2 = |   | RüB |   |   |
|  gArD | gemess. Armdurchmesser | r | l | ∅ |   | ArD |   |   |
|  gBrB | gemessene Brustbreite |   |   | gBrB : 2 = |   | BrB |   |   |
|  BrU | Brustumfang waagerecht |   | RüB + ArD + BrB = ½ BrU |   |   | Σ = |  · 2 = | BrU  |

**Auffällig:** Die OCR schreibt in Spalte 1 „gAIT" bzw. in der Ergebnisspalte
„AIT" (Großbuchstabe I) statt „gAlT"/„AlT" – dieselbe l/I-Verwechslung wie
bei `tbl-3` und bei „AlT" auf Seite 9. In der letzten Zeile (BrU) hat die
OCR „Σ = -2 =" als eine Zelle gelesen; im Foto wirkt das nach zwei getrennten
Zellen „Σ =" und „· 2 =" (Malpunkt, kein Minus) – vermutlich dieselbe
Malpunkt/Minus-Verwechslung wie bei „mal in Berechnungen" auf Seite 9. Beides
am Original prüfen.

## tbl-5 – Obere Rückenbreite/Brustbreite, Ober-/Unterbrustabstand, Unterbrustumfang

|  oRüB | obere Rückenbreite |   | ½  |
| --- | --- | --- | --- |
|  oBrB | obere Brustbreite |   | ½  |
|  oBrA | Oberbrustabstand → BrP |   |   |
|  uBrU | Unterbrustumfang |   | ½  |
|  uBrA | Unterbrustabstand → BrP |   |   |

## tbl-6 – Schulterwinkel

|  SuWi | Schulterwinkel | r | l  |
| --- | --- | --- | --- |

## tbl-7 – Armlänge, Oberarm-, Handgelenk-, Hand-, Armansatzumfang, Schulterbreite

|  ArL | Armlänge |   |
| --- | --- | --- |
|  OaU | Oberarmumfang |   |
|  HagU | Handgelenkumfang |   |
|  HaU | Handumfang |   |
|  AraU | Armansatzumfang |   |
|  SuB | Schulterbreite |   |

**Auffällig:** Das Kürzel „HaU" wird auf dieser Seite doppelt vergeben – in
`tbl-0`/`tbl-3` für „Halsansatzumfang", hier für „Handumfang". Am Original
prüfen, ob das im Buch tatsächlich so steht (Kürzelkollision) oder ob eines
der beiden Kürzel von der OCR falsch gelesen wurde.

## tbl-8 – Hüfttiefe bis Unterleibumfang

|  HüT | Hüfttiefe |   |
| --- | --- | --- |
|  SiH | Sitzhöhe |   |
|  OsU | Oberschenkelumfang |   |
|  KnU | Knieumfang |   |
|  uKnU | unterer Knieumfang |   |
|  WaU | Wadenumfang |   |
|  FeU | Fesselumfang |   |
|  RiU | Ristumfang |   |
|  UlU | Unterleibumfang |   |

**Auffällig:** Die OCR schreibt das letzte Kürzel „UIU" (Großbuchstabe I);
vermutlich „UlU" (dieselbe l/I-Verwechslung wie oben). Am Original prüfen.

## tbl-9 – Optimale Balance nach Brustumfang

|  Brustumfang BrU | optimale Balance Bal  |
| --- | --- |
|  80 bis 89 | + 3,5  |
|  90 bis 99 | + 4,0  |
|  100 bis 109 | (BrU − 100) : 10 + 4,5  |
|  110 bis 119 | (BrU − 100) : 10 + 5,0  |
|  120 bis 129 | (BrU − 100) : 10 + 5,5  |
|  130 bis 150 | (BrU − 100) : 10 + 6,0  |
|  optimale Balance | Bal  |

**Auffällig:** In der Zeile „100 bis 109" liest die OCR „(2rU − 100) : 10 +
4,5" statt „(BrU − 100) : 10 + 4,5" wie in den vier folgenden Zeilen. Sieht
nach einem OCR-Lesefehler aus (Br → 2r); am Original bestätigen, dass dort
ebenfalls „BrU" steht.

## tbl-10 – Individuelle Balance

|   | VL |   |
| --- | --- | --- |
|   | minus RüL | −  |
|  individuelle Balance = |   |   |
