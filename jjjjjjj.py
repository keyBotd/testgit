import unittest
from parameterized import parameterized


# class TestRomeSimbols(unittest.TestCase):
#     @parameterized.expand([
#         ('MDCCCLVII', 1857),
#         ("Невозможно вывести эти значения", 0),
#         ("Невозможно вывести эти значения", -1),
#         ("Неверный тип данных", 'LLLL')
#     ])
#     def test_int_rome(self, k, a):
#         rome_int = RomeSim()
#         self.assertEqual(k, rome_int.check_int_in_rome(a))
#
#     @parameterized.expand([
#         (1737, 'MDCCXXXVII'),
#         ('Невозможно вывести эти значения', ''),
#         ('Невозможно вывести эти значения', ' '),
#         ("Неверный тип данных", 100)
#     ])
#     def test_rome_int(self, k, a):
#         int_rome = RomeSim()
#         self.assertEqual(k, int_rome.check_rome_in_int(a))
#
#
# class RomeSim:
#     def check_int_in_rome(self, int_in_rome):
#         if int == type(int_in_rome):
#             if int_in_rome > 0:
#                 rome_int_sure = ''
#
#                 M_sim = int_in_rome // 1000
#                 int_in_rome = int_in_rome - M_sim * 1000
#                 rome_int_sure = rome_int_sure + M_sim * "M"
#
#                 D_sim = int_in_rome // 500
#                 int_in_rome = int_in_rome - D_sim * 500
#                 rome_int_sure = rome_int_sure + D_sim * "D"
#
#                 C_sim = int_in_rome // 100
#                 int_in_rome = int_in_rome - C_sim * 100
#                 rome_int_sure = rome_int_sure + C_sim * "C"
#
#                 L_sim = int_in_rome // 50
#                 int_in_rome = int_in_rome - L_sim * 50
#                 rome_int_sure = rome_int_sure + L_sim * "L"
#
#                 X_sim = int_in_rome // 10
#                 int_in_rome = int_in_rome - X_sim * 10
#                 rome_int_sure = rome_int_sure + X_sim * "X"
#
#                 V_sim = int_in_rome // 5
#                 int_in_rome = int_in_rome - V_sim * 5
#                 rome_int_sure = rome_int_sure + V_sim * "V"
#
#                 I_sim = int_in_rome // 1
#                 int_in_rome = int_in_rome - I_sim * 1
#                 rome_int_sure = rome_int_sure + I_sim * "I"
#
#                 return rome_int_sure
#             else:
#                 return "Невозможно вывести эти значения"
#         else:
#             return "Неверный тип данных"
#
#     def check_rome_in_int(self, rome_in_int: str):
#         if str == type(rome_in_int):
#             if rome_in_int.strip() == '':
#                 return "Невозможно вывести эти значения"
#
#             int_rome_sure = 0
#
#             int_rome_sure += rome_in_int.count('M') * 1000
#             int_rome_sure += rome_in_int.count('D') * 500
#             int_rome_sure += rome_in_int.count('C') * 100
#             int_rome_sure += rome_in_int.count('L') * 50
#             int_rome_sure += rome_in_int.count('X') * 10
#             int_rome_sure += rome_in_int.count('V') * 5
#             int_rome_sure += rome_in_int.count('I') * 1
#
#             return int_rome_sure
#         else:
#             return "Неверный тип данных"

class TestPoisk(unittest.TestCase):
    @parameterized.expand([
        (5, [5, 8, 12, 9, 1, 23], 23),
        ("Неверный тип", '', "1"),
        ("Пустой список", [], 1)
    ])
    def test_index(self, k, a, t):
        o = Poisk()
        self.assertEqual(k, o.poisk(a, t))


class Poisk:
    def poisk(self, lst, t):
        if type(lst) == list and type(t) == int:
            if len(lst) != 0:
                lst.sort()
                start = 0
                end = len(lst) - 1
                while start <= end:
                    mid = (start + end) // 2
                    if lst[mid] > t:
                        end = mid - 1
                    elif lst[mid] < t:
                        start = mid + 1
                    else:
                        return mid
            else:
                return "Пустой список"
        else:
            return "Неверный тип"


