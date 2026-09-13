"""Vertragstests fuer Hueftbogenpunkte und Abnaeher auf S. 34."""

from __future__ import annotations

import math
import unittest

from hueftbogen_und_abnaeher import (
    Formstatus,
    GeometrieVertragError,
    Punkt2D,
    ZweiHintereAbnaeherErforderlichError,
    hueftbogen_und_abnaeher_konstruieren,
)


BUCH_EINGABEN = dict(
    vordere_mitte=Punkt2D(0.0, 0.0),
    p7=Punkt2D(250.0, 0.0),
    p8=Punkt2D(250.0, 500.0),
    hintere_mitte=Punkt2D(500.0, 0.0),
    taillenerhoehung_seitenlinie_mm=10.0,
    taillenerhoehung_vorderer_abnaeher_mm=5.0,
    taillenerhoehung_hinterer_abnaeher_mm=10.0 / 3.0,
    hueftabstich_mm=65.0,
    taillenumfang_mm=720.0,
    vorderer_abnaeherinhalt_mm=25.0,
    hinterer_abnaeherinhalt_mm=40.0,
    vordere_abnaeherlaenge_mm=90.0,
    hintere_abnaeherlaenge_mm=145.0,
)


class HueftbogenUndAbnaeherTest(unittest.TestCase):
    def test_buchwerte_positionieren_hueftbogenpunkte_und_abnaeher(self) -> None:
        konstruktion = hueftbogen_und_abnaeher_konstruieren(**BUCH_EINGABEN)

        self.assertEqual(konstruktion.p10, Punkt2D(250.0, -10.0))
        self.assertEqual(
            konstruktion.vorderer_hueftbogenpunkt, Punkt2D(217.5, -10.0)
        )
        self.assertEqual(
            konstruktion.hinterer_hueftbogenpunkt, Punkt2D(282.5, -10.0)
        )

        vorne = konstruktion.vorderer_abnaeher
        hinten = konstruktion.hinterer_abnaeher
        self.assertIsNotNone(vorne)
        self.assertIsNotNone(hinten)
        assert vorne is not None and hinten is not None
        self.assertEqual(vorne.mitte, Punkt2D(145.5, -5.0))
        self.assertEqual(vorne.schenkel_vorne, Punkt2D(133.0, -5.0))
        self.assertEqual(vorne.schenkel_hinten, Punkt2D(158.0, -5.0))
        self.assertEqual(vorne.spitze, Punkt2D(145.5, 85.0))
        self.assertEqual(hinten.mitte.x_mm, 391.25)
        self.assertAlmostEqual(hinten.mitte.y_mm, -10.0 / 3.0)
        self.assertEqual(hinten.schenkel_vorne.x_mm, 371.25)
        self.assertEqual(hinten.schenkel_hinten.x_mm, 411.25)
        self.assertAlmostEqual(hinten.spitze.y_mm, 145.0 - 10.0 / 3.0)

    def test_abnaeherinhalte_werden_exakt_halbiert(self) -> None:
        konstruktion = hueftbogen_und_abnaeher_konstruieren(**BUCH_EINGABEN)
        assert konstruktion.vorderer_abnaeher is not None
        assert konstruktion.hinterer_abnaeher is not None

        vorne = konstruktion.vorderer_abnaeher
        hinten = konstruktion.hinterer_abnaeher
        self.assertAlmostEqual(
            vorne.schenkel_hinten.x_mm - vorne.schenkel_vorne.x_mm, 25.0
        )
        self.assertAlmostEqual(
            hinten.schenkel_hinten.x_mm - hinten.schenkel_vorne.x_mm, 40.0
        )
        self.assertAlmostEqual(
            vorne.mitte.x_mm - vorne.schenkel_vorne.x_mm,
            vorne.schenkel_hinten.x_mm - vorne.mitte.x_mm,
        )

    def test_nullinhalt_erzeugt_keinen_scheinabnaeher(self) -> None:
        eingaben = dict(BUCH_EINGABEN)
        eingaben["vorderer_abnaeherinhalt_mm"] = 0.0
        eingaben["vordere_abnaeherlaenge_mm"] = None

        konstruktion = hueftbogen_und_abnaeher_konstruieren(**eingaben)

        self.assertIsNone(konstruktion.vorderer_abnaeher)
        self.assertIsNotNone(konstruktion.hinterer_abnaeher)

    def test_buchbereiche_fuer_laengen_und_inhalte_werden_erzwungen(self) -> None:
        for name, wert in (
            ("vordere_abnaeherlaenge_mm", 79.9),
            ("vordere_abnaeherlaenge_mm", 100.1),
            ("hintere_abnaeherlaenge_mm", 129.9),
            ("hintere_abnaeherlaenge_mm", 160.1),
            ("vorderer_abnaeherinhalt_mm", 9.9),
        ):
            with self.subTest(name=name):
                eingaben = dict(BUCH_EINGABEN)
                eingaben[name] = wert
                with self.assertRaises(ValueError):
                    hueftbogen_und_abnaeher_konstruieren(**eingaben)

        eingaben = dict(BUCH_EINGABEN)
        eingaben["hinterer_abnaeherinhalt_mm"] = 45.1
        with self.assertRaises(ZweiHintereAbnaeherErforderlichError):
            hueftbogen_und_abnaeher_konstruieren(**eingaben)

    def test_hintere_erhoehung_muss_exakt_aus_schritt_12_stammen(self) -> None:
        eingaben = dict(BUCH_EINGABEN)
        eingaben["taillenerhoehung_hinterer_abnaeher_mm"] = 3.0

        with self.assertRaises(ValueError) as context:
            hueftbogen_und_abnaeher_konstruieren(**eingaben)
        self.assertEqual(
            context.exception.__class__.__name__, "InkonsistenteErhoehungError"
        )

    def test_unpassende_grundgeometrie_und_nicht_endliche_werte_stoppen(self) -> None:
        faelle = (
            ("p8", Punkt2D(250.0, 0.0)),
            ("hintere_mitte", Punkt2D(200.0, 0.0)),
            ("taillenumfang_mm", math.inf),
        )
        for name, wert in faelle:
            with self.subTest(name=name):
                eingaben = dict(BUCH_EINGABEN)
                eingaben[name] = wert
                with self.assertRaises((GeometrieVertragError, ValueError)):
                    hueftbogen_und_abnaeher_konstruieren(**eingaben)

    def test_offene_kurven_und_taillennaehte_werden_nicht_erfunden(self) -> None:
        konstruktion = hueftbogen_und_abnaeher_konstruieren(**BUCH_EINGABEN)

        self.assertEqual(konstruktion.hueftbogenstatus, Formstatus.OFFEN_BIS_S36)
        self.assertEqual(konstruktion.taillennahtstatus, Formstatus.OFFEN_BIS_S35)
        self.assertEqual(konstruktion.provenienz.source_page, 34)
        self.assertEqual(
            konstruktion.provenienz.formula_ids, ("HOF-B1-S034-F05",)
        )
        self.assertEqual(konstruktion.provenienz.contract_version, "1.0.0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
