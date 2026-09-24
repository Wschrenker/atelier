# Formeln s105 – Normalisierung (vorläufig, Walking Skeleton)

**Achtung:** Wie in [`formeln_s105.md`](formeln_s105.md) vermerkt, ist keine
Stelle dieser Seite von Werner am Original bestätigt. Alle drei erfassten
Beziehungen stehen deshalb auf `offen`, unabhängig von der inhaltlichen
Klarheit der Buchfassung. Dies ist ein Walking-Skeleton-Durchlauf, kein Ersatz
für die Bestätigung.

## Formel 1 – Öffnen der Schnittteile durch Abnäherschluss (Drehpunkt-Technik)

- **Quelle:** [`formeln_s105.md`](formeln_s105.md), Abschnitt 1
- **Buchfassung:**
  ```text
  Am RT verlaufen einige Einschnitte u.U. über die Abnaherschenkel.
  Manche Abnaher konnen auf den nachstliegenden Einschnitt verlangert oder
  verkurzt werden.
  Einschnittlinien einschneiden und die Einzetteile an der Taille bzw. an den
  Abnaherspitzen passend ansetzen.
  Schnitttel öffnen, indem man alle Abnaher schließt.
  ```
- **Technische Formel:**
  ```text
  für jeden betroffenen Abnäher a:
      abnaeher_winkel(a) -> 0   (Abnäher wird geschlossen)
      dadurch: einschnittlinie(a) öffnet sich proportional um den
               geschlossenen Abnäherwinkel (Drehpunkt = Abnäherspitze bzw.
               Taillenansatzpunkt)
  ```
  Reine Beschreibung der Drehpunkt-Technik aus dem Buchtext; keine
  quantifizierte Winkel- oder Längenformel im Wortlaut enthalten.
- **Eingaben und Einheiten:** Lage der Einschnittlinien und Abnäherspitzen auf
  dem Grundschnitt „Eingestellter Rock RT“ (☐5); betroffene Abnäher, die auf
  den nächstliegenden Einschnitt verlängert/verkürzt werden können (keine
  Einheit angegeben).
- **Ausgabe und Einheit:** Geöffnete Schnittteile (Einschnittlinien) nach
  Abnäherschluss; keine Zahlenausgabe im Buchtext.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** „Manche Abnäher können
  … verlängert oder verkürzt werden“ – fachlicher Auswahlspielraum, keine
  feste Regel, welcher Abnäher wann verlängert/verkürzt wird. Zuordnung
  Abnäher ↔ Einschnitt nicht formalisiert.
- **Abhängigkeiten:** Grundschnitt „Eingestellter Rock RT“ (☐5,
  [skizzen/s105_skizze_02.png](skizzen/s105_skizze_02.png)); [[Formel 2]]
  (Ergebnis der Öffnung wird dort über die SN-Länge geprüft).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Keine quantifizierte Beziehung (Winkel, Länge) im Buchtext – nur
    qualitative Beschreibung der Slash-and-Spread-Technik.
  - Kennung `1` mit Scherensymbol auf der Zeichnung ist im Fließtext nicht
    erwähnt; Zuordnung zu diesem oder einem anderen Schritt ungeklärt.
  - Zuordnung der blauen Schrittkennungen `5`–`7` zu den einzelnen Sätzen
    dieses Abschnitts nicht bestätigt.

## Formel 2 – Ausgleich der Seitennaht-Längen

- **Quelle:** [`formeln_s105.md`](formeln_s105.md), Abschnitt 2
- **Buchfassung:**
  ```text
  Die Öffnungen werden hinter weniger regelmäß erfolgen. Insgesamt muss aber
  die hintere SN-Länge mit der vorderen SN-Länge übereinstimmen.
  Durch Verändern der Öffnungen an der Seitennaht muss man so lange
  probieren, bis die SN-Längen übereinstimmen.
  ```
- **Technische Formel:**
  ```text
  Bedingung:  sn_laenge_hinten == sn_laenge_vorne

  Verfahren (iterativ, keine geschlossene Formel im Buchtext):
      solange sn_laenge_hinten != sn_laenge_vorne:
          seitennaht_oeffnung anpassen
  ```
- **Eingaben und Einheiten:** `sn_laenge_hinten` (cm, vermutlich), Länge der
  Seitennaht am hinteren Rockteil nach dem Öffnen; `sn_laenge_vorne` (cm,
  vermutlich), Länge der Seitennaht am vorderen Rockteil. Einheit im Buchtext
  nicht genannt, nur aus Kontext (Schnittkonstruktion in cm) angenommen.
- **Ausgabe und Einheit:** Angeglichene Seitennaht-Öffnungen, sodass
  `sn_laenge_hinten = sn_laenge_vorne` gilt.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Gleichheitsbedingung
  ohne Toleranzangabe; „weniger regelmäß[ig]“ (Buchwortlaut unvollständig,
  vermutlich „regelmäßig“) beschreibt die hintere Verteilung der Öffnungen
  qualitativ, ohne Zahl. Kein fester Wert oder Default für die
  Anpassungsschritte – Buchtext beschreibt ein Probierverfahren, keine
  geschlossene Formel.
- **Abhängigkeiten:** [[Formel 1]] (Ausgangslage der Öffnungen entsteht durch
  den Abnäherschluss); Folgeschritt „Taillennaht ausgleichen“ (nicht als
  eigene Formel erfasst, siehe formeln_s105.md).
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - OCR-Wortlaut „hinter weniger regelmäß erfolgen“ unvollständig/unsicher
    (vermutlich „hinten … regelmäßig“) – am Original zu prüfen.
  - Keine Toleranz für „übereinstimmen“ angegeben.

## Formel 3 – Nahtzugaben-Breite an den Seitennähten (Auswahlregel)

- **Quelle:** [`formeln_s105.md`](formeln_s105.md), Abschnitt 3
- **Buchfassung:**
  ```text
  Die Breite der NZg an den Seiten-nähten ist wegen der starken Rundung eher
  Klein.
  ```
- **Technische Formel:**
  ```text
  nzg_breite_seitennaht = f(rundungsstaerke)
  bei starker Rundung: nzg_breite_seitennaht eher klein   (kein Zahlenwert)
  ```
- **Eingaben und Einheiten:** Krümmungsstärke der Seitennaht (qualitativ,
  keine Einheit angegeben).
- **Ausgabe und Einheit:** `nzg_breite_seitennaht` (cm, vermutlich) – kein
  Zahlenwert im Buchtext, nur qualitative Tendenz „eher klein“.
- **Bereiche, Bedingungen und Auswahlentscheidungen:** Reine Auswahlregel
  ohne festen Wert oder Bereich; „eher klein“ bleibt fachlicher
  Ermessensspielraum, kein Default zu wählen.
- **Abhängigkeiten:** Bezieht sich auf dieselben Seitennähte wie [[Formel 2]].
- **Status:** offen
- **Offene Fragen oder Widersprüche:**
  - Kein Punkt dieser Seite ist von Werner am Original bestätigt.
  - Kein Zahlenwert oder Bereich für „eher klein“ im Buchtext – nicht
    quantifizierbar ohne weitere Fachregel.
