# Formeln s172 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s172.md`](formeln_s172.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Beide Formeln stehen
deshalb auf `offen`. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz für
die Bestätigung.

## Formel 1 – Modell-Passformklasse-Zuordnung

- **Quelle:** [`formeln_s172.md`](formeln_s172.md), Abschnitt 1
- **Buchfassung:**
  ```text
  ☐1 Jeansjacke aus tailliertem OT-GS mit Brustabnäher (PK 4-5)
  ☐2 Klassische Weste aus tailliertem OT-GS mit Brustabnäher (PK 4-5)
  ☐4 Enges Kleid (Etuhleid) aus dem taillierten OT-GS mit Brustabnäher (PK 3-4)
  ☐5 Damen-Blazer aus dem taillierten OT-GS mit Brustabnäher (PK 5-7)
  ☐6 Trenchcoat aus dem taillierten OT-GS mit Brustabnäher (PK 9-10)
  ```
- **Technische Formel:**
  ```text
  pk_bereich = lookup_modelltyp(modell)

  lookup_modelltyp:
    Jeansjacke (tailliertes OT-GS, Brustabnäher)      -> [4, 5]
    Klassische Weste (tailliertes OT-GS, Brustabnäher) -> [4, 5]
    Enges Kleid/Etuikleid (tailliertes OT-GS, Brustabnäher) -> [3, 4]
    Damen-Blazer (tailliertes OT-GS, Brustabnäher)     -> [5, 7]
    Trenchcoat (tailliertes OT-GS, Brustabnäher)       -> [9, 10]
  ```
- **Eingaben und Einheiten:** `modell` (Modelltyp, kategorial, hier fünf Beispiele
  aus tailliertem Oberteil-Grundschnitt mit Brustabnäher); keine physische
  Einheit.
- **Ausgabe und Einheit:** `pk_bereich` – Passformklasse-Bereich (dimensionslose
  Klassenskala), als Intervall mit Unter- und Obergrenze.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Jeder Bereich ist auf
  dieser Seite als geschlossenes Intervall mit ganzzahligen Grenzen angegeben
  (z. B. „4-5"); kein fester Einzelwert. Die Beispiele gelten ausdrücklich für
  Modelle „aus tailliertem OT-GS mit Brustabnäher" – ob dieselbe Zuordnung auch
  für andere Grundschnitt-Varianten gilt, ist auf dieser Seite nicht erkennbar.
- **Abhängigkeiten:** Bedeutung von „PK" und „Passformklasse" allgemein: siehe
  Seite 176 („Passformklassen und Zugaben", laut Inhaltsverzeichnis dieser
  Seite) – nicht kopiert, nur zu verlinken, sobald diese Seite bearbeitet ist.
  [[Formel 2]] nutzt denselben PK-Bereich 4-5 für ☐1/☐2.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Ob die Zuordnung Modelltyp → PK-Bereich eine feste Buchregel oder nur ein
    Beispiel ist, ist ohne Seite 176 nicht zu klären.
  - Kategorisierung `modell` ist informell (Fließtext-Beschreibung), keine
    eindeutige Codeliste.

## Formel 2 – Passform-Piktogramm: Referenzmaße und Weitenzugaben für PK 4-5

- **Quelle:** [`formeln_s172.md`](formeln_s172.md), Abschnitt 2
  (zeichnungsgebunden, `skizzen/s172_skizze_03.png`)
- **Buchfassung:**
  ```text
  Passform-Piktogramm mit Weitenzugaben (☐3)

  Höhe: 168
  Brust: 88
  Taille: 72
  Hüfte: 97

  Passformklasse: 4 - 5
  Brust-Weitenzugabe: 7 - 11
  Taillen-Weitenzugabe: 6 - 10
  Hüft-Weitenzugabe: 4 - 8
  ```
- **Technische Formel:**
  ```text
  Referenzkörper (cm):
    hoehe_ref  = 168
    brust_ref  = 88
    taille_ref = 72
    huefte_ref = 97

  Weitenzugabe je Zone für pk_bereich = [4, 5]:
    zugabe_brust  ∈ [7, 11]   cm
    zugabe_taille ∈ [6, 10]   cm
    zugabe_huefte ∈ [4, 8]    cm
  ```
- **Eingaben und Einheiten:** `hoehe_ref`, `brust_ref`, `taille_ref`,
  `huefte_ref` (cm) – Referenz-Körpermaße der Zeichnung; `pk_bereich` (dimensionslos,
  hier fest 4-5 laut Zeichnung).
- **Ausgabe und Einheit:** `zugabe_brust`, `zugabe_taille`, `zugabe_huefte`
  (cm) – Weitenzugabe-Bereiche je Körperzone für die abgebildete
  Passformklasse.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Alle drei Zugabewerte
  bleiben Bereiche (Intervalle), kein Default gewählt. Die Piktogramm-Werte
  gelten ausdrücklich nur für PK 4-5; für andere PK-Bereiche (z. B. 3-4, 5-7,
  9-10 aus [[Formel 1]]) liegen auf dieser Seite keine Zahlen vor.
- **Abhängigkeiten:** [[Formel 1]] (gleicher PK-Bereich 4-5 bei ☐1/☐2);
  allgemeine Erläuterung des Passform-Piktogramms laut Inhaltsverzeichnis auf
  Seite 176 – nicht auf dieser Seite, nur zu verlinken.
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Bedeutung der roten/pinken Hervorhebung der Taillen-Box ist ungeklärt
    (z. B. Warnhinweis, Sonderfall) – auf dieser Seite nicht erklärt.
  - Ob `hoehe_ref` (168) als Körpergröße oder als andere Bezugslänge zu lesen
    ist, ist aus der Zeichnung allein nicht sicher; keine Beschriftung
    „Körpergröße" auf dieser Seite sichtbar.
  - Wie sich die Weitenzugabe-Bereiche aus den Referenzmaßen ableiten
    (Formel, Tabelle oder reine Beispielwerte), ist ohne Seite 176/177
    („Konstruktionstabelle") nicht erkennbar.
