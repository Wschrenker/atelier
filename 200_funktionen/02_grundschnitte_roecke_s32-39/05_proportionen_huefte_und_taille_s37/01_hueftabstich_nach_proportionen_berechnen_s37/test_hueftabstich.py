"""Technische Beispiele zu S. 37, keine dort gedruckten Buchmaße."""

import unittest

from hueftabstich import Figurform, hueftabstich_berechnen


class HueftabstichTest(unittest.TestCase):
    def test_fachentscheidungen_sind_pflicht_ohne_fallback(self):
        basis = dict(
            taillenausfall_mm=130.0,
            figurform=Figurform.BREITE_HUEFTE_FLACHES_GESAESS,
            hueftform_korrektur_mm=10.0,
        )
        for name in ("figurform", "hueftform_korrektur_mm"):
            with self.subTest(fehlend=name):
                ohne = {k: v for k, v in basis.items() if k != name}
                with self.assertRaises(TypeError):
                    hueftabstich_berechnen(**ohne)
            with self.subTest(leer=name):
                with self.assertRaises(ValueError) as ctx:
                    hueftabstich_berechnen(**(basis | {name: None}))
                self.assertEqual(type(ctx.exception).__name__, "EntscheidungFehltError")
        for figur in ("normal", "breite_huefte_flaches_gesaess", "flach", 1, True):
            with self.subTest(figur=figur):
                with self.assertRaises(ValueError) as ctx:
                    hueftabstich_berechnen(**(basis | {"figurform": figur}))
                self.assertEqual(type(ctx.exception).__name__, "UngueltigeFigurformError")

    def test_ungueltige_zahlen_und_bereiche_werden_nicht_geklemmt(self):
        basis = dict(
            taillenausfall_mm=130.0,
            figurform=Figurform.BREITE_HUEFTE_FLACHES_GESAESS,
            hueftform_korrektur_mm=10.0,
        )
        faelle = [
            (name, wert, "NichtEndlicherWertError")
            for name in ("taillenausfall_mm", "hueftform_korrektur_mm")
            for wert in (float("nan"), float("inf"), -float("inf"))
        ] + [
            ("taillenausfall_mm", wert, "WertAusserhalbBereichError")
            for wert in (-1.0, 0.0)
        ] + [
            ("hueftform_korrektur_mm", wert, "WertAusserhalbBereichError")
            for wert in (-10.0, 0.0, 4.999, 15.001)
        ] + [
            (name, wert, "UngueltigerZahlentypError")
            for name in ("taillenausfall_mm", "hueftform_korrektur_mm")
            for wert in (True, False, "10", [], complex(10, 0))
        ] + [("taillenausfall_mm", None, "UngueltigerZahlentypError")]
        for name, wert, fehler in faelle:
            with self.subTest(name=name, wert=wert):
                with self.assertRaises((ValueError, TypeError)) as ctx:
                    hueftabstich_berechnen(**(basis | {name: wert}))
                self.assertEqual(type(ctx.exception).__name__, fehler)

    def test_abstich_darf_nicht_negativ_oder_groesser_als_taaf_sein(self):
        for figur in Figurform:
            with self.subTest(figur=figur):
                with self.assertRaises(ValueError) as ctx:
                    hueftabstich_berechnen(
                        taillenausfall_mm=29.0,
                        figurform=figur,
                        hueftform_korrektur_mm=15.0,
                    )
                self.assertEqual(type(ctx.exception).__name__, "WertAusserhalbBereichError")
        for figur, erwartet in (
            (Figurform.BREITE_HUEFTE_FLACHES_GESAESS, 30.0),
            (Figurform.SCHMALE_HUEFTE_STARKES_GESAESS, 0.0),
        ):
            ergebnis = hueftabstich_berechnen(
                taillenausfall_mm=30.0,
                figurform=figur,
                hueftform_korrektur_mm=15.0,
            )
            self.assertAlmostEqual(ergebnis.hueftabstich_mm, erwartet)

    def test_nicht_darstellbare_ganzzahl_stoppt_typisiert(self):
        for name in ("taillenausfall_mm", "hueftform_korrektur_mm"):
            with self.subTest(name=name):
                eingaben = dict(
                    taillenausfall_mm=130.0,
                    figurform=Figurform.BREITE_HUEFTE_FLACHES_GESAESS,
                    hueftform_korrektur_mm=10.0,
                )
                eingaben[name] = 10 ** 400
                with self.assertRaises((ValueError, ArithmeticError)) as ctx:
                    hueftabstich_berechnen(**eingaben)
                self.assertEqual(type(ctx.exception).__name__, "NichtEndlicherWertError")

    def test_neuberechnung_ohne_zwischenrundung_und_mit_bilanz(self):
        from decimal import Decimal
        for taaf_text in ("130.123456", "200.25", "300.777777"):
            for korrektur_text in ("5.01", "9.876543", "14.999"):
                taaf, korrektur = Decimal(taaf_text), Decimal(korrektur_text)
                ergebnisse = [
                    hueftabstich_berechnen(
                        taillenausfall_mm=float(taaf), figurform=figur,
                        hueftform_korrektur_mm=float(korrektur),
                    ) for figur in Figurform
                ]
                for ergebnis, vorzeichen in zip(ergebnisse, (1, -1)):
                    erwartet = taaf / 2 + vorzeichen * korrektur
                    self.assertAlmostEqual(ergebnis.hueftabstich_mm, float(erwartet), places=10)
                self.assertAlmostEqual(
                    sum(e.hueftabstich_mm for e in ergebnisse), float(taaf), places=10,
                )

    def test_taaf_uebergabe_aus_s33_ohne_umdeutung(self):
        import importlib.util
        from pathlib import Path
        import sys
        kapitel = Path(__file__).resolve().parents[2]
        pfad = (kapitel / "01_gerader_rock_konstruktionstabelle_und_grundgeruest_s32-33"
                / "01_konstruktionstabelle_erstellen_s32-33" / "konstruktionstabelle.py")
        name = "s37_test_vorgaenger_s33"
        spec = importlib.util.spec_from_file_location(name, pfad)
        modul = importlib.util.module_from_spec(spec)
        sys.modules[name] = modul
        try:
            spec.loader.exec_module(modul)
            taaf = modul.taillenausfall_aus_halben_weiten(500.0, 370.0)
            ergebnis = hueftabstich_berechnen(
                taillenausfall_mm=taaf,
                figurform=Figurform.BREITE_HUEFTE_FLACHES_GESAESS,
                hueftform_korrektur_mm=15.0,
            )
            self.assertAlmostEqual(ergebnis.taillenausfall_mm, 130.0)
            self.assertAlmostEqual(ergebnis.hueftabstich_mm, 80.0)
        finally:
            del sys.modules[name]

    def test_beide_figurformen_mit_bereichsgrenzen_und_provenienz(self):
        faelle = (
            (Figurform.BREITE_HUEFTE_FLACHES_GESAESS, 5.0, 70.0, "HOF-B1-S037-F01"),
            (Figurform.BREITE_HUEFTE_FLACHES_GESAESS, 12.5, 77.5, "HOF-B1-S037-F01"),
            (Figurform.BREITE_HUEFTE_FLACHES_GESAESS, 15.0, 80.0, "HOF-B1-S037-F01"),
            (Figurform.SCHMALE_HUEFTE_STARKES_GESAESS, 5.0, 60.0, "HOF-B1-S037-F02"),
            (Figurform.SCHMALE_HUEFTE_STARKES_GESAESS, 12.5, 52.5, "HOF-B1-S037-F02"),
            (Figurform.SCHMALE_HUEFTE_STARKES_GESAESS, 15.0, 50.0, "HOF-B1-S037-F02"),
        )
        for figur, korrektur, erwartet, formel_id in faelle:
            with self.subTest(figur=figur, korrektur=korrektur):
                eingaben = dict(
                    taillenausfall_mm=130.0,
                    figurform=figur,
                    hueftform_korrektur_mm=korrektur,
                )
                ergebnis = hueftabstich_berechnen(**eingaben)
                self.assertAlmostEqual(ergebnis.hueftabstich_mm, erwartet)
                self.assertEqual(ergebnis.taillenausfall_mm, 130.0)
                self.assertEqual(ergebnis.figurform, figur)
                self.assertEqual(ergebnis.hueftform_korrektur_mm, korrektur)
                self.assertEqual(ergebnis.provenienz.source_page, 37)
                self.assertEqual(ergebnis.provenienz.formula_ids, (formel_id,))
                self.assertEqual(ergebnis.provenienz.input_names, ("taillenausfall_mm",))
                self.assertEqual(dict(ergebnis.provenienz.selected_options), {
                    "figurform": figur.value,
                    "hueftform_korrektur_mm": korrektur,
                })
                self.assertEqual(ergebnis, hueftabstich_berechnen(**eingaben))


if __name__ == "__main__":
    unittest.main()
