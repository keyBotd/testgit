def triangle_type(a: float, b: float, c: float) -> str:
    '''
    Определить тип треугольника (равносторонний, равнобедренный и произвольный)
    :param a: первая сторона
    :param b: вторая сторона
    :param c: третья сторона
    :return: тип треугольника
    '''
    try:
        if type(a) not in [float, int] or type(b) not in [float, int] or type(c) not in [float, int]:
            raise TypeError
        else:
            if a > 0 and b > 0 and c > 0:
                if (a + b) > c and (b + c) > a and (a + c) > b:
                    if a == b and b == c:
                        return 'равносторонний'
                    elif a == b or b == c or a == c:
                        return 'равнобедренный'
                    elif a ** 2 == (b ** 2 + c ** 2) or b ** 2 == (a ** 2 + c ** 2) or c ** 2 == (a ** 2 + b ** 2):
                        return 'прямоугольный'
                    return 'произвольный'
                return 'это не треугольник'
            return 'стороны должны быть больше нуля'

    except TypeError:
        return 'Неверный тип данных'


def delete_space(text: str) -> str:
    '''

    :param s: строка
    :return: строка
    '''
    text = text.strip()
    if text != '':
        text = text.split()
        return ' '.join(text)
    return 'пустая строка'


if __name__ == '__main__':
    # print(triangle_type(9, 9, 8))
    print(delete_space('hello world'))
