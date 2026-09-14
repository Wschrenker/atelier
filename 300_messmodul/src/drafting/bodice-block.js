import { offsetPolygon, point, sampleQuadratic } from "../geometry.js";
import {
  HOFENBITZER_BAND1_BODICE_METHOD,
  HOFENBITZER_BODICE_RULE_REFS,
  HOFENBITZER_BODICE_SOURCE_REFS
} from "../methods/hofenbitzer-band1-bodice.js";
import { derivationEntry } from "./derivation-trace.js";

const METHOD = HOFENBITZER_BAND1_BODICE_METHOD;
const EPSILON = 1e-6;
const cmToMm = (value) => value * 10;
// Design-Abweichung 18.07. (Werner + Munkhuu): vorderer Halsausschnitt 4 cm tiefer in der
// Mitte, bewusst im geteilten Grundschnitt -> gilt fuer ALLE fuenf Kleider (Abweichung vom
// Buch-Grundschnitt, keine Modellierung).
const FRONT_NECK_DROP_MM = 40;

function samePoint(left, right) {
  return left.x === right.x && left.y === right.y;
}

function midpoint(left, right) {
  return point((left.x + right.x) / 2, (left.y + right.y) / 2);
}

function horizontalIntersection(from, to, y) {
  const height = to.y - from.y;
  if (Math.abs(height) <= EPSILON) throw new Error("line must cross the requested horizontal level");
  const ratio = (y - from.y) / height;
  return point(from.x + (to.x - from.x) * ratio, y);
}

function lineYAtX(from, angleRadians, x) {
  return from.y + Math.tan(angleRadians) * (x - from.x);
}

// Exportiert seit Etappe 3 (2026-07-13): Balance-Gate im Braut-Adapter nutzt
// dieselbe S.174/178-Tabelle — keine zweite Formelquelle.
export function optimalBalanceCm(breastCircumferenceCm) {
  if (breastCircumferenceCm < 80 || breastCircumferenceCm > 150) {
    throw new Error("brustUmfangCm must be between 80 and 150 for the Hofenbitzer balance table");
  }
  if (breastCircumferenceCm < 90) return 3.5;
  if (breastCircumferenceCm < 100) return 4;
  if (breastCircumferenceCm < 110) return (breastCircumferenceCm - 100) / 10 + 4.5;
  if (breastCircumferenceCm < 120) return (breastCircumferenceCm - 100) / 10 + 5;
  if (breastCircumferenceCm < 130) return (breastCircumferenceCm - 100) / 10 + 5.5;
  return (breastCircumferenceCm - 100) / 10 + 6;
}

function trace({ outputId, value, dependsOn, ruleRef, sourceRef }) {
  return derivationEntry({
    outputId,
    value,
    unit: "mm",
    dependsOn,
    ruleRef,
    sourceRefs: [sourceRef]
  });
}

function outlineFromSections(sections) {
  const seamLine = [];
  const edgeAllowances = [];

  for (const section of sections) {
    if (!Array.isArray(section.points) || section.points.length < 2) {
      throw new Error("outline section must contain at least two points");
    }
    if (seamLine.length === 0) seamLine.push(section.points[0]);
    if (!samePoint(seamLine.at(-1), section.points[0])) {
      throw new Error("outline sections must connect without gaps");
    }
    for (let index = 1; index < section.points.length; index += 1) {
      seamLine.push(section.points[index]);
      edgeAllowances.push(section.allowance);
    }
  }

  if (!samePoint(seamLine[0], seamLine.at(-1))) {
    throw new Error("outline sections must form a closed polygon");
  }

  return {
    seamLine,
    cuttingLine: offsetPolygon(seamLine.slice(0, -1), edgeAllowances)
  };
}

function line(type, from, to, label) {
  return {
    type,
    ...(label ? { label } : {}),
    points: [point(from.x, from.y), point(to.x, to.y)]
  };
}

export function applyBodiceMethodDefaults(input = {}) {
  return {
    ...METHOD.inputDefaults,
    ...input,
    allowancesMm: {
      ...METHOD.allowancesMm,
      ...(input.allowancesMm ?? {})
    }
  };
}

export function validateBodiceInput(input) {
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    throw new TypeError("bodice input must be an object");
  }

  for (const key of METHOD.validationRules.requiredMeasurements) {
    if (!Number.isFinite(input[key]) || input[key] <= 0) {
      throw new TypeError(`${key} must be finite and positive`);
    }
  }

  for (const key of METHOD.validationRules.positiveParameters) {
    if (!Number.isFinite(input[key]) || input[key] <= 0) {
      throw new TypeError(`${key} must be finite and positive`);
    }
  }

  if (!Number.isFinite(input.hintereMitteVersatzCm) || input.hintereMitteVersatzCm < 0) {
    throw new TypeError("hintereMitteVersatzCm must be finite and non-negative");
  }

  const angleRule = METHOD.validationRules.shoulderAngle;
  if (input.schulterwinkelGrad <= angleRule.minExclusive
      || input.schulterwinkelGrad >= angleRule.maxExclusive) {
    throw new RangeError("schulterwinkelGrad is outside the constructible range");
  }

  const easeRule = METHOD.validationRules.backShoulderEase;
  if (input.hintereSchulterEinhalteweiteCm < easeRule.min
      || input.hintereSchulterEinhalteweiteCm > easeRule.max) {
    throw new RangeError("hintereSchulterEinhalteweiteCm must be between 0.5 and 1 cm");
  }

  const gapRule = METHOD.validationRules.sideLineGap;
  if (input.seitenlinienAbstandCm < gapRule.min || input.seitenlinienAbstandCm > gapRule.max) {
    throw new RangeError("seitenlinienAbstandCm must be between 7 and 10 cm");
  }

  if (input.modellLaengeCm <= input.rueckenlaengeCm) {
    throw new RangeError("modellLaengeCm must extend below the waistline");
  }

  for (const key of ["seam", "hem", "centerBack"]) {
    if (!Number.isFinite(input.allowancesMm?.[key]) || input.allowancesMm[key] < 0) {
      throw new TypeError(`allowancesMm.${key} must be finite and non-negative`);
    }
  }

  optimalBalanceCm(input.brustUmfangCm);
  return input;
}

export function normalizeBodiceUnits(input) {
  return {
    input,
    measurementsMm: {
      bodyHeight: cmToMm(input.koeHCm),
      breastCircumference: cmToMm(input.brustUmfangCm),
      waistCircumference: cmToMm(input.taillenUmfangCm),
      hipCircumference: cmToMm(input.hueftUmfangCm),
      armholeDepth: cmToMm(input.armlochtiefeCm),
      hipDepth: cmToMm(input.huefttiefeCm),
      breastDepth: cmToMm(input.brusttiefeCm),
      modelLength: cmToMm(input.modellLaengeCm),
      neckWidth: cmToMm(input.halslochbreiteCm),
      halfBackWidth: cmToMm(input.rueckenbreiteHalbCm),
      armDiameter: cmToMm(input.armdurchmesserCm),
      halfBreastBreadth: cmToMm(input.brustbreiteHalbCm),
      shoulderWidth: cmToMm(input.schulterbreiteCm),
      shoulderAngleDegrees: input.schulterwinkelGrad,
      backLength: cmToMm(input.rueckenlaengeCm),
      frontLength: cmToMm(input.vorderlaengeCm)
    },
    constructionMm: {
      breastEase: cmToMm(input.brustZugabeCm),
      waistEase: cmToMm(input.taillenZugabeCm),
      hipEase: cmToMm(input.hueftZugabeCm),
      armholeDepthEase: cmToMm(input.armlochtiefeZugabeCm),
      backWidthEase: cmToMm(input.rueckenbreiteZugabeCm),
      armDiameterEase: cmToMm(input.armdurchmesserZugabeCm),
      breastBreadthEase: cmToMm(input.brustbreiteZugabeCm),
      shoulderWidthEase: cmToMm(input.schulterbreiteZugabeCm),
      backShoulderEase: cmToMm(input.hintereSchulterEinhalteweiteCm),
      sideLineGap: cmToMm(input.seitenlinienAbstandCm),
      backCenterOffset: cmToMm(input.hintereMitteVersatzCm),
      breastWidthTolerance: cmToMm(input.brustweitenToleranzCm)
    },
    allowancesMm: { ...input.allowancesMm }
  };
}

export function deriveBodiceMeasures(normalized) {
  const { measurementsMm: measurements, constructionMm: construction } = normalized;
  const breastWidth = measurements.breastCircumference + construction.breastEase;
  const halfBreastWidth = breastWidth / 2;
  const waistWidth = measurements.waistCircumference + construction.waistEase;
  const halfWaistWidth = waistWidth / 2;
  const hipWidth = measurements.hipCircumference + construction.hipEase;
  const halfHipWidth = hipWidth / 2;
  const armholeDepthPlus = measurements.armholeDepth + construction.armholeDepthEase;
  const backWidthPlus = measurements.halfBackWidth + construction.backWidthEase;
  const armDiameterPlus = measurements.armDiameter + construction.armDiameterEase;
  const quarterArmDiameterPlus = armDiameterPlus / 4;
  const thirdArmDiameterPlus = armDiameterPlus / 3;
  const twoThirdArmDiameterPlus = armDiameterPlus * 2 / 3;
  const breastBreadthPlus = measurements.halfBreastBreadth + construction.breastBreadthEase;
  const shoulderSeamLength = measurements.shoulderWidth + construction.shoulderWidthEase;
  const backShoulderSeamLength = shoulderSeamLength + construction.backShoulderEase;
  const individualBalance = measurements.frontLength - measurements.backLength;
  const optimalBalance = cmToMm(optimalBalanceCm(normalized.input.brustUmfangCm));
  const balanceDeviation = Math.abs(individualBalance - optimalBalance);
  const backBreastWidth = backWidthPlus + twoThirdArmDiameterPlus;
  const frontBreastWidth = thirdArmDiameterPlus + breastBreadthPlus;
  const breastWidthSum = backBreastWidth + frontBreastWidth;
  const breastWidthDifference = breastWidthSum - halfBreastWidth;

  const derived = {
    breastWidth,
    halfBreastWidth,
    waistWidth,
    halfWaistWidth,
    hipWidth,
    halfHipWidth,
    armholeDepthPlus,
    backWidthPlus,
    armDiameterPlus,
    quarterArmDiameterPlus,
    thirdArmDiameterPlus,
    twoThirdArmDiameterPlus,
    breastBreadthPlus,
    shoulderSeamLength,
    backShoulderSeamLength,
    individualBalance,
    optimalBalance,
    balanceDeviation,
    backBreastWidth,
    frontBreastWidth,
    breastWidthSum,
    breastWidthDifference
  };

  const table = HOFENBITZER_BODICE_SOURCE_REFS.table;
  const widthLines = HOFENBITZER_BODICE_SOURCE_REFS.widthLines;
  const derivationTrace = [
    trace({ outputId: "derived.breastWidth", value: breastWidth, dependsOn: ["measurements.brustUmfangCm", "construction.brustZugabeCm"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.breastWidth, sourceRef: table }),
    trace({ outputId: "derived.halfBreastWidth", value: halfBreastWidth, dependsOn: ["derived.breastWidth"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.breastWidth, sourceRef: table }),
    trace({ outputId: "derived.waistWidth", value: waistWidth, dependsOn: ["measurements.taillenUmfangCm", "construction.taillenZugabeCm"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.waistWidth, sourceRef: table }),
    trace({ outputId: "derived.halfWaistWidth", value: halfWaistWidth, dependsOn: ["derived.waistWidth"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.waistWidth, sourceRef: table }),
    trace({ outputId: "derived.hipWidth", value: hipWidth, dependsOn: ["measurements.hueftUmfangCm", "construction.hueftZugabeCm"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.hipWidth, sourceRef: table }),
    trace({ outputId: "derived.halfHipWidth", value: halfHipWidth, dependsOn: ["derived.hipWidth"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.hipWidth, sourceRef: table }),
    trace({ outputId: "derived.armholeDepthPlus", value: armholeDepthPlus, dependsOn: ["measurements.armlochtiefeCm", "construction.armlochtiefeZugabeCm"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.armholeDepth, sourceRef: table }),
    trace({ outputId: "derived.backWidthPlus", value: backWidthPlus, dependsOn: ["measurements.rueckenbreiteHalbCm", "construction.rueckenbreiteZugabeCm"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.backWidth, sourceRef: table }),
    trace({ outputId: "derived.armDiameterPlus", value: armDiameterPlus, dependsOn: ["measurements.armdurchmesserCm", "construction.armdurchmesserZugabeCm"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.armDiameter, sourceRef: table }),
    trace({ outputId: "derived.quarterArmDiameterPlus", value: quarterArmDiameterPlus, dependsOn: ["derived.armDiameterPlus"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.armDiameter, sourceRef: widthLines }),
    trace({ outputId: "derived.thirdArmDiameterPlus", value: thirdArmDiameterPlus, dependsOn: ["derived.armDiameterPlus"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.armDiameter, sourceRef: widthLines }),
    trace({ outputId: "derived.twoThirdArmDiameterPlus", value: twoThirdArmDiameterPlus, dependsOn: ["derived.armDiameterPlus"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.armDiameter, sourceRef: widthLines }),
    trace({ outputId: "derived.breastBreadthPlus", value: breastBreadthPlus, dependsOn: ["measurements.brustbreiteHalbCm", "construction.brustbreiteZugabeCm"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.breastBreadth, sourceRef: table }),
    trace({ outputId: "derived.shoulderSeamLength", value: shoulderSeamLength, dependsOn: ["measurements.schulterbreiteCm", "construction.schulterbreiteZugabeCm"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.shoulderLength, sourceRef: table }),
    trace({ outputId: "derived.backShoulderSeamLength", value: backShoulderSeamLength, dependsOn: ["derived.shoulderSeamLength", "construction.hintereSchulterEinhalteweiteCm"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.backShoulderLength, sourceRef: table }),
    trace({ outputId: "derived.individualBalance", value: individualBalance, dependsOn: ["measurements.vorderlaengeCm", "measurements.rueckenlaengeCm"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.balance, sourceRef: HOFENBITZER_BODICE_SOURCE_REFS.balance }),
    trace({ outputId: "derived.optimalBalance", value: optimalBalance, dependsOn: ["measurements.brustUmfangCm"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.balance, sourceRef: HOFENBITZER_BODICE_SOURCE_REFS.balance }),
    trace({ outputId: "derived.balanceDeviation", value: balanceDeviation, dependsOn: ["derived.individualBalance", "derived.optimalBalance"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.balance, sourceRef: HOFENBITZER_BODICE_SOURCE_REFS.balance }),
    trace({ outputId: "derived.backBreastWidth", value: backBreastWidth, dependsOn: ["derived.backWidthPlus", "derived.twoThirdArmDiameterPlus"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.breastWidthCheck, sourceRef: widthLines }),
    trace({ outputId: "derived.frontBreastWidth", value: frontBreastWidth, dependsOn: ["derived.thirdArmDiameterPlus", "derived.breastBreadthPlus"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.breastWidthCheck, sourceRef: widthLines }),
    trace({ outputId: "derived.breastWidthSum", value: breastWidthSum, dependsOn: ["derived.frontBreastWidth", "derived.backBreastWidth"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.breastWidthCheck, sourceRef: widthLines }),
    trace({ outputId: "derived.breastWidthDifference", value: breastWidthDifference, dependsOn: ["derived.breastWidthSum", "derived.halfBreastWidth"], ruleRef: HOFENBITZER_BODICE_RULE_REFS.breastWidthCheck, sourceRef: widthLines })
  ];

  return { ...normalized, derived, derivationTrace };
}

export function constructBodiceLandmarks(state) {
  const { measurementsMm: measurements, constructionMm: construction, derived } = state;
  const p1 = point(0, 0);
  const p2 = point(0, measurements.neckWidth / 3 + 10);
  const p3 = point(0, p2.y + measurements.modelLength);
  const p4 = point(0, p2.y + derived.armholeDepthPlus);
  const p5 = point(0, p2.y + measurements.backLength);
  const p6 = point(0, p5.y + measurements.hipDepth);
  const p7 = point(construction.backCenterOffset, p5.y);
  const p8 = point(construction.backCenterOffset, p3.y);
  // Gedruckte Alternative: Eine gerade hM kann von P2 über den 2-cm-Punkt
  // auf der Hüftlinie geführt werden. Etappe 1 baut den Default mit hM-Naht.
  const p9 = horizontalIntersection(p2, p7, p4.y);
  const p10 = point(p9.x + derived.backWidthPlus, p4.y);
  const p11 = point(p10.x + derived.twoThirdArmDiameterPlus, p4.y);
  const p12 = point(p11.x + construction.sideLineGap, p4.y);
  const p13 = point(p12.x + derived.thirdArmDiameterPlus, p4.y);
  const p14 = point(p13.x + derived.breastBreadthPlus, p4.y);

  const backHlp = point(p1.x + measurements.neckWidth + 5, p1.y);
  const backShoulderAngle = (measurements.shoulderAngleDegrees - 2) * Math.PI / 180;
  const hSuP = point(
    backHlp.x + derived.backShoulderSeamLength * Math.cos(backShoulderAngle),
    backHlp.y + derived.backShoulderSeamLength * Math.sin(backShoulderAngle)
  );
  const p16 = point(p10.x, lineYAtX(backHlp, backShoulderAngle, p10.x));
  const p17 = midpoint(p10, p16);
  const hAP = midpoint(p10, p17);
  const p18 = point(p13.x, hAP.y);

  const p19 = point(p14.x, p5.y);
  const p20 = point(p14.x, p19.y - (measurements.frontLength - 10));
  const p21 = point(p14.x, p20.y + (measurements.breastDepth - 10));
  const frontHlp = point(p20.x - measurements.neckWidth, p20.y);
  const frontNeckDepth = point(p20.x, p20.y + measurements.neckWidth + 5 + FRONT_NECK_DROP_MM);
  const frontShoulderAngle = (measurements.shoulderAngleDegrees + 2) * Math.PI / 180;
  const vSuP = point(
    frontHlp.x - derived.shoulderSeamLength * Math.cos(frontShoulderAngle),
    frontHlp.y + derived.shoulderSeamLength * Math.sin(frontShoulderAngle)
  );
  const vAP = point(p13.x, p13.y - derived.quarterArmDiameterPlus);

  return {
    ...state,
    landmarks: {
      P1: p1,
      P2: p2,
      P3: p3,
      P4: p4,
      P5: p5,
      P6: p6,
      P7: p7,
      P8: p8,
      P9: p9,
      P10: p10,
      P11: p11,
      P12: p12,
      P13: p13,
      P14: p14,
      P15: null,
      P16: p16,
      P17: p17,
      P18: p18,
      P19: p19,
      P20: p20,
      P21: p21,
      backHLP: backHlp,
      hSuP,
      hAP,
      frontHLP: frontHlp,
      frontNeckDepth,
      vSuP,
      vAP
    }
  };
}

function buildBackPiece(state) {
  const { landmarks: p, allowancesMm: allowances } = state;
  const backNeck = sampleQuadratic(p.P2, point(p.backHLP.x, p.P2.y), p.backHLP, 10);
  const upperArmhole = sampleQuadratic(p.hSuP, p.P16, p.hAP, 10);
  const lowerArmhole = sampleQuadratic(p.hAP, point(p.P11.x, p.hAP.y), p.P11, 10);
  const sideHem = point(p.P11.x, p.P3.y);
  const outline = outlineFromSections([
    { points: backNeck, allowance: allowances.seam },
    { points: [p.backHLP, p.hSuP], allowance: allowances.seam },
    { points: [...upperArmhole, ...lowerArmhole.slice(1)], allowance: allowances.seam },
    { points: [p.P11, sideHem], allowance: allowances.seam },
    { points: [sideHem, p.P8], allowance: allowances.hem },
    { points: [p.P8, p.P7, p.P2], allowance: allowances.centerBack }
  ]);
  const centerAtShoulderBlade = horizontalIntersection(p.P2, p.P7, p.P17.y);

  return {
    id: "back",
    label: "Oberteil RT - Grundgeruest",
    cutQuantity: 2,
    onFold: false,
    ...outline,
    internalLines: [
      line("breastline", p.P9, p.P11, "Brustlinie"),
      line("waistline", p.P7, point(p.P11.x, p.P5.y), "Taillenlinie"),
      line("hipline", point(p.P8.x, p.P6.y), point(p.P11.x, p.P6.y), "Hueftlinie"),
      line("armline", p.P10, point(p.P10.x, p.P6.y), "hintere Armlinie"),
      line("sideline", p.P11, sideHem, "hintere Seitenlinie"),
      line("shoulder-blade-line", centerAtShoulderBlade, p.P17, "Schulterblattlinie")
    ],
    grainline: {
      from: point(p.P9.x + (p.P11.x - p.P9.x) * 0.35, p.P5.y + 30),
      to: point(p.P9.x + (p.P11.x - p.P9.x) * 0.35, p.P3.y - 60)
    }
  };
}

function buildFrontPiece(state) {
  const { landmarks: p, allowancesMm: allowances } = state;
  const frontNeck = sampleQuadratic(
    p.frontNeckDepth,
    point(p.frontHLP.x, p.frontNeckDepth.y),
    p.frontHLP,
    10
  );
  const upperArmhole = sampleQuadratic(p.vSuP, point(p.P13.x, p.vSuP.y), p.vAP, 10);
  const lowerArmhole = sampleQuadratic(p.vAP, point(p.P12.x, p.vAP.y), p.P12, 10);
  const sideHem = point(p.P12.x, p.P3.y);
  const frontHem = point(p.P14.x, p.P3.y);
  const outline = outlineFromSections([
    { points: frontNeck, allowance: allowances.seam },
    { points: [p.frontHLP, p.vSuP], allowance: allowances.seam },
    { points: [...upperArmhole, ...lowerArmhole.slice(1)], allowance: allowances.seam },
    { points: [p.P12, sideHem], allowance: allowances.seam },
    { points: [sideHem, frontHem], allowance: allowances.hem },
    { points: [frontHem, p.frontNeckDepth], allowance: 0 }
  ]);

  return {
    id: "front",
    label: "Oberteil VT - Grundgeruest im vM-Bruch",
    cutQuantity: 1,
    onFold: true,
    ...outline,
    internalLines: [
      line("breastline", p.P12, p.P14, "Brustlinie"),
      line("waistline", point(p.P12.x, p.P19.y), p.P19, "Taillenlinie"),
      line("hipline", point(p.P12.x, p.P6.y), point(p.P14.x, p.P6.y), "Hueftlinie"),
      line("armline", point(p.P13.x, p.vSuP.y), point(p.P13.x, p.P19.y), "vordere Armlinie"),
      line("sideline", p.P12, sideHem, "vordere Seitenlinie")
    ],
    grainline: {
      from: point(p.P14.x - (p.P14.x - p.P12.x) * 0.4, p.P19.y + 30),
      to: point(p.P14.x - (p.P14.x - p.P12.x) * 0.4, p.P3.y - 60)
    }
  };
}

export function constructBodiceBlock(state) {
  const { input, derived, constructionMm: construction, landmarks, derivationTrace } = state;
  const checkPassed = Math.abs(derived.breastWidthDifference) <= construction.breastWidthTolerance + EPSILON;
  const warnings = checkPassed ? [] : [{
    code: "BRUSTWEITENKONTROLLE_ABWEICHUNG",
    message: "vBrW + hBrW weicht von der halben BrW ab; Eingabemaße und Zugaben prüfen.",
    ruleRef: HOFENBITZER_BODICE_RULE_REFS.breastWidthCheck,
    sourceRefs: [HOFENBITZER_BODICE_SOURCE_REFS.widthLines]
  }];
  const mmToCm = (value) => value / 10;

  return {
    metadata: {
      name: "Oberteil-Grundgeruest ohne Abnaeher",
      method: METHOD.source,
      methodId: METHOD.id,
      methodVersion: METHOD.version,
      methodStatus: METHOD.status,
      methodSourceRefs: [...METHOD.sourceRefs],
      units: "mm",
      measurements: Object.fromEntries(
        METHOD.validationRules.requiredMeasurements.map((key) => [key, input[key]])
      ),
      constructionParameters: Object.fromEntries(
        Object.keys(METHOD.constructionParameters).map((key) => [key, input[key]])
      ),
      allowancesMm: { ...state.allowancesMm },
      modelMeasurements: {
        brWCm: mmToCm(derived.breastWidth),
        halfBrWCm: mmToCm(derived.halfBreastWidth),
        taWCm: mmToCm(derived.waistWidth),
        halfTaWCm: mmToCm(derived.halfWaistWidth),
        hueWCm: mmToCm(derived.hipWidth),
        halfHueWCm: mmToCm(derived.halfHipWidth),
        aitPlusCm: mmToCm(derived.armholeDepthPlus),
        rueBPlusCm: mmToCm(derived.backWidthPlus),
        arDPlusCm: mmToCm(derived.armDiameterPlus),
        quarterArDPlusCm: mmToCm(derived.quarterArmDiameterPlus),
        thirdArDPlusCm: mmToCm(derived.thirdArmDiameterPlus),
        twoThirdArDPlusCm: mmToCm(derived.twoThirdArmDiameterPlus),
        brBPlusCm: mmToCm(derived.breastBreadthPlus),
        suNLCm: mmToCm(derived.shoulderSeamLength),
        hSuNLCm: mmToCm(derived.backShoulderSeamLength)
      },
      constructionChecks: {
        breastWidth: {
          vBrWCm: mmToCm(derived.frontBreastWidth),
          hBrWCm: mmToCm(derived.backBreastWidth),
          sumCm: mmToCm(derived.breastWidthSum),
          expectedHalfBrWCm: mmToCm(derived.halfBreastWidth),
          differenceCm: mmToCm(derived.breastWidthDifference),
          toleranceCm: input.brustweitenToleranzCm,
          passed: checkPassed,
          ruleRef: HOFENBITZER_BODICE_RULE_REFS.breastWidthCheck,
          sourceRefs: [HOFENBITZER_BODICE_SOURCE_REFS.widthLines]
        },
        balance: {
          individualCm: mmToCm(derived.individualBalance),
          optimalCm: mmToCm(derived.optimalBalance),
          deviationCm: mmToCm(derived.balanceDeviation),
          withinOneCm: derived.balanceDeviation <= 10 + EPSILON,
          correctionApplied: false,
          ruleRef: HOFENBITZER_BODICE_RULE_REFS.balance,
          sourceRefs: [HOFENBITZER_BODICE_SOURCE_REFS.balance]
        }
      },
      points: Object.fromEntries(
        Object.entries(landmarks).map(([key, value]) => [key, value === null ? null : point(value.x, value.y)])
      ),
      warnings,
      derivationTrace: derivationTrace.map((entry) => ({
        ...entry,
        dependsOn: [...entry.dependsOn],
        sourceRefs: [...entry.sourceRefs]
      }))
    },
    pieces: [buildBackPiece(state), buildFrontPiece(state)]
  };
}

function assertFiniteClosedPolygon(name, points) {
  if (!Array.isArray(points) || points.length < 4) throw new Error(`${name} must contain a polygon`);
  for (const item of points) {
    if (!Number.isFinite(item.x) || !Number.isFinite(item.y)) {
      throw new Error(`${name} must contain only finite coordinates`);
    }
  }
  if (!samePoint(points[0], points.at(-1))) throw new Error(`${name} must be closed`);
}

export function validateBodiceBlock(block) {
  if (block?.metadata?.units !== "mm") throw new Error("bodice block must use millimetres");
  if (block?.metadata?.methodId !== METHOD.id || block?.metadata?.methodStatus !== METHOD.status) {
    throw new Error("bodice block must carry the approved Hofenbitzer method profile");
  }
  if (!Array.isArray(block.pieces) || block.pieces.length !== 2) {
    throw new Error("bodice block must contain back and front pieces");
  }
  if (block.pieces.map(({ id }) => id).join(",") !== "back,front") {
    throw new Error("bodice block pieces must have stable back and front ids");
  }
  for (const currentPiece of block.pieces) {
    assertFiniteClosedPolygon(`${currentPiece.id}.seamLine`, currentPiece.seamLine);
    assertFiniteClosedPolygon(`${currentPiece.id}.cuttingLine`, currentPiece.cuttingLine);
    for (const internalLine of currentPiece.internalLines) {
      for (const item of internalLine.points) {
        if (!Number.isFinite(item.x) || !Number.isFinite(item.y)) {
          throw new Error(`${currentPiece.id}.${internalLine.type} must contain finite coordinates`);
        }
      }
    }
  }
  for (const entry of block.metadata.derivationTrace) {
    if (!entry.ruleRef || !Array.isArray(entry.sourceRefs) || entry.sourceRefs.length === 0) {
      throw new Error(`${entry.outputId} must carry Hofenbitzer provenance`);
    }
  }
  return block;
}

export function draftBodiceBlock(input = {}) {
  const resolvedInput = applyBodiceMethodDefaults(input);
  const validInput = validateBodiceInput(resolvedInput);
  const normalized = normalizeBodiceUnits(validInput);
  const derived = deriveBodiceMeasures(normalized);
  const landmarks = constructBodiceLandmarks(derived);
  const block = constructBodiceBlock(landmarks);
  return validateBodiceBlock(block);
}
