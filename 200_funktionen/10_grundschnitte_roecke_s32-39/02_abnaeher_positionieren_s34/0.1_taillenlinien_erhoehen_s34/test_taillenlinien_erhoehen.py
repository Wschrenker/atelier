"""Vertragstests fuer die erhoehten Taillenlinien auf S. 34."""

from __future__ import annotations

import math
import unittest

from taillenlinien_erhoehen import (
    GeometrieVertragError,
    Punkt2D,
    Taillenlinienstatus,
    WertAusserhalbBereichError,
    taillenlinien_erhoehen,
)


class TaillenlinienErhoehenTest(unittest.TestCase):
    def test_buchgeometrie_erzeugt_p10_und_exakten_drittelwert(self) -> None:
        ergebnis = taillenlinien_erhoehen(
            p7=Punkt2D(250.0, 0.0),
            p8=Punkt2D(250.0, 500.0),
            taillenlinie_start=Punkt2D(0.0, 0.0),
            taillenlinie_ende=Punkt2D(500.0, 0.0),
            taillenerhoehung_seitenlinie_mm=10.0,
            taillenerhoehung_vorderer_abnaeher_mm=5.0,
        )

        self.assertEqual(ergebnis.p10, Punkt2D(250.0, -10.0))
        self.assertEqual(ergebnis.erhoehungsrichtung, (0.0, -1.0))
        self.assertEqual(ergebnis.taillenrichtung, (1.0, 0.0))
        self.assertEqual(ergebnis.taillenerhoehung_hinterer_abnaeher_mm, 10.0 / 3.0)
        self.assertEqual(ergebnis.status, Taillenlinienstatus.VOLLSTAENDIG)

    def test_buchbereiche_sind_inklusiv_und_werden_nicht_geklemmt(self) -> None:
        for seite_mm in (10.0, 15.0):
            for vorne_mm in (5.0, 7.0):
                with self.subTest(seite_mm=seite_mm, vorne_mm=vorne_mm):
                    ergebnis = taillenlinien_erhoehen(
                        p7=Punkt2D(0.0, 0.0),
                        p8=Punkt2D(0.0, 100.0),
                        taillenlinie_start=Punkt2D(-100.0, 0.0),
                        taillenlinie_ende=Punkt2D(100.0, 0.0),
                        taillenerhoehung_seitenlinie_mm=seite_mm,
                        taillenerhoehung_vorderer_abnaeher_mm=vorne_mm,
                    )
                    self.assertEqual(ergebnis.p10.y_mm, -seite_mm)

        for name, seite_mm, vorne_mm in (
            ("taillenerhoehung_seitenlinie_mm", 9.9, 5.0),
            ("taillenerhoehung_seitenlinie_mm", 15.1, 5.0),
            ("taillenerhoehung_vorderer_abnaeher_mm", 10.0, 4.9),
            ("taillenerhoehung_vorderer_abnaeher_mm", 10.0, 7.1),
        ):
            with self.subTest(name=name):
                with self.assertRaises(WertAusserhalbBereichError) as context:
                    taillenlinien_erhoehen(
                        p7=Punkt2D(0.0, 0.0),
                        p8=Punkt2D(0.0, 100.0),
                        taillenlinie_start=Punkt2D(-100.0, 0.0),
                        taillenlinie_ende=Punkt2D(100.0, 0.0),
                        taillenerhoehung_seitenlinie_mm=seite_mm,
                        taillenerhoehung_vorderer_abnaeher_mm=vorne_mm,
                    )
                self.assertEqual(context.exception.wert_name, name)

    def test_beliebige_rechtwinklige_ausrichtung_bleibt_richtungsgetreu(self) -> None:
        ergebnis = taillenlinien_erhoehen(
            p7=Punkt2D(10.0, 20.0),
            p8=Punkt2D(110.0, 20.0),
            taillenlinie_start=Punkt2D(10.0, -80.0),
            taillenlinie_ende=Punkt2D(10.0, 120.0),
            taillenerhoehung_seitenlinie_mm=15.0,
            taillenerhoehung_vorderer_abnaeher_mm=7.0,
        )

        self.assertEqual(ergebnis.p10, Punkt2D(-5.0, 20.0))
        self.assertEqual(ergebnis.erhoehungsrichtung, (-1.0, 0.0))
        self.assertEqual(ergebnis.taillenrichtung, (0.0, 1.0))

    def test_nicht_endliche_entartete_oder_schiefe_geometrie_stoppt(self) -> None:
        faelle = (
            dict(p7=Punkt2D(math.nan, 0.0), p8=Punkt2D(0.0, 100.0)),
            dict(p7=Punkt2D(0.0, 0.0), p8=Punkt2D(0.0, 0.0)),
            dict(p7=Punkt2D(0.0, 0.0), p8=Punkt2D(100.0, 100.0)),
        )
        for ersatz in faelle:
            with self.subTest(ersatz=ersatz):
                eingaben = dict(
                    p7=Punkt2D(0.0, 0.0),
                    p8=Punkt2D(0.0, 100.0),
                    taillenlinie_start=Punkt2D(-100.0, 0.0),
                    taillenlinie_ende=Punkt2D(100.0, 0.0),
                    taillenerhoehung_seitenlinie_mm=10.0,
                    taillenerhoehung_vorderer_abnaeher_mm=5.0,
                )
                eingaben.update(ersatz)
                with self.assertRaises(GeometrieVertragError):
                    taillenlinien_erhoehen(**eingaben)

    def test_provenienz_benennt_quelle_formel_und_entscheidungen(self) -> None:
        ergebnis = taillenlinien_erhoehen(
            p7=Punkt2D(250.0, 0.0),
            p8=Punkt2D(250.0, 500.0),
            taillenlinie_start=Punkt2D(0.0, 0.0),
            taillenlinie_ende=Punkt2D(500.0, 0.0),
            taillenerhoehung_seitenlinie_mm=10.0,
            taillenerhoehung_vorderer_abnaeher_mm=5.0,
        )

        self.assertEqual(ergebnis.provenienz.source_page, 34)
        self.assertEqual(ergebnis.provenienz.formula_ids, ("HOF-B1-S034-F02",))
        self.assertEqual(
            ergebnis.provenienz.selected_options,
            (
                ("taillenerhoehung_seitenlinie_mm", 10.0),
                ("taillenerhoehung_vorderer_abnaeher_mm", 5.0),
            ),
        )
        self.assertEqual(ergebnis.provenienz.contract_version, "1.0.0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
