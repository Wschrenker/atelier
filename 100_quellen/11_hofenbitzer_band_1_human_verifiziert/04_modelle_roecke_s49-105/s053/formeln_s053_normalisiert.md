# Formeln – s053 (normalisiert)

Technische Fassung zu [formeln_s053.md](formeln_s053.md). Jede Formel verweist
auf ihren Abschnitt dort. Buchfassung und technische Fassung bleiben getrennt.

Walking Skeleton: Auf Werners ausdrücklichen Wunsch entstand diese Fassung ohne
vollständige Vorab-Bestätigung. Nur die Reduzierung an `vM`/`hM` um ca.
`0,2 cm` ist bestätigt; alle Formeln unten führen daher überwiegend den Status
`offen`, keinen `normalisiert`.

## F1 – Beleg-Weitenreduktion an vM/hM

- **Quelle:** [formeln_s053.md](formeln_s053.md), Abschnitt 1.
- **Buchfassung:**

```text
Die Weite wird an der VM und NM um ca. 0,2 cm reduziert.
```

- **Technische Formel:** `Beleg_Weite(vM) = Kopie_Weite(vM) - 0,2 cm`,
  `Beleg_Weite(hM) = Kopie_Weite(hM) - 0,2 cm`.
- **Eingaben und Einheiten:** Weite der kopierten Belegfläche an `vM` und `hM`,
  in cm.
- **Ausgabe und Einheit:** reduzierte Beleg-Weite an denselben Stellen, in cm.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** `ca. 0,2 cm`, kein fester
  Wert; „ca." bleibt erhalten.
- **Abhängigkeiten:** unabhängig von F2 (andere Kante).
- **Status:** normalisiert.
- **Offene Fragen oder Widersprüche:** Die OCR-Schreibweise `VM und NM` weicht
  von den bestätigten Kürzeln `vM`/`hM` ab (vermutliche OCR-Verlesung von
  `NM` statt `hM`).

## F2 – Beleg-Höhenreduktion an der oberen Kante

- **Quelle:** [formeln_s053.md](formeln_s053.md), Abschnitt 2.
- **Buchfassung:**

```text
An der oberen Kante kann der Beleg um ebenfalls ca. 0,2 cm gekürzt werden, damit er oben nicht hervorschaut.
```

- **Technische Formel:** `Beleg_Hoehe(obere_Kante) = Kopie_Hoehe(obere_Kante) - 0,2 cm`
  (optional, siehe Bedingung).
- **Eingaben und Einheiten:** Höhe der kopierten Belegfläche an der oberen
  Kante, in cm.
- **Ausgabe und Einheit:** gekürzte Höhe an der oberen Kante, in cm.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** `ca. 0,2 cm`; laut Buchtext
  optional („kann"), kein Zwang zur Anwendung.
- **Abhängigkeiten:** gleicher Betrag wie F1, andere Kante; keine Buchregel
  verknüpft beide explizit als eine Formel.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Nicht bestätigt, ob diese Kürzung
  unabhängig von F1 anzuwenden ist oder in der Praxis immer zusammen erfolgt.

## F3 – Reduzierung für einen Reißverschluss

- **Quelle:** [formeln_s053.md](formeln_s053.md), Abschnitt 3.
- **Buchfassung:**

```text
0,5 bis 0,7 cm Abstand der Belegnaht von den Reißverschlusszähnchen
```

```text
Zusätzlich wird am Beleg an der Stelle, an der der Reißverschluss eingarbeitet wird, nochmals ca. 0,5 bis 0,7 cm gekürzt, da der Taillenbeleg vor den Reißverschluss-Zähnchen endet.
```

- **Technische Formel:** `Beleg_Kuerzung(Reissverschluss_Stelle) ∈ [0,5 cm, 0,7 cm]`,
  zusätzlich zu F1/F2 an der Reißverschlussstelle.
- **Eingaben und Einheiten:** keine externe Messgröße; Betrag ist ein
  Buchbereich.
- **Ausgabe und Einheit:** Kürzungsbetrag an der Reißverschlussstelle, cm.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** `0,5–0,7 cm`, kein
  Default gewählt.
- **Abhängigkeiten:** zusätzlich zu F1 (Weitenreduktion), gleiche Belegfläche.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** keine Rechnung zu prüfen, reine
  Bereichsangabe; nicht bestätigt, ob „nochmals" additiv zu F1 oder eigenständig
  zu verstehen ist.

## F4 – Nahtzugabe (NZg) an unterer Belegkante bei Futter

- **Quelle:** [formeln_s053.md](formeln_s053.md), Abschnitt 4.
- **Buchfassung:**

```text
Die Beleg-Schnittteile mit Nahtzugaben (NZg) versehen. Es sind dieselben NZg zu verwenden, wie am Schnittteil, an das der Beleg genäht wird (hier der Vorder- und der Hinter-Rock). Für das Annähen eines Futters (ab Seite 59) wird an der unteren Belegkante ebenfalls eine NZg von 1 cm angezeichnet.
```

- **Technische Formel:** `NZg(Beleg, Rand) = NZg(Traegerschnittteil, Rand)`
  für die übrigen Ränder; `NZg(Beleg, untere_Kante) = 1 cm`, wenn Futter
  angebracht wird (siehe Seite 59, nicht kopiert).
- **Eingaben und Einheiten:** `NZg(Traegerschnittteil, Rand)` aus dem
  jeweiligen Vorder-/Hinter-Rock-Schnittteil (seitenübergreifend, nicht
  kopiert).
- **Ausgabe und Einheit:** `NZg(Beleg, Rand)` in cm.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Bedingung „nur bei
  Futteranbringung" für den festen Wert `1 cm` an der unteren Kante.
- **Abhängigkeiten:** Seite 59 (Futterkonstruktion, Verweis, nicht kopiert);
  Vorder-/Hinter-Rock-Schnittteil (seitenübergreifend, Verweis).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** keine Rechnung zu prüfen; die
  „übrigen" NZg-Werte selbst liegen auf einer anderen Seite und werden hier
  nicht übernommen.

## F5 – Auswahlregel: Knips bei NZg über 1 cm

- **Quelle:** [formeln_s053.md](formeln_s053.md), Abschnitt 5.
- **Buchfassung:**

```text
An NZg von mehr als 1 cm Breite wird ein Knips gesetzt. Ebenfalls an Symmetriellinen (Körpermitten, hier die VM).
```

- **Technische Formel:** `if NZg(Rand) > 1 cm: Knips(Rand) = wahr`;
  zusätzlich `Knips(Symmetrielinie) = wahr` unabhängig vom NZg-Betrag.
- **Eingaben und Einheiten:** `NZg(Rand)` in cm.
- **Ausgabe und Einheit:** boolesche Markierungsentscheidung je Rand
  (Knips ja/nein).
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Schwellenwert `> 1 cm`,
  fest im Buchtext (kein „ca.").
- **Abhängigkeiten:** F4 (NZg-Werte).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** keine Rechnung zu prüfen; ob die Regel
  allgemein für alle Schnittteile oder nur für den Beleg gilt, ist im
  Buchtext an dieser Stelle nicht getrennt.

## F6 – Bohrloch-Position oberhalb der Abnäherspitze

- **Quelle:** [formeln_s053.md](formeln_s053.md), Abschnitt 6.
- **Buchfassung:**

```text
Die Abnäher an VT und RT werden je nach Körperposition geformt, mit Knipsen an der Taillennaht sowie mit einem Bohrloch 2 cm oberhalb der Abnäherspitze versehen.
```

- **Technische Formel:** `Bohrloch_Position = Abnäherspitze + 2 cm`
  (Richtung: entlang der Abnäherlängsachse nach oben, laut Buchtext).
- **Eingaben und Einheiten:** Position der Abnäherspitze (aus dem jeweiligen
  Abnäher, nicht auf dieser Seite berechnet).
- **Ausgabe und Einheit:** Bohrloch-Position, `2 cm` Versatz zur
  Abnäherspitze.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** fester Wert `2 cm`, kein
  „ca.".
- **Abhängigkeiten:** Abnäherform an VT und RT („je nach Körperposition
  geformt" — im Buchtext an dieser Stelle nicht mit einer Regel hinterlegt).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** keine Rechnung zu prüfen; die Stelle
  ist nicht Teil der in s053.md vorab bestätigten Angabe (nur die
  Weitenreduktion an vM/hM ist bestätigt).
