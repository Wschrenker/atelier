# Hofenbitzer Band 1 — Transkription (Stufe 2)

Stand: 2026-06-21

Quellen: Fotos in `../Photos-3-001/` und `../Photos-3-001 2/`.

## Zweck

Diese Dateien erfassen die für die Engine benötigten Buchseiten als strukturierte, mit Seiten und
Fotodateien belegte Regeln. Sie sind die digitale Arbeitsgrundlage für Gate M0.

**Freigabe:** Werner/Munkhuu haben die Transkriptionen am 2026-06-21 als richtig bestätigt. Damit sind
Hofenbitzer-Golden-Tests und die Umstellung der Konstruktionsmethode freigegeben.

## Arbeitsweise

1. Claude oder Codex transkribiert direkt aus den Fotos.
2. Eine zweite digitale Instanz gleicht Formeln, Zahlen, Punktnummern und Zeichnungsbeschriftungen erneut
   mit den Fotos ab.
3. Wirklich verdeckte Stellen werden als `UNLESBAR` markiert; es wird nie geraten.
4. Werner/Munkhuu führen die menschliche Freigabe am Buch durch.
5. Erst danach erhält jede implementierte Regel `ruleRef` und `sourceRef` im MethodProfile.

## Konfidenzzeichen

- ✅ direkt im Foto lesbar und gegengeprüft
- ⚠️ sichtbare Buch-Inkonsistenz oder nicht implementierungsrelevanter Hinweis
- ❓ noch ungeklärte Lesestelle; in den freigegebenen Dateien derzeit keine vorhanden

## Dateien und digitaler Stand

| Datei | Seiten | Inhalt | Digitaler Stand |
|---|---:|---|---|
| [`s32-36_gerader-rock-grundschnitt.md`](s32-36_gerader-rock-grundschnitt.md) | 32–36 | Konstruktionstabelle, Grundgerüst, Abnäher, Produktionsschnitt | vollständig |
| [`s39-41_bund.md`](s39-41_bund.md) | 39–41 | Gerader Bund, Taillenmehrweite, Über-/Untertritt, Produktionsschnitt | vollständig |
| [`s42-43_saumerweiterter-rock.md`](s42-43_saumerweiterter-rock.md) | 42–43 | Einschnittlinien, Abnäherverlegung, Öffnungsbetrag, Saumform | vollständig |
| [`s44_glockenrock.md`](s44_glockenrock.md) | 44 | Vollglocke/Tellerrock, Kreisformeln und Zuschnitt | vollständig |

## Aufgelöste frühere Fehler/Unsicherheiten

- S.33: P4 liegt eindeutig auf der **Taillenlinie**.
- S.33: `97 + 3 = 100` und `72 + 2 = 74` sind klar lesbar.
- S.43: `12 bis 15 cm` bezeichnet die Länge des neuen RT-Abnähers.
- S.43: An jeder Seitennaht wird die Hälfte des Öffnungsbetrags ausgestellt.
- S.44: Der echte Glockenrock ist ein **Vollkreisring**; Halb-/Viertelkreis sind Zuschnittaufteilungen.
- S.44: `NZg` ist ein Parameter, kein fehlender fester Buchwert.

## Menschliche Verifikations-Checkliste

- [x] S.32–36 am Buch geprüft und freigegeben
- [x] S.39–41 am Buch geprüft und freigegeben
- [x] S.42–43 am Buch geprüft und freigegeben
- [x] S.44 am Buch geprüft und freigegeben
- [x] Freigegeben durch Werner/Munkhuu am 2026-06-21

## Unabhängige digitale Nachprüfung (Claude, 2026-06-25)

Die ursprüngliche Foto-Zweitprüfung dieser vier Dateien stammt vom 2026-06-21. Am 2026-06-25 hat
Claude die **engine-kritischen Zahlen und Formeln** unabhängig erneut gegen die Originalfotos geprüft
(aufgerichtete Hochzoom-Kacheln). **Ergebnis: alles fototreu, kein Transkriptionsfehler.**

Ziffer für Ziffer bestätigt:

- **S.33 Konstruktionstabelle** (`…160220.jpg`): HüU 97 / Zg 3 → HüW 100 · ½50 · ¼25; TaU 72 / Zg 2 →
  TaW 74 · ½37 · ¼18,5; ½HüW−½TaW = 13 · ½6,5; HüT 21; Hüftabstich 6,5; Größe 38. Komplett deckungsgleich.
- **S.35 Hüftabstich-Variante** (`…160234.jpg`): 6 / 1,5 / 3 / 2,5 / Σ13; Diagramm ☐7: TaU:10, 8–10 cm,
  13–16 cm, 12–14 cm, 1,5/2,5/3,0 cm, ⅓+0 bis 1 cm. Deckungsgleich.
- **S.39 Bund** (`…160306.jpg`): Kontroll-Box 19,7 + 17,5 − 36,0 = 1,2 cm Einhalteweite; Bundbreite 2–5 cm.
  Der ⚠️ Buch-Typo (linke Bildunterschrift „vordere Taillennaht **(hTaN)**" statt vTaN) ist am Foto bestätigt.
- **S.43 saumerweiterter Rock** (`…160332.jpg`): Diagramm „öffnen hier 6 cm", „ausstellen hier 3 cm",
  „12 bis 15 cm" (RT-Abnäher), Drittel-Einteilung, ZP separat. Deckungsgleich.
- **S.44 Glockenrock** (`…160345.jpg`): Berechnungsbox rTaW = 72:(2·3,14) = 11,5 · rSaW = 11,5+50 = 61,5 ·
  SaW = 2·3,14·61,5 = 386,2 cm. Deckungsgleich.

Damit haben diese vier Dateien alle drei Gates durchlaufen: **T (transkribiert) · D (digital, 21.06. +
unabhängig nachgeprüft 25.06.) · H (menschlich freigegeben 21.06.)**. Siehe Ledger `_status.csv`.
