# Formeln s190 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s190.md](s190.md)). Kein einziger formel- oder coderelevanter Punkt ist bisher
von Werner am Original bestätigt. Diese Extraktion wurde auf ausdrücklichen
Wunsch Werners trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker
übersprungen) und beruht auf [`ocr_s190.md`](ocr_s190.md) sowie den
Bildunterschriften in [`skizzen_s190.json`](skizzen_s190.json). Sie ersetzt
keine spätere Bestätigung der formelrelevanten Stellen am Original und darf
nicht als menschlich verifiziert gelten.

`s190.md` vermerkte bislang: „Die Layout-Antwort enthält auch keinen
eigenständigen Formeltext-Block; es gibt daher keine `formeln_s190.md`.“
Dieser Befund wird hier revidiert: Der Abschnitt „4 Saumverlauf“ enthält vier
zahlen- bzw. regelbasierte Konstruktionsanweisungen, und die Bildunterschrift
zu ☐5 im Skizzenausschnitt `s190_skizze_02.png` enthält zwei weitere
zahlenbasierte Maßangaben.

Zur bekannten offenen Stelle aus `s190.md`: Ob die Ziffer „5“ vor der ersten
Saumverlauf-Anweisung und die (im Rohtext fehlenden) drei weiteren blauen
Kreiszahlen fortlaufende Arbeitsschritte oder Punktnummern sind, ist nicht
geklärt (siehe Prüfstelle 2 in `s190.md`). Die vier Anweisungen werden hier
unabhängig von dieser Nummerierung einzeln erfasst.

## 1. Hinterer Saum – rechtwinklig zur hM

Quelle: `ocr_s190.md`, Zeile 25, zweiter Satz.

```text
Der hintere Saum wird immer rechtwinklig zur hM gezeichnet.
```

Hinweis: geometrische Beziehung (Winkel), kein Längenmaß.

## 2. Hintere Seitennaht unterhalb der Hüfte – parallel zur hM

Quelle: `ocr_s190.md`, Zeile 26.

```text
Unterhalb der Hüfte verläuft eine verlangerte hintere Seitennaht parallel zur
hinteren Mitte.
```

Hinweis: geometrische Beziehung mit Gültigkeitsbereich („unterhalb der
Hüfte“), kein Längenmaß. OCR-Schreibweise „verlangerte“ unverändert
übernommen (siehe Anmerkungen in `s190.md`, vermutlich „verlängerte“).

## 3. Seitennähte – gleiche Länge

Quelle: `ocr_s190.md`, Zeile 27.

```text
Die Seitennahte werden auf die gleiche Länge gebracht.
```

Hinweis: Gleichheitsbeziehung ohne Zahlenwert. OCR-Schreibweise
„Seitennahte“ unverändert übernommen (vermutlich „Seitennähte“).

## 4. Vorderer Saum an der vM – Verlängerung um 0,5 cm

Quelle: `ocr_s190.md`, Zeile 28.

```text
Den vorderen Saum an der vM um 0,5 cm verlangern und wie skizziert formen.
```

Hinweis: OCR-Schreibweise „verlangern“ unverändert übernommen (vermutlich
„verlängern“). Der Zusatz „wie skizziert formen“ verweist auf eine Kurvenform
aus der Zeichnung, die hier nicht in Zahlen vorliegt.

## 5. Brustabnäher-Bezugsmaß (zeichnungsgebunden)

Quelle: `skizzen_s190.json`, Bildregion `img-0.jpeg` (Datei
`skizzen/s190_skizze_02.png`), Beschreibungsfeld, Bildunterschrift im
geöffneten rosa Abnäher-Keil.

```text
BrU:20 – 1 bis + 1 cm
```

Hinweis: zeichnungsgebunden, aus der Bildregion-Beschreibung übernommen, nicht
aus einem eigenen OCR-Textblock (die Seite meldet keinen Formeltext-Block).
Am Original zu prüfen, ob „BrU:20“ tatsächlich „BrU geteilt durch 20“ bedeutet
und wie sich die Angabe zur benachbarten Bildunterschrift „ca. 1 cm“ verhält
(siehe „Nicht als Formel erfasst“).

## 6. Zweites Schnittteil – Bezug „wie seitlich“ (zeichnungsgebunden)

Quelle: `skizzen_s190.json`, Bildregion `img-0.jpeg` (Datei
`skizzen/s190_skizze_02.png`), Beschreibungsfeld, Maßangabe unten am linken
Schnittteil.

```text
wie seitlich + 0,5 cm
```

Hinweis: zeichnungsgebunden. Bezugsgröße „seitlich“ nicht eindeutig benannt.

## 7. Modelllänge – frei wählbar

Quelle: `ocr_s190.md`, Zeile 9, letzter Satz.

```text
Die Modelllänge kann jeweils beliebig gewählt werden.
```

Hinweis: Auswahlregel ohne Rechenbeziehung (freier Parameter, kein fester
Wert oder Default).

## Nicht als Formel erfasst

- `skizzen_s190.json`, Bildregion `img-0.jpeg`, Bildunterschrift „ca. 1 cm“:
  isolierte Maßangabe ohne erkennbare eigene Rechenbeziehung zu einer anderen
  Größe; möglicher Zusammenhang mit Abschnitt 5 („BrU:20 – 1 bis + 1 cm“) am
  Original zu klären.
- Zahlenmarken „5“ (vor der ersten Saumverlauf-Anweisung) sowie „6“, „7“
  (zweimal: „me 7“, „üb 7“), „8“, „9“ in der Zeichnung: laut Kapitelregel für
  `07_grundschnitte_oberteile_s171-196` vermutlich Punktnummern, keine
  Rechenwerte oder fortlaufenden Schritte (siehe Prüfstelle 2 in `s190.md`).
- `ocr_s190.md`, Zeile 15 („Figuren mit starker Brust haben eine größere
  VL…“): qualitative Passformbeschreibung ohne Zahl oder Rechenbeziehung.
- `ocr_s190.md`, Zeile 7 („UNISEX“) und das laut `s190.md` nicht erfasste
  Symbol daneben: kein Formelbezug.
- Der graue Platzhalterkasten „Konstruktions-tabelle hier aufkleben!“ in
  `img-0.jpeg`: laut `s190.md` ein unausgefüllter Platzhaltertext im
  gedruckten Buch, keine Tabelle oder Formel.
