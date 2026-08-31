# Fachlich normalisierte Formeln — S. 379

Quelle der Normalisierung: `../hofenbitzer_band_1_digital/10_ausschnitte_s370-437/formeln_s379_codex_v2.md`
Originaltranskript: `../hofenbitzer_band_1_digital/10_ausschnitte_s370-437/s379_codex_v2.md`
Buchseite: Hofenbitzer, Band 1, S. 379

## HOF-B1-S379-F01 — Unbezeichnete Multiplikation über sechs Nähte

- **Fachlicher Zweck:** Die extrahierte Multiplikation eines Betrags von `1 cm` mit sechs Nähten rechnerisch erhalten; die fachliche Ausgabe bleibt wegen der im Extrakt fehlenden Bezeichnungszeile offen.
- **Quelle:** `formeln_s379_codex_v2.md`, Zeilen 9 und 14; Originaltranskript `s379_codex_v2.md`, Zeilen 13 und 15; Buchseite 379.
- **Originalbezeichnung:** Im Extrakt unbezeichnete Rechnung `1 cm × 6 Nähte = 6 cm`.
- **Normalisierte Bezeichnung:** `unbezeichnete_multiplikation_sechs_naehte`

### Buchfassung

```text
**= 1 cm × 6 Nähte am gesamten Modell**
```

```text
**= 6 cm**
```

### Eingaben

| Technische Variable | Buchbegriff | Wert | Einheit |
|---|---|---:|---|
| `betrag_je_naht` | unbezeichneter Betrag je Naht | 1 | cm |
| `anzahl_naehte` | Nähte am gesamten Modell | 6 | dimensionslos |

### Formel und Rechenschritte

```text
unbezeichnetes_gesamtmass = betrag_je_naht * anzahl_naehte
                           = 1 cm * 6
                           = 6 cm
```

### Ausgabe

| Technische Variable | Bedeutung | Wert | Einheit |
|---|---|---:|---|
| `unbezeichnetes_gesamtmass` | im Extrakt fachlich nicht bezeichnetes Gesamtmaß | 6 | cm |

- **Abhängigkeiten:** Betrag je Naht und Anzahl der Nähte am gesamten Modell.
- **Gültigkeitsbereich:** Numerische Rechnung auf S. 379; eine fachliche Bindung an die Saumweitenreduzierung ist erst nach Ergänzung der Extraktionsschicht zulässig.
- **Technische Randbedingung:** Die Rechnung ist numerisch vollständig, aber ihre Überschrift und die unmittelbar vorangehende Bezeichnungszeile fehlen im verbindlichen Extrakt.
- **Offene Fragen oder Widersprüche:** Das Originaltranskript bezeichnet die Rechnung als Reduzierung der Saumweite. Diese Bezeichnung darf hier nicht zur Buchfassung ergänzt werden, solange sie im Formel-Extrakt fehlt.
- **Status:** `offen`
- **Hinweis für die spätere Python-Umsetzung:** Noch keine fachlich benannte Funktion erzeugen; zunächst die fehlende Bezeichnungszeile in der Extraktionsschicht ergänzen und erneut normalisieren.

## Ausgeschlossene Kandidaten

| Quelldatei und Quelle | Kandidatenzeilen | Ausschlussgrund |
|---|---:|---|
| `formeln_s379_codex_v2.md`, Zeile 19 | 1 | Wiederholung der auf S. 377 beschriebenen Öffnung des seitlichen Vorderteils um `ca. 0,3 bis 0,7 cm`; konstruktiver Eingabebereich, keine aus Eingaben berechnete Beziehung |
| **Summe** | **1** | **1 wiederholte Konstruktionsregel ausgeschlossen** |

## Prüfhinweis zur Extraktionsgrenze

Die Überschrift `Reduzierung der Saumweite` und der Satz, dass die Reduzierung an jeder Naht `1 cm` beträgt, stehen nur im Originaltranskript unmittelbar vor den extrahierten Rechenzeilen. Deshalb bleibt die Rechnung trotz des klaren Seitenkontexts fachlich ungebunden und `offen`. Der Abschluss von `M02` gilt für den vorhandenen extrahierten Kandidatenbestand.
