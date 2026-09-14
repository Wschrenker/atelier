import assert from "node:assert/strict";
import test from "node:test";
import { bridalValuesToDressMeasurements } from "../src/dress/bridal-measurement-adapter.js";

const fehlendesHaUGap = "HlB/BrT/VL: HaU (neck_base_circumference) fehlt — nicht berechenbar";
const huefttiefeMissingGap = "HueT: waist_to_hip fehlt — nicht berechenbar";
const vorderlaengeAdvisory = "VL: Taillenschräglage-vorne-Korrektur nicht angewendet (manueller Beobachtungswert, default 0)";

test("HlB wird nach S.19 aus HaU berechnet", () => {
  const { measurements } = bridalValuesToDressMeasurements({
    neck_base_circumference: 36
  });

  assert.equal(measurements.halslochbreiteCm, 6.5);
});

test("BrT ist der gBrT-Durchschnitt abzueglich HlB", () => {
  const { measurements } = bridalValuesToDressMeasurements({
    neck_base_circumference: 36,
    measured_bust_depth_right: 27,
    measured_bust_depth_left: 27
  });

  assert.equal(measurements.brusttiefeCm, 20.5);
});

test("VL verwendet ohne Taillenschraeglage den Default 0 und meldet das Advisory", () => {
  const result = bridalValuesToDressMeasurements({
    neck_base_circumference: 36,
    measured_front_length_right: 44,
    measured_front_length_left: 44
  });

  assert.equal(result.measurements.vorderlaengeCm, 37.5);
  assert.deepEqual(result.gaps, [huefttiefeMissingGap, vorderlaengeAdvisory]);
});

test("VL addiert eine vorzeichenbehaftete Taillenschraeglage ohne Advisory", () => {
  const result = bridalValuesToDressMeasurements({
    neck_base_circumference: 36,
    measured_front_length_right: 44,
    measured_front_length_left: 44,
    waist_slope_front_cm: 1
  });

  assert.equal(result.measurements.vorderlaengeCm, 38.5);
  assert.deepEqual(result.gaps, [huefttiefeMissingGap]);
});

test("fehlendes HaU blockiert HlB, BrT und VL mit einem deterministischen Gap", () => {
  const result = bridalValuesToDressMeasurements({
    measured_bust_depth_right: 27,
    measured_bust_depth_left: 27,
    measured_front_length_right: 44,
    measured_front_length_left: 44
  });

  assert.equal(result.measurements.halslochbreiteCm, undefined);
  assert.equal(result.measurements.brusttiefeCm, undefined);
  assert.equal(result.measurements.vorderlaengeCm, undefined);
  assert.deepEqual(result.gaps, [huefttiefeMissingGap, fehlendesHaUGap]);
});

test("leerer Input wirft nicht und behaelt nur die vorgesehenen offenen Gaps", () => {
  let result;
  assert.doesNotThrow(() => {
    result = bridalValuesToDressMeasurements({});
  });

  assert.equal(result.measurements.halslochbreiteCm, undefined);
  assert.equal(result.measurements.brusttiefeCm, undefined);
  assert.equal(result.measurements.vorderlaengeCm, undefined);
  assert.equal(result.measurements.huefttiefeCm, undefined);
  assert.deepEqual(result.gaps, [huefttiefeMissingGap, fehlendesHaUGap]);
});

// ---- HueT-Wahrheit: echtes Profilmass statt Platzhalter 21 ----

test("HueT 23 bleibt exakt 23 — kein Placeholder-Gap, kein Default 21", () => {
  const result = bridalValuesToDressMeasurements({ waist_to_hip: 23 });

  assert.equal(result.measurements.huefttiefeCm, 23);
  assert.equal(result.gaps.includes(huefttiefeMissingGap), false);
  assert.ok(result.gaps.every((gap) => !gap.includes("21")));
});

test("fehlende HueT bleibt undefined und erzeugt den deterministischen Gap", () => {
  const result = bridalValuesToDressMeasurements({ neck_base_circumference: 36 });

  assert.equal(result.measurements.huefttiefeCm, undefined);
  assert.ok(result.gaps.includes(huefttiefeMissingGap));
});

test("HueT ist das echte Profilmass (kein konstanter Default 21 in irgendeinem Pfad)", () => {
  assert.equal(bridalValuesToDressMeasurements({ waist_to_hip: 20 }).measurements.huefttiefeCm, 20);
  assert.equal(bridalValuesToDressMeasurements({ waist_to_hip: 25 }).measurements.huefttiefeCm, 25);
  assert.equal(bridalValuesToDressMeasurements({}).measurements.huefttiefeCm, undefined);
});
