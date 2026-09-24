# Formeln s195 – Normalisierung (vorläufig)

**Status:** Lokale KI-Ablesung, kein Mistral OCR, vollständig unbestätigt. Alle Formeln stehen auf `offen`.

## Formel 1 – Differenz der SuB-Zugaben

- **Quelle:** [`formeln_s195.md`](formeln_s195.md), Abschnitt 1
- **Technische Formel:** `differenz_SuB = zugabe_SuB(PK9) - zugabe_SuB(PK3)`
- **Werte:** `0,9 cm - 0,3 cm = 0,6 cm`
- **Status:** offen

## Formel 2 – Neue vordere Schulternaht

- **Quelle:** [`formeln_s195.md`](formeln_s195.md), Abschnitt 2
- **Technische Formel:** `vSuN_neu = vSuN_alt + differenz_SuB`
- **Werte:** `12,5 cm + 0,6 cm = 13,1 cm`
- **Status:** offen

## Formel 3 – Neue hintere Schulternaht

- **Quelle:** [`formeln_s195.md`](formeln_s195.md), Abschnitt 3
- **Technische Formel:** `hSuN_neu = vSuN_neu + einhalteweite`
- **Werte:** `13,1 cm + 0,7 cm = 13,8 cm`
- **Bedingung:** `einhalteweite ∈ [0,5 cm, 1,0 cm]`
- **Status:** offen

## Formel 4 – Vertiefung der Ärmelpunkte

- **Quelle:** [`formeln_s195.md`](formeln_s195.md), Abschnitt 4
- **Technische Formel:** `vertiefung_aermelpunkt = 3/4 * differenz_AlT`
- **Buchwert:** `¾ von 2,7 cm = 2,0 cm`
- **Status:** offen
- **Prüfhinweis:** Der Buchwert ist gerundet; Rundungsregel ist nicht angegeben.

## Formel 5 – Taillenweiten-Korrektur

- **Quelle:** [`formeln_s195.md`](formeln_s195.md), Abschnitt 5
- **Technische Formel:** `mehrbetrag_TaW = halbe_TaW - (TaU + zugabe_TaW) / 2`
- **Werte:** `44,6 cm - (72 cm + 16 cm) / 2 = 0,6 cm`
- **Zusatzangabe:** Am halben Schnitt können `0,4 cm` entfernt werden.
- **Status:** offen
- **Offene Frage:** Verhältnis zwischen `0,6 cm Mehrbetrag` und `0,4 cm` Entfernung klären; keine automatische Korrektur.

## Formel 6 – Hüftweiten-Korrektur

- **Quelle:** [`formeln_s195.md`](formeln_s195.md), Abschnitt 6
- **Technische Formel:** `mehrbetrag_HueW = halbe_HueW - (HueU + zugabe_HueW) / 2`
- **Werte:** `56,1 cm - (97 cm + 12 cm) / 2 = 1,6 cm`
- **Folgerung laut Buch:** `entfernung_halber_schnitt = mehrbetrag_HueW / 2 = 0,8 cm`
- **Status:** offen

Keine dieser Normalisierungen darf vor Werners Prüfung als Fachwahrheit oder Codevertrag verwendet werden.
