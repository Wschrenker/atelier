# Übergabe — was hier drin gilt

## Wozu dieser Ordner da ist

Ein Chat endet, ein neuer beginnt — mit einer KI, die nichts vom letzten Mal
weiß. Diese drei Dateien sind die Übergabe. Sie beantworten die drei Fragen,
die jemand hat, der neu dazukommt, Mensch wie KI.

| Datei | Frage | Regel |
|---|---|---|
| `777_vergangenheit.md` | Wo kommen wir her? | wächst an, wird nie gekürzt |
| `888_Gegenwart.md` | Woran arbeiten wir jetzt? | wird **überschrieben**, max. eine Seite |
| `999_zukunft.md` | Was steht im Raum? | jeder Eintrag mit Datum und Status |

Dieser Ordner ist **keine Arbeitsstufe**. Er steht neben der Kette
100 → 200 → 300 → 400, nicht darin. Deshalb die 1000.

## Diese Datei allein reicht nicht

> **Ist dieser AGENT geladen, werden `777` und `888` mitgelesen.**
> `999` nicht — es steht als eigene Zeile in der Ladeliste.

Das gilt nur für diesen Ordner. Die Ladeliste in `CLAUDE.md` entscheidet, **ob**
dieser AGENT geladen wird.

---

## 777 — Vergangenheit darf nicht zum zweiten Git werden

Git hat die vollständige Historie schon: jede Änderung, jede Datei, jeder
Zeitpunkt. Wenn `777` das nachbaut, entstehen zwei Wahrheiten und eine wird
falsch.

Was Git **nicht** kann, ist das **Warum**. Git zeigt perfekt, dass `HaU` zu
`HdU` wurde. Es zeigt nirgends, dass das Buch beide gleich schreibt, dass der
Mensch damit klarkommt und Code nicht — und dass das die erste bewusste
Abweichung des Projekts war.

> **Git = was geändert wurde. `777` = warum es entschieden wurde.**

Damit bleibt die Datei klein und wird nie überflüssig.

## 888 — Gegenwart wird überschrieben, nicht angehängt

Sonst ist sie nach drei Chats eine zweite Vergangenheit.
Eine Seite, immer aktuell. Was überholt ist, wandert nach `777` — **mit dem
Grund**, nicht nur mit dem Datum.

## 999 — Zukunft braucht Statusmarken, sonst wird sie gefährlich

Was dort steht, ist **nicht entschieden**. Die Gefahr: eine KI liest drei Chats
später „Prinzessnaht als v002" und behandelt es als Plan. Notiertes wirkt
beschlossen.

Deshalb trägt jeder Eintrag **Datum und Status**:

| Status | Bedeutung |
|---|---|
| `Idee` | einmal genannt, nicht geprüft |
| `erwogen` | besprochen, offen |
| `verworfen` | mit Grund — **gehört ausdrücklich hinein**, sonst schlagen wir es in vier Wochen wieder vor |

## Wann geschrieben wird

Bei jedem Chatwechsel. Wenn `777` zu groß wird, entscheiden wir dann, wie
geteilt wird — nicht vorher.



