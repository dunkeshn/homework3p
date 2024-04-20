# Напечатать таблицу умножения для числа n, использовать f строки

def multitable(n: int, r: int) -> None:
    print(f'Таблица умножения для числа {n}:')
    for i in range(1, r + 1):
        print(f'{n} * {i} = {n * i}')


if __name__ == '__main__':
    n = int(input('Введите число n: '))
    r = int(input('Введите размерность таблицы: '))
    multitable(n, r)
