// BLUEPRINTSHOT (Discovery) — Adapter Braut-Masssatz (S.11-15-IDs aus
// src/measurements/bridal-body-measurements.js) -> Kleid-Konstruktions-Inputs.
//
// Kompatibilitaets-Wrapper: die S.19-Laengenmasse HlB/BrT/VL kommen aus der
// geteilten Ableitung s19-length-derivations.js (dieselbe wie im kanonischen
// bridal-measurement-bodice-adapter.js) — kein Formelsatz doppelt. HueT ist das
// echte Profilmass waist_to_hip (kein Platzhalter 21); fehlt es, ehrlicher Gap.

import { deriveS19ConstructionLengths } from "./s19-length-derivations.js";

const mean = (...values) => {
  const usable = values.filter((value) => Number.isFinite(value));
  if (usable.length === 0) return undefined;
  return usable.reduce((total, value) => total + value, 0) / usable.length;
};

export function bridalValuesToDressMeasurements(values = {}) {
  const gaps = [];
  const v = (id) => (Number.isFinite(values[id]) ? values[id] : undefined);

  // ---- sauber ableitbar (S.12-15, transkribiert) ----
  const brustUmfangCm = v("bust_circumference");
  const taillenUmfangCm = v("waist_circumference_horizontal");
  const hueftUmfangCm = v("hip_circumference_horizontal");
  const koeHCm = v("body_height");
  const armlochtiefeCm = v("armhole_depth"); // AlT gemessen (Papierstreifen, S.14)
  const rueckenbreiteHalbCm = v("measured_back_width") !== undefined
    ? v("measured_back_width") / 2 // RueB = gRueB : 2 (S.14)
    : undefined;
  const oaU = mean(v("upper_arm_circumference_right"), v("upper_arm_circumference_left"));
  const gArD = mean(v("measured_arm_diameter_right"), v("measured_arm_diameter_left"));
  // ArD: Durchschnitt der Messungen; sicherere Alternative OaU*0,6-7,5 (S.14)
  const armdurchmesserCm = gArD ?? (oaU !== undefined ? oaU * 0.6 - 7.5 : undefined);
  // BrB = gBrB:2 oder BrU:2 - RueB - ArD (S.14)
  const brustbreiteHalbCm = v("measured_bust_width") !== undefined
    ? v("measured_bust_width") / 2
    : (brustUmfangCm !== undefined && rueckenbreiteHalbCm !== undefined && armdurchmesserCm !== undefined
      ? brustUmfangCm / 2 - rueckenbreiteHalbCm - armdurchmesserCm
      : undefined);
  const schulterbreiteCm = mean(v("shoulder_width_right"), v("shoulder_width_left")); // Mittelwert (S.15)
  const suWiRight = v("shoulder_angle_right");
  const suWiLeft = v("shoulder_angle_left");
  // S.15: bei ungleichen Werten den KLEINEREN verwenden
  const schulterwinkelGrad = suWiRight !== undefined && suWiLeft !== undefined
    ? Math.min(suWiRight, suWiLeft)
    : suWiRight ?? suWiLeft;
  // ANNAHME: RueL = gRueL (Taillenschraeglage-Korrektur muesste manuell erfolgen, S.13)
  const rueckenlaengeCm = v("measured_back_length");

  // ---- Konstruktionsmasse nach S.19 (geteilte kanonische Ableitung) ----
  const s19 = deriveS19ConstructionLengths(values);
  const halslochbreiteCm = s19.halslochbreiteCm;
  const brusttiefeCm = s19.brusttiefeCm;
  const vorderlaengeCm = s19.vorderlaengeCm;

  // HueT: echtes Profilmass waist_to_hip (S.20-31) — kein Platzhalter, kein Default 21.
  const huefttiefeCm = v("waist_to_hip");
  if (huefttiefeCm === undefined) {
    gaps.push("HueT: waist_to_hip fehlt — nicht berechenbar");
  }
  if (halslochbreiteCm === undefined) {
    gaps.push("HlB/BrT/VL: HaU (neck_base_circumference) fehlt — nicht berechenbar");
  }
  if (s19.taillenschraeglageDefaulted) {
    gaps.push("VL: Taillenschräglage-vorne-Korrektur nicht angewendet (manueller Beobachtungswert, default 0)");
  }

  return {
    measurements: {
      koeHCm,
      brustUmfangCm,
      taillenUmfangCm,
      hueftUmfangCm,
      armlochtiefeCm,
      huefttiefeCm,
      brusttiefeCm,
      halslochbreiteCm,
      rueckenbreiteHalbCm,
      armdurchmesserCm,
      brustbreiteHalbCm,
      schulterbreiteCm,
      schulterwinkelGrad,
      rueckenlaengeCm,
      vorderlaengeCm
    },
    gaps
  };
}
