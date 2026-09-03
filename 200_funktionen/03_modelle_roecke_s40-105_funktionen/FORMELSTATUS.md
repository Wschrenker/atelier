# Formelstatus S. 40–105

## Herkunft und Grenze

Quelle: `C:\ATELIER\100_quellen\10_hofenbitzer_b1\1_hofenbitzer_band_1_digital\03_modelle_roecke_s40-105`

Bestand der Quelle:

- 50 extrahierte `formeln_*.md` ohne Suffix `_normalisiert`;
- 15 Dateien `formeln_*_normalisiert.md`;
- darin 42 eindeutige Formel-IDs: 36 `normalisiert`, 1 `offen`, 5 `gesperrt`.

Die fachliche Sicht teilt die 65 Dateien in drei Gruppen:

- **30 Kern-Allowlist-Dateien:** 15 Extrakte mit ihren 15 Normalisierungen;
- **12 Kontroll-/Grenzfälle:** Definitionen, Maßvorgaben oder geometrische
  Gleichsetzungen ohne abgeschlossene Normalisierung;
- **23 Nachweis-/Fehlklassifikationsdateien:** nur Bildverweise,
  Produktionsbeschriftungen, Stückzahlen oder Lückennachweise — ausdrücklich
  keine Formel-Allowlist.

Alle 65 Dateien wurden zusammen mit ihren Seitenbelegen in die zuständigen
Funktionsordner kopiert. Die 23 Nachweisdateien bleiben ausschließlich für den
Auditpfad sichtbar und dürfen nicht als Rechenregeln behandelt werden. Der
Dateiname `formeln_...` beweist nicht, dass eine ausführbare Formel enthalten
ist. Nur die normalisierten Dateien besitzen Formel-IDs und Statusfelder. Auch
`normalisiert` bedeutet noch keine fachliche Freigabe für Code.

## Normalisierte Gruppen

| Seiten | Funktion | Dateien |
|---|---|---|
| 40 | Knopflochlänge am geraden Bund | `formeln_s40.md`, `formeln_s40_normalisiert.md` |
| 43 | Keilanzahl, Öffnungs-/Ausstellbetrag | `formeln_s43.md`, `formeln_s43_normalisiert.md` |
| 44–45 | Voll-/Halbglocke: Taillenradius, Saumradius, Saumweite | jeweiliger Extrakt + Normalisierung |
| 47 | Innenbeinteil-Breiten | `formeln_s47.md`, `formeln_s47_normalisiert.md` |
| 48 | Kräuselfaktoren | `formeln_s48.md`, `formeln_s48_normalisiert.md` |
| 52 | Taillenvertiefung mit Zuschlag | `formeln_s52_codex_v2_digital_geprueft.md`, `formeln_s52_normalisiert.md` |
| 68 | Saumweite mit eingesetzten Godets | `formeln_s68.md`, `formeln_s68_normalisiert.md` |
| 79 | Saumweitenreduzierung Ballonrock | Extrakt + Normalisierung S. 79 |
| 86 | Faltenraster und Weitenkontrolle | Extrakt + Normalisierung S. 86 |
| 88–89 | Falteninhalt/Faltentiefe | jeweiliger Extrakt + Normalisierung |
| 90–91 | Vollkreis-/Mehrkreis-Volants | jeweiliger Extrakt + Normalisierung |
| 93 | doppelter Schlitzeinschlag | `formeln_s93.md`, `formeln_s93_normalisiert.md` |

## Offen

- `HOF-B1-S047-F03` — halbes Bezugsmaß plus 0,5 am hinteren Innenbeinteil;
  fachliche Bezugsgröße/Einheit bleibt zu klären.

## Gesperrt

- `HOF-B1-S086-F07` — Kontrolle der offenen Weite.
- `HOF-B1-S090-F05` — Ansatzradius bei zwei Kreisringen.
- `HOF-B1-S090-F07` — gesamte Saumweite bei zwei Kreisringen.
- `HOF-B1-S091-F01` — Ansatzradius bei vier Kreisringen.
- `HOF-B1-S091-F03` — gesamte Saumweite bei vier Kreisringen.

Die Sperren bleiben bestehen, bis Rechenweg, Buchwert und Bedeutung der
Nahtzugaben am physischen Buch fachlich geklärt sind. Keine korrigierte Formel
erfinden.

## Weitere sichtbare Buchgrenzen

Die zentrale Kopie `08_pruefung_und_kontrolle/quellenbelege/00_pruefstellen.md`
führt zehn offene Buchpunkte: A7–A13, B8–B9 und N1. Höchste Priorität hat N1 auf
S. 79, weil ein unlesbares Wort mitten in einer Konstruktionsanweisung steht.

Darüber hinaus bleiben bei der seitenübergreifenden Funktionsanalyse sichtbar:

- S. 92/95: hM/SN-Zuordnung beim RV-/Futterschlitz prüfen;
- S. 96: SN im Satz gegenüber RV-Zähnchen an hM prüfen;
- S. 97: VT-/RT-Beschriftungen und `1 bis 1 cm` gegenüber `1 bis 4 cm` prüfen;
- S. 43: im Extrakt abgeschnittene Zeilen und fehlende allgemeine Verdopplung
  der Keile kontrollieren;
- S. 98: Schritte 12–15 sind laut Formeldatei nicht transkribiert.

Für S. 41, 49, 50, 58, 61, 74–76, 80–84, 99, 103 und 104 liegt keine
Formeldatei vor. Daraus darf ohne vollständigen Extraktionsindex nicht gefolgert
werden, dass die Buchseiten fachlich keine Formeln enthalten.

## Nächster Schritt

Zuerst N1 S. 79 und danach die fünf gesperrten Formeln am Buch prüfen. Erst nach
protokollierter fachlicher Freigabe darf aus einer Formel ein Primitive werden.
Noch keinen Python-Code schreiben.
