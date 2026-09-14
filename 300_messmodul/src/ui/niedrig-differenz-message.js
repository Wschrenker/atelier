// #24: Pure, headless testbare Formatierung der NIEDRIG_DIFFERENZ-Meldung.
// Erhält AUSSCHLIESSLICH error.detail der Engine/API — keine eigene
// Grenzberechnung, keine DOM-Abhängigkeit.
//
// Liefert bei beschädigtem oder unvollständigem detail `null`, damit der
// Aufrufer (app.js) auf den generischen Fehlerpfad zurückfallen kann,
// statt erneut zu werfen.

export const NIEDRIG_DIFFERENZ_CODE = "NIEDRIG_DIFFERENZ";

// Der eingefrorene Engine-/API-Vertrag umfasst genau diese sieben Pflichtfelder.
// Ein Teilobjekt bedeutet Beschädigung oder Versionsdrift -> null.
const PFLICHTFELDER = Object.freeze([
  "hipWaistDifferenceMm",
  "requiredHipWaistDifferenceExclusiveMm",
  "waistSuppressionMm",
  "requiredWaistSuppressionExclusiveMm",
  "sideHipIntakeMm",
  "frontDartIntakeMm",
  "backDartTotalIntakeMm"
]);

function mmAlsCmText(mm) {
  // Millimeter -> Zentimeter mit einer Nachkommastelle und deutschem Dezimalkomma.
  return (mm / 10).toFixed(1).replace(".", ",");
}

export function formatNiedrigDifferenzMessage(detail) {
  if (!detail || typeof detail !== "object") return null;
  if (!PFLICHTFELDER.every((feld) => Number.isFinite(detail[feld]))) return null;
  // Sichtbar werden weiterhin NUR die zwei transportierten Anzeige-Felder;
  // keine Schwelle wird im UI neu berechnet.
  const gemessenMm = detail.hipWaistDifferenceMm;
  const erforderlichMm = detail.requiredHipWaistDifferenceExclusiveMm;

  return "Kein Schnitt erzeugt: Diese Hofenbitzer-Rockmethode deckt die geringe "
    + "Taille-Hüft-Differenz nicht ab. "
    + `Gemessen: ${mmAlsCmText(gemessenMm)} cm. `
    + "Mit den gewählten Zugaben und Abnähern sind mehr als "
    + `${mmAlsCmText(erforderlichMm)} cm erforderlich. `
    + "Die Geometrie für diesen Figurfall wird erst nach der realen Rock-Toile festgelegt.";
}
