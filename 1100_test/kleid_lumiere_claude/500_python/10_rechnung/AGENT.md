# Rechnung — Arbeitsordner

## Navigation — Regel

Diese Datei gilt nur für `500_python/10_rechnung/` und führt zu dessen direkten
Unterordnern.

## Navigation

| Bereich | Inhalt | Buchseiten |
|---|---|---|
| `geometrie/` | modeblinde Primitive B1–B9 | — |
| `masse/` | DOB-Größentabelle | S. 20 |
| `schnitt/` | Abnäher, erhöhte Nähte, Schnittlinien — was Rock und Oberteil teilen | — |
| `rock/` | gerader Rock, saumerweiterter Rock, Vollglocke | S. 33–35, 42–43, 44 |
| `oberteil/` | Grundgerüst, taillierter Oberteil-GS | S. 177–181, 184–185 |
| `ausgabe/` | neutrales Schnittteil, DXF-Export | — |

`test_buchwerte.py` hält die Prüfwerte des Buchs. **Ohne grünen Lauf gilt hier
nichts als fertig.**

    python 500_python/10_rechnung/test_buchwerte.py

Unterhalb dieser Ebene gilt Python-Namensraum: kleine Buchstaben, keine
Ziffer am Anfang, keine Umlaute — auch nicht in Bezeichnern und Docstrings.

## Stand der Freigaben

Alle Module rechnen aus **digital geprüften**, aber noch nicht **fachlich
freigegebenen** Transkripten. Einzige Ausnahme: S.44 (Vollglocke), fachlich
freigegeben durch Werner/Munkhuu am 2026-06-21.

Jede offene oder widersprüchliche Buchstelle steht im Kopf des betroffenen
Moduls, nicht in einem Sammel-Dokument — dort wird sie gelesen, wo sie wirkt.
