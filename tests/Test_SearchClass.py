import unittest
import SearchClass as sc
import PeptideClass as pc
import IonClass as ic
import helperMethods as h
import staticVariables as sV


''' oxo = oxonium (glycan) '''
_oxo_ppm = 5
_findOxo = [204.08667, 274.0921, 366.1395]
_oxo_tolPairs = h.ppm_tolerance(_findOxo, _oxo_ppm)
_lenOxo = len(_findOxo)

'''' pp = peptide (larger fragment) '''
_pp_ppm = 7
_findPP = [1786.9487, 1990.0281, 2136.086]
_pp_tolPairs = h.ppm_tolerance(_findPP, _pp_ppm)
_lenPP = len(_findPP)

''' cm = doubly or triply charged mass'''
cm = []
for f in _findPP:
    for n in range(2, 4):
        cm.append(h.chargedMassVar(f, n))
cm_tolPairs = h.ppm_tolerance(cm, _pp_ppm)


class TestDoSearch(unittest.TestCase):

    def setUp(self):
        self.dds = sc.DoSearch()
        self.ds = sc.DoSearch(_findOxo, _oxo_ppm,
                              _findPP, _pp_ppm)

    def tearDown(self):
        del self.dds
        del self.ds

    def test_defaultInitSearch(self):
        self.assertEqual(self.dds.oxoList, [],
                         'default oxoList not empty')
        self.assertEqual(self.dds.ppList, [],
                         'default oxoList not empty')
        self.assertEqual(self.dds.oxo_ppm, 0,
                         'default oxoList not empty')
        self.assertEqual(self.dds.pp_ppm, 0,
                         'default oxoList not empty')

    def test_initSearch(self):
        self.assertEqual(self.ds.oxoList, _findOxo,
                         'oxoList not initialised correctly with given values')
        self.assertEqual(self.ds.ppList, _findPP,
                         'ppList not initialised correctly with given values')
        self.assertEqual(self.ds.oxo_ppm, _oxo_ppm,
                         'oxo_ppm not initialised correctly with given values')
        self.assertEqual(self.ds.pp_ppm, _pp_ppm,
                         'pp_ppm not initialised correctly with given values')

    def test_numberSearchList(self):
        numberOfValues = (_lenOxo + _lenPP
                          + (_lenPP * 2))  # 2ly & 3ly charged for _findPP
        self.assertEqual(len(self.ds.searchList), numberOfValues,
                         'wrong number of values in searchList')

    def test_initGlycans(self):
        for i in range(_lenOxo):
            dsi = self.ds.searchList[i]
            self.assertEqual(dsi.ptype, pc.pType[pc._G],
                             'Wrong ptype for Glycan')
            self.assertEqual(dsi.chtype, sV.chType[sV._single],
                             'Wrong charge type for Glycan')
            self.assertEqual([dsi.mz, dsi.tol], _oxo_tolPairs[i],
                             'incorrect Glycans in searchList.')

    def test_initPeptides(self):
        for i in range(_lenOxo, _lenPP):
            a = i-_lenOxo
            dsi = self.ds.searchList[_lenOxo+i]
            self.assertEqual(dsi.ptype, pc.pType[pc._P],
                             'Wrong ptype for Glycan')
            self.assertEqual(dsi.chtype, sV.chType[sV._single],
                             'Wrong charge type for Peptide')
            self.assertEqual([dsi.mz, dsi.tol], _pp_tolPairs[a],
                             'incorrect Peptides in searchList.')

    def test_initPotentials(self):
        for i in range(_lenPP, _lenPP*2):
            a = i-_lenOxo
            dsi = self.ds.searchList[_lenPP+i]
            self.assertEqual(dsi.ptype, pc.pType[pc._M],
                             'Wrong ptype for Multi-charged')
            self.assertNotEqual(dsi.chtype, sV._single,
                                'Wrong charge type for Multi-charged')
            if i % 2:
                self.assertEqual(dsi.chtype, sV._double,
                                 'Multi-charged not doubly charged')
            else:
                self.assertEqual(dsi.chtype, sV._triple,
                                 'Multi-charged not triply charged')
            self.assertEqual([dsi.mz, dsi.tol], cm_tolPairs[a],
                             'incorrect Potentials in searchList.')

    def test_search(self):
        ion = ic.Ions()
        self.ds.search([_findOxo[0], 1234], ion)
        self.ds.search([_findOxo[2], 3333], ion)
        print(str(ion.fragments))
        self.assertIn(_findOxo[0], list(ion.fragments.keys()),
                      'fragment not added to fragment list.')
        del ion


def suiteIsDoSearch():
    suite = unittest.TestSuite()
    suite.addTest(TestDoSearch('test_defaultInitSearch'))
    suite.addTest(TestDoSearch('test_initSearch'))
    suite.addTest(TestDoSearch('test_numberSearchList'))
    suite.addTest(TestDoSearch('test_initGlycans'))
    suite.addTest(TestDoSearch('test_initPeptides'))
    suite.addTest(TestDoSearch('test_initPotentials'))
    suite.addTest(TestDoSearch('test_search'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suiteIsDoSearch())
    # unittest.main()
