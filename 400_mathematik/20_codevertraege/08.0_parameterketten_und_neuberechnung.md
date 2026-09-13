# Parameterketten und Neuberechnung

**Status:** `bereit`

**Herleitung:** [`13_parametrische_masse_und_abhaengigkeitskette.md`](../90_recherche/13_parametrische_masse_und_abhaengigkeitskette.md), [`14_aenderung_und_neuberechnung.md`](../90_recherche/14_aenderung_und_neuberechnung.md).

## Schichten

```text
Quellenwerte
  → fachlich normalisierte Parameter
  → mathematische Hilfswerte
  → Konstruktionspunkte und -pfade
  → Prüfwerte
  → Ausgabegeometrie
```

Jeder abgeleitete Wert besitzt genau eine Rechenquelle. Eingaben, Zugaben, Auswahlentscheidungen und Ergebnisse werden nicht unter demselben Namen überschrieben.

## Daten- und Ergebnisstrukturen

```python
ParameterSpec(
    name: str,
    unit: str | None,
    kind: INPUT | DECISION | DERIVED | CHECK,
    dependencies: tuple[str, ...],
    compute_id: str | None,
    source_ref: str | None,
    validator_id: str,
    contract_version: str,
)
ValueRecord(name, value, unit, kind, source_ref, formula_id)
RecomputeResult(values, evaluation_order, errors, provenance)
```

`compute_id` und `validator_id` verweisen auf versionierte reine Funktionen. `INPUT` und `DECISION` besitzen kein `compute_id`; `DERIVED` und `CHECK` müssen eines besitzen. Namen sind innerhalb einer Funktionsscheibe eindeutig.

## Zielprimitiven

```python
validate_parameter_specs(specs) -> ValidationResult
topological_order(specs) -> tuple[str, ...]
recompute(specs, inputs, decisions, function_registry) -> RecomputeResult
```

## Ausführungsalgorithmus

1. Namen, Einheiten, Quellenfelder und Abhängigkeitsnamen validieren.
2. Mit Kahns Algorithmus eine stabile topologische Reihenfolge bilden; bei mehreren freien Knoten lexikografisch nach Namen ordnen.
3. Fehlende `INPUT`- oder `DECISION`-Werte vor der Berechnung melden.
4. Werte in Reihenfolge berechnen und jeden Wert unmittelbar mit seinem `validator_id` prüfen.
5. Beim ersten Fehler stoppen und bereits berechnete Werte sowie den typisierten Fehler im Ergebnis ausweisen; keine abhängigen Scheinwerte erzeugen.
6. Eingaben, Entscheidungen und abgeleitete Werte getrennt als `ValueRecord` zurückgeben.

## Zielmuster

```python
result = recompute(specs, input_data, decisions, function_registry)
```

- gleiche Eingaben und dieselbe Vertragsversion ergeben dieselbe Ausgabe;
- keine versteckten globalen Werte;
- keine Mutation der Eingaben;
- jede Fachformel kann über ihre Quellen-ID zurückverfolgt werden;
- Neuberechnung darf zunächst die gesamte kleine Funktionsscheibe erneut ausführen. Ein Dirty-Node-System ist keine Voraussetzung.

## Abhängigkeitsgraph

Ein berechneter Wert benennt seine direkten Vorgänger. Zyklen sind unzulässig, sofern kein ausdrücklich dokumentiertes numerisches Lösungsverfahren eingesetzt wird.

```text
input → derived measure → point → path → check
```

Ein allgemeiner Constraint-Solver wird nicht vorsorglich gebaut. Zielwertprobleme, beispielsweise Kurvenlängenpassung, erhalten eine kleine lokal begrenzte Solver-Funktion mit Intervall, Abbruchbedingung und Nichtkonvergenz-Fehler.

## Fachliche Auswahlregeln

Bereiche wie `4 bis 6 cm` oder Wörter wie `nach Bedarf`, `schön ausformen` und `je nach Hüftform` sind keine automatisch ausführbaren Zahlen. Die Funktionsschicht muss sie als eine der folgenden Formen führen:

- explizite Benutzereingabe;
- belegte Auswahlregel;
- offener Entscheidungspunkt;
- manuelle/visuelle Operation ohne automatische Berechnung.

## Provenienz je Ergebnis

Mindestens:

```text
source_page
formula_id oder source_statement
math_contract
input_names
selected_options
contract_version
```

## Fehlerfälle

- fehlende Pflichtquelle oder Auswahl → typisierter Stop;
- widersprüchliche Fachwerte → `gesperrt`;
- zyklische Abhängigkeit → `DependencyCycleError`;
- Nichtkonvergenz → `ConvergenceError` mit Restfehler und Iterationszahl.

## Invarianten und Prüffälle

- Änderung eines Eingabewerts beeinflusst nur davon abhängige Ergebnisse semantisch.
- unveränderte Eingabe ergibt byte-stabil serialisierbare numerische Daten, sofern Reihenfolgen festgelegt sind.
- Beispielkette `4 cm → 40 mm → Punktverschiebung 40 mm` bleibt ohne Zwischenrundung konsistent.
- Quellenwerte und berechnete Werte sind im Ergebnis getrennt sichtbar.

Konkrete Prüffälle:

| Fall | Erwartung |
|---|---|
| `INPUT a=4`, `DERIVED b=2×a` | Reihenfolge `a,b`; `b=8` |
| unabhängige Knoten `z` und `a` | stabile Reihenfolge `a,z` |
| `a` hängt von `b`, `b` von `a` ab | `DependencyCycleError`, keine Werte |
| Pflichtinput fehlt | typisierter Eingabefehler vor erster Berechnung |
| gleicher Spec-/Input-/Registry-Stand zweimal | identische Werte, Reihenfolge und Provenienz |
