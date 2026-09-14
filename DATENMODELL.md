# Globales Datenmodell

## Zweck

Alle Module tauschen klar benannte, versionierte Daten aus. Körpermaße, Entscheidungen, Berechnungen und Geometrie bleiben getrennt und nachvollziehbar.

## Gemeinsame Datentypen

Die Typen beschreiben die verbindliche Bedeutung an Modulgrenzen. Python darf sie als unveränderliche Dataclasses, JavaScript als validierte Objekte abbilden.

| Typ | Pflichtinhalt |
|---|---|
| `MeasurementValue` | `id`, `value`, `unit`, optional `side` |
| `ObservationValue` | `id`, `value`, optional `unit`, `note` |
| `ChoiceValue` | `id`, `value`, optional `unit`, `origin` (`default` oder `user`) |
| `DerivedValue` | `id`, `value`, `unit`, `depends_on`, `rule_ref` |
| `SourceRef` | `source_id`, `page`, optional `rule_id`, `status` |
| `Point` | `x_mm`, `y_mm` |
| `Line` | `start`, `end` |
| `CubicBezier` | `p0`, `p1`, `p2`, `p3` |
| `Path` | geordnete Linien/Kurven, `closed` |
| `Connection` | `id`, `kind`, `geometry_ref`, erlaubte Gegenanschlüsse |
| `PatternPiece` | `id`, `name`, Naht- und Schnittpfad, Anschlüsse, Markierungen, Zuschnittangabe, Status |
| `Provenance` | Quellen, Regeln, Eingaben, Entscheidungen und Vertragsversion |
| `ValidationIssue` | `code`, `message`, optional `data_ref` oder `geometry_ref` |
| `ValidationResult` | `valid`, Liste der `issues` |
| `ModuleRequest` | `module_id`, `contract_version`, benötigte Werte, Entscheidungen und Geometrieanschlüsse |
| `ModuleResult` | `module_id`, `contract_version`, erzeugte Werte, Geometrie, Anschlüsse, Provenienz und Validierung |

Ein lokaler Bausteinvertrag legt nur fest, welche dieser Typen und IDs der Baustein annimmt und zurückgibt. Adapter dürfen vorhandene Namen oder Zentimeterwerte übersetzen; innerhalb der Engine gelten die Typen und Millimeterkonventionen dieser Datei.

## Zentrale Datenobjekte

### 1. Personenprofil

- stabile ID und Name;
- gemessene Körpermaße mit Maß-ID, Wert und Einheit;
- getrennte Seitenwerte bleiben getrennt;
- Figurbeobachtungen und Notizen sind keine Körpermaße;
- fehlende Werte bleiben sichtbar und werden nicht geschätzt.

### 2. Schnittauftrag

- gewünschtes Kleidungsstück;
- gewählte Bausteine und erlaubte Positionen aus dem Patchwork-Modul;
- Modell-, Passform- und Konstruktionsentscheidungen;
- Verweis auf das verwendete Personenprofil.

### 3. Bausteinvertrag

Jeder anschlussfähige Baustein benennt:

- stabile ID und Vertragsversion;
- Zweck, Status und Quellenbezug;
- benötigte Eingaben und erzeugte Ausgaben;
- unterstützte Kleidungsstücke, Positionen und Anschlussstellen;
- Vorbedingungen, Fehlerfälle und Prüfungen.

### 4. Konstruktionsstand

- verwendete Eingaben und Entscheidungen;
- abgeleitete Konstruktionswerte;
- Punkte, Linien, Kurven, Flächen und Schnittteile;
- Provenienz: Regel, Quelle, Abhängigkeiten und Bausteinversion;
- Validierungsstatus und offene Fehler.

### 5. Schnittteil

- stabile Teil-ID und Bezeichnung;
- Nahtlinie und Schnittlinie;
- Anschlusskanten und zugehörige Gegenkanten;
- Abnäher, Knipse, Fadenlauf und Beschriftungen;
- Zuschnittangabe, Lage und Symmetrie;
- Status von Arbeitskontur bis fachlich freigegeben.

### 6. Ausgabe

DXF, SVG und maßstäbliche PDF werden aus demselben geprüften Konstruktionsstand erzeugt. Die Ausgabe berechnet das Kleidungsstück nicht neu.

## Verbindliche Regeln

- Eingabe darf in der erfassten Einheit bleiben; an der Engine-Grenze wird einmalig in Millimeter umgerechnet.
- Interne Längen tragen `_mm`, Winkel ihre Einheit im Namen; Zwischenwerte werden nicht gerundet.
- IDs und Feldbedeutungen bleiben über Modulgrenzen stabil.
- Körpermaß, Beobachtung, Wahlwert und berechneter Wert dürfen nicht vermischt werden.
- Jede Ableitung nennt ihre Eingaben und ihren Quellen- oder Regelbezug.
- Fehlende, ungültige oder fachlich offene Daten erzeugen einen sichtbaren Zustand statt eines stillen Ersatzwerts.
- Technische Prüfung, CLO-Prüfung, Nessel und Anprobe bleiben getrennte Nachweise.

## Datenfluss

```text
Personenprofil + Schnittauftrag
            ↓
      Konstruktionsbausteine
            ↓
       Konstruktionsstand
            ↓
   Prüfung und Aufbereitung
            ↓
       DXF + SVG + PDF
```
