import { test } from "node:test";
import assert from "node:assert/strict";

import {
  bridalValuesToStraightSkirtInput,
  HIP_DEPTH_MEASUREMENT_ID,
  STRAIGHT_SKIRT_BODY_MAP
} from "../src/dress/straight-skirt-measurement-adapter.js";
import { draftStraightSkirt } from "../src/drafting/straight-skirt.js";
import { createBridalMeasurementProfile } from "../src/measurements/bridal-body-measurements.js";

// Hofenbitzer Gr.38-Referenz: TaU 72, HueU 97 -> reproduziert den verifizierten Fall.
const REFERENCE_VALUES = Object.freeze({
  waist_circumference_horizontal: 72,
  hip_circumference_horizontal: 97,
  [HIP_DEPTH_MEASUREMENT_ID]: 21
});

test("maps waist, hip and hip-depth onto the engine input and takes length from config", () => {
  const result = bridalValuesToStraightSkirtInput(REFERENCE_VALUES, { lengthCm: 60 });
  assert.equal(result.ok, true);
  assert.deepEqual(result.input, {
    waistCm: 72,
    hipCm: 97,
    waistToHipCm: 21,
    lengthCm: 60
  });
});

test("stops instead of guessing when hip-depth (HueT) is missing", () => {
  const { [HIP_DEPTH_MEASUREMENT_ID]: _drop, ...withoutHipDepth } = REFERENCE_VALUES;
  const result = bridalValuesToStraightSkirtInput(withoutHipDepth, { lengthCm: 60 });
  assert.equal(result.ok, false);
  assert.deepEqual(result.missing, [HIP_DEPTH_MEASUREMENT_ID]);
  // Kein gedefaulteter 21-cm-Buchwert im Ergebnis.
  assert.equal("input" in result, false);
});

test("stops when the design length is not configured", () => {
  const result = bridalValuesToStraightSkirtInput(REFERENCE_VALUES, {});
  assert.equal(result.ok, false);
  assert.deepEqual(result.missing, ["config.lengthCm"]);
});

test("reports every missing body measure at once, in map order", () => {
  const result = bridalValuesToStraightSkirtInput({}, {});
  assert.equal(result.ok, false);
  assert.deepEqual(result.missing, [
    "waist_circumference_horizontal",
    "hip_circumference_horizontal",
    HIP_DEPTH_MEASUREMENT_ID,
    "config.lengthCm"
  ]);
});

test("ignores empty strings / non-finite values as if unmeasured (no coercion here)", () => {
  const dirty = { ...REFERENCE_VALUES, hip_circumference_horizontal: NaN };
  const result = bridalValuesToStraightSkirtInput(dirty, { lengthCm: 60 });
  assert.equal(result.ok, false);
  assert.deepEqual(result.missing, ["hip_circumference_horizontal"]);
});

test("real body measures win over stray same-named config keys", () => {
  const result = bridalValuesToStraightSkirtInput(REFERENCE_VALUES, { lengthCm: 60, waistCm: 999 });
  assert.equal(result.ok, true);
  assert.equal(result.input.waistCm, 72);
});

test("passes engine overrides (e.g. overlapCm) through from config", () => {
  const result = bridalValuesToStraightSkirtInput(REFERENCE_VALUES, { lengthCm: 60, overlapCm: 0 });
  assert.equal(result.ok, true);
  assert.equal(result.input.overlapCm, 0);
});

test("end-to-end: adapter output drafts a valid Hofenbitzer straight skirt", () => {
  const result = bridalValuesToStraightSkirtInput(REFERENCE_VALUES, { lengthCm: 60 });
  assert.equal(result.ok, true);
  const block = draftStraightSkirt(result.input);
  assert.equal(block.metadata.methodStatus, "verified");
  assert.deepEqual(block.pieces.map((p) => p.id), ["back", "front", "waistband"]);
  // Die durchgereichten Koerpermasse landen unveraendert im Schnitt-Metadatensatz.
  assert.deepEqual(block.metadata.measurements, {
    waistCm: 72,
    hipCm: 97,
    waistToHipCm: 21,
    lengthCm: 60
  });
});

test("map is stable and hip-depth id is the single point of change", () => {
  assert.equal(STRAIGHT_SKIRT_BODY_MAP.waistToHipCm, HIP_DEPTH_MEASUREMENT_ID);
  assert.equal(STRAIGHT_SKIRT_BODY_MAP.waistCm, "waist_circumference_horizontal");
  assert.equal(STRAIGHT_SKIRT_BODY_MAP.hipCm, "hip_circumference_horizontal");
});

test("profile payoff: measured hip depth reaches the straight-skirt adapter", () => {
  const profile = createBridalMeasurementProfile({
    shapeId: "a_line",
    values: REFERENCE_VALUES
  });
  const values = Object.fromEntries(profile.measurements.map(({ id, value }) => [id, value]));
  assert.equal(bridalValuesToStraightSkirtInput(values, { lengthCm: 60 }).ok, true);

  delete values.waist_to_hip;
  const missing = bridalValuesToStraightSkirtInput(values, { lengthCm: 60 });
  assert.equal(missing.ok, false);
  assert.ok(missing.missing.includes("waist_to_hip"));
});

// #24: Der fruehere Honesty-Test (95/97, Adapter reicht durch, Engine wirft nackt)
// beschrieb den alten offenen Zustand. Neuer Vertrag: Der Adapter klassifiziert
// Niedrig-Differenz selbst — mit Munkhuus ECHTEN Werten 94/96.
const MUNKHUU_REAL_VALUES = Object.freeze({
  waist_circumference_horizontal: 94,
  hip_circumference_horizontal: 96,
  [HIP_DEPTH_MEASUREMENT_ID]: 20
});

const MUNKHUU_DETAIL = Object.freeze({
  hipWaistDifferenceMm: 20,
  requiredHipWaistDifferenceExclusiveMm: 90,
  waistSuppressionMm: 15,
  requiredWaistSuppressionExclusiveMm: 50,
  sideHipIntakeMm: 7.5,
  frontDartIntakeMm: 25,
  backDartTotalIntakeMm: -17.5
});

test("niedrig-differenz: real Munkhuu 94/96 returns the structured domain signal, no input, no missing", () => {
  const result = bridalValuesToStraightSkirtInput(MUNKHUU_REAL_VALUES, { lengthCm: 60 });
  assert.deepEqual(result, {
    ok: false,
    reason: "NIEDRIG_DIFFERENZ",
    detail: MUNKHUU_DETAIL
  });
  assert.equal("input" in result, false);
  assert.equal("missing" in result, false);
  assert.ok(Object.isFrozen(result));
  assert.ok(Object.isFrozen(result.detail));
});

test("niedrig-differenz: adapter detail is byte-identical to the typed engine error detail", () => {
  const result = bridalValuesToStraightSkirtInput(MUNKHUU_REAL_VALUES, { lengthCm: 60 });
  let engineError = null;
  try {
    draftStraightSkirt({ waistCm: 94, hipCm: 96, waistToHipCm: 20, lengthCm: 60 });
  } catch (e) {
    engineError = e;
  }
  assert.ok(engineError, "engine still rejects 94/96 with defaults");
  assert.equal(engineError.code, "NIEDRIG_DIFFERENZ");
  assert.match(engineError.message, /back dart intake/);
  assert.deepEqual(result.detail, engineError.detail);
});

test("niedrig-differenz: missing gate still wins over classification", () => {
  const { waist_circumference_horizontal: _drop, ...withoutWaist } = MUNKHUU_REAL_VALUES;
  const result = bridalValuesToStraightSkirtInput(withoutWaist, { lengthCm: 60 });
  assert.equal(result.ok, false);
  assert.deepEqual(result.missing, ["waist_circumference_horizontal"]);
  assert.equal("detail" in result, false);
});

test("niedrig-differenz: otherwise invalid config overrides are NOT misclassified — engine validation stays responsible", () => {
  // waistEaseCm 99 liegt ausserhalb der Buchgrenzen: Der Adapter enthaelt sich
  // (ok:true, Durchreichen), die bestehende Engine-Validierung wirft wie bisher.
  const result = bridalValuesToStraightSkirtInput(MUNKHUU_REAL_VALUES, { lengthCm: 60, waistEaseCm: 99 });
  assert.equal(result.ok, true);
  assert.throws(() => draftStraightSkirt(result.input), /waistEaseCm/);

  // Nicht-finite Overrides ebenso: kein neuer Adapter-Throw, keine Umetikettierung.
  const nonFinite = bridalValuesToStraightSkirtInput(MUNKHUU_REAL_VALUES, { lengthCm: 60, hipEaseCm: Number.NaN });
  assert.equal(nonFinite.ok, true);
  assert.throws(() => draftStraightSkirt(nonFinite.input), /hipEaseCm/);
});

test("niedrig-differenz: body measures still win over same-named config keys in classification", () => {
  // Config-waistCm 72 wuerde gesund rechnen — das echte Koerpermass 94 gewinnt
  // und fuehrt zum Domänensignal.
  const result = bridalValuesToStraightSkirtInput(MUNKHUU_REAL_VALUES, { lengthCm: 60, waistCm: 72 });
  assert.equal(result.ok, false);
  assert.equal(result.reason, "NIEDRIG_DIFFERENZ");
  assert.deepEqual(result.detail, MUNKHUU_DETAIL);
});
