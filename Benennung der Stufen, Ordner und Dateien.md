# Benennung der Stufen, Ordner und Dateien

## Grundprinzip

Die Anzahl der Ziffern vor dem Punkt zeigt die Stufe (Tiefe). Punkte stehen **nur** für Tiefe, nie für Einschübe.

| Stufe | Format              | Beispiel                  |
|-------|---------------------|----------------------------|
| 1     | 3-stellig           | `100`, `200`, `900`        |
| 2     | 2-stellig           | `10`, `20`, `90`           |
| 3     | 1-stellig           | `1`, `4`, `9`              |
| 4     | 1 Nachkommastelle   | `0.1`, `0.8`               |
| 5     | 2 Nachkommastellen  | `0.01`, `0.04`             |
| 6     | 3 Nachkommastellen  | `0.001`, `0.023`           |
| 7     | 4 Nachkommastellen  | `0.0001`, `0.0023`         |

Jede Stufe hält ihre Ziffernbreite ein — sonst ist die Tiefe am Namen nicht mehr ablesbar.

## Zehner-Lücken für Einschübe

Basis-Nummern gehen in Zehnerschritten (`10, 20, 30 … 90`). Die Lücken dazwischen (`11–19`, `21–29` …) sind für spätere Einschübe reserviert, ohne dass etwas umbenannt werden muss.

```
20_roecke/
21_roecke_uebergroessen/    ← Einschub zwischen 20 und 30
30_hosen/
```

## Überlauf: `_zz_`, `_zza_`, `_zzb_` …

Wenn die Zehner-Lücken einer Stufe aufgebraucht sind (z. B. bei `90` angekommen), wird nicht auf die nächste Ziffernbreite gesprungen (das würde die Stufen-Regel oben brechen). Stattdessen kommt der Überlauf-Marker `_zz_` — und macht innen wieder von vorne mit Zehner-Lücken:

```
900_letzte/
900_zz_10_naechste/     ← 1. Überlauf-Gruppe
900_zz_20_naechste/
...
900_zz_90_naechste/     ← auch diese Gruppe voll
900_zza_10_naechste/    ← 2. Überlauf-Gruppe, gleiches Muster
900_zza_20_naechste/
```

**Warum `zz` und nicht `z`:** Kein deutsches Wort beginnt mit "zz". Dadurch kollidiert der Marker nie mit einem echten Namen — egal wie der Nachbar-Ordner heißt (auch nicht bei Wörtern, die selbst mit "z" anfangen, z. B. "Zugabe").

Sortierung bleibt in jedem Fall korrekt: Basis < `zz_10` < `zz_20` < … < `zz_90` < `zza_10` < …

## Datei vs. Ordner

Die Regel unterscheidet nicht zwischen Datei und Ordner — beide folgen demselben Muster auf jeder Stufe. Ob aus einem Eintrag später ein Ordner wird (weil er wächst), ändert nichts an seiner Nummer.

```
01.0_abnaeher_position.md       ← Datei, offene Position
01.1_abnaeher_variante/         ← aus Datei gewachsener Ordner, Nummer bleibt gleich
├── 01_naht.md
└── 01.0_sonderfall.md
```
