# Tabellen s031 (OCR-Rohfassung)

Aus dem Layout-JSON der Mistral-OCR (`ocr_s031_raw.json`, Blöcke `tbl-0` und
`tbl-1`).

## tbl-0 – Punkt- und Linien-Namen auf Schablonen und Schnittteilen

|  VM | vordere Mitte | vAp | vorderer Ärmelpunkt  |
| --- | --- | --- | --- |
|  hM | hintere Mitte | hAP | hinterer Ärmelpunkt  |
|  SN | Seitennaht | tP | tiefster Punkt  |
|  BU | Brustlinie | SuP | Schulterpunkt  |
|  UT | Übertritt | Reb | Reversbruch  |
|  UT | Untertritt | Krb | Kragenbruch  |
|  RV | Reißverschluss(-ende) | StKa | Schlitzkante  |

**Auffällig (noch nicht bestätigt):** Die OCR gibt mehrere Sonderzeichen als
„�“ (nicht erkanntes Zeichen) wieder, vermutlich Ä/Ü/ß. Außerdem führt die
Tabelle die Kürzel „VM“ (statt vermutlich „vM“) und zweimal „UT“ (einmal für
„Übertritt“, einmal für „Untertritt“ – vermutlich müsste die erste Zeile „ÜT“
heißen) sowie „StKa“ (vermutlich „SlKa“ für Schlitzkante). Am Original zu
prüfen.

## tbl-1 – Schnittteilliste (Kopfzeile und alle 31 Zeilen)

|  Schnittteilleiste |   |   | Modell | Toscana 035  |   |   |
| --- | --- | --- | --- | --- | --- | --- |
|   | Kollektion | HW-2026 | Bearbeiter | Andrea Muster | Datum | 02.08.2024  |
|  Nr. | Schnittteilname |   | Material | Name Intern | Farbe | No. Intern Anzahl  |
|  1. | Vorderteil |   | OSt.1, El.1 |  |  | 2x-p  |
|  2. | Seitenteil |   | OSt.1, El.1 |  |  | 2x-p  |
|  3. | RT-Passe |   | OSt.1, El.2 |  |  | 1x  |
|  4. | Rückteil |   | OSt.1 |  |  | 2x-p  |
|  5. | Unterärmel |   | OSt.1 |  |  | 2x-p  |
|  6. | Oberärmel |   | OSt.1 |  |  | 2x-p  |
|  7. | VT-Beleg |   | OSt.1, El.2 |  |  | 2x-p  |
|  8. | RT-Beleg |   | OSt.1, El.2 |  |  | 1x  |
|  9. | Oberkragen |   | OSt.2, El.2 |  |  | 1x  |
|  10. | Unterkragen |   | OSt.2, El.2 |  |  | 2x-p  |
|  11. | Kragensteg |   | OSt.2, El.2 |  |  | 2x  |
|  12. | Taschenspiegel |   | OSt.1 |  |  | 2x-p  |
|  13. | Paspelstreifen |   | OSt.2 |  |  | 4x  |
|  14. | VT-Futter |   | Fu.1 |  |  | 2x-p  |
|  15. | ST-Futter |   | Fu.1 |  |  | 2x-p  |
|  16. | RT-Futter links |   | Fu.1 |  |  | 1x  |
|  17. | RT-Futter rechts |   | Fu.1 |  |  | 1x  |
|  18. | v-Armel-Futter |   | Fu.2 |  |  | 2x-p  |
|  19. | h-Armel-Futter |   | Fu.2 |  |  | 2x-p  |
|  20. | v-Taschenbeutel |   | Fu.3 |  |  | 2x-p  |
|  21. | h-Taschenbeutel |   | Fu.3 |  |  | 2x-p  |
|  22. | v-Armelkugel |   | El.3 |  |  | 2x-p  |
|  23. | h-Armelkugel |   | El.3 |  |  | 2x-p  |
|  24. | ST-Armloch |   | El.3 |  |  | 2x-p  |
|  25. | RT-Armloch |   | El.3 |  |  | 2x-p  |
|  26. | ST-Saum |   | El.2 |  |  | 2x-p  |
|  27. | RT-Saum |   | El.2 |  |  | 2x-p  |
|  28. | RT-Schlitz |   | El.2 |  |  | 2x-p  |
|  29. | Plack 1 |   | El.4 |  |  | 2x-p  |
|  30. | Plack 2 |   | El.4 |  |  | 1x  |
|  31. | Bügelschablone Kantenabstich |   | Pappe |  |  |   |

**Auffällig (noch nicht bestätigt):**

- Kopfzeile: Die OCR fasst „No. intern“ und „Anzahl“ (laut Foto zwei
  getrennte Spalten) zu einer Zelle „No. Intern Anzahl“ zusammen. Am Original
  zu prüfen, ob die Spaltenaufteilung dadurch verschoben wurde.
- **Anzahl-Spalte ab Zeile 9 wirkt um eine Zeile verschoben:** Beim optischen
  Abgleich mit dem Foto passt ab Zeile 9 („Oberkragen“) jeder OCR-Wert der
  Anzahl-Spalte zum Schnittteil der jeweils vorigen Zeile, nicht zur eigenen
  Zeile (z. B. OCR-Zeile 9 „1x“ wirkt wie der Wert von Zeile 8 „RT-Beleg“,
  OCR-Zeile 13 „4x“ wie der Wert von Zeile 12 „Taschenspiegel“). Für Zeile 31
  „Bügelschablone Kantenabstich“ bleibt dadurch kein Anzahl-Wert übrig – im
  Foto ist diese Zelle ohnehin leer. Zeilen 1–8 zeigen dieses Muster nicht.
  Am Original zu prüfen, ob es sich um einen OCR-Lesefehler oder eine
  tatsächliche Verschiebung im Layout handelt.
- Zeilen 30/31, Spalte „Material“: Die OCR ordnet „El.4“ Zeile 30 („Plack 2“)
  und „Pappe“ Zeile 31 („Bügelschablone Kantenabstich“) zu. Im Fotoeindruck
  wirkt „Pappe“ dagegen schon bei Zeile 30 vermerkt und Zeile 31 materiallos.
  Am Original zu prüfen.
- Zeilen 25 und 28, Spalte „Material“ („El.3“/„El.2“ bzw. „El.2“/„El.4“): Im
  Fotoeindruck wirken die Werte gegenüber der OCR vertauscht. Am Original zu
  prüfen.
