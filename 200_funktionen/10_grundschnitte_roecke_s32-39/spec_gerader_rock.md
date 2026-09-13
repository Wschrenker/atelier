# Spec — Gerader Rock, nähfertig

> **Stand:** Entwurf vom 2026-09-13, Fragerunde mit Werner.
> Entscheidungen von Werner sind mit **(W)** markiert. Alles ohne (W) ist ein
> Vorschlag und gilt erst, wenn Werner es bestätigt.

## 1. Ziel

Aus vier Körpermaßen einen nähfertigen geraden Rock mit Bund erzeugen, der
als Probeteil aus Nessel genäht und von einer Schneiderin beurteilt wird. **(W)**

Reihenfolge **(W)**:

1. Buchbeispiel rechnen und ausgeben (vergleichbar mit dem Buch).
2. Dieselbe Rechnung mit den Maßen einer echten Person; die Schneiderin misst. **(W)**

## 2. Umfang

| Gehört dazu | Quelle |
|---|---|
| VT und RT, erhöhte Taille **(W)** | S. 32–35 |
| Abnäher, Hüftbogen, Taillennaht | S. 34–35 |
| Nahtzugaben, Saumeinschlag, Markierungen, Beschriftung | S. 36, ab S. 22 **(W)** |
| Gerader Bund, nur S. 39 **(W)** | S. 39 |

| Gehört **nicht** dazu | Grund |
|---|---|
| Rock an natürlicher Taille S. 38 | **(W)** erst später |
| Gehschlitz | **(W)** erst ohne, Nessel zeigt es |
| Bund-Folgeseiten S. 40–41 (Übertritt, Knopf) | **(W)** nur S. 39 |
| Produktionsfreigabe, Brautkleid | eigenes Thema |

## 3. Eingang

### Körpermaße (Pflicht, in cm)

| Maß | Buchbeispiel |
|---|---|
| Hüftumfang HüU | 97 |
| Taillenumfang TaU | 72 |
| Hüfttiefe | 21 |
| Modelllänge | 50 |

### Wahlwerte

Regel **(W)**: Jeder Wahlwert hat einen Standard und kann für eine Person
bewusst überschrieben werden. Jede Überschreibung steht sichtbar im Ergebnis.

Erlaubter Bereich **(W)**: Was irgendeine Buchseite erlaubt, ist erlaubt. Die
Tabelle auf S. 33 ist ein Beispiel und keine Sperre.

| Wahlwert | Standard | Herkunft Standard | Erlaubt (alle Buchstellen zusammen) |
|---|---|---|---|
| Hüftzugabe | 3 cm | Buchbeispiel S. 33 | 2–3 cm |
| Taillenzugabe | 2 cm | Buchbeispiel S. 33 | 1–2 cm |
| Taillenerhöhung Seitenlinie | 1 cm | S. 34, normale Hüftrundung | 1–1,5 cm |
| Taillenerhöhung vorderer Abnäher | 0,5 cm | S. 34 | 0,5–0,7 cm |
| Taillenerhöhung hinterer Abnäher | ⅓ der Seitenlinie | S. 34 | 0,3–0,5 cm |
| Hüftabstich | ½ TaAf (= 6,5 cm) | Buchbeispiel S. 33/34 | ½ TaAf ± 0 bis 1,5 cm (S. 33, 34, 37) |
| Vorderer Abnäherinhalt | 2,5 cm | Buchbeispiel S. 33/34 | 0 oder 1–2,5 cm (S. 33, 34) |
| Hinterer Abnäherinhalt | Rest (= 4 cm) | S. 34 | Rest; erster hinterer höchstens 4,5 cm |
| Anzahl RT-Abnäher | nach Regel unten | S. 34/35/37 **(W)** | 1 oder 2 |
| Vordere Abnäherlänge | 9 cm | Vorschlag: Bereichsmitte | 8–10 cm |
| Hintere Abnäherlänge (1.) | 14,5 cm | Vorschlag: Bereichsmitte | 13–16 cm |
| Zweite hintere Abnäherlänge | 13 cm | Vorschlag: Bereichsmitte | 12–14 cm |
| Inhaltsdifferenz 1./2. RT-Abnäher | 0,5 cm | Vorschlag: untere Grenze | 0,5–1 cm |
| Positionskorrektur 1. RT-Abnäher | 0 cm | Vorschlag | 0–1 cm |
| Nahtzugabe | 1,5 cm | **(W)** | 1–3 cm (S. 36) |
| Saumeinschlag | 3 cm | **(W)** | 2–5 cm (S. 36) |
| Bundbreite | 4 cm | **(W)** | 2–5 cm (S. 39) |
| Taillenkurve, Hüftbogenform | fester Standard | **(W)** Nessel entscheidet | eigene Kurvenfamilie, keine Buchformel |

Regel RT-Abnäher **(W)**: Automatisch zwei, wenn der hintere Rest mehr als
4,5 cm beträgt (S. 34). Bei weniger darf man bewusst zwei wählen (S. 37).

Der Standard für Taillenkurve und Hüftbogen wird beim ersten Durchlauf aus der
[Kurvenansicht](03_rueckteil_mit_zwei_abnaehern_s35/02_schnitt_fertigstellen_s35/kurvenansicht.html)
gewählt und hier eingetragen: `durchhang_mm = ___`, `hueftform = ___`.

## 4. Ablauf

Die vorhandenen Bausteine werden benutzt, nicht neu geschrieben. Wo ein
Baustein dem Ablauf widerspricht, wird der Baustein angepasst und der
Widerspruch in Abschnitt 8 notiert.

| Nr. | Schritt | Baustein | Stand |
|---|---|---|---|
| 1 | Konstruktionstabelle: Weiten, TaAf | [konstruktionstabelle.py](01_gerader_rock_konstruktionstabelle_und_grundgeruest_s32-33/01_konstruktionstabelle_erstellen_s32-33/konstruktionstabelle.py) | da, Grenzen zu eng |
| 2 | Grundgerüst P1–P9 | [grundgeruest.py](01_gerader_rock_konstruktionstabelle_und_grundgeruest_s32-33/02_grundgeruest_zeichnen_s33/grundgeruest.py) | da |
| 3 | Taillenerhöhung P10 | [taillenlinien_erhoehen.py](02_abnaeher_positionieren_s34/01_taillenlinien_erhoehen_s34/taillenlinien_erhoehen.py) | da |
| 4 | Hüftabstich (Figurform) | [hueftabstich.py](05_proportionen_huefte_und_taille_s37/01_hueftabstich_nach_proportionen_berechnen_s37/hueftabstich.py) | in Arbeit |
| 5 | Taillenausfall aufteilen | [taillenausfall_aufteilen.py](02_abnaeher_positionieren_s34/02_taillenausfall_aufteilen_s34/taillenausfall_aufteilen.py) | da |
| 6 | Hüftbogenpunkte, VT-Abnäher, 1 RT-Abnäher | [hueftbogen_und_abnaeher.py](02_abnaeher_positionieren_s34/03_hueftbogen_und_abnaeher_zeichnen_s34/hueftbogen_und_abnaeher.py) | da, stoppt bei > 4,5 cm |
| 7 | oder: zwei RT-Abnäher | [zwei_hintere_abnaeher.py](03_rueckteil_mit_zwei_abnaehern_s35/01_zwei_hintere_abnaeher_konstruieren_s35/zwei_hintere_abnaeher.py) | da |
| 8 | Taillennaht, Hüftbogen, Kontur VT/RT | [grundkontur.py](03_rueckteil_mit_zwei_abnaehern_s35/02_schnitt_fertigstellen_s35/grundkontur.py) | Arbeitsfassung |
| 9 | Abnäher schließen, Taillennaht ausgleichen | – | fehlt |
| 10 | Bund: Rechteck, vM/hM/SN, Taillenmehrweite | – | fehlt (S. 39) |
| 11 | VT an vM spiegeln (Bruch) | [vt_spiegeln.py](04_abnaeherformen_schablone_und_produktionsschnitt_s36/03_produktionsschnitt_vorbereiten_s36/vt_spiegeln.py) | da |
| 12 | Nahtzugaben, Saum, Markierungen, Beschriftung | – | fehlt (S. 36, ab S. 22) |
| 13 | Ausgabe SVG, PDF, DXF | – | fehlt |

Alles läuft über **eine** Funktion, die Körpermaße und Wahlwerte nimmt und
alle Teile zurückgibt. Kein Schritt setzt Werte von Hand ein, die ein
früherer Schritt ausrechnet.

## 5. Schnittteile

| Teil | Zuschnitt | Verschluss / Besonderheit |
|---|---|---|
| VT | 1x Oberstoff, vM im Bruch (S. 36) | – |
| RT | 2x paarig Oberstoff (S. 36) | – |
| Seitennaht | – | RV in der Seitennaht **(W)**, Bild S. 36 |
| Bund | nach S. 39 | Verschluss an der SN, siehe O1 |

Beschriftung je Teil nach S. 36: Teilname, Zuschnittanzahl, Stoff, Name, Datum,
Hüftlinie eingezeichnet.

## 6. Ausgabe **(W)**

- **SVG**: Ansicht, maßstäblich in mm.
- **PDF**: 1:1 auf A4 zum Zusammenkleben, mit Klebemarken und
  10-cm-Prüfquadrat. **(W)**
- **DXF-AAMA**: zum Einlesen in CLO, mit Teilen, Knipsen und Fadenlauf. **(W)**
- Dazu eine Textdatei mit allen Maßen, Wahlwerten, Überschreibungen und
  Prüfergebnissen (die „Konstruktionstabelle zum Aufkleben“, S. 36).

## 7. Abnahme

### Digital (vor dem Nähen)

- Kontrollsumme: Hüftabstich + alle Abnäher = TaAf (S. 33–35).
- Taillenmehrweite = vTaN + hTaN − TaU : 2 liegt bei 1–1,5 cm; über 1,5 cm ist
  ein Fehler (S. 39).
- VT- und RT-Seitennaht sind gleich lang.
- PDF-Prüfquadrat misst ausgedruckt 10 cm.
- Buchbeispiel: Ausdruck liegt auf der Zeichnung S. 35 (Maßstab umgerechnet).

### Nessel **(W)**

Probeteil nähen und von der Schneiderin anschauen lassen. Beobachtungspunkte:

- Sitz an Taille, Hüfte, Gesäß; Seitennaht senkrecht.
- **Seitennaht oben:** Taille und Hüftbogen treffen sich zurzeit mit etwa 64°
  statt 90°. Gibt das eine Spitze in der Taille? **(W)** Nessel entscheidet.
- Form von Taillennaht und Hüftbogen (Standardkurve aus Abschnitt 3).
- Bund: Weite, Einhalteweite.

Ergebnis wird hier eingetragen, mit Datum und was geändert wurde.

## 8. Offene Punkte und bekannte Widersprüche

| Nr. | Punkt | Wer klärt |
|---|---|---|
| O1 | RV sitzt in der SN **(W)**, wie im Bild S. 36 und in der [README S. 36](04_abnaeherformen_schablone_und_produktionsschnitt_s36/03_produktionsschnitt_vorbereiten_s36/README.md). Der Bund auf S. 39 ist aber für einen Verschluss an der hM gezeichnet (Bund-Enden = hM). Wie der Bund bei RV in der SN aussieht (Enden an der SN statt hM), steht nicht auf S. 39. | Werner am Buch |
| O2 | Schritt 17 „TaU : 10“: Körpermaß TaU (72) oder Taillenweite TaW (74)? Das Arbeitsbeispiel benutzt 74. | Werner am Buch |
| O3 | Bund-Zuschnitt: S. 39 gibt nur die fertige Bundform. Doppelt gelegt, Einlage, Übertritt fehlen, weil S. 40–41 nicht dazugehören. Für ein nähfertiges Teil nötig. | Werner / Schneiderin |
| O4 | Markierungen „ab S. 22“: Seiten noch nicht für diesen Rock gelesen. | vor Schritt 12 |
| O5 | Prüfstellen S. 37 (F01, F02): Wahl des Betrags innerhalb des Bereichs. Durch „Standard + überschreibbar“ beantwortet, sobald Werner das bestätigt. | Werner |
| O6 | Grenzen in konstruktionstabelle.py (±1 cm, vorderer Abnäher ab 1,5 cm, 2. RT-Abnäher = 0) und hueftbogen_und_abnaeher.py (Stopp > 4,5 cm) passen nicht zu Abschnitt 3. | beim Zusammenbau |
| O7 | Standards mit „Vorschlag“ in Abschnitt 3 sind nicht bestätigt. | Werner |
| O8 | Ecken an vM/hM und Abnäher schließen (Schritt 9): kein Buchtext dazu gelesen. | vor Schritt 9 |
