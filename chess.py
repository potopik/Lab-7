while True:  # Проверка на ввод данных
    try:
        horizont = int(input('Введите координату клетки фигуры по горизонтали: '))
        if horizont > 8 or horizont < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            continue
        vertical = int(input('Введите координату клетки фигуры по вертикали: '))
        if vertical > 8 or vertical < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            continue
        attackhorizont = int(input('Введите координату атакуемой клетки по горизонтали: '))
        if attackhorizont > 8 or attackhorizont < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            continue
        attackvertical = int(input('Введите координату атакуемой клетки по вертикали: '))
        if attackvertical > 8 or attackvertical < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            continue
        figure = int(input('''Какую фигуру вы хотите использовать?
        1 - Ферзь
        2 - Ладья
        3 - Слон
        4 - Конь
        Ваш выбор: '''))
        if figure > 4 or figure < 0:
            print('Введены некорректные данные. Попробуйте снова.')
            continue
    except ValueError:
        print('Введены некорректные данные. Попробуйте снова.')
        continue

    # Проверка на совпадение цвета полей
    if (horizont + vertical) % 2 == (attackhorizont + attackvertical) % 2:
        print('Они одного цвета -', end=' ')
        if (horizont + vertical) % 2 == 0:
            print('белого')
        else:
            print('черного')
    else:
        print('Поля не одного цвета')

    # Расстояние по горизонтали и вертикали
    dx = abs(horizont - attackhorizont)
    dy = abs(vertical - attackvertical)

    # Проверка угрожает ли фигура полю, а так же второй ход
    if figure == 1:     # Ферзь
        if horizont == attackhorizont or vertical == attackvertical or dx == dy:
            print(f'Ферзь угрожает полю ({attackhorizont}; {attackvertical})')
        else:
            print(f'Ферзь не угрожает полю ({attackhorizont}; {attackvertical})')
            print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({attackhorizont}; {vertical})')
    elif figure == 2:   # Ладья
        if horizont == attackhorizont or vertical == attackvertical:
            print(f'Ладья угрожает полю ({attackhorizont}; {attackvertical})')
        else:
            print(f'Ладья не угрожает полю ({attackhorizont}; {attackvertical})')
            print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({attackhorizont}; {vertical})')
    elif figure == 3:   # Слон
        if dx == dy:
            print(f'Слон угрожает полю ({attackhorizont}; {attackvertical})')
        else:
            print(f'Слон не угрожает полю ({attackhorizont}; {attackvertical})')
            if (horizont + vertical) % 2 != (attackhorizont + attackvertical) % 2:
                print(f'Слон никаким образом не может угрожать полю ({attackhorizont}; {attackvertical})')
            else:
                m0 = attackhorizont
                n0 = attackvertical
                m1 = 0
                n1 = 0
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 += 1
                    n0 += 1
                    if abs(horizont - m0) == abs(vertical - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = attackhorizont
                n0 = attackvertical
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 -= 1
                    n0 += 1
                    if abs(horizont - m0) == abs(vertical - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = attackhorizont
                n0 = attackvertical
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 += 1
                    n0 -= 1
                    if abs(horizont - m0) == abs(vertical - n0):
                        m1 = m0
                        n1 = n0
                        break
                m0 = attackhorizont
                n0 = attackvertical
                while 0 < m0 < 9 and 0 < n0 < 9:
                    m0 -= 1
                    n0 -= 1
                    if abs(horizont - m0) == abs(vertical - n0):
                        m1 = m0
                        n1 = n0
                        break
                print(f'Чтобы за два хода попасть в это поле необходимо встать на поле ({m1}; {n1})')
    else:   # Конь
        if abs(dx - dy) == 1:
            print(f'Конь угрожает полю ({attackhorizont}; {attackvertical})')
        else:
            print(f'Конь не угрожает полю ({attackhorizont}; {attackvertical})')
    break