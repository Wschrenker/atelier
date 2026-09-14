import assert from "node:assert/strict";
import test from "node:test";
import {
  BRIDAL_BODY_MEASUREMENTS,
  MEASUREMENT_VIEWS,
  createBridalMeasurementProfile,
  getBodyMeasurement,
  validateMeasurementValue
} from "../src/measurements/bridal-body-measurements.js";

test("bridal body measurement ids are unique even when book abbreviations repeat", () => {
  const ids = BRIDAL_BODY_MEASUREMENTS.map(({ id }) => id);
  assert.equal(ids.length, 46);
  assert.equal(new Set(ids).size, ids.length);
  assert.equal(getBodyMeasurement("measured_bust_depth_right").abbreviation, "gBrT");
  assert.equal(getBodyMeasurement("measured_bust_depth_left").abbreviation, "gBrT");
  assert.notEqual(getBodyMeasurement("measured_bust_depth_right").id, getBodyMeasurement("measured_bust_depth_left").id);
});

test("HaU remains unique to the neck base while hand circumference uses HdU", () => {
  assert.equal(getBodyMeasurement("neck_base_circumference").abbreviation, "HaU");
  assert.equal(getBodyMeasurement("hand_circumference_right").abbreviation, "HdU");
  assert.equal(getBodyMeasurement("hand_circumference_left").abbreviation, "HdU");
  assert.equal(BRIDAL_BODY_MEASUREMENTS.filter(({ abbreviation }) => abbreviation === "HaU").length, 1);
  assert.match(getBodyMeasurement("hand_circumference_right").instruction, /Im Buch \(S\.15\) mit HaU bezeichnet/);
});

test("hip depth is a real below-waist body measurement with its honest source override", () => {
  const hipDepth = getBodyMeasurement("waist_to_hip");
  assert.equal(hipDepth.position, 8);
  assert.equal(hipDepth.group, "below_waist");
  assert.equal(hipDepth.abbreviation, "HüT");
  assert.equal(hipDepth.unit, "cm");
  assert.equal(hipDepth.source.page, "20–31");
  assert.match(hipDepth.source.reference, /Werner-Entscheid 2026-07-11/);
  assert.match(hipDepth.source.transcript, /s20-31_groessen-und-konstruktionsstandards_rohtranskription\.md$/);
  assert.equal(BRIDAL_BODY_MEASUREMENTS.indexOf(hipDepth), BRIDAL_BODY_MEASUREMENTS.findIndex(({ id }) => id === "waist_height_side_left") + 1);
});

test("all numbered source positions 1 through 28 are represented with page references", () => {
  assert.deepEqual(
    [...new Set(BRIDAL_BODY_MEASUREMENTS.map(({ position }) => position))],
    Array.from({ length: 28 }, (_, index) => index + 1)
  );
  for (const measurement of BRIDAL_BODY_MEASUREMENTS.filter(({ id }) => id !== "waist_to_hip")) {
    assert.ok(measurement.instruction.length > 40, measurement.id);
    assert.ok([12, 13, 14, 15].includes(measurement.source.page), measurement.id);
    assert.match(measurement.source.reference, /Hofenbitzer, Band 1, S\. (12|13|14|15)/);
    assert.match(measurement.source.transcript, /s11-15_rohtranskription\.md#s(12|13|14|15)$/);
  }
});

test("front, side and back views have measurement guides", () => {
  const coveredViews = new Set();
  for (const measurement of BRIDAL_BODY_MEASUREMENTS) {
    assert.ok(measurement.views.length > 0, measurement.id);
    for (const view of measurement.views) {
      assert.ok(MEASUREMENT_VIEWS.includes(view), `${measurement.id}: ${view}`);
      coveredViews.add(view);
    }
    assert.deepEqual(measurement.views, [...new Set(measurement.guides.map(({ view }) => view))]);
  }
  assert.deepEqual([...coveredViews].sort(), [...MEASUREMENT_VIEWS].sort());
});

test("directional and bilateral partial measurements remain separate", () => {
  const expectedIds = [
    "waistband_distance_front_center",
    "waistband_distance_side_right",
    "waistband_distance_side_left",
    "waistband_distance_back_center",
    "waist_height_front_center",
    "waist_height_back_center",
    "waist_height_side_right",
    "waist_height_side_left",
    "measured_arm_diameter_right",
    "measured_arm_diameter_left",
    "shoulder_width_right",
    "shoulder_width_left",
    "shoulder_angle_right",
    "shoulder_angle_left"
  ];
  for (const id of expectedIds) assert.ok(getBodyMeasurement(id), id);
  assert.equal(getBodyMeasurement("waistband_distance_side_right").abbreviation, "sBuA");
  assert.equal(getBodyMeasurement("waistband_distance_side_left").abbreviation, "sBuA");
});

test("measurement values accept only finite positive numbers", () => {
  assert.equal(validateMeasurementValue(12.5), 12.5);
  assert.equal(validateMeasurementValue("12.5"), 12.5);
  for (const invalid of [0, -1, Number.NaN, Number.POSITIVE_INFINITY, "", "   ", "nichts"]) {
    assert.throws(() => validateMeasurementValue(invalid), /endliche positive Zahl/);
  }
});

test("measurement profile carries shape id, collision-safe ids, values and units", () => {
  const profile = createBridalMeasurementProfile({
    shapeId: "mermaid",
    values: {
      measured_bust_depth_right: "31.2",
      measured_bust_depth_left: 30.8,
      shoulder_angle_left: 19
    }
  });
  assert.deepEqual(profile, {
    shapeId: "mermaid",
    measurements: [
      { id: "measured_bust_depth_right", abbreviation: "gBrT", value: 31.2, unit: "cm" },
      { id: "measured_bust_depth_left", abbreviation: "gBrT", value: 30.8, unit: "cm" },
      { id: "shoulder_angle_left", abbreviation: "SuWi", value: 19, unit: "deg" }
    ]
  });
  assert.throws(() => createBridalMeasurementProfile({ shapeId: "unknown", values: {} }), /Unbekannte Grundform/);
  assert.throws(() => createBridalMeasurementProfile({ shapeId: "a_line", values: { imaginary: 1 } }), /Unbekannte Maß-ID/);
  assert.throws(() => createBridalMeasurementProfile({ shapeId: "a_line", values: { body_height: -1 } }), /endliche positive Zahl/);
});

test("measurement profile carries the measured hip depth without a default", () => {
  const profile = createBridalMeasurementProfile({ shapeId: "a_line", values: { waist_to_hip: "23.5" } });
  assert.deepEqual(profile.measurements, [
    { id: "waist_to_hip", abbreviation: "HüT", value: 23.5, unit: "cm" }
  ]);
  assert.deepEqual(createBridalMeasurementProfile({ shapeId: "a_line", values: {} }).measurements, []);
});

test("centimetres are used for all linear measures; source-defined shoulder angle stays degrees", () => {
  for (const measurement of BRIDAL_BODY_MEASUREMENTS) {
    const expectedUnit = measurement.position === 28 ? "deg" : "cm";
    assert.equal(measurement.unit, expectedUnit, measurement.id);
  }
});
