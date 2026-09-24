# Formeln – s065 (normalisiert, technische Fassung)

Technische Fassung zu [formeln_s065.md](formeln_s065.md). Seite 65 ist
OCR-Rohfassung; **keine der hier erfassten Beziehungen ist von Werner am
Original bestätigt**, und die formel-/coderelevanten Prüfstellen wurden für
diese Seite noch nicht vorab geklärt. Alle Status stehen deshalb auf `offen`,
bis Werner Wortlaut, Bahnenzahlen und die Zuordnung der Skizzen bestätigt.
Diese Fassung entsteht als Walking Skeleton auf Werners ausdrücklichen
Wunsch, um die Ablage- und Vertragsform vorab zu erproben.

## F1 – Gleich breite Bahnenaufteilung, 10-Bahnenrock

- **Quelle:** [formeln_s065.md](formeln_s065.md), Abschnitt 1.
- **Buchfassung:**

```text
Die zehn Teilungshähte unterteilen diesen Rock in zehn an der Hüfte und am Saum gleich breite "Bahnen".
```

- **Technische Formel:** `Bahnbreite_Hüfte = Hüftweite_gesamt / n`,
  `Bahnbreite_Saum = Saumweite_gesamt / n`, mit `n = 10`.
- **Eingaben und Einheiten:** `Hüftweite_gesamt` (cm), `Saumweite_gesamt`
  (cm) – auf dieser Seite nicht beziffert, nur als „wie skizziert"
  beschrieben; `n = 10` (Bahnenzahl, Modellparameter, dimensionslos).
- **Ausgabe und Einheit:** `Bahnbreite_Hüfte`, `Bahnbreite_Saum`, jeweils cm.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine; feste
  Gleichteilung laut Buchtext.
- **Abhängigkeiten:** `Hüftweite_gesamt`/`Saumweite_gesamt` kommen aus dem
  zugrunde liegenden Rock-Grundschnitt (andere Seite, nicht kopiert). Siehe
  F2 für die Aufteilung auf die Rockhälften.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Die Formel ist aus der Buchbeschreibung
  „gleich breite Bahnen" abgeleitet, nicht wörtlich als Gleichung gedruckt.
  Ob die Teilung rein arithmetisch (Gesamtweite/10) erfolgt oder ob einzelne
  Bahnen (z. B. an den Seitennähten) laut Zeichnung abweichen, ist ohne
  Prüfung der Skizze `skizzen/s065_skizze_02.png` am Original nicht
  gesichert.

## F2 – Bahnenzahl je Rockhälfte

- **Quelle:** [formeln_s065.md](formeln_s065.md), Abschnitt 2.
- **Buchfassung:**

```text
Es ergeben sich im halben Vorderrock und im halben Hinterrock jeweils die entsprechenden Schnittteile für den halben Rock, zusammen 5 bzw. 6 Bahnen, sowie für den ganzen Rock 10 bzw. 12 Bahnen.
```

- **Technische Formel:** `n_halb = n_gesamt / 2`, mit `n_gesamt ∈ {10, 12}`
  je nach Modell (10-Bahnenrock bzw. 12-Bahnenrock).
- **Eingaben und Einheiten:** `n_gesamt = 10` oder `12` (Stückzahl,
  Modellparameter, keine Längeneinheit).
- **Ausgabe und Einheit:** `n_halb = 5` (bei `n_gesamt = 10`) bzw. `6` (bei
  `n_gesamt = 12`).
- **Bereiche, Bedingungen, Auswahlentscheidungen:** Auswahl des Modells
  (10- oder 12-Bahnenrock) bestimmt `n_gesamt`; keine weitere Buchregel.
- **Abhängigkeiten:** F1 und F3 (gleiches `n_gesamt`).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Auffälligkeit
  (`5 = 10/2`, `6 = 12/2`). Nicht bestätigt, ob „halber Rock" hier
  Vorderrock-Hälfte und Hinterrock-Hälfte zusammengenommen meint (so liest
  sich der Satz) oder etwas anderes – reine Lesart, keine bestätigte Aussage.

## F3 – Gleich breite Bahnenaufteilung, 12-Bahnenrock

- **Quelle:** [formeln_s065.md](formeln_s065.md), Abschnitt 3.
- **Buchfassung:**

```text
Die zwölf Teilungshähte unterteilen den Rock in zwölf gleich breite Schnittteile an der Hüfte und am Saum.
```

- **Technische Formel:** `Bahnbreite_Hüfte = Hüftweite_gesamt / n`,
  `Bahnbreite_Saum = Saumweite_gesamt / n`, mit `n = 12`.
- **Eingaben und Einheiten:** wie F1, mit `n = 12`.
- **Ausgabe und Einheit:** wie F1.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine; feste
  Gleichteilung.
- **Abhängigkeiten:** F2 (`n_gesamt = 12`).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** gleiche Unsicherheit wie F1 (Buchtext
  beschreibt die Gleichteilung, nennt aber keine Gleichung).

## F4 – Neue Teilungsnaht an der Abnähermitte

- **Quelle:** [formeln_s065.md](formeln_s065.md), Abschnitt 4.
- **Buchfassung:**

```text
Die Abnäherinhalte am Grundschnitt messen und an die Einschnittlinien (= Abnähermitte) übertragen.
```

- **Technische Formel:** `Position(Einschnittlinie) = Position(Abnähermitte_Grundschnitt)`;
  keine Berechnung der Abnäherinhalte selbst auf dieser Seite.
- **Eingaben und Einheiten:** Abnäherinhalte (cm) und deren Lage am
  Grundschnitt – Quellseite („Rock-Grundschnitt") auf s065 nicht benannt, nur
  zu verlinken, sobald bekannt.
- **Ausgabe und Einheit:** Lage der neuen Teilungsnaht (Positionsangabe,
  keine eigene Längenberechnung).
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine.
- **Abhängigkeiten:** Grundschnitt-Seite (Abnäherinhalte, Quellseite offen);
  die Einschnittlinien aus dieser Regel definieren zugleich die
  Bahnengrenzen aus F1/F3.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Die konkrete Quellseite des
  „Rock-Grundschnitt" ist hier nicht ermittelt und die Abnäherinhalte sind
  nicht beziffert; ohne beides bleibt diese Beziehung nicht weiterverwendbar.

## Zusammenfassung

Vier Beziehungen erfasst (drei Bahnenaufteilungen/-zahlen, eine
Positionsregel), keine bestätigt. Alle vier stehen auf `offen`: aus Fließtext
abgeleitet, nicht am Original bestätigt, aber ohne erkennbaren inneren
Widerspruch. Für einen späteren Codevertrag muss Werner mindestens die
Bahnenzahlen (F1–F3) und die Grundschnitt-Referenz samt Abnäherinhalten (F4)
bestätigen.
