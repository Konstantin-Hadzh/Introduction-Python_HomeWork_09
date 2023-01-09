

import unittest

class TestSum(unittest.TestCase):
        
    def testnotin(self):
        self.assertNotIn(1, [10])
        
if __name__ == '__main__':
    unittest.main()