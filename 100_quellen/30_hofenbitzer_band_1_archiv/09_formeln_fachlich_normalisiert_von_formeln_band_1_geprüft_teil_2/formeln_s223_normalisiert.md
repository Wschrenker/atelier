# Fachlich normalisierte Formeln — S. 223

Quelle der Normalisierung: `formeln_s223_digital_geprüft.md`
Originaltranskript: `s223_digital_geprüft.md`
Buchseite: Hofenbitzer, Band 1, S. 223
Extraktionsstand: v2

## HOF-B1-S223-F01 — Unbezeichnete Summe mit doppeltem Teilbetrag

- **Fachlicher Zweck:** Die vollständig extrahierte Einsetzrechnung erhalten, ohne ihr die nur im Originaltranskript stehende fachliche Bezeichnung als verbindliche Buchfassung zuzuschreiben.
- **Quelle:** `formeln_s223_digital_geprüft.md`, Zeile 9; Originaltranskript `s223_digital_geprüft.md`, Zeile 18; Buchseite 223. Fachlicher Kontext nur im Originaltranskript, Zeilen 14–16.
- **Originalbezeichnung:** Im Extrakt nicht enthalten; dort steht nur die Einsetzrechnung.
- **Normalisierte Bezeichnung:** `unbezeichnete_summe_mit_doppeltem_teilbetrag`

### Buchfassung

```text
   hier: 20 cm + (2× 4 cm) = 28 cm
```

### Eingaben

| Technische Variable | Bezeichnung im Extrakt | Wert | Einheit |
|---|---|---:|---|
| `grundwert_unbezeichnet` | erster Summand | 20 | cm |
| `anzahl_teilbetraege` | Faktor | 2 | dimensionslos |
| `teilbetrag_unbezeichnet` | Betrag in der Klammer | 4 | cm |

### Formel und Rechenschritte

```text
unbezeichnetes_ergebnis = grundwert_unbezeichnet + (anzahl_teilbetraege * teilbetrag_unbezeichnet)
unbezeichnetes_ergebnis = 20 cm + (2 * 4 cm)
unbezeichnetes_ergebnis = 28 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `unbezeichnetes_ergebnis` | rechnerisches Ergebnis ohne im Extrakt belegten fachlichen Zielnamen | 28 | cm |

- **Abhängigkeiten:** Die fachliche Bedeutung der drei Zahlen muss durch eine korrigierte beziehungsweise ergänzte Extraktion belegt werden. Das Originaltranskript nennt in Zeilen 14–16 einen Bezug zur Ärmelsaum-Weite, Manschettenweite, Faltenzahl und zum Falteninhalt; dieser Kontext ist nicht Bestandteil des Extrakts.
- **Gültigkeitsbereich:** Rechnerisch nur die gedruckte Einsetzrechnung auf S. 223; keine ausführbare fachliche Regel, solange die Bezeichnungszeile im Extrakt fehlt.
- **Technische Randbedingung:** Die Klammer wird zuerst berechnet. Die Größen dürfen technisch noch nicht an Manschetten- oder Faltenvariablen gebunden werden.
- **Offene Fragen oder Widersprüche:** `20 + (2 × 4) = 28` ist rechnerisch richtig. Offen bleibt die fachliche Bindung, weil die allgemeine Bezeichnungszeile nicht extrahiert wurde.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Noch nicht implementieren. Zuerst die Extraktionslücke schließen und danach die fachlichen Eingabe- und Ausgabenamen gegen die Quelle übernehmen.

## Ausgeschlossene Kandidaten

| Quelle in `formeln_s223_digital_geprüft.md` | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| Zeilen 14–15 | 2 | Produktionsschnitt-Angaben zu Stückzahl, Oberstoff/Einlage und doppelter Manschettenbreite; keine berechnete Ausgabe |
| Zeile 20 | 1 | Produktionsschnitt-Angabe `4× OSt+El`; Stückzahl und Material, keine Rechenformel |
| **Summe** | **3** | **3 Produktions-/Zuschnittbeschriftungen** |

## Extraktionsgrenze

Die allgemeine Beziehung `Manschettenweite + (Faltenzahl x Falteninhalt)` steht im Originaltranskript `s223_digital_geprüft.md`, Zeile 16, fehlt aber im verbindlichen Extrakt. Sie wurde deshalb nicht als Buchfassung ergänzt. Weitere formelartige Angaben zu halber Manschettenbreite und halber Ärmelsaum-Weite stehen ebenfalls nur im Transkript. Der Seitenabschluss gilt für den vorhandenen extrahierten Kandidatenbestand.
