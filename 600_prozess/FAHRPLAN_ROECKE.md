# Fahrplan Röcke — von den Dateien zum Python-Code

Stand: 2026-09-04. Geschrieben für eine frische Session und für Werner.

Diese Datei sagt: was schon passiert ist, was der Bestand ist, und in welchen
Schritten wir von Buchseiten zu lauffähigem Python kommen. Sie erklärt keine
einzelne Formel.

---

## 1. Was schon passiert ist

Das Repo wurde entschlackt. Der Befund war:

Von 479 Markdown-Dateien im Ordner `200_funktionen` waren **455 byte-identische
Kopien**. Die Mathematik-Dateien stammten alle aus
`400_mathematik/10_mathe_einzupflegen`, die Transkripte und Formeldateien alle
aus `100_quellen`. Eine Datei wie `07_geraden_und_schnittpunkte.md` lag
dreizehnmal im Repo, das Transkript `s89.md` fünfmal.

Entfernt wurden:

| Was | Umfang |
|---|---|
| Kopien in `200_funktionen` | 455 Dateien |
| Doppelte Buchfotos in `200_funktionen` | 18 Dateien |
| Zwischenablagen `_tmp_verify_481_510`, `tmp_hofenbitzer_upright` | 254 MB |
| `__pycache__`, `.pytest_cache` | — |
| `1100_test` (verworfener Prototyp) | 66 Dateien |

`200_funktionen` ging damit von 68 MB auf 424 KB, von 517 Dateien auf 38.

**Nichts ging verloren.** Die Zuordnung „welche Buchseite gehört zu welcher
Funktion" war die eigentliche Arbeitsleistung. Sie steht jetzt als `INHALT.md`
in jedem Kapitelordner und verweist auf das Original, statt es zu kopieren.

Neu gebaut: `600_prozess/werkzeuge/verweise_pruefen.py`. Das Skript prüft alle
Dateiverweise im Repo und meldet tote. Erster Lauf: **869 tote Verweise, alle
schon vorher vorhanden**, keiner durch das Aufräumen entstanden.

Sicherungspunkt: `git tag vor-aufraeumen-2026-09-04`.

### Warum 869 tote Verweise wichtig sind

Sie stammen überwiegend aus den Indexdateien
`00_index_normalisierte_formeln_band_1_v2.md` und `..._v3.md`. Die verweisen auf
normalisierte Formeldateien, die nie angelegt wurden. Genau das erzeugte den
Eindruck, alle Formeln seien fertig normalisiert. Sind sie nicht.

Ein toter Verweis ist die Stelle, an der ein Sprachmodell anfängt zu raten.
Deshalb gilt ab jetzt: **vor und nach jedem Umräumen `verweise_pruefen.py`
laufen lassen und beide Zahlen nennen.** Die Zahl darf nie steigen.

---

## 2. Wo wir stehen

Es geht um Röcke, zwei Blöcke:

| Block | Ordner | Buchseiten | Zustand |
|---|---|---|---|
| Grundschnitte | `200_funktionen/02_grundschnitte_roecke_s32-39_funktionen` | 32–39 | Formeln praktisch fertig normalisiert, 18 Formel-IDs, 4 offen oder gesperrt |
| Modelle | `200_funktionen/03_modelle_roecke_s40-105_funktionen` | 40–105 | 42 Formel-IDs, aber nur 15 von 50 Extrakten normalisiert |

Die Originale liegen in
`100_quellen/10_hofenbitzer_b1/1_hofenbitzer_band_1_digital/`, die Fotos in
`.../2_bilder/`. Die Ordner unter `200_funktionen` enthalten keine Kopien mehr,
sondern Verweise.

---

## 3. Es gibt zwei Sorten Prüfstellen

Das ist die häufigste Verwechslung im Projekt. Der Name „Prüfstellen" steht für
zwei völlig verschiedene Arbeitsvorräte.

**Textprüfstellen.** Druckfehler, unlesbare Stellen, fehlende Wörter im Buch.
Stehen in `00_pruefstellen.md` im jeweiligen Kapitel, in Gruppen A, B und N.
Braucht einen Menschen mit dem physischen Buch — Werner oder Munkhuu.
Die meisten davon blockieren keinen Code. Ein Druckfehler in einer
Bildunterschrift stört die Rechnung nicht.

**Formelprüfstellen.** Widersprüche im Rechenweg. Stehen in `FORMELSTATUS.md`
mit Status `offen` oder `gesperrt`. Braucht ebenfalls das Buch, blockiert aber
Code direkt.

**Dazu ein Drittes, das oft mitgemeint ist:** das Normalisierungsprotokoll
(`pruefstellen_*.md` in Block 02). Das ist Buchhaltung darüber, welche
Kandidatenzeile zur Formel wurde und welche verworfen — maschinell nachrechenbar,
braucht niemanden.

Regel fürs Sortieren: Gruppe A blockiert nicht. Gruppen B und N blockieren.
Status `offen` und `gesperrt` blockieren.

---

## 4. Der Weg zum Code

Fünf Schritte. Jeder wird in einer eigenen Session gemacht, mit Rückmeldung
dazwischen.

### Schritt 1 — Dossier-Generator

Ein Skript, das pro Rockmodell **eine** Markdown-Datei erzeugt: Buchtext,
Formeln, Prüfstellen, Bildpfade, Mathematik-Verweise, alles untereinander.

Der Sinn: Werner will eine Schachtel pro Modell, in der alles drin ist. Wenn man
diese Schachtel zusammenkopiert, hat man das Dublettenproblem sofort wieder.
Wenn man sie **erzeugt**, gibt es sie genau einmal, sie veraltet nie, und man
kann sie jederzeit wegwerfen und neu bauen.

Ergebnis: ein Dossier für den geraden Rock (S. 32–39) und eines für den
Glockenrock (S. 44–45).

### Schritt 2 — Triage und Normalisierung, nur Block 03

Erst sortieren, dann rechnen. Jede Formeldatei kommt in genau einen Topf:

- **A** — echte Rechenformel, normalisierbar
- **B** — gar keine Formel, nur Bildverweis, Stückzahl oder Beschriftung
- **C** — geometrische Konstruktion, braucht erst die Engine

Erst nach der Sortierung wird normalisiert, und zwar nur Topf A. Das ist wichtig:
von den 50 Extrakten in Block 03 sind laut `FORMELSTATUS.md` 23 gar keine
Formeln. Der echte Rest liegt bei etwa zwölf Seiten, nicht bei 35.

Kapitel 07 (Wickeln, Drapieren, Asymmetrie) hat null Normalisierungen. Das ist
kein Rückstand, sondern ein Befund: dort stehen Konstruktionsanweisungen, keine
Rechenformeln. Das Kapitel gehört nach Topf C.

### Schritt 3 — Python für den Grundschnitt, Block 02

Der Grundschnitt ist die Basis, auf der alle Modelle aufsetzen. Deshalb kommt er
vor den Modellen, obwohl seine Formeln schon länger fertig sind.

Die Seiten 33 bis 35 bilden eine geschlossene Kette: Taillenausfall ausrechnen,
auf Hüftabstich und Abnäher verteilen, Kontrollsumme prüfen. Die Kontrollsumme
ist gleichzeitig der Test — das Buch liefert die Prüfung mit.

### Schritt 4 — Python für die Modelle, Block 03

Zuerst die geschlossenen Einzelformeln: Glocke (S. 44, 45), Kräuselfaktoren
(S. 48), Godet-Saumweite (S. 68), Faltentiefe (S. 88, 89). Das sind reine
Funktionen mit einem Eingang, einem Ausgang und einem gedruckten Buchwert als
Test. Alles Geometrische kommt später, wenn die Engine steht.

### Schritt 5 — Aufräumen von Text und Sprache

READMEs auf je eine Seite kürzen, normales Deutsch. Die alten Prüfprotokolle
umbenennen, damit sie nicht mehr wie Einstiegstexte aussehen. Indizes auf das
kürzen, was wirklich existiert — das senkt auch die 869 toten Verweise.

---

## 5. Regeln, die in jedem Schritt gelten

1. **Nichts erfinden.** Fehlt eine Bezugsgröße, eine Einheit oder eine
   Rundungsregel, ist der Status `offen` und der Grund wird benannt. Lieber
   offen als geraten.
2. **Buchwerte nachrechnen.** Weicht das eigene Ergebnis ab, ist der Status
   `gesperrt` und der Widerspruch wird beziffert. Buchfehler werden nie
   stillschweigend korrigiert.
3. **Eine Quelle pro Information.** Nie kopieren, immer verweisen oder erzeugen.
4. **Vor und nach jedem Umräumen `verweise_pruefen.py`.** Basiswert 869, darf
   nicht steigen.
5. **Normales Deutsch.** Kurze Sätze, keine verschachtelten Blockzitate, keine
   Kürzelcodes wie „A90–A110" in Texten, die zum Einstieg gedacht sind.
   Protokolle heißen `protokoll_...` und stehen nicht im Weg.
6. **Die Ordnerstruktur bestimmt Werner.** Wenn eine Struktur für ihn
   überschaubar ist, ist sie richtig. Ein Sprachmodell braucht keine bestimmte
   Hierarchie — es braucht nur, dass jede Information genau einmal existiert.

---

## 6. So startet die nächste Session

Ein Satz genügt:

    Lies 600_prozess/FAHRPLAN_ROECKE.md und AGENT.md. Erklär mir den Plan in
    eigenen Worten, sag mir, was du im Repo vorfindest, und dann machen wir
    Schritt 1.

Nach jedem Schritt: kurz berichten, was rauskam, und was gefehlt hat. Erst dann
der nächste Schritt.
