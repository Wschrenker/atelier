const TRANSCRIPTION = "hofenbitzer/band_1/transkription/s172-187_oberteil-grundgeruest_ENTWURF.md";

export const HOFENBITZER_BODICE_SOURCE_REFS = Object.freeze({
  balance: `${TRANSCRIPTION}#4-balance-logik`,
  table: `${TRANSCRIPTION}#3-konstruktionstabelle-logik`,
  firstLines: `${TRANSCRIPTION}#-erste-linien-und-hintere-mitte`,
  widthLines: `${TRANSCRIPTION}#-brustweite-arm--und-seitenlinien-sowie-vordere-mitte`,
  backNeckShoulder: `${TRANSCRIPTION}#-hinteres-halsloch-und-schulter`,
  frontNeck: `${TRANSCRIPTION}#-vorderes-halsloch-und-brustabnäher-linie`,
  frontShoulder: `${TRANSCRIPTION}#-vordere-schulter`,
  referenceCase: `${TRANSCRIPTION}#pk4--primärer-rechnerisch-in-sich-stimmiger-referenzsatz`
});

export const HOFENBITZER_BODICE_RULE_REFS = Object.freeze({
  breastWidth: "HB1-S176-178-BRW",
  waistWidth: "HB1-S176-178-TAW",
  hipWidth: "HB1-S176-178-HUEW",
  armholeDepth: "HB1-S178-AITPLUS",
  backWidth: "HB1-S176-180-RUEBPLUS",
  armDiameter: "HB1-S176-181-ARDPLUS",
  breastBreadth: "HB1-S176-181-BRBPLUS",
  shoulderLength: "HB1-S177-181-SUNL",
  backShoulderLength: "HB1-S177-181-HSUNL",
  balance: "HB1-S174-178-BALANCE",
  firstLines: "HB1-S179-SCHRITTE-1-9",
  widthLines: "HB1-S180-SCHRITTE-10-14",
  breastWidthCheck: "HB1-S180-BRW-KONTROLLE",
  backNeckShoulder: "HB1-S181-SCHRITTE-15-18",
  frontNeck: "HB1-S181-SCHRITTE-19-23",
  frontShoulder: "HB1-S181-SCHRITT-24",
  productionAllowances: "HB1-OBERTEIL-PRODUKTIONSZUGABEN"
});

const sampleMeasurements = Object.freeze({
  koeHCm: 168,
  brustUmfangCm: 88,
  taillenUmfangCm: 72,
  hueftUmfangCm: 97,
  armlochtiefeCm: 20.1,
  huefttiefeCm: 21,
  brusttiefeCm: 28.1,
  modellLaengeCm: 95,
  halslochbreiteCm: 6.5,
  rueckenbreiteHalbCm: 16.5,
  armdurchmesserCm: 9.3,
  brustbreiteHalbCm: 18.2,
  schulterbreiteCm: 12.2,
  schulterwinkelGrad: 20,
  rueckenlaengeCm: 41.6,
  vorderlaengeCm: 45.3
});

const constructionParameters = Object.freeze({
  brustZugabeCm: 8,
  taillenZugabeCm: 6,
  hueftZugabeCm: 4,
  armlochtiefeZugabeCm: 1.7,
  rueckenbreiteZugabeCm: 0.8,
  armdurchmesserZugabeCm: 2,
  brustbreiteZugabeCm: 1.2,
  schulterbreiteZugabeCm: 0.4,
  hintereSchulterEinhalteweiteCm: 0.7,
  seitenlinienAbstandCm: 8.5,
  hintereMitteVersatzCm: 2,
  brustweitenToleranzCm: 0.01
});

const allowancesMm = Object.freeze({
  seam: 10,
  hem: 30,
  centerBack: 10
});

export const HOFENBITZER_BAND1_BODICE_METHOD = Object.freeze({
  id: "hofenbitzer-band1-bodice-block",
  version: "1.0.0",
  status: "source-approved",
  source: "Guido Hofenbitzer, Grundschnitte und Modellentwicklungen, Band 1, 3. Auflage 2024, S. 172-181.",
  pageReferences: Object.freeze(["Hofenbitzer Band 1 (2024), S. 172-181"]),
  sourceRefs: Object.freeze(Object.values(HOFENBITZER_BODICE_SOURCE_REFS)),
  sampleMeasurements,
  constructionParameters,
  allowancesMm,
  referenceCase: Object.freeze({
    name: "Hofenbitzer Band 1, PK4, Groesse 38",
    expectedCm: Object.freeze({
      breastWidth: 96,
      halfBreastWidth: 48,
      waistWidth: 78,
      halfWaistWidth: 39,
      hipWidth: 101,
      halfHipWidth: 50.5,
      armholeDepthPlus: 21.8,
      backWidthPlus: 17.3,
      armDiameterPlus: 11.3,
      breastBreadthPlus: 19.4,
      shoulderSeamLength: 12.6,
      backShoulderSeamLength: 13.3,
      optimalBalance: 3.5
    }),
    sourceRefs: Object.freeze([
      HOFENBITZER_BODICE_SOURCE_REFS.referenceCase,
      HOFENBITZER_BODICE_SOURCE_REFS.table
    ])
  }),
  validationRules: Object.freeze({
    requiredMeasurements: Object.freeze(Object.keys(sampleMeasurements)),
    positiveParameters: Object.freeze(Object.keys(constructionParameters).filter((key) => (
      key !== "hintereMitteVersatzCm"
    ))),
    shoulderAngle: Object.freeze({ minExclusive: 2, maxExclusive: 88 }),
    backShoulderEase: Object.freeze({ min: 0.5, max: 1 }),
    sideLineGap: Object.freeze({ min: 7, max: 10 })
  }),
  inputDefaults: Object.freeze({
    ...constructionParameters,
    allowancesMm
  })
});
