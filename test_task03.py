

import unittest

class TestUnpack(unittest.TestCase):
    def testraises(self):
        with self.assertRaises(Exception):
            1 / 0

        
if __name__ == '__main__':
    unittest.main()