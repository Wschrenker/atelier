"""Vertragstests fuer das Grundgeruest P1-P9 auf S. 33."""

from __future__ import annotations

import math
import unittest
from unittest import mock

import grundgeruest as grundgeruest_modul
from grundgeruest import (
    Geometriestatus,
    KeinEindeutigerGeradenschnittError,
    Punkt2D,
    UngueltigerGeometriewertError,
    geradenschnitt,
    grundgeruest_zeichnen,
    mittelpunkt,
    punkt_liegt_auf_gerade,
    sind_parallel,
    stehen_rechtwinklig,
)


class GrundgeruestTest(unittest.TestCase):
    def test_buchpunkte_p1_bis_p6_folgen_x_rechts_y_unten_in_mm(self) -> None:
        geruest = grundgeruest_zeichnen(
            modelllaenge_mm=500.0,
            huefttiefe_mm=210.0,
            halbe_hueftweite_mm=500.0,
        )

        self.assertEqual(geruest.punkt("P1"), Punkt2D(0.0, 0.0))
        self.assertEqual(geruest.punkt("P2"), Punkt2D(0.0, 500.0))
        self.assertEqual(geruest.punkt("P3"), Punkt2D(0.0, 210.0))
        self.assertEqual(geruest.punkt("P4"), Punkt2D(500.0, 0.0))
        self.assertEqual(geruest.punkt("P5"), Punkt2D(500.0, 500.0))
        self.assertEqual(geruest.punkt("P6"), Punkt2D(500.0, 210.0))

    def test_p7_und_p8_halbieren_mit_der_mittelpunktprimitive(self) -> None:
        self.assertEqual(
            mittelpunkt(Punkt2D(10.0, 20.0), Punkt2D(30.0, 60.0)),
            Punkt2D(20.0, 40.0),
        )
        with mock.patch.object(
            grundgeruest_modul, "mittelpunkt", wraps=mittelpunkt
        ) as mittelpunkt_spion:
            geruest = grundgeruest_zeichnen(
                modelllaenge_mm=500.0,
                huefttiefe_mm=210.0,
                halbe_hueftweite_mm=500.0,
            )

        self.assertEqual(
            mittelpunkt_spion.call_args_list,
            [
                mock.call(Punkt2D(0.0, 0.0), Punkt2D(500.0, 0.0)),
                mock.call(Punkt2D(0.0, 500.0), Punkt2D(500.0, 500.0)),
            ],
        )
        self.assertEqual(geruest.punkt("P7"), Punkt2D(250.0, 0.0))
        self.assertEqual(geruest.punkt("P8"), Punkt2D(250.0, 500.0))
        self.assertEqual(
            geruest.punkt("P7").x_mm - geruest.punkt("P1").x_mm,
            geruest.punkt("P4").x_mm - geruest.punkt("P7").x_mm,
        )
        self.assertEqual(
            geruest.punkt("P8").x_mm - geruest.punkt("P2").x_mm,
            geruest.punkt("P5").x_mm - geruest.punkt("P8").x_mm,
        )

    def test_mittelpunkt_vermeidet_ueberlauf_bei_endlichen_koordinaten(self) -> None:
        maximum = float.fromhex("0x1.fffffffffffffp+1023")
        punkt = Punkt2D(maximum, maximum)

        self.assertEqual(mittelpunkt(punkt, punkt), punkt)

    def test_grundgeruest_vermeidet_nan_bei_endlichen_maximalwerten(self) -> None:
        maximum = float.fromhex("0x1.fffffffffffffp+1023")

        geruest = grundgeruest_zeichnen(
            modelllaenge_mm=maximum,
            huefttiefe_mm=maximum,
            halbe_hueftweite_mm=maximum,
        )

        for punkt in (
            geruest.p1,
            geruest.p2,
            geruest.p3,
            geruest.p4,
            geruest.p5,
            geruest.p6,
            geruest.p7,
            geruest.p8,
            geruest.p9,
        ):
            self.assertTrue(math.isfinite(punkt.x_mm))
            self.assertTrue(math.isfinite(punkt.y_mm))
        self.assertEqual(geruest.p9, Punkt2D(maximum / 2.0, maximum))

    def test_kleine_positive_geometrie_bleibt_skalenrichtig(self) -> None:
        geruest = grundgeruest_zeichnen(
            modelllaenge_mm=2e-9,
            huefttiefe_mm=1e-9,
            halbe_hueftweite_mm=2e-9,
        )

        self.assertEqual(geruest.p9, Punkt2D(1e-9, 1e-9))

    def test_p9_entsteht_durch_eindeutigen_geradenschnitt(self) -> None:
        self.assertEqual(
            geradenschnitt(
                Punkt2D(20.0, 0.0),
                Punkt2D(20.0, 50.0),
                Punkt2D(0.0, 30.0),
                Punkt2D(40.0, 30.0),
            ),
            Punkt2D(20.0, 30.0),
        )
        with mock.patch.object(
            grundgeruest_modul, "geradenschnitt", wraps=geradenschnitt
        ) as schnitt_spion:
            geruest = grundgeruest_zeichnen(
                modelllaenge_mm=500.0,
                huefttiefe_mm=210.0,
                halbe_hueftweite_mm=500.0,
            )

        schnitt_spion.assert_called_once_with(
            Punkt2D(250.0, 0.0),
            Punkt2D(250.0, 500.0),
            Punkt2D(0.0, 210.0),
            Punkt2D(500.0, 210.0),
        )
        self.assertEqual(geruest.punkt("P9"), Punkt2D(250.0, 210.0))

    def test_taillen_hueft_und_saumlinien_sind_parallel(self) -> None:
        geruest = grundgeruest_zeichnen(
            modelllaenge_mm=500.0,
            huefttiefe_mm=210.0,
            halbe_hueftweite_mm=500.0,
        )

        self.assertTrue(
            sind_parallel(
                geruest.punkt("P1"),
                geruest.punkt("P4"),
                geruest.punkt("P3"),
                geruest.punkt("P6"),
            )
        )
        self.assertTrue(
            sind_parallel(
                geruest.punkt("P3"),
                geruest.punkt("P6"),
                geruest.punkt("P2"),
                geruest.punkt("P5"),
            )
        )

    def test_mitten_und_seitenlinie_stehen_rechtwinklig_zu_querlinien(self) -> None:
        geruest = grundgeruest_zeichnen(
            modelllaenge_mm=500.0,
            huefttiefe_mm=210.0,
            halbe_hueftweite_mm=500.0,
        )

        for senkrechte, waagerechte in (
            (("P1", "P2"), ("P1", "P4")),
            (("P4", "P5"), ("P1", "P4")),
            (("P7", "P8"), ("P3", "P6")),
        ):
            with self.subTest(senkrechte=senkrechte, waagerechte=waagerechte):
                self.assertTrue(
                    stehen_rechtwinklig(
                        geruest.punkt(senkrechte[0]),
                        geruest.punkt(senkrechte[1]),
                        geruest.punkt(waagerechte[0]),
                        geruest.punkt(waagerechte[1]),
                    )
                )

    def test_p9_liegt_auf_seitenlinie_und_hueftlinie(self) -> None:
        geruest = grundgeruest_zeichnen(
            modelllaenge_mm=500.0,
            huefttiefe_mm=210.0,
            halbe_hueftweite_mm=500.0,
        )

        self.assertTrue(
            punkt_liegt_auf_gerade(
                geruest.punkt("P9"), geruest.punkt("P7"), geruest.punkt("P8")
            )
        )
        self.assertTrue(
            punkt_liegt_auf_gerade(
                geruest.punkt("P9"), geruest.punkt("P3"), geruest.punkt("P6")
            )
        )

    def test_provenienz_und_status_belegen_das_grundgeruest(self) -> None:
        geruest = grundgeruest_zeichnen(
            modelllaenge_mm=500.0,
            huefttiefe_mm=210.0,
            halbe_hueftweite_mm=500.0,
        )

        self.assertEqual(geruest.geometriestatus, Geometriestatus.VOLLSTAENDIG)
        self.assertEqual(geruest.provenienz.source_page, 33)
        self.assertEqual(
            geruest.provenienz.source_statement,
            "Grundgeruest P1-P9, Schritte 1-9",
        )
        self.assertEqual(
            geruest.provenienz.formula_ids,
            ("HOF-B1-S033-F03",),
        )
        self.assertEqual(
            geruest.provenienz.math_contracts,
            (
                "400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md",
                "400_mathematik/20_codevertraege/20_punkte_vektoren_geraden_und_projektion.md",
                "400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md",
            ),
        )
        self.assertEqual(
            geruest.provenienz.input_names,
            ("modelllaenge_mm", "huefttiefe_mm", "halbe_hueftweite_mm"),
        )
        self.assertEqual(geruest.provenienz.selected_options, ())
        self.assertEqual(geruest.provenienz.contract_version, "1.0.0")

    def test_entartete_geraden_stoppen_in_oeffentlichen_primitiven_typisiert(self) -> None:
        punkt = Punkt2D(10.0, 20.0)
        for primitive, argumente in (
            (sind_parallel, (punkt, punkt, Punkt2D(0.0, 0.0), Punkt2D(1.0, 0.0))),
            (
                stehen_rechtwinklig,
                (punkt, punkt, Punkt2D(0.0, 0.0), Punkt2D(0.0, 1.0)),
            ),
            (punkt_liegt_auf_gerade, (Punkt2D(99.0, 99.0), punkt, punkt)),
            (
                geradenschnitt,
                (punkt, punkt, Punkt2D(0.0, 0.0), Punkt2D(0.0, 1.0)),
            ),
        ):
            with self.subTest(primitive=primitive.__name__):
                with self.assertRaises(ValueError) as context:
                    primitive(*argumente)
                self.assertEqual(
                    context.exception.__class__.__name__,
                    "EntarteteGeradeError",
                )

    def test_nahezu_identische_geradenpunkte_gelten_als_entartet(self) -> None:
        with self.assertRaises(ValueError) as context:
            sind_parallel(
                Punkt2D(0.0, 0.0),
                Punkt2D(1e-12, 0.0),
                Punkt2D(0.0, 0.0),
                Punkt2D(1.0, 0.0),
            )
        self.assertEqual(
            context.exception.__class__.__name__,
            "EntarteteGeradeError",
        )

    def test_nicht_endliche_punkte_stoppen_in_oeffentlichen_primitiven_typisiert(self) -> None:
        nan_punkt = Punkt2D(float("nan"), 0.0)
        a = Punkt2D(0.0, 0.0)
        b = Punkt2D(10.0, 0.0)
        c = Punkt2D(0.0, 10.0)
        for primitive, argumente in (
            (mittelpunkt, (nan_punkt, b)),
            (sind_parallel, (nan_punkt, b, a, b)),
            (stehen_rechtwinklig, (nan_punkt, b, a, c)),
            (punkt_liegt_auf_gerade, (nan_punkt, a, b)),
            (geradenschnitt, (nan_punkt, b, a, c)),
        ):
            with self.subTest(primitive=primitive.__name__):
                with self.assertRaises(ValueError) as context:
                    primitive(*argumente)
                self.assertEqual(
                    context.exception.__class__.__name__,
                    "NichtEndlicherPunktError",
                )

    def test_geradenschnitt_stoppt_typisiert_wenn_er_nicht_eindeutig_ist(self) -> None:
        with self.assertRaises(KeinEindeutigerGeradenschnittError):
            geradenschnitt(
                Punkt2D(0.0, 0.0),
                Punkt2D(100.0, 0.0),
                Punkt2D(0.0, 20.0),
                Punkt2D(100.0, 20.0),
            )

    def test_nullmasse_stoppen_vor_entarteter_grundgeruestgeometrie(self) -> None:
        for wert_name in (
            "modelllaenge_mm",
            "huefttiefe_mm",
            "halbe_hueftweite_mm",
        ):
            with self.subTest(wert_name=wert_name):
                eingaben = {
                    "modelllaenge_mm": 500.0,
                    "huefttiefe_mm": 210.0,
                    "halbe_hueftweite_mm": 500.0,
                }
                eingaben[wert_name] = 0.0
                with self.assertRaises(UngueltigerGeometriewertError) as context:
                    grundgeruest_zeichnen(**eingaben)
                self.assertEqual(context.exception.wert_name, wert_name)

    def test_richtungstragende_masse_muessen_nulltoleranz_ueberschreiten(self) -> None:
        for wert_name in ("modelllaenge_mm", "halbe_hueftweite_mm"):
            with self.subTest(wert_name=wert_name):
                eingaben = {
                    "modelllaenge_mm": 500.0,
                    "huefttiefe_mm": 0.5e-9,
                    "halbe_hueftweite_mm": 500.0,
                }
                eingaben[wert_name] = 1e-9
                with self.assertRaises(UngueltigerGeometriewertError) as context:
                    grundgeruest_zeichnen(**eingaben)
                self.assertEqual(context.exception.wert_name, wert_name)

    def test_huefttiefe_unterhalb_des_saums_stoppt_typisiert(self) -> None:
        with self.assertRaises(ValueError) as context:
            grundgeruest_zeichnen(
                modelllaenge_mm=500.0,
                huefttiefe_mm=501.0,
                halbe_hueftweite_mm=500.0,
            )
        self.assertEqual(
            context.exception.__class__.__name__,
            "UngueltigeGrundgeruestProportionError",
        )

    def test_nicht_endliche_und_negative_geometrielaengen_stoppen_typisiert(self) -> None:
        with self.assertRaises(UngueltigerGeometriewertError) as nicht_endlich:
            grundgeruest_zeichnen(
                modelllaenge_mm=float("inf"),
                huefttiefe_mm=210.0,
                halbe_hueftweite_mm=500.0,
            )
        self.assertEqual(nicht_endlich.exception.wert_name, "modelllaenge_mm")

        with self.assertRaises(UngueltigerGeometriewertError) as negativ:
            grundgeruest_zeichnen(
                modelllaenge_mm=500.0,
                huefttiefe_mm=-1.0,
                halbe_hueftweite_mm=500.0,
            )
        self.assertEqual(negativ.exception.wert_name, "huefttiefe_mm")


if __name__ == "__main__":
    unittest.main(verbosity=2)
