"""Tests der ausdrücklich gewählten digitalen Kurvenfamilie, keine Buchformel."""
import importlib.util
import unittest
from pathlib import Path


class KurvenTest(unittest.TestCase):
    def test_taillenbogen_hat_feste_anker_und_gewaehlten_durchhang(self):
        self.assertIsNotNone(importlib.util.find_spec('kurven'), 'Kurvenbaustein fehlt')
        from kurven import Punkt, taillenbogen, auswerten
        a, b = Punkt(0, 0), Punkt(100, -10)
        links, rechts = taillenbogen(a, b, durchhang_mm=3)
        self.assertEqual(links.p0, a)
        self.assertEqual(rechts.p3, b)
        self.assertEqual(links.p3, Punkt(50, -2))
        self.assertEqual(links.p3, rechts.p0)
        self.assertEqual(auswerten(links, 0), a)
        self.assertEqual(auswerten(rechts, 1), b)
        # Waagrechte Endtangenten an Mitte und Abnäherschenkeln.
        self.assertEqual(links.p1.y_mm, a.y_mm)
        self.assertEqual(rechts.p2.y_mm, b.y_mm)
        # Identische Ableitung am inneren Anschluss (C1).
        self.assertAlmostEqual(links.p3.y_mm-links.p2.y_mm,
                               rechts.p1.y_mm-rechts.p0.y_mm)


    def test_hueftbogen_bleibt_monoton_und_schliesst_senkrecht_an(self):
        import kurven
        self.assertTrue(hasattr(kurven, 'hueftbogen'), 'Hüftbogen fehlt')
        a, b = kurven.Punkt(220, -10), kurven.Punkt(250, 200)
        for form in (0.1, 0.33, 0.45):
            k = kurven.hueftbogen(a, b, form=form)
            self.assertEqual(k.p0, a)
            self.assertEqual(k.p3, b)
            self.assertEqual(k.p2.x_mm, b.x_mm)
            punkte = [kurven.auswerten(k, i/100) for i in range(101)]
            self.assertTrue(all(p.x_mm <= q.x_mm and p.y_mm < q.y_mm
                                for p, q in zip(punkte, punkte[1:])))
        self.assertNotEqual(kurven.hueftbogen(a,b,form=0.1),
                            kurven.hueftbogen(a,b,form=0.45))


    def test_ungueltige_geometrie_stoppt_typisiert(self):
        import kurven as k
        self.assertTrue(hasattr(k, 'KurvenVertragError'), 'Fehlervertrag fehlt')
        a, b = k.Punkt(0, 0), k.Punkt(100, 200)
        faelle = [
            lambda: k.taillenbogen(a,a,durchhang_mm=0),
            lambda: k.taillenbogen(a,k.Punkt(1e-10,0),durchhang_mm=0),
            lambda: k.taillenbogen(b,a,durchhang_mm=0),
            lambda: k.taillenbogen(a,b,durchhang_mm=-1),
            lambda: k.taillenbogen(a,b,durchhang_mm=float('nan')),
            lambda: k.hueftbogen(a,b,form=0),
            lambda: k.hueftbogen(a,b,form=0.51),
            lambda: k.hueftbogen(b,a,form=0.3),
            lambda: k.hueftbogen(a,k.Punkt(-1,200),form=0.3),
            lambda: k.taillenbogen(k.Punkt(-1e308,0),k.Punkt(1e308,0),durchhang_mm=0),
            lambda: k.auswerten(k.Kubisch(a,a,b,b),1.1),
            lambda: k.auswerten(k.Kubisch(a,a,k.Punkt(float('inf'),0),b),0.5),
        ]
        for fall in faelle:
            with self.subTest(fall=fall), self.assertRaises(k.KurvenVertragError):
                fall()


    def test_laengenintervall_umfasst_unabhaengige_parabelformel(self):
        import math
        import kurven as k
        self.assertTrue(hasattr(k, 'messen'), 'Adaptive Messung fehlt')
        c = k.Kubisch(k.Punkt(0,0), k.Punkt(100/3,100/3),
                      k.Punkt(200/3,100/3), k.Punkt(100,0))
        erwartet = 50*(math.sqrt(2)+math.asinh(1))
        for tol in (0.1, 0.001):
            m = k.messen(c, fehler_mm=tol)
            self.assertLessEqual(m.untergrenze_mm, erwartet)
            self.assertGreaterEqual(m.obergrenze_mm, erwartet)
            self.assertLessEqual(m.obergrenze_mm-m.untergrenze_mm,tol)
            self.assertEqual(m.punkte[0],c.p0)
            self.assertEqual(m.punkte[-1],c.p3)
        for tol in (0,-1,float('inf')):
            with self.assertRaises(k.KurvenVertragError):
                k.messen(c,fehler_mm=tol)


if __name__ == '__main__':
    unittest.main()
