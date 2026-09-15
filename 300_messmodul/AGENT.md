# 300_messmodul — Arbeitsregeln

## Aufgabe

`300_messmodul/` erfasst Körpermaße und getrennte Beobachtungen. An der Engine-Grenze werden Längen einmalig in Millimeter umgerechnet und gemäß `DATENMODELL.md` an die `bridal_engine_v2` übergeben.

## Direkte Kinder

- `src/` — Messlogik, Adapter, Validierung und vorhandene Konstruktionen.
- `test/` — übergreifende Modultests.
- `brautkleid-messmodul.html`, `.css` und `.js` — Benutzeroberfläche.
- `server.js`, `start-messmodul.cmd` und `package.json` — lokaler Start und Testkonfiguration.

## Grenzen

- Körpermaß, Beobachtung, Wahlwert und Ableitung nicht vermischen.
- Fehlende Werte nicht schätzen; Fehler sichtbar zurückgeben.
- Kleidungsvarianten wählt das Dashboard in `500_patchwork/`, nicht das Messmodul.
- Fachregeln und bestehende Konstruktionen nur mit geprüftem Quellen- und Vertragsbezug ändern.