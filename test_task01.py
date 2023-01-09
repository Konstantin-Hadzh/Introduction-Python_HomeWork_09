

import unittest

class TestGenNum(unittest.TestCase):
    def testin(self):
        self.assertIn("2-го", ["бабушка приехала", "2-го", "числа", (3, 5, 7, 9)])
    
    def testnotin(self):
        self.assertNotIn(1, ["бабушка приехала", "2-го", "числа", (3, 5, 7, 9)])    
        
if __name__ == '__main__':
    unittest.main()