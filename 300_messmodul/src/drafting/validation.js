const POSITIVE_FIELDS = Object.freeze([
  "waistCm",
  "hipCm",
  "waistToHipCm",
  "lengthCm",
  "frontDartLengthCm",
  "backDartLength1Cm",
  "backDartLength2Cm"
]);

const NON_NEGATIVE_FIELDS = Object.freeze([
  "waistEaseCm",
  "hipEaseCm",
  "sideSeamUpliftCm",
  "frontDartIntakeCm",
  "frontDartUpliftCm",
  "backDartUpliftCm",
  "secondBackDartUpliftCm",
  "backDartDifferenceCm",
  "backDartPositionOffsetCm",
  "seamAllowanceCm",
  "hemAllowanceCm",
  "centerBackAllowanceCm"
]);

const FINITE_FIELDS = Object.freeze(["sideHipShapeAdjustmentCm"]);

function requireFinite(name, value) {
  if (!Number.isFinite(value)) throw new Error(`${name} must be a finite number`);
}

export function parseOptionalNumber(input, key, fallback) {
  const raw = input?.[key];
  if (raw === undefined || raw === null || raw === "") return fallback;
  const value = Number(raw);
  requireFinite(key, value);
  return value;
}

function validateRange(name, value, rule) {
  if (!rule || (rule.allowZero && value === 0)) return;
  if (value < rule.min || value > rule.max) {
    throw new Error(`${name} must be between ${rule.min} and ${rule.max} cm`);
  }
}

export function validateStraightSkirtInput(input, validationRules = {}) {
  for (const name of POSITIVE_FIELDS) {
    const value = input[name];
    requireFinite(name, value);
    if (value <= 0) throw new Error(`${name} must be a positive number`);
  }

  for (const name of NON_NEGATIVE_FIELDS) {
    const value = input[name];
    requireFinite(name, value);
    if (value < 0) throw new Error(`${name} must be zero or a positive number`);
  }

  for (const name of FINITE_FIELDS) requireFinite(name, input[name]);

  for (const [name, rule] of Object.entries(validationRules)) {
    validateRange(name, input[name], rule);
  }

  if (input.hipCm <= input.waistCm) {
    throw new Error("hipCm must be larger than waistCm for this first skirt block");
  }
  if (input.lengthCm <= input.waistToHipCm) {
    throw new Error("lengthCm must be larger than waistToHipCm");
  }

  return input;
}
