import unittest
import module1

class Module1TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_calculation(self):
        self.assertEqual(2 * 2, 4, 'wrong calculation')