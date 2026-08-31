> **STATUS: H PUNKTE 1–3 + ENGINE-ENTSCHEID PUNKT 4 (2026-07-05, Werner-#).** Werner hat die Punkte 1–3 am Originalbuch H-freigegeben: Li26-Formel, volle Brustabnäher-Drehung und hintere Abnäher-Längen inklusive Engine-Mittwerte. Punkt 4 ist ausdrücklich **kein Buch-H**, sondern eine quellenbegründete `modelDecision`: begrenzte Proportionsverteilung für TaAf 3–9 cm; außerhalb ist eine andere Variante nötig.
> Quelle: S.184–186. D (digital fototreu) durch Claude/Opus am Originalfoto `20260618_185606.jpg` (S.184) + `20260618_185613.jpg` (S.185) am 2026-07-03 zweitgeprüft. Baut auf der freigegebenen Grundgerüst-Spec (`s172-187_oberteil-grundgeruest_ENTWURF.md`, H Werner 2026-06-27) auf.
>
> **Was seit dem ENTWURF geklärt wurde (D 2026-07-03; H 2026-07-05):**
> 1. **H Werner: Li26 = BrU : 20 + 1 cm** — die Roh-Lesung „BrU:20 ≈ 1 cm" war ein Lesefehler; das Foto liest eindeutig „maximal / BrU:20 / +1 cm" (Abschnitt 4).
> 2. **H Werner: Brustabnäher-Default voll bis Li26 drehen** (max. Brustformung, engstes Armloch).
> 3. **H Werner: □8c-Abnäher-Zuordnung und Längen** — shAbl 12–14 cm, hAbl 14–16 cm; Engine-Mittwerte 13/15 cm (Abschnitt 7).
> 4. **Engine-Entscheid Werner-# 2026-07-05, kein Buch-H:** Proportion `2 : 2 : 2,8` innerhalb TaAf 3–9 cm begrenzt auf die Buchbereiche verteilen; außerhalb stoppen/Variantenweg verlangen. `shAbl → 0` ist keine automatische Klein-TaAf-Regel, sondern nur eine ausdrücklich gewählte andere Konstruktion/Variante.

# Oberteil-Abnäher S.184–186 — konsolidierte Spec (Freigabe-Kandidat)

## 1. Status & Scope

Diese Spec beschreibt ausschließlich die **Brustabnäher-Öffnung** sowie die **Taillen- und Hüftabnäher** des taillierten Oberteil-Grundschnitts (mit Hüftausfall, S.184–185). Sie wiederholt das Grundgerüst nicht. Die Variante *ohne* Hüftausfall (S.186) ist als Referenz-/Testfall dokumentiert (Abschnitt 8.2), aber **nicht** das v1-Bau-Ziel — zuerst wird die S.184–185-Variante gebaut (in sich rechnerisch geschlossen, Golden-tauglich).

Baut auf: Grundgerüst bis P31 / BrP + Brustabnäher-Linie (freigegeben). Diese Spec erzeugt daraus die Öffnung/Formung.

## 2. Anknüpfung an das freigegebene Grundgerüst

*Quelle: Grundgerüst-Spec nach S.181; Weiterentwicklung auf S.184–186.*

| Gegeben aus dem Grundgerüst | Verwendung hier | Quelle |
|---|---|---|
| BrP und Brustabnäher-Linie | Lage/Achse fest; hier erst Öffnung/Formung. | S.181, S.184 |
| vSuP, vSuP1, vAP, hAP, P17, P18 | Bezugspunkte Brustabnäher, Armloch, Schulterabnäher, Knips. | S.181, S.184–186 |
| vordere/hintere Armlinie | Bezug für Li26, Taillenabtrag, hintere Abnähermitte. | S.181, S.184–186 |
| Taillenlinie, Hüftlinie | Ausgangslinien für Erhöhung, Abnäher, Hüftausfall, Hüftbreiten. | S.179, S.184–186 |
| vM, hM | Begrenzen die gemessenen vorderen/hinteren Breiten. | S.179–181, S.184–186 |
| SN / Seitenlinien | Aufnahme eines Teils des TaAf; Ausstellen des HüFb. | S.184–186 |
| `½ TaW`, `½ HüW` | Kontrollwerte aus der Konstruktionstabelle; nicht neu herleiten. | S.184–186 |

## 3. Maß-Glossar (Abnäher)

*Längen/Umfänge in cm; PK einheitenlos.*

| Kürzel | Klartext | Quelle |
|---|---|---|
| BrU | Brustumfang (Körpermaß) | S.184 |
| TaU / TaW | Taillenumfang (Körper) / Taillenweite (Modell); halb = `½ TaW` | S.184–186 |
| HüU / HüW | Hüftumfang / Hüftweite; halb = `½ HüW` | S.185–186 |
| me | gemessene Reststrecke vom Ende des `¼ TaU`-Abtrags zur vM | S.184 |
| vAbl | vorderer Taillenabnäher-Inhalt | S.184–186 |
| shAbl | seitlicher hinterer Abnäher-Inhalt | S.185–186 |
| hAbl | hinterer Abnäher-Inhalt (an der hinteren Abnähermitte) | S.185–186 |
| TaB (vTaB/hTaB) | gemessene Taillenbreite (vorn/hinten), Summe = TaB | S.184–186 |
| TaAf | Taillenausfall; `TaB − ½ TaW` | S.184–186 |
| HüAf | Hüftausfall im VT (bes. Abnäherinhalt); `vAbl − 2 cm` | S.185 |
| HüB (vHüB/hHüB) | gemessene Hüftbreite (vorn/hinten), Summe = HüB | S.185–186 |
| HüFb | Hüftfehlbetrag; `HüB − ½ HüW` (Betrag verwenden) | S.185–186 |
| Li26 | Hilfs-/Grenzlinie aus Schritt ㉖ für die max. Brustabnäher-Drehung | S.184 |
| BrP, vSuP1/vSuP2, hAP, hintere Abnähermitte | Konstruktionspunkte/-linien | S.184–186 |

## 4. Brustabnäher-Öffnung — **GEKLÄRT**

*Quelle: S.184, Abschnitt ❼ + Abbildung □8b; Foto-D 2026-07-03; H Werner 2026-07-05.*

Die Grundgerüst-Spec endet bei BrP + Brustabnäher-Linie. Hier entsteht daraus die Öffnung durch **Drehung eines Dreiecks um BrP**:

| Schritt | Handlung | Wert | Ergebnis |
|---:|---|---|---|
| ㉕ | Vom vSuP1 Hilfslinie zum BrP → Dreieck. | — | Dreieck vSuP1–BrP |
| ㉖ | **Li26** = senkrechte Grenzlinie im Abstand **`BrU : 20 + 1 cm`** rechts der vorderen Armlinie anzeichnen. | Bsp. BrU 88 → `88:20 + 1 = 4,4 + 1 = 5,4 cm` | Li26 |
| ㉗ | Dreieck um BrP drehen, vSuP1 **maximal bis Li26** anlegen → vSuP2. (Alternativ bei BrP einschneiden und bis Li26 falten.) | Drehzentrum BrP, Grenze Li26 | geöffneter Brustabnäher, neue Lage vSuP2 |

**⚠️ Korrektur gegenüber der Roh-Transkription:** Diese hatte „BrU : 20 ≈ 1 cm" und markierte selbst, dass sie Formel und Abstand nicht binden kann. Das Original-Label in □8b liest über drei Zeilen **„maximal / BrU:20 / +1 cm"** (Foto `20260618_185606.jpg`, Zoom bestätigt). Richtig ist also **`BrU:20 + 1 cm`**, nicht „≈1 cm".

**Engine-Default (H Werner 2026-07-05; zuvor Werner + Munkhuu 2026-07-03):** Für das Braut-Bodice wird **voll bis Li26 gedreht** = maximale Brustformung, engstes/anliegendstes Armloch. Weniger drehen (lockereres Armloch, kleinerer Brustabnäher) ist eine Variante (Buch verweist auf S.192/S.217) und **nicht** der v1-Default.

**Knips/Kürzung:** S.184 nennt für den *Brustabnäher* selbst keinen Knips/keine Kürzung. Die Angaben „Doppelknips an hAP 1 cm nach oben" und „zum Nähen auf ca. 10 cm gekürzt" gehören zum *hinteren* Abnäher (□8c, S.185) → Abschnitt 7.

## 5. Vorderer Taillenabnäher (vAbl)

*Quelle: S.184, ❾–❿.*

| Schritt | Handlung | Formel / Wert |
|---:|---|---|
| ㉞ | Taillenlinie an beiden Seitenlinien um `1 cm`, an der hinteren Armlinie um `0,5 cm` erhöhen. | erhöhte Taillenlinie |
| ㉟ | Von der vorderen Armlinie `¼ TaU` auf der erhöhten Taillenlinie abtragen (**nicht** `¼ TaW`). | Ausgang für me |
| ㊱ | Reststrecke `me` zur vM messen, PK-Zuschlag: **`vAbl = me + Zuschlag`**. PK≤4: `+1,0` · PK5–7: `+0,5` · PK≥8: `+0`. | Bsp. `me 2,2 + 1,0 = 3,2 cm` |
| ㊲ | Abnäher zum **BrP** zeichnen. | vorderer Taillenabnäher |

*Reicht `¼ TaU` über die vM hinaus → „Starke Figur" (Band 2, nicht v1). Bildangaben getrennt lesen: `1 cm`/`0,5 cm` = Taillen-Erhöhung ㉞; „Abnäher 1,5 cm" = Schulterabnäher ㉛, nicht vAbl.*

## 6. Taillenausfall (TaAf)

*Quelle: S.184–185, ⓫.*

1. vTaB **ohne vAbl** und hTaB messen → `TaB = vTaB + hTaB`.
2. `½ TaW` aus der Konstruktionstabelle.
3. **`TaAf = TaB − ½ TaW`**. Bsp: `42,8 − 36 = 6,8 cm`.

Der vordere Taillenabnäher ist in TaB **bereits berücksichtigt** und wird nicht erneut aus TaAf verteilt. TaAf wird über **SN-Einstellung + Rückteilabnäher** entfernt.

## 7. Hintere Taillenabnäher + Hüfte — **ZUORDNUNG GEKLÄRT**

*Quelle: S.185, ⓬–⓯ + □8c; Foto-D 2026-07-03 (`20260618_185613.jpg`, Zoom); H Werner 2026-07-05 für Zuordnung, Bereiche und Engine-Mittwerte.*

### 7.1 Verteilung & hintere Abnäher (Foto-eindeutig gebunden)

| Schritt | Element | Buch-Bereich | Länge (□8c) | Buchbeispiel (TaAf 6,8) |
|---:|---|---|---|---|
| ㊴ | **SN**-Taillierung (2×1 cm) | 0–2 cm | (an der Naht) | 2,0 cm |
| ㊵ | **shAbl** (seitl. hinterer Abnäher) | 1–3 cm | ca. 12–14 cm | 2,0 cm |
| ㊶ | **hAbl** (hinterer Abnäher, an der hinteren Abnähermitte) | 2–4 cm | ca. 14–16 cm | 2,8 cm |
| | **Kontrolle Σ** | | | **6,8 cm** ✓ |

- Abnäher „zur BrL und nach unten" zeichnen (㊴㊵㊶).
- **hAbl** wird zum Nähen an der Spitze auf **ca. 10 cm gekürzt**; **Doppelknips an hAP, 1 cm nach oben** markieren (beide Angaben gehören zum hinteren Abnäher/hAP, Foto-bestätigt).
- Hintere Abnähermitte = Senkrechte auf halber Strecke zwischen hM und hinterer Armlinie (aus ㉚, Grundgerüst-Anschluss).

**Engine-Default Abnäher-Längen (H Werner 2026-07-05):** Bereichsmitten verwenden: **shAbl 13 cm**, **hAbl 15 cm**.

### 7.2 **TaAf-Verteilung — Engine-Entscheid, ausdrücklich keine Buchregel**

Das Buch gibt für die Konstruktion S.184–185 nur das Beispiel `6,8 = 2,0/2,0/2,8` und die Bereiche `SN 0–2 · shAbl 1–3 · hAbl 2–4` an. Auf S.176–182 findet sich keine allgemeine TaAf-Verteilungsformel; „proportional ausgewogen" auf S.176 bezieht sich auf die Weitenzugaben, nicht auf Abnäher.

**Engine-Regel (Werner-# 2026-07-05):** Die Buchproportion des Referenzfalls `SN : shAbl : hAbl = 2 : 2 : 2,8` wird auf die tatsächliche TaAf skaliert und anschließend als **begrenzte Proportionsprojektion** so in die Buchbereiche gelegt, dass die Summe exakt TaAf bleibt. Die Projektion minimiert die Abweichung von der skalierten Buchproportion unter den Grenzen `SN 0–2 · shAbl 1–3 · hAbl 2–4`.

| TaAf | Engine-Verteilung | Bedeutung |
|---:|---|---|
| 3 cm | `SN 0 / shAbl 1 / hAbl 2` | untere Grenze der S.185-Regel |
| 4 cm | `SN 1 / shAbl 1 / hAbl 2` | begrenzte Interpolation |
| 6,8 cm | `SN 2 / shAbl 2 / hAbl 2,8` | Buchbeispiel exakt |
| 9 cm | `SN 2 / shAbl 3 / hAbl 4` | obere Grenze der S.185-Regel |

Die Regel ist nur für **TaAf 3–9 cm** lösbar. Unter 3 cm ist eine reduzierte/optionale Abnäher-Variante nötig; über 9 cm reichen die drei Buch-Maxima nicht aus und es braucht zusätzliche Abnäher, eine Teilungsnaht oder eine andere Konstruktion. Die Engine darf außerhalb des Bereichs nicht still klemmen oder einen Restbetrag verlieren, sondern muss mit `TAAF_OUT_OF_METHOD_RANGE` stoppen.

`shAbl → 0` wird aus der allgemeinen Regel entfernt: S.186 nennt den shAbl in einer anderen Konstruktion ohne Hüftausfall als optional und verteilt dort zusätzlich auf den vAbl. Das ist keine allgemeine Regel für kleine TaAf in S.184–185. `shAbl = 0` darf nur durch eine ausdrücklich gewählte Figur-/Konstruktionsvariante entstehen.

`modelDecision:true`, `ruleRef: ENGINE-HB1-S185-TAAF-BOUNDED-PROPORTION`, `validTaAfCm: [3, 9]`, `sourceRefs: [S.184–185 Bereiche + Buchbeispiel + externe Stützquellen unten]`. Das Buchbeispiel bleibt Golden-Anker, aber nicht Beleg für eine universelle Skalierungsregel.

#### 7.2.1 Externe Stützquellen für den Engine-Entscheid

Die Quellen zeigen übereinstimmend, dass der Gesamt-Ausfall vollständig verteilt werden muss, aber die **Aufteilung methoden-, modell- und figurabhängig** ist:

- **Hofenbitzer, Korrektur-/Altauflagen-Auszug „Oberteil-Grundschnitt mit alternativer Taillierung":** Bei individuellen Maßen, besonders schlanken Figuren mit größerem BrU, kann eine andere Verteilung nötig sein. Das stützt einen Variantenweg statt einer universellen Buchformel. https://doczz.net/doc/5925867/liebe-nutzer-der-ersten-druckquote-des-buchs-schnittkonst...
- **Winifred Aldrich, _Metric Pattern Cutting for Women's Wear_, offizieller Wiley-Auszug, S.20:** feste klassische Verteilung für den Beispielblock; alternative Verteilungen abhängig von Design und Block ausdrücklich vorgesehen. https://catalogimages.wiley.com/images/db/pdf/9781405175678.excerpt.pdf
- **In the Folds, „How to draft a bodice block":** gleichmäßige Drittelung auf Vorderabnäher, Rückenabnäher und Seitennaht als eigenes System. https://inthefolds.squarespace.com/blog/2016/2/22/how-to-draft-a-bodice-block
- **Modeliste Creative, „Drafting a Basic Bodice Block":** größerer Anteil im Vorderteil, 2–3 cm an der Seitennaht, Rest im Rücken; Anpassung nach Größe mit fachlichem Ermessen. https://modelistecreative.com/2019/02/07/drafting-a-basic-bodice-block-explained/
- **Stitch Paper Scissors, „Custom Bodice Block":** Drittelung, danach Vorderabnäher auf- und Rückenabnäher abrunden, Seitennaht nimmt den Rest auf. https://stitchpaperscissors.com/custom-bodice-block/
- **Twill & Heftstich, „Das Versprechen Maßschnitt":** gleiche Umfangsmaße können verschiedene Proportionen haben; die Autorin benötigt mehr Ausfall in hinteren Abnähern als an der Seitennaht. https://heftstich.net/das-versprechen-massschnitt/

**Ableitung für die Engine:** TaAf allein bestimmt die anatomisch optimale Verteilung nicht eindeutig. Die begrenzte Proportionsprojektion ist deshalb ein reproduzierbarer v1-Default. Der spätere Figur-/Toile-Pass darf eine ausdrücklich getrackte Variante wählen, ohne den Default nachträglich als Buchregel umzudeuten.

### 7.3 Hüftausfall im VT (HüAf)

*Quelle: S.185, ⓮.*

| Regel | Wert |
|---|---|
| `HüAf = vAbl − 2 cm` | Bsp. `3,2 − 2 = 1,2 cm`; ㊷ senkrecht bis Saumlinie |
| `< 0,5 cm` | nicht zeichnen |
| `0,5–1 cm` | kann vernachlässigt werden |
| Minusbetrag | kein HüAf → Variante S.186 (ohne Hüftausfall) |

### 7.4 Hüftbreite & Hüftfehlbetrag (HüFb)

*Quelle: S.185, ⓯.*

| Schritt | Formel / Wert |
|---:|---|
| ㊸ | `HüB = vHüB (ohne HüAf) + hHüB` → Bsp. `44,9 cm` |
| ㊸ | `HüFb = HüB − ½ HüW = 44,9 − 50,5 = −5,6 → Betrag 5,6 cm` (Formel liefert negativ, verwendet wird der **Betrag** — allgemeine Regel, Werner-bestätigt) |
| ㊹ | `HüFb : 2 = 2,8 cm` je Seite an den Seitenlinien in Hüfthöhe **ausstellen** |
| ㊺ | Hüftbögen formen; SN senkrecht bis Saumlinie |

*HüFb < 2 cm → HüU unterproportional; > 8 cm → überproportional (beides ggf. Figurproblem, Band 2).*

## 8. Referenzbeispiele (Golden-Anker)

### 8.1 S.184–185 — Gr. 38, TaU 68, PK3, **mit Hüftausfall** → v1-Bau-Ziel + Golden

| Wert | Formel → Buchwert |
|---|---|
| vAbl | `me 2,2 + 1,0 = 3,2 cm` |
| TaAf | `42,8 − 36 = 6,8 cm` |
| Verteilung | `SN 2,0 / shAbl 2,0 / hAbl 2,8` (Σ 6,8) |
| HüAf | `3,2 − 2 = 1,2 cm` |
| HüFb | `44,9 − 50,5 = −5,6 → 5,6 cm`; je Seite `2,8 cm` |
| Brustabnäher | Li26 = `88:20 + 1 = 5,4 cm`, voll gedreht |

→ In sich geschlossen, wird der **automatische Golden-Test** (wie Gr.38 beim geraden Rock).

### 8.2 S.186 — Gr. 38, TaU 72, PK3, **ohne Hüftausfall** (Referenz, nicht v1-Bau)

Tabellenwerte gelten (Werner-Entscheid Grundgerüst §7): `½ TaW 38 · ½ HüW 50,5 · TaAf 8 · HüFb −4`. Die gedruckte Verteilung (`2+2+0+3,7 = 7,7`) und Hüftausstellung (`2,2`) stammen aus den abweichenden Inline-Werten (`38,5/51`) — bekannter **Buchfehler** (zwei Wertepaare), Foto-bestätigt. Für den v1-Bau irrelevant, da S.184–185-Variante zuerst gebaut wird; die Rest-`0,3 cm` (8 vs. 7,7) muss **nicht** aufgelöst werden.

## 9. Entscheidungs-Ledger (vormals „offen")

| Seite | Frage | Entscheid |
|---|---|---|
| S.184 | Li26-Wert / max. Drehweg | ✅ **H Werner 2026-07-05:** `BrU:20 + 1 cm` (Foto-D; Roh-„≈1cm" war Lesefehler) |
| S.184 | Brustabnäher-Drehung Default | ✅ **H Werner 2026-07-05:** voll bis Li26 |
| S.185 | □8c-Längen `12 / 12–14 / 14–16 cm` → welcher Abnäher | ✅ **H Werner 2026-07-05:** shAbl 12–14 · hAbl 14–16; Engine-Mittwerte 13 / 15 cm |
| S.185 | „auf ca. 10 cm gekürzt" + „Doppelknips hAP" → welcher Abnäher | ✅ **hAbl** bzw. **hAP** (Foto-D) |
| S.185 | TaAf-Verteilung bei beliebiger TaAf | ✅ **Engine-Entscheid Werner-# 2026-07-05, kein Buch-H:** begrenzte Proportionsprojektion `2:2:2,8` für TaAf 3–9 cm; außerhalb `TAAF_OUT_OF_METHOD_RANGE`; `shAbl=0` nur explizite Variante |
| S.185 | HüFb-Vorzeichen | ✅ **Betrag** verwenden (allgemeine Regel) |
| S.185 | Hintere Abnäher-Längen als Engine-Default | ✅ **H Werner 2026-07-05:** Bereichsmitten shAbl 13 cm / hAbl 15 cm; Feinschliff Toile |
| S.187 | Fertigung | Alle Abnäher-Spitzen **2 cm gekürzt**; BrP mit **Bohrloch**; VT-Abnäher ggf. als Englische Naht (S.376), RT-Flankennaht (S.388) — v2 |
| S.186 | Inline-vs-Tabelle (38,5/51 vs. 38/50,5) + Rest 0,3 | Tabellenwerte gelten (Grundgerüst §7); Rest für v1 irrelevant |

## 10. Provenance

*Quelle: Claude-Rohtranskription S.184–186 + Original-Foto-D (2026-07-03) + H-Gegenlesen Werner am Originalbuch (2026-07-05) für Punkte 1–3; Benennung/Anschluss aus der freigegebenen Grundgerüst-Spec; externe Stützquellen in 7.2.1.* Nicht ergänzt: geometrische Annahmen jenseits des Buchtexts, geglättete Werte, Band-2-/S.192/S.217/S.376-Inhalte. Der Engine-Default für die hinteren Abnäher-Längen ist H-freigegeben. Die allgemeine TaAf-Verteilung in 7.2 ist eine von Werner autorisierte `modelDecision` und darf **nicht** als Buchwert oder Buch-H ausgegeben werden.
