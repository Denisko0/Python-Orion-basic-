from unittest import TestCase
from calc import Calc
import math


class Testing(TestCase):

    def test_0001(self):
        self.assertEqual(Calc.add(2, 6), 8)

    def test_0002(self):
        self.assertEqual(Calc.substract(9, 3), 6)

    def test_0003(self):
        self.assertEqual(Calc.multiplay(2, 6), 12)

    def test_0004(self):
        self.assertEqual(Calc.divide(12, 6), 2)

    def test_0005(self):
        self.assertEqual(Calc.exponentiation(12, 2), 144)

    def test_0006(self):
        self.assertEqual(Calc.sqrt(169), 13)

    def test_0008(self):
        self.assertEqual(Calc.percentage(60, 20), 12)
