# Fachlich normalisierte Formeln — S. 34

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/02_grundschnitte_roecke_s32-39/formeln_s34.md`
Originaltranskript: `../Band_1_geprüft_v1/s34.md`
Buchseite: Hofenbitzer, Band 1, S. 34

## HOF-B1-S034-F01 — Kontrollsumme bei einem hinteren Abnäher

- **Fachlicher Zweck:** Prüfen, dass Hüftabstich, vorderer Abnäher und ein hinterer Abnäher zusammen den Taillenausfall ergeben.
- **Quelle:** `formeln_s34.md`, Zeilen 17–20; Originaltranskript `s34.md`, Zeilen 21–31; Buchseite 34.
- **Originalbezeichnung:** `Kontrolle: Σ = TaAf`
- **Normalisierte Bezeichnung:** `kontrollsumme_taillenausfall_ein_hinterer_abnaeher`

### Buchfassung

```text
| Kontrolle: | Σ = TaAf | 13 |
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `hueftabstich` | Hüftabstich | 6,5 | cm |
| `vorderer_abnaeherinhalt` | v. Abnäher | 2,5 | cm |
| `hinterer_abnaeherinhalt` | 1. h. Abnäher | 4 | cm |
| `taillenausfall` | TaAf | 13 | cm |

### Formel und Rechenschritte

```text
kontrollsumme_taillenausfall_ein_hinterer_abnaeher = hueftabstich
                                                     + vorderer_abnaeherinhalt
                                                     + hinterer_abnaeherinhalt
                                                     = 6,5 cm + 2,5 cm + 4 cm
                                                     = 13 cm

kontrollsumme_taillenausfall_ein_hinterer_abnaeher = taillenausfall
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `kontrollsumme_taillenausfall_ein_hinterer_abnaeher` | Summe der drei Verteilungsbeträge | 13 | cm |
| `verteilung_ist_vollstaendig` | Kontrollaussage `Σ = TaAf` | wahr | boolesch |

- **Abhängigkeiten:** `HOF-B1-S033-F01` und die auf S. 34 gewählten Verteilungsbeträge.
- **Gültigkeitsbereich:** Beispielvariante auf S. 34 mit genau einem hinteren Abnäher.
- **Technische Randbedingung:** Alle Summanden müssen dieselbe Längeneinheit tragen.
- **Offene Fragen oder Widersprüche:** Keine; `6,5 + 2,5 + 4 = 13`.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Dieselbe allgemeine Kontrollfunktion wie für S. 33 verwenden; die Anzahl der hinteren Abnäher als variable Liste modellieren.

## HOF-B1-S034-F02 — Taillenerhöhung am hinteren Abnäher

- **Fachlicher Zweck:** Erhöhung der Taillenlinie am hinteren Abnäher als ungefähr ein Drittel der Erhöhung an der Seitenlinie bestimmen.
- **Quelle:** `formeln_s34.md`, Zeilen 27–30; Originaltranskript `s34.md`, Zeilen 37–46; Buchseite 34.
- **Originalbezeichnung:** `0,3 bis 0,5 cm ≙ ⅓ der Erhöhung an der Seitenlinie`
- **Normalisierte Bezeichnung:** `taillenerhoehung_hinterer_abnaeher`

### Buchfassung

```text
> (12) und für den hinteren Abnäher 0,3 bis 0,5 cm ≙ ⅓ der Erhöhung an der Seitenlinie.
```

### Eingaben

| Technische Variable | Buchbegriff | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenerhoehung_seitenlinie` | Erhöhung an der Seitenlinie | 1 bis 1,5 | cm |
| `anteil_hinterer_abnaeher` | ⅓ | 1/3 | dimensionslos |

### Formel und Rechenschritte

```text
taillenerhoehung_hinterer_abnaeher ≈ taillenerhoehung_seitenlinie * anteil_hinterer_abnaeher

bei 1 cm:   1 cm * 1/3 ≈ 0,33 cm
bei 1,5 cm: 1,5 cm * 1/3 = 0,5 cm
Buchbereich: 0,3 bis 0,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert in der Buchfassung | Einheit |
|---|---|---:|---|
| `taillenerhoehung_hinterer_abnaeher` | Erhöhung der Taillenlinie am hinteren Abnäher | 0,3 bis 0,5 | cm |

- **Abhängigkeiten:** Gewählte `taillenerhoehung_seitenlinie`.
- **Gültigkeitsbereich:** Seitenlinien-Erhöhung von `1 bis 1,5 cm` innerhalb dieser Konstruktion.
- **Technische Randbedingung:** Das Buchzeichen `≙` wird als fachliche Entsprechung und nicht als mathematisch exakte Gleichheit behandelt.
- **Offene Fragen oder Widersprüche:** Ein Drittel von `1 cm` ist rechnerisch etwa `0,33 cm`; der Buchbereich beginnt gerundet bei `0,3 cm`. Eine verbindliche Rundungsregel nennt die Quelle nicht.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Zunächst den exakten Drittelwert berechnen. Eine Rundung auf Millimeter erst nach einer gesondert belegten oder technisch festgelegten Rundungsregel anwenden.

## HOF-B1-S034-F03 — Hüftabstich bei flacher Hüftrundung

- **Fachlicher Zweck:** Seitlichen Hüftabstich für eine flache Hüftrundung aus dem halben Taillenausfall und einem Abzugsbetrag bestimmen.
- **Quelle:** `formeln_s34.md`, Zeilen 37–40; Originaltranskript `s34.md`, Zeilen 50–63; Buchseite 34.
- **Originalbezeichnung:** `Bei einer flachen Hüftrundung: TaAf : 2 − 1 bis 1,5 cm`
- **Normalisierte Bezeichnung:** `hueftabstich_flache_hueftrundung`

### Buchfassung

```text
> Bei einer flachen Hüftrundung: TaAf : 2 − 1 bis 1,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Beispiel | Einheit |
|---|---|---:|---|
| `taillenausfall` | TaAf | 13 | cm |
| `hueftform_korrektur` | Abzug bei flacher Hüftrundung | 1 bis 1,5 | cm |

### Formel und Rechenschritte

```text
hueftabstich_flache_hueftrundung = (taillenausfall / 2) - hueftform_korrektur

bei TaAf = 13 cm:
(13 cm / 2) - 1 cm   = 5,5 cm
(13 cm / 2) - 1,5 cm = 5 cm
Ergebnisbereich: 5 bis 5,5 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Aus dem Buchbeispiel abgeleiteter Bereich | Einheit |
|---|---|---:|---|
| `hueftabstich_flache_hueftrundung` | Seitlicher Hüftabstich bei flacher Hüftrundung | 5 bis 5,5 | cm |

- **Abhängigkeiten:** `taillenausfall` aus `HOF-B1-S033-F01` und fachlich gewählte `hueftform_korrektur`.
- **Gültigkeitsbereich:** Nur für die im Buch als flach bezeichnete Hüftrundung.
- **Technische Randbedingung:** Der Korrekturbetrag muss innerhalb `1 bis 1,5 cm` gewählt werden; wie innerhalb dieses Bereichs gewählt wird, belegt die Quelle nicht.
- **Offene Fragen oder Widersprüche:** Der Ergebnisbereich `5 bis 5,5 cm` ist technisch aus `TaAf = 13 cm` berechnet, aber nicht als Ergebnis im Buch gedruckt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Hüftform nicht automatisch aus Maßen klassifizieren; die Auswahl „flach“ bleibt eine separate fachliche Eingabe.

## HOF-B1-S034-F04 — Hüftabstich bei starker Hüftrundung

- **Fachlicher Zweck:** Seitlichen Hüftabstich für eine starke Hüftrundung aus dem halben Taillenausfall und einem Zuschlagsbetrag bestimmen.
- **Quelle:** `formeln_s34.md`, Zeilen 37–41; Originaltranskript `s34.md`, Zeilen 50–63; Buchseite 34.
- **Originalbezeichnung:** `bei einer starken Hüftrundung: TaAf : 2 + 1 bis 1,5 cm`
- **Normalisierte Bezeichnung:** `hueftabstich_starke_hueftrundung`

### Buchfassung

```text
> und bei einer starken Hüftrundung: TaAf : 2 + 1 bis 1,5 cm
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Beispiel | Einheit |
|---|---|---:|---|
| `taillenausfall` | TaAf | 13 | cm |
| `hueftform_korrektur` | Zuschlag bei starker Hüftrundung | 1 bis 1,5 | cm |

### Formel und Rechenschritte

```text
hueftabstich_starke_hueftrundung = (taillenausfall / 2) + hueftform_korrektur

bei TaAf = 13 cm:
(13 cm / 2) + 1 cm   = 7,5 cm
(13 cm / 2) + 1,5 cm = 8 cm
Ergebnisbereich: 7,5 bis 8 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Aus dem Buchbeispiel abgeleiteter Bereich | Einheit |
|---|---|---:|---|
| `hueftabstich_starke_hueftrundung` | Seitlicher Hüftabstich bei starker Hüftrundung | 7,5 bis 8 | cm |

- **Abhängigkeiten:** `taillenausfall` aus `HOF-B1-S033-F01` und fachlich gewählte `hueftform_korrektur`.
- **Gültigkeitsbereich:** Nur für die im Buch als stark bezeichnete Hüftrundung.
- **Technische Randbedingung:** Der Korrekturbetrag muss innerhalb `1 bis 1,5 cm` gewählt werden; wie innerhalb dieses Bereichs gewählt wird, belegt die Quelle nicht.
- **Offene Fragen oder Widersprüche:** Der Ergebnisbereich `7,5 bis 8 cm` ist technisch aus `TaAf = 13 cm` berechnet, aber nicht als Ergebnis im Buch gedruckt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Hüftform und Korrekturbetrag als sichtbare Eingaben führen; keine unbelegte automatische Auswahl ergänzen.

## HOF-B1-S034-F05 — Position der vorderen Abnähermitte

- **Fachlicher Zweck:** Abstand der vorderen Abnähermitte vom vorderen Hüftbogen aus dem Taillenumfang bestimmen.
- **Quelle:** `formeln_s34.md`, Zeilen 53–56; Originaltranskript `s34.md`, Zeilen 65–75; Buchseite 34.
- **Originalbezeichnung:** `Die Abnähermitte TaU:10 vom vorderen Hüftbogen`
- **Normalisierte Bezeichnung:** `abstand_vordere_abnaehermitte`

### Buchfassung

```text
> (17) **Vorderer Abnäher:** Die Abnähermitte TaU:10 vom vorderen Hüftbogen auf die erhöhte
```

### Eingaben

| Technische Variable | Buchbegriff | Wert im Maßbeispiel | Einheit |
|---|---|---:|---|
| `taillenumfang` | TaU | 72 | cm |
| `positions_divisor` | Divisor 10 | 10 | dimensionslos |

### Formel und Rechenschritte

```text
abstand_vordere_abnaehermitte = taillenumfang / positions_divisor

für TaU = 72 cm aus dem Maßsatz auf S. 33:
abstand_vordere_abnaehermitte = 72 cm / 10
                                = 7,2 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Aus dem Maßbeispiel abgeleiteter Wert | Einheit |
|---|---|---:|---|
| `abstand_vordere_abnaehermitte` | Abstand vom vorderen Hüftbogen bis zur vorderen Abnähermitte | 7,2 | cm |

- **Abhängigkeiten:** `taillenumfang` aus dem verwendeten Maßsatz.
- **Gültigkeitsbereich:** Positionierung des vorderen Rockabnähers in dieser Konstruktion; gemessen vom vorderen Hüftbogen auf der erhöhten Abnäherlinie.
- **Technische Randbedingung:** `positions_divisor` darf nicht `0` sein. Startpunkt und Richtung gehören zur geometrischen Konstruktion und dürfen in der Umsetzung nicht verloren gehen.
- **Offene Fragen oder Widersprüche:** `7,2 cm` ist aus dem Maßsatz der S. 33 berechnet und auf S. 34 nicht als Ergebnis gedruckt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Nicht nur einen Zahlenwert liefern; das Ergebnis ist eine gerichtete Strecke ab dem vorderen Hüftbogen entlang der erhöhten Abnäherlinie.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s34.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 7–10, 12–15, 22–25, 32–35, 43–46, 48–51 und 58–61 | 7 | Bildverweise mit `+`, unvollständige Konstruktionssätze und Schrittverweise; keine vollständigen Rechenformeln |
| Zeilen 63–66 | 1 | Wiederholung von `TaU : 10` als Zeichnungslabel; bereits in `HOF-B1-S034-F05` erfasst |
| Zeilen 68–71 | 1 | administrative Verifikationsnotiz mit Wiederholung der Kontrollsumme; keine zusätzliche Buchformel |
| **Summe** | **9** | **9 ausgeschlossene Kandidatenzeilen** |
