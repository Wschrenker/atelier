# Formeln s081 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s081.md](s081.md)). Kein einziger formel- oder coderelevanter Punkt ist bisher
von Werner am Original bestätigt. Diese Extraktion wurde auf ausdrücklichen
Wunsch Werners trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker
übersprungen) und beruht ausschließlich auf [`ocr_s081.md`](ocr_s081.md) sowie,
wo als zeichnungsgebunden gekennzeichnet, auf `skizzen_kontaktbogen.jpg`. Sie
ersetzt keine spätere Bestätigung der formelrelevanten Stellen am Original und
darf nicht als menschlich verifiziert gelten.

`s081.md` vermerkte bislang „Keine Tabelle und keine Formel auf dieser Seite
erkannt." Dieser Befund wird hier revidiert: Die Seite enthält keine
zahlenbasierten Rechenbeziehungen, aber fünf geometrische
Konstruktionsbeziehungen und Auswahlregeln (Verschiebung um einen Betrag,
Positions- und Formentscheidungen), die für einen späteren Codevertrag relevant
sein können.

## 1. Ansatzposition der Glocke – Taille vs. unterhalb der Taille

Quelle: `ocr_s081.md`, Zeile 9–12 (Einleitungstext).

```text
Die Glocken können entsprechend der Formung
der Tailleinhalt wahlweise direkt aus der Taille fallen (wie
hier am VT) oder welcher unterhalb der Taille (wie hier am
RT gezeigt).
```

Hinweis: OCR-Schreibweise „Tailleinhalt" (statt vermutlich „Taillennaht") und
„welcher" (laut Bildvergleich in `s081.md` vermutlich „weicher") unverändert
übernommen, nicht still korrigiert.

## 2. Verschiebung der Teilungsnaht-Abnäher an den Öffnungspunkt

Quelle: `ocr_s081.md`, Zeile 18.

```text
Die Abnaher der vorderen bzw. hinteren Teilungsnahte werden an die Öffnungsposition verschoben, indem Dort die beiden Schnittteile um die Beträge der Abnaherinhalte überschnitten werden.
```

Hinweis: OCR-Schreibweisen „Abnaher", „Teilungsnahte", „Dort" (großgeschrieben)
und „Abnaherinhalte" unverändert übernommen, siehe bekannte OCR-Lücke in
`s081.md`.

## 3. Saumöffnung für die Glocke

Quelle: `ocr_s081.md`, Zeile 19, erster Teilsatz.

```text
Am Saum wird für die Glocke die gewünschte Weite geöffnet
```

## 4. Ausrundung der Ecke an der Ansatznaht (Auswahlregel)

Quelle: `ocr_s081.md`, Zeile 25–26.

```text
Wird die entstandene Ecke an der Ansatznah nicht ausgerundet, fällt die Glocke klar und scharf.
Bei einem ausgerundeten Verlauf der Ansatznah, fällt die Glocke welcher und breiter.
```

Hinweis: OCR-Schreibweisen „Ansatznah" (statt „Ansatznaht") und „welcher"
(vermutlich „weicher", siehe `s081.md`) unverändert übernommen.

## 5. Modell 2 – zusätzliches Ausstellen beider Seitennähte

Quelle: `ocr_s081.md`, Zeile 37–39; zeichnungsgebunden zusätzlich in
`skizzen_kontaktbogen.jpg` (rechtes Schnittbild, Beschriftungen „hier **ohne**
zusätzliches Ausstellen an SN" bei Modell 1 / VT und „hier **mit**
zusätzlichem Ausstellen an SN" bei Modell 2 / RT).

```text
Bei Modell 2 werden beide Seiten-
nähte (wie hier am RT gezeigt) für
mehr Saumweite ausgestellt.
```

## Nicht als Formel erfasst

- Zeile 19, zweiter Teilsatz („und der Saumverlauf rund geformt"): reine
  Forminstruktion ohne Zahl, Betrag oder benannte Auswahlbeziehung, hier nicht
  als eigene Formel geführt (siehe Abschnitt 3, gleicher Satz).
- Zeile 6–9 („Klar positionierte Glocken sind an diesem Rock nur an den
  seitlichen Teilungsnähten des geraden 10-Bahnenrocks eingearbeitet. Die
  mittleren Teilungsnähte werden ignoriert…"): Modellbeschreibung ohne
  eigenständige Rechen- oder Auswahlbeziehung auf dieser Seite.
- Bildunterschriften „☐2 Modell 1" / „☐2 Modell 2" (Zeile 28–35) und „☐3
  Produktionsschnitte für Rock mit positionierten Glocken (Schnittteile noch
  spiegeln)" (nur im Bildausschnitt, siehe `s081.md`): reine
  Teile-/Zuordnungsbeschreibungen ohne Zahlenwert oder Rechenbeziehung.
- Rote Nummernbox „65" oben rechts (nur am Foto erkennbar, siehe `s081.md`):
  Randverweis auf eine andere Seite, keine Formel dieser Seite.
- Stückzahlangaben „1× OSt" in `skizzen_kontaktbogen.jpg`: reine Stückzahl
  ohne Rechen- oder Auswahlbeziehung, gemäß Ausschlussregel des Prompts.
