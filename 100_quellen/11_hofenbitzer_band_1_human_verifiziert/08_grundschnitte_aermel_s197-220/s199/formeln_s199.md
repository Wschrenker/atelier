# Formelstellen – s199 (OCR-Rohfassung)

**OCR-Rohfassung – noch nicht menschlich verifiziert.**

Mechanisch aus dem OCR-Text (`ocr_s199.md`), den erkannten Tabellen
(`tabellen_s199.md`) und der ergänzten Armloch-Zeichnung
(`skizzen/s199_skizze_03.png`) zusammengetragen: Zeilen mit Gleichheits-,
Prozent-, Bruch- oder Bereichsangaben sowie mit einem freistehenden
Rechenzeichen zwischen Größen. Fototreu und OCR-nah, ausdrücklich ungeprüft
und **keine** fachlich normalisierten Formeln. Die Auswahl ist rein
mechanisch; sie kann zu viel und zu wenig enthalten.

Diese Seite liegt außerhalb der drei Kapitel, für die der volle
Extraktions-/Normalisierungs-Workflow vorgesehen ist
(`03_grundschnitte_roecke`, `04_modelle_roecke`, `07_grundschnitte_oberteile`).
Diese Datei bleibt deshalb bewusst bei der fototreuen Sammlung stehen; eine
separate `formeln_s199_normalisiert.md` entsteht erst nach einer eigenen
Klärung, ob und wie der Workflow auf dieses Kapitel ausgeweitet wird.

## Block text (ArD aus OaU)

```text
Sicherheitshalber den ArD aus dem OaU berechnen (siehe Seite 14): OaU : 10 · 6 - 7,5 cm
```

Quelle: `ocr_s199.md`, Zeile 117.

## Block text (PK-Berechnungssatz, OCR erkennbar fehlerhaft)

```text
In Umlenkung (Anregal) mit Oberteil minus ½ Brutumfang (Körperteil)
```

Quelle: `ocr_s199.md`, Zeilen 133–134. Laut `s199.md` ("Bekannte auffällige
Stellen im Rohtext") ist dieser Satz erkennbar fehlerhaft gelesen; der
tatsächliche Kastentext am Original ist noch nicht bestätigt.

## Block text (PK-Schlussformel)

```text
* PK = BrW-Zugabe zum ½ Grundschnitt
oder
½ BrW (½ gemessene BrW am Schnitt)
- ½ BrU (½ gemesser BrU am Körper)
```

Quelle: `ocr_s199.md`, Zeilen 140–146.

## Block tabelle (Tabelle 1 – Konstruktionstabelle, Zeilenformeln)

```text
Ärmellänge ± = Ärmellänge (ÄL)
Oberärmumfang + = Oberärmweite (OaW)
Handgelenkumfang + = Saumweite (ÄSaW)
Einhalteweite in cm = AlU + Einhalteweite in %
Ärmelkugelumfang (ÄKU) = AlU + Einhalteweite in cm
```

Quelle: `tabellen_s199.md`, Tabelle 1 (`tbl-0.md`), Zeilen 12–16.

## Block tabelle (Tabelle 2 – Berechnungstabelle für Ärmel-Konstruktionen)

```text
Schmaler Ärmel:
  Oberärmweite (OaW) = OaU + 0,7 bis 1 · PK* des Oberteils
  Ärmelsaumweite (ÄSaW) = HgU + 1 bis 2 · PK* des Oberteils
  Einhalteweite in % = + 3% bis + 10% des AlU

Enger Ärmel:
  Oberärmweite (OaW) = OaU + 0,5 bis 1 · PK* des Oberteils
  Ärmelsaumweite (ÄSaW) = HgU + 0 bis 1,5 · PK* des Oberteils
  Einhalteweite in % = 0% bis + 3% des AlU

Welter/Weiter Ärmel:
  Oberärmweite (OaW) = OaU + 1 bis 2,5 · PK* des Oberteils
  Ärmelsaumweite (ÄSaW) = entsteht automatisch
  Einhalteweite in % = - 1% bis + 3% des AlU
```

Quelle: `tabellen_s199.md`, Tabelle 2 (`tbl-1.md`), Zeilen 23–25. Die
Buchfassung schreibt in Zeile 25 „Welter Ärmel“; `s199.md` vermerkt dies
bereits als vermutlichen Lesefehler für „Weiter Ärmel“ (Prüfstelle 3), hier
unverändert übernommen.

## Block text (Einhalteweite-Wahl nach Material, Bereichsangaben)

```text
Sehr geringe EW: 0% bis 3%
Geringe EW: 3% bis 5%
Mittlere EW: 5% bis 7%
Größe EW: 7% bis 10%
```

Quelle: `ocr_s199.md`, Zeilen 73, 80, 88, 96.

## Block zeichnung (Armloch-Zeichnung, geometrische Beziehungen)

```text
tP-Position an der Grundlinie: 1/3 (VT-Seite) und 2/3 (RT-Seite)
1/4 ArD+ (Strecke von vÄP bis zur 1/3-Marke)
ArD+ = ArD + Zugabe
```

Quelle: zeichnungsgebunden, `skizzen/s199_skizze_03.png` (manuell ergänzter
Ausschnitt, siehe `skizzen_s199.json`, Region `manuell-03`).

Hinweis: Der Fließtext (`ocr_s199.md`, Zeilen 106–108) nennt für dieselbe
tP-Position „½ ArD am VT und … ½ ArD am RT“, während die Zeichnung „1/3“ und
„2/3“ zeigt. Dieser Widerspruch zwischen Text und Zeichnung ist ungeprüft und
wird hier nicht aufgelöst.
