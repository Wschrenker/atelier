# eingang_codex — Digitale Zweitprüfung

Stand: 2026-06-25
Prüfer (digital, 2. Instanz): Claude (Opus 4.8), im Auftrag von Werner/Munkhuu.

Dieser Ordner enthält die von **Codex** roh transkribierten Hofenbitzer-Seiten (Band 1).
Diese README dokumentiert die **digitale Zweitprüfung** dieser Dateien: was geprüft wurde,
was bestätigt ist und was **zwingend noch ein Mensch am gedruckten Buch** prüfen muss.

> Einordnung in den Workflow (siehe `../README.md`):
> 1. Codex/Claude transkribiert aus den Fotos. ← liegt hier vor
> 2. **Eine zweite digitale Instanz gleicht Formeln, Zahlen, Punktnummern und
>    Zeichnungsbeschriftungen erneut ab.** ← **das ist diese Prüfung**
> 3. Verdeckte Stellen werden `UNLESBAR` markiert (hier: keine).
> 4. Werner/Munkhuu führen die **menschliche Freigabe am Buch** durch. ← steht noch aus
> 5. Erst danach erhalten Regeln `ruleRef`/`sourceRef` im MethodProfile.

---

## Was diese digitale Zweitprüfung leisten kann — und was nicht

**Geprüft wurde digital:**
- Vollständiges Lesen aller 8 Dateien.
- **Arithmetik**: jede Rechnung und jede abgeleitete Zahl nachgerechnet
  (Glockenrock-Kreisformeln, Grundschnitt-Konstruktionstabellen, Differenz-/Zugabenrechnungen).
- **Interne Konsistenz**: Zugabentabelle (PK 0–10) auf S.537 gegen die Auszüge auf
  S.194/195/196 abgeglichen — stimmig.
- **Foto-Stichproben** an besonders kritischen Stellen (siehe unten).

**Kann digital NICHT abschließend geprüft werden** (→ Menschaufgabe):
- **Feindruck** in dichten Tabellen und winzige Zeichnungs-Callouts. Die Fotos sind zwar
  4080×3060 px, werden für die Maschinen-Sicht aber herunterskaliert; einzelne kleine
  Ziffern, Kürzel und `×-p`-Angaben sind dann **nicht sicher lesbar**.
- **Fachliche/konstruktive Richtigkeit** der Schnittregeln — ist ausdrücklich nicht
  Gegenstand der Transkription und nur durch Werner/Munkhuu freizugeben.
- **Farbkodierung** (welche Linie blau/rot/grün ist) — nur am Original verifizierbar.

---

## Prüfstatus pro Datei

| # | Datei | Buchseiten | Vollständig gelesen | Arithmetik/Konsistenz | Foto-Stichprobe | Status |
|--:|---|---|:--:|:--:|:--:|---|
| 1 | [`s7-8_10_16-19_einfuehrung_massnehmen_codex_transkription.md`](s7-8_10_16-19_einfuehrung_massnehmen_codex_transkription.md) | 7, 8, 10, 16–19 | ✅ | ✅ | ⚠️ S.19 Feindruck nicht lesbar | **digital zweitgeprüft, 1 offener Punkt** |
| 2 | [`s191-196_grundschnitt-weite-und-korsage_rohtranskription.md`](s191-196_grundschnitt-weite-und-korsage_rohtranskription.md) | 191–196 | ✅ | ✅ alle Rechnungen stimmig | — | **digital zweitgeprüft** |
| 3 | [`s400-401_452-453_empire_codex_transkription.md`](s400-401_452-453_empire_codex_transkription.md) | 400, 401, 452, 453 | ✅ | ✅ (keine Rechnungen) | — | **digital zweitgeprüft** |
| 4 | [`s406_454-457_etui-saeule_codex_transkription.md`](s406_454-457_etui-saeule_codex_transkription.md) | 406, 454–457 | ✅ | ✅ | ✅ S.457 (Foto) | **digital zweitgeprüft** |
| 5 | [`s45-46_382-387_407_458-461_codex_transkription.md`](s45-46_382-387_407_458-461_codex_transkription.md) | 45, 46, 382–387, 407, 458–461 | ✅ | ✅ S.45 Formeln | ✅ S.45 (Foto) | **digital zweitgeprüft** |
| 6 | [`s45-46_382-387_407_458-461_prinzessin-ballkleid_codex_transkription.md`](s45-46_382-387_407_458-461_prinzessin-ballkleid_codex_transkription.md) | (45, 46, 382–387, 407, 458–461) | ✅ | — | — | **DUPLIKAT von #5 → löschen** |
| 7 | [`s64-73_454-457_meerjungfrau_codex_transkription.md`](s64-73_454-457_meerjungfrau_codex_transkription.md) | 64–73, 454–457 | ✅ | ✅ Bahnen-/Godet-Anteile stimmig | ✅ S.457 (Foto) | **digital zweitgeprüft, 1 Tippfehler gefunden** |
| 8 | [`s92-97_537_539_produktionsschnitt_codex_transkription.md`](s92-97_537_539_produktionsschnitt_codex_transkription.md) | 92–97, 537, 539 | ✅ | ✅ Zugabentabelle stimmig | — | **digital zweitgeprüft** |

**Kurz:** Alle 8 Dateien sind digital zweitgeprüft. Inhaltlich sind keine Rechenfehler in den
Transkriptionen gefunden worden — die markierten Zahlen-Widersprüche sind **Buch-Eigenheiten**,
keine Transkriptionsfehler. Es gibt aber **strukturelle Befunde** (Duplikat, Seiten-Überlapp,
1 Tippfehler) und eine Reihe von **Punkten, die ein Mensch am Buch bestätigen muss**.

---

## Foto-Stichproben (echter Abgleich mit dem Originalfoto)

| Seite | Foto | Geprüft | Ergebnis |
|--:|---|---|---|
| 45 | `Photos-3-001/20260617_160351.jpg` | Glockenrock-Berechnungen | **exakt korrekt**: `72:3,14=22,9`; `22,9+50=72,9`; `3,14·72,9=229`. Bildnummern □1–□4 stimmen. |
| 457 | `Photos-3-001 4/Photos-3-001 (3)/20260619_145437.jpg` | Beschriftung am RV + □9-Unterschrift | Beschriftung liest sich als **„Futteransatz-Naht am RV"** → Datei #4 korrekt, Datei #7 hat Tippfehler. □9 sagt im Buch wirklich „am VT" (echter Buchfehler, korrekt bewahrt). |
| 19 | `Photos-3-001 2/20260617_160007.jpg` | Maßtabellen-Kürzel | Feindruck **bei verfügbarer Auflösung nicht sicher lesbar** → siehe offener Punkt B-1. |

---

## ⚠️ MUSS vom Menschen am Buch geprüft werden

### A — Datei-/Struktur-Entscheidungen (ohne Buch lösbar, aber Entscheidung nötig)

- [ ] **A-1 Duplikat löschen.** Datei #6 (`…_prinzessin-ballkleid_…`) ist **inhaltlich identisch**
  mit Datei #5 (`…_codex_transkription.md`) — einziger Unterschied sind 6 eingefügte Leerzeilen.
  Eine der beiden löschen (empfohlen: die Datei mit dem aussagekräftigeren Namen behalten und die
  andere entfernen), damit es keine zwei „Wahrheiten" gibt.
- [ ] **A-2 Seiten-Überlapp S.454–457 auflösen.** Die Seiten **454–457 sind doppelt** transkribiert:
  in Datei #4 (Etui) **und** in Datei #7 (Meerjungfrau). Eine kanonische Quelle festlegen; in der
  anderen Datei den Abschnitt entfernen oder klar als Verweis kennzeichnen.
- [ ] **A-3 Dateiname vs. Inhalt (Datei #7).** Die Datei heißt „meerjungfrau", enthält aber
  Bahnenröcke/Godetformen (S.64–73) und das Etuikleid (S.454–457) — **keine eigene
  „Meerjungfrau"-Seite**. Bestätigen, dass die Bündelung so gewollt ist (Meerjungfrau-Silhouette
  wird aus Bahnen-/Godet-Technik gebaut), oder Datei umbenennen.

### B — Inhaltliche Buch-Abgleiche (Originalbuch nötig)

- [ ] **B-1 S.19 — Doppelbelegung `HaU`.** Die Maßtabelle führt `HaU` zweimal:
  als **Halsansatzumfang** (mit Formel `HaU : 6 + 0,5 = HlB`) **und** als **Handumfang**.
  Das Buch selbst sagt (S.8): „Doppelte Bedeutungen sind sehr selten." → Am Buch prüfen, ob für
  Handumfang wirklich `HaU` steht oder ein anderes Kürzel (z. B. `HdU`). Digital nicht auflösbar.
- [ ] **B-2 S.457 — „Futteransatz-Naht" vs. „Futtereinsatz-Naht".** Datei #4 schreibt
  **Futter*ansatz*-Naht**, Datei #7 schreibt **Futter*einsatz*-Naht** (auch in deren Bildbeschreibung).
  Foto-Stichprobe spricht für **„Futteransatz-Naht"** (= Datei #4). Bitte am Buch endgültig bestätigen
  und Datei #7 entsprechend korrigieren.
- [ ] **B-3 S.195 — Zahlen-Widerspruch im Buch (wirkt auf die Konstruktion).** Die Rechnung der
  Taillenweiten-Korrektur ergibt **„0,6 cm Mehrbetrag"**, der Folgesatz nennt aber **„0,4 cm"**
  (Zeichnung: −0,2 / −0,2). Die analoge Hüft-Rechnung (1,6 → 0,8) ist in sich schlüssig. → Am Buch
  klären, welcher Wert für die Taille gilt, bevor eine Engine-Regel daraus abgeleitet wird.
- [ ] **B-4 S.97 — „1 bis 1 cm" vs. „1 bis 4 cm".** Am linken RT-Futter steht `1 bis 1 cm`, an
  benachbarten Futterteilen an gleichartiger Linie `1 bis 4 cm`. Am Buch prüfen, ob `1 bis 1 cm`
  Druckfehler ist.

### C — Produktionsschnitt: hM/SN-Widersprüche (S.92–96, je am Buch bestätigen)

Im Fließtext steht teils „hM", in der roten Zeichnungsbeschriftung „SN" (bzw. umgekehrt) für
**dieselbe** RV-Schlitz-Maßnahme. Das betrifft die Konstruktion direkt und muss eindeutig sein:

- [ ] **C-1 S.92** — Überschrift/Schritte 3–5 nennen die **hM**, die Zeichnungsbeschriftung beim
  Schlitzende die **SN**.
- [ ] **C-2 S.95** — Fließtext nennt **hM**, Zeichnung nennt **SN**; zusätzlich Schrittfolge im Druck
  vertauscht: **6, 7, 9, 8**.
- [ ] **C-3 S.96** — Schritt 7 beginnt mit der **SN**, nennt die RV-Zähnchen danach aber „an der **hM**"
  (Rock laut Einleitung seitlich geschlossen).

### D — Bewahrte Buchfehler bestätigen (verbatim übernommen — bitte als „echter Buchfehler" abnicken)

Diese sind **bewusst unverändert** aus dem Druck übernommen. Ein Mensch sollte am Buch bestätigen,
dass es sich wirklich um Druckfehler des Buches handelt (und nicht um Transkriptionsfehler), und
entscheiden, wie die Engine damit umgeht:

- [ ] **D-1 S.46** — fehlendes Satzzeichen zwischen „werden" und „lange".
- [ ] **D-2 S.69** — „kei**e**n" (statt „keine"); zusätzlich widersprüchliche Klammerung
  „Das (RT3 noch spiegeln.)".
- [ ] **D-3 S.70** — „des Zehn-Bahnenrock" (fehlendes Genitiv-s).
- [ ] **D-4 S.191** — „identisch" steht im Klammertext doppelt.
- [ ] **D-5 S.192** — „vordern" in Bildunterschrift □2.
- [ ] **D-6 S.195** — „kontruieren".
- [ ] **D-7 S.196** — „eines erprobten Kleider-Grundschnitt"; „zugelegen".
- [ ] **D-8 S.382** — „auf der folgenden Seiten".
- [ ] **D-9 S.383** — „mit parallelem, leicht runden Schulterabnäher".
- [ ] **D-10 S.384** — „aus dem tailliertem OT-GS"; „der identischen Betrag".
- [ ] **D-11 S.387** — „wird … wird" (doppelt).
- [ ] **D-12 S.453** — „des hinteren Träger"; Satz „Diese FaT nicht zu schmal gewählt werden."
  (kein finites Verb).
- [ ] **D-13 S.457** — Bildunterschrift □9 sagt „am VT", obwohl die Seite das **RT** behandelt
  (im Foto bestätigt: steht so im Buch); Schritt 28 „Mehrweite in Futter".
- [ ] **D-14 S.460** — „Die vordere und hintere Spitze liegt" (Singular); Abschnittsnummer „2"
  doppelt vergeben.
- [ ] **D-15 S.539** — Definition „Hüfte" grammatisch unstimmig.

### E — Feindruck, der nur am Buch/Original sicher verifizierbar ist

Bei diesen Stellen reicht die Maschinen-Auflösung nicht; bitte am Buch (oder am Foto in voller
Auflösung) gegenlesen:

- [ ] **E-1** Zugabentabelle **S.537** (und die Auszüge S.194/196): alle Einzelziffern PK 0–10.
  *(Digital konsistent gegengerechnet, aber die Ziffern selbst nicht pixelgenau verifiziert.)*
- [ ] **E-2** Kleine Zuschnitt-Angaben **`×-p`** auf S.459 und S.461 (Groß-/Kleinschreibung `p`).
- [ ] **E-3** Konstruktionsmarken-Nummern in den Zeichnungen (Punkt-/Schrittnummern an den Skizzen).
- [ ] **E-4** Maßtabelle **S.19** komplett (siehe B-1).

### F — Fachliche Freigabe (Grundvoraussetzung für Gate M0)

- [ ] **F-1** Alle 8 Dateien tragen „**noch keine fachliche Freigabe durch Werner/Munkhuu**".
  Die konstruktive Richtigkeit der Regeln ist von der digitalen Prüfung **nicht** abgedeckt und
  muss am Buch freigegeben werden, bevor `ruleRef`/`sourceRef` vergeben werden.

---

## Was digital bereits bestätigt ist (keine Nacharbeit nötig)

- **S.45 Halbglocke** — alle Kreisformeln korrekt (Foto-bestätigt).
- **S.191–196** — alle Konstruktions-, Differenz- und Zugabenrechnungen in sich stimmig:
  z. B. `88+6=94 → ½ 47`; `ArD-Diff 3,5 → ⅓ 1,2 + ⅔ 2,3`; `vSuN 12,5+0,6=13,1`, `hSuN +0,7=13,8`;
  `½ HüW 56,1 − 54,5 = 1,6 → 0,8`.
- **Zugabentabelle S.537** stimmt mit den auf S.194/195/196 verwendeten PK-Werten überein
  (PK0/PK3/PK9 durchgeprüft).
- **Bildnummern/□-Sequenzen und Schrittnummerierungen** laufen innerhalb jeder Seite konsistent
  (Ausnahmen sind als Buchfehler markiert, s. D).
- **`UNLESBAR`**: in keiner der 8 Dateien vorhanden.

### Nebenbefund (kein Blocker, für die Tool-Pipeline)
- Die Fotopfade sind uneinheitlich notiert: Datei #7/#8 nennen teils repo-relative Pfade
  (`hofenbitzer/band_1/Photos-3-001/…`), die übrigen nur den Ordner ab `Photos-3-001 …`.
  Für spätere Automatisierung vereinheitlichen.
