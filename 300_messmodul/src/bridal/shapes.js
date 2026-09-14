export const BRIDAL_SHAPES = Object.freeze({
  a_line: Object.freeze({
    id: "a_line",
    label: "A-Linie",
    aliases: ["A-line"],
    description: "Das Oberteil liegt körpernah. Ab der natürlichen Taille erweitert sich der Rock gleichmäßig und moderat bis zum Saum.",
    waistline: "natürliche Taille",
    flareStartsAt: "Taille",
    volume: "mittel",
    fittedThrough: ["Oberteil", "Taille"],
    patternFamilies: ["bodice_block", "a_line_skirt"],
    status: "design_class_only"
  }),
  princess_ball_gown: Object.freeze({
    id: "princess_ball_gown",
    label: "Prinzessin / Ballkleid",
    aliases: ["Ball Gown", "Duchesse"],
    description: "Ein enges Oberteil trifft an der natürlichen Taille auf einen sehr weiten, konstruktiv gestützten oder mehrlagigen Rock.",
    waistline: "natürliche Taille",
    flareStartsAt: "Taille",
    volume: "sehr hoch",
    fittedThrough: ["Oberteil", "Taille"],
    patternFamilies: ["bodice_block", "full_skirt", "support_structure"],
    status: "design_class_only"
  }),
  mermaid: Object.freeze({
    id: "mermaid",
    label: "Meerjungfrau",
    aliases: ["Fishtail"],
    description: "Die Silhouette folgt Oberkörper, Taille, Hüfte und Oberschenkeln eng. Die starke Erweiterung beginnt am Knie oder knapp darunter.",
    waistline: "natürlich oder modellabhängig",
    flareStartsAt: "Knie / unteres Knie",
    volume: "unten hoch",
    fittedThrough: ["Oberteil", "Taille", "Hüfte", "Oberschenkel"],
    patternFamilies: ["fitted_dress_block", "mermaid_flare"],
    status: "design_class_only"
  }),
  empire: Object.freeze({
    id: "empire",
    label: "Empire",
    aliases: ["Empire Waist"],
    description: "Die konstruktive Taillenlinie liegt direkt unter der Brust. Der Rock fällt von dieser erhöhten Linie weich und frei nach unten.",
    waistline: "unter der Brust",
    flareStartsAt: "Empire-Linie",
    volume: "niedrig bis mittel",
    fittedThrough: ["Brustbereich"],
    patternFamilies: ["empire_bodice", "raised_waist_skirt"],
    status: "design_class_only"
  }),
  sheath_column: Object.freeze({
    id: "sheath_column",
    label: "Etui / Säule",
    aliases: ["Sheath", "Column"],
    description: "Eine schmale, langgezogene Silhouette folgt dem Körper oder fällt nahezu gerade. Der Rock besitzt nur geringe Saumweite.",
    waistline: "natürlich oder ungegliedert",
    flareStartsAt: "keine deutliche Ausstellung",
    volume: "niedrig",
    fittedThrough: ["Oberteil", "Taille", "Hüfte"],
    patternFamilies: ["fitted_dress_block", "straight_skirt"],
    status: "design_class_only"
  })
});

export const BRIDAL_SHAPE_IDS = Object.freeze(Object.keys(BRIDAL_SHAPES));

export function getBridalShape(shapeId) {
  return BRIDAL_SHAPES[shapeId] || null;
}
