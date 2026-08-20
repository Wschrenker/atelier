# eingang_claude — Status der digitalen Zweitprüfung

Stand: 2026-06-25 · erstellt durch Claude

Dieser Ordner ist der **Posteingang** für Claude-Rohtranskriptionen aus Hofenbitzer Band 1.
Keine der Dateien hier ist fachlich freigegeben — die menschliche Freigabe durch Werner/Munkhuu
am Buch steht für **alle** Dateien dieses Ordners noch aus.

## Zwei getrennte Prüfstufen (nicht verwechseln)

1. **Digitale Zweitprüfung** — eine zweite digitale Instanz gleicht den transkribierten Text
   Zeichen für Zeichen, Zahl für Zahl gegen die Originalfotos ab. Prüft nur die *Transkriptions­treue*,
   **nicht** die fachliche Richtigkeit der Konstruktionsmethode.
2. **Menschliche Freigabe** — Werner/Munkhuu prüfen am physischen Buch und geben frei. Erst danach
   darf eine Regel `ruleRef`/`sourceRef` im MethodProfile bekommen.

Dieses README betrifft ausschließlich **Stufe 1**.

## Status-Übersicht (6 Dateien)

| Datei | Seiten | Digital 2. geprüft? | Durch / Stand | Bemerkung |
|---|---|:--:|---|---|
| `s11-15_rohtranskription.md` | 11–15 | ✅ ja | Codex, 21.06.2026 (bildweise) | laut Kopfzeile vollständig gegengeprüft |
| `s172-181_184-187_oberteil-grundschnitt_rohtranskription.md` | 172–181, 184–187 | ✅ ja | Codex, 21.06.2026 (alle 14 Fotos) | laut Kopfzeile vollständig gegengeprüft |
| `s406-407_s438-439_kleidformen_rohtranskription.md` | 406, 407, 438, 439 | ✅ ja | Codex, 21.06.2026 (Seite für Seite) | maßgeblich für S.438/439 (siehe Konflikt C1) |
| `s20-31_groessen-und-konstruktionsstandards_rohtranskription.md` | 20–31 | 🟡 teilweise | Claude, 25.06.2026 | **S.20-Größentabelle vollständig fototreu verifiziert**; S.21–31 noch offen |
| `s370_372-375_410-419_rohtranskription.md` | 370, 372–375, 410–419 | 🟡 teilweise | Claude, 25.06.2026 | Schlüsselformel S.416 + Labels S.372 verifiziert; Autoren-Doppelprüfung bestätigt; übrige Seiten Stichprobe |
| `s426-431_438-439_rohtranskription.md` | 426–431, 438, 439 | 🔴 nein | — | nur Rohtranskription; in diesem Durchgang **nicht** verifiziert |

Legende: ✅ vollständig · 🟡 teilweise (Stichprobe/Kerninhalt) · 🔴 noch nicht

## Was am 25.06.2026 digital gegen die Fotos geprüft wurde

**Methode:** Die Fotos liegen gedreht vor (EXIF-Orientation teils 6). Sie wurden rein technisch
aufgerichtet (EXIF-Transpose) und in hochauflösende, aufrechte Ausschnitte zerlegt; die temporären
Lesekopien liegen außerhalb des Projektordners (System-Temp) und werden verworfen. Am Buchinhalt
wurde nichts verändert.

Geprüft und **Wert für Wert fototreu bestätigt**:

- **S.20 — DOB-Größentabelle** (`20260617_160018.jpg`): die gesamte Tabelle, alle ~28 Messzeilen
  × 15 Größenspalten (32–60), linke und rechte Hälfte. **100 % deckungsgleich** mit der Transkription,
  einschließlich der beiden auffälligen Werte (siehe A1/A2) und der unklaren US-52-Zelle (B1).
- **S.416 — Radius-Formel** (`20260619_144917.jpg`): `½ BrB – 2 cm` sowie `ca. 1,5 cm`,
  `ca. 2,5 cm`, `PK2 bis PK4` im □6-Text — bestätigt.
- **S.372 — Diagramm □2** (`20260619_144456.jpg`): `0 bis 1,5 cm`, `hier 0 cm`, RT/VT, Schrittkreise — bestätigt.

**Ergebnis:** An allen geprüften Stellen ist die Transkription fototreu. Es wurde **kein
Transkriptionsfehler** gefunden. Die in den Dateien selbst markierten Unsicherheiten sind ehrlich gesetzt.

---

## ⚠️ WAS DER MENSCH AM BUCH PRÜFEN MUSS

### A. Vermutete **Buchfehler** — Transkription ist fototreu, das *Buch* ist zu prüfen

- **A1 — S.20, Zeile `7.HW bis Fußsohle`, Größe 58:** Im Foto steht eindeutig **„15,5"**
  (deutlich kürzer als die Nachbarwerte 150,1 / 150,9). In der Reihe …150,1 → ? → 150,9 fehlt
  offensichtlich eine Ziffer → vermutlich **150,5**. *Am Buch klären: Druckfehler oder beschädigte Stelle?*
- **A2 — S.20, Zeile `ArD` (Armdurchmesser), Größen 46/48/50 = 12,1 / 12,2 / 14,3:** Sprung
  12,2 → 14,3 ist unregelmäßig (sonst Schrittweite +1,1: 14,3→15,4→16,5…). Fototreu übernommen.
  *Am Buch klären (vermutlich soll Größe 48 = 13,2 lauten).*
- **A3 — S.428:** „Borten können nur an gerade Kanten gearbeitet werden." (grammatisch auffällig, wörtlich).
- **A4 — S.430:** „mit derselben Breiten" (wörtlich übernommen).
- **A5 — S.439:** Komma in „Zweigeteilte Kleider, können …" sowie „und ein (gerader) Rock" (wörtlich).
- **A6 — S.418** (Datei `s370…`, ca. Zeile 893): Satzbau-/Buchfehler — Satz endet nach „reicht.",
  der mit „Da" beginnende Folgesatz bleibt grammatisch unvollständig.

### B. **Unlesbare / nicht zweifelsfreie** Stellen — am Buch nachlesen

- **B1 — S.20, Vergleichstabelle US-Größe 52:** Zelle erscheint auch im Zoom leer/unklar → `UNLESBAR`.
  (Niedrige Priorität — US-Größen sind nicht engine-relevant.)
- **B2 — S.22:** Schnittteil-Stempel-Abkürzungen `OSE`, `E1`/`EL`, `OSt`, `OSF`, „2x-g" sehr klein
  fotografiert, nicht zweifelsfrei; Bildunterschrift ☐2 nicht auffindbar.
- **B3 — S.24:** Klammerinhalt (mittlere Spalte ❶) und ein Wort (❼) unsicher; die drei
  Fuß-Bildunterschriften angeschnitten.
- **B4 — S.27:** Wortende „…kante" (vermutlich „Saumbelegkante") nicht sicher; Randregister-Begriff verdeckt.
- **B5 — S.28:** Widerspruch im Buch selbst — „Die Knipslänge ist **5 mm**" (mittlere Spalte) vs.
  „Die Knipslänge von **6 mm**" (rechte Spalte). Beide so im Foto. *Am Buch klären, welche gilt.*
- **B6 — S.29:** Werkzeug-Bildnummer (Knipszange/Lochbohrer) nicht eindeutig; Randregister-Begriff verdeckt.
- **B7 — S.31** (Beispiel-/Abkürzungsseite): linke Wortanfänge und rechte Beschreibungen am Spaltenrand
  angeschnitten (in der Transkription mit `[ ]` markiert); Modellnamen am linken Rand angeschnitten
  (`…-18`, `…-Marie`, `…ella`); `TSp` (Tasch…) angeschnitten; Foto leicht schräg → Restunsicherheit
  bei der Zuordnung Material-/Anzahl-Spalten zu den Namen.

### C. **Datei-übergreifende Konflikte** (separat gemeldet, hier zur Erinnerung)

- **C1 — S.438/439 doppelt transkribiert:** in `s406-407_s438-439…` (✅ geprüft) **und** in
  `s426-431_438-439…` (🔴 roh). Abweichung im Wortlaut („…verwendet **und** Verschlusslösungen" vs.
  „…**sowie**…") und beim Verweis □8 (geprüfte Datei: „**424** am Oberteil und 391 am Rock"; Roh-Datei: nur „391").
  → Die geprüfte Datei als maßgeblich festlegen; S.438/439 in der Roh-Datei bereinigen/verweisen.
- **C2 — Duplikat** der beiden `s45-46_382-387_407_458-461…`-Dateien liegt in `../eingang_codex/`
  (nicht in diesem Ordner) — nur als Querverweis.

### D. **Noch ausstehende digitale Zweitprüfung** (von mir am 25.06. NICHT verifizierte Seiten)

- `s20-31…`: **S.21–S.31** (Fließtext-Seiten „Standards bei Schnittkonstruktionen") — Wortlaut noch
  nicht unabhängig gegen die Fotos gegengeprüft.
- `s370_372-375_410-419…`: **S.370, 373, 374, 375, 410–414, 417, 419** — nur Stichprobe; vollständige
  Zahlen-/Formelprüfung Seite für Seite offen. (S.416 und S.418 sind laut Datei bereits zweimal vom
  Autor gegengeprüft.)
- `s426-431_438-439…`: **komplette Datei** (S.426–431, 438, 439) — in diesem Durchgang nicht angefasst.

---

## Reihenfolge bis zur Freigabe

1. Digitale Zweitprüfung **vollständig** abschließen (Abschnitt D abarbeiten).
2. Punkte aus A/B/C am physischen Buch durch Werner/Munkhuu klären und freigeben.
3. Erst dann erhält jede implementierte Regel `ruleRef` und `sourceRef` im MethodProfile.
