# Formeln normalisiert – s051

Technische Fassung zu [formeln_s051.md](formeln_s051.md). Alle vier Stellen
sind über die zugrundeliegende Formel-/Codeprüfung noch nicht bestätigt;
Status durchgängig `offen`. Walking Skeleton auf ausdrücklichen Wunsch
Werners.

## 1. Hohlkreuz / tief sitzendes Gesäß, geringe Taillenvertiefung

**Quelle:** [formeln_s051.md](formeln_s051.md), Abschnitt 1.

**Buchfassung:**

```text
Bei Hohlkreuz bzw. tief sitzendem Gesäß und geringer Taillenvertiefung:
hinten muss ein größerer Betrag entfernt werden als vorne.
```

**Technische Formel:**

```text
hinten_Betrag > vorne_Betrag
```

**Eingaben und Einheiten:** `vorne_Betrag` (cm, Taillenvertiefung vorne),
`hinten_Betrag` (cm, Taillenvertiefung hinten). Kein numerischer Faktor in
der Buchfassung.

**Ausgabe und Einheit:** keine Berechnung, nur eine Ungleichung als
Auswahlregel zwischen `vorne_Betrag` und `hinten_Betrag`.

**Bereiche, Bedingungen und Auswahlentscheidungen:** gilt nur bei
Figurtyp „Hohlkreuz bzw. tief sitzendes Gesäß" und „geringe
Taillenvertiefung". Kein Zahlenverhältnis angegeben, daher kein
berechenbarer Betrag ableitbar.

**Abhängigkeiten:** Figurtypbestimmung (Gesäßform, Grad der
Taillenvertiefung) liegt außerhalb dieser Seite.

**Status:** offen.

**Offene Fragen oder Widersprüche:** Kein Faktor oder Prozentwert im
Buchtext; die Regel ist ohne weitere Fachfestlegung nicht in eine
konkrete Zahl übersetzbar.

## 2. Starkes Gesäß, große Taillenvertiefung

**Quelle:** [formeln_s051.md](formeln_s051.md), Abschnitt 2.

**Buchfassung:**

```text
Bei starkem bzw. hinten sehr hoch gewölbtem Gesäß und großer Taillenvertiefung:
Taillenvertiefung an der hM = 1/2 der vorderen Vertiefung oder noch weniger
```

**Technische Formel:**

```text
hM_Betrag <= 0,5 * vorne_Betrag
```

**Eingaben und Einheiten:** `vorne_Betrag` (cm, vordere
Taillenvertiefung). `hM` nicht ausgeschrieben, hier ungeprüft als „hintere
Mitte" übernommen.

**Ausgabe und Einheit:** `hM_Betrag` (cm) als oberer Grenzwert, kein
fester Wert.

**Bereiche, Bedingungen und Auswahlentscheidungen:** Obergrenze
„die Hälfte oder weniger" — offener Bereich nach unten, keine Untergrenze
im Buchtext.

**Abhängigkeiten:** Figurtypbestimmung „starkes Gesäß" liegt außerhalb
dieser Seite; Bezug zu `vorne_Betrag` aus Abschnitt 1 nicht hergestellt
(unterschiedliche Figurtypen).

**Status:** offen.

**Offene Fragen oder Widersprüche:** Bedeutung von „hM" nicht bestätigt.

## 3. Flaches Gesäß, geringe Taillenvertiefung

**Quelle:** [formeln_s051.md](formeln_s051.md), Abschnitt 3.

**Buchfassung:**

```text
Beim flachen Gesäß und geringer Taillenvertiefung:
hinten muss ein größerer Betrag entfernt werden als vorne.
```

**Technische Formel:**

```text
hinten_Betrag > vorne_Betrag
```

**Eingaben und Einheiten:** wie Abschnitt 1.

**Ausgabe und Einheit:** keine Berechnung, nur eine Ungleichung.

**Bereiche, Bedingungen und Auswahlentscheidungen:** gilt nur bei
Figurtyp „flaches Gesäß" und „geringe Taillenvertiefung". Strukturell
identisch zu Abschnitt 1, aber für einen anderen Figurtyp im Buch
getrennt formuliert — nicht zusammengeführt.

**Abhängigkeiten:** wie Abschnitt 1.

**Status:** offen.

**Offene Fragen oder Widersprüche:** Kein Faktor oder Prozentwert im
Buchtext.

## 4. Flaches Gesäß, große Taillenvertiefung

**Quelle:** [formeln_s051.md](formeln_s051.md), Abschnitt 4.

**Buchfassung:**

```text
Beim flachen Gesäß und großer Taillenvertiefung:
vorne entfernter Betrag = hinten entfernter Betrag
seitlich entfernter Betrag = ca. 10% mehr als vorne/hinten
(aber nicht mehr als 1 cm)
```

**Technische Formel:**

```text
hinten_Betrag = vorne_Betrag
seitlich_Betrag ≈ vorne_Betrag * 1,10   (Obergrenze unklar, siehe unten)
```

**Eingaben und Einheiten:** `vorne_Betrag` (cm).

**Ausgabe und Einheit:** `hinten_Betrag` (cm), `seitlich_Betrag` (cm,
ca.-Wert).

**Bereiche, Bedingungen und Auswahlentscheidungen:** gilt nur bei
Figurtyp „flaches Gesäß" und „große Taillenvertiefung". Die Kappung
„aber nicht mehr als 1 cm" ist textlich nicht eindeutig einer Größe
zugeordnet (siehe unten).

**Abhängigkeiten:** keine zu anderen Seiten erkennbar.

**Status:** offen.

**Offene Fragen oder Widersprüche:** Unklar, ob sich „nicht mehr als
1 cm" auf `seitlich_Betrag` insgesamt oder auf die Differenz
`seitlich_Betrag − vorne_Betrag` bezieht. Beide Lesarten bleiben
nebeneinander offen; keine wird als Default gewählt.
