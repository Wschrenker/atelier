# Vergangenheit — warum wir es so entschieden haben

> **Git = was geändert wurde. Diese Datei = warum.**
> Kein zweites Änderungsprotokoll. Nur Entscheidungen und ihre Gründe.
> Wächst an, wird nie gekürzt.

---

## Chat 1 — 2026-08-19 · Werner + Claude (Coder)

### Richtung

| Entscheidung | Warum | Wer |
|---|---|---|
| **ATELIER ist Neuanfang. SANDAG / Engine 5.5 ist eingefroren.** | Bei 5.5 ging das Buch rein und ein Kleid raus. Saß das Kleid falsch, war nicht lokalisierbar, **warum**. Ohne Fachurteil ist jede Abweichung verhandelbar — damit gibt es kein „fertig". Die kleinste prüfbare Einheit war „ein Kleid", jetzt ist sie „eine Seite". | Werner |
| **Ziel ist ein definiertes Kleid, nicht das ganze Buch.** | Das Kleid ruft die Module ins Leben, nicht das Inhaltsverzeichnis. Nichts entsteht auf Vorrat, jedes Modul wird sofort im Ernstfall benutzt. Wenn das Kleid steht, ist der Scope zu. | Werner |
| **Kleid v001 = Tellerrock (S. 44) + asymmetrisches drapiertes Wickeloberteil (S. 423 ❑8).** | Ruhiger geometrischer Rock unter bewegtem Oberteil. Technisch: der einfachste Schnitt des Buchs unter dem schwierigsten. | Werner |
| **Grundlagen zuerst — S. 9, 11–15, 20, 21–31 — trotz Bedarfssteuerung.** | Bedarfsgetrieben heißt „keine Modelle auf Vorrat", nicht „Grundlagen überspringen". Die Begriffe müssen verstanden sein, die Konstruktion baut darauf auf, die Formeln sollen von Anfang an nachvollziehbar sein. | Werner |
| **Der gerade Rock S. 32–36 fällt aus dem kritischen Pfad.** | Ein Tellerrock braucht ihn nicht. Damit steht der einzige fachlich freigegebene Baustein nicht mehr auf dem Weg — bewusst in Kauf genommen, weil S. 44 sich über die eigenen Buchzahlen selbst prüft. | Folge der Kleidwahl |

### Fachliche Festlegungen

| Entscheidung | Warum | Wer |
|---|---|---|
| **Handumfang heißt `HdU` statt `HaU`.** | Das Buch schreibt Halsansatzumfang (S. 13) und Handumfang (S. 15) **beide** `HaU` — das ist korrekt so und kein Transkriptionsfehler. Für den Menschen über den Zusammenhang lösbar, für Code nicht. **Erste bewusste Abweichung vom Buch.** | Werner |
| **π wird exakt gerechnet, Buchwerte mit relativer Toleranz von 0,1 % geprüft.** | Das Buch rechnet mit 3,14. Die absolute Abweichung **wächst mit der Größe** (0,006 cm → 0,20 cm → 0,37 cm), die relative bleibt konstant bei 0,051 %. Eine feste Zentimetergrenze passt deshalb nie überall: 0,25 cm wird bei bodenlang knapp, 0,5 cm ließe bei kleinen Teilen echte Fehler durch. | Werner |
| **Die Schnittzeichen sind eine Ausgabe-Anforderung, kein Lernmaterial.** | Knips, Bohrloch, Fadenlauf, Stoffbruch und Beschriftung müssen im DXF und PDF stehen, sonst ist der Schnitt nicht produktionsfähig. | Werner |

### Struktur und Ordnung

| Entscheidung | Warum | Wer |
|---|---|---|
| **Transkripte kommen ins Git, nur Bilder bleiben draußen.** | 99 Transkriptions-Markdowns waren komplett ungesichert, obwohl teils fachlich freigegeben. Die Bildregel ist **global** und ohne Pfad (`*.jpg`), damit eine Ordner-Umbenennung sie nie wieder aushebelt. | Claude, bestätigt Werner |
| **Struktur folgt der Arbeitsrichtung: 100 Quellen → 200 Grundlagen → 300 Module → 400 Pattern.** | Die Quelle speist die Grundlagen, deshalb hat sie die kleinere Nummer. Ein Kleid ist keine Grundlage — `pattern` ist Geschwister von `grundlagen`, nicht Kind. | Werner |
| **Ein Modul liegt nie im Kleiderordner.** | Die Glockenrock-Formel gilt für **jeden** Kreisrock. Lag sie in `kleid_v001`, wüsste sie, zu welchem Kleid sie gehört. **Der Ort ist die erste Form von „wissen, wozu man gehört"** — die eiserne Regel auf Ordnerebene. | Werner |
| **Nummern nach Kontenplan-Logik: nie umgewidmet, nie umnummeriert.** | Werner denkt beruflich in Kontenplänen. Eine Ordnung, in der Nummern wandern, versteht nach einem Jahr niemand. Falsch einsortiert heilt man mit einer **neuen** Nummer. Lücken sind deshalb Absicht. | Werner |
| **`1000_übergabe` ist die einzige Ausnahme vom Dateischlüssel — und die Ausnahme steht neben der Regel.** | Dort bedeuten 777/888/999 eine Zeitachse statt Sachordnung. **Ungeschriebene Ausnahmen sind die, die Ordnungen kaputtmachen** — deshalb steht sie in `1_Hermes_AtelierAGENT.md` direkt unter der Regel, die sie bricht. | Werner |
| **Jeder Ordner trägt seine eigene `1_…AGENT.md`.** | Kontext in der Tiefe, in der gearbeitet wird — keine 160 Zeilen Projektphilosophie, um eine Formel einzupflegen. Was oben steht, wird unten nicht wiederholt. | Werner |
| **`CLAUDE.md` als Wegweiser im Wurzelordner.** | Claude Code lädt automatisch nur eine Datei dieses Namens. Ohne sie würden die `1_…AGENT.md`-Dateien in einer neuen Sitzung schlicht nicht bemerkt. | Claude, bestätigt Werner |

### Zusammenarbeit

| Entscheidung | Warum | Wer |
|---|---|---|
| **KI-Rollen sind offen benannt: Leader und Coder.** Hermes ist Leader, Claude derzeit Coder. | Die Rollen wechseln, die Konstellation bleibt. Deshalb liegt der gemeinsame Stand **im Repo, nicht im Chat** — sonst startet jede KI kalt. | Werner |
| **Mathe darf vorgecodet werden, Konstruktionen nicht.** | Mathe ist modeblind und kann das Verfahren nicht verfälschen. Entstünde Konstruktionscode schon beim Transkribieren, stünde der Code vor dem Prüfwert — und das Buch würde gegen den Code geprüft statt umgekehrt. Genau der Mechanismus, der 5.5 hervorgebracht hat. | Werner |
| **Ein eigener Agent wird erst gebaut, nachdem die Sache zweimal von Hand gemacht wurde.** | Vorher kodiert man eine Vermutung statt eines Könnens — derselbe Fehler wie ein Modul, das zu viel weiß. | Werner |
| **Zahlen → CSV. Regeln → Markdown mit Tabellen. Excel nur als Arbeitsoberfläche.** | Werner liest Matrizen, nicht Fließtext. Bei `.xlsx` zeigt Git nur „Datei geändert" — bei Prüfwerten muss aber nachvollziehbar sein, **wann und von wem** sich eine Zahl geändert hat. | Werner |
| **Drei Prüftore, keines ersetzt das andere:** Buchzahlen → CLO 3D → genäht. | CLO beweist nichts: ein in sich stimmiger, aber falscher Abnäher simuliert sauber. Würde CLO zum Prüfinstrument, wäre das alte Problem zurück. | Werner |
