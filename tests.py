import unittest
from alg1.worker import Programmist


class TestWorker(unittest.TestCase):

    def test_first(self):
        georgii = Programmist()
        self.assertEqual(georgii.email, "lev201611@gmail.com")