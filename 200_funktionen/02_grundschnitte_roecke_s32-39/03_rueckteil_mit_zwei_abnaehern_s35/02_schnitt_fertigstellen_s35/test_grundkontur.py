"""Integration der vorhandenen Buchpunkt-Bausteine mit eigenen Arbeitskurven."""
import importlib.util
import unittest


class GrundkonturTest(unittest.TestCase):
    def test_vorhandene_konstruktion_liefert_zwei_teile_mit_drei_abnaehern(self):
        self.assertIsNotNone(importlib.util.find_spec('grundkontur'), 'Konturmontage fehlt')
        from grundkontur import arbeitsbeispiel, kontur
        basis = arbeitsbeispiel()
        self.assertEqual(set(basis), {'VT','RT'})
        self.assertEqual(len(basis['VT'].abnaeher), 1)
        self.assertEqual(len(basis['RT'].abnaeher), 2)
        self.assertEqual([a.inhalt_mm for a in basis['RT'].abnaeher], [30,25])
        for teil in basis.values():
            ergebnis = kontur(teil,durchhang_mm=1,hueftform=0.33)
            self.assertEqual(ergebnis.ring[0],ergebnis.ring[-1])
            self.assertEqual(ergebnis.ring[0],teil.mitte)
            self.assertEqual(ergebnis.huefte.p0,teil.seite_oben)
            self.assertEqual(ergebnis.huefte.p3.x_mm,teil.breite_mm)
            self.assertIn(teil.abnaeher[0].links,ergebnis.ring)
            self.assertIn(teil.abnaeher[0].rechts,ergebnis.ring)
            self.assertGreater(ergebnis.seitenlaenge_mm[0],teil.laenge_mm)
            self.assertEqual(ergebnis.status,'arbeitskontur_nicht_produktionsfreigegeben')


    def test_ungueltige_teilbasis_und_zu_tiefe_taille_stoppen(self):
        from dataclasses import replace
        from grundkontur import arbeitsbeispiel, kontur
        from kurven import Punkt, KurvenVertragError
        b = arbeitsbeispiel()['VT']
        faelle = [replace(b,laenge_mm=100), replace(b,breite_mm=0),
                  replace(b,mitte=Punkt(1,0)), replace(b,huefttiefe_mm=float('nan')),
                  replace(b,abnaeher=(replace(b.abnaeher[0],spitze=Punkt(800,90)),)),
                  replace(b,abnaeher=(replace(b.abnaeher[0],inhalt_mm=99),)),
                  replace(b,abnaeher=(b.abnaeher[0],b.abnaeher[0]))]
        for basis in faelle:
            with self.subTest(basis=basis), self.assertRaises(KurvenVertragError):
                kontur(basis,durchhang_mm=1,hueftform=0.3)
        with self.assertRaises(KurvenVertragError):
            kontur(b,durchhang_mm=300,hueftform=0.3)


    def test_reglerdaten_sind_echte_python_geometrie_ohne_produktionsbehauptung(self):
        import importlib.util
        self.assertIsNotNone(importlib.util.find_spec('ansicht_erzeugen'), 'Ansichtsgenerator fehlt')
        from ansicht_erzeugen import ansichtsdaten
        from grundkontur import arbeitsbeispiel,kontur
        daten = ansichtsdaten()
        self.assertEqual(daten['status'],'arbeitskontur_nicht_produktionsfreigegeben')
        self.assertEqual(set(daten['teile']),{'VT','RT'})
        for name,basis in arbeitsbeispiel().items():
            d = daten['teile'][name]
            self.assertEqual(len(d['taillen']),len(daten['durchhang_mm']))
            self.assertEqual(len(d['hueften']),len(daten['hueftform']))
            k = kontur(basis,durchhang_mm=daten['durchhang_mm'][4],
                       hueftform=daten['hueftform'][8])
            self.assertEqual(d['taillen'][4]['laenge_mm'],list(k.taillenlaenge_mm))
            self.assertEqual(d['hueften'][8]['laenge_mm'],list(k.seitenlaenge_mm))
            self.assertNotEqual(d['taillen'][0]['kontur'],d['taillen'][-1]['kontur'])
            self.assertNotEqual(d['hueften'][0]['kontur'],d['hueften'][-1]['kontur'])


    def test_offline_html_enthaelt_daten_und_alle_regler(self):
        from pathlib import Path
        self.assertTrue(Path(__file__).with_name('kurvenansicht.vorlage.html').exists(),
                        'Offline-Ansicht fehlt')
        from ansicht_erzeugen import html_erzeugen
        html = html_erzeugen()
        self.assertNotIn('__KURVENDATEN__',html)
        self.assertNotIn('<script src=',html)
        for id_ in ('vt-taille','rt-taille','vt-huefte','rt-huefte'):
            self.assertIn('id="'+id_+'"',html)
        self.assertIn('Keine Produktionsfreigabe',html)


if __name__ == '__main__':
    unittest.main()
