# Fachlich normalisierte Formeln — S. 39

Quelle der Normalisierung: `../formeln_band_1_geprüft_v1/formeln_s39.md`
Originaltranskript: `../Band_1_geprüft_v1/s39.md`
Buchseite: Hofenbitzer, Band 1, S. 39

## HOF-B1-S039-F01 — Grundmaße des geraden Bundes

- **Fachlicher Zweck:** Länge und Breite des rechteckigen geraden Bundes festlegen.
- **Quelle:** `formeln_s39.md`, Zeilen 7–10; Originaltranskript `s39.md`, Zeilen 12–20; Buchseite 39.
- **Originalbezeichnung:** `Länge ≈ TaU, Höhe (Bundbreite) = 2 bis 5 cm`
- **Normalisierte Bezeichnung:** `grundmasse_gerader_bund`

### Buchfassung

```text
- Ein **Rechteck** zeichnen: Länge ≈ TaU, Höhe (**Bundbreite**) = **2 bis 5 cm**.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert oder Bereich | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | nicht festgelegt | cm |
| `bundbreite` | Bundbreite | 2 bis 5 | cm |

### Formel und Rechenschritte

```text
bundlaenge ≈ taillenumfang
bundhoehe = bundbreite
2 cm <= bundbreite <= 5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `bundlaenge` | Länge des rechteckigen Bundstreifens | cm |
| `bundhoehe` | Höhe des rechteckigen Bundstreifens | cm |

- **Abhängigkeiten:** `taillenumfang` und fachlich gewählte `bundbreite`.
- **Gültigkeitsbereich:** Gerader, an der waagerechten Taille sitzender Bund auf S. 39.
- **Technische Randbedingung:** Das Buchzeichen `≈` bezeichnet eine ungefähre Entsprechung. Eine konkrete Toleranz oder zusätzliche Verschlusslänge ist in dieser Formel nicht festgelegt.
- **Offene Fragen oder Widersprüche:** Die Quelle erklärt nicht rechnerisch, warum die Bundlänge nur ungefähr dem Taillenumfang entspricht und welcher Abweichungsbereich zulässig ist.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** `≈` nicht als exakte Gleichheit oder selbst gewählte Toleranz implementieren; eine spätere technische Festlegung muss sichtbar getrennt werden.

## HOF-B1-S039-F02 — Taillenmehrweite am geraden Bund

- **Fachlicher Zweck:** Einhalteweite als Überschuss der vorderen und hinteren Taillennaht gegenüber dem halben Taillenumfang bestimmen.
- **Quelle:** `formeln_s39.md`, Zeilen 17–22; Originaltranskript `s39.md`, Zeilen 36–51; Buchseite 39.
- **Originalbezeichnung:** `Taillenmehrweite (Einhalteweite)`
- **Normalisierte Bezeichnung:** `taillenmehrweite_einhalteweite`

### Buchfassung

```text
Taillenmehrweite (Einhalteweite) = vTaN + hTaN − TaU:2
                                 = 19,7 + 17,5 − 36,0 cm
                                 = 1,2 cm Einhalteweite
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `vordere_taillennaht` | vTaN | 19,7 | cm |
| `hintere_taillennaht` | hTaN | 17,5 | cm |
| `taillenumfang` | TaU | 72,0 | cm |
| `halbierungsfaktor` | 2 | 2 | dimensionslos |

### Formel und Rechenschritte

```text
taillenmehrweite_einhalteweite = vordere_taillennaht
                                  + hintere_taillennaht
                                  - (taillenumfang / halbierungsfaktor)
                                = 19,7 cm + 17,5 cm - (72,0 cm / 2)
                                = 37,2 cm - 36,0 cm
                                = 1,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenmehrweite_einhalteweite` | An den Taillennähten einzuhaltende Mehrweite | 1,2 | cm |

- **Abhängigkeiten:** Gemessene `vordere_taillennaht`, gemessene `hintere_taillennaht` und `taillenumfang`.
- **Gültigkeitsbereich:** Gerader Bund und die auf S. 39 beschriebene Messung der Taillennähte ohne Abnäherinhalte.
- **Technische Randbedingung:** Der Halbierungsfaktor darf nicht `0` sein. Die Quelle nennt `ca. 1 bis 1,5 cm` als üblichen Überschneidungsbetrag und Werte über `1,5 cm` als mögliches Fehleranzeichen.
- **Offene Fragen oder Widersprüche:** Im Originaltranskript ist eine Buch-Typografie markiert: Die linke Bildunterschrift nennt für die vordere Taillennaht fälschlich `hTaN`; Formel und Fließtext verwenden eindeutig `vTaN`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bei einem Ergebnis über `1,5 cm` einen Prüfhinweis erzeugen, aber nicht automatisch korrigieren; die Fehlerursache muss fachlich ermittelt werden.

## Ausgeschlossener Kandidat

| Quelle in `formeln_s39.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeile 14 | 1 | Hinweis `einhalten` mit VT-/RT-Anzahlen; Konstruktions- und Wiederholungsmarkierung, keine Rechenformel |
