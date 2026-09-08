"""Vertragstests für zwei hintere Abnäher auf S. 35."""

from __future__ import annotations

import unittest

from zwei_hintere_abnaeher import Punkt2D, zwei_hintere_abnaeher_konstruieren


BUCH_EINGABEN = dict(
    p7=Punkt2D(250.0, 0.0),
    p8=Punkt2D(250.0, 500.0),
    hintere_mitte=Punkt2D(500.0, 0.0),
    hinterer_hueftbogenpunkt=Punkt2D(280.0, -10.0),
    taillenausfall_mm=130.0,
    hueftabstich_mm=60.0,
    vorderer_abnaeherinhalt_mm=15.0,
    hinterer_gesamtinhalt_mm=55.0,
    inhaltsdifferenz_mm=5.0,
    positionskorrektur_erster_abnaeher_mm=0.0,
    taillenerhoehung_seitenlinie_mm=10.0,
    taillenerhoehung_vorderer_abnaeher_mm=5.0,
    taillenerhoehung_erster_hinterer_abnaeher_mm=10.0 / 3.0,
    laenge_erster_hinterer_abnaeher_mm=145.0,
    laenge_zweiter_hinterer_abnaeher_mm=130.0,
)


class ZweiHintereAbnaeherTest(unittest.TestCase):
    def test_buchwerte_werden_aufgeteilt_positioniert_und_kontrolliert(self) -> None:
        konstruktion = zwei_hintere_abnaeher_konstruieren(**BUCH_EINGABEN)

        self.assertEqual(konstruktion.erster_abnaeher.inhalt_mm, 30.0)
        self.assertEqual(konstruktion.zweiter_abnaeher.inhalt_mm, 25.0)
        self.assertEqual(konstruktion.kontrollsumme_mm, 130.0)
        self.assertTrue(konstruktion.verteilung_ist_vollstaendig)

        self.assertAlmostEqual(
            konstruktion.erster_abnaeher.mitte.x_mm,
            500.0 - 250.0 / 3.0,
        )
        self.assertAlmostEqual(
            konstruktion.erster_abnaeher.mitte.y_mm,
            -10.0 / 3.0,
        )
        self.assertAlmostEqual(
            konstruktion.zweiter_abnaeher.mitte.x_mm,
            340.8333333333333,
        )
        self.assertEqual(konstruktion.zweiter_abnaeher.mitte.y_mm, -5.0)
        self.assertEqual(konstruktion.provenienz.formula_ids, ("HOF-B1-S035-F01",))
        self.assertEqual(konstruktion.provenienz.source_page, 35)

    def test_inhaltsdifferenz_und_maximalinhalt_folgen_der_buchregel(self) -> None:
        for differenz_mm in (4.9, 10.1):
            with self.subTest(differenz_mm=differenz_mm):
                eingaben = dict(BUCH_EINGABEN)
                eingaben["inhaltsdifferenz_mm"] = differenz_mm
                with self.assertRaises(ValueError) as context:
                    zwei_hintere_abnaeher_konstruieren(**eingaben)
                self.assertEqual(
                    context.exception.__class__.__name__,
                    "WertAusserhalbBereichError",
                )

        eingaben = dict(BUCH_EINGABEN)
        eingaben["hinterer_gesamtinhalt_mm"] = 90.0
        with self.assertRaises(ValueError) as context:
            zwei_hintere_abnaeher_konstruieren(**eingaben)
        self.assertEqual(
            context.exception.__class__.__name__,
            "WertAusserhalbBereichError",
        )

    def test_position_laengen_und_erhoehungen_folgen_den_buchbereichen(self) -> None:
        for name, wert in (
            ("positionskorrektur_erster_abnaeher_mm", -0.1),
            ("positionskorrektur_erster_abnaeher_mm", 10.1),
            ("laenge_erster_hinterer_abnaeher_mm", 129.9),
            ("laenge_erster_hinterer_abnaeher_mm", 160.1),
            ("laenge_zweiter_hinterer_abnaeher_mm", 119.9),
            ("laenge_zweiter_hinterer_abnaeher_mm", 140.1),
        ):
            with self.subTest(name=name, wert=wert):
                eingaben = dict(BUCH_EINGABEN)
                eingaben[name] = wert
                with self.assertRaises(ValueError):
                    zwei_hintere_abnaeher_konstruieren(**eingaben)

        for name, wert in (
            ("taillenerhoehung_erster_hinterer_abnaeher_mm", 3.0),
            ("taillenerhoehung_vorderer_abnaeher_mm", 4.9),
        ):
            with self.subTest(name=name):
                eingaben = dict(BUCH_EINGABEN)
                eingaben[name] = wert
                with self.assertRaises(ValueError):
                    zwei_hintere_abnaeher_konstruieren(**eingaben)


if __name__ == "__main__":
    unittest.main(verbosity=2)
