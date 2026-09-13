# Fachlich normalisierte Formeln — S. 216

Quelle der Normalisierung: `formeln_s216_digital_geprüft.md`
Originaltranskript: `s216_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 216
Extraktionsstand: v2

## HOF-B1-S216-F01 — Öffnungen des Ärmels für eine Schulterpolster-Erhöhung

- **Fachlicher Zweck:** Die waagerechte und senkrechte Öffnung des Ärmels aus der Schulterpolster-Erhöhung ableiten.
- **Quelle:** `formeln_s216_digital_geprüft.md`, Zeilen 9 und 14; Originaltranskript `s216_digital_geprüft.md`, Zeilen 19–20 und 51; Buchseite 216.
- **Originalbezeichnung:** Schulterpolster-Erhöhung, Polsterdicke
- **Normalisierte Bezeichnung:** `aermeloeffnungen_fuer_schulterpolster_erhoehung`

### Buchfassung

Waagerechte Öffnung:

```text
6. An der waagerechten Öffnungen um ca. ⅓ Schulterpolster-Erhöhung = ungefähre Polsterdicke öffnen.
```

Senkrechte Öffnung:

```text
- öffnen um ca. ⅙ Schulterpolster-Erhöhung (= ½ Polsterdicke)
```

### Eingaben

| Technische Variable | Buchbegriff | Einheit |
|---|---|---|
| `schulterpolster_erhoehung` | Schulterpolster-Erhöhung | cm |

### Formel und Rechenschritte

```text
polsterdicke_annaehernd = schulterpolster_erhoehung * (1 / 3)
waagerechte_oeffnung = polsterdicke_annaehernd
senkrechte_oeffnung = schulterpolster_erhoehung * (1 / 6)
senkrechte_oeffnung = polsterdicke_annaehernd * (1 / 2)
```

### Ausgabe

| Technische Variable | Bedeutung | Einheit |
|---|---|---|
| `waagerechte_oeffnung` | Öffnung quer zur Ärmelkugel | cm |
| `senkrechte_oeffnung` | proportionale Öffnung in Längsrichtung | cm |

- **Abhängigkeiten:** Die Schulterpolster-Erhöhung wird laut Transkript als Differenz der Messstrecke über das Polster und derselben Strecke ohne Polster bestimmt; diese Differenz ist nicht Teil des extrahierten Formelbestands.
- **Gültigkeitsbereich:** Anpassung eines schmalen Ärmels an eine Schulterpolster-Erhöhung bei identischer Einhalteweite.
- **Technische Randbedingung:** Beide Beziehungen sind mit `ca.` beziehungsweise `ungefähr` angegeben und dürfen nicht als exakte Materialdickenmessung ausgegeben werden.
- **Offene Fragen oder Widersprüche:** Keine rechnerische Unstimmigkeit. Die Gleichsetzung der Polsterdicke mit ungefähr ⅓ der Schulterpolster-Erhöhung ist eine Näherung der Quelle.
- **Status:** `normalisiert`
- **Hinweis für die spätere Python-Umsetzung:** Ergebnisse als Näherungswerte kennzeichnen und die Schulterpolster-Erhöhung als bereits gemessene Eingabe verlangen.
