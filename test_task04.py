

import unittest

class TestSplit(unittest.TestCase):
    def testraises(self):
        with self.assertRaises(Exception):
            1 / 0
            
        
    def testfalse(self):
        self.assertFalse(0)         
            
if __name__ == '__main__':
    unittest.main()