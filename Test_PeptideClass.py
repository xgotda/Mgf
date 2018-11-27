import unittest
from PeptideClass import *

class TestPeptides(unittest.TestCase):

    def setUp(self):
        self.pep = Pep()
        self.peptide = Peptide()
        self.m = 110.07169
        self.i = 4823.96

    def tearDown(self):
        del self.pep
        del self.peptide

    def test_defaultInitsPepPeptide(self):
        self.assertEqual(self.pep.mz, 0.0,
                         'incorrect init mz value for Pep')

        self.assertEqual(self.peptide.mz, 0.0,
                         'incorrect init mz value for Peptide')

        self.assertEqual(self.peptide.intensity, 0.0,
                         'incorrect intensity for Peptide')

    def test_initPep(self):
        self.pepm = Pep(m_z = self.m)
        self.assertEqual(self.pepm.mz, self.m, 'Pep incorrect initialised')

    def test_initPeptide(self):
        pass

    def test_setmzPeps(self):
        mzVal = 12.999
        self.pep.mz = mzVal
        self.peptide.mz = mzVal
        self.assertEqual(self.pep.mz, mzVal, 'wrong after setting for Pep')
        self.assertEqual(self.peptide.mz, mzVal, 'wrong after setting for Peptide')

    def test_setIntensityPeps(self):
        intensityVal = 12.999
        self.pep.intensity = intensityVal
        self.peptide.intensity = intensityVal
        self.assertEqual(self.pep.intensity, intensityVal,
                         'wrong after setting for Pep')
        self.assertEqual(self.peptide.intensity, intensityVal,
                         'wrong after setting for Peptide')

    def test_frLine(self):
        aLine = str(self.m) + ' ' + str(self.i)
        self.peptide.frLine(aLine)
        self.assertEqual(self.peptide.mz, self.m, 'mz incorrectly saved')
        self.assertEqual(self.peptide.intensity, self.i,
                         'intensity incorrectly saved')


class TestFindPep(unittest.TestCase):
    def setUp(self):
        self.fpep = FindPep()
        self.fMcP = FindMcPep()

    def test_defaultInitsFindPeps(self):
        self.assertEqual(self.fpep.mz, 0.0, 'incorrect mz for FindPep')
        self.assertEqual(self.fMcP.mz, 0.0, 'incorrect mz for FindMcPep')



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
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suiteIsPep())
    runner.run(suiteIsFindPeps())
    # unittest.main()
