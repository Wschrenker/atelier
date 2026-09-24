# Formeln – s067 (normalisiert)

Technische Fassung zu [formeln_s067.md](formeln_s067.md). Jede Formel verweist
auf ihren Abschnitt dort. Buchfassung und technische Fassung bleiben getrennt.

**Achtung:** s067 ist weiterhin `OCR-Rohfassung – noch nicht menschlich
verifiziert`; es liegt keine „Vorab geklärte formel- und coderelevante
Stellen"-Freigabe vor. Diese Normalisierung entstand auf Werners ausdrückliche
Anweisung als Walking-Skeleton-Lauf und ist deshalb durchgehend `gesperrt`.

## F1 – Godethöhe und Winkel → Saumweite/Optik

- **Quelle:** [formeln_s067.md](formeln_s067.md), Abschnitt 1.
- **Buchfassung:**

```text
[□7] Für eine besonders große Saumweite nimmt man eine eher große Godethöhe und einen großen Winkel (maximal 90°).
□8 Für einen optisch welligen Saum wählt man eine geringe Godethöhe bei mäßigem bis großem Winkel.
Eine dezente Saumweite erzielt man mit geringem Winkel bei jeder Godethöhe.
```

- **Technische Formel:**
  - `saumweite = "groß"` WENN `godethöhe = "groß"` UND `winkel` groß, mit
    `winkel ≤ 90°`
  - `saum_optik = "wellig"` WENN `godethöhe = "gering"` UND
    `winkel ∈ {"mäßig", "groß"}`
  - `saumweite = "dezent"` WENN `winkel = "gering"`, unabhängig von
    `godethöhe`
- **Eingaben und Einheiten:** `godethöhe` (Kategorie gering/mittel/hoch, keine
  Zahlenwerte im Buch benannt); `winkel` (Grad, kategorisiert
  gering/mäßig/groß, harte Obergrenze `90°`).
- **Ausgabe und Einheit:** qualitative Einstufung (`saumweite`: groß/dezent,
  `saum_optik`: wellig); keine Maßzahl.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** `winkel ≤ 90°` ist die
  einzige harte Zahlengrenze auf der Seite. Die Kategorien „gering", „mäßig"
  und „groß" für Winkel und Godethöhe sind im Buchtext nicht mit Zahlengrenzen
  hinterlegt.
- **Abhängigkeiten:** keine zu anderen Seiten ermittelt; exemplifiziert durch
  F3 und F4.
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** Das Kästchenlabel `□7` fehlt in der
  OCR-Fassung (siehe formeln_s067.md, Abschnitt 1) und ist am Original zu
  bestätigen. Ob „gering/mäßig/groß" für Winkel und Godethöhe an anderer
  Stelle im Buch zahlenmäßig definiert sind, ist hier nicht geklärt. Ohne
  solche Zahlengrenzen ist keine eindeutige Implementierung möglich.

## F2 – Stoffart → Saumweite

- **Quelle:** [formeln_s067.md](formeln_s067.md), Abschnitt 2.
- **Buchfassung:**

```text
Feine und leichte Stoffe erfordern eine eher größere Saumweite, während feste und schwere Stoffe eine eher mäßige bis geringe Saumweite benötigen.
```

- **Technische Formel:**
  - `saumweite_tendenz = "eher groß"` WENN `stoffart ∈ {"fein", "leicht"}`
  - `saumweite_tendenz = "eher mäßig bis gering"` WENN
    `stoffart ∈ {"fest", "schwer"}`
- **Eingaben und Einheiten:** `stoffart` als Kategorie (fein/leicht vs.
  fest/schwer); keine Zahlenwerte.
- **Ausgabe und Einheit:** Tendenzaussage zur Saumweite; keine Maßzahl.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** reine Tendenzaussage
  („eher"), kein fester Wert oder Bereich.
- **Abhängigkeiten:** ergänzt F1; das Buch nennt keine Regel, wie
  `saumweite_tendenz` (F2) und `saumweite` (F1) zusammenwirken, wenn sie sich
  widersprechen.
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** Keine Verknüpfungsregel im Buchtext, wie
  diese Stoffart-Tendenz mit der Godethöhe/Winkel-Regel aus F1 zusammen die
  tatsächliche Saumweite bestimmt.

## F3 – Godet-Varianten 1–4 (Bügelrichtung und Material)

- **Quelle:** [formeln_s067.md](formeln_s067.md), Abschnitt 3.
  Zeichnungsgebunden.
- **Buchfassung:**

```text
□3 Godet-Variante 1: Eingesetzte mittelhohe, mäßig weite Godets, nach außen gebügelt, aus festem Material.
□4 Godet-Variante 2: Eingesetzte mittelhohe, mäßig weite Godets, nach innen gebügelt, aus weich fallendem, leichtem Material.
□5 Godet-Variante 3: Eingesetzte kurze, weite Godets, nach außen gebügelt, aus weich fallendem, leichtem Material.
□6 Godet-Variante 4: Eingesetzte hohe, mäßig weite Godets, nach innen gebügelt, aus festem Material.
```

- **Technische Formel:** feste Zuordnungstabelle
  `variante → (godethöhe, godetweite, bügelrichtung, material)`:
  - Variante 1: `godethöhe=mittelhoch, weite=mäßig weit, bügelrichtung=außen, material=fest`
  - Variante 2: `godethöhe=mittelhoch, weite=mäßig weit, bügelrichtung=innen, material=weich/leicht`
  - Variante 3: `godethöhe=kurz, weite=weit, bügelrichtung=außen, material=weich/leicht`
  - Variante 4: `godethöhe=hoch, weite=mäßig weit, bügelrichtung=innen, material=fest`
- **Eingaben und Einheiten:** kategoriale Attribute; keine Zahlenmaße für Höhe
  oder Weite im Buchtext angegeben.
- **Ausgabe und Einheit:** Variantenzuordnung (1–4); katalogartig, keine
  Berechnung.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine Berechnungsregel,
  sondern vier feste Beispielkombinationen.
- **Abhängigkeiten:** exemplifiziert die Auswahlregeln aus F1 (Godethöhe/
  Winkel) und möglicherweise F2 (Material/Stoffart); das Buch verknüpft die
  Varianten nicht formal mit F1/F2.
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** Unklar, ob diese vier Varianten eine
  vollständige Aufzählung oder nur Beispiele sind. Ohne Zahlenwerte für Höhe
  und Weite ist keine Überführung in eine Rechenregel möglich.

## F4 – Angeschnittene Godets am 10-Bahnenrock

- **Quelle:** [formeln_s067.md](formeln_s067.md), Abschnitt 4.
  Zeichnungsgebunden.
- **Buchfassung:**

```text
□7 Angeschnittene hohe und weite Godets am 10-Bahnenrock, Nähte nach außen gebügelt.
□8 Angeschnittene kurze und mäßig weite Godets am 10-Bahnenrock, Nähte nach innen gebügelt.
```

- **Technische Formel:** zwei weitere feste Beispielkombinationen für ein
  10-Bahnenrock-Modell:
  - `□7: godethöhe=hoch, weite=weit, bügelrichtung=außen, ausführung=angeschnitten`
  - `□8: godethöhe=kurz, weite=mäßig weit, bügelrichtung=innen, ausführung=angeschnitten`
- **Eingaben und Einheiten:** `bahnenanzahl=10` (Rockmodell); Godethöhe/-weite
  kategorial; Nahtart „angeschnitten".
- **Ausgabe und Einheit:** Variantenbeschreibung; keine Maßzahl.
- **Bereiche, Bedingungen, Auswahlentscheidungen:** keine Rechnung, feste
  Beispielkombination.
- **Abhängigkeiten:** thematisch verwandt mit F1/F3; `bahnenanzahl=10`
  verweist auf ein eigenes Rockmodell (10-Bahnenrock), dessen Grundschnitt
  hier nicht ermittelt und deshalb nicht verlinkt wird.
- **Status:** gesperrt.
- **Offene Fragen oder Widersprüche:** Laut formeln_s067.md sind die
  Kästchenlabels `7`/`8` auf der Seite doppelt vergeben (Fließtext oben,
  diese Bildunterschriften unten). Ohne Prüfung am Original bleibt offen, ob
  hier dieselbe Zählung wie in F1 gemeint ist oder eine unabhängige.
