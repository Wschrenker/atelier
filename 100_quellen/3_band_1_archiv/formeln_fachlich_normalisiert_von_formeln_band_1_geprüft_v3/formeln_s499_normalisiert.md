# Fachlich normalisierte Formeln — S. 499

Extraktionsstand: v3
Quelle der Normalisierung: `formeln_s499.md`
Originaltranskript: `s499.md`
Buchseite: Hofenbitzer, Band 1, S. 499

Die Seite ist die zweite Seite des Jogginghosen-Grundschnitts. Sie zeigt die Zeichnung `□2 Grundschnitt enge Jogginghose mit Taillenbeleg`, die Schritte 16 bis 24 sowie den angeschnittenen Bund und das Strickbündchen. Der Schritttext der Schritte 1 bis 15 und die Konstruktionstabelle stehen auf S. 498.

Alle sieben extrahierten Kandidatenzeilen sind Beschriftungen der Zeichnung `□2`. Fünf davon wiederholen Rechenbeziehungen, deren Schritttext auf S. 498 steht; zwei tragen Beziehungen, die im Schritttext von S. 498 nicht vorkommen. Nur diese beiden erhalten hier eine eigene Formel-ID.

## HOF-B1-S499-F01 — Wadenhöhe aus der Kniehöhe

- **Fachlicher Zweck:** Den Höhenabstand der Wadenlinie unterhalb der Knielinie aus der bereits berechneten Kniehöhe bestimmen.
- **Quelle:** `formeln_s499.md`, Zeile 9; Originaltranskript `s499.md`, Zeile 14; Buchseite 499.
- **Originalbezeichnung:** `WaH = KnH : 2`
- **Normalisierte Bezeichnung:** `wadenhoehe_jogginghose`

### Buchfassung

```text
- WaH = KnH : 2
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `kniehoehe` | KnH | 32 (Konstruktionstabelle S. 498) | cm |
| `halbierungsfaktor` | `: 2` | 2 | dimensionslos |

### Formel und Rechenschritte

```text
wadenhoehe = kniehoehe / 2

Buchwert der Konstruktionstabelle auf S. 498 (KnH = 32 cm):
wadenhoehe = 32 cm / 2 = 16 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `wadenhoehe` | Höhenabstand zwischen Knielinie und Wadenlinie im Grundgerüst | cm |

- **Abhängigkeiten:** `KnH` aus der Konstruktionstabelle auf S. 498 (`SrH : 10 · 4`), diese wiederum aus `SrH = sTaH − SiH`.
- **Gültigkeitsbereich:** Grundgerüst der engen Jogginghose, Zeichnung `□2`; gilt für Vorder- und Rückteil gleich, weil die Wadenlinie durchgehend abgewinkelt wird.
- **Technische Randbedingung:** Die Beschriftung nennt keine Richtung. Schritt 11 auf S. 498 („Von dort die WaH abtragen, abwinkeln → Wadenlinie") legt die Richtung nach unten von der Knielinie aus fest; die Richtung stammt also aus der Nachbarseite und ist hier als gekennzeichneter Kontext geführt. Der eingesetzte Wert `KnH = 32 cm` stammt ebenfalls aus der Tabelle der Nachbarseite; S. 499 druckt kein Ergebnis.
- **Offene Fragen oder Widersprüche:** Keine Rechenunsicherheit. Die Kette `sTaH → SrH → KnH → WaH` ist geschlossen; erst diese Beschriftung belegt `WaH` überhaupt als Rechenwert, denn die Konstruktionstabelle auf S. 498 führt keine `WaH`-Zeile.
- **Abgrenzung:** Dieselbe Beziehung steht auf S. 501 als Beschriftung der Leggings-Zeichnung und ist dort als `HOF-B1-S501-F09` eigenständig geführt. Jogginghose und Leggings sind zwei verschiedene Grundschnitte mit eigener Schrittfolge; keine der beiden Seiten erklärt eine Identität. Die IDs bleiben deshalb getrennt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `WaH` als abgeleiteten Wert aus `KnH` führen und nicht als eigenes Körpermaß einlesen. Die Wadenlinie liegt bei `KnH + WaH` unterhalb der Schrittlinie, nicht bei `WaH` unterhalb der Taillenlinie.

## HOF-B1-S499-F02 — Höhenabstand der Hüftlinie

- **Fachlicher Zweck:** Den Höhenabstand der Hüftlinie aus dem Hüftumfang und einem festen Zuschlag bestimmen.
- **Quelle:** `formeln_s499.md`, Zeile 13; Originaltranskript `s499.md`, Zeile 18; Buchseite 499.
- **Originalbezeichnung:** `HüU : 20 + 3 cm`
- **Normalisierte Bezeichnung:** `hueftlinienabstand_jogginghose`

### Buchfassung

```text
- HüU : 20 + 3 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hueftumfang` | HüU | 97 (Konstruktionstabelle S. 498) | cm |
| `konstante_hueftlinienzugabe` | `3 cm` | 3 | cm |

### Formel und Rechenschritte

```text
hueftlinienabstand = (hueftumfang / 20) + 3 cm

Buchwert der Konstruktionstabelle auf S. 498 (HüU = 97 cm):
hueftlinienabstand = (97 cm / 20) + 3 cm = 4,85 cm + 3 cm = 7,85 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hueftlinienabstand` | Höhenabstand zwischen Schrittlinie und Hüftlinie im Grundgerüst | cm |

- **Abhängigkeiten:** `HüU` aus der Konstruktionstabelle auf S. 498; die Jogginghose reduziert die Umfangsmaße ausdrücklich **nicht** (S. 498: „Die Umfangsmaße werden aus diesem Grund nicht reduziert").
- **Gültigkeitsbereich:** Grundgerüst der engen Jogginghose, Zeichnung `□2`.
- **Technische Randbedingung:** Die Beschriftung nennt weder Ausgangs- noch Zielpunkt der Strecke. Sie steht in der Zeichnung als Höhenmaß zwischen Schritt- und Hüftlinie; der Schritttext auf S. 498 führt diesen Schritt nicht auf. Die Lesart „von der Schrittlinie nach oben" stützt sich auf die Zeichnung und auf die gleichnamigen Beziehungen auf S. 110 und S. 495, nicht auf den Schritttext dieser Konstruktion.
- **Offene Fragen oder Widersprüche:** Der Schritttext auf S. 498 kennt keinen Schritt zur Hüftlinie: Die Schritte 1 bis 15 bauen Saum-, Taillen-, Schritt-, Knie- und Wadenlinie. Die Zeichnung `□2` beschriftet die Hüftlinie dagegen ausdrücklich (`HüLi`, Transkriptzeile 12), und die Schritte 8 und 9 auf S. 498 setzen sie mit „Die HüLi links (hinten) …" bereits als vorhanden voraus. Der Konstruktionsschritt fehlt damit im gedruckten Text und ist nur über die Zeichnung belegt. Er wird hier nicht erfunden, sondern als Fehlstelle benannt.
- **Abgrenzung:** Die Beziehung ist wortgleich mit `HOF-B1-S110-F01` (Standardhose), `HOF-B1-S495-F01` (einfache Sporthose) und der Beschriftung auf S. 501 (Leggings, `HOF-B1-S501-F04`). Sie erhält hier eine eigene ID, weil die Jogginghose ein eigener Grundschnitt mit eigener Schrittfolge ist und keine der Seiten eine Identität mit einer anderen Konstruktion erklärt. Dieselbe Regel wurde bereits in `V3-S01` angewandt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Betrag und Richtung trennen. Die Hüftlinie ist in dieser Konstruktion nur zeichnerisch belegt; sie sollte als eigener, kennzeichenbarer Konstruktionsschritt geführt werden, damit die Lücke im Schritttext sichtbar bleibt.

## Zeichnungsbelege zu Schritten auf S. 498

Fünf der sieben Kandidatenzeilen wiederholen wortgleich Rechenbeziehungen, deren Schritttext auf S. 498 steht und dort ebenfalls als Kandidatenzeile extrahiert ist. Nach der in `V3-J05` festgelegten und in `V3-S01` bestätigten Regel erhalten Zeichnungsbeschriftungen keine zweite ID, wenn der zugehörige Schritttext auf einer Nachbarseite als Formel geführt wird.

| Beschriftung auf S. 499 | Extraktzeile | Schritttext auf S. 498 | Fundstelle im S.-498-Extrakt |
|---|---:|---|---|
| `HüU : 4 + 0 bis 2 cm` | 10 | Schritt 6: „Auf dieser nach rechts und links HüU : 4 + 0 bis 2 cm abtragen" | `formeln_s498.md`, Zeile 14 |
| `HüU : 10 + 0 bis 1 cm` | 11 | Schritt 8: „Die HüLi links (hinten) um HüU : 10 + 0 bis 1 cm und" | `formeln_s498.md`, Zeile 19 |
| `HüU : 20 + 1 bis 2 cm` | 12 | Schritt 9: „rechts (vorne) um HüU : 20 + 1 bis 2 cm verlängern." | `formeln_s498.md`, Zeile 20 |
| `WaU : 2 + 0 bis 1 cm` | 14 | Schritt 12: „Den WaU : 2 + 0 bis 1 cm nach links und rechts abtragen." | `formeln_s498.md`, Zeile 25 |
| `SaW : 2` | 15 | Schritt 3: „Die SaW : 2 nach rechts und links abtragen." | `formeln_s498.md`, Zeile 9 |

**Bearbeitungsstand dieser fünf Belege:** S. 498 ist in der Tranchenkarte der Tranche `V3-S02` zugeordnet und dort inzwischen normalisiert. Die fünf Zeilen sind Belege zu den folgenden IDs in `formeln_s498_normalisiert.md` und erhalten hier keine zweite ID:

| Beschriftung auf S. 499 | Ziel-ID auf S. 498 |
|---|---|
| `SaW : 2` | `HOF-B1-S498-F01` |
| `HüU : 4 + 0 bis 2 cm` | `HOF-B1-S498-F02` |
| `HüU : 10 + 0 bis 1 cm` | `HOF-B1-S498-F03` |
| `HüU : 20 + 1 bis 2 cm` | `HOF-B1-S498-F04` |
| `WaU : 2 + 0 bis 1 cm` | `HOF-B1-S498-F05` |

Sie sind nicht ausgeschlossen: die Rechenbeziehungen sind vollständig und rechenfähig, nur ihre Fundstelle als Schritttext liegt auf der Nachbarseite.

Die Zusammenführung ist durch die Seiten selbst gedeckt: Die Bildunterschrift `□2` auf S. 499 gehört zum Grundschnitt, dessen Schritte 1 bis 15 auf S. 498 stehen, und S. 499 setzt die Zählung mit Schritt 16 fort.

## Ausgeschlossene Kandidaten

Keine. Alle sieben extrahierten Kandidatenzeilen sind Rechenbeziehungen; zwei sind hier normalisiert, fünf sind Belege zu Schritten auf S. 498.

## Prüfhinweise

1. **Fehlender Hüftlinienschritt:** Der Schritttext auf S. 498 baut die Hüftlinie nicht, setzt sie in den Schritten 8 und 9 aber voraus. Belegt ist sie nur über die Zeichnungsbeschriftung `HüLi` und über `HüU : 20 + 3 cm` auf S. 499. Der Widerspruch liegt in der Quelle und wurde nicht durch einen erfundenen Schritt geschlossen.
2. **Zwei Hüftmaße nebeneinander:** Die Zeichnung trägt `HüU : 20 + 1 bis 2 cm` (Längsverlängerung der vorderen Hüftlinie, Schritt 9) und `HüU : 20 + 3 cm` (Höhenabstand der Hüftlinie) unmittelbar nebeneinander. Beide teilen den Nenner 20, sind aber verschiedene Größen mit verschiedener Richtung. Sie dürfen technisch nicht zusammengezogen werden.
3. **Keine Weitenreduzierung:** Anders als bei der Leggings auf S. 500 und S. 501 arbeitet die Jogginghose mit den unreduzierten Umfangsmaßen. Die auf S. 499 stehenden Bereichszugaben (`+ 0 bis 2 cm`, `+ 0 bis 1 cm`, `+ 1 bis 2 cm`) sind Weitenzugaben, keine Dehnungswerte.
4. **`WaH` nur zeichnerisch belegt:** Die Konstruktionstabelle auf S. 498 führt `SrH` und `KnH`, aber keine `WaH`-Zeile. `HOF-B1-S499-F01` ist damit die einzige Fundstelle der Wadenhöhen-Berechnung für diesen Grundschnitt.
5. **Extraktionsgrenze:** Das Originaltranskript `s499.md` enthält weitere bemaßte und rechenfähige Angaben, die im verbindlichen Extrakt nicht als Kandidatenzeilen vorliegen und deshalb nicht als Buchfassungen ergänzt wurden:
   - Zeile 21: `6 bis 8 cm` (Kürzung unten an der Seitenlinie, Schritt 2 auf S. 498) · `1 bis 1,5 cm` (Kürzung oben, Schritt 4) · `1 bis 2 cm` (Einstellung an der Knielinie, Schritt 14) · `2 bis 3 cm` · `3 cm` (Ausstellung an P3a, Schritt 3a; Einstellung der Gesäßnaht, Schritt 19) · `ca. 1 cm` (Einstellung der vM, Schritt 16);
   - Zeile 22: `Für Herren + ca. 0,7 cm`;
   - Zeile 23: die Bruchangaben `½` und `¼` am vorderen Hosenausschnitt mit den Symbolen `♀` und `♂`;
   - Zeile 50: `Bündchenbreite 4 bis 8 cm` und Zeile 51: `FeU − 0 bis −2 cm` (Weite des Strickbündchens, Schritt 24).

   Besonders `FeU − 0 bis −2 cm` ist eine vollständige Rechenbeziehung mit benannter Eingabe und Ausgabe und die einzige Weitenangabe zum Strickbündchen. Sie bleibt als Prüfstelle für eine spätere Nachextraktion vermerkt. Der Abschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
6. **Verweisfehler auf der Vorseite:** S. 498 verweist auf den „Sporthosen-Grundschnitt auf Seite 468"; die Sporthose steht tatsächlich auf S. 494 bis S. 496. Das Transkript hält den Fehler als gedruckten Wortlaut fest. Er berührt keine der hier normalisierten Beziehungen.
