const RAW_MEASUREMENT_META = Object.freeze({
  measured_back_width: Object.freeze({ target: "RüB", label: "Rückenbreite", expr: "gRüB ÷ 2", sourceRef: "S.14" }),
  measured_bust_width: Object.freeze({ target: "BrB", label: "Brustbreite", expr: "gBrB ÷ 2", sourceRef: "S.14" }),
  measured_arm_diameter_right: Object.freeze({ target: "ArD", label: "Armdurchmesser", expr: "(gArD r + gArD l) ÷ 2", sourceRef: "S.14" }),
  measured_arm_diameter_left: Object.freeze({ target: "ArD", label: "Armdurchmesser", expr: "(gArD r + gArD l) ÷ 2", sourceRef: "S.14" }),
  measured_back_length: Object.freeze({ target: "RüL", label: "Rückenlänge", expr: null, sourceRef: "S.13" }),
  measured_bust_depth_right: Object.freeze({ target: "BrT", label: "Brusttiefe", expr: null, sourceRef: "S.13" }),
  measured_bust_depth_left: Object.freeze({ target: "BrT", label: "Brusttiefe", expr: null, sourceRef: "S.13" }),
  measured_front_length_right: Object.freeze({ target: "VL", label: "Vorderlänge", expr: null, sourceRef: "S.13" }),
  measured_front_length_left: Object.freeze({ target: "VL", label: "Vorderlänge", expr: null, sourceRef: "S.13" })
});

export const RAW_MEASUREMENT_IDS = Object.freeze(Object.keys(RAW_MEASUREMENT_META));

export function deriveConstructionValue(measurementId, values = {}) {
  const meta = RAW_MEASUREMENT_META[measurementId];
  if (!meta) return null;

  let value = null;
  if (measurementId === "measured_back_width" && Number.isFinite(values.measured_back_width)) {
    value = values.measured_back_width / 2;
  } else if (measurementId === "measured_bust_width" && Number.isFinite(values.measured_bust_width)) {
    value = values.measured_bust_width / 2;
  } else if (measurementId === "measured_arm_diameter_right" || measurementId === "measured_arm_diameter_left") {
    const right = values.measured_arm_diameter_right;
    const left = values.measured_arm_diameter_left;
    if (Number.isFinite(right) && Number.isFinite(left)) value = (right + left) / 2;
  }

  return Object.freeze({ ...meta, value });
}
