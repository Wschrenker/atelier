# Fachliche Normalisierung — Hofenbitzer Band 1, geprüft v1

## Auftrag

Dieser Ordner enthält die **fachlich und technisch normalisierte Arbeitsfassung** der bereits extrahierten Hofenbitzer-Formeln.

Arbeitsrichtung:

```text
hofenbitzer_band_1_digital/
→ Formeln_fachlich_normalisiert_von_formeln_band_1_geprüft_v1/
```

Langfristige Kette:

```text
Buch → geprüftes Transkript → extrahierte Formel → fachlich normalisierte Formel
→ Mathematik → Python-Modul → Schnittfamilie → Brautkleid
```

Die spätere v2 und v3 blockieren diese v1-Arbeit nicht.

## Verbindliche Grenzen

- Der Quellordner `../hofenbitzer_band_1_digital/` bleibt unverändert.
- Normalisierung ersetzt und korrigiert keine Buchquelle.
- Buchfassung und technische Fassung bleiben sichtbar getrennt.
- Keine fehlenden Werte, Begriffe oder Regeln erfinden.
- Widersprüche erhalten, benennen und höchstens getrennt als Hypothese ausweisen.
- Seitenzahl, Quelldatei und Zeilenbereich jeder Formel erhalten.
- Vorhandene Python-Fragmente sind später technische Bausteine, aber kein Beweis für eine Buchformel.
- Keine Änderungen außerhalb dieses Zielordners, sofern der Auftrag sie nicht ausdrücklich verlangt.
- Nicht committen oder pushen ohne ausdrückliche Freigabe.

Das verbindliche Einzelformular und die Statusbedeutungen stehen in [`00_normalisierungsformat.md`](00_normalisierungsformat.md).

## Arbeitsweise in Tranchen

### 1. Gesamtbestand zuerst flach kartieren

Alle extrahierten Formeldateien nur so weit überfliegen, dass je Datei feststeht:

- Seite und Kapitel;
- fachliches Thema;
- Anzahl und Art der echten Formeln;
- verwendete Variablen und Abhängigkeiten;
- erkennbare Widersprüche;
- Fehlklassifikationen;
- Schwierigkeit: einfach, mittel oder komplex.

Dabei noch nicht den gesamten Bestand normalisieren.

### 2. Fachliche Tranchen bilden

Nicht starr zehn Seiten bündeln. Zusammengehörige Formeln und abhängige Folgeseiten bleiben zusammen.

Richtwerte:

- einfache Einzelrechnungen oder Tabellen: 10–20 Seiten;
- normale Formelgruppen: 5–10 Seiten;
- komplexe Konstruktionen: 2–5 Seiten;
- widersprüchliche Stellen: bei Bedarf nur eine Seite.

Zielgröße: ungefähr **20–40 echte Formeln pro Tranche**. Fachlicher Zusammenhang ist wichtiger als die Zahl.

Voraussichtliche Hauptwellen:

1. Einführung, Zeichen und Proportionen;
2. Körpermaße und Maßtabellen;
3. Röcke;
4. Hosen;
5. Oberteile;
6. Ärmel;
7. Kragen, Ausschnitte und Kapuzen;
8. weitere Modellkonstruktionen;
9. Gesamtprüfung der Variablen, Abhängigkeiten und offenen Stellen.

### 3. Eine Tranche bearbeiten

1. Extrahierte Formeldateien und die genannten Originaltranskripte lesen.
2. Begriffe und Kürzel innerhalb der Tranche konsistent verwenden.
3. Jede Formel nach `00_normalisierungsformat.md` normalisieren.
4. Buchfassung unverändert übernehmen.
5. Eingaben, Ausgaben, Einheiten, Rechenfolge und Abhängigkeiten ausweisen.
6. Unklarheiten als `hypothetisch`, `offen` oder `gesperrt` markieren.
7. Quelldatei und Ziel direkt vergleichen.
8. Index und Arbeitsstand aktualisieren.

Eine offene Formel blockiert nicht die belegbaren Formeln derselben Tranche.

## Benennung

- Eine normalisierte Datei bleibt einer Quellseite eindeutig zugeordnet: `formeln_s<seite>_normalisiert.md`.
- Formel-ID: `HOF-B1-S<dreistellige Seite>-F<zweistellige laufende Nummer>`.
- Technische Variablen: beschreibendes `snake_case` ohne Umlaute.
- Buchkürzel bleiben erhalten, wenn die Quelle sie vorgibt; keine Kürzel erfinden.

## Qualitätsprüfung nach jeder Tranche

- Buchfassungen kommen wortgleich in Quelle und Ziel vor.
- Seiten, Dateipfade und Zeilenbereiche stimmen.
- Rechenergebnisse und Einheiten sind geprüft.
- Keine unbelegte Regel wurde ergänzt.
- Widersprüche und Hypothesen sind sichtbar.
- Formel-IDs und Dateinamen sind eindeutig.
- Markdown-Fences und interne Verweise sind gültig.
- Der Quellordner ist unverändert.
- [`00_index_normalisierte_formeln_band_1_v1.md`](00_index_normalisierte_formeln_band_1_v1.md) ist aktuell.

## Aktueller Stand

- Quellbestand bei der ersten Inventur: 183 Formeldateien plus Index.
- S. 1 und S. 2 sind Fehlklassifikationen: Adresse beziehungsweise ISBN, keine Formeln.
- Tranche `F01` ist abgeschlossen: S. 11, 14, 19 und 20 enthalten zusammen 20 normalisierte Formeln.
- In `F01` sind 18 Formeln `normalisiert`, 1 `offen` und 1 `hypothetisch`; ausgeschlossene Kandidaten sind in den jeweiligen Zieldateien benannt.
- Tranche `K01` ist abgeschlossen: Die 28 Kandidatenzeilen auf S. 8.1, 17, 18 und 21–24 sind Abkürzungs- oder Symboldefinitionen, Seitenverweise, Linien- und Maßbeschriftungen, Randregister oder Schnittteil-Stempel. Keine davon ist eine Rechenformel; deshalb wurden keine leeren Normalisierungsdateien angelegt.
- Tranche `K02` ist abgeschlossen: Die 35 Kandidatenzeilen auf S. 25–31 sind Randregister, Schnitt- und Maßlabels, Konstruktions- oder Produktionsregeln, Zuschnittkürzel, Tabellenangaben, Datumsangaben oder Verweise. Keine davon enthält eine belegte Rechenformel; deshalb wurden keine leeren Normalisierungsdateien angelegt.
- Tranche `R01` ist abgeschlossen: Die 23 Kandidatenzeilen auf S. 33–36 wurden geprüft. 9 belegte Formeln zu Taillenausfall, Hüftweite, Kontrollsummen, Hüftabstich und Abnäherposition sind normalisiert; 14 Fehlklassifikationen oder Wiederholungen sind dokumentiert. Für S. 36 wurde keine leere Normalisierungsdatei angelegt.
- Tranche `R02` ist abgeschlossen: Die 18 Kandidatenzeilen auf S. 37–40 wurden geprüft. 14 Kandidatenzeilen bilden 10 fachlich bearbeitete Formelblöcke zu figurabhängigem Hüftabstich, tiefer Bundposition, geradem Bund, Einhalteweite und Knopflochlänge; 4 Fehlklassifikationen oder Wiederholungen sind dokumentiert. 9 Formeln sind `normalisiert`, die widersprüchliche Formel `TaAf = Taillenabtrennung - 1/2 BuW` auf S. 38 bleibt `gesperrt`.
- Tranche `R03` ist abgeschlossen: Die 34 Kandidatenzeilen auf S. 42–45 wurden geprüft. 24 Kandidatenzeilen bilden 11 normalisierte Formelblöcke zu Saumerweiterung, Keil- und Öffnungsbeträgen sowie Voll- und Halbglocke; 10 Fehlklassifikationen, Eingabewerte oder Wiederholungen sind dokumentiert. S. 42 enthält im extrahierten Bestand keine Rechenformel; formelartige Beziehungen im Originaltranskript sind als Extraktionslücke sichtbar festgehalten und wurden nicht stillschweigend normalisiert.
- Tranche `R04` ist abgeschlossen: Die 12 Kandidatenzeilen auf S. 46–48 wurden geprüft. 6 Kandidatenzeilen bilden 6 fachlich bearbeitete Formelblöcke zu den Breitenbereichen des vorderen und hinteren Hosenrock-Innenbeinteils, einer unvollständig bezeichneten Halbierungsbeziehung und drei Kräuselfaktoren; 6 Nachweis-, Bildverweis- oder Wiederholungszeilen sind dokumentiert. 5 Formeln sind `normalisiert`, die Beziehung `1/2 + 0,5` auf S. 47 bleibt wegen fehlender Bezugsgröße und Einheit `offen`. Für S. 46 wurde keine leere Normalisierungsdatei angelegt.
- Tranche `R05` ist abgeschlossen: Die 16 Kandidatenzeilen auf S. 51–57, 59, 60 und 62 wurden geprüft. 1 Kandidatenzeile bildet die normalisierte Formel zur seitlichen Taillenvertiefung mit 10 Prozent Zuschlag; 15 Bildverweise, Konstruktionsanweisungen, Eingabebereiche oder Zeichnungslabels sind dokumentiert und ausgeschlossen. Nur für S. 52 wurde eine Normalisierungsdatei angelegt. Formelartige Beziehungen, die in mehreren Originaltranskripten vorkommen, aber im extrahierten Bestand fehlen, sind als Extraktionslücken sichtbar festgehalten und wurden nicht stillschweigend normalisiert.
- Tranche `R06` ist abgeschlossen: Die 20 Kandidatenzeilen auf S. 64–73, 78 und 79 wurden geprüft. 2 Kandidatenzeilen bilden 2 normalisierte Formelblöcke zur Rocksaumweite mit eingesetzten Godets und zur Saumweitenreduzierung des Ballonrocks; 18 Konstruktions- und Produktionsregeln, Zuschnittbeschriftungen oder Quellenfoto-Zuordnungen sind dokumentiert und ausgeschlossen. Nur für S. 68 und S. 79 wurden Normalisierungsdateien angelegt. Formelartige Beziehungen in den Originaltranskripten, die im extrahierten Bestand fehlen, sind als Extraktionslücken sichtbar festgehalten und wurden nicht stillschweigend normalisiert.
- Tranche `R07` ist abgeschlossen: Die 28 Kandidatenzeilen auf S. 85–87 und 92–97 wurden geprüft. 14 Kandidatenzeilen bilden 8 fachlich bearbeitete Formelblöcke zu Hüft- und Taillenweite, Taillenausfall, Faltenabständen, Falteninhalt, offener Stoffweite und doppeltem Schlitzeinschlag; 14 Bildverweise, Produktionsbeschriftungen, leere Tabellenzeilen oder reine Linienbezeichnungen sind dokumentiert und ausgeschlossen. 7 Formeln sind `normalisiert`; die Kontrolle der offenen Weite auf S. 86 bleibt wegen des Widerspruchs zwischen allgemeiner Formel (`504,8 cm`) und Einsetzzeile samt Druckergebnis (`302,4 cm`) `gesperrt`. Nur für S. 86 und S. 93 wurden Normalisierungsdateien angelegt. Extraktionslücken der Originaltranskripte sind sichtbar festgehalten.
- Tranche `H01` ist abgeschlossen: Die 25 Kandidatenzeilen auf S. 116–118 und 120–123 wurden geprüft. 19 Kandidatenzeilen bilden 15 normalisierte Formelblöcke zu hinterem Abnäherinhalt, Hosenausschnitt, Umfangsteilwerten, Hosenbreiten, Knie- und Wadenhöhe sowie individueller und vereinfachter Taillenvertiefung; 6 Wiederholungen, Produktionslabels oder reine Messbeschriftungen sind dokumentiert und ausgeschlossen. Für S. 118 und S. 121 wurden keine leeren Normalisierungsdateien angelegt. Extraktionslücken der Originaltranskripte sind sichtbar festgehalten.
- Tranche `H02` ist abgeschlossen: Die 28 Kandidatenzeilen auf S. 124–127 wurden geprüft. 15 Kandidatenzeilen bilden 14 fachlich bearbeitete Formelblöcke zur Konstruktion und Kontrolle der engen Vorder- und Hinterhose; 13 Wiederholungen, leere Tabellenzeilen oder reine Eingabewerte sind dokumentiert und ausgeschlossen. 13 Formeln sind `normalisiert`; der unbezeichnete Ausdruck `HüU : 20 + 3 cm` auf S. 125 bleibt wegen seines fehlenden geometrischen Referenten `offen`. Extraktionslücken der Originaltranskripte sind sichtbar festgehalten.
- Tranche `H03` ist abgeschlossen: Die 34 Kandidatenzeilen auf S. 128–129 wurden geprüft. 21 Kandidatenzeilen bilden 12 fachlich bearbeitete Formelblöcke zur Materialdehnung, Umfangsreduktion und Konstruktion der weiterreduzierten engen Hose; 13 Wiederholungen, leere Tabellenzeilen, Zeichnungslabels oder Eingabewerte sind dokumentiert und ausgeschlossen. 8 Formeln sind `normalisiert`; 4 Einsetzrechnungen auf S. 128 bleiben wegen ihrer im Extrakt fehlenden Bezeichnungszeilen `offen`. Extraktionslücken der Originaltranskripte sind sichtbar festgehalten.
- Tranche `H04` ist abgeschlossen: Die 32 Kandidatenzeilen auf S. 130–135 und 137 wurden geprüft. 18 Kandidatenzeilen bilden 14 fachlich bearbeitete Formelblöcke zu Bundfalteninhalten, Hosenausschnitten, Hosenbreiten, Saum- und Taillenmaßen; 14 Eingabewerte, Wiederholungen, Begriffs- oder Zeichnungslabels sind dokumentiert und ausgeschlossen. 13 Formeln sind `normalisiert`; das unvollständig extrahierte Öffnungsbetrags-Fragment auf S. 134 bleibt wegen des fehlenden Minuenden `offen`. Für S. 133 und S. 135 wurden keine leeren Normalisierungsdateien angelegt. Extraktionslücken und der Kontextwiderspruch auf S. 137 sind sichtbar festgehalten.
- Tranche `H05` ist abgeschlossen: Die 32 Kandidatenzeilen auf S. 140 und 142–145 wurden geprüft. 5 Kandidatenzeilen bilden 5 normalisierte Formelblöcke zu gemessener Knie- und Saumweite, den Differenzen zu den gewünschten Fertigmaßen und der Biesenöffnung; 27 Bildverweise, Eingabewerte, Produktionsbeschriftungen oder Konstruktionslabels sind dokumentiert und ausgeschlossen. Nur für S. 143 wurde eine Normalisierungsdatei angelegt. Extraktionslücken der Verteilungsrechnungen sind sichtbar festgehalten.
- Tranche `O01` ist abgeschlossen: Die 29 Kandidatenzeilen auf S. 172–175 wurden geprüft. 14 Kandidatenzeilen bilden 11 fachlich bearbeitete Formelblöcke zu Balance, figurabhängigen VL-/RüL-Korrekturen, der BrU-abhängigen Bal-Tabelle und der Rückübertragung auf den Grundschnitt; 15 Modell-, Passformklassen-, Bereichs-, Mess- oder Prüfzeilen sind dokumentiert und ausgeschlossen. 8 Formeln sind `normalisiert`; 3 Formeln auf S. 174 bleiben wegen widersprüchlicher Skizzenrechnungen beziehungsweise des Vorzeichenkonflikts beim Balance-Problem `gesperrt`. Für S. 172 und S. 173 wurden keine leeren Normalisierungsdateien angelegt. Extraktionslücken und der Buchfehler bei □5b sind sichtbar festgehalten.
- Tranche `O02` ist abgeschlossen: Die 35 Kandidatenzeilen auf S. 176–177 wurden geprüft. 29 Kandidatenzeilen bilden 17 fachlich bearbeitete Formelblöcke zur Passformklassen-Zugabe, Zugabentabelle, Konstruktionstabelle, Balance sowie zu Taillenausfall, Hüftfehlbetrag und Armlochmehrweite; 6 Tabellenkopf-, Metadaten-, Prüf- oder unveränderte Eingabezeilen sind dokumentiert und ausgeschlossen. 16 Formeln sind `normalisiert`; der Korrekturblock für VL und RüL auf S. 177 bleibt wegen fehlender Ausgangs- und Korrekturwerte `offen`. Bereichsauswahlen und Rundungen sind sichtbar erhalten, ohne unbelegte Auswahl- oder Rundungsregeln zu ergänzen.
- Tranche `O03` ist abgeschlossen: Die 30 Kandidatenzeilen auf S. 178–181 wurden geprüft. 23 Kandidatenzeilen bilden 20 fachlich bearbeitete Formelblöcke zur PK-3-Konstruktionstabelle, Balance, Armlochmehrweite und zum geometrischen Grundgerüst; 7 Metadaten-, Prüf-, Eingabe-, direkte Maßübertragungs- oder Punktdefinitionszeilen sind dokumentiert und ausgeschlossen. 17 Formeln sind `normalisiert`; der Korrekturblock auf S. 178 bleibt wegen fehlender Korrekturwerte `offen`, die widersprüchlichen Werte `AIT+ = 21,8` und `½ BrW = 48` bleiben `gesperrt`. Extraktionslücken der Konstruktionsbeziehungen sind sichtbar festgehalten.
- Tranche `O04` ist abgeschlossen: Die 36 Kandidatenzeilen auf S. 184–187 wurden geprüft. 27 Kandidatenzeilen bilden 23 fachlich bearbeitete Formelblöcke zu vorderem Taillenabnäher, Taillen- und Hüftausfall, Hüftfehlbetrag, Armlochmehrweite, Konstruktionstabelle und Ausfallverteilung; 9 Wiederholungs-, Tabellenkopf-, Metadaten-, Prüf- oder reine Konstruktionszeilen sind dokumentiert und ausgeschlossen. 18 Formeln sind `normalisiert`; die Verteilungskontrolle auf S. 185 bleibt wegen fehlender Summanden `offen`, vier widersprüchliche Inline- und Tabellenpfade auf S. 186 bleiben `gesperrt`. Für S. 187 wurde keine leere Normalisierungsdatei angelegt.
- Tranche `O05` ist abgeschlossen: Die 28 Kandidatenzeilen auf S. 194 wurden geprüft. 22 Kandidatenzeilen bilden 8 normalisierte Formelblöcke zum vorhandenen PK-3-Breitensatz sowie zu den Zugabedifferenzen und Verteilungen beim Öffnen auf PK 9; 6 Kontext-, Überschriften- oder wiederholte Zeichnungszeilen sind dokumentiert und ausgeschlossen. Die exakten und gedruckten Drittelwerte der ArD-Differenz bleiben getrennt sichtbar; die gedruckten Teilwerte summieren sich konsistent zur Differenz, ohne dass eine Rundungsregel erfunden wurde.
- Tranche `O06` ist abgeschlossen: Die 28 Kandidatenzeilen auf S. 195 wurden geprüft. 23 Kandidatenzeilen bilden 6 fachlich bearbeitete Formelblöcke zu Schulterzugabe, Schulternahtlängen, Ärmelpunktvertiefung sowie Taillen- und Hüftweitenkontrolle; 5 Überschriften- oder wiederholte Zeichnungs- und Eingabelabels sind dokumentiert und ausgeschlossen. 4 Formeln sind `normalisiert`; die Korrekturen der Taillen- und Hüftweite bleiben wegen der Widersprüche `0,6 cm`/`0,4 cm` beziehungsweise `1,6 cm`/`0,8 cm` `gesperrt`.
- Tranche `O07` ist abgeschlossen: Die 29 Kandidatenzeilen auf S. 196 wurden geprüft. 17 Kandidatenzeilen bilden 6 normalisierte Formelblöcke zu den Zugabedifferenzen von PK 3 zu PK 0 für Brustbreite, Armdurchmesser, Rückenbreite, Armlochtiefe, Taillenweite und Hüftweite; 12 wiederholte Tabellenzeilen, Kontext- und Überschriftenzeilen sowie Zeichnungslabels sind dokumentiert und ausgeschlossen. Die Weitenreduzierung ist auf der Seite die Methode zur Gewinnung des Korsagen-Grundschnitts und kein zweiter unabhängiger Formelblock.
- Tranche `A01` ist abgeschlossen: Die 20 Kandidatenzeilen auf S. 231–236 wurden geprüft. 7 Kandidatenzeilen auf S. 235 bilden 2 normalisierte Formelblöcke zur Erhöhung der Futter-Ärmelkugelnaht und zur Kürzung des Futterärmels; 13 Kandidaten — 11 Produktions-/Zuschnittbeschriftungen, ein Eingabelabel und eine unvollständige Wiederholung — sind dokumentiert und ausgeschlossen. Für S. 231–234 und S. 236 wurden keine leeren Normalisierungsdateien angelegt.
- Tranche `A02` ist abgeschlossen: Die 33 Kandidatenzeilen auf S. 237–240 wurden geprüft. 3 Kandidatenzeilen bilden 2 fachlich bearbeitete Formelblöcke zum Mindestabstand des untersten Ärmelknopfes vom Saum und zu zwei unbezeichneten Additionen am offenen Ärmelschlitz; 30 Produktions-/Zuschnittbeschriftungen, Wiederholungen und eine geometrische Linienbezeichnung sind dokumentiert und ausgeschlossen. 1 Formel ist `normalisiert`; die beiden Additionen auf S. 240 bleiben wegen fehlender geometrischer Referenten und Einheiten in einem gemeinsamen Formelblock `offen`. Für S. 238 und S. 239 wurden keine leeren Normalisierungsdateien angelegt.
- Tranche `K03` ist abgeschlossen: Die 2 Kandidatenzeilen auf S. 306 bilden 2 normalisierte Formelblöcke zu den Teilungsanteilen der Einschnittabstände am runden Volantkragen und am Volantkragen für den V-Ausschnitt. Beide allgemeinen Formeln und Buchbeispiele sind rechnerisch konsistent; es wurden keine Kandidaten ausgeschlossen.
- Tranche `M01` ist abgeschlossen: Die 19 Kandidatenzeilen auf S. 368–369 wurden geprüft. 2 Kandidatenzeilen bilden 2 normalisierte Formelblöcke zur Nahtzugabe als halbe Paspelbreite und zur Verlängerung um die doppelte Leistenbreite; 17 Kandidaten — Produktions-/Zuschnittbeschriftungen, ein Bildverweis, eine direkte Maßübertragung und eine Wiederholung — sind dokumentiert und ausgeschlossen. Extraktionslücken der geometrischen Biesenverdopplung und weiterer Konstruktionsmaße sind sichtbar festgehalten.
- Tranche `M02` ist abgeschlossen: Die 18 Kandidatenzeilen auf S. 371, 375–377, 379, 380 und 382–387 wurden geprüft. 5 Kandidatenzeilen bilden 4 fachlich bearbeitete Formelblöcke zur Armdurchmesser-Verkleinerung, Saumerweiterung, einer unbezeichnet extrahierten Nahtmultiplikation und der RT-Mehrweite; 13 Konstruktions-, Bildverweis-, Wiederholungs- oder Provenienzzeilen sind dokumentiert und ausgeschlossen. 3 Formeln sind `normalisiert`; die Rechnung auf S. 379 bleibt wegen der im Extrakt fehlenden fachlichen Bezeichnungszeile `offen`. Für acht Seiten wurden keine leeren Normalisierungsdateien angelegt.
- Tranche `M03` ist abgeschlossen: Die 17 Kandidatenzeilen auf S. 390–396, 398, 400 und 401 wurden geprüft. 3 Kandidatenzeilen auf S. 391 bilden 2 normalisierte Formelblöcke zur Saumerweiterung an den Seitennahtkanten und am Vorderteil nach Abzug des Hüftausfalls; 14 Bildverweis-, Methoden-, Eingabe-, Mess- oder Provenienzzeilen sind dokumentiert und ausgeschlossen. Nur für S. 391 wurde eine Normalisierungsdatei angelegt. Extraktionslücken der allgemeinen Verteilung und weiterer geometrischer Beziehungen sind sichtbar festgehalten.
- Tranche `M04` ist abgeschlossen: Die 24 Kandidatenzeilen auf S. 406, 407, 409–412 und 414–416 wurden geprüft. 1 Kandidatenzeile auf S. 409 bildet die normalisierte Verdopplung der halben Rückenteil-Taillennaht; 23 Provenienz-, Bildverweis-, Methoden-, Produktions-, Übertragungs- oder Beschriftungszeilen sind dokumentiert und ausgeschlossen. Nur für S. 409 wurde eine Normalisierungsdatei angelegt. Formelartige Beziehungen, die in den Originaltranskripten vorkommen, aber im Extrakt fehlen, sind als Extraktionslücken sichtbar festgehalten.
- Tranche `M05` ist abgeschlossen: Die 21 Kandidatenzeilen auf S. 426, 427, 429–432 und 434 wurden geprüft. Alle 21 Kandidaten sind Produktions- und Zuschnittbeschriftungen, Definitionen, Bildverweise, direkte Maßübertragungen oder redaktionelle Zeichnungsbeschreibungen; keine bildet eine extrahierte Rechenformel. Deshalb wurden keine leeren Normalisierungsdateien angelegt. Die im Originaltranskript von S. 434 enthaltene Beziehung `Einschlagbreite = Ausschnitthöhe − 4 bis 6 cm` ist als Extraktionslücke sichtbar festgehalten und wurde nicht stillschweigend normalisiert.
- Tranche `M06` ist abgeschlossen: Die 5 Kandidatenzeilen auf S. 438–439 wurden gegen die maßgebliche digital geprüfte Erstfassung und die rohe Zweitfassung geprüft. Die Kandidaten sind eine Provenienzzeile sowie zwei Bildnummernverweise, die in der Zweitfassung wiederholt werden; keine bildet eine Rechenformel. Deshalb wurden keine leeren Normalisierungsdateien angelegt. Der Doppeltranskript-Konflikt bleibt sichtbar, ohne die Klassifikation zu verändern.
- Tranche `M07` ist abgeschlossen: Die 33 Kandidatenzeilen auf S. 452–461 wurden geprüft. 1 Kandidatenzeile auf S. 452 bildet den normalisierten Abstand der Unterbrustnaht vom Brustpunkt mit den zwei Buchwegen `ca. ½ BrB - 2 cm` oder `uBrA`; 32 Produktions-, Verweis-, Provenienz-, Methoden- oder Eingabezeilen sind dokumentiert und ausgeschlossen. Nur für S. 452 wurde eine Normalisierungsdatei angelegt. Die im Buch nicht bestimmte Auswahl nach Brustgröße und weitere Extraktionslücken bleiben sichtbar.
- Tranche `M08` ist abgeschlossen: Die 32 Kandidatenzeilen auf S. 475, 476 und 478–482 wurden geprüft. 2 Kandidatenzeilen auf S. 479 und 480 bilden 2 normalisierte, gegenseitig ergänzende Formelblöcke zur gleichen Belegnahtverlängerung an Vorderteil und Beleg und zur daraus entstehenden Faltentiefe; 30 Bildverweis-, Produktions-, Methoden-, Eingabe-, Nahtzugaben- oder Wiederholungszeilen sind dokumentiert und ausgeschlossen. Nur für S. 479 und 480 wurden Normalisierungsdateien angelegt. Extraktionslücken und die im Extrakt fehlende modelllängenabhängige Auswahl innerhalb von ca. `0,5 bis 1 cm` bleiben sichtbar.
- Tranche `M09` ist abgeschlossen: Die 56 Kandidatenzeilen auf S. 484–486 wurden geprüft. Alle Kandidaten sind Verifikations- oder Modellmetadaten, Schnittteil-, Material-, Stückzahl- und Produktionsbeschriftungen, eine Fixierbeschreibung, eine Erklärung der Produktionsnotation `2×-p` oder ein Seitenverweis zur Grundschnittwahl; keine bildet eine extrahierte Rechenformel. Deshalb wurden keine leeren Normalisierungsdateien angelegt. Die im Originaltranskript auf S. 486 enthaltene proportionale Beziehung der Armlochauflockerung am Rückteil zum Vorderteil bleibt als Extraktionslücke sichtbar.
- Tranche `Z01` ist abgeschlossen: Die 16 Kandidatenzeilen auf S. 537 und 539 wurden geprüft. 12 Kandidatenzeilen auf S. 537 bilden 10 normalisierte Formelblöcke zu Umfang und Zugabe, Proportionskontrolle, korrigierten Balancelängen, individueller Balance, Taillenausfall, Hüftfehlbetrag sowie Armlochmehrweite und Sollwert; 4 unvollständige Feld-, Leerfeld- oder Provenienzzeilen sind dokumentiert und ausgeschlossen. Für S. 539 wurde keine leere Normalisierungsdatei angelegt. Die ausgefüllten PK-4-Beispiele auf S. 177 bleiben getrennt von den allgemeinen Beziehungen des Formulars auf S. 537.
- Beim Vergleich mit den Originaltranskripten wurden auf S. 17 formelartige Beziehungen im Fließtext sichtbar, die in `formeln_s17.md` nicht extrahiert sind. Sie gehören nicht zum belegten Quellbestand dieser Normalisierung und werden hier weder ergänzt noch stillschweigend normalisiert.
- Alle kartierten Tranchen des extrahierten v1-Bestands sind abgeschlossen.

## Einstieg für eine neue Session

1. Projektregeln lesen: `C:\ATELIER\AGENT.md`, `100_quellen/AGENT.md`, `100_quellen/10_hofenbitzer_b1/AGENT.md`.
2. Dieses README, `00_normalisierungsformat.md` und den Index lesen.
3. Zielbestand inventarisieren und vorhandene Dateien vor Änderungen verstehen.
4. Falls noch nicht vorhanden: flache Gesamtkarte erstellen und fachliche Tranchen festlegen.
5. Genau **eine** vereinbarte Tranche normalisieren, prüfen und im Index dokumentieren.
6. Kurz berichten: bearbeiteter Block, geprüfte Formeln, offene Stellen und nächste Tranche.

## Flache Gesamtkarte und verbindliche Tranchen

Stand der Kartierung: 2026-08-29.

Die Karte deckt den gesamten Quellindex ab: **183 Formeldateien mit 905
extrahierten Kandidatenzeilen**. Die Zeilenzahl ist nur eine Größenangabe aus dem
Extraktionsindex. Sie ist noch keine Anzahl echter Formeln: Der Extraktor hat
auch Adressen, ISBN, Überschriften, Bildnachweise, Schnittteilbeschriftungen und
reinen Fließtext erfasst. Jede Tranche trennt deshalb zuerst echte Formeln von
Fehlklassifikationen und normalisiert danach nur den belegten Formelbestand.

Statuszeichen:

- `✅` erledigt und im Zielindex dokumentiert;
- `🟡` teilweise bearbeitet;
- `⬜` offen;
- `🔎` überwiegend Sichtungs- und Fehlklassifikationsprüfung;
- `⚠️` bekannte Widersprüche oder besonders hoher Prüfbedarf.

Die Reihenfolge in der Tabelle ist die Arbeitsreihenfolge für neue Sessions.
Ausnahme: `K00` ist bereits abgeschlossen. Eine Session nimmt die erste noch
nicht erledigte Tranche, sofern Werner keine andere ausdrücklich auswählt.

| Status | Tranche | Quelldateien / Buchseiten | Kandidatenzeilen | Fachlicher Block | Schwierigkeit und bekannte Abhängigkeiten |
|---|---|---|---:|---|---|
| ✅ 🔎 | `K00` | S. 1, 2 | 2 | Adresse und ISBN | keine Formeln; als Fehlklassifikationen ausgeschlossen |
| ✅ | `F01` | S. 11, 14, 19, 20 | 27 | Figurine, Maßnehmen, Maßtabelle und Konfektionsgröße | 20 Formeln normalisiert und geprüft; offene Vorzeichen-, Messauswahl- und Größenregeln bleiben sichtbar markiert |
| ✅ 🔎 | `K01` | S. 8.1, 17, 18, 21–24 | 28 | Abkürzungssystem, Figurbeobachtung und Standards | keine Rechenformeln im extrahierten Bestand; 28 Fehlklassifikationen geprüft und im Zielindex dokumentiert; Extraktionslücke im Fließtext von S. 17 sichtbar erhalten |
| ✅ 🔎 | `K02` | S. 25–31 | 35 | Standards, Belege, Markierungen und Schnittteilangaben | keine Rechenformeln; 35 Fehlklassifikationen als Regeln, Labels, Zuschnitt- und Tabellenangaben geprüft und im Zielindex dokumentiert |
| ✅ | `R01` | S. 33–36 | 23 | Gerader Rock-Grundschnitt | 9 Formeln normalisiert und geprüft; 14 Fehlklassifikationen oder Wiederholungen ausgeschlossen; S. 36 ohne Rechenformel |
| ✅ ⚠️ | `R02` | S. 37–40 | 18 | Proportionen, tiefe Bundposition und gerader Bund | 10 Formelblöcke geprüft; 9 normalisiert, 1 wegen `BuW`/`BuU` gesperrt; 4 Fehlklassifikationen oder Wiederholungen ausgeschlossen |
| ✅ 🔎 | `R03` | S. 42–45 | 34 | Saumerweiterter Rock, Vollglocke und Halbglocke | 11 Formeln normalisiert; 10 Fehlklassifikationen, Eingabewerte oder Wiederholungen ausgeschlossen; Extraktionslücken auf S. 42/43 dokumentiert |
| ✅ 🔎 | `R04` | S. 46–48 | 12 | Glockenrock-Fortsetzung, Hosenrock und Kräuselweite | 6 Formelblöcke geprüft; 5 normalisiert, 1 wegen fehlender Bezugsgröße und Einheit offen; 6 Nachweis-, Bildverweis- oder Wiederholungszeilen ausgeschlossen; S. 46 ohne Rechenformel |
| ✅ 🔎 | `R05` | S. 51–57, 59, 60, 62 | 16 | Taillenvertiefung, Belege, Formbund, Passen und Miederbund | 1 Formel zur seitlichen Taillenvertiefung normalisiert; 15 Bildverweise, Konstruktionsanweisungen, Eingabebereiche oder Labels ausgeschlossen; Extraktionslücken dokumentiert |
| ✅ 🔎 | `R06` | S. 64–73, 78, 79 | 20 | Rock-Modellentwicklungen, Passenrock und Ballonrock | 2 Formeln normalisiert; 18 Konstruktions- und Produktionsregeln, Zuschnittbeschriftungen oder Quellenfoto-Zuordnungen ausgeschlossen; Extraktionslücken dokumentiert |
| ✅ ⚠️ | `R07` | S. 85–87, 92–97 | 28 | Faltenröcke und Produktionsschnitt | 8 Formelblöcke geprüft; 7 normalisiert, 1 wegen des Widerspruchs `504,8 cm`/`302,4 cm` gesperrt; 14 Fehlklassifikationen ausgeschlossen; Extraktionslücken dokumentiert |
| ✅ 🔎 | `H01` | S. 116–118, 120–123 | 25 | Standardhose, Produktionsschnitt und Taillenvertiefung | 15 Formeln normalisiert; 6 Wiederholungen, Produktionslabels oder Messbeschriftungen ausgeschlossen; Extraktionslücken dokumentiert |
| ✅ 🔎 | `H02` | S. 124–127 | 28 | Enge Hose | 14 Formelblöcke geprüft; 13 normalisiert, 1 wegen fehlendem geometrischem Referenten offen; 13 Wiederholungen, leere Tabellenzeilen oder Eingabewerte ausgeschlossen |
| ✅ ⚠️ | `H03` | S. 128–129 | 34 | Weitenreduzierte enge Hose für elastische Stoffe | 12 Formelblöcke geprüft; 8 normalisiert, 4 wegen fehlender Bezeichnungszeilen im Extrakt offen; 13 Wiederholungen, Labels oder Eingabewerte ausgeschlossen |
| ✅ ⚠️ | `H04` | S. 130–135, 137 | 32 | Bundfaltenhose und legere Hose | 14 Formelblöcke geprüft; 13 normalisiert, 1 wegen fehlendem Minuenden im Extrakt offen; 14 Eingabewerte, Wiederholungen oder Labels ausgeschlossen |
| ✅ 🔎 | `H05` | S. 140, 142–145 | 32 | Hosenbeine, Chinos und Karottenform | 5 Formeln normalisiert; 27 Bildverweise, Eingabewerte, Produktionsbeschriftungen oder Konstruktionslabels ausgeschlossen; Extraktionslücken dokumentiert |
| ✅ ⚠️ | `O01` | S. 172–175 | 29 | Oberteil-Typen, Balance und Figurkorrekturen | 11 Formelblöcke geprüft; 8 normalisiert, 3 wegen widersprüchlicher Skizzenrechnungen oder Vorzeichenkonflikt gesperrt; 15 Modell-, Bereichs-, Mess- oder Prüfzeilen ausgeschlossen; S. 172/173 ohne Rechenformel |
| ✅ ⚠️ | `O02` | S. 176–177 | 35 | Passformklassen, Zugaben und Konstruktionstabelle | 17 Formelblöcke geprüft; 16 normalisiert, 1 wegen fehlender Ausgangs- und Korrekturwerte offen; 6 Tabellenkopf-, Metadaten-, Prüf- oder Eingabezeilen ausgeschlossen; PK8-Kontextfehler, Bereichsauswahlen und Rundungen dokumentiert |
| ✅ ⚠️ | `O03` | S. 178–181 | 30 | Gemeinsames Grundgerüst aller Oberteil-Grundschnitte | 20 Formelblöcke geprüft; 17 normalisiert, 1 wegen fehlender Korrekturwerte offen, 2 Rechenwidersprüche bei `AIT+` und `½ BrW` gesperrt; 7 Kandidatenzeilen ausgeschlossen |
| ✅ ⚠️ | `O04` | S. 184–187 | 36 | Taillierter Oberteil-Grundschnitt mit und ohne Hüftausfall | 23 Formelblöcke geprüft; 18 normalisiert, 1 wegen fehlender Summanden offen, 4 widersprüchliche Taillen-/Hüftpfade gesperrt; 9 Kandidatenzeilen ausgeschlossen; S. 187 ohne Rechenformel |
| ✅ ⚠️ | `O05` | S. 194 | 28 | Weite an erprobtem Oberteil hinzufügen, Teil 1 | 8 Formeln normalisiert; 22 Kandidatenzeilen abgebildet, 6 Kontext-, Überschriften- oder Wiederholungszeilen ausgeschlossen; exakte und gedruckte ArD-Drittelwerte getrennt erhalten |
| ✅ ⚠️ | `O06` | S. 195 | 28 | Weite an erprobtem Oberteil hinzufügen, Teil 2 | 6 Formelblöcke geprüft; 4 normalisiert, 2 wegen widersprüchlicher Korrekturbeträge gesperrt; 5 Überschriften- oder Wiederholungszeilen ausgeschlossen |
| ✅ ⚠️ | `O07` | S. 196 | 29 | Weite am Oberteil reduzieren / Korsagenbezug | 6 Zugabedifferenzen normalisiert; 17 Kandidatenzeilen abgebildet, 12 Wiederholungs-, Kontext-, Überschriften- oder Zeichnungszeilen ausgeschlossen; beide Überschriften bezeichnen eine gemeinsame Methode |
| ✅ 🔎 | `A01` | S. 231–236 | 20 | Festliche Ärmel, Einnaht- und Zweinahtärmel | 2 Futterärmel-Formeln auf S. 235 normalisiert; 7 Kandidatenzeilen abgebildet, 13 Produktions-, Zuschnitt-, Eingabe- oder Wiederholungslabels ausgeschlossen; übrige Seiten ohne extrahierte Rechenformeln |
| ✅ 🔎 | `A02` | S. 237–240 | 33 | Blazerärmel, Schlitze und Futterschnitte | 2 Formelblöcke geprüft; Mindestabstand normalisiert, zwei unbezeichnete Additionen offen; 30 Produktions-/Zuschnittlabels, Wiederholungen oder Linienbezeichnungen ausgeschlossen; S. 238/239 ohne neue Formel |
| ✅ | `K03` | S. 306 | 2 | Volantkragen an Rund- und V-Ausschnitt | 2 Teilungsformeln normalisiert; Nenner `13` und `17` sowie die Anteile `1/13`, `2/13`, `1/17` und `2/17` geprüft; keine Kandidaten ausgeschlossen |
| ✅ 🔎 | `M01` | S. 368–369 | 19 | Eingeschnittene Taschen | 2 Formeln normalisiert; 17 Kandidaten als Produktions-/Zuschnittbeschriftungen, Bildverweis, direkte Maßübertragung oder Wiederholung ausgeschlossen; geometrische Extraktionslücke dokumentiert |
| ✅ 🔎 | `M02` | S. 371, 375–377, 379, 380, 382–387 | 18 | Oberteil-Modellentwicklung und Englische/Wiener Nähte | 4 Formelblöcke geprüft; 3 normalisiert, 1 wegen fehlender Bezeichnungszeile offen; 13 Konstruktions-, Bildverweis-, Wiederholungs- oder Provenienzzeilen ausgeschlossen |
| ✅ 🔎 | `M03` | S. 390–396, 398, 400, 401 | 17 | Teilungsnähte, Sakkoabnäher und körpernahe Oberteile | 2 Saumerweiterungsformeln auf S. 391 normalisiert; 3 Kandidatenzeilen abgebildet, 14 Bildverweis-, Methoden-, Eingabe-, Mess- oder Provenienzzeilen ausgeschlossen; übrige Seiten ohne extrahierte Rechenformeln |
| ✅ 🔎 | `M04` | S. 406, 407, 409–412, 414–416 | 24 | Kleidformen, Wickel-Form, Abnäherflächen und Ausschnittoptimierung | 1 Verdopplungsformel auf S. 409 normalisiert; 1 Kandidatenzeile abgebildet, 23 Provenienz-, Bildverweis-, Methoden-, Produktions-, Übertragungs- oder Beschriftungszeilen ausgeschlossen; übrige Seiten ohne extrahierte Rechenformeln |
| ✅ 🔎 | `M05` | S. 426, 427, 429–432, 434 | 21 | Quer-Teilungsnähte, Belege, tiefe Dekolletés, Blenden und Wasserfall | keine Rechenformel im extrahierten Bestand; 21 Produktions-/Zuschnittlabels, Definitionen, Bildverweise, direkte Übertragungen oder redaktionelle Beschreibungen ausgeschlossen; Extraktionslücke auf S. 434 dokumentiert |
| ✅ 🔎 ⚠️ | `M06` | S. 438–439 | 5 | Kleidformen-Übersicht und Baukasten | keine Rechenformel; 1 Provenienzzeile und 4 Bildnummernverweis-Zeilen einschließlich Wiederholungen der Zweitfassung ausgeschlossen; maßgebliche digital geprüfte Erstfassung verwendet |
| ✅ 🔎 | `M07` | S. 452–461 | 33 | Empire-, Etui-, Säulen- und weitere Kleidmodelle | 1 Formel zum Unterbrustnaht-Abstand normalisiert; 1 Kandidatenzeile abgebildet, 32 Produktions-, Verweis-, Provenienz-, Methoden- oder Eingabezeilen ausgeschlossen; Auswahlregel nach Brustgröße und Extraktionslücken dokumentiert |
| ✅ 🔎 | `M08` | S. 475, 476, 478–482 | 32 | Blazer, Belege und Futterentwicklung | 2 ergänzende Formeln zur Belegnahtverlängerung und Faltentiefe normalisiert; 2 Kandidatenzeilen abgebildet, 30 Bildverweis-, Produktions-, Methoden-, Eingabe-, Nahtzugaben- oder Wiederholungszeilen ausgeschlossen; Extraktionslücken dokumentiert |
| ✅ 🔎 | `M09` | S. 484–486 | 56 | Blazer-Produktionsschnitt, Materialliste und Mantelbeginn | keine Rechenformel; 56 Verifikations-, Modell-, Produktions-, Material-, Stückzahl-, Notations- oder Verweiskandidaten ausgeschlossen; Extraktionslücke auf S. 486 dokumentiert |
| ✅ ⚠️ | `Z01` | S. 537, 539 | 16 | Konstruktionstabellen und Produktionsschnitt-Anhang | 10 allgemeine Oberteil-Formeln normalisiert; 12 Kandidatenzeilen abgebildet, 4 Feld-/Provenienzzeilen ausgeschlossen; S. 539 ohne Rechenformel |

### Vollständigkeits- und Übergaberegel

- Die oben genannten Seiten entsprechen exakt den 183 Einträgen mit Herkunft `v1`
  in `../hofenbitzer_band_1_digital/00_index_formeln_band_1.md`; keine v1-Quelldatei
  ist außerhalb einer Tranche.
- Nicht vorhandene Zwischenseiten sind keine Lücke dieser Karte: Im
  Extraktionsindex gibt es für sie keine Formeldatei.
- Nach einer Tranche wird ihr Status hier und der konkrete Zielbestand in
  `00_index_normalisierte_formeln_band_1_v1.md` aktualisiert.
- Bei Teilabschluss bleibt die Tranche `🟡`; eine Folgesession setzt genau dort
  fort. Erst nach Quellenvergleich und Qualitätsprüfung wird sie `✅`.
- **Nächste Tranche: keine** — alle 183 kartierten Formeldateien sind bearbeitet.
  Als nächster Arbeitsschritt folgt die Gesamtprüfung der Variablen,
  Abhängigkeiten und offenen Stellen, sofern Werner sie beauftragt.
