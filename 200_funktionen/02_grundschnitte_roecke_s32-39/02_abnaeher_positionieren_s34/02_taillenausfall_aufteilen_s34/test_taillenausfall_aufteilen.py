"""Vertragstests fuer die Aufteilung des Taillenausfalls auf S. 34."""

from __future__ import annotations

import math
import unittest

from taillenausfall_aufteilen import (
    EntscheidungFehltError,
    Hueftform,
    Verteilungsstatus,
    WertAusserhalbBereichError,
    taillenausfall_aufteilen,
)


class TaillenausfallAufteilenTest(unittest.TestCase):
    def test_buchbeispiel_teilt_130_mm_vollstaendig_auf(self) -> None:
        verteilung = taillenausfall_aufteilen(
            taillenausfall_mm=130.0,
            hueftform=Hueftform.DURCHSCHNITTLICH,
            hueftform_korrektur_mm=None,
            vorderer_abnaeherinhalt_mm=25.0,
        )

        self.assertEqual(verteilung.hueftabstich_mm, 65.0)
        self.assertEqual(verteilung.vorderer_abnaeherinhalt_mm, 25.0)
        self.assertEqual(verteilung.hinterer_abnaeherinhalt_mm, 40.0)
        self.assertEqual(verteilung.kontrollsumme_mm, 130.0)
        self.assertTrue(verteilung.verteilung_ist_vollstaendig)
        self.assertEqual(
            verteilung.status,
            Verteilungsstatus.VOLLSTAENDIG_EIN_HINTERER_ABNAEHER,
        )

    def test_flache_und_starke_hueftform_verwenden_explizite_korrektur(self) -> None:
        flach = taillenausfall_aufteilen(
            taillenausfall_mm=130.0,
            hueftform=Hueftform.FLACH,
            hueftform_korrektur_mm=15.0,
            vorderer_abnaeherinhalt_mm=10.0,
        )
        stark = taillenausfall_aufteilen(
            taillenausfall_mm=130.0,
            hueftform=Hueftform.STARK,
            hueftform_korrektur_mm=10.0,
            vorderer_abnaeherinhalt_mm=25.0,
        )

        self.assertEqual(flach.hueftabstich_mm, 50.0)
        self.assertEqual(flach.hinterer_abnaeherinhalt_mm, 70.0)
        self.assertEqual(
            flach.status,
            Verteilungsstatus.ZWEI_HINTERE_ABNAEHER_ERFORDERLICH,
        )
        self.assertEqual(stark.hueftabstich_mm, 75.0)
        self.assertEqual(stark.hinterer_abnaeherinhalt_mm, 30.0)

    def test_korrektur_wird_nicht_geraten_und_nicht_unbemerkt_ignoriert(self) -> None:
        with self.assertRaises(EntscheidungFehltError):
            taillenausfall_aufteilen(
                taillenausfall_mm=130.0,
                hueftform=Hueftform.FLACH,
                hueftform_korrektur_mm=None,
                vorderer_abnaeherinhalt_mm=10.0,
            )
        with self.assertRaises(ValueError) as context:
            taillenausfall_aufteilen(
                taillenausfall_mm=130.0,
                hueftform=Hueftform.DURCHSCHNITTLICH,
                hueftform_korrektur_mm=10.0,
                vorderer_abnaeherinhalt_mm=20.0,
            )
        self.assertEqual(
            context.exception.__class__.__name__, "UnpassendeEntscheidungError"
        )

    def test_korrektur_und_vorderer_abnaeher_folgen_den_belegten_bereichen(self) -> None:
        for korrektur_mm in (10.0, 15.0):
            for vorne_mm in (0.0, 10.0, 15.0, 25.0):
                with self.subTest(korrektur_mm=korrektur_mm, vorne_mm=vorne_mm):
                    ergebnis = taillenausfall_aufteilen(
                        taillenausfall_mm=200.0,
                        hueftform=Hueftform.FLACH,
                        hueftform_korrektur_mm=korrektur_mm,
                        vorderer_abnaeherinhalt_mm=vorne_mm,
                    )
                    self.assertEqual(ergebnis.kontrollsumme_mm, 200.0)

        for name, korrektur_mm, vorne_mm in (
            ("hueftform_korrektur_mm", 9.9, 10.0),
            ("hueftform_korrektur_mm", 15.1, 10.0),
            ("vorderer_abnaeherinhalt_mm", 10.0, 9.9),
            ("vorderer_abnaeherinhalt_mm", 10.0, 25.1),
        ):
            with self.subTest(name=name):
                with self.assertRaises(WertAusserhalbBereichError) as context:
                    taillenausfall_aufteilen(
                        taillenausfall_mm=200.0,
                        hueftform=Hueftform.FLACH,
                        hueftform_korrektur_mm=korrektur_mm,
                        vorderer_abnaeherinhalt_mm=vorne_mm,
                    )
                self.assertEqual(context.exception.wert_name, name)

    def test_negativer_rest_und_nicht_endliche_werte_stoppen_typisiert(self) -> None:
        with self.assertRaises(ValueError) as negativ:
            taillenausfall_aufteilen(
                taillenausfall_mm=30.0,
                hueftform=Hueftform.STARK,
                hueftform_korrektur_mm=15.0,
                vorderer_abnaeherinhalt_mm=25.0,
            )
        self.assertEqual(negativ.exception.__class__.__name__, "NegativerRestbetragError")

        for name, wert in (
            ("taillenausfall_mm", math.inf),
            ("vorderer_abnaeherinhalt_mm", math.nan),
        ):
            with self.subTest(name=name):
                eingaben = dict(
                    taillenausfall_mm=130.0,
                    hueftform=Hueftform.DURCHSCHNITTLICH,
                    hueftform_korrektur_mm=None,
                    vorderer_abnaeherinhalt_mm=20.0,
                )
                eingaben[name] = wert
                with self.assertRaises(ValueError):
                    taillenausfall_aufteilen(**eingaben)

    def test_provenienz_ist_von_der_gewaehlten_hueftform_abhaengig(self) -> None:
        flach = taillenausfall_aufteilen(
            taillenausfall_mm=130.0,
            hueftform=Hueftform.FLACH,
            hueftform_korrektur_mm=10.0,
            vorderer_abnaeherinhalt_mm=15.0,
        )
        durchschnittlich = taillenausfall_aufteilen(
            taillenausfall_mm=130.0,
            hueftform=Hueftform.DURCHSCHNITTLICH,
            hueftform_korrektur_mm=None,
            vorderer_abnaeherinhalt_mm=25.0,
        )

        self.assertEqual(
            flach.provenienz.formula_ids,
            ("HOF-B1-S034-F01", "HOF-B1-S034-F03"),
        )
        self.assertEqual(
            durchschnittlich.provenienz.formula_ids,
            ("HOF-B1-S034-F01",),
        )
        self.assertEqual(flach.provenienz.source_page, 34)
        self.assertEqual(flach.provenienz.contract_version, "1.0.0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
