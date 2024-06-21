print('10'.split())


def plus(stroka):
    if str == type(stroka):
        if stroka == '':
            return 0

        stroka = stroka.split(",")
        return sum(list(map(int, stroka)))
    else:
        return 'Не верный тип данных'

print(plus('10'))