# Hofenbitzer Band 1 digital – geschützter Quellenbestand

## Status und Zweck

Dieser Ordner ist ein **schreibgeschützter Quellenbestand** für den Aufbau der
Bridal Engine. Der Schutz ist eine verbindliche Arbeitsregel für Menschen und
Agenten; er ist kein technischer Windows-Dateischutz.

Alle Inhalte dürfen jederzeit **gelesen und über ihre Pfade referenziert**
werden. Engine-Code und erzeugte Ergebnisse werden außerhalb dieses Ordners
geführt.

## Schreibschutz

Diese Regeln gelten rekursiv für den gesamten Ordner. Eine untergeordnete
`AGENT.md` darf die folgenden Grenzen nicht erweitern.

Nicht verändern, löschen, verschieben oder umbenennen:

- Seitentranskriptionen `sNNN.md`
- ursprüngliche Formeldateien `formeln_sNNN.md`
- bestehende Prüfstellen und deren Belegstruktur
- Ordnernamen und die bestehende Quellenstruktur
- sonstige vorhandene Quelldateien

Auch offensichtliche Schreibfehler werden nicht still in den Quellen
korrigiert. Die Originaldateien bleiben als Beleg erhalten.

### Was „bestehende Prüfstellen" hier meint

Gemeint ist der **Beleg**: der Wortlaut einer Prüfstelle, ihre Nummer und
ihre Zuordnung zur Buchseite. Der wird nicht angetastet.

Nicht gemeint ist der **Status**. Eine Prüfstelle wandert im Lauf der Arbeit
von `zu klären` nach `geklärt` oder `Anmerkung` — das ist der Zweck der
Prüfstellen und kein Eingriff in die Quelle. Der Eintrag verschwindet dabei
nie: er bleibt mit seiner Antwort stehen. Auch eine Prüfstelle, die sich als
gegenstandslos erweist, wird nicht gelöscht, sondern trägt künftig den
Vermerk, dass geprüft und nichts gefunden wurde. Nur so ist später
unterscheidbar, ob eine Seite geprüft und in Ordnung war oder nie
angeschaut wurde.

**Wo der Status geändert wird:** ausschließlich in den fünf Zusammenzügen im
Archiv unter `100_quellen/30_hofenbitzer_band_1_archiv/`. Die liegen
außerhalb dieses geschützten Ordners.

## Einzige fachliche Ausnahme: Normalisierungen

Wenn beim konkreten Aufbau der Engine eine noch fehlende Normalisierung
benötigt und anhand der Quelle geprüft wird, darf im passenden Buchordner die
Datei

```text
formeln_sNNN_normalisiert.md
```

neu angelegt oder fachlich ergänzt werden.

Dabei gilt:

1. Die Normalisierung ergänzt die Quelle; sie ersetzt oder verändert sie nicht.
2. Sie muss der konkreten Buchseite und der ursprünglichen Formeldatei
   eindeutig zugeordnet bleiben.
3. Unklare oder ungeprüfte Aussagen bleiben als solche sichtbar und dürfen
   nicht als gesicherte Formel ausgegeben werden.
4. Es werden nur Normalisierungen eingepflegt, die in der laufenden
   Engine-Arbeit tatsächlich benötigt und geprüft wurden.
5. Nach einer Normalisierung darf ausschließlich der zugehörige Status in
   dieser `AGENT.md` aktualisiert werden.

Andere neue oder geänderte Dateien sind in diesem Quellenbestand nicht
zulässig.

## Zweite Ausnahme: die erzeugte Arbeitsansicht

`pruefstellen_nach_seiten/` ist keine Quelle, sondern eine **abgeleitete
Ansicht**. Sie enthält keinen eigenen Inhalt: jede ihrer 472 Dateien wird
aus den fünf Zusammenzügen im Archiv erzeugt.

Dieser Ordner darf deshalb überschrieben werden — aber **nur** durch das
Skript, nie von Hand:

```text
python 600_prozess/werkzeuge/pruefstellen_ansicht_bauen.py             Probelauf
python 600_prozess/werkzeuge/pruefstellen_ansicht_bauen.py --schreiben
```

Dabei gilt:

1. Der Status einer Prüfstelle wird in der Archivquelle geändert, nicht hier.
2. Danach wird die Ansicht neu erzeugt. Der Probelauf zeigt vorher, welche
   Seitendateien sich ändern würden.
3. Von Hand in der Ansicht geänderte Dateien gehen beim nächsten Lauf
   verloren. Wer hier etwas ändern will, ändert die Quelle.
4. Das Skript liest die Seitentranskriptionen und Formeldateien nicht und
   schreibt außerhalb von `pruefstellen_nach_seiten/` nichts.

## Was außerhalb dieses Ordners bleibt

Insbesondere nicht hier ablegen:

- Python- oder anderer Engine-Code
- Tests und Testdaten
- JSON-Zwischendaten
- Berechnungsergebnisse
- SVG-, DXF- oder PDF-Ausgaben
- Arbeitskopien der Quellen

Diese Artefakte gehören in `200_funktionen` beziehungsweise in die dafür
vorgesehenen Engine- und Ausgabeordner. Die Engine greift von dort lesend auf
diesen Quellenbestand zu.

## Inhaltsverzeichnis und Normalisierungsstand

„Offen“ bedeutet hier mechanisch: Eine Datei `formeln_sNNN.md` ist vorhanden,
aber die zugehörige Datei `formeln_sNNN_normalisiert.md` fehlt.

| Bereich | Seiten | Formeldateien | Normalisiert | Offen |
|---|---:|---:|---:|---:|
| [`00_vorspann_s1-7`](00_vorspann_s1-7/) | 1–7 | 0 | 0 | 0 |
| [`01_grundlagen_s8-31`](01_grundlagen_s8-31/) | 8–31 | 18 | 4 | 14 |
| [`02_grundschnitte_roecke_s32-39`](02_grundschnitte_roecke_s32-39/) | 32–39 | 7 | 6 | 1 |
| [`03_modelle_roecke_s40-105`](03_modelle_roecke_s40-105/) | 40–105 | 50 | 15 | 35 |
| [`04_grundschnitte_hosen_s106-137`](04_grundschnitte_hosen_s106-137/) | 106–137 | 26 | 21 | 5 |
| [`05_modelle_hosen_s138-170`](05_modelle_hosen_s138-170/) | 138–170 | 26 | 10 | 16 |
| [`06_grundschnitte_oberteile_s171-196`](06_grundschnitte_oberteile_s171-196/) | 171–196 | 23 | 20 | 3 |
| [`07_grundschnitte_aermel_s197-220`](07_grundschnitte_aermel_s197-220/) | 197–220 | 18 | 12 | 6 |
| [`08_aermel_varianten_s221-289`](08_aermel_varianten_s221-289/) | 221–289 | 60 | 13 | 47 |
| [`09_kragen_kapuzen_taschen_s290-369`](09_kragen_kapuzen_taschen_s290-369/) | 290–369 | 65 | 39 | 26 |
| [`10_ausschnitte_s370-437`](10_ausschnitte_s370-437/) | 370–437 | 41 | 6 | 35 |
| [`11_modelle_kleider_blusen_westen_s438-464`](11_modelle_kleider_blusen_westen_s438-464/) | 438–464 | 23 | 7 | 16 |
| [`12_modelle_jacken_s465-492`](12_modelle_jacken_s465-492/) | 465–492 | 24 | 5 | 19 |
| [`13_sportswear_waesche_unisex_s493-534`](13_sportswear_waesche_unisex_s493-534/) | 493–534 | 38 | 25 | 13 |
| [`14_anhang_sachwortverzeichnis_s535-544`](14_anhang_sachwortverzeichnis_s535-544/) | 535–544 | 6 | 5 | 1 |
| [`pruefstellen_nach_seiten`](pruefstellen_nach_seiten/) | seitenweise Prüfstellen | – | – | – |
| **Gesamt** | **1–544** | **425** | **188** | **237** |

## Offene Normalisierungen nach Bereich

- **01 – Grundlagen:** S. 8, 17, 18, 21–31
- **02 – Grundschnitte Röcke:** S. 36
- **03 – Modelle Röcke:** S. 42, 46, 51, 53–57, 59–60, 62–67, 69–73,
  77–78, 85, 87, 92, 94–98, 100–102, 105
- **04 – Grundschnitte Hosen:** S. 113, 118, 121, 133, 135
- **05 – Modelle Hosen:** S. 140, 142, 144–145, 147–149, 151, 156–159,
  161–162, 164, 169
- **06 – Grundschnitte Oberteile:** S. 172–173, 187
- **07 – Grundschnitte Ärmel:** S. 201, 206, 208, 213–215
- **08 – Ärmelvarianten:** S. 222, 224–234, 236, 238–239, 241–245, 247,
  249–253, 255–257, 260–262, 265–270, 272, 274, 276, 278–279, 282–285
- **09 – Kragen, Kapuzen und Taschen:** S. 291–293, 303, 305, 319, 321,
  325, 329, 331, 333, 335, 337–340, 356–357, 359–365, 367
- **10 – Ausschnitte:** S. 375, 377, 382–388, 390, 392–396, 398, 400–401,
  406–407, 410–412, 414–416, 426–427, 429–432, 434, 436–437
- **11 – Modelle Kleider, Blusen und Westen:** S. 438–439, 442–443, 446–447,
  453–462
- **12 – Modelle Jacken:** S. 469–478, 481–482, 484–490
- **13 – Sportswear, Wäsche und Unisex:** S. 496, 503, 505, 507, 516,
  521–523, 526–527, 530, 532, 534
- **14 – Anhang und Sachwortverzeichnis:** S. 539

Die Liste ist ein Arbeitsindex und keine automatische fachliche Freigabe. Eine
Normalisierung gilt erst dann als verwendbar, wenn sie im konkreten
Engine-Schritt anhand der Quelle und vorhandener Prüfstellen kontrolliert
wurde.
