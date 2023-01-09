

import unittest 

class TestSplit(unittest.TestCase):
    
    def testraises(self):
        with self.assertRaises(Exception):
            1 / 0
            
    def testfalse(self):
        self.assertFalse(0)
        
    def testtrue(self):
        self.assertTrue(10)
        
        
if __name__ == '__main__':
    unittest.main()