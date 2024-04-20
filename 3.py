# Расчет факториала числа с выводом каждого шага.

def factorial(n: int) -> int: # Рекурсивная функция факториала
    if n == 1:
        print(1)
        return 1
    else:
        print(n) # Вывод шагов
        return n * factorial(n-1) # Каждый раз число умножается на число меньшее на 1,
                                  # вызывается новая функция factorial


if __name__ == '__main__':
    a = int(input('Введите число: '))
    print('\nКаждый шаг функции: ')
    print(f'Вычисленный факториал: {factorial(a)}')
