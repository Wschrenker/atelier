"""Vertragstests für zwei hintere Abnäher auf S. 35."""

from __future__ import annotations

import math
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

    def test_widerspruechliche_verteilung_stoppt_vor_der_geometrie(self) -> None:
        eingaben = dict(BUCH_EINGABEN)
        eingaben["hinterer_gesamtinhalt_mm"] = 50.0

        with self.assertRaises(ValueError) as context:
            zwei_hintere_abnaeher_konstruieren(**eingaben)

        self.assertEqual(
            context.exception.__class__.__name__,
            "InkonsistenteVerteilungError",
        )

    def test_entartete_oder_schiefe_grundgeometrie_stoppt_typisiert(self) -> None:
        for name, wert in (
            ("p7", Punkt2D(500.0, 0.0)),
            ("p8", Punkt2D(250.0, 0.0)),
            ("p8", Punkt2D(500.0, 500.0)),
        ):
            with self.subTest(name=name, wert=wert):
                eingaben = dict(BUCH_EINGABEN)
                eingaben[name] = wert
                with self.assertRaises(ValueError) as context:
                    zwei_hintere_abnaeher_konstruieren(**eingaben)
                self.assertEqual(
                    context.exception.__class__.__name__,
                    "GeometrieVertragError",
                )

    def test_nicht_endliche_masswerte_stoppen_vor_der_berechnung(self) -> None:
        for name, wert in (
            ("taillenausfall_mm", math.inf),
            ("hueftabstich_mm", math.nan),
            ("hinterer_gesamtinhalt_mm", -math.inf),
        ):
            with self.subTest(name=name):
                eingaben = dict(BUCH_EINGABEN)
                eingaben[name] = wert
                with self.assertRaises(ValueError) as context:
                    zwei_hintere_abnaeher_konstruieren(**eingaben)
                self.assertEqual(
                    context.exception.__class__.__name__,
                    "NichtEndlicherWertError",
                )

    def test_negative_verteilungswerte_werden_nicht_als_geometrie_akzeptiert(self) -> None:
        faelle = (
            ("taillenausfall_mm", 0.0),
            ("hueftabstich_mm", -1.0),
            ("vorderer_abnaeherinhalt_mm", -1.0),
            ("hinterer_gesamtinhalt_mm", -1.0),
        )
        for name, wert in faelle:
            with self.subTest(name=name):
                eingaben = dict(BUCH_EINGABEN)
                eingaben[name] = wert
                with self.assertRaises(ValueError) as context:
                    zwei_hintere_abnaeher_konstruieren(**eingaben)
                self.assertEqual(
                    context.exception.__class__.__name__,
                    "WertAusserhalbBereichError",
                )

    def test_abnaeher_und_hueftbogen_muessen_im_rueckteil_liegen(self) -> None:
        zu_schmal = dict(BUCH_EINGABEN)
        zu_schmal.update(
            p7=Punkt2D(470.0, 0.0),
            p8=Punkt2D(470.0, 500.0),
            hinterer_hueftbogenpunkt=Punkt2D(475.0, -10.0),
        )
        ausserhalb = dict(BUCH_EINGABEN)
        ausserhalb["hinterer_hueftbogenpunkt"] = Punkt2D(520.0, -10.0)

        for eingaben in (zu_schmal, ausserhalb):
            with self.subTest(eingaben=eingaben):
                with self.assertRaises(ValueError) as context:
                    zwei_hintere_abnaeher_konstruieren(**eingaben)
                self.assertEqual(
                    context.exception.__class__.__name__,
                    "PositionAusserhalbRueckteilError",
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
