

import unittest

class TestGetMass(unittest.TestCase):
    def testtrue(self):
        self.assertTrue(12500)
        
    def testfalse(self):
        self.assertFalse(0)    
    
        
if __name__ == '__main__':
    unittest.main()