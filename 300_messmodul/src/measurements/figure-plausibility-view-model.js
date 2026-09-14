const DEVIATING_STATUSES = new Set(["off-norm", "unsicher"]);

export function coerceMeasurementValues(stringMap = {}) {
  const entries = [];

  for (const [measurementId, rawValue] of Object.entries(stringMap)) {
    const normalizedValue = typeof rawValue === "string"
      ? rawValue.trim().replace(/,/g, ".")
      : rawValue;
    if (normalizedValue === "") continue;

    const numericValue = Number(normalizedValue);
    if (!Number.isFinite(numericValue) || numericValue <= 0) continue;
    entries.push([measurementId, numericValue]);
  }

  return Object.fromEntries(entries);
}

export function deriveFigureDisplayState(assessment = {}) {
  const checks = Array.isArray(assessment.checks) ? assessment.checks : [];
  const flaggedChecks = checks.filter(({ status }) => DEVIATING_STATUSES.has(status));
  const isIdeal = checks.length > 0 && checks.every(({ status }) => status === "ok");
  const state = flaggedChecks.length > 0
    ? "deviates"
    : isIdeal
      ? "ideal"
      : "incomplete";
  const missingMeasurementIds = [...new Set(checks.flatMap((check) => (
    Array.isArray(check.missingMeasurementIds) ? check.missingMeasurementIds : []
  )))];

  return {
    state,
    flaggedChecks,
    missingMeasurementIds,
    requiredExtraMeasurements: Array.isArray(assessment.requiredExtraMeasurements)
      ? assessment.requiredExtraMeasurements
      : [],
    advisories: Array.isArray(assessment.advisories) ? assessment.advisories : []
  };
}
