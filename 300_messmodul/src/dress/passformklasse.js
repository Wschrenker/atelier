// Passformklasse (PK) — Fit-Klasse als DESIGN-Entscheidung, NICHT als Koerpermass.
// Eine Wahrheitsquelle fuer: Empfehlung, waehlbare Optionen, Validierung.
//
// Hofenbitzer Band 1 S.176: koerpernahe Kleider -> PK 3 ("sehr koerpernah").
// Regel "Stopp statt Raten": Die Engine setzt PK NIE still (siehe draftALineDress,
// draftFittedDressBodice, bridalValuesToBodiceInput). Das UI waehlt die Empfehlung
// SICHTBAR vor und erklaert ihre Wirkung — kein versteckter Buchwert.
//
// Reines Modul ohne Abhaengigkeiten: laeuft im Node-Test UND im Browser (Messmodul).

export const RECOMMENDED_PASSFORMKLASSE = 3;

// Waehlbare Klassen fuers Brautkleid (Werner-Vorgabe 3/4/5).
//
// EHRLICHER STAND DER MATHEMATIK: PK wirkt aktuell NUR ueber den vorderen
// Taillenabnaeher-Zuschlag (pkSurcharge in fitted-bodice.js): PK<=4 -> +1,0 cm ·
// PK5-7 -> +0,5 cm. Die Zugaben-Tabelle (Brust/Taille/Huefte) ist auf PK 3 fest
// verdrahtet (pk3Construction). Folge: PK 3 und PK 4 liefern DIESELBE Geometrie;
// erst PK 5 senkt die vordere Taillenzugabe um 0,5 cm. Die volle Passformklassen-
// Differenzierung (eigene Zugaben je Klasse) braucht die Hofenbitzer-Zugaben-Tabelle
// und ist NOCH NICHT gebaut — die Wirkungstexte sagen genau das, was heute stimmt.
export const PASSFORMKLASSE_OPTIONS = Object.freeze([
  Object.freeze({
    value: 3,
    label: "PK 3 — sehr koerpernah",
    recommended: true,
    effect: "Engste Stufe: volle vordere Taillenzugabe (+1,0 cm). Empfohlen fuers koerpernahe Brautkleid (S.176).",
    sourceRef: "Hofenbitzer Band 1, S.176"
  }),
  Object.freeze({
    value: 4,
    label: "PK 4 — koerpernah",
    recommended: false,
    effect: "Buch-Zuschlagsstufe wie PK 3 (Klasse <=4 -> +1,0 cm) — im aktuellen Engine-Stand geometrisch identisch zu PK 3."
  }),
  Object.freeze({
    value: 5,
    label: "PK 5 — maessig koerpernah",
    recommended: false,
    effect: "Naechste Stufe (5-7 -> +0,5 cm): 0,5 cm weniger vordere Taillenzugabe, minimal bequemer."
  })
]);

const VALID_VALUES = new Set(PASSFORMKLASSE_OPTIONS.map((option) => option.value));

// Streng: true nur fuer die angebotenen Klassen (3/4/5). Strings/undefined/NaN -> false.
export function isValidPassformklasse(value) {
  return typeof value === "number" && Number.isFinite(value) && VALID_VALUES.has(value);
}
