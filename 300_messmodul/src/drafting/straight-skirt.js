import { closePolygon, offsetPolygon, point, sampleQuadratic } from "../geometry.js";
import {
  HOFENBITZER_BAND1_STRAIGHT_SKIRT_METHOD,
  HOFENBITZER_RULE_REFS,
  HOFENBITZER_SOURCE_REFS
} from "../methods/hofenbitzer-band1-straight-skirt.js";
import { derivationEntry } from "./derivation-trace.js";
import { classifyNiedrigDifferenzMm, deriveSuppressionMm } from "./niedrig-differenz.js";
import { validateStraightSkirtInput } from "./validation.js";

const METHOD = HOFENBITZER_BAND1_STRAIGHT_SKIRT_METHOD;
const METHOD_PARAMETER_DEFAULTS = Object.freeze({
  ...METHOD.constructionParameters,
  ...METHOD.allowances,
  overlapCm: METHOD.inputDefaults.overlapCm
});
const EPSILON = 1e-6;
const NOTCH_LENGTH_MM = 5;
const cmToMm = (value) => value * 10;

const CONSTRUCTION_PARAMETER_PROVENANCE = Object.freeze([
  ["waistEaseCm", "waistEase", HOFENBITZER_RULE_REFS.waistWidth, HOFENBITZER_SOURCE_REFS.table],
  ["hipEaseCm", "hipEase", HOFENBITZER_RULE_REFS.hipWidth, HOFENBITZER_SOURCE_REFS.table],
  ["sideSeamUpliftCm", "sideUplift", HOFENBITZER_RULE_REFS.sideWaistUplift, HOFENBITZER_SOURCE_REFS.shaping],
  ["sideHipShapeAdjustmentCm", "sideHipShapeAdjustment", HOFENBITZER_RULE_REFS.sideHipIntake, HOFENBITZER_SOURCE_REFS.shaping],
  ["frontDartIntakeCm", "frontDartIntake", HOFENBITZER_RULE_REFS.frontDartIntake, HOFENBITZER_SOURCE_REFS.shaping],
  ["frontDartLengthCm", "frontDartLength", HOFENBITZER_RULE_REFS.hipAndDarts, HOFENBITZER_SOURCE_REFS.shaping],
  ["frontDartUpliftCm", "frontDartUplift", HOFENBITZER_RULE_REFS.frontWaistUplift, HOFENBITZER_SOURCE_REFS.shaping],
  ["backDartLength1Cm", "backDartLength1", HOFENBITZER_RULE_REFS.hipAndDarts, HOFENBITZER_SOURCE_REFS.shaping],
  ["backDartLength2Cm", "backDartLength2", HOFENBITZER_RULE_REFS.splitBackDart, HOFENBITZER_SOURCE_REFS.twoBackDarts],
  ["backDartUpliftCm", "backDartUplift", HOFENBITZER_RULE_REFS.backWaistUplift, HOFENBITZER_SOURCE_REFS.shaping],
  ["secondBackDartUpliftCm", "secondBackDartUplift", HOFENBITZER_RULE_REFS.splitBackDart, HOFENBITZER_SOURCE_REFS.twoBackDarts],
  ["backDartDifferenceCm", "backDartDifference", HOFENBITZER_RULE_REFS.splitBackDart, HOFENBITZER_SOURCE_REFS.twoBackDarts],
  ["backDartPositionOffsetCm", "backDartPositionOffset", HOFENBITZER_RULE_REFS.splitBackDart, HOFENBITZER_SOURCE_REFS.twoBackDarts],
  ["waistbandWidthCm", "waistbandWidth", HOFENBITZER_RULE_REFS.waistbandWidth, HOFENBITZER_SOURCE_REFS.waistband]
]);

const ALLOWANCE_PROVENANCE = Object.freeze([
  ["seamAllowanceCm", "seam"],
  ["hemAllowanceCm", "hem"],
  ["centerBackAllowanceCm", "centerBack"]
]);

function interpolateY(anchors, x) {
  if (anchors.length === 1) return anchors[0].y;
  return anchors.reduce((sum, anchor, index) => {
    let basis = 1;
    for (let otherIndex = 0; otherIndex < anchors.length; otherIndex += 1) {
      if (otherIndex === index) continue;
      const divisor = anchor.x - anchors[otherIndex].x;
      if (Math.abs(divisor) < EPSILON) throw new Error("waist shaping points must have distinct positions");
      basis *= (x - anchors[otherIndex].x) / divisor;
    }
    return sum + anchor.y * basis;
  }, 0);
}

function sampleWaistLine(anchors, steps = 12) {
  const endX = anchors.at(-1).x;
  return Array.from({ length: steps + 1 }, (_, index) => {
    const x = endX * index / steps;
    return point(x, interpolateY(anchors, x));
  });
}

function dart(centerX, intake, length, waistY) {
  return {
    type: "dart",
    points: [
      point(centerX - intake / 2, waistY),
      point(centerX, waistY + length),
      point(centerX + intake / 2, waistY)
    ]
  };
}

function notch(label, from, to) {
  return {
    type: "notch",
    label,
    points: [point(from.x, from.y), point(to.x, to.y)]
  };
}

function horizontalNotch(label, anchor, direction) {
  return notch(
    label,
    anchor,
    point(anchor.x + direction * NOTCH_LENGTH_MM, anchor.y)
  );
}

function dartLegNotches(darts) {
  return darts.flatMap((currentDart) => [currentDart.points[0], currentDart.points.at(-1)]
    .map((anchor) => notch(
      "dart-leg",
      anchor,
      point(anchor.x, anchor.y + NOTCH_LENGTH_MM)
    )));
}

function outline({ waistAnchors, hipWidth, hipDepth, length }) {
  const waistLine = sampleWaistLine(waistAnchors);
  const sideWaist = waistLine.at(-1);
  const sideHip = point(hipWidth, hipDepth);
  const hipCurve = sampleQuadratic(
    sideWaist,
    point(hipWidth, sideWaist.y),
    sideHip,
    12
  );
  return closePolygon([
    ...waistLine,
    ...hipCurve.slice(1),
    point(hipWidth, length),
    point(0, length)
  ]);
}

function piece({ id, label, seamLine, hipDepth, allowance, centerAllowance, hemAllowance, darts, onFold, sideWaist }) {
  const open = seamLine.slice(0, -1);
  const allowances = open.map((_, index) => {
    if (index === open.length - 2) return hemAllowance;
    if (index === open.length - 1) return centerAllowance;
    return allowance;
  });
  const maxX = Math.max(...open.map((item) => item.x));
  const length = Math.max(...open.map((item) => item.y));
  const centerWaist = seamLine[0];
  const notches = [
    horizontalNotch("side-hip", point(maxX, hipDepth), -1),
    horizontalNotch("SN", sideWaist, -1),
    horizontalNotch(onFold ? "vM" : "hM", centerWaist, 1),
    ...dartLegNotches(darts)
  ];
  return {
    id,
    label,
    cutQuantity: onFold ? 1 : 2,
    onFold,
    seamLine,
    cuttingLine: offsetPolygon(open, allowances),
    internalLines: [
      ...darts,
      { type: "hipline", points: [point(0, hipDepth), point(maxX, hipDepth)] },
      ...notches
    ],
    grainline: { from: point(maxX * 0.45, 180), to: point(maxX * 0.45, Math.max(220, length - 120)) }
  };
}

function waistbandPiece({ finishedLength, finishedWidth, allowance, overlap }) {
  if (!Number.isFinite(finishedLength) || finishedLength <= 0) {
    throw new Error("waistbandFinishedLength must be finite and positive");
  }
  if (!Number.isFinite(finishedWidth) || finishedWidth <= 0) {
    throw new Error("waistbandWidthCm must produce a finite positive width");
  }
  if (!Number.isFinite(overlap) || overlap < 0) {
    throw new Error("overlapCm must produce a finite non-negative length");
  }

  const gesamtLaenge = finishedLength + overlap;
  const seamLineHeight = finishedWidth * 2;
  const seamLine = closePolygon([
    point(0, 0),
    point(gesamtLaenge, 0),
    point(gesamtLaenge, seamLineHeight),
    point(0, seamLineHeight)
  ]);
  const markerPositions = [
    ["hM", 0],
    ["SN", finishedLength / 4],
    ["vM", finishedLength / 2],
    ["SN", finishedLength * 3 / 4],
    ["hM", finishedLength]
  ];
  const marks = markerPositions.map(([label, x]) => ({
    type: "waistband-mark",
    label,
    points: [point(x, 0), point(x, seamLineHeight)]
  }));
  const notches = markerPositions
    .filter(([label]) => label === "SN")
    .map(([, x]) => notch("SN", point(x, 0), point(x, NOTCH_LENGTH_MM)));

  return {
    id: "waistband",
    label: "Bund / Gerader Rock - 1x Ost + El",
    cutQuantity: 1,
    onFold: false,
    seamLine,
    cuttingLine: offsetPolygon(seamLine.slice(0, -1), Array(4).fill(allowance)),
    internalLines: [
      {
        type: "foldline",
        label: "Umbruch-/Bügellinie",
        points: [point(0, finishedWidth), point(gesamtLaenge, finishedWidth)]
      },
      ...marks,
      ...(overlap > 0 ? [{
        type: "overlap-mark",
        label: "Übertritt",
        points: [
          point(finishedLength, 0),
          point(finishedLength, seamLineHeight),
          point(gesamtLaenge, seamLineHeight),
          point(gesamtLaenge, 0)
        ]
      }] : []),
      ...notches
    ],
    grainline: {
      from: point(0, finishedWidth / 2),
      to: point(gesamtLaenge, finishedWidth / 2)
    },
    metadata: {
      finishedLengthMm: finishedLength,
      overlapMm: overlap,
      gesamtLaengeMm: gesamtLaenge,
      finishedWidthMm: finishedWidth,
      seamLineHeightMm: seamLineHeight,
      cutHeightMm: seamLineHeight + allowance * 2,
      foldedLengthwise: true,
      materials: ["Ost", "El"]
    }
  };
}

function lineLength(points) {
  return points.slice(1).reduce((total, current, index) => (
    total + Math.hypot(current.x - points[index].x, current.y - points[index].y)
  ), 0);
}

function waistSeamLength(seamLine, darts) {
  const open = seamLine.slice(0, -1);
  const sideWaistY = Math.min(...open.map(({ y }) => y));
  const sideWaistIndex = open.findIndex(({ y }) => Math.abs(y - sideWaistY) <= EPSILON);
  if (sideWaistIndex < 1) throw new Error("waist seam cannot be measured");
  const dartIntake = darts.reduce((total, currentDart) => (
    total + lineLength([currentDart.points[0], currentDart.points.at(-1)])
  ), 0);
  return lineLength(open.slice(0, sideWaistIndex + 1)) - dartIntake;
}

function trace({
  outputId,
  value,
  dependsOn,
  ruleRef,
  sourceRef,
  modelDecision = false,
  decisionNote
}) {
  const entry = derivationEntry({
    outputId,
    value,
    unit: "mm",
    dependsOn,
    ruleRef,
    sourceRefs: [sourceRef]
  });
  return {
    ...entry,
    ...(modelDecision ? { modelDecision: true, decisionNote } : {})
  };
}

function splitBackDarts(totalIntake, difference) {
  if (totalIntake <= 45 + EPSILON) return [totalIntake];
  const first = (totalIntake + difference) / 2;
  const second = (totalIntake - difference) / 2;
  if (second <= 0 || first > 45 + EPSILON) {
    throw new Error("back dart intake is outside the verified Hofenbitzer two-dart range");
  }
  return [first, second];
}

export function applyStraightSkirtMethodDefaults(input = {}) {
  return { ...METHOD_PARAMETER_DEFAULTS, ...input };
}

export function validateStraightSkirt(input) {
  const validated = validateStraightSkirtInput(input, METHOD.validationRules);
  if (!Number.isFinite(validated.overlapCm) || validated.overlapCm < 0) {
    throw new Error("overlapCm must be a finite non-negative number");
  }
  return validated;
}

export function normalizeStraightSkirtUnits(input) {
  return {
    input,
    measurementsMm: {
      waist: cmToMm(input.waistCm),
      hip: cmToMm(input.hipCm),
      hipDepth: cmToMm(input.waistToHipCm),
      length: cmToMm(input.lengthCm)
    },
    constructionMm: {
      waistEase: cmToMm(input.waistEaseCm),
      hipEase: cmToMm(input.hipEaseCm),
      sideUplift: cmToMm(input.sideSeamUpliftCm),
      sideHipShapeAdjustment: cmToMm(input.sideHipShapeAdjustmentCm),
      frontDartIntake: cmToMm(input.frontDartIntakeCm),
      frontDartLength: cmToMm(input.frontDartLengthCm),
      frontDartUplift: cmToMm(input.frontDartUpliftCm),
      backDartLength1: cmToMm(input.backDartLength1Cm),
      backDartLength2: cmToMm(input.backDartLength2Cm),
      backDartUplift: cmToMm(input.backDartUpliftCm),
      secondBackDartUplift: cmToMm(input.secondBackDartUpliftCm),
      backDartDifference: cmToMm(input.backDartDifferenceCm),
      backDartPositionOffset: cmToMm(input.backDartPositionOffsetCm),
      waistbandWidth: cmToMm(input.waistbandWidthCm)
    },
    allowancesMm: {
      seam: cmToMm(input.seamAllowanceCm),
      hem: cmToMm(input.hemAllowanceCm),
      centerBack: cmToMm(input.centerBackAllowanceCm)
    },
    overlapMm: cmToMm(input.overlapCm)
  };
}

export function deriveStraightSkirtMeasures(normalized) {
  const { input, measurementsMm, constructionMm, allowancesMm } = normalized;
  // #24: Die Suppressionskette kommt aus der EINEN Rechenquelle in
  // niedrig-differenz.js — keine lokale Formelkopie mehr, damit Klassifikation
  // und Geometriepfad nie auseinanderdriften können.
  const {
    hipWidth,
    waistWidth,
    halfHipWidth,
    quarterHipWidth,
    halfWaistWidth,
    waistSuppression,
    sideHipIntake,
    frontDartIntake,
    backDartTotalIntake
  } = deriveSuppressionMm({
    hipMm: measurementsMm.hip,
    waistMm: measurementsMm.waist,
    hipEaseMm: constructionMm.hipEase,
    waistEaseMm: constructionMm.waistEase,
    sideHipShapeAdjustmentMm: constructionMm.sideHipShapeAdjustment,
    frontDartIntakeMm: constructionMm.frontDartIntake
  });

  if (waistSuppression <= 0) throw new Error("Hofenbitzer waist suppression must be positive");
  if (sideHipIntake <= 0 || sideHipIntake >= waistSuppression) {
    throw new Error("sideHipShapeAdjustmentCm produces an invalid side hip intake");
  }
  // #24: Die Niedrig-Differenz-Entscheidung trifft die eine Klassifikationsquelle;
  // Meldungstext und Error-Konstruktor bleiben unverändert (Stress-/Honesty-Vertrag),
  // additiv kommen code und detail für Adapter, API und UI dazu.
  const niedrigDifferenz = classifyNiedrigDifferenzMm({
    hipMm: measurementsMm.hip,
    waistMm: measurementsMm.waist,
    hipEaseMm: constructionMm.hipEase,
    waistEaseMm: constructionMm.waistEase,
    sideHipShapeAdjustmentMm: constructionMm.sideHipShapeAdjustment,
    frontDartIntakeMm: constructionMm.frontDartIntake
  });
  if (niedrigDifferenz.ok === false) {
    const error = new Error("front and side intake leave no positive back dart intake");
    error.code = niedrigDifferenz.reason;
    error.detail = niedrigDifferenz.detail;
    throw error;
  }

  const backDartIntakes = splitBackDarts(backDartTotalIntake, constructionMm.backDartDifference);
  const frontWaistWidth = quarterHipWidth - sideHipIntake / 2;
  const backWaistWidth = quarterHipWidth - sideHipIntake / 2;
  const frontDartCenter = frontDartIntake > 0
    ? frontWaistWidth - measurementsMm.waist / 10
    : null;
  const backDartCenters = backDartIntakes.length === 1
    ? [backWaistWidth / 2]
    : (() => {
        const first = quarterHipWidth / 3 + constructionMm.backDartPositionOffset;
        const second = (first + backDartIntakes[0] / 2 + backWaistWidth) / 2;
        return [first, second];
      })();

  if (frontDartCenter !== null && frontDartCenter <= frontDartIntake / 2) {
    throw new Error("front dart does not fit between front centre and side seam");
  }
  for (const [index, center] of backDartCenters.entries()) {
    const halfIntake = backDartIntakes[index] / 2;
    if (center - halfIntake <= 0 || center + halfIntake >= backWaistWidth) {
      throw new Error(`back dart ${index + 1} does not fit inside the waist line`);
    }
  }

  const netHalfWaist = frontWaistWidth + backWaistWidth
    - frontDartIntake
    - backDartTotalIntake;
  if (Math.abs(netHalfWaist - halfWaistWidth) > EPSILON) {
    throw new Error("Hofenbitzer intake balance does not reproduce the half waist width");
  }

  const frontWaistSeamLength = frontWaistWidth - frontDartIntake;
  const backWaistSeamLength = backWaistWidth - backDartTotalIntake;
  const waistbandFinishedLength = measurementsMm.waist;
  if (!Number.isFinite(waistbandFinishedLength) || waistbandFinishedLength <= 0) {
    throw new Error("TaU must be finite and positive for the waistband");
  }
  const waistbandHalfEase = frontWaistSeamLength + backWaistSeamLength - waistbandFinishedLength / 2;

  const derived = {
    hipWidth,
    waistWidth,
    halfHipWidth,
    quarterHipWidth,
    halfWaistWidth,
    waistSuppression,
    sideHipIntake,
    frontDartIntake,
    backDartTotalIntake,
    backDartIntakes,
    frontWaistWidth,
    backWaistWidth,
    frontDartCenter,
    backDartCenters,
    netHalfWaist,
    frontWaistSeamLength,
    backWaistSeamLength,
    waistbandFinishedLength,
    waistbandWidth: constructionMm.waistbandWidth,
    waistbandHalfEase
  };

  const derivationTrace = [
    trace({
      outputId: "derived.hipWidth",
      value: hipWidth,
      dependsOn: ["measurements.hip", "construction.hipEase"],
      ruleRef: HOFENBITZER_RULE_REFS.hipWidth,
      sourceRef: HOFENBITZER_SOURCE_REFS.table
    }),
    trace({
      outputId: "derived.waistWidth",
      value: waistWidth,
      dependsOn: ["measurements.waist", "construction.waistEase"],
      ruleRef: HOFENBITZER_RULE_REFS.waistWidth,
      sourceRef: HOFENBITZER_SOURCE_REFS.table
    }),
    trace({
      outputId: "derived.waistSuppression",
      value: waistSuppression,
      dependsOn: ["derived.halfHipWidth", "derived.halfWaistWidth"],
      ruleRef: HOFENBITZER_RULE_REFS.waistSuppression,
      sourceRef: HOFENBITZER_SOURCE_REFS.table
    }),
    trace({
      outputId: "derived.sideHipIntake",
      value: sideHipIntake,
      dependsOn: ["derived.waistSuppression", "construction.sideHipShapeAdjustment"],
      ruleRef: HOFENBITZER_RULE_REFS.sideHipIntake,
      sourceRef: HOFENBITZER_SOURCE_REFS.shaping
    }),
    trace({
      outputId: "derived.frontDartIntake",
      value: frontDartIntake,
      dependsOn: ["construction.frontDartIntake"],
      ruleRef: HOFENBITZER_RULE_REFS.frontDartIntake,
      sourceRef: HOFENBITZER_SOURCE_REFS.shaping
    }),
    trace({
      outputId: "derived.backDartTotalIntake",
      value: backDartTotalIntake,
      dependsOn: ["derived.waistSuppression", "derived.sideHipIntake", "derived.frontDartIntake"],
      ruleRef: HOFENBITZER_RULE_REFS.backDartIntake,
      sourceRef: HOFENBITZER_SOURCE_REFS.shaping
    }),
    trace({
      outputId: "derived.frontDartCenter",
      value: frontDartCenter ?? 0,
      dependsOn: ["derived.frontWaistWidth", "measurements.waist"],
      ruleRef: HOFENBITZER_RULE_REFS.hipAndDarts,
      sourceRef: HOFENBITZER_SOURCE_REFS.shaping
    }),
    ...backDartCenters.map((value, index) => trace({
      outputId: `derived.backDartCenters.${index}`,
      value,
      dependsOn: backDartCenters.length === 1
        ? ["derived.backWaistWidth"]
        : ["derived.quarterHipWidth", "construction.backDartPositionOffset"],
      ruleRef: backDartCenters.length === 1
        ? HOFENBITZER_RULE_REFS.hipAndDarts
        : HOFENBITZER_RULE_REFS.splitBackDart,
      sourceRef: backDartCenters.length === 1
        ? HOFENBITZER_SOURCE_REFS.shaping
        : HOFENBITZER_SOURCE_REFS.twoBackDarts
    })),
    trace({
      outputId: "derived.waistbandFinishedLength",
      value: waistbandFinishedLength,
      dependsOn: ["measurements.waist"],
      ruleRef: HOFENBITZER_RULE_REFS.waistbandLength,
      sourceRef: HOFENBITZER_SOURCE_REFS.waistband
    }),
    trace({
      outputId: "derived.waistbandWidth",
      value: constructionMm.waistbandWidth,
      dependsOn: ["construction.waistbandWidth"],
      ruleRef: HOFENBITZER_RULE_REFS.waistbandWidth,
      sourceRef: HOFENBITZER_SOURCE_REFS.waistband
    }),
    trace({
      outputId: "derived.frontWaistSeamLength",
      value: frontWaistSeamLength,
      dependsOn: ["derived.frontWaistWidth", "derived.frontDartIntake"],
      ruleRef: HOFENBITZER_RULE_REFS.waistbandConnection,
      sourceRef: HOFENBITZER_SOURCE_REFS.waistband
    }),
    trace({
      outputId: "derived.backWaistSeamLength",
      value: backWaistSeamLength,
      dependsOn: ["derived.backWaistWidth", "derived.backDartTotalIntake"],
      ruleRef: HOFENBITZER_RULE_REFS.waistbandConnection,
      sourceRef: HOFENBITZER_SOURCE_REFS.waistband
    }),
    trace({
      outputId: "derived.waistbandHalfEase",
      value: waistbandHalfEase,
      dependsOn: ["derived.frontWaistSeamLength", "derived.backWaistSeamLength", "measurements.waist"],
      ruleRef: HOFENBITZER_RULE_REFS.waistbandEase,
      sourceRef: HOFENBITZER_SOURCE_REFS.waistband
    }),
    ...CONSTRUCTION_PARAMETER_PROVENANCE.map(([inputKey, normalizedKey, ruleRef, sourceRef]) => trace({
      outputId: `construction.${inputKey}`,
      value: constructionMm[normalizedKey],
      dependsOn: [`input.${inputKey}`],
      ruleRef,
      sourceRef
    })),
    ...ALLOWANCE_PROVENANCE.map(([inputKey, normalizedKey]) => trace({
      outputId: `allowances.${inputKey}`,
      value: allowancesMm[normalizedKey],
      dependsOn: [`input.${inputKey}`],
      ruleRef: HOFENBITZER_RULE_REFS.productionAllowances,
      sourceRef: HOFENBITZER_SOURCE_REFS.production
    })),
    trace({
      outputId: "metadata.overlapCm",
      value: cmToMm(input.overlapCm),
      dependsOn: ["input.overlapCm"],
      ruleRef: HOFENBITZER_RULE_REFS.waistbandOverlap,
      sourceRef: HOFENBITZER_SOURCE_REFS.waistband,
      modelDecision: true,
      decisionNote: "Engine overlap length for the hM closure; S.39-41 defines the closure, not a fixed value"
    })
  ];

  return { ...normalized, derived, derivationTrace };
}

export function constructStraightSkirtLandmarks(state) {
  const { measurementsMm, constructionMm, derived } = state;
  const frontAnchors = [point(0, 0)];
  if (derived.frontDartCenter !== null) {
    frontAnchors.push(point(derived.frontDartCenter, -constructionMm.frontDartUplift));
  }
  frontAnchors.push(point(derived.frontWaistWidth, -constructionMm.sideUplift));

  const backAnchors = [point(0, 0)];
  derived.backDartCenters.forEach((center, index) => {
    const uplift = index === 0
      ? constructionMm.backDartUplift
      : constructionMm.secondBackDartUplift;
    backAnchors.push(point(center, -uplift));
  });
  backAnchors.push(point(derived.backWaistWidth, -constructionMm.sideUplift));

  const commonOutline = {
    hipWidth: derived.quarterHipWidth,
    hipDepth: measurementsMm.hipDepth,
    length: measurementsMm.length
  };
  const frontSeamLine = outline({ ...commonOutline, waistAnchors: frontAnchors });
  const backSeamLine = outline({ ...commonOutline, waistAnchors: backAnchors });

  return {
    ...state,
    landmarks: {
      front: {
        seamLine: frontSeamLine,
        darts: derived.frontDartCenter === null ? [] : [
          dart(
            derived.frontDartCenter,
            derived.frontDartIntake,
            constructionMm.frontDartLength,
            interpolateY(frontAnchors, derived.frontDartCenter)
          )
        ]
      },
      back: {
        seamLine: backSeamLine,
        darts: derived.backDartCenters.map((center, index) => dart(
          center,
          derived.backDartIntakes[index],
          index === 0 ? constructionMm.backDartLength1 : constructionMm.backDartLength2,
          interpolateY(backAnchors, center)
        ))
      }
    }
  };
}

export function constructStraightSkirtBlock(state) {
  const {
    input,
    measurementsMm,
    constructionMm,
    allowancesMm,
    overlapMm,
    landmarks,
    derived,
    derivationTrace
  } = state;
  const frontWaistSeamLength = waistSeamLength(landmarks.front.seamLine, landmarks.front.darts);
  const backWaistSeamLength = waistSeamLength(landmarks.back.seamLine, landmarks.back.darts);
  const waistbandHalfEase = frontWaistSeamLength
    + backWaistSeamLength
    - derived.waistbandFinishedLength / 2;
  const measuredWaistbandTrace = [
    trace({
      outputId: "derived.frontWaistSeamLength",
      value: frontWaistSeamLength,
      dependsOn: ["landmarks.front.seamLine", "landmarks.front.darts"],
      ruleRef: HOFENBITZER_RULE_REFS.waistbandConnection,
      sourceRef: HOFENBITZER_SOURCE_REFS.waistband
    }),
    trace({
      outputId: "derived.backWaistSeamLength",
      value: backWaistSeamLength,
      dependsOn: ["landmarks.back.seamLine", "landmarks.back.darts"],
      ruleRef: HOFENBITZER_RULE_REFS.waistbandConnection,
      sourceRef: HOFENBITZER_SOURCE_REFS.waistband
    }),
    trace({
      outputId: "derived.waistbandHalfEase",
      value: waistbandHalfEase,
      dependsOn: ["derived.frontWaistSeamLength", "derived.backWaistSeamLength", "derived.waistbandFinishedLength"],
      ruleRef: HOFENBITZER_RULE_REFS.waistbandEase,
      sourceRef: HOFENBITZER_SOURCE_REFS.waistband
    })
  ];
  const measuredOutputIds = new Set(measuredWaistbandTrace.map(({ outputId }) => outputId));
  const blockDerivationTrace = [
    ...derivationTrace.filter(({ outputId }) => !measuredOutputIds.has(outputId)),
    ...measuredWaistbandTrace
  ];
  const waistbandWarnings = waistbandHalfEase > 15 + EPSILON
    ? [{
        code: "WAISTBAND_EASE_ABOVE_VERIFIED_RANGE",
        message: "Taillenmehrweite ist größer als 1,5 cm; Rock-Konstruktion oder Messung prüfen.",
        ruleRef: HOFENBITZER_RULE_REFS.waistbandEase,
        sourceRefs: [HOFENBITZER_SOURCE_REFS.waistband]
      }]
    : [];
  const waistbandReference = METHOD.referenceCase.expectedCm;
  return {
    metadata: {
      name: "Gerader Rock-Grundschnitt",
      method: METHOD.source,
      methodId: METHOD.id,
      methodVersion: METHOD.version,
      methodStatus: METHOD.status,
      methodSourceRefs: [...METHOD.sourceRefs, HOFENBITZER_SOURCE_REFS.waistband],
      units: "mm",
      measurements: {
        waistCm: input.waistCm,
        hipCm: input.hipCm,
        waistToHipCm: input.waistToHipCm,
        lengthCm: input.lengthCm
      },
      allowances: {
        seamAllowanceCm: input.seamAllowanceCm,
        hemAllowanceCm: input.hemAllowanceCm,
        centerBackAllowanceCm: input.centerBackAllowanceCm
      },
      overlapCm: input.overlapCm,
      constructionParameters: Object.fromEntries(
        Object.keys(METHOD.constructionParameters).map((key) => [key, input[key]])
      ),
      constructionChecks: {
        hipWidthCm: derived.hipWidth / 10,
        waistWidthCm: derived.waistWidth / 10,
        waistSuppressionCm: derived.waistSuppression / 10,
        sideHipIntakeCm: derived.sideHipIntake / 10,
        frontDartIntakeCm: derived.frontDartIntake / 10,
        backDartIntakesCm: derived.backDartIntakes.map((value) => value / 10),
        netHalfWaistCm: derived.netHalfWaist / 10,
        waistbandFinishedLengthCm: derived.waistbandFinishedLength / 10,
        waistbandWidthCm: derived.waistbandWidth / 10,
        frontWaistSeamLengthCm: frontWaistSeamLength / 10,
        backWaistSeamLengthCm: backWaistSeamLength / 10,
        waistbandHalfEaseCm: waistbandHalfEase / 10
      },
      referenceChecks: {
        waistbandSize38: {
          frontWaistSeamLengthCm: waistbandReference.frontWaistSeamLength,
          backWaistSeamLengthCm: waistbandReference.backWaistSeamLength,
          halfWaistCm: waistbandReference.waistbandHalfWaist,
          waistbandHalfEaseCm: waistbandReference.waistbandHalfEase,
          ruleRef: HOFENBITZER_RULE_REFS.waistbandEase,
          sourceRefs: [HOFENBITZER_SOURCE_REFS.waistband]
        }
      },
      warnings: waistbandWarnings,
      derivationTrace: blockDerivationTrace.map((entry) => ({
        ...entry,
        dependsOn: [...entry.dependsOn],
        sourceRefs: [...entry.sourceRefs]
      }))
    },
    pieces: [
      piece({
        id: "back",
        label: "RT gerader Rock - 2x-p Oberstoff",
        seamLine: landmarks.back.seamLine,
        hipDepth: measurementsMm.hipDepth,
        allowance: allowancesMm.seam,
        centerAllowance: allowancesMm.centerBack,
        hemAllowance: allowancesMm.hem,
        darts: landmarks.back.darts,
        onFold: false,
        sideWaist: point(derived.backWaistWidth, -constructionMm.sideUplift)
      }),
      piece({
        id: "front",
        label: "VT gerader Rock - 1x Oberstoff im vM-Bruch",
        seamLine: landmarks.front.seamLine,
        hipDepth: measurementsMm.hipDepth,
        allowance: allowancesMm.seam,
        centerAllowance: 0,
        hemAllowance: allowancesMm.hem,
        darts: landmarks.front.darts,
        onFold: true,
        sideWaist: point(derived.frontWaistWidth, -constructionMm.sideUplift)
      }),
      waistbandPiece({
        finishedLength: derived.waistbandFinishedLength,
        finishedWidth: constructionMm.waistbandWidth,
        allowance: allowancesMm.seam,
        overlap: overlapMm
      })
    ]
  };
}

function assertFinitePoints(name, points) {
  if (!Array.isArray(points) || points.length < 4) throw new Error(`${name} must contain a polygon`);
  for (const item of points) {
    if (!Number.isFinite(item.x) || !Number.isFinite(item.y)) {
      throw new Error(`${name} must contain only finite coordinates`);
    }
  }
  const first = points[0];
  const last = points.at(-1);
  if (first.x !== last.x || first.y !== last.y) throw new Error(`${name} must be closed`);
}

export function validateStraightSkirtBlock(block) {
  if (block?.metadata?.units !== "mm") throw new Error("straight-skirt block must use millimetres");
  if (block?.metadata?.methodId !== METHOD.id || block?.metadata?.methodStatus !== "verified") {
    throw new Error("straight-skirt block must carry the verified Hofenbitzer method profile");
  }
  if (!Array.isArray(block.pieces) || block.pieces.length !== 3) {
    throw new Error("straight-skirt block must contain back, front and waistband pieces");
  }
  if (block.pieces.map(({ id }) => id).join(",") !== "back,front,waistband") {
    throw new Error("straight-skirt block pieces must have stable back, front and waistband ids");
  }
  for (const currentPiece of block.pieces) {
    assertFinitePoints(`${currentPiece.id}.seamLine`, currentPiece.seamLine);
    assertFinitePoints(`${currentPiece.id}.cuttingLine`, currentPiece.cuttingLine);
  }
  for (const entry of block.metadata.derivationTrace) {
    if (!entry.ruleRef || entry.sourceRefs.length === 0) {
      throw new Error(`${entry.outputId} must carry Hofenbitzer provenance`);
    }
  }
  return block;
}

export function draftStraightSkirt(input = {}) {
  const resolvedInput = applyStraightSkirtMethodDefaults(input);
  const validInput = validateStraightSkirt(resolvedInput);
  const normalized = normalizeStraightSkirtUnits(validInput);
  const derived = deriveStraightSkirtMeasures(normalized);
  const landmarks = constructStraightSkirtLandmarks(derived);
  const block = constructStraightSkirtBlock(landmarks);
  return validateStraightSkirtBlock(block);
}
