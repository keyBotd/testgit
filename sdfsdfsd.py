# from icecream import ic
import unittest
from parameterized import parameterized


# class TestFizzBuzz(unittest.TestCase):
#     @parameterized.expand([
#         ('Fizz', 3),
#         ('Buzz', 10),
#         ("FizzBuzz", 15),
#         ("Error Type", '10')
#     ])
#     def test_index(self, k, a):
#         o = FizzBuzz()
#         self.assertEqual(k, o.fizz_buzz(a))
#
#
# class FizzBuzz:
#     def fizz_buzz(self, n):
#         if type(n) == int:
#             if n % 3 == 0 and n % 5 == 0:
#                 return 'FizzBuzz'
#
#             elif n % 3 == 0:
#                 return "Fizz"
#
#             elif n % 5 == 0:
#                 return "Buzz"
#
#         else:
#             return "Error Type"

class TestFooBarQix(unittest.TestCase):
    @parameterized.expand([
        ('Foo', 3),
        ('Bar', 5),
        ("Qix", 7),
        ("Foo Bar Qix", 105),
        ("Error Type", '10')
    ])
    def test_index(self, k, a):
        o = FooBarQix()
        self.assertEqual(k, o.foo_bar_qix(a))


class FooBarQix:
    def foo_bar_qix(self, n):
        if type(n) == int:
            if n % 3 == 0 and n % 5 == 0 and n % 7 == 0:
                return 'Foo Bar Qix'

            if n % 3 == 0:
                return "Foo"

            elif n % 5 == 0:
                return "Bar"

            elif n % 7 == 0:
                return "Qix"

        else:
            return "Error Type"

