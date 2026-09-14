// Kanonische Hofenbitzer-S.19-Ableitung der drei Konstruktions-Laengenmasse
// HlB, BrT und VL. EINZIGE Quelle dieser Formeln — beide Braut-Adapter rufen
// diese Funktion (bridal-measurement-bodice-adapter.js = kanonisch/oeffentlich,
// bridal-measurement-adapter.js = Kompatibilitaets-Wrapper), damit kein
// Formelsatz doppelt lebt.
//
// Formeln (S.19; Reihenfolge zwingend: HlB zuerst):
//   HlB = HaU / 6 + 0,5                                (HaU = neck_base_circumference)
//   BrT = Ø(gBrT r, gBrT l) - HlB
//   VL  = Ø(gVL r, gVL l) - HlB + Taillenschraeglage vorne (fehlt -> 0, Advisory)
//
// Vorzeichen der Taillenschraeglage wird durchgereicht (kein Betrag).
// Rohwerte kommen als Zahlen vom vorgelagerten Layer (keine Komma/Strings).
// Reine Funktion, kein throw.

export const TAILLENSCHRAEGLAGE_DEFAULT_ADVISORY = "TAILLENSCHRAEGLAGE_DEFAULT_0";

function finiteValue(values, id) {
  return Number.isFinite(values?.[id]) ? values[id] : undefined;
}

function mean(...candidates) {
  const finite = candidates.filter((value) => Number.isFinite(value));
  if (finite.length === 0) return undefined;
  return finite.reduce((sum, value) => sum + value, 0) / finite.length;
}

/**
 * Rechnet HlB, BrT und VL nach S.19 aus dem Roh-Masssatz.
 * @param {Record<string, number>} values  Mess-id -> Zahl
 * @returns {{
 *   halsansatzUmfangCm?: number,
 *   halslochbreiteCm?: number,
 *   gemesseneBrusttiefeCm?: number,
 *   brusttiefeCm?: number,
 *   gemesseneVorderlaengeCm?: number,
 *   vorderlaengeCm?: number,
 *   taillenschraeglageVorneCm?: number,
 *   taillenschraeglageDefaulted: boolean
 * }}
 */
export function deriveS19ConstructionLengths(values = {}) {
  // 1) HlB zuerst — BrT und VL haengen davon ab.
  const halsansatzUmfangCm = finiteValue(values, "neck_base_circumference");
  const halslochbreiteCm = halsansatzUmfangCm !== undefined
    ? halsansatzUmfangCm / 6 + 0.5
    : undefined;

  // 2) BrT = Ø(gBrT) - HlB
  const gemesseneBrusttiefeCm = mean(
    finiteValue(values, "measured_bust_depth_right"),
    finiteValue(values, "measured_bust_depth_left")
  );
  const brusttiefeCm = gemesseneBrusttiefeCm !== undefined && halslochbreiteCm !== undefined
    ? gemesseneBrusttiefeCm - halslochbreiteCm
    : undefined;

  // 3) VL = Ø(gVL) - HlB + Taillenschraeglage vorne (Vorzeichen durchgereicht)
  const gemesseneVorderlaengeCm = mean(
    finiteValue(values, "measured_front_length_right"),
    finiteValue(values, "measured_front_length_left")
  );
  const taillenschraeglageVorneCm = finiteValue(values, "waist_slope_front_cm");
  const vorderlaengeCm = gemesseneVorderlaengeCm !== undefined && halslochbreiteCm !== undefined
    ? gemesseneVorderlaengeCm - halslochbreiteCm + (taillenschraeglageVorneCm ?? 0)
    : undefined;

  const taillenschraeglageDefaulted =
    vorderlaengeCm !== undefined && taillenschraeglageVorneCm === undefined;

  return {
    halsansatzUmfangCm,
    halslochbreiteCm,
    gemesseneBrusttiefeCm,
    brusttiefeCm,
    gemesseneVorderlaengeCm,
    vorderlaengeCm,
    taillenschraeglageVorneCm,
    taillenschraeglageDefaulted
  };
}
