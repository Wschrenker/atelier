# Fachlich normalisierte Formeln — S. 330

Extraktionsstand: v3  
Quelle der Normalisierung: `formeln_s330.md`  
Originaltranskript: `s330.md`  
Buchseite: Hofenbitzer, Band 1, S. 330

## HOF-B1-S330-F01 — Hintere Stegbreite aus seitlicher Stegbreite

- **Fachlicher Zweck:** Hintere Stegbreite für den Reverskragen mit angeschnittenem Beleg bestimmen.
- **Quelle:** `formeln_s330.md`, Extraktzeilen 14 und 31; Originaltranskript `s330.md`, Zeilen 34 und 52; Buchseite 330.
- **Originalbezeichnung:** `hStegB = sStegB + 0,5 cm`
- **Normalisierte Bezeichnung:** `hintere_stegbreite_angeschnittener_beleg`

### Buchfassung
```text
15. die hStegB = sStegB + 0,5 cm abtragen sowie den Kragenbruch in den ReB einlaufend formen.
```

```text
- hStegB = sStegB + 0,5 cm
```

### Eingaben
`seitliche_stegbreite` (sStegB), variabel, cm; Zuschlag `0,5 cm`, cm.

### Formel und Rechenschritte
```text
hintere_stegbreite = seitliche_stegbreite + 0,5 cm
```

### Ausgabe
`hintere_stegbreite` — hStegB, cm.

- **Abhängigkeiten:** sStegB.
- **Gültigkeitsbereich:** Reverskragen mit am Vorderteil angeschnittenem Beleg, S. 330.
- **Offene Fragen oder Widersprüche:** Keine für die additive Beziehung; die Buchzeilen sind zwei Nachweise.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Festen Zuschlag von `0,5 cm` verwenden.

## HOF-B1-S330-F02 — Unbezeichnete X-Korrekturfortsetzung

- **Fachlicher Zweck:** Die numerische Fortsetzung einer hKrB-Korrektur dokumentieren, ohne die fehlende Zielbezeichnung zu ergänzen.
- **Quelle:** `formeln_s330.md`, Extraktzeilen 24–26; Originaltranskript `s330.md`, Zeilen 48–50; Buchseite 330.
- **Originalbezeichnung:** Im Extrakt fehlt die vorangehende Bezeichnungszeile `hKrB (3 bis 5 cm) + ⅒ X`.
- **Normalisierte Bezeichnung:** `unbezeichnete_x_korrekturfortsetzung_angeschnittener_beleg`

### Buchfassung
```text
- = 3 cm + 4,8 cm : 10
- = 3 cm + 0,5 cm
- = 3,5 cm
```

### Eingaben
`hintere_kragenbreite` aus dem Seitenkontext: `3 cm`; `X`: `4,8 cm`; Zielbezeichnung: im Extrakt nicht enthalten.

### Formel und Rechenschritte
```text
unbekannte_zielgroesse = 3 cm + (4,8 cm / 10)
unbekannte_zielgroesse = 3 cm + 0,48 cm = 3,48 cm (ungerundet)
```

Der Buchweg verwendet `0,5 cm` und druckt `3,5 cm`. Die technische Zielgröße wird nicht erfunden.

### Ausgabe
`unbekannte_zielgroesse` — im Extrakt nicht sicher bezeichnet; gedruckt `3,5 cm`, ungerundet `3,48 cm`.

- **Abhängigkeiten:** hKrB und X sind nur aus dem Kontext erschließbar.
- **Gültigkeitsbereich:** Konstruktion mit angeschnittenem Beleg, S. 330.
- **Offene Fragen oder Widersprüche:** Fehlende linke Bezeichnung und nicht erklärte Rundung.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Nicht implementieren, bevor die fehlende Bezeichnungszeile extrahiert und fachlich zugeordnet ist.

## HOF-B1-S330-F03 — Seitliche Kragenbreite mit Zuschlagsbereich

- **Fachlicher Zweck:** Seitliche Kragenbreite aus der hinteren Kragenbreite und einem kleinen Zuschlagsbereich angeben.
- **Quelle:** `formeln_s330.md`, Extraktzeile 32; Originaltranskript `s330.md`, Zeile 53; Buchseite 330.
- **Originalbezeichnung:** `sKrB = hKrB + 0 bis 0,5 cm`
- **Normalisierte Bezeichnung:** `seitliche_kragenbreite_aus_hinterer_kragenbreite`

### Buchfassung
```text
- sKrB = hKrB + 0 bis 0,5 cm
```

### Eingaben
`hintere_kragenbreite` (hKrB), variabel, cm; Zuschlag `0 bis 0,5 cm`, cm.

### Formel und Rechenschritte
```text
seitliche_kragenbreite_min = hintere_kragenbreite + 0 cm
seitliche_kragenbreite_max = hintere_kragenbreite + 0,5 cm
```

### Ausgabe
`seitliche_kragenbreite` — sKrB, cm.

- **Abhängigkeiten:** hKrB.
- **Gültigkeitsbereich:** Kontrolle im Schulterbereich, S. 330.
- **Offene Fragen oder Widersprüche:** Auswahl innerhalb des Zuschlagsbereichs nicht belegt.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Beide Bereichsgrenzen führen; keinen Zuschlag automatisch auswählen.

## Ausgeschlossene Kandidaten

| Extraktzeile(n) | Anzahl | Ausschlussgrund |
|---|---:|---|
| 9 | 1 | Maßstabsfaktor ohne fachliche Zielberechnung |
| 19 | 1 | X-Messung als Eingabewert |
| **Summe** | **2** | **Maßstabs- und Eingabeangabe ausgeschlossen** |
