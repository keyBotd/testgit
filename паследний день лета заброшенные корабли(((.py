import parameterized
import unittest


class NumberTwoLol:
    def kkk(self, number: str, name: str, age: int):
        if type(number) != str and type(name) != str and type(age) != int:
            return False
        elif number[0:2] != '+79' and len(number) != 12:
            return False
        elif name.split()[0].islower() and name.split()[1].islower() and name.split()[2].islower():
            return False
        else:
            return True


class TestNumberTwoLol(unittest.TestCase):
    @parameterized.parameterized.expand([
        (True, '+79393902402', "Купутдинов Фаяз Айратович", 12),
        (True, "+79123123123", "Альбер Ринатович Биберджан", 25)
    ])
    def test_sqrt(self, res, num, name, age):
        c = NumberTwoLol()
        self.assertEqual(res, c.kkk(num, name, age))

    @parameterized.parameterized.expand([
        (False, 000000, 12, ""),
        (False, "+7999999999", 123, 12),
        (False, "+7999999999", "A A A", "aaa")
    ])
    def test_exception_typeError(self, res, value, name, age):
        c = NumberTwoLol()
        self.assertEqual(res, c.kkk(value, name, age))


