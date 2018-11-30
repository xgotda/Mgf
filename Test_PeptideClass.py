import unittest
import PeptideClass as pC
import staticVariables as sV


_m = 110.07169
_i = 4823.96
_t = 0.00234
_z = 0.0


class TestPeptides(unittest.TestCase):

    def setUp(self):
        self.pep = pC.Pep()
        self.peptide = pC.Peptide()

    def tearDown(self):
        del self.pep
        del self.peptide

    def test_defaultInitsPepPeptide(self):
        self.assertEqual(self.pep.mz, _z,
                         'incorrect init mz value for Pep')

        self.assertEqual(self.peptide.mz, _z,
                         'incorrect init mz value for Peptide')

        self.assertEqual(self.peptide.intensity, _z,
                         'incorrect intensity for Peptide')

    def test_initPep(self):
        self.pepm = pC.Pep(m_z=_m)
        self.assertEqual(self.pepm.mz, _m, 'Pep incorrect initialised')

    def test_initPeptide(self):
        pass

    def test_setmzPeps(self):
        mzVal = 12.999
        self.pep.mz = mzVal
        self.peptide.mz = mzVal
        self.assertEqual(self.pep.mz, mzVal, 'wrong after setting for Pep')
        self.assertEqual(self.peptide.mz, mzVal,
                         'wrong after setting for Peptide')

    def test_setIntensityPeps(self):
        intensityVal = 12.999
        self.pep.intensity = intensityVal
        self.peptide.intensity = intensityVal
        self.assertEqual(self.pep.intensity, intensityVal,
                         'wrong after setting for Pep')
        self.assertEqual(self.peptide.intensity, intensityVal,
                         'wrong after setting for Peptide')

    def test_frLine(self):
        aLine = str(_m) + ' ' + str(_i)
        self.peptide.frLine(aLine)
        self.assertEqual(self.peptide.mz, _m, 'mz incorrectly saved')
        self.assertEqual(self.peptide.intensity, _i,
                         'intensity incorrectly saved')
        # TODO: test for wrong string type and format
        # aLine = 'this is a string'
        # self.peptide.frLine(aLine)
        # self.asser


class TestFindPep(unittest.TestCase):
    def setUp(self):
        self.fpep = pC.FindPep()
        self.fMcP = pC.FindMcPep()


    def tearDown(self):
        del self.fpep
        del self.fMcP

    def test_defaultInitsFindPeps(self):
        self.assertEqual(self.fpep.mz, _z, 'incorrect mz for FindPep')
        self.assertEqual(self.fpep.tol, _z, 'incorrect tol for FindPep')
        self.assertEqual(self.fpep.ptype, pC.pType[pC._G],
                         'incorrect ptype for FindPep')
        self.assertEqual(self.fpep.chtype, sV.chType[sV._single],
                         'incorrect chtype for FindPep')

        self.assertEqual(self.fMcP.mz, _z, 'incorrect mz for FindMcPep')
        self.assertEqual(self.fMcP.tol, _z, 'incorrect tol for FindMcPep')
        self.assertEqual(self.fMcP.ptype, pC.pType[pC._M],
                         'incorrect ptype for FindMcPep')
        self.assertEqual(self.fMcP.chtype, sV.chType[sV._double],
                         'incorrect chtype for FindMcPep')

    def test_initFindPep(self):
        self.fpep = pC.FindPep(m_z=_m, tolerance=_t, ptype=pC._P)
        self.assertEqual(self.fpep.mz, _m, 'incorrect mz for FindPep')
        self.assertEqual(self.fpep.tol, _t, 'incorrect mz for FindPep')
        self.assertEqual(self.fpep.ptype, pC.pType[pC._P],
                         'incorrect ptype for FindPep')
        self.assertEqual(self.fpep.chtype, sV.chType[sV._single],
                         'incorrect chtype for FindPep')

    def test_initFindMcPep(self):
        self.fMcP = pC.FindMcPep(m_z=_m, tolerance=_t,
                                 chargeType=sV._triple)
        self.assertEqual(self.fMcP.mz, _m, 'incorrect mz for FindMcPep')
        self.assertEqual(self.fMcP.tol, _t, 'incorrect tol for FindMcPep')
        self.assertEqual(self.fMcP.ptype, pC.pType[pC._M],
                         'incorrect ptype for FindMcPep')
        self.assertEqual(self.fMcP.chtype, sV.chType[sV._triple],
                         'incorrect chtype for FindMcPep')


def suiteIsPep():
    suite = unittest.TestSuite()
    suite.addTest(TestPeptides('test_defaultInitsPepPeptide'))
    suite.addTest(TestPeptides('test_initPep'))
    suite.addTest(TestPeptides('test_setmzPeps'))
    suite.addTest(TestPeptides('test_setIntensityPeps'))
    suite.addTest(TestPeptides('test_frLine'))
    return suite


def suiteIsFindPeps():
    suite = unittest.TestSuite()
    suite.addTest(TestFindPep('test_defaultInitsFindPeps'))
    suite.addTest(TestFindPep('test_initFindPep'))
    suite.addTest(TestFindPep('test_initFindMcPep'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suiteIsPep())
    runner.run(suiteIsFindPeps())
    # unittest.main()
