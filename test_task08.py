

import unittest

class TestFunc(unittest.TestCase):
        
    def testtrue(self):

        self.assertTrue(10) 

        
    def testisnone(self):

        self.assertIsNone(None)    
        
if __name__ == '__main__':
    unittest.main()