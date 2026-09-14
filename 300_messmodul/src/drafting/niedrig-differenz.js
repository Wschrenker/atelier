// #24: Einzige Rechen- und Klassifikationsquelle für die Niedrig-Differenz-Wand
// des Hofenbitzer-Rocks (Guard 3 in deriveStraightSkirtMeasures).
//
// Fachlicher Hintergrund: Hofenbitzer Band 1, S.33-34 verteilt den Taillenausfall
// auf Seitennaht, vorderen und hintere(n) Abnäher. Bei zu kleiner Taille-Hüft-
// Differenz bleibt kein positiver hinterer Abnäher übrig — die Methode deckt
// diesen Figurfall nicht. Es wird KEINE Geometrie erfunden; die Apfel-Geometrie
// wird erst nach der realen Rock-Toile festgelegt (SSOT #24).
//
// deriveSuppressionMm ist die EINE Rechenquelle für die Suppressionskette
// (Millimeter). Klassifikation (hier) und Geometriepfad
// (deriveStraightSkirtMeasures in straight-skirt.js) rechnen nicht mehr
// getrennt, sondern beziehen beide aus dieser Kette:
//   hipWidth         = hip + hipEase
//   waistWidth       = waist + waistEase
//   halfHipWidth     = hipWidth / 2
//   quarterHipWidth  = hipWidth / 4
//   halfWaistWidth   = waistWidth / 2
//   waistSuppression = halfHipWidth - halfWaistWidth
//   sideHipIntake    = waistSuppression/2 + sideHipShapeAdjustment
//   frontDartIntake  = frontDartIntake
//   backDartTotal    = waistSuppression - sideHipIntake - frontDartIntake
//
// NIEDRIG_DIFFERENZ gilt NUR, wenn die früheren Guards passieren würden
// (waistSuppression > 0 und gültiger sideHipIntake) und backDartTotal <= 0.
// Guard-1-/Guard-2-Fälle und nicht-finite Eingaben liefern { ok: true } —
// dort bleiben die bestehenden Fehler/Validierungen zuständig.

export const NIEDRIG_DIFFERENZ = "NIEDRIG_DIFFERENZ";

const OK = Object.freeze({ ok: true });

export function deriveSuppressionMm({
  hipMm,
  waistMm,
  hipEaseMm,
  waistEaseMm,
  sideHipShapeAdjustmentMm,
  frontDartIntakeMm
} = {}) {
  const hipWidth = hipMm + hipEaseMm;
  const waistWidth = waistMm + waistEaseMm;
  const halfHipWidth = hipWidth / 2;
  const quarterHipWidth = hipWidth / 4;
  const halfWaistWidth = waistWidth / 2;
  const waistSuppression = halfHipWidth - halfWaistWidth;
  const sideHipIntake = waistSuppression / 2 + sideHipShapeAdjustmentMm;
  const frontDartIntake = frontDartIntakeMm;
  const backDartTotalIntake = waistSuppression - sideHipIntake - frontDartIntake;

  return Object.freeze({
    hipWidth,
    waistWidth,
    halfHipWidth,
    quarterHipWidth,
    halfWaistWidth,
    waistSuppression,
    sideHipIntake,
    frontDartIntake,
    backDartTotalIntake
  });
}

export function classifyNiedrigDifferenzMm({
  hipMm,
  waistMm,
  hipEaseMm,
  waistEaseMm,
  sideHipShapeAdjustmentMm,
  frontDartIntakeMm
} = {}) {
  const inputs = [hipMm, waistMm, hipEaseMm, waistEaseMm, sideHipShapeAdjustmentMm, frontDartIntakeMm];
  if (!inputs.every(Number.isFinite)) return OK;

  const derived = deriveSuppressionMm({
    hipMm,
    waistMm,
    hipEaseMm,
    waistEaseMm,
    sideHipShapeAdjustmentMm,
    frontDartIntakeMm
  });

  if (derived.waistSuppression <= 0) return OK;
  if (derived.sideHipIntake <= 0 || derived.sideHipIntake >= derived.waistSuppression) return OK;
  if (derived.backDartTotalIntake > 0) return OK;

  return Object.freeze({
    ok: false,
    reason: NIEDRIG_DIFFERENZ,
    detail: Object.freeze({
      hipWaistDifferenceMm: hipMm - waistMm,
      requiredHipWaistDifferenceExclusiveMm:
        4 * (sideHipShapeAdjustmentMm + frontDartIntakeMm) - hipEaseMm + waistEaseMm,
      waistSuppressionMm: derived.waistSuppression,
      requiredWaistSuppressionExclusiveMm: 2 * (sideHipShapeAdjustmentMm + frontDartIntakeMm),
      sideHipIntakeMm: derived.sideHipIntake,
      frontDartIntakeMm: derived.frontDartIntake,
      backDartTotalIntakeMm: derived.backDartTotalIntake
    })
  });
}
