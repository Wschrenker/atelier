# Formeln s041 (normalisiert)

Walking-Skeleton-Hinweis: Alle drei Formeln unten stehen auf `offen`, weil die
zugrundeliegenden Text- und Bildstellen noch nicht einzeln von Werner am
Original bestätigt sind (siehe [formeln_s041.md](formeln_s041.md)). Die
Normalisierung zeigt bereits die vollständige technische Form für den
Walking-Skeleton-Durchstich, ersetzt aber keine Bestätigung.

## Formel 1: Bundlänge über Knopfloch-Auge und Knopfannahtpunkt (Variante 2, Untertritt)

- **Quelle:** [formeln_s041.md](formeln_s041.md), Abschnitt „Variante 2: Bund
  mit Untertritt“, Textstelle (ocr_s041.md, Zeile 9) und zugehörige
  Zeichnungsbeschriftung (skizzen/s041_skizze_02.png).
- **Buchfassung:**

  ```text
  Die Länge vom Knopfloch-Auge zum Knopfannahpunkt entspricht dem Bundumfang (TaU).
  ```

  Bildbeschriftung (skizzen/s041_skizze_02.png): „Taillenumfang (TaU)“.
- **Technische Formel:** `Laenge(Knopflochauge, Knopfannahtpunkt) = TaU`
- **Eingaben und Einheiten:** `TaU` – Taillenumfang/Bundumfang, cm (Bezeichnung
  im Original uneinheitlich, siehe offene Fragen).
- **Ausgabe und Einheit:** Länge des neu eingeteilten Bundstreifens vom
  Knopfloch-Auge bis zum Knopfannahtpunkt, cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; exakte
  Gleichsetzung ohne Toleranzangabe.
- **Abhängigkeiten:** `TaU` als Konstruktionsmaß, siehe
  `000_sprache/20_symbole_abkuerzungen/02_zzb_abkuerzungen_koerpermasse_konstruktionsmasse.md`
  und `000_sprache/20_symbole_abkuerzungen/02_zzc_abkuerzungen_aus_formeln_band_1_geprueft_v1.md`
  (dort mit Quellverweis auf `formeln_s120.md`). Bezieht sich auf den zuvor
  neu eingeteilten geraden Bund dieser Seite; die ursprüngliche
  Bundeinteilung selbst ist nicht Teil dieser Seite.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** Fließtext nennt „Bundumfang (TaU)“,
  die Zeichnung beschriftet dieselbe Bemaßung als „Taillenumfang (TaU)“. Ob
  das bewusst gleichgesetzt ist oder eine Druckungenauigkeit vorliegt, ist am
  Original bzw. mit Werner zu klären. Zusätzlich noch nicht von Werner
  bestätigt.

## Formel 2: Mindestabstand des Untertritts zur Kante (Variante 2, Untertritt)

- **Quelle:** [formeln_s041.md](formeln_s041.md), Abschnitt „Variante 2: Bund
  mit Untertritt“, Textstelle (ocr_s041.md, Zeile 10) und zugehörige
  Zeichnungsbeschriftung (skizzen/s041_skizze_02.png).
- **Buchfassung:**

  ```text
  Der Abstand zur Kante sollte mindestens dem Knopfdurchmesser (KnoD) + 0,5 cm entsprechen, damit der Untertritt von innen das Knopfloch abdeckt.
  ```

  Bildbeschriftung (skizzen/s041_skizze_02.png): „KnoD + mind. 0,5 cm“.
- **Technische Formel:** `Abstand(Kante, Untertritt) >= KnoD + 0,5 cm`
- **Eingaben und Einheiten:** `KnoD` – Knopfdurchmesser, cm.
- **Ausgabe und Einheit:** Mindestabstand des Untertritts von der Kante, cm
  (untere Schranke, kein fester Wert).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** nur Mindestwert
  angegeben („mindestens“); keine Obergrenze im Buch genannt, bleibt offen.
- **Abhängigkeiten:** `KnoD` ist bisher in keiner Datei unter
  `000_sprache/20_symbole_abkuerzungen/` verzeichnet; auf dieser Seite neu.
  Ergänzung des Sprachbestands ist nicht Teil dieses Prompts.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine inhaltlichen Widersprüche
  zwischen Text und Zeichnung; Bestätigung am Original steht aus, und `KnoD`
  ist noch nicht im Abkürzungsbestand geführt.

## Formel 3: Bundlänge über Haken und Öse/Knopfposition (Variante 3, Übertritt)

- **Quelle:** [formeln_s041.md](formeln_s041.md), Abschnitt „Variante 3: Bund
  mit Übertritt“, Textstelle (ocr_s041.md, Zeile 28) und zugehörige
  Zeichnungsbeschriftung (skizzen/s041_skizze_04.png).
- **Buchfassung:**

  ```text
  Der Abstand zum Haken entspricht dem TaU.
  ```

  Bildbeschriftung (skizzen/s041_skizze_04.png): „Taillenumfang (TaU)“.
- **Technische Formel:** `Abstand(Oese_oder_Knopfposition, Haken) = TaU`
- **Eingaben und Einheiten:** `TaU` – Taillenumfang, cm.
- **Ausgabe und Einheit:** Länge des neu eingeteilten Bundstreifens
  (Übertritt-Variante), cm.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** keine; exakte
  Gleichsetzung ohne Toleranzangabe.
- **Abhängigkeiten:** gleiche `TaU`-Definition wie Formel 1. Übertritt-Variante
  ist strukturell analog zur Untertritt-Variante (Formel 1), nutzt aber die
  linke Seitennaht (`lSN`) statt der vorderen Mitte als Trennstelle.
- **Status:** offen
- **Offene Fragen oder Widersprüche:** keine inhaltlichen Widersprüche;
  Bestätigung am Original steht aus.
