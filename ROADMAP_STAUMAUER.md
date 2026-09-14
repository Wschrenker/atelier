# Roadmap Staumauer — vom verstandenen Kontext zum real geprüften Schnittmuster

> **Status:** Arbeitsroadmap, angelegt am 13. September 2026  
> **Ort:** `C:\ATELIER\ROADMAP_STAUMAUER.md`  
> **Eigentümer der Richtung und fachlichen Wahrheit:** Werner  
> **Koordination, Abgrenzung und unabhängige Prüfung:** Hermes  
> **Technische Ausführung begrenzter Werkstücke:** Claude Code  
> **Erste mögliche Öffnung:** der gerade Rock; erst nach ausdrücklicher Bestätigung  

## 1. Warum diese Roadmap existiert

Die letzten Tage fühlten sich nicht wie Vorwärtsarbeit an, weil viele richtige
Einzelteile vorhanden waren, aber der tragende Zusammenhang fehlte. Diese
Roadmap macht diesen Zusammenhang sichtbar.

Das Bild dafür ist eine **Staumauer**:

- Hinter der Mauer liegt viel wertvolles Wasser: Buchwissen, Bilder, Formeln,
  Prüfstellen, Sprache, Mathematik, vorhandener Code und praktische Erfahrung.
- Ohne Ordnung drückt alles gleichzeitig auf die Arbeit. Eine KI kann dann
  schnell viel erzeugen, aber nicht zuverlässig unterscheiden, was fachlich
  wahr, nur vermutet oder noch unverstanden ist.
- Die Mauer soll das Wissen nicht blockieren. Sie soll es halten, ordnen und
  durch klar gebaute Öffnungen kontrolliert in funktionierende Werkstücke
  leiten.
- Jede Öffnung ist ein vollständiger, begrenzter Arbeitsweg von der verstandenen
  Quelle bis zum digital und später real geprüften Schnittmuster.

Diese Roadmap ist deshalb **kein Ersatz für Vorwärtsarbeit**. Sie ist fertig,
wenn eine neue Session den ersten vollständigen Arbeitsweg sicher beginnen
kann. Danach darf die Planung nicht weiter wachsen, nur weil noch weitere
Ordnung denkbar wäre.

---

## 2. Rolle dieser Datei

Diese Datei beantwortet eine einzige Hauptfrage:

> **In welcher Reihenfolge bauen und prüfen wir die Staumauer und wie öffnen wir
> danach den ersten vollständigen Arbeitsweg?**

Sie ist:

- die gemeinsame Navigation für Folgesessions;
- die Reihenfolge der noch zu klärenden Bauteile;
- eine sichtbare Grenze gegen Überorganisation;
- ein Verzeichnis der Prüf- und Entscheidungstore;
- der Ort für den aktuellen Gesamtstand und den nächsten gemeinsamen Schritt.

Sie ist **nicht**:

- die fachliche SSOT für eine Buchregel;
- ein Ersatz für die lokale `AGENT.md`-Kette;
- ein Sammelplatz für alle Formeln, Quellen oder Entscheidungen;
- ein Auftrag, sofort alle hier genannten Dokumenttypen anzulegen;
- eine technische Spezifikation für jeden späteren Schnitt;
- ein Beweis, dass vorhandener Code fachlich oder real geprüft ist.

Eine aktuelle ausdrückliche Aussage von Werner steht immer über dieser Roadmap.
Ändert Werner die Richtung, wird die Roadmap bewusst angepasst; die Änderung
wird nicht stillschweigend aus Agentenannahmen abgeleitet.

---

## 3. Zielbild

`C:\ATELIER` soll eine beliebig erweiterbare, aber verständlich bleibende
Arbeitsumgebung für ein fachlich und technisch verlässliches
Schnittmusterprogramm werden.

Ein späterer vollständiger Durchfluss sieht so aus:

```text
Werner versteht und entscheidet
    ↓
Buchseite, Bild und Prüfstelle sind eingeordnet
    ↓
Fachbegriffe und Abkürzungen sind eindeutig
    ↓
Fachregel oder offene Entscheidung ist sichtbar
    ↓
benötigter modeblinder Mathematikvertrag ist bekannt
    ↓
begrenzte Python-Funktion wird gebaut
    ↓
technische Tests und Hermes-Prüfung
    ↓
maßstäbliche Ausgabe in SVG / PDF / DXF
    ↓
CLO-3D-Prüfung
    ↓
Nessel, Nähen und reale Anprobe
    ↓
Werner entscheidet: bestätigen, korrigieren, parken oder verwerfen
    ↓
Git hält den akzeptierten technischen Zeitpunkt fest
```

Das System soll dabei jederzeit unterscheiden können zwischen:

1. **Idee**;
2. **von Werner getroffener Entscheidung**;
3. **fachlich verstandener und belegter Aussage**;
4. **technisch implementiertem Kandidaten**;
5. **digital geprüftem Ergebnis**;
6. **in CLO plausibilisiertem Ergebnis**;
7. **physisch genähtem und angeprobtem Ergebnis**;
8. **von Werner real akzeptiertem Stand**.

Keine niedrigere Stufe darf sich automatisch als höhere ausgeben.

---

## 4. Unverhandelbare Bauprinzipien

### 4.1 Werner bleibt die oberste Entscheidungsinstanz

Werner bestimmt:

- was gebaut wird;
- welche fachliche Lesart gilt;
- welche Unklarheit offen bleibt;
- welche reale Wirkung akzeptiert wird;
- wann ein Versuch beendet, geändert oder verworfen wird.

Hermes und Claude dürfen Vorschläge machen. Sie dürfen eine fachliche
Entscheidung aber nicht unbemerkt ersetzen.

### 4.2 Verstehen kommt vor Automatisieren

Bilder oder Buchseiten werden nicht pauschal mit dem Auftrag „KI, mach, dass es
funktioniert“ übergeben. Vor der technischen Arbeit wird der benötigte Kontext
so weit verstanden, dass mindestens sichtbar ist:

- was das Buch ausdrücklich sagt;
- welche Aussage aus einem Bild stammt;
- welche Prüfstelle existiert;
- was Werner verstanden und bestätigt hat;
- was mathematisch allgemein gilt;
- was nur ein technischer Vorschlag ist;
- was weiterhin offen bleibt.

### 4.3 Eine Frage hat einen Besitzer

Eine fachliche oder technische Frage erhält genau einen maßgeblichen Besitzer.
Andere Dateien verlinken auf diesen Besitzer, statt seine Antwort zu kopieren.
Damit wird eine Änderung an einer Stelle vorgenommen und nicht in mehreren
abweichenden Fassungen.

### 4.4 Die Ordnernummer ist eine dauerhafte Adresse

Die Benennung folgt
[`Benennung der Stufen, Ordner und Dateien.md`](Benennung%20der%20Stufen,%20Ordner%20und%20Dateien.md).

- Die Ziffernbreite zeigt die Tiefe.
- Zehner-Lücken erlauben spätere Einschübe.
- `_zz_`, `_zza_`, `_zzb_` und weitere Überlaufgruppen erlauben Wachstum, ohne
  vorhandene Adressen erneut umnummerieren zu müssen.
- Datei und Ordner folgen auf derselben Stufe derselben Logik.
- Eine neue Ebene entsteht nur für eine echte fachliche, technische oder
  organisatorische Grenze.

Die derzeit noch vorhandenen alten Verweise nach der großen Umbenennung sind
eine Übergangsarbeit. Ihre spätere Korrektur ist ein eigener begrenzter Schritt
und darf nicht die inhaltliche Staumauerplanung verschlucken.

### 4.5 Nicht jedes Bauteil braucht eine eigene Datei

Zuerst wird die notwendige **Verantwortung** bestimmt. Erst danach wird
entschieden, ob sie:

- bereits von einer vorhandenen Datei getragen wird;
- als Abschnitt in einen bestehenden Besitzer gehört;
- wirklich eine neue Datei benötigt;
- nur eine zeitweilige Gesprächsfrage ist und gar nicht dauerhaft gespeichert
  werden muss.

### 4.6 Kleinste vollständige Öffnung vor flächigem Ausbau

Wir bauen nicht vorsorglich alle Kapitel, alle Exporte, eine vollständige
CAD-Bibliothek oder jede denkbare Agentenregel. Wir öffnen zuerst einen einzigen
vollständigen Weg. Erst seine tatsächliche Benutzung zeigt, welche Bauteile der
Mauer tragen und welche nur zusätzliche Verwaltung wären.

---

## 5. Die Bauteile der Staumauer

Jedes Bauteil wird gemeinsam nach demselben Schema geprüft:

1. Welche Frage beantwortet es?
2. Wer besitzt die Antwort?
3. Welche Eingaben erhält es?
4. Was gibt es weiter?
5. Wo muss es bei Unklarheit stoppen?
6. Wodurch wird seine Funktion nachgewiesen?
7. Welche vorhandene Datei besitzt es bereits?
8. Braucht es überhaupt eine neue Datei?

### 5.1 Baugrund — Ziel und reale Abnahme

**Frage:** Wofür wird die gesamte Anlage gebaut?

Der Baugrund ist nicht „möglichst viel Code“, sondern ein Schnittmusterprogramm,
das aus belegten Fachregeln kontrollierbare Schnittteile erzeugt. Seine
Ergebnisse müssen am Ende nähbar, prüfbar und für die reale Atelierarbeit
nützlich sein.

**Zu formulieren:**

- dauerhaftes Produktziel;
- wirtschaftlicher und handwerklicher Nutzen;
- Verhältnis von Buchtreue, individueller Anpassung und Gestaltung;
- welche Ausgaben langfristige Ziele sind;
- welche reale Prüfung für welche Produktstufe notwendig ist.

**Für die erste Öffnung festgelegt (Werner, 14. September 2026):**

- Erstes vollständiges Werkstück ist ein digitaler und physischer gerader Rock,
  der aus freigegebenen Körpermaßen ein Schnittmuster erzeugt.
- Größe 38 ist die bewusst gewählte, globale Ausgangsbasis für den Code aller
  Schnittmuster; sie ist keine Begrenzung auf Größe 38.
- Mindesteingaben sind Taille, Hüfte und Rocklänge. Weitere Maße werden nur
  ergänzt, wenn sie fachlich nachweisbar nötig sind; fehlende Maße werden nicht
  geschätzt. Werner gibt Maße frei.
- Ein lokales Bedien-Modul zeigt eine Rockskizze und bietet feste, keine frei
  verschiebbaren Wahlen: zwei Abnäher vorn und/oder zwei Abnäher hinten;
  Verschluss keine / Reißverschluss / Knopf / Reißverschluss und Knopf; Position
  Seite oder hinten.
- Das Werkstück erzeugt SVG, PDF und DXF. DXF dient dem bereits erprobten Import
  in CLO 3D.
- Buchtreue gilt. Eine Ableitung bei Buchfehlern oder technischen Grenzen braucht
  Werners ausdrückliche Entscheidung.
- Der erste reale Durchfluss näht und beurteilt eine bewusst gewählte
  Referenzvariante als Nessel in Größe 38. Alle vereinbarten Varianten müssen im
  Bedien-Modul wählbar sein. Vor der Akzeptanz wird die Referenzvariante
  mindestens in einer weiteren Größe ebenfalls als Nessel genäht und anprobiert.
- Zielnutzen ist verlässlich entwickelte Maßkleidung: gezieltere Stoffbestellung,
  Proben, Fotografie, Werbung und Verkauf werden dadurch möglich.

**Reale Abschlussfrage:** Ein gerader Rock ist akzeptiert, wenn er von der
Grundbasis Größe 38 aus anhand freigegebener Körpermaße berechnet, im
Bedien-Modul in seinen vereinbarten Varianten gewählt, als SVG/PDF/DXF
reproduzierbar ausgegeben, in CLO 3D geprüft und als Nessel in Größe 38 sowie
mindestens einer weiteren Größe passend anprobiert wurde.

**Hält, wenn:** Jede technische Entscheidung auf ein sichtbares Produktziel und
eine reale Prüfart zurückgeführt werden kann.

### 5.2 Bauherr — Entscheidungs- und Wahrheitsordnung

**Frage:** Wer darf welche Wahrheit ändern?

Die Grundordnung lautet:

```text
Werner / Munkhuu → Hermes → Claude Code → technische Tests → CLO / Nessel → Werner / Munkhuu
```

- Werner und Munkhuu entscheiden Richtung und fachliche Wirklichkeit.
- Hermes übersetzt Entscheidungen in begrenzte Arbeit, schützt den Zusammenhang
  und prüft unabhängig.
- Claude Code baut ein klar abgegrenztes technisches Werkstück.
- Tests bestätigen nur ihren technischen Prüfbereich.
- CLO und Nessel liefern fachliche und physische Beobachtungen.
- Werner oder Munkhuu entscheiden, was diese Beobachtungen für den nächsten Stand
  bedeuten.

**Für die erste Öffnung festgelegt (Werner, 14. September 2026):**

- Werner und Munkhuu sind gleichberechtigte Bauherren. Beide dürfen fachliche,
  technische und reale Entscheidungen treffen sowie einen technischen Git-Stand
  jeweils allein freigeben. Munkhuu schneidert; Werner verantwortet Büro, KI und
  Stick.
- Hermes darf einen klar abgegrenzten Claude-Auftrag auslösen, wenn dessen
  Voraussetzungen, erlaubter Datei-Scope und fachliche Entscheidungen sichtbar
  sind. Hermes legt bei Unklarheit einen eigenen Vorschlag mit Begründung vor.
- Claude darf die interne technische Umsetzung und Tests innerhalb seines engen
  Auftrags selbst entscheiden. Er darf keine Fachregel, Produktgrenze oder
  Architekturentscheidung erweitern.
- Bei Widerspruch oder fehlender fachlicher Entscheidung stoppt Claude, berichtet
  konkret und baut keine Annahme weiter. Der Bericht geht an Hermes; Hermes und
  ein berechtigter Bauherr entscheiden den nächsten Auftrag.
- Technische Tests belegen nur die vereinbarte technische Regel. CLO, Nessel und
  Anprobe sind Beobachtungen, keine automatische Codeänderung. Ihre Bedeutung
  entscheidet Werner oder Munkhuu.
- Ein nicht passender Versuch bewahrt den letzten technisch funktionierenden
  Stand. Ein neuer Versuch entsteht sichtbar daneben; ein akzeptierter Stand wird
  nicht still überschrieben.

**Hält, wenn:** Kein Agentenergebnis ohne sichtbare Entscheidungskette zur neuen
fachlichen Wahrheit wird.

### 5.3 Wasserzulauf — Quellen und Erfahrung

**Frage:** Welches Material darf fachliche Aussagen speisen?

Mögliche Zuläufe sind:

- Buchtext;
- Buchbild;
- Buchformel;
- Sachwortverzeichnis und Abkürzungssystem;
- normalisierte Fachformeln;
- Prüfstellen und Transkriptionshinweise;
- Werners fachliches Verständnis;
- Erfahrung der Schneiderin;
- CLO-Beobachtung;
- Nessel, Anprobe und reales Nähen.

Diese Zuläufe haben unterschiedliche Autorität. Ein Bild kann eine Form zeigen,
ohne eine exakte Kurvenformel zu liefern. Ein grüner Test kann eine Rechnung
bestätigen, ohne den Sitz am Körper zu beweisen.

**Für die erste Öffnung festgelegt (Werner, 14. September 2026):**

- Hofenbitzer ist die fachliche Hauptquelle für die erste Rock-Konstruktion. Bei
  abweichender oder mehrdeutiger Lesart hat das Buchbild Vorrang vor dem Buchtext.
- Munkhuus Schneiderpraxis darf eine Buchregel ersetzen. Die ursprüngliche
  Buchregel bleibt als Quelle erhalten; die Abweichung wird getrennt mit ihrem
  Grund als Entscheidung festgehalten.
- CLO, Nessel und Anprobe liefern Beobachtungen, zum Beispiel „an der Hüfte zu
  eng“. Sie sind nicht selbst eine neue Konstruktionsregel.
- Später dürfen weitere sorgfältig von Werner ausgewählte Fachquellen,
  beispielsweise zu Corsett oder Corsage, als gleichwertige Fachquellen dienen.
- Jede wichtige Aussage trägt ihre Herkunft: Buchseite, Munkhuus Schneiderpraxis,
  Werner-/Munkhuu-Entscheid, CLO-/Nessel-Beobachtung oder technischer Vorschlag.
- Bei Unklarheit wird situativ entschieden, ob Codierung stoppt oder ein klar als
  Kandidat markierter Versuch gebaut wird. Diese Entscheidung bleibt bei Werner
  oder Munkhuu; sie darf weder Quelle noch Fachregel still ersetzen.

**Hält, wenn:** Jede wichtige Aussage erkennen lässt, aus welchem Zulauf sie
stammt und wie weit dieser Zulauf sie tatsächlich trägt.

### 5.4 Einlaufkontrolle — Werners seitenweise Kontextarbeit

**Frage:** Ist der benötigte Ausschnitt des Quellwissens bereit für technische
Arbeit?

Das ist Werners bewusstes Vorhaben vor der ersten Öffnung. Es besteht nicht nur
aus dem Einfügen von Bildern. Pro benötigter Seite oder zusammengehörigem
Abschnitt werden nach Möglichkeit geklärt:

- Seitenzweck im Gesamtzusammenhang;
- wörtliche oder verlässlich übertragene Buchaussage;
- Bedeutung der Abbildung;
- zugehörige Konstruktionsschritte;
- Fachbegriffe und Abkürzungen;
- Maße, Werte, Bereiche und Wahlmöglichkeiten;
- Formeln und Rechenbeziehungen;
- Abhängigkeit von vorherigen oder späteren Seiten;
- bekannte Prüfstelle;
- Widerspruch, Druckfehler oder Transkriptionsunsicherheit;
- Werners Verständnis;
- ausdrücklich offene Frage;
- mögliche technische Folge, noch ohne sie vorwegzunehmen.

**Möglicher kompakter Prüfblock pro Seite:**

```text
Seite / Bereich:
Zweck:
Buchaussage:
Bildbedeutung:
Fachbegriffe:
Maße / Werte / Bereiche:
Formeln / Beziehungen:
Abhängigkeiten:
Prüfstelle:
Werner versteht es so:
Noch offen:
Bereit für Technik: ja / nein / teilweise
```

**Hält, wenn:** Die KI benennen kann, was belegt, entschieden, vorgeschlagen und
offen ist, ohne Lücken mit plausiblen Annahmen zu füllen.

### 5.5 Grundriss — Nummerierung und Hierarchie

**Frage:** Wie bleibt jeder Arbeitsort auch bei starkem Wachstum auffindbar?

Die Hierarchie ist eine visuelle Adresse:

```text
ATELIER-Dach
└── Hunderter: großer Verantwortungsbereich
    └── Zehner: Hauptgruppe
        └── Einer: fachlich begrenzter Abschnitt
            └── Zehntel: Arbeitsschritt oder Unterfunktion
                └── Hundertstel: nur bei einer weiteren echten Grenze
```

**Zu prüfen:**

- Jede Ebene besitzt eine echte Aufgabe.
- Die Tiefe ist am Namen ablesbar.
- Direkte Kinder sind im zuständigen `AGENT.md` sichtbar.
- Ein späterer Einschub erzwingt keine Umbenennung bestehender Nachbarn.
- Überlaufgruppen bleiben verständlich.
- Pfade sind Adressen, keine fachliche Wahrheit.

**Hält, wenn:** Neue Bereiche eingefügt werden können, ohne die bestehende
Arbeitswelt wieder umzubauen.

### 5.6 Mauersegmente — Verantwortungsbereiche

Der gegenwärtige Grundfluss ist:

| Segment | Hauptverantwortung |
|---|---|
| `000_sprache/` | Fachwörter, Symbole, Abkürzungen und sprachliche Eindeutigkeit |
| `100_quellen/` | Buchfassung, Bilder, Prüfstellen und fachliche Provenienz |
| `200_funktionen/` | konkrete fachliche Zusammensetzung, Python-Funktionen und zugehörige Tests |
| `400_mathematik/` | modeblinde Rechen- und Geometrieverträge |
| spätere Ausgabeschicht | SVG, PDF, DXF, JSON und ihre Formatverträge |
| Prozess-/Prüfschicht bei echtem Bedarf | Aufträge, Verifikation, Übergaben und bedeutende Prüfprotokolle |
| `800_werners spick/` | Werners Denk- und Orientierungsmodelle; nicht automatisch geltende Regel |

**Hält, wenn:** Kein Segment still die Autorität eines anderen übernimmt.

### 5.7 Bewehrung — `AGENT.md`-Kette

**Frage:** Welche Grenzen und direkten Kinder gelten am tatsächlichen
Arbeitsort?

Die Ladeweise soll hierarchisch bleiben:

1. `C:\ATELIER\AGENT.md`;
2. `AGENT.md` des aktiven Hunderters;
3. `AGENT.md` des aktiven direkten Kindes;
4. tiefer nur entlang des tatsächlich bearbeiteten Pfads.

Ein lokales `AGENT.md` besitzt:

- Aufgabe des Ordners;
- harte Grenzen;
- direkte Kinder;
- Ladeweise oder Übergang zum nächsten Kind;
- nur Regeln, die in seinem ganzen Bereich gelten.

Es besitzt nicht:

- die komplette Fachwahrheit;
- kopierte Regeln aller Eltern;
- den Status jeder einzelnen Datei;
- eine flächige Liste des gesamten Repositorys.

**Hält, wenn:** Eine neue Session mit wenigen Dateien den richtigen Arbeitsraum
und seine Grenzen versteht.

### 5.8 Fugen — Schnittstellen zwischen den Segmenten

**Frage:** Was darf von einem Segment zum nächsten übergeben werden?

#### Quelle → Sprache

- Fachbegriff;
- genaue Bedeutung im Buchkontext;
- Schreibweise und Abkürzung;
- offene Mehrdeutigkeit.

#### Quelle → Mathematik

- fachlich festgelegte Eingaben und Ausgaben;
- belegte Beziehung oder Operation;
- Einheit;
- erlaubter Bereich;
- fachlich offene Wahl.

Die Mathematik darf daraus keine neue Buchregel erfinden.

#### Mathematik → Funktion

- allgemeiner Rechen- oder Geometrievertrag;
- Eingabe- und Ausgabetypen;
- Einheiten und Koordinatensystem;
- Sonderfälle und typisierte Fehler;
- Invarianten und Prüffälle.

#### Funktion → Ausgabe

- vollständige, endliche Geometrie;
- getrennte Nahtlinie, Schnittlinie und genähter Zustand;
- Teile, Markierungen, Fadenlauf, Beschriftung und Provenienz;
- sichtbare Wahlwerte und Überschreibungen.

#### Ausgabe → reale Prüfung

- eindeutiger Git- oder Kandidatenstand;
- verwendete Maße und Wahlwerte;
- reproduzierbare Datei;
- definierte Beobachtungsfragen;
- Rückmeldung ohne automatische Umdeutung zur Entscheidung.

**Hält, wenn:** Jede Übergabe ein benennbares Paket ist und keine Seite
heimlich Wissen aus einem fremden Segment ergänzt.

### 5.9 Eine Wahrheit pro Frage — SSOT-Verteilung

**Frage:** Wo wird eine bestimmte Antwort dauerhaft geändert?

Vor dem Anlegen neuer Dokumente wird für jede wichtige Frage bestimmt:

| Frage | Möglicher Besitzer |
|---|---|
| Wie arbeiten wir mit Werner und Unsicherheit? | ein kurzer globaler Zusammenarbeitsvertrag, falls wirklich nötig |
| Was gilt fachlich zu einem konkreten Thema? | niedrigste passende fachliche SSOT |
| Welche Grenzen gelten in einem Ordner? | lokales `AGENT.md` |
| Was bauen wir in diesem Arbeitszug? | zeitlich begrenzter Scope |
| Was muss das Werkstück leisten? | konkrete Spec |
| Was soll Claude jetzt tun? | konkreter Prompt oder direktes Auftragspaket |
| Was behauptet Claude getan zu haben? | Ergebnisbericht, nur bei bedeutender Arbeit dauerhaft |
| Was wurde beobachtet? | Learning oder Prüfprotokoll beim niedrigsten Besitzer |
| Was ist jetzt der nächste Gesamtschritt? | diese Roadmap oder ein später wirklich benötigter kurzer Handoff |
| Was wurde technisch festgehalten? | Git |

**Hält, wenn:** Eine Änderung nicht in mehreren gleichrangigen Dateien gesucht
und nachgeführt werden muss.

### 5.10 Kontrollraum — Hermes

**Frage:** Wie wird aus Werners Wahrheit ein sicherer, ganzer Arbeitszug?

Hermes soll:

- die zuständige SSOT und lokale Regelkette finden;
- die kleinste vollständige Aufgabe abgrenzen;
- Voraussetzungen vor dem Auftrag prüfen;
- Ideen, Entscheidungen und Implementierung auseinanderhalten;
- Claude einen selbstständigen, begrenzten Bauauftrag geben;
- dessen Bericht nicht ungeprüft übernehmen;
- Diff, Code, Tests und Artefakte unabhängig prüfen;
- Widersprüche und fehlende Voraussetzungen früh nennen;
- den Gesamtzusammenhang bewahren;
- Werner nur die Entscheidung zurückgeben, die wirklich seine fachliche
  Autorität benötigt.

Hermes soll nicht:

- selbstständig Fachwahrheit erfinden;
- Claude mit dem ganzen Repository als offenem Problem losschicken;
- aus einem grünen Test reale Passform ableiten;
- jedes gute Gespräch sofort in neue Dokumente verwandeln;
- ohne frisches `#` committen, pushen, löschen, verschieben, herunterladen oder
  veröffentlichen.

**Hält, wenn:** Werner Richtung geben kann, ohne jeden technischen Einzelschritt
selbst überwachen zu müssen.

### 5.11 Bauarbeiter — Claude Code

**Frage:** Wie wird ein begrenztes technisches Werkstück ausgeführt?

Claude erhält nur:

- Ziel und Ausgangspunkt;
- zuständige Regeln und Spec;
- exakt erlaubten Datei-Scope;
- benötigte Quellen- und Mathematikverweise;
- erwartete Eingaben und Ausgaben;
- Tests und Akzeptanzgrenzen;
- Stopps bei Widerspruch oder fehlender Entscheidung;
- Auftrag zum Bericht über Änderungen, Tests, offene Punkte und Nichtgetanes.

Claude entscheidet nicht selbst über:

- neue fachliche Wahrheit;
- großflächige Architekturänderungen;
- zusätzliche Produktziele;
- Umorganisation außerhalb seines Scopes;
- Commit und Push ohne Werners dafür geltende Freigabe.

**Hält, wenn:** Claude schwere technische Arbeit selbstständig erledigen kann,
ohne den fachlichen oder organisatorischen Fluss umzuleiten.

### 5.12 Schleusenplan — Scope und Spec

**Frage des Scopes:** Woran arbeiten wir jetzt, und was ausdrücklich nicht?

**Frage der Spec:** Was muss das konkrete Werkstück leisten, und woran wird es
angenommen?

Ein Scope sollte enthalten:

- aktives Ziel;
- enthaltene Bereiche;
- ausgeschlossene Bereiche;
- Ausgangsstand;
- Abhängigkeiten;
- Stopps;
- Abschlussbedingung.

Eine Spec sollte enthalten:

- fachliches Ergebnis;
- Inputs und Wahlwerte;
- Outputs;
- belegte Regeln;
- offene Entscheidungen;
- Fehler- und Grenzfälle;
- technische Akzeptanz;
- digitale und reale Abnahme;
- klaren Nichtumfang.

Nicht jeder kleine Arbeitsschritt benötigt zwei neue Dateien. Bei kleinem Umfang
können Scope und Spec in einem vorhandenen Besitzer oder im Auftragspaket klar
genug enthalten sein.

**Hält, wenn:** Vor dem Bauen sichtbar ist, wann das Werkstück fertig ist und
wann der Arbeiter stoppen muss.

### 5.13 Schleusentor — konkretes Auftragspaket

**Frage:** Was darf bei genau dieser Öffnung jetzt hindurch?

Ein belastbares Auftragspaket für Claude enthält mindestens:

```text
Ziel:
Ausgangsstand:
Verbindliche Besitzer / Quellen:
Erlaubte Dateien:
Verbotene Bereiche:
Eingaben:
Erwartete Ausgaben:
Technische Verträge:
Akzeptanztests:
Stopps und Rückfragen:
Was nicht getan werden darf:
Erwarteter Ergebnisbericht:
```

**Hält, wenn:** Ein neuer technischer Arbeiter den Auftrag ohne freien
Architekturentwurf ausführen und ohne fachliches Raten stoppen kann.

### 5.14 Rückschlagventile — Schutz vor falschem Fluss

Notwendige Ventile sind:

- Unklarheit wird als Unklarheit zurückgegeben.
- Fehlende Entscheidung erzeugt keinen versteckten Standard.
- Unmögliche oder entartete Geometrie erzeugt einen typisierten Zustand oder
  Fehler, keinen erfundenen Ersatzpunkt.
- Nahtlinie, Schnittlinie und genähter Zustand bleiben getrennt.
- Ein Worker schreibt nur in seinem erlaubten Scope.
- In einem gemeinsamen Worktree gibt es nur einen Schreiber.
- `#` ist frisch, einmalig und nur für den unmittelbar besprochenen geschützten
  Schritt gültig.
- Fachquellen werden nicht als Nebenwirkung technischer Arbeit verändert.
- Persönliche Maße und private Daten werden nicht unnötig vervielfältigt oder
  veröffentlicht.

**Hält, wenn:** Ein Fehler sichtbar stoppt, bevor er sich durch mehrere Schichten
als scheinbar fertiges Ergebnis fortsetzt.

### 5.15 Messinstrumente — technische und fachliche Nachweise

Jede Prüfart beantwortet nur ihre eigene Frage:

| Nachweis | Beantwortet |
|---|---|
| Quellprüfung | Ist die fachliche Aussage korrekt gelesen und belegt? |
| Rechenbeispiel | Stimmt die ausdrücklich geprüfte Beziehung für diese Werte? |
| Unit-Test | Verhält sich eine kleine Funktion im getesteten Bereich korrekt? |
| Invariantentest | Bleiben notwendige geometrische Eigenschaften erhalten? |
| Integrationstest | Arbeiten mehrere Bausteine im definierten Ablauf zusammen? |
| visueller Vergleich | Ist die erzeugte Form für den betrachteten Fall plausibel? |
| PDF-Prüfmaß | Ist die physische Skalierung der Ausgabe korrekt? |
| DXF/CLO | Ist die Datei technisch lesbar und digital als Schnittteil brauchbar? |
| Nessel / Nähen | Ist das Teil herstellbar und verhält es sich im Material? |
| Anprobe | Funktioniert es am realen Körper für das beabsichtigte Ziel? |
| Werner | Wird die beobachtete Wirkung akzeptiert oder geändert? |

**Hält, wenn:** Kein Nachweis stärker benannt wird, als seine tatsächliche
Prüfgrenze erlaubt.

### 5.16 Überlauf — Ideen und offene Fragen

Neue Ideen werden nicht unterdrückt. Sie werden aber nicht automatisch Teil des
aktiven Flusses.

Jede neue Idee erhält zunächst nur:

- kurze Bezeichnung;
- Nutzen oder erwartete Wirkung;
- Bezug zum aktiven Ziel;
- Status `Idee`, `offen`, `später`, `verworfen` oder `von Werner aktiviert`;
- Aktivierungsauslöser, wenn bekannt.

Eine eigene `IDEAS.md` wird erst angelegt, wenn die Zahl und Wiederkehr der Ideen
einen echten Besitzer nötig machen. Bis dahin können wenige offene Punkte in
der zuständigen Spec oder Roadmap bleiben.

**Hält, wenn:** Gute Gedanken nicht verloren gehen, aber den aktuellen
Arbeitsweg auch nicht ungefragt verändern.

### 5.17 Bautagebuch — Entscheidungen und Erkenntnisse

Entscheidungen und Beobachtungen sind verschieden:

- **Entscheidung:** Werner legt fest, was gelten oder als Nächstes geschehen
  soll.
- **Erkenntnis:** Ein Test, CLO, eine Schneiderin oder ein reales Stück zeigt
  etwas Beobachtbares.

Eine Erkenntnis wird nicht automatisch zur Entscheidung. Sie enthält:

- Gegenstand;
- Ausgangsstand;
- Beobachtung;
- Beleg oder Artefakt;
- Reichweite;
- Unsicherheit;
- mögliche Folge;
- Werners spätere Entscheidung.

Dauerhafte Register entstehen nur dort, wo mehrere relevante Einträge wirklich
zusammengeführt werden müssen.

### 5.18 Wartungsmarken — Git

Git ist die technische Nachweisschicht:

- Working Tree: aktueller Kandidat;
- Diff: konkrete Veränderung;
- Commit: bewusst festgehaltener technischer Zeitpunkt;
- Branch: getrennte Entwicklungsrichtung;
- Historie: Entwicklung früherer Zeitpunkte;
- Tag: später nur bei echtem Bedarf, etwa für einen bestimmten CLO- oder
  Nesselversuch.

Git ist keine fachliche Wahrheitsinstanz. Ein commitierter Fehler bleibt ein
Fehler.

**Hält, wenn:** Ein wichtiger Versuch und seine Artefakte einem eindeutigen
technischen Stand zugeordnet werden können.

### 5.19 Unterwasserbereich — Ausgabe und reale Wirklichkeit

Die Anlage endet nicht beim Python-Code. Der Fluss muss bis zu einem nutzbaren
Schnittteil reichen.

Langfristige Ausgaben:

- SVG für kontrollierbare visuelle Geometrie;
- PDF in echtem Maßstab für Ausdruck und Werkstatt;
- DXF-AAMA für CLO und weitere CAD-Verwendung;
- JSON für nachvollziehbare Daten und spätere Schnittstellen;
- Prüf- oder Konstruktionsprotokoll mit Maßen, Wahlwerten und Ergebnissen.

Reale Nachweisstufen:

1. digital erzeugbar;
2. geometrisch geprüft;
3. maßstäblich ausgegeben;
4. in CLO importierbar und plausibel;
5. als Nessel nähbar;
6. an realer Figur beobachtet;
7. von Werner und der fachlichen Praxis akzeptiert.

**Hält, wenn:** Die Software nicht nur Zahlen produziert, sondern einen
reproduzierbaren Weg zu einem realen Kleidungsstück besitzt.

---

## 6. Bauphasen

Die Phasen sind eine Reihenfolge, kein Zwang, alles gleichzeitig zu
dokumentieren. Eine Phase ist nur so weit auszuarbeiten, wie ihr Prüftor es für
die nächste Phase verlangt.

### Phase 0 — Orientierung stabilisieren

**Ziel:** Eine Folgesession findet ohne alte Chatgeschichte den Arbeitsrahmen.

**Bereits vorhanden:**

- `C:\ATELIER` als aktive Repository-Heimat;
- oberstes `AGENT.md`;
- verbindliche Benennungsregel;
- gegliederte Bereiche für Sprache, Quellen, Funktionen und Mathematik;
- Werners Denkmodell in `800_werners spick/`;
- vorhandene Python-Bausteine und Tests für Teile des geraden Rocks;
- eine vorhandene Spec für den geraden Rock.

**Noch gemeinsam zu prüfen:**

- Welches Dokument besitzt dauerhaft das Produktziel?
- Welche der in Werners Denkmodell genannten Rollen benötigen wirklich eine
  eigene Datei?
- Welche Aussagen sind bereits verbindliche Regeln und welche nur Vorschläge?
- Welche alte Pfadnennung wird später als eigener Übergangsschritt korrigiert?

**Prüftor 0:** Eine neue Session kann diese Roadmap und das oberste `AGENT.md`
lesen und anschließend genau ein Bauteil zur gemeinsamen Formulierung auswählen.

### Phase 1 — Baugrund und Verantwortung ausformulieren

**Ziel:** Ziel, Rollen, Wahrheitsstufen und Entscheidungsrechte tragen.

**Gemeinsame Arbeit:**

1. Produktziel in einem klaren Satz bestätigen.
2. Rolle von Werner, Hermes, Claude, Tests, CLO, Schneiderin und Nessel einzeln
   formulieren.
3. Zustände `Idee`, `entschieden`, `implementiert`, `digital geprüft`, `real
   geprüft` und `akzeptiert` eindeutig trennen.
4. Festlegen, welches vorhandene Dokument jede dauerhafte Antwort besitzt.
5. Nur fehlende Eigentümer als neue Datei erwägen.

**Prüftor 1:** Für jede Richtungs- oder Wahrheitsänderung ist klar, wer sie
entscheiden und wo sie dauerhaft festhalten darf.

### Phase 2 — Einlaufkontrolle seitenweise aufbauen

**Ziel:** Der erste Quellabschnitt wird von Werner in seinem Zusammenhang
verstanden und technisch übergabefähig.

**Werners eigener Arbeitszug:**

1. Nicht das ganze Buch auf einmal bearbeiten.
2. Den für die erste Öffnung notwendigen Seitenbereich bestimmen.
3. Seite für Seite Text, Bild, Formel, Fachbegriffe und Prüfstellen verbinden.
4. Eigene Verständnisfassung sichtbar von wörtlicher Buchfassung trennen.
5. Offene Fragen nicht durch Vermutung schließen.
6. Abhängigkeiten zu früheren oder späteren Seiten sichtbar machen.
7. Erst nach dem Zusammenhang die technische Übergabebereitschaft markieren.

**Rolle der KI dabei:**

- strukturieren;
- Widersprüche zeigen;
- Begriffe und Abhängigkeiten zurückspiegeln;
- Rechnungen nach ausdrücklichen Regeln prüfen;
- keine fachliche Lücke selbst schließen;
- erst auf Werners Auftrag die nächste Seite oder Frage öffnen.

**Prüftor 2:** Für die erste Öffnung existiert ein begrenztes Quellenpaket, das
belegte Regeln, Entscheidungen und offene Stellen unterscheidet.

### Phase 3 — Hierarchie und SSOT-Besitz prüfen

**Ziel:** Jeder benötigte Inhalt hat genau einen belastbaren Platz.

**Gemeinsame Arbeit:**

1. Hunderter-, Zehner-, Einer- und tiefere Ebenen an einem echten Pfad prüfen.
2. Pro Ebene die reale Verantwortung formulieren.
3. Direkte Kinder mit der zuständigen `AGENT.md`-Navigation vergleichen.
4. Für jede Frage den niedrigsten vollständigen Besitzer bestimmen.
5. Doppelte Wahrheiten nicht neu erzeugen.
6. Alte Pfade erst nach Abschluss der Strukturentscheidung in einem eigenen
   Arbeitspaket korrigieren.
7. Prüfen, ob die Benennung zukünftige Einschübe ohne erneute Migration trägt.

**Prüftor 3:** Von der Wurzel bis zum ersten Werkstück gibt es einen eindeutigen
Lade- und Besitzpfad.

### Phase 4 — Fugen und Verträge festziehen

**Ziel:** Übergaben zwischen Quelle, Sprache, Mathematik, Funktion und Ausgabe
sind eindeutig.

**Gemeinsame Arbeit:**

1. Eine reale Fachregel aus dem ersten Quellenpaket wählen.
2. Ihre Inputs, Outputs, Einheiten, Bereiche und Entscheidungen benennen.
3. Benötigte Begriffe aus `000_sprache/` zuordnen.
4. Nur den notwendigen Vertrag aus `400_mathematik/` auswählen.
5. Prüfen, ob der Vertrag bereit, offen oder gesperrt ist.
6. Den kleinsten Funktionsvertrag in `200_funktionen/` bestimmen.
7. Fehlerzustände und Invarianten vor dem Code sichtbar machen.
8. Festlegen, welches Ergebnis an den nächsten Schritt übergeben wird.

**Prüftor 4:** Eine Regel kann ohne kopierte Wahrheit und ohne versteckte
Annahme durch alle benötigten Segmente verfolgt werden.

### Phase 5 — Kontrollraum und Schleusentor erproben

**Ziel:** Werner kann eine Aufgabe über Hermes an Claude geben, ohne die
Verantwortungskette zu verlieren.

**Trockenübung ohne großen Bauauftrag:**

1. Einen kleinen bereits verstandenen Funktionsschritt auswählen.
2. Hermes formuliert Scope, erlaubte Dateien, Verträge, Tests und Stopps.
3. Werner prüft nur Ziel und fachliche Grenzen.
4. Claude erhält das begrenzte Paket.
5. Hermes prüft unabhängig, ob Claude den Scope und die Verträge eingehalten
   hat.
6. Werner beurteilt, ob der Ablauf verständlich und entlastend war.
7. Nur tatsächlich nützliche Regeln werden dauerhaft übernommen.

**Prüftor 5:** Der Ablauf funktioniert mit wenig Rücksteuerung, ohne dass Claude
Architektur oder Fachwahrheit selbst erweitert.

### Phase 6 — Messinstrumente abstimmen

**Ziel:** Jede Öffnung besitzt genau die Nachweise, die für ihren aktuellen
Reifegrad nötig sind.

**Zu bestimmen:**

- Unit-Tests pro Primitive;
- Integrationsprüfungen der Berechnungskette;
- geometrische Invarianten;
- Vergleich mit Buchbeispielen;
- visuelle Kontrollen;
- Maßstabsprüfung für PDF;
- Importprüfung für DXF/CLO;
- Protokoll für Nessel und Anprobe;
- Kriterien für Werners Annahme oder Korrektur.

**Grenze:** Keine vollständige Release-Bürokratie vor dem ersten realen
Werkstück. Es werden nur die Nachweise gebaut, die bei dieser Öffnung eine
wichtige falsche Aussage verhindern können.

**Prüftor 6:** Für den ersten vollständigen Durchfluss ist bekannt, welcher Test
welche Behauptung beweist und welche Behauptung erst CLO oder Nessel prüfen kann.

### Phase 7 — Das erste Loch öffnen

**Ziel:** Ein einziger vollständiger Weg durch die Mauer wird praktisch benutzt.

**Derzeitiger Kandidat:** gerader Rock, geführt durch
[`200_funktionen/10_grundschnitte_roecke_s32-39/spec_gerader_rock.md`](200_funktionen/10_grundschnitte_roecke_s32-39/spec_gerader_rock.md).
Der Kandidat wird erst zur aktiven ersten Öffnung, wenn Werner ihn ausdrücklich
bestätigt und das notwendige Quellenpaket bereit ist.

**Voraussichtlicher Durchfluss:**

1. Buchbeispiel und fachliche Regeln vollständig eingrenzen.
2. Vorhandene Rechen- und Geometriebausteine inventarisieren.
3. Bestehende Bausteine verbinden, nicht grundlos neu schreiben.
4. Fehlende fachliche Entscheidungen vor dem Code klären.
5. Fehlende technische Schritte in kleinen Aufträgen bauen.
6. Gesamtablauf aus Körpermaßen und Wahlwerten erzeugen.
7. Buchbeispiel rechnen und geometrisch vergleichen.
8. SVG erzeugen und visuell prüfen.
9. PDF 1:1 mit Prüfmaß erzeugen.
10. DXF-AAMA erzeugen und in CLO prüfen.
11. Erst danach reale Personenmaße in einem kontrollierten Durchlauf verwenden.
12. Nessel nähen und Beobachtungen protokollieren.
13. Werner und Schneiderin beurteilen die reale Wirkung.
14. Korrekturen als neue bewusste Runde zurückführen.

**Bekannte technische Themen aus der vorhandenen Spec:**

- vorhandene Einzelprimitive zu einer Funktion verbinden;
- Abnäher im genähten Zustand schließen und Taillennaht ausgleichen;
- Bund fachlich vollständig klären und konstruieren;
- Nahtzugaben, Saum, Markierungen und Beschriftungen;
- SVG-, PDF- und DXF-Ausgabe;
- Kontrollsummen und Nahtlängen;
- offene Fachfragen nicht technisch übergehen.

**Prüftor 7:** Ein reproduzierbares Schnittmuster durchläuft Quelle, Code,
technische Prüfung, Ausgabe und mindestens die für diesen Versuch vereinbarte
reale Abnahmestufe.

### Phase 8 — Mauer nach dem ersten Durchfluss prüfen

**Ziel:** Nicht die Theorie, sondern die reale Benutzung entscheidet über die
endgültige Organisationsform.

Nach dem ersten vollständigen Weg beantworten Werner und Hermes:

- Welche Dokumente wurden tatsächlich gebraucht?
- Welche Antwort musste mehrfach gesucht werden?
- Wo entstand doppelte Wahrheit?
- Wo war ein `AGENT.md` zu lang oder zu schwach?
- Welche Rückfrage hätte durch besseren Kontext verhindert werden können?
- Wo stoppte das System richtig?
- Wo stoppte es unnötig?
- Welche Prüfung war wertvoll?
- Welche Prüfung war Verwaltung ohne Erkenntnis?
- Welche Rolle oder Schnittstelle fehlte?
- Welche vorgeschlagene Datei wird nicht gebraucht?

Danach wird die Mauer gezielt nachjustiert. Keine flächige Regelvermehrung.

**Prüftor 8:** Die Arbeitsordnung beruht auf einem realen Durchlauf und nicht nur
auf einem vollständigen theoretischen Modell.

### Phase 9 — Kontrolliert erweitern

**Ziel:** Weitere Öffnungen nutzen die bewährte Konstruktion, ohne sie blind zu
kopieren.

Pro neuer Funktion oder Modellgruppe:

1. benötigten Quellenbereich eingrenzen;
2. Werners Verständnis und Prüfstellen klären;
3. vorhandene Sprache, Mathematik und Primitive wiederverwenden;
4. nur neue fachliche Verantwortung ergänzen;
5. kleinsten vollständigen Durchfluss bauen;
6. digitale und reale Nachweise angemessen wiederholen;
7. Erfahrungen in die bestehenden Besitzer zurückführen.

Die Mauer darf hoch und breit wachsen. Ihr Kern bleibt aber klein:
Verantwortung, klare Übergaben, sichtbare Stopps und überprüfbare Ergebnisse.

---

## 7. Aktueller Stand

### Bereits tragend

- [x] `C:\ATELIER` ist die aktive Repository-Heimat.
- [x] Werner besitzt Richtung und fachliche Wahrheit.
- [x] Hermes koordiniert, grenzt ab und prüft unabhängig.
- [x] Claude Code ist als begrenzter technischer Arbeiter vorgesehen.
- [x] Die Nummerierungslogik für beliebiges Wachstum ist formuliert.
- [x] Sprache, Quellen, Funktionen und Mathematik sind als verschiedene
      Verantwortungsbereiche erkennbar.
- [x] Technische und reale Nachweisstufen werden grundsätzlich getrennt.
- [x] Für Teile des geraden Rocks existieren Python-Bausteine und Tests.
- [x] Eine ausführliche Arbeits-Spec für den geraden Rock existiert.

### Im Bau

- [ ] Jedes Bauteil dieser Roadmap gemeinsam ausformulieren und seinen Besitzer
      festlegen.
- [ ] Verbindliche Regeln von Denkmodellen und Vorschlägen trennen.
- [ ] Entscheiden, welche fehlenden Rollen wirklich eine eigene Datei brauchen.
- [ ] Einen eindeutigen Ladepfad für Folgesessions herstellen.
- [ ] Übergabeverträge an einem realen Funktionsschritt prüfen.

### Werners vorgelagerter Arbeitszug

- [ ] Prüfstellen im Zusammenhang aufarbeiten.
- [ ] Den Kontext selbst verstehen und nicht nur Bilder ablegen.
- [ ] Seite für Seite Text, Bild, Fachbegriffe, Formeln und offene Fragen
      verbinden.
- [ ] Belegte Aussage, eigenes Verständnis und offene Frage sichtbar trennen.
- [ ] Den Quellenbereich für die erste Öffnung als technisch bereit oder noch
      nicht bereit kennzeichnen.

### Bewusst noch nicht aktiv

- [ ] Pauschale Reparatur aller alten Pfade.
- [ ] Vollständige Ausarbeitung aller Buchkapitel.
- [ ] Vollständige allgemeine CAD-Bibliothek.
- [ ] Automatische Anlage aller denkbaren Markdown-Rollen.
- [ ] Flächige Claude-Aufträge ohne verstandenen Quellenkontext.
- [ ] Produktionsfreigabe aus rein digitalen Tests.

---

## 8. Arbeitsweise in Folgesessions

### 8.1 Start einer Session zur Staumauer

Eine neue Session erhält zunächst nur:

1. den aktuellen Auftrag von Werner;
2. `C:\ATELIER\AGENT.md`;
3. diese `ROADMAP_STAUMAUER.md`;
4. bei Arbeit an einem konkreten Bauteil nur dessen vorhandenen Besitzer;
5. bei Arbeit in einem Ordner die lokale `AGENT.md`-Kette entlang genau dieses
   Pfads.

`100_quellen/` wird nicht pauschal durchsucht oder vollständig geladen. Ein
Quellabschnitt wird nur geöffnet, wenn Werner ihn für die konkrete Seite oder
Frage als Teil des aktuellen Arbeitsauftrags benennt.

### 8.2 Gesprächsrhythmus pro Bauteil

Hermes arbeitet mit Werner jeweils nur an einem Bauteil:

```text
Befund
→ Bedeutung für die ganze Mauer
→ Vorschlag
→ mögliche Bruchstelle
→ Werners Entscheidung
→ richtiger Besitzer
→ erst dann eventuell schreiben
```

Keine Folgeentscheidung wird still vorausgesetzt. Wenn Werner zuerst nur reden
will, bleiben alle Werkzeuge lesend und es wird nichts geändert.

### 8.3 Abschluss einer Session

Am Ende wird knapp festgehalten:

- welches Bauteil besprochen wurde;
- was Werner entschieden hat;
- wo die Entscheidung dauerhaft besitzt wird;
- was weiterhin offen ist;
- welches eine Bauteil als Nächstes folgt;
- ob Dateien geändert wurden;
- ob Tests liefen;
- ob Commit oder Push ausdrücklich freigegeben und ausgeführt wurden.

Diese Roadmap wird nur aktualisiert, wenn sich ihr Gesamtstand oder ihre
Reihenfolge wirklich geändert hat. Lokale Fachergebnisse bleiben beim lokalen
Besitzer.

---

## 9. Prüfschema für jedes Bauteil

Dieses Schema kann in einer Folgesession direkt verwendet werden:

```markdown
## Bauteil: <Name>

**Frage:**

**Warum braucht die Mauer dieses Bauteil?**

**Eigentümer der Antwort:**

**Vorhandener Besitzer im Repository:**

**Eingaben:**

**Ausgaben / Übergabe:**

**Harte Grenzen:**

**Stopps bei Unklarheit:**

**Nachweis, dass es trägt:**

**Mögliche Bruchstelle oder Doppelung:**

**Braucht es eine neue Datei?** ja / nein / noch offen

**Werners Entscheidung:**

**Status:** offen / formuliert / praktisch erprobt / nachjustieren / trägt
```

Ein Bauteil gilt nicht allein deshalb als fertig, weil sein Text schön klingt.
Es gilt zunächst als **formuliert**. Erst der erste echte Durchfluss zeigt, ob es
praktisch trägt.

---

## 10. Gesamtprüfung vor der ersten Öffnung

Vor dem ersten vollständigen Claude-Arbeitszug wird die Konstruktion einmal als
Ganzes geprüft.

### Verantwortung

- [ ] Werner kann jede fachliche Richtungsentscheidung erkennen und behalten.
- [ ] Hermes besitzt einen klaren Prüf- und Integrationsauftrag.
- [ ] Claude besitzt einen engen technischen Scope.
- [ ] Tests, CLO, Nessel und Werner haben getrennte Aussagen.

### Wissen

- [ ] Der benötigte Quellbereich wurde im Zusammenhang verstanden.
- [ ] Buchaussage, Bildaussage, Werners Entscheidung und Agentenvorschlag sind
      unterscheidbar.
- [ ] Offene Prüfstellen sind sichtbar.
- [ ] Keine technische Vorgabe ersetzt eine fachlich offene Entscheidung.

### Struktur

- [ ] Der aktive Pfad folgt der Benennungsregel.
- [ ] Jede Ebene besitzt eine echte Verantwortung.
- [ ] Die zuständigen `AGENT.md` nennen nur direkte Kinder.
- [ ] Jede wichtige Frage hat einen einzigen Besitzer.
- [ ] Die neue Session muss nicht das ganze Repository laden.

### Übergaben

- [ ] Quelle → Sprache ist eindeutig.
- [ ] Quelle → Mathematik trennt Fachregel und allgemeine Geometrie.
- [ ] Mathematik → Funktion besitzt Inputs, Outputs, Einheiten und Fehler.
- [ ] Funktion → Ausgabe trennt Geometriezustände und Provenienz.
- [ ] Ausgabe → reale Prüfung besitzt einen reproduzierbaren Stand und konkrete
      Beobachtungsfragen.

### Sicherheit

- [ ] Fehlende Entscheidung führt zu einem sichtbaren Stopp.
- [ ] Unmögliche Geometrie wird nicht still repariert.
- [ ] Erlaubte und verbotene Dateien sind im Auftrag benannt.
- [ ] Ein Schreiber pro Worktree ist festgelegt.
- [ ] Geschützte Aktionen benötigen ein frisches `#`.
- [ ] Private Maße und Quellen werden nicht unnötig vervielfältigt.

### Nachweis

- [ ] Für jede Behauptung ist die richtige Prüfart bestimmt.
- [ ] Der Buchbeispielfall ist definiert.
- [ ] Der digitale Ausgabefall ist definiert.
- [ ] CLO- und Nessel-Fragen sind vor dem Versuch benannt.
- [ ] Der reale Versuch kann einem technischen Stand zugeordnet werden.

Wenn ein Punkt nicht erfüllt ist, wird nur diese Bruchstelle nachgebessert. Die
ganze Mauer wird nicht jedes Mal neu entworfen.

---

## 11. Definition: Die Mauer hält

Die Staumauer ist für die erste Öffnung ausreichend gebaut, wenn:

1. eine neue Session ohne alte Chatgeschichte den aktiven Weg findet;
2. Werner nicht wieder den ganzen Zusammenhang erklären muss;
3. jede fachliche Frage ihren Besitzer hat;
4. der benötigte Quellenkontext verstanden und begrenzt ist;
5. offene Stellen sichtbar stoppen;
6. die Nummerierung weiteres Wachstum ohne erneute Gesamtumbenennung erlaubt;
7. Hermes einen vollständigen, aber kleinen Auftrag bilden kann;
8. Claude ihn ohne freie Fach- oder Architekturannahmen ausführen kann;
9. technische Tests und reale Prüfung nicht verwechselt werden;
10. ein Ergebnis von der Quelle bis zum realen Artefakt zurückverfolgt werden
    kann;
11. Git einen akzeptierten technischen Zeitpunkt festhalten kann;
12. der erste reale Durchfluss wichtiger wird als weiterer Ausbau der
    Dokumentarchitektur.

Dann wird nicht weiter theoretisch verstärkt. Dann wird das erste Loch geöffnet.

---

## 12. Nächster gemeinsamer Schritt

**Noch kein Codeauftrag. Noch keine flächige Pfadreparatur.**

Der nächste gemeinsame Schritt ist:

> **Bauteil 1 — Baugrund:** Das dauerhafte Produktziel und die reale
> Abschlussfrage so formulieren, dass jede spätere technische Entscheidung daran
> geprüft werden kann.

Danach folgen in dieser Reihenfolge:

1. Bauherr und Verantwortungsordnung;
2. Wasserzulauf und Autoritätsstufen;
3. Einlaufkontrolle für Werners Seitenarbeit;
4. Grundriss und Hierarchie;
5. Mauersegmente und ihre Besitzer;
6. Bewehrung durch die `AGENT.md`-Kette;
7. Fugen und Übergabeverträge;
8. Kontrollraum, Bauarbeiter und Schleusentor;
9. Rückschlagventile und Messinstrumente;
10. Gesamtprüfung;
11. Werners Entscheidung über die erste Öffnung;
12. erster vollständiger Durchfluss.

Wir gehen diese Punkte nicht als Fragebogen in einem einzigen Gespräch durch.
Wir nehmen einen Punkt, formulieren ihn gemeinsam, prüfen seine Verbindung zur
ganzen Mauer und entscheiden erst dann, wo er dauerhaft hingehört.

---

## 13. Leitsatz

> **Wir bauen nicht möglichst viel auf einmal. Wir bauen eine Ordnung, die viel
> halten kann und genau dort Wasser durchlässt, wo Quelle, Verantwortung,
> Technik und Wirklichkeit miteinander verbunden sind.**
