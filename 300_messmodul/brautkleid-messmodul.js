import { BRIDAL_BODY_SCHEMAS } from "/src/measurements/bridal-body-schemas.js";
import {
  BRIDAL_BODY_MEASUREMENTS,
  BRIDAL_MEASUREMENT_CONTEXT,
  MEASUREMENT_GROUPS,
  MEASUREMENT_VIEWS,
  createBridalMeasurementProfile,
  validateMeasurementValue
} from "/src/measurements/bridal-body-measurements.js";
import { assessFigurePlausibility } from "/src/measurements/figure-plausibility.js";
import {
  coerceMeasurementValues,
  deriveFigureDisplayState
} from "/src/measurements/figure-plausibility-view-model.js";
import {
  RAW_MEASUREMENT_IDS,
  deriveConstructionValue
} from "/src/measurements/construction-derivations.js";
import { BRIDAL_SHAPES, getBridalShape } from "/src/bridal/shapes.js";
import { PASSFORMKLASSE_OPTIONS, RECOMMENDED_PASSFORMKLASSE } from "/src/dress/passformklasse.js";

const SVG_NS = "http://www.w3.org/2000/svg";
const form = document.querySelector("#measurementForm");
const groupsRoot = document.querySelector("#measurementGroups");
const searchInput = document.querySelector("#measurementSearch");
const enteredCount = document.querySelector("#enteredCount");
const formStatus = document.querySelector("#formStatus");
const profileOutput = document.querySelector("#profileOutput");
const viewTabs = document.querySelector("#viewTabs");
const bodyDrawing = document.querySelector("#bodyDrawing");
const measurementGuide = document.querySelector("#measurementGuide");
const schemaTitle = document.querySelector("#schemaTitle");
const schemaDescription = document.querySelector("#schemaDescription");
const viewHint = document.querySelector("#viewHint");
const brideList = document.querySelector("#brideList");
const brideName = document.querySelector("#brideName");
const brideNotes = document.querySelector("#brideNotes");
const brideStatus = document.querySelector("#brideStatus");
const newBrideButton = document.querySelector("#newBrideButton");
const saveBrideButton = document.querySelector("#saveBrideButton");
const deleteBrideButton = document.querySelector("#deleteBrideButton");
const figurePlausibilityPanel = document.querySelector("#figurePlausibilityPanel");
const figurePlausibilityTitle = document.querySelector("#figurePlausibilityTitle");
const figurePlausibilitySummary = document.querySelector("#figurePlausibilitySummary");
const figurePlausibilityFeedback = document.querySelector("#figurePlausibilityFeedback");
const figurePlausibilityDetails = document.querySelector("#figurePlausibilityDetails");
const figureStatusCompact = document.querySelector("#figureStatusCompact");
const figureStatusPill = document.querySelector("#figureStatusPill");
const rawMeasurementBadge = document.querySelector("#rawMeasurementBadge");
const constructionValue = document.querySelector("#constructionValue");
const passformklasseOptions = document.querySelector("#passformklasseOptions");
const waistSlopeFrontInput = document.querySelector("#waistSlopeFrontInput");
const rawMeasurementIdSet = new Set(RAW_MEASUREMENT_IDS);
const constructionNumber = new Intl.NumberFormat("de-DE", { maximumFractionDigits: 2 });

const FIGURE_STATE_PRESENTATION = Object.freeze({
  deviates: Object.freeze({
    title: "Prüfung nötig",
    compactLabel: "Prüfen",
    pillLabel: "Prüfen"
  }),
  incomplete: Object.freeze({
    title: "Noch nicht vollständig prüfbar",
    compactLabel: "Offen",
    pillLabel: "Offen"
  }),
  ideal: Object.freeze({
    title: "Kontrollen innerhalb der Fenster",
    compactLabel: "OK",
    pillLabel: "OK"
  })
});

const CHECK_STATUS_LABELS = Object.freeze({
  ok: "innerhalb des Fensters",
  unsicher: "konstruktiv unsicher",
  "off-norm": "außerhalb des Kontrollfensters",
  unbestimmbar: "noch nicht bestimmbar"
});

function selectedShape() {
  const queryShapeId = new URLSearchParams(window.location.search).get("shapeId");
  let storedShapeId = null;
  try {
    storedShapeId = window.sessionStorage.getItem("bridalShapeId");
  } catch {
    // Die Seite funktioniert auch ohne Web Storage.
  }
  return getBridalShape(queryShapeId) || getBridalShape(storedShapeId) || BRIDAL_SHAPES.a_line;
}

let shape = selectedShape();
try {
  window.sessionStorage.setItem("bridalShapeId", shape.id);
} catch {
  // Auswahl bleibt mindestens über den Query-Parameter erhalten.
}

document.querySelector("#selectedShapeLabel").textContent = shape.label;
document.querySelector("#selectedShapeId").textContent = shape.id;
document.querySelector("#measurementContext").textContent = BRIDAL_MEASUREMENT_CONTEXT.instruction;

let activeMeasurement = BRIDAL_BODY_MEASUREMENTS[0];
let activeView = activeMeasurement.views[0];
let activeBrideId = null;
let activePassformklasse = RECOMMENDED_PASSFORMKLASSE;
let activeWaistSlopeFront = 0;

function setBrideStatus(message, isError = false) {
  brideStatus.textContent = message;
  brideStatus.classList.toggle("error", isError);
  if (isError) brideStatus.classList.remove("saved");
}

// Kurze sichtbare Bestätigung nach erfolgreichem Speichern (Werner-Wunsch): Button + Status blinken grün.
function flashSaved() {
  brideStatus.classList.add("saved");
  if (!saveBrideButton) return;
  saveBrideButton.classList.remove("saved-flash");
  void saveBrideButton.offsetWidth; // Reflow erzwingen, damit der Blink auch bei schnellem Mehrfach-Speichern neu startet.
  saveBrideButton.classList.add("saved-flash");
}

function setShape(shapeId) {
  const nextShape = getBridalShape(shapeId);
  if (!nextShape) throw new Error(`Unbekannte Grundform: ${shapeId}`);
  shape = nextShape;
  document.querySelector("#selectedShapeLabel").textContent = shape.label;
  document.querySelector("#selectedShapeId").textContent = shape.id;
  try {
    window.sessionStorage.setItem("bridalShapeId", shape.id);
  } catch {
    // Die geladene Grundform bleibt auch ohne Web Storage aktiv.
  }
}

async function requestJson(url, options) {
  const response = await fetch(url, options);
  const body = await response.json().catch(() => ({}));
  if (!response.ok) throw new Error(body.error || `Anfrage fehlgeschlagen (${response.status}).`);
  return body;
}

function readableUpdatedAt(value) {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return new Intl.DateTimeFormat("de-CH", {
    dateStyle: "medium",
    timeStyle: "short"
  }).format(date);
}

function renderBrideList(brides) {
  brideList.replaceChildren();
  if (!brides.length) {
    const empty = document.createElement("p");
    empty.className = "bride-list-empty";
    empty.textContent = "Noch keine Braut gespeichert.";
    brideList.appendChild(empty);
    return;
  }

  for (const bride of brides) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = "bride-list-button";
    button.setAttribute("aria-current", String(bride.id === activeBrideId));
    const name = document.createElement("strong");
    name.textContent = bride.name;
    const meta = document.createElement("span");
    meta.textContent = `${readableUpdatedAt(bride.updatedAt)} · ${bride.measurementCount} Messwerte`;
    button.append(name, meta);
    button.addEventListener("click", () => loadBride(bride.id));
    brideList.appendChild(button);
  }
}

async function loadBrideList() {
  try {
    renderBrideList(await requestJson("/api/brides"));
    return true;
  } catch (error) {
    setBrideStatus(`Braut-Liste konnte nicht geladen werden: ${error.message}`, true);
    return false;
  }
}

function clearMeasurementValues() {
  for (const measurement of BRIDAL_BODY_MEASUREMENTS) {
    const input = form.elements.namedItem(measurement.id);
    if (!input) continue;
    input.value = "";
    input.setCustomValidity("");
  }
}

function startNewBride() {
  activeBrideId = null;
  brideName.value = "";
  brideNotes.value = "";
  deleteBrideButton.disabled = true;
  clearMeasurementValues();
  activePassformklasse = RECOMMENDED_PASSFORMKLASSE;
  activeWaistSlopeFront = 0;
  waistSlopeFrontInput.value = activeWaistSlopeFront;
  syncPassformklasseSelection();
  updateProfilePreview();
  brideList.querySelectorAll(".bride-list-button").forEach((button) => {
    button.setAttribute("aria-current", "false");
  });
  formStatus.textContent = "";
  formStatus.classList.remove("error");
  setBrideStatus("Neue Braut: Name und Maße können jetzt erfasst werden.");
  brideName.focus();
}

async function loadBride(id) {
  try {
    const bride = await requestJson(`/api/brides/${encodeURIComponent(id)}`);
    activeBrideId = bride.id;
    brideName.value = bride.name;
    brideNotes.value = bride.notes || "";
    setShape(bride.shapeId);
    activePassformklasse = resolvePassformklasse(bride.passformklasse);
    activeWaistSlopeFront = Number.isFinite(Number(bride.waistSlopeFrontCm))
      ? Number(bride.waistSlopeFrontCm)
      : 0;
    waistSlopeFrontInput.value = activeWaistSlopeFront;
    syncPassformklasseSelection();
    clearMeasurementValues();
    for (const [measurementId, value] of Object.entries(bride.values)) {
      const input = document.querySelector(`#measure-${measurementId}`);
      if (input) input.value = value;
    }
    updateProfilePreview();
    deleteBrideButton.disabled = false;
    if (await loadBrideList()) setBrideStatus(`${bride.name} wurde geladen.`);
  } catch (error) {
    setBrideStatus(`Braut konnte nicht geladen werden: ${error.message}`, true);
  }
}

async function saveBride() {
  const name = brideName.value.trim();
  if (!name) {
    setBrideStatus("Bitte einen Namen für die Braut eingeben.", true);
    brideName.focus();
    return;
  }
  if (!form.reportValidity()) {
    setBrideStatus("Bitte nur endliche positive Messwerte eingeben.", true);
    return;
  }

  try {
    updateProfilePreview();
    const saved = await requestJson("/api/brides", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        id: activeBrideId || undefined,
        name,
        shapeId: shape.id,
        passformklasse: activePassformklasse,
        waistSlopeFrontCm: activeWaistSlopeFront,
        values: enteredValues(),
        notes: brideNotes.value
      })
    });
    activeBrideId = saved.id;
    brideName.value = saved.name;
    brideNotes.value = saved.notes || "";
    deleteBrideButton.disabled = false;
    if (await loadBrideList()) setBrideStatus(`${saved.name} wurde gespeichert.`);
    flashSaved();
  } catch (error) {
    setBrideStatus(`Braut konnte nicht gespeichert werden: ${error.message}`, true);
  }
}

async function deleteActiveBride() {
  if (!activeBrideId) return;
  const name = brideName.value.trim() || "diese Braut";
  if (!window.confirm(`${name} wirklich löschen?`)) return;

  try {
    await requestJson(`/api/brides/${encodeURIComponent(activeBrideId)}`, { method: "DELETE" });
    activeBrideId = null;
    brideName.value = "";
    brideNotes.value = "";
    deleteBrideButton.disabled = true;
    clearMeasurementValues();
    updateProfilePreview();
    if (await loadBrideList()) setBrideStatus(`${name} wurde gelöscht.`);
  } catch (error) {
    setBrideStatus(`Braut konnte nicht gelöscht werden: ${error.message}`, true);
  }
}

function svgElement(name, attributes = {}) {
  const element = document.createElementNS(SVG_NS, name);
  for (const [key, value] of Object.entries(attributes)) element.setAttribute(key, String(value));
  return element;
}

function renderBodySchema() {
  const schema = BRIDAL_BODY_SCHEMAS[activeView];
  bodyDrawing.replaceChildren();
  measurementGuide.replaceChildren();

  bodyDrawing.appendChild(svgElement("path", { d: schema.outline, class: "body-outline" }));
  for (const detail of schema.details) {
    bodyDrawing.appendChild(svgElement("path", { d: detail, class: "body-detail" }));
  }

  const guides = activeMeasurement.guides.filter((guide) => guide.view === activeView);
  for (const guide of guides) {
    const attributes = { ...guide, class: "measurement-guide" };
    delete attributes.view;
    delete attributes.kind;
    measurementGuide.appendChild(svgElement(guide.kind, attributes));
    if (guide.kind === "line") {
      measurementGuide.appendChild(svgElement("circle", { cx: guide.x1, cy: guide.y1, r: 5, class: "measurement-guide-point" }));
      measurementGuide.appendChild(svgElement("circle", { cx: guide.x2, cy: guide.y2, r: 5, class: "measurement-guide-point" }));
    }
  }

  schemaTitle.textContent = `${schema.label}: ${activeMeasurement.label}`;
  schemaDescription.textContent = `${schema.description} Die hervorgehobene Linie zeigt ${activeMeasurement.label}.`;
  const namedViews = activeMeasurement.views.map((view) => BRIDAL_BODY_SCHEMAS[view].label).join(", ");
  viewHint.textContent = guides.length
    ? `Hervorgehoben: ${activeMeasurement.label} (${activeMeasurement.abbreviation}).`
    : `Diese Messstelle ist in folgender Ansicht eingezeichnet: ${namedViews}.`;
}

function renderViewTabs() {
  viewTabs.replaceChildren();
  for (const view of MEASUREMENT_VIEWS) {
    const schema = BRIDAL_BODY_SCHEMAS[view];
    const button = document.createElement("button");
    button.type = "button";
    button.className = "view-tab";
    button.setAttribute("role", "tab");
    button.setAttribute("aria-selected", String(view === activeView));
    button.textContent = schema.label;
    button.addEventListener("click", () => {
      activeView = view;
      renderViewTabs();
      renderBodySchema();
    });
    viewTabs.appendChild(button);
  }
}

function renderMeasurementDetails() {
  document.querySelector("#measurePosition").textContent = `Position ${activeMeasurement.position}`;
  document.querySelector("#measureLabel").textContent = activeMeasurement.label;
  document.querySelector("#measureAbbreviation").textContent = activeMeasurement.abbreviation;
  document.querySelector("#measureInstruction").textContent = activeMeasurement.instruction;
  document.querySelector("#measureSource").textContent = `${activeMeasurement.source.reference}; geprüfte Transkription`;
  document.querySelector("#sourcePill").textContent = `S. ${activeMeasurement.source.page}`;
  safeRenderConstructionDetails();
}

function selectMeasurement(measurementId) {
  const measurement = BRIDAL_BODY_MEASUREMENTS.find((entry) => entry.id === measurementId);
  if (!measurement) return;
  activeMeasurement = measurement;
  activeView = measurement.views[0];
  document.querySelectorAll(".measurement-select").forEach((button) => {
    button.setAttribute("aria-current", String(button.dataset.measurementId === measurementId));
  });
  renderViewTabs();
  renderBodySchema();
  renderMeasurementDetails();
}

function filterMeasurementRows(query) {
  const normalizedQuery = query.trim().toLocaleLowerCase("de");
  document.querySelectorAll(".measurement-group").forEach((group) => {
    let visibleRows = 0;
    group.querySelectorAll(".measurement-row").forEach((row) => {
      const visible = !normalizedQuery || row.dataset.searchText.includes(normalizedQuery);
      row.hidden = !visible;
      if (visible) visibleRows += 1;
    });
    group.hidden = visibleRows === 0;
  });
}

function jumpToMeasurement(measurementId) {
  searchInput.value = "";
  filterMeasurementRows("");
  selectMeasurement(measurementId);
  const input = document.getElementById(`measure-${measurementId}`);
  if (!input) return;
  input.focus({ preventScroll: true });
  input.scrollIntoView({ behavior: "smooth", block: "center" });
}

function buildMeasurementRows() {
  for (const group of MEASUREMENT_GROUPS) {
    const section = document.createElement("section");
    section.className = "measurement-group";
    section.dataset.groupId = group.id;
    const heading = document.createElement("h3");
    heading.textContent = `${group.label} · ${group.positions}`;
    const list = document.createElement("ul");
    list.className = "measurement-list";

    for (const measurement of BRIDAL_BODY_MEASUREMENTS.filter((entry) => entry.group === group.id)) {
      const item = document.createElement("li");
      item.className = "measurement-row";
      item.dataset.searchText = `${measurement.label} ${measurement.abbreviation} ${measurement.part || ""}`.toLocaleLowerCase("de");

      const selectButton = document.createElement("button");
      selectButton.type = "button";
      selectButton.className = "measurement-select";
      selectButton.dataset.measurementId = measurement.id;
      selectButton.setAttribute("aria-current", String(measurement.id === activeMeasurement.id));
      const label = document.createElement("strong");
      label.textContent = measurement.label;
      const meta = document.createElement("span");
      meta.textContent = `${measurement.position} · ${measurement.abbreviation}`;
      selectButton.append(label, meta);
      if (rawMeasurementIdSet.has(measurement.id)) {
        const badge = document.createElement("span");
        badge.className = "raw-measurement-badge";
        badge.textContent = "Rohmaß";
        selectButton.appendChild(badge);
      }
      selectButton.addEventListener("click", () => selectMeasurement(measurement.id));

      const valueLabel = document.createElement("label");
      valueLabel.className = "visually-hidden";
      valueLabel.htmlFor = `measure-${measurement.id}`;
      valueLabel.textContent = `${measurement.label} in ${measurement.unit}`;
      const input = document.createElement("input");
      input.id = `measure-${measurement.id}`;
      input.name = measurement.id;
      input.className = "measurement-value";
      input.type = "number";
      input.min = "0";
      input.step = "any";
      input.inputMode = "decimal";
      input.setAttribute("aria-label", `${measurement.label} in ${measurement.unit}`);
      input.addEventListener("focus", () => selectMeasurement(measurement.id));
      input.addEventListener("input", () => handleMeasurementInput(input));

      const unit = document.createElement("span");
      unit.className = "unit-label";
      unit.textContent = measurement.unit === "deg" ? "Grad" : "cm";
      item.append(selectButton, valueLabel, input, unit);
      list.appendChild(item);
    }

    section.append(heading, list);
    groupsRoot.appendChild(section);
  }
}

function enteredValues() {
  return Object.fromEntries(
    BRIDAL_BODY_MEASUREMENTS.map((measurement) => [measurement.id, form.elements.namedItem(measurement.id)?.value ?? ""])
  );
}

function updateProfilePreview() {
  // shapeId und passformklasse sind beide DESIGN-Wahlen; das Messobjekt traegt sie
  // neben den reinen Koerpermassen. createBridalMeasurementProfile bleibt unangetastet.
  const profile = Object.freeze({
    ...createBridalMeasurementProfile({ shapeId: shape.id, values: enteredValues() }),
    passformklasse: activePassformklasse
  });
  profileOutput.textContent = JSON.stringify(profile, null, 2);
  enteredCount.textContent = `${profile.measurements.length} erfasst`;
  window.bridalMeasurementProfile = profile;
  renderFigurePlausibility();
  safeRenderConstructionDetails();
  return profile;
}

// Passformklasse (3/4/5) — sichtbar vorgewaehlte Empfehlung, nicht still gesetzt.
function resolvePassformklasse(value) {
  const number = Number(value);
  return PASSFORMKLASSE_OPTIONS.some((option) => option.value === number)
    ? number
    : RECOMMENDED_PASSFORMKLASSE;
}

function syncPassformklasseSelection() {
  if (!passformklasseOptions) return;
  passformklasseOptions.querySelectorAll(".passformklasse-option").forEach((label) => {
    const isSelected = Number(label.dataset.value) === activePassformklasse;
    label.classList.toggle("is-selected", isSelected);
    const input = label.querySelector("input");
    if (input) input.checked = isSelected;
  });
}

function setPassformklasse(value) {
  activePassformklasse = resolvePassformklasse(value);
  syncPassformklasseSelection();
  updateProfilePreview();
}

function renderPassformklasseOptions() {
  if (!passformklasseOptions) return;
  passformklasseOptions.replaceChildren();
  for (const option of PASSFORMKLASSE_OPTIONS) {
    const label = document.createElement("label");
    label.className = "passformklasse-option";
    label.dataset.value = String(option.value);

    const input = document.createElement("input");
    input.type = "radio";
    input.name = "passformklasse";
    input.value = String(option.value);
    input.checked = option.value === activePassformklasse;
    input.addEventListener("change", () => {
      if (input.checked) setPassformklasse(option.value);
    });

    const text = document.createElement("span");
    text.className = "passformklasse-option-text";
    const title = document.createElement("strong");
    title.textContent = option.label;
    if (option.recommended) {
      const badge = document.createElement("span");
      badge.className = "passformklasse-recommended";
      badge.textContent = "empfohlen";
      title.appendChild(badge);
    }
    const effect = document.createElement("small");
    effect.textContent = option.effect;
    text.append(title, effect);

    label.append(input, text);
    passformklasseOptions.appendChild(label);
  }
  syncPassformklasseSelection();
}

function renderConstructionDetails() {
  if (!rawMeasurementBadge || !constructionValue) return;
  const values = coerceMeasurementValues(enteredValues());
  const derivation = deriveConstructionValue(activeMeasurement.id, values);
  rawMeasurementBadge.hidden = !derivation;
  constructionValue.replaceChildren();
  constructionValue.hidden = !derivation?.value && derivation?.value !== 0;
  if (constructionValue.hidden) return;
  constructionValue.textContent = `Konstruktionsmaß ${derivation.target} = ${constructionNumber.format(derivation.value)} cm (${derivation.expr}, ${derivation.sourceRef})`;
}

function safeRenderConstructionDetails() {
  try {
    renderConstructionDetails();
  } catch (error) {
    try {
      if (rawMeasurementBadge) rawMeasurementBadge.hidden = true;
      if (constructionValue) {
        constructionValue.hidden = true;
        constructionValue.replaceChildren();
      }
      console.error("Konstruktionsmaß konnte nicht aktualisiert werden.", error);
    } catch {
      // Die abgeleitete Anzeige darf Erfassung und Speichern niemals blockieren.
    }
  }
}

function measurementLabel(measurementId) {
  return BRIDAL_BODY_MEASUREMENTS.find(({ id }) => id === measurementId)?.label || measurementId;
}

function appendSectionHeading(root, text) {
  const heading = document.createElement("h4");
  heading.textContent = text;
  root.appendChild(heading);
}

function renderFlaggedChecks(root, checks) {
  if (!checks.length) return;
  const section = document.createElement("section");
  section.className = "figure-feedback-section";
  appendSectionHeading(section, "Betroffene Kontrollen");
  const list = document.createElement("ul");
  for (const check of checks) {
    const item = document.createElement("li");
    const label = document.createElement("strong");
    label.textContent = check.label;
    const status = document.createElement("span");
    status.textContent = CHECK_STATUS_LABELS[check.status] || check.status;
    item.append(label, status);
    list.appendChild(item);
  }
  section.appendChild(list);
  root.appendChild(section);
}

function renderMissingMeasurements(root, measurementIds) {
  if (!measurementIds.length) return;
  const section = document.createElement("section");
  section.className = "figure-feedback-section";
  appendSectionHeading(section, "Noch benötigte Maße");
  const text = document.createElement("p");
  text.textContent = measurementIds.map(measurementLabel).join(", ");
  section.appendChild(text);
  root.appendChild(section);
}

function renderExtraMeasurements(root, measurements) {
  if (!measurements.length) return;
  const section = document.createElement("section");
  section.className = "figure-feedback-section";
  appendSectionHeading(section, "Zusatzmessungen nötig");
  const actions = document.createElement("div");
  actions.className = "figure-extra-actions";
  for (const measurement of measurements) {
    const action = document.createElement("div");
    action.className = "figure-extra-action";
    const button = document.createElement("button");
    button.type = "button";
    button.className = "figure-measurement-button";
    button.textContent = `${measurement.abbreviation} · ${measurementLabel(measurement.measurementId)}`;
    button.addEventListener("click", () => jumpToMeasurement(measurement.measurementId));
    const reference = document.createElement("span");
    reference.textContent = `${measurement.reason} Quelle: ${measurement.bookRef}`;
    action.append(button, reference);
    actions.appendChild(action);
  }
  section.appendChild(actions);
  root.appendChild(section);
}

function renderAdvisories(root, advisories) {
  if (!advisories.length) return;
  const section = document.createElement("section");
  section.className = "figure-feedback-section";
  appendSectionHeading(section, "Hinweise zum Nachmessen");
  const list = document.createElement("ul");
  list.className = "figure-advisory-list";
  for (const advisory of advisories) {
    const item = document.createElement("li");
    const reason = document.createElement("span");
    reason.textContent = advisory.reason;
    const reference = document.createElement("small");
    reference.textContent = advisory.bookRef;
    item.append(reason, reference);
    list.appendChild(item);
  }
  section.appendChild(list);
  root.appendChild(section);
}

function readableCheckValue(value) {
  if (value === null || value === undefined) return "—";
  if (typeof value === "string") return value;
  return JSON.stringify(value);
}

function renderTechnicalDetails(checks) {
  figurePlausibilityDetails.replaceChildren();
  for (const check of checks) {
    const article = document.createElement("article");
    article.className = "figure-check-detail";
    const heading = document.createElement("h4");
    heading.textContent = check.label;
    const status = document.createElement("p");
    status.textContent = `Status: ${CHECK_STATUS_LABELS[check.status] || check.status}`;
    const computed = document.createElement("p");
    computed.textContent = `Berechnet: ${readableCheckValue(check.computed)}`;
    const expected = document.createElement("p");
    expected.textContent = `Erwartet: ${readableCheckValue(check.expected)}`;
    const source = document.createElement("p");
    source.textContent = `Quelle: ${check.sourceRef}`;
    article.append(heading, status, computed, expected, source);
    figurePlausibilityDetails.appendChild(article);
  }
}

function applyFigureState(state) {
  const presentation = FIGURE_STATE_PRESENTATION[state];
  for (const element of [figurePlausibilityPanel, figureStatusCompact]) {
    element.classList.remove("is-deviates", "is-incomplete", "is-ideal");
    element.classList.add(`is-${state}`);
  }
  figurePlausibilityTitle.textContent = presentation.title;
  figureStatusCompact.textContent = presentation.compactLabel;
  figureStatusPill.textContent = presentation.pillLabel;
}

function renderFigurePlausibility() {
  try {
    const values = coerceMeasurementValues(enteredValues());
    const assessment = assessFigurePlausibility({ values });
    const display = deriveFigureDisplayState(assessment);
    applyFigureState(display.state);

    if (display.state === "deviates") {
      figurePlausibilitySummary.textContent = `${display.flaggedChecks.length} Kontrolle${display.flaggedChecks.length === 1 ? "" : "n"} benötigt eine fachliche Prüfung.`;
    } else if (display.state === "ideal") {
      figurePlausibilitySummary.textContent = "Alle fünf Kontrollen liegen innerhalb der hinterlegten Fenster.";
    } else if (display.missingMeasurementIds.length > 0) {
      figurePlausibilitySummary.textContent = `Für die vollständige Prüfung fehlen noch ${display.missingMeasurementIds.length} Maßwerte.`;
    } else {
      figurePlausibilitySummary.textContent = "Mindestens eine Kontrolle kann mit den aktuellen Werten noch nicht bestimmt werden.";
    }

    figurePlausibilityFeedback.replaceChildren();
    renderFlaggedChecks(figurePlausibilityFeedback, display.flaggedChecks);
    renderMissingMeasurements(figurePlausibilityFeedback, display.missingMeasurementIds);
    renderExtraMeasurements(figurePlausibilityFeedback, display.requiredExtraMeasurements);
    renderAdvisories(figurePlausibilityFeedback, display.advisories);
    renderTechnicalDetails(assessment.checks);
  } catch (error) {
    applyFigureState("incomplete");
    figurePlausibilityTitle.textContent = "Plausibilitätsanzeige nicht verfügbar";
    figurePlausibilitySummary.textContent = "Die Maße können weiterhin erfasst und gespeichert werden.";
    figurePlausibilityFeedback.replaceChildren();
    figurePlausibilityDetails.replaceChildren();
    console.error("Figur-Plausibilität konnte nicht aktualisiert werden.", error);
  }
}

function handleMeasurementInput(input) {
  input.setCustomValidity("");
  if (input.value !== "") {
    try {
      validateMeasurementValue(input.value);
    } catch (error) {
      input.setCustomValidity(error.message);
    }
  }
  formStatus.textContent = "";
  formStatus.classList.remove("error");
  if (form.checkValidity()) updateProfilePreview();
  renderFigurePlausibility();
  safeRenderConstructionDetails();
}

searchInput.addEventListener("input", () => {
  filterMeasurementRows(searchInput.value);
});

waistSlopeFrontInput.addEventListener("input", () => {
  const numericValue = Number(waistSlopeFrontInput.value);
  if (Number.isFinite(numericValue)) activeWaistSlopeFront = numericValue;
});

form.addEventListener("submit", (event) => {
  event.preventDefault();
  if (!form.reportValidity()) {
    formStatus.textContent = "Bitte nur endliche positive Werte eingeben.";
    formStatus.classList.add("error");
    return;
  }

  try {
    const profile = updateProfilePreview();
    formStatus.textContent = `${profile.measurements.length} Messwerte als strukturiertes Objekt bereitgestellt.`;
    formStatus.classList.remove("error");
    window.dispatchEvent(new CustomEvent("bridal-measurement-profile", { detail: profile }));
  } catch (error) {
    formStatus.textContent = error.message;
    formStatus.classList.add("error");
  }
});

newBrideButton.addEventListener("click", startNewBride);
saveBrideButton.addEventListener("click", saveBride);
deleteBrideButton.addEventListener("click", deleteActiveBride);

buildMeasurementRows();
renderPassformklasseOptions();
renderViewTabs();
renderBodySchema();
renderMeasurementDetails();
updateProfilePreview();
loadBrideList();
