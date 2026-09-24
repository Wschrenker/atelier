# Formeln s040 – Normalisierung (Gerader Bund (2): Bund mit Über- und Untertritt)

Alle Einträge tragen Status `gesperrt`, solange s040 nicht menschlich
verifiziert ist (siehe [s040.md](s040.md) und der Hinweis in
[formeln_s040.md](formeln_s040.md)). Diese Fassung dient als
Walking-Skeleton-Schritt, um Struktur und Felder zu erproben, nicht als
freigegebene Fachregel.

## Formel 1: Knopflochlänge

- **Quelle:** [formeln_s040.md, Formel 1](formeln_s040.md#formel-1-knopflochlänge)
- **Buchfassung:**
  ```text
  Knopflochlänge = Knopfdurchmesser + ca. 2 mm.
  ```
- **Technische Formel:** `knopflochlaenge = knopfdurchmesser + zugabe`
- **Eingaben und Einheiten:** `knopfdurchmesser` (mm); `zugabe` ≈ 2 mm (Buch
  nennt „ca.", kein fester Wert).
- **Ausgabe und Einheit:** `knopflochlaenge` (mm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** `zugabe` ist als „ca."
  gekennzeichnet – kein fixer Wert, kein Default ohne weitere Buchregel
  wählbar.
- **Abhängigkeiten:** `knopfdurchmesser` ist auf dieser Seite nicht selbst
  hergeleitet, sondern Modell-/Kundenvorgabe (kein Verweis auf andere
  Hofenbitzer-Formel erkennbar).
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** Seite nicht menschlich verifiziert;
  Werner muss Wortlaut, Zahl „2 mm" und den „ca."-Charakter am Original
  bestätigen, bevor der Status wechseln kann.

## Formel 2: Untertrittbreite

- **Quelle:** [formeln_s040.md, Formel 2](formeln_s040.md#formel-2-untertrittbreite)
- **Buchfassung:**
  ```text
  Der Untertritt sollte mindestens so lang sein wie das Knopfloch, better 0,5 bis 1 cm länger.
  ```
- **Technische Formel:**
  `untertrittbreite_min = knopflochlaenge`
  `untertrittbreite_empfohlen ∈ [knopflochlaenge + 0,5 cm; knopflochlaenge + 1 cm]`
- **Eingaben und Einheiten:** `knopflochlaenge` (aus Formel 1, dort in mm
  angegeben; diese Buchstelle rechnet in cm-Zuschlägen – Einheiten laut Buch
  nicht vereinheitlicht, hier bewusst nebeneinander dokumentiert statt
  geglättet).
- **Ausgabe und Einheit:** `untertrittbreite` (cm bzw. mm, je nach
  Bezugsgröße), als Mindestwert plus empfohlener Bereichszuschlag.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Untergrenze
  „mindestens so lang wie das Knopfloch"; empfohlener Zuschlagsbereich
  0,5–1 cm bleibt Bereich, kein fester Auswahlwert im Buch angegeben.
- **Abhängigkeiten:** hängt von Formel 1 (`knopflochlaenge`) ab.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** Seite nicht menschlich verifiziert;
  zusätzlich klärt Werner, ob OCR-Wort „better" tatsächlich „besser" heißt und
  ob die cm/mm-Einheiten in Formel 1 und 2 im Original tatsächlich
  unterschiedlich sind oder ein OCR-Artefakt vorliegt.

## Auswahlregel 3: Seite von Übertritt und Untertritt

- **Quelle:** [formeln_s040.md, Auswahlregel 3](formeln_s040.md#auswahlregel-3-seite-von-übertritt-und-untertritt)
- **Buchfassung:**
  ```text
  Damen schließen "rechts über links", während Herren "links über rechts" schließen, d.h. bei Damen liegt die rechte Bekleidungsselte am Verschluss oben, der Übertritt ist auf der rechten Seite des Kleidungsstücks und der Untertritt auf der linken Seite - bei Herren ist der Verschluss traditionell an der anderen Seite.

  Bei vorderen Verschlüssen kommt der Übertritt bei Damenmode auf die rechte Körperseite. [...] Der Übertritt kommt hinten auf die linke Körperseite, bzw. auf das linke hintere Schnittteil.

  Bei einem Bund mit Verschluss an der linken Seitennaht, kommt der Übertritt an das linke vordere Bundende. Der Untertritt wird jeweils am anderen Bundende platziert.
  ```
- **Technische Formel:** Auswahlregel, keine Rechenformel:
  `seite_uebertritt = f(geschlecht, verschlussposition)`, mit
  `seite_untertritt` = jeweils andere Seite/das andere Bundende.
- **Eingaben und Einheiten:** `geschlecht` (Damen/Herren, kategorial);
  `verschlussposition` (vM, hM, seitliche Naht – kategorial, keine
  physikalische Einheit).
- **Ausgabe und Einheit:** `seite_uebertritt`, `seite_untertritt`
  (kategorial: rechts/links bzw. konkretes Bundende).
- **Bereiche, Bedingungen und Auswahlentscheidungen:**
  - Damen, vorderer Verschluss → Übertritt rechte Körperseite.
  - Damen, hinterer Verschluss → Übertritt linke Körperseite / linkes
    hinteres Schnittteil.
  - Herren → „traditionell" andere Seite als Damen (Buch spezifiziert hier
    nicht vorne/hinten getrennt wie bei Damen).
  - Seitennaht-Verschluss (Beispiel im Buch: linke Seitennaht) → Übertritt am
    genannten Bundende, Untertritt am jeweils anderen Bundende.
- **Abhängigkeiten:** keine Rechenabhängigkeit zu Formel 1/2; wirkt als
  vorgelagerte Auswahlentscheidung für deren Platzierung am Bund.
- **Status:** gesperrt
- **Offene Fragen oder Widersprüche:** Seite nicht menschlich verifiziert;
  Herren-Fall ist im Buchtext nur allgemein („traditionell an der anderen
  Seite") beschrieben, nicht so differenziert wie der Damen-Fall – ob das
  eine bewusste Buchlücke oder ein Auszugsproblem ist, klärt Werner am
  Original.
