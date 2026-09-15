# Spec — Gerader Rock

## Ziel

Aus Körpermaßen und bewussten Wahlwerten einen modular aufgebauten geraden Rock mit Bund erzeugen. Zuerst wird das Hofenbitzer-Buchbeispiel gerechnet und ausgegeben, danach ein Schnittmuster für eine reale Person.

## Umfang

**Enthalten:**

- Vorder- und Rückteil mit erhöhter Taille, Abnähern, Hüftbogen und Taillennaht nach S. 32–35;
- Produktionsschnitt mit Nahtzugaben, Saum, Markierungen und Beschriftung nach S. 36 und den dafür benötigten Grundregeln;
- Proportionsregeln nach S. 37;
- gerader Bund nach S. 39;
- Ausgabe als DXF, SVG und maßstäbliche PDF.

**Nicht enthalten:** Rock an natürlicher Taille S. 38, Rockmodelle ab S. 40, Gehschlitz und Produktionsfreigabe.

## Eingaben

| Körpermaß | Buchbeispiel |
|---|---:|
| Hüftumfang `HüU` | 97 cm |
| Taillenumfang `TaU` | 72 cm |
| Hüfttiefe | 21 cm |
| Modelllänge | 50 cm |

Wahlwerte besitzen einen belegten Standard und dürfen bewusst überschrieben werden. Jede Überschreibung muss im Ergebnis sichtbar bleiben; fehlende Körpermaße werden nicht geschätzt.

## Modulare Konstruktion

Vorhandene Bausteine werden verbunden und bei nachgewiesenem Bedarf korrigiert, nicht grundlos neu geschrieben:

1. Konstruktionstabelle und Taillenausfall;
2. Grundgerüst;
3. Taillenerhöhungen;
4. Hüftabstich und Verteilung des Taillenausfalls;
5. Hüftbogen und Abnäher;
6. ein oder zwei hintere Abnäher;
7. Taillennaht, Kurven und Grundkontur;
8. Produktionsschnitt und Spiegelung;
9. Bund;
10. Nahtzugaben, Saum, Markierungen und Beschriftung;
11. gemeinsame Prüfung und Ausgabe.

Jeder Baustein erhält einen kleinen Vertrag mit:

- fachlichem Zweck und verifizierter Quelle;
- Eingaben, Ausgaben und interner Einheit;
- verwendeten Mathematikverträgen;
- Abhängigkeiten und benannten Anschlussstellen;
- Fehlerfällen und technischen Tests.

Ein späterer Schritt übernimmt berechnete Ergebnisse über diese Anschlüsse; er setzt keine Ergebnisse früherer Schritte von Hand neu ein. Eine übergeordnete Rockfunktion verbindet die Module und gibt vollständige Schnittteile zurück. DXF, SVG und PDF verwenden dieselbe geprüfte Geometrie.

## Vollständiger Pilotauftrag

Der erste durchgängige Referenzauftrag verbindet das Personenprofil aus dem Messmodul mit der Auswahl aus dem Patchwork-Dashboard:

| Herkunft | Typ | ID | Wert an der Engine-Grenze |
|---|---|---|---:|
| Messmodul | `MeasurementValue` | `waist_circumference_horizontal` | 720 mm |
| Messmodul | `MeasurementValue` | `hip_circumference_horizontal` | 970 mm |
| Messmodul | `MeasurementValue` | `waist_to_hip` | 210 mm |
| Dashboard | `ChoiceValue` | `garment` | `straight_skirt` |
| Dashboard | `ChoiceValue` | `model_length` | 500 mm |
| Dashboard | `ChoiceValue` | `waistband` | gewählt |
| Dashboard | `ChoiceValue` | `zipper_position` | hintere Mitte |
| Engine | automatische Regel | `darts` | automatisch berechnen |

Die `bridal_engine_v2` erhält daraus einen versionierten `ModuleRequest`. Erwartet wird ein validierter `ModuleResult` mit Vorderteil, Rückenteil und Bund, gemeinsamer Provenienz und sichtbaren Fehlerzuständen. Der Reißverschluss wird erst Bestandteil des Ergebnisses, wenn sein eigener belegter Codebaustein vorhanden und angeschlossen ist; bis dahin darf das Dashboard ihn nicht anbieten.

## Schnittteile und Ausgabe

- Vorderteil: im Bruch;
- Rückteil: paarig;
- gerader Bund;
- Nahtlinie und Schnittlinie getrennt;
- Fadenlauf, Knipse, Teilname, Zuschnittangabe und verwendete Maße/Wahlwerte;
- SVG in Millimetern, PDF 1:1 mit Prüfquadrat und DXF-AAMA für CLO.

## Technische Abnahme

- Hüftabstich und Abnäher ergeben zusammen den Taillenausfall.
- Vorder- und Rückteil passen an ihren vorgesehenen Nähten zusammen.
- Konturen sind endlich, geschlossen und ohne still erzeugte Ersatzpunkte.
- Das Buchbeispiel ist reproduzierbar.
- Alle Modul- und Verbindungstests bestehen.
- SVG, PDF und DXF beruhen auf demselben berechneten Stand.
- Das PDF-Prüfquadrat misst ausgedruckt 10 cm.

Technische Tests beweisen keine Passform. CLO, Nessel, Anprobe und fachliche Annahme bleiben getrennte Prüfungen.

## Offene Fachpunkte

Diese Punkte werden vor dem jeweils abhängigen Modul geklärt:

- Bundlösung bei Reißverschluss in der Seitennaht;
- Bedeutung von „TaU : 10“ auf S. 39: Körpermaß oder berechnete Taillenweite;
- nähfertiger Bundaufbau, soweit S. 39 ihn nicht beschreibt;
- benötigte Markierungs- und Beschriftungsregeln ab S. 22;
- bestätigte Standards für Abnäherlängen, Taillenkurve und Hüftbogen;
- fachliche Regel für geschlossene Abnäher und ausgeglichene Taillennaht.
