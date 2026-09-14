import { deriveWidthControls } from "../dress/bridal-measurement-bodice-adapter.js";

const SOURCE_REFS = Object.freeze({
  constructibleBust: "src/drafting/bodice-block.js:32-34; Hofenbitzer Band 1, S.19 Balance-Tabelle 80-150",
  idealHipWaistWindow: "hofenbitzer/band_1/transkription/eingang_claude/s11-15_rohtranskription.md:39",
  directMeasurements: "hofenbitzer/band_1/transkription/eingang_claude/s11-15_rohtranskription.md:301-303",
  balanceWindow: "hofenbitzer/band_1/transkription/eingang_codex/s7-8_10_16-19_einfuehrung_massnehmen_codex_transkription.md:323-343,428-431,466-483",
  breastWidthControl: "hofenbitzer/band_1/transkription/eingang_claude/s11-15_rohtranskription.md:269-293; hofenbitzer/band_1/transkription/eingang_codex/s7-8_10_16-19_einfuehrung_massnehmen_codex_transkription.md:436",
  derivedWidthControl: "hofenbitzer/band_1/transkription/eingang_claude/s11-15_rohtranskription.md:268-281 (S.14 roter Kasten: Alternative Bestimmung von RueB, ArD und BrB)",
  armholeDepthControl: "hofenbitzer/band_1/transkription/eingang_claude/s11-15_rohtranskription.md:254-257; hofenbitzer/band_1/transkription/eingang_codex/s7-8_10_16-19_einfuehrung_massnehmen_codex_transkription.md:432"
});

const EXTRA_MEASUREMENTS = Object.freeze([
  Object.freeze({
    measurementId: "measured_back_width",
    abbreviation: "gRüB",
    reason: "Off-norm/unsichere Figur: Rückenbreite direkt nach S.14 erfassen.",
    bookRef: "❑6, S.14"
  }),
  Object.freeze({
    measurementId: "measured_arm_diameter_right",
    abbreviation: "gArD",
    reason: "Off-norm/unsichere Figur: Armdurchmesser rechts direkt nach S.14 erfassen.",
    bookRef: "❑6, S.14"
  }),
  Object.freeze({
    measurementId: "measured_arm_diameter_left",
    abbreviation: "gArD",
    reason: "Off-norm/unsichere Figur: Armdurchmesser links direkt nach S.14 erfassen.",
    bookRef: "❑6, S.14"
  }),
  Object.freeze({
    measurementId: "measured_bust_width",
    abbreviation: "gBrB",
    reason: "Off-norm/unsichere Figur: Brustbreite direkt nach S.14 erfassen.",
    bookRef: "❑7, S.14"
  })
]);

const SHAPE_CHECK_IDS = Object.freeze([
  "constructible-bust-range",
  "ideal-hip-waist-window"
]);

const ADVISORY_TEMPLATES = Object.freeze({
  balance: Object.freeze({
    id: "balance-figure-observation",
    kind: "observe-figure",
    reason: "Balance-Problem > 1 cm: Taillenband-Lage prüfen, gVL/gRüL nachmessen, Figurbeobachtung.",
    bookRef: "S.17–18"
  }),
  breastWidth: Object.freeze({
    id: "breast-width-remeasure",
    kind: "remeasure",
    measurementId: "measured_bust_width",
    reason: "gBrB exakt waagerecht nachmessen.",
    bookRef: "❑7, S.14"
  }),
  armholeDepth: Object.freeze({
    id: "armhole-depth-correct-toward-control",
    kind: "correct-toward-control",
    measurementId: "armhole_depth",
    reason: "gAlT Richtung Kontrollwert anpassen.",
    bookRef: "S.14/S.19"
  }),
  useDerivedWidths: Object.freeze({
    id: "width-derivation-strategy",
    kind: "use-derived-widths",
    reason: "Direkte Breitenkontrolle geht nicht auf; quellenbelegte Alternativableitung als Konstruktionsstrategie verwenden (ArD = OaU × 0,6 − 7,5; BrB = BrU ÷ 2 − RüB − ArD). Rohmessung nicht überschreiben.",
    bookRef: "S.14 (roter Kasten)"
  })
});

const DIRECT_BREAST_WIDTH_TOLERANCE_CM = Object.freeze({ min: -1, max: 4 });
const ARMHOLE_DEPTH_TOLERANCE_CM = 1;
const BALANCE_TOLERANCE_CM = 1;

function finiteValue(values, id) {
  return Number.isFinite(values?.[id]) ? values[id] : undefined;
}

function missingIds(values, ids) {
  return ids.filter((id) => finiteValue(values, id) === undefined);
}

function freezeCheck(check) {
  if (Array.isArray(check.missingMeasurementIds)) Object.freeze(check.missingMeasurementIds);
  if (check.computed && typeof check.computed === "object") Object.freeze(check.computed);
  if (check.expected && typeof check.expected === "object") Object.freeze(check.expected);
  return Object.freeze(check);
}

function unbestimmbarCheck({ id, label, expected, sourceRef, missingMeasurementIds }) {
  return freezeCheck({
    id,
    label,
    status: "unbestimmbar",
    computed: null,
    expected,
    sourceRef,
    missingMeasurementIds: Object.freeze(missingMeasurementIds)
  });
}

function constructibleBustCheck(values) {
  const bust = finiteValue(values, "bust_circumference");
  if (bust === undefined) {
    return unbestimmbarCheck({
      id: "constructible-bust-range",
      label: "BrU-Konstruierbarkeit",
      expected: "80 <= BrU <= 150 cm",
      sourceRef: SOURCE_REFS.constructibleBust,
      missingMeasurementIds: ["bust_circumference"]
    });
  }

  // Hofenbitzer-Balance-Tabelle und Engine-Grenze sind inklusiv: 80 <= BrU <= 150.
  return freezeCheck({
    id: "constructible-bust-range",
    label: "BrU-Konstruierbarkeit",
    status: bust >= 80 && bust <= 150 ? "ok" : "unsicher",
    computed: Object.freeze({ bustCircumferenceCm: bust }),
    expected: "80 <= BrU <= 150 cm",
    sourceRef: SOURCE_REFS.constructibleBust
  });
}

function idealHipWaistCheck(values) {
  const missingMeasurementIds = missingIds(values, [
    "hip_circumference_horizontal",
    "waist_circumference_horizontal"
  ]);

  if (missingMeasurementIds.length > 0) {
    return unbestimmbarCheck({
      id: "ideal-hip-waist-window",
      label: "Idealfigur-Fenster HüU-TaU",
      expected: "25 <= HüU - TaU <= 32 cm",
      sourceRef: SOURCE_REFS.idealHipWaistWindow,
      missingMeasurementIds
    });
  }

  const difference = finiteValue(values, "hip_circumference_horizontal")
    - finiteValue(values, "waist_circumference_horizontal");
  // S.11 nennt die Normalfigur-Grenze inklusiv: 25 <= HüU - TaU <= 32.
  return freezeCheck({
    id: "ideal-hip-waist-window",
    label: "Idealfigur-Fenster HüU-TaU",
    status: difference >= 25 && difference <= 32 ? "ok" : "off-norm",
    computed: Object.freeze({ hipMinusWaistCm: difference }),
    expected: "25 <= HüU - TaU <= 32 cm",
    sourceRef: SOURCE_REFS.idealHipWaistWindow
  });
}

function optimalBalanceCm(bustCircumferenceCm) {
  if (bustCircumferenceCm < 80 || bustCircumferenceCm > 150) return undefined;
  if (bustCircumferenceCm < 90) return 3.5;
  if (bustCircumferenceCm < 100) return 4;
  if (bustCircumferenceCm < 110) return (bustCircumferenceCm - 100) / 10 + 4.5;
  if (bustCircumferenceCm < 120) return (bustCircumferenceCm - 100) / 10 + 5;
  if (bustCircumferenceCm < 130) return (bustCircumferenceCm - 100) / 10 + 5.5;
  return (bustCircumferenceCm - 100) / 10 + 6;
}

function balanceWindowCheck(values) {
  const requiredIds = [
    "measured_front_length_right",
    "measured_front_length_left",
    "measured_back_length",
    "neck_base_circumference",
    "bust_circumference"
  ];
  const missingMeasurementIds = missingIds(values, requiredIds);

  if (missingMeasurementIds.length > 0) {
    return unbestimmbarCheck({
      id: "balance-window",
      label: "Balance VL-RüL",
      expected: "|individuelle Balance - optimale Balance| <= 1 cm",
      sourceRef: SOURCE_REFS.balanceWindow,
      missingMeasurementIds
    });
  }

  const bust = finiteValue(values, "bust_circumference");
  const optimalBalance = optimalBalanceCm(bust);
  if (optimalBalance === undefined) {
    return freezeCheck({
      id: "balance-window",
      label: "Balance VL-RüL",
      status: "unbestimmbar",
      computed: Object.freeze({ bustCircumferenceCm: bust }),
      expected: "|individuelle Balance - optimale Balance| <= 1 cm; 80 <= BrU <= 150 cm",
      sourceRef: SOURCE_REFS.balanceWindow
    });
  }

  // S.19: HlB = HaU : 6 + 0,5. HaU ist der Halsansatzumfang, nicht Handumfang.
  const neckHoleWidth = finiteValue(values, "neck_base_circumference") / 6 + 0.5;
  const measuredFrontLength = (
    finiteValue(values, "measured_front_length_right")
    + finiteValue(values, "measured_front_length_left")
  ) / 2;
  // Caveat S.17: Taillenschräglage muss ggf. manuell beobachtet/korrigiert werden.
  const frontLength = measuredFrontLength - neckHoleWidth;
  const backLength = finiteValue(values, "measured_back_length");
  const individualBalance = frontLength - backLength;
  const deviation = Math.abs(individualBalance - optimalBalance);

  return freezeCheck({
    id: "balance-window",
    label: "Balance VL-RüL",
    status: deviation <= BALANCE_TOLERANCE_CM ? "ok" : "off-norm",
    computed: Object.freeze({
      neckHoleWidthCm: neckHoleWidth,
      measuredFrontLengthAverageCm: measuredFrontLength,
      frontLengthCm: frontLength,
      backLengthCm: backLength,
      individualBalanceCm: individualBalance,
      optimalBalanceCm: optimalBalance,
      deviationCm: deviation
    }),
    expected: Object.freeze({ maxDeviationCm: BALANCE_TOLERANCE_CM }),
    sourceRef: SOURCE_REFS.balanceWindow
  });
}

function breastWidthControlCheck(values) {
  const requiredIds = [
    "measured_back_width",
    "measured_arm_diameter_right",
    "measured_arm_diameter_left",
    "measured_bust_width",
    "bust_circumference"
  ];
  const missingMeasurementIds = missingIds(values, requiredIds);

  if (missingMeasurementIds.length > 0) {
    return unbestimmbarCheck({
      id: "breast-width-control",
      label: "Brustweitenkontrolle Direktmaße",
      expected: "-1 <= 2 * (RüB + ArD + BrB) - BrU <= 4 cm",
      sourceRef: SOURCE_REFS.breastWidthControl,
      missingMeasurementIds
    });
  }

  // S.14/S.19, nur mit Direktmaßen: mit BrB-Formel wäre die Kontrolle tautologisch.
  const backWidth = finiteValue(values, "measured_back_width") / 2;
  const armDiameter = (
    finiteValue(values, "measured_arm_diameter_right")
    + finiteValue(values, "measured_arm_diameter_left")
  ) / 2;
  const bustWidth = finiteValue(values, "measured_bust_width") / 2;
  const directHalfBustSum = backWidth + armDiameter + bustWidth;
  const deltaTotal = 2 * directHalfBustSum - finiteValue(values, "bust_circumference");

  return freezeCheck({
    id: "breast-width-control",
    label: "Brustweitenkontrolle Direktmaße",
    status: deltaTotal >= DIRECT_BREAST_WIDTH_TOLERANCE_CM.min
      && deltaTotal <= DIRECT_BREAST_WIDTH_TOLERANCE_CM.max
      ? "ok"
      : "off-norm",
    computed: Object.freeze({
      backWidthCm: backWidth,
      armDiameterCm: armDiameter,
      bustWidthCm: bustWidth,
      directHalfBustSumCm: directHalfBustSum,
      reconstructedBustCircumferenceCm: 2 * directHalfBustSum,
      deltaTotalCm: deltaTotal
    }),
    expected: DIRECT_BREAST_WIDTH_TOLERANCE_CM,
    sourceRef: SOURCE_REFS.breastWidthControl
  });
}

// S.14 roter Kasten: quellenbasierte Alternativableitung als zweite Kontrolle.
// ArD = OaU * 0,6 - 7,5; BrB = BrU/2 - RueB - ArD. Die Summe geht per Konstruktion
// auf BrU/2 auf — die Kontrolle prueft daher die PLAUSIBILITAET der Ableitung
// (ArD/BrB positiv) und weist die Abweichungen zu den Direktmessungen aus.
function derivedWidthControlCheck(values) {
  const requiredIds = ["measured_back_width", "bust_circumference"];
  const missingMeasurementIds = missingIds(values, requiredIds);
  const hasOaU = Number.isFinite(values?.upper_arm_circumference_right)
    || Number.isFinite(values?.upper_arm_circumference_left);
  if (!hasOaU) {
    missingMeasurementIds.push("upper_arm_circumference_right or upper_arm_circumference_left");
  }

  if (missingMeasurementIds.length > 0) {
    return unbestimmbarCheck({
      id: "breast-width-derived-control",
      label: "Brustweitenkontrolle Quellenformel (S.14 Alternative)",
      expected: "RüB + ArD(OaU) + BrB = ½ BrU; ArD > 0 und BrB > 0",
      sourceRef: SOURCE_REFS.derivedWidthControl,
      missingMeasurementIds
    });
  }

  const derived = deriveWidthControls(values).quellenformel;
  const plausible = derived.armdurchmesserCm > 0 && derived.brustbreiteHalbCm > 0;

  return freezeCheck({
    id: "breast-width-derived-control",
    label: "Brustweitenkontrolle Quellenformel (S.14 Alternative)",
    status: plausible ? "ok" : "off-norm",
    computed: Object.freeze({
      oaUMittelCm: derived.oaUMittelCm,
      armdurchmesserCm: derived.armdurchmesserCm,
      rueckenbreiteHalbCm: derived.rueckenbreiteHalbCm,
      brustbreiteHalbCm: derived.brustbreiteHalbCm,
      kontrolleSummeCm: derived.kontrolleSummeCm,
      halberBrUCm: derived.halberBrUCm,
      abweichungGArDCm: derived.abweichungGArDCm ?? null,
      abweichungGBrBCm: derived.abweichungGBrBCm ?? null
    }),
    expected: "RüB + ArD(OaU) + BrB = ½ BrU; ArD > 0 und BrB > 0",
    sourceRef: SOURCE_REFS.derivedWidthControl
  });
}

function armholeDepthControlCheck(values) {
  const requiredIds = ["body_height", "bust_circumference", "armhole_depth"];
  const missingMeasurementIds = missingIds(values, requiredIds);

  if (missingMeasurementIds.length > 0) {
    return unbestimmbarCheck({
      id: "armhole-depth-control",
      label: "AlT-Kontrolle",
      expected: "|gAlT - ((KöH + BrU) / 10 - 6)| <= 1 cm",
      sourceRef: SOURCE_REFS.armholeDepthControl,
      missingMeasurementIds
    });
  }

  // S.19 Kontrollmaß: AlT = (KöH + BrU) : 10 - 6 cm; Schwelle SSOT #20.
  const control = (finiteValue(values, "body_height") + finiteValue(values, "bust_circumference")) / 10 - 6;
  const measured = finiteValue(values, "armhole_depth");
  const deviation = Math.abs(measured - control);

  return freezeCheck({
    id: "armhole-depth-control",
    label: "AlT-Kontrolle",
    status: deviation <= ARMHOLE_DEPTH_TOLERANCE_CM ? "ok" : "off-norm",
    computed: Object.freeze({
      measuredArmholeDepthCm: measured,
      controlArmholeDepthCm: control,
      deviationCm: deviation
    }),
    expected: Object.freeze({ maxDeviationCm: ARMHOLE_DEPTH_TOLERANCE_CM }),
    sourceRef: SOURCE_REFS.armholeDepthControl
  });
}

function requiredExtraMeasurements(values, checks) {
  const needsBypass = checks.some(({ id, status }) => (
    SHAPE_CHECK_IDS.includes(id) && (status === "off-norm" || status === "unsicher")
  ));
  if (!needsBypass) return Object.freeze([]);
  return Object.freeze(EXTRA_MEASUREMENTS
    .filter(({ measurementId }) => !Number.isFinite(values?.[measurementId]))
    .map((measurement) => Object.freeze({ ...measurement })));
}

function advisoriesForChecks(checks) {
  const advisories = [];
  if (checks.find(({ id, status }) => id === "balance-window" && status === "off-norm")) {
    advisories.push(Object.freeze({ ...ADVISORY_TEMPLATES.balance }));
  }
  if (checks.find(({ id, status }) => id === "breast-width-control" && status === "off-norm")) {
    advisories.push(Object.freeze({ ...ADVISORY_TEMPLATES.breastWidth }));
    // Strategie-Hinweis: Wenn die quellenbasierte Alternativableitung plausibel
    // vorliegt, ist sie die belegte Konstruktionsstrategie (S.14 roter Kasten).
    if (checks.find(({ id, status }) => id === "breast-width-derived-control" && status === "ok")) {
      advisories.push(Object.freeze({ ...ADVISORY_TEMPLATES.useDerivedWidths }));
    }
  }
  if (checks.find(({ id, status }) => id === "armhole-depth-control" && status === "off-norm")) {
    advisories.push(Object.freeze({ ...ADVISORY_TEMPLATES.armholeDepth }));
  }
  return Object.freeze(advisories);
}

export function assessFigurePlausibility({ values = {} } = {}) {
  const checks = Object.freeze([
    constructibleBustCheck(values),
    idealHipWaistCheck(values),
    balanceWindowCheck(values),
    breastWidthControlCheck(values),
    derivedWidthControlCheck(values),
    armholeDepthControlCheck(values)
  ]);

  return Object.freeze({
    checks,
    isIdealFigure: checks.every(({ status }) => status === "ok"),
    requiredExtraMeasurements: requiredExtraMeasurements(values, checks),
    advisories: advisoriesForChecks(checks)
  });
}
