// Adapter: Braut-Masssatz (S.11-15-IDs aus src/measurements/bridal-body-measurements.js)
// -> Engine-Input fuer draftStraightSkirt (src/drafting/straight-skirt.js).
//
// SCOPE: NUR gerader Rock (Werner-Entscheid Option A, 2026-07-10).
//  - TaU (waist_circumference_horizontal) -> waistCm   (die Engine halbiert selbst)
//  - HueU (hip_circumference_horizontal)  -> hipCm     (die Engine halbiert selbst)
//  - HueT (waist_to_hip)                  -> waistToHipCm  (echtes Koerpermass)
//  - lengthCm = Design/Konfiguration, KEIN Koerpermass -> kommt aus `config`.
//
// STOPP STATT RATEN: Fehlt ein Koerpermass oder die Rocklaenge, liefert der Adapter
// { ok:false, missing:[...] } zurueck. KEIN Default, KEIN Gr.38-Buchwert (21 cm) —
// das war die alte Wand im dress-Adapter (bridal-measurement-adapter.js).
//
// #24 NIEDRIG-DIFFERENZ: Nach dem Missing-Gate klassifiziert der Adapter den
// vollstaendigen Engine-Input ueber DIESELBE Formelquelle wie die Engine
// (src/drafting/niedrig-differenz.js) und liefert { ok:false,
// reason:"NIEDRIG_DIFFERENZ", detail:{...} } — ohne input, ohne missing.
// Bei sonst ungueltigen Config-Overrides (z.B. Ease ausserhalb der Buchgrenzen)
// klassifiziert er NICHT und laesst die bestehende Engine-Validierung entscheiden.

import { classifyNiedrigDifferenzMm } from "../drafting/niedrig-differenz.js";
import {
  applyStraightSkirtMethodDefaults,
  validateStraightSkirt
} from "../drafting/straight-skirt.js";

const cmToMm = (value) => value * 10;

function classifyResolvedInput(input) {
  let resolved;
  try {
    // Exakt die Aufloesung + Validierung, die draftStraightSkirt selbst faehrt.
    // Wirft die Validierung (ungueltige Overrides, hip<=waist, ...), entscheidet
    // weiterhin die Engine beim Draft — der Adapter etikettiert nichts um.
    resolved = validateStraightSkirt(applyStraightSkirtMethodDefaults(input));
  } catch {
    return { ok: true };
  }
  return classifyNiedrigDifferenzMm({
    hipMm: cmToMm(resolved.hipCm),
    waistMm: cmToMm(resolved.waistCm),
    hipEaseMm: cmToMm(resolved.hipEaseCm),
    waistEaseMm: cmToMm(resolved.waistEaseCm),
    sideHipShapeAdjustmentMm: cmToMm(resolved.sideHipShapeAdjustmentCm),
    frontDartIntakeMm: cmToMm(resolved.frontDartIntakeCm)
  });
}

// HueT-Messstrecke im Messmodul. Einzeiler-Wechsel, falls Werner eine andere id waehlt.
export const HIP_DEPTH_MEASUREMENT_ID = "waist_to_hip";

// Engine-Eingang -> Mess-id. Reihenfolge = Reihenfolge der Fehlermeldung.
export const STRAIGHT_SKIRT_BODY_MAP = Object.freeze({
  waistCm: "waist_circumference_horizontal",
  hipCm: "hip_circumference_horizontal",
  waistToHipCm: HIP_DEPTH_MEASUREMENT_ID
});

function finiteValue(values, id) {
  return Number.isFinite(values?.[id]) ? values[id] : undefined;
}

/**
 * Bildet einen (bereits zu Zahlen normalisierten) Braut-Masssatz auf den
 * geraden-Rock-Engine-Input ab. Rein, ohne Seiteneffekt, ohne throw.
 *
 * @param {Record<string, number>} values  Mess-id -> Zahl (z.B. coerceMeasurementValues-Ausgabe)
 * @param {{ lengthCm?: number, [k: string]: unknown }} config  Design/Konfiguration (Rocklaenge etc.)
 * @returns {{ ok: true, input: object }
 *   | { ok: false, missing: string[], reason: string }
 *   | { ok: false, reason: "NIEDRIG_DIFFERENZ", detail: object }}
 */
export function bridalValuesToStraightSkirtInput(values = {}, config = {}) {
  const missing = [];
  const body = {};

  for (const [engineKey, measurementId] of Object.entries(STRAIGHT_SKIRT_BODY_MAP)) {
    const value = finiteValue(values, measurementId);
    if (value === undefined) missing.push(measurementId);
    else body[engineKey] = value;
  }

  const lengthCm = Number.isFinite(config.lengthCm) ? config.lengthCm : undefined;
  if (lengthCm === undefined) missing.push("config.lengthCm");

  if (missing.length > 0) {
    return Object.freeze({
      ok: false,
      missing: Object.freeze(missing),
      reason: "Fehlende Koerpermasse oder Rocklaenge — Adapter stoppt statt zu raten."
    });
  }

  // Koerpermasse gewinnen ueber etwaige gleichnamige config-Schluessel; lengthCm aus config.
  const input = Object.freeze({ ...config, ...body, lengthCm });

  // #24: Niedrig-Differenz-Klassifikation NACH dem Missing-Gate, gleiche Quelle wie die Engine.
  const niedrigDifferenz = classifyResolvedInput(input);
  if (niedrigDifferenz.ok === false) {
    return Object.freeze({
      ok: false,
      reason: niedrigDifferenz.reason,
      detail: niedrigDifferenz.detail
    });
  }

  return Object.freeze({ ok: true, input });
}
