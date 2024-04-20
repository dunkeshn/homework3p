# Подсчитать количество цифр в числе. Реализовать двумя видами циклов

def digit_num(n: int) -> int:
    return len(str(n))


if __name__ == '__main__':
    n = int(input('Введите число n: '))
    print(f'Количество цифр в числе: {digit_num(n)}')