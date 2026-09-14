const TRANSCRIPTION_ROOT = "hofenbitzer/band_1/transkription";

export const HOFENBITZER_SOURCE_REFS = Object.freeze({
  overview: `${TRANSCRIPTION_ROOT}/s32-36_gerader-rock-grundschnitt.md#seite-32`,
  table: `${TRANSCRIPTION_ROOT}/s32-36_gerader-rock-grundschnitt.md#seite-33`,
  shaping: `${TRANSCRIPTION_ROOT}/s32-36_gerader-rock-grundschnitt.md#seite-34`,
  twoBackDarts: `${TRANSCRIPTION_ROOT}/s32-36_gerader-rock-grundschnitt.md#seite-35`,
  production: `${TRANSCRIPTION_ROOT}/s32-36_gerader-rock-grundschnitt.md#seite-36`,
  waistband: `${TRANSCRIPTION_ROOT}/s39-41_bund.md#s39--gerader-bund-1`
});

export const HOFENBITZER_RULE_REFS = Object.freeze({
  hipWidth: "HB1-S33-HUEFTWEITE",
  waistWidth: "HB1-S33-TAILLENWEITE",
  waistSuppression: "HB1-S33-TAILLENAUSFALL",
  sideHipIntake: "HB1-S34-SCHRITT-13",
  frontDartIntake: "HB1-S34-SCHRITT-14",
  backDartIntake: "HB1-S34-SCHRITT-15",
  sideWaistUplift: "HB1-S34-SCHRITT-10",
  frontWaistUplift: "HB1-S34-SCHRITT-11",
  backWaistUplift: "HB1-S34-SCHRITT-12",
  hipAndDarts: "HB1-S34-SCHRITTE-16-18",
  splitBackDart: "HB1-S35-SCHRITTE-19-21",
  finishWaist: "HB1-S35-SCHRITTE-22-26",
  productionAllowances: "HB1-S36-PRODUKTIONSSCHNITT",
  waistbandConnection: "HB1-S39-SCHRITTE-3-4",
  waistbandLength: "HB1-S39-BUNDLAENGE",
  waistbandWidth: "HB1-S39-BUNDBREITE",
  waistbandEase: "HB1-S39-EINHALTEWEITE",
  waistbandOverlap: "HB1-S40-HM-UEBERTRITT"
});

const sampleMeasurements = Object.freeze({
  waistCm: 72,
  hipCm: 97,
  waistToHipCm: 21,
  lengthCm: 50
});

const constructionParameters = Object.freeze({
  waistEaseCm: 2,
  hipEaseCm: 3,
  sideSeamUpliftCm: 1,
  sideHipShapeAdjustmentCm: 0,
  frontDartIntakeCm: 2.5,
  frontDartLengthCm: 9,
  frontDartUpliftCm: 0.5,
  backDartLength1Cm: 14.5,
  backDartLength2Cm: 13,
  backDartUpliftCm: 0.3,
  secondBackDartUpliftCm: 0.5,
  backDartDifferenceCm: 0.5,
  backDartPositionOffsetCm: 0,
  waistbandWidthCm: 4
});

const allowances = Object.freeze({
  seamAllowanceCm: 2,
  hemAllowanceCm: 3.5,
  centerBackAllowanceCm: 2
});

const referenceCase = Object.freeze({
  name: "Hofenbitzer Band 1, Groesse 38",
  expectedCm: Object.freeze({
    hipWidth: 100,
    halfHipWidth: 50,
    quarterHipWidth: 25,
    waistWidth: 74,
    halfWaistWidth: 37,
    waistSuppression: 13,
    sideHipIntake: 6.5,
    frontDartIntake: 2.5,
    backDartTotalIntake: 4,
    frontWaistSeamLength: 19.7,
    backWaistSeamLength: 17.5,
    waistbandHalfWaist: 36,
    waistbandHalfEase: 1.2
  }),
  sourceRefs: Object.freeze([HOFENBITZER_SOURCE_REFS.table, HOFENBITZER_SOURCE_REFS.shaping])
});

export const HOFENBITZER_BAND1_STRAIGHT_SKIRT_METHOD = Object.freeze({
  id: "hofenbitzer-band1-straight-skirt",
  version: "1.0.0",
  status: "verified",
  source: "Guido Hofenbitzer, Grundschnitte und Modellentwicklungen, Band 1, 3. Auflage 2024, S. 32-36.",
  pageReferences: Object.freeze(["Hofenbitzer Band 1 (2024), S. 32-36"]),
  sourceRefs: Object.freeze([
    HOFENBITZER_SOURCE_REFS.overview,
    HOFENBITZER_SOURCE_REFS.table,
    HOFENBITZER_SOURCE_REFS.shaping,
    HOFENBITZER_SOURCE_REFS.twoBackDarts,
    HOFENBITZER_SOURCE_REFS.production
  ]),
  sampleMeasurements,
  constructionParameters,
  allowances,
  referenceCase,
  validationRules: Object.freeze({
    waistEaseCm: Object.freeze({ min: 1, max: 2, sourceRef: HOFENBITZER_SOURCE_REFS.table }),
    hipEaseCm: Object.freeze({ min: 2, max: 3, sourceRef: HOFENBITZER_SOURCE_REFS.table }),
    sideSeamUpliftCm: Object.freeze({ min: 1, max: 1.5, sourceRef: HOFENBITZER_SOURCE_REFS.shaping }),
    sideHipShapeAdjustmentCm: Object.freeze({ min: -1.5, max: 1.5, sourceRef: HOFENBITZER_SOURCE_REFS.shaping }),
    frontDartIntakeCm: Object.freeze({ min: 0, max: 2.5, sourceRef: HOFENBITZER_SOURCE_REFS.shaping }),
    frontDartLengthCm: Object.freeze({ min: 8, max: 10, sourceRef: HOFENBITZER_SOURCE_REFS.shaping }),
    frontDartUpliftCm: Object.freeze({ min: 0.5, max: 0.7, sourceRef: HOFENBITZER_SOURCE_REFS.shaping }),
    backDartLength1Cm: Object.freeze({ min: 13, max: 16, sourceRef: HOFENBITZER_SOURCE_REFS.shaping }),
    backDartLength2Cm: Object.freeze({ min: 12, max: 14, sourceRef: HOFENBITZER_SOURCE_REFS.twoBackDarts }),
    backDartUpliftCm: Object.freeze({ min: 0.3, max: 0.5, sourceRef: HOFENBITZER_SOURCE_REFS.shaping }),
    secondBackDartUpliftCm: Object.freeze({ min: 0.5, max: 0.7, sourceRef: HOFENBITZER_SOURCE_REFS.twoBackDarts }),
    backDartDifferenceCm: Object.freeze({ min: 0.5, max: 1, sourceRef: HOFENBITZER_SOURCE_REFS.twoBackDarts }),
    backDartPositionOffsetCm: Object.freeze({ min: 0, max: 1, sourceRef: HOFENBITZER_SOURCE_REFS.twoBackDarts }),
    waistbandWidthCm: Object.freeze({ min: 2, max: 5, sourceRef: HOFENBITZER_SOURCE_REFS.waistband }),
    overlapCm: Object.freeze({ min: 0, max: 8, allowZero: true, sourceRef: HOFENBITZER_SOURCE_REFS.waistband }),
    seamAllowanceCm: Object.freeze({ min: 1, max: 3, allowZero: true, sourceRef: HOFENBITZER_SOURCE_REFS.production }),
    hemAllowanceCm: Object.freeze({ min: 2, max: 5, allowZero: true, sourceRef: HOFENBITZER_SOURCE_REFS.production }),
    centerBackAllowanceCm: Object.freeze({ min: 1, max: 3, allowZero: true, sourceRef: HOFENBITZER_SOURCE_REFS.production })
  }),
  inputDefaults: Object.freeze({
    ...sampleMeasurements,
    ...constructionParameters,
    ...allowances,
    overlapCm: 4
  })
});
