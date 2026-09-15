# Pilotvertrag — Messmodul zum geraden Rock

## Zweck

Das Messmodul liefert für den ersten vollständigen Rock-Pilot ein gültiges Personenprofil. Die Kleidungswahl und die Rocklänge gehören zum Schnittauftrag des visuellen Dashboards, nicht zu den Körpermaßen.

## Pflichtwerte des Personenprofils

| Maß-ID | Bedeutung | Eingabe |
|---|---|---|
| `waist_circumference_horizontal` | Taillenumfang | cm |
| `hip_circumference_horizontal` | Hüftumfang | cm |
| `waist_to_hip` | gemessene Hüfttiefe | cm |

Jeder Wert ist eine endliche positive Zahl. Fehlende oder ungültige Werte bleiben sichtbar; das Modul schätzt nichts und verwendet insbesondere keinen stillen Standardwert für die Hüfttiefe.

## Übergabe an die Engine

Das Dashboard ergänzt mindestens die Wahl `straight_skirt` und den Wahlwert `model_length`. An der Grenze zur `bridal_engine_v2` werden alle Längen einmalig in Millimeter umgerechnet und als getrennte `MeasurementValue`- und `ChoiceValue`-Einträge gemäß `DATENMODELL.md` übergeben.

Der vorhandene JavaScript-Adapter arbeitet derzeit noch mit Zentimeterfeldern (`waistCm`, `hipCm`, `waistToHipCm`, `lengthCm`). Er ist die funktionierende Referenz; die spätere Millimeter-Schnittstelle ersetzt diese Übergabe kontrolliert, nicht stillschweigend.

## Referenzauftrag

- Taillenumfang: 72 cm → 720 mm
- Hüftumfang: 97 cm → 970 mm
- Hüfttiefe: 21 cm → 210 mm
- Rocklänge: 50 cm → 500 mm
- Kleidungswahl: gerader Rock

## Abnahme

Der Pilot besteht, wenn Profil und Schnittauftrag gemeinsam ohne Ersatzwerte einen validierten Rock-Auftrag erzeugen und die Engine Vorderteil, Rückenteil und Bund aus demselben nachvollziehbaren Konstruktionsstand zurückgibt. Technische Tests ersetzen nicht die getrennte Prüfung von Ausdruck und Toile.