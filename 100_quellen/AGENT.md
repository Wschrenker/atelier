# Quellen — was hier drin gilt

## Navigation — Regel

Diese Datei führt nur zu den direkten Unterordnern von `100_quellen/`.
Einzelne Fachdateien und tiefere Unterordner werden hier nicht aufgeführt. Sie
gehören in die Agentendatei des jeweiligen Unterordners.

Die Ladeliste dient der Navigation. Automatisch geladen werden nur die
angekreuzten Agentendateien.

## Navigation

- [x ] `10_hofenbitzer_b1/AGENT.md`
- [ ] `20_lexikon_der_gewebe/AGENT.md`

## Zweck

Die Bücher und ihre Abschriften.

**Originalbilder und Buchinhalt sind unveränderlich.** Sie werden nur gelesen
und niemals retuschiert, verbessert oder überschrieben.

Die Transkripte dürfen und müssen dagegen gepflegt werden: Abschreibfehler
werden gegen das Original korrigiert, unlesbare oder widersprüchliche Stellen
markiert und Prüfstatus ergänzt. Jede Änderung bleibt originalgetreu und über
Git nachvollziehbar; der Buchinhalt wird dabei niemals umformuliert oder
fachlich verbessert.

Alles, was die Engine fachlich behauptet, stammt aus diesem Ordner und trägt
eine **Seitenzahl**. Was hier nicht belegt ist, gibt es für die Engine nicht.

| Ordner | Quelle |
|---|---|
| `10_hofenbitzer_b1` | Guido Hofenbitzer, *Grundschnitte und Modellentwicklungen. Schnittkonstruktion für Damenmode.* Europa-Lehrmittel. Band 1 (3. Auflage 2024), Band 2 (teilweise) |
| `20_lexikon_der_gewebe` | angelegt, noch leer |

## Grenze

| Nicht hier | Sondern |
|---|---|
| Formeln in Rechenform, Maßregister | `300_formeln/` |
| Begriffe und Abkürzungen | `000_sprache/` |
| Offene Fragen, Wer-ist-dran | `600_prozess/` |
| Fotos im Git | nirgends — `.gitignore` hält alle Bilder draußen |

Und die härteste Grenze: **Der Buchinhalt wird nie korrigiert.**
Ein vermuteter Buchfehler wird *markiert*, nicht ausgebessert. Was im Foto
steht, steht in der Abschrift — auch wenn es fachlich falsch erscheint. Nur eine
vom Original abweichende Abschrift wird korrigiert.

## Nummernschlüssel

Erste Stufe — ein Zehner pro Buch:

| Nummer | Buch |
|---|---|
| `10_` | Hofenbitzer |
| `20_` | Lexikon der Gewebe |

Weitere Bücher bekommen `30_`, `40_`. **Eine vergebene Nummer wird nie neu
belegt** — auch nicht, wenn ein Buch wieder verschwindet.

Zweite Stufe — in jedem Buchordner derselbe Aufbau:

| Ordner | Inhalt | Git |
|---|---|---|
| `1_Bilder/` | Fotos der Seiten, nach Seitenbereich gebündelt, dazu `index.md` — was wo steht | **draußen** |
| `2_transkript/` | Die Abschriften, nach Band getrennt | **drin** |

Grund für die Trennung: die Fotos sind rund 2,1 GB und gehören nicht ins Repo.
Die Transkripte **sind** die Quelle der Engine und dürfen nie verloren gehen.

## Form eines Eintrags

Eine Transkriptdatei heißt:

```
s<seiten>_<thema>_<stufe>.md
```

- `s172-181_184-187` — alle enthaltenen Seiten, Bereiche mit Bindestrich,
  Sprünge mit Unterstrich
- `<thema>` — nur wenn es hilft: `oberteil-grundschnitt`, `glockenrock`
- `<stufe>` — siehe Tabelle unten

Jede Datei nennt in der Kopfzeile: **Seiten, Stufe, wer sie erzeugt hat, Datum.**

## Drei Zustände — nicht verwechseln

| Zustand | Was passiert ist | Was er wert ist |
|---|---|---|
| **roh** | abgetippt, sonst nichts | Arbeitsmaterial |
| **digital geprüft** | eine zweite digitale Instanz hat Zeichen für Zeichen, Zahl für Zahl gegen die Originalfotos verglichen | *Transkriptionstreue* belegt — **nicht** die fachliche Richtigkeit |
| **freigegeben** | Werner oder Munkhuu hat die Seite **am physischen Buch** bestätigt | belegt |

Die digitale Prüfung ersetzt die menschliche nicht. Sie prüft, ob richtig
**abgeschrieben** wurde — nicht, ob die Konstruktion stimmt.

## Fertig-Regel

Eine Seite ist verwendbar, wenn:

1. sie **freigegeben** ist — digital geprüft allein reicht nicht,
2. ihre offenen Stellen (unlesbar, vermuteter Buchfehler, Widerspruch)
   in der Datei selbst markiert sind,
3. sie **nur einmal** transkribiert ist — Doppeltranskriptionen bekommen eine
   maßgebliche Datei, die andere verweist darauf.

**Nur eine freigegebene Seite darf einen Prüfwert tragen.**

Wer ein Transkript benutzt, nimmt die **Seitenzahl mit** — Korrekturen müssen
später jede Kopie finden können.

## Offene Stellen

Der Prüfstand steht in `10_hofenbitzer_b1/2_transkript/band_1_archiv/band_1/README.md`:
vermutete Buchfehler (A1–A6), unlesbare Stellen (B1–B7), der Doppel-Konflikt
S. 438/439 (C1) und die noch ausstehende digitale Zweitprüfung (D).
**Er wird dort gepflegt, nicht hier.**

Struktur, noch nicht aufgeräumt:

- `10_hofenbitzer_b1` heißt „b1", enthält aber auch `2_transkript/band_2/`
  — entweder Ordner zu `10_hofenbitzer` kürzen oder Band 2 herauslösen
- `20_lexikon_der_gewebe` ist leer — Buch oder Nummer wieder freigeben
- Namen gegen die Regel der obersten Ebene: `1_Bilder` (Großbuchstabe),
  `Photos-3-001 (4)` (Leerzeichen und Klammern), `…_ENTWURF.md` (Versalien)
- Vier Stufen-Endungen für drei Zustände: `rohtranskription`,
  `codex_transkription`, `codex_v2_mit_pruefstellen`, `ENTWURF` — eine
  einheitliche Benennung fehlt
