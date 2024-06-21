import unittest
from parameterized import parameterized


class Test_check(unittest.TestCase):
    @parameterized.expand([
        (35, [8, 10, 4, 9, 15, 10]),
        (36, [1, 9, 4, 10, 10, 16]),
        (37, [8, 1, 11, 12, 2, 14])
    ])
    def test_sheep_sum(self, k, a):
        self.assertEqual(k, check(a))


def check(sheep):
    sheep_sorted = list(reversed(sorted(sheep)))
    return sheep_sorted[0] + sheep_sorted[1] + sheep_sorted[2]
