# Formeln normalisiert – s062

Technische Fassung zu [formeln_s062.md](formeln_s062.md). Keine der dortigen
Buchfassungen ist laut [s062.md](s062.md) am Original bestätigt; alle
Einträge unten erhalten deshalb konsequent den Status `offen`, unabhängig
davon, wie eindeutig der Text wirkt. Diese Datei erzeugt keine Python-Funktion,
keinen Engine-Vertrag und keine neue Fachregel.

## F1 – Taillenweiten-Reduzierung beim Entfernen der Einhalteweite

- **Quelle:** [formeln_s062.md](formeln_s062.md), Abschnitt 1.
- **Buchfassung:**
  ```text
  Die Einhalteweite aus dem Rock-Grundschnitt wird entfernt, indem die Abnäher im Grundschnitt gemessen und die neu positionierten Abnäher an jedem Rockviertel um ca. 0,5 cm größer gezeichnet werden. Die gesamte Taillenweite ist somit um ca. 2 cm reduziert.
  ```
- **Technische Formel:** `ΔTaW_gesamt ≈ n_Viertel × ΔAbnäher_Viertel`.
- **Eingaben und Einheiten:** `ΔAbnäher_Viertel` (cm, ca. 0,5); `n_Viertel` (Anzahl Rockviertel, auf dieser Seite nicht genannt).
- **Ausgabe und Einheit:** `ΔTaW_gesamt` (cm, ca. 2).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** beide Werte als „ca." markiert, keine festen Grenzen. Rechnerisch passt `n_Viertel = 4` (`4 × 0,5 = 2`), das ist aber eine Prüfrechnung dieser Normalisierung, keine Buchaussage dieser Seite.
- **Abhängigkeiten:** möglicher Bezug zur Abnäherstruktur des Rock-Grundschnitts (z. B. Tabellen auf früheren Seiten wie s033/s038), auf dieser Seite nicht verlinkt.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Anzahl der Rockviertel nicht belegt; Seite nicht menschlich bestätigt.

## F2 – Miederbelege, Breiten-Reduzierung (☐2)

- **Quelle:** [formeln_s062.md](formeln_s062.md), Abschnitt 2.
- **Buchfassung:**
  ```text
  ☐2 Miederbelege mit Breiten-Reduzierung um ca. 0,2 cm
  ```
- **Technische Formel:** `ΔBreite_Miederbeleg ≈ 0,2 cm`.
- **Eingaben und Einheiten:** keine benannte Ausgangsbreite auf dieser Seite.
- **Ausgabe und Einheit:** `ΔBreite_Miederbeleg` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Einzelwert „ca. 0,2 cm", kein Bereich.
- **Abhängigkeiten:** zeichnungsgebunden, siehe [skizzen/s062_skizze_02.png](skizzen/s062_skizze_02.png); Bezug zur Ausgangsbreite nur aus der Zeichnung ablesbar, nicht textlich beziffert.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** worauf sich die Reduzierung bezieht (welche Ausgangsgröße), ist ohne Skizzenprüfung unklar.

## F3 – Abnäher zulegen, Weiten-Reduzierung oben/unten (☐4)

- **Quelle:** [formeln_s062.md](formeln_s062.md), Abschnitt 3.
- **Buchfassung:**
  ```text
  ☐4 Abnäher zulegen mit gleichzeitiger Weiten-Reduzierung um ca. 0,2 cm an den oberen Kanten und max. 0,5 cm an den unteren Belegnähten
  ```
- **Technische Formel:** `ΔWeite_oben ≈ 0,2 cm`; `ΔWeite_unten ≤ 0,5 cm`.
- **Eingaben und Einheiten:** keine.
- **Ausgabe und Einheit:** `ΔWeite_oben`, `ΔWeite_unten` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** oben ein „ca."-Einzelwert; unten ein Bereich `[0; 0,5]` cm mit ausdrücklicher Obergrenze („max.").
- **Abhängigkeiten:** zeichnungsgebunden, siehe [skizzen/s062_skizze_04.png](skizzen/s062_skizze_04.png). Inhaltlich verwandt mit F5 (untere Belegnaht, „bis zu 0,5 cm").
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** keine buchseitige Auswahlregel, wo innerhalb `[0; 0,5]` der tatsächliche Wert liegt.

## F4 – Miederbelege kopieren, obere Kante

- **Quelle:** [formeln_s062.md](formeln_s062.md), Abschnitt 4.
- **Buchfassung:**
  ```text
  6 ☐3+4 Die Flächen der Miederbelege kopieren und für eine Weitenreduzierung die Abnäher an der oberen Kante um ca. 0,2 cm übereinanderlegen.
  ```
- **Technische Formel:** `ΔWeite_oben ≈ 0,2 cm` (Übereinanderlegen der Abnäher an der oberen Kante).
- **Eingaben und Einheiten:** keine.
- **Ausgabe und Einheit:** `ΔWeite_oben` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Einzelwert „ca. 0,2 cm".
- **Abhängigkeiten:** inhaltlich gleicher Reduzierungswert wie F2 und F3 (obere Kante); nicht vereinheitlicht, da drei getrennte Textstellen.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Schrittnummer laut [s062.md](s062.md) ein dokumentierter OCR-Fehler (vermutlich ⑤, OCR „6"); inhaltlich ändert das nichts an der Formel.

## F5 – Untere Belegnaht, Übereinanderlegen bis 0,5 cm mit Dehnungsausgleich

- **Quelle:** [formeln_s062.md](formeln_s062.md), Abschnitt 5.
- **Buchfassung:**
  ```text
  6 An der unteren Belegnaht kann man an den Abnähern bis zu 0,5 cm übereinanderlegen. Die hier reduzierte Weite wird am Stoff vor der Weiterverarbeitung durch Dehnen der Naht ausgeglichen.
  ```
- **Technische Formel:** `ΔWeite_unten ≤ 0,5 cm`, anschließend `Weite_ausgeglichen = Weite_original` (Dehnungsausgleich am Stoff, kein numerischer Wert angegeben).
- **Eingaben und Einheiten:** keine.
- **Ausgabe und Einheit:** `ΔWeite_unten` (cm); Dehnungsausgleich ohne Einheit/Wert.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Bereich `[0; 0,5]` cm, ausdrücklich als „bis zu" markiert (Obergrenze, keine Untergrenze genannt).
- **Abhängigkeiten:** möglicherweise dieselbe Regel wie in F3 (☐4, „max. 0,5 cm an den unteren Belegnähten"), hier aber als eigener Textabschnitt mit zusätzlichem Dehnungshinweis; nicht zusammengeführt.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Verhältnis F3/F5 zueinander (gleiche Regel zweimal formuliert, oder zwei getrennte Nähte?) ungeklärt; keine Zahl für den Dehnungsausgleich.

## F6 – Belegflächen formen, obere Rockkante (☐5)

- **Quelle:** [formeln_s062.md](formeln_s062.md), Abschnitt 6.
- **Buchfassung:**
  ```text
  7 ☐5 Die Breiten der so entstandenen Belegflächen werden an der oberen Rockkante um ca. 0,2 cm reduziert und die untere Belegnaht geformt.
  ```
- **Technische Formel:** `ΔWeite_oben ≈ 0,2 cm`.
- **Eingaben und Einheiten:** keine.
- **Ausgabe und Einheit:** `ΔWeite_oben` (cm).
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Einzelwert „ca. 0,2 cm"; „untere Belegnaht geformt" ohne Zahl.
- **Abhängigkeiten:** letzter Schritt der Reduzierungskette F2/F4/F6 (obere Kante, jeweils ca. 0,2 cm).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** keine.

## F7 – Abnäherpositionen, Reihenfolge Länge vorne/hinten

- **Quelle:** [formeln_s062.md](formeln_s062.md), Abschnitt 7.
- **Buchfassung:**
  ```text
  Seitliche paarweise Abnäherpositionen sehen am besten aus, wenn der vorderste am küzesten und der hinterste am längsten ist.
  ```
- **Technische Formel:** Ordnungsrelation `Länge(vorderer Abnäher) < Länge(hinterer Abnäher)`, mit dem mittleren/seitlichen Abnäher dazwischen liegend, sofern vorhanden.
- **Eingaben und Einheiten:** keine (ästhetische Empfehlung, kein Rechenwert).
- **Ausgabe und Einheit:** keine.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „sehen am besten aus" ist eine gestalterische Empfehlung, keine harte Konstruktionsregel.
- **Abhängigkeiten:** betrifft dieselben paarweisen Abnäherpositionen wie in Abschnitt 1 (F1).
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** Anzahl und genaue Zuordnung der „paarweisen" Positionen zur Zeichnung auf dieser Seite nicht spezifiziert.

## F8 – Abnäherinhalt nimmt oberhalb der Taille ab

- **Quelle:** [formeln_s062.md](formeln_s062.md), Abschnitt 8.
- **Buchfassung:**
  ```text
  Oberhalb der Taille wird der Körper wieder breiter. Die Abnäherinhalte sind also an der Taille am größten und werden für mehr Weite nach oben hin wieder kleiner. Abnäher und Seitennähte kann man nach oben spiegeln.
  ```
- **Technische Formel:** `AbnäherInhalt(Höhe)` monoton fallend oberhalb der Taillenlinie, Maximum bei `Höhe = Taille`; alternative Konstruktionsmethode: Spiegelung von Abnäher- und Seitennahtverlauf nach oben.
- **Eingaben und Einheiten:** keine numerische Angabe.
- **Ausgabe und Einheit:** keine.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** rein qualitative Monotonie-Aussage; „spiegeln" als optionale, nicht verpflichtende Methode („kann man").
- **Abhängigkeiten:** betrifft dieselbe Abnäherstruktur wie F1.
- **Status:** offen.
- **Offene Fragen oder Widersprüche:** keine numerische Funktion angegeben.
