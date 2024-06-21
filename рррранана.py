import math
import parameterized
import unittest


class SqrtMy:
    def kkk(self, n: int):
        if type(n) is not int:
            raise TypeError('Num must be int')
        elif n < 0:
            raise ValueError('Num must be int > 0')
        else:
            n = math.sqrt(n)
            return n


class TestSqrtMy(unittest.TestCase):
    @parameterized.parameterized.expand([
        (1, 1),
        (2, 4),
        (13, 169)
    ])
    def test_sqrt(self, res, num):
        c = SqrtMy()
        self.assertEqual(res, c.kkk(num))

    @parameterized.parameterized.expand([
        ('Num must be int', 'aaaa'),
        ('Num must be int', [1, 2, 3])
    ])
    def test_exception_typeError(self, _, value):
        with self.assertRaises(TypeError):
            c = SqrtMy()
            c.kkk(value)


    @parameterized.parameterized.expand([
        ('Num must be int > 0', -1)
    ])

    def test__exception_valueError(self, _, value):
        with self.assertRaises(ValueError):
            c = SqrtMy()
            c.kkk(value)
