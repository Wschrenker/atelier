# Formeln s176 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert` ([s176.md](s176.md)).
Von Werner am Original bestätigt ist bisher nur die Spaltenfolge
`BrU | TaU | HüU | AlT | RüB | ArD | BrB | SuB` sowie die Überschrift
„BrW-Zugaben (für ½ Schnitt)" in Tabelle 2 (Abschnitt 3 unten); diese
Bestätigung betrifft ausdrücklich nur diese Tabellenstelle. Alle übrigen
Zahlenwerte, Tabellenzellen und Textstellen dieser Extraktion sind **nicht**
bestätigt. Diese Extraktion wurde auf ausdrücklichen Wunsch Werners trotzdem
als Walking-Skeleton-Durchlauf erstellt (Blocker übersprungen) und beruht auf
[`ocr_s176.md`](ocr_s176.md), [`tabellen_s176.md`](tabellen_s176.md) und der
Bildregionen-Beschreibung in [`skizzen_s176.json`](skizzen_s176.json). Sie
ersetzt keine spätere Bestätigung der übrigen formelrelevanten Stellen am
Original und darf nicht als menschlich verifiziert gelten.

## 1. Rechenbeispiel PK5 – BrW-Zugabe

Quelle: `ocr_s176.md`, Zeilen 15–19 (Fließtext neben den Piktogramm-Ziffern
„1"/„2", die im Rohtext ohne Kreissymbol erscheinen).

```text
1 Die Ziffern einer Passformklasse (PK) geben die jeweilige die Zugabe für den halben Brustumfang an; hier z.B. für eine enge Jacke:

2

PK5 2 × 5 cm = 10 cm BrW-Zugabe
```

Hinweise:

- OCR-Zeile 15 enthält die Dopplung „geben die jeweilige die Zugabe" (vermutlich
  Buchtext „geben jeweils die Zugabe" o.ä.), unverändert übernommen, nicht
  still korrigiert.
- Widerspruch, sichtbar dokumentiert statt aufgelöst: Der Fließtext spricht von
  der „Zugabe für den **halben** Brustumfang", während der Wert 10 cm in
  Tabelle 2 (Abschnitt 3) für PK5 in der ersten Zugabenspalte steht, die dort
  laut OCR-Kopfzeile „Zugaben (für den **ganzen** Schnitt)" überschrieben ist.

## 2. Tabelle 1 – Auswahltabelle Passformklasse → Anwendung/Modelle

Quelle: `tabellen_s176.md`, Tabelle 1 (`tbl-0.md`), Zeilen 7–19.

```text
| Anwendung | Passformklasse | Modelle Woche / Kleid / Bluse | Jacke | Weste / Mantel |
| extrem k�rpernah | 0 | Rademoden, W�sche Korsage Grund, Nieder | | |
| | 1 | | | |
| | 2 | | | |
| sehr k�rpernah | 3 | Kleid Kleid, Bluse eng | Jacke sehr eng | Weste eng |
| | 4 | | | |
| k�rpernah | 5 | Kleid, Bluse halbweit Kleid, Bluse weit | Jacke eng Jacke halbweit | Weste halbweit Mantel eng |
| | 6 | | | |
| locker | 7 | Kleid, Bluse sehr weit | Jacke weit Jacke halbweit | Mantel halbweit Mantel weit |
| | 8 | | | |
| k�rperfern | 9 | | Jacke sehr weit Jacke sehr weit | Mantel weit Mantel sehr weit |
| | 10 | | | |
```

Hinweise:

- Auswahltabelle: die Passformklasse (0–10) wählt eine Anwendungskategorie und
  je Sparte (Modelle/Jacke/Weste-Mantel) eine oder mehrere Modellbezeichnungen.
- Zeilen mit Passformklasse 1, 2, 4, 6, 8, 10 sind in der OCR-Rohfassung leer;
  laut `s176.md` (Prüfstelle 6) vermutlich verbundene Zellen der jeweils
  vorhergehenden „Anwendung"-Zeile im Original, am Original zu bestätigen.
- OCR-Zeichenfehler `�` (statt `ö`/`ü`) unverändert aus `tabellen_s176.md`
  übernommen.

## 3. Tabelle 2 – Zugabentabelle (Passformklasse → Zugabenwerte)

Quelle: `tabellen_s176.md`, Tabelle 2 (`tbl-1.md`), Zeilen 23–36.

```text
| Passformklasse | Zugaben (für den ganzen Schnitt) | | | | BrW-Zugaben (für 15 Schnitt) | | | Gr.B |
| | BrW | TaU | HäU | AIT | HäU | ArD | BrA | |
| 0 | 0 | 0 | 0 | 0 - 0,5 | 0 | 0 | 0 - 0,4 | 0 |
| 1 | 2 | 0 - 2 | 0 - 2 | 0,2 - 0,7 | 0,1 | 0,3 | 0,6 | 0,1 |
| 2 | 4 | 2 - 4 | 2 - 4 | 0,5 - 1 | 0,3 | 0,9 | 0,8 | 0,2 |
| 3 | 6 | 4 - 6 | 4 - 6 | 1,3 | 0,5 | 1,5 | 1 | 0,3 |
| 4 | 8 | 4 - 8 | 4 - 8 | 1,7 | 0,8 | 2 | 1,2 | 0,4 |
| 5 | 10 | 8 - 12 | 6 - 8 | 2,1 | 1,1 | 2,5 | 1,4 | 0,5 |
| 6 | 12 | 8 - 16 | 6 - 10 | 2,5 | 1,4 | 3 | 1,6 | 0,6 |
| 7 | 14 | 12 - 16 | 8 - 12 | 3 | 1,6 | 3,6 | 1,8 | 0,7 |
| 8 | 16 | 12 - 20 | 8 - 16 | 3,5 | 1,8 | 4,2 | 2 | 0,8 |
| 9 | 18 | 12 - 20 | 10 - 20 | 4 | 2 | 5 | 2 | 0,9 |
| 10 | 20 | 16 - 24 | 10 - 24 | 4,5 | 2,2 | 5,8 | 2 | 1 |
```

Bestätigt (`s176.md`, „Vorab geklärte formel- und coderelevante Stellen"): Die
zweite Kopfzeile lautet tatsächlich `BrU | TaU | HüU | AlT | RüB | ArD | BrB |
SuB`, und die Überschrift der letzten Spaltengruppe lautet „BrW-Zugaben (für ½
Schnitt)" — nicht die oben roh übernommene OCR-Fassung „BrW | TaU | HäU | AIT |
HäU | ArD | BrA" bzw. „für 15 Schnitt". Die Spaltenposition bleibt dabei
unverändert; nur die Bezeichnungen wurden ersetzt. Diese Bestätigung betrifft
ausschließlich die Spaltenbezeichnungen, nicht die Zahlenwerte der Tabelle.

Hinweis: OCR-Zeichenfehler `�` (statt `ö`/`ü`) im rohen Zitat unverändert
übernommen.

## 4. Piktogramm-Beispiel Größe 38, PK5 (zeichnungsgebunden)

Quelle: `skizzen_s176.json`, Region `img-0.jpeg` (Bildbeschreibung, nicht
selbst pixelgenau nachgeprüft); Bildunterschrift ☐1 in `ocr_s176.md`, Zeile 48;
Legende der Ziffern 2–8 in `ocr_s176.md`, Zeilen 31–40.

```text
Körpermaße-Piktogramm: Körpersilhouette mit Kreispunkten 1-8, Zahlen 168/88/72/97 und Zugabewerten 5/10/10/7 (Bildunterschrift ☐1)
```

```text
☐1 Passform-Piktogramm der Damen-Größe 38 mit Ergänzung der Passformklasse und der Weitenzugaben für eine enge Jacke der PK 5
```

```text
2 Körperhöhe (KöH)
3 Brustumfang (BrU)
4 Taillenumfang (TaU)
5 Hüftumfang (HüU)

6 zum Brustumfang
7 zum Taillenumfang
8 zum Hüftumfang
```

Hinweise:

- Die vier Körpermaßzahlen 168/88/72/97 liegen bei den Ziffern 2–5 (KöH, BrU,
  TaU, HüU); die Zuordnung Ziffer→Zahl ist eine Lesart der Bildbeschreibung,
  am Original zu bestätigen (siehe `s176.md`, Prüfstelle 5).
- Die vier Zugabewerte 5/10/10/7 sind vier Werte für drei Zugabe-Ziffern
  (6, 7, 8); welcher der vier Werte wohin gehört (z.B. ob „5" die Passformklasse
  selbst statt ein vierter Zugabewert ist) ist aus der Bildbeschreibung allein
  nicht eindeutig und wird hier nicht aufgelöst.
- Zeichnungsgebunden: keine der vier Zahlen und keiner der vier Zugabewerte ist
  bisher am Original bestätigt.

## Nicht als Formel erfasst

- Zeilen 9–13 (Einleitungstext zu Zugaben allgemein): keine Zahl, keine
  Rechenbeziehung.
- Zeile 21 (Absatz über uneinheitliche Verwendung von Passformklassen):
  Fachbeschreibung ohne Zahl.
- Zeile 27–29 (Überschrift/Einleitung „Passform-Piktogramm"): keine eigene
  Zahl oder Rechenbeziehung.
- ☐2 (Zeile 54, Brustumfangsmaße am Körperquerschnitt) und ☐3 (Zeile 60,
  Armlochtiefe/Armloch mit Längenzugabe): reine Bildunterschriften ohne
  eigenen Zahlenwert auf dieser Seite.
- Zeilen 62–66 („Konstruktionstabelle ausfüllen"): verweist auf Größentabelle
  (Seite 18) und Maßtabelle (Seite 17), enthält aber selbst keine Formel;
  Verweis nicht kopiert, nur benannt.
- Zeilen 68–70 („Korrektur der Balancemaße"): verweist auf Seite 174 für die
  Korrektur von VL/RüL, enthält selbst keinen Rechenwert; Verweis nicht
  kopiert, nur benannt.
- Registerreiter und Daumen am linken Bildrand (laut `s176.md`): kein
  Seiteninhalt.
