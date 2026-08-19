# Abweichung Aldrich-Prototyp → Hofenbitzer Band 1

Stand: 2026-06-21

Verglichen werden der historische Node-Prototyp aus `PROTOTYPE_SPEC.md` und die aktive, von
Werner/Munkhuu freigegebene Hofenbitzer-Transkription S. 32–41.

| Bereich | Alter Aldrich-naher Prototyp | Aktiver Hofenbitzer-Draft |
|---|---|---|
| Quellenstatus | unbelegter technischer Startwert | MethodProfile `hofenbitzer-band1-straight-skirt` v1.0.0, Status `verified` |
| Referenzmaße | 68 / 94 / 20,6 / 60 cm | Buchfall Größe 38: TaU 72, HüU 97, HüT 21, MoL 50 cm |
| Weitenzugaben | Taille 1, Hüfte 3 cm | Taille 1–2 cm, Hüfte 2–3 cm; Referenz 2 / 3 cm (S. 33) |
| Hüftbreite | Vorder- und Rückteil asymmetrisch berechnet | halbe Hüftweite, dann halbiert; Referenz je 25 cm (S. 33) |
| Taillenausfall | indirekt über feste Teilbreiten | `½ HüW − ½ TaW`; Referenz 13 cm (S. 33) |
| Hüftabstich | aus Teilbreiten entstanden | normal `TaAf : 2`, mit belegter Figurkorrektur ±1 bis 1,5 cm (S. 34) |
| Vorderer Abnäher | fest 2 cm, Position `Teilbreite : 3` | 0 bzw. 1,5–2,5 cm; Mitte `TaU : 10` vom Hüftbogen (S. 34) |
| Hintere Abnäher | immer zwei, beide fest 2 cm | Restbetrag; erst über 4,5 cm auf zwei Abnäher teilen (S. 34–35) |
| Taillenerhöhungen | Seite fest 1,25 cm | Seite 1–1,5, vorn 0,5–0,7, hinten 0,3–0,5 cm (S. 34–35) |
| Hüft-/Taillenform | quadratische Kurve mit technischen Startkonstanten | Kurve durch die belegten Konstruktionspunkte; keine Aldrich-Konstante übernommen |
| Naht-/Saumzugaben | fest 1,5 / 3 / 2 cm | belegte Bereiche 1–3 bzw. 2–5 cm; Profilwahl 2 / 3,5 / 2 cm (S. 36) |
| Bundanschluss | nicht kontrolliert | Bundlänge TaU und halbe Taillenmehrweite als Kontrollwerte (S. 39) |
| Provenienz | keine Regel- oder Seitenbelege | jeder abgeleitete Wert mit `ruleRef` und `sourceRefs` im Contract 0.2 |

Der alte Methodendraft ist aus `src/methods/` entfernt. Die unveränderte Vergleichsbasis bleibt im
Archiv; aktive Engine und Exporte verwenden ausschließlich das Hofenbitzer-Profil.

## Bewusst noch nicht festgelegt

Der Bundverschluss ist nicht automatisch gewählt. S. 40–41 bieten drei Varianten; Übertritt,
Untertritt, Knopf und Knopfloch werden erst nach einer Modellentscheidung als Produktionsschnitt
erzeugt. Der belegte Bundanschluss und seine Mehrweitenkontrolle sind bereits im Draft enthalten.
