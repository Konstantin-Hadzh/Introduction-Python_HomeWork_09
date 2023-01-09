

import unittest

class TestSum(unittest.TestCase):
        
    def testnotin(self):
        self.assertNotIn(1, ['Фамилия: '])
        
    def testis(self):
        lastname = input('Фамилия: ')
        b = lastname
        self.assertIs(lastname, b)
        
if __name__ == '__main__':
    unittest.main()