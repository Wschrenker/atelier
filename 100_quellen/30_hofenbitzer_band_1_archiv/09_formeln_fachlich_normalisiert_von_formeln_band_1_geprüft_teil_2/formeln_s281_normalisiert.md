# Fachlich normalisierte Formeln — S. 281

Quelle der Normalisierung: `formeln_s281_digital_geprüft.md`
Originaltranskript: `s281_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 281
Extraktionsstand: v2

## HOF-B1-S281-F01 — Öffnungsbereich unter dem Arm

- **Fachlicher Zweck:** Den Öffnungsbetrag unter dem Arm für Vorder- und Hinterärmel aus der Armlochvertiefung begrenzen.
- **Quelle:** `formeln_s281_digital_geprüft.md`, Zeile 9; Originaltranskript `s281_digital_geprüft.md`, Zeile 11; Buchseite 281.
- **Originalbezeichnung:** Betrag unter dem Arm, Armlochvertiefung
- **Normalisierte Bezeichnung:** `oeffnungsbetrag_unter_dem_arm`

### Buchfassung

```text
10. □4+5 An beiden Ärmeln denselben Betrag unter dem Arm um ⅔ bis zum ganzen Betrag der Armlochvertiefung öffnen. Je größer der Öffnungsbetrag, desto größer die Hebelänge des Ärmels.
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `armlochvertiefung` | Armlochvertiefung | cm |
| `oeffnungsfaktor` | gewählter Anteil von ⅔ bis zum ganzen Betrag | dimensionslos |

### Formel und Rechenschritte

```text
oeffnungsfaktor_min = 2 / 3
oeffnungsfaktor_max = 1
oeffnungsbetrag_unter_dem_arm = armlochvertiefung * oeffnungsfaktor

(2 / 3) * armlochvertiefung <= oeffnungsbetrag_unter_dem_arm <= armlochvertiefung
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `oeffnungsbetrag_unter_dem_arm` | identischer Öffnungsbetrag an Vorder- und Hinterärmel | cm |

- **Abhängigkeiten:** Die gewählte Armlochvertiefung der Dolman-Anlage und eine fachliche Wahl des Öffnungsfaktors im gedruckten Bereich.
- **Gültigkeitsbereich:** Öffnung für die Hebelänge an beiden Ärmeln der Dolman-Anlage auf S. 281.
- **Technische Randbedingung:** Vorder- und Hinterärmel erhalten denselben Betrag. `armlochvertiefung >= 0` und `2/3 <= oeffnungsfaktor <= 1` müssen gelten.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Unstimmigkeit. Die Quelle beschreibt die Wirkung eines größeren Öffnungsbetrags, gibt aber keine Auswahlregel für den konkreten Faktor im Bereich vor.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Den Öffnungsfaktor als explizite fachliche Eingabe verlangen, gegen den Bereich prüfen und denselben berechneten Betrag an beiden Ärmeln verwenden.

## Ausgeschlossene Kandidaten

Keine. Die eine extrahierte Kandidatenzeile ist vollständig abgebildet.

## Extraktionsgrenze

Die Fertigmaßtabelle und weitere qualitative Aussagen zur Hebelänge im Originaltranskript sind keine zusätzlichen extrahierten Rechenbeziehungen. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
