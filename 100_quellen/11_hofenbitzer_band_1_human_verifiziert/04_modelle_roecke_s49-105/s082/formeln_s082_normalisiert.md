# Formeln s082 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s082.md`](formeln_s082.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle Punkte stehen
deshalb auf `offen`, unabhängig von der inhaltlichen Klarheit der Buchfassung.
Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für die Bestätigung.

Anders als bei den meisten anderen Seiten dieses Buches enthält s082 keine
Formel mit Zahlenwert. Die Punkte 1–4 sind benannte geometrische
Konstruktionsgrößen (`FaI`, `FaT`) und ihre textlich/zeichnerisch belegte
Beziehung zueinander; Punkt 5 ist eine Stückzahl-Beziehung (Falten pro Bahn),
kein Maß.

## Formel 1 – Falteninhalt (FaI), Definition

- **Quelle:** [`formeln_s082.md`](formeln_s082.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Die Falteninhalte (FaI) werden an allen Teilen des geraden Bahnenrocks gleichmäßig angezeichnet.
  ```
- **Technische Formel:**
  ```text
  FaI = Falteninhalt  (Eingabeparameter je Bahn, cm; auf dieser Seite kein Zahlenwert)
  FaI_i = FaI  für alle Bahnen i = 1..10  (gleichmäßig laut Buchtext)
  ```
- **Eingaben und Einheiten:** `FaI` (cm), auf dieser Seite unbeziffert.
- **Ausgabe und Einheit:** Breite/Position der Faltenzugabe an jeder
  Teilungsnaht bzw. jedem Bahnende (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „gleichmäßig ... an
  allen Teilen" – kein bahnenindividueller Wert laut Buchtext vorgesehen.
- **Abhängigkeiten:** [[Formel 2]] (FaT als Teilgröße von FaI), [[Formel 5]]
  (Anzahl der Bahnen/Falten).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kein Zahlenwert für FaI auf dieser Seite; Herkunft eines möglichen
    Zahlenwerts (andere Seite oder freie Wahl der Schneiderin) nicht ermittelt.

## Formel 2 – Faltentiefe (FaT) als Abstand zur Faltenmitte

- **Quelle:** [`formeln_s082.md`](formeln_s082.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die Bruchlinie in der Faltenmitte ist der Falten-Innenbruch. Der Abstand dorthin ist die Faltentiefe (FaT).
  ```
- **Technische Formel:**
  ```text
  FaT = Abstand(Teilungsnaht, Falten-Innenbruch)
  Falten-Innenbruch liegt "in der Faltenmitte" von FaI

  Lesart (nicht im Buch als Gleichung ausgeschrieben):
  FaT ≈ FaI / 2
  ```
- **Eingaben und Einheiten:** `FaI` (cm), unbeziffert.
- **Ausgabe und Einheit:** `FaT` (cm), unbeziffert; Lage der Bruchlinie
  (Falten-Innenbruch).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Bereichsangabe im
  Buch. Die Gleichung `FaT ≈ FaI / 2` ist eine eigene Lesart der Formulierung
  „in der Faltenmitte", keine im Buch ausgeschriebene Formel.
- **Abhängigkeiten:** [[Formel 1]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob FaT exakt FaI/2 entspricht oder nur ungefähr „in der Mitte" liegt, ist
    am Buchtext nicht eindeutig zu entscheiden.
  - Die Zeichnung (`skizzen/s082_skizze_02.png`) zeigt den FaT-Maßpfeil optisch
    kürzer als den FaI-Maßpfeil, was mit einer Halbierung vereinbar wäre, aber
    ein Foto liefert dafür keinen Beweis.

## Formel 3 – Faltentiefe an Seitennähten statt vollem Falteninhalt

- **Quelle:** [`formeln_s082.md`](formeln_s082.md), Abschnitt 3
- **Buchfassung:**
  ```text
  An den Seitennahten werden jeweils nur die Faltentiefen angezeichnet. So ist die Ansatznaht an den Falten unsichtbar. Bei Faltenröcken werden Abtrennungen immer an den Faltentiefen vorgenommen.
  ```
- **Technische Formel:**
  ```text
  fuer Teilungsnaht_i:
      wenn Teilungsnaht_i = aeussere Seitennaht (Rand des VT-/RT-Teils):
          angezeichnete_Groesse = FaT
      sonst:
          angezeichnete_Groesse = FaI
  ```
- **Eingaben und Einheiten:** `FaI`, `FaT` (cm, unbeziffert); Position der Naht
  (innere Teilungsnaht vs. äußere Seitennaht).
- **Ausgabe und Einheit:** anzuzeichnende Maßgröße je Nahtposition (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Auswahlregel nach
  Nahtposition (Bedingung, kein fester Zahlenwert).
- **Abhängigkeiten:** [[Formel 1]], [[Formel 2]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - „Seitennaht" bezeichnet hier vermutlich die äußeren Kanten des VT-/RT-Teils
    (vM-/RV-Rand laut Zeichnung), nicht zwingend die reale Rock-Seitennaht am
    Körper – Zuordnung aus der Zeichnung plausibel, aber textlich nicht so
    benannt.

## Formel 4 – Faltenschraffur/Legerichtung: Faltenkante auf Anstoßlinie legen

- **Quelle:** [`formeln_s082.md`](formeln_s082.md), Abschnitt 4
- **Buchfassung:**
  ```text
  Die Faltenschraffur markiert die als Falte zu legende Fläche. Diese Fläche ist bei gelegter (gebügelter) Falte nicht sightbar. Der Pfeil der Legerschtung kennzeichnet an seinem Ursprung die Faltenkante und an seiner Spitze die Faltenanstöblinie; die Faltenkante wird auf die Anstöblinie gelegt.
  ```
- **Technische Formel:**
  ```text
  Faltenkante (Pfeilursprung) wird auf Faltenanstoßlinie (Pfeilspitze) gelegt
  => Faltenschraffur-Flaeche liegt danach verdeckt unter der gelegten (gebuegelten) Falte
  ```
- **Eingaben und Einheiten:** Lage von Faltenkante und Faltenanstoßlinie (aus
  Zeichnung, keine Zahlenwerte auf dieser Seite).
- **Ausgabe und Einheit:** gelegte/gebügelte Faltenposition (geometrische
  Zuordnung, keine Einheit).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Zahl; reine
  geometrische Zuordnungsregel (Kante → Linie).
- **Abhängigkeiten:** [[Formel 1]] (Faltenschraffur-Fläche liegt innerhalb der
  FaI-Zone).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kein numerischer Wert; „Legerichtung" ist auf dieser Seite laut Zeile 18
    rundum einheitlich, Ausnahmen laut Zeile 19 möglich, aber keiner
    bestimmten Stelle dieser Seite zugeordnet.

## Formel 5 – Anzahl der Falten aus der Bahnenzahl

- **Quelle:** [`formeln_s082.md`](formeln_s082.md), Abschnitt 5
- **Buchfassung:**
  ```text
  Aus dem geraden 10-Bahnenrock entsteht durch einseitig gelegte (gebügelte) Falten an jeder Teilungsnaht ein Rundum-Faltenrock mit 10 abgenähten Falten.
  ```
- **Technische Formel:**
  ```text
  Anzahl_Falten = Anzahl_Teilungsnaehte_Basismodell
  Buchbeispiel: Anzahl_Bahnen_Basismodell = 10  =>  Anzahl_Falten = 10
  ```
- **Eingaben und Einheiten:** Anzahl der Bahnen/Teilungsnähte des geraden
  Bahnenrock-Grundschnitts (hier: 10, aus dem Modellnamen „10-Bahnenrock").
- **Ausgabe und Einheit:** Anzahl der Falten (Stückzahl, keine physikalische
  Einheit).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine Verallgemeinerung
  auf andere Bahnenzahlen im Buchtext ausgeschrieben; nur der 10-Bahn-Fall
  belegt.
- **Abhängigkeiten:** Basismodell „gerader 10-Bahnenrock" (andere Seite dieses
  Buches, Herkunftsseite auf s082 nicht benannt – nur verlinken, sobald
  bekannt, nicht kopieren).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob die Regel „1 Falte pro Teilungsnaht" allgemein für n Bahnen gilt oder
    nur für dieses 10-Bahn-Modell gemeint ist, ist textlich nicht
    verallgemeinert.
