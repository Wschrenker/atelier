import { test } from "node:test";
import * as assert from "node:assert/strict";
import { bridalValuesToBodiceInput } from "./bridal-measurement-bodice-adapter.js";
import { bridalValuesToDressMeasurements } from "./bridal-measurement-adapter.js";
import { draftBodiceBlock } from "../drafting/bodice-block.js";
import { createBridalMeasurementProfile } from "../measurements/bridal-body-measurements.js";

// Rein erfundene, plausible Masse (Gr.38-nah). Keine echten Namen / PII (#15).
// HaU 36 -> HlB 6,5 ; gBrT 27 -> BrT 20,5 ; gVL 51,6 -> VL 45,1.
// gVL seit Etappe 3 balance-plausibel (VL - RueL = 45,1 - 41,6 = 3,5 = optimale
// Balance bei BrU 88), damit das Balance-Gate den Referenzfall nicht stoppt —
// die alte gVL 44 war figurunplausibel (Abweichung 7,6 cm).
const fullMeasurements = {
  body_height: 168,
  bust_circumference: 88,
  waist_circumference_horizontal: 72,
  hip_circumference_horizontal: 97,
  armhole_depth: 20.1,
  waist_to_hip: 21,
  neck_base_circumference: 36,
  measured_bust_depth_right: 27,
  measured_bust_depth_left: 27,
  measured_back_width: 33,
  measured_arm_diameter_right: 9.3,
  measured_arm_diameter_left: 9.3,
  measured_bust_width: 36.4,
  shoulder_width_right: 12.2,
  shoulder_width_left: 12.2,
  shoulder_angle_right: 20,
  shoulder_angle_left: 22,
  measured_back_length: 41.6,
  measured_front_length_right: 51.6,
  measured_front_length_left: 51.6
};
const validConfig = Object.freeze({ modellLaengeCm: 95, passformklasse: 3 });

const TAILLENSCHRAEGLAGE_ADVISORY = "TAILLENSCHRAEGLAGE_DEFAULT_0";

test("bridalValuesToBodiceInput (kanonisch)", async (t) => {
  await t.test("Referenzfall: alle Masse + Config vorhanden -> ok:true", () => {
    const result = bridalValuesToBodiceInput(fullMeasurements, validConfig);
    assert.equal(result.ok, true);
    assert.ok(result.input);
    assert.equal(result.input.koeHCm, 168);
    assert.equal(result.input.brustUmfangCm, 88);
    assert.equal(result.input.modellLaengeCm, 95);
    assert.equal(result.input.passformklasse, 3);
    assert.equal(result.input.halslochbreiteCm, 6.5); // #1 HlB = 36/6 + 0,5
    assert.equal("bodiceBlock" in result.input, false);
    assert.equal("bodiceOptions" in result.input, false);
  });

  await t.test("#1 HlB wird nach S.19 aus HaU berechnet (36 -> 6,5)", () => {
    const result = bridalValuesToBodiceInput(fullMeasurements, validConfig);
    assert.equal(result.input.halslochbreiteCm, 6.5);
  });

  await t.test("#2 BrT = Ø(gBrT) - HlB (27/27, HlB 6,5 -> 20,5)", () => {
    const result = bridalValuesToBodiceInput(fullMeasurements, validConfig);
    assert.equal(result.input.brusttiefeCm, 20.5);
  });

  await t.test("#2b BrT mittelt bilateral vor dem HlB-Abzug (26/28 -> 27 -> 20,5)", () => {
    const values = { ...fullMeasurements, measured_bust_depth_right: 26, measured_bust_depth_left: 28 };
    const result = bridalValuesToBodiceInput(values, validConfig);
    assert.equal(result.input.brusttiefeCm, 20.5);
  });

  await t.test("#3 VL = Ø(gVL) - HlB ohne Schraeglage (51,6/51,6 -> 45,1) + Advisory (#4)", () => {
    const result = bridalValuesToBodiceInput(fullMeasurements, validConfig);
    assert.equal(result.input.vorderlaengeCm, 45.1);
    assert.ok(result.advisories.includes(TAILLENSCHRAEGLAGE_ADVISORY));
  });

  await t.test("#5 Schraeglage +1 -> VL 46,1, kein Advisory", () => {
    const values = { ...fullMeasurements, waist_slope_front_cm: 1 };
    const result = bridalValuesToBodiceInput(values, validConfig);
    assert.equal(result.input.vorderlaengeCm, 46.1);
    assert.equal(result.advisories.includes(TAILLENSCHRAEGLAGE_ADVISORY), false);
  });

  await t.test("#6 Schraeglage -1 (Vorzeichen durchgereicht) -> VL 44,1, kein Advisory", () => {
    const values = { ...fullMeasurements, waist_slope_front_cm: -1 };
    const result = bridalValuesToBodiceInput(values, validConfig);
    assert.equal(result.input.vorderlaengeCm, 44.1);
    assert.equal(result.advisories.includes(TAILLENSCHRAEGLAGE_ADVISORY), false);
  });

  await t.test("#7 Echte HueT: huefttiefeCm = waist_to_hip (23), kein Default 21", () => {
    const values = { ...fullMeasurements, waist_to_hip: 23 };
    const result = bridalValuesToBodiceInput(values, validConfig);
    assert.equal(result.input.huefttiefeCm, 23);
  });

  await t.test("#8 Fehlende HueT stoppt (kein stiller Default 21)", () => {
    const values = { ...fullMeasurements };
    delete values.waist_to_hip;
    const result = bridalValuesToBodiceInput(values, validConfig);
    assert.equal(result.ok, false);
    assert.ok(result.missing.includes("waist_to_hip"));
    assert.equal("input" in result, false);
  });

  await t.test("#9 Fehlende HaU stoppt HlB/BrT/VL", () => {
    const values = { ...fullMeasurements };
    delete values.neck_base_circumference;
    const result = bridalValuesToBodiceInput(values, validConfig);
    assert.equal(result.ok, false);
    assert.ok(result.missing.includes("neck_base_circumference"));
  });

  await t.test("#10 Fehlende Modelllaenge stoppt", () => {
    const result = bridalValuesToBodiceInput(fullMeasurements, { passformklasse: 3 });
    assert.equal(result.ok, false);
    assert.ok(result.missing.includes("config.modellLaengeCm"));
  });

  await t.test("#11 Fehlende Passformklasse stoppt (kein stiller PK3-Default)", () => {
    const result = bridalValuesToBodiceInput(fullMeasurements, { modellLaengeCm: 95 });
    assert.equal(result.ok, false);
    assert.ok(result.missing.includes("config.passformklasse"));
  });

  await t.test("#11b Ungueltige Passformklasse (2) stoppt — nur 3/4/5 erlaubt", () => {
    const result = bridalValuesToBodiceInput(fullMeasurements, { modellLaengeCm: 95, passformklasse: 2 });
    assert.equal(result.ok, false);
    assert.ok(result.missing.some((m) => m.includes("passformklasse")));
  });

  await t.test("#12 Nichtpositives berechnetes BrT stoppt", () => {
    // gBrT 6/6 -> BrT = 6 - 6,5 = -0,5 (nicht positiv)
    const values = { ...fullMeasurements, measured_bust_depth_right: 6, measured_bust_depth_left: 6 };
    const result = bridalValuesToBodiceInput(values, validConfig);
    assert.equal(result.ok, false);
    assert.ok(result.missing.some((m) => m.includes("brusttiefeCm")));
  });

  await t.test("Schulterwinkel: Minimum der zwei Seiten", () => {
    const values = { ...fullMeasurements, shoulder_angle_right: 25, shoulder_angle_left: 20 };
    const result = bridalValuesToBodiceInput(values, validConfig);
    assert.equal(result.input.schulterwinkelGrad, 20);
  });

  await t.test("RueB und BrB werden halbiert", () => {
    const result = bridalValuesToBodiceInput(fullMeasurements, validConfig);
    assert.equal(result.input.rueckenbreiteHalbCm, 16.5);
    assert.equal(result.input.brustbreiteHalbCm, 18.2);
  });

  await t.test("Fehlendes Koerpermass -> ok:false, missing[]", () => {
    const values = { ...fullMeasurements };
    delete values.bust_circumference;
    const result = bridalValuesToBodiceInput(values, validConfig);
    assert.equal(result.ok, false);
    assert.ok(result.missing.includes("bust_circumference"));
  });

  await t.test("Optionale Abnaeher-Laengen liegen flach im Input, Rest undefined", () => {
    const result = bridalValuesToBodiceInput(fullMeasurements, {
      ...validConfig, passformklasse: 4, shAblLaengeCm: 14, hAblLaengeCm: 16
    });
    assert.equal(result.input.passformklasse, 4);
    assert.equal(result.input.shAblLaengeCm, 14);
    assert.equal(result.input.hAblLaengeCm, 16);

    const bare = bridalValuesToBodiceInput(fullMeasurements, validConfig);
    assert.equal(bare.input.shAblLaengeCm, undefined);
    assert.equal(bare.input.hAblLaengeCm, undefined);
  });

  await t.test("#13 E2E: Profil -> Adapter -> draftBodiceBlock -> gueltiger Block", () => {
    const profile = createBridalMeasurementProfile({ shapeId: "a_line", values: fullMeasurements });
    const values = Object.fromEntries(profile.measurements.map(({ id, value }) => [id, value]));
    const result = bridalValuesToBodiceInput(values, validConfig);
    assert.equal(result.ok, true);

    const block = draftBodiceBlock(result.input);
    assert.deepEqual(block.pieces.map(({ id }) => id), ["back", "front"]);
    for (const piece of block.pieces) {
      assert.deepEqual(piece.seamLine[0], piece.seamLine.at(-1));
      assert.ok(piece.seamLine.every(({ x, y }) => Number.isFinite(x) && Number.isFinite(y)));
      assert.ok(piece.cuttingLine.every(({ x, y }) => Number.isFinite(x) && Number.isFinite(y)));
    }
  });

  await t.test("#14 Paritaet: Wrapper und kanonischer Adapter liefern gleiche Konstruktionswerte (HlB/BrT/VL/HueT)", () => {
    const measurements23 = { ...fullMeasurements, waist_to_hip: 23 };
    const canonical = bridalValuesToBodiceInput(measurements23, validConfig);
    const wrapper = bridalValuesToDressMeasurements(measurements23);
    assert.equal(canonical.ok, true);
    assert.equal(canonical.input.halslochbreiteCm, wrapper.measurements.halslochbreiteCm);
    assert.equal(canonical.input.brusttiefeCm, wrapper.measurements.brusttiefeCm);
    assert.equal(canonical.input.vorderlaengeCm, wrapper.measurements.vorderlaengeCm);
    assert.equal(canonical.input.huefttiefeCm, wrapper.measurements.huefttiefeCm);
    assert.equal(wrapper.measurements.huefttiefeCm, 23);
  });
});
