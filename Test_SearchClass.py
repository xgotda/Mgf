import unittest
import SearchClass as sc


''' oxo = oxonium (glycan) '''
_oxo_ppm = 5
_findOxo = [204.08667, 274.0921, 366.1395]
# _oxo_tolPairs = ppm_tolerance(findOxo, oxo_ppm)

'''' pp = peptide (larger fragment) '''
_pp_ppm = 7
_findPP = [1786.9487, 1990.0281, 2136.086]
# _pp_tolPairs = ppm_tolerance(findPP, pp_ppm)


class TestDoSearch(unittest.TestCase):

    def setUp(self):
        self.dds = sc.DoSearch()
        self.ds = sc.DoSearch(glycans=_findOxo, glycan_ppm=_oxo_ppm,
                              peptides=_findPP, peptide_ppm=_pp_ppm)


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


    def test_searchList(self):
        numberOfValues = (len(_findOxo) + len(_findPP)
                             + (len(_findPP) *2))  # doubly and triply charged for _findPP
        self.assertEqual(len(self.ds.searchList), numberOfValues,
                         'wrong number of values in searchList')

def suiteIsDoSearch():
    suite = unittest.TestSuite()
    suite.addTest(TestDoSearch('test_defaultInitSearch'))
    suite.addTest(TestDoSearch('test_initSearch'))
    suite.addTest(TestDoSearch('test_searchList'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suiteIsDoSearch())
    # unittest.main()
