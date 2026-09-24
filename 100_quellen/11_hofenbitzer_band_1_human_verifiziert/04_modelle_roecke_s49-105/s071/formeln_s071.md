# Formeln s071 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s071.md](s071.md)). Kein einziger formel- oder coderelevanter Punkt ist
bisher von Werner am Original bestätigt. Diese Extraktion wurde auf
ausdrücklichen Wunsch Werners trotzdem als Walking-Skeleton-Durchlauf erstellt
(Blocker übersprungen) und beruht ausschließlich auf
[`ocr_s071.md`](ocr_s071.md). Sie ersetzt keine spätere Bestätigung der
formelrelevanten Stellen am Original und darf nicht als menschlich verifiziert
gelten.

`s071.md` vermerkte bislang „Keine Tabelle und keine Formel auf dieser Seite
erkannt.“ Dieser Befund wird hier präzisiert: Die Seite enthält keine
zahlenbasierte Rechenformel, aber drei coderelevante Konstruktions- und
Auswahlregeln im Fließtext.

Die drei Skizzenbereiche (`img-0` bis `img-2`) sind noch nicht als eigene
Ausschnitte extrahiert. Von `s071.md` genannte, noch nicht transkribierte
Zeichnungsbeschriftungen (u. a. „1/20 Saumerweiterung") stehen weder in
`ocr_s071.md` noch in `ocr_s071_raw.json` als Text zur Verfügung und werden
hier deshalb nicht als Formel geführt, siehe „Nicht als Formel erfasst".

## 1. Eckbehandlung an der Taillennaht (Auswahlregel)

Quelle: `ocr_s071.md`, Zeile 13–14.

```text
Sollen die Glocken direkt aus der Taille fallen, verbleibt die Ecke an der
Taillennnaht.
2 Durfen die Glocken welcher ab unterhalb der Taille fallen, wird die Ecke an
der Taillennah ausgerundet.
```

Hinweis: OCR-Schreibweisen „Taillennnaht" (ein n zu viel), „Durfen" (fehlender
Umlaut) und „welcher" (statt „weicher") unverändert übernommen, siehe bekannte
OCR-Lücken in [s071.md](s071.md). Die Punktnummer „2" ist laut s071.md
vermutlich falsch (Foto zeigt ⑤ statt „2"); am Original zu prüfen.

## 2. Saumrundungen als Kreisbögen (geometrische Konstruktionsregel)

Quelle: `ocr_s071.md`, Zeile 16, erster Satz.

```text
Die Saumrundungen können als Kreisbögen gezeichnet werden.
```

## 3. Saumkürzung an den Teilungsnähten (unquantifizierte Anpassungsregel)

Quelle: `ocr_s071.md`, Zeile 16 zweiter Satz und Zeile 18.

```text
Wegen des schrägen Fadenlaufs der Nähte wird sich dort der Stoff, je nach
Beschaffenheit, mehr oder weniger stark ausdehnen.
3 Der Saum kann daher an den Teilungsnähten leicht gekürzt werden.
```

Hinweis: Kein Zahlenwert im Buchtext für „leicht gekürzt". Die Punktnummer „3"
ist laut s071.md vermutlich falsch (Foto zeigt ⑥ statt „3"); am Original zu
prüfen.

## Nicht als Formel erfasst

- Zeile 11 („Die große Saumweite wird an allen Nähten (hier an allen 10
  Nähten) hinzu gegeben, was dem Rock eine gleichmäßig glockig schwingende
  Form gibt."): beschreibt die Verteilung der Saumerweiterung auf 10 Nähte,
  nennt aber keinen Rechenwert oder Aufteilungsschlüssel (kein „je" oder
  „gleich verteilt" pro Naht im Wortlaut) – hier nicht als eigene Formel
  geführt, um keine Rechenbeziehung zu ergänzen, die im Buchtext nicht steht.
- Zeile 20 („Hier werden aus Platzgründen nur die hinteren Rockteile
  dargestellt. Die vorderen sind entsprechend zu erstellen."): allgemeine
  Symmetrieanweisung ohne Zahl oder Rechenbeziehung.
- Zeilen 22, 28–29 (□1 „Glockiger 10-Bahnen-Rock", □2 „Produktionschnitt des
  Rückteils (RT3 noch spiegeln)"): reine Bild-/Teileverweise, keine Formeln.
- Von `s071.md` genannte, aber nicht transkribierte Zeichnungslabels („VT",
  „SN", „10-Bahnen-Rock RT 1/RT 2/RT 3", „2×-p OSt", „1× OSt", „1/20
  Saumerweiterung", Kreisnummern): in `ocr_s071.md`/`ocr_s071_raw.json` nicht
  als Text vorhanden (geprüft), daher hier nicht übernommen. Insbesondere „1/20
  Saumerweiterung" wäre potenziell coderelevant (möglicher Aufteilungsschlüssel
  für die Saumerweiterung über die Schnittteilkanten), muss aber erst durch
  eine echte Skizzenextraktion und Bildprüfung belegt werden, nicht durch freie
  Bildsuche ergänzt werden.
