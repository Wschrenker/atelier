export function derivationEntry({ outputId, value, unit, dependsOn, ruleRef = null, sourceRefs = [] }) {
  if (!outputId) throw new Error("derivation outputId is required");
  if (!Number.isFinite(value)) throw new Error(`${outputId} must have a finite value`);
  if (!unit) throw new Error(`${outputId} must declare a unit`);
  if (!Array.isArray(dependsOn) || dependsOn.length === 0) {
    throw new Error(`${outputId} must declare dependencies`);
  }
  return {
    outputId,
    value,
    unit,
    dependsOn: [...dependsOn],
    ruleRef,
    sourceRefs: [...sourceRefs]
  };
}
