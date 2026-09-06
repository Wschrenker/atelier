# Fachlich normalisierte Formeln — S. 320

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s320.md`  
Originaltranskript: `s320.md`  
Buchseite: Hofenbitzer, Band 1, S. 320

## HOF-B1-S320-F01 — Begrenzte hintere Kragenbreite beim angeschnittenen Unterkragen

- **Fachlicher Zweck:** Die zulässige hintere Kragenbreite für den vollständig am Oberteil angeschnittenen Schalkragen festlegen.
- **Quelle:** `formeln_s320.md`, Zeile 19 (Buchfassung Zeile 38); Originaltranskript `s320.md`, Zeile 38; Buchseite 320.
- **Originalbezeichnung:** `hKrB = mind. hStegB + 1 cm bis max. 4 cm`
- **Normalisierte Bezeichnung:** `hintere_kragenbreite_angeschnittener_unterkragen`

### Buchfassung

```text
- hKrB = mind. hStegB + 1 cm bis max. 4 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `hintere_stegbreite` | hStegB | variabel | cm |
| `hinterer_kragen_zuschlag` | mind. `+ 1 cm` | 1 oder größer | cm |
| `maximale_hintere_kragenbreite` | max. 4 cm | 4 | cm |

### Formel und Rechenschritte

```text
hintere_kragenbreite_min = hintere_stegbreite + 1 cm
hintere_kragenbreite_max = 4 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `hintere_kragenbreite` | sichtbare hintere Kragenbreite hKrB | cm |

- **Abhängigkeiten:** Hintere Stegbreite hStegB.
- **Gültigkeitsbereich:** Schalkragen mit am Vorderteil angeschnittenem Unterkragen auf S. 320.
- **Technische Randbedingung:** Die hintere und seitliche Kragenbreite darf bei dieser Konstruktion nicht breiter als `4 cm` sein; der konkrete Wert muss zugleich mindestens `hStegB + 1 cm` betragen.
- **Offene Fragen oder Widersprüche:** Die Quelle nennt keine Auswahlregel innerhalb des zulässigen Bereichs. Der Seitenkontext nennt außerdem weitere Einschränkungen; diese werden nicht in diese Breitenformel eingerechnet.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Konstruktionstyp als Gültigkeitskontext prüfen und die obere Grenze `4 cm` nicht mit der separaten Schalkragenkonstruktion bis `7 cm` von S. 316 vermischen.

## HOF-B1-S320-F02 — Unbezeichnete Fortsetzung der X-Korrekturrechnung

- **Fachlicher Zweck:** Die im Extrakt erhaltene numerische Fortsetzung einer Korrektur an hKrB dokumentieren.
- **Quelle:** `formeln_s320.md`, Zeilen 24–26; Originaltranskript `s320.md`, Zeilen 39–42; Buchseite 320.
- **Originalbezeichnung:** Im Extrakt fehlt die zugehörige Bezeichnungszeile `hKrB + ⅒ X`; erhalten sind nur die Fortsetzungszeilen.
- **Normalisierte Bezeichnung:** `unbezeichnete_x_korrekturfortsetzung`

### Buchfassung

```text
- = 4 cm − 6,1 cm : 10
- = 4 cm − 0,6 cm
- = 3,4 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Buchwert | Einheit |
|---|---|---:|---|
| `unbekannte_ausgangsbezeichnung` | im Extrakt nicht enthalten | unbekannt | unbekannt |
| `x_wert` | X | −6,1 | cm |
| `hintere_kragenbreite` | hKrB, aus dem Seitenkontext | 4 | cm |

### Formel und Rechenschritte

```text
unbekannte_ausgangsbezeichnung = 4 cm − (6,1 cm / 10)
unbekannte_ausgangsbezeichnung = 4 cm − 0,6 cm = 3,4 cm (gedruckter Rechenweg)
```

Die fachliche Zielgröße ist wegen der fehlenden linken Seite im Extrakt nicht sicher zuzuweisen. Wörtlich ergibt `4 cm − 6,1 cm / 10 = 3,39 cm`; die Buchrechnung verwendet den gerundeten Zwischenwert `0,6 cm`.

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `unbekannte_ausgangsbezeichnung` | nicht sicher identifizierte Zielgröße | 3,4 gedruckt; 3,39 aus ungerundetem Weg | cm |

- **Abhängigkeiten:** Nur aus dem Transkript-Kontext erschließbare Größen hKrB und X; die Zielbezeichnung fehlt im verbindlichen Extrakt.
- **Gültigkeitsbereich:** Schalkragen-Konstruktion auf S. 320.
- **Technische Randbedingung:** Die Ergänzung der fehlenden linken Seite bleibt eine technische Zuordnungshypothese und darf nicht als Buchfassung ausgegeben werden.
- **Offene Fragen oder Widersprüche:** Extraktionslücke bei der Zielbezeichnung; zusätzlich gerundeter Zwischenwert `0,6 cm` statt `0,61 cm` beziehungsweise `0,6` aus der Buchdarstellung.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bevor die fehlende Bezeichnungszeile aus der Extraktionsschicht nachgeführt und fachlich zugeordnet ist.

## Ausgeschlossene Kandidaten

| Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Maßstabsfaktorangabe ohne fachliche Zielberechnung |
| 14 | 1 | Lage-/Vorzeichenhinweis zu X; Eingabekontext ohne eigene Zielberechnung |
| 28–31 | 4 | Halslochverbreiterung, X-Messung, Kragenbreiten-/Stegbreitenbereiche und direkte Konstruktionsangaben |
| 35 | 1 | Begriffsdefinition `Fasson`; keine Rechenoperation |
| **Summe** | **7** | **Maßstabs-, Kontext-, Eingabe- und Definitionsangaben ausgeschlossen** |
