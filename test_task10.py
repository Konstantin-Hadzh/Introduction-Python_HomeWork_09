

import unittest

class TestSumSplit(unittest.TestCase):
        
    def testnotin(self):
        self.assertNotIn(1, [10])
        
    def testin(self):
        self.assertIn(1, [1, 2, 3])
        
    def testraises(self):
        with self.assertRaises(Exception):
            1 / 0
            
    def testtrue(self):
        self.assertTrue(10)
        
if __name__ == '__main__':
    unittest.main()