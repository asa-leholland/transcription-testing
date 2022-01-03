import unittest

from transcribeSR import getSRVersion, getHarvardAudioText

pathToAudioFile = 'audio_files_harvard.wav'

from runJiwer import determineAccuracy

class TestSetup(unittest.TestCase):
    
    def testHarvard(self):
        self.assertIsNotNone(getHarvardAudioText(pathToAudioFile))
    


class TestJiwer(unittest.TestCase):
    def testPerfect(self):
        expected = "The quick brown fox sleeps"
        actual = "The quick brown fox sleeps"
        self.assertEqual(determineAccuracy(expected, actual), 1)

    def testEightyPercent(self):
        expected = "The quick brawn fox sleeps"
        actual = "The quick brown fox sleeps"
        self.assertEqual(determineAccuracy(expected, actual), 0.8)

    def testImperfect(self):
        expected = "They're over there in their house"
        actual = "Their oven's not on the mouse"
        self.assertEqual(determineAccuracy(expected, actual), 0)   

    def testInteger(self):
        expected = "They're over there in their house"
        actual = 1
        self.assertEqual(determineAccuracy(expected, actual), False)   

    def testDecimal(self):
        expected = "They're over there in their house"
        actual = 1.5
        self.assertEqual(determineAccuracy(expected, actual), False)   
    
    def testNone(self):
        expected = "They're over there in their house"
        actual = None
        self.assertEqual(determineAccuracy(expected, actual), False)   
    
    def testZero(self):
        expected = "They're over there in their house"
        actual = 0
        self.assertEqual(determineAccuracy(expected, actual), False)   

    def testEmptyString(self):
        expected = "They're over there in their house"
        actual = ""
        self.assertEqual(determineAccuracy(expected, actual), False)   
    
    def testDictionary(self):
        expected = "They're over there in their house"
        actual = {}
        self.assertEqual(determineAccuracy(expected, actual), False)   


if __name__ == "__main__":
    unittest.main()