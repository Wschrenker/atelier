import { BRIDAL_SHAPE_IDS } from "../bridal/shapes.js";

export const MEASUREMENT_VIEWS = Object.freeze(["front", "side", "back"]);

export const BRIDAL_MEASUREMENT_CONTEXT = Object.freeze({
  instruction: "In aufrechter, natürlich-lockerer Haltung und nur mit Slip und Büstenhalter messen. Das Maßband liegt glatt am Körper, weder zu stramm noch zu locker. „Rechts“ und „links“ bezeichnen immer die Körperseite der gemessenen Person (aus ihrer Sicht), nie die Sicht der messenden Person.",
  source: Object.freeze({
    page: 12,
    reference: "Hofenbitzer, Band 1, S. 12",
    transcript: "hofenbitzer/band_1/transkription/eingang_claude/s11-15_rohtranskription.md#s12"
  })
});

export const MEASUREMENT_GROUPS = Object.freeze([
  Object.freeze({ id: "main", label: "Hauptmaße", positions: "1–5" }),
  Object.freeze({ id: "below_waist", label: "Unterhalb der Taille", positions: "6–8" }),
  Object.freeze({ id: "upper_lengths", label: "Hals und Oberkörperlängen", positions: "9–12" }),
  Object.freeze({ id: "torso_widths", label: "Rücken-, Armloch- und Brustbreiten", positions: "13–17" }),
  Object.freeze({ id: "bust", label: "Brustmaße", positions: "18–21" }),
  Object.freeze({ id: "arms", label: "Schulter-, Arm- und Handmaße", positions: "22–28" })
]);

const line = (view, x1, y1, x2, y2) => ({ view, kind: "line", x1, y1, x2, y2 });
const ellipse = (view, cx, cy, rx, ry) => ({ view, kind: "ellipse", cx, cy, rx, ry });
const path = (view, d) => ({ view, kind: "path", d });

function defineMeasurement(config) {
  const guides = config.guides.map((guide) => Object.freeze(guide));
  const views = [...new Set(guides.map((guide) => guide.view))];
  return Object.freeze({
    ...config,
    unit: config.unit || "cm",
    guides: Object.freeze(guides),
    views: Object.freeze(views),
    source: Object.freeze(config.source || {
      page: config.page,
      reference: `Hofenbitzer, Band 1, S. ${config.page}`,
      transcript: `hofenbitzer/band_1/transkription/eingang_claude/s11-15_rohtranskription.md#s${config.page}`
    })
  });
}

const instructions = Object.freeze({
  bodyHeight: "Von der Schädeldecke bis zur Fußsohle messen, ohne Schuhe und ohne voluminöse Kopfbehaarung. Dafür ein Anthropometer, Lotband oder eine andere genaue Messhilfe an einer Senkrechten verwenden.",
  bustCircumference: "Hinter der Kundin stehen. Das Maßband waagerecht über die Brustpunkte und unter den Armen hindurchführen, über dem unteren Schulterblattansatz leicht anheben und anliegend, aber nicht zu straff schließen. Den Wert ungefähr in der Rückenmitte ablesen.",
  waistCircumference: "Das Taillenband knapp unterhalb der schmalsten Körperstelle, mittig zwischen unterem Rippenbogen und Hüftknochen, anlegen. Als sicherer Anhaltspunkt: die unteren Rippenknochen (unterer Rippenbogen) ertasten und das Band knapp darunter führen. Seitlich liegt es an der engsten Stelle und möglichst waagerecht zur Standebene. Umfang ablesen und das Band bis zum Ende des Maßnehmens liegen lassen; eine zunächst leicht höhere oder tiefere Lage vorne oder hinten ist akzeptabel.",
  hipCircumference: "Den Körper von der Seite betrachten und das Maßband waagerecht um die stärkste Gesäßstelle legen. Langsam waagerecht nach unten gleiten lassen, damit sich die Bandweite anpasst und auch eine tiefer liegende seitliche Wölbung erfasst wird.",
  waistbandCircumference: "Das Maßband hinten oberhalb des Gesäßes an eine für die Kundin angenehme Position legen; bei starken Figuren vorne in die Bauchfalte beziehungsweise dorthin, wo Rock- oder Hosenbund gewöhnlich getragen werden. Dort wird der Bund figurbedingt später liegen.",
  waistbandDistance: "Den Abstand zwischen Unterkante des waagerechten Taillenbandes und Unterkante des Bundbandes an der bezeichneten Messstelle messen.",
  centerWaistHeight: "Mit dem Lot-Maßband von der Unterkante des waagerechten Taillenbandes bis zur Standebene messen. Das Taillenband liegt tief an der engsten Stelle, definitionsgemäß auf halber Höhe zwischen unterem Rippenbogen und Hüftknochen; besonders bei starken Figuren muss es zunächst waagerecht verlaufen.",
  sideWaistHeight: "An der bezeichneten Körperseite mit dem Lotband am Körper entlang von der Unterkante des Taillenbandes bis zur Standebene messen.",
  neckBaseCircumference: "Das Maßband hinten über den 7. Halswirbel und vorne am Schlüsselbein deutlich unterhalb des Adamsapfels durch die dortige Kuhle führen.",
  backLength: "Vom 7. Halswirbel beziehungsweise der hinteren Halsmitte entlang der Wirbelsäule bis zur Unterkante des waagerechten Taillenbandes messen. Dessen Unterkante sitzt an der tiefsten Stelle der waagerechten Taille, also an der engsten Stelle des hinteren Rumpfs. Lässt sich das Band nicht waagerecht anlegen, die Taillenschräglage von der Seite beobachten, in der Maßtabelle notieren und die Rückenlänge rechnerisch auf eine waagerechte Bandlage korrigieren; liegt das Band hinten zum Beispiel 1 cm tiefer, ist gRüL um 1 cm zu reduzieren.",
  bustDepth: "Start am 7. Halswirbel (auf der Wirbelsäule, hinten). Von dort eng um den Hals herum und weiter bis zum Brustpunkt der bezeichneten Körperhälfte messen. Beide Körperhälften getrennt messen; das spätere Konstruktionsmaß BrT wird daraus berechnet.",
  frontLength: "Start ebenfalls am 7. Halswirbel (auf der Wirbelsäule). Von dort am Hals entlang, über den Brustpunkt und dann senkrecht bis zur Unterkante des exakt waagerechten Taillenbandes messen. Beide Körperseiten getrennt messen. Nicht bis zur natürlichen Taille messen; das Konstruktionsmaß VL wird berechnet. Lässt sich das Band nicht waagerecht anlegen, die Taillenschräglage von der Seite beobachten, notieren und die Vorderlänge rechnerisch so korrigieren, als wäre zu einem waagerechten Taillenband gemessen worden.",
  upperBackWidth: "Als Kontrollmaß zwischen den Armansatzfalten über die Schulterblätter messen.",
  armholeDepth: "Zuerst einen etwa 2 bis 4 cm breiten, gegebenenfalls schwach klebenden Papierstreifen unter den höchsten Armstellen durchführen und exakt waagerecht über den Rücken legen; vorne muss er sichtbar sein. Dann vom 7. Halswirbel entlang der Wirbelsäule bis zur Oberkante dieses Streifens messen. Zur Kontrolle darf das Maß berechnet werden; bei starker Abweichung wird der Messwert in Richtung des berechneten Werts korrigiert.",
  measuredBackWidth: "Auf dem waagerechten Papierstreifen bei locker und natürlich hängenden Armen beide hinteren Armansätze mit einem senkrecht zum Körper gehaltenen Stift markieren. Den Abstand zwischen den Markierungen messen; für die Konstruktion gilt RüB = gRüB ÷ 2.",
  measuredArmDiameter: "Auf dem waagerechten Papierstreifen bei locker und natürlich hängenden Armen den vorderen Armansatz der bezeichneten Seite an der Streifenoberkante markieren und den Armdurchmesser zwischen vorderer und hinterer Markierung messen. Für die Konstruktion wird der Durchschnitt aus rechter und linker Messung verwendet. Weil diese Messung häufig schwierig ist, nennt die Quelle als sicherere Alternative die Berechnung ArD = OaU × 0,6 − 7,5 cm.",
  measuredBustWidth: "Über die stärksten Brustrundungen messen, und zwar exakt waagerecht bis zur SENKRECHTEN unter der vorderen Armansatz-Markierung auf dem Papierstreifen (❑7: „gBrB exakt waagerecht zur vorderen Armansatz-Markierung messen – nicht zum Oberarm!“). Die Markierungen liegen meist höher als die Brustlinie; das Band endet daher an der gedachten Senkrechten unter der Markierung, niemals am Oberarm. Für die Konstruktion gilt BrB = gBrB ÷ 2. Weil diese Messung häufig schwierig ist, nennt die Quelle als Alternative: BrB = BrU ÷ 2 − RüB − ArD (mit ArD = OaU × 0,6 − 7,5); die waagerechte Messung dient dann als Kontrolle, eine geringe Abweichung ist tolerierbar. Die Summe der waagerechten Teilstrecken kann wegen ihres Verlaufs einige Zentimeter größer als der direkt und schräg gemessene BrU sein.",
  upperBustWidth: "Bei locker hängenden Armen zwischen den vorderen Armansätzen oberhalb der Brüste messen.",
  upperBustDistance: "Gleichzeitig mit der oberen Brustbreite mit dem anderen Maßbandende den Abstand zwischen der Unterkante dieses Maßbandes und dem Brustpunkt der bezeichneten Seite messen.",
  underbustCircumference: "Das Maßband von hinten waagerecht unter der Brust und unter den Armen hindurchführen und hinten ablesen.",
  underbustDistance: "Gleichzeitig mit dem Unterbrustumfang mit dem anderen Maßbandende den Abstand zwischen der Oberkante des Umfangsbandes und dem Brustpunkt der bezeichneten Seite messen.",
  shoulderWidth: "Vom höchsten Schulterpunkt am seitlichen Hals, wo die Halslochnaht liegen soll, bis zum äußersten seitlichen Schulterknochen messen, wo die Armlochnaht liegen soll. Beide Seiten getrennt messen; anschließend kann der Mittelwert notiert werden.",
  armLength: "An der Armaußenkante vom Schulterpunkt über die leicht angewinkelte Ellenbogenspitze bis zum äußeren Handgelenkknöchel messen. Der Ellenbogen soll dabei höchstens 45° angewinkelt sein.",
  upperArmCircumference: "Bei natürlich herabhängendem Arm das Maßband anliegend und waagerecht um die stärkste Stelle unterhalb der Achselhöhle legen.",
  wristCircumference: "Den Umfang mit dem Maßband über die stärkste Stelle der Handgelenkknöchel messen.",
  handCircumference: "Den Umfang mit dem Maßband über die stärkste Stelle der geschlossenen Hand messen. Im Buch (S.15) mit HaU bezeichnet — gleiche Abkürzung wie der Halsansatzumfang; hier zur Eindeutigkeit HdU.",
  armscyeCircumference: "Mit einem dünnen Maßband oder einer Kordel unter der Achsel hindurch und über die seitliche Schulter messen.",
  shoulderAngle: "Mit einem Winkelmesser, zum Beispiel einer Smartphone-Wasserwaagen-App, den Schulterwinkel zwischen Halsansatz und Schulterpunkt messen. Die Quelle nennt 20° als Normalwert. Rechts und links getrennt messen; bei unterschiedlichen Werten ist für die Konstruktion der kleinere zu verwenden."
});

export const BRIDAL_BODY_MEASUREMENTS = Object.freeze([
  defineMeasurement({ id: "body_height", position: 1, group: "main", label: "Körperhöhe", abbreviation: "KöH", page: 12, instruction: instructions.bodyHeight, guides: [line("front", 42, 42, 42, 486)] }),
  defineMeasurement({ id: "bust_circumference", position: 2, group: "main", label: "Brustumfang", abbreviation: "BrU", page: 12, instruction: instructions.bustCircumference, guides: [ellipse("front", 120, 174, 48, 11), ellipse("side", 120, 174, 34, 11), ellipse("back", 120, 174, 47, 10)] }),
  defineMeasurement({ id: "waist_circumference_horizontal", position: 3, group: "main", label: "Taillenumfang waagerecht", abbreviation: "TaU", page: 12, instruction: instructions.waistCircumference, guides: [ellipse("front", 120, 244, 34, 8), ellipse("side", 120, 244, 25, 8), ellipse("back", 120, 244, 34, 8)] }),
  defineMeasurement({ id: "hip_circumference_horizontal", position: 4, group: "main", label: "Hüftumfang waagerecht", abbreviation: "HüU", page: 12, instruction: instructions.hipCircumference, guides: [ellipse("front", 120, 300, 49, 10), ellipse("side", 120, 300, 34, 10), ellipse("back", 120, 300, 48, 10)] }),
  defineMeasurement({ id: "waistband_circumference", position: 5, group: "main", label: "Bundumfang", abbreviation: "BuU", page: 12, instruction: instructions.waistbandCircumference, guides: [ellipse("front", 120, 271, 42, 9), ellipse("side", 120, 271, 30, 9), ellipse("back", 120, 271, 42, 9)] }),

  defineMeasurement({ id: "waistband_distance_front_center", position: 6, group: "below_waist", label: "Vorderer Bundabstand", abbreviation: "vBuA", part: "vorne mittig", page: 13, instruction: instructions.waistbandDistance, guides: [line("front", 120, 244, 120, 271), line("side", 95, 244, 95, 271)] }),
  defineMeasurement({ id: "waistband_distance_side_right", position: 6, group: "below_waist", label: "Seitlicher Bundabstand rechts", abbreviation: "sBuA", part: "rechts", page: 13, instruction: instructions.waistbandDistance, guides: [line("front", 86, 244, 78, 271)] }),
  defineMeasurement({ id: "waistband_distance_side_left", position: 6, group: "below_waist", label: "Seitlicher Bundabstand links", abbreviation: "sBuA", part: "links", page: 13, instruction: instructions.waistbandDistance, guides: [line("front", 154, 244, 162, 271), line("side", 120, 244, 120, 271)] }),
  defineMeasurement({ id: "waistband_distance_back_center", position: 6, group: "below_waist", label: "Hinterer Bundabstand", abbreviation: "hBuA", part: "hinten mittig", page: 13, instruction: instructions.waistbandDistance, guides: [line("back", 120, 244, 120, 271), line("side", 145, 244, 145, 271)] }),
  defineMeasurement({ id: "waist_height_front_center", position: 7, group: "below_waist", label: "Vordere Taillenhöhe", abbreviation: "vTaH", part: "vorne mittig", page: 13, instruction: instructions.centerWaistHeight, guides: [line("front", 110, 244, 110, 486), line("side", 98, 244, 98, 486)] }),
  defineMeasurement({ id: "waist_height_back_center", position: 7, group: "below_waist", label: "Hintere Taillenhöhe", abbreviation: "hTaH", part: "hinten mittig", page: 13, instruction: instructions.centerWaistHeight, guides: [line("back", 130, 244, 130, 486), line("side", 142, 244, 142, 486)] }),
  defineMeasurement({ id: "waist_height_side_right", position: 8, group: "below_waist", label: "Seitliche Taillenhöhe rechts", abbreviation: "rTaH", part: "rechts", page: 13, instruction: instructions.sideWaistHeight, guides: [line("front", 82, 244, 69, 486)] }),
  defineMeasurement({ id: "waist_height_side_left", position: 8, group: "below_waist", label: "Seitliche Taillenhöhe links", abbreviation: "lTaH", part: "links", page: 13, instruction: instructions.sideWaistHeight, guides: [line("front", 158, 244, 171, 486)] }),
  defineMeasurement({
    id: "waist_to_hip",
    position: 8,
    group: "below_waist",
    label: "Hüfttiefe",
    abbreviation: "HüT",
    page: "20–31",
    instruction: "Senkrechter Abstand von der Unterkante des waagerechten Taillenbandes bis zur Hüftlinie (stärkste Gesäßstelle, Höhe des waagerechten Hüftumfangs). Seitlich mit dem Lot-Maßband am Körper messen. Echtes Körpermaß — ersetzt die Buch-Konstruktionskonstante von 21 cm (S.20–31).",
    source: {
      page: "20–31",
      reference: "Hofenbitzer, Band 1, S. 20–31 — dort HüT=21 cm als Konstruktionskonstante; hier als echtes Körpermaß erfasst (Werner-Entscheid 2026-07-11).",
      transcript: "hofenbitzer/band_1/transkription/eingang_claude/s20-31_groessen-und-konstruktionsstandards_rohtranskription.md"
    },
    guides: [line("side", 98, 244, 98, 300), line("front", 120, 244, 120, 300)]
  }),

  defineMeasurement({ id: "neck_base_circumference", position: 9, group: "upper_lengths", label: "Halsansatzumfang", abbreviation: "HaU", page: 13, instruction: instructions.neckBaseCircumference, guides: [ellipse("front", 120, 111, 24, 6), ellipse("side", 120, 111, 18, 6), ellipse("back", 120, 111, 24, 6)] }),
  defineMeasurement({ id: "measured_back_length", position: 10, group: "upper_lengths", label: "Gemessene Rückenlänge", abbreviation: "gRüL", page: 13, instruction: instructions.backLength, guides: [path("back", "M120 105 C118 145 121 196 120 244"), path("side", "M131 105 C146 142 143 198 140 244")] }),
  defineMeasurement({ id: "measured_bust_depth_right", position: 11, group: "upper_lengths", label: "Gemessene Brusttiefe rechts", abbreviation: "gBrT", part: "rechts", page: 13, instruction: instructions.bustDepth, guides: [path("front", "M112 106 C99 121 94 144 93 179"), path("side", "M121 106 C100 128 96 153 98 179")] }),
  defineMeasurement({ id: "measured_bust_depth_left", position: 11, group: "upper_lengths", label: "Gemessene Brusttiefe links", abbreviation: "gBrT", part: "links", page: 13, instruction: instructions.bustDepth, guides: [path("front", "M128 106 C141 121 146 144 147 179")] }),
  defineMeasurement({ id: "measured_front_length_right", position: 12, group: "upper_lengths", label: "Gemessene Vorderlänge rechts", abbreviation: "gVL", part: "rechts", page: 13, instruction: instructions.frontLength, guides: [path("front", "M112 106 C99 128 93 153 93 179 L101 244"), path("side", "M121 106 C100 134 98 158 98 179 L101 244")] }),
  defineMeasurement({ id: "measured_front_length_left", position: 12, group: "upper_lengths", label: "Gemessene Vorderlänge links", abbreviation: "gVL", part: "links", page: 13, instruction: instructions.frontLength, guides: [path("front", "M128 106 C141 128 147 153 147 179 L139 244")] }),

  defineMeasurement({ id: "upper_back_width", position: 13, group: "torso_widths", label: "Obere Rückenbreite", abbreviation: "oRüB", page: 14, instruction: instructions.upperBackWidth, guides: [path("back", "M76 144 C98 132 142 132 164 144")] }),
  defineMeasurement({ id: "armhole_depth", position: 14, group: "torso_widths", label: "Armlochtiefe", abbreviation: "AlT", page: 14, instruction: instructions.armholeDepth, guides: [line("back", 120, 105, 120, 187), line("side", 136, 105, 136, 187)] }),
  defineMeasurement({ id: "measured_back_width", position: 15, group: "torso_widths", label: "Gemessene Rückenbreite", abbreviation: "gRüB", page: 14, instruction: instructions.measuredBackWidth, guides: [line("back", 72, 187, 168, 187)] }),
  // gArD ist ein TIEFENMASS (vorderer <-> hinterer Armansatz, front-to-back), auf dem
  // waagerechten Papierstreifen von der SEITE gemessen. Eine Tiefe ist frontal nicht als
  // Strecke sichtbar -> nur "side"-Guide (analog AlT). Fruehere "front"-Linie taeuschte ein
  // Breitenmass vor (sah in Vorder- und Seitenansicht gleich aus) -> entfernt (Werner 18.07.).
  defineMeasurement({ id: "measured_arm_diameter_right", position: 16, group: "torso_widths", label: "Gemessener Armdurchmesser rechts", abbreviation: "gArD", part: "rechts", page: 14, instruction: instructions.measuredArmDiameter, guides: [line("side", 82, 187, 116, 187)] }),
  defineMeasurement({ id: "measured_arm_diameter_left", position: 16, group: "torso_widths", label: "Gemessener Armdurchmesser links", abbreviation: "gArD", part: "links", page: 14, instruction: instructions.measuredArmDiameter, guides: [line("side", 124, 187, 158, 187)] }),
  defineMeasurement({ id: "measured_bust_width", position: 17, group: "torso_widths", label: "Gemessene Brustbreite", abbreviation: "gBrB", page: 14, instruction: instructions.measuredBustWidth, guides: [
    // Messstrecke endet an den SENKRECHTEN unter den vorderen Armansatz-Markierungen
    // (x=83/157 wie die gArD-Markierungen), nicht am Oberarm (❑7).
    path("front", "M83 181 C98 170 142 170 157 181"),
    line("front", 83, 170, 83, 195),
    line("front", 157, 170, 157, 195),
    // Seitenansicht: waagerecht von der Brustrundung zur Senkrechten am vorderen
    // Armansatz (x=82 = vorderes Ende der gArD-Markierung), nicht zum Oberarm.
    line("side", 82, 181, 98, 181),
    line("side", 82, 170, 82, 195)
  ] }),

  defineMeasurement({ id: "upper_bust_width", position: 18, group: "bust", label: "Obere Brustbreite", abbreviation: "oBrB", page: 15, instruction: instructions.upperBustWidth, guides: [line("front", 77, 154, 163, 154), line("side", 96, 154, 143, 154)] }),
  defineMeasurement({ id: "upper_bust_distance_right", position: 19, group: "bust", label: "Oberbrustabstand rechts", abbreviation: "oBrA", part: "rechts", page: 15, instruction: instructions.upperBustDistance, guides: [line("front", 93, 154, 93, 179), line("side", 98, 154, 98, 179)] }),
  defineMeasurement({ id: "upper_bust_distance_left", position: 19, group: "bust", label: "Oberbrustabstand links", abbreviation: "oBrA", part: "links", page: 15, instruction: instructions.upperBustDistance, guides: [line("front", 147, 154, 147, 179)] }),
  defineMeasurement({ id: "underbust_circumference", position: 20, group: "bust", label: "Unterbrustumfang", abbreviation: "uBrU", page: 15, instruction: instructions.underbustCircumference, guides: [ellipse("front", 120, 207, 42, 9), ellipse("side", 120, 207, 29, 9), ellipse("back", 120, 207, 41, 9)] }),
  defineMeasurement({ id: "underbust_distance_right", position: 21, group: "bust", label: "Unterbrustabstand rechts", abbreviation: "uBrA", part: "rechts", page: 15, instruction: instructions.underbustDistance, guides: [line("front", 93, 179, 93, 207), line("side", 98, 179, 98, 207)] }),
  defineMeasurement({ id: "underbust_distance_left", position: 21, group: "bust", label: "Unterbrustabstand links", abbreviation: "uBrA", part: "links", page: 15, instruction: instructions.underbustDistance, guides: [line("front", 147, 179, 147, 207)] }),

  defineMeasurement({ id: "shoulder_width_right", position: 22, group: "arms", label: "Schulterbreite rechts", abbreviation: "SuB", part: "rechts", page: 15, instruction: instructions.shoulderWidth, guides: [line("front", 105, 112, 73, 139), line("back", 105, 112, 73, 139)] }),
  defineMeasurement({ id: "shoulder_width_left", position: 22, group: "arms", label: "Schulterbreite links", abbreviation: "SuB", part: "links", page: 15, instruction: instructions.shoulderWidth, guides: [line("front", 135, 112, 167, 139), line("back", 135, 112, 167, 139)] }),
  defineMeasurement({ id: "arm_length_right", position: 23, group: "arms", label: "Armlänge rechts", abbreviation: "ArL", part: "rechts", page: 15, instruction: instructions.armLength, guides: [path("front", "M73 139 C58 203 53 269 47 348") ] }),
  defineMeasurement({ id: "arm_length_left", position: 23, group: "arms", label: "Armlänge links", abbreviation: "ArL", part: "links", page: 15, instruction: instructions.armLength, guides: [path("front", "M167 139 C182 203 187 269 193 348") ] }),
  defineMeasurement({ id: "upper_arm_circumference_right", position: 24, group: "arms", label: "Oberarmumfang rechts", abbreviation: "OaU", part: "rechts", page: 15, instruction: instructions.upperArmCircumference, guides: [ellipse("front", 63, 187, 11, 5), ellipse("side", 84, 187, 11, 5)] }),
  defineMeasurement({ id: "upper_arm_circumference_left", position: 24, group: "arms", label: "Oberarmumfang links", abbreviation: "OaU", part: "links", page: 15, instruction: instructions.upperArmCircumference, guides: [ellipse("front", 177, 187, 11, 5), ellipse("side", 156, 187, 11, 5)] }),
  defineMeasurement({ id: "wrist_circumference_right", position: 25, group: "arms", label: "Handgelenkumfang rechts", abbreviation: "HagU", part: "rechts", page: 15, instruction: instructions.wristCircumference, guides: [ellipse("front", 47, 342, 8, 4)] }),
  defineMeasurement({ id: "wrist_circumference_left", position: 25, group: "arms", label: "Handgelenkumfang links", abbreviation: "HagU", part: "links", page: 15, instruction: instructions.wristCircumference, guides: [ellipse("front", 193, 342, 8, 4)] }),
  defineMeasurement({ id: "hand_circumference_right", position: 26, group: "arms", label: "Handumfang rechts", abbreviation: "HdU", part: "rechts", page: 15, instruction: instructions.handCircumference, guides: [ellipse("front", 45, 365, 10, 6)] }),
  defineMeasurement({ id: "hand_circumference_left", position: 26, group: "arms", label: "Handumfang links", abbreviation: "HdU", part: "links", page: 15, instruction: instructions.handCircumference, guides: [ellipse("front", 195, 365, 10, 6)] }),
  defineMeasurement({ id: "armscye_circumference_right", position: 27, group: "arms", label: "Armansatzumfang rechts", abbreviation: "AraU", part: "rechts", page: 15, instruction: instructions.armscyeCircumference, guides: [ellipse("front", 74, 151, 14, 20), ellipse("side", 83, 151, 14, 20)] }),
  defineMeasurement({ id: "armscye_circumference_left", position: 27, group: "arms", label: "Armansatzumfang links", abbreviation: "AraU", part: "links", page: 15, instruction: instructions.armscyeCircumference, guides: [ellipse("front", 166, 151, 14, 20), ellipse("side", 157, 151, 14, 20)] }),
  defineMeasurement({ id: "shoulder_angle_right", position: 28, group: "arms", label: "Schulterwinkel rechts", abbreviation: "SuWi", part: "rechts", unit: "deg", page: 15, instruction: instructions.shoulderAngle, guides: [path("front", "M105 112 L73 139 M105 112 L73 112"), path("back", "M105 112 L73 139 M105 112 L73 112")] }),
  defineMeasurement({ id: "shoulder_angle_left", position: 28, group: "arms", label: "Schulterwinkel links", abbreviation: "SuWi", part: "links", unit: "deg", page: 15, instruction: instructions.shoulderAngle, guides: [path("front", "M135 112 L167 139 M135 112 L167 112"), path("back", "M135 112 L167 139 M135 112 L167 112")] })
]);

const measurementsById = new Map(BRIDAL_BODY_MEASUREMENTS.map((measurement) => [measurement.id, measurement]));

export function getBodyMeasurement(measurementId) {
  return measurementsById.get(measurementId) || null;
}

export function validateMeasurementValue(value) {
  if (typeof value === "string" && value.trim() === "") {
    throw new TypeError("Messwert muss eine endliche positive Zahl sein.");
  }
  const numericValue = Number(value);
  if (!Number.isFinite(numericValue) || numericValue <= 0) {
    throw new TypeError("Messwert muss eine endliche positive Zahl sein.");
  }
  return numericValue;
}

export function createBridalMeasurementProfile({ shapeId, values = {} }) {
  if (!BRIDAL_SHAPE_IDS.includes(shapeId)) {
    throw new TypeError(`Unbekannte Grundform: ${shapeId}`);
  }

  for (const measurementId of Object.keys(values)) {
    if (!measurementsById.has(measurementId)) {
      throw new TypeError(`Unbekannte Maß-ID: ${measurementId}`);
    }
  }

  const measurements = [];
  for (const definition of BRIDAL_BODY_MEASUREMENTS) {
    const rawValue = values[definition.id];
    if (rawValue === "" || rawValue === null || rawValue === undefined) continue;
    measurements.push(Object.freeze({
      id: definition.id,
      abbreviation: definition.abbreviation,
      value: validateMeasurementValue(rawValue),
      unit: definition.unit
    }));
  }

  return Object.freeze({ shapeId, measurements: Object.freeze(measurements) });
}
