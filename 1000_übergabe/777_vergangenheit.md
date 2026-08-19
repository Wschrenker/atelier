# Vergangenheit — warum wir es so entschieden haben

> **Git = was geändert wurde. Diese Datei = warum.**
> Wächst an, wird nie gekürzt.

---

## Chat 2 — 2026-08-19 · Werner + Claude · Thema: die eigenen `.md` aufräumen

| Entscheidung | Warum | Wer |
|---|---|---|
| **Antwort in vier Schichten: Vergangenheit → Gegenwart → Zukunft → Meta.** | Werner kam mit Lesen und Korrigieren nicht hinterher: auf Auftrag A lieferte die KI noch a.a, a.b und Befunde zu b und c. **Das ist die Quelle des Drifts** — nicht die Dokumente, sondern die Menge. Die Schicht *Zukunft* ist der Kasten fürs Beiwerk und darf übersprungen werden. | Werner |
| **Reihenfolge chronologisch, nicht nach Wichtigkeit.** | Sie ist dieselbe wie `777` → `888` → `999`. Ein Schema statt zwei. Nebengewinn: Probleme stehen vorn, nicht im Nachsatz. | Werner |
| **Ausnahme: wurde nichts getan, kommt nur *Meta*.** | Sonst vier Überschriften für einen Satz — das Gerüst würde zur Zeremonie. | Werner |
| **`CLAUDE.md` ist jetzt Ladeliste statt Wegweiser.** | Nur angekreuzte Dateien werden geladen. Kleiner Kontext erzwingt kurze Antworten — dieselbe Ursache wie oben, an der anderen Seite angefasst. Die alte Wegweiser-Fassung liegt in Commit `2714636`. | Werner |
| **Ladeliste trägt pro Zeile den vollen Dateipfad.** | „Grundlagen" ist mehrdeutig, ein Pfad nicht. | Claude, bestätigt Werner |
| **„Die eiserne Regel" bezeichnet nur noch eine Sache.** | Die Überschrift stand über zwei verschiedenen Regeln — in `1_Hermes_AtelierAGENT.md` über *nicht vorsorglich verallgemeinern*, in Grundlagen und Modul über *ein Modul darf nie wissen, welches Kleid gebaut wird*. **Eine doppelt belegte Überschrift ist derselbe Fehler wie eine umgewidmete Kontonummer.** Der zweite Name musste nicht erfunden werden — er stand in `1_Hermes_ModulAGENT.md` schon da. | Werner |
| **`888_Gegenwart.md` ist kein Statusregister mehr, sondern zeigt hin.** | Der Status stand vierfach (888, ROADMAP, GrundlagenAGENT, AtelierAGENT), die Blockaden dreifach. 888 und ROADMAP **widersprachen sich bereits** bei A1. Was nichts behauptet, kann mit nichts streiten. | Werner |
| **Zuständigkeit für Offenes: technische Abhängigkeit → `ROADMAP`, Fachfrage ans Buch → `999`, was Werner als Nächstes vorgelegt bekommt → `888`.** | Für Blockaden gab es als einziges keine Zuständigkeit — deshalb landeten sie überall. | Werner |
| **Alle `.md` werden klein neu geschrieben, nicht nachgebessert.** | Nachbessern erzeugt wieder Text zum Gegenlesen — neu anfangen ist billiger als korrigieren. Erst als `_v2` daneben geschrieben, dann an die Stelle der alten Dateien gesetzt. **Chat 1 steht damit nicht mehr in `777`** — bewusst in Kauf genommen, die Entscheidungen von Chat 1 liegen in Commit `2714636`. | Werner |
| **Auch `100_quellen` trägt eine `1_…AGENT.md`.** | Sie war der einzige Ordner ohne — die Ebenen-Regel gilt ausnahmslos. | Werner |
| **Verweis statt Kopie.** | Eine Kopie läuft still auseinander und niemand merkt es — so entstanden der vierfache Status und der A1-Widerspruch. Ein toter Verweis dagegen fällt sofort auf und ist billig zu finden. **Verweis erzeugt Abhängigkeit, Kopie erzeugt Widerspruch.** | Werner |
| **Vorgehen bei externer Änderung durch Werner:** er sagt Bescheid → KI liest → KI sucht, was daran hängt → Meldung unter *Meta* mit Stufe → KI ändert erst auf sein Wort. | Ohne Meldung schreibt die KI irgendwann über seine Arbeit, ohne dass es jemand merkt (*Lost Update*). Und er muss die Tragweite kennen, bevor er entscheidet. | Werner |
| **Stufen heißen folgenlos / nachziehen / Entscheidung — keine Ampelfarben.** | Rot, Gelb und Grün sind im Atelier schon als Modi vergeben. Ein Zeichen mit zwei Bedeutungen ist derselbe Fehler wie „Die eiserne Regel". | Claude, bestätigt Werner |
| **In die `1000er` wird nur auf den Befehl *Chatübergabe* geschrieben, nicht laufend.** | Sonst entsteht nebenher Text, den Werner gegenlesen muss — genau der Drift, den wir abstellen. | Werner |
