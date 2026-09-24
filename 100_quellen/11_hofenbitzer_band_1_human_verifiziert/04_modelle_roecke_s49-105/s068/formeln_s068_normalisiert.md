# Formeln s068 – normalisierte Fassung

Quelle für alle Buchfassungen: [formeln_s068.md](formeln_s068.md).

## Formel 1: Rocksaumweite mit eingesetzten Godets

**Quelle:** [formeln_s068.md](formeln_s068.md), Abschnitt 1.

**Buchfassung:**

```text
SaW_Rock = SaW_Godet × Anzahl_Godets + SaW_Rock-GS
```

**Technische Formel:**

```text
saw_rock = saw_godet * anzahl_godets + saw_rock_gs
```

**Eingaben und Einheiten:**

- `saw_godet` – Saumweite eines einzelnen Godets, cm
- `anzahl_godets` – Anzahl der eingesetzten Godets, ganzzahlig, dimensionslos
- `saw_rock_gs` – Saumweite des Grundschnitt-Rocks ohne Godets (Variable im
  Buch mit Bindestrich `SaW_Rock-GS` geschrieben), cm

**Ausgabe und Einheit:**

- `saw_rock` – gesamte Saumweite des Rocks mit eingesetzten Godets, cm

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buch genannt.

**Abhängigkeiten:** `saw_rock_gs` bezieht sich auf den Grundschnitt-Rock
(10-Bahnen-Rock); die zugehörige Grundschnittseite ist auf s068 nicht
verlinkt und wurde hier nicht nachgeschlagen.

**Status:** normalisiert (Buchformel inklusive Variablenschreibweise am
Original bestätigt, siehe [s068.md](s068.md)).

**Offene Fragen oder Widersprüche:** keine.

## Formel 2: Konstruktion des Godet-Kreisausschnitts

**Quelle:** [formeln_s068.md](formeln_s068.md), Abschnitt 2.

**Buchfassung:**

```text
Kreisbogen-Radius = Godethöhe
Bogenlänge (Kreisbogen) = Godetweite
```

**Technische Formel:**

```text
radius = godethoehe
bogenlaenge = godetweite
```

**Eingaben und Einheiten:**

- `godethoehe` – gewünschte Godethöhe, cm
- `godetweite` – gewünschte Godetweite, cm (auf dem Bogen abgemessen oder per
  Winkel bestimmt)

**Ausgabe und Einheit:**

- `radius`, cm
- `bogenlaenge`, cm

**Bereiche, Bedingungen und Auswahlentscheidungen:** Der Buchtext lässt zwei
gleichwertige Wege offen, `godetweite` auf dem Bogen festzulegen (direktes
Abmessen der Bogenlänge oder Konstruktion über einen Winkel). Keine Buchregel
wählt zwischen beiden oder nennt eine Umrechnung Winkel↔Bogenlänge; ein
fixer Zusammenhang darf hier nicht ergänzt werden.

**Abhängigkeiten:** `godetweite` geht in Formel 1 (`saw_godet`) ein; der
genaue Bezug zwischen der hier konstruierten Bogenlänge und `saw_godet` aus
Formel 1 steht nicht im Buchtext dieser Seite.

**Status:** offen (Quelle noch nicht am Original bestätigt, siehe
[formeln_s068.md](formeln_s068.md) Abschnitt 2; Auswahl zwischen den zwei
Konstruktionswegen fachlich ungeklärt).

**Offene Fragen oder Widersprüche:** Zusammenhang zwischen Winkel- und
Abmess-Methode zur Bestimmung der Godetweite ist im Buchtext nicht formalisiert.

## Formel 3: Teilung der Godetweite an der Fadenlaufmitte

**Quelle:** [formeln_s068.md](formeln_s068.md), Abschnitt 3.

**Buchfassung:**

```text
Bogenabschnitt_links = Bogenabschnitt_rechts = Godetweite / 2
```

**Technische Formel:**

```text
bogenabschnitt_links = bogenabschnitt_rechts = godetweite / 2
```

**Eingaben und Einheiten:**

- `godetweite` – wie Formel 2, cm

**Ausgabe und Einheit:**

- `bogenabschnitt_links`, `bogenabschnitt_rechts`, cm

**Bereiche, Bedingungen und Auswahlentscheidungen:** keine im Buch genannt.

**Abhängigkeiten:** setzt `godetweite` aus Formel 2 voraus; die Mittelmarkierung
entspricht laut Buchtext dem Fadenlauf des Godets.

**Status:** offen (Quelle noch nicht am Original bestätigt, siehe
[formeln_s068.md](formeln_s068.md) Abschnitt 3).

**Offene Fragen oder Widersprüche:** keine über die fehlende Bestätigung hinaus.
