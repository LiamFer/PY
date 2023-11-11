import unittest
from unit1 import place

class testingPlace(unittest.TestCase):
    
    def testCityCountry(self):
        funcReturn = place("santiago",'chile',500)
        self.assertEqual(funcReturn,"Santiago, Chile - 500")

unittest.main()