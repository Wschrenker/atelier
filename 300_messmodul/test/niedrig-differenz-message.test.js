import test from "node:test";
import assert from "node:assert/strict";

import {
  NIEDRIG_DIFFERENZ_CODE,
  formatNiedrigDifferenzMessage
} from "../src/ui/niedrig-differenz-message.js";

const MUNKHUU_DETAIL = Object.freeze({
  hipWaistDifferenceMm: 20,
  requiredHipWaistDifferenceExclusiveMm: 90,
  waistSuppressionMm: 15,
  requiredWaistSuppressionExclusiveMm: 50,
  sideHipIntakeMm: 7.5,
  frontDartIntakeMm: 25,
  backDartTotalIntakeMm: -17.5
});

test("formatter: Munkhuu detail produces the exact German message with decimal commas", () => {
  assert.equal(
    formatNiedrigDifferenzMessage(MUNKHUU_DETAIL),
    "Kein Schnitt erzeugt: Diese Hofenbitzer-Rockmethode deckt die geringe "
      + "Taille-Hüft-Differenz nicht ab. Gemessen: 2,0 cm. Mit den gewählten "
      + "Zugaben und Abnähern sind mehr als 9,0 cm erforderlich. Die Geometrie "
      + "für diesen Figurfall wird erst nach der realen Rock-Toile festgelegt."
  );
});

test("formatter: uses ONLY the transported detail, no threshold recomputation", () => {
  // Vollstaendiger Sieben-Feld-Vertrag mit absichtlich „unmoeglichen“
  // Anzeige-Werten: der Formatter muss sie unveraendert zeigen, statt aus den
  // uebrigen Feldern selbst zu rechnen.
  const text = formatNiedrigDifferenzMessage({
    hipWaistDifferenceMm: 33,
    requiredHipWaistDifferenceExclusiveMm: 77,
    waistSuppressionMm: 15,
    requiredWaistSuppressionExclusiveMm: 50,
    sideHipIntakeMm: 7.5,
    frontDartIntakeMm: 25,
    backDartTotalIntakeMm: -17.5
  });
  assert.match(text, /Gemessen: 3,3 cm\./);
  assert.match(text, /mehr als 7,7 cm erforderlich/);
});

test("formatter: every one of the seven mandatory fields is individually enforced", () => {
  const felder = [
    "hipWaistDifferenceMm",
    "requiredHipWaistDifferenceExclusiveMm",
    "waistSuppressionMm",
    "requiredWaistSuppressionExclusiveMm",
    "sideHipIntakeMm",
    "frontDartIntakeMm",
    "backDartTotalIntakeMm"
  ];
  for (const feld of felder) {
    const fehlend = { ...MUNKHUU_DETAIL };
    delete fehlend[feld];
    const kaputte = [
      fehlend,
      { ...MUNKHUU_DETAIL, [feld]: Number.NaN },
      { ...MUNKHUU_DETAIL, [feld]: Infinity }
    ];
    for (const detail of kaputte) {
      let result;
      assert.doesNotThrow(() => {
        result = formatNiedrigDifferenzMessage(detail);
      }, `${feld} case must not throw`);
      assert.equal(result, null, `${feld} case must return null`);
    }
  }
});

test("formatter: an explicit 6-of-7 contract returns null", () => {
  // backDartTotalIntakeMm fehlt: Teilobjekt = Beschaedigung oder Versionsdrift.
  const sechsVonSieben = {
    hipWaistDifferenceMm: 20,
    requiredHipWaistDifferenceExclusiveMm: 90,
    waistSuppressionMm: 15,
    requiredWaistSuppressionExclusiveMm: 50,
    sideHipIntakeMm: 7.5,
    frontDartIntakeMm: 25
  };
  assert.equal(formatNiedrigDifferenzMessage(sechsVonSieben), null);
});

test("formatter: German decimal comma, never a dot", () => {
  const text = formatNiedrigDifferenzMessage(MUNKHUU_DETAIL);
  assert.equal(/\d\.\d/.test(text), false);
  assert.match(text, /2,0 cm/);
  assert.match(text, /mehr als 9,0 cm/);
});

test("formatter: damaged or incomplete detail returns null without throwing", () => {
  const damaged = [
    undefined,
    null,
    "kaputt",
    42,
    {},
    { hipWaistDifferenceMm: 20 },
    { requiredHipWaistDifferenceExclusiveMm: 90 },
    { hipWaistDifferenceMm: "20", requiredHipWaistDifferenceExclusiveMm: 90 },
    { hipWaistDifferenceMm: Number.NaN, requiredHipWaistDifferenceExclusiveMm: 90 },
    { hipWaistDifferenceMm: 20, requiredHipWaistDifferenceExclusiveMm: Infinity }
  ];
  for (const detail of damaged) {
    let result;
    assert.doesNotThrow(() => {
      result = formatNiedrigDifferenzMessage(detail);
    });
    assert.equal(result, null);
  }
});

test("formatter: exports the stable code constant used by the UI branch", () => {
  assert.equal(NIEDRIG_DIFFERENZ_CODE, "NIEDRIG_DIFFERENZ");
});
