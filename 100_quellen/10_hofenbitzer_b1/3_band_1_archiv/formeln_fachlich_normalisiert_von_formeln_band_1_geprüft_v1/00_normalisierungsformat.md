# Normalisierungsformat — Hofenbitzer Band 1, geprüft v1

## Zweck und Grenze

Dieses Format trennt zwei Ebenen:

1. **Buchfassung:** unveränderter Auszug aus der extrahierten Formeldatei.
2. **Technische Normalisierung:** eindeutige Benennung und Struktur für eine spätere Umsetzung.

Die technische Normalisierung ist eine abgeleitete Arbeitsfassung. Sie korrigiert die Buchfassung nicht. Ergänzungen, Verallgemeinerungen oder mögliche Lesarten werden ausdrücklich als Hypothese oder technische Festlegung bezeichnet.

## Pflichtfelder pro Formel

- **Formel-ID:** stabil als `HOF-B1-S<Seite>-F<laufende Nummer>`.
- **Fachlicher Zweck**
- **Quelle:** extrahierte Formeldatei, dortiger Zeilenbereich, Originaltranskript und Buchseite.
- **Originalbezeichnung**
- **Normalisierte Bezeichnung**
- **Buchfassung:** unverändert in einem `text`-Block.
- **Eingaben:** technische Variable, Buchbegriff und Einheit.
- **Rechenschritte:** erst allgemeine technische Form, danach die Buchwerte.
- **Ausgabe:** technische Variable, Bedeutung und Einheit.
- **Abhängigkeiten**
- **Gültigkeitsbereich und Randbedingungen**
- **Offene Fragen oder Widersprüche**
- **Status:** `normalisiert`, `hypothetisch`, `offen` oder `gesperrt`.
- **Hinweis für die spätere Python-Umsetzung**

## Schreibregeln

- Technische Variablen verwenden beschreibende `snake_case`-Namen ohne Umlaute.
- Buchkürzel bleiben erhalten, sofern die Quelle eines vorgibt; sie werden nicht erfunden.
- Einheiten stehen an jedem Eingabe- und Ausgabewert.
- `:` wird technisch als Division `/`, `·` oder `×` als Multiplikation `*` dargestellt.
- Klammern machen die Rechenreihenfolge eindeutig.
- Deutsches Dezimalkomma bleibt bei Buchwerten erhalten. Ein Dezimalpunkt ist erst in Python-Code zulässig.
- Reine Zahlen wie Teilungs- oder Maßstabsfaktoren tragen die Einheit `dimensionslos`.
- Technische Randbedingungen werden als solche bezeichnet und nicht als Aussage des Buches ausgegeben.

## Statusbedeutung

| Status | Bedeutung |
|---|---|
| `normalisiert` | Die Buchfassung lässt sich ohne fachliche Ergänzung technisch eindeutig darstellen. |
| `hypothetisch` | Eine mögliche technische Lesart ist dokumentiert, aber nicht als endgültige Regel belegt. |
| `offen` | Für eine eindeutige Normalisierung fehlt eine belegte Information oder Entscheidung. |
| `gesperrt` | Ein Widerspruch verhindert die spätere Umsetzung bis zur Quellen- oder Fachentscheidung. |

Der Status bewertet die **Normalisierung**, nicht den Freigabestatus des Buchtranskripts.
