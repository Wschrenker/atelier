# Formeln — was hier drin gilt

## Zweck

Was wir aus den Quellen ziehen: das **Maßregister** und die
**Konstruktionsformeln**.

In Rechenform, aber **nicht als Code**. Ein Eintrag hier ist für Werner und
Munkhuu lesbar und zugleich eindeutig genug, dass später Code daraus entsteht.

Merksatz: Hier steht, **wie gerechnet wird** — nicht, was die Kürzel bedeuten
(`000_sprache`), und nicht, wer es ausführt (`500_python`).

## Grenze

| Nicht hier | Sondern |
|---|---|
| Bedeutung eines Kürzels, Glossar | `000_sprache/` |
| Buchtext, ganze Seiten, Fotos | `100_quellen/` |
| Wie ein Lot, ein Kreis, ein Versatz rechnet | `400_mathematik/` — hier wird nur **benannt**, welche Primitive nötig sind |
| Python, Klassen, Tests | `500_python/` |
| Entscheidungen, die nur ein Kleid betreffen (`MoL = 105 cm`) | `700_schnitte/<kleid>/DEFINITION.md` |
| Wer wann prüft, Arbeitsstände | `600_prozess/` |

Beim Einpflegen entstehen **strukturierte Formeln, kein Code**. Konstruktionen
werden nicht vorgecodet — sonst wird am Ende das Buch gegen den Code geprüft
statt umgekehrt.

## Nummernschlüssel

Zehner = Bereich:

| Nummer | Bereich |
|---|---|
| `10_masse` | Maße und Maßberechnungen — gilt für alles darüber |
| `20_rock` | Rockkonstruktionen |
| `30_oberteil` | Oberteilkonstruktionen |

Weitere Bereiche: `40_`, `50_`. Innerhalb eines Bereichs laufen die Dateien
wieder in Zehnern (`10_MASSREGISTER.md`, `20_massberechnungen.md`).

**Eine vergebene Nummer wird nie neu belegt.**

## Form eines Eintrags

### Kopf jeder Datei

```markdown
**Quelle:** Buch, Band, Seiten
**Foto:** Pfad ins Bilderverzeichnis
**Transkript:** Pfad nach 100_quellen
**Begriffe:** siehe 300_formeln/10_masse/10_MASSREGISTER.md

Stand: JJJJ-MM-TT · eingepflegt durch …
Status: … · Fachliche Freigabe durch Werner/Munkhuu: …
```

### Ein Formelblock

```markdown
## F-<seite>-<lfd> · <Name>

- **Ergebnis:** was herauskommt, welche Art von Maß
- **Eingang:** welche Maße hineingehen
- **Formel:** wörtlich wie im Buch
- **Quelle:** Seite + Kasten oder Position
- **Prüfwert:** Beispielzahl des Buchs, nachgerechnet — oder „keine im Buch"
- **Mathematik:** welche Primitive nötig sind
- **Warum / Hinweis:** nur wenn die Formel es braucht
```

Die Kennung `F-44-1` ist **Buchseite + laufende Nummer auf dieser Seite**.
Sie bleibt, auch wenn die Datei umzieht oder umbenannt wird — Module und Tests
berufen sich später darauf.

### Zwei Sonderblöcke

| Zeichen | Block | Was er verlangt |
|---|---|---|
| ⚡ | **Bewusste Abweichung** | Das Buch sagt X, die Engine macht Y. Braucht Grund, Namen und Datum der Freigabe. |
| ⚠️ | **Offener Punkt** | Fachfrage ans Buch. Bleibt **bei der Formel** stehen, wird nicht ausgelagert. |

**Alles, was nicht unter ⚡ steht, folgt dem Buch.** Diese Umkehrung ist der
ganze Zweck des Blocks: eine Abweichung, die nirgends steht, gibt es nicht.

## Prüfwerte und Toleranz

Ein Prüfwert wird **relativ** verglichen, mit **0,1 %**:

```
|berechnet − Buchwert| ≤ 0,001 · Buchwert
```

Grund: das Buch rechnet mit `π = 3,14`. Daraus entsteht eine konstante
Abweichung von 0,051 % — unabhängig von der Größe des Teils. Eine feste
Zentimetergrenze passt nie über alle Größen: sie ist beim kleinen Teil zu grob
und beim bodenlangen Rock zu knapp.

Der Buchwert wird notiert, **wie er im Buch steht** (386,2 — nicht 386,22).

*Festlegung Werner, 19.08.2026 — siehe `20_rock/formel_rock_glocke.md`.*

## Fertig-Regel

Eine Formel ist fertig, wenn sie vier Dinge trägt:

1. **Seitenzahl** — welche Buchseite,
2. **Prüfwert** — die Beispielzahl des Buchs, nachgerechnet, oder ausdrücklich
   „keine im Buch",
3. **Mathematik** — welche Primitive sie braucht,
4. **Freigabestatus** — transkribiert, digital geprüft oder freigegeben.

Der Status wird vom Transkript **geerbt**. Ist die Seite nur
transkriptionsgeprüft, ist die Formel es auch — und kein Modul darf sich
darauf berufen.

**Ohne Prüfwert kein Code.** Und: nicht raten. Fehlt im Buch die
Verallgemeinerung, wird die zugehörige Seite eingepflegt, statt eine Formel zu
erfinden.

## Offene Stellen

Die **fachlichen** offenen Punkte stehen in den Dateien selbst, nicht hier:
`A1` (HaU/HdU), `P2` (zwei Wege zur Brustbreite), `P3`, `P4` im Maßregister,
die Saumweite bei Brautlänge im Glockenrock.

Struktur, noch nicht aufgeräumt:

- `20_rock/formel_rock_glocke.md` trägt keine Nummer → `10_formel_rock_glocke.md`
- `30_oberteil` ist leer
- `10_masse/10_MASSREGISTER.md` steht in Versalien
- Der Wurzeltext, der bis 2026-08-20 in dieser Datei stand (Ziel, Quelle,
  Grundlagen-Blöcke, „Phase jetzt"), gehört in die Wurzel oder nach
  `600_prozess` und ist noch nicht umgezogen.
