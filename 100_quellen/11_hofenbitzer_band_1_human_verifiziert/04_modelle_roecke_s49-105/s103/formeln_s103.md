# Formeln s103 – fototreue Extraktion (vorläufig, Walking Skeleton)

**Achtung – Bereitschaftsstufe unvollständig:** Die Seite trägt weiterhin den
Status `OCR-Rohfassung – noch nicht menschlich verifiziert`
([s103.md](s103.md)). Kein einziger formel- oder coderelevanter Punkt ist
bisher von Werner am Original bestätigt — im Gegenteil, `s103.md` nennt mehrere
offene Widersprüche zu genau diesem Abschnitt (Schrittkennung `⑩`–`⑬`
unbestätigt zugeordnet, `1× OSX` vs. `1× OSt`, „Poduktionsschnitt" vs.
„Produktionsschnitt"). Diese Extraktion wurde auf ausdrücklichen Wunsch Werners
trotzdem als Walking-Skeleton-Durchlauf erstellt (Blocker übersprungen) und
beruht ausschließlich auf [`ocr_s103.md`](ocr_s103.md). Sie ersetzt keine
spätere Bestätigung der formelrelevanten Stellen am Original und darf nicht
als menschlich verifiziert gelten.

Die Seite enthält keine Tabelle und keine zahlenbasierte Formel im engeren
Sinn. Der Abschnitt „Vorderteile entwickeln" enthält jedoch drei
Konstruktionsregeln mit einer echten Rechen-/Auswahlbeziehung (Gleichverteilung,
punktgebundener Zuschnitt, sichtbarkeitsgebundene Auswahlregel), auch wenn
keine davon einen Zahlenwert nennt.

Zusätzlich gilt die bekannte OCR-Lücke aus [s103.md](s103.md): Die
eingekreisten Foto-Schrittzahlen `⑩`–`⑬` wurden von der OCR nicht übernommen
(nur eine nackte „6" vor dem ersten Absatz, keine Ziffer vor den übrigen drei).
Die unten angegebene Foto-Schrittzahl stammt aus der (ebenfalls unbestätigten)
Zuordnung in `s103.md`, nicht aus einer eigenen Bildprüfung.

## 1. Gleichmäßiges Öffnen der Falteneinschnitte

Quelle: `ocr_s103.md`, Zeile 23 (Schrittfließtext, laut Lückenhinweis
Foto-Schritt `⑪`).

```text
Dann nacheinander alle Falteneinschnitte ungefähr gleich welt öffnen. Dabei möglichst alle im Grundschnitt vorhandenen Abnäher schließen.
```

Hinweis: OCR-Schreibweise „welt" (statt „weit") unverändert übernommen, nicht
still korrigiert.

## 2. Faltenrückschnitt an P1 gerade abschneiden

Quelle: `ocr_s103.md`, Zeile 24 (Schrittfließtext, laut Lückenhinweis
Foto-Schritt `⑫`).

```text
Die Faltenrückschnitte durch Zulegen und Zurückschneiden der Falten bestimmen. An P1 (Beginn der Übertritt-Kante) wird der Rückschnitt gerade abgeschnitten.
```

Hinweis: Der Punkt `P1` wird hier nur textlich benannt; auf dieser Seite keine
eigene Maßzahl oder Koordinate dazu gefunden. Vermutlich in
`skizzen/s103_skizze_02.png` markiert (nicht eigens geprüft).

## 3. Beleg-Breite für die Wasserfall-Kante (Sichtbarkeitsbedingung)

Quelle: `ocr_s103.md`, Zeile 25 (Schrittfließtext, laut Lückenhinweis
Foto-Schritt `⑬`), erster und zweiter Satz.

```text
Für die Wasserfall-Kante muss ein Beleg konstruiert werden (hier in Gelb-Orange). Dazu wird oben der ursprüngliche Taillenverlauf verwendet und nach unten die Beleg-Kante so breit zum Saum gezeichnet, dass sie beim Umschlagen der Übertritt-Kante nicht direkt sichtbar wird.
```

Hinweis: Kein Zahlenwert für die Beleg-Breite angegeben; die Auswahlregel ist
an eine Sichtbarkeitsbedingung gebunden, nicht an einen festen Betrag.

## Nicht als Formel erfasst

- Zeile 22 (`⑩` „Die Wasserfallkante öffnen, indem man den linken vorderen
  Abnäher schließt und die Kante neu formt."): reine Operationsbeschreibung
  ohne Zahl, Bereich oder Auswahlbeziehung.
- Zeile 26 („Den Beleg kopieren und spiegeln (der fertige Beleg-Schnitt ist
  hier unter dem Text hinterlegt).") — reine Operationsbeschreibung, keine
  eigene Rechen-/Auswahlbeziehung.
- Zeilen 3–8 (doppelte Kapitelüberschrift „Wickelrock (2) / mit Drapierung und
  Wasserfall-Kante"): OCR-Duplikat, kein Formelinhalt (vgl. `s103.md`).
- Zeilen 12, 16–17 (Bildunterschriften `☐4 Produktionsschnitt Bund`, `☐5
  Produktionsschnitt rechtes VT mit Wasserfall-Kante`): reine
  Teile-/Zuordnungsbeschreibungen ohne Zahlenwert.
- Zeilen 28–30 (Bildunterschrift „Drapierter Wickelrock / Übertritt-Beleg /
  1× OSX"): Stückzahlkennzeichnung, ausdrücklich ausgeschlossen; laut
  `s103.md` zudem mutmaßlicher OCR-Fehler (Original zeigt „1× OSt").
- Zeilen 32–33 (Bildunterschrift „☐6 Produktionsschnitt Übertritt-Beleg"):
  reine Teile-/Zuordnungsbeschreibung ohne Zahlenwert.
- Zeilen 37–38 (Bildunterschrift „Wickelrock mit Drapierfalten und
  Wasserfall-Kante"): Bildunterschrift ohne Zahlenwert.
- Skizzenausschnitte laut [`skizzen_s103.json`](skizzen_s103.json): zeigen nur
  Markierungen (`VM`, `SN`, `hM`, „Einschlag Untertritt") ohne erkennbare
  Maßzahl oder Rechenbeziehung; hier nicht als eigene Formel erfasst.
