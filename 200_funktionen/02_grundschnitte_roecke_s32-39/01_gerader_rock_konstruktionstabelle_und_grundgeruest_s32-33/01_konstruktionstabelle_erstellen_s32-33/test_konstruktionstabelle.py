"""Vertragstests fuer die Konstruktionstabelle auf S. 32-33."""

from __future__ import annotations

import unittest
from unittest import mock

import konstruktionstabelle as konstruktionstabelle_modul
from konstruktionstabelle import (
    Berechnungsstatus,
    EntscheidungFehltError,
    UngueltigerLaengenwertError,
    ZugabeAusserhalbBereichError,
    konstruktionstabelle_erstellen,
    taillenausfall_aus_halben_weiten,
)


BUCH_ENTSCHEIDUNGEN_CM = {
    "hueftzugabe": 3.0,
    "taillenzugabe": 2.0,
    "hueftabstich": 6.5,
    "vorderer_abnaeherinhalt": 2.5,
    "erster_hinterer_abnaeherinhalt": 4.0,
    "zweiter_hinterer_abnaeherinhalt": 0.0,
}


class KonstruktionstabelleTest(unittest.TestCase):
    def test_buchbeispiel_wird_an_der_systemgrenze_in_mm_umgerechnet(self) -> None:
        tabelle = konstruktionstabelle_erstellen(
            hueftumfang_cm=97.0,
            taillenumfang_cm=72.0,
            huefttiefe_cm=21.0,
            modelllaenge_cm=50.0,
            entscheidungen_cm=BUCH_ENTSCHEIDUNGEN_CM,
        )

        self.assertEqual(tabelle.hueftumfang_mm, 970.0)
        self.assertEqual(tabelle.taillenumfang_mm, 720.0)
        self.assertEqual(tabelle.huefttiefe_mm, 210.0)
        self.assertEqual(tabelle.modelllaenge_mm, 500.0)
        self.assertEqual(tabelle.hueftweite_mm, 1000.0)
        self.assertEqual(tabelle.halbe_hueftweite_mm, 500.0)
        self.assertEqual(tabelle.viertel_hueftweite_mm, 250.0)
        self.assertEqual(tabelle.taillenweite_mm, 740.0)
        self.assertEqual(tabelle.halbe_taillenweite_mm, 370.0)
        self.assertEqual(tabelle.viertel_taillenweite_mm, 185.0)
        self.assertEqual(tabelle.taillenausfall_mm, 130.0)
        self.assertEqual(tabelle.halber_taillenausfall_mm, 65.0)
        self.assertEqual(tabelle.kontrollsumme_taillenausfall_mm, 130.0)

    def test_zugabenbereiche_sind_inklusiv_und_werden_nicht_geklemmt(self) -> None:
        for name, grenzen_cm in (
            ("hueftzugabe", (2.0, 3.0)),
            ("taillenzugabe", (1.0, 2.0)),
        ):
            for grenze_cm in grenzen_cm:
                with self.subTest(name=name, grenze_cm=grenze_cm):
                    entscheidungen = dict(BUCH_ENTSCHEIDUNGEN_CM)
                    entscheidungen[name] = grenze_cm
                    tabelle = konstruktionstabelle_erstellen(
                        hueftumfang_cm=97.0,
                        taillenumfang_cm=72.0,
                        huefttiefe_cm=21.0,
                        modelllaenge_cm=50.0,
                        entscheidungen_cm=entscheidungen,
                    )
                    self.assertEqual(
                        getattr(tabelle, f"{name}_mm"), grenze_cm * 10.0
                    )

        for name, wert_cm, minimum_mm, maximum_mm in (
            ("hueftzugabe", 1.9, 20.0, 30.0),
            ("hueftzugabe", 3.1, 20.0, 30.0),
            ("taillenzugabe", 0.9, 10.0, 20.0),
            ("taillenzugabe", 2.1, 10.0, 20.0),
        ):
            with self.subTest(name=name, wert_cm=wert_cm):
                entscheidungen = dict(BUCH_ENTSCHEIDUNGEN_CM)
                entscheidungen[name] = wert_cm
                with self.assertRaises(ZugabeAusserhalbBereichError) as context:
                    konstruktionstabelle_erstellen(
                        hueftumfang_cm=97.0,
                        taillenumfang_cm=72.0,
                        huefttiefe_cm=21.0,
                        modelllaenge_cm=50.0,
                        entscheidungen_cm=entscheidungen,
                    )
                self.assertEqual(context.exception.entscheidung_name, name)
                self.assertEqual(context.exception.wert_mm, wert_cm * 10.0)
                self.assertEqual(context.exception.minimum_mm, minimum_mm)
                self.assertEqual(context.exception.maximum_mm, maximum_mm)

    def test_fachliche_entscheidungsbereiche_werden_nicht_ueberschritten(self) -> None:
        for name, wert_cm in (
            ("hueftabstich", 5.4),
            ("hueftabstich", 7.6),
            ("vorderer_abnaeherinhalt", 1.0),
            ("erster_hinterer_abnaeherinhalt", 4.6),
            ("zweiter_hinterer_abnaeherinhalt", 0.1),
            ("zweiter_hinterer_abnaeherinhalt", 1e-12),
        ):
            with self.subTest(name=name, wert_cm=wert_cm):
                entscheidungen = dict(BUCH_ENTSCHEIDUNGEN_CM)
                entscheidungen[name] = wert_cm
                with self.assertRaises(ValueError) as context:
                    konstruktionstabelle_erstellen(
                        hueftumfang_cm=97.0,
                        taillenumfang_cm=72.0,
                        huefttiefe_cm=21.0,
                        modelllaenge_cm=50.0,
                        entscheidungen_cm=entscheidungen,
                    )
                self.assertEqual(
                    context.exception.__class__.__name__,
                    "EntscheidungAusserhalbBereichError",
                )

    def test_alle_sechs_entscheidungen_sind_ohne_defaults_erforderlich(self) -> None:
        for fehlender_name in BUCH_ENTSCHEIDUNGEN_CM:
            with self.subTest(fehlender_name=fehlender_name):
                entscheidungen = dict(BUCH_ENTSCHEIDUNGEN_CM)
                del entscheidungen[fehlender_name]
                with self.assertRaises(EntscheidungFehltError) as context:
                    konstruktionstabelle_erstellen(
                        hueftumfang_cm=97.0,
                        taillenumfang_cm=72.0,
                        huefttiefe_cm=21.0,
                        modelllaenge_cm=50.0,
                        entscheidungen_cm=entscheidungen,
                    )
                self.assertEqual(
                    context.exception.fehlende_entscheidungen, (fehlender_name,)
                )

    def test_none_gilt_als_fehlende_entscheidung(self) -> None:
        entscheidungen = dict(BUCH_ENTSCHEIDUNGEN_CM)
        entscheidungen["hueftabstich"] = None

        with self.assertRaises(EntscheidungFehltError) as context:
            konstruktionstabelle_erstellen(
                hueftumfang_cm=97.0,
                taillenumfang_cm=72.0,
                huefttiefe_cm=21.0,
                modelllaenge_cm=50.0,
                entscheidungen_cm=entscheidungen,
            )
        self.assertEqual(
            context.exception.fehlende_entscheidungen,
            ("hueftabstich",),
        )

    def test_taillenausfall_entsteht_aus_zugabenhaltigen_halbweiten(self) -> None:
        entscheidungen = dict(BUCH_ENTSCHEIDUNGEN_CM)
        entscheidungen["hueftzugabe"] = 2.0
        entscheidungen["taillenzugabe"] = 1.0
        entscheidungen["hueftabstich"] = 3.25

        self.assertEqual(taillenausfall_aus_halben_weiten(470.0, 405.0), 65.0)
        with mock.patch.object(
            konstruktionstabelle_modul,
            "taillenausfall_aus_halben_weiten",
            wraps=taillenausfall_aus_halben_weiten,
        ) as taillenausfall_spion:
            tabelle = konstruktionstabelle_erstellen(
                hueftumfang_cm=92.0,
                taillenumfang_cm=80.0,
                huefttiefe_cm=21.0,
                modelllaenge_cm=50.0,
                entscheidungen_cm=entscheidungen,
            )

        taillenausfall_spion.assert_called_once_with(470.0, 405.0)
        self.assertEqual(tabelle.taillenausfall_mm, 65.0)

    def test_kontrollsumme_meldet_vollstaendig_ohne_rest_zu_verteilen(self) -> None:
        vollstaendig = konstruktionstabelle_erstellen(
            hueftumfang_cm=97.0,
            taillenumfang_cm=72.0,
            huefttiefe_cm=21.0,
            modelllaenge_cm=50.0,
            entscheidungen_cm=BUCH_ENTSCHEIDUNGEN_CM,
        )
        self.assertEqual(vollstaendig.kontrollsumme_taillenausfall_mm, 130.0)
        self.assertTrue(vollstaendig.verteilung_ist_vollstaendig)

        entscheidungen = dict(BUCH_ENTSCHEIDUNGEN_CM)
        entscheidungen["erster_hinterer_abnaeherinhalt"] = 3.0
        unvollstaendig = konstruktionstabelle_erstellen(
            hueftumfang_cm=97.0,
            taillenumfang_cm=72.0,
            huefttiefe_cm=21.0,
            modelllaenge_cm=50.0,
            entscheidungen_cm=entscheidungen,
        )

        self.assertEqual(unvollstaendig.erster_hinterer_abnaeherinhalt_mm, 30.0)
        self.assertEqual(unvollstaendig.kontrollsumme_taillenausfall_mm, 120.0)
        self.assertFalse(unvollstaendig.verteilung_ist_vollstaendig)

    def test_provenienz_und_berechnungsstatus_sind_vollstaendig(self) -> None:
        tabelle = konstruktionstabelle_erstellen(
            hueftumfang_cm=97.0,
            taillenumfang_cm=72.0,
            huefttiefe_cm=21.0,
            modelllaenge_cm=50.0,
            entscheidungen_cm=BUCH_ENTSCHEIDUNGEN_CM,
        )

        self.assertEqual(tabelle.berechnungsstatus, Berechnungsstatus.VOLLSTAENDIG)
        self.assertEqual(tabelle.provenienz.source_page, 33)
        self.assertEqual(
            tabelle.provenienz.formula_ids,
            ("HOF-B1-S033-F01", "HOF-B1-S033-F02", "HOF-B1-S033-F03"),
        )
        self.assertEqual(
            tabelle.provenienz.math_contracts,
            (
                "400_mathematik/20_codevertraege/10_numerik_einheiten_und_toleranzen.md",
                "400_mathematik/20_codevertraege/80_parameterketten_und_neuberechnung.md",
            ),
        )
        self.assertEqual(
            tabelle.provenienz.input_names,
            (
                "hueftumfang_cm",
                "taillenumfang_cm",
                "huefttiefe_cm",
                "modelllaenge_cm",
            ),
        )
        self.assertEqual(
            tabelle.provenienz.selected_options,
            (
                ("hueftzugabe_mm", 30.0),
                ("taillenzugabe_mm", 20.0),
                ("hueftabstich_mm", 65.0),
                ("vorderer_abnaeherinhalt_mm", 25.0),
                ("erster_hinterer_abnaeherinhalt_mm", 40.0),
                ("zweiter_hinterer_abnaeherinhalt_mm", 0.0),
            ),
        )
        self.assertEqual(tabelle.provenienz.contract_version, "1.0.0")

        entscheidungen = dict(BUCH_ENTSCHEIDUNGEN_CM)
        entscheidungen["erster_hinterer_abnaeherinhalt"] = 3.0
        unvollstaendig = konstruktionstabelle_erstellen(
            hueftumfang_cm=97.0,
            taillenumfang_cm=72.0,
            huefttiefe_cm=21.0,
            modelllaenge_cm=50.0,
            entscheidungen_cm=entscheidungen,
        )
        self.assertEqual(
            unvollstaendig.berechnungsstatus,
            Berechnungsstatus.UNVOLLSTAENDIG,
        )

    def test_abgeleiteter_taillenausfall_ueberlauf_stoppt_typisiert(self) -> None:
        maximum = float.fromhex("0x1.fffffffffffffp+1023")

        with self.assertRaises(ArithmeticError) as context:
            taillenausfall_aus_halben_weiten(maximum, -maximum)
        self.assertEqual(
            context.exception.__class__.__name__,
            "NichtEndlicherBerechnungswertError",
        )

    def test_cm_zu_mm_ueberlauf_stoppt_als_berechnungsfehler(self) -> None:
        entscheidungen = dict(BUCH_ENTSCHEIDUNGEN_CM)
        entscheidungen["zweiter_hinterer_abnaeherinhalt"] = float.fromhex(
            "0x1.fffffffffffffp+1023"
        )

        with self.assertRaises(ArithmeticError) as context:
            konstruktionstabelle_erstellen(
                hueftumfang_cm=97.0,
                taillenumfang_cm=72.0,
                huefttiefe_cm=21.0,
                modelllaenge_cm=50.0,
                entscheidungen_cm=entscheidungen,
            )
        self.assertEqual(
            context.exception.__class__.__name__,
            "NichtEndlicherBerechnungswertError",
        )

    def test_koerpermasse_und_konstruktionslaengen_muessen_positiv_sein(self) -> None:
        for wert_name in (
            "hueftumfang_cm",
            "taillenumfang_cm",
            "huefttiefe_cm",
            "modelllaenge_cm",
        ):
            with self.subTest(wert_name=wert_name):
                eingaben = {
                    "hueftumfang_cm": 97.0,
                    "taillenumfang_cm": 72.0,
                    "huefttiefe_cm": 21.0,
                    "modelllaenge_cm": 50.0,
                    "entscheidungen_cm": BUCH_ENTSCHEIDUNGEN_CM,
                }
                eingaben[wert_name] = 0.0
                with self.assertRaises(UngueltigerLaengenwertError) as context:
                    konstruktionstabelle_erstellen(**eingaben)
                self.assertEqual(context.exception.wert_name, wert_name)

    def test_nicht_endliche_und_negative_laengen_stoppen_typisiert(self) -> None:
        with self.assertRaises(UngueltigerLaengenwertError) as nicht_endlich:
            konstruktionstabelle_erstellen(
                hueftumfang_cm=float("inf"),
                taillenumfang_cm=72.0,
                huefttiefe_cm=21.0,
                modelllaenge_cm=50.0,
                entscheidungen_cm=BUCH_ENTSCHEIDUNGEN_CM,
            )
        self.assertEqual(nicht_endlich.exception.wert_name, "hueftumfang_cm")

        entscheidungen = dict(BUCH_ENTSCHEIDUNGEN_CM)
        entscheidungen["vorderer_abnaeherinhalt"] = -1.0
        with self.assertRaises(UngueltigerLaengenwertError) as negativ:
            konstruktionstabelle_erstellen(
                hueftumfang_cm=97.0,
                taillenumfang_cm=72.0,
                huefttiefe_cm=21.0,
                modelllaenge_cm=50.0,
                entscheidungen_cm=entscheidungen,
            )
        self.assertEqual(
            negativ.exception.wert_name,
            "vorderer_abnaeherinhalt",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
