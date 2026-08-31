# Kleid Lumière — Definition

Stand: 2026-08-31 · Status: **Entwurf aus dem Moodboard, wartet auf Werners Freigabe**

Diese Datei ist das **Scope-Dokument**. Was hier nicht steht, wird nicht gebaut.

Vorlage: Moodboard „KLEID 3 · LUMIÈRE — asymmetrische Eleganz",
`Codex-Bild 31. Aug. 2026, 13_53_03.png`.
Das Moodboard ist eine **Bildvorlage, keine Quelle**. Es liefert die
Modellidee; jede Zahl kommt aus dem Buch oder ist hier als
Modellentscheidung ausgewiesen.

---

## Die Idee

Ein bodenlanges Brautkleid mit **asymmetrischem Wickeloberteil über einer
Schulter**, **offenem V-Rücken** und einem **fließenden A-Linien-Rock mit
Beinschlitz**.

Das Moodboard sagt zum Rock ausdrücklich „ohne seitliches Volumen" und
„weniger Stoff an den Seiten". Deshalb ist der Rock ein **saumerweiterter
Rock (S.42–43)** und **kein Glockenrock** — die Erweiterung wird gleichmäßig
über sechs Stellen verteilt, nicht an die Seitennaht gelegt.

## Die Quellen

| Teil | Buchseite | Bezeichnung im Buch | Lage der Quelle |
|---|---|---|---|
| Maßsatz | S. 20 | DOB-Größentabelle | geprüft |
| Oberteil-Grundgerüst | S. 177–181 | Grundgerüst für sämtliche Oberteil-GS | geprüft |
| Oberteil tailliert | S. 184–185 | Taillierter Oberteil-GS mit Hüftausfall | geprüft |
| Rock-Grundgerüst | S. 33–35 | Gerader Rock-Grundschnitt | geprüft |
| Rock A-Linie | S. 42–43 | Saumerweiterter Rock-Grundschnitt | geprüft |
| Asymmetrische Drapierung | S. 423 | Asymmetrische OT-Gestaltung, Wickeloptik ❑8 | **roh, keine Zahlen** |

Transkripte: `100_quellen/10_hofenbitzer_b1/2_transkript/hofenbitzer_band_1_digital/`

**S. 44 (echter Glockenrock) wird für dieses Kleid nicht benutzt.** Das Modul
liegt trotzdem in `500_python/10_rechnung/rock/glocke.py`, weil S.44 die
einzige bereits **fachlich freigegebene** Rockseite ist und als Prüfwert dient.

---

## Entscheidungen

Die Spalte **Herkunft** ist das Wichtigste an dieser Tabelle. `Buch` heißt:
steht so im Transkript. `Modell` heißt: von uns gewählt, das Buch sagt dazu
nichts.

| Entscheidung | Festlegung | Herkunft | Status |
|---|---|---|---|
| Referenzgröße | 38 | Buch S.20 | ✅ |
| Passformklasse Oberteil | PK 4 | Buch S.176/177 | ✅ |
| BrU-Zugabe | + 8 cm → BrW 96 | Buch S.177 | ✅ |
| HüU-Zugabe Oberteil | + 4 cm | Buch S.177 | ✅ |
| **TaU-Zugabe, Rock und Oberteil gemeinsam** | + 2 cm → TaW 74 | Buch S.33 (Spanne 1–2) | ✅ |
| HüU-Zugabe Rock | + 3 cm → HüW 100 | Buch S.33 (Spanne 2–3) | ✅ |
| Zwischenraum RT/VT | 8,5 cm | Buch S.180 (Spanne 7–10) | ✅ |
| vAbl-Zuschlag | + 1,0 cm | Buch S.184 (bis PK 4) | ✅ |
| Aufteilung TaAf | SN 2,0 · shAbl 2,37 · hAbl 3,28 | Buch S.185 (Spannen) | ✅ |
| hAbl-Länge | 10 cm | Buch S.185 Abb. ❑8c | ✅ |
| Schulterabnäher | **entfällt** | Modell | ✅ |
| Rocklänge (MoL) | 106 cm = sTaH Gr. 38 | Buch S.20 + Modell | ✅ |
| Saumerweiterung | 90 cm → 15 cm je Keil, Saumweite 190 cm | Modell | ⬜ am Stoff prüfen |
| Beinschlitz | 62 cm ab Saum, an der vM | Modell | ⬜ |
| Tiefe V-Rücken | Spitze 6 cm oberhalb der Taille | Modell | ⬜ |
| Wickelkante an der linken SN | 7 cm unter der Brustlinie | Modell | ⬜ |
| Untertritt-Oberkante | SN 1 cm unter, vM 4 cm über der Brustlinie | Modell | ⬜ |
| Taillennaht | ja, durchgehend | Modell | ✅ |
| Ärmel | ohne | Modell | ✅ |
| Rückenverschluss | hM-Naht im Oberteil und im Rock, Knopfleiste/RV | Modell | ⬜ Lage offen |
| Nahtzugaben | **nicht enthalten** | — | ⬜ |
| Futter / Unterkleid | offen | — | ⬜ |
| Brustabnäher | **nur als Konstruktionslinie**, siehe unten | — | 🔒 |

## Der offene Punkt mit Gewicht: der Brustabnäher

S.184 bestimmt den Brustabnäher in Schritt ㉖/㉗ **grafisch**:

> ㉖ Rechts der vorderen Armlinie den maximalen Abstand zur Armlinie
> anzeichnen → Li26.
> ㉗ Das dargestellte Dreieck kopieren, um den BrP drehen und den vSuP1
> maximal bis zur Li26 drehen und anlegen.

Aus dem Transkript geht **nicht** hervor, welche Linie Li26 genau ist und wo
der geöffnete Abnäher anschließend liegt. Der Code nimmt die **vordere
Seitenlinie** als Li26 an und rechnet daraus **13,5° Drehung um den BrP**.
Diese Zahl steht auf jedem Vorderteil im DXF.

**Der Abnäher ist im Schnitt nicht ausgeschnitten.** Eingezeichnet sind nur
die Brustabnäher-Linie (S.181 Schritt ㉒) und der BrP. Grund: solange Li26
nicht am Buch geprüft ist, wäre ein ausgeschnittener Abnäher eine erfundene
Zahl — und in einem Wickeloberteil, dessen Abnäherinhalt ohnehin in
Drapierfalten wandert (S.423 ❑7/❑8), die falsche Stelle zum Raten.

**Werner prüft am Buch, Abb. ❑8b auf S.184.** Danach wird der Abnäher
entweder in die Seitennaht („aufspringender Abnäher", S.423 ❑7) oder in
diagonale Falten verlegt.

## Was das Buch zur Drapierung sagt — und was nicht

S.423 ist im Repo als Rohtranskript vorhanden. Es enthält **keine einzige
Zahl**. Es sagt:

- Beide Abnäher können aufspringend oder als Falte verarbeitet werden.
- Am schönsten fallen drapierte Stoffe, wenn die Faltenkanten im schrägen
  Fadenlauf liegen.
- Das obere Wickelteil wird in der Seitennaht mitgenäht.
- Das linke VT (Untertritt) kann mit einem gewöhnlichen Brustabnäher
  gearbeitet werden.
- Die Falten- und Ausschnittgestaltung erfolgt **am gespiegelten GS**.

Der Schnitt setzt genau das um: das rVT ist **ein Teil über die ganze
Vorderbreite** (gespiegelter GS), das lVT ist der Untertritt. Die Zahl,
Lage und Tiefe der Falten sind **nicht** im Schnitt — sie werden an der
Puppe gesteckt.

---

## ⚠️ Fachnähte und Verarbeitungen — Werner prüft am Buch

| # | Thema | Buchstelle |
|---:|---|---|
| 1 | Ansatz-/Taillennaht Rock an Oberteil | S. 406–407, 438–439 |
| 2 | Seitennaht mit eingefasstem Wickelteil (drei Lagen) | S. 423 ❑8 |
| 3 | Drapierfalten / aufspringende Abnäher — Fixierung und Auslauf | S. 423 ❑7, ❑8 |
| 4 | Asymmetrischer Ausschnitt mit Beleg | S. 423 ❑8b + Belege-Kapitel |
| 5 | Armloch-Verarbeitung, ärmellos | ? |
| 6 | Knopfleiste / Reißverschluss in der hM | ? |
| 7 | Beinschlitz im saumerweiterten Rock | ? |
| 8 | Schmaler Saum bei großer Saumweite | ? |
| 9 | Aushängen vor dem Saumen | ? — evtl. gar nicht im Buch |
| 10 | Futter / Unterkleid | ? |
| 11 | Produktionsschnitt + Nahtzugaben | S. 36, 92–97 |

## Was bewusst draußen bleibt

Schleppe · Korsage · Prinzessnaht · Ärmel · Volants · Kräuselweite ·
Glockenrock. Nicht verworfen — vertagt.
