import { randomBytes } from "node:crypto";
import { mkdir, readFile, readdir, rename, unlink, writeFile } from "node:fs/promises";
import path from "node:path";
import { BRIDAL_BODY_MEASUREMENTS } from "../measurements/bridal-body-measurements.js";
import { BRIDAL_SHAPE_IDS } from "./shapes.js";
import { isValidPassformklasse } from "../dress/passformklasse.js";
import { isValidBalanceEntscheidungStruktur } from "../dress/bridal-measurement-bodice-adapter.js";

const BRIDE_ID_PATTERN = /^[a-z0-9-]+$/;
const measurementIds = new Set(BRIDAL_BODY_MEASUREMENTS.map((measurement) => measurement.id));

// Taillenschraeglage vorne ist ein FIGUR-BEOBACHTUNGSWERT (kein Messwert), vorzeichenbehaftet
// (Band steigt +, faellt -, waagerecht 0), Default 0, optional persistiert. Fliesst spaeter als
// values.waist_slope_front_cm in den S.19-Adapter (VL = gVL - HlB + Schraeglage). SIGNED: finite,
// NICHT > 0 — die Positiv-Wand der Koerpermasse gilt hier bewusst nicht.
function isValidWaistSlopeFront(value) {
  return Number.isFinite(Number(value));
}

function validateBrideId(id) {
  if (typeof id !== "string" || !BRIDE_ID_PATTERN.test(id)) {
    throw new TypeError("Ungültige Braut-ID.");
  }
  return id;
}

function validateBrideInput({
  id,
  name,
  shapeId,
  values,
  notes,
  passformklasse,
  waistSlopeFrontCm,
  balanceEntscheidung
}) {
  if (id !== undefined && id !== null && id !== "") validateBrideId(id);

  const cleanName = typeof name === "string" ? name.trim() : "";
  if (!cleanName) throw new TypeError("Name darf nicht leer sein.");
  if (!BRIDAL_SHAPE_IDS.includes(shapeId)) {
    throw new TypeError(`Unbekannte Grundform: ${shapeId}`);
  }
  if (!values || typeof values !== "object" || Array.isArray(values)) {
    throw new TypeError("Messwerte müssen ein Objekt sein.");
  }
  for (const measurementId of Object.keys(values)) {
    if (!measurementIds.has(measurementId)) {
      throw new TypeError(`Unbekannte Maß-ID: ${measurementId}`);
    }
  }
  if (notes !== undefined && notes !== null && typeof notes !== "string") {
    throw new TypeError("Notizen müssen Text sein.");
  }

  // Passformklasse ist eine DESIGN-Wahl (kein Messwert), optional persistiert.
  // Fehlt sie -> nicht gesetzt (rückwärtskompatibel). Gesetzt -> muss 3/4/5 sein.
  const hasPassformklasse = passformklasse !== undefined && passformklasse !== null && passformklasse !== "";
  const passformklasseValue = hasPassformklasse ? Number(passformklasse) : undefined;
  if (hasPassformklasse && !isValidPassformklasse(passformklasseValue)) {
    throw new TypeError(`Unbekannte Passformklasse: ${passformklasse}`);
  }

  const hasWaistSlopeFront = waistSlopeFrontCm !== undefined && waistSlopeFrontCm !== null && waistSlopeFrontCm !== "";
  const waistSlopeFrontValue = hasWaistSlopeFront ? Number(waistSlopeFrontCm) : undefined;
  if (hasWaistSlopeFront && !isValidWaistSlopeFront(waistSlopeFrontValue)) {
    throw new TypeError(`Ungültige Taillenschräglage vorne: ${waistSlopeFrontCm}`);
  }

  // Balance-Entscheidung ist eine KONSTRUKTIONSENTSCHEIDUNG (kein Messwert),
  // optional persistiert und auditierbar. Die Struktur kommt ausschliesslich aus
  // dem kanonischen Adapter-Schema (kein zweiter Validator). Der produktive Store
  // persistiert davon nur die Quelle "figuranalyse"; "testentscheidung" bleibt
  // allein fuer Adapter-/Fixture-Tests strukturell erkennbar.
  const hasBalanceEntscheidung = balanceEntscheidung !== undefined && balanceEntscheidung !== null;
  if (hasBalanceEntscheidung && !isValidBalanceEntscheidungStruktur(balanceEntscheidung)) {
    throw new TypeError(
      "Ungültige balanceEntscheidung: quelle (figuranalyse/testentscheidung), "
      + "ziel (vorderlaengeCm/rueckenlaengeCm), endliches deltaCm und nichtleere begruendung erforderlich."
    );
  }
  if (hasBalanceEntscheidung && balanceEntscheidung.quelle !== "figuranalyse") {
    throw new TypeError(
      "Ungültige balanceEntscheidung für den produktiven Braut-Store: "
      + "quelle muss figuranalyse sein; testentscheidung wird nicht persistiert."
    );
  }

  return {
    id: id || null,
    name: cleanName,
    shapeId,
    values: { ...values },
    notes: notes || "",
    ...(hasPassformklasse ? { passformklasse: passformklasseValue } : {}),
    ...(hasWaistSlopeFront ? { waistSlopeFrontCm: waistSlopeFrontValue } : {}),
    ...(hasBalanceEntscheidung
      ? {
        balanceEntscheidung: {
          quelle: balanceEntscheidung.quelle,
          ziel: balanceEntscheidung.ziel,
          deltaCm: balanceEntscheidung.deltaCm,
          begruendung: balanceEntscheidung.begruendung
        }
      }
      : {})
  };
}

function slugFor(name) {
  const slug = name
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
  return slug || "braut";
}

function isBrideRecord(record, expectedId) {
  return Boolean(
    record
    && record.schemaVersion === 1
    && record.id === expectedId
    && BRIDE_ID_PATTERN.test(record.id)
    && typeof record.name === "string"
    && BRIDAL_SHAPE_IDS.includes(record.shapeId)
    && record.values
    && typeof record.values === "object"
    && !Array.isArray(record.values)
    && Object.keys(record.values).every((measurementId) => measurementIds.has(measurementId))
    && (record.notes === undefined || typeof record.notes === "string")
    && (record.passformklasse === undefined || isValidPassformklasse(record.passformklasse))
    && (record.waistSlopeFrontCm === undefined || isValidWaistSlopeFront(record.waistSlopeFrontCm))
    && (record.balanceEntscheidung === undefined || (
      isValidBalanceEntscheidungStruktur(record.balanceEntscheidung)
      && record.balanceEntscheidung.quelle === "figuranalyse"
    ))
    && typeof record.createdAt === "string"
    && typeof record.updatedAt === "string"
    && Number.isFinite(Date.parse(record.createdAt))
    && Number.isFinite(Date.parse(record.updatedAt))
  );
}

export function createBrideStore(baseDir) {
  const storageDir = path.resolve(baseDir);
  let lastTimestampMs = 0;

  function bridePath(id) {
    return path.join(storageDir, `${validateBrideId(id)}.json`);
  }

  function nextTimestamp(previousTimestamp) {
    const previousMs = Date.parse(previousTimestamp || "") || 0;
    lastTimestampMs = Math.max(Date.now(), lastTimestampMs + 1, previousMs + 1);
    return new Date(lastTimestampMs).toISOString();
  }

  async function getBride(id) {
    const filePath = bridePath(id);
    try {
      const record = JSON.parse(await readFile(filePath, "utf8"));
      return record;
    } catch (error) {
      if (error.code === "ENOENT") return null;
      throw error;
    }
  }

  async function listBrides() {
    let entries;
    try {
      entries = await readdir(storageDir, { withFileTypes: true });
    } catch (error) {
      if (error.code === "ENOENT") return [];
      throw error;
    }

    const brides = [];
    for (const entry of entries) {
      if (!entry.isFile() || !entry.name.endsWith(".json")) continue;
      const id = entry.name.slice(0, -5);
      if (!BRIDE_ID_PATTERN.test(id)) continue;
      try {
        const record = JSON.parse(await readFile(path.join(storageDir, entry.name), "utf8"));
        if (!isBrideRecord(record, id)) continue;
        brides.push({
          id: record.id,
          name: record.name,
          shapeId: record.shapeId,
          updatedAt: record.updatedAt,
          measurementCount: Object.values(record.values).filter(
            (value) => value !== "" && value !== null && value !== undefined
          ).length
        });
      } catch {
        // Defekte oder fremde Dateien gehören nicht in die Braut-Liste.
      }
    }

    return brides.sort((left, right) => right.updatedAt.localeCompare(left.updatedAt));
  }

  async function saveBride(input) {
    const bride = validateBrideInput(input || {});
    let existing = null;
    let id = bride.id;

    if (id) {
      existing = await getBride(id);
    } else {
      do {
        id = `${slugFor(bride.name)}-${randomBytes(3).toString("hex")}`;
      } while (await getBride(id));
    }

    const updatedAt = nextTimestamp(existing?.updatedAt);
    const record = {
      schemaVersion: 1,
      id,
      name: bride.name,
      shapeId: bride.shapeId,
      values: bride.values,
      notes: bride.notes,
      ...(bride.passformklasse !== undefined ? { passformklasse: bride.passformklasse } : {}),
      ...(bride.waistSlopeFrontCm !== undefined ? { waistSlopeFrontCm: bride.waistSlopeFrontCm } : {}),
      ...(bride.balanceEntscheidung !== undefined ? { balanceEntscheidung: bride.balanceEntscheidung } : {}),
      createdAt: existing?.createdAt || updatedAt,
      updatedAt
    };
    const targetPath = bridePath(id);
    const temporaryPath = `${targetPath}.tmp`;

    await mkdir(storageDir, { recursive: true });
    await writeFile(temporaryPath, `${JSON.stringify(record, null, 2)}\n`, "utf8");
    await rename(temporaryPath, targetPath);
    return record;
  }

  async function deleteBride(id) {
    const filePath = bridePath(id);
    try {
      await unlink(filePath);
      return true;
    } catch (error) {
      if (error.code === "ENOENT") return false;
      throw error;
    }
  }

  return { listBrides, getBride, saveBride, deleteBride };
}

export const brideStore = createBrideStore(
  path.join(import.meta.dirname, "..", "..", "data", "brides")
);

export default brideStore;
