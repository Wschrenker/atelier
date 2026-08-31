# Fachlich normalisierte Formeln — S. 184

Quelle der Normalisierung: `formeln_s184.md`
Originaltranskript: `s184.md`
Buchseite: Hofenbitzer, Band 1, S. 184

## HOF-B1-S184-F01 — Inhalt des vorderen Taillenabnähers

- **Fachlicher Zweck:** Den vorderen Abnäherinhalt aus der gemessenen Strecke und einer passformklassenabhängigen Zugabe bestimmen.
- **Quelle:** `formeln_s184.md`, Zeile 9; Originaltranskript `s184.md`, Zeilen 49–53; Buchseite 184.
- **Originalbezeichnung:** `vAbl = me + 0 bis 1 cm = 3,2 cm`
- **Normalisierte Bezeichnung:** `vorderer_taillenabnaeherinhalt`

### Buchfassung

```text
> **vAbl = me + 0 bis 1 cm = 3,2 cm**
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `gemessene_strecke_vorderer_abnaeher` | me | im Extrakt nicht beziffert | cm |
| `abnaeher_zugabe` | `0 bis 1 cm` | im Beispiel nicht separat beziffert | cm |

### Formel und Rechenschritte

```text
vorderer_taillenabnaeherinhalt = gemessene_strecke_vorderer_abnaeher + abnaeher_zugabe
Buchergebnis = 3,2 cm

Kontextkontrolle im Originaltranskript, nicht Teil der Buchfassung:
2,2 cm + 1 cm = 3,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Buchwert | Einheit |
|---|---|---:|---|
| `vorderer_taillenabnaeherinhalt` | vAbl | 3,2 | cm |

- **Abhängigkeiten:** Gemessene Strecke `me`, gewählte Zugabe und Passformklasse.
- **Gültigkeitsbereich:** Vorderer Taillenabnäher des taillierten Oberteil-Grundschnitts.
- **Technische Randbedingung:** Die Zugabe muss innerhalb 0 bis 1 cm liegen; die Auswahlregel steht nur im Originalkontext.
- **Offene Fragen oder Widersprüche:** Die allgemeine Beziehung und das Ergebnis sind eindeutig. Die Einzelwerte `me = 2,2 cm` und `+1 cm` fehlen im Extrakt, stimmen im Originalkontext aber mit 3,2 cm überein.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Messwert und ausgewählte Zugabe als getrennte Eingaben verlangen.

## HOF-B1-S184-F02 — Taillenausfall mit bereits berücksichtigtem vorderen Abnäher

- **Fachlicher Zweck:** Den noch zu verteilenden Taillenausfall aus gemessener Taillenbreite und halber Taillenweite bestimmen.
- **Quelle:** `formeln_s184.md`, Zeile 14; Originaltranskript `s184.md`, Zeilen 58–62; Buchseite 184.
- **Originalbezeichnung:** `TaAf = TaB − ½ TaW`
- **Normalisierte Bezeichnung:** `taillenausfall_mit_hueftausfallgrundschnitt`

### Buchfassung

```text
> **Taillenausfall (TaAf) = TaB − ½ TaW = 42,8 cm − 36 cm = 6,8 cm**
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `taillenbreite_gemessen` | TaB | 42,8 | cm |
| `halbe_taillenweite` | ½ TaW | 36 | cm |

### Formel und Rechenschritte

```text
taillenausfall = taillenbreite_gemessen - halbe_taillenweite
                = 42,8 cm - 36 cm
                = 6,8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `taillenausfall` | noch an Seitennähten und Rückteilabnähern zu verteilender TaAf | 6,8 | cm |

- **Abhängigkeiten:** Gemessene vTaB/hTaB und ½ TaW; vAbl aus `HOF-B1-S184-F01` ist laut Original bereits berücksichtigt.
- **Gültigkeitsbereich:** Taillierter Oberteil-Grundschnitt mit Hüftausfall, Beispielgröße 38.
- **Technische Randbedingung:** TaB wird ohne den bereits berücksichtigten vorderen Abnäherinhalt gemessen.
- **Offene Fragen oder Widersprüche:** Keine; die Rechnung stimmt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Bereits berücksichtigte und noch zu verteilende Abnäherbeträge nicht doppelt zählen.
