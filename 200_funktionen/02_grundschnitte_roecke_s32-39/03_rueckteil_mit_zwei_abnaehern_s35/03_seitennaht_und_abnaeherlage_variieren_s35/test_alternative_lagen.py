"""Vertragstests für alternative Seitennaht- und Abnäherlagen auf S. 35."""

from __future__ import annotations

import math
import unittest

from alternative_lagen import (
    Punkt2D,
    abnaeher_spitze_zur_seitennaht_verschieben,
    seitennaht_oben_nach_vorn_verschieben,
)


class AlternativeLagenTest(unittest.TestCase):
    def test_seitennaht_wird_um_gewaehlte_5_mm_nach_vorn_verschoben(self) -> None:
        ergebnis = seitennaht_oben_nach_vorn_verschieben(
            seitennaht_oben=Punkt2D(250.0, -10.0),
            richtungspunkt_vorne=Punkt2D(200.0, -10.0),
            verschiebung_mm=5.0,
        )

        self.assertEqual(ergebnis.neuer_punkt, Punkt2D(245.0, -10.0))
        self.assertEqual(ergebnis.verschiebung_mm, 5.0)
        self.assertEqual(ergebnis.provenienz.source_page, 35)
        self.assertEqual(ergebnis.provenienz.source_statement, "Schritt 24")

    def test_verschobene_spitze_erhaelt_zwei_identische_schenkellaengen(self) -> None:
        ergebnis = abnaeher_spitze_zur_seitennaht_verschieben(
            schenkel_a=Punkt2D(100.0, 0.0),
            schenkel_b=Punkt2D(120.0, 0.0),
            spitze=Punkt2D(110.0, 100.0),
            richtungspunkt_seitennaht=Punkt2D(0.0, 100.0),
            verschiebung_mm=5.0,
        )

        self.assertEqual(ergebnis.neue_spitze, Punkt2D(105.0, 100.0))
        laenge_a = math.hypot(
            ergebnis.schenkel_a.x_mm - ergebnis.neue_spitze.x_mm,
            ergebnis.schenkel_a.y_mm - ergebnis.neue_spitze.y_mm,
        )
        laenge_b = math.hypot(
            ergebnis.schenkel_b.x_mm - ergebnis.neue_spitze.x_mm,
            ergebnis.schenkel_b.y_mm - ergebnis.neue_spitze.y_mm,
        )
        self.assertAlmostEqual(laenge_a, laenge_b)
        self.assertEqual(ergebnis.schenkel_b, Punkt2D(120.0, 0.0))
        self.assertEqual(ergebnis.verlaengerter_schenkel, "a")
        self.assertEqual(ergebnis.provenienz.source_statement, "Schritte 25-26")

    def test_entartete_richtungen_und_schenkel_stoppen_typisiert(self) -> None:
        with self.assertRaises(ValueError) as richtung:
            seitennaht_oben_nach_vorn_verschieben(
                seitennaht_oben=Punkt2D(250.0, -10.0),
                richtungspunkt_vorne=Punkt2D(250.0, -10.0),
                verschiebung_mm=5.0,
            )
        self.assertEqual(richtung.exception.__class__.__name__, "GeometrieVertragError")

        with self.assertRaises(ValueError) as schenkel:
            abnaeher_spitze_zur_seitennaht_verschieben(
                schenkel_a=Punkt2D(105.0, 100.0),
                schenkel_b=Punkt2D(120.0, 0.0),
                spitze=Punkt2D(110.0, 100.0),
                richtungspunkt_seitennaht=Punkt2D(0.0, 100.0),
                verschiebung_mm=5.0,
            )
        self.assertEqual(schenkel.exception.__class__.__name__, "GeometrieVertragError")

    def test_nichtpositive_verschiebung_wird_nicht_still_geklemmt(self) -> None:
        with self.assertRaises(ValueError) as context:
            seitennaht_oben_nach_vorn_verschieben(
                seitennaht_oben=Punkt2D(250.0, -10.0),
                richtungspunkt_vorne=Punkt2D(200.0, -10.0),
                verschiebung_mm=0.0,
            )
        self.assertEqual(
            context.exception.__class__.__name__,
            "WertAusserhalbBereichError",
        )

    def test_negative_und_nicht_endliche_verschiebung_stoppen_typisiert(self) -> None:
        for betrag_mm in (-5.0, math.nan, math.inf):
            with self.subTest(verschiebung_mm=betrag_mm):
                with self.assertRaises(ValueError) as context:
                    seitennaht_oben_nach_vorn_verschieben(
                        seitennaht_oben=Punkt2D(250.0, -10.0),
                        richtungspunkt_vorne=Punkt2D(200.0, -10.0),
                        verschiebung_mm=betrag_mm,
                    )
                self.assertEqual(
                    context.exception.__class__.__name__,
                    "WertAusserhalbBereichError",
                )

    def test_nicht_endliche_punktkoordinaten_stoppen_typisiert(self) -> None:
        with self.assertRaises(ValueError) as ausgangspunkt:
            seitennaht_oben_nach_vorn_verschieben(
                seitennaht_oben=Punkt2D(math.inf, -10.0),
                richtungspunkt_vorne=Punkt2D(200.0, -10.0),
                verschiebung_mm=5.0,
            )
        self.assertEqual(
            ausgangspunkt.exception.__class__.__name__,
            "GeometrieVertragError",
        )

        with self.assertRaises(ValueError) as richtungspunkt:
            seitennaht_oben_nach_vorn_verschieben(
                seitennaht_oben=Punkt2D(250.0, -10.0),
                richtungspunkt_vorne=Punkt2D(math.nan, -10.0),
                verschiebung_mm=5.0,
            )
        self.assertEqual(
            richtungspunkt.exception.__class__.__name__,
            "GeometrieVertragError",
        )

    def test_spitzenverschiebung_prueft_den_betrag_vor_der_geometrie(self) -> None:
        for betrag_mm in (0.0, -5.0, math.nan, math.inf):
            with self.subTest(verschiebung_mm=betrag_mm):
                with self.assertRaises(ValueError) as context:
                    abnaeher_spitze_zur_seitennaht_verschieben(
                        schenkel_a=Punkt2D(100.0, 0.0),
                        schenkel_b=Punkt2D(120.0, 0.0),
                        spitze=Punkt2D(110.0, 100.0),
                        richtungspunkt_seitennaht=Punkt2D(0.0, 100.0),
                        verschiebung_mm=betrag_mm,
                    )
                self.assertEqual(
                    context.exception.__class__.__name__,
                    "WertAusserhalbBereichError",
                )

    def test_entartete_richtung_der_spitzenverschiebung_stoppt_typisiert(self) -> None:
        with self.assertRaises(ValueError) as context:
            abnaeher_spitze_zur_seitennaht_verschieben(
                schenkel_a=Punkt2D(100.0, 0.0),
                schenkel_b=Punkt2D(120.0, 0.0),
                spitze=Punkt2D(110.0, 100.0),
                richtungspunkt_seitennaht=Punkt2D(110.0, 100.0),
                verschiebung_mm=5.0,
            )
        self.assertEqual(context.exception.__class__.__name__, "GeometrieVertragError")

    def test_nicht_endlicher_schenkelpunkt_stoppt_vor_der_verlaengerung(self) -> None:
        with self.assertRaises(ValueError) as context:
            abnaeher_spitze_zur_seitennaht_verschieben(
                schenkel_a=Punkt2D(math.nan, 0.0),
                schenkel_b=Punkt2D(120.0, 0.0),
                spitze=Punkt2D(110.0, 100.0),
                richtungspunkt_seitennaht=Punkt2D(0.0, 100.0),
                verschiebung_mm=5.0,
            )
        self.assertEqual(context.exception.__class__.__name__, "GeometrieVertragError")

    def test_entarteter_zweiter_schenkel_stoppt_ebenfalls(self) -> None:
        with self.assertRaises(ValueError) as context:
            abnaeher_spitze_zur_seitennaht_verschieben(
                schenkel_a=Punkt2D(100.0, 0.0),
                schenkel_b=Punkt2D(105.0, 100.0),
                spitze=Punkt2D(110.0, 100.0),
                richtungspunkt_seitennaht=Punkt2D(0.0, 100.0),
                verschiebung_mm=5.0,
            )
        self.assertEqual(context.exception.__class__.__name__, "GeometrieVertragError")


if __name__ == "__main__":
    unittest.main(verbosity=2)
