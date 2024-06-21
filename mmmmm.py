import unittest
from parameterized import parameterized


class Calculator:
    def plus(self, stroka):
        if str == type(stroka):
            if stroka == '':
                return 0
            stroka = stroka.split(",")
            return sum(list(map(int, stroka)))
        else:
            return 'Не верный тип данных'


class CalculatorTest(unittest.TestCase):
    @parameterized.expand([
        # (13, '12,1'),
        (10, '10'),
        # (40, '10,10,10,10'),
        # (0, ''),
        # ("Не верный тип данных", 12)
    ])
    def test_plus(self, res, stroka):
        calc = Calculator()
        self.assertEqual(res, calc.plus(stroka))
