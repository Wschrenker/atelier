"""Tests der Punktspiegelung; keine Passform- oder Produktionsfreigabe."""

import importlib
import importlib.util
import unittest


class VtSpiegelnTest(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(
            importlib.util.find_spec("vt_spiegeln"),
            "Der Spiegelungsbaustein fehlt noch",
        )
        self.m = importlib.import_module("vt_spiegeln")
        self.P = self.m.Punkt2D

    def test_spiegelt_punkte_an_vm_und_behaelt_original(self):
        punkte = (self.P(0, 0), self.P(20, 30), self.P(0, 600))
        ergebnis = self.m.vt_punkte_spiegeln(
            punkte=punkte,
            vm_oben=self.P(0, 0),
            vm_unten=self.P(0, 600),
            achsen_nulltoleranz_mm=1e-9,
        )
        self.assertEqual(ergebnis.original, punkte)
        self.assertEqual(
            ergebnis.gespiegelt,
            (self.P(0, 0), self.P(-20, 30), self.P(0, 600)),
        )
        self.assertEqual(ergebnis.quellseite, 36)
        self.assertEqual(ergebnis.bildnummer, 2)

    def test_waagrechte_und_schraege_achse(self):
        for a, b, p, soll in (
            ((0, 10), (100, 10), (20, 30), (20, -10)),
            ((10, 20), (110, 120), (30, 50), (40, 40)),
        ):
            with self.subTest(achse=(a, b)):
                ist = self.m.vt_punkte_spiegeln(
                    punkte=(self.P(*p),), vm_oben=self.P(*a),
                    vm_unten=self.P(*b), achsen_nulltoleranz_mm=1e-9,
                ).gespiegelt[0]
                self.assertAlmostEqual(ist.x_mm, soll[0], delta=1e-9)
                self.assertAlmostEqual(ist.y_mm, soll[1], delta=1e-9)

    def test_achse_ist_unendliche_gerade_und_richtung_unerheblich(self):
        for oben, unten in ((self.P(10, 0), self.P(10, 1)),
                            (self.P(10, 1), self.P(10, 0))):
            ergebnis = self.m.vt_punkte_spiegeln(
                punkte=(self.P(30, 600),), vm_oben=oben, vm_unten=unten,
                achsen_nulltoleranz_mm=0,
            )
            self.assertEqual(ergebnis.gespiegelt, (self.P(-10, 600),))

    def test_zweimal_spiegeln_erhaelt_ausgangslage_und_abstaende(self):
        import math
        from itertools import combinations
        original = (self.P(13, 7), self.P(80, 42), self.P(3, 600))
        achse = dict(vm_oben=self.P(10, 20), vm_unten=self.P(110, 320),
                     achsen_nulltoleranz_mm=1e-9)
        einmal = self.m.vt_punkte_spiegeln(punkte=original, **achse).gespiegelt
        zweimal = self.m.vt_punkte_spiegeln(punkte=einmal, **achse).gespiegelt
        for p, q in zip(original, zweimal):
            self.assertAlmostEqual(p.x_mm, q.x_mm, delta=1e-9)
            self.assertAlmostEqual(p.y_mm, q.y_mm, delta=1e-9)
        for i, j in combinations(range(len(original)), 2):
            vorher = math.hypot(original[i].x_mm - original[j].x_mm,
                                original[i].y_mm - original[j].y_mm)
            nachher = math.hypot(einmal[i].x_mm - einmal[j].x_mm,
                                 einmal[i].y_mm - einmal[j].y_mm)
            self.assertAlmostEqual(vorher, nachher, delta=1e-9)

    def test_achsenpunkte_bleiben_auch_auf_schraeger_achse_fest(self):
        original = (self.P(10, 20), self.P(60, 170), self.P(110, 320))
        ergebnis = self.m.vt_punkte_spiegeln(
            punkte=original, vm_oben=original[0], vm_unten=original[-1],
            achsen_nulltoleranz_mm=1e-9,
        )
        for p, q in zip(original, ergebnis.gespiegelt):
            self.assertAlmostEqual(p.x_mm, q.x_mm, delta=1e-9)
            self.assertAlmostEqual(p.y_mm, q.y_mm, delta=1e-9)

    def test_ergebnis_ist_unveraenderlich(self):
        from dataclasses import FrozenInstanceError
        ergebnis = self.m.vt_punkte_spiegeln(
            punkte=(self.P(20, 30),), vm_oben=self.P(0, 0),
            vm_unten=self.P(0, 600), achsen_nulltoleranz_mm=1e-9,
        )
        with self.assertRaises(FrozenInstanceError):
            ergebnis.gespiegelt[0].x_mm = 99
        with self.assertRaises(FrozenInstanceError):
            ergebnis.original = ()

    def test_ungueltige_geometrie_stoppt_mit_value_error(self):
        basis = dict(
            punkte=(self.P(20, 30),),
            vm_oben=self.P(0, 0), vm_unten=self.P(0, 600),
            achsen_nulltoleranz_mm=1e-9,
        )
        faelle = [
            dict(vm_unten=self.P(0, 0)),
            dict(vm_unten=self.P(0, 1e-9)),
            dict(achsen_nulltoleranz_mm=-1),
            dict(achsen_nulltoleranz_mm=float("nan")),
            dict(achsen_nulltoleranz_mm=float("inf")),
            dict(vm_oben=self.P(float("nan"), 0)),
            dict(vm_unten=self.P(0, float("inf"))),
            dict(punkte=(self.P(float("inf"), 0),)),
            dict(punkte=(self.P(20, float("nan")),)),
            dict(punkte=()),
            # Endliche Eingaben mit nicht darstellbaren Zwischenwerten.
            dict(vm_oben=self.P(-1e308, 0), vm_unten=self.P(1e308, 0)),
            dict(punkte=(self.P(1e308, 0),), vm_oben=self.P(-1e308, 0),
                 vm_unten=self.P(-1e308, 100)),
        ]
        for aenderung in faelle:
            with self.subTest(aenderung=aenderung):
                with self.assertRaises(self.m.GeometrieVertragError):
                    self.m.vt_punkte_spiegeln(**(basis | aenderung))


if __name__ == "__main__":
    unittest.main()
