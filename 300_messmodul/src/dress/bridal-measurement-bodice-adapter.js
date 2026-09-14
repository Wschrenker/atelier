// KANONISCHER Profil->Bodice-Adapter: Braut-Masssatz (aus Messmodul/Braut-Profil)
// -> Engine-Input fuer draftBodiceBlock (src/drafting/bodice-block.js)
//    + Kleid-Abnaeher-Optionen (passformklasse, Abnaeher-Laengen).
//
// Dies ist die eine oeffentliche fachliche Wahrheit fuer Profil->Bodice-Input.
// Die S.19-Laengenmasse (HlB, BrT, VL) kommen aus der geteilten Ableitung
// s19-length-derivations.js — kein Formelsatz wird hier dupliziert.
//
// Messung -> Bodice-Block-Input:
//  - body_height                        -> koeHCm
//  - bust_circumference                 -> brustUmfangCm
//  - waist_circumference_horizontal     -> taillenUmfangCm
//  - hip_circumference_horizontal       -> hueftUmfangCm
//  - armhole_depth                      -> armlochtiefeCm
//  - waist_to_hip                       -> huefttiefeCm (echtes Koerpermass, S.20-31; KEIN Default 21)
//  - neck_base_circumference            -> halslochbreiteCm = HaU/6 + 0,5 (S.19)
//  - measured_bust_depth_{right,left}   -> brusttiefeCm = Ø(gBrT) - HlB (S.19)
//  - measured_front_length_{right,left} -> vorderlaengeCm = Ø(gVL) - HlB + Schraeglage (S.19)
//  - measured_back_width                -> rueckenbreiteHalbCm = gRueB / 2
//  - shoulder_width_{right,left}        -> schulterbreiteCm (Mittelwert)
//  - shoulder_angle_{right,left}        -> schulterwinkelGrad (Minimum der Seiten)
//  - measured_back_length               -> rueckenlaengeCm
//
// BREITENSTRATEGIE (S.14, transparent, Rohmessung bleibt unangetastet):
//  - "direkt" (Default): armdurchmesserCm = Ø(gArD), brustbreiteHalbCm = gBrB/2.
//  - "quellenformel" (S.14 roter Kasten "Alternative Bestimmung von RueB, ArD und BrB"):
//      ArD = Ø(OaU) * 0,6 - 7,5  ·  BrB = BrU/2 - RueB - ArD.
//    Fuer haeufige Messprobleme bei gArD/gBrB. Die direkten Rohwerte werden NICHT
//    ueberschrieben; beide Kontrollen stehen auditierbar in result.widthDerivation.
//
// BALANCE-GATE (S.17-18/S.174-178, vor produktiver Geometrie):
//  - |(VL - RueL) - optimale Balance(BrU)| > 1 cm -> typisierter Stopp
//    code BALANCE_REQUIRES_FIGURE_ANALYSIS mit allen Diagnosewerten.
//  - Keine Autokorrektur. PRODUKTIV zulaessig ist ausschliesslich eine explizite
//    balanceEntscheidung mit quelle "figuranalyse" (reale Figurbeobachtung nach
//    S.17-18); sie passt NUR die abgeleiteten Konstruktionslaengen deklariert an,
//    wird im Ergebnis dokumentiert und aendert nie Rohwerte.
//  - quelle "testentscheidung" ist produktiv UNZULAESSIG und stoppt strukturiert:
//    synthetische Geometrie gehoert in Test-Fixtures, nicht in den Adapter.
//
// STOPP STATT RATEN:
//  - Fehlt ein erforderliches Koerpermass -> missing[]
//  - modellLaengeCm + passformklasse kommen AUSSCHLIESSLICH aus config; fehlt -> Stopp
//    (kein stiller PK3-Default im Adapter)
//  - Berechnete BrT/VL/ArD/BrB muessen endlich und positiv sein, sonst strukturierter Stopp

import {
  deriveS19ConstructionLengths,
  TAILLENSCHRAEGLAGE_DEFAULT_ADVISORY
} from "./s19-length-derivations.js";
import { isValidPassformklasse } from "./passformklasse.js";
import { optimalBalanceCm } from "../drafting/bodice-block.js";

// Unilaterale Messwerte (direkt 1:1)
export const BODICE_BODY_MEASUREMENT_MAP = Object.freeze({
  koeHCm: "body_height",
  brustUmfangCm: "bust_circumference",
  taillenUmfangCm: "waist_circumference_horizontal",
  hueftUmfangCm: "hip_circumference_horizontal",
  armlochtiefeCm: "armhole_depth",
  huefttiefeCm: "waist_to_hip",
  rueckenlaengeCm: "measured_back_length"
});

export const WIDTH_STRATEGIES = Object.freeze(["direkt", "quellenformel"]);
export const BALANCE_TOLERANCE_CM = 1;
const BALANCE_EPSILON = 1e-9;

// KANONISCHES Schema der Balance-Entscheidung (eine Wahrheit fuer Adapter, Store
// und CLI — kein zweiter Validator). Produktiv zulaessig ist NUR "figuranalyse";
// "testentscheidung" ist strukturell gueltig (Fixtures), stoppt aber im Adapter.
export const BALANCE_ENTSCHEIDUNG_QUELLEN = Object.freeze(["figuranalyse", "testentscheidung"]);
export const BALANCE_ENTSCHEIDUNG_ZIELE = Object.freeze(["vorderlaengeCm", "rueckenlaengeCm"]);

// Strukturelle Gueltigkeit: nachvollziehbare Zielgroesse (ziel, Einheit cm im
// Feldnamen), endliche Korrektur (deltaCm) und nichtleere Begruendung.
export function isValidBalanceEntscheidungStruktur(entscheidung) {
  return entscheidung !== null
    && typeof entscheidung === "object"
    && !Array.isArray(entscheidung)
    && BALANCE_ENTSCHEIDUNG_QUELLEN.includes(entscheidung.quelle)
    && BALANCE_ENTSCHEIDUNG_ZIELE.includes(entscheidung.ziel)
    && Number.isFinite(entscheidung.deltaCm)
    && typeof entscheidung.begruendung === "string"
    && entscheidung.begruendung.trim().length > 0;
}

// Bilaterale Messwerte, die im Adapter selbst gemittelt/minimiert werden.
// BrT/VL sind NICHT hier — sie kommen aus der geteilten S.19-Ableitung.
const BODICE_BILATERAL_MEASUREMENTS = Object.freeze({
  schulterbreiteCm: ["shoulder_width_right", "shoulder_width_left"],
  schulterwinkelGrad: ["shoulder_angle_right", "shoulder_angle_left"] // MIN
});

function finiteValue(values, id) {
  return Number.isFinite(values?.[id]) ? values[id] : undefined;
}

function average(values) {
  const finite = values.filter(v => Number.isFinite(v));
  if (finite.length === 0) return undefined;
  return finite.reduce((sum, v) => sum + v, 0) / finite.length;
}

// S.14 roter Kasten: ArD = OaU * 0,6 - 7,5 (sicherere Alternative zu gArD).
export function armDiameterFromUpperArm(oaUCm) {
  return Number.isFinite(oaUCm) ? oaUCm * 0.6 - 7.5 : undefined;
}

// Beide Breiten-Kontrollen auditierbar rechnen (Rohwerte unangetastet):
//  - direkt:        gRueB + gBrB + 2*Ø(gArD) gegen BrU (S.14 ❑6/❑7)
//  - quellenformel: RueB + ArD(OaU) + BrB(Formel) = BrU/2 per Konstruktion
export function deriveWidthControls(values = {}) {
  const gRueB = finiteValue(values, "measured_back_width");
  const gBrB = finiteValue(values, "measured_bust_width");
  const gArD = average([
    finiteValue(values, "measured_arm_diameter_right"),
    finiteValue(values, "measured_arm_diameter_left")
  ]);
  const brU = finiteValue(values, "bust_circumference");
  const oaU = average([
    finiteValue(values, "upper_arm_circumference_right"),
    finiteValue(values, "upper_arm_circumference_left")
  ]);

  const direkt = (gRueB !== undefined && gBrB !== undefined && gArD !== undefined && brU !== undefined)
    ? (() => {
      const sumCm = gRueB + gBrB + 2 * gArD;
      return Object.freeze({
        rueckenbreiteHalbCm: gRueB / 2,
        armdurchmesserCm: gArD,
        brustbreiteHalbCm: gBrB / 2,
        summeDirektmasseCm: sumCm,
        brUCm: brU,
        deltaCm: sumCm - brU
      });
    })()
    : undefined;

  const arDBerechnet = armDiameterFromUpperArm(oaU);
  const quellenformel = (gRueB !== undefined && brU !== undefined && arDBerechnet !== undefined)
    ? (() => {
      const rueB = gRueB / 2;
      const brB = brU / 2 - rueB - arDBerechnet;
      return Object.freeze({
        oaUMittelCm: oaU,
        rueckenbreiteHalbCm: rueB,
        armdurchmesserCm: arDBerechnet,
        brustbreiteHalbCm: brB,
        kontrolleSummeCm: rueB + arDBerechnet + brB, // = BrU/2 per Konstruktion
        halberBrUCm: brU / 2,
        abweichungGArDCm: gArD !== undefined ? gArD - arDBerechnet : undefined,
        abweichungGBrBCm: gBrB !== undefined ? gBrB / 2 - brB : undefined
      });
    })()
    : undefined;

  return { direkt, quellenformel };
}

/**
 * Bildet einen Braut-Masssatz (Messmodul-Profile) auf Bodice-Block-Input ab.
 * Rein, ohne Seiteneffekt, ohne throw.
 *
 * @param {Record<string, number>} values  Mess-id -> Zahl (z.B. aus coerceMeasurementValues)
 * @param {{
 *   modellLaengeCm?: number,
 *   passformklasse?: number,
 *   breitenStrategie?: "direkt"|"quellenformel",
 *   balanceEntscheidung?: { quelle: "figuranalyse", ziel: "vorderlaengeCm"|"rueckenlaengeCm", deltaCm: number, begruendung: string },
 *   shAblLaengeCm?: number, hAblLaengeCm?: number, [k: string]: unknown
 * }} config  Design/Konfiguration
 * @returns {{ ok: true, input: object, advisories: string[], widthDerivation: object, balance: object }
 *          | { ok: false, missing: string[], reason: string, code?: string, balance?: object, advisories: string[] }}
 */
export function bridalValuesToBodiceInput(values = {}, config = {}) {
  const missing = [];
  const advisories = [];
  const body = {};

  // Breitenstrategie: transparent, Default = bisheriges Verhalten ("direkt").
  const breitenStrategie = config.breitenStrategie ?? "direkt";
  if (!WIDTH_STRATEGIES.includes(breitenStrategie)) {
    return Object.freeze({
      ok: false,
      missing: Object.freeze([`config.breitenStrategie (ungueltig: ${breitenStrategie}, erlaubt ${WIDTH_STRATEGIES.join("/")})`]),
      reason: "Unbekannte Breitenstrategie — Adapter stoppt statt zu raten.",
      advisories: Object.freeze(advisories)
    });
  }

  // Geteilte S.19-Ableitung (HlB, BrT, VL) — einzige Formelquelle.
  const s19 = deriveS19ConstructionLengths(values);
  if (s19.taillenschraeglageDefaulted) advisories.push(TAILLENSCHRAEGLAGE_DEFAULT_ADVISORY);

  // Unilaterale Messungen
  for (const [engineKey, measurementId] of Object.entries(BODICE_BODY_MEASUREMENT_MAP)) {
    const value = finiteValue(values, measurementId);
    if (value === undefined) {
      missing.push(measurementId);
    } else {
      body[engineKey] = value;
    }
  }

  // Bilaterale Messungen (Durchschnitt bzw. Minimum)
  for (const [engineKey, [rightId, leftId]] of Object.entries(BODICE_BILATERAL_MEASUREMENTS)) {
    const right = finiteValue(values, rightId);
    const left = finiteValue(values, leftId);

    if (right === undefined && left === undefined) {
      missing.push(`${rightId} or ${leftId}`);
    } else if (engineKey === "schulterwinkelGrad") {
      // Schulterwinkel: MINIMUM verwenden (engste Schulter)
      body[engineKey] = right !== undefined && left !== undefined
        ? Math.min(right, left)
        : (right !== undefined ? right : left);
    } else {
      body[engineKey] = average([right, left]);
    }
  }

  // Breiten: gRueB halbiert der Adapter immer selbst (S.14); ArD/BrB je Strategie.
  const widthDerivation = deriveWidthControls(values);
  const gRueckenbreite = finiteValue(values, "measured_back_width");
  if (gRueckenbreite === undefined) {
    missing.push("measured_back_width");
  } else {
    body.rueckenbreiteHalbCm = gRueckenbreite / 2;
  }

  if (breitenStrategie === "direkt") {
    const gArD = average([
      finiteValue(values, "measured_arm_diameter_right"),
      finiteValue(values, "measured_arm_diameter_left")
    ]);
    if (gArD === undefined) {
      missing.push("measured_arm_diameter_right or measured_arm_diameter_left");
    } else {
      body.armdurchmesserCm = gArD;
    }
    const gBrustbreite = finiteValue(values, "measured_bust_width");
    if (gBrustbreite === undefined) {
      missing.push("measured_bust_width");
    } else {
      body.brustbreiteHalbCm = gBrustbreite / 2;
    }
  } else {
    // "quellenformel" (S.14): braucht OaU (mind. eine Seite) + BrU + gRueB.
    if (widthDerivation.quellenformel === undefined) {
      const oaU = average([
        finiteValue(values, "upper_arm_circumference_right"),
        finiteValue(values, "upper_arm_circumference_left")
      ]);
      if (oaU === undefined) missing.push("upper_arm_circumference_right or upper_arm_circumference_left");
      // bust_circumference / measured_back_width sind oben bereits als missing erfasst.
    } else {
      body.armdurchmesserCm = widthDerivation.quellenformel.armdurchmesserCm;
      body.brustbreiteHalbCm = widthDerivation.quellenformel.brustbreiteHalbCm;
    }
  }

  // S.19-Laengenmasse: erforderliche Rohmasse pruefen (HaU, gBrT, gVL).
  if (s19.halsansatzUmfangCm === undefined) missing.push("neck_base_circumference");
  if (s19.gemesseneBrusttiefeCm === undefined) {
    missing.push("measured_bust_depth_right or measured_bust_depth_left");
  }
  if (s19.gemesseneVorderlaengeCm === undefined) {
    missing.push("measured_front_length_right or measured_front_length_left");
  }

  // modellLaengeCm + passformklasse: ERFORDERLICH aus Config (kein stiller Default).
  const modellLaengeCm = Number.isFinite(config.modellLaengeCm) ? config.modellLaengeCm : undefined;
  if (modellLaengeCm === undefined) missing.push("config.modellLaengeCm");

  const passformklasse = Number.isFinite(config.passformklasse) ? config.passformklasse : undefined;
  if (passformklasse === undefined) {
    missing.push("config.passformklasse");
  } else if (!isValidPassformklasse(passformklasse)) {
    // Vorhanden, aber ausserhalb 3/4/5 -> ehrlicher Stopp (wie Kleid/CLI/Store).
    missing.push(`config.passformklasse (ungueltig: ${passformklasse}, erlaubt 3/4/5)`);
  }

  if (missing.length > 0) {
    return Object.freeze({
      ok: false,
      missing: Object.freeze(missing),
      reason: "Fehlende Koerpermasse/Modelllaenge oder fehlende/ungueltige Passformklasse — Adapter stoppt statt zu raten.",
      advisories: Object.freeze(advisories)
    });
  }

  // Alle Rohmasse da -> S.19-Konstruktionswerte uebernehmen.
  body.halslochbreiteCm = s19.halslochbreiteCm;
  body.brusttiefeCm = s19.brusttiefeCm;
  body.vorderlaengeCm = s19.vorderlaengeCm;

  // Berechnete Konstruktionsmasse muessen endlich und positiv sein (sonst ehrlicher Stopp).
  const notPositive = (name, value) => !(Number.isFinite(value) && value > 0)
    ? `derived:${name} (nicht endlich/positiv: ${value})`
    : undefined;
  const derivedProblems = [
    notPositive("brusttiefeCm", body.brusttiefeCm),
    notPositive("vorderlaengeCm", body.vorderlaengeCm),
    notPositive("armdurchmesserCm", body.armdurchmesserCm),
    notPositive("brustbreiteHalbCm", body.brustbreiteHalbCm)
  ].filter(Boolean);
  if (derivedProblems.length > 0) {
    return Object.freeze({
      ok: false,
      missing: Object.freeze(derivedProblems),
      reason: "Berechnete Konstruktionsmasse nicht endlich/positiv — Masssatz unplausibel, Adapter stoppt.",
      advisories: Object.freeze(advisories)
    });
  }

  // ---- Balance-Gate (S.17-18 Figurbeobachtung; Tabelle S.174/178) ----
  // Individuelle Balance = VL - RueL; ausserhalb ±1 cm um die optimale Balance
  // stoppt der Adapter typisiert. KEINE Autokorrektur, kein Raten VL vs. RueL.
  // Audit: Rohwerte VOR jeder Entscheidung festhalten (Rohbalance != korrigierte
  // Balance muss in Export-/Auditmetadaten unterscheidbar sein).
  const rohVorderlaengeCm = body.vorderlaengeCm;
  const rohRueckenlaengeCm = body.rueckenlaengeCm;
  let balanceEntscheidungApplied;
  const entscheidung = config.balanceEntscheidung;
  if (entscheidung !== undefined) {
    // Produktiv unzulaessige Quelle zuerst: testentscheidung stoppt strukturiert.
    if (entscheidung !== null && typeof entscheidung === "object" && entscheidung.quelle === "testentscheidung") {
      return Object.freeze({
        ok: false,
        code: "BALANCE_TESTENTSCHEIDUNG_NOT_PRODUCTION",
        missing: Object.freeze(["config.balanceEntscheidung.quelle (testentscheidung ist produktiv unzulaessig; nur figuranalyse)"]),
        reason: "Eine Testentscheidung darf nie zur produktiven Balance-Korrektur werden — synthetische Geometrie gehoert in Test-Fixtures, nicht in den Adapter.",
        advisories: Object.freeze(advisories)
      });
    }
    // Kanonischer Struktur-Validator + produktives Quelle-Gate (nur figuranalyse).
    const valid = isValidBalanceEntscheidungStruktur(entscheidung)
      && entscheidung.quelle === "figuranalyse";
    if (!valid) {
      return Object.freeze({
        ok: false,
        missing: Object.freeze(["config.balanceEntscheidung (quelle figuranalyse, ziel vorderlaengeCm/rueckenlaengeCm, deltaCm, begruendung erforderlich)"]),
        reason: "Balance-Entscheidung unvollstaendig — Adapter stoppt statt zu raten.",
        advisories: Object.freeze(advisories)
      });
    }
    // Deklarierte Anpassung NUR am abgeleiteten Konstruktionsmass (nie am Rohwert).
    body[entscheidung.ziel] = body[entscheidung.ziel] + entscheidung.deltaCm;
    balanceEntscheidungApplied = Object.freeze({
      quelle: entscheidung.quelle,
      ziel: entscheidung.ziel,
      deltaCm: entscheidung.deltaCm,
      begruendung: entscheidung.begruendung
    });
    advisories.push(`BALANCE_ENTSCHEIDUNG_${entscheidung.quelle.toUpperCase()}`);
  }

  let balance;
  if (body.brustUmfangCm >= 80 && body.brustUmfangCm <= 150) {
    const optimal = optimalBalanceCm(body.brustUmfangCm);
    const individuell = body.vorderlaengeCm - body.rueckenlaengeCm;
    const abweichung = individuell - optimal;
    const rohIndividuell = rohVorderlaengeCm - rohRueckenlaengeCm;
    balance = Object.freeze({
      // Effektive (ggf. korrigierte) Balance — Grundlage des Gates:
      vorderlaengeCm: body.vorderlaengeCm,
      rueckenlaengeCm: body.rueckenlaengeCm,
      individuelleBalanceCm: individuell,
      optimaleBalanceCm: optimal,
      abweichungCm: abweichung,
      toleranzCm: BALANCE_TOLERANCE_CM,
      withinTolerance: Math.abs(abweichung) <= BALANCE_TOLERANCE_CM + BALANCE_EPSILON,
      // Audit: Rohbalance (abgeleitet aus unveraenderten Rohmessungen, VOR Korrektur):
      roh: Object.freeze({
        vorderlaengeCm: rohVorderlaengeCm,
        rueckenlaengeCm: rohRueckenlaengeCm,
        individuelleBalanceCm: rohIndividuell,
        abweichungCm: rohIndividuell - optimal
      }),
      // Audit: Korrektur mit Quelle und Begruendung (nur wenn angewendet):
      ...(balanceEntscheidungApplied ? { entscheidung: balanceEntscheidungApplied } : {})
    });
    if (!balance.withinTolerance) {
      return Object.freeze({
        ok: false,
        code: "BALANCE_REQUIRES_FIGURE_ANALYSIS",
        missing: Object.freeze([]),
        reason: "Balance ausserhalb ±1 cm — explizite Figuranalyse/Korrekturentscheidung erforderlich, keine Autokorrektur (S.17-18).",
        balance,
        advisories: Object.freeze(advisories)
      });
    }
  }
  // BrU ausserhalb 80-150: Balance-Tabelle nicht anwendbar; draftBodiceBlock stoppt dort ehrlich.

  // Abnaeher-Optionen: passformklasse ist Pflicht (oben geprueft), Laengen optional.
  const options = {
    passformklasse,
    shAblLaengeCm: config.shAblLaengeCm, // undefined -> METHOD.engineDefaults (im fitted-bodice)
    hAblLaengeCm: config.hAblLaengeCm     // undefined -> METHOD.engineDefaults (im fitted-bodice)
  };

  return Object.freeze({
    ok: true,
    input: Object.freeze({ ...config, ...body, ...options }),
    advisories: Object.freeze(advisories),
    widthDerivation: Object.freeze({ strategie: breitenStrategie, ...widthDerivation }),
    balance
  });
}
